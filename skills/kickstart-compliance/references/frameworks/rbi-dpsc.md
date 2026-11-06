---
id: rbi-dpsc
name: RBI Digital Payment Security Controls (DPSC) Directions 2021
official_name: Reserve Bank of India (Digital Payment Security Controls) Directions, 2021 (Master Direction RBI/2020-21/74, DoS.CO.CSITE.SEC.No.1852/31.01.015/2020-21, 18 February 2021)
governing_body: Reserve Bank of India (Department of Supervision, CSITE)
type: security
legal_status: binding-regulation
region: India
industry: finance, payments (scheduled commercial banks excl. RRBs, small finance banks, payments banks, credit card issuing NBFCs)
current_version: Master Direction dated 18 Feb 2021; "come into effect six months from the day they are placed on the official website" (i.e. about August 2021)
superseded_by: none
official_sources:
  - title: Master Direction on Digital Payment Security Controls (18 February 2021)
    url: https://www.rbi.org.in/scripts/BS_ViewMasDirections.aspx?id=12032
    accessed: 2026-11-06
last_verified: 2026-11-06T00:00:00Z
verification: verified
---

## What it is
"RBI DPSC" officially refers to the Reserve Bank of India (Digital Payment Security Controls) Directions, 2021. The Master Direction requires regulated entities to "set up a robust governance structure and implement common minimum standards of security controls for digital payment products and services" across internet banking, mobile payments and card payments. RBI describes it as "technology and platform agnostic".

## Who it applies to
Para 2: "Scheduled Commercial Banks (excluding Regional Rural Banks); Small Finance Banks; Payments Banks; and Credit card issuing NBFCs." Chapter III applies to entities offering internet banking, Chapter IV to mobile banking/payments apps, Chapter V to card issuers (credit/debit/prepaid, physical or virtual). Non-bank Payment System Operators are covered by a separate instrument (Master Directions on Cyber Resilience and Digital Payment Security Controls for non-bank PSOs, 30 July 2024, referenced in the PA Master Direction para 9(e)).

## Engineering obligations
| ID | Obligation | Official reference |
|---|---|---|
| DPSC-01 | Board-approved policy for digital payment products covering payment security requirements | Para 4 |
| DPSC-02 | Maintain a database of all systems/applications storing customer data in the payment ecosystem and their PCI compliance | Para 8 |
| DPSC-03 | Implement WAF and DDoS mitigation for internet-facing digital payment services | Para 15 |
| DPSC-04 | Strong, non-deprecated key lengths, algorithms, cipher suites, certificates and protocols | Para 16 |
| DPSC-05 | Secure application life cycle across design, development, testing, code review, implementation and decommissioning; threat modelling | Paras 21-22 |
| DPSC-06 | Source-code escrow for third-party licensed payment applications | Para 23 |
| DPSC-07 | Security testing covering standards like OWASP (incl. Mobile Top 10); certificate from developer when source code is not owned; VA "at least on a half-yearly basis", PT "at least on a yearly basis", and on new apps or major changes | ASLC paras 21-31 |
| DPSC-08 | Mask/redact account numbers, card numbers and other sensitive information in SMS and e-mails | Para 32 |
| DPSC-09 | Multi-factor authentication for electronic payments and fund transfers, with at least one factor "dynamic or non-replicable" (OTP, device binding + SIM, biometric/PKI/hardware tokens, EMV chip) | Para 33 |
| DPSC-10 | MFA and alerts for all payment transactions, beneficiary changes, account detail changes and limit revisions; alerts/OTPs name the merchant, not the PA | Authentication Framework, paras 33-36 |
| DPSC-11 | Protect against MITM/MITB; session and its encryption remain intact; terminate session and resolve/reverse transactions on interference | Authentication Framework, paras 33-36 |
| DPSC-12 | Parameterised fraud alerts (transaction velocity, high-risk MCCs, counterfeit card parameters, etc.) | Para 37 |
| DPSC-13 | Reconciliation of all digital payment transactions "not later than 24 hours from the time of receipt of settlement file(s)" | Para 41 |
| DPSC-14 | In-app mandatory secure-usage guidance at onboarding and after updates; in-app grievance lodging; in-app mechanism to mark a transaction as fraudulent | Paras 42-43, 50 |
| DPSC-15 | Internet banking: adaptive authentication or strong CAPTCHA with server-side validation; DNS cache poisoning and cookie protections; virtual keyboard; auto-terminate sessions after inactivity; forced change of RE-issued password on first login | Paras 51-53 |
| DPSC-16 | Mobile apps: device policy enforcement; secure download; deactivate older app versions within six months of a new release; data and device encryption; minimal permissions; sandboxing; detect remote-access apps; code obfuscation | Para 56 |
| DPSC-17 | Mobile apps: consider root/jailbreak detection; publish checksum of current app version; device binding | Paras 58-60 |
| DPSC-18 | Mobile apps: do not load web content on SSL/TLS errors; show certificate errors; encrypt sensitive data in the database; guard against SQL injection | Chapter IV (final paras) |
| DPSC-19 | Cards: follow PCI-PIN, PCI-PTS, PCI-HSM, PCI-P2PE over and above PCI-DSS/PA-DSS | Para 67 |
| DPSC-20 | ATMs: BIOS password, USB/autorun disabled, patching, anti-skimming, whitelisting; prohibit ATMs on unsupported OS | Para 71 |
| DPSC-21 | Card transaction limits at card/BIN/RE level set at the network switch; 24x7 monitoring of limit breaches; no plain-text card details at RE or vendor locations | Para 72 |
| DPSC-22 | Card data scanning tools must first be tested in a test environment | Para 73 |

## Deadlines and numbers
| What | Value | Official reference |
|---|---|---|
| Reconciliation of digital payment transactions | "not later than 24 hours from the time of receipt of settlement file(s)" | Para 41 |
| Vulnerability assessment | "at least on a half-yearly basis" | ASLC section (paras 21-31) |
| Penetration testing | "at least on a yearly basis" | ASLC section (paras 21-31) |
| Old mobile app versions | "not exceeding six months from the date of release of newer version" | Para 56 |
| Fraud limit breach monitoring | "on a 24x7 basis, including weekends, long holidays" | Para 72 |
| Commencement | "six months from the day they are placed on the official website" | Para 1 |

## Assessment and certification
No certification. RBI supervises compliance; source-code review/certification is obtained yearly where applications change (ASLC section). PCI standard compliance is evidenced per system (para 8).

## Notes
- Catalog row "RBI DPSC (Data Protection and Security Controls) ... privacy, security ... Banks and NBFCs handling customer financial data" is wrong on the name and type: DPSC stands for **Digital Payment Security Controls**; it is a security (not privacy) instrument; scope is SCBs (excl. RRBs), SFBs, Payments Banks and credit-card-issuing NBFCs only, not NBFCs generally.
- The DPSC MD does not set an incident-reporting deadline; incident reporting follows the CSF/IT Governance MD and CERT-In.
- A separate July 2024 Master Direction on Cyber Resilience and Digital Payment Security Controls applies to non-bank PSOs (e.g. PAs, PPI issuers); not documented here.
