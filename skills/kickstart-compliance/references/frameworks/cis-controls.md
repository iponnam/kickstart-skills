---
id: cis-controls
name: CIS Controls
official_name: "CIS Critical Security Controls (CIS Controls) Version 8.1"
governing_body: Center for Internet Security (CIS)
type: security
legal_status: voluntary-standard
region: global
industry: any
current_version: "CIS Controls v8.1 (iterative update to v8; release date UNVERIFIED, see Notes)"
superseded_by: none
official_sources:
  - title: "CIS Critical Security Controls Version 8.1"
    url: https://www.cisecurity.org/controls/v8-1
    accessed: 2026-11-06
  - title: "18 CIS Critical Security Controls (list)"
    url: https://www.cisecurity.org/controls/cis-controls-list
    accessed: 2026-11-06
  - title: "CIS Critical Security Controls Implementation Groups"
    url: https://www.cisecurity.org/controls/implementation-groups
    accessed: 2026-11-06
  - title: "Implementation Group 1 / 2 / 3 pages"
    url: https://www.cisecurity.org/controls/implementation-groups/ig1
    accessed: 2026-11-06
  - title: "CIS Critical Security Controls overview"
    url: https://www.cisecurity.org/controls
    accessed: 2026-11-06
last_verified: 2026-11-06T00:00:00Z
verification: verified
---

## What it is
"The CIS Critical Security Controls (CIS Controls) are a prioritized set of CIS Safeguards to defend against the most prevalent cyber attacks against systems and networks" (v8.1 page). "CIS Controls v8.1 is an iterative update to v8. It includes updated alignment to evolving industry standards and frameworks, revised asset classes and CIS Safeguard descriptions, and the addition of the 'Govern' security function introduced in the ... NIST Cybersecurity Framework (CSF) 2.0" (v8.1 page). They were "Formerly the SANS Critical Security Controls (SANS Top 20)" (controls list).

## Who it applies to
Voluntary; "enterprises of every size" (IG page). "Every enterprise should start with IG1" (IG page). Some US states reference the CIS Controls as a way of demonstrating "reasonable" security (overview page).

Implementation Groups (IG pages):
- IG1: "essential cyber hygiene", "a foundational set of 56 cyber defense Safeguards"; typically small to medium-sized enterprises with limited IT/security expertise.
- IG2: "comprised 74 additional Safeguards and builds upon the 56 Safeguards identified in IG1".
- IG3: "comprised of an additional 23 Safeguards"; "IG3 is comprised of all the Controls and Safeguards".

## Engineering obligations
The 18 Controls (titles and summaries from the official list):

| ID | Obligation | Official reference |
|---|---|---|
| CIS 1 | Inventory and Control of Enterprise Assets: actively manage all assets including cloud; find unauthorised assets | Control 1 |
| CIS 2 | Inventory and Control of Software Assets: only authorised software installed and executes | Control 2 |
| CIS 3 | Data Protection: identify, classify, securely handle, retain and dispose of data | Control 3 |
| CIS 4 | Secure Configuration of Enterprise Assets and Software | Control 4 |
| CIS 5 | Account Management: user, administrator and service accounts | Control 5 |
| CIS 6 | Access Control Management: create, assign, manage and revoke credentials and privileges | Control 6 |
| CIS 7 | Continuous Vulnerability Management: continuously assess, track and remediate vulnerabilities | Control 7 |
| CIS 8 | Audit Log Management: "Collect, alert, review, and retain audit logs" | Control 8 |
| CIS 9 | Email and Web Browser Protections | Control 9 |
| CIS 10 | Malware Defenses | Control 10 |
| CIS 11 | Data Recovery: restore in-scope assets "to a pre-incident and trusted state" | Control 11 |
| CIS 12 | Network Infrastructure Management | Control 12 |
| CIS 13 | Network Monitoring and Defense | Control 13 |
| CIS 14 | Security Awareness and Skills Training | Control 14 |
| CIS 15 | Service Provider Management: evaluate providers holding sensitive data or running critical platforms | Control 15 |
| CIS 16 | Application Software Security: manage the security life cycle of in-house developed, hosted or acquired software | Control 16 |
| CIS 17 | Incident Response Management: policies, plans, procedures, roles, training, communications | Control 17 |
| CIS 18 | Penetration Testing | Control 18 |

Individual Safeguard numbers (e.g. 16.1) and their IG assignment are in the downloadable v8.1 PDF/Excel (registration form), not read here.

## Deadlines and numbers
| What | Value | Official reference |
|---|---|---|
| Number of Controls | 18 ("18 CIS Critical Security Controls") | Controls list |
| Total Safeguards | "There is a total of 153 Safeguards in CIS Controls v8 and v8.1" | IG page |
| IG1 Safeguards | "56" | IG1 page |
| IG2 Safeguards | "74 additional" (130 cumulative) | IG2 page |
| IG3 Safeguards | "an additional 23" (153 cumulative) | IG3 page |

## Assessment and certification
No CIS certification of organisations. Self-assessment (e.g. CIS-CAT, CIS CSAT tools). "CIS Controls Accreditation offers CIS SecureSuite® Members a way to demonstrate their ability to provide CIS Controls implementation, auditing, and/or assessment for their customers" (overview page): it accredits service providers, not end organisations.

## Notes
- `framework-catalog.md` says "CIS Controls v8"; current is v8.1 (same 18 Controls and 153 Safeguards; v8.1 adds the Govern function, revised asset classes and Safeguard descriptions). Update the version.
- Safeguard-level text and per-Safeguard IG assignment not verified (download behind a form).
- UNVERIFIED: the v8.1 release date (not shown on the pages read; widely reported as June 2024). No v9 is published (cisecurity.org/controls/v9 returns 404 on 2026-11-06).
