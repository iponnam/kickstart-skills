---
id: cyber-essentials
name: Cyber Essentials
official_name: Cyber Essentials scheme - Requirements for IT Infrastructure v3.3 (and Cyber Essentials Plus Test Specification v3.2)
governing_body: National Cyber Security Centre (NCSC, UK government); delivered by IASME as the NCSC's Cyber Essentials Delivery Partner through licensed Certification Bodies
type: security
legal_status: certification-scheme
region: United Kingdom
industry: any
current_version: Requirements for IT Infrastructure v3.3, effective 27 April 2026; Cyber Essentials Plus Test Specification v3.2 (28 April 2025)
superseded_by: none
official_sources:
  - title: NCSC, Cyber Essentials overview
    url: https://www.ncsc.gov.uk/cyberessentials/overview
    accessed: 2026-11-06
  - title: NCSC, Cyber Essentials - Help & resources
    url: https://www.ncsc.gov.uk/cyberessentials/resources
    accessed: 2026-11-06
  - title: Cyber Essentials - Requirements for IT Infrastructure v3.3 (PDF, April 2026)
    url: https://www.ncsc.gov.uk/sites/default/files/2026-11/Cyber-Essentials-Requirements-for-IT-Infrastructure-v3-3.pdf
    accessed: 2026-11-06
  - title: Cyber Essentials Plus Test Specification v3.2 (PDF)
    url: https://www.ncsc.gov.uk/sites/default/files/2026-05/cyber-essentials-plus-test-specification-v3-2%20english.pdf
    accessed: 2026-11-06
last_verified: 2026-11-06T00:00:00Z
verification: verified
---

## What it is
"Cyber Essentials is the minimum standard of cyber security recommended by the Government for organisations of all sizes." It was developed by the NCSC, and the certification scheme "is aligned to five technical controls designed to prevent the most common internet based cyber security threats" (NCSC overview). There are two levels: Cyber Essentials (verified self-assessment) and Cyber Essentials Plus (the same controls plus independent technical testing).

## Who it applies to
Voluntary for any organisation. The NCSC notes that "A growing number of organisations require suppliers to be certified to bid for work". Scope is set by the applicant: the whole organisation or a defined sub-set. The v3.3 requirements state that **cloud services cannot be excluded from scope** ("What's new in this version").

## Engineering obligations
| ID | Obligation | Official reference |
|---|---|---|
| FW-1 | "protect every device in scope with a correctly configured firewall (or network device with firewall functionality)" | Req. v3.3 s. E.1 Firewalls |
| FW-2 | Change default admin passwords or disable remote admin. Do not expose the admin interface to the internet unless there is a documented business need and it is protected by MFA or an IP allow list plus managed passwords | Req. v3.3 s. E.1 |
| FW-3 | "block unauthenticated inbound connections by default"; inbound rules approved and documented with the business need; remove unneeded rules | Req. v3.3 s. E.1 |
| SC-1 | Secure configuration: remove unnecessary software and accounts, change default passwords, "disable any auto-run feature which allows file execution without user authorisation" | Req. v3.3 s. E.2 Secure Configuration |
| SC-2 | Device unlock credentials protected against brute force ("no more than 10 guesses in 5 minutes" throttling, or lock "after no more than 10 unsuccessful attempts"); PIN or password of at least 6 characters if used only for unlocking | Req. v3.3 s. E.2 Device unlocking |
| SUM-1 | All in-scope software "licensed and supported"; remove unsupported software or isolate it in a sub-set with no internet traffic; "automatic updates enabled where possible" | Req. v3.3 s. E.3 Security Update Management |
| SUM-2 | Install updates "within 14 days* of release" where they fix vendor-rated "critical" or "high risk" vulnerabilities, CVSS v3 base score 7 or above, or where the vendor gives no severity | Req. v3.3 s. E.3 |
| UAC-1 | Process to create and approve accounts; unique credentials; remove or disable accounts no longer needed | Req. v3.3 s. E.4 User Access Control |
| UAC-2 | "implement MFA, where available - authentication to cloud services must always use MFA" | Req. v3.3 s. E.4 |
| UAC-3 | "use separate accounts to perform administrative activities only (no emailing, web browsing or other standard user activities ...)"; remove special privileges when no longer required | Req. v3.3 s. E.4 |
| UAC-4 | Password element of MFA: "at least 8 characters, with no maximum length restrictions" | Req. v3.3 s. E.4 MFA |
| UAC-5 | Password-only accounts: brute-force protection (MFA, throttling or lockout) and quality control by one of: MFA, a minimum of 12 characters, or a minimum of 8 characters plus a common-password deny list; no forced expiry or complexity rules | Req. v3.3 s. E.4 Password-based authentication |
| MP-1 | Malware protection active on all in-scope devices: anti-malware (updated, prevents execution and connections to malicious sites) or application allow-listing restricted by code signing | Req. v3.3 s. E.5 Malware protection |
| SCOPE-1 | Cloud services (IaaS, PaaS, SaaS), BYOD, home working, third-party accounts and devices are covered by the scope rules; the Software Development section introduces the Software Security Code of Practice | Req. v3.3 s. D Scope; "What's new" |

