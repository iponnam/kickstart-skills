#!/usr/bin/env python3
"""Validate compliance framework files.

Each file in skills/kickstart-compliance/references/frameworks/*.md must have:
- front matter with the required keys
- at least one official source with url and accessed date
- a verification value of verified | partial | unreachable
- the required section headings
- no source URL on a known non-official domain (vendors, blogs, wikis)
and every framework id listed in framework-catalog.md must have a file.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FW_DIR = ROOT / "skills/kickstart-compliance/references/frameworks"
CATALOG = ROOT / "skills/kickstart-compliance/references/framework-catalog.md"

REQUIRED_KEYS = ["id", "name", "official_name", "governing_body", "type", "legal_status", "region",
                 "industry", "current_version", "official_sources", "last_verified", "verification"]
REQUIRED_SECTIONS = ["## What it is", "## Who it applies to", "## Engineering obligations",
                     "## Assessment and certification", "## Notes"]
VERIFICATION = {"verified", "partial", "unreachable"}
NON_OFFICIAL = re.compile(r"(scrut\.io|vanta\.com|drata\.com|secureframe|wikipedia\.org|iapp\.org|medium\.com|"
                          r"linkedin\.com|gdpr-info\.eu|onetrust|deloitte|pwc\.com|kpmg|ey\.com|lexology|jdsupra|"
                          r"law\.cornell\.edu|blog\.)", re.I)

ok = True
ids = set()
for f in sorted(p for p in FW_DIR.glob("*.md") if p.name != "README.md"):
    t = f.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", t, re.S)
    if not m:
        print(f"FAIL {f.name}: no front matter"); ok = False; continue
    fm = m.group(1)
    for k in REQUIRED_KEYS:
        if not re.search(rf"^{k}:", fm, re.M):
            print(f"FAIL {f.name}: missing key {k}"); ok = False
    fid = (re.search(r"^id:\s*(\S+)", fm, re.M) or [None, ""])[1]
    if fid != f.stem:
        print(f"FAIL {f.name}: id '{fid}' does not match filename"); ok = False
    ids.add(fid)
    ver = (re.search(r"^verification:\s*(\S+)", fm, re.M) or [None, ""])[1]
    if ver not in VERIFICATION:
        print(f"FAIL {f.name}: verification '{ver}' invalid"); ok = False
    urls = re.findall(r"url:\s*(\S+)", fm)
    if not urls and ver != "unreachable":
        print(f"FAIL {f.name}: no official source url"); ok = False
    for u in urls:
        if NON_OFFICIAL.search(u):
            print(f"FAIL {f.name}: non-official source {u}"); ok = False
    if urls and not re.search(r"accessed:\s*\d{4}-\d{2}-\d{2}", fm):
        print(f"FAIL {f.name}: source without accessed date"); ok = False
    body = t[m.end():]
    for s in REQUIRED_SECTIONS:
        if s not in body:
            print(f"FAIL {f.name}: missing section {s}"); ok = False
    print(f"ok   {f.stem:28s} {ver:11s} sources={len(urls)}")

if CATALOG.exists():
    cat_ids = set(re.findall(r"\[`([a-z0-9-]+)`\]\(frameworks/", CATALOG.read_text(encoding="utf-8")))
    for missing in sorted(cat_ids - ids):
        print(f"FAIL catalog links to missing framework file: {missing}"); ok = False
    for orphan in sorted(ids - cat_ids):
        print(f"WARN framework file not linked from catalog: {orphan}")

print(f"\n{len(ids)} framework files checked")
sys.exit(0 if ok else 1)
