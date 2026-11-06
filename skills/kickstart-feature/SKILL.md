---
name: kickstart-feature
description: Spec-driven feature workflow for a kickstarted project. Takes a plain-language request through specify, clarify, plan, tasks, a consistency check, implement and converge, writing spec.md, plan.md, tasks.md and design files under specs/NNN-feature/. Every plan is gated against .kickstart/constitution.md and the compliance checklist; tests come first; the loop ends only when the code is shown to satisfy the spec. Picks up wherever the feature left off. Use when the user says "add a feature", "build X", "implement Y", "I want users to be able to…", "write a spec", "plan this", "break this into tasks", "continue the feature", or any request to change product behaviour.
---

# kickstart-feature

Every feature goes through the same stages, leaving reviewable files behind. The user only has to describe what they want; this skill works out which stage comes next.

Adapted from GitHub Spec Kit's Spec-Driven Development workflow (MIT), with kickstart's additions: mandatory tests, the compliance checklist, and the freshness rule. See `docs/ATTRIBUTION.md` in the kickstart repository.

## Stages

| Stage | Output | Procedure | Pet projects |
|---|---|---|---|
| 1. Specify | `specs/NNN-slug/spec.md` | `references/specify.md` | Yes, shorter |
| 2. Clarify | answers written into `spec.md` | `references/clarify.md` | Up to 3 questions |
| 3. Plan | `plan.md`, plus `research.md`, `data-model.md`, `contracts/`, `quickstart.md` | `references/plan.md` | `plan.md` only, unless the feature has an API or new tables |
| 4. Tasks | `tasks.md` | `references/tasks.md` | Yes |
| 5. Check | consistency report (read-only) | `references/analyze.md` | Yes, quick |
| 6. Implement | code, tests, ticked `tasks.md` | `references/implement.md` | Yes |
| 7. Converge | appended tasks, or "Converged" | `references/converge.md` | Yes |
| Optional: requirements checklist | `checklists/<domain>.md` | `references/checklist.md` | When asked |

Read only the reference file for the stage you are running.

## Step 0: Load context and find the stage

Read silently:

- `.kickstart/project.md` for stack, commands, scale and enforcement.
- `.kickstart/constitution.md` for the rules. If it is missing, run `kickstart-constitution` first; if the user declines, continue and say plans are not gated.
- `.kickstart/compliance.md` for the controls.

Then decide where to start:

- **New request** with no matching folder under `specs/`: create the next number, `specs/NNN-slug/`, three digits, slug from the request in 2–4 words. Start at Stage 1. If the repo uses git, create the branch `NNN-slug` unless the user works on one branch.
- **Existing feature** (the user names it, or the current branch matches `NNN-slug`): pick the first stage whose output is missing or stale:
  - no `spec.md`, start at 1
  - `spec.md` has `[NEEDS CLARIFICATION]` markers, run 2
  - no `plan.md`, or `spec.md` changed after `plan.md`, run 3
  - no `tasks.md`, or `plan.md` changed after `tasks.md`, run 4 then 5
  - unticked tasks in `tasks.md`, run 6
  - all ticked, run 7
- **Explicit request** ("clarify the spec", "just plan it", "check consistency", "converge"): run that stage.

## Review checkpoints

Pause for the user at three points, with a short summary and the file links:

1. After Stages 1–2: "Here is the spec. Approve, or tell me what to change."
2. After Stages 3–5: "Here is the plan and the task list. The check found <n> issues. Approve to start building."
3. After Stage 7: either "Converged" or the list of appended tasks.

If the user says "go all the way" or "don't stop", run straight through, but still stop on any CRITICAL finding from Stage 5 or Stage 7.

## Rules that apply to every stage

- **Constitution first.** A conflict with a MUST principle is CRITICAL. Fix the spec, plan or tasks. Never reinterpret the principle. If the principle itself should change, use `kickstart-constitution`.
- **Tests are mandatory.** Unlike Spec Kit, where tests are optional, every requirement and acceptance scenario gets a test, written before the code.
- **Compliance is part of the plan.** If the feature touches personal data, auth, payments, logging, file upload, third-party sharing or AI calls, `kickstart-compliance` re-verifies the affected framework records when they are more than 60 days old and lists the controls. The plan states how each is met. Never cite a deadline or obligation from memory.
- **Stack facts are fresh.** Any library or API version in the plan is checked on its official page within 24 hours, under the freshness rule in `kickstart-stack-advisor`.
- **Stable IDs.** Requirements are `FR-001…`, success criteria `SC-001…`, acceptance scenarios `US1/AC1…`, tasks `T001…`, checklist items `CHK001…`. Never renumber. Append.
- **What, then how.** `spec.md` says what and why, with no languages, frameworks or APIs. `plan.md` says how.
- **Small slices.** If the spec has more than about five user stories or the plan exceeds roughly two days, split into several features and deliver P1 first.

## Finish

When converged:

- Set `status: done` in `spec.md`.
- Add a line under `Unreleased` in `CHANGELOG.md`.
- Update `.kickstart/compliance.md` rows the feature touched, with evidence.
- Commit with Conventional Commits. For `scale`, offer to open a pull request whose body links the spec, lists the tests, and names the compliance rows changed.

Tell the user in under ten lines: what was built, how to try it (from `quickstart.md` when it exists), what the tests cover, compliance rows changed, and anything deferred.
