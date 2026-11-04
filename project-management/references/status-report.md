# PowerPoint status report

The status uses the neutral template `assets/template.pptx`: a cover, two model content slides (with footer and page number) and a closing slide. You can swap in your organization's template (see "Using your organization's template" at the end of this file). The script `scripts/build_status.py` fills everything and invents nothing: any field without information shows as **n/a**.

## Contents

- Flow
- What the file contains
- JSON format
- Choosing the content (what makes a status useful)
- If the layout does not fit
- Using your organization's template

## Flow

1. Gather the period's data with the user (or read it from the project tool, if there is a connector). **Ask for what is missing; do not estimate progress, budget or dates.**
2. Write the JSON (format below) to a working file.
3. Build the file:
   ```
   python3 scripts/build_status.py --data status.json --out status_<project>_<date>.pptx
   ```
   Dependency: `python-pptx` (`pip install python-pptx` if missing). The script defaults to English labels; `--lang pt` switches them to Portuguese.
4. Read the script's warnings. It trims lists that exceed the limit and says so; prioritize the content rather than blindly accepting the cut. If the sample-text warning appears (organization name, footer or closing contact still from the template), tell the user when delivering and ask for the details to replace them; do not let the status go out with the sample footer and do not invent names.
5. Check the result visually (convert to PDF and look at the slides) before delivering.
6. Deliver the file and say in one sentence what the status highlights (for example, the main point of attention).

## What the file contains

| Slide | Content |
|---|---|
| 1. Cover | Project name |
| 2. Period summary | 4 indicators (overall status, deadline, complete, budget spent), deliverables of the period, next steps |
| 3. Risks, issues and decisions | Table of the top 3 risks, up to 3 open issues, up to 3 decisions needed |
| 4. Milestones and schedule | Only if there are milestones in the JSON (up to 7) |
| Last. Closing | The template's own slide, unchanged |

Content slides copy everything on slide 2 of the template (footer, bars, logo) and number the page. The subtitle shows project, period, PM and approach when provided.

## JSON format

All fields are optional except `project`. See `assets/example_status.json` (fictitious values, just to show the format).

```json
{
  "project": "Project name",
  "period": "Oct 27 to Oct 31, 2026",
  "pm": "PM name",
  "approach": "Predictive | Agile | Hybrid",
  "overall_status": "green | amber | red",
  "status_note": "up to ~40 characters, explains the color",
  "deadline": {"label": "Go-live", "value": "Dec 15, 2026", "status": "on track"},
  "percent_complete": 60,
  "complete_basis": "of planned deliverables",
  "budget_pct": 45,
  "budget_note": "within plan",
  "deliverables": ["up to 5 items, up to ~100 characters each"],
  "next_steps": ["up to 5 items"],
  "risks": [{"description": "...", "pi": "H / M", "response": "...", "owner": "..."}],
  "issues": ["up to 3 items"],
  "decisions": ["up to 3 items: what needs deciding, by whom and by when"],
  "milestones": [{"milestone": "...", "date": "mm/dd", "status": "completed | on_track | at_risk | late | not_started", "notes": "..."}]
}
```

Notes:

- `pi` is probability / impact (H = high, M = medium, L = low), or the project risk plan's scale.
- `percent_complete` needs a clear basis (`complete_basis`): % of deliverables, stories, scope? A number without a basis misleads. On agile projects, reflect what the team actually measures (for example, backlog delivered).
- `budget_pct` is what has been spent, not the balance.
- `overall_status` is the PM's assessment. Justify the color in `status_note`. A color without justification breeds distrust; amber and red without an action plan do too.
- The script also accepts the Portuguese keys used by the Portuguese version of this skill.

## Choosing the content (what makes a status useful)

- **Start with what requires action from the reader.** Decisions needed and the highest risks weigh more than a list of everything that was done.
- **Deliverables of the period** are results, not activities ("workstream A testing signed off", not "testing meetings").
- **Risks**: only the 3 that would change a reader's decision. The full list stays in the risk register.
- **Issues** are problems that already happened; a risk that materialized goes here, not in the risk table.
- **Decisions** with owner and deadline. If nothing needs deciding, leave it empty; do not pad.
- **Transparency:** a significant deviation appears with its cause and recovery plan. Do not soften the color to avoid a hard conversation.
- On adaptive or hybrid projects, replace "% complete against schedule" with a metric the team really uses (burn-up, velocity, backlog delivered) and state it in `complete_basis`.

## If the layout does not fit

The script covers the common case. For a different slide (burn-up chart, roadmap), build the status and then adjust or add the slide with the available PowerPoint skill, starting from the generated file.

## Using your organization's template

In the neutral template, the organization name on the cover, the footer ("Organization name | Program or area") and the closing contact line are sample text: replace them in PowerPoint before first use. To use a different template, it must follow this structure:

1. Exactly 4 slides: cover, model content slide, second model content slide, closing.
2. On the cover, the title box with the shape name **Cover title**.
3. On slide 2, the page number box with the shape name **Slide number**. Everything on that slide (footer, logo, bars) is copied to every generated content slide.
4. The working area of content slides runs from 0.5 to 9.5 inches horizontally and 0.3 to 5.2 inches vertically (16:9 slide, 10 x 5.625 in). Keep that area clear.

In PowerPoint, rename a shape in Home > Arrange > Selection Pane. Then run the script with `--template path/to/template.pptx` or replace `assets/template.pptx`.
