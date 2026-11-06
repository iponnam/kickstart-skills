---
id: pci-dss
name: PCI DSS
official_name: "Payment Card Industry Data Security Standard (PCI DSS) v4.0.1"
governing_body: PCI Security Standards Council (PCI SSC) maintains the standard; compliance is required and enforced by payment brands and acquirers
type: security
legal_status: contractual
region: global
industry: payments; any entity that stores, processes or transmits cardholder data
current_version: "PCI DSS v4.0.1 (published June 2024: UNVERIFIED date); v4.0 retired 31 December 2024"
superseded_by: none
official_sources:
  - title: "PCI Data Security Standard (PCI DSS) standard page"
    url: https://www.pcisecuritystandards.org/standards/pci-dss/
    accessed: 2026-11-06
  - title: "PCI SSC Document Library (featured: PCI DSS v4.0.1; Summary of Changes v4.0 to v4.0.1)"
    url: https://www.pcisecuritystandards.org/document_library/
    accessed: 2026-11-06
  - title: "PCI SSC Bulletin: SAQs for PCI DSS v4.0.1 Now Available (15 October 2024)"
    url: https://www.pcisecuritystandards.org/wp-content/uploads/2024/10/SAQs_for_PCI_DSS_v4.0.1_Bulletin.pdf
    accessed: 2026-11-06
  - title: "FAQ 1588: How does an e-commerce merchant meet the SAQ A eligibility criteria for scripts? (February 2025)"
    url: https://www.pcisecuritystandards.org/faqs/1588/
    accessed: 2026-11-06
  - title: "FAQ 1604: Do ASV scans in SAQ A apply to merchants with webpages that redirect to TPSPs or include TPSPs' embedded iframes? (June 2026)"
    url: https://www.pcisecuritystandards.org/faqs/1604
    accessed: 2026-11-06
  - title: "FAQ 1133: Why are there multiple PCI DSS Self-assessment Questionnaires (SAQs)? (April 2024)"
    url: https://www.pcisecuritystandards.org/faqs/1133/
    accessed: 2026-11-06
  - title: "FAQ 1328: Where can I find the current version of PCI DSS? (October 2024)"
    url: https://www.pcisecuritystandards.org/faq/articles/Frequently_Asked_Question/where-can-i-find-the-current-version-of-pci-dss/
    accessed: 2026-11-06
  - title: "FAQ 1565: Does an entity's PCI DSS assessment result expire when the standard ... is retired?"
    url: https://www.pcisecuritystandards.org/faq/articles/Frequently_Asked_Question/does-an-entity-s-pci-dss-assessment-result-expire-when-the-standard-against-which-the-entity-was-assessed-is-retired/
    accessed: 2026-11-06
last_verified: 2026-11-06T00:00:00Z
verification: partial
---

## What it is
"PCI DSS was developed to encourage and enhance payment card account data security and facilitate the broad adoption of consistent data security measures globally. PCI DSS provides a baseline of technical and operational requirements designed to protect payment account data" (PCI DSS standard page). The Document Library features "PCI DSS v4.0.1" and the "Summary of Changes v4.0 to v4.0.1" as the current documents. The SAQ bulletin states "The SAQs for PCI DSS v4.0 will remain active until PCI DSS v4.0 is retired on 31 December 2024."

## Who it applies to
"Entities that store, process, or transmit cardholder data (CHD) and/or sensitive authentication data (SAD) or could impact the security of the cardholder data environment (CDE). This includes all entities involved in payment card processing – including merchants, processors, acquirers, issuers, and service providers" (standard page). "Whether an entity is required to comply with or validate compliance to a PCI SSC standard is at the discretion of organizations that manage compliance programs, such as a payment brand, acquirer, or other entity" (standard page).

