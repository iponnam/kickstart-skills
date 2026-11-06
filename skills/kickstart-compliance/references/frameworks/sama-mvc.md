---
id: sama-mvc
name: SAMA Minimum Verification Controls
official_name: SAMA Minimum Verification Controls (Circular No. 202200000245, 20/9/1443H, 21/4/2022G)
governing_body: Saudi Central Bank (SAMA)
type: security
legal_status: binding-regulation
region: Saudi Arabia
industry: finance - fintech (e-wallets, lending, crowdfunding, other fintech models); rulebook scope: Finance Sector, Payment Systems and PSPs, Money Exchange Sector, Regulatory Sandbox
current_version: Circular 202200000245 dated 21 April 2022; rulebook status "In-Force"
superseded_by: none
official_sources:
  - title: SAMA Rulebook - Minimum Verification Controls (full text)
    url: https://rulebook.sama.gov.sa/en/minimum-verification-controls-0
    accessed: 2026-11-06
  - title: SAMA Rulebook - Minimum Verification Controls (section landing page)
    url: https://rulebook.sama.gov.sa/en/minimum-verification-controls
    accessed: 2026-11-06
last_verified: 2026-11-06T00:00:00Z
verification: verified
---

## What it is
A SAMA instrument published under that exact name in the SAMA Rulebook (Cyber Risk Control > Cyber Resilience). It sets mandatory customer registration/onboarding, authentication, OTP, notification and anti-fraud controls for fintech business models, in addition to other SAMA regulations (s.1). It supersedes "E-Wallet Security Controls v1.0" (Appendix A). It is not a general baseline of the SAMA CSF.

## Who it applies to
s.2: "any member organization that provide E-wallet, lending products, crowdfunding or other fintech business model under SAMA supervision". Section 5 adds controls for lending companies.

## Engineering obligations
| ID | Obligation | Official reference |
|---|---|---|
| MVC-3.1 | Each phone number or National ID/Iqama linked to one application only | 3.1 |
| MVC-3.3 | Registration uses strong authentication from an independent trusted party; for e-wallets via National Single Sign-On (NSSO) with username, password and OTP | 3.3 (a)-(c) |
| MVC-3.4 | Verify phone-number ownership matches user (name and national ID) via trusted party (e.g. Tahaqaq) | 3.4 |
| MVC-3.5 | OTP during registration, sent to the verified phone number | 3.5 |
| MVC-3.6 | Session timeout for all issued OTPs | 3.6 |
| MVC-3.7 | SMS notification for registration, device re-registration, account status changes | 3.7 |
| MVC-3.8 | App bound to one device, otherwise OTP on each login and concurrent login disabled | 3.8 |
| MVC-3.9 | Secure deactivation, reactivation and device re-registration | 3.9 |
| MVC-4.2 | Distribute only via official app stores | 4.2 |
| MVC-4.3 | Restrict installation on jailbroken/rooted devices | 4.3 |
| MVC-4.4 | Contingency, backup and recovery procedures | 4.4 |
| MVC-4.7 | Inactive accounts policy | 4.7 |
| MVC-4.8 | "Multi Factor Authentication (MFA) should be implemented to authenticate each log in" | 4.8 |
| MVC-4.9 | OTP for wallet-to-wallet transfers (first time per beneficiary), marketplace transactions, bill payments (first time), password reset, wallet reactivation, risky transactions | 4.9 |
| MVC-4.10 | OTP over a different delivery channel for over-limit wallet transfers, IBAN transfers, international transfers, high-risk transactions (first time per beneficiary) | 4.10 |
| MVC-4.11 | SMS notification for all transactions and account changes; clear SMS content naming the organisation | 4.11, 4.15 |
| MVC-4.12 | Fraud use cases: user behaviour anomaly monitoring, device usage behaviour | 4.12, 4.13 |
| MVC-4.16 | Reflect all controls in board-approved policies with periodic review | 4.16 |
| MVC-5.1 | Lending: confirm recipient IBAN belongs to the loan requester | 5.1 |
| MVC-5.2 | Lending: trusted, authorised digital signature provider; promissory notes via national trusted party (e.g. Nafith) | 5.2, 5.3 |
| MVC-5.5 | Lending: confirmation call; SMS on submission and on approval/denial | 5.4, 5.5 |

## Deadlines and numbers
| What | Value | Official reference |
|---|---|---|
| Transfer threshold for extra OTP channel | "(Defined Value)" circulated by SAMA memo, not published in the text | 4.9, 4.10, footnote 2 |

## Assessment and certification
No assessment method is set in the document; supervision by SAMA. Controls must be in board-approved internal policies (4.16).

## Notes
- Catalog row "SAMA Minimum Verification Controls | SA | finance | security | law | M | Financial institutions in Saudi Arabia (baseline)" is wrong on scope: MVC is not a baseline for all financial institutions; it targets fintech (e-wallet, lending, crowdfunding, other fintech) member organizations. It is a SAMA regulatory control set, not a law.
- The "Defined Value" amount is communicated by memo and was not verifiable.
