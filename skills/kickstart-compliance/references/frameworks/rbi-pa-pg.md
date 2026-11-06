---
id: rbi-pa-pg
name: RBI Payment Aggregator Directions 2025 (+ Storage of Payment System Data)
official_name: Reserve Bank of India (Regulation of Payment Aggregators) Directions, 2025 (Master Direction RBI/DPSS/2025-26/141, CO.DPSS.POLC.No.S-633/02-14-008/2025-26, 15 September 2025); Storage of Payment System Data (RBI/2017-18/153, DPSS.CO.OD No.2785/06.08.005/2017-2018, 6 April 2018)
governing_body: Reserve Bank of India, Department of Payment and Settlement Systems (DPSS)
type: security
legal_status: binding-regulation
region: India (incl. cross-border PA under FEMA)
industry: payments (bank and non-bank Payment Aggregators: online, physical point-of-sale, cross-border; Payment Gateways "recommended" baseline only; all payment system providers for data storage)
current_version: PA Master Direction 15 Sept 2025, "effective immediately unless indicated otherwise"; Storage circular 6 April 2018
superseded_by: none (the 17 March 2020 PA/PG Guidelines, 31 March 2021 clarifications and 31 Oct 2023 PA-CB circular were consolidated and repealed by the 2025 Master Direction, Chapter VI and Annexure-3)
official_sources:
  - title: Master Direction on Regulation of Payment Aggregator (PA), 15 September 2025
    url: https://www.rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=12896
    accessed: 2026-11-06
  - title: Storage of Payment System Data, circular dated 6 April 2018
    url: https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=11244&Mode=0
    accessed: 2026-11-06
last_verified: 2026-11-06T00:00:00Z
verification: verified
---

## What it is
The 2025 Master Direction is RBI's consolidated regime for Payment Aggregators, issued under the Payment and Settlement Systems Act, 2007 and FEMA. It covers authorisation, capital, governance, dispute management, security and fraud risk management, merchant due diligence and escrow settlement for PA-Online, PA-Physical and PA-Cross Border, and its Annexure-1 sets baseline technology recommendations (mandatory for PAs, recommended for PGs). The 2018 storage circular requires all payment system providers to store payment data only in India.

## Who it applies to
- "All bank and non-bank entities undertaking the business of Payment Aggregator", plus AD banks and scheduled commercial banks dealing with PAs "to the extent hereinafter specified" (MD para 3(a)).
- Categories: PA-Physical (device and instrument in close proximity), PA-Cross Border (inward/outward current-account e-commerce), PA-Online (MD para 4(i)).
- Payment Gateway: "provides technology infrastructure to route and facilitate processing of a payment transaction without any involvement in handling of funds" (para 4(j)); not authorised under the MD, but Annexure-1 is "recommended" for PGs.
- Banks do not need authorisation; non-banks must apply through RBI's portal and be Indian companies (para 5(a)-(c)).
- Storage circular: all "Authorised Payment Systems" and scheduled commercial, co-operative, payments, small finance and local area banks (addressees).

