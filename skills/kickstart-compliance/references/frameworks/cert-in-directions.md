---
id: cert-in-directions
name: CERT-In Cyber Security Directions 2022
official_name: Directions under sub-section (6) of section 70B of the Information Technology Act, 2000 relating to information security practices, procedure, prevention, response and reporting of cyber incidents for Safe & Trusted Internet (No. 20(3)/2022-CERT-In, 28 April 2022)
governing_body: Indian Computer Emergency Response Team (CERT-In), Ministry of Electronics and Information Technology, Government of India
type: security
legal_status: binding-regulation
region: India; per FAQ, applies to entities "providing services to the users in the country" including foreign service providers
industry: any (service providers, intermediaries, data centres, body corporate, Government organisations); extra record-keeping for data centres, VPS, cloud, VPN and virtual asset providers
current_version: Directions dated 28 April 2022, "effective after 60 days from the date on which it is issued"; FAQs May 2022
superseded_by: none
official_sources:
  - title: CERT-In Directions under section 70B(6) of the IT Act, 2000, dated 28 April 2022
    url: https://www.cert-in.org.in/PDF/CERT-In_Directions_70B_28.04.2022.pdf
    accessed: 2026-11-06
  - title: FAQs on Cyber Security Directions of 28.04.2022 (May 2022)
    url: https://www.cert-in.org.in/PDF/FAQs_on_CyberSecurityDirections_May2022.pdf
    accessed: 2026-11-06
last_verified: 2026-11-06T00:00:00Z
verification: verified
---

## What it is
Binding directions issued by CERT-In, India's national incident response agency, under s.70B(6) of the IT Act, 2000. They mandate clock synchronisation, 6-hour reporting of specified cyber incidents, a point of contact, 180-day log retention, subscriber records for infrastructure/VPN providers and KYC/transaction records for virtual asset providers. Non-compliance "may invite punitive action under sub-section (7) of the section 70B".

## Who it applies to
- "All service providers, intermediaries, data centres, body corporate and Government organisations" (Directions (i)-(iv)). FAQ: "Individual citizens are not covered".
- Data Centres, VPS providers, Cloud Service providers and VPN Service providers: subscriber registration records (Direction (v)). FAQ Q34: "VPN Service provider" means entities providing "Internet proxy like services ... to general Internet subscribers/users"; enterprise/corporate VPNs are not covered.
- Virtual asset service providers, virtual asset exchange providers and custodian wallet providers: KYC and transaction records (Direction (vi)).
- FAQ Q31: reporting applies even where the affected data sits in a third party's systems.

## Engineering obligations
| ID | Obligation | Official reference |
|---|---|---|
| CERTIN-01 | Synchronise all ICT system clocks to NTP servers of NIC or NPL, or servers traceable to them; multi-geography entities may use another accurate source that "shall not deviate from NPL and NIC" | Direction (i) |
| CERTIN-02 | Report Annexure I incident types to CERT-In "within 6 hours of noticing such incidents or being brought to notice" via incident@cert-in.org.in, phone 1800-11-4949 or fax 1800-11-6969 | Direction (ii); Annexure I |
| CERTIN-03 | Partial reports are acceptable: "provide information to the extent available at the time of reporting" and supplement later | FAQ Q30 |
| CERTIN-04 | Maintain an incident classifier covering all Annexure I types (targeted scanning, compromise, unauthorised access, defacement, malware/ransomware, attacks on servers/DNS/routers, identity theft/phishing, DoS/DDoS, SCADA/OT/wireless, application attacks, data breach, data leak, IoT, digital payments, malicious/fake mobile apps, social media account takeover, cloud, big data/blockchain/virtual assets/drones etc.) | Annexure I |
| CERTIN-05 | Act on CERT-In orders/directions and provide information (format up to near real-time) within the specified timeframe | Direction (iii) |
| CERTIN-06 | Designate a Point of Contact and register it with CERT-In in the Annexure II format; keep updated | Direction (iii); Annexure II |
| CERTIN-07 | "Enable logs of all their ICT systems and maintain them securely for a rolling period of 180 days ... within the Indian jurisdiction"; supply logs with incident reports or on order | Direction (iv) |
| CERTIN-08 | Log scope guidance: firewall, IPS, SIEM, web/database/mail/FTP/proxy, critical-system event logs, application, ATM switch, SSH, VPN logs (non-exhaustive) | FAQ Q37 |
| CERTIN-09 | Data centre / VPS / cloud / VPN providers: record validated subscriber names, hire period, allotted IPs, registration email + IP + timestamp, purpose, validated address and phone, ownership pattern; keep "for a period of 5 years or longer duration as mandated by the law after any cancellation or withdrawal of the registration" | Direction (v)(a)-(g) |
| CERTIN-10 | Virtual asset providers: keep KYC and financial transaction records "for a period of five years", with enough detail (IPs with timestamps and time zones, transaction ID, public keys, addresses, nature/date, amount) to reconstruct each transaction | Direction (vi) |
| CERTIN-11 | Foreign/offshore service providers serving users in India must "enable and maintain logs and records of financial transactions in Indian jurisdiction" | FAQ Q36 |

## Deadlines and numbers
| What | Value | Official reference |
|---|---|---|
| Incident report to CERT-In | "within 6 hours of noticing such incidents or being brought to notice about such incidents" | Direction (ii) |
| Log retention | "rolling period of 180 days" "within the Indian jurisdiction" | Direction (iv) |
| Log storage location (clarification) | "The logs may be stored outside India also as long as the obligation to produce logs to CERT-In is adhered to by the entities in a reasonable time" | FAQ Q35 |
| Subscriber records (DC/VPS/cloud/VPN) | "5 years or longer ... after any cancellation or withdrawal of the registration" | Direction (v) |
| Virtual asset KYC and transaction records | "five years" | Direction (vi) |
| Effective date | "effective after 60 days from the date on which it is issued" (issued 28 April 2022) | Directions, final para |

## Assessment and certification
No certification. CERT-In may call for information and issue directions; non-compliance may invite punitive action under s.70B(7) of the IT Act, 2000 (Directions, penultimate para).

## Notes
- Previous catalog ("Any entity in India: 6-hour incident reporting, 180-day log retention, NTP sync") and checklist ("keep logs 180 days in India; ... KYC/subscriber records 5 years for the specified service types") are broadly correct. Corrections: (a) the FAQ Q35 allows logs to be stored outside India if they can be produced to CERT-In in reasonable time, while Q36 requires services offered to users in India to keep logs and financial transaction records in Indian jurisdiction; the "in India" wording should cite both. (b) The 5-year subscriber-record clock runs from cancellation/withdrawal of registration. (c) KYC records (Direction (vi)) apply to virtual asset providers, not to VPS/cloud/VPN providers, which keep subscriber registration data under (v). (d) Coverage is not limited to entities "in India": the FAQ extends logging obligations to any service provider offering services to users in India. (e) Enterprise/corporate VPNs are excluded from (v).
- UNVERIFIED: the later CERT-In notification extending the compliance deadline for MSMEs and for data centre/VPS/cloud/VPN subscriber validation (reported as to 25 September 2022) was not fetched from cert-in.org.in; it is historical and does not change current obligations.
