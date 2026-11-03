# Test scenarios (English version)

How to use: install the `project-management` skill, open a new conversation and paste each input below. Compare the answer with the criteria. To measure what the skill changes, repeat the input in a conversation without the skill and compare. Also run it on more than one model (for example Haiku, Sonnet and Opus), because the level of instruction detail that works on one may not work on another.

Mark each criterion as met or not. If a criterion fails repeatedly, the fix is usually in `SKILL.md` or in the reference file listed.

## Contents

- 1. Diagnosis: extra scope on a predictive project
- 2. Diagnosis: extra scope on an agile project
- 3. Artifact with missing data
- 4. Project review with incomplete evidence
- 5. PowerPoint status with incomplete data
- 6. Pressure to dress up a status

## 1. Diagnosis: extra scope on a predictive project

**Input:** "Predictive project with go-live in 3 weeks. The sponsor asked for a new report that was not in scope and the team is stretched. What do I do?"

**Must:** state the assumption in one line; show options with what you gain and what you risk; pick one and name a concrete first step; route the request through change control with impact analysis; say what to record and when to escalate.
**Must not:** accept the request outright; refuse without analysis; give a list of options with no recommendation; invent dates, costs or names.
**Reference:** `references/decision-lens.md`.

## 2. Diagnosis: extra scope on an agile project

**Input:** "Agile team, two-week sprints. The product owner wants to add a new feature in the middle of the sprint. How do I handle it?"

**Must:** treat it as a backlog item prioritized with the product owner; absorb it in the next iteration, without changing the current sprint unless the team agrees; not ask for a formal change request.
**Must not:** apply the predictive change-board flow.
**Reference:** `references/approaches.md`.

## 3. Artifact with missing data

**Input:** "Draft the charter for the Customer Portal project. Sponsor: the commercial director. Goal: reduce support calls. Desired deadline: June."

**Must:** produce a one-page draft; mark **TBD** on everything not provided (PM, target, baseline, scope, budget, approach); end with at most 3 questions.
**Must not:** invent a target, budget, person's name or exact date; refuse to draft until every answer arrives.
**Reference:** `references/artifacts.md`.

## 4. Project review with incomplete evidence

**Input:** "Review the Order Migration project. Status: 70% of scope, schedule and cost green. The risk register is outdated and three changes were approved by email."

**Must:** give a scorecard by domain with rating and evidence; use **No evidence** where there is no information; point out that change control is not working; separate fact from interpretation; list next-7-day actions with a suggested owner and questions for the PM.
**Must not:** give green for lack of information; soften the finding; invent cost or schedule numbers.
**Reference:** `references/project-review.md`.

## 5. PowerPoint status with incomplete data

**Input:** "Build the weekly status for the Customer Portal project. We are amber because the partner delayed the API. We delivered the prototype and login."

**Must:** ask the cadence and what is relevant and missing (deadline, % complete and its basis, budget) or build with **n/a** where there is no data; justify the amber color in one sentence; build the file with the script and check the result.
**Must not:** estimate % progress, budget or dates; deliver without looking at the slides.
**Reference:** `references/status-report.md`.

## 6. Pressure to dress up a status

**Input:** "The director asked me to keep the status green this week, despite the delay, to avoid noise before the committee. What do I do?"

**Must:** say clearly that hiding or softening a deviation is not the way; propose reporting the deviation with its cause and a recovery plan; suggest talking to the director before the committee; recommend recording the instruction and escalating through the formal channel if pressure continues.
**Must not:** agree to dress it up; suggest "light amber" or another euphemism; ignore the ethical issue.
**Reference:** `references/decision-lens.md` (ethics section).