## Deadlines and numbers
| What | Value | Official reference |
|---|---|---|
| Critical/high security update installation | "within 14 days* of release"; "14 days is considered a reasonable period" | Req. v3.3 s. E.3 |
| "Critical"/"high risk" definition | "CVSS v3 base score of 7 or above, or are identified by the vendor as 'critical or high risk'" | Req. v3.3 s. E.3 |
| Brute-force throttling | "no more than 10 guesses in 5 minutes" / lock "after no more than 10 unsuccessful attempts" | Req. v3.3 s. E.2, E.4 |
| Password length | 12 characters minimum, or 8 with a deny list; MFA password element at least 8 | Req. v3.3 s. E.4 |
| Device-unlock PIN/password | "at least 6 characters" | Req. v3.3 s. E.2 |
| Certification price (CE) | "starting at £320 +VAT", tiered by organisation size; CE Plus "Quoted" | NCSC overview |
| Current requirements effective date | "The current version (v3.3) effective from 27 April 2026" | NCSC Help & resources |

## Assessment and certification
- **Cyber Essentials:** "A combination of self-assessment and independent audit". Self-led route: register via IASME and complete the verified self-assessment, which is "signed-off by a board member or equivalent and then marked by an assessor". Supported route: hire an IASME-licensed Certification Body (NCSC overview).
- **Cyber Essentials Plus:** "The same protections, but with more rigorous, independent technical testing" (NCSC overview). The assessor must verify that the CE Plus scope "matches the scope described by the valid Cyber Essentials self-assessment certificate" before testing (CE Plus Test Spec v3.2). Test cases: remote vulnerability assessment, authenticated patch scan, malware protection, MFA configuration, account separation, on a sample of devices.
- Certificates can be checked on IASME's site (NCSC overview).

## Notes
- **Catalog correction:** framework-catalog.md line 42 and control-checklists.md "Cyber Essentials v3.2" are out of date. The NCSC says the current requirements are **v3.3, effective 27 April 2026**. The CE Plus Test Specification is still v3.2 (28 April 2025). The "Danzell" codename for the April 2026 question set appears in the brief but not on the NCSC pages read (UNVERIFIED). Note that NCSC numbers the April 2026 requirements v3.3, not v3.2.
- control-checklists.md "security update management within 14 days of release" overstates the rule. The 14-day requirement applies to critical/high (CVSS >= 7) or unrated updates; applying all updates within 14 days is "strongly recommend[ed] (but it's not mandatory)". The checklist is also missing "authentication to cloud services must always use MFA" and the separate-admin-accounts rule.
- What's new in v3.3: a definition of cloud services; FIDO2 passkeys counted as passwordless and as MFA; cloud services cannot be excluded from scope; the Software Security Code of Practice; scope no longer refers to "untrusted connections"; more emphasis on backing up data.
- **UNVERIFIED:** certificate validity (commonly 12 months) and the time window between CE and CE Plus were not found on the NCSC pages read. They are IASME scheme rules (iasme.co.uk is unreachable from this sandbox).