The 12 principal requirements (titles per PCI DSS v4.x; UNVERIFIED against the standard text because the PDF sits behind a Cloudflare challenge in this sandbox):
1. Install and maintain network security controls
2. Apply secure configurations to all system components
3. Protect stored account data
4. Protect cardholder data with strong cryptography during transmission over open, public networks
5. Protect all systems and networks from malicious software
6. Develop and maintain secure systems and software
7. Restrict access to system components and cardholder data by business need to know
8. Identify users and authenticate access to system components
9. Restrict physical access to cardholder data
10. Log and monitor all access to system components and cardholder data
11. Test security of systems and networks regularly
12. Support information security with organizational policies and programs

## Engineering obligations
| ID | Obligation | Official reference |
|---|---|---|
| Req 3 | Do not store SAD after authorization; protect stored PAN (truncation, tokenisation, strong cryptography) | Req 3 (UNVERIFIED text); FAQ title "why is storage of sensitive authentication data (SAD) after authorization not permitted" (verified on FAQ index) |
| Req 4 | Strong cryptography for PAN over open, public networks | Req 4 (UNVERIFIED text) |
| Req 6.4.3 | Manage all payment-page scripts loaded in the consumer's browser (authorise, ensure integrity, inventory with justification) | Req 6.4.3 named in FAQ 1588; detail UNVERIFIED |
| Req 11.6.1 | Change- and tamper-detection mechanism for payment pages (HTTP headers and script contents) | Req 11.6.1 named in FAQ 1588; detail UNVERIFIED |
| SAQ A script criterion | Iframe-embedding SAQ A merchants must confirm "their site is not susceptible to attacks from scripts that could affect the merchant's e-commerce system(s)", either by techniques "such as, but not limited to, those detailed in PCI DSS Requirements 6.4.3 and 11.6.1" or by confirmation from their PCI DSS compliant TPSP | FAQ 1588 |
| Req 11.3.2 | Quarterly external vulnerability scans by a PCI SSC Approved Scanning Vendor, including for SAQ A e-commerce webpages that redirect or embed a TPSP iframe | FAQ 1604 ("Requirements 11.3.2 and 11.3.2.1 were added to SAQ A") |
| Req 11.3.2.1 | External scans after any significant change | FAQ 1604 names 11.3.2.1; detail UNVERIFIED |
| Req 12.3.1 | Targeted risk analysis for requirements that allow flexible frequency | Req 12.3.1 (UNVERIFIED text; listed in PCI blog via search result only) |
| Req 6 | Secure development, vulnerability management and patching | Req 6 (UNVERIFIED text) |
| Req 7–8 | Need-to-know access; unique IDs; MFA for CDE access | Req 7, 8 (UNVERIFIED text) |
| Req 10 | Audit logs of all access to system components and cardholder data, reviewed | Req 10 (UNVERIFIED text) |
| Req 12.8 / 12.9 | Manage TPSPs; TPSPs acknowledge responsibility | Req 12.8, 12.9 (UNVERIFIED text) |
| SAQ selection | Confirm SAQ eligibility with the compliance-accepting entity (acquirer or payment brand) before self-assessing | SAQ bulletin; FAQ 1133; FAQ 1588 |

## Deadlines and numbers
| What | Value | Official reference |
|---|---|---|
| v4.0 retirement | "PCI DSS v4.0 is retired on 31 December 2024" | SAQ v4.0.1 Bulletin (15 Oct 2024) |
| v4.0.1 SAQs published | "15 October 2024" | SAQ v4.0.1 Bulletin |
| Future-dated requirements effective | 31 March 2025 (the date the v4.0 "best practice until" requirements become mandatory) | UNVERIFIED from standard text; FAQ 1564 title references requirements "noted in PCI DSS as best practices until a future date" |
| ASV scan frequency | Quarterly external ASV scan (Req 11.3.2) | FAQ 1604 names Req 11.3.2; "quarterly" UNVERIFIED from standard text |
| SAQ for service providers | "SAQ D for Service Providers is the ONLY SAQ for SAQ-eligible service providers. All other SAQs are for merchant use only." | FAQ 1133 |
| Assessment validity on retirement | "The period for which an entity's PCI DSS assessment result is valid does not change if the standard against which the entity was assessed has been retired" | FAQ 1565 |

