# Catalog Data Contract

The taxonomy is `data/taxonomy.yml`. Topic IDs are globally unique and belong to one chapter. References can cross chapters without duplicating a topic or a canonical resource.

Each `data/resources/<chapter>.yml` is a YAML list. Use this shape:

```yaml
- id: mdn-http-overview
  title: Overview of HTTP
  url: https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview
  author: MDN contributors
  type: documentation
  language: en
  difficulty: beginner
  audiences: [learner, tester, developer]
  primary_topic: http
  related_topics: [request-lifecycle]
  tier: core
  annotation: >-
    Explain the actual contribution, intended reader and important limits.
    Core annotations usually contain two to four useful sentences.
  cost: free
  access: public
  verification:
    status: content-reviewed
    checked_on: '2026-10-03'
    method: jina-reader
    scope: Relevant English sections inspected; no code executed.
    evidence: A concrete content observation, not just a title or HTTP status.
  provenance:
    origin: additional-research
    upstream_ids: []
  archive_url: null
  version_context: null
```

Allowed values:

- `type`: documentation, specification, article, advisory, postmortem, incident-analysis, exploit-writeup, bug-bounty-report, poc-repository, talk, book, course, lab, tool, payload-list, cheatsheet, community, tradecraft-note, archived-material.
- `difficulty`: beginner, intermediate, advanced.
- `audiences`: any nonempty subset of learner, tester, developer.
- `tier`: core, extended. These are curation tiers, **not** difficulty levels.
- `cost`: free, paid, mixed, unknown. Never infer paid content has been inspected.
- `access`: public, registration-required, subscription-required, mixed, unknown. A public course overview is distinct from an account-required exercise.
- `verification.status`: content-reviewed or public-excerpt-reviewed. Use the latter if the recommendation is limited to inspected samples/overview; explicitly state the limit in the annotation and scope.
- `provenance.origin`: upstream, additional-research, both. Agents can initially use additional-research; integration compares against the complete upstream URLs and records exact matches.
- `verification.method`: identify the actual reading route, e.g. jina-reader, webfetch, public-source-file. Search-result snippets alone are insufficient.

No unverified resource is a Core/Extended recommendation. Such candidates belong in research notes. A source need not have been read exhaustively: state precisely which sections or public excerpts were inspected. The full upstream snapshot is preserved separately, including all its languages/statuses and duplicate entries; its metadata is not our verification.

## Authored pages and generated listings

Agents write chapter `docs/topics/<chapter>/README.md` and optional topic pages, plus resources and `research/findings/<chapter>.md`. A topic-page heading or explicit anchor uses its topic ID for reliable path linking. Write meaningful prerequisites, mechanisms, reading order, practical/testing/defensive guidance and misconceptions; not repetitive placeholder prose. A chapter should have an explicit anchored section for each taxonomy topic, with honest gaps if needed.

The generator writes only `docs/topics/<chapter>/resources.md`, `docs/extended/<chapter>.md`, `docs/indexes/*` and `docs/upstream/*`. Do not manually edit generated files. Authored chapter pages link `resources.md#<topic-id>` for curated sources. Topic sections can cross-link other authored chapter pages using relative paths.

Research notes cite inspected original URLs, explain useful observations and exclusions/access limitations, and distinguish actual inspection from proposed future reading. Research is practical, not an academic bibliography. All authored material is English. Do not copy full articles, execute discovered code, install tools, log into services or access credentials.
