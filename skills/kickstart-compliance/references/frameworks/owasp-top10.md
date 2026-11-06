---
id: owasp-top10
name: OWASP Top 10
official_name: "OWASP Top 10:2025 - The Ten Most Critical Web Application Security Risks"
governing_body: OWASP Foundation (OWASP Top 10 flagship project)
type: security
legal_status: voluntary-standard
region: global
industry: any
current_version: "OWASP Top 10:2025 (8th installment); release date UNVERIFIED (see Notes)"
superseded_by: none
official_sources:
  - title: OWASP Top 10 project page (owasp.org)
    url: https://owasp.org/www-project-top-ten/
    accessed: 2026-11-06
  - title: OWASP Top 10:2025 index (official OWASP/Top10 repository, source of top10.owasp.org)
    url: https://raw.githubusercontent.com/OWASP/Top10/master/2025/docs/en/index.md
    accessed: 2026-11-06
  - title: OWASP Top 10:2025 Introduction ("What's changed in the Top 10 for 2025")
    url: https://raw.githubusercontent.com/OWASP/Top10/master/2025/docs/en/0x00_2025-Introduction.md
    accessed: 2026-11-06
  - title: OWASP Top 10:2025 category pages A01-A10 ("How to prevent" sections)
    url: https://raw.githubusercontent.com/OWASP/Top10/master/2025/docs/en/
    accessed: 2026-11-06
last_verified: 2026-11-06T00:00:00Z
verification: partial
---

## What it is
The OWASP Top 10 is "a standard awareness document for developers and web application security" that "represents a broad consensus about the most critical security risks to web applications" (owasp.org project page). The project page states: "The most current released version is the OWASP Top 10 2025. Previous versions are available at OWASP Top 10 2021 and OWASP Top 10 2017". The 2025 edition is described as "the 8th installment of the OWASP Top Ten" and is "data-informed, but not blindly data-driven": 12 categories were ranked from contributed data and two were promoted from a community survey (Introduction, Methodology).

## Who it applies to
No legal scope. OWASP says "Companies should adopt this document and start the process of ensuring that their web applications minimize these risks" (project page). It is an awareness document, not a certifiable standard; for verifiable requirements OWASP points to ASVS (not covered here).

Official category list (Top 10:2025, from the official index):

| ID | Category | Change vs 2021 (Introduction) |
|---|---|---|
| A01:2025 | Broken Access Control | Stays #1; "Server-Side Request Forgery (SSRF) has been rolled into this category" (was A10:2021) |
| A02:2025 | Security Misconfiguration | "moved up from #5 in 2021 to #2 in 2025" |
| A03:2025 | Software Supply Chain Failures | New name/scope: "an expansion of A06:2021-Vulnerable and Outdated Components" to dependencies, build systems and distribution infrastructure |
| A04:2025 | Cryptographic Failures | "falls two spots from #2 to #4" |
| A05:2025 | Injection | "falls two spots from #3 to #5" (includes XSS) |
| A06:2025 | Insecure Design | "slides two spots from #4 to #6" |
| A07:2025 | Authentication Failures | Stays #7; renamed from "Identification and Authentication Failures" |
| A08:2025 | Software or Data Integrity Failures | "continues at #8" (2021 name: Software and Data Integrity Failures) |
| A09:2025 | Security Logging & Alerting Failures | Stays #9; renamed from "Security Logging and Monitoring Failures" |
| A10:2025 | Mishandling of Exceptional Conditions | "a new category for 2025" (24 CWEs) |

Summary from OWASP: "There are two new categories and one consolidation in the Top Ten for 2025" (new: A03 Software Supply Chain Failures, A10 Mishandling of Exceptional Conditions; consolidation: SSRF into A01).

## Engineering obligations
Each row paraphrases the "How to prevent" section of the cited 2025 category page.

