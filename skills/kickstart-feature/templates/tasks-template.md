# Tasks: [FEATURE NAME]

- feature: [NNN-slug]
- inputs: spec.md, plan.md[, research.md, data-model.md, contracts/]

Format: `- [ ] T### [P] [US#] Description with exact file path`. `[P]` means it can run in parallel. Tests come first in every story and must fail before the code is written.

## Phase 1: Setup

- [ ] T001 [...]

## Phase 2: Foundational

Blocks every story. Nothing story-specific here.

- [ ] T002 [...]

## Phase 3: User Story 1 - [Title] (P1) MVP

### Tests (write first, see them fail)

- [ ] T003 [P] [US1] Test US1/AC1 in [tests/...]
- [ ] T004 [P] [US1] Test FR-003 unauthorised access is rejected in [tests/...]

### Implementation

- [ ] T005 [US1] [...] in [src/...]

**Checkpoint**: [what can be demonstrated now]

## Phase 4: User Story 2 - [Title] (P2)

[...]

## Phase N: Polish and cross-cutting

- [ ] T0xx Update .env.example, README and quickstart.md
- [ ] T0xx Record compliance evidence in .kickstart/compliance.md for [controls]

## Coverage

| Requirement | Implemented by | Tested by |
|---|---|---|
| FR-001 | T005 | T003 |
| US1/AC1 | T005 | T003 |
| SC-001 | T0xx | T0xx |

## Strategy

- MVP: User Story 1.
- Parallel: [phases or stories that are independent].

<!-- Stage 7 appends "## Phase N: Convergence" below. Never edit or renumber the tasks above. -->
