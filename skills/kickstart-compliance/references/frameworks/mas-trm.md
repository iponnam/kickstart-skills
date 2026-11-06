---
id: mas-trm
name: MAS TRM Guidelines + Notices on TRM and Cyber Hygiene
official_name: Guidelines on Risk Management Practices - Technology Risk (Technology Risk Management Guidelines, January 2021); MAS Notice FSM-N05 Technology Risk Management; MAS Notice FSM-N06 Cyber Hygiene (and equivalent sector notices)
governing_body: Monetary Authority of Singapore (MAS)
type: security
legal_status: binding-regulation
region: Singapore
industry: finance (banks, insurers, capital markets intermediaries, payment service providers, trust companies, other MAS-regulated FIs)
current_version: TRM Guidelines published 18 January 2021; Notices FSM-N05 and FSM-N06 issued 9 May 2024, effective 10 May 2024
superseded_by: none (Notices 644, 127, 506, 830, 912, 644A, PSN05 on TRM and Notice 655 on Cyber Hygiene were cancelled with effect from 10 May 2024 and replaced by FSMA notices)
official_sources:
  - title: Guidelines on Risk Management Practices - Technology Risk (page, lists related notices)
    url: https://www.mas.gov.sg/regulation/guidelines/technology-risk-management-guidelines
    accessed: 2026-11-06
  - title: Technology Risk Management Guidelines (January 2021) PDF
    url: https://www.mas.gov.sg/-/media/mas/regulations-and-financial-stability/regulatory-and-supervisory-framework/risk-management/trm-guidelines-18-january-2021.pdf
    accessed: 2026-11-06
  - title: MAS Notice FSM-N05 Notice on Technology Risk Management (banks)
    url: https://www.mas.gov.sg/-/media/mas-media-library/regulation/notices/trpd/notice-fsm-n05/mas-notice-fsm-n05.pdf?sc_lang=en
    accessed: 2026-11-06
  - title: MAS Notice FSM-N06 Cyber Hygiene
    url: https://www.mas.gov.sg/-/media/mas-media-library/regulation/notices/trpd/notice-fsm-n06/mas-notice-fsm-n06.pdf?sc_lang=en
    accessed: 2026-11-06
  - title: Notice 655 Cyber Hygiene [Cancelled]
    url: https://www.mas.gov.sg/regulation/notices/notice-655
    accessed: 2026-11-06
last_verified: 2026-11-06T00:00:00Z
verification: verified
---

## What it is
The TRM Guidelines are MAS's "risk management principles and best practice standards to guide financial institutions in managing technology risk" across governance, security-by-design, software development, IT service management, resilience, access control, cryptography, data and infrastructure security, cyber operations, cyber assessment and online financial services. They are non-statutory guidance; supervision considers "the degree of observance with the spirit of the Guidelines" (TRM 2.2). The legally binding requirements (1-hour incident notification, 4-hour RTO, cyber hygiene) sit in the Notices.

## Who it applies to
- TRM Guidelines: all FIs regulated by MAS (page lists banking, insurance, capital markets, payments and other licence types); implementation "commensurate with the level of risk and complexity" (TRM 2.2).
- FSM-N05: issued under s.29(1) of the Financial Services and Markets Act 2022, "applies to all banks in Singapore" (para 1). Equivalent TRM notices exist for other FI types (e.g. insurers, CMS licensees, payment institutions); only the bank notice was read.
- FSM-N06: applies to "relevant entities" (banks in Singapore for FSM-N06; sector equivalents for others).

