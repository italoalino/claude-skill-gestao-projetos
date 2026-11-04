# Skill de Gestão de Projetos para o Claude

*[English version below](#project-management-skill-for-claude)*

Uma skill que transforma o Claude num copiloto de gerente de projetos. Ela não ensina o PMBOK: ela se apoia em boas práticas, alinhadas ao PMBOK 8 e a práticas ágeis, para responder a pergunta que interessa no dia a dia, "o que eu faço agora, neste projeto, com estas pessoas e este prazo?".

Escrevi esta skill para o meu próprio trabalho como GP e decidi abrir para quem quiser usar e adaptar.

## O que ela faz

**1. Diagnóstico de situações.** O sponsor pediu escopo extra, o fornecedor atrasou, um stakeholder parou de responder. A skill classifica a situação, considera se o projeto é preditivo, ágil ou híbrido, compara as opções reais e fecha com uma recomendação, o primeiro passo e o que registrar.

**2. Artefatos.** TAP, discovery, registro de riscos, partes interessadas, plano de comunicação, solicitação de mudança, ata, lições aprendidas e termo de encerramento. Tudo enxuto e preenchido só com o que você informou: o que falta aparece como "A definir", nunca como chute.

**3. Status report em PowerPoint.** Gera um status de 4 a 5 slides (resumo com indicadores, riscos, questões, decisões e marcos) num template neutro que você pode trocar pelo da sua empresa.

**4. Revisão de saúde do projeto.** Percorre as áreas do projeto (governança, escopo, cronograma, finanças, partes interessadas, recursos e risco) atrás de evidência, dá nota por área (incluindo "Sem evidência", que também é um achado) e sugere ações para os próximos 7 dias.

## O que tem no repositório

```
gestao-projetos/        versão em português
project-management/     versão em inglês
evals/                  cenários de teste
```

Cada pasta é uma skill completa:

```
SKILL.md                instruções principais
references/             método: lente de decisão, abordagens, artefatos, áreas do projeto,
                        revisão de projeto, status report e fluxo de entrada de projetos
assets/                 template.pptx (neutro) e um JSON de exemplo
scripts/build_status.py gera o status em PowerPoint
```

## Como instalar

**No Claude (app e web):** baixe o .zip pronto na [página de Releases](https://github.com/italoalino/claude-skill-gestao-projetos/releases/latest) (`gestao-projetos.zip` em português ou `project-management.zip` em inglês). Depois, em **Customize > Skills**, clique em "+", escolha "Create skill" e "Upload a skill", e envie o .zip. É preciso ter execução de código habilitada. Detalhes e requisitos de plano no [artigo de ajuda do Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude).

**No Claude Code:** copie a pasta da skill para `~/.claude/skills/` (uso pessoal) ou para `.claude/skills/` dentro do projeto. Mais em [Agent Skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview).

O status em PowerPoint usa a biblioteca `python-pptx`. No Claude ela normalmente já está disponível; se não estiver, `pip install python-pptx`.

## Como adaptar à sua empresa

A skill funciona sem ajuste, mas fica bem melhor com o contexto da sua organização:

- **Fluxo de entrada:** edite `references/fluxo-entrada.md` com o fluxo real (quem aprova, como o GP é designado, cadência de status, alçadas). Hoje ele traz um fluxo típico e a lista do que perguntar quando faltar informação.
- **Template do status:** troque `assets/template.pptx` pelo template da sua empresa. Ele precisa ter 4 slides e duas formas com nomes específicos ("Cover title" e "Slide number"). O passo a passo está no fim de `references/status-report.md`.
- **Templates oficiais do PMO:** se a sua organização tiver, a skill pergunta e dá prioridade a eles.

## Exemplos de uso

- "O sponsor quer incluir um relatório novo a duas semanas do go-live. Projeto preditivo. O que eu faço?"
- "Monta o TAP do projeto de migração com o que eu te passei."
- "Revisa a saúde desse projeto. Seguem o último status e o registro de riscos."
- "Gera o status semanal em PowerPoint com estes dados."

## Testes

A pasta `evals/` tem 6 cenários de teste com critérios do que a skill deve e não deve fazer (diagnóstico preditivo e ágil, artefato com dados faltando, revisão, status e pressão para maquiar resultado). Rode em uma conversa nova, de preferência com e sem a skill e em mais de um modelo, e abra uma issue se algum critério falhar. Arquivos: [`cenarios.md`](evals/cenarios.md) e [`scenarios.md`](evals/scenarios.md).

## Sobre o conteúdo

Os arquivos de referência são orientação prática, escrita a partir da experiência de gestão de projetos e alinhada às áreas que o PMBOK® Guide trata. Eles não reproduzem nem substituem o guia: para a descrição oficial de processos, entradas e saídas, consulte o PMBOK® Guide. “PMBOK” é uma marca registrada do Project Management Institute, Inc. Este projeto é independente e não tem vínculo, patrocínio ou aprovação do PMI.

A skill não substitui as políticas, alçadas e a governança da sua organização. Quando houver conflito, vale a regra interna.

## Licença

MIT. Use, adapte e redistribua à vontade, mantendo o aviso de licença. Veja [LICENSE](LICENSE).

## Autor

Italo Alves Lino, gerente de projetos. Sugestões e melhorias são bem-vindas via issues e pull requests.

---

# Project Management Skill for Claude

A skill that turns Claude into a project manager's copilot. It does not teach PMBOK: it relies on good practice, aligned with PMBOK 8 and agile practice, to answer the question that matters day to day, "what do I do now, on this project, with these people and this deadline?".

I wrote it for my own work as a PM and decided to open it up for anyone to use and adapt.

## What it does

**1. Situation diagnosis.** The sponsor wants extra scope, the vendor is late, a stakeholder stopped responding. The skill classifies the situation, considers whether the project is predictive, agile or hybrid, compares the real options and closes with a recommendation, the first step and what to record.

**2. Artifacts.** Charter, discovery, risk register, stakeholder register, communication plan, change request, minutes, lessons learned and closure report. Lean, and filled only with what you provided: anything missing shows as "TBD", never as a guess.

**3. PowerPoint status report.** Builds a 4 to 5 slide status (summary with indicators, risks, issues, decisions and milestones) on a neutral template you can swap for your company's.

**4. Project health review.** Walks through the project areas (governance, scope, schedule, finance, stakeholders, resources and risk) looking for evidence, rates each area (including "No evidence", which is a finding too) and suggests actions for the next 7 days.

## What is in the repository

```
gestao-projetos/        Portuguese version
project-management/     English version
evals/                  test scenarios
```

Each folder is a complete skill:

```
SKILL.md                main instructions
references/             method: decision lens, approaches, artifacts, project areas,
                        project review, status report and project intake flow
assets/                 template.pptx (neutral) and an example JSON
scripts/build_status.py builds the PowerPoint status
```

## Installing

**In Claude (app and web):** download the ready-made .zip from the [Releases page](https://github.com/italoalino/claude-skill-gestao-projetos/releases/latest) (`project-management.zip` in English or `gestao-projetos.zip` in Portuguese). Then, in **Customize > Skills**, click "+", choose "Create skill" and "Upload a skill", and upload the .zip. Code execution must be enabled. Details and plan requirements in the [Claude help article](https://support.claude.com/en/articles/12512180-use-skills-in-claude).
**In Claude Code:** copy the skill folder to `~/.claude/skills/` (personal use) or to `.claude/skills/` inside a project. More in [Agent Skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview).

The PowerPoint status uses the `python-pptx` library. It is usually already available in Claude; if not, `pip install python-pptx`.

## Adapting it to your company

The skill works out of the box, but gets much better with your organization's context:

- **Intake flow:** edit `references/intake-flow.md` with your real flow (who approves, how the PM is assigned, status cadence, authority limits). Today it holds a typical flow and a list of what to ask when information is missing.
- **Status template:** replace `assets/template.pptx` with your company's template. It needs 4 slides and two shapes with specific names ("Cover title" and "Slide number"). Step by step at the end of `references/status-report.md`.
- **Official PMO templates:** if your organization has them, the skill asks and gives them priority.

## Usage examples

- "The sponsor wants a new report added two weeks before go-live. Predictive project. What do I do?"
- "Draft the charter for the migration project with what I gave you."
- "Review this project's health. Here are the latest status and the risk register."
- "Build the weekly status in PowerPoint with this data."

## Tests

The `evals/` folder has 6 test scenarios with criteria for what the skill must and must not do (predictive and agile diagnosis, artifact with missing data, review, status and pressure to dress up results). Run them in a fresh conversation, ideally with and without the skill and on more than one model, and open an issue if a criterion fails. Files: [`scenarios.md`](evals/scenarios.md) and [`cenarios.md`](evals/cenarios.md).

## About the content

The reference files are practical guidance, written from project management experience and aligned with the areas the PMBOK® Guide covers. They do not reproduce or replace the guide: for the official description of processes, inputs and outputs, consult the PMBOK® Guide. “PMBOK” is a registered mark of Project Management Institute, Inc. This project is independent and is not affiliated with, sponsored by or endorsed by PMI.

The skill does not replace your organization's policies, authority levels and governance. When they conflict, the internal rule wins.

## License

MIT. Use, adapt and redistribute freely, keeping the license notice. See [LICENSE](LICENSE).

## Author

Italo Alves Lino, project manager. Suggestions and improvements are welcome through issues and pull requests.
