# Coverage & Gaps

Last local inventory: **2026-10-03**. This report separates snapshot preservation, structural coverage, authored content, and research quality. None of these counts is a claim that the knowledge base is complete.

## Snapshot preservation

- Source: `qazbnm456/awesome-web-security` `data/index.json`.
- Snapshot: `data/upstream/awesome-web-security/index.json`.
- Manifest: `data/upstream/awesome-web-security/manifest.json`.
- Mapping: `data/upstream/awesome-web-security/mapping.yml`.
- Generated catalog: [Full Upstream Catalog](../docs/upstream/README.md).
- The existing local snapshot contains **535 entries across 100 categories**. These counts were rechecked locally; the upstream index was not refetched for this inventory.

The snapshot preserves catalog records and links, not the full texts of linked works. Inclusion in the upstream catalog does not mean this project has reviewed or recommended a source. Existing non-English, historical, duplicate, dead, or unverified upstream records remain preserved.

## Structural topic coverage

All 79 taxonomy IDs have at least one canonical resource whose `primary_topic` matches that ID. First-pass authored topic pages are present in every chapter. This establishes navigation and topic-ID coverage, **not** adequate depth, diverse formats, universal Core coverage, or content accuracy.

| Part | Taxonomy topics | Primary topics represented | Canonical resources | Content status |
|---|---:|---:|---:|---|
| ch01-foundations | 6 | 6 | 7 | First pass; expand explanations and source perspectives |
| ch02-web-architecture | 8 | 8 | 8 | First pass; broaden real architecture and integration examples |
| ch03-identity | 8 | 8 | 11 | First pass; expand original identity analyses and cases |
| ch04-vulnerabilities | 13 | 13 | 14 | First pass; expand vulnerability write-ups and root-cause analyses |
| ch05-browser-protocols | 12 | 12 | 15 | First pass; contextualize protocol research and historical defenses |
| ch06-api-frameworks | 8 | 8 | 9 | First pass; expand framework advisories and workflow cases |
| ch07-cloud-supply-chain | 8 | 8 | 11 | First pass; expand deployment and supply-chain incidents |
| ch08-emerging-practice | 8 | 8 | 8 | First pass; expand original AI research and practical learning material |
| ch09-security-engineering | 8 | 8 | 8 | First pass; review accuracy and broaden engineering evidence |
| **Total** | **79** | **79** | **91** | **Research and content review remain in progress** |

Resource counts in this table count each canonical record once, in its primary chapter. Related-topic views may display the same record elsewhere without creating another source.

## Reviewed catalog breadth and format diversity

The current curated data contains **91 records: 88 Core and 3 Extended**. Existing verification records describe previous source reviews; this inventory did not re-review every external source.

| Recorded type | Canonical records |
|---|---:|
| cheatsheet | 52 |
| documentation | 26 |
| specification | 5 |
| article | 5 |
| tool | 2 |
| lab | 1 |

Cheatsheets account for **57.1%** of the catalog. There are only six represented formats. There are currently no curated records classified as books, courses, talks, advisories, postmortems, incident analyses, exploit write-ups, bug bounty reports, or PoC repositories. Useful cheatsheets should remain; diversity must improve through substantive new sources, not cosmetic reclassification.

## Research expansion in progress

A diversification pass is reading original technical articles, historical vulnerability analyses, first-party incident reports, advisory text, book chapters, and extracted talk slides. Candidates already inspected include AWS idempotent APIs, Semgrep JWT mistakes, original SSTI research, a historical SSRF chain, HTTP/2 and browser-powered desync research, Next.js's middleware postmortem, Cloudflare's parser incident, GitHub Actions trust boundaries, Codecov's uploader incident, and public TLS/overload book chapters.

**These diversification candidates have not yet been integrated into the canonical YAML catalog.** Downloaded pages are not automatically reviewed; reviewed candidates are not automatically published records. The original 2019 desync article already has a canonical record and must not be counted again. A Duo SAML retrieval returned an unrelated tracking page and is not valid review evidence.

Outstanding work:

- Integrate substantively reviewed candidates with honest review scope, historical context, and deduplicated provenance.
- Continue broad research across all nine chapters, including lawful book samples, courses, talk material, labs, public repositories, advisories, and real cases.
- Update the upstream mapping when an upstream source becomes curated; preserve many-to-one provenance.
- Add cited findings by chapter and reflect selected diverse readings in all three learning paths.
- Review inaccurate absolutes about DAST, RAG controls, HTTPS/privacy, referrers, IMDSv2, and virtual patching.
- Refine outdated desync mitigation claims; client-facing HTTP/2 does not eliminate risks from HTTP/1.1 downgrading.
- Fix and verify internal paths and anchors, including the tester path's evidence/disclosure links.

## Validation limits

- `scripts/validate.py` checks selected schema fields, enums, canonical ID/URL duplication, topic references, and snapshot/mapping ID counts.
- `scripts/generate.py --check` checks whether generated output matches current data. It does not judge curation quality.
- The four current unit tests cover selected fixture/data properties, topic-ID coverage, and absence of one placeholder phrase. They do not fully exercise importer behavior or validator rejection cases.
- The current validator does **not** check Markdown paths and anchors.
- A full external-link health pass has not been completed. Successful research fetches are not a catalog-wide link check.
- Structural checks do not prove that every verification record is accurate, that every source was completely read, or that the repository is comprehensive.

## Access, rights, and realistic sources

Published offensive research, public PoCs, bug bounty reports, and tradecraft may be read and contextualized for learning. No exploit code, malware, PoC scripts, live-target scans, or credential tests are executed as part of this research. Historical or limited-access sources need explicit context and review-scope labels. No license has been selected for newly authored material; linked works retain their respective rights.
