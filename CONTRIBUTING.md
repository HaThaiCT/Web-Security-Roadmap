# Contributing

This repository keeps two different catalogs:

1. **Full Upstream Catalog** — preserved data imported from `awesome-web-security`. Do not edit this by hand.
2. **Curated Catalog** — reviewed English resources with annotations, topic ownership, and learning-path use.

## Add or update an upstream snapshot

Run:

```bash
python3 scripts/import_upstream.py
python3 scripts/validate.py
python3 scripts/generate.py
```

Do not manually remove upstream entries because they are non-English, archived-only, blocked, offensive, duplicated, or outside the curated scope. Preserve provenance and use mapping/status fields to explain how the project treats them.

## Add a curated resource

Curated resources live in `data/resources/<chapter>.yml`. Follow `data/SCHEMA.md`.

A curated resource must have:

- English content inspected directly.
- A primary topic from `data/taxonomy.yml`.
- `tier: core` or `tier: extended`.
- A useful annotation grounded in inspected content.
- Verification scope and evidence.
- Provenance that says whether it came from upstream, additional research, or both.

Search snippets, titles, star counts, and hearsay are not enough.

## Offensive or realistic sources

Exploit write-ups, bug bounty reports, public PoC repositories, incident analyses, offensive tradecraft notes, and payload collections can be valuable learning sources. They are not excluded because they are realistic. Treat them carefully:

- Read and summarize; do not execute code.
- Explain version/context limits.
- Prefer mechanism, evidence, root cause, and defensive lessons.
- Do not turn a source into a live-target attack procedure.
- Mark unverified or blocked material honestly.

## Authored pages

Authored chapter pages live at `docs/topics/<chapter>/README.md`. Generated resource pages live at `docs/topics/<chapter>/resources.md` and are overwritten by `scripts/generate.py`.

Each authored topic section should include:

- anchor using the topic ID;
- prerequisites;
- what the mechanism is;
- how to read or reason about it in real systems;
- practical learning or authorized-testing guidance when relevant;
- prevention or remediation guidance when relevant;
- caveats and common misunderstandings;
- a link to the generated resource section.

## Checks

Run before considering the repository healthy:

```bash
python3 scripts/validate.py
python3 scripts/generate.py --check
python3 -m unittest discover -s tests
```

Use `python3 scripts/check_links.py` when you want current external link status. A single network failure is not proof that a source is dead.

## License

The project license for newly authored material and scripts has not been chosen yet. Do not add a license file or license header without an explicit decision. Upstream entries and linked works retain their own rights.
