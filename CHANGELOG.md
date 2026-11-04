# Changelog

## 1.0.1

- O script `build_status.py` agora avisa quando a capa, o rodapé ou o encerramento ainda têm o texto de exemplo do template neutro / `build_status.py` now warns when the cover, footer or closing still have the neutral template's sample text.
- Novo exemplo no `SKILL.md` para o pedido misto "revise e monte o status" / New `SKILL.md` example for the mixed request "review and build the status".
- `references/status-report.md` orienta a avisar o usuário quando o rodapé de exemplo for detectado / `status-report.md` tells the skill to flag the sample footer to the user.

## 1.0.0

Primeira versão pública / First public release.

- Skill `gestao-projetos` (português) e `project-management` (inglês), alinhadas ao PMBOK 8 e a práticas ágeis.
- Três modos: diagnóstico de situações, geração de artefatos e revisão de saúde do projeto.
- Status report em PowerPoint com template neutro e script `build_status.py`, com avisos de estouro de texto.
- Fluxo de entrada de projetos genérico, para adaptar à sua organização.
- Seis cenários de teste em `evals/`.
