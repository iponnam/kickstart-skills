# Stage 1: Specify

Turn the user's words into `specs/NNN-slug/spec.md` using `templates/spec-template.md`.

## Procedure

1. Extract from the request: actors, actions, data, constraints and the outcome the user wants.
2. Write user stories as independent slices, each with a priority (P1 is the minimum valuable product). Each story must be testable on its own and deliver value on its own.
3. For every story, write acceptance scenarios as **Given / When / Then**, numbered `US1/AC1`, `US1/AC2`…
4. List edge cases: empty, invalid, duplicate, concurrent, unauthorised, offline, limits.
5. Write functional requirements `FR-001…`. Each uses MUST and names one testable capability. Include the security and privacy requirements the feature implies (who may do it, what data it stores, how long).
6. List key entities if data is involved: name, what it represents, key attributes and relationships, without storage details.
7. Write success criteria `SC-001…`: measurable, technology-agnostic outcomes. "Users complete checkout in under 3 minutes", not "the API responds in 200 ms".
8. Write assumptions: reasonable defaults you chose instead of asking. State each one.
9. Mark what you genuinely cannot decide as `[NEEDS CLARIFICATION: <question>]`. **At most 3 markers.** Prefer an assumption when a sensible default exists. Reserve markers for decisions that change scope, security, compliance or the user experience significantly.
10. Fill the Compliance section: personal data involved (yes/no and which fields), and the frameworks from `.kickstart/compliance.md` that the feature touches.

## Quality gate (run before showing the spec)

Check each item and fix the spec until it passes, at most three rounds:

- [ ] No languages, frameworks, libraries or API names
- [ ] Every story has at least one acceptance scenario
- [ ] Every requirement is testable and unambiguous
- [ ] Success criteria are measurable and technology-agnostic
- [ ] Edge cases listed
- [ ] Scope is bounded: an Out of scope list exists
- [ ] Assumptions stated
- [ ] No more than 3 `[NEEDS CLARIFICATION]` markers
- [ ] Compliance section filled

Write the gate result to `specs/NNN-slug/checklists/requirements.md`.

## For pet projects

One or two stories, five or fewer requirements, two success criteria. Skip Key Entities if there is no new data. The quality gate still applies.
