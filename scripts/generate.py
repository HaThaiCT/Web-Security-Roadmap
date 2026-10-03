#!/usr/bin/env python3
"""Generate Markdown catalog pages from local YAML/JSON data."""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs"
RESOURCES_DIR = DATA / "resources"
UPSTREAM_DIR = DATA / "upstream" / "awesome-web-security"
GENERATED = "<!-- GENERATED FILE: do not edit by hand. Run scripts/generate.py. -->\n\n"


def slug(value: str) -> str:
    value = value.lower().strip()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-") or "item"


def read_yaml(path: Path) -> Any:
    if not path.exists():
        return None
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def write_if_changed(path: Path, content: str, check: bool, changed: list[Path]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    old = path.read_text(encoding="utf-8") if path.exists() else None
    if old != content:
        changed.append(path)
        if not check:
            path.write_text(content, encoding="utf-8")


def load_taxonomy() -> dict[str, Any]:
    taxonomy = read_yaml(DATA / "taxonomy.yml") or {}
    if not isinstance(taxonomy, dict):
        raise SystemExit("taxonomy.yml must contain an object")
    return taxonomy


def load_resources() -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    if not RESOURCES_DIR.exists():
        return rows
    for path in sorted(RESOURCES_DIR.glob("*.yml")):
        data = read_yaml(path) or []
        if not isinstance(data, list):
            continue
        for row in data:
            if isinstance(row, dict):
                row = dict(row)
                row.setdefault("_source_file", str(path.relative_to(ROOT)))
                rows.append(row)
    return rows


def resource_line(resource: dict[str, Any]) -> str:
    audiences = ", ".join(resource.get("audiences") or [])
    meta = [str(resource.get("type", "resource")), str(resource.get("difficulty", "unknown"))]
    if audiences:
        meta.append(audiences)
    cost = resource.get("cost")
    access = resource.get("access")
    if cost or access:
        meta.append("/".join(str(x) for x in [cost, access] if x))
    annotation = str(resource.get("annotation", "")).strip()
    return (
        f"- **[{resource.get('title')}]({resource.get('url')})** — "
        f"*{' · '.join(meta)}*  \n  {annotation}"
    )


def generate_chapter_resources(taxonomy: dict[str, Any], resources: list[dict[str, Any]], check: bool, changed: list[Path]) -> None:
    by_topic: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for resource in resources:
        topic_ids = [resource.get("primary_topic")] + list(resource.get("related_topics") or [])
        for topic_id in topic_ids:
            if topic_id:
                by_topic[str(topic_id)].append(resource)

    for chapter in taxonomy.get("chapters", []) or []:
        chapter_id = chapter.get("id")
        title = chapter.get("title", chapter_id)
        lines = [GENERATED.rstrip(), f"# Curated Resources — {title}", ""]
        for topic in chapter.get("topics", []) or []:
            tid = topic.get("id")
            lines.extend([f"<a id=\"{tid}\"></a>", f"## {topic.get('title')}", ""])
            topic_resources = sorted(by_topic.get(tid, []), key=lambda r: (r.get("tier") != "core", r.get("title", "")))
            if not topic_resources:
                lines.append("No curated resources have been published for this topic yet. See `research/coverage.md` for gaps.\n")
                continue
            core = [r for r in topic_resources if r.get("tier") == "core"]
            extended = [r for r in topic_resources if r.get("tier") == "extended"]
            if core:
                lines.extend(["### Core", ""])
                lines.extend(resource_line(r) for r in core)
                lines.append("")
            if extended:
                lines.extend(["### Extended", ""])
                lines.extend(resource_line(r) for r in extended)
                lines.append("")
        write_if_changed(DOCS / "topics" / str(chapter_id) / "resources.md", "\n".join(lines).rstrip() + "\n", check, changed)


def generate_extended(taxonomy: dict[str, Any], resources: list[dict[str, Any]], check: bool, changed: list[Path]) -> None:
    by_chapter: dict[str, list[dict[str, Any]]] = defaultdict(list)
    topic_to_chapter: dict[str, str] = {}
    for chapter in taxonomy.get("chapters", []) or []:
        for topic in chapter.get("topics", []) or []:
            topic_to_chapter[topic.get("id")] = chapter.get("id")
    for resource in resources:
        if resource.get("tier") == "extended":
            chapter_id = topic_to_chapter.get(resource.get("primary_topic"), "uncategorized")
            by_chapter[chapter_id].append(resource)
    for chapter in taxonomy.get("chapters", []) or []:
        cid = chapter.get("id")
        lines = [GENERATED.rstrip(), f"# Extended Resources — {chapter.get('title')}", ""]
        rows = sorted(by_chapter.get(cid, []), key=lambda r: r.get("title", ""))
        if rows:
            lines.extend(resource_line(r) for r in rows)
        else:
            lines.append("No extended resources have been published for this chapter yet.")
        write_if_changed(DOCS / "extended" / f"{cid}.md", "\n".join(lines).rstrip() + "\n", check, changed)


def table_row(resource: dict[str, Any]) -> str:
    return "| " + " | ".join(
        [
            f"[{resource.get('title')}]({resource.get('url')})",
            str(resource.get("type", "")),
            str(resource.get("difficulty", "")),
            ", ".join(resource.get("audiences") or []),
            str(resource.get("tier", "")),
            str(resource.get("primary_topic", "")),
        ]
    ) + " |"


def generate_indexes(resources: list[dict[str, Any]], check: bool, changed: list[Path]) -> None:
    header = "| Resource | Type | Difficulty | Audiences | Tier | Primary topic |\n|---|---|---|---|---|---|"
    dimensions = {
        "by-type": lambda r: str(r.get("type", "unknown")),
        "by-difficulty": lambda r: str(r.get("difficulty", "unknown")),
        "by-audience": lambda r: ", ".join(r.get("audiences") or ["unknown"]),
        "by-topic": lambda r: str(r.get("primary_topic", "unknown")),
    }
    for name, key_fn in dimensions.items():
        grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
        for resource in resources:
            grouped[key_fn(resource)].append(resource)
        lines = [GENERATED.rstrip(), f"# Resources {name.replace('-', ' ').title()}", ""]
        for key in sorted(grouped):
            lines.extend([f"## {key}", "", header])
            lines.extend(table_row(r) for r in sorted(grouped[key], key=lambda x: x.get("title", "")))
            lines.append("")
        write_if_changed(DOCS / "indexes" / f"{name}.md", "\n".join(lines).rstrip() + "\n", check, changed)


def load_upstream() -> tuple[list[dict[str, Any]], list[dict[str, Any]], dict[str, Any]]:
    index_path = UPSTREAM_DIR / "index.json"
    manifest_path = UPSTREAM_DIR / "manifest.json"
    if not index_path.exists():
        return [], [], {}
    data = json.loads(index_path.read_text(encoding="utf-8"))
    manifest = json.loads(manifest_path.read_text(encoding="utf-8")) if manifest_path.exists() else {}
    return data.get("categories", []) or [], data.get("entries", []) or [], manifest


def upstream_entry_line(entry: dict[str, Any]) -> str:
    language = ", ".join(entry.get("languages") or [])
    meta = " · ".join(str(x) for x in [entry.get("type"), entry.get("difficulty"), language, entry.get("status")] if x)
    title = entry.get("title") or entry.get("id")
    archive = f" Archive: {entry.get('archive_url')}" if entry.get("archive_url") else ""
    return f"- **[{title}]({entry.get('url')})** — *{meta}*. Upstream ID: `{entry.get('id')}`.{archive}"


def generate_upstream(check: bool, changed: list[Path]) -> None:
    categories, entries, manifest = load_upstream()
    if not entries:
        return
    by_category: dict[str, list[dict[str, Any]]] = defaultdict(list)
    by_status: dict[str, list[dict[str, Any]]] = defaultdict(list)
    by_language: dict[str, list[dict[str, Any]]] = defaultdict(list)
    by_type: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for entry in entries:
        by_category[str(entry.get("category", "uncategorized"))].append(entry)
        by_status[str(entry.get("status", "unknown"))].append(entry)
        by_type[str(entry.get("type", "unknown"))].append(entry)
        langs = entry.get("languages") or ["unknown"]
        for lang in langs:
            by_language[str(lang)].append(entry)

    lines = [
        GENERATED.rstrip(),
        "# Full Upstream Catalog — awesome-web-security",
        "",
        "This catalog preserves the upstream entries as provenance. Presence here is not this project's content review or recommendation.",
        "",
        f"- Source URL: `{manifest.get('source_url', '')}`",
        f"- Fetched at: `{manifest.get('fetched_at', '')}`",
        f"- Categories: **{manifest.get('category_count', len(categories))}**",
        f"- Entries: **{manifest.get('entry_count', len(entries))}**",
        f"- SHA-256: `{manifest.get('sha256', '')}`",
        "",
        "## Views",
        "",
        "- [By status](by-status.md)",
        "- [By language](by-language.md)",
        "- [By type](by-type.md)",
        "- [Categories](categories/README.md)",
        "",
    ]
    write_if_changed(DOCS / "upstream" / "README.md", "\n".join(lines).rstrip() + "\n", check, changed)

    for name, grouped in [("by-status", by_status), ("by-language", by_language), ("by-type", by_type)]:
        lines = [GENERATED.rstrip(), f"# Upstream {name.replace('-', ' ').title()}", ""]
        for key in sorted(grouped):
            lines.extend([f"## {key}", ""])
            lines.extend(upstream_entry_line(e) for e in sorted(grouped[key], key=lambda item: item.get("title", "")))
            lines.append("")
        write_if_changed(DOCS / "upstream" / f"{name}.md", "\n".join(lines).rstrip() + "\n", check, changed)

    category_titles = {c.get("key"): c.get("title") for c in categories}
    lines = [GENERATED.rstrip(), "# Upstream Categories", ""]
    for key in sorted(by_category):
        path = f"{slug(key)}.md"
        lines.append(f"- [{category_titles.get(key, key)}](categories/{path}) — `{key}` ({len(by_category[key])})")
        clines = [GENERATED.rstrip(), f"# {category_titles.get(key, key)}", "", f"Upstream category key: `{key}`", ""]
        clines.extend(upstream_entry_line(e) for e in sorted(by_category[key], key=lambda item: item.get("title", "")))
        write_if_changed(DOCS / "upstream" / "categories" / path, "\n".join(clines).rstrip() + "\n", check, changed)
    write_if_changed(DOCS / "upstream" / "categories" / "README.md", "\n".join(lines).rstrip() + "\n", check, changed)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Fail if generated files are not up to date.")
    args = parser.parse_args()

    taxonomy = load_taxonomy()
    resources = load_resources()
    changed: list[Path] = []
    generate_chapter_resources(taxonomy, resources, args.check, changed)
    generate_extended(taxonomy, resources, args.check, changed)
    generate_indexes(resources, args.check, changed)
    generate_upstream(args.check, changed)

    if args.check and changed:
        print("Generated files are out of date:", file=sys.stderr)
        for path in changed:
            print(path.relative_to(ROOT), file=sys.stderr)
        return 1
    if changed:
        print("Updated generated files:")
        for path in changed:
            print(path.relative_to(ROOT))
    else:
        print("Generated files are up to date")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
