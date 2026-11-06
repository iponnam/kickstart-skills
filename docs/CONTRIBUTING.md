# Contributing

Thanks for helping make kickstart better. The most valuable contributions, in order:

1. **Framework record updates** in `skills/kickstart-compliance/references/frameworks/<id>.md`. Every fact must come from the framework's official governing body (regulator, standard owner, legislature or official gazette), with the exact URL and access date. Vendors, law firms, Wikipedia and news are not accepted as sources. Update `last_verified` and `verification`, then regenerate the catalog with `python3 scripts/build-catalog.py`. Do not edit `framework-catalog.md` by hand.
2. **Cost updates** in `skills/kickstart-stack-advisor/references/cost-reference.md`. Include the provider pricing page URL and the date.
3. **Stack profiles** in `skills/kickstart-stack-advisor/references/stack-catalog.md` and matching scaffold notes in `skills/kickstart-scaffold/references/layouts.md`.
4. **Audit detections** in `skills/kickstart-audit/scripts/audit.py`: new unsafe patterns, new scanner integrations, better coverage parsing. Keep it standard-library only.
5. **Guardrail templates** for other hook managers, forges or agents.

## Skill format

Each skill is a folder under `skills/` with a `SKILL.md` that starts with YAML frontmatter:

```yaml
---
name: kickstart-something        # lowercase, hyphens, matches the folder name
description: What it does and when to use it, including the phrases a user would say.
---
```

Keep `SKILL.md` focused on procedure. Put long reference material in `references/`, runnable code in `scripts/`, and files to copy into projects in `templates/`. The skill body should tell the agent when to read each reference, so context is loaded only when needed.

## Testing a change

```bash
# needs PyYAML: pip install pyyaml
# frontmatter and structure
python3 scripts/check-skills.py

# framework records: required keys, official sources, sections, catalog links
python3 scripts/build-catalog.py
python3 scripts/check-frameworks.py

# audit script against a sample repo
python3 skills/kickstart-audit/scripts/audit.py --repo /path/to/some/repo --out /tmp/kickstart-audit
```

Try the skill in a real agent session on both a new empty folder and an existing repo before opening a pull request.

## Pull requests

- Conventional Commits (`feat:`, `fix:`, `docs:`...).
- One topic per PR.
- For catalog or cost changes, include the source link in the PR description.
