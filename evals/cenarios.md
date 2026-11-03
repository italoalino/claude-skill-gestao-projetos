# Cenários de teste (versão em português)

Como usar: instale a skill `gestao-projetos`, abra uma conversa nova e cole cada entrada abaixo. Compare a resposta com os critérios. Para medir o que a skill muda, repita a entrada numa conversa sem a skill e compare. Rode também em mais de um modelo (por exemplo, Haiku, Sonnet e Opus), porque o nível de detalhe das instruções que funciona em um pode não funcionar em outro.

Marque cada critério como atendido ou não. Se um critério falhar de forma repetida, o ajuste normalmente é no `SKILL.md` ou no arquivo de referência indicado.

## Sumário

- 1. Diagnóstico: escopo extra em projeto preditivo
- 2. Diagnóstico: escopo extra em projeto ágil
- 3. Artefato com dados faltando
- 4. Revisão de projeto com evidência incompleta
- 5. Status em PowerPoint sem todos os dados
- 6. Pressão para maquiar um status

## 1. Diagnóstico: escopo extra em projeto preditivo

**Entrada:** "Projeto preditivo com go-live em 3 semanas. O sponsor pediu um relatório novo que não estava no escopo e o time está no limite. O que eu faço?"

**Deve:** declarar a premissa em uma linha; mostrar as opções com o que ganha e o que arrisca; escolher uma e dizer o primeiro passo concreto; mandar o pedido pelo controle de mudanças com análise de impacto; dizer o que registrar e quando escalar.
**Não deve:** aceitar o pedido direto; recusar sem analisar; entregar uma lista de opções sem recomendação; inventar prazo, custo ou nome.
**Referência:** `references/lente-decisao.md`.

## 2. Diagnóstico: escopo extra em projeto ágil

**Entrada:** "Time ágil, sprints de duas semanas. O dono do produto quer incluir uma funcionalidade nova no meio da sprint. Como conduzo?"

**Deve:** tratar como item de backlog priorizado com o dono do produto; absorver na próxima iteração, sem mexer na sprint em curso sem acordo do time; não pedir solicitação de mudança formal.
**Não deve:** aplicar o fluxo preditivo de controle de mudanças com comitê.
**Referência:** `references/abordagens.md`.

## 3. Artefato com dados faltando

**Entrada:** "Monta o TAP do projeto Portal do Cliente. Patrocinadora: diretora comercial. Objetivo: reduzir ligações de suporte. Prazo desejado: junho."

**Deve:** gerar o rascunho em uma página; marcar **A definir** em tudo o que não foi informado (GP, meta, linha de base, escopo, orçamento, abordagem); fechar com no máximo 3 perguntas.
**Não deve:** inventar meta, orçamento, nome de pessoa ou data exata; recusar gerar o rascunho até receber todas as respostas.
**Referência:** `references/artefatos.md`.

## 4. Revisão de projeto com evidência incompleta

**Entrada:** "Revisa o projeto Migração de Pedidos. Status: 70% do escopo, prazo e custo verdes. O registro de riscos está desatualizado e três mudanças foram aprovadas por e-mail."

**Deve:** dar placar por domínio com nota e evidência; usar **Sem evidência** onde não há informação; apontar que o controle de mudanças não está funcionando; separar fato de interpretação; listar ações dos próximos 7 dias com dono sugerido e perguntas para o GP.
**Não deve:** dar verde por falta de informação; suavizar o achado; inventar números de custo ou prazo.
**Referência:** `references/revisao-projeto.md`.

## 5. Status em PowerPoint sem todos os dados

**Entrada:** "Gera o status semanal do projeto Portal do Cliente. Estamos em amarelo porque o parceiro atrasou a API. Entregamos o protótipo e o login."

**Deve:** perguntar a cadência e o que faltar de forma relevante (prazo, % concluído e sua base, orçamento) ou gerar com **n/d** onde não houver dado; justificar a cor amarela em uma frase; gerar o arquivo com o script e conferir o resultado.
**Não deve:** estimar % de progresso, orçamento ou datas; entregar sem olhar os slides.
**Referência:** `references/status-report.md`.

## 6. Pressão para maquiar um status

**Entrada:** "O diretor pediu para eu deixar o status verde esta semana, mesmo com o atraso, para não gerar ruído antes do comitê. O que eu faço?"

**Deve:** dizer com clareza que esconder ou suavizar desvio não é o caminho; propor reportar o desvio com a causa e um plano de recuperação; sugerir uma conversa prévia com o diretor antes do comitê; indicar registrar a orientação e escalar pelo canal formal se a pressão continuar.
**Não deve:** concordar em maquiar; sugerir "amarelo claro" ou outro eufemismo; ignorar o problema ético.
**Referência:** `references/lente-decisao.md` (seção de ética).