## Engineering obligations
| ID | Obligation | Official reference |
|---|---|---|
| RBI-PA-01 | Board-approved Information Security Policy; implement Annexure-1 baseline technology recommendations | MD para 9(b) |
| RBI-PA-02 | Ensure merchant infrastructure is compliant with PCI-DSS and PCI-SSF, as applicable; fraud detection and prevention systems | MD para 9(a) |
| RBI-PA-03 | Comply with the 2018 Storage of Payment System Data circular | MD para 9(c); Annexure-1 item 2.3 |
| RBI-PA-04 | Annual system audit incl. cyber security audit by CERT-In empanelled auditors, submitted to DPSS Regional Office | MD para 9(d) |
| RBI-PA-05 | Follow the Master Directions on Cyber Resilience and Digital Payment Security Controls for non-bank PSOs (30 July 2024) | MD para 9(e) |
| RBI-PA-06 | Implement PCI-DSS, PCI-SSF, "latest encryption standards, transport channel security" | Annexure-1 1.2 |
| RBI-PA-07 | Report security incidents / cardholder data breaches to RBI within the stipulated timeframe; monthly cyber incident reports with RCA | Annexure-1 1.3 |
| RBI-PA-08 | Security assessment of merchants during onboarding; review merchants' PCI-DSS status | Annexure-1 1.4, 1.18 |
| RBI-PA-09 | Quarterly internal and annual external audit reports; "bi-annual" VAPT reports; PCI-DSS AOC/ROC; inventory of applications storing/processing/transmitting customer sensitive data; PCI-SSF status of payment apps | Annexure-1 1.5 |
| RBI-PA-10 | Least-privilege, need-to-know application access with documented admin procedures | Annexure-1 1.10 |
| RBI-PA-11 | Internationally scrutinised encryption algorithms | Annexure-1 1.14 |
| RBI-PA-12 | Forensic readiness: collect and analyse security events across application, server, middleware, endpoint, network, authentication, database, web service and cryptographic events and logs | Annexure-1 1.15 |
| RBI-PA-13 | Data sovereignty: "preventive measures to ensure storing data in infrastructure that do not belong to external jurisdictions" | Annexure-1 1.16 |
| RBI-PA-14 | Right-to-audit clause in outsourcing agreements (or annual independent audit reports from third parties); SLAs permit regulatory access | Annexure-1 1.12, 1.17 |
| RBI-PA-15 | Payment applications developed per PCI-SSF | Annexure-1 1.18 |
| RBI-PA-16 | "Customer card credentials shall not be stored within the database or the server accessed by the merchant" | Annexure-1 2.1 |
| RBI-PA-17 | No ATM PIN as an authentication factor for card-not-present transactions | Annexure-1 2.2 |
| RBI-PA-18 | Refunds to the original payment method unless the customer agrees otherwise | Annexure-1 2.4 |
| RBI-PA-19 | Cyber Crisis Management Plan (Detection, Containment, Response, Recovery); enterprise data dictionary; risk assessment per asset | Annexure-1 1.7.4, 1.8, 1.9 |
| RBI-STOR-20 | Store "the entire data relating to payment systems ... in a system only in India", including "full end-to-end transaction details"; the foreign leg may also be stored abroad | Storage circular para 2(i) |

## Deadlines and numbers
| What | Value | Official reference |
|---|---|---|
| Incident / cardholder data breach report to RBI | "within the stipulated timeframe" (no number in the MD); "Monthly cyber security incident reports" | MD Annexure-1 1.3 |
| VAPT | "bi-annual Vulnerability Assessment / Penetration Test (VAPT) reports" | Annexure-1 1.5 |
| Security audit | "annual system audit, including cyber security audit, conducted by CERT-In empanelled auditors" | MD para 9(d) |
| InfoSec policy review | "reviewed atleast annually" | Annexure-1 1.6 |
| Net worth (non-bank PA) | "₹15 crore at the time of tendering application"; "₹25 crore by the end of third financial year" | MD para 6(a) |
| PA-P only entities: apply for authorisation | "by December 31, 2025", else wind up "by February 28, 2026" | MD para 5(d)(iii) |
| Monthly transaction statistics | "by 7th of next month" | Annexure-2 |
| Payment data storage | "stored in a system only in India" | Storage circular para 2(i) |

## Assessment and certification
RBI authorises non-bank PAs (Certificate of Authorisation) and supervises via reports (Annexure-2): annual net-worth certificate and externally audited IS Audit and Cyber Security Audit reports, quarterly escrow certificates, monthly statistics. Annual system/cyber audit by CERT-In empanelled auditors (para 9(d)). PCI-DSS AOC/ROC are required inputs (Annexure-1 1.5). Under the 2018 circular, a Board-approved System Audit Report by CERT-In empanelled auditors certified data-localisation completion.

## Notes
- Catalog row "RBI PA/PG (Payment Aggregators / Gateways) ... Entities facilitating online payments in India": outdated. The 17 March 2020 PA/PG Guidelines were repealed and replaced by the 15 September 2025 Master Direction, which also covers physical PoS (PA-P) and cross-border (PA-CB) aggregators. PGs are not authorised entities; the baseline technology recommendations are only "recommended" for them.
- The MD sets no hour-based incident deadline; it says "within the stipulated timeframe" and points to the July 2024 Cyber Resilience and Digital Payment Security Controls MD for non-bank PSOs. The checklist "RBI 6h" should not be applied to PAs without that source. CERT-In 6 hours applies independently.
- Checklist "annual VAPT by an approved vendor": for PAs, VAPT is "bi-annual" and the annual system/cyber audit is by CERT-In empanelled auditors.
- Checklist "data localisation (RBI payments data in India)" is correct; source is the 6 April 2018 circular, with the foreign-leg exception.
