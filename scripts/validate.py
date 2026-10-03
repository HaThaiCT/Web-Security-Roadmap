#!/usr/bin/env python3
"""Validate taxonomy, curated resources, and upstream snapshot/mapping."""
from __future__ import annotations

import json
import sys
from pathlib import Path
from urllib.parse import urlparse

import yaml

ROOT = Path(__file__).resolve().parents[1]
TAXONOMY = ROOT / "data" / "taxonomy.yml"
RESOURCES_DIR = ROOT / "data" / "resources"
UPSTREAM_DIR = ROOT / "data" / "upstream" / "awesome-web-security"

REQUIRED_RESOURCE_FIELDS = {
    "id",
    "title",
    "url",
    "type",
    "language",
    "difficulty",
    "audiences",
    "primary_topic",
    "tier",
    "annotation",
    "cost",
    "access",
    "verification",
    "provenance",
}
ALLOWED_TYPES = {
    "documentation",
    "specification",
    "article",
    "advisory",
    "postmortem",
    "incident-analysis",
    "exploit-writeup",
    "bug-bounty-report",
    "poc-repository",
    "talk",
    "book",
    "course",
    "lab",
    "tool",
    "payload-list",
    "cheatsheet",
    "community",
    "tradecraft-note",
    "archived-material",
}
ALLOWED_DIFFICULTIES = {"beginner", "intermediate", "advanced"}
ALLOWED_TIERS = {"core", "extended"}
ALLOWED_AUDIENCES = {"learner", "tester", "developer"}
ALLOWED_COSTS = {"free", "paid", "mixed", "unknown"}
ALLOWED_ACCESS = {"public", "registration-required", "subscription-required", "mixed", "unknown"}
ALLOWED_VERIFICATION_STATUSES = {"content-reviewed", "public-excerpt-reviewed"}
ALLOWED_PROVENANCE_ORIGINS = {"upstream", "additional-research", "both"}


