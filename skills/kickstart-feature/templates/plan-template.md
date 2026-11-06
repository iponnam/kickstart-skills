# Implementation Plan: [FEATURE NAME]

- feature: [NNN-slug]
- spec: [specs/NNN-slug/spec.md]
- date: [YYYY-MM-DD]

## Summary

[Primary requirement and the technical approach in three sentences.]

## Technical Context

- language and version: [from project.md, checked within 24h]
- framework: [...]
- storage: [...]
- testing: [...]
- target platform: [...]
- performance goals: [from SC-###]
- constraints: [...]
- unknowns: [NEEDS RESEARCH: ...]

## Constitution Check

*Gate: must pass before research, and again after design.*

| Principle | Result | Evidence |
|---|---|---|
| I. Security baseline | pass / fail | [...] |
| II. Compliance | pass / fail | [...] |
| III. Tests first | pass / fail | [...] |
| IV. Guardrails | pass / fail | [...] |
| V. Stack and conventions | pass / fail | [...] |
| VI. Simplicity | pass / fail | [...] |
| VII. Official sources | pass / fail | [...] |
| VIII. Operability (scale) | pass / fail / n/a | [...] |

## Compliance Controls

| Control | How this feature meets it | Evidence (file, test, config) |
|---|---|---|
| [A01:2025] | [...] | [...] |

## Design Files

- research.md: [yes / no]
- data-model.md: [yes / no]
- contracts/: [yes / no]
- quickstart.md: yes

## Files to Change

```
[real paths in the existing layout, e.g.]
src/db/schema/booking.ts
src/app/api/bookings/route.ts
tests/integration/bookings.test.ts
```

## Rollout (scale projects)

- feature flag: [...]
- migration: [expand / contract steps]
- monitoring: [...]
- rollback: [...]

## Complexity Tracking

*Only when a constitution check failed and the exception is justified.*

| Exception | Why needed | Simpler alternative rejected because |
|---|---|---|
