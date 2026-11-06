---
id: sox-itgc
name: SOX Section 404 (ICFR / ITGC)
official_name: Sarbanes-Oxley Act of 2002, Section 404 (15 U.S.C. 7262), Management assessment of internal controls; implemented by SEC Rules 13a-15 / 15d-15 (17 CFR 240.13a-15, 240.15d-15) and Regulation S-K Item 308 (17 CFR 229.308); auditor attestation under PCAOB AS 2201
governing_body: U.S. Securities and Exchange Commission (SEC); Public Company Accounting Oversight Board (PCAOB) for auditor standards
type: governance
legal_status: law
region: US (issuers with securities registered under, or reporting under, the Securities Exchange Act of 1934, including foreign private issuers)
industry: any (public companies)
current_version: 17 CFR 240.13a-15 and 229.308 as in eCFR on 2026-11-06; PCAOB AS 2201 (version not verified)
superseded_by: none
official_sources:
  - title: 17 CFR 240.13a-15 Issuer's disclosure controls and procedures (eCFR)
    url: https://www.ecfr.gov/current/title-17/chapter-II/part-240/subject-group-ECFR4fa8ad1ac0ab9e2/section-240.13a-15
    accessed: 2026-11-06
  - title: 17 CFR 229.308 (Item 308) Internal control over financial reporting (eCFR)
    url: https://www.ecfr.gov/current/title-17/chapter-II/part-229/subpart-229.300/section-229.308
    accessed: 2026-11-06
  - title: 17 CFR 240.12b-2 Definitions (accelerated filer, large accelerated filer) (eCFR)
    url: https://www.ecfr.gov/current/title-17/chapter-II/part-240/subject-group-ECFR8c9733a1d9a6a8a/section-240.12b-2
    accessed: 2026-11-06
  - title: 15 U.S.C. 7262, Management assessment of internal controls (Office of the Law Revision Counsel, uscode.house.gov; current through Pub. L. 119-136)
    url: https://uscode.house.gov/us/usc/t15/s7262/
    accessed: 2026-11-06
  - title: PCAOB AS 2201, An Audit of Internal Control Over Financial Reporting That Is Integrated with An Audit of Financial Statements (attempted)
    url: https://pcaobus.org/oversight/standards/auditing-standards/details/AS2201
    accessed: 2026-11-06
last_verified: 2026-11-06T00:00:00Z
verification: partial
---

## What it is
Section 404 requires management of public companies to assess and report annually on the effectiveness of internal control over financial reporting (ICFR), and requires certain issuers' auditors to attest to it. ICFR is "a process designed by, or under the supervision of, the issuer's principal executive and principal financial officers ... to provide reasonable assurance regarding the reliability of financial reporting and the preparation of financial statements for external purposes in accordance with generally accepted accounting principles" (17 CFR 240.13a-15(f)). IT general controls (ITGCs) matter because ICFR includes policies and procedures over records, authorization of transactions, and prevention or timely detection of unauthorized use of assets (§240.13a-15(f)(1)-(3)), much of which runs through financial systems.

## Who it applies to
- Statute (SOX §404, 15 U.S.C. 7262): the SEC must require "each annual report required by section 78m(a) or 78o(d)" to contain an internal control report that states management's responsibility "for establishing and maintaining an adequate internal control structure and procedures for financial reporting" and assesses their effectiveness "as of the end of the most recent fiscal year" (§7262(a)). The audit firm "shall attest to, and report on, the assessment", except for "an emerging growth company" (§7262(b), added by Pub. L. 112-106, 2012), and §7262(b) "shall not apply" to an issuer that is "neither a 'large accelerated filer' nor an 'accelerated filer'" (§7262(c), added by Pub. L. 111-203, 2010). The attestation follows PCAOB attestation standards and "shall not be the subject of a separate engagement" (§7262(b)).
- Management assessment (404(a)): issuers that file annual reports under Exchange Act section 13(a) or 15(d) and filed one for the prior fiscal year, other than registered investment companies (§240.13a-15(c)).
- Auditor attestation (404(b)): only if the registrant "is an accelerated filer or a large accelerated filer" and is not an emerging growth company (Item 308(b), 17 CFR 229.308(b)). Accelerated filer: public float "$75 million or more, but less than $700 million"; large accelerated filer: "$700 million or more"; both exclude issuers eligible for smaller reporting company status under the revenue test (annual revenues "less than $100 million") (§240.12b-2).
- SaaS vendors are in scope indirectly when customers' ICFR relies on their systems (often evidenced by SOC 1 reports; not in SEC text).

## Engineering obligations
Rows are engineering controls that support the ICFR elements in the SEC definition. The ITGC domain split (access, change, operations) is the conventional audit approach; AS 2201 text could not be fetched to confirm wording.

