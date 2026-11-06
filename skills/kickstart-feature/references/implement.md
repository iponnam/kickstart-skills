# Stage 6: Implement

Execute `tasks.md` in order and tick each task as it is done.

## Before starting

1. Stage 5 must have no CRITICAL findings.
2. If `checklists/` has files with unticked items, show the count per file and ask whether to proceed. Do not edit checklist files here.
3. Confirm the ignore files match the stack (`.gitignore`, `.dockerignore`), adding missing ecosystem patterns.

## Execution

- Go phase by phase. Do not start a phase until the previous one passes its checkpoint.
- Within a phase, write the test tasks first and run them to see them fail. Then implement until they pass.
- `[P]` tasks may be done together; sequential tasks in order.
- Follow `.kickstart/project.md` conventions and the existing code around each change: naming, layout, error handling, logging.
- Apply the constitution while coding: server-side authorisation, boundary validation, parameterised queries, no secrets, no PII in logs.
- After each task: run the project's `lint` and `test` commands, then change `- [ ]` to `- [X]` in `tasks.md`.
- If a task cannot be done as written, stop, explain why, and propose a change to the plan or tasks. Do not silently improvise.
- With `enforced` guardrails, make each commit pass the hooks. Never bypass them.
- Update `.env.example`, README and `quickstart.md` when a variable, command or step appears.

## Commits

One commit per phase or per user story, Conventional Commits, referencing the feature: `feat(booking): US1 tutor lists availability (specs/004-booking)`.

## End of stage

When every task is ticked, run the full test suite and the quickstart. Then go to Stage 7. Ticked boxes are not evidence that the spec is met; Stage 7 checks that.
