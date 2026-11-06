# Stage 2: Clarify

Find what is still ambiguous in `spec.md`, ask the few questions that matter most, and write the answers into the spec.

## Coverage scan

Rate each category Clear, Partial or Missing (keep the map internal):

- **Scope and behaviour:** user goals, success criteria, out of scope, roles
- **Data:** entities, identity and uniqueness, lifecycle and states, volume
- **User flow:** critical journeys, error, empty and loading states, accessibility, localisation
- **Quality attributes:** performance targets, scale limits, availability and recovery, observability
- **Security and privacy:** who may do what, data protection, threats
- **Compliance:** the controls from `.kickstart/compliance.md` the feature touches, retention, consent, children's data
- **Integrations:** external services and their failure modes, formats, versions
- **Edge cases:** negative scenarios, rate limits, conflicts and concurrent edits
- **Constraints and trade-offs:** fixed choices, rejected alternatives
- **Terminology:** one name per concept
- **Completion signals:** testable acceptance criteria, measurable done
- **Placeholders:** TODOs, `[NEEDS CLARIFICATION]`, vague adjectives such as "fast", "secure", "intuitive"

Skip a gap if answering it would not change what gets built or how it is tested, or if it is really a technology choice (that belongs in the plan).

## Questions

- **At most 5 per session** (3 for pet projects). Ask one at a time.
- Prioritise by impact on scope, security, compliance and data model, then UX, then everything else.
- Each question is either multiple choice (2–5 options, with your recommended option first and a one-line reason) or a short answer of five words or fewer.
- Accept "you decide": use the recommended option and record it as an assumption.
- Stop early when the remaining gaps are low impact or the user says "done".

## Write back

After each answer, immediately:

1. Add a line under `## Clarifications` → `### Session YYYY-MM-DD`: `- Q: <question> → A: <answer>`.
2. Apply the answer in the right section: a requirement, a scenario, an entity attribute, an edge case or a success criterion. Remove the `[NEEDS CLARIFICATION]` marker it resolves. Replace contradicted text; do not leave both.
3. Save the file.

## Report

Show a short table: category and status (Resolved, Deferred, Clear, Outstanding). Recommend whether to plan now or clarify again after planning.