| ID | Obligation | Official reference |
|---|---|---|
| ICFR-01 | Maintain records that "in reasonable detail accurately and fairly reflect the transactions and dispositions of the assets" (data integrity, complete audit trail in financial systems) | §240.13a-15(f)(1) |
| ICFR-02 | Ensure transactions are recorded to permit GAAP financial statements and are made "only in accordance with authorizations of management and directors" (role-based approval workflows, segregation of duties in finance apps) | §240.13a-15(f)(2) |
| ICFR-03 | "prevention or timely detection of unauthorized acquisition, use or disposition of the issuer's assets" (logical access controls, privileged access review, monitoring) | §240.13a-15(f)(3) |
| ICFR-04 | Management evaluates ICFR effectiveness "as of the end of each fiscal year" using a "suitable, recognized control framework" (e.g., document control descriptions, owners, evidence) | §240.13a-15(c) |
| ICFR-05 | Evaluate each quarter any change in ICFR that "has materially affected, or is reasonably likely to materially affect" ICFR (change management records for financially relevant systems) | §240.13a-15(d); Item 308(c) |
| ICFR-06 | Disclosure controls and procedures so required information is "recorded, processed, summarized and reported, within the time periods specified" | §240.13a-15(b), (e) |
| ICFR-07 | Management report: responsibility statement, framework used, effectiveness conclusion, disclosure of any material weakness | Item 308(a)(1)-(3) |
| ITGC-01 | Access management to financial systems: provisioning, removal, periodic review (UNVERIFIED wording, AS 2201 not fetched) | AS 2201 (UNVERIFIED) |
| ITGC-02 | Program change management: authorized, tested, approved deployments to financial systems (UNVERIFIED wording) | AS 2201 (UNVERIFIED) |
| ITGC-03 | Computer operations: job scheduling, backup and recovery, incident handling for financial systems (UNVERIFIED wording) | AS 2201 (UNVERIFIED) |

## Deadlines and numbers
| What | Value | Official reference |
|---|---|---|
| Management assessment date | "as of the end of each fiscal year" (rule); "as of the end of the most recent fiscal year of the issuer" (statute) | §240.13a-15(c); 15 U.S.C. 7262(a)(2) |
| Auditor attestation exemptions | emerging growth companies; issuers neither large accelerated nor accelerated filers | 15 U.S.C. 7262(b), (c) |
| Change evaluation | "during each of the issuer's fiscal quarters" | §240.13a-15(d) |
| Accelerated filer float | "$75 million or more, but less than $700 million" | §240.12b-2 |
| Large accelerated filer float | "$700 million or more" | §240.12b-2 |
| SRC revenue test excluding 404(b) | "annual revenues of less than $100 million" and public float under $700 million | §240.12b-2 "Smaller reporting company" (2) |
| Interpretive guidance safe harbor | evaluation per SEC "Release No. 34-55929 will satisfy the evaluation required" | §240.13a-15(c) |

## Assessment and certification
Management self-assesses annually and reports in the Form 10-K/20-F (Item 308(a)). For accelerated and large accelerated filers (non-EGC), the registered public accounting firm that audits the financial statements issues an attestation report on ICFR (Item 308(b)), performed under PCAOB AS 2201 as an integrated audit. The PCAOB inspects audit firms; the SEC enforces issuer obligations.

## Notes
- Catalog row "`+` SOX (ITGC) ... attestation ... Public companies" should note that auditor attestation (404(b)) applies only to accelerated and large accelerated filers that are not emerging growth companies (Item 308(b)); all reporting issuers (after their first annual report) need management's 404(a) assessment.
- PCAOB AS 2201 content is UNVERIFIED: pcaobus.org returned a Cloudflare challenge to curl and to headless Chromium. ITGC rows rely on conventional practice and should be confirmed against AS 2201 before shipping.
- Statute text now verified (follow-up pass): 15 U.S.C. 7262 read on uscode.house.gov (source credit "Pub. L. 107-204, title IV, § 404, July 30, 2002, 116 Stat. 789; Pub. L. 111-203, title IX, § 989G(a), July 21, 2010, 124 Stat. 1948; Pub. L. 112-106, title I, § 103, Apr. 5, 2012, 126 Stat. 310"). It matches Item 308(b) and §240.13a-15. The old uscode.house.gov view.xhtml URL form now returns 404; use /us/usc/t15/s7262/.
- PCAOB AS 2201 remains UNVERIFIED (pcaobus.org is still blocked by its own bot protection), so the ITGC rows and the integrated-audit wording are not confirmed. `verification` stays partial for that reason.
- The 2007 SEC interpretive guidance (Release No. 34-55929) is referenced in §240.13a-15(c) but its sec.gov page was not found at the URL tried.
