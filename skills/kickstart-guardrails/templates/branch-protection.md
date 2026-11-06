# Repository settings for guardrails

Apply by hand in the forge UI, or with the commands below when `gh` is authenticated.

## GitHub

Branch protection on the default branch (replace `OWNER/REPO` and `main`):

```bash
gh api -X PUT repos/OWNER/REPO/branches/main/protection \
  -H "Accept: application/vnd.github+json" \
  --input - <<'EOF'
{
  "required_status_checks": { "strict": true, "contexts": ["quality", "secret scan", "dependency vulnerabilities"] },
  "enforce_admins": false,
  "required_pull_request_reviews": { "required_approving_review_count": 1, "dismiss_stale_reviews": true },
  "restrictions": null,
  "allow_force_pushes": false,
  "allow_deletions": false,
  "required_linear_history": true,
  "required_conversation_resolution": true
}
EOF
```

For a solo `pet` project set `required_approving_review_count` to 0 and keep the status checks.

Secret scanning and push protection, Dependabot alerts and security updates:

```bash
gh api -X PATCH repos/OWNER/REPO \
  --input - <<'EOF'
{
  "security_and_analysis": {
    "secret_scanning": { "status": "enabled" },
    "secret_scanning_push_protection": { "status": "enabled" },
    "dependabot_security_updates": { "status": "enabled" }
  }
}
EOF
```

Dependabot config (`.github/dependabot.yml`):

```yaml
version: 2
updates:
  - package-ecosystem: "npm"          # or pip, gomod, cargo, bundler, composer, nuget, maven, gradle, pub, mix
    directory: "/"
    schedule: { interval: "weekly" }
    groups:
      minor-and-patch:
        update-types: ["minor", "patch"]
  - package-ecosystem: "github-actions"
    directory: "/"
    schedule: { interval: "weekly" }
```

## GitLab

- Settings → Repository → Protected branches: protect `main`, allowed to push: no one, allowed to merge: maintainers.
- Settings → Merge requests: pipelines must succeed; all threads resolved.
- Settings → Security: enable secret detection and dependency scanning templates in `.gitlab-ci.yml` (`include: template: Security/Secret-Detection.gitlab-ci.yml`).

## Advised mode

Still turn on secret scanning and push protection. They cost nothing and catch the worst mistake. Skip required reviews and required checks until the team is ready, and record that in `.kickstart/project.md`.
