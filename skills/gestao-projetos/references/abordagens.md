# Escolha e adaptação da abordagem (preditivo, ágil, híbrido)

Orientação prática para escolher e combinar abordagens, escrita a partir da experiência de gestão de projetos. Para aprofundar em práticas ágeis, consulte o Guia de Prática Ágil (PMI e Agile Alliance) e o Scrum Guide.

## Sumário

- Ideia central
- Ciclos de vida
- Como combinar abordagens
- Perguntas rápidas para definir a abordagem de um projeto novo
- Prática ágil em projeto real
- Sinais de que a abordagem não está funcionando
- Como adaptar a gestão a cada abordagem

## Ideia central

O objetivo é entregar valor de negócio da melhor forma que o contexto permite. Ser ágil não é o objetivo. A pergunta que decide é: "como podemos ter mais sucesso aqui?". Feedback frequente ajuda? Entregas em partes ajudam. Preciso explorar risco enquanto aprendo? Ciclos curtos ajudam. A organização não consegue consumir valor parcial? Ágil pode não ajudar.

## Ciclos de vida

A tabela mistura definição com heurística de prática (as colunas "quando faz sentido" e "sinal de alerta"). Trate como ponto de partida para conversa, não como regra.

| Ciclo | Quando faz sentido | Sinal de alerta |
|---|---|---|
| **Preditivo** | Trabalho definível, escopo estável, regulação ou contrato rígido, entrega única no fim | Requisitos mudando a cada reunião |
| **Iterativo** | Requisitos pouco claros; aprende-se refinando o produto | Ninguém sabe quando parar |
| **Incremental** | Valor pode ser liberado em partes; retorno antecipado ao patrocinador | Entregas parciais sem uso real |
| **Ágil** | Alta incerteza, cliente disponível, equipe com autonomia, entregas frequentes | Sem patrocinador que entenda a abordagem; equipe sem autonomia para decidir |
| **Híbrido** | Partes diferentes do projeto pedem tratamentos diferentes | Virar "o pior dos dois mundos" por falta de intenção |

## Como combinar abordagens

Projetos reais raramente são puros. Três combinações aparecem com frequência:

1. **Por frente de trabalho.** A parte incerta (descoberta, produto novo) roda em ciclos curtos; a parte regulada, contratada ou dependente de terceiros segue um plano com marcos. Defina onde as frentes se encontram (marcos de integração).
2. **Por fase.** Desenvolvimento com incerteza em ciclos curtos, seguido de uma implantação definida e repetível, planejada de forma preditiva (por exemplo, produto novo e depois implantação com treinamento para muitos usuários).
3. **Por transição.** A equipe adota primeiro as práticas que ajudam a aprender e alinhar (ciclos curtos, revisões, retrospectivas) e mantém estimativa e acompanhamento no estilo antigo. Depois evolui para entregas incrementais. Mudança de cultura leva tempo, e quanto maior a organização, mais tempo.

Combine por intenção, a partir dos riscos do projeto. Misturar sem critério produz burocracia dos dois lados.

## Perguntas rápidas para definir a abordagem de um projeto novo

Use no discovery, antes de escrever o plano:

1. Quanto do escopo é conhecido hoje e quanto vai ser descoberto?
2. O cliente ou usuário consegue dar feedback a cada poucas semanas?
3. O valor pode ser entregue em partes, ou só faz sentido completo?
4. Há restrições rígidas (regulação, contrato de preço fixo, integração com parceiro com prazo próprio)?
5. A equipe tem autonomia e experiência para decidir como fazer?
6. Existe patrocinador que apoie a forma de trabalho escolhida?
7. Qual o custo de errar? Produto crítico ou regulado pede mais verificação antes de liberar.

Registre as respostas e a decisão no termo de abertura ou no plano de abordagem. Se as respostas se dividem, a abordagem é híbrida: diga quais frentes seguem qual lógica. As incompatibilidades que aparecerem (por exemplo, equipe sem autonomia num projeto que pede autonomia) entram no registro de riscos e abrem conversa com as partes afetadas.

## Prática ágil em projeto real

- **Papel do GP em ambiente adaptativo:** muda a forma, não a responsabilidade. Serve o time, remove impedimentos, cuida de partes interessadas, risco, comunicação e alinhamento ao valor. Não decide "como" a equipe faz o trabalho.
- **Backlog:** lista ordenada do trabalho. Não precisa estar completo para o projeto inteiro: o suficiente para a primeira entrega em linhas gerais e detalhe para a próxima iteração.
- **Refinamento:** dono do produto e equipe preparam as próximas histórias antes de entrarem no ciclo.
- **Definição de pronto e de preparado:** critérios objetivos para considerar uma história concluída ou pronta para começar. Resolvem boa parte do "o trabalho nunca fica pronto".
- **Retrospectiva:** poucos itens de melhoria por vez, com um jeito de medir o resultado.
- **Demonstração e revisão:** o cliente vê o produto e aceita aos poucos.
- **Medição:** velocidade (de cada equipe, nunca para comparar equipes), burn-down e burn-up, fluxo, tempo de ciclo.

## Sinais de que a abordagem não está funcionando

| Sinal | Possível causa | Resposta típica |
|---|---|---|
| Entregas parciais que ninguém usa | Valor não foi combinado com quem consome | Alinhar com o cliente o que é uma entrega útil antes de planejar o ciclo |
| Retrabalho constante | Trabalho antecipado demais, ou requisito mal entendido | Entregar menos e validar mais cedo; limitar trabalho em andamento |
| Escopo mudando sem registro | Mudança entra por conversa lateral | Canal único de entrada (backlog ou controle de mudanças, conforme a abordagem) |
| Equipe pedindo aprovação para tudo | Autonomia prometida e não dada | Definir o que a equipe decide sozinha e o que escala |
| Reuniões sem decisão | Cerimônia copiada sem propósito | Revisar o objetivo de cada reunião; cortar o que não decide nem alinha |
| Status sempre verde e surpresa no fim | Medição fraca ou transparência com medo | Métrica visível e simples; tratar o mensageiro com respeito |
| Tudo "quase pronto" | Falta critério de pronto | Definir critérios de aceite por entrega |

## Como adaptar a gestão a cada abordagem

| Tema | Preditivo | Ágil | Híbrido |
|---|---|---|---|
| Escopo | Declaração, EAP, linha de base | Visão, backlog priorizado | Linha de base nas frentes fixas, backlog nas incertas |
| Mudança | Controle integrado com comitê e análise de impacto | Esperada; reprioriza o backlog | Dois canais, com regra explícita de qual vale para qual frente |
| Cronograma | Caminho crítico, marcos | Roadmap, release e iteração | Marcos para o que é externo, cadência para o resto |
| Custo | Linha de base e EVM | Financiamento incremental, gasto por iteração | Orçamento por frente |
| Aceite | Formal por fase | A cada revisão, contra a definição de pronto | Aceite formal onde o contrato exige |
| Status | Variação contra linha de base | Velocidade, burn-up, backlog | Um relatório só, com a métrica certa por frente |
| Risco | Registro formal e reservas | Embutido na cadência | Registro único, revisado na cadência da frente |
