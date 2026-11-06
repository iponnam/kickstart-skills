---
id: sebi-cscrf
name: SEBI CSCRF
official_name: Cybersecurity and Cyber Resilience Framework (CSCRF) for SEBI Regulated Entities (REs) (circular SEBI/HO/ITD-1/ITD_CSC_EXT/P/CIR/2024/113, 20 August 2024)
governing_body: Securities and Exchange Board of India (SEBI), Information Technology Department
type: security
legal_status: binding-regulation
region: India
industry: "finance (securities markets: stock exchanges, depositories, clearing corporations, stock brokers, DPs, MFs/AMCs, KRAs, RTAs/QRTAs, portfolio managers, AIFs, VCFs, research analysts, investment advisers and other SEBI REs)"
current_version: Version 1.0, 20 Aug 2024, read with clarifications CIR/2024/184 (31 Dec 2024), extension CIR/2025/45 (28 Mar 2025), clarifications CIR/2025/60 (30 Apr 2025), FAQs (11 Jun 2025), extension CIR/2025/96 (30 Jun 2025) and technical clarifications CIR/2025/119 (28 Aug 2025)
superseded_by: none
official_sources:
  - title: CSCRF for SEBI Regulated Entities, circular dated 20 August 2024 (page)
    url: https://www.sebi.gov.in/legal/circulars/aug-2024/cybersecurity-and-cyber-resilience-framework-cscrf-for-sebi-regulated-entities-res-_85964.html
    accessed: 2026-11-06
  - title: CSCRF circular and Annexure-1 framework (PDF)
    url: https://www.sebi.gov.in/sebi_data/attachdocs/aug-2024/1724326790365.pdf
    accessed: 2026-11-06
  - title: Clarifications to CSCRF, circular dated 31 December 2024 (PDF)
    url: https://www.sebi.gov.in/sebi_data/attachdocs/dec-2024/1735646756843.pdf
    accessed: 2026-11-06
  - title: FAQs on CSCRF (June 2025)
    url: https://www.sebi.gov.in/sebi_data/faqfiles/jun-2025/1749647139924.pdf
    accessed: 2026-11-06
  - title: Clarifications to CSCRF for SEBI REs, circular SEBI/HO/ITD-1/ITD_CSC_EXT/P/CIR/2025/60, 30 April 2025 (PDF)
    url: https://www.sebi.gov.in/sebi_data/attachdocs/apr-2025/1746016112057.pdf
    accessed: 2026-11-06
  - title: Extension towards Adoption and Implementation of CSCRF, circular SEBI/HO/ITD-1/ITD_CSC_EXT/P/CIR/2025/96, 30 June 2025 (PDF)
    url: https://www.sebi.gov.in/sebi_data/attachdocs/jun-2025/1751286353420.pdf
    accessed: 2026-11-06
  - title: Technical Clarifications to CSCRF for SEBI REs, circular SEBI/HO/ITD-1/ITD_CSC_EXT/P/CIR/2025/119, 28 August 2025 (PDF)
    url: https://www.sebi.gov.in/sebi_data/attachdocs/aug-2025/1756380695925.pdf
    accessed: 2026-11-06
last_verified: 2026-11-06T00:00:00Z
verification: verified
---

## What it is
A single, graded cybersecurity framework replacing SEBI's earlier entity-specific cyber circulars. It is organised around cyber resilience goals (Anticipate, Withstand, Contain, Recover, Evolve) and functions (Governance, Identify, Protect, Detect, Respond, Recover), with standards and mandatory guidelines whose applicability depends on the RE's category. It draws on ISO 27000, CIS v8, NIST and CPMI-IOSCO guidance.

## Who it applies to
- SEBI REs listed in the addressees (AIFs, banks as DPs/brokers, clearing corporations, depositories, DPs, KRAs, MFs/AMCs, portfolio managers, RTAs, stock brokers, stock exchanges, VCFs and others).
- Five categories: "Market Infrastructure Institutions (MIIs), Qualified REs, Mid-size REs, Small-size REs, Self-certification REs" (Framework, "Thresholds for REs' categorization"). The category "shall be decided at the beginning of the financial year based on the data of the previous financial year" using entity-specific thresholds (e.g. AUM bands for AIFs).

