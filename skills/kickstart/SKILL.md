---
name: kickstart
description: Entry point for making any project production-grade, regardless of tech stack. Use when the user types /kickstart, says "start a new project", "set up this project", "make this production ready", "audit this repo", "is this codebase healthy", or opens an empty folder and describes something they want to build. Detects new vs existing project, asks two decisions (pet project or scale; enforced or advised guardrails), then routes to kickstart-stack-advisor, kickstart-scaffold, kickstart-audit, kickstart-compliance and kickstart-guardrails. Records every decision in .kickstart/project.md so later sessions follow them automatically.
---

# kickstart

You are the front door. Keep it simple for the user: one command, two questions, plain language. Do the heavy lifting by delegating to the other `kickstart-*` skills and recording decisions so nobody has to repeat them.

## Step 0: Detect context

Run these checks silently before saying anything:

1. **Already kickstarted?** `.kickstart/project.md` exists. Go to [Mode C](#mode-c-already-kickstarted).
2. **Existing project?** Any of: a `.git` directory with commits, a dependency manifest (`package.json`, `pyproject.toml`, `requirements.txt`, `go.mod`, `Cargo.toml`, `pom.xml`, `build.gradle`, `Gemfile`, `composer.json`, `*.csproj`, `mix.exs`, `pubspec.yaml`), or more than 5 source files. Go to [Mode B](#mode-b-existing-project).
3. **Otherwise** it is a new project. Go to [Mode A](#mode-a-new-project).

If the user's message already states their intent clearly (for example "audit this" in a new folder, or "start fresh" in an existing repo), follow their intent instead of the detection.

## The two decisions

Ask these in every mode, one at a time, unless `.kickstart/project.md` already answers them. Accept short answers. Do not explain at length unless asked.

**Decision 1: Pet project or scale?**

> Is this a personal/pet project, or something that must scale to real users and revenue?

- `pet`: minimal process, free or near-free hosting, essentials only. Still secure. Still has tests and CI, because those take minutes and save hours.
- `scale`: full set. Observability, migrations, rollback, compliance scope, cost modelling, team conventions.

If the user is unsure, ask: "Will anyone other than you depend on it in the next 6 months?" Yes means `scale`.

**Decision 2: Enforced or advised?**

> Should guardrails be enforced (git hooks and CI block commits and merges on secrets, critical vulnerabilities or failing tests) or advised (you get warnings and recommendations, nothing blocks)?

- `enforced` is the right default for `scale` and for teams.
- `advised` is fine for `pet` and for existing repos that are not ready for blocking yet. Offer to flip to enforced after the first audit's critical items are fixed.

Record both answers in `.kickstart/project.md` before continuing.

## Mode A: New project

1. Ask what they want to build, in their own words. One open question. Do not ask about tech yet.
2. Ask Decision 1 and Decision 2.
3. Ask for compliance context in one question: "Which country or region are your users in, and what industry is this?" (Needed by `kickstart-compliance`. If they say "not sure", default to their likely location and "general SaaS".)
4. Invoke **kickstart-stack-advisor** with the description, scale answer, region and industry. It returns 2–3 options with costs and trade-offs. Present them. Let the user choose. If the user is non-technical, recommend one explicitly and say why in two sentences.
5. Invoke **kickstart-compliance** with region, industry and stack. It proposes frameworks (OWASP Top 10 always on). User confirms or edits the list. It writes `.kickstart/compliance.md`.
6. Write `.kickstart/project.md` (template below) with everything decided so far.
7. Invoke **kickstart-constitution**. It writes `.kickstart/constitution.md`, the versioned rules every later plan is checked against, seeded from the decisions so far, and asks one question about house rules.
8. Invoke **kickstart-scaffold** with the chosen stack. It creates the runnable project, CI, tests, scanning, docs, auth, database, deploy config and the first feature, built through the `kickstart-feature` spec workflow.
9. Invoke **kickstart-guardrails** with the enforcement choice. It installs hooks, CI gates and agent hooks.
10. Write the `CLAUDE.md` block (below). If `AGENTS.md` exists or the user's agent is not Claude, write the same block there.
11. Finish with a short summary: what was created, how to run it, and the most useful next steps by their plain-language triggers: add a feature, fix a bug, release, refresh dependencies.

## Mode B: Existing project

1. Ask Decision 1 and Decision 2. For existing repos suggest `advised` first unless the user is confident.
2. Ask the compliance context question (region, industry) if not inferable from the code or docs.
3. Invoke **kickstart-audit**. It runs its audit script, produces the executive summary with a 0–100 score, and a ranked list of proposed changes, each with before/after numbers and effort. Show the executive summary. Do not show the full report unless the user asks for "details".
4. Invoke **kickstart-compliance** with the audit's findings so the compliance checklist reflects reality (controls already met are marked implemented).
5. Write `.kickstart/project.md` with the detected stack, decisions and the audit score.
6. Invoke **kickstart-constitution**, recording the conventions the codebase actually follows.
7. Offer the proposed changes one at a time, highest impact first. Apply only what the user picks. After each applied change, re-run the relevant audit check and show the number moving.
8. Invoke **kickstart-guardrails** at the end, or as soon as the user picks a change that adds hooks or CI.
9. Write the `CLAUDE.md` block.

Never rewrite an existing project's structure wholesale. Propose, show numbers, apply what is chosen.

## Mode C: Already kickstarted

Read `.kickstart/project.md` and `.kickstart/audit/latest.md` if present. Show a five-line status:

- Stack, scale, enforcement
- Last audit score and date
- Compliance frameworks and the count of controls implemented / total
- Constitution version, and features under `specs/` that are not yet converged
- Any open proposed changes from the last audit
- What they can do next: add a feature, fix a bug, release, refresh dependencies, re-audit

Then wait for instruction. If the last audit is older than 30 days, offer to re-run it.

## `.kickstart/project.md` template

Write it exactly in this shape so every other skill can parse it.

```markdown
# Project: <name>

> Source of truth for agents and humans. Edit freely. Keep the field names.

## What we are building
<one paragraph in the user's words>

## Decisions
- scale: pet | scale
- enforcement: enforced | advised
- region: <countries or regions>
- industry: <industry>
- created: <YYYY-MM-DD>
- kickstart_version: 0.2.0

## Stack
- language: <e.g. TypeScript>
- framework: <e.g. Next.js 15>
- database: <e.g. Postgres via Supabase>
- auth: <e.g. Supabase Auth>
- hosting: <e.g. Vercel>
- ci: <e.g. GitHub Actions>
- package_manager: <e.g. pnpm>
- test_runner: <e.g. vitest>
- lint: <e.g. eslint + prettier>

## Commands
- install: <command>
- dev: <command>
- test: <command>
- lint: <command>
- build: <command>
- audit: python3 .kickstart/audit.py

## Compliance
- frameworks: OWASP Top 10, <others>
- checklist: .kickstart/compliance.md

## Audit
- last_score: <0-100 or none>
- last_run: <date or none>
- report: .kickstart/audit/latest.md

## Conventions
<bullet list: branch naming, commit style, folder layout, anything the team agreed>
```

## `CLAUDE.md` block

Append this block if it is not already present. Keep it short. It is what makes usage organic: any future session reads it and behaves accordingly without the user typing anything.

```markdown
<!-- kickstart:start -->
## Project guardrails (kickstart)

This project was set up with kickstart. Before making changes:
1. Read `.kickstart/constitution.md` and `.kickstart/project.md`. The constitution's MUST rules are non-negotiable.
2. Read `.kickstart/compliance.md` before touching auth, data storage, logging, payments or anything user-facing.
3. For product changes use the kickstart-feature workflow: spec, clarify, plan, tasks, consistency check, implement, converge, with files under `specs/NNN-feature/`. For bugs use kickstart-bugfix: assess, fix with a regression test, verify.
4. Before a release run the kickstart-release checklist.
5. Never commit secrets. Never disable a guardrail to make a check pass. Fix the cause.
6. Never state a price, library version, compliance deadline or framework version from memory. Use `.kickstart/cache/` only if its `last_verified` is within the allowed age: 24 hours for tech stack facts, 60 days for compliance framework records. Otherwise re-check the official source first and update the cache.
<!-- kickstart:end -->
```

## Freshness: never rely on memory

Some facts change faster than any model's training data: compliance frameworks and their deadlines, prices and free tiers, framework and library versions, generator commands, and vulnerability data. Every `kickstart-*` skill follows one rule for them:

- Use only facts checked against the official source within the allowed age:

  | Kind of fact | Maximum age | Checked by |
  |---|---|---|
  | Tech stack: prices, free tiers, framework and library versions, generator commands | **24 hours** | `kickstart-stack-advisor`, `kickstart-scaffold`, `kickstart-refresh` |
  | Compliance frameworks: versions, scope, deadlines, thresholds, penalties | **60 days**, or sooner when a known change takes effect | `kickstart-compliance` (`freshness.py`) |
  | Vulnerability data | Always live | Scanners run at the time of the check |

- Bundled reference files and the project cache under `.kickstart/cache/` carry a `last_verified:` timestamp. Older than the allowed age means re-fetch from the official source before use, then update the cache.
- If the official source cannot be reached, continue with the older value, label it `unverified since <date>`, and tell the user which source failed.
- Fetch only what the current step uses, so the check stays fast.

Tell the user this once, during setup, in one sentence.

## Tone and behaviour

- Ask one question at a time. Accept one-word answers.
- Non-technical users exist. When they pick a stack, confirm in plain words what they are getting and what it will cost per month.
- Show numbers before and after any change you propose.
- Never silently change an existing project. Propose, then apply what the user chooses.
- If a tool the audit needs is missing, say so in one line and continue with what is available. Do not stop.
- If the user wants to skip a step, let them. Record `skipped` in `project.md` so the next session can offer it again.

## Delegation summary

| Need | Skill |
|---|---|
| Recommend a stack with costs | `kickstart-stack-advisor` |
| Create a runnable new project | `kickstart-scaffold` |
| Measure an existing project | `kickstart-audit` |
| Choose frameworks, write checklist | `kickstart-compliance` |
| Install hooks and CI gates | `kickstart-guardrails` |
| Write or amend the project rules | `kickstart-constitution` |
| Build a feature (spec, clarify, plan, tasks, check, implement, converge) | `kickstart-feature` |
| Fix a bug (assess, fix, verify) | `kickstart-bugfix` |
| Ship a version | `kickstart-release` |
| Update dependencies | `kickstart-refresh` |
