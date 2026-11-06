---
name: kickstart-feature
description: Day-to-day feature workflow for a kickstarted project: spec, plan, build, test, review. Reads .kickstart/project.md and .kickstart/compliance.md so every feature respects the chosen stack, scale, enforcement and compliance controls without the user re-explaining anything. Use when the user says "add a feature", "build X", "implement Y", "I want users to be able to…", or any request to change product behaviour in a project that has a .kickstart directory.
---

# kickstart-feature

Make features the same way every time: a short spec, a plan the user can read, code that follows the project's conventions, tests that prove it, and a review against the compliance checklist. Compressed for `pet`, full for `scale`.

## Step 0: Load context (silently)

Read `.kickstart/project.md` (stack, commands, conventions, scale, enforcement) and `.kickstart/compliance.md` (controls). If `.kickstart/` is missing, say so in one line and offer `kickstart` first; if the user declines, continue with sensible defaults.

## Step 1: Spec (5 minutes, not 50)

Write `docs/features/NNNN-<slug>.md`:

```markdown
# NNNN: <feature name>
- status: draft | building | done
- date: YYYY-MM-DD
- owner: <user>

## User story
As a <role>, I want <capability> so that <outcome>.

## Acceptance criteria
- [ ] <observable behaviour 1>
- [ ] <observable behaviour 2>
- [ ] <error or edge case>

## Out of scope
- <what we are not doing now>

## Data
- new or changed tables/fields: <list or "none">
- personal data involved: yes/no (if yes: which fields, retention, deletion path)

## Compliance controls touched
- <IDs from .kickstart/compliance.md, e.g. A01:2025, A05:2025, PRIV-04, PCI-05> or "none"

## Open questions
- <anything that needs the user>
```

Ask the user only the open questions. If there are none, show the acceptance criteria and proceed unless they object. For `pet`, the spec can be the user story and three acceptance criteria.

## Step 2: Plan

List the files to create or change, the migration if any, the tests to write, and the order. Five to fifteen lines. For `scale`, include rollout notes: feature flag, backward-compatible migration (expand then contract), and the rollback path.

If the feature touches auth, personal data, payments, logging, file upload, third-party data sharing or AI model calls, use `kickstart-compliance`: it re-verifies the affected framework records when they are more than 60 days old, then lists the applicable control rows from `.kickstart/compliance.md`. State how each is satisfied in the plan. Do not cite a deadline or obligation from memory. This is where compliance becomes organic: it is one paragraph in the plan, not a separate process.

## Step 3: Build

- Follow the stack conventions in `project.md` and the existing code around the change. Match naming, folder layout, error handling and logging patterns already in use.
- Validate input at the boundary. Authorise on the server. Parameterise queries. Log the event without PII. These are not optional; they map to OWASP A01:2025, A05:2025 and A09:2025.
- Migrations: additive first. Never drop or rename a column in the same release that stops writing to it.
- Keep the diff small and focused. No drive-by refactors; note them for a separate change.
- Update `.env.example` and the README when a new variable or command appears.

## Step 4: Test

- Unit tests for logic, one integration test per new endpoint or server action, and a negative test (unauthorised, invalid input) for every new entry point.
- Run the project's `test` and `lint` commands from `project.md`. Fix failures. Do not weaken a test to make it pass.
- If `enforcement` is `enforced`, the hooks will run on commit and push; make the commit pass the gates rather than bypassing them.

## Step 5: Review

Before saying done, run this self-review and show the result as a short checklist:

- [ ] Every acceptance criterion has a test or a manual verification note
- [ ] No new secret, no PII in logs, no string-built query, no `eval`-class call
- [ ] Authorisation checked for every new route or action
- [ ] Compliance rows touched are updated in `.kickstart/compliance.md` (status and evidence)
- [ ] Migration is backward compatible (scale) or at least reversible (pet)
- [ ] Docs updated: feature spec status `done`, README/env if needed, CHANGELOG line under Unreleased
- [ ] Commits follow Conventional Commits and are grouped sensibly

For `scale`, offer to open a pull request with the spec summary, test evidence and the compliance rows as the PR body.

## Step 6: Report

Tell the user in under ten lines: what was built, how to try it, what tests cover it, any compliance rows changed, and anything left open. Then stop.

## When the feature is big

If the plan exceeds roughly 15 files or two days, split it into milestones in the spec and deliver the first milestone end to end. A vertical slice that works beats a horizontal layer that does not.
