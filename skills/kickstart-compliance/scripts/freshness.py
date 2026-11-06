#!/usr/bin/env python3
"""Freshness check for framework records.

Tells the agent which framework files are older than the allowed age (default 60 days)
and must be re-verified against their official sources before use. Standard library only.

A record is looked up in the project cache first (.kickstart/cache/frameworks/<id>.md),
then in the bundled skill references (references/frameworks/<id>.md).
Its age comes from the `last_verified:` front-matter value (ISO 8601). Records without
it fall back to the newest `accessed:` date, read as 00:00 UTC that day.

Usage:
  freshness.py check  --ids gdpr,owasp-top10 [--max-age-days 60]
  freshness.py check  --all
  freshness.py adopt  --ids gdpr        # copy bundled record into the project cache
  freshness.py mark   --ids gdpr        # stamp cache record last_verified = now (after re-verifying)

Output of `check` is JSON: one object per id with source, last_verified, age_hours,
stale, verification and the official URLs to re-fetch. Exit code is 0 when all are fresh,
1 when any is stale or missing, so it can gate scripts.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import shutil
import sys
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
BUNDLED = SKILL_DIR / "references" / "frameworks"
DEFAULT_CACHE = Path(".kickstart/cache/frameworks")
UTC = dt.timezone.utc


def now() -> dt.datetime:
    return dt.datetime.now(UTC)


def parse_ts(value: str) -> dt.datetime | None:
    value = value.strip().strip('"\'')
    try:
        if len(value) == 10:
            return dt.datetime.fromisoformat(value).replace(tzinfo=UTC)
        ts = dt.datetime.fromisoformat(value.replace("Z", "+00:00"))
        return ts if ts.tzinfo else ts.replace(tzinfo=UTC)
    except ValueError:
        return None


def front_matter(text: str) -> str:
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    return m.group(1) if m else ""


def record(fid: str, cache: Path) -> dict:
    path = cache / f"{fid}.md"
    origin = "project-cache"
    if not path.exists():
        path = BUNDLED / f"{fid}.md"
        origin = "bundled"
    if not path.exists():
        return {"id": fid, "source": "missing", "stale": True, "reason": "no record; research from official sources"}
    fm = front_matter(path.read_text(encoding="utf-8"))
    lv = re.search(r"^last_verified:\s*(\S+)", fm, re.M)
    never = bool(lv) and lv.group(1).strip("\"'").lower() == "never"
    ts = parse_ts(lv.group(1)) if lv and not never else None
    if ts is None and not never:
        dates = [parse_ts(d) for d in re.findall(r"accessed:\s*(\S+)", fm)]
        dates = [d for d in dates if d]
        ts = max(dates) if dates else None
    ver = re.search(r"^verification:\s*(\S+)", fm, re.M)
    return {
        "id": fid,
        "source": origin,
        "path": str(path),
        "last_verified": ts.isoformat() if ts else None,
        "age_hours": round((now() - ts).total_seconds() / 3600, 1) if ts else None,
        "verification": ver.group(1) if ver else None,
        "urls": re.findall(r"url:\s*(\S+)", fm),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("action", choices=["check", "adopt", "mark"])
    ap.add_argument("--ids", default="")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--cache", default=str(DEFAULT_CACHE))
    ap.add_argument("--max-age-days", type=float, default=60.0)
    ap.add_argument("--max-age-hours", type=float, default=None, help="overrides --max-age-days")
    a = ap.parse_args()

    max_hours = a.max_age_hours if a.max_age_hours is not None else a.max_age_days * 24
    cache = Path(a.cache)
    ids = sorted(p.stem for p in BUNDLED.glob("*.md") if p.name != "README.md") if a.all else [i.strip() for i in a.ids.split(",") if i.strip()]
    if not ids:
        ap.error("give --ids or --all")

    if a.action == "check":
        out, any_stale = [], False
        for fid in ids:
            r = record(fid, cache)
            if "age_hours" in r:
                r["stale"] = r["age_hours"] is None or r["age_hours"] > max_hours
            any_stale |= r["stale"]
            out.append(r)
        print(json.dumps({"max_age_hours": max_hours, "checked_at": now().isoformat(), "records": out}, indent=2))
        return 1 if any_stale else 0

    cache.mkdir(parents=True, exist_ok=True)
    for fid in ids:
        dst = cache / f"{fid}.md"
        if a.action == "adopt":
            src = BUNDLED / f"{fid}.md"
            if not src.exists():
                print(f"{fid}: no bundled record", file=sys.stderr)
                continue
            if not dst.exists():
                shutil.copyfile(src, dst)
            print(f"{fid}: cached at {dst}")
        else:  # mark
            if not dst.exists():
                print(f"{fid}: not in cache; adopt or write it first", file=sys.stderr)
                continue
            t = dst.read_text(encoding="utf-8")
            stamp = now().replace(microsecond=0).isoformat().replace("+00:00", "Z")
            if re.search(r"^last_verified:", t, re.M):
                t = re.sub(r"^last_verified:.*$", f"last_verified: {stamp}", t, count=1, flags=re.M)
            else:
                t = t.replace("\nverification:", f"\nlast_verified: {stamp}\nverification:", 1)
            dst.write_text(t, encoding="utf-8")
            print(f"{fid}: last_verified = {stamp}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
