---
id: swift-csp
name: SWIFT CSP
official_name: "Swift Customer Security Programme (CSP): Customer Security Controls Framework (CSCF) and Customer Security Controls Policy"
governing_body: SWIFT (Society for Worldwide Interbank Financial Telecommunication)
type: sector
legal_status: contractual
region: global (all Swift users)
industry: finance (Swift-connected institutions)
current_version: "UNVERIFIED: CSCF v2026 (published mid-2025) governs attestations submitted July–December 2026; CSCF v2027 (expected mid-2026) not checked"
superseded_by: "UNVERIFIED"
official_sources:
  - title: "Customer Security Programme (CSP) - mySwift (unreachable: HTTP 403 / host not allowed)"
    url: https://www.swift.com/myswift/customer-security-programme-csp
    accessed: 2026-11-06
  - title: "Understand Controls - mySwift (unreachable)"
    url: https://www.swift.com/myswift/customer-security-programme/understand-controls
    accessed: 2026-11-06
  - title: "Swift Customer Security Controls Framework v2026 (PDF, www2.swift.com: unreachable)"
    url: https://www2.swift.com/knowledgecentre/rest/v1/publications/cscf_dd/70.0/CSCF_v2026_202507015.pdf?logDownload=true
    accessed: 2026-11-06
  - title: "Swift Customer Security Controls Policy (PDF, www2.swift.com: unreachable)"
    url: https://www2.swift.com/knowledgecentre/rest/v1/publications/csp_s_cust_sec_ctrl_pol/8.0/csp_s_cust_sec_ctrl_pol.pdf
    accessed: 2026-11-06
last_verified: never
verification: unreachable
---

## What it is
UNVERIFIED (official site unreachable from this sandbox). The Swift Customer Security Programme requires every Swift user to secure its local Swift-related infrastructure against the Customer Security Controls Framework (CSCF) and to attest compliance annually through Swift's KYC Security Attestation (KYC-SA) application. The CSCF is reissued every year as "CSCF v<year>".

## Who it applies to
UNVERIFIED. All Swift users (banks, market infrastructures, corporates connected to Swift). Control applicability depends on the user's architecture type (A1, A2, A3, A4, B). Per search-result summaries of the CSCF v2026 PDF (not fetched), v2026 makes customer client connectors (API endpoints, middleware, file transfer clients) mandatory in scope for several controls, and some users previously on architecture B may need to attest as A4.

## Engineering obligations
All rows UNVERIFIED (CSCF text not readable). Control numbers follow the CSCF structure (3 objectives, 7 principles).

| ID | Obligation | Official reference |
|---|---|---|
| 1.1 | Swift environment protection: segregate the secure zone from general IT | CSCF 1.1 (UNVERIFIED) |
| 1.2 | Restrict and control privileged operating system accounts | CSCF 1.2 (UNVERIFIED) |
| 1.3 | Virtualisation or cloud platform protection | CSCF 1.3 (UNVERIFIED) |
| 1.4 | Restrict internet access | CSCF 1.4 (UNVERIFIED) |
| 2.1 | Internal data flow security (confidentiality, integrity, authentication) | CSCF 2.1 (UNVERIFIED) |
| 2.2 | Security updates within defined timeframes | CSCF 2.2 (UNVERIFIED) |
| 2.3 | System hardening | CSCF 2.3 (UNVERIFIED) |
| 2.6 / 2.7 | Operator session confidentiality and integrity / vulnerability scanning | CSCF 2.6, 2.7 (UNVERIFIED) |
| 3.1 | Physical security | CSCF 3.1 (UNVERIFIED) |
| 4.1 / 4.2 | Password policy / multi-factor authentication | CSCF 4.1, 4.2 (UNVERIFIED) |
| 5.1 / 5.4 | Logical access control / physical and logical password storage | CSCF 5.1, 5.4 (UNVERIFIED) |
| 6.1 / 6.4 | Malware protection / logging and monitoring | CSCF 6.1, 6.4 (UNVERIFIED) |
| 7.1 | Cyber incident response planning | CSCF 7.1 (UNVERIFIED) |
| 2.8 | Outsourced critical activity protection | CSCF 2.8 (UNVERIFIED) |
| 2.9 / 2.11A | Transaction business controls / RMA business controls | CSCF (UNVERIFIED) |

## Deadlines and numbers
| What | Value | Official reference |
|---|---|---|
| Controls in CSCF v2026 | "32 security controls (26 mandatory controls and 6 advisory controls)" | CSCF v2026 (quoted in search snippet only: UNVERIFIED) |
| Attestation window | "from 01 July until 31 December" each year, against the CSCF version published in the middle of the previous year | swift.com CSP pages / Controls Policy (search snippet only: UNVERIFIED) |
| Mandatory vs advisory | Users must attest against all mandatory controls; advisory controls are optional | Customer Security Controls Policy (search snippet only: UNVERIFIED) |

## Assessment and certification
UNVERIFIED. Annual self-attestation in KYC-SA, which must be supported by an independent assessment (internal independent function such as second/third line, or an external assessor) per the Swift Independent Assessment Framework. Attestations are visible to counterparties on request; Swift may report non-attesting or non-compliant users to supervisors.

## Notes
- `framework-catalog.md` row "`+` SWIFT CSP | global | finance | security | self / attestation | M": broadly right, but "self" understates it: since CSCF v2021 attestations must be backed by an independent assessment (UNVERIFIED in this pass). Type should be "sector"; legal status contractual (Swift user obligation).
- Everything in this file is UNVERIFIED: www.swift.com returned an error/403 and www2.swift.com (knowledge centre PDFs) is not allowed by the sandbox network. The host names www.swift.com and www2.swift.com must be allowed to verify. Specifically check (a) whether CSCF v2027 has been published (expected around July 2026) and its control counts, (b) the 31 December attestation deadline, (c) mandatory/advisory counts for v2026.
