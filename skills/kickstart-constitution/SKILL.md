---
name: kickstart-constitution
description: "Creates and amends the project constitution, .kickstart/constitution.md, a short versioned set of MUST/SHOULD principles that every spec, plan, task list and change in the project is checked against. Seeds it from the kickstart decisions (stack, scale, enforcement, compliance frameworks) so security, testing and compliance rules are binding, not advisory. Use during kickstart setup, or when the user says \"add a principle\", \"change our rules\", \"update the constitution\", \"we decided to always/never…\", or when a plan needs a rule changed instead of an exception."
---

# kickstart-constitution

The constitution is the project's non-negotiable rules. Every other skill reads it. `kickstart-feature` gates each plan against it, and its consistency check treats any conflict with a MUST principle as critical. Keep it short. A principle nobody can check is not a principle.

Adapted from the constitution step of GitHub Spec Kit (MIT). See `docs/ATTRIBUTION.md` in the kickstart repository.

## Create (during kickstart setup)

1. Read `.kickstart/project.md` and `.kickstart/compliance.md`.
2. Copy `templates/constitution-template.md` to `.kickstart/constitution.md`.
3. Fill every placeholder from those files: project name, stack, scale, enforcement mode, the selected compliance frameworks with versions, the test and lint commands.
4. Keep the seeded principles. They are what makes kickstart's guarantees binding:
   - I. Security baseline (OWASP Top 10, secrets, input validation, access control)
   - II. Compliance (the selected frameworks, the checklist, the freshness rule)
   - III. Tests first and always
   - IV. Guardrails are never bypassed
   - V. Stack and conventions
   - VI. Simplicity
   - VII. Facts from official sources, never memory
   - VIII. Operability (scale projects only; delete for pet projects)
5. Ask the user one question: "Anything else you always or never want in this project?" Add each answer as a principle with MUST or SHOULD wording and a one-line rationale. Accept "no".
6. Set version `1.0.0`, ratified and last-amended dates to today. Write the Sync Impact Report comment at the top (template shows the shape).

For an existing project, also read the codebase conventions the audit found (formatter, folder layout, test style) and record the real ones under Principle V. Do not invent conventions the code does not follow.

## Amend

When the user asks to change a rule, or a plan needs an exception that keeps recurring:

1. Show the current principle and the proposed text.
2. Choose the version bump:
   - **MAJOR**: a principle removed or redefined in a backward-incompatible way.
   - **MINOR**: a new principle or section, or materially expanded guidance.
   - **PATCH**: wording or clarification with no change in meaning.
3. Update the text, version and `Last Amended` date.
4. Rewrite the Sync Impact Report: old → new version, principles changed, and which artifacts must follow. Search `specs/*/plan.md`, `specs/*/tasks.md` and `.kickstart/compliance.md` for anything the change affects and list them.
5. Tell the user which open features need re-checking. `kickstart-feature` re-runs its consistency check on them the next time they are touched.

Never weaken Principle I, II or VII to make a single feature pass. Record a justified exception in that feature's `plan.md` Complexity Tracking table instead. If the same exception appears in three features, propose an amendment.

## Rules

- Each principle uses MUST or SHOULD and can be checked by reading code, config or CI.
- Remove vague words such as "robust", "secure" or "fast" unless quantified.
- No compliance deadlines or framework versions are copied in beyond the list of selected frameworks. Those live in the framework records and are re-verified under the freshness rule.
- The constitution supersedes conventions in `project.md` where they conflict. Fix `project.md` to match.
