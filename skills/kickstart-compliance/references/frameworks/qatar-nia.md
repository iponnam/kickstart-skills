---
id: qatar-nia
name: Qatar NIA
official_name: National Information Assurance (NIA) Policy / Standard (certification currently against NIA V2.1) under the National Information Security Compliance Framework (NISCF)
governing_body: National Cyber Security Agency (NCSA), Qatar - National Cyber Governance and Assurance Affairs
type: security
legal_status: binding-regulation
region: Qatar
industry: government (mandatory per NCSA material); others voluntary/optional unless extended
current_version: NIA V2.1 (named in NCSA certification service request form); NIA policy text itself not retrieved
superseded_by: UNVERIFIED
official_sources:
  - title: NCSA home page (agency established by Emiri Decision No. 1 of 2021)
    url: https://www.ncsa.gov.qa/en
    accessed: 2026-11-06
  - title: NIA V2.1 Certification Service Request Form [NCSA-NISCF-CERT-NIA-RQTF]
    url: https://www.ncsa.gov.qa/shared/document_library/94787172324409/33000/1826/1.0~356b00f9-56d2-40d8-9eaa-56bd57b3e7cc?mimetype=application%2Fpdf&filename=NCSA-NISCF-CERT-NIAV2.1-RQTF-V1.0+%28NIA+Certification++Service+Request+Form+-+Public%29_1+%281%29.pdf
    accessed: 2026-11-06
  - title: NISCF Audit Standard [NCSA-NCGAA-NISCF-AS] V1.1
    url: https://www.ncsa.gov.qa/shared/document_library/94787172324409/33000/3007/1.0~21728f23-512f-4700-b6e5-209dbc823f7b?mimetype=application%2Fpdf&filename=ExternalE.pdf
    accessed: 2026-11-06
  - title: NIA Workshop Slides (14 March 2019)
    url: https://www.ncsa.gov.qa/shared/document_library/94787172324409/33000/8833/1.0~0bc50a6a-0230-4f8c-8f17-c181ad801085?mimetype=application%2Fpdf&filename=NIA_Workshop_Slides_20190314+%281%29.pdf
    accessed: 2026-11-06
last_verified: 2026-11-06T00:00:00Z
verification: partial
---

## What it is
Qatar's national information assurance control set, run by NCSA under the National Information Security Compliance Framework (NISCF). NCSA material describes the "National Information Assurance Policy" as the control set that compliance certification is based on, with "26 domains" and baseline controls that are "mandatory (subject to applicability)", selected through a business impact / classification approach and documented in a Statement of Applicability (Workshop Slides; NISCF Audit Standard App. B 1.2). The NIA Policy/Manual text itself could not be retrieved in this session.

## Who it applies to
Workshop Slides: "Evidencing compliance with the NIA and SSQA standards is mandatory for the government sector. NIA compliance may be extended to other organizations at a later stage." Other organisations can certify voluntarily. NCSA itself was established by Emiri Decision No. 1 of 2021 (NCSA home page; NISCF Audit Standard).

## Engineering obligations
| ID | Obligation | Official reference |
|---|---|---|
| NIA-01 | Define the certification scope, asset classification and Statement of Applicability before audit | NISCF Audit Standard App. B 1.2; Request Form (h) |
| NIA-02 | Implement applicable NIA baseline controls selected per the NIA Policy and Manual; justify non-applicable baselines | NISCF Audit Standard App. B 1.2 |
| NIA-03 | Classify and label information per NIA Policy and Manual | NISCF Audit Standard (evidence handling, line "in accordance with NIA Policy and Manual, the auditee's classification, labelling and security policies") |
| NIA-04 | Keep operating evidence (logs, tracks, requests, changes) for an audit period of 3-12 months | NISCF Audit Standard App. B 1.1.2-1.1.3 |
| NIA-05 | Name a contact responsible for all NIA certification matters; use NCSA-accredited service providers for audit | Request Form; Workshop Slides |
| NIA-06 | Re-assess when changes materially affect control applicability (certificate otherwise invalidated) | Workshop Slides |
| NIA-07 | Undergo surveillance audits and remediate findings | NISCF Audit Standard s.3.5 |

## Deadlines and numbers
| What | Value | Official reference |
|---|---|---|
| Audit period | "shall not exceed 12 months" and "shall not be shorter than 3 months" | NISCF Audit Standard App. B 1.1.2-1.1.3 |
| Audit records retention (by auditors) | "retention period of two years" | NISCF Audit Standard (records section) |
| Number of NIA domains | "26 domains" | Workshop Slides (2019; may predate V2.1) |

## Assessment and certification
Independent audit by an NCSA-accredited service provider, scope validated by National Cyber Governance and Assurance Affairs, certification decision by NCSA; surveillance audits follow. Certificate validity (reported elsewhere as 3 years with annual maintenance) is UNVERIFIED because the NCSA certification page failed to load.

## Notes
- Catalog row "Qatar NIA | government, critical | security | law" overstates it as a law; it is an NCSA-mandated standard for government, with certification under NISCF. Current version is V2.1 (form title).
- The NIA Policy/Standard text, its control IDs, domain list for V2.1 and any incident reporting window were not retrievable (ncsa.gov.qa without www, assurance.ncsa.gov.qa and qcert.ncsa.gov.qa are blocked here; NCSA SPA pages returned an error). Older "NIA Manual v2.0 (2018, MOTC)" exists on qcert.ncsa.gov.qa (not fetched).
