# Optional: requirements checklist

A checklist that tests the **requirements**, not the code. Think of it as unit tests for the spec: is every requirement complete, clear, consistent, measurable and covering its edge cases? Run it when the user asks ("make a security checklist for this feature", "UX checklist", "is the spec ready?"), or offer it before planning a `scale` feature in a sensitive area.

## Write `specs/NNN-slug/checklists/<domain>.md`

Domains: `security`, `privacy`, `ux`, `api`, `performance`, `accessibility`, `data`, or the user's own. If the file exists, append and continue numbering.

Each item is a question about the written requirements, tagged with its quality dimension and the spec reference:

```
- [ ] CHK001 Are authorisation rules specified for every action in US1? [Completeness, Spec §FR-003]
- [ ] CHK002 Is "fast search" quantified with a response-time target? [Clarity, Spec §SC-002]
- [ ] CHK003 Is the behaviour defined when the payment provider times out? [Edge case, Gap]
- [ ] CHK004 Is the retention period for booking records stated and consistent with the compliance checklist? [Consistency, Spec §FR-007]
```

Dimensions: Completeness, Clarity, Consistency, Measurability, Coverage, Edge case, Compliance. Use `[Gap]` when the spec has nothing to reference.

## Never write implementation tests here

- Wrong: "Verify the button submits the form." "Test that the API returns 200."
- Right: "Is the success and failure feedback for submission specified?" "Are error responses defined for every endpoint in the contract?"

Items that start with "verify", "test" or "confirm" plus a code behaviour belong in `tasks.md`, not here.

## For the security and privacy domains

Seed items from the OWASP Top 10 categories in `.kickstart/compliance.md` and from the controls the feature touches, so the spec is checked for authorisation, input validation, logging, retention, consent and deletion before any code is written.

Stage 6 shows unticked checklist items before it starts; ticking them is the user's job or happens by fixing the spec.
