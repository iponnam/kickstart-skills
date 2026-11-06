# Stage 5: Consistency check

A read-only check that `spec.md`, `plan.md` and `tasks.md` agree with each other, with the constitution and with the compliance checklist. Runs automatically after Stage 4, and whenever the user asks "check consistency".

**Do not edit any file in this stage.** Produce a report. Offer fixes; apply them only after the user approves.

## Passes

Report at most 50 findings; summarise the rest.

- **A. Duplication:** near-duplicate requirements.
- **B. Ambiguity:** vague adjectives without numbers ("fast", "scalable", "secure", "robust", "intuitive"); leftover placeholders (TODO, ???, `[NEEDS CLARIFICATION]`).
- **C. Underspecification:** requirements missing an object or measurable outcome; stories whose scenarios do not match the requirements; tasks naming files or components the plan never mentions.
- **D. Constitution:** any requirement, plan decision or task that conflicts with a MUST principle; a quality gate the constitution requires that the tasks omit (for example a missing test task, or a missing security control).
- **E. Coverage:** requirements or scenarios with no task; requirements with no test task; tasks that map to no requirement; measurable success criteria with no task measuring them.
- **F. Inconsistency:** the same concept named differently across files; entities in the plan but not the spec or the reverse; tasks ordered before their dependencies; conflicting decisions.
- **G. Compliance:** controls listed in the spec or plan with no task producing evidence; personal data in the data model with no retention or deletion handling; a deadline or obligation cited without a framework record reference.

## Severity

- **CRITICAL:** conflicts with a constitution MUST; a core artifact is missing; a P1 requirement has no task or no test.
- **HIGH:** conflicting or duplicate requirements; an ambiguous security, privacy or performance requirement; an untestable acceptance scenario; a compliance control with no evidence task.
- **MEDIUM:** terminology drift; a missing non-functional task; an underspecified edge case.
- **LOW:** wording and minor redundancy.

## Report

```
Consistency check: specs/NNN-slug
| ID | Pass | Severity | Where | Finding | Suggested fix |
Coverage: <n>/<n> requirements with tasks, <n>/<n> with tests
Constitution: <n> principles checked, <n> conflicts
Findings: <c> critical, <h> high, <m> medium, <l> low
```

Any CRITICAL finding blocks Stage 6. Offer the concrete edits; after approval, apply them to the right file and re-run this stage.
