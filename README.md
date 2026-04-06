# Projeto Taggy

O _Taggy_ é uma solução de pagamento automático (Tag) que vai além da conveniência. Nosso objetivo é transformar cada passagem por pedágios e estacionamentos em dados acionáveis de sustentabilidade (ESG), economia de combustível e eficiência operacional.

---

## Visão Geral

O sistema utiliza a inteligência de dados para calcular o impacto ambiental positivo gerado pela fluidez no trânsito. Focamos em três pilares:

1. _Inteligência:_ Cálculos baseados no GHG Protocol para CO₂ e economia de diesel.
2. _Engajamento:_ Linguagem lúdica para aproximar o usuário da causa ambiental.
3. _Gestão:_ Dashboards robustos para frotas que buscam certificados ESG.

## Público-Alvo (Personas)

- _Mariana Costa (Sustentabilidade):_ Precisa de dados auditáveis para relatórios anuais.
- _Ricardo Almeida (Operações):_ Focado em redução de custos de combustível e manutenção.
- _Tiago Mendes (Motorista):_ Valoriza praticidade, status e o "tempo ganho".
- _Jéssica Castro (Product Lead):_ Busca métricas de engajamento e diferenciais competitivos.

## Estrutura do Projeto

O projeto está dividido em 5 pilares estratégicos:

- _Pilar 1:_ O Cálculo (Inteligência de Dados)
- _Pilar 2:_ Os Painéis (Visualização)
- _Pilar 3:_ Incentivos e Avisos (Gamificação)
- _Pilar 4:_ Conexão e Linguagem (UX Writing)
- _Pilar 5:_ Vantagens de Negócio (Certificações)

---

## User Stories

Versão detalhada (Card, Conversation e Confirmation): [docs/user-stories.md](docs/user-stories.md).

### 🔴 Prioridade Alta: Fundação e entregas core

- _[US01] Configuração do repositório:_ Boilerplate front/back, qualidade de código e documentação mínima para onboarding.
- _[US02] Tradução Lúdica de Impacto:_ Metáforas visuais para impacto ambiental (carbono, água, papel).
- _[US03] Conversor de Combustível em Carbono:_ Cálculo ESG com GHG Protocol (leve flex / pesado diesel) e auditoria.
- _[US04] Cálculo de Economia de Papel Térmico:_ Papel (BPA) evitado, água poupada e árvores preservadas no dashboard.
- _[US05] Dashboard Comparativo "Com vs. Sem Taggy":_ ROI com delta em R$ e litros e filtros por veículo, placa ou período.
- _[US06] Gestão de Inventário de Frota:_ Cadastro de veículos e Tags com validações, lote (CSV/Excel) e CRUD.

### 🟡 Prioridade Média: Rotina e Experiência

- _[US07] Placar de "Tempo de Vida":_ Horas/dias ganhos com atualização após cada transação confirmada.
- _[US08] Roteirizador de Fluxo Sustentável:_ Rotas verdes no mapa e estimativa de CO₂ evitado antes do trajeto.
- _[US09] Notificações "Passagem Limpa":_ Push rápido com economia de combustível e CO₂ da passagem.

### 🟢 Prioridade Baixa: Diferenciais e Negócio

- _[US10] Barra de Progresso de Metas Semanais:_ Metas semanais configuráveis por frota ou perfil.
- _[US11] Calculadora de Payback Operacional:_ Saldo real (economia − mensalidade) e status "Tag Paga".

---

## Sketches e storyboards do protótipo

Esta seção documenta os **sketches e storyboards** do produto (requisito da disciplina: histórias com protótipo acessível pelo repositório). Existem **12 telas** em [`docs/images/mockup/`](docs/images/mockup/) (`01.png` … `12.png`). Cada mockup pode ilustrar **várias user stories** ao mesmo tempo: na tabela abaixo indicamos as **US principais** e as **relacionadas**.

**US01 (configuração do repositório)** não corresponde a uma funcionalidade de tela isolada; o storyboard de **fundação** reflete-se na **estrutura recorrente** das vistas web (sidebar, cabeçalho, layout da “Plataforma Operacional”) nas telas **09 a 12**, alinhada ao boilerplate e onboarding.

Em conjunto, as 12 imagens cobrem **as 11 user stories** (acima do mínimo de 10). As telas **01 a 03** são variações do mesmo dashboard (abas Carbono / Água / Papel), o que é habitual num storyboard.

### Mapa telas ↔ user stories

