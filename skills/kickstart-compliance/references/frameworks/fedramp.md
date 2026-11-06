---
id: fedramp
name: FedRAMP
official_name: Federal Risk and Authorization Management Program (FedRAMP), FedRAMP Consolidated Rules for 2026 (CR26), covering FedRAMP Rev5 and FedRAMP 20x Certifications
governing_body: U.S. General Services Administration (GSA), FedRAMP program office; established in law by the FedRAMP Authorization Act (Dec 2022); policy in OMB Memorandum M-24-15
type: security
legal_status: certification-scheme
region: US federal (cloud services with direct or indirect government-wide use by federal agencies)
industry: government, cloud
current_version: Consolidated Rules for 2026, officially launched 2026-06-24; optional adoption from July 4, 2026; mandatory January 1, 2027
superseded_by: none (FedRAMP Rev5 Certifications are being phased out in favour of FedRAMP 20x; no new Rev5 Certifications after June 11, 2027)
official_sources:
  - title: FedRAMP.gov home (What's New, Marketplace counts)
    url: https://www.fedramp.gov/
    accessed: 2026-11-06
  - title: FedRAMP 20x
    url: https://www.fedramp.gov/20x
    accessed: 2026-11-06
  - title: Important Dates for the Consolidated Rules for 2026
    url: https://www.fedramp.gov/2026/timeline/
    accessed: 2026-11-06
  - title: What's Changing in 2026
    url: https://www.fedramp.gov/2026/providers/updating/changes/
    accessed: 2026-11-06
  - title: Choosing a Certification Class (Low, Moderate, High vs Classes)
    url: https://www.fedramp.gov/2026/providers/start/class/
    accessed: 2026-11-06
  - title: Key Security Indicators (reference)
    url: https://www.fedramp.gov/2026/reference/key-security-indicators/
    accessed: 2026-11-06
  - title: Incident Evaluation and Communication ruleset
    url: https://www.fedramp.gov/2026/reference/incident-evaluation-and-communication/
    accessed: 2026-11-06
  - title: Vulnerability Detection and Response ruleset
    url: https://www.fedramp.gov/2026/reference/vulnerability-detection-and-response/
    accessed: 2026-11-06
  - title: Cloud Service Providers (government-wide use cases, CMMC note)
    url: https://www.fedramp.gov/2026/providers/
    accessed: 2026-11-06
last_verified: 2026-11-06T00:00:00Z
verification: verified
---

## What it is
FedRAMP is the government-wide program for security assessment of cloud services used by federal agencies. Under the Consolidated Rules for 2026 FedRAMP describes itself as "a security framework for businesses to set security goals for themselves, continuously validate the effectiveness of the capabilities used to meet those goals" and says "It should not be treated like a traditional compliance framework" (Providers page). FedRAMP now issues "FedRAMP Certification" (the law defines a FedRAMP authorization as "a certification that a cloud computing product or service has completed a FedRAMP authorization process") under two paths: FedRAMP Rev5 (NIST SP 800-53 Rev. 5 control based) and FedRAMP 20x (outcome based, measured through Key Security Indicators). The machine-readable rules in the FedRAMP rules repository are the "source of truth" (Using the Consolidated Rules).

## Who it applies to
Cloud service offerings with "Direct Government-Wide Use" (used directly by multiple federal agency customers within federal information systems under 44 USC § 3506) or "Indirect Government-Wide Use" (third-party information resource inside such services) (Providers page). "FedRAMP does not support or provide 'equivalency'"; CMMC/FedRAMP equivalency questions go to the Department of War (Providers page).

Certification classes replace the old impact-level labels:
- 20x: Class A (pilot/entry, "designed for existing commercial products that already have a SOC 2 Type II certification and a mature security program"), Class B (Low), Class C (Moderate); Class D (High) planned for Phase 4 (20x page; Choosing a Class).
- Rev5: Class B, Class C, Class D (Rev5 reference).
- "There is not a direct correlation between FedRAMP Certification Class and Impact Level" but classes "loosely align with the baseline security expectations" of NIST SP 800-53B low, moderate and high (Choosing a Class).

## Engineering obligations
| ID | Obligation | Official reference |
|---|---|---|
| KSI-IAM-APM | "Secure passwordless methods are used for user authentication ... when feasible, otherwise strong passwords with phishing-resistant MFA is used" | Key Security Indicators |
| KSI-IAM-AAM | Account, role and group lifecycle and privileges managed using automation | KSI-IAM-AAM |
| KSI-IAM-JIT / KSI-IAM-ELP | Least-privileged, role/attribute-based, just-in-time authorization model, persistently reviewed | KSI-IAM-JIT, KSI-IAM-ELP |
| KSI-IAM-SNU | Secure authentication for non-user accounts and services | KSI-IAM-SNU |
| KSI-IAM-SUS | Disable or secure privileged accounts in response to suspicious activity | KSI-IAM-SUS |
| KSI-CMT-LMC | Modifications to the cloud service offering are logged and monitored | KSI-CMT-LMC |
| KSI-CMT-RMV | Change machine resources by redeploying version-controlled resources rather than direct modification | KSI-CMT-RMV |
| KSI-CMT-VTD | Automated testing and validation of changes throughout deployment | KSI-CMT-VTD |
| KSI-CNA-MAT / KSI-CNA-RNT | Minimal attack surface, limit lateral movement; restrict inbound/outbound network traffic | KSI-CNA-MAT, KSI-CNA-RNT |
| KSI-SVC-ACM | Configuration managed with automation and reviewed for drift | KSI-SVC-ACM |
| KSI-SVC-ASM | Automate management, protection and rotation of keys, certificates and secrets | KSI-SVC-ASM |
| KSI-SVC-SIN | "Information is encrypted or otherwise secured from unwanted access or modification" | KSI-SVC-SIN |
| KSI-SVC-VRI | Use cryptographic methods to validate integrity of machine-based resources | KSI-SVC-VRI |
| KSI-MLA-OSM | SIEM or similar for centralized, tamper-resistant logging | KSI-MLA-OSM |
| KSI-MLA-LET / KSI-MLA-RVL | Maintain list of logged event types; persistently review logs | KSI-MLA-LET, KSI-MLA-RVL |
| KSI-MLA-EVC | Persistently evaluate and test configuration, especially infrastructure as code | KSI-MLA-EVC |
| KSI-PIY-GIV | Automatically generate real-time inventories of all information resources from authoritative sources | KSI-PIY-GIV |
| KSI-PIY-RSD | Build security and privacy into the SDLC, aligned with CISA Secure By Design | KSI-PIY-RSD |
| KSI-SCR-MON | Automatically monitor third-party software for upstream vulnerabilities | KSI-SCR-MON |
| KSI-RPL-RRO / KSI-RPL-TRC | Define RTO/RPO; persistently test recovery capability | KSI-RPL-RRO, KSI-RPL-TRC |
| IEC-CSO-EFR / IIR | Evaluate incidents for FedRAMP reportability; send Initial Incident Report to fedramp_security@fedramp.gov, agency customers and trust center within class/PAIN timeframes | Incident Evaluation and Communication |
| VDR (Timeframes) | Run vulnerability detection on drift-prone resources (Class C at least every 14 days, Class D every 7 days); mitigate within PAIN-based timeframes; avoid and remediate KEVs | Vulnerability Detection and Response |

## Deadlines and numbers
| What | Value | Official reference |
|---|---|---|
| Initial incident report, Class C | PAIN-5/4/3: "1 hour"; PAIN-2: "24 hours"; PAIN-1: "1 business day" | IEC-CSO-IIR |
| Initial incident report, Class B (and Class A, SHOULD) | PAIN-5/4/3: "6 hours"; PAIN-2/1: "1 business day" | IEC-CSO-IIR |
| Initial incident report, Class D | PAIN-5/4/3: "0.25 hours"; PAIN-2/1: "1 hour" | IEC-CSO-IIR |
| Default rating if not estimated | treat as PAIN 5 | IEC-CSO-DPR |
| Vulnerability detection frequency | Class C "at least once every 14 days"; Class D "at least once every 7 days" | VDR Timeframes |
| Optional early adoption of CR26 | July 4, 2026 | Important Dates |
| FedRAMP Ready goes legacy | July 28, 2026 | Important Dates |
| 20x Class A pipeline opens | August 3, 2026 | Important Dates |
| 20x Class B & C pipeline opens | August 31, 2026 | Important Dates |
| Mandatory adoption of CR26 | January 1, 2027 | Important Dates |
| End of new Rev5 Certifications | June 11, 2027 | Important Dates; What's Changing |
| Existing Rev5 Certifications remain active | "until at least December 31, 2028, unless FedRAMP is otherwise directed" | What's Changing |
| Marketplace counts (2026-11-06) | 554 FedRAMP Certified services; 36 FedRAMP 20x Certified | fedramp.gov home |

## Assessment and certification
Independent assessors (FedRAMP recognized assessors listed on the Marketplace) perform assessments; FedRAMP grants the FedRAMP Certification and lists it on the FedRAMP Marketplace. Agencies still issue their own authorization to operate for the federal information system that uses the service (OMB Circular A-130). Ongoing Certification (formerly "continuous monitoring") is required; failing it "will result in a loss of FedRAMP Certification" (What's Changing). First full FedRAMP 20x Class C Certification announced November 2, 2026 (home page).

## Notes
- Catalog row "`+` FedRAMP ... certification ... Cloud services sold to US federal agencies" is broadly right but outdated: (1) FedRAMP now uses "Certification" and Classes A-D rather than "Authorization" and Low/Moderate/High (CR26 What's Changing); (2) FedRAMP 20x is officially live (Class A, B, C rules finalized; Class D in Phase 4, FY27 Q1-Q2 estimated); (3) the SSP is replaced by a "Certification Package Overview and Security Decision Record"; (4) new Rev5 Certifications stop June 11, 2027. "FedRAMP Ready" is legacy after July 28, 2026.
- Catalog row for NIST 800-53 says "basis for FedRAMP": still true for the Rev5 path; 20x KSIs map to 800-53 controls ("Related SP 800-53 Controls") but are not a control baseline.
- The legacy LI-SaaS / Low / Moderate / High baseline documents are on fedramp.gov/legacy; not re-checked in this pass.
- Future phase dates are described by FedRAMP as "estimates for public awareness, not firm commitments" (20x page).
