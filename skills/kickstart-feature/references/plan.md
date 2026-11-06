# Stage 3: Plan

Decide how to build the spec, within the project's stack and constitution. Output `plan.md` from `templates/plan-template.md`, plus design files.

## Before you start

- Refuse to plan if `spec.md` still has `[NEEDS CLARIFICATION]` markers on scope, security or compliance. Run Stage 2 first, or ask the user to accept a stated assumption.
- Read `.kickstart/project.md` (stack, commands, conventions) and `.kickstart/constitution.md`.

## Procedure

1. **Technical context.** Fill language, framework, storage, testing, target platform, performance goals and constraints from `project.md`. Mark anything unknown `NEEDS RESEARCH`.
2. **Constitution check (gate).** For each principle, write pass or fail with one line of evidence. Any fail on a MUST stops planning until the plan changes. A justified exception goes in the Complexity Tracking table with the simpler alternative that was rejected and why.
3. **Compliance controls.** If the spec's Compliance section lists frameworks, call `kickstart-compliance` for the affected controls (it re-verifies records older than 60 days). Add a table: control ID, how this feature meets it, where the evidence will be.
4. **Research** (`research.md`). For each `NEEDS RESEARCH` item and each new dependency or external API: the decision, the rationale, the alternatives considered. Check library and API versions on their official pages under the 24-hour freshness rule. Never pin a version from memory.
5. **Data model** (`data-model.md`), when the feature adds or changes data: entities, fields, types, validation rules, relationships, state transitions, indexes, and the migration approach (expand, then contract).
6. **Contracts** (`contracts/`), when the feature exposes an interface: one file per endpoint, event or command, in the project's format (OpenAPI, GraphQL schema, JSON schema, CLI usage). Include auth requirements and error responses.
7. **Quickstart** (`quickstart.md`): how to run and try the feature end to end, which later becomes the manual verification script.
8. **Project structure.** List the real directories and files that will change, using the existing layout. No placeholder trees.
9. **Re-run the constitution check** after the design. Update the plan if anything now fails.

## For pet projects

Write `plan.md` only: technical context, constitution check, files to change, data changes inline. Add `data-model.md` or `contracts/` only if the feature has new tables or a public API.

## For scale projects

Add rollout notes: feature flag, backward-compatible migration, monitoring to add, and the rollback path.
