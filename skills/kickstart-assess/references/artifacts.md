# Assessment artifacts

All files live in `.kickstart/assessments/<slug>/`. Dates are ISO 8601. Unknowns are `[NEEDS CLARIFICATION: …]`. Unsourced claims are tagged `ASSUMPTION`.

## intake.md

```markdown
# Idea Intake: <short title>

- slug: <slug>
- created: <YYYY-MM-DD>
- source: <sanitized URL, "pasted text", or repo path>
- type: new-capability | improvement | fix | exploration | cost-saving | compliance | other

## Idea (as captured)
> <original wording, secrets redacted>

## Restated
<one or two neutral sentences>

## Origin and context
- raised by: <who | [NEEDS CLARIFICATION]>
- trigger: <what prompted it | [NEEDS CLARIFICATION]>

## First-glance unknowns
- [NEEDS CLARIFICATION: …]
```

## research.md

```markdown
# Idea Research: <short title>

- slug: <slug>
- researched: <YYYY-MM-DD>
- overall confidence: high | medium | low

## Users and demand
- <finding> (confidence, cited | ASSUMPTION)

## Prior art
- <internal and external attempts, and why they worked or failed>

## Market and context
- <alternatives users use today; cost of doing nothing>

## Data and constraints
- <metrics, volumes, platform limits>

## Compliance exposure
| Regulated aspect | Framework record | Heaviest obligation | Official reference | Record last verified |
|---|---|---|---|---|
| <e.g. children's data> | <coppa> | <verifiable parental consent> | <16 CFR 312.5> | <date> |

## Competitors and prices
| Product | What it offers | Price | Source | Checked |
|---|---|---|---|---|

## Evidence against the idea
- <finding, or "None found after checking: …">

## Gaps and open questions
- [NEEDS CLARIFICATION: …]

## Sources
- <url> (accessed <YYYY-MM-DD>)
```

## problem.md

```markdown
# Problem Definition: <short title>

## Problem statement
<who has what problem, in what situation, with what consequence; no solution>

## Affected users and stakeholders
- <group>: <how they are affected>

## Goals
- <outcome>

## Non-goals
- <explicitly not solving>

## Success metrics
- <measurable: metric, current value if known, target, by when>

## Cost of inaction
<what happens if nothing is built>

## Open questions
- [NEEDS CLARIFICATION: …]
```

## concept.md

```markdown
# Concept: <short title>

## Options

### Option A: <name>
- what: <description>
- appetite: S | M | L
- in scope / out of scope: <…>
- risks: <…>
- compliance effort: <frameworks triggered and rough work>
- running cost: launch ~<$/month>, growth ~<$/month> (<sources, checked date>)

### Option B: <name>
<same fields>

### Option C: <name> (optional)

## Recommendation
<option and why, two sentences>

## Out of scope for the recommended option
- <…>

## Assumptions to validate
- <assumption>: <how to test it cheaply>
```

## decision.md

```markdown
# Decision: <short title>

- slug: <slug>
- decided: <YYYY-MM-DD>
- verdict: go | needs-clarification | kill
- artifacts reviewed: intake.md, research.md, problem.md, concept.md

## Scorecard
| Criterion | Rating | Justification |
|---|---|---|
| Problem validity | strong/adequate/weak/unknown | … |
| Evidence strength | … | … |
| Value vs inaction | … | … |
| Feasibility and appetite | … | … |
| Strategic fit | … | … |
| Risk posture | … | … |
| Compliance exposure | … | … |
| Cost to run | … | … |

## Verdict and rationale
<the call and why, referencing the scorecard; every "unknown" acknowledged>

## If needs-clarification
- blocking questions: [NEEDS CLARIFICATION: …]
- revisit stage: intake | research | define | shape

## If go: handoff
- target: kickstart (new project) | kickstart-feature (existing project)
- problem: <one line>
- chosen approach: <recommended option>
- in scope / out of scope: <summary>
- success metrics: <summary>
- compliance: <frameworks and key obligations, with record ids>
- expected running cost: <launch / growth>
- suggested scale: pet | scale
- open questions carried forward: <list>
```