| ID | Obligation | Official reference |
|---|---|---|
| A01-01 | Enforce access control in trusted server-side code; "Except for public resources, deny by default"; implement once and reuse; minimise CORS | A01:2025 How to prevent |
| A01-02 | Enforce record ownership in models; disable directory listing; keep .git/backup files out of web roots | A01:2025 How to prevent |
| A01-03 | Log access-control failures and alert; rate-limit API/controller access; invalidate server sessions at logout; keep stateless JWTs short-lived; include access control in unit/integration tests | A01:2025 How to prevent |
| A02-01 | Repeatable hardening process; dev/QA/prod configured identically with different credentials; minimal platform without unused features | A02:2025 How to prevent |
| A02-02 | Segmented architecture between components/tenants; send security headers; automated verification of configuration in all environments (manual verification "annually at a minimum" if not automated) | A02:2025 How to prevent |
| A02-03 | Use identity federation, short-lived credentials or platform roles "instead of embedding static keys or secrets in code, configuration files, or pipelines" | A02:2025 How to prevent |
| A03-01 | "Centrally generate and manage the Software Bill of Materials (SBOM)"; track transitive dependencies; remove unused dependencies | A03:2025 How to prevent |
| A03-02 | Continuously inventory component versions and monitor CVE/NVD/OSV; use software composition analysis; obtain components from official sources, prefer signed packages | A03:2025 How to prevent |
| A03-03 | Update CI/CD and developer tooling; staged/canary rollouts; change-track CI/CD settings and code repositories | A03:2025 How to prevent |
| A04-01 | Classify data; encrypt sensitive data at rest; don't store sensitive data unnecessarily (tokenise/truncate) | A04:2025 How to prevent |
| A04-02 | Encrypt in transit with "protocols >= TLS 1.2 only, with forward secrecy (FS) ciphers"; enforce HSTS; disable caching of sensitive responses | A04:2025 How to prevent |
| A04-03 | Hash passwords with adaptive salted functions "such as Argon2, yescrypt, scrypt or PBKDF2-HMAC-SHA-512"; use authenticated encryption; keys in HSM where most sensitive | A04:2025 How to prevent |
| A05-01 | Keep data separate from commands: safe/parameterised APIs or ORMs; positive server-side input validation; escape residual dynamic queries | A05:2025 How to prevent |
| A06-01 | Secure development lifecycle; secure design pattern library; threat model authentication, access control, business logic and key flows | A06:2025 How to prevent |
| A06-02 | Unit/integration tests for use-cases and misuse-cases per tier; segregate tiers and tenants | A06:2025 How to prevent |
| A07-01 | Implement MFA where possible; no default credentials; check new passwords against worst-password and breached-credential lists; align with NIST 800-63b; no forced rotation unless breach suspected | A07:2025 How to prevent |
| A07-02 | Same message for all outcomes to prevent account enumeration; limit/delay failed logins and alert; server-side session manager issuing new high-entropy ID after login, not in URL, invalidated on logout/idle/absolute timeout; validate JWT `aud`/`iss` and scopes | A07:2025 How to prevent |
| A08-01 | Verify software/data with digital signatures; consume only trusted repositories; review process for code and config changes; segregated, access-controlled CI/CD | A08:2025 How to prevent |
| A08-02 | Do not use unsigned/unencrypted serialized data from untrusted clients without integrity check | A08:2025 How to prevent |
| A09-01 | Log login, access-control and input-validation failures with user context, retained long enough for delayed forensics; log every security control success/failure; consumable log format; encode log data | A09:2025 How to prevent |
| A09-02 | Audit trail with integrity controls (e.g. append-only tables); alert on suspicious behaviour; monitoring/alerting playbooks; incident response plan (e.g. NIST 800-61r2 or later) | A09:2025 How to prevent |
| A10-01 | Catch errors where they occur; roll back partial transactions; "Always fail closed" | A10:2025 How to prevent; A09:2025 |
| A10-02 | Rate limiting, resource quotas and throttling everywhere ("Nothing in information technology should be limitless"); centralised error handling, logging, monitoring and a global exception handler | A10:2025 How to prevent |

## Deadlines and numbers
| What | Value | Official reference |
|---|---|---|
| Edition count | "the 8th installment of the OWASP Top Ten" | Introduction |
| CWEs analysed | "589 CWEs in this edition" (vs "almost 400 CWEs in 2021") | Introduction, How the categories are structured |
| Categories ranked from data / from survey | "We ranked 12 categories based on the data contributed, and allowed two to be promoted or highlighted by responses from the community survey" | Introduction, Methodology |
| A01 incidence | "3.73% of applications tested had one or more of the 40 Common Weakness Enumerations (CWEs)" | Introduction |
| Minimum manual config verification | "manually verified annually at a minimum" (if not automated) | A02:2025 How to prevent |
| Minimum TLS | "protocols >= TLS 1.2 only" | A04:2025 How to prevent |

## Assessment and certification
None. OWASP does not certify or attest Top 10 compliance; the Top 10 is an awareness document. Organisations self-assess (code review, SAST/DAST, pen testing). OWASP ASVS is OWASP's verifiable requirements standard (not researched here).

## Notes
- Corrections to `references/owasp-top10.md`: (1) title "2021 edition, with 2025 candidate notes" is outdated; the owasp.org project page says "The most current released version is the OWASP Top 10 2025". (2) The 2021 ordering/IDs are used throughout; 2025 IDs differ (A02 is now Security Misconfiguration, A03 Software Supply Chain Failures, A04 Cryptographic Failures, A05 Injection, A06 Insecure Design). (3) A07 name is now "Authentication Failures"; A08 is "Software or Data Integrity Failures"; A09 is "Security Logging & Alerting Failures". (4) "A10 Server-Side Request Forgery" no longer exists as a category; SSRF was rolled into A01:2025. (5) The "2025 candidate additions" A11*/A12* do not exist: Software Supply Chain Failures is A03:2025 (replacing A06:2021 Vulnerable and Outdated Components) and Mishandling of Exceptional Conditions is A10:2025. There are exactly ten categories. (6) The file says A06 should run `npm audit` etc.; that content belongs under A03:2025. (7) "Log retention per compliance (for example 180 days for CERT-In)" is not an OWASP requirement; OWASP only says logs should be "held for enough time to allow delayed forensic analysis".
- Corrections to `framework-catalog.md`: no OWASP-specific errors found other than implicit 2021 references.
- UNVERIFIED: the exact publication date of the final 2025 edition. top10.owasp.org (where the 2025 edition is hosted; owasp.org/Top10/2025/ redirects there) was blocked by the sandbox proxy, and the GitHub API for commit dates was not available. The release-candidate vs final status was verified via the owasp.org project page ("most current released version", "Latest Version 2025") and the official repository index ("Welcome to the OWASP Top 10:2025 Release").
- verification is `partial` only because of the release date; category list, names and changes are verified from official OWASP sources.
