# OWASP Top 10 (2021 edition, with 2025 candidate notes) as engineering controls

Mandatory for every kickstart project. Each row is one control the checklist tracks. "How to verify" is what the audit or reviewer checks.

| ID | Category | Control (what to implement) | How to verify | Pet projects |
|---|---|---|---|---|
| A01 | Broken Access Control | Every non-public route checks authentication and authorisation server-side. Deny by default. Object-level checks (user can only read/write their own records). No IDs guessable from the client that grant access. CORS allow-list, not `*`. | Grep routes/handlers for a shared auth middleware; test that user A cannot read user B's record (one automated test). | Required |
| A02 | Cryptographic Failures | TLS everywhere (HSTS on). Passwords hashed with bcrypt/argon2/scrypt, never MD5/SHA-1. Secrets in env or secret manager, never in code. Sensitive fields encrypted at rest where the law requires. No custom crypto. | Secret scanner clean; hashing library present; HSTS header present; no `md5(`/`sha1(` on passwords. | Required |
| A03 | Injection | Parameterised queries or ORM for SQL. Output encoding for HTML (framework default). Validate all input at the boundary with a schema (zod, pydantic, joi, struct tags…). No shell commands built from user input. | Grep for string-concatenated SQL and `exec(`/`system(` with variables; schema validation present on every request body. | Required |
| A04 | Insecure Design | Threat model written for auth, payments, file upload and admin. Rate limits on login, signup, password reset, and expensive endpoints. Business-logic abuse cases listed as tests. | `.kickstart/decisions/threat-model.md` exists; rate-limit middleware present. | Threat model can be 10 lines |
| A05 | Security Misconfiguration | Security headers set (CSP, X-Content-Type-Options, X-Frame-Options or frame-ancestors, Referrer-Policy, Permissions-Policy). Debug mode off in prod. Default credentials removed. Stack traces not shown to users. Directory listing off. Cloud storage buckets private by default. | Header check against the running app; `DEBUG`/`NODE_ENV` wired to env. | Required |
| A06 | Vulnerable and Outdated Components | Dependency lockfile committed. Automated vulnerability scan in CI (`npm audit`, `pip-audit`, `cargo audit`, `govulncheck`, `osv-scanner`, Dependabot/Renovate). Critical and high findings fixed before release. SBOM generated at release for `scale`. | Lockfile exists; CI job present; last scan has 0 critical. | Scan required; SBOM planned |
| A07 | Identification and Authentication Failures | Use a vetted auth library or provider. MFA available for `scale`. Session tokens rotated on login, invalidated on logout, HttpOnly + Secure + SameSite cookies. Password policy: length over complexity, breached-password check for `scale`. Brute-force protection. | Auth provider or library identified; cookie flags visible; login rate-limited. | Provider auth is enough |
| A08 | Software and Data Integrity Failures | CI pulls dependencies from lockfile with integrity hashes. Signed commits or protected branches for `scale`. No deserialisation of untrusted data with unsafe loaders (`pickle`, `yaml.load`, Java native). Third-party scripts pinned with SRI or self-hosted. | Lockfile integrity fields; grep for unsafe deserialisers; branch protection on. | Lockfile required |
| A09 | Security Logging and Monitoring Failures | Structured logs (JSON) with request ID. Auth events (login success/fail, password change, privilege change) logged. No secrets or full PII in logs. Errors reported to a tracker (Sentry or equivalent). Alerts on error-rate spike for `scale`. Log retention per compliance (for example 180 days for CERT-In). | Logger present; auth events logged; error tracker DSN wired. | Logger + error tracker |
| A10 | Server-Side Request Forgery | Any server-side fetch of a user-supplied URL validates scheme and host against an allow-list, blocks private IP ranges and metadata endpoints (169.254.169.254), and disables redirects or re-validates after each hop. | Grep for fetch/requests with user-controlled URLs; allow-list helper present. | Required if feature exists |

## 2025 candidate additions (track as planned for `scale`)

| ID | Category | Control |
|---|---|---|
| A11* | Supply Chain Failures | Pin GitHub Actions and container base images by digest. Review new dependencies' maintainers and download counts before adding. Build reproducibly. |
| A12* | Mishandling of Exceptional Conditions | Fail closed: errors in auth or payment paths deny, never allow. Timeouts and retries with limits on every external call. Resource limits on uploads and queries. |

## Minimum automated tests the baseline expects

1. Unauthenticated request to a protected route returns 401/403.
2. User A cannot access user B's object (returns 403/404).
3. A request body with an unexpected field or wrong type is rejected (400).
4. Login with wrong password 10 times triggers rate limiting.
5. Security headers are present on a GET of `/`.

These five tests take under an hour in any framework and cover A01, A03, A04, A05 and A07.
