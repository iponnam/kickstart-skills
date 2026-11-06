#!/usr/bin/env python3
"""Validate skill folders: frontmatter present, name matches folder, description length, referenced files exist."""
import re
import sys
from pathlib import Path

root = Path(__file__).resolve().parent.parent / "skills"
ok = True
for skill_dir in sorted(p for p in root.iterdir() if p.is_dir()):
    md = skill_dir / "SKILL.md"
    if not md.exists():
        print(f"FAIL {skill_dir.name}: no SKILL.md"); ok = False; continue
    text = md.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        print(f"FAIL {skill_dir.name}: no frontmatter"); ok = False; continue
    fm = dict(line.split(":", 1) for line in m.group(1).splitlines() if ":" in line)
    fm = {k.strip(): v.strip() for k, v in fm.items()}
    name, desc = fm.get("name", ""), fm.get("description", "")
    if name != skill_dir.name:
        print(f"FAIL {skill_dir.name}: name '{name}' != folder"); ok = False
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name) or len(name) > 64:
        print(f"FAIL {skill_dir.name}: invalid name"); ok = False
    if not desc or len(desc) > 1024:
        print(f"FAIL {skill_dir.name}: description missing or over 1024 chars ({len(desc)})"); ok = False
    body = text[m.end():]
    for ref in re.findall(r"`((?:references|scripts|templates)/[^`]+)`", body):
        if not (skill_dir / ref).exists():
            print(f"FAIL {skill_dir.name}: referenced file missing: {ref}"); ok = False
    words = len(body.split())
    print(f"ok   {name:28s} desc={len(desc):4d} chars  body={words:5d} words")
sys.exit(0 if ok else 1)
