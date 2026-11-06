#!/usr/bin/env python3
"""Generate skills/kickstart-compliance/references/framework-catalog.md.

Facts (name, governing body, legal status, verification, official source) are read from
each record's front matter in references/frameworks/<id>.md, so the catalog never drifts
from the records. The shortlisting tags below (region, industry, trigger, effort) are
kickstart's own recommendation metadata, not official facts.

Run from the repository root after adding or editing a record:
    python3 scripts/build-catalog.py
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FW = ROOT / "skills/kickstart-compliance/references/frameworks"
OUT = ROOT / "skills/kickstart-compliance/references/framework-catalog.md"

# id: (group, region tags, industry tags, trigger, effort)
TAGS = {
    # Baseline
    "owasp-top10": ("Baseline", "global", "any", "Always on for every project", "S"),
    # Security, global
    "soc2": ("Security", "global, strongest in US", "any", "Selling to US or enterprise buyers who ask for a security report", "M–L"),
    "soc1": ("Security", "global", "finance, any affecting customers' financial reporting", "Your service affects customers' financial statements", "M"),
    "soc3": ("Security", "global", "any", "Public-facing summary report after SOC 2", "S"),
    "pci-dss": ("Security", "global", "payments, any taking cards", "Accepting, processing, storing or transmitting card data", "S–L"),
    "iso-27001-2022": ("Security", "global", "any", "Enterprise or government buyers, especially outside the US", "L"),
    "iso-27001-2013": ("Security", "global", "any", "Withdrawn edition; only for mapping legacy certificates", "-"),
    "iso-27002-2022": ("Security", "global", "any", "Control guidance used with ISO/IEC 27001", "M"),
    "iso-27017": ("Security", "global", "cloud", "Cloud service providers or customers wanting cloud-specific controls", "M"),
    "iso-27018": ("Privacy", "global", "cloud", "Public cloud processors of personal data", "M"),
    "iso-27701": ("Privacy", "global", "any", "Certifiable privacy information management", "M–L"),
    "csa-star": ("Security", "global", "cloud", "Cloud providers proving security posture", "M"),
    "cis-controls": ("Security", "global", "any", "Practical prioritised baseline for any organisation", "M"),
    "nist-csf-2-0": ("Security", "global, US origin", "any", "Structured risk programme", "M"),
    "nist-csf-1-1": ("Security", "global, US origin", "any", "Superseded by CSF 2.0; only for legacy mappings", "-"),
    "hitrust": ("Security", "US, global", "any, common in health", "Partners demanding a certified framework", "L"),
    "swift-csp": ("Security", "global", "finance", "SWIFT-connected institutions", "M"),
    "iec-62443": ("Security", "global", "industrial, energy, OT", "Industrial control systems and OT products", "L"),
    "cobit-2019": ("Governance", "global", "any", "IT governance in larger organisations", "L"),
    # Quality and continuity
    "iso-9001": ("Quality", "global", "any", "Quality management, often asked by manufacturing or government buyers", "M"),
    "iso-20000-1": ("Quality", "global", "IT services", "IT service management for managed service providers", "M"),
    "iso-22301": ("Continuity", "global", "any", "Business continuity, often asked by enterprise buyers", "M–L"),
    "iso-13485": ("Quality", "global", "medtech", "Medical device quality management", "L"),
    # AI
    "eu-ai-act": ("AI", "EU", "ai", "AI systems placed on the EU market or used in the EU", "M–L"),
    "iso-42001": ("AI", "global", "ai", "AI management system; enterprise or regulated buyers of AI", "L"),
    "nist-ai-rmf": ("AI", "global, US origin", "ai", "Building or deploying AI systems; US buyers", "M"),
    # US
    "nist-800-53": ("Security", "US", "government, government suppliers", "US federal systems; basis for FedRAMP", "L"),
    "nist-800-171": ("Security", "US", "defence, government suppliers", "Protecting controlled unclassified information", "M–L"),
    "nist-800-171a": ("Security", "US", "defence, government suppliers", "Assessment procedures for 800-171", "M"),
    "cmmc": ("Security", "US", "defence", "US DoD contractors and subcontractors", "M–L"),
    "fedramp": ("Security", "US", "government, cloud", "Cloud services sold to US federal agencies", "L"),
    "nydfs-500": ("Security", "US-NY", "finance, insurance", "Entities licensed by New York DFS", "M"),
    "sox-itgc": ("Governance", "US", "public companies", "SEC registrants; IT general controls over financial reporting", "M"),
    "hipaa": ("Privacy", "US", "health", "Protected health information; covered entities and business associates", "M–L"),
    "glba": ("Privacy", "US", "finance", "Non-bank financial institutions under FTC jurisdiction", "M"),
    "coppa": ("Privacy", "US", "any with child users", "Online services directed to children or with actual knowledge", "S–M"),
    "ferpa": ("Privacy", "US", "education", "Education records at funded institutions and their vendors", "S–M"),
    "ccpa-cpra": ("Privacy", "US-CA", "any", "California consumers above the statutory thresholds", "S–M"),
    "nj-data-privacy": ("Privacy", "US-NJ", "any", "New Jersey consumers above the statutory thresholds", "S"),
    "us-state-privacy": ("Privacy", "US", "any", "Residents of states with comprehensive privacy laws", "M"),
    # EU and UK
    "gdpr": ("Privacy", "EU/EEA, extraterritorial", "any", "Personal data of people in the EU/EEA", "M"),
    "uk-gdpr": ("Privacy", "UK, extraterritorial", "any", "Personal data of people in the UK", "M"),
    "dora": ("Security", "EU", "finance, ICT providers to finance", "EU financial entities and critical ICT third parties", "M–L"),
    "nis2": ("Security", "EU", "essential and important sectors", "Entities in Annex I/II sectors above size thresholds", "M–L"),
    "cyber-essentials": ("Security", "UK", "any", "UK organisations; required for many UK government contracts", "S"),
    "dtac": ("Sector", "UK-England", "health", "Digital health products used by the NHS", "M"),
    "easa": ("Sector", "EU, global aviation", "aviation", "Safety-related software, hardware or information security in aviation", "L"),
    "tisax": ("Sector", "DE, EU, global automotive", "automotive", "Suppliers to automotive OEMs", "M–L"),
    "bsi-c5": ("Security", "DE", "cloud", "Cloud providers selling to German public sector and regulated buyers", "L"),
    "ens": ("Security", "ES", "government, government suppliers", "Spanish public sector and its suppliers", "M–L"),
    "hds": ("Sector", "FR", "health", "Hosting personal health data in France", "L"),
    # India
    "dpdpa": ("Privacy", "IN, extraterritorial", "any", "Digital personal data of individuals in India", "S–M"),
    "cert-in-directions": ("Security", "IN", "any", "Any entity with systems or users in India", "S–M"),
    "rbi-csf-banks": ("Security", "IN", "banking", "Banks and RBI-regulated entities in scope", "L"),
    "rbi-pa-pg": ("Security", "IN", "payments", "Payment aggregators and gateways in India", "M–L"),
    "rbi-dpsc": ("Security", "IN", "banking, cards", "Digital payment products of in-scope banks and NBFCs", "M"),
    "sebi-cscrf": ("Security", "IN", "securities markets", "All SEBI-regulated entities", "M–L"),
    "irdai-cyber": ("Security", "IN", "insurance", "Insurers and insurance intermediaries in India", "M–L"),
    # APAC
    "mas-trm": ("Security", "SG", "finance", "MAS-regulated financial institutions", "M–L"),
    "pdpa-sg": ("Privacy", "SG", "any", "Personal data in Singapore", "S–M"),
    "essential-eight": ("Security", "AU", "government, any", "Australian baseline mitigation strategies", "S–M"),
    "australia-ism": ("Security", "AU", "government", "Australian government systems and suppliers", "L"),
    "australia-privacy-act": ("Privacy", "AU, extraterritorial", "any", "APP entities, incl. small businesses in listed categories", "M"),
    "appi-japan": ("Privacy", "JP, extraterritorial", "any", "Personal information of people in Japan", "M"),
    "ismap": ("Security", "JP", "government, cloud", "Cloud services for Japanese government", "L"),
    "k-isms-p": ("Security", "KR", "any above thresholds", "Korean organisations required to certify", "L"),
    "pipl-china": ("Privacy", "CN, extraterritorial", "any", "Personal information of individuals in China", "L"),
    # Middle East
    "nca-ecc": ("Security", "SA", "government, critical", "Saudi national entities and their suppliers", "M–L"),
    "sama-csf": ("Security", "SA", "finance", "SAMA-regulated financial institutions", "L"),
    "sama-mvc": ("Security", "SA", "fintech", "SAMA-licensed fintech: e-wallets, lending, crowdfunding", "M"),
    "sama-cyber-resilience": ("Security", "SA", "fintech", "SAMA sandbox entities and licence applicants", "M"),
    "saudi-pdpl": ("Privacy", "SA, extraterritorial", "any", "Personal data processed in or about people in Saudi Arabia", "M"),
    "dubai-isr": ("Security", "AE-Dubai", "government, suppliers", "Dubai government entities and their suppliers", "M"),
    "uae-pdpl": ("Privacy", "AE", "any", "Personal data in the UAE outside free zones with their own law", "M"),
    "uae-ias": ("Security", "AE", "government, critical", "UAE government and critical information infrastructure", "M–L"),
    "qatar-nia": ("Security", "QA", "government, critical", "Qatar government and critical sectors", "M–L"),
    # Americas
    "pipeda": ("Privacy", "CA", "any", "Personal information in commercial activity in Canada", "S–M"),
    "phipa": ("Privacy", "CA-ON", "health", "Personal health information in Ontario", "M"),
    "quebec-law-25": ("Privacy", "CA-QC", "any", "Personal information of people in Quebec", "M"),
    "lgpd": ("Privacy", "BR, extraterritorial", "any", "Personal data of people in Brazil", "M"),
    # Africa
    "popia": ("Privacy", "ZA", "any", "Personal information in South Africa", "M"),
    "nigeria-ndpa": ("Privacy", "NG", "any", "Personal data in Nigeria", "S–M"),
    "kenya-dpa": ("Privacy", "KE", "any", "Personal data in Kenya", "S–M"),
    "botswana-dpa": ("Privacy", "BW", "any", "Personal data in Botswana", "S–M"),
    "seychelles-dpa": ("Privacy", "SC", "any", "Personal data in Seychelles", "S–M"),
}

REGION_MAP = [
    ("India", "dpdpa, cert-in-directions", "soc2 or iso-27001-2022 for B2B", "rbi-csf-banks, rbi-pa-pg, rbi-dpsc (banking, payments); sebi-cscrf (SEBI-regulated); irdai-cyber (insurance)"),
    ("United States", "us-state-privacy, ccpa-cpra, nj-data-privacy", "soc2", "hipaa, glba, coppa, ferpa, pci-dss, nist-800-171 + cmmc (defence), nist-800-53 + fedramp (federal), nydfs-500 (NY finance), sox-itgc (public)"),
    ("European Union", "gdpr", "iso-27001-2022", "dora (finance), nis2 (essential services), eu-ai-act (AI), tisax (automotive), easa (aviation), bsi-c5 / ens / hds (country cloud and health)"),
    ("United Kingdom", "uk-gdpr", "cyber-essentials, iso-27001-2022, soc2", "dtac (NHS digital health)"),
    ("Singapore", "pdpa-sg", "iso-27001-2022", "mas-trm (finance)"),
    ("Australia", "australia-privacy-act", "essential-eight", "australia-ism (government)"),
    ("Canada", "pipeda, quebec-law-25 (Quebec)", "soc2", "phipa (Ontario health)"),
    ("Saudi Arabia", "saudi-pdpl, nca-ecc (national entities)", "iso-27001-2022", "sama-csf, sama-mvc, sama-cyber-resilience (finance, fintech)"),
    ("UAE", "uae-pdpl", "iso-27001-2022", "dubai-isr (Dubai government), uae-ias (federal government, critical)"),
    ("Qatar", "", "iso-27001-2022", "qatar-nia (government, critical)"),
    ("Brazil", "lgpd", "iso-27001-2022, soc2", "pci-dss (cards)"),
    ("Japan", "appi-japan", "iso-27001-2022", "ismap (government cloud)"),
    ("South Korea", "", "iso-27001-2022", "k-isms-p"),
    ("China", "pipl-china", "", ""),
    ("Africa", "popia (ZA), nigeria-ndpa (NG), kenya-dpa (KE), botswana-dpa (BW), seychelles-dpa (SC)", "iso-27001-2022", ""),
    ("Global SaaS, no fixed region", "gdpr, us-state-privacy", "soc2, iso-27001-2022", "pci-dss if taking cards"),
]

INDUSTRY_MAP = [
    ("Fintech, banking, payments", "pci-dss, soc2, plus the national regulator: rbi-*, sebi-cscrf, mas-trm, sama-*, nydfs-500, dora, glba"),
    ("Health", "hipaa (US), phipa (Ontario), dtac (NHS), hds (France), iso-27001-2022, hitrust"),
    ("Education", "ferpa (US), coppa if child users, local privacy law"),
    ("Government suppliers", "nist-800-53 + fedramp (US), australia-ism, ens, ismap, dubai-isr, nca-ecc, cyber-essentials (UK)"),
    ("Defence", "cmmc, nist-800-171"),
    ("Automotive", "tisax"),
    ("Aviation", "easa"),
    ("Medical devices", "iso-13485, plus health privacy law"),
    ("AI products", "eu-ai-act, iso-42001, nist-ai-rmf"),
    ("Cloud and infrastructure providers", "iso-27017, iso-27018, csa-star, bsi-c5"),
    ("Industrial, energy, OT", "iec-62443, nis2 (EU)"),
    ("E-commerce", "pci-dss, consumer privacy law, coppa if applicable"),
    ("General B2B SaaS", "soc2 or iso-27001-2022, gdpr, us-state-privacy"),
    ("Pet project with real users", "owasp-top10 plus the one local privacy law"),
]

GROUP_ORDER = ["Baseline", "Security", "Privacy", "Sector", "AI", "Quality", "Continuity", "Governance"]


def fm(path: Path) -> dict:
    t = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", t, re.S)
    block = m.group(1) if m else ""
    def g(k):
        r = re.search(rf"^{k}:\s*(.*)$", block, re.M)
        return r.group(1).strip().strip('"\'') if r else ""
    urls = re.findall(r"url:\s*(\S+)", block)
    return {"name": g("name"), "body": g("governing_body"), "legal": g("legal_status"),
            "ver": g("verification"), "url": urls[0] if urls else ""}


def short(s: str, n: int = 70) -> str:
    s = re.sub(r"\s*\(.*?\)", "", s).replace("|", "/")
    return s if len(s) <= n else s[: n - 1].rstrip() + "…"


def main() -> None:
    records = {p.stem: fm(p) for p in FW.glob("*.md") if p.name != "README.md"}
    missing_tags = sorted(set(records) - set(TAGS))
    missing_recs = sorted(set(TAGS) - set(records))
    lines = [
        "# Framework catalog",
        "",
        "Generated by `scripts/build-catalog.py` from the records in `frameworks/`. Do not edit by hand.",
        "",
        "Use this table to shortlist. It holds no versions, deadlines or thresholds: those live only in each record, which cites the official governing body and is re-verified under the freshness rule (60 days) before use.",
        "",
        "Columns `Region`, `Industry`, `When it applies` and `Effort` are kickstart's recommendation tags, not official text. Effort is a rough guide for a small team starting from a kickstart baseline: S days, M weeks, L months.",
        "",
        "`Verified` is the record's status when it was written: verified, partial (some facts unconfirmed or behind a paywall) or unreachable (official site blocked automated access; re-check before relying on it).",
        "",
    ]
    by_group = {}
    for fid, tag in TAGS.items():
        if fid in records:
            by_group.setdefault(tag[0], []).append(fid)
    counts = {"verified": 0, "partial": 0, "unreachable": 0}
    for g in GROUP_ORDER:
        ids = by_group.get(g, [])
        if not ids:
            continue
        lines += [f"## {g}", "", "| Framework | Governing body | Legal status | Region | Industry | When it applies | Effort | Verified | Official source |",
                  "|---|---|---|---|---|---|---|---|---|"]
        for fid in ids:
            r, (_, region, industry, trigger, effort) = records[fid], TAGS[fid]
            counts[r["ver"]] = counts.get(r["ver"], 0) + 1
            src = f"[link]({r['url']})" if r["url"] else "none reachable"
            lines.append(f"| [`{fid}`](frameworks/{fid}.md) {short(r['name'], 40)} | {short(r['body'])} | {r['legal']} | {region} | {industry} | {trigger} | {effort} | {r['ver']} | {src} |")
        lines.append("")
    lines += ["## Region quick map", "", "Always add `owasp-top10`. IDs link to records above.", "",
              "| User region | Required or strongly expected | Customer-expected | Industry add-ons |", "|---|---|---|---|"]
    lines += [f"| {a} | {b} | {c} | {d} |" for a, b, c, d in REGION_MAP]
    lines += ["", "## Industry quick map", "", "| Industry | Add on top of region |", "|---|---|"]
    lines += [f"| {a} | {b} |" for a, b in INDUSTRY_MAP]
    lines.append("")
    known = set(records)
    for row in REGION_MAP + INDUSTRY_MAP:
        for tok in re.findall(r"[a-z0-9]+(?:-[a-z0-9]+)+", " ".join(row)):
            if tok not in known and not tok.endswith("-") and tok not in {"rbi", "sama"}:
                print(f"quick map mentions unknown id: {tok}")
    total = sum(counts.values())
    lines.insert(10, f"Records: {total} · verified {counts['verified']} · partial {counts['partial']} · unreachable {counts['unreachable']}.\n")
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)}: {total} frameworks {counts}")
    if missing_tags:
        print("records without tags (not in catalog):", ", ".join(missing_tags))
    if missing_recs:
        print("tags without records:", ", ".join(missing_recs))


if __name__ == "__main__":
    main()