| Tela   | Arquivo    | Descrição breve                                                                 | US principais | US relacionadas                          |
| :----- | :--------- | :------------------------------------------------------------------------------ | :------------ | :--------------------------------------- |
| 01     | `01.png`   | Dashboard mobile — aba Carbono (impacto lúdico + valor técnico em kg CO₂)     | US02, US03    | US04, US07, US10                         |
| 02     | `02.png`   | Mesmo dashboard — aba Água (litros poupados)                                    | US02, US04    | US03, US07, US10                         |
| 03     | `03.png`   | Mesmo dashboard — aba Papel (metragem evitada)                                 | US02, US04    | US03, US07, US10                         |
| 04     | `04.png`   | Resumo e lista das últimas passagens (CO₂, combustível, tempo por passagem)    | US03, US07    | US05, US09                               |
| 05     | `05.png`   | Notificação push no ecrã de bloqueio (praça, g CO₂, ml diesel, min ganhos)      | US09          | US03, US07                               |
| 06     | `06.png`   | Perfil motorista (frota, placa, combustível; atalhos histórico / notificações)  | US06          | US07, US09                               |
| 07     | `07.png`   | Mapa — inserir destino / pesquisar (início da jornada de rota)                  | US08          | —                                        |
| 08     | `08.png`   | Rota Verde no mapa + painel Eco-estimativa (CO₂ evitado, tempo parado)          | US08          | US03, US07                               |
| 09     | `09.png`   | Dashboard web operacional (KPIs, filtros, exportar ESG, heatmap, top 5)         | US05, US03    | US06, US10, US11                         |
| 10     | `10.png`   | Registro de frota (tag, placa, modelo, combustível; CSV; editar / excluir)      | US06          | US03                                     |
| 11     | `11.png`   | Configurações — conta e calibração operacional (parâmetros de ROI)             | US11          | US01                                     |
| 12     | `12.png`   | Gerar relatórios com filtros e área de resultado                              | US03, US04    | US11, US01                               |

### Fluxo resumido (motorista vs. plataforma web)

```mermaid
flowchart LR
  subgraph mobile [App motorista]
    M07[07 Mapa destino]
    M08[08 Rota verde eco]
    M01[01-03 Dashboard impacto]
    M04[04 Historico passagens]
    M05[05 Push]
    M06[06 Perfil]
  end
  subgraph web [Plataforma operacional]
    W09[09 Dashboard KPIs]
    W10[10 Frota]
    W11[11 Config ROI]
    W12[12 Relatorios]
  end
  M07 --> M08
  M05 --> M01
```

### Galeria de mockups

<table>
  <tr>
    <td align="center" valign="top" width="50%">
      <p><strong>Tela 01</strong> — Dashboard, aba Carbono</p>
      <img src="docs/images/mockup/01.png" alt="Mockup: dashboard mobile com placar de tempo, impacto lúdico na aba Carbono e meta semanal" width="340" />
    </td>
    <td align="center" valign="top" width="50%">
      <p><strong>Tela 02</strong> — Dashboard, aba Água</p>
      <img src="docs/images/mockup/02.png" alt="Mockup: mesmo dashboard com impacto lúdico na aba Água e litros de água poupados" width="340" />
    </td>
  </tr>
  <tr>
    <td align="center" valign="top">
      <p><strong>Tela 03</strong> — Dashboard, aba Papel</p>
      <img src="docs/images/mockup/03.png" alt="Mockup: mesmo dashboard com impacto lúdico na aba Papel e papel evitado" width="340" />
    </td>
    <td align="center" valign="top">
      <p><strong>Tela 04</strong> — Resumo e últimas passagens</p>
      <img src="docs/images/mockup/04.png" alt="Mockup: resumo total de passagens CO2 e horas e lista de últimas passagens com métricas por praça" width="340" />
    </td>
  </tr>
  <tr>
    <td align="center" valign="top">
      <p><strong>Tela 05</strong> — Notificação push</p>
      <img src="docs/images/mockup/05.png" alt="Mockup: tela de bloqueio com notificação de passagem limpa CO2 diesel e minutos ganhos" width="340" />
    </td>
    <td align="center" valign="top">
      <p><strong>Tela 06</strong> — Perfil motorista</p>
      <img src="docs/images/mockup/06.png" alt="Mockup: perfil do motorista com frota placa e atalhos para histórico notificações e veículo" width="340" />
    </td>
  </tr>
  <tr>
    <td align="center" valign="top">
      <p><strong>Tela 07</strong> — Mapa, inserir destino</p>
      <img src="docs/images/mockup/07.png" alt="Mockup: mapa com campo para inserir destino e pesquisar" width="340" />
    </td>
    <td align="center" valign="top">
      <p><strong>Tela 08</strong> — Rota Verde e eco-estimativa</p>
      <img src="docs/images/mockup/08.png" alt="Mockup: mapa com rota verde rotulada e painel com CO2 evitado e tempo poupado antes de iniciar rota" width="340" />
    </td>
  </tr>
  <tr>
    <td align="center" valign="top">
      <p><strong>Tela 09</strong> — Dashboard web operacional</p>
      <img src="docs/images/mockup/09.png" alt="Mockup: dashboard web com KPIs CO2 combustível ROI taggys filtros exportar ESG e tabela top 5" width="440" />
    </td>
    <td align="center" valign="top">
      <p><strong>Tela 10</strong> — Registro de frota</p>
      <img src="docs/images/mockup/10.png" alt="Mockup: tabela de registo de frota com tag placa modelo combustível importar CSV e ações editar eliminar" width="440" />
    </td>
  </tr>
  <tr>
    <td align="center" valign="top">
      <p><strong>Tela 11</strong> — Configurações e calibração ROI</p>
      <img src="docs/images/mockup/11.png" alt="Mockup: página de configurações da conta e calibração operacional para ROI" width="440" />
    </td>
    <td align="center" valign="top">
      <p><strong>Tela 12</strong> — Gerar relatórios</p>
      <img src="docs/images/mockup/12.png" alt="Mockup: tela gerar relatórios com filtros e área de resultado" width="440" />
    </td>
  </tr>
