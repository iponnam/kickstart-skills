---
id: nydfs-500
name: NYDFS 23 NYCRR Part 500
official_name: 23 NYCRR Part 500, Cybersecurity Requirements for Financial Services Companies (as amended by the Second Amendment, November 1, 2023)
governing_body: New York State Department of Financial Services (DFS)
type: security
legal_status: binding-regulation
region: US-NY (entities licensed or authorized by DFS, wherever they operate)
industry: finance, insurance (DFS-regulated)
current_version: Part 500 as amended effective November 1, 2023 (UNVERIFIED, official site unreachable)
superseded_by: none
official_sources:
  - title: DFS Cybersecurity Resource Center (attempted)
    url: https://www.dfs.ny.gov/industry_guidance/cybersecurity
    accessed: 2026-11-06
  - title: 23 NYCRR Part 500 Second Amendment (PDF, attempted)
    url: https://www.dfs.ny.gov/system/files/documents/2023/10/rf23_nycrr_part_500_amend02_20231101.pdf
    accessed: 2026-11-06
last_verified: never
verification: unreachable
---

## What it is
UNVERIFIED (official site unreachable; see Notes). Part 500 requires DFS-regulated "covered entities" to maintain a risk-based cybersecurity program and written policies, appoint a CISO, implement specified technical controls, report cybersecurity events to DFS, and certify compliance annually. The Second Amendment (adopted November 1, 2023) added governance duties, Class A company requirements, extortion payment notice, and phased technical requirements.

## Who it applies to
UNVERIFIED. "Covered entity": any person operating or required to operate under a DFS license, registration, charter, certificate, permit, accreditation or similar authorization under the Banking Law, Insurance Law or Financial Services Law (§500.1). Limited exemptions for small entities (§500.19). "Class A companies" (larger entities, by NY revenue and total revenue/employee thresholds) have extra obligations (§500.1, §500.7, §500.14).

## Engineering obligations
All rows UNVERIFIED (from the assignment brief and prior knowledge; not checked against dfs.ny.gov).

| ID | Obligation | Official reference |
|---|---|---|
| 500.2 | Risk-based cybersecurity program; Class A independent audit | §500.2 (UNVERIFIED) |
| 500.3 | Written cybersecurity policies approved at least annually by a senior governing body | §500.3 (UNVERIFIED) |
| 500.4 | CISO; reporting to the senior governing body | §500.4 (UNVERIFIED) |
| 500.5 | Vulnerability management: penetration testing at least annually, automated scans | §500.5 (UNVERIFIED) |
| 500.6 | Audit trail and record retention | §500.6 (UNVERIFIED) |
| 500.7 | Access privileges and management; privileged access review; password policy; Class A PAM | §500.7 (UNVERIFIED) |
| 500.8 | Application security: secure development practices | §500.8 (UNVERIFIED) |
| 500.9 | Periodic risk assessment | §500.9 (UNVERIFIED) |
| 500.11 | Third-party service provider security policy | §500.11 (UNVERIFIED) |
| 500.12 | Multi-factor authentication for any individual accessing any information system (phased to November 2025) | §500.12 (UNVERIFIED) |
| 500.13 | Asset inventory (phased to November 2025); data retention limits | §500.13 (UNVERIFIED) |
| 500.14 | Monitoring and training; Class A EDR and centralized logging | §500.14 (UNVERIFIED) |
| 500.15 | Encryption of nonpublic information in transit and at rest | §500.15 (UNVERIFIED) |
| 500.16 | Incident response and business continuity / disaster recovery plans, tested | §500.16 (UNVERIFIED) |
| 500.17 | Notify DFS of cybersecurity events within 72 hours; extortion payment notice within 24 hours; annual compliance certification | §500.17 (UNVERIFIED) |

## Deadlines and numbers
| What | Value | Official reference |
|---|---|---|
| Notification to regulator | within 72 hours of determining a cybersecurity event occurred (UNVERIFIED) | §500.17(a) (UNVERIFIED) |
| Extortion payment notice | within 24 hours of payment; written description of reasons within 30 days (UNVERIFIED) | §500.17(c) (UNVERIFIED) |
| Annual certification / acknowledgment of noncompliance | by April 15 each year (UNVERIFIED) | §500.17(b) (UNVERIFIED) |
| Phased compliance dates | November 1, 2023 (adoption); April 29, 2024; November 1, 2024; May 1, 2025; November 1, 2025 (final MFA and asset inventory) (UNVERIFIED) | §500.22 (UNVERIFIED) |

## Assessment and certification
UNVERIFIED. Self-certification of compliance (or acknowledgment of noncompliance with remediation plan) signed by the highest-ranking executive and CISO, filed with DFS annually; Class A companies need an independent audit of the program; DFS examinations and enforcement.

## Notes
- verification: unreachable. www.dfs.ny.gov returned a Cloudflare challenge ("Just a moment... Enable JavaScript and cookies") to curl, and headless Chromium could not complete it because challenges.cloudflare.com is refused by this sandbox's proxy. The regulation PDF URL returned the same challenge page. govt.westlaw.com (official NYCRR) and dos.ny.gov (State Register) were refused by the proxy. Every fact in this file is UNVERIFIED and must be checked against dfs.ny.gov before shipping.
- Follow-up pass (2026-11-06): no reachable official copy found. www.dfs.ny.gov remains blocked by its bot protection (not retried), and the other official New York hosts that could carry the text (govt.westlaw.com official NYCRR, dos.ny.gov State Register, ny.gov, nysenate.gov, ag.ny.gov) all failed to connect from this sandbox. The file stays `unreachable`; nothing was changed in the rows above.
- Catalog row "NYDFS 23 NYCRR 500 ... law ... Financial institutions licensed by New York DFS" is directionally correct (it is a binding regulation rather than a statute; scope includes insurance and other DFS licensees). control-checklists.md "NYDFS 72h" matches the commonly cited §500.17(a) window but is UNVERIFIED here.
