---
id: gdpr
name: GDPR
official_name: Regulation (EU) 2016/679 of the European Parliament and of the Council of 27 April 2016 on the protection of natural persons with regard to the processing of personal data and on the free movement of such data (General Data Protection Regulation)
governing_body: European Parliament and Council of the EU (legislator); enforced by national supervisory authorities (Art. 51, 55) coordinated by the European Data Protection Board
type: privacy
legal_status: law
region: EU (Art. 3(1) establishment in the Union); extraterritorial for controllers/processors not established in the Union that offer goods or services to, or monitor the behaviour of, data subjects "who are in the Union" (Art. 3(2))
industry: any
current_version: Regulation (EU) 2016/679, applies from 25 May 2018 (Art. 99(2)); Digital Omnibus amendments are proposals only (not adopted as of 2026-11-06)
superseded_by: none
official_sources:
  - title: Regulation (EU) 2016/679, original text as adopted by the EU (legislation.gov.uk "Original (As adopted by EU)" view of the OJ text), Arts. 3, 7, 8, 12, 15, 17, 20, 21, 25, 27, 28, 30, 32, 33, 34, 35, 37, 44, 83, 99
    url: https://www.legislation.gov.uk/eur/2016/679/contents/adopted
    accessed: 2026-11-06
  - title: Article 33 (original EU text)
    url: https://www.legislation.gov.uk/eur/2016/679/article/33/adopted
    accessed: 2026-11-06
  - title: Article 12 (original EU text)
    url: https://www.legislation.gov.uk/eur/2016/679/article/12/adopted
    accessed: 2026-11-06
  - title: Article 83 (original EU text)
    url: https://www.legislation.gov.uk/eur/2016/679/article/83/adopted
    accessed: 2026-11-06
  - title: European Commission, Digital Rulebook / Digital Omnibus page
    url: https://digital-strategy.ec.europa.eu/en/policies/digital-rulebook
    accessed: 2026-11-06
  - title: Regulation (EU) 2016/679, Official Journal text as published (Publications Office of the EU, CELEX 32016R0679)
    url: https://publications.europa.eu/resource/cellar/3e485e15-11bd-11e6-ba9a-01aa75ed71a1.0006.03/DOC_1
    accessed: 2026-11-06
  - title: Decision of the EEA Joint Committee No 154/2018 of 6 July 2018 incorporating Regulation (EU) 2016/679 into the EEA Agreement (OJ L 183, 19.7.2018)
    url: https://publications.europa.eu/resource/cellar/03c28303-8b25-11e8-8a53-01aa75ed71a1.0006.03/DOC_1
    accessed: 2026-11-06
last_verified: 2026-11-06T00:00:00Z
verification: verified
---

## What it is
The EU's general data protection law. It sets the principles for processing personal data, lawful bases, data subject rights, controller and processor obligations (security, breach notification, DPIA, records, DPO), rules for transfers to third countries, and administrative fines. It applies directly in every Member State from 25 May 2018 (Art. 99(2)).

## Who it applies to
- Art. 3(1): processing "in the context of the activities of an establishment of a controller or a processor in the Union, regardless of whether the processing takes place in the Union or not."
- Art. 3(2): controllers or processors not established in the Union that process personal data of data subjects "who are in the Union", where the processing relates to (a) "the offering of goods or services, irrespective of whether a payment of the data subject is required", or (b) "the monitoring of their behaviour as far as their behaviour takes place within the Union".
- Art. 27(1): where Art. 3(2) applies, the controller or processor "shall designate in writing a representative in the Union" (exceptions in Art. 27(2), e.g. occasional processing not involving large-scale special-category data).
- Art. 30(5): the records obligation does not apply to an organisation "employing fewer than 250 persons" unless the processing is likely to result in a risk, is not occasional, or includes special-category or criminal-offence data.

