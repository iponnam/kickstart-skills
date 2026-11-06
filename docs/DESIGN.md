# Design notes

Why kickstart is shaped the way it is.

## Goals (from the original brief)

- Ship production-grade apps regardless of tech stack.
- For everyone: solo developers, teams, non-technical founders directing an agent.
- Bake in tech, security, vulnerability and compliance guidelines so people only think about what they want to build.
- Usage must be organic: auto-trigger from context, one simple default command, and files in the repo that future sessions pick up.
- Existing projects: audit, propose, show the effect of changes in numbers, executive summary first with details on request.
- New projects: scaffold code plus the process and documentation layer, through to the first real feature.
- Stack-agnostic: recommend options with costs and trade-offs; always ask pet project vs scale.
- Compliance: OWASP Top 10 mandatory; recommend others by region and industry from the full catalog; user selects.
- Enforced vs advised chosen at init.
- Decisions persist in the repo.
- Day-to-day skills: feature workflow, release checklist, monthly refresh.
- Costs cover hosting and third-party services including AI APIs.

## Three ways usage becomes organic

1. **Descriptions that match natural phrases.** Each `SKILL.md` description lists the things people actually say ("ship it", "add a feature", "is this production ready"). Agents that select skills by description trigger them without a slash command.
2. **One default command.** `/kickstart` is the only thing anyone has to remember. It routes.
3. **Files in the repo.** `.kickstart/project.md`, `.kickstart/compliance.md` and the `CLAUDE.md`/`AGENTS.md` block are read by every future session. The project remembers its own decisions, so the user never re-explains them and every agent follows them.

## Why numbers

Non-technical readers cannot evaluate "you should add rate limiting". They can evaluate "Security 41 → 68 in 1.5 hours". Every proposal in the audit carries before/after score, overall gain, effort and risk, and the executive summary fits on one screen. Details exist for engineers who want them.

## Why compliance is a checklist with three statuses

Frameworks are large. Engineering teams need to know what to build, what is done, and what is deliberately out of scope. `implemented | planned | n/a` with an evidence pointer is the smallest format that an auditor, a founder and an agent can all read. The catalog is tagged by region, industry and trigger so the recommendation step is a filter, not a lecture.

## Why freshness rules (24 hours for stack, 60 days for compliance)

Compliance deadlines, framework editions, prices and library versions change faster than any model's training data. During the first research pass for this repo, official sources overturned a dozen of the original catalog's claims, including the current OWASP Top 10 edition, the PCI DSS version and the Cyber Essentials version. So no skill states such a fact from memory. Bundled records carry `official_sources` and a `last_verified` timestamp. Tech stack facts (prices, free tiers, versions, generator commands) change weekly, so they expire after 24 hours. Compliance framework records change on legislative and standards cycles, so they expire after 60 days, or sooner when a record's Notes show a pending change has taken effect. When a record is past its age, the agent re-fetches the official pages for the frameworks, providers or libraries it is about to use, updates a project-local copy under `.kickstart/cache/`, and stamps it with `freshness.py mark`. Only what the current step needs is re-checked, which keeps it to a handful of fetches. If a source is unreachable, work continues with the older value, clearly labelled.

## Why enforced vs advised is a mode, not a fork

The checks are identical in both modes; only the exit code differs. A single shim (`kickstart-mode.sh`) reads the mode from `project.md`, so switching is a one-line edit and the hook, CI and agent layers all follow.

## Why a Python script for the audit

It must run anywhere with no install step, handle a dozen ecosystems, and degrade gracefully when scanners are missing. Python 3 standard library is the most portable choice. The scoring contract is documented in the skill so an agent without Python can do the same assessment by hand.

## Non-goals

- Not a code generator for every framework. It uses each ecosystem's official generator and layers production pieces on top.
- Not a legal compliance product. It prepares engineering evidence; auditors and lawyers do the rest.
- Not a replacement for Dependabot, Sentry, or a CI system. It wires those in.

## Open questions and roadmap

- Per-framework control sets beyond the condensed families (contributions welcome).
- Audit script: GitLab CI parsing depth, monorepo per-package mode, SARIF output for forge integration.
- A `kickstart-threat-model` skill for `scale` projects.
- Localised cost tables (INR, EUR, GBP) with a dated exchange rate note.