## Engineering obligations
| ID | Obligation | Official reference |
|---|---|---|
| MAS-01 | Framework and process to identify critical systems | FSM-N05 para 4 |
| MAS-02 | High availability: maximum unscheduled downtime per critical system "does not exceed a total of 4 hours within any period of 12 months" | FSM-N05 para 5 |
| MAS-03 | RTO "of not more than 4 hours for each critical system"; validate and document recovery testing "at least once every 12 months" | FSM-N05 para 6 |
| MAS-04 | Notify MAS "as soon as possible, but not later than 1 hour, upon the discovery of a relevant incident" | FSM-N05 para 7 |
| MAS-05 | Root cause and impact analysis report within 14 days (executive summary, root cause, impact on compliance/operations/customers, remediation) | FSM-N05 para 8 |
| MAS-06 | IT controls to protect customer information from unauthorised access or disclosure | FSM-N05 para 9 |
| MAS-07 | Secure every administrative account on OS, database, application, security appliance or network device | FSM-N06 para 4.1 |
| MAS-08 | Apply security patches within a timeframe commensurate with risk; compensating controls where no patch exists | FSM-N06 para 4.2 |
| MAS-09 | Written security standards for every system; conformance or compensating controls | FSM-N06 para 4.3 |
| MAS-10 | Network perimeter controls restricting all unauthorised traffic | FSM-N06 para 4.4 |
| MAS-11 | Malware protection on every system where available | FSM-N06 para 4.5 |
| MAS-12 | MFA for all admin accounts on critical systems and all accounts on systems used to access customer information through the internet | FSM-N06 para 4.6 |
| MAS-13 | Patch management process; test patches before applying | TRM 7.4 |
| MAS-14 | Systems' RTO and RPO established; resilience and recovery testing | TRM 8.2 |
| MAS-15 | Strong password policy; MFA for users with access to sensitive system functions; periodic user access reviews | TRM 9.1.4-9.1.6 |
| MAS-16 | Cryptography, data and infrastructure security, cyber security operations | TRM 10-12 |
| MAS-17 | Penetration testing of internet-facing systems "at least once annually or whenever these systems undergo major changes"; scenario-based cyber exercises; red teaming | TRM 13.2-13.4 |
| MAS-18 | Online financial services: mobile app security (Annex C), distribute apps only via official stores or secure channels, address rooted/jailbroken devices | TRM 14.1.4-14.1.7; Annex C |
| MAS-19 | Security awareness training "at least annually for all staff" | TRM 3.6.2 |

## Deadlines and numbers
| What | Value | Official reference |
|---|---|---|
| Incident notification to MAS | "as soon as possible, but not later than 1 hour, upon the discovery of a relevant incident" | FSM-N05 para 7 |
| Root cause and impact report | "within 14 days or such longer period as the Authority may allow, from the discovery" | FSM-N05 para 8 |
| Critical system unscheduled downtime | "a total of 4 hours within any period of 12 months" | FSM-N05 para 5 |
| RTO | "not more than 4 hours for each critical system" | FSM-N05 para 6 |
| Recovery test validation | "at least once every 12 months" | FSM-N05 para 6 |
| Penetration testing (internet-facing) | "at least once annually" or on major change | TRM 13.2 |
| Effective date of notices | "take effect on 10 May 2024" | FSM-N05 para 10; FSM-N06 para 5.1 |

## Assessment and certification
No certification. MAS supervises compliance with the Notices (breach is an offence under the relevant Act) and considers observance of the Guidelines in supervision (TRM 2.2). Independent audits, PT and red teaming are expected under TRM Section 13.

## Notes
- Catalog row "MAS TRM 2021 ... law": the Guidelines themselves are non-binding guidance; the binding rules are the Notices (FSM-N05 / FSM-N06 for banks and sector equivalents). The previous notice numbers (644, 655, etc.) were cancelled from 10 May 2024.
- Checklist "MAS 1h for critical": the 1-hour rule is in the Notice on Technology Risk Management (FSM-N05 para 7 for banks), triggered by a "relevant incident" (system malfunction or IT security incident with severe and widespread impact on operations or material impact on service to customers), measured from discovery, not occurrence. A 14-day RCA report follows.
- Checklist omits the binding 4-hour RTO and 4-hour/12-month downtime limit for critical systems.
- Pending: a 2026 MAS consultation paper on proposed amendments to the Notices on Technology Risk Management exists on mas.gov.sg; its content and status were not fetched (UNVERIFIED).