## Engineering obligations
| ID | Obligation | Official reference |
|---|---|---|
| Art. 25 | Data protection by design and by default: implement appropriate technical and organisational measures at design time and at the time of processing | Art. 25(1) |
| Art. 7 | Be able to demonstrate consent; present the consent request distinguishably and in plain language; withdrawal must be possible | Art. 7(1)–(3) |
| Art. 8 | Child consent for information society services: lawful at 16+, below that only with parental authorisation; make "reasonable efforts to verify" parental consent "taking into consideration available technology" | Art. 8(1)–(2) |
| Art. 12 | Provide information and communications in a "concise, transparent, intelligible and easily accessible form"; when a request is made electronically, respond electronically where possible | Art. 12(1), 12(3) |
| Art. 15 | Right of access: confirm processing and provide a copy plus the listed information | Art. 15 |
| Art. 17 | Right to erasure "without undue delay" where a listed ground applies | Art. 17(1) |
| Art. 20 | Data portability "in a structured, commonly used and machine-readable format" | Art. 20(1) |
| Art. 21 | Right to object (including to profiling based on Art. 6(1)(e)/(f)) | Art. 21 |
| Art. 28 | Use only processors giving sufficient guarantees; sub-processors only with prior written authorisation of the controller; written processor contract | Art. 28(1)–(3) |
| Art. 30 | Maintain records of processing activities (purposes, categories, recipients, transfers, erasure time limits, description of security measures), in writing including electronic form, available to the supervisory authority on request | Art. 30(1)–(4) |
| Art. 32(1)(a) | "the pseudonymisation and encryption of personal data" | Art. 32(1)(a) |
| Art. 32(1)(b) | Ensure "the ongoing confidentiality, integrity, availability and resilience of processing systems and services" | Art. 32(1)(b) |
| Art. 32(1)(c) | "the ability to restore the availability and access to personal data in a timely manner" after an incident (backup/restore) | Art. 32(1)(c) |
| Art. 32(1)(d) | "a process for regularly testing, assessing and evaluating the effectiveness" of security measures | Art. 32(1)(d) |
| Art. 33(1) | Notify the supervisory authority of a personal data breach without undue delay and where feasible within 72 hours of becoming aware, unless the breach is unlikely to result in a risk | Art. 33(1) |
| Art. 33(2) | Processor notifies the controller "without undue delay after becoming aware" of a breach | Art. 33(2) |
| Art. 33(5) | Document every personal data breach (facts, effects, remedial action) so that the supervisory authority can verify compliance | Art. 33(5) |
| Art. 34 | Tell data subjects about high-risk breaches without undue delay; not required if the data were rendered unintelligible, e.g. by encryption | Art. 34(1), 34(3)(a) |
| Art. 35 | DPIA before processing likely to result in a high risk; mandatory for systematic and extensive automated evaluation or profiling with legal or similar effects, large-scale special-category data, and large-scale systematic monitoring of public areas | Art. 35(1), 35(3) |
| Art. 37 | Designate a DPO where processing is by a public authority, where core activities need regular and systematic monitoring on a large scale, or where core activities are large-scale processing of special-category or criminal data; publish the DPO's contact details | Art. 37(1), 37(7) |
| Art. 44 | Transfer to third countries only under Chapter V conditions (adequacy, appropriate safeguards, derogations), including onward transfers | Art. 44 |

