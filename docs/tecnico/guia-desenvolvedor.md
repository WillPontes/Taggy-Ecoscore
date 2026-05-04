# Guia do desenvolvedor — motor de cálculo Taggy

Guia prático: **webhook → payload**, exemplo JSON e FAQ. Índice da pasta, ordem de leitura e links para premissas/user stories: **[README.md](README.md)**.

---

## Visão geral do sistema em uma frase

> Dado um evento de passagem no pedágio ou estacionamento (placa, UF, tempo decorrido), o motor calcula quanto CO₂e foi evitado, quanto dinheiro foi economizado, e monta um payload JSON para o dashboard, relatórios ESG e notificações.

---

## Passo a passo: do webhook ao payload

### Etapa 1 — Recepção do evento (`TransactionOrchestrator.handle_tag_event`)

**O que acontece:** o hardware envia um webhook com os dados da passagem. O orquestrador recebe e coordena tudo.

**Campos do webhook:**

| Campo | Tipo | Exemplo | Obrigatório |
|-------|------|---------|-------------|
| `plate` | string | `"ABC1D23"` | Sim |
| `elapsed_time` | int (segundos) | `5` | Sim |
| `context` | string | `"pedagio"` ou `"estacionamento"` | Sim |
| `uf_passagem` | string | `"SP"` | Sim |
| `is_digital` | bool | `true` | Não (default `true`) |
| `payback` | dict | `{"monthly_tag_fee_brl": 19.90, "accumulated_savings_brl": 45.00}` | Não |