## Engineering obligations
| ID | Obligation | Official reference |
|---|---|---|
| CSCRF-01 | Board/Partners/Proprietor-approved cybersecurity and cyber resilience policy | Circular Annexure summary (Governance); GV standards |
| CSCRF-02 | Cyber risk management framework (MIIs, Qualified and Mid-size REs); risk assessment including post-quantum risks, half-yearly (MIIs) / yearly (Qualified, Mid-size) | Governance (c); ID.RA guideline 1 |
| CSCRF-03 | Board-approved list of critical systems; all IT assets inventoried in an ITSM tool | Identify; ID.AM |
| CSCRF-04 | Obtain SBOMs for existing critical systems "within 6 months" of issuance and for new critical software/SaaS at procurement | GV.SC.S5 |
| CSCRF-05 | Authentication and access policy with effective log collection; collect system, application, network, database, security, performance, audit trail and event logs; log retention per IT Act, DPDP Act and CERT-In | Protect (a); DE/PR log guidelines |
| CSCRF-06 | Network segmentation; Full Disk Encryption plus File-based Encryption for data protection | Protect (b)-(c) |
| CSCRF-07 | Separate production and non-production environments for critical-system software | Protect (d) |
| CSCRF-08 | API and endpoint security with rate limiting, throttling, authentication and authorisation | Protect (g) |
| CSCRF-09 | Security requirements (session management, audit trail, logging, data integrity, exception handling) in business requirement documents; secure SDLC | SSDLC guideline 4(a) |
| CSCRF-10 | Vulnerability assessment for every production release; VAPT for every major release; VAPT of all critical systems per the framework's scope | Protect (f); testing guideline 3(b) |
| CSCRF-11 | ISO 27001 certification: mandatory for MIIs; for Qualified REs now "encouraged and recommended (not mandatory)" | Protect (h); PR.IP.S16 as clarified by CIR/2025/119 para 6.11 |
| CSCRF-12 | SOC (own, group, third-party or Market SOC); small-size and self-certification REs onboard the Market SOC (NSE/BSE) but may leverage an existing own SOC and submit SOC efficacy reports; SOC/M-SOC exemption for DPs, RTAs, and self-certification PMs and AIF/VCF managers with fewer than 100 clients | Detect (a)-(c); CIR/2025/60 paras 2.2, 2.6, 2.7, 3; CIR/2025/119 para 6.9 |
| CSCRF-13 | Red teaming exercises (MIIs and Qualified REs) | Detect (d) |
| CSCRF-14 | Incident response management plan, CCMP, RCA and forensic analysis | Respond |
| CSCRF-15 | Report incidents under CERT-In directions to SEBI and CERT-In within 6 hours (mkt_incidents@sebi.gov.in), details on SEBI Incident Reporting Portal within 24 hours; others within 24 hours | RS.CO guideline 1 |
| CSCRF-16 | Recovery plan: design and test systems to resume critical operations within two hours of a disruption (two-hour RTO, per IOSCO), plan for scenarios where this is not achieved; "RPO for critical systems shall be 15 minutes"; periodic recovery drills; documented backup plan | RC.RP.S2 as clarified by CIR/2025/119 para 6.10 |
| CSCRF-17 | Store "Regulatory Data" "within the legal boundaries of India" in accessible, legible, usable form (original data in India for foreign investors) | Definitions, data categories |
| CSCRF-18 | Third-party services: RE "solely accountable"; background checks, NDAs, cybersecurity compliance for vendors | Governance (e); GV.SC |
| CSCRF-20 | Critical systems include any system on the same network segment as core-impacting, regulatory-data, connecting, internet-facing or client-facing systems (on premise and cloud) | CIR/2025/119 para 6.1 |
| CSCRF-21 | Zero-trust: implement strategies such as zero-trust networks, segmentation, no single point of failure and high availability, approved by the IT Committee (replaces the default-deny wording) | PR.AA.S4-S5 as clarified by CIR/2025/119 para 6.2 |
| CSCRF-22 | Dedicated HSM mandatory for MIIs and Qualified REs under the cloud framework (Annexure-J); others may use a Board-approved risk-assessed alternative | CIR/2025/60 para 5 |
| CSCRF-23 | Submit only VAPT and cyber audit summaries in the CSCRF format; do not submit explicit vulnerabilities unless SEBI asks | CIR/2025/119 para 6.7 |
| CSCRF-24 | Follow CERT-In Comprehensive Cyber Security Audit Policy Guidelines for cyber audits | CIR/2025/119 Part D para 8 |
| CSCRF-19 | Periodic cyber audit by CERT-In empanelled IS auditing organisation, with MD/CEO declaration | Protect (e); Audit section |