## Deadlines and numbers
| What | Value | Official reference |
|---|---|---|
| Breach notification to supervisory authority | "without undue delay and, where feasible, not later than 72 hours after having become aware of it"; if later, "accompanied by reasons for the delay" | Art. 33(1) |
| Processor to controller | "without undue delay after becoming aware" | Art. 33(2) |
| Notification to individuals | "without undue delay" when "likely to result in a high risk" | Art. 34(1) |
| Data subject request response | "without undue delay and in any event within one month of receipt of the request"; "may be extended by two further months where necessary", with the data subject told of the extension within one month | Art. 12(3) |
| Refusal to act | Inform the data subject "at the latest within one month of receipt of the request" | Art. 12(4) |
| Child consent age | "at least 16 years old"; Member States may lower it, "provided that such lower age is not below 13 years" | Art. 8(1) |
| Records exemption threshold | "fewer than 250 persons" (with exceptions) | Art. 30(5) |
| Fines, upper tier (principles, consent, Art. 9, rights Arts. 12–22, transfers Arts. 44–49) | "up to 20 000 000 EUR, or in the case of an undertaking, up to 4 % of the total worldwide annual turnover of the preceding financial year, whichever is higher" | Art. 83(5) |
| Fines, lower tier (Arts. 8, 11, 25–39, 42, 43) | "up to 10 000 000 EUR ... up to 2 %" of worldwide annual turnover, whichever is higher | Art. 83(4) |
| Application date | "It shall apply from 25 May 2018." | Art. 99(2) |

## Assessment and certification
No mandatory certification. Supervisory authorities enforce through investigations and corrective powers (Art. 58) and fines (Art. 83). Approved codes of conduct (Art. 40) and certification mechanisms (Art. 42) are voluntary and may be used "as an element by which to demonstrate compliance" with Art. 32(1) (Art. 32(3)).

## Notes
- **Source caveat (updated in follow-up pass):** eur-lex.europa.eu still returns an AWS WAF challenge. Article text was first read from legislation.gov.uk's "Original (As adopted by EU)" view, and key quotes (Art. 3(2) "who are in the Union", Art. 12(3) "within one month of receipt of the request", Art. 33(1) "not later than 72 hours after having become aware", Art. 83(4)-(6) fine amounts, Art. 99(2) "It shall apply from 25 May 2018") were re-checked against the Official Journal XHTML served by the EU Publications Office (CELEX 32016R0679). No consolidated version was read; any separate EU instrument on GDPR enforcement procedure was not checked (UNVERIFIED).
- **Catalog corrections (framework-catalog.md line 76):** "applies to anyone serving EU residents" and "Any personal data of EU/EEA residents" are inaccurate. Art. 3(2) turns on data subjects "who are in the Union" (location, not residence), combined with offering goods or services or monitoring behaviour. Art. 3(1) separately covers any processing in the context of an EU establishment, wherever the data subjects are.
- **Catalog corrections (control-checklists.md PRIV-05):** "GDPR 30d" is wrong. Art. 12(3) says "within one month of receipt", extendable "by two further months" for complex or numerous requests.
- control-checklists.md PRIV-08 "GDPR 72h" is correct, but the text is "where feasible, not later than 72 hours after having become aware", and the notice is not required when the breach is "unlikely to result in a risk".
- control-checklists.md PRIV-11 "GDPR 13–16 by state" is correct (default 16, Member State floor 13, Art. 8(1)).
- control-checklists.md "representative in EU/UK if established outside" is too broad. The obligation applies only where Art. 3(2) applies, and Art. 27(2) has exceptions.
- **EEA:** the GDPR was incorporated into the EEA Agreement (Annex XI) by EEA Joint Committee Decision No 154/2018 of 6 July 2018, which also provides that EFTA States' supervisory authorities "shall participate fully in the one-stop-shop and the consistency mechanism" (recital 4). The Decision enters into force "on the day following the last notification under Article 103(1) of the EEA Agreement"; that actual date (and so the date the GDPR applied in Iceland, Liechtenstein and Norway) was not shown in the text read (UNVERIFIED).
- **Pending change (proposal, not adopted):** the Commission's Digital Omnibus "takes the shape of two distinct proposed regulations", including "Digital Omnibus covering data, cybersecurity and privacy rules", for example a single entry point for incident and breach reports (digital-strategy.ec.europa.eu Digital Rulebook page). As of 2026-11-06 that page still calls the data and privacy omnibus a proposal. Only the separate AI Omnibus is described as in force (27 July 2026).
