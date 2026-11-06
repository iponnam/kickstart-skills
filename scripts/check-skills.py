#!/usr/bin/env python3
"""Validate skill folders: frontmatter present, name matches folder, description length, referenced files exist."""
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("PyYAML is required: pip install pyyaml")

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
    try:
        fm = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError as e:
        print(f"FAIL {skill_dir.name}: front matter is not valid YAML: {str(e).splitlines()[0]}"); ok = False; continue
    name, desc = str(fm.get("name", "")), str(fm.get("description", ""))
    if name != skill_dir.name:
        print(f"FAIL {skill_dir.name}: name '{name}' != folder"); ok = False
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name) or len(name) > 64:
        print(f"FAIL {skill_dir.name}: invalid name"); ok = False
    if not desc or len(desc) > 1024:
        print(f"FAIL {skill_dir.name}: description missing or over 1024 chars ({len(desc)})"); ok = False
    body = text[m.end():]
    for ref in re.findall(r"`((?:references|scripts|templates)/[^`]+)`", body):
        if "<" in ref: continue
        if not (skill_dir / ref).exists():
            print(f"FAIL {skill_dir.name}: referenced file missing: {ref}"); ok = False
    words = len(body.split())
    print(f"ok   {name:28s} desc={len(desc):4d} chars  body={words:5d} words")
sys.exit(0 if ok else 1)
