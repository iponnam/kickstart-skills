---
id: ccpa-cpra
name: CCPA / CPRA
official_name: California Consumer Privacy Act of 2018 (Cal. Civ. Code § 1798.100 et seq.) as amended by the California Privacy Rights Act of 2020 (Proposition 24); CCPA Regulations, Cal. Code Regs. tit. 11, div. 6, ch. 1 (§ 7000 et seq.)
governing_body: California Privacy Protection Agency (CPPA, now styled "CalPrivacy"); California Attorney General (concurrent enforcement)
type: privacy
legal_status: law
region: US-CA (businesses that do business in California, wherever located)
industry: any
current_version: CCPA statute as posted by CPPA "effective 01/01/2026 – AB 137, AB 566 update"; CCPA Regulations "Effective 1/1/2026" (2025 package adopted July 24, 2025, approved by OAL September 22, 2025)
superseded_by: none
official_sources:
  - title: California Consumer Privacy Act of 2018, statute text effective 01/01/2026 (CPPA PDF)
    url: https://cppa.ca.gov/pdf/20260101_ccpa_statute.pdf
    accessed: 2026-11-06
  - title: CCPA Regulations, Effective 1/1/2026 (CPPA PDF)
    url: https://cppa.ca.gov/regulations/pdf/ccpa_statute_eff_20260101.pdf
    accessed: 2026-11-06
  - title: CCPA Updates, Cybersecurity Audits, Risk Assessments, ADMT, and Insurance Regulations (rulemaking page)
    url: https://cppa.ca.gov/regulations/ccpa_updates.html
    accessed: 2026-11-06
  - title: Updated Monetary Thresholds in CCPA (effective 1/1/2025)
    url: https://cppa.ca.gov/regulations/cpi_adjustment.html
    accessed: 2026-11-06
  - title: CPPA Law & Regulations page
    url: https://cppa.ca.gov/regulations/
    accessed: 2026-11-06
last_verified: 2026-11-06T00:00:00Z
verification: verified
---

## What it is
The CCPA gives California consumers rights to know, delete, correct, opt out of sale or sharing, limit use of sensitive personal information, and (from the 2025 regulations) to access and opt out of certain uses of automated decisionmaking technology (ADMT). Proposition 24 (November 2020) amended the CCPA and established the Agency, which is "responsible for implementing and enforcing the CCPA as well as the Delete Act" (CPPA Law & Regulations page). The 2025 regulations "(1) updated existing CCPA regulations; (2) implemented requirements for certain businesses to conduct risk assessments and complete annual cybersecurity audits; (3) implemented consumers' rights to access and opt–out of businesses' use of ADMT; and (4) clarified when insurance companies must comply" (ccpa_updates page).

## Who it applies to
A for-profit entity that collects consumers' personal information, determines purposes and means, "does business in the State of California, and that satisfies one or more of the following thresholds" (Civ. Code § 1798.140(d)(1)):
- (A) annual gross revenues in excess of $25,000,000 in the preceding calendar year, "as adjusted pursuant to subdivision (d) of Section 1798.199.95"; currently $26,625,000 (effective January 1, 2025, CPPA thresholds page);
- (B) "annually buys, sells, or shares the personal information of 100,000 or more consumers or households";
- (C) "Derives 50 percent or more of its annual revenues from selling or sharing consumers' personal information".