def load_yaml(path: Path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def taxonomy_topics(errors: list[str]) -> tuple[set[str], set[str]]:
    data = load_yaml(TAXONOMY)
    chapters = data.get("chapters", []) if isinstance(data, dict) else []
    chapter_ids: set[str] = set()
    topic_ids: set[str] = set()
    for chapter in chapters:
        cid = chapter.get("id")
        if not cid:
            fail(errors, "Chapter without id")
            continue
        if cid in chapter_ids:
            fail(errors, f"Duplicate chapter id: {cid}")
        chapter_ids.add(cid)
        for topic in chapter.get("topics", []) or []:
            tid = topic.get("id")
            if not tid:
                fail(errors, f"Topic without id in {cid}")
                continue
            if tid in topic_ids:
                fail(errors, f"Duplicate topic id: {tid}")
            topic_ids.add(tid)
    return chapter_ids, topic_ids


def validate_resources(errors: list[str], topic_ids: set[str]) -> None:
    if not RESOURCES_DIR.exists():
        return
    ids: dict[str, Path] = {}
    urls: dict[str, Path] = {}
    for path in sorted(RESOURCES_DIR.glob("*.yml")):
        rows = load_yaml(path) or []
        if not isinstance(rows, list):
            fail(errors, f"{path}: expected a YAML list")
            continue
        for i, row in enumerate(rows, start=1):
            prefix = f"{path}:{i}"
            if not isinstance(row, dict):
                fail(errors, f"{prefix}: row is not an object")
                continue
            missing = REQUIRED_RESOURCE_FIELDS - set(row)
            if missing:
                fail(errors, f"{prefix}: missing fields {sorted(missing)}")
            rid = row.get("id")
            if rid in ids:
                fail(errors, f"Duplicate resource id {rid}: {ids[rid]} and {path}")
            elif rid:
                ids[str(rid)] = path
            url = row.get("url")
            if url:
                parsed = urlparse(str(url))
                if parsed.scheme not in {"http", "https"} or not parsed.netloc:
                    fail(errors, f"{prefix}: invalid URL {url}")
                if url in urls:
                    fail(errors, f"Duplicate canonical URL {url}: {urls[url]} and {path}")
                else:
                    urls[str(url)] = path
            primary = row.get("primary_topic")
            if primary and primary not in topic_ids:
                fail(errors, f"{prefix}: unknown primary_topic {primary}")
            for topic in row.get("related_topics") or []:
                if topic not in topic_ids:
                    fail(errors, f"{prefix}: unknown related topic {topic}")
            if row.get("type") not in ALLOWED_TYPES:
                fail(errors, f"{prefix}: invalid type {row.get('type')}")
            if row.get("difficulty") not in ALLOWED_DIFFICULTIES:
                fail(errors, f"{prefix}: invalid difficulty {row.get('difficulty')}")
            if row.get("tier") not in ALLOWED_TIERS:
                fail(errors, f"{prefix}: invalid tier {row.get('tier')}")
            audiences = set(row.get("audiences") or [])
            if not audiences or audiences - ALLOWED_AUDIENCES:
                fail(errors, f"{prefix}: invalid audiences {sorted(audiences)}")
            if row.get("language") != "en":
                fail(errors, f"{prefix}: curated resources must be English; got {row.get('language')}")
            if row.get("cost") not in ALLOWED_COSTS:
                fail(errors, f"{prefix}: invalid cost {row.get('cost')}")
            if row.get("access") not in ALLOWED_ACCESS:
                fail(errors, f"{prefix}: invalid access {row.get('access')}")
            verification = row.get("verification") or {}
            if not isinstance(verification, dict) or not verification.get("status") or not verification.get("evidence"):
                fail(errors, f"{prefix}: verification.status and evidence are required")
            elif verification.get("status") not in ALLOWED_VERIFICATION_STATUSES:
                fail(errors, f"{prefix}: invalid verification.status {verification.get('status')}")
            provenance = row.get("provenance") or {}
            if not isinstance(provenance, dict) or not provenance.get("origin"):
                fail(errors, f"{prefix}: provenance.origin is required")
            elif provenance.get("origin") not in ALLOWED_PROVENANCE_ORIGINS:
                fail(errors, f"{prefix}: invalid provenance.origin {provenance.get('origin')}")


def validate_upstream(errors: list[str]) -> None:
    index_path = UPSTREAM_DIR / "index.json"
    mapping_path = UPSTREAM_DIR / "mapping.yml"
    manifest_path = UPSTREAM_DIR / "manifest.json"
    if not index_path.exists():
        fail(errors, "Missing upstream index.json; run scripts/import_upstream.py")
        return
    if not mapping_path.exists():
        fail(errors, "Missing upstream mapping.yml; run scripts/import_upstream.py")
        return
    if not manifest_path.exists():
        fail(errors, "Missing upstream manifest.json; run scripts/import_upstream.py")
    index = json.loads(index_path.read_text(encoding="utf-8"))
    entries = index.get("entries", [])
    if not isinstance(entries, list):
        fail(errors, "Upstream index entries is not a list")
        return
    upstream_ids = {entry.get("id") for entry in entries if isinstance(entry, dict) and entry.get("id")}
    mapping = load_yaml(mapping_path) or {}
    rows = mapping.get("entries", []) if isinstance(mapping, dict) else []
    mapped_ids = {row.get("upstream_id") for row in rows if isinstance(row, dict) and row.get("upstream_id")}
    missing = sorted(upstream_ids - mapped_ids)
    extra = sorted(mapped_ids - upstream_ids)
    if missing:
        fail(errors, f"Upstream entries missing from mapping: {missing[:20]}{'...' if len(missing) > 20 else ''}")
    if extra:
        fail(errors, f"Mapping contains IDs not present in snapshot: {extra[:20]}{'...' if len(extra) > 20 else ''}")
    if len(rows) != len(entries):
        fail(errors, f"Mapping row count {len(rows)} != upstream entry count {len(entries)}")


def main() -> int:
    errors: list[str] = []
    _chapters, topics = taxonomy_topics(errors)
    validate_resources(errors, topics)
    validate_upstream(errors)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("Validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
