---
id: appi-japan
name: APPI (Japan)
official_name: Act on the Protection of Personal Information (Act No. 57 of 2003), with the Rules for Enforcement of the Act on the Protection of Personal Information (Rules of the Personal Information Protection Commission No. 3 of 2016)
governing_body: Personal Information Protection Commission (PPC), Japan
type: privacy
legal_status: law
region: Japan; also applies to businesses that, "in relation to supplying a good or service to a person in Japan", handle that person's personal information "in a foreign country" (Art. 171)
industry: any (private-sector "business handling personal information"; Chapter V separately covers administrative entities)
current_version: Act No. 57 of 2003, official English translation reflecting amendments up to "Act No. 37 of 2021"; Enforcement Rules translation reflecting "Rules of the Personal Information Protection Commission No. 5 of 2024"
superseded_by: none
official_sources:
  - title: Act on the Protection of Personal Information (Act No. 57 of 2003) - English - Japanese Law Translation (Ministry of Justice)
    url: https://www.japaneselawtranslation.go.jp/en/laws/view/4241/en
    accessed: 2026-11-06
  - title: Rules for Enforcement of the Act on the Protection of Personal Information - English - Japanese Law Translation
    url: https://www.japaneselawtranslation.go.jp/en/laws/view/5226/en
    accessed: 2026-11-06
  - title: PPC - Laws and Policies (English) (Playwright returned PPC's 503 "high traffic" notice listing the leak-report portal)
    url: https://www.ppc.go.jp/en/legal/
    accessed: 2026-11-06
  - title: PPC leakage report submission portal (private businesses), as listed on the PPC notice page
    url: https://roueihoukoku.ppc.go.jp/incident/?top=r2.kojindata
    accessed: 2026-11-06
last_verified: 2026-11-06T00:00:00Z
verification: verified
---

## What it is
Japan's general personal information protection statute. Its purpose is "to protect the rights and interests of individuals" while recognising the value of using personal information, by setting basic principles, obligations for businesses and administrative entities, and establishing the Personal Information Protection Commission (Art. 1). Detailed requirements (breach reporting content and deadlines, record-keeping periods, cross-border transfer information) are set by the PPC's Enforcement Rules.

## Who it applies to
- "Business handling personal information": "a person that uses a personal information database or the equivalent for business", excluding national government organs, local governments and other listed public bodies (Art. 16(2)). "Personal information database or the equivalent" includes collections "systematically organized so as to be searchable for particular personal information using a computer" (Art. 16(1)(i)).
- No size threshold appears in Art. 16(2).
- Extraterritorial: the Act "also applies" where, "in relation to supplying a good or service to a person in Japan", a business handles that person's personal information (or pseudonymized/anonymized information derived from it) "in a foreign country" (Art. 171).
- Administrative entities are covered by Chapter V (e.g., Art. 68 leak reporting).
- "Sensitive personal information" covers race, creed, social status, medical history, criminal record, having suffered damage by a crime and other Cabinet Order items (Art. 2(3)).

## Engineering obligations
| ID | Obligation | Official reference |
|---|---|---|
| APPI-17 | Specify the purpose of use "as much as possible"; do not handle personal information beyond it without prior consent | Arts. 17(1), 18(1) |
| APPI-20 | No acquisition by deception or wrongful means; obtain prior consent before acquiring sensitive personal information (subject to exceptions) | Art. 20(1)-(2) |
| APPI-21 | Promptly notify the person of, or publish, the purpose of use once personal information is acquired | Art. 21(1) |
| APPI-22 | Keep personal data accurate and up to date, and "delete the personal data without delay if they no longer require it" (endeavour duty) | Art. 22 |
| APPI-23 | Take "necessary and appropriate measures for managing the security of personal data including preventing the leaking, loss or damage" | Art. 23 |
| APPI-24/25 | Supervise employees and entrusted persons (processors) handling personal data | Arts. 24, 25 |
| APPI-26a | Report qualifying leaks, loss or damage to the PPC (preliminary report "promptly", full report within 30/60 days) via the PPC electronic system | Art. 26(1); Rules Arts. 7, 8 |
| APPI-26b | Notify affected individuals "promptly" of qualifying incidents (items (i), (ii), (iv), (v), (ix) of Rules Art. 8(1)), unless difficult and alternative measures are taken | Art. 26(2); Rules Art. 10 |
| APPI-26c | An entrusted processor may instead notify the entrusting business "promptly" | Art. 26(1) proviso; Rules Art. 9 |
| APPI-27 | Prior consent before providing personal data to a third party, except listed cases (opt-out route needs PPC notification and public disclosure) | Art. 27(1), (2), (4); Rules Art. 14 |
| APPI-28 | Transfers to third parties in a foreign country: consent after giving information on the foreign country's system and the recipient's measures, unless the country is PPC-recognised or the recipient has an "equivalent measures" system; for the latter, ensure continuous implementation and inform the person on request | Art. 28(1)-(3); Rules Art. 18 |
| APPI-29/30 | Keep records of personal data provided to and received from third parties, prepared "promptly each time" (bulk records allowed for continuous provision) | Arts. 29, 30; Rules Arts. 19-21 |
| APPI-32 | Make information about retained personal data (business name and address, purposes of use, request procedures, and Cabinet Order matters) accessible to identifiable persons | Art. 32(1) |
| APPI-33 | Disclose retained personal data "without delay by means that person requests" (including electronic records), subject to listed exceptions | Art. 33(1)-(2) |
| APPI-34/35 | Handle correction, addition, deletion, and cease-use/deletion/cease-provision requests; notify the result "without delay" | Arts. 34, 35 |
| APPI-37 | A method for receiving rights requests may be specified | Art. 37(1) |
| APPI-40 | Process complaints "appropriately and promptly" | Art. 40(1) |
| APPI-41 | Pseudonymized information: process to PPC standards so individuals cannot be identified unless collated with other information; no third-party provision except under laws | Arts. 41, 42 |
| APPI-43/45 | Anonymized information: process to PPC standards, disclose categories and means when providing to third parties, never re-identify | Arts. 43-45 |

## Deadlines and numbers
| What | Value | Official reference |
|---|---|---|
| Preliminary leak report to PPC | "promptly after the business handling personal information becomes aware of the relevant situations" | Rules Art. 8(1) |
| Full leak report to PPC | "within 30 days after the business handling personal information becomes aware of the relevant situation (or within 60 days if the relevant situation is the one prescribed by item (iii) of the preceding Article)" (item (iii) = leakage arising from an act possibly for wrongful purposes) | Rules Art. 8(2), Art. 7(iii) |
| Reportable situations | sensitive personal information (unless "advanced encryption or other necessary measures" taken); data that could cause property damage; acts for wrongful purposes; "the number of persons identifiable by the personal data exceeds 1,000" | Rules Art. 7(i)-(iv) |
| Notification to individuals | "promptly after becoming aware" | Rules Art. 10 |
| Disclosure request response | "without delay" | Art. 33(2) |
| Third-party provision/receipt record retention | one year from last provision (records of Art. 19(3) type), three years (bulk records), otherwise "three years" | Rules Art. 21 (and parallel article for receipt records) |
| Penalty: violating a PPC order | "imprisonment with work for not more than one year or to a fine of not more than 1,000,000 yen" (individual) | Art. 178 |
| Penalty: providing/misappropriating a database for illegal profit | "imprisonment with work for not more than one year or to a fine of not more than 500,000 yen" (individual) | Art. 179 |
| Corporate fine for Arts. 178-179 | "a fine of not more than 100 million yen" | Art. 184(1)(i) |
| Failure to report / false report to PPC | "a fine of not more than 500,000 yen" | Art. 182 |

## Assessment and certification
No mandatory certification or audit. The PPC supervises (reports, inspections, guidance, recommendations and orders; violations of orders are punishable under Art. 178). The Act provides for PPC-certified "personal information protection organizations" (accredited bodies handling complaints for member businesses; Arts. 47-51), which is not a product certification.

## Notes
- Assignment claims now verified: preliminary report to PPC "promptly" and full report within 30 days, or 60 days for leaks from acts for wrongful purposes (Rules Art. 8). The "about 3-5 days" gloss for "promptly" is not in the Rules text; it comes from PPC guidelines that were not read (PPC site returned a 503 high-traffic page), so it stays UNVERIFIED.
- Previous catalog row "APPI | JP | any | privacy | law | M | Personal information in Japan" is accurate; it could add the extraterritorial reach (Art. 171) and the 1,000-person reporting threshold.
- The Japanese Law Translation texts are official translations, but only the Japanese text is legally binding; the translation's "Last Version" is Act No. 37 of 2021. Whether later amendments to the Act (for example a PPC triennial-review amendment bill) have been enacted since is UNVERIFIED.
- PPC guidelines (General Rules Guidelines, Q&A) were not read; any guideline-level interpretations remain UNVERIFIED.
