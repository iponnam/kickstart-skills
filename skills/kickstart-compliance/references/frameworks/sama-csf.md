---
id: sama-csf
name: SAMA CSF
official_name: SAMA Cyber Security Framework (Circular No. 381000091275, 28/8/1438H, 24/5/2017G)
governing_body: Saudi Central Bank (SAMA), IT Risk Supervision / Deputyship of Supervision
type: security
legal_status: binding-regulation
region: Saudi Arabia
industry: finance (banks, insurance/reinsurance, financing companies, credit bureaus, financial market infrastructure; rulebook scope also lists payment systems/PSPs and regulatory sandbox)
current_version: Version 1.0, issued 24 May 2017 (Circular 381000091275); rulebook status "In-Force"
superseded_by: none
official_sources:
  - title: SAMA Rulebook - Cyber Security Framework (full text)
    url: https://rulebook.sama.gov.sa/en/cyber-security-framework-2
    accessed: 2026-11-06
  - title: SAMA Rulebook - Cyber Security Framework (Finance Sector circular with implementation steps)
    url: https://rulebook.sama.gov.sa/en/cyber-security-framework-0
    accessed: 2026-11-06
last_verified: 2026-11-06T00:00:00Z
verification: verified
---

## What it is
SAMA's principle-based cyber security framework for its regulated "Member Organizations". It defines four domains with subdomains, each stating a principle, objective and control considerations, plus a 0-5 maturity model; member organizations must reach at least maturity level 3. It is based on SAMA requirements and industry standards "such as NIST, ISF, ISO, BASEL and PCI" and supersedes earlier SAMA cyber security circulars (s.1.1).

## Who it applies to
s.1.4: "All Banks operating in Saudi Arabia; All Insurance and/or Reinsurance Companies...; All Financing Companies...; All Credit Bureaus...; The Financial Market Infrastructure". All domains apply to banks; other financial institutions are exempt from 3.2.3 (but must apply PCI DSS / SWIFT CSCF if they handle cardholder data or SWIFT), 3.3.12 and 3.3.13 (but must implement MFA if they provide online customer services). Scope covers electronic and physical information, applications, devices, ATMs, storage, premises and third-party-held assets (s.1.3). The rulebook page lists scope as "Banking Sector—Finance Sector—Payment Systems and Payment Services Providers—Credit Bureaus—Regulatory Sandbox".

## Engineering obligations
| ID | Obligation | Official reference |
|---|---|---|
| 3.1.1 | Cyber security function independent of IT, separate reporting lines, reporting to CEO/MD or control-function GM; cyber security committee | 3.1.1 (control considerations 6, 7) |
| 3.1.3 | Approved cyber security policy, periodically reviewed; requires that breaches and suspected weaknesses are reported | 3.1.3 |
| 3.1.5 | Cyber security integrated into project management; independent cyber security review of projects | 3.1.5 |
| 3.2.1 | Cyber security risk management: identification, analysis, response, monitoring; risk assessment when launching new products and technologies | 3.2.1, 3.2.1.1-3.2.1.4 |
| 3.2.3 | Comply with (inter)national standards incl. PCI DSS and SWIFT CSCF where applicable | 3.2.3, 1.4 |
| 3.2.4 | "Customer and internet facing services should be subject to annual review and penetration tests"; record and follow up results | 3.2.4 (2)-(5) |
| 3.2.5 | Independent cyber security audits per generally accepted auditing standards | 3.2.5 |
| 3.3.3 | Accurate, up-to-date information asset inventory | 3.3.3 |
| 3.3.4 | Defined and periodically reviewed cyber security architecture | 3.3.4 |
| 3.3.5 | IAM policy: need-to-know, joiner/mover/leaver driven by HR, periodic access reviews, audit trail of access requests, automation, privileged and remote account review | 3.3.5 (4)(a)-(d) |
| 3.3.6 | Application development follows an approved secure SDLC; define events to monitor and retain | 3.3.6 (4) |
| 3.3.7 | Change management incl. code review (internal and external apps) or independent assurance statement; post-implementation review | 3.3.7 |
| 3.3.8 | Infrastructure security incl. DLP, remote maintenance, periodic compliance review | 3.3.8 |
| 3.3.9 | Cryptographic standard: approved solutions, when to apply, key lifecycle management | 3.3.9 (4) |
| 3.3.10 | BYOD controls | 3.3.10 |
| 3.3.11 | Secure disposal of information assets | 3.3.11 |
| 3.3.13 | Electronic banking: MFA at customer registration and for all e-banking services; MFA activation via different channels; SMS notification on new MFA mechanism | 3.3.13 (6) |
| 3.3.14 | Security event management: protected logs; automated, centralised log correlation (SIEM) | 3.3.14 (h), (j) |
| 3.3.15 | Incident management: designated team, classification, evidence and log protection, forensics/RCA, incident repository | 3.3.15 (4) |
| 3.3.15-R | Inform SAMA IT Risk Supervision "immediately" of medium/high incidents; formal incident report after resuming operations (fields a-k) | 3.3.15 (5)-(7) |
| 3.3.16 | Threat management / intelligence | 3.3.16 |
| 3.3.17 | Vulnerability management: all assets, risk-based scan frequency, classification, mitigation timelines per class, patch management | 3.3.17 (3) |
| 3.4.1-3.4.3 | Third-party cyber security: contract/vendor management, outsourcing (SAMA approval rules), cloud computing | 3.4.1-3.4.3 |

## Deadlines and numbers
| What | Value | Official reference |
|---|---|---|
| Incident notification to SAMA | "inform 'SAMA IT Risk Supervision' immediately when a medium or high classified security incident has occurred and identified" | 3.3.15 (5) |
| Media contact about an incident | obtain "'no objection' from 'SAMA IT Risk Supervision' before any media interaction" | 3.3.15 (6) |
| Formal incident report | submit "after resuming operations" | 3.3.15 (7) |
| Penetration testing | "annual review and penetration tests" for customer and internet facing services | 3.2.4 (2) |
| Minimum maturity | "at least operate at maturity level 3 or higher" | 2.4 |
| Finance-company compliance date | full compliance "by the end of the fourth quarter of the year 2019" (amended by circular 51610/99, 17/08/1440H) | Finance Sector circular page |

## Assessment and certification
Periodic self-assessment by the member organization using a SAMA questionnaire; self-assessments "reviewed and audited by SAMA" to determine compliance and maturity (s.2.3). Waivers via Appendix D. No third-party certificate. Finance companies also had to submit a board-approved business plan and quarterly progress reports to SAMA (CRC.Compliance@SAMA.GOV.SA).

## Notes
- Catalog row "SAMA CSF ... | finance | security | law | L" is broadly right; `legal_status` is better described as a binding SAMA regulatory framework (circular), not a statute.
- Rulebook page says "Translation of this section is for demo purposes only" on the Finance Sector English page; the Arabic text is authoritative.
- The control-checklists SAMA grouping gives no SAMA reporting window; SAMA's is "immediately" for medium/high incidents (not a fixed hour count).
- No log retention period is stated in the CSF itself (CRFR 3.2.11 sets one year for its in-scope entities).