## Engineering obligations
| ID | Obligation | Official reference |
|---|---|---|
| CCPA-01 | Privacy policy and notice at collection | Regs §7011, §7012; Civ. Code §1798.100, §1798.130 |
| CCPA-02 | "Do Not Sell or Share My Personal Information" link and "Limit the Use of My Sensitive Personal Information" link (or alternative opt-out link) | Regs §7013, §7014, §7015; Civ. Code §1798.135 |
| CCPA-03 | Process opt-out preference signals (e.g., browser signals) as valid opt-out requests | Regs §7025; Civ. Code §1798.135 |
| CCPA-04 | Stop selling/sharing "no later than 15 business days" after an opt-out request and notify third parties | Regs §7026(f)(1) |
| CCPA-05 | Request intake methods for delete, correct, know; confirm receipt within 10 business days | Regs §7020, §7021(a) |
| CCPA-06 | Respond to delete/correct/know/ADMT access/ADMT appeal within 45 calendar days (extendable once by 45) | Regs §7021(b); Civ. Code §1798.130(a)(2) |
| CCPA-07 | Opt-in consent for sale/sharing of personal information of consumers under 16 (parent/guardian for under 13); wait 12 months before re-asking after refusal | Civ. Code §1798.120(c); §1798.135 |
| CCPA-08 | Implement reasonable security procedures; private right of action for breaches of nonencrypted/nonredacted personal information | Civ. Code §1798.100(e); §1798.150 |
| CCPA-09 | Cybersecurity audit by businesses whose processing presents significant risk to security (50% revenue from selling/sharing, or revenue threshold plus 250,000+ consumers/households or 50,000+ consumers' sensitive PI) | Regs §7120-§7124 |
| CCPA-10 | Risk assessment before initiating significant-risk processing: selling/sharing, processing sensitive PI, ADMT for significant decisions, certain automated inferences, training ADMT | Regs §7150-§7156 |
| CCPA-11 | Submit risk assessment information to the Agency | Regs §7157 |
| CCPA-12 | ADMT for significant decisions: pre-use notice, opt-out, access requests | Regs §7200, §7220-§7222 |
| CCPA-13 | Browser developers must include a configurable opt-out preference signal (operative January 1, 2027) | Civ. Code §1798.136(a), (f) |
| CCPA-14 | Service provider/contractor contracts with required terms | Civ. Code §1798.100(d); Regs §7051 |

## Deadlines and numbers
| What | Value | Official reference |
|---|---|---|
| Revenue threshold | $26,625,000 (adjusted from $25,000,000), effective 1/1/2025 | CPPA thresholds page; Civ. Code §1798.140(d)(1)(A) |
| Volume threshold | "100,000 or more consumers or households" | §1798.140(d)(1)(B) |
| Selling/sharing revenue threshold | "50 percent or more of its annual revenues" | §1798.140(d)(1)(C) |
| Data subject request response | "no later than 45 calendar days after receipt"; up to an additional 45 days, "maximum total of 90 calendar days" | Regs §7021(b); Civ. Code §1798.130 ("within 45 days") |
| Acknowledge request | "No later than 10 business days" | Regs §7021(a) |
| Opt-out of sale/sharing | "no later than 15 business days" | Regs §7026(f)(1) |
| Age threshold (sale/sharing opt-in) | under 16; under 13 requires parent or guardian | Civ. Code §1798.120(c) |
| Administrative fines | "Not more than $2,663 for each violation or $7,988 for each intentional violation" and violations involving known minors under 16 (adjusted 1/1/2025) | CPPA thresholds page; §1798.155 |
| Statutory damages (breach private action) | "Not less than $107 and not greater than $799 per consumer per incident or actual damages" (adjusted 1/1/2025) | CPPA thresholds page; §1798.150(a)(1)(A) |
| 2025 regulations effective | "Effective Date: January 1, 2026" | ccpa_updates page |
| First cybersecurity audit report | April 1, 2028 (2026 revenue > $100M); April 1, 2029 ($50M-$100M); April 1, 2030 (< $50M); then annually by April 1 | Regs §7121(a), (b) |
| Risk assessments for processing ongoing before 2026 | complete "no later than December 31, 2027" | Regs §7155(b) |
| Risk assessment review | "At least once every three years"; update within 45 calendar days of a material change | Regs §7155(a)(2), (a)(3) |
| Risk assessment retention | as long as processing continues or "five years after the completion of the risk assessment, whichever is later" | Regs §7155(c) |
| Risk assessment submission | 2026-2027 assessments "no later than April 1, 2028"; thereafter by April 1 following year | Regs §7157(a) |
| ADMT compliance | businesses using ADMT for significant decisions before 2027 must comply "no later than January 1, 2027" | Regs §7200(b) |
| Browser opt-out signal duty | "operative on January 1, 2027" | Civ. Code §1798.136(f) |

## Assessment and certification
No certification. Covered businesses must complete an independent cybersecurity audit (internal or external auditor meeting independence requirements, Regs §7122) and submit a certification of completion (Regs §7124). Enforcement by the CPPA (administrative) and the Attorney General (civil); private right of action limited to data breaches (§1798.150).

## Notes
- Catalog row "CCPA / CPRA ... California residents' data above thresholds (revenue, volume, or data sales)" is correct; suggest stating the current adjusted revenue threshold of $26,625,000 and 100,000 consumers or households.
- control-checklists.md PRIV-05 "CCPA 45d" is correct for response; add 10-business-day acknowledgment and 15-business-day opt-out deadline.
- control-checklists.md CCPA row says "annual risk assessment and cybersecurity audit for high-risk businesses". Correction: cybersecurity audits are annual (after phased first deadlines 2028-2030), but risk assessments are required before initiating the processing and reviewed at least every three years, not annually (Regs §7155). Add ADMT obligations (from January 1, 2027) and the browser OOPS duty (January 1, 2027).
- Monetary thresholds are adjusted every odd-numbered year (§1798.199.95(d)); a January 1, 2027 adjustment may follow. The CPPA page also notes it has "no proposed regulation packages at this time" (checked 2026-11-06), with preliminary activity on OOPS, employee data, notices, and friction reduction.
- oag.ca.gov responded (HTTP 200) but was not needed; facts come from cppa.ca.gov official texts.
