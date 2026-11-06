# OWASP Top 10:2025 as engineering controls

Mandatory for every kickstart project. Source: OWASP Foundation, which says "The most current released version is the OWASP Top 10 2025" ([project page](https://owasp.org/www-project-top-ten/), accessed 2026-11-06). Controls paraphrase each category's official "How to prevent" section ([official repository](https://github.com/OWASP/Top10/tree/master/2025/docs/en)). Full source record: [`frameworks/owasp-top10.md`](frameworks/owasp-top10.md).

OWASP calls the Top 10 an awareness document. It is not certifiable, and OWASP does not attest compliance. Teams self-assess with code review, SAST/DAST and testing. "How to verify" below is kickstart's check, not OWASP text.

| ID | Category | Control (what to implement) | How to verify | Pet projects |
|---|---|---|---|---|
| A01:2025 | Broken Access Control (now includes SSRF) | Enforce access control in trusted server-side code. "Except for public resources, deny by default." Implement once and reuse. Enforce record ownership. Minimise CORS. Disable directory listing and keep `.git`/backups out of web roots. Invalidate sessions at logout; keep stateless JWTs short-lived. For server-side fetches of user-supplied URLs, allow-list destinations and block internal addresses (SSRF, formerly A10:2021). | Shared auth middleware on every non-public route; a test that user A cannot read user B's record; grep for fetches of user-controlled URLs. | Required |
| A02:2025 | Security Misconfiguration | Repeatable hardening. Dev, QA and prod configured identically with different credentials. Minimal platform, no unused features. Send security headers. Automate configuration verification in all environments (OWASP: manual verification "annually at a minimum" if not automated). Use identity federation, short-lived credentials or platform roles "instead of embedding static keys or secrets in code, configuration files, or pipelines". | Header check against the running app; debug flags wired to env; secret scanner clean. | Required |
| A03:2025 | Software Supply Chain Failures (expands A06:2021) | "Centrally generate and manage the Software Bill of Materials (SBOM)." Track transitive dependencies; remove unused ones. Continuously monitor CVE/NVD/OSV with software composition analysis. Obtain components from official sources; prefer signed packages. Keep CI/CD and developer tooling updated; change-track CI/CD settings. Use staged or canary rollouts. | Lockfile committed; dependency scan in CI with 0 critical; Dependabot/Renovate configured; SBOM at release. | Scan required; SBOM planned |
| A04:2025 | Cryptographic Failures | Classify data. Do not store sensitive data unnecessarily; tokenise or truncate. Encrypt sensitive data at rest. In transit use "protocols >= TLS 1.2 only, with forward secrecy (FS) ciphers" and HSTS. Disable caching of sensitive responses. Hash passwords with adaptive salted functions "such as Argon2, yescrypt, scrypt or PBKDF2-HMAC-SHA-512". Use authenticated encryption. | HSTS header present; password hashing library identified; no MD5/SHA-1 on passwords. | Required |
| A05:2025 | Injection (includes XSS) | Keep data separate from commands: safe parameterised APIs or ORMs. Positive server-side input validation. Escape any residual dynamic query. | No string-built SQL or shell commands; schema validation on every request body. | Required |
| A06:2025 | Insecure Design | Secure development lifecycle. Library of secure design patterns. Threat model authentication, access control, business logic and key flows. Unit and integration tests for use-cases and misuse-cases. Segregate tiers and tenants. | `.kickstart/decisions/threat-model.md` exists; misuse-case tests present. | Threat model can be 10 lines |
| A07:2025 | Authentication Failures | MFA where possible. No default credentials. Check new passwords against breached-credential lists; align with NIST SP 800-63B; no forced rotation unless breach suspected. Same response for all login outcomes to prevent enumeration. Limit or delay failed logins and alert. Server-side sessions with a new high-entropy ID after login, never in the URL, invalidated on logout, idle and absolute timeout. Validate JWT `aud`, `iss` and scopes. | Auth provider or vetted library; cookie flags HttpOnly/Secure/SameSite; login rate-limited. | Provider auth is enough |
| A08:2025 | Software or Data Integrity Failures | Verify software and data with digital signatures. Consume only trusted repositories. Review process for code and configuration changes. Segregated, access-controlled CI/CD. Do not accept unsigned or unencrypted serialized data from untrusted clients without an integrity check. | Branch protection on; no unsafe deserialisers (`pickle`, `yaml.load`, Java native) on untrusted input; third-party scripts pinned with SRI. | Lockfile + branch protection |
| A09:2025 | Security Logging & Alerting Failures | Log login, access-control and input-validation failures with user context, retained long enough for delayed forensic analysis. Consumable log format; encode log data. Audit trail with integrity controls such as append-only tables. Alert on suspicious behaviour. Monitoring playbooks and an incident response plan. | Structured logger present; auth events logged; error tracker wired; alert on error spike (scale). | Logger + error tracker |
| A10:2025 | Mishandling of Exceptional Conditions (new) | Catch errors where they occur. Roll back partial transactions. "Always fail closed." Rate limits, resource quotas and throttling everywhere ("Nothing in information technology should be limitless"). Centralised error handling with a global exception handler. | Global error handler; timeouts on external calls; upload and query size limits; auth and payment paths deny on error. | Required |

Log retention periods are not set by OWASP. They come from the laws you select, for example CERT-In in India. See the framework files.

## Minimum automated tests the baseline expects

These are kickstart's minimum, chosen to cover the categories that are cheapest to test.

1. Unauthenticated request to a protected route returns 401 or 403 (A01).
2. User A cannot access user B's object, returning 403 or 404 (A01).
3. A request body with an unexpected field or wrong type is rejected with 400 (A05).
4. Ten failed logins trigger rate limiting (A07).
5. Security headers are present on a GET of `/` (A02).
6. A forced downstream error on a protected route returns an error, not a success (A10).

They take about an hour in any framework.

## Changes from the 2021 edition

OWASP says "There are two new categories and one consolidation in the Top Ten for 2025".

| 2021 | 2025 |
|---|---|
| A01 Broken Access Control | A01 Broken Access Control, now including SSRF |
| A05 Security Misconfiguration | A02 Security Misconfiguration |
| A06 Vulnerable and Outdated Components | A03 Software Supply Chain Failures (wider scope) |
| A02 Cryptographic Failures | A04 Cryptographic Failures |
| A03 Injection | A05 Injection |
| A04 Insecure Design | A06 Insecure Design |
| A07 Identification and Authentication Failures | A07 Authentication Failures |
| A08 Software and Data Integrity Failures | A08 Software or Data Integrity Failures |
| A09 Security Logging and Monitoring Failures | A09 Security Logging & Alerting Failures |
| A10 Server-Side Request Forgery | Merged into A01 |
| (none) | A10 Mishandling of Exceptional Conditions |

Projects checked against 2021 IDs should relabel their checklist rows with this table.
