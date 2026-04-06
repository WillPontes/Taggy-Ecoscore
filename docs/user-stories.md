## 🔴 Prioridade Alta: Fundação e entregas core

### **ID: US01 – Configuração do repositório**

- **Épico / Sprint:** Épico 1 – Fundação · Sprint 1
- **Descrição:** Criar boilerplate de front-end e back-end: estrutura, qualidade de código e documentação mínima para onboarding.
- **Card:** Como time de desenvolvimento, queremos um repositório padronizado com front-end e back-end, ferramentas de qualidade e documentação clara para que qualquer pessoa consiga clonar, configurar e rodar o projeto localmente com previsibilidade.
- **Conversation:** A base técnica deve incluir convenções de Git, lint/formatador, variáveis de ambiente documentadas sem segredos e, opcionalmente, templates que facilitem issues e pull requests.
- **Confirmation:** README com visão do projeto e instruções para rodar localmente; estrutura de pastas acordada e `.gitignore` adequado; convenção de branches e fluxo de PR documentados; ESLint e Prettier (ou equivalente) configurados; `.env.example` com variáveis explicadas (sem segredos); templates de issue/PR opcionais criados.

### **ID: US02 – Tradução Lúdica de Impacto**

- **Épico / Sprint:** Épico 2 – Sustentabilidade · Sprint 3
- **Descrição:** Transforma dados técnicos de sustentabilidade em metáforas visuais compreensíveis para o dia a dia.
- **Card:** Como usuário, quero ver meu impacto ambiental traduzido em exemplos cotidianos (ex: árvores, campos de futebol) para que minha contribuição seja tangível e fácil de compartilhar.
- **Conversation:** A interface deve converter kg de $CO_2$ em unidades como "filtros de café evitados" ou "km rodados de graça".
- **Confirmation:** Oferecer ao menos 3 variações de metáforas configuráveis para Carbono; ao menos 3 para Água; ao menos 3 para Papel.

### **ID: US03 – Conversor de Combustível em Carbono**

- **Épico / Sprint:** Épico 2 – Sustentabilidade · Sprint 2
- **Descrição:** O motor de cálculo que sustenta o pilar ESG, garantindo precisão nos dados de emissão.
- **Card:** Como gestora de sustentabilidade (Mariana), quero converter o combustível economizado em emissões de $CO_2$ evitadas para gerar relatórios ESG precisos e auditáveis.
- **Conversation:** Utilizar os fatores de emissão do GHG Protocol, diferenciando o cálculo para veículos leves (flex) e pesados (diesel).
- **Confirmation:** O dashboard exibe o cálculo em kg de $CO_2$; disponibilizar opção de exportar dados brutos (logs) para auditoria externa; validar diferenciação de cálculo entre veículos leves e pesados.

### **ID: US04 – Cálculo de Economia de Papel Térmico**

- **Épico / Sprint:** Épico 2 – Sustentabilidade · Sprint 2
- **Descrição:** Foca na redução de resíduos físicos e na digitalização do processo de pedágio/estacionamento.
- **Card:** Como gestor de operações (Ricardo), quero visualizar o impacto ambiental e operacional de não utilizar recibos físicos para eliminar resíduos e burocracia de conferência manual.
- **Conversation:** Quantificar o papel térmico (BPA) evitado por transação e converter em litros de água poupados na produção desse papel.
- **Confirmation:** Converter papel evitado em litros de água poupados; o dashboard exibe o cálculo em litros de água poupados; exibir o total acumulado de "árvores preservadas".

### **ID: US05 – Dashboard Comparativo "Com vs. Sem Taggy"**

- **Épico / Sprint:** Épico 3 – Operações e Valor · Sprint 4
- **Descrição:** Ferramenta de análise financeira e operacional para provar o valor do produto.
- **Card:** Como gerente de operações, quero comparar meu gasto real contra o prejuízo estimado de um cenário sem tag para validar o retorno sobre o investimento (ROI).
- **Conversation:** O gráfico deve mostrar o "Custo da Ineficiência" (combustível em marcha lenta + desgaste de freios em filas) vs. a fluidez da Taggy.
- **Confirmation:** Apresentar delta de economia em R$; apresentar delta de economia em litros; implementar filtros por veículo, placa ou período.

### **ID: US06 – Gestão de Inventário de Frota**

