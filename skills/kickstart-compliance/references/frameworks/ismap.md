---
id: ismap
name: ISMAP (Japan government cloud)
official_name: Information system Security Management and Assessment Program (ISMAP), incl. ISMAP-LIU (low-impact use SaaS)
governing_body: ISMAP Steering Committee; operated by the National Cybersecurity Office, the Digital Agency, the Ministry of Internal Affairs and Communications and the Ministry of Economy, Trade and Industry, with technical support from IPA
type: security
legal_status: certification-scheme
region: Japan (government procurement)
industry: government, cloud (IaaS, PaaS, SaaS providers selling to Japanese government)
current_version: Basic Regulations (supplementary provisions enacted 3 July 2023 and 22 September 2023); Cloud Service Registration Rules June 3, 2020, last revised November 10, 2023; Control Criteria June 3, 2020, last revised September 22, 2023
superseded_by: none
official_sources:
  - title: ISMAP Overview (English reference page)
    url: https://www.ismap.go.jp/csm?id=kb_article_view&sysparm_article=KB0010301
    accessed: 2026-11-06
  - title: Basic Regulations for ISMAP (English reference PDF)
    url: https://www.ismap.go.jp/sys_attachment.do?sys_id=ac0c5b8a2b5fa250f0bbfd69fe91bfff
    accessed: 2026-11-06
  - title: ISMAP Cloud Service Registration Rules (English reference PDF)
    url: https://www.ismap.go.jp/sys_attachment.do?sys_id=fc0c9b8a2b5fa250f0bbfd69fe91bf0b
    accessed: 2026-11-06
  - title: Control Criteria of ISMAP (English reference PDF)
    url: https://www.ismap.go.jp/sys_attachment.do?sys_id=2c0c9b8a2b5fa250f0bbfd69fe91bf06
    accessed: 2026-11-06
  - title: ISMAP Cloud Service List
    url: https://www.ismap.go.jp/csm?id=cloud_service_list
    accessed: 2026-11-06
last_verified: 2026-11-06T00:00:00Z
verification: verified
---

## What it is
ISMAP "aims to secure the security level of the government's cloud service procurement by evaluating and registering cloud services that meet the security requirements of the government in advance". It is based on the "Basic Framework of the Security Assessment System for Cloud Services in Government Information Systems" (Cybersecurity Strategic Headquarters, 30 January 2020). Cloud services audited by a registered ISMAP audit institution against the Control Criteria are registered in the ISMAP Cloud Service List; "In principle, procurement ministries and agencies will procure cloud services from those listed".

## Who it applies to
Cloud service providers wishing to sell to Japanese government ministries and agencies (voluntary application; procurement-driven). ISMAP-LIU is a separate track for SaaS used for low-impact operations and information (ISMAP-LIU Cloud Service Registration Rules and impact evaluation guidance). The English pages are "for reference only, and the official version is only in Japanese".

## Engineering obligations
| ID | Obligation | Official reference |
|---|---|---|
| ISMAP-01 | Implement all Governance criteria and Management criteria "in principle" | Control Criteria, Ch. 2 (implementation) |
| ISMAP-02 | Implement all Controls criteria "as control objectives"; detailed controls ending in "B"/"PB" are baseline items | Control Criteria, Ch. 2 |
| ISMAP-03 | Criteria are built on JIS Q 27001:2014, 27002:2014, 27014:2015, 27017:2016 (ISO/IEC equivalents), referencing the Common Standards for Information Security Measures for Government Agencies (FY2023) and mapped to NIST SP 800-53 | Control Criteria Ch. 1; attached tables 4-7 |
| ISMAP-04 | Define the statement scope (service name, scope, controls implemented, assessment period); these are published on the Cloud Service List | Control Criteria 2.2; Registration Rules Ch. 7 |
| ISMAP-05 | Obtain an assessment by a registered ISMAP audit institution against the audit standards | ISMAP Overview; Basic Regulations Ch. 3-4 |
| ISMAP-06 | Report information security incidents that could have a serious impact on users: urgent report within three days, confirmed report within 30 days, with follow-up updates | Registration Rules Ch. 3 (applicant requirements), 9.1-9.3; Appendix 1 |
| ISMAP-07 | Report significant control changes or changes to listed information without delay | Registration Rules Ch. 3 (applicant requirements), Ch. 10 |
| ISMAP-08 | Renew registration before expiry (registration automatically revoked otherwise) and disclose changes after the previous assessment period | Registration Rules 8.1; Basic Regulations 3.5 |

## Deadlines and numbers
| What | Value | Official reference |
|---|---|---|
| Incident urgent report | "in principle, within three days (not including holidays of government agencies) from the date of recognizing the occurrence" | Registration Rules 9.2 |
| Incident confirmed report | "in principle, within 30 days from the date of recognizing the occurrence of an information security incident" | Registration Rules 9.3 |
| Registration validity (cloud service) | "from the day after the last day of the assessment period covered by the registration to 16 months later" | Basic Regulations 3.5 |
| Audit institution registration validity | "two years from the date of decision of registration" | Basic Regulations 4.4 |
| Application document check | "in principle within two weeks from the date of receipt" | Registration Rules 5.3 |

## Assessment and certification
Third-party assessment by audit institutions listed on the ISMAP Audit Institutions List, following the ISMAP Information Security Assessment Guidelines; the ISMAP Steering Committee examines and registers the service in the ISMAP Cloud Service List. Registration effectively runs on a yearly assessment cycle (16-month validity window); suspension or revocation is possible on monitoring results or failure to report incidents (Basic Regulations 5.4; Registration Rules 9.5).

## Notes
- Catalog row "ISMAP ... certification ... Cloud services for Japanese government" is correct. Add ISMAP-LIU for low-impact SaaS, and that registration is a listing (not a certificate), valid until 16 months after the end of the assessment period.
- English documents are reference translations; the Japanese originals govern.
