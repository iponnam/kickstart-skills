---
id: rbi-csf-banks
name: RBI Cyber Security Framework in Banks + IT Governance Master Direction
official_name: Cyber Security Framework in Banks (RBI/2015-16/418, DBS.CO/CSITE/BC.11/33.01.001/2015-16, 2 June 2016); Reserve Bank of India (Information Technology Governance, Risk, Controls and Assurance Practices) Directions, 2023 (RBI/2023-24/107, DoS.CO.CSITEG/SEC.7/31.01.015/2023-24, 7 November 2023)
governing_body: Reserve Bank of India (Department of Supervision, CSITE Cell)
type: security
legal_status: binding-regulation
region: India (foreign banks operating in India in branch mode included, with "comply or explain" for the Master Direction)
industry: finance (banking; NBFCs Top/Upper/Middle Layer, Credit Information Companies and AIFIs for the Master Direction)
current_version: CSF circular 2 June 2016 (in force; not in the Master Direction's repeal list); IT Governance Master Direction 7 Nov 2023, "come into effect from April 1, 2024"
superseded_by: none
official_sources:
  - title: Cyber Security Framework in Banks, circular dated June 2, 2016
    url: https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=10435&Mode=0
    accessed: 2026-11-06
  - title: Annex 1 - Baseline Cyber Security and Resilience Requirements
    url: https://rbidocs.rbi.org.in/rdocs/content/pdfs/CSFB020616_AN1.pdf
    accessed: 2026-11-06
  - title: Annex 3 - Template for reporting Cyber Incidents
    url: https://rbidocs.rbi.org.in/rdocs/content/pdfs/CSFB020616_AN3.pdf
    accessed: 2026-11-06
  - title: Master Direction on Information Technology Governance, Risk, Controls and Assurance Practices (7 Nov 2023)
    url: https://www.rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=12562
    accessed: 2026-11-06
last_verified: 2026-11-06T00:00:00Z
verification: verified
---

## What it is
The 2016 circular requires scheduled commercial banks to have a Board-approved cyber security policy distinct from the IT policy, a Security Operations Centre, a Cyber Crisis Management Plan and incident reporting to RBI, and sets indicative baseline controls (Annex 1). The 2023 Master Direction consolidates and updates RBI's IT governance, IT/information security risk management, BCP/DR and IS audit instructions across banks, larger NBFCs, CICs and AIFIs, effective 1 April 2024.

## Who it applies to
- CSF 2016: "All Scheduled Commercial Banks (excluding Regional Rural Banks)" (addressee line).
- Master Direction para 2(a): commercial banks (incl. foreign banks, SFBs, Payments Banks per footnote 1); NBFCs in the Top, Upper and Middle Layers under Scale Based Regulation; Credit Information Companies; EXIM Bank, NABARD, NaBFID, NHB and SIDBI. Not applicable to Local Area Banks and NBFC-Core Investment Companies (para 2(b)). Foreign bank branches: "comply or explain" (para 2(c)).
- Housing Finance Companies report cyber incidents to NHB, not RBI (MD footnote 17).

## Engineering obligations
| ID | Obligation | Official reference |
|---|---|---|
| RBI-CSF-01 | Board-approved Cyber Security Policy "distinct and separate from the broader IT policy / IS Security policy" | CSF paras 3-4; MD para 24(a) |
| RBI-CSF-02 | Set up a SOC for "continuous surveillance" and real-time monitoring of cyber risks | CSF paras 6, 8; Annex 2 |
| RBI-CSF-03 | Cyber Crisis Management Plan covering detection, response, recovery and containment | CSF paras 11-12; MD para 24(a) |
| RBI-CSF-04 | Up-to-date inventory of business IT assets with criticality; data classification | CSF Annex 1 control 1 |
| RBI-CSF-05 | Application whitelisting / control of unauthorised software; expeditious and emergency patching | Annex 1 controls 2, 7 |
| RBI-CSF-06 | Network security, secure configuration, application security life cycle, user access control, customer authentication framework | Annex 1 controls 4-6, 8-9 |
| RBI-CSF-07 | Vendor risk management, removable media, anti-phishing, DLP strategy | Annex 1 controls 11-12, 14-15 |
| RBI-CSF-08 | Maintenance, monitoring and analysis of audit logs; audit log settings | Annex 1 controls 16-17 |
| RBI-CSF-09 | VA/PT and red team exercises; incident response and management; risk-based transaction monitoring; forensics; metrics | Annex 1 controls 18-22 |
| RBI-CSF-10 | Report "all unusual cyber-security incidents (whether they were successful or were attempts which did not fructify)" to RBI, using the Annex 3 template | CSF paras 14-15; Annex 3 |
| RBI-MD-11 | Change and patch management policy: assess impact, apply patches "in a secure and timely manner" | MD para 13 |
| RBI-MD-12 | Every IT application that can access or affect critical or sensitive information must have audit and system logging and audit trails detailed enough for forensics and non-repudiation; monitor them regularly | MD para 15 |
| RBI-MD-13 | Strong cryptography: internationally accepted, non-deprecated algorithms, key lengths, cipher suites and protocols | MD para 16 |
| RBI-MD-14 | Straight-through processing: no manual intervention or modification of data in transit between processes/applications | MD para 17 |
| RBI-MD-15 | Define RPO and RTO for all critical information systems | MD para 21(a) |
| RBI-MD-16 | VA "at least once in every six months" and PT "at least once in 12 months" for critical systems and customer-facing DMZ systems; VA/PT across lifecycle and on production after implementation; fix vulnerabilities time-bound | MD para 26 |
| RBI-MD-17 | Documented incident response and recovery procedures; forensic root-cause analysis; "pro-actively notify CERT-In and RBI regarding incidents, as per regulatory requirements" | MD para 27 |
| RBI-MD-18 | DR drills for critical systems "at least on a half-yearly basis"; resolve issues and re-test | MD para 29 |
| RBI-MD-19 | CISO (GM rank or equivalent) not reporting to Head of IT and without business targets; reviews cyber risk with the Board/RMCB/ITSC "atleast on a quarterly basis" | MD para 24(c) |
| RBI-MD-20 | IS Audit policy approved by the Audit Committee of the Board, risk-based IS audit planning | MD para 30 |

## Deadlines and numbers
| What | Value | Official reference |
|---|---|---|
| Incident reporting to RBI | "Security Incident Reporting (SIR) to RBI (within two to 6 hours)" | CSF Annex 3, item 1 |
| Incident timestamps | "Please specify in Indian Local Time (+5.30 GMT)" | CSF Annex 3 |
| VA (critical / DMZ customer-facing) | "at least once in every six months" | MD para 26(a) |
| PT (critical / DMZ customer-facing) | "at least once in 12 months" | MD para 26(a) |
| DR drills (critical systems) | "at least on a half-yearly basis" | MD para 29(a) |
| CISO review to Board | "atleast on a quarterly basis" | MD para 24(c) |
| Policies review by Board | "reviewed at least annually" | MD para 5(b) |
| Effective date of Master Direction | "come into effect from April 1, 2024" | MD para 1(c) |

## Assessment and certification
No certification. RBI supervises through CSITE examinations. CSF para 13 requires preparedness indicators tested "through independent compliance checks and audits carried out by qualified and competent professionals". MD Chapter VI requires internal/external IS audit under the Audit Committee of the Board.

## Notes
- Catalog row "RBI CSF ... audit: law" is acceptable, but the legal status is a binding RBI circular/direction, not a statute. Scope in the catalog ("Banks regulated by the Reserve Bank of India") is narrower than the 2023 Master Direction, which also covers SFBs, Payments Banks, upper-layer NBFCs, CICs and AIFIs; CSF 2016 itself excludes Regional Rural Banks.
- Checklist "RBI 6h" is approximately right: the official text is "within two to 6 hours" (CSF Annex 3). CERT-In's 6-hour rule applies in parallel. The 2023 MD does not set its own number; it says notify CERT-In and RBI "as per regulatory requirements".
- Checklist "annual VAPT by an approved vendor" is inaccurate for RBI: the MD requires VA every six months and PT every 12 months for critical systems, by "appropriately trained and independent information security experts/ auditors"; no "approved vendor" list is set in the MD.
- Checklist "data localisation (RBI payments data in India)" belongs to the 2018 storage of payment system data circular (see rbi-pa-pg), not to CSF.
