# Web Secuirty Roadmap

A practical, curated Web Security knowledge base built around three ways to use the same material:

1. **Follow a learning path** for your role and current level.
2. **Browse the nine-part knowledge map** when you know the topic you need.
3. **Search the full upstream catalog** imported from `qazbnm456/awesome-web-security` when you want the preserved source list.

This repository is independent from the installed `awesome-web-security` plugin. It preserves the upstream catalog as provenance, then adds a curated English catalog and practical guidance for learning, authorized testing, and secure engineering.

## What this repository is

- A practical Web Security map with topic overviews, reading order, and curated resources.
- A full local snapshot of the upstream `awesome-web-security` index.
- A set of role-oriented learning paths for:
  - [Learner](docs/learning-paths/learner.md)
  - [Authorized Tester / Researcher](docs/learning-paths/authorized-tester-researcher.md)
  - [Developer / AppSec](docs/learning-paths/developer-appsec.md)
- A maintainable data model that separates upstream preservation from curated recommendations.

## What this repository is not

- It is not a claim to have read or verified every upstream entry.
- It is not a live-target testing playbook.
- It does not execute PoCs, exploit code, malware, or scans.
- It does not copy full articles, books, videos, or source repositories.
- It does not choose a license for newly authored material yet.

## Start here

### I want to learn Web Security

Use the [Learner path](docs/learning-paths/learner.md). It starts with the web model and request lifecycle, then moves into identity, common vulnerability classes, browser/client risks, APIs, and system-level security engineering.

### I want to test authorized targets

Use the [Authorized Tester / Researcher path](docs/learning-paths/authorized-tester-researcher.md). It emphasizes methodology, evidence, impact, realistic write-ups, lab practice, and keeping testing inside authorization boundaries.

### I want to build or fix secure systems

Use the [Developer / AppSec path](docs/learning-paths/developer-appsec.md). It prioritizes secure implementation, controls, code review, regression tests, deployment, and security engineering decisions.

### I want the original upstream list

Browse the [Full Upstream Catalog](docs/upstream/README.md). This is a preserved snapshot of the upstream entries. Inclusion there means the entry existed upstream; it does **not** mean this project has reviewed or recommended it.

## Nine-part knowledge map

The nine parts are reference sections, not a mandatory linear course. Learning paths link to the sections, topics, and resources that fit each audience.

| Part | Topic page | Curated resources |
|---|---|---|
| 1. Web Foundations & Standards | [Overview](docs/topics/ch01-foundations/README.md) | [Resources](docs/topics/ch01-foundations/resources.md) |
| 2. Web/Software Architecture & Engineering | [Overview](docs/topics/ch02-web-architecture/README.md) | [Resources](docs/topics/ch02-web-architecture/resources.md) |
| 3. Authentication, Authorization & Identity Security | [Overview](docs/topics/ch03-identity/README.md) | [Resources](docs/topics/ch03-identity/resources.md) |
| 4. Vulnerability Classes & Root Causes | [Overview](docs/topics/ch04-vulnerabilities/README.md) | [Resources](docs/topics/ch04-vulnerabilities/resources.md) |
| 5. Browser, Client & Protocol Security | [Overview](docs/topics/ch05-browser-protocols/README.md) | [Resources](docs/topics/ch05-browser-protocols/resources.md) |
| 6. API, Framework & Application Ecosystem Security | [Overview](docs/topics/ch06-api-frameworks/README.md) | [Resources](docs/topics/ch06-api-frameworks/resources.md) |
| 7. Cloud, Deployment & Supply Chain Security | [Overview](docs/topics/ch07-cloud-supply-chain/README.md) | [Resources](docs/topics/ch07-cloud-supply-chain/resources.md) |
| 8. Emerging Web Risks, Privacy & Practical Testing | [Overview](docs/topics/ch08-emerging-practice/README.md) | [Resources](docs/topics/ch08-emerging-practice/resources.md) |
| 9. Security Architecture & Engineering | [Overview](docs/topics/ch09-security-engineering/README.md) | [Resources](docs/topics/ch09-security-engineering/resources.md) |

## Curated indexes

Generated views over reviewed English resources:

- [By type](docs/indexes/by-type.md)
- [By difficulty](docs/indexes/by-difficulty.md)
- [By audience](docs/indexes/by-audience.md)
- [By topic](docs/indexes/by-topic.md)

The curated catalog is intentionally separate from the full upstream catalog. A resource becomes Core or Extended only after relevant content has been inspected and annotated.

## Upstream snapshot status

The current upstream snapshot was imported with:

```bash
python3 scripts/import_upstream.py
```

Generated upstream catalog:

- [Overview](docs/upstream/README.md)
- [By status](docs/upstream/by-status.md)
- [By language](docs/upstream/by-language.md)
- [By type](docs/upstream/by-type.md)
- [Categories](docs/upstream/categories/README.md)

## Local maintenance commands

```bash
python3 scripts/import_upstream.py
python3 scripts/validate.py
python3 scripts/generate.py
python3 scripts/generate.py --check
python3 -m unittest discover -s tests
python3 scripts/check_links.py
```

`import_upstream.py` needs network access. Unit tests should use local fixtures and must not depend on network access.

## Current status

- Full upstream import: implemented.
- Generated upstream catalog: implemented.
- Curated resources: 91 canonical records (88 Core, 3 Extended); 52 are cheatsheets. Broader, more varied curation is still in progress.
- Topic overviews: first-pass content is present across nine parts and 79 topics; accuracy and depth review remain ongoing.
- Learning paths: three role-specific paths are present; selected readings and internal links still need refinement.
- Link checker: implemented for curated resources, with optional upstream checking; a full external-link pass has not been completed.
- Local validation, generation checks, and unit tests cover structural properties, not research completeness or every Markdown anchor.

See [research coverage](research/coverage.md) for gaps and verification status.
