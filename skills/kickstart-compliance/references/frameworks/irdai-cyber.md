---
id: irdai-cyber
name: IRDAI Information and Cyber Security Guidelines 2026
official_name: IRDAI Information and Cyber Security Guidelines, 2026 (circular IRDAI/GA&HR/CIR/MISC/51/4/2026, 6 April 2026), revising the IRDAI Information and Cyber Security Guidelines, 2023 (IRDAI/GA&HR/GDL/MISC/88/04/2023, 24 April 2023)
governing_body: Insurance Regulatory and Development Authority of India (IRDAI)
type: security
legal_status: regulator-guideline
region: India
industry: finance (insurance: insurers incl. Foreign Re-insurance Branches, insurance intermediaries, Insurance Information Bureau)
current_version: 2026 Guidelines (circular dated 6 April 2026; listed on irdai.gov.in 08-04-2026), compliance "from the current financial year"
superseded_by: none (the 2026 Guidelines revise the 2023 Guidelines)
official_sources:
  - title: IRDAI Guidelines listing (shows 2026 and 2023 cyber security guidelines)
    url: https://irdai.gov.in/guidelines
    accessed: 2026-11-06
  - title: IRDAI Information and Cybersecurity Guidelines, 2026 - document detail (circular, Annexure A summary of changes, Annexure B guidelines and annexures I-VI)
    url: https://irdai.gov.in/document-detail?documentId=9189223
    accessed: 2026-11-06
  - title: IRDAI Information and Cyber Security Guidelines, 2023 - document detail
    url: https://irdai.gov.in/document-detail?documentId=3314780
    accessed: 2026-11-06
last_verified: 2026-11-06T00:00:00Z
verification: verified
---

## What it is
IRDAI's minimum information and cyber security standards and governance mechanisms for regulated entities in insurance. The 2026 revision (Annexure B, 175 pages) is a model Information and Cyber Security Policy set, aligned to NIST CSF (Annexure I maps NIST applicability by entity type), with an annual independent assurance audit and auditor checklist (Annexure III).

## Who it applies to
- "All Insurers including Foreign Re-Insurance Branches (FRBs) and Insurance Intermediaries regulated by" IRDAI (Guidelines 1.4). Circular para 5 lists "Brokers, Corporate Agents, Web Aggregators, TPAs, IMFs, insurance Repositories, ISNP, Corporate Surveyors, MISPs, CSCs and the Insurance Information Bureau of India (IIB)".
- Excluded: "Insurance Agents, Micro-Insurance Agents, Point of Sale Persons and Individual Surveyors"; insurers must ensure they follow a minimum security framework (1.4).
- Intermediaries are classified for applicability in Annexure II.

## Engineering obligations
| ID | Obligation | Official reference |
|---|---|---|
| IRDAI-01 | Board-approved Information and Cyber Security Policy (ICSP) and governance (ISRMC, CISO, CRO roles) | Guidelines 1.0-1.6 |
| IRDAI-02 | CISO manages and monitors the SOC "24*7" and ensures effective functioning of SOC, DLP and other security solutions | Guidelines 1.6 (CISO) |
| IRDAI-03 | Report cyber incidents "to Cert-In within 6 hours of noticing or being brought to notice ... with a copy to IRDAI and other concerned regulators" | Incident management policy |
| IRDAI-04 | Maintain ICT infrastructure logs "for a rolling period of 180 days and within the Indian jurisdiction as per directions issued by Cert-In" | Logging and monitoring policy, items 13-14 |
| IRDAI-05 | Log and protect system administrator and operator activities; monitor attempts to access deactivated accounts | Logging policy, items 15-16 |
| IRDAI-06 | Synchronise clocks of all relevant information systems "with an agreed accurate time source" | System security standards, item 6 |
| IRDAI-07 | Harden servers, routers and firewalls per MBSS before production | System security standards, item 5 |
| IRDAI-08 | Security reviews of applications before production per application security standards | 3.1.2.1 |
| IRDAI-09 | VAPT of critical internal applications/infrastructure "at least once in a year"; VA of all internet-facing assets "at least once every 6 months"; external grey/white-box PT of internet-facing assets "once in 6 months"; all by CERT-In empanelled auditors | Security assessment policy, items 2-3 |
| IRDAI-10 | Mandatory security testing for all changes to internet-facing assets; close gaps before production | Security assessment policy, item 5 |
| IRDAI-11 | Define RTO and RPO for all applications; documented IT DR for new applications; BCP/DR testing | BCP/ITDR policy |
| IRDAI-12 | Cloud: use only MeitY-empanelled CSPs with valid STQC audit; CSP must support MFA; security requirements in contracts | Cloud security policy, 3.4 |
| IRDAI-13 | Classification (Confidential, Restricted, Internal, Public) reviewed at least every two years; secure destruction at end of retention | Data classification and disposal |
| IRDAI-14 | Personal information: obtain consent for purpose, means and mode of use before collection; collect sensitive personal information only for lawful, necessary purposes | 3.5.2 Collection of PII |
| IRDAI-15 | Close annual audit non-conformities "within 12 months of reporting" | Guidelines 1.6 (Board) |

## Deadlines and numbers
| What | Value | Official reference |
|---|---|---|
| Incident report | "to Cert-In within 6 hours of noticing or being brought to notice about such incidents with a copy to IRDAI" | Incident management policy, item 3 |
| Log retention | "rolling period of 180 days and within the Indian jurisdiction" | Logging policy, item 14 |
| VA internet-facing | "at least once every 6 months" | Security assessment, item 3 |
| PT internet-facing | "once in 6 months" | Security assessment, item 3 |
| VAPT critical internal | "at least once in a year" | Security assessment, item 2 |
| Assurance audit | "An independent Assurance Audit shall be carried out by the Auditor every year" | Guidelines 1.10 |
| Audit gap closure | "within 12 months of reporting" | Guidelines 1.6 |
| Assurance auditor rotation | "rotated every three years" | Audit policy |

## Assessment and certification
Annual independent assurance audit (1.10) by an audit firm meeting Annexure IV eligibility criteria, reported in the Annexure III format (summary, findings, non-compliances, risk rating, checklist) with an audit certificate (Annexures V/VI). Plans and reports go to the Audit Committee / RMC / Board. No certification.

## Notes
- The assignment and catalog cite the 2023 Guidelines; IRDAI issued revised **2026** Guidelines (circular dated 6 April 2026, listed 8 April 2026), effective "from the current financial year". The catalog should reference the 2026 version.
- Catalog row "IRDAI cyber guidelines ... law ... Insurers regulated in India" understates scope: intermediaries (brokers, corporate agents, web aggregators, TPAs, etc.) and IIB are also covered; legal status is a regulator guideline/circular.
- The 6-hour rule in the IRDAI text is reporting to CERT-In with a copy to IRDAI (not a separate IRDAI clock). UNVERIFIED: the June 2023 IRDAI circular on reporting of cyber security incidents (24-hour detail submission to IRDAI) was seen only via search results and not fetched.
