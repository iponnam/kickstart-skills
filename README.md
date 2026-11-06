# kickstart-skills

**One command. Production-grade apps. Any stack.**

`kickstart` is a bundle of agent skills that bakes engineering, security, vulnerability and compliance guidelines into every project, so you only have to think about *what* you want to build.

It works for **new projects** (recommend a stack, scaffold a runnable app with CI, tests, security scanning, auth, database, deployment and a first feature) and for **existing projects** (audit, score, and propose changes with numbers you can read in thirty seconds).

Works with Claude Code, Cursor, Codex, OpenCode and any agent that reads the open [Agent Skills](https://agentskills.io) format.

---

## Install

**Any agent (recommended):**

```bash
npx skills add iponnam/kickstart-skills
```

Add `-g` to install for every project on your machine instead of just the current one.

**Claude Code plugin:**

```bash
claude plugin marketplace add iponnam/kickstart-skills
claude plugin install kickstart@kickstart-skills
```

**Manual:** copy the `skills/` folders into `.claude/skills/` (Claude Code), `.cursor/skills/` (Cursor) or your agent's skills directory.

---

## Use

Open your project (or an empty folder) in your agent and type:

```
/kickstart
```

That is the whole interface. `kickstart` detects whether the folder is a new or existing project and routes you:

| Situation | What happens |
|---|---|
| **Empty folder** | Asks what you want to build and whether it is a pet project or must scale. Recommends 2–3 stacks with costs and trade-offs. Scaffolds a runnable app with CI, lint, tests, security scanning, docs, auth, database, deployment config and your first real feature. |
| **Existing repo** | Runs an audit. Shows an executive summary first (score, critical findings, effort to fix), then lets you drill into details. Proposes changes and shows what each change does in numbers before touching anything. |
| **Already kickstarted** | Shows status and offers the day-to-day skills below. |

During setup you choose two things that every later session respects:

- **Pet project or scale?** Shapes stack, hosting and how much process is worth it.
- **Enforced or advised?** *Enforced* installs git hooks and CI gates that block commits and merges on secrets, critical vulnerabilities or missing tests. *Advised* reports and recommends but never blocks.

Your decisions are written to `.kickstart/project.md` and a short block in `CLAUDE.md` (or `AGENTS.md`), so every future session, by any teammate or agent, follows them automatically. No need to re-explain your project.

---

## The skills

You can call any skill directly, but `/kickstart` routes to them for you.

| Skill | When it runs | What it does |
|---|---|---|
| [`kickstart`](skills/kickstart/SKILL.md) | `/kickstart`, or when you say "start a project", "set this project up", "audit this repo" | Entry point and router. Detects context, asks the two decisions, delegates, records everything in `.kickstart/`. |
| [`kickstart-stack-advisor`](skills/kickstart-stack-advisor/SKILL.md) | New project, or "which stack should I use" | Turns a plain-language description into 2–3 concrete stack options with hosting, third-party service and AI API costs, plus pros and cons for pet vs scale. Works for non-technical users. |
| [`kickstart-scaffold`](skills/kickstart-scaffold/SKILL.md) | New project after a stack is chosen | Generates a runnable project: app skeleton, CI, lint and format, tests, secret and dependency scanning, docs, auth, database, deploy config, and the first feature. |
| [`kickstart-audit`](skills/kickstart-audit/SKILL.md) | Existing repo, or "how healthy is this codebase" | Runs `scripts/audit.py` to measure security, dependencies, tests, CI, docs and compliance. Produces an executive summary with a 0–100 score and a drill-down report. Every proposed change comes with before/after numbers. |
| [`kickstart-compliance`](skills/kickstart-compliance/SKILL.md) | During setup, or "what compliance do I need" | OWASP Top 10 is always on. Recommends further frameworks from 85 records (SOC 2, ISO/IEC 27001, GDPR, HIPAA, PCI DSS, DPDPA, DORA, NIS 2, EU AI Act, RBI, SEBI, MAS, SAMA…) based on your region and industry. Every record cites its official governing body and is re-verified when older than 60 days. You pick. Writes engineering-level checklists, not legal fluff. |
| [`kickstart-guardrails`](skills/kickstart-guardrails/SKILL.md) | During setup, or "add pre-commit hooks" | Installs the enforced or advised guardrails: secret scanning, dependency audit, lint, tests, and agent hooks. Same checks locally, in CI, and in the agent. |
| [`kickstart-feature`](skills/kickstart-feature/SKILL.md) | "Add a feature", "build X", "implement Y" | Spec, plan, build, test, review. Reads `.kickstart/project.md` so every feature respects the stack, scale and compliance decisions. |
| [`kickstart-release`](skills/kickstart-release/SKILL.md) | "Ship it", "release", "deploy to production" | Pre-release checklist: tests, vulnerabilities, secrets, migrations, rollback plan, changelog, monitoring. Blocks or warns per your enforcement choice. |
| [`kickstart-refresh`](skills/kickstart-refresh/SKILL.md) | Monthly, or "update dependencies" | Dependency and vulnerability refresh. Groups updates by risk, runs tests between groups, re-audits, and reports the delta in numbers. |

---

## What "production grade" means here

Every project kickstart touches ends up with, at minimum:

- **Security:** OWASP Top 10 controls mapped to concrete code, secret scanning, dependency vulnerability scanning, security headers, input validation, least-privilege config.
- **Quality:** linter, formatter, type checking where the language allows, unit and integration tests, CI that runs them on every push.
- **Operability:** structured logging, health endpoint, environment-based config, Dockerfile or platform config, deployment pipeline, rollback plan.
- **Documentation:** README that lets a stranger run it in five minutes, architecture note, decision log, runbook.
- **Compliance:** a scoped checklist in `.kickstart/compliance.md` with each control marked implemented, planned or not applicable.

The depth is scaled to your answer to "pet project or scale?". A weekend project gets the essentials in minutes. A product that must scale gets the full set.

---

## Project files kickstart creates

```
your-project/
├── .kickstart/
│   ├── project.md        # stack, scale, enforcement, owners: the source of truth for agents
│   ├── compliance.md     # chosen frameworks and control checklist with status
│   ├── cache/            # official-source records and prices, each with last_verified (24h for stack, 60d for compliance)
│   ├── decisions/        # one file per architectural decision (ADR format)
│   └── audit/
│       └── latest.md     # most recent audit summary and score
├── CLAUDE.md             # short block pointing agents at .kickstart/ (also works as AGENTS.md)
└── ...
```

Everything is plain Markdown and JSON. Commit it. Read it. Edit it by hand if you like.

---

## Example sessions

**New project, non-technical founder**

```
> /kickstart
I want a web app where tutors list availability and students book and pay.

kickstart: Is this a personal/pet project or something that must scale to real users?
> It needs to scale, I plan to charge for it.

kickstart: Should guardrails be enforced (block bad commits) or advised (warn only)?
> Enforced.

kickstart: Which region are your users in, and what industry? (for compliance)
> India and the UK. Education.

kickstart → stack-advisor: Here are 3 options…
  1. Next.js + Supabase + Stripe on Vercel   ~$0–25/mo to start, scales to ~$200/mo at 10k users …
  2. Django + Postgres + Stripe on Railway    …
  3. Rails + Postgres on Fly.io               …
> 1

kickstart → compliance: OWASP Top 10 is on. For India + UK + education I recommend
  DPDP Act (India), UK GDPR, and PCI DSS SAQ-A (you use Stripe Checkout, so minimal). Add any?
> That's fine.

kickstart → scaffold: Creating project… 47 files. CI green. Auth, bookings table, Stripe checkout and first feature "tutor lists availability" done. Run `npm run dev`.
```

**Existing project**

```
> /kickstart

kickstart → audit:
  Score: 58/100

  Critical (fix this week)
  • 2 secrets committed in history (.env, config/prod.yml)
  • 7 critical / 23 high dependency vulnerabilities

  Executive summary
  • Security 41/100 · Dependencies 35/100 · Tests 62/100 · CI 80/100 · Docs 70/100 · Compliance 55/100
  • Est. effort to reach 85: ~14 hours across 9 changes

  Say "details" for the full report, or pick a change to apply:
  1. Rotate and purge secrets        → Security 41 → 68   (1.5h)
  2. Upgrade 23 vulnerable deps      → Dependencies 35 → 88 (3h, 2 breaking)
  3. Add secret-scanning pre-commit  → prevents recurrence (10m)
  ...
```

---

## Philosophy

1. **Simple on the surface.** One command. Two questions. Plain language.
2. **Opinionated underneath, agnostic about stacks.** We care that you have tests, scanning and a rollback plan. We do not care whether you write Go or TypeScript.
3. **Numbers, not lectures.** Every recommendation says what changes and by how much.
4. **Decisions persist.** Agents forget. Files don't. `.kickstart/` is the project's memory.
5. **Compliance is engineering.** A control is a piece of code, config or process, with a status. Not a PDF.
6. **Official sources, never memory.** Every framework fact cites its governing body: the regulator, standard owner or official gazette. Prices, free tiers and library versions older than 24 hours, and compliance framework records older than 60 days, are re-checked against the official source before use and cached in `.kickstart/cache/` with a timestamp. If a source cannot be reached, the value is shown as `unverified since <date>`.

---

## Repository layout

```
kickstart-skills/
├── skills/                  # the skills (one folder each, SKILL.md inside)
├── .claude-plugin/          # Claude Code plugin + marketplace manifests
├── docs/                    # design notes, framework catalog sources, contributing
├── LICENSE                  # MIT
└── README.md
```

## Contributing

See [docs/CONTRIBUTING.md](docs/CONTRIBUTING.md). Framework catalog corrections, new stack profiles and cost updates are the most useful contributions.

## License

MIT. Use it, fork it, ship things.
