# Stage 4: Tasks

Turn the plan into `tasks.md` using `templates/tasks-template.md`: an ordered list someone could execute without asking questions.

## Format

Every task is one line:

```
- [ ] T012 [P] [US1] Add booking model with start/end validation in src/db/schema/booking.ts
```

- `T012`: sequential ID in execution order, never reused.
- `[P]`: optional. Only when the task touches different files from other open tasks and has no unfinished dependency.
- `[US1]`: the user story it serves. Required in story phases; omitted in Setup, Foundational and Polish.
- Description with an exact file path.

## Phases

1. **Setup:** dependencies, configuration, migrations scaffolding.
2. **Foundational:** what every story needs and blocks them all (models shared across stories, auth wiring, routing). Nothing story-specific.
3. **One phase per user story, in priority order.** Inside each:
   - Tests first: one test per acceptance scenario and per requirement the story covers, including the negative cases (unauthorised, invalid input). These must fail before implementation.
   - Then models, then services, then endpoints or UI, then integration.
   - End with a checkpoint line: what can be demonstrated now.
4. **Polish and cross-cutting:** docs, `.env.example`, README, compliance evidence, performance, the quickstart walkthrough.

Kickstart rule: test tasks are always generated. This differs from Spec Kit, where they are optional.

## Coverage

At the end of `tasks.md`, add a coverage table mapping each `FR-###`, `SC-###` and `US#/AC#` to the task IDs that implement and test it. Every row needs at least one test task. A success criterion that needs measurable work (performance, availability, security) needs a task that measures it.

## Strategy line

State the MVP: usually User Story 1 alone. Say which phases can run in parallel and which stories are independent.
