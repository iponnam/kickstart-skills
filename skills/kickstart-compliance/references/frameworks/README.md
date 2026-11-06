# Framework records

One file per framework, named `<id>.md`. Every fact in a record comes from the framework's official governing body: the standard owner, regulator, legislature or official gazette. Vendors, law firms, Wikipedia, IAPP and news are never sources of facts.

Records are re-verified under the skill's freshness rule: when `last_verified` is more than 60 days old, or earlier when a pending change in the record's Notes has taken effect, the agent re-fetches `official_sources`, updates the record in the project cache (`.kickstart/cache/frameworks/<id>.md`) and stamps a new `last_verified` with `scripts/freshness.py mark`.

`verification` means:

- `verified`: scope, version and the key numbers were confirmed on an official source.
- `partial`: some facts were confirmed; the rest are marked `UNVERIFIED` in the record. Common for paid standards (ISO, parts of AICPA) where only the official free abstract is readable, and for sites that block automated access.
- `unreachable`: no official source could be read when the record was written. Treat every fact as unverified and re-check before use.

## Template

```markdown
---
id: <kebab-id, same as file name>
name: <short common name>
official_name: <full official title>
governing_body: <issuer; and enforcer if different>
type: security | privacy | quality | continuity | governance | ai | sector
legal_status: law | binding-regulation | regulator-guideline | voluntary-standard | certification-scheme | contractual
region: <jurisdiction(s), incl. extraterritorial reach if stated>
industry: <any | sectors>
current_version: <version / act number, date of adoption or in-force date>
superseded_by: <newer version, or "none">
official_sources:
  - title: <document or page title>
    url: <exact url>
    accessed: <YYYY-MM-DD>
last_verified: <ISO 8601 timestamp of the last full check>
verification: verified | partial | unreachable
---

## What it is
## Who it applies to
## Engineering obligations
| ID | Obligation | Official reference |
## Deadlines and numbers
| What | Value | Official reference |
## Assessment and certification
## Notes
```

Run `python3 scripts/check-frameworks.py` from the repository root after adding or editing a record.
