## 🟢 Prioridade Alta: Inteligência e Impacto

### **ID: US01 – Tradução Lúdica de Impacto**

- **Descrição:** Transforma dados técnicos de sustentabilidade em metáforas visuais compreensíveis para o dia a dia.
- **Card:** Como usuário, quero ver meu impacto ambiental traduzido em exemplos cotidianos (ex: árvores, campos de futebol) para que minha contribuição seja tangível e fácil de compartilhar.
- **Conversation:** A interface deve converter kg de $CO_2$ em unidades como "filtros de café evitados" ou "km rodados de graça". Deve ser um componente visual de destaque na home do app.
- **Confirmation:** O sistema deve oferecer ao menos 3 variações de metáforas configuráveis para Carbono, Água e Papel.

### **ID: US02 – Conversor de Combustível em Carbono**

- **Descrição:** O motor de cálculo que sustenta o pilar ESG, garantindo precisão nos dados de emissão.
- **Card:** Como gestora de sustentabilidade (Mariana), quero converter o combustível economizado em emissões de $CO_2$ evitadas para gerar relatórios ESG precisos e auditáveis.
- **Conversation:** Utilizar os fatores de emissão do GHG Protocol, diferenciando o cálculo para veículos leves (flex) e pesados (diesel).
- **Confirmation:** O dashboard deve exibir o cálculo em kg de $CO_2$ com a opção de exportar os dados brutos (logs) para fins de auditoria externa.

### **ID: US03 – Cálculo de Economia de Papel Térmico**

- **Descrição:** Foca na redução de resíduos físicos e na digitalização do processo de pedágio/estacionamento.
- **Card:** Como gestor de operações (Ricardo), quero visualizar o impacto ambiental e operacional de não utilizar recibos físicos para eliminar resíduos e burocracia de conferência manual.
- **Conversation:** Quantificar o papel térmico (BPA) evitado por transação e converter em litros de água poupados na produção desse papel.
- **Confirmation:** O sistema deve contabilizar cada passagem sem parada como um ticket evitado e exibir o total acumulado de "árvores preservadas".

### **ID: US04 – Dashboard Comparativo "Com vs. Sem Taggy"**

- **Descrição:** Ferramenta de análise financeira e operacional para provar o valor do produto.
- **Card:** Como gerente de operações, quero comparar meu gasto real contra o prejuízo estimado de um cenário sem tag para validar o retorno sobre o investimento (ROI).
- **Conversation:** O gráfico deve mostrar o "Custo da Ineficiência" (combustível em marcha lenta + desgaste de freios em filas) vs. a fluidez da Taggy.
- **Confirmation:** A visualização deve apresentar o delta de economia (em R$ e Litros) com filtros por veículo, placa ou período.

### **ID: US05 – Gestão de Inventário de Frota**

- **Descrição:** Centraliza o cadastro de veículos e suas respectivas Tags para viabilizar os cálculos do sistema.
- **Card:** Como gestor de frota, quero cadastrar meus veículos vinculando placa, modelo, tipo de combustível e ID da Tag para que o sistema processe os dados de economia corretamente.
- **Conversation:** O sistema deve permitir a edição e exclusão de veículos. É essencial capturar o tipo de combustível (Diesel S10, S500, Flex) para alimentar o motor de cálculo de CO2.
- **Confirmation:** O sistema deve validar se uma Tag já está vinculada a outra placa e permitir o upload em lote (CSV/Excel) para frotas grandes.

---

## 🔵 Prioridade Média: Rotina e Experiência

### **ID: US06 – Placar de "Tempo de Vida"**

- **Descrição:** Valoriza o ativo mais precioso do motorista: o tempo.
- **Card:** Como motorista (Tiago), quero ver o acumulado de horas economizadas por não parar em filas para valorizar meu tempo produtivo ou de descanso.
- **Conversation:** O cálculo baseia-se na diferença entre o tempo médio de espera em cabines manuais e o tempo de passagem pela Tag.
- **Confirmation:** O placar deve ser atualizado em tempo real após cada transação confirmada e exibido em formato de "Horas/Dias Ganhos".

### **ID: US07 – Roteirizador de Fluxo Sustentável**

- **Descrição:** Inteligência logística para escolher caminhos com menos emissões.
- **Card:** Como usuário, quero que o sistema sugira rotas com maior fluidez de cancelas para reduzir o desgaste do veículo e a pegada de carbono da viagem.
- **Conversation:** O mapa deve sinalizar "Rotas Verdes" onde o histórico de fluxo de tags integradas garante menos paradas.
- **Confirmation:** O roteirizador deve exibir uma estimativa de $CO_2$ que será evitado antes do usuário iniciar o trajeto sugerido.

### **ID: US08 – Notificações "Passagem Limpa"**

- **Descrição:** Reforço positivo imediato para engajar o motorista após o uso.
- **Card:** Como motorista, quero receber um push logo após passar pelo pedágio informando o impacto positivo imediato daquela ação específica.
- **Conversation:** Enviar alerta dinâmico: "Boa! Você economizou 150ml de diesel e evitou Xg de $CO_2$ agora".
- **Confirmation:** A notificação deve ser disparada em até 3 minutos após o processamento da transação pela concessionária.

---

## 🟡 Prioridade Baixa: Diferenciais e Negócio

### **ID: US09 – Barra de Progresso de Metas Semanais**

- **Descrição:** Elemento de gamificação para manter o uso recorrente do serviço.
- **Card:** Como Product Lead (Jéssica), quero implementar metas de economia semanais para aumentar o engajamento e a retenção do usuário no aplicativo.
- **Conversation:** Interface visual onde o usuário acompanha quanto falta para bater sua meta de eficiência verde (ex: completar 10 passagens sem fila).
- **Confirmation:** A barra deve permitir personalização de metas por frota ou por perfil de usuário individual.

### **ID: US10 – Calculadora de Payback Operacional**

- **Descrição:** Demonstra transparência financeira sobre o custo do serviço.
- **Card:** Como proprietário de veículo, quero comparar o custo da mensalidade da tag com a economia gerada para saber quando o serviço se torna "lucro".
- **Conversation:** Relatório simplificado: (Economia de Diesel + Manutenção) - Mensalidade = Saldo Real.
- **Confirmation:** O sistema deve destacar o status "Tag Paga" assim que o saldo de economia superar o valor da mensalidade do mês vigente.
