<!--
Sync Impact Report
- Version: none → 1.0.0
- Principles added: I–VIII (seeded by kickstart)
- Principles changed: none
- Artifacts to update: none
- Deferred: none
-->

# [PROJECT_NAME] Constitution

These rules bind every spec, plan, task list and change in this project. `kickstart-feature` checks each plan against them, and any conflict with a MUST is a critical finding.

## Core Principles

### I. Security baseline

- Every change MUST satisfy the OWASP Top 10 controls in `.kickstart/compliance.md`.
- Access control MUST be enforced server-side and deny by default.
- All external input MUST be validated at the boundary with a schema.
- Queries and commands MUST be parameterised; no string-built SQL or shell.
- Secrets MUST NOT appear in code, config files, logs or commits.

Rationale: these are the failures attackers exploit first, and they are cheap to prevent.

### II. Compliance

- This project is in scope for: [FRAMEWORKS_WITH_VERSIONS].
- Any feature touching personal data, auth, payments, logging, file upload, third-party sharing or AI MUST list the affected controls in its plan and update their status in `.kickstart/compliance.md`.
- Deadlines and obligations MUST come from the framework records, re-verified when older than 60 days.

Rationale: compliance is built in, not retrofitted before an audit.

### III. Tests first and always

- Every functional requirement and acceptance scenario MUST have an automated test.
- Tests MUST be written before the implementation they cover, and seen to fail first.
- The six baseline security tests MUST stay green.
- A failing test MUST NOT be weakened or skipped to make a build pass.

Rationale: tests are the only evidence a requirement is met.

### IV. Guardrails are never bypassed

- Enforcement mode: [ENFORCEMENT].
- Hooks and CI gates MUST NOT be disabled or skipped to land a change. Fix the cause.
- Secret scanning MUST run on every commit and in CI regardless of mode.

Rationale: a gate that can be skipped under pressure is not a gate.

### V. Stack and conventions

- Stack: [STACK_SUMMARY]. Changing a stack component MUST be recorded as a decision in `.kickstart/decisions/`.
- Code MUST follow the project's formatter and linter: [LINT_COMMAND].
- [PROJECT_CONVENTIONS]

Rationale: consistency makes the codebase readable to people and agents.

### VI. Simplicity

- Build only what the spec asks for. Speculative abstractions and unused code SHOULD NOT be added.
- A new dependency SHOULD be justified in the plan; prefer the platform or an existing dependency.

Rationale: every line is a liability to maintain and secure.

### VII. Facts from official sources, never memory

- Prices, free tiers, framework and library versions MUST be checked on the official source within the last 24 hours before they are relied on.
- Compliance facts MUST come from framework records checked within the last 60 days.
- A fact that could not be checked MUST be labelled `unverified since <date>`.

Rationale: models and documents go stale; official sources are the ground truth.

### VIII. Operability (scale projects)

- Services MUST expose a health endpoint and emit structured logs with a request ID.
- Errors MUST be reported to the error tracker.
- Every release MUST have a tested rollback path.
- Database migrations MUST be backward compatible (expand, then contract).

Rationale: production problems are found and fixed by what the system tells you.

## Governance

- This constitution supersedes other project conventions where they conflict.
- Amendments go through `kickstart-constitution`: proposed text, version bump, updated Sync Impact Report.
- Versioning: MAJOR for removed or redefined principles, MINOR for new principles or expanded guidance, PATCH for wording.
- A justified one-off exception is recorded in the feature's `plan.md` Complexity Tracking table, never silently.
- Compliance with this constitution is reviewed in every release checklist.

**Version**: 1.0.0 | **Ratified**: [DATE] | **Last Amended**: [DATE]