## Deadlines and numbers
| What | Value | Official reference |
|---|---|---|
| Incident notification (CERT-In-listed incidents) to SEBI and CERT-In | "within 6 hours of noticing/ detecting such incidents or being brought to notice" | RS.CO guideline 1 |
| Incident details on SEBI portal | "within 24 hours" | RS.CO guideline 1 |
| Other cybersecurity incidents | "reported to SEBI, CERT-In and NCIIPC (as applicable) within 24 hours" | RS.CO guideline 1 |
| VAPT (CII/protected systems) | "One VAPT activity ... in each half of the financial year" | Section 4.3 |
| VAPT report submission | "within one (1) month of completion of VAPT activity" | Table 19 |
| VAPT findings closure | "Within 3 months of submission" | Table 19 |
| VAPT revalidation | "within 5 months of completion of VAPT" | Table 19 |
| Auditor rotation | maximum "three consecutive years", then "cooling off period of two years" | Audit section (b) |
| SBOM for existing critical systems | "within 6 months" of CSCRF issuance | GV.SC.S5 |
| Cyber Capability Index | MIIs third-party "half-yearly"; Qualified REs self-assessment "yearly" | Governance (d) |
| Compliance dates | Six REs with prior circulars "by January 01, 2025"; others "by April 01, 2025" | Circular para 17 |
| Forbearance / extensions | "regulatory forbearance is provided till March 31, 2025"; KRAs and DPs extended "to April 01, 2025" | Clarifications 31 Dec 2024 |
| Compliance deadline (after extensions) | "timeline for compliance is June 30, 2025" (CIR/2025/45 REs); then extended "by two (2) months, i.e., till August 31, 2025 to all REs, except" MIIs, KRAs and QRTAs | CIR/2025/60 para 10; CIR/2025/96 para 2 |
| Disaster declaration / RTO / RPO | declare 'Disaster' within 30 minutes (original guideline); resume critical operations "within two hours"; "RPO for critical systems shall be 15 minutes" | RC.RP.S2; CIR/2025/119 para 6.10 |
| Stock broker thresholds | Qualified: "More than 10 lakhs" registered clients or > 10,00,000 crore annual clientele trading volume; Mid: > 1 lakh to 10 lakhs clients; Small: > 10,000 to 1 lakh; Self-certification: > 1,000 to 10,000; exempt below 1,000 clients and 1,000 crore volume | CIR/2025/60 Table 1, para 2.1.2 |
| Portfolio manager thresholds (current) | Mid-size: AUM Rs. 10,000 crores and above; Small: > Rs. 3,000 to < 10,000 crores; Self-certification: Rs. 3,000 crores and below | CIR/2025/119 Part C Table 1 |
| AIF/VCF thresholds (manager level) | Mid-size: corpus Rs. 10,000 crores and above; Small: > Rs. 3,000 to < 10,000 crores; Self-certification: Rs. 3,000 crores and below | CIR/2025/60 Table 4 |
| Merchant bankers (current) | active MBs: Small-size REs; inactive MBs: "Exempt from CSCRF" | CIR/2025/119 Part C Table 2 |

## Assessment and certification
Cyber audits by CERT-In empanelled IS auditing organisations (all audits unless otherwise specified), with an auditor's checklist in the framework and an MD/CEO declaration (Annexure-B). Self-certification REs report in the Annexure-P format. ISO 27001 certification for MIIs (recommended, not mandatory, for Qualified REs per CIR/2025/119). REs also regulated by another regulator (e.g. banks under RBI) apply the Principle of Exclusivity (CSCRF scope limited to systems exclusively used for SEBI-regulated activities, with shared infrastructure in scope if the primary regulator does not cover it) and the Principle of Equivalence (controls with an equivalent in the primary regulator's framework deemed compliant), and must demonstrate this at compliance submission (CIR/2025/119 Part A). CCI assessment for MIIs (third party) and Qualified REs (self). Per FAQ, audits "for audit period from FY 2025-26 onwards shall be as per the circular ... dated August 20, 2024, read along with the clarifications issued".

## Notes
- Catalog row "SEBI CSCRF ... finance (market infrastructure) ... Stock exchanges, brokers, depositories, market intermediaries": broadly correct but understates scope; it applies to all listed SEBI REs including AIFs, VCFs, portfolio managers, RTAs, KRAs and MFs, in five categories with graded obligations.
- Checklist "SEBI 6h" is correct for incidents covered by CERT-In directions; add the 24-hour portal detail and 24-hour rule for other incidents.
- Checklist "annual VAPT by an approved vendor": for SEBI, VAPT cadence depends on category (half-yearly for CII/protected systems, at least once a year for others) and audits use CERT-In empanelled auditors.
- Second pass: the 30 April 2025 (CIR/2025/60), 30 June 2025 (CIR/2025/96) and 28 August 2025 (CIR/2025/119) circulars were read. Changes: re-categorisation thresholds for stock brokers, DPs, PMs, AIFs/VCFs and MBs; KRAs moved from MIIs to Qualified REs; standalone IAs and RAs (not registered in other capacities) exempt, with BSE as reporting authority for IAs/RAs; inactive MBs exempt; ISO 27001 no longer mandatory for Qualified REs; mobile application security guidelines (PR.AA.S16) now "recommendatory (not mandatory)"; the press-release requirement for high-impact incidents (RS.CO.S2) replaced by action per the approved CCMP; NCIIPC principles apply only to REs identified as CII; compliance deadline moved to 31 August 2025 for all REs other than MIIs, KRAs and QRTAs.
- The 6-hour and 24-hour incident reporting figures (RS.CO guideline 1) were not changed by these circulars.
- Verification raised to `verified`: scope, categories, compliance deadlines and key numbers are now confirmed from the SEBI circular texts. Later (post-August 2025) circulars, if any, were not checked.