</table>

### Anexos no Trello (por cartão)

Para cumprir o requisito de **anexar os storyboards no cartão correspondente**, use os mesmos arquivos em `docs/images/mockup/`:

| Cartão | Arquivos sugeridos para anexar |
| :----- | :------------------------------ |
| US01   | `09.png`, `10.png`, `11.png`, `12.png` (shell da plataforma operacional) |
| US02   | `01.png`, `02.png`, `03.png` |
| US03   | `01.png`, `02.png`, `04.png`, `05.png`, `08.png`, `09.png` |
| US04   | `02.png`, `03.png`, `09.png`, `12.png` |
| US05   | `04.png`, `09.png` |
| US06   | `06.png`, `09.png`, `10.png` |
| US07   | `01.png`, `02.png`, `03.png`, `04.png`, `05.png`, `08.png` |
| US08   | `07.png`, `08.png` |
| US09   | `05.png`, `06.png` |
| US10   | `01.png`, `02.png`, `03.png`, `09.png` |
| US11   | `09.png`, `11.png`, `12.png` |

_Não é necessário duplicar arquivos no repositório: no Trello, faça upload desses PNG a partir da pasta local após clonar o projeto._

---

## Backlog (Trello)

O backlog do projeto está organizado no quadro da equipe na disciplina, com cartões alinhados às user stories e prioridades. Acompanhe o estado das tarefas em: [Trello – cesar-projetos-2](https://trello.com/b/alfFb7dV/cesar-projetos-2).

## Evidências

Capturas de tela solicitadas para comprovar o backlog e a organização do trabalho no Trello. Os arquivos originais ficam em [`docs/images/`](docs/images/). No GitHub (e na maioria dos previews de Markdown), as figuras abaixo aparecem **embutidas** no README — basta que `docs/images/*.png` esteja versionado no repositório.

_Backlog no Trello:_

<table>
  <tr>
    <td align="center" valign="top" width="33%">
      <img src="docs/images/backlog-01.png" alt="Backlog no Trello – visão 1 do quadro" width="440" />
    </td>
    <td align="center" valign="top" width="33%">
      <img src="docs/images/backlog-02.png" alt="Backlog no Trello – visão 2 do quadro" width="440" />
    </td>
    <td align="center" valign="top" width="33%">
      <img src="docs/images/backlog-03.png" alt="Backlog no Trello – visão 3 do quadro" width="440" />
    </td>
  </tr>
</table>

---

## Equipe e Papéis

| Nome              | Papel                   | E-mail             |
| :---------------- | :---------------------- | :----------------- |
| _Afonso Araujo_   | Desenvolvedor Back-End  | ahma@cesar.school  |
| _Igor Phillipe_   | Desenvolvedor FullStack | ipara@cesar.school |
| _Williams Pontes_ | Product Owner           | jwlp@cesar.school  |
| _Jean Augusto_    | Desenvolvedor Back-End  | jasm2@cesar.school |
| _Lucas Gabriel_   | Desenvolvedor FullStack | lgcs2@cesar.school |
| _Kellwen Costa_   | Desenvolvedor Back-End  | kilc@cesar.school  |

---

Este projeto faz parte da disciplina de SI010 - Fundamentos de Desenvolvimento de Software.
