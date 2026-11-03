# Status report em PowerPoint

O status usa o template neutro `assets/template.pptx`: capa, dois slides de conteúdo modelo (com rodapé e numeração) e slide de encerramento. Dá para trocar pelo template da organização (ver "Usar o template da sua organização" no fim deste arquivo). O script `scripts/build_status.py` preenche tudo e não inventa nada: campo sem informação aparece como **n/d**.

## Sumário

- Fluxo
- O que o arquivo gera
- Formato do JSON
- Como escolher o conteúdo (o que torna o status útil)
- Se o layout não servir
- Usar o template da sua organização

## Fluxo

1. Reúna os dados do período com o usuário (ou leia da ferramenta do projeto, se houver conector). **Pergunte o que faltar; não estime número de progresso, orçamento ou datas.**
2. Escreva o JSON (formato abaixo) em um arquivo de trabalho.
3. Gere o arquivo:
   ```
   python3 scripts/build_status.py --data status.json --out status_<projeto>_<data>.pptx
   ```
   Dependência: `python-pptx` (`pip install python-pptx --break-system-packages` se faltar). Os rótulos dos slides saem em português; `--lang en` troca para inglês.
4. Leia os avisos do script. Ele corta listas que passam do limite e avisa; priorize o conteúdo em vez de aceitar o corte às cegas.
5. Confira o resultado visualmente (converta para PDF e olhe os slides) antes de entregar.
6. Entregue o arquivo e diga em uma frase o que o status destaca (por exemplo, o ponto de atenção principal).

## O que o arquivo gera

| Slide | Conteúdo |
|---|---|
| 1. Capa | Nome do projeto |
| 2. Resumo do período | 4 indicadores (status geral, prazo, concluído, orçamento consumido), entregas do período, próximos passos |
| 3. Riscos, questões e decisões | Tabela dos 3 principais riscos, até 3 questões abertas, até 3 decisões necessárias |
| 4. Marcos e cronograma | Só se houver marcos no JSON (até 7) |
| Último. Encerramento | Slide original do template, sem alteração |

Os slides de conteúdo copiam tudo o que está no slide 2 do template (rodapé, barras, logo) e numeram a página. O subtítulo mostra projeto, período, GP e abordagem quando informados.

## Formato do JSON

Todos os campos são opcionais, exceto `projeto`. Veja `assets/exemplo_status.json` (valores fictícios, só para ver o formato).

```json
{
  "projeto": "Nome do projeto",
  "periodo": "27/10 a 31/10/2026",
  "gp": "Nome do GP",
  "abordagem": "Preditivo | Ágil | Híbrido",
  "status_geral": "verde | amarelo | vermelho",
  "status_texto": "até ~40 caracteres, explica a cor",
  "prazo": {"label": "Go-live", "valor": "15/12/2026", "situacao": "no prazo"},
  "concluido_pct": 60,
  "concluido_base": "das entregas planejadas",
  "orcamento_pct": 45,
  "orcamento_texto": "dentro do previsto",
  "entregas": ["até 5 itens, até ~100 caracteres cada"],
  "proximos_passos": ["até 5 itens"],
  "riscos": [{"descricao": "...", "pi": "A / M", "resposta": "...", "dono": "..."}],
  "questoes": ["até 3 itens"],
  "decisoes": ["até 3 itens: o que precisa ser decidido, por quem e até quando"],
  "marcos": [{"marco": "...", "data": "dd/mm", "status": "concluido | no_prazo | em_risco | atrasado | nao_iniciado", "obs": "..."}]
}
```

Notas:

- `pi` é probabilidade / impacto (A = alta, M = média, B = baixa), ou a escala do plano de riscos do projeto.
- `concluido_pct` deve ter base clara (`concluido_base`): % de entregas, de histórias, de escopo? O número sem base engana. Em projeto ágil, prefira refletir o que o time mede (por exemplo, backlog entregue).
- `orcamento_pct` é o consumido, não o saldo.
- `status_geral` é uma avaliação do GP. Justifique a cor em `status_texto`. Cor sem justificativa gera desconfiança; amarelo e vermelho sem plano de ação também.

## Como escolher o conteúdo (o que torna o status útil)

- **Comece pelo que exige ação de quem lê.** Decisões necessárias e riscos mais altos pesam mais do que a lista de tudo o que foi feito.
- **Entregas do período** são resultados, não atividades ("homologação da frente A aprovada", não "reuniões de homologação").
- **Riscos**: só os 3 que mudariam uma decisão de quem lê. O registro completo fica no registro de riscos.
- **Questões** são problemas que já aconteceram; risco que se concretizou entra aqui, não na tabela de riscos.
- **Decisões** com dono e prazo. Se nada precisa ser decidido, deixe vazio, não encha.
- **Transparência:** desvio relevante aparece com a causa e o plano de recuperação. Não suavize a cor para evitar conversa difícil.
- Em projeto adaptativo ou híbrido, troque a leitura de "% concluído contra cronograma" por uma métrica que o time realmente usa (burn-up, velocidade, backlog entregue) e escreva isso em `concluido_base`.

## Se o layout não servir

O script cobre o caso comum. Para um slide diferente (gráfico de burn-up, roadmap), gere o status e depois ajuste ou acrescente o slide com a skill de PowerPoint disponível, partindo do arquivo gerado.

## Usar o template da sua organização

No template neutro, o nome da organização na capa, o rodapé ("Nome da organização | Programa ou área") e o contato do encerramento são textos de exemplo: troque no PowerPoint antes do primeiro uso. Para usar um template diferente, ele precisa seguir esta estrutura:

1. Exatamente 4 slides: capa, slide de conteúdo modelo, segundo slide de conteúdo modelo, encerramento.
2. Na capa, a caixa do título com o nome de forma **Cover title**.
3. No slide 2, a caixa do número da página com o nome de forma **Slide number**. Tudo o que estiver nesse slide (rodapé, logo, barras) vai para todos os slides de conteúdo gerados.
4. A área útil dos slides de conteúdo é de 0,5 a 9,5 polegadas na horizontal e de 0,3 a 5,2 na vertical (slide 16:9 de 10 x 5,625 pol.). Deixe essa área livre.

No PowerPoint, o nome da forma se muda em Página Inicial > Organizar > Painel de Seleção. Depois rode o script com `--template caminho/do/template.pptx` ou substitua `assets/template.pptx`.
