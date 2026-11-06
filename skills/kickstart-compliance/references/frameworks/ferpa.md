---
id: ferpa
name: FERPA
official_name: Family Educational Rights and Privacy Act, 20 U.S.C. 1232g (section 444 of the General Education Provisions Act); implementing regulations 34 CFR Part 99
governing_body: U.S. Department of Education, Student Privacy Policy Office (SPPO)
type: privacy
legal_status: law
region: US
industry: education (agencies and institutions receiving U.S. Department of Education funds, and their contractors acting as school officials)
current_version: 34 CFR Part 99 as in eCFR on 2026-11-06
superseded_by: none
official_sources:
  - title: 34 CFR Part 99 Family Educational Rights and Privacy (eCFR)
    url: https://www.ecfr.gov/current/title-34/subtitle-A/part-99
    accessed: 2026-11-06
  - title: Student Privacy Policy Office, FERPA page
    url: https://studentprivacy.ed.gov/ferpa
    accessed: 2026-11-06
last_verified: 2026-11-06T00:00:00Z
verification: verified
---

## What it is
FERPA gives parents, and students once they become "eligible students", rights to inspect and review education records, seek amendment, and consent to disclosure of personally identifiable information from education records, subject to listed exceptions (34 CFR 99.7(a)(2), 99.10, 99.20, 99.30, 99.31). The SPPO page describes 34 CFR Part 99 as "the regulations ... implementing section 444 of the General Education Provision Act (GEPA), which is commonly referred to as the Family Educational Rights and Privacy Act (FERPA)".

## Who it applies to
"An educational agency or institution to which funds have been made available under any program administered by the Secretary" (§99.1(a)), applying "to the recipient as a whole, including each of its components" (§99.1(d)). Rights transfer to the student when the student "has reached 18 years of age or is attending an institution of postsecondary education" (§99.3 "Eligible student"; §99.5(a)). EdTech vendors are reached through the school official exception (§99.31(a)(1)(i)(B)) and redisclosure limits (§99.33), and can be barred from access for violations (§99.67).

## Engineering obligations
| ID | Obligation | Official reference |
|---|---|---|
| 99.31(a)(1)(i)(B) | A vendor may be a "school official" only if it performs an institutional service, "Is under the direct control of the agency or institution with respect to the use and maintenance of education records", and is bound by §99.33(a) | §99.31(a)(1)(i)(B)(1)-(3) |
| 99.31(a)(1)(ii) | "use reasonable methods to ensure that school officials obtain access to only those education records in which they have legitimate educational interests" (physical or technological access controls, or an effective administrative policy) | §99.31(a)(1)(ii) |
| 99.33(a) | Recipients may not redisclose PII without consent and may use it "only for the purposes for which the disclosure was made" | §99.33(a)(1), (2) |
| 99.30 | Obtain "signed and dated written consent" (may be electronic, meeting §99.30(d)) before disclosures outside exceptions | §99.30(a), (d) |
| 99.10 | Support parent/eligible student inspection and review of records | §99.10(a), (b) |
| 99.20 | Support amendment requests and record the decision | §99.20 |
| 99.32 | Keep a record of each request for access to and each disclosure of PII, kept with the education records "as long as the records are maintained" | §99.32(a)(1), (2) |
| 99.37 | Honour directory information opt-outs; keep honouring former students' valid opt-outs | §99.37(a), (b) |
| 99.12 | When records cover multiple students, show only the requesting student's information | §99.12(a) |
| 99.7 | Annual notification of rights, including school official / legitimate educational interest criteria | §99.7(a) |

## Deadlines and numbers
| What | Value | Official reference |
|---|---|---|
| Access request response | "within a reasonable period of time, but not more than 45 days after it has received the request" | §99.10(b) |
| Age at which rights transfer | "reached 18 years of age or is attending an institution of postsecondary education" | §99.3 "Eligible student" |
| Disclosure record retention | "as long as the records are maintained" | §99.32(a)(2) |
| Third-party bar after certain violations | access denied "for at least five years" | §99.67(c) |
| Notice of conflict with State law | notify the Office "within 45 days" | §99.61 |

## Assessment and certification
No certification. The Department of Education (SPPO) investigates complaints and enforces, ultimately through withholding of funds or other actions (§§99.60-99.67). Institutions self-assess.

## Notes
- control-checklists.md FERPA row is consistent with the regulation. Suggest adding: 45-day access deadline (§99.10(b)); vendor "direct control" condition (§99.31(a)(1)(i)(B)(2)); disclosure recordkeeping (§99.32); access controls for legitimate educational interest (§99.31(a)(1)(ii)); five-year bar on violating third parties (§99.67(c)).
- Catalog row "Student education records at funded institutions" is correct.
- FERPA has no breach notification requirement in Part 99 (none found in the text).
