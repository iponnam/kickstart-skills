# Stage 7: Converge

Check the actual code against the spec, plan, tasks, constitution and compliance checklist. Append whatever is still unbuilt as new tasks. Repeat Stage 6 and Stage 7 until the result is **Converged**.

## Rules

- **Append-only.** The only file this stage writes is `tasks.md`, and only by appending a new phase at the end. It never edits code, never edits or renumbers existing tasks, never deletes code.
- **Ticks are not evidence.** Assess every requirement, whether or not its task is ticked.
- **Stay in scope.** Assess only the files and components the plan and tasks name, plus a keyword search for each requirement's concepts.

## Procedure

1. Build the inventory: every `FR-###`, `SC-###`, `US#/AC#`, each plan decision that implies work, each constitution MUST that applies, and each compliance control the plan lists.
2. For each item, inspect the code and tests. Record a finding only where there is a gap:
   - **missing:** the work is absent.
   - **partial:** it exists but does not fully meet the requirement.
   - **contradicts:** the code conflicts with the spec, plan or a constitution MUST.
   - **unrequested:** code exists that nothing asked for. Converge does not delete it; it adds a task to justify or remove it.
3. Run the tests. A requirement whose test fails or does not exist is at least `partial`.
4. Assign severity:
   - **CRITICAL:** a constitution MUST is violated, or a P1 story is blocked.
   - **HIGH:** a core requirement or scenario is missing or partial; a compliance control has no evidence.
   - **MEDIUM:** a secondary requirement is partial; an unrequested addition lacks justification.
   - **LOW:** polish, minor gaps.
5. Show the findings table before writing anything:

```
| ID | Gap | Severity | Source | Evidence | Remaining work |
| F1 | missing | HIGH | FR-008 | no retention job in src/jobs/ | Add 90-day deletion job |
Checked: <n> requirements, <n> scenarios, <n> plan decisions, <n> principles, <n> controls
```

## Outcome

- **Findings exist:** append `## Phase N: Convergence` to `tasks.md` (N = last phase + 1). One task per finding, CRITICAL and HIGH first, IDs continuing from the highest existing ID:
  `- [ ] T043 Add 90-day deletion job in src/jobs/retention.ts per FR-008 (missing)`
  Then return to Stage 6.
- **No findings:** do not touch `tasks.md`. Report "Converged: the implementation satisfies the spec, plan and tasks", with the counts checked. Go to the Finish step in the skill.

Stop the loop after three rounds that each append tasks, and ask the user whether to continue, descope or split the feature.
