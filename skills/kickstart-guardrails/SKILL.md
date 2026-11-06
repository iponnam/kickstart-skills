---
name: kickstart-guardrails
description: Installs the project's guardrails in enforced or advised mode: pre-commit and pre-push git hooks (secret scanning, lint, tests), CI gates (dependency vulnerabilities, secret scan, tests), repository settings (branch protection, push protection), and agent hooks so Claude Code and other agents cannot commit secrets or skip tests. Same checks locally, in CI and in the agent. Use during kickstart setup, when the user says "add pre-commit hooks", "block secrets from being committed", "make CI fail on vulnerabilities", "enforce tests", or wants to switch between enforced and advised.
---

# kickstart-guardrails

One set of checks, three places they run: the developer's machine, the CI server, and the agent. Enforced mode blocks. Advised mode reports. The checks are identical; only the exit code differs.

## Inputs

From `.kickstart/project.md`: `enforcement` (`enforced` | `advised`), stack, commands (`lint`, `test`). From the repo: which forge (GitHub, GitLab, other) and which hook manager is already in use, if any (husky, lefthook, pre-commit, simple-git-hooks, lint-staged, overcommit).

## The check set

| Check | Local (pre-commit) | Local (pre-push) | CI | Agent hook |
|---|---|---|---|---|
| Secret scan (gitleaks on staged diff / full on CI) | yes | | yes | before `git commit` |
| Lint + format on changed files | yes | | yes | |
| Type check | | yes | yes | |
| Unit tests | | yes | yes | before `git push` |
| Dependency vulnerability scan | | | yes (fail on critical/high) | |
| Lockfile present and frozen install | | | yes | |
| Conventional commit message | commit-msg | | | |
| No `.env` or key files staged | yes | | yes | before `git commit` |
| Large file guard (>5 MB) | yes | | | |

In `advised` mode every row runs and prints findings, then exits 0 with a clear "ADVISED: would have blocked" line. In `enforced` mode it exits non-zero.

## Step 1: Pick the hook manager

Respect what exists. Otherwise, by ecosystem:

- JavaScript/TypeScript: **lefthook** (single binary, fast, parallel) or husky + lint-staged if the team already knows it.
- Python: **pre-commit** framework.
- Go, Rust, Ruby, PHP, .NET, Java, mixed or no package manager: **lefthook** (works everywhere, config in `lefthook.yml`).

Templates in `templates/`: `lefthook.yml`, `.pre-commit-config.yaml`, `husky/` scripts. Each template reads the mode from `.kickstart/project.md` through the small shim `templates/kickstart-mode.sh` so flipping the mode is a one-line edit.

## Step 2: Install local hooks

1. Copy every `*.sh` file from this skill's `templates/` into the project at `.kickstart/hooks/` (the project owns its hooks; they must work without this skill installed). Then copy the matching hook-manager template (`lefthook.yml`, `.pre-commit-config.yaml`) to the project root and substitute the project's `lint`, `typecheck` and `test` commands for the `{{...}}` placeholders.
2. Install the manager as a dev dependency or document the install (`brew install lefthook` / `pipx install pre-commit`), and add a `postinstall`/`prepare` or `make setup` so teammates get hooks automatically.
3. Install gitleaks detection: prefer the `gitleaks` binary; fall back to `trufflehog`; if neither can be installed, use `templates/secret-patterns.sh` (regex-based, weaker, say so).
4. Run the hooks once on the whole repo to confirm they pass (or, for existing repos, to list what they would block). Never leave the user with hooks that fail on an untouched repo in `enforced` mode; fix or move the failing check to `advised` for that check and record it in `project.md` under Conventions.

## Step 3: CI gates

Add or extend the CI workflow with the `security` job from `templates/ci-security.yml`:

- gitleaks: full history scan on the default branch, diff scan on pull requests.
- Dependency scan with the ecosystem tool, `osv-scanner` as universal fallback. Fail on critical/high in `enforced`; `continue-on-error: true` with a summary in `advised`.
- Lockfile check: install with frozen/locked flag.
- Required checks: in `enforced`, instruct the user to mark `quality` and `security` as required status checks in branch protection (`templates/branch-protection.md` has the exact settings and the `gh api` command).

## Step 4: Repository settings

Tell the user, or run with `gh` if authorised:

- Branch protection on the default branch: require PR, require status checks, no force push, require linear history (`scale`), signed commits (`scale`, optional).
- GitHub secret scanning + push protection: on. Dependabot alerts: on.
- Template commands are in `templates/branch-protection.md`.

## Step 5: Agent hooks

Agents should be held to the same rules. For Claude Code, add to the project's `.claude/settings.json` (merge, do not overwrite) using `templates/claude-settings.json`:

- `PreToolUse` hook on `Bash` matching `git commit`: runs the staged secret scan and the `.env`/key-file guard. Blocks in `enforced`, warns in `advised`.
- `PreToolUse` hook on `Bash` matching `git push`: runs tests. Same rule.
- `PreToolUse` hook on `Write|Edit` for paths matching `.env`, `*.pem`, `*.key`, `id_rsa*`: blocks writing secrets into tracked files.

For other agents that support hooks, mirror the same three rules; where unsupported, the `CLAUDE.md`/`AGENTS.md` block from kickstart states the rules in prose.

## Step 6: Record and explain

Update `.kickstart/project.md`:

```
## Guardrails
- mode: enforced | advised
- hook_manager: lefthook | pre-commit | husky
- secret_scanner: gitleaks | trufflehog | regex-fallback
- ci_security_job: yes
- branch_protection: on | documented, not applied
- agent_hooks: claude-code
```

Tell the user in five lines: what blocks, what warns, how to bypass in a real emergency (`git commit --no-verify` and `LEFTHOOK=0`; say it is logged in CI anyway), and how to flip the mode (`enforcement:` line in `project.md`, then re-run this skill).

## Switching modes

When asked to flip: edit `project.md`, re-run the hook install step (templates read the mode at runtime, so often nothing else changes), update CI `continue-on-error`, and re-run the hooks once to show what now blocks.

## Rules

- Never weaken an existing stricter check. If the repo already fails on medium vulnerabilities, keep that.
- Never store secrets or tokens in hook config or CI YAML. Use the forge's secret store.
- Keep pre-commit under 10 seconds: staged-files only for lint and secret scan. Tests go to pre-push and CI.
- Hooks must work on macOS, Linux and Windows (Git Bash). Avoid GNU-only flags in shell templates.
