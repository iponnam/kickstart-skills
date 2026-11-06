---
id: glba
name: GLBA Safeguards Rule
official_name: Standards for Safeguarding Customer Information (FTC Safeguards Rule), 16 CFR Part 314, implementing sections 501 and 505(b)(2) of the Gramm-Leach-Bliley Act
governing_body: Federal Trade Commission (FTC)
type: security
legal_status: binding-regulation
region: US
industry: finance (non-bank financial institutions under FTC jurisdiction, e.g. lenders, mortgage brokers, tax preparers, payment and fintech firms engaged in financial activities)
current_version: 16 CFR Part 314 as amended 86 FR 70304 (Dec. 9, 2021) and 88 FR 77509 (Nov. 13, 2023); FTC notification requirement §314.4(j) effective May 13, 2024
superseded_by: none
official_sources:
  - title: 16 CFR Part 314 Standards for Safeguarding Customer Information (eCFR)
    url: https://www.ecfr.gov/current/title-16/chapter-I/subchapter-C/part-314
    accessed: 2026-11-06
  - title: eCFR versioner, version history for 16 CFR Part 314
    url: https://www.ecfr.gov/api/versioner/v1/versions/title-16.json?part=314
    accessed: 2026-11-06
  - title: eCFR point-in-time text, 16 CFR 314.5 as of 2022-11-23 (87 FR 71510)
    url: https://www.ecfr.gov/api/versioner/v1/full/2022-11-23/title-16.xml?section=314.5
    accessed: 2026-11-06
  - title: eCFR point-in-time text, 16 CFR 314.5 as of 2024-05-13 (88 FR 77509)
    url: https://www.ecfr.gov/api/versioner/v1/full/2024-05-13/title-16.xml?section=314.5
    accessed: 2026-11-06
last_verified: 2026-11-06T00:00:00Z
verification: verified
---

## What it is
Part 314 "sets forth standards for developing, implementing, and maintaining reasonable administrative, technical, and physical safeguards to protect the security, confidentiality, and integrity of customer information" (§314.1(a)). It requires a written information security program with specific elements (§314.3, §314.4).

## Who it applies to
"All financial institutions over which the Federal Trade Commission ... has jurisdiction", i.e. entities engaging in activities "financial in nature or incidental to such financial activities" under 12 U.S.C. 1843(k) (§314.1(b)). Banks and other institutions supervised by federal banking agencies follow the Interagency Guidelines instead (not covered here). Small-institution exception: §314.4(b)(1) (written risk assessment), (d)(2) (pen testing/vulnerability assessment), (h) (written incident response plan) and (i) (board reporting) "do not apply to financial institutions that maintain customer information concerning fewer than five thousand consumers" (§314.6).

## Engineering obligations
| ID | Obligation | Official reference |
|---|---|---|
| 314.4(a) | Designate a Qualified Individual to oversee and enforce the program | §314.4(a) |
| 314.4(b)(1) | Written risk assessment with criteria for risk categorization, CIA assessment, and mitigation/acceptance | §314.4(b)(1) |
| 314.4(c)(1) | Access controls: authenticate users; limit access to information needed for duties (customers to their own data) | §314.4(c)(1) |
| 314.4(c)(2) | Inventory and manage data, personnel, devices, systems and facilities | §314.4(c)(2) |
| 314.4(c)(3) | "Protect by encryption all customer information held or transmitted by you both in transit over external networks and at rest"; compensating controls only if encryption infeasible and approved by the Qualified Individual | §314.4(c)(3) |
| 314.4(c)(4) | Secure development practices for in-house apps; evaluate security of externally developed apps | §314.4(c)(4) |
| 314.4(c)(5) | "Implement multi-factor authentication for any individual accessing any information system", unless the Qualified Individual approves equivalent controls in writing | §314.4(c)(5) |
| 314.4(c)(6) | Secure disposal no later than two years after last use (with exceptions); periodically review data retention policy | §314.4(c)(6) |
| 314.4(c)(7) | Change management procedures | §314.4(c)(7) |
| 314.4(c)(8) | Monitor and log activity of authorized users; detect unauthorized access, use or tampering | §314.4(c)(8) |
| 314.4(d)(2) | Continuous monitoring, or annual penetration testing and vulnerability assessments at least every six months | §314.4(d)(2) |
| 314.4(e) | Security awareness training; qualified security personnel | §314.4(e) |
| 314.4(f) | Oversee service providers: select capable providers, require safeguards by contract, assess periodically | §314.4(f) |
| 314.4(h) | Written incident response plan (goals, processes, roles, communications, remediation, documentation, post-event review) | §314.4(h) |
| 314.4(i) | Qualified Individual reports in writing at least annually to the board | §314.4(i) |
| 314.4(j) | Notify the FTC of notification events affecting 500 or more consumers | §314.4(j) |

## Deadlines and numbers
| What | Value | Official reference |
|---|---|---|
| Notification to regulator (FTC) | "if the notification event involves the information of at least 500 consumers, you must notify the Federal Trade Commission as soon as possible, and no later than 30 days after discovery of the event" | §314.4(j)(1) |
| Notification event | "acquisition of unencrypted customer information without the authorization of the individual"; information is unencrypted if the key was accessed | §314.2(m) |
| Discovery | "treated as discovered as of the first day on which such event is known to you" | §314.4(j)(2) |
| Effective date of FTC notification | "Section 314.4(j) is effective as of May 13, 2024" | §314.5 |
| Penetration testing | "Annual penetration testing" | §314.4(d)(2)(i) |
| Vulnerability assessments | "at least every six months" | §314.4(d)(2)(ii) |
| Board report | "regularly and at least annually" | §314.4(i) |
| Disposal of customer information | "no later than two years after the last date the information is used" (subject to exceptions) | §314.4(c)(6)(i) |
| Small-institution exception | "fewer than five thousand consumers" | §314.6 |

## Assessment and certification
No certification or mandated external audit. The FTC enforces through investigations and orders. Compliance is self-assessed through the risk assessment, testing and annual board report.

## Notes
- control-checklists.md GLBA row says "notice to FTC of breaches affecting 500+". Correction: the trigger is a "notification event" (unauthorized acquisition of unencrypted customer information) involving "at least 500 consumers", notified "no later than 30 days after discovery"; add the 30-day deadline and the May 13, 2024 effective date. Also add annual pen test, 6-monthly vulnerability assessment, 2-year disposal rule, and the under-5,000-consumers exception.
- Catalog row "GLBA ... privacy, security ... law" is fine at Act level; note that the engineering-relevant part is the FTC Safeguards Rule (16 CFR 314) for non-bank financial institutions. The GLBA Privacy Rule (Regulation P, 12 CFR 1016, CFPB) was not reviewed here.
- **Compliance date for the 2021 amendments confirmed (follow-up pass):** the eCFR point-in-time text of §314.5 from 2022-11-23 reads "Sections 314.4(a), (b)(1), (c)(1) through (8), (d)(2), (e), (f)(3), (h), and (i) are effective as of June 9, 2023. [87 FR 71510, Nov. 23, 2022]". From 2024-05-13 §314.5 was replaced by "Section 314.4(j) is effective as of May 13, 2024. [88 FR 77509, Nov. 13, 2023]". eCFR version history for Part 314: 2021-12-09 and 2022-01-07 (86 FR 70304 amendments), 2022-11-23 (§314.5 only), 2023-11-13 and 2024-05-13 (§§314.2, 314.4, 314.5); no later change. ftc.gov guidance remains blocked but is not needed for the rule text.