**Código:** [engine-calculo.md §6 Bloco 4](engine-calculo.md#bloco-4--transactionorchestrator) — `TransactionOrchestrator.handle_tag_event`.

**O que verificar:** todos os campos obrigatórios presentes? `uf_passagem` é sigla de 2 letras? `elapsed_time` é razoável (não negativo, não centenas de horas)?

---

### Etapa 2 — Resolução dos dados do veículo (`VehicleDatabase.get_complete_vehicle_data`)

**O que acontece:** o sistema precisa do tipo de veículo (leve ou pesado) e do combustível para os cálculos. Ordem: **BD interna (cache) → API Senatran/Serpro → perfil genérico de fallback**.

**Resultado esperado:** dict com pelo menos `plate`, `category`, `fuel_type`, `model`.

**Código:** [engine-calculo.md §6 Bloco 2](engine-calculo.md#bloco-2--vehicledatabase) — `get_complete_vehicle_data` e `_map_external_to_internal`.

**O que verificar:** `category` ∈ `leve` \| `pesado`. `fuel_type` no catálogo da engine (`diesel_s10`, `gasolina_c`, `etanol`, …).

**Mapeamento de combustível e APIs:** limitações e casos conservadores → [§7 Limitações](engine-calculo.md#7-limitações).

---

### Etapa 3 — Carregamento dos specs (`OfficialSourceProvider.get_all_specs`)

**O que acontece:** o orquestrador carrega `technical_specs` (BD, sincronizado com ANP/MCTI) e injeta em `self.engine.specs`. Se a BD estiver vazia, usa `_fallback_technical_specs`.

**Código:** [engine-calculo.md §6 Bloco 3](engine-calculo.md#bloco-3--officialsourceprovider-e-_fallback_technical_specs).

**O que verificar:** presença das chaves usadas pelo motor — ver [engine-calculo.md — seção 4 (Dicionário de `technical_specs`)](engine-calculo.md#4-dicionário-de-technical_specs-e-get_all_specs).

---

### Etapas seguintes — `CalcEngine.process_transaction` (§6 Bloco 1)

Tudo após as etapas 1–3 ocorre em **`process_transaction`**: baseline de tempo, litros (marcha lenta + aceleração evitada), papel/água, CO₂e, preço por UF, `pricing_snapshot`, financeiro, `comparison`, metáforas e `payback` opcional. Fórmulas e ordem exata no código de referência.

| Ordem (típica) | Método | Resumo |
|----------------|--------|--------|
| 1 | *(lógica inline em `process_transaction`)* | `time_saved` a partir de `baselines` e tempo real. |
| 2 | `calculate_avoided_idle_fuel` | Litros não queimados em marcha lenta no tempo poupado. |
| 3 | `calculate_avoided_acceleration_fuel` | Volume extra de combustível evitado ao não fazer parada na cabine de pedágio (valor fixo por passagem, por categoria). |
| 4 | `calculate_paper_and_water_savings` | CO₂e, água e tickets de papel se `is_digital`. |
| 5 | `calculate_emissions_from_fuel` | Litros × fator de emissão por `fuel_type`. |
| 6 | `resolve_fuel_price_brl_per_liter` | R$/L por UF com fallbacks; alimenta `metadata.pricing_snapshot`. |
| 7 | `calculate_financial_savings` | Combustível, freio, micro-manutenção em R$. |
| 8 | `build_comparison` | Cenários com vs. sem tag e deltas. |
| 9 | `get_ludic_metrics` / `get_ludic_metrics_by_axis` | Metáforas para UI: versão antiga (`legacy`) e por eixo (`by_axis`). |
| 10 | `calculate_payback_snapshot` | Só se o webhook trouxer o bloco `payback`. |

**Semântica útil:** em `build_comparison`, `calculate_financial_savings` entra nos dois ramos como modelo de custo por cenário; o significado de `delta.estimated_brl` vs. `financial.total_savings_brl` está no [FAQ](#perguntas-frequentes) abaixo.

---

## Como revisar a engine — roteiro para dev iniciante

Este roteiro guia qualquer desenvolvedor do time na revisão do código da engine, mesmo sem ter escrito o código original.

### Passo 1 — Entenda o fluxo geral (`engine-visao-geral.md`)

Abra [engine-visao-geral.md](engine-visao-geral.md) e leia o fluxograma **"Visão geral: webhook até o payload"**. Cada nó do diagrama corresponde a um método — os nomes no diagrama são os mesmos do código. Confirme que a sequência faz sentido: **veículo resolvido → specs carregados → engine calcula → payload montado**.

> **Checkpoint:** o nó de veículo (etapas 2–5) é resolvido _antes_ de chamar `get_all_specs` e `process_transaction`. Se vir alguma implementação que inverta essa ordem, é um bug.

### Passo 2 — Confira as assinaturas dos métodos no mesmo arquivo

As seções `TransactionOrchestrator`, `VehicleDatabase`, `OfficialSourceProvider` e `CalcEngine` no [engine-visao-geral.md](engine-visao-geral.md) mostram os **métodos com corpo `pass`** — ou seja, mostram o que cada método recebe, o que retorna e o que não faz, sem a implementação.

> **Checkpoint:** `handle_tag_event` não calcula nada — só orquestra. Qualquer lógica de cálculo nele é suspeita. `process_transaction` é quem coordena os cálculos internos.

### Passo 3 — Verifique os cálculos em `engine-calculo.md §6 Bloco 1`

Abra [engine-calculo.md §6 Bloco 1](engine-calculo.md#bloco-1--calcengine). Para cada método abaixo, leia a implementação e confirme que ela faz exatamente o descrito:

| Método | O que deve fazer | O que checar no código |
|--------|-----------------|----------------------|
| `calculate_avoided_idle_fuel` | `time_saved_sec × idle_rate[category]` (litros) | usa `specs["idle_rates"][category]` — sem constante numérica hardcoded |
| `calculate_avoided_acceleration_fuel` | retorna `specs["accel_surge"][category]` — valor fixo por passagem | **não** depende de tempo; só da categoria do veículo |
| `calculate_emissions_from_fuel` | `liters × emission_factors[fuel_type]` → kg CO₂e | fator vem de `specs["emission_factors"]`; se o tipo não existe, cai no fallback 2.15 |
| `calculate_paper_and_water_savings` | se `is_digital=False` retorna zeros; se `True` usa `specs["paper_impact"]` | confirmar que `is_digital=False` retorna `{"co2": 0.0, "water": 0.0, "paper_tickets": 0.0}` |
| `resolve_fuel_price_brl_per_liter` | UF pedida → `fuel_prices_by_uf` → `default_uf` → `fuel_prices` → 5.80 | cadeia de 4 fallbacks; resultado inclui `uf_applied` (pode diferir da UF pedida) |
| `calculate_financial_savings` | soma `idle_brl + accel_brl + brake_brl + maint` | `brake_brl = specs["brake_cost_per_stop_brl"][category] × stops_avoided` |
| `build_comparison` | calcula custo dos dois cenários e subtrai para obter o delta | cenário "com tag": `accel_liters=0.0` e `stops_with=0` quando `is_digital=True` |
| `get_ludic_metrics_by_axis` | `value = total ÷ fator_da_unidade` para cada metáfora | cada eixo tem ≥ 3 entradas; se `specs["ludic_metaphors"]` não existir, usa `_default_ludic_metaphors()` |
| `calculate_payback_snapshot` | `net_brl = accumulated - fee × months`; `"tag_paga"` se `net_brl >= 0` | é `@staticmethod` — pode ser chamado sem instanciar `CalcEngine` |
| `process_transaction` | chama todos os métodos acima em ordem e monta o dict final | `payback` só aparece no retorno se o input trouxer o bloco `payback` |

### Passo 4 — Cruzamento com o dicionário de specs (`engine-calculo.md §4`)

Abra [§4 Dicionário de technical_specs](engine-calculo.md#4-dicionário-de-technical_specs-e-get_all_specs). Para cada chave usada nos métodos do Passo 3, confirme que:

- A chave existe na tabela do §4.
- A unidade bate com o uso no código (ex.: `idle_rates` em L/s, `emission_factors` em kg CO₂e/L, `brake_cost_per_stop_brl` em R$/parada).

> **Checkpoint final:** rode o exemplo completo da seção abaixo com os valores de fallback e confira se os números conferem com a tabela de rastreabilidade. Se os valores mudaram, os specs foram atualizados — verifique o `fuel_prices_meta.as_of` no banco.

Para registrar sua revisão de cada método, use a tabela em [engine-revisao-funcoes.md](engine-revisao-funcoes.md).

---

## Exemplo completo trabalhado

**Cenário:** carro leve, gasolina comum, pedágio em SP, passagem em 5 segundos, ticket digital.

**Webhook:**
```json
{
  "plate": "ABC1D23",
  "elapsed_time": 5,
  "context": "pedagio",
  "uf_passagem": "SP",
  "is_digital": true
}
```

**Payload resultante (valores calculados com specs de fallback):**

```json
{
  "environmental": {
    "co2_kg": 0.2155,
    "water_liters": 0.5,
    "fuel_liters": 0.0947,
    "paper_tickets": 1.0
  },
  "financial": {
    "fuel_savings_idle_brl": 0.47,
    "fuel_savings_accel_brl": 0.09,
    "fuel_savings_brl": 0.56,
    "brake_wear_brl": 0.15,
    "maintenance_savings_brl": 0.05,
    "total_savings_brl": 0.76
  },
  "comparison": {
    "without_tag": { "time_sec": 300, "fuel_liters": 0.3305, "co2_kg": 0.7105, "water_liters": 0.0, "estimated_brl": 2.21 },
    "with_tag":    { "time_sec": 5,   "fuel_liters": 0.00135, "co2_kg": 0.0149, "water_liters": 0.5, "estimated_brl": 0.22 },
    "delta":       { "fuel_liters": 0.3292, "co2_kg": 0.6956, "water_liters": 0.5, "estimated_brl": 1.99 }
  },
  "storytelling": {
    "legacy": { "trees_saved": 0.01, "smartphone_charges": 25, "coffee_filters": 2 },
    "by_axis": {
      "carbon": [{ "id": "tree_year", "label": "Árvores (absorção ~1 ano)", "value": 0.0144 }, ...],
      "water":  [{ "id": "shower_8min", "label": "Chuveiros (~8 min)", "value": 0.0083 }, ...],
      "paper":  [{ "id": "ream_a4", "label": "Resmas A4 (~500 folhas)", "value": 0.002 }, ...]
    }
  },
  "metadata": {
    "time_saved_sec": 295,
    "baseline_wait_sec": 300,
    "context": "pedagio",
    "is_digital": true,
    "uf_passagem": "SP",
    "pricing_snapshot": {
      "fuel_price_brl_per_liter": 5.85,
      "fuel_type_applied": "gasolina_c",
      "uf_applied": "SP",
      "currency": "BRL",
      "price_as_of": "2026-04-01",
      "price_source": "basedosdados:br_anp_precos_combustiveis"
    }
  }
}
```

**Rastreabilidade de cada número:**

| Campo | Cálculo | Spec usada |
|-------|---------|-----------|
| `co2_kg` = 0.2155 | `0.09465 L × 2.15 + 0.012` | `emission_factors.gasolina_c = 2.15`, `paper_impact.co2_per_ticket = 0.012` |
| `water_liters` = 0.5 | ticket digital evitado | `paper_impact.water_per_ticket = 0.5` |
| `fuel_liters` = 0.0947 | `295 × 0.00027 + 0.015` | `idle_rates.leve = 0.00027`, `accel_surge.leve = 0.015` |
| `total_savings_brl` = 0.76 | `(0.07965+0.015)×5.85 + 0.15 + 0.05` | `fuel_prices_by_uf.SP.gasolina_c = 5.85`, `brake_cost_per_stop_brl.leve = 0.15`, `maint_costs.leve = 0.05` |
| `time_saved_sec` = 295 | `300 - 5` | `baselines.pedagio.avg_wait_sec = 300` |

---

## Perguntas frequentes

**Por que o motor recebe um baseline e não mede o tempo diretamente?**
O hardware mede apenas o tempo real de passagem com a tag. O tempo que o motorista teria esperado sem a tag (baseline) é uma estimativa estatística configurada nos specs por contexto (pedágio ou estacionamento). É transparente e auditável — qualquer um pode replicar o cálculo com a planilha + specs versionados.

**O que é `accel_surge` e por que é fixo?**
É o volume extra de combustível consumido ao acelerar após uma parada completa na cabine de pedágio. É fixo porque o modelo assume exatamente uma parada evitada por passagem — independente do tempo de espera. Se a passagem for anômala (múltiplas paradas), o motor pode subestimar o consumo real.

**Qual a diferença entre `financial.total_savings_brl` e `comparison.delta.estimated_brl`?**
- `financial.total_savings_brl`: economia real calculada com os litros e a parada evitados nesta passagem (perspectiva: o que esta passagem economizou).
- `comparison.delta.estimated_brl`: diferença entre o custo total estimado dos dois cenários (sem tag vs. com tag), incluindo litros do baseline completo. Reflete o que teria custado sem a tag.
Em uma passagem típica `delta.estimated_brl > total_savings_brl` porque o cenário sem tag inclui o baseline completo de 300s, enquanto `total_savings_brl` usa o `time_saved` (baseline − tempo real).

**Por que `pricing_snapshot` precisa ser gravado junto com a passagem?**
Os preços de combustível mudam semanalmente. Se você gravar só o cálculo final, não consegue auditar ou reproduzir o valor calculado meses depois. Com o snapshot, qualquer auditoria (ESG, fiscal, produto) pode verificar que o preço aplicado era o vigente na semana da passagem.

**Os specs mudam com frequência?**
O dicionário `technical_specs` é sincronizado periodicamente (job agendado) a partir da ANP (preços por UF) e do MCTI (fatores de emissão). Os fatores físicos (`idle_rates`, `accel_surge`, `emission_factors`) são mais estáveis — mudam quando há revisão metodológica. Os preços por UF podem mudar semanalmente. Por isso os specs são versionados no banco e o snapshot de preços é gravado por passagem.

---

## Referências

- [README.md](README.md) — índice e ordem de leitura da pasta `tecnico/`
- [engine-visao-geral.md](engine-visao-geral.md) — fluxo, diagramas, assinaturas dos métodos (sem implementação)
- [engine-calculo.md](engine-calculo.md) — specs, código §6, §7 Limitações
- [engine-debitos-e-backlog.md](engine-debitos-e-backlog.md) — revisão US, TODOs §6, melhorias conhecidas
- [../negocio/premissas-desafio.md](../negocio/premissas-desafio.md) — premissas do desafio ESG
- [../produto/user-stories.md](../produto/user-stories.md) — user stories US02–US11
