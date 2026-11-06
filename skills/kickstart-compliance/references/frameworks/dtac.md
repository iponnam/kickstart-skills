---
id: dtac
name: DTAC
official_name: Digital Technology Assessment Criteria for health and social care (DTAC)
governing_body: NHS England (Transformation Directorate; formerly NHSX)
type: sector
legal_status: regulator-guideline
region: England (NHS and social care buyers)
industry: health
current_version: UNVERIFIED (official site unreachable)
superseded_by: UNVERIFIED
official_sources:
  - title: NHS England Transformation Directorate - Digital Technology Assessment Criteria (DTAC) (not reachable from sandbox)
    url: https://transform.england.nhs.uk/key-tools-and-info/digital-technology-assessment-criteria-dtac/
    accessed: 2026-11-06
  - title: DHSC, A guide to good practice for digital and data-driven health technologies (gov.uk; related guidance, not DTAC itself)
    url: https://www.gov.uk/government/publications/code-of-conduct-for-data-driven-health-and-care-technology/initial-code-of-conduct-for-data-driven-health-and-care-technology
    accessed: 2026-11-06
last_verified: never
verification: unreachable
---

## What it is
UNVERIFIED. The official NHS England DTAC page could not be reached. Background, not verified: DTAC is the NHS's baseline assessment that health and social care buyers use to assess digital health technologies before procurement.

## Who it applies to
UNVERIFIED. Background, not verified: suppliers of digital health technologies (apps, software, platforms) to NHS and social care organisations in England.

## Engineering obligations
| ID | Obligation | Official reference |
|---|---|---|
| DTAC-C1 | Clinical safety: comply with DCB0129 (manufacturer clinical risk management), with a named Clinical Safety Officer, clinical risk management file and hazard log. Buyers deploy under DCB0160. UNVERIFIED | DTAC section C1 (UNVERIFIED) |
| DTAC-C2 | Data protection: UK GDPR compliance, DPIA, NHS Data Security and Protection Toolkit. UNVERIFIED | DTAC section C2 (UNVERIFIED) |
| DTAC-C3 | Technical security: Cyber Essentials certification, penetration testing, secure development practices. UNVERIFIED | DTAC section C3 (UNVERIFIED) |
| DTAC-C4 | Interoperability: open standards and APIs; FHIR/NHS standards where relevant. UNVERIFIED | DTAC section C4 (UNVERIFIED) |
| DTAC-D1 | Usability and accessibility: accessibility standard conformance (WCAG level and version UNVERIFIED) | DTAC section D1 (UNVERIFIED) |

## Deadlines and numbers
None verified.

## Assessment and certification
UNVERIFIED. Background, not verified: the supplier completes the DTAC form and supplies evidence, and the buying organisation assesses it. It is not a certification.

## Notes
- **Follow-up pass (2026-11-06):** www.gov.uk is now reachable, but a gov.uk search (search API for "digital technology assessment criteria", "DTAC NHS") found no DTAC page or document; DTAC is published only by NHS England (transform.england.nhs.uk, still unreachable upstream). The file therefore stays `unreachable`. The related DHSC "guide to good practice for digital and data-driven health technologies" on gov.uk (last updated 19 January 2021) states: "To sell into the NHS, manufacturers must demonstrate compliance with the Clinical Safety Standards referred to as DCB0129 and DCB0160. This is mandated under the Health and Social Care Act 2012", and that DCB0129 needs a clinical safety management system, a hazard log, a clinical safety case report and a clinical safety management plan, shared with customers for their DCB0160 duty. This supports the substance of DTAC-C1 but does not confirm DTAC's own wording. The same guide lists "WCAG 2.1 for accessibility" among recommended open standards (2021); that is not evidence of the current DTAC requirement (2.1 vs 2.2 still UNVERIFIED).
- **Unreachable (first pass):** transform.england.nhs.uk, england.nhs.uk, digital.nhs.uk and gov.uk all failed at the proxy (CONNECT refused or tunnel failure) from this sandbox on 2026-11-06, including via Playwright. Nothing in this file is verified. Every row above is background knowledge marked UNVERIFIED and must be checked before release.
- **Catalog check (not verifiable):** control-checklists.md lists five areas (clinical safety DCB0129/DCB0160; data protection; technical security incl. Cyber Essentials, pen test, MFA; interoperability; usability and accessibility, "WCAG 2.2 AA"). None of this could be confirmed. The WCAG version (2.1 vs 2.2) and the current DTAC version number in particular need checking against the NHS England page. framework-catalog.md line 38 labels audit type "self". That is plausible (supplier self-declaration assessed by the buyer) but UNVERIFIED.
- To complete: allow transform.england.nhs.uk (and digital.nhs.uk for DCB0129/DCB0160 standard pages) in the session's network settings and re-run.
