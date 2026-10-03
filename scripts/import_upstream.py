#!/usr/bin/env python3
"""Import the full awesome-web-security live index into a local snapshot."""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
UPSTREAM_URL = "https://raw.githubusercontent.com/qazbnm456/awesome-web-security/master/data/index.json"
OUT_DIR = ROOT / "data" / "upstream" / "awesome-web-security"
INDEX_PATH = OUT_DIR / "index.json"
MANIFEST_PATH = OUT_DIR / "manifest.json"
MAPPING_PATH = OUT_DIR / "mapping.yml"


def fetch(url: str) -> bytes:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "practical-awesome-web-security-import/1.0",
            "Accept": "application/json,text/plain;q=0.9,*/*;q=0.1",
        },
    )
    with urllib.request.urlopen(request, timeout=60) as response:  # noqa: S310 - fixed public URL
        return response.read()


def load_existing_mapping() -> dict[str, str]:
    if not MAPPING_PATH.exists():
        return {}
    try:
        import yaml

        data = yaml.safe_load(MAPPING_PATH.read_text(encoding="utf-8")) or {}
        rows = data.get("entries", []) if isinstance(data, dict) else []
        return {str(row.get("upstream_id")): str(row.get("status", "imported-only")) for row in rows if row.get("upstream_id")}
    except Exception:
        return {}


def write_mapping(entries: list[dict]) -> None:
    import yaml

    existing_status = load_existing_mapping()
    rows = []
    for entry in sorted(entries, key=lambda item: item.get("id", "")):
        upstream_id = entry.get("id")
        rows.append(
            {
                "upstream_id": upstream_id,
                "url": entry.get("url"),
                "title": entry.get("title"),
                "upstream_category": entry.get("category"),
                "upstream_status": entry.get("status"),
                "languages": entry.get("languages") or [],
                "canonical_resource_id": None,
                "primary_topic": None,
                "curation_status": existing_status.get(upstream_id, "imported-only"),
                "notes": "Preserved from upstream snapshot; not yet a curated recommendation.",
            }
        )
    payload = {
        "schema_version": 1,
        "source": "qazbnm456/awesome-web-security live index",
        "generated_from": "index.json",
        "entries": rows,
    }
    MAPPING_PATH.write_text(yaml.safe_dump(payload, sort_keys=False, allow_unicode=True), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--url", default=UPSTREAM_URL)
    parser.add_argument("--no-fetch", action="store_true", help="Validate and refresh mapping/manifest from existing snapshot only.")
    args = parser.parse_args()

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    if args.no_fetch:
        if not INDEX_PATH.exists():
            print("No existing upstream snapshot found", file=sys.stderr)
            return 1
        raw = INDEX_PATH.read_bytes()
    else:
        raw = fetch(args.url)
        INDEX_PATH.write_bytes(raw)

    try:
        index = json.loads(raw)
    except json.JSONDecodeError as exc:
        print(f"Invalid JSON from upstream: {exc}", file=sys.stderr)
        return 1

    categories = index.get("categories")
    entries = index.get("entries")
    if not isinstance(categories, list) or not isinstance(entries, list):
        print("Upstream index missing categories or entries arrays", file=sys.stderr)
        return 1

    entry_ids = [entry.get("id") for entry in entries if isinstance(entry, dict)]
    duplicate_ids = sorted({item for item in entry_ids if entry_ids.count(item) > 1})
    digest = hashlib.sha256(raw).hexdigest()
    manifest = {
        "schema_version": 1,
        "source_url": args.url,
        "fetched_at": dt.datetime.now(dt.timezone.utc).isoformat(),
        "sha256": digest,
        "category_count": len(categories),
        "entry_count": len(entries),
        "duplicate_entry_ids": duplicate_ids,
        "note": "Full upstream snapshot preservation. Presence here is provenance, not project curation or verification.",
    }
    MANIFEST_PATH.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    write_mapping(entries)

    print(json.dumps(manifest, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
