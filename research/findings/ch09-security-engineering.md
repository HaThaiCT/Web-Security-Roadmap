# Chapter 9 — Security Architecture & Engineering Findings

## 2026-10-03 batch

### MDN — Practical security implementation guides

- URL: <https://developer.mozilla.org/en-US/docs/Web/Security/Practical_implementation_guides>
- Method: WebFetch public page reading.
- Verification scope: public English index page and control table inspected; linked sub-guides not exhaustively inspected in this batch.
- Promoted resource: `mdn-practical-security-implementation-guides` in `data/resources/ch09-security-engineering.yml`.

Useful observations:

- MDN presents this page as an index of practical guides for protecting sensitive user information, connected to Mozilla HTTP Observatory audit recommendations.
- The inspected table orders controls by implementation priority and includes impact/difficulty labels. This makes the page useful for developers turning vulnerability knowledge into implementation work.
- Covered controls include TLS configuration, HTTPS resource loading, HTTPS redirection, HSTS, clickjacking prevention, CSRF prevention, secure cookies, CORP, MIME type verification, CSP, CORS, Referrer-Policy, robots.txt and SRI.
- The page is a good Chapter 9 resource because it supports hardening and secure defaults rather than explaining a single vulnerability class in isolation.

Limits and follow-up:

- This is an index page. Future curation should inspect individual sub-guides, especially HSTS, secure cookies, CSP, CORS, CSRF and clickjacking.
- It should be paired with testing/verifications sources so implementation guidance becomes reviewable requirements and regression checks.

### OWASP — Application Security Verification Standard

- URL: <https://owasp.org/www-project-application-security-verification-standard/>
- Method: WebFetch public project page reading.
- Verification scope: public OWASP project page inspected; full standard documents not exhaustively inspected in this batch.
- Promoted resource: `owasp-application-security-verification-standard` in `data/resources/ch09-security-engineering.yml`.

Useful observations:

- The project page describes ASVS as a structured requirements list for secure development and application security verification.
- It aims to normalize the coverage and rigor of application security verification, which fits Chapter 9's role of converting vulnerability knowledge into engineering requirements and assurance.
- The page states that requirements use chapter.section.requirement numbering and recommends versioned references, which is important for stable links from docs, tests and reports.
- It notes CSV/JSON formats and latest stable release v5.0.0, which can support future local tooling or mappings without scraping prose.

Limits and follow-up:

- Because only the project page was inspected in this batch, the resource is marked `public-excerpt-reviewed`. Specific ASVS requirement chapters should be inspected before mapping detailed controls.
- Future work should connect ASVS requirements to this repository's topics and learning paths without presenting ASVS as a beginner reading assignment in full.

### Swissky and contributors — PayloadsAllTheThings

- URL: <https://github.com/swisskyrepo/PayloadsAllTheThings>
- Method: WebFetch repository structure, documentation, and methodology inspection.
- Verification scope: repository structure, READMEs, and methodology sections inspected; no exploit payloads executed.
- Promoted resource: `payloadsallthethings-repository` in `data/resources/ch09-security-engineering.yml`.

Useful observations:

- Authoritative, widely referenced repository providing comprehensive testing methodology, payload lists, and bypasses across modern web application vulnerabilities.
- Covers SQLi, NoSQLi, Command Injection, Directory Traversal, SSTI, Deserialization, Race Conditions, Request Smuggling, and Prompt Injection.
- Provides boundary-case inputs that illustrate how parsers, sanitizers, and web application firewalls (WAFs) fail when handling non-standard encodings, unusual delimiters, or parser desynchronization.
- Crucial reference for authorized testers constructing targeted test cases and AppSec engineers evaluating defensive filter robustness.

### OWASP — Threat Modeling Cheat Sheet

- URL: <https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html>
- Method: Exa search and Jina Reader inspection of public cheat sheet.
- Verification scope: relevant English threat modeling cheat sheet sections inspected; no external threat model files processed.
- Promoted resource: `owasp-threat-modeling-cheat-sheet` in `data/resources/ch09-security-engineering.yml`.

Useful observations:

- Establishes a structured, repeatable methodology for evaluating software systems from an adversarial perspective during design and development.
- Anchored in the Threat Modeling Manifesto's four fundamental questions:
  1. What are we working on?
  2. What can go wrong?
  3. What are we going to do about it?
  4. Did we do a good enough job?
- Explores system decomposition through Data Flow Diagrams (DFDs), identifying processes, data stores, data flows, and critical trust boundaries where privilege levels change.
- Details the STRIDE mnemonic for threat categorization mapped to security attributes:
  - **Spoofing** (violates Authenticity)
  - **Tampering** (violates Integrity)
  - **Repudiation** (violates Non-repudiation)
  - **Information Disclosure** (violates Confidentiality)
  - **Denial of Service** (violates Availability)
  - **Elevation of Privilege** (violates Authorization)
- Defines actionable risk responses: Mitigate (implement controls), Eliminate (remove risky feature), Transfer (shift to third-party/customer), Accept (document formal business sign-off).
- Connects threat modeling directly to NIST SP 800-218 (Secure Software Development Framework) and OWASP ASVS verification criteria.

### OWASP — Secure Product Design Cheat Sheet

- URL: <https://cheatsheetseries.owasp.org/cheatsheets/Secure_Product_Design_Cheat_Sheet.html>
- Method: WebFetch public page reading.
- Verification scope: relevant English secure product design cheat sheet sections inspected; no design artifacts created.
- Promoted resource: `owasp-secure-product-design-cheat-sheet` in `data/resources/ch09-security-engineering.yml`.

Useful observations:

- Frames application security as an architectural discipline that begins at product conception and evolves continuously through implementation and deployment.
- Establishes four foundational security design principles:
  1. Least Privilege & Separation of Duties: Restrict user and service rights to the absolute minimum necessary; ensure sensitive multi-step actions require dual authorization.
  2. Defense-in-Depth: Layer controls across networking, application logic, and storage so that the failure of any single barrier does not result in total system compromise.
  3. Zero Trust: Treat all callers, network segments, and internal microservices as inherently untrusted until authenticated and continuously verified.
  4. Security-in-the-Open: Avoid relying on security through obscurity; validate architecture against open standards and adversarial peer review.
- Structures product security reviews across five focal areas:
  - Context (organizational risk profile and regulatory boundaries).
  - Components (inventorying, scanning, and validating open-source libraries and SaaS dependencies).
  - Connections (data flows, protocol encryption, and API endpoints).
  - Code (secure coding standards, input validation, and fail-safe error handling).
  - Configuration (hardened production defaults, automated patch management, and secrets separation).

Limits and follow-up:

- Secure design principles provide the overarching strategy; pair with Threat Modeling (Chapter 9), Verification Standards (ASVS), and specific vulnerability chapters.