## Assessment and certification
Validation is set by payment brands/acquirers, not PCI SSC: "how long an assessment result is valid and how frequently an entity must be reassessed is determined by organizations that manage compliance programs (for example, payment brands and acquirers)" (FAQ 1565). Routes: Report on Compliance (ROC) by a Qualified Security Assessor ("independent security organizations that have been qualified by the PCI Security Standards Council to validate an entity's adherence to PCI DSS", standard page) or Internal Security Assessor, or a Self-Assessment Questionnaire (SAQ) with Attestation of Compliance where eligible. ASV scans must be "performed by a PCI Approved Scan Vendor (ASV) listed as an Approved Scanning Vendor on the PCI SSC website" (FAQ 1604).

SAQ types (names as commonly published; eligibility detail UNVERIFIED because SAQ PDFs could not be downloaded): A (card-not-present, all account data functions fully outsourced to PCI DSS compliant TPSPs: redirect, iframe or fully outsourced), A-EP (e-commerce merchants whose website does not receive account data but can affect the security of the payment transaction, e.g. direct post / JavaScript form), B (imprint or standalone dial-out terminals), B-IP (standalone PTS-approved IP terminals), C-VT (manually entered virtual terminal on an isolated computer), C (payment application systems connected to the internet, no electronic storage), P2PE (validated P2PE solution hardware terminals), SPoC (software-based PIN entry on COTS; status UNVERIFIED), D for Merchants (all other merchants), D for Service Providers. The v4.0.1 bulletin confirms: "Clarifying SAQ Eligibility Criteria in SAQs A, A-EP, and C-VT" and "Adding a requirement to SAQ A and removing a requirement from SAQ C".

## Notes
- `control-checklists.md` PCI-03: "Vulnerability scan by an ASV quarterly if you have a public-facing payment page (SAQ-A-EP and above)" is wrong. FAQ 1604: SAQ A "includes requirements for external vulnerability scanning by a PCI SSC Approved Scanning Vendor (ASV) for merchant e-commerce webpages, even where payment processing is fully outsourced", including redirect and iframe pages.
- `control-checklists.md` PCI-02 says "iframe/redirect integrity (SRI on provider scripts, CSP)". Since SAQ A r1 (v4.0.1), 6.4.3/11.6.1 themselves are not SAQ A requirements; instead the SAQ A eligibility criterion requires iframe merchants to confirm the site is not susceptible to script attacks (by 6.4.3/11.6.1-style techniques or TPSP confirmation); it does not apply to redirect merchants (FAQ 1588). Reword accordingly.
- `control-checklists.md` heading "PCI DSS v4.0" and `framework-catalog.md` "PCI DSS v4.0" are outdated: v4.0 retired 31 December 2024; current is v4.0.1.
- `control-checklists.md` PCI-07 "Annual SAQ completion" is not a PCI SSC rule; reassessment frequency is set by acquirers/payment brands (FAQ 1565). Mark as "usually annual, per acquirer".
- `control-checklists.md` PCI-01 "Card data never ... transits your servers ... (SAQ-A scope)": SAQ A requires all account data functions be outsourced; fine in spirit but eligibility must be confirmed with the acquirer (FAQ 1133).
- UNVERIFIED: requirement titles, SAQ eligibility texts, the 31 March 2025 future-dated effective date (stated in PCI blog posts surfaced by search, but blog.pcisecuritystandards.org, listings.pcisecuritystandards.org and docs-prv (Cloudflare challenge) were unreachable from this sandbox). Re-verify against PCI-DSS-v4_0_1.pdf and the SAQ A/A-EP/D PDFs when access is available.
- No newer PCI DSS version than v4.0.1 is featured in the Document Library as of 2026-11-06.