- **Épico / Sprint:** Épico 3 – Operações e Valor · Sprint 2
- **Descrição:** Centraliza o cadastro de veículos e suas respectivas Tags para viabilizar os cálculos do sistema.
- **Card:** Como gestor de frota, quero cadastrar meus veículos vinculando placa, modelo, tipo de combustível e ID da Tag para que o sistema processe os dados de economia corretamente.
- **Conversation:** O sistema deve permitir a edição e exclusão de veículos. É essencial capturar o tipo de combustível para alimentar o motor de cálculo de $CO_2$.
- **Confirmation:** Campos obrigatórios para placa, modelo, combustível e ID da Tag; validar se uma Tag já está vinculada a outra placa no cadastro; permitir upload de dados em lote via CSV/Excel para frotas grandes; garantir edição e exclusão de veículos cadastrados.

---

## 🟡 Prioridade Média: Rotina e Experiência

### **ID: US07 – Placar de "Tempo de Vida"**

- **Épico / Sprint:** Épico 4 – Jornada do Usuário · Sprint 4
- **Descrição:** Valoriza o ativo mais precioso do motorista: o tempo.
- **Card:** Como motorista (Tiago), quero ver o acumulado de horas economizadas por não parar em filas para valorizar meu tempo produtivo ou de descanso.
- **Conversation:** O cálculo baseia-se na diferença entre o tempo médio de espera em cabines manuais e o tempo de passagem pela Tag.
- **Confirmation:** Atualizar o placar em tempo real após transação confirmada; exibir dados no formato de "Horas/Dias Ganhos".

### **ID: US08 – Roteirizador de Fluxo Sustentável**

- **Épico / Sprint:** Épico 4 – Jornada do Usuário · Sprint 3
- **Descrição:** Inteligência logística para escolher caminhos com menos emissões.
- **Card:** Como usuário, quero que o sistema sugira rotas com maior fluidez de cancelas para reduzir o desgaste do veículo e a pegada de carbono da viagem.
- **Conversation:** O mapa deve sinalizar "Rotas Verdes" onde o histórico de fluxo de tags integradas garante menos paradas.
- **Confirmation:** Exibir estimativa de $CO_2$ evitado antes de iniciar o trajeto; sinalizar visualmente as "Rotas Verdes" no mapa.

### **ID: US09 – Notificações "Passagem Limpa"**

- **Épico / Sprint:** Épico 4 – Jornada do Usuário · Sprint 4
- **Descrição:** Reforço positivo imediato para engajar o motorista após o uso.
- **Card:** Como motorista, quero receber um push logo após passar pelo pedágio informando o impacto positivo imediato daquela ação específica. Exemplo: "Boa! Você economizou 150ml de diesel e evitou Xg de $CO_2$ agora".
- **Conversation:** Mensagens devem refletir a transação processada e reforçar economia e carbono evitado naquele momento.
- **Confirmation:** Disparar notificação em até 3 minutos após o processamento da transação; incluir dados variáveis de economia de combustível e $CO_2$ no texto do push.

---

## 🟢 Prioridade Baixa: Diferenciais e Negócio

### **ID: US10 – Barra de Progresso de Metas Semanais**

- **Épico / Sprint:** Épico 4 – Jornada do Usuário · Sprint 5
- **Descrição:** Elemento de gamificação para manter o uso recorrente do serviço.
- **Card:** Como Product Lead (Jéssica), quero implementar metas de economia semanais para aumentar o engajamento e a retenção do usuário no aplicativo.
- **Conversation:** Interface visual onde o usuário acompanha quanto falta para bater sua meta de eficiência verde (ex: completar 10 passagens sem fila).
- **Confirmation:** Barra de progresso funcional na interface; permitir personalização de metas por frota ou perfil individual.

### **ID: US11 – Calculadora de Payback Operacional**

- **Épico / Sprint:** Épico 3 – Operações e Valor · Sprint 5
- **Descrição:** Demonstra transparência financeira sobre o custo do serviço.
- **Card:** Como proprietário de veículo, quero comparar o custo da mensalidade da tag com a economia gerada para saber quando o serviço se torna "lucro".
- **Conversation:** Relatório simplificado: (Economia de Diesel + Manutenção) - Mensalidade = Saldo Real.
- **Confirmation:** Exibir o cálculo de saldo real de forma clara; destacar o status "Tag Paga" quando a economia superar a mensalidade.
