# Chapter 8 — Emerging Web Risks, Privacy & Practical Testing Findings

## 2026-10-03 batch

### PortSwigger — Web Security Academy

- URL: <https://portswigger.net/web-security>
- Method: WebFetch public page reading.
- Verification scope: public academy landing page and topic list inspected; labs were not executed.
- Promoted resource: `portswigger-web-security-academy` in `data/resources/ch08-emerging-practice.yml`.
- Upstream relation: exact URL appears in upstream as `practices-application-portswigger-web-security-academy`.

Useful observations:

- The inspected page presents the Academy as free web security training in a safe and legal environment, which fits this repository's boundary of learning through labs rather than unauthorized targets.
- The topic list spans foundational and advanced practical areas: SQL injection, XSS, CSRF, SSRF, XXE, JWT attacks, OAuth, race conditions, NoSQL injection, LLM/AI attacks, web cache deception, prototype pollution, API testing, GraphQL and WebSockets.
- Labs are described as realistic puzzles for developing hacker skills, making the Academy useful across learner, authorized tester and developer/AppSec paths.
- The source is best represented as a cross-topic lab hub rather than a single vulnerability reference, so it is owned here under `practice-labs` and linked to many related topics.

Limits and follow-up:

- This batch inspected the public landing page and topic list, not individual lab solutions or exercises.
- Some labs may require a PortSwigger account and Burp Suite. Future per-topic curation should inspect individual academy topic pages before promoting them as Core/Extended under specific vulnerability topics.

### OWASP — Web Security Testing Guide

- URL: <https://owasp.org/www-project-web-security-testing-guide/>
- Method: WebFetch public project page reading.
- Verification scope: public OWASP project page inspected; full versioned guide chapters not exhaustively inspected in this batch.
- Promoted resource: `owasp-web-security-testing-guide` in `data/resources/ch08-emerging-practice.yml`.

Useful observations:

- The project page describes WSTG as a web application security testing resource for developers and security professionals.
- It exposes versioned release information, including stable v4.2 and v5.0 in development, plus hosted documentation and PDF access paths.
- The project framing, contribution guide and code of conduct make it a suitable methodology entry point for authorized testing rather than an ad hoc offensive toolkit.
- In this repository it belongs under `testing-methodology`, with cross-links to evidence/disclosure, labs, Chapter 9 security testing and developer/AppSec review work.

### OWASP — Top 10 for Large Language Model Applications

- URL: <https://genai.owasp.org/llm-top-10/>
- Method: WebFetch / Jina Reader agent-reach public inspection.
- Verification scope: relevant English 2025 risk taxonomy and definitions inspected; no model APIs invoked.
- Promoted resource: `owasp-top-10-for-llm-applications` in `data/resources/ch08-emerging-practice.yml`.

Useful observations:

- Establishes a comprehensive taxonomy for security risks in applications integrating LLMs, covering risks LLM01 through LLM10.
- LLM01: Prompt Injection — separates direct prompt injection (system prompt override / jailbreaks) from indirect prompt injection (attacker embeds instructions in external web content, emails, or untrusted documents parsed by the LLM).
- LLM02: Sensitive Information Disclosure — models inadvertently echoing training data, system instructions, or proprietary information in responses.
- LLM05: Improper Output Handling — blind trust in LLM outputs forwarded into downstream sinks (e.g., rendering raw markdown/HTML leading to XSS, executing LLM-generated code, or generating unparameterized SQL).
- LLM06: Excessive Agency — giving autonomous agents or tool-calling models unnecessary system permissions (e.g., destructive API endpoints, unconstrained file access) without human-in-the-loop validation.
- LLM08: Vector and Embedding Weaknesses — manipulation of retrieval embeddings in RAG systems leading to unauthorized document retrieval across tenant boundaries.
- Defensive architecture requires: strict sandboxing of external data ingestion, dual LLM pattern (quarantined reader vs. executive model), least privilege for tool plugins, and output encoding before execution.

### XS-Leaks Research Community — XS-Leaks Wiki

- URL: <https://xsleaks.dev/>
- Method: WebFetch public wiki documentation reading.
- Verification scope: relevant English XS-Leaks concept, attack, and defense wiki sections inspected; no timing probes executed.
- Promoted resource: `xs-leaks-wiki` in `data/resources/ch08-emerging-practice.yml`.

Useful observations:

- Defines Cross-Site Leaks (XS-Leaks) as a vulnerability class exploiting web platform features and browser side channels to infer sensitive user information across origins without directly violating the Same-Origin Policy (SOP).
- Breaks down browser side-channel attack vectors:
  - Network and Execution Timing Oracles: Measuring the time required to load cross-origin resources to determine application state (e.g. searching for a string: results take longer to render than empty responses, creating Cross-Site Search / XS-Search).
  - Frame Counting: Abusing `window.length` on cross-origin iframe references to determine how many frames or elements were rendered.
  - Error and Event Oracles: Monitoring `onload` vs `onerror` events or DOM resolution changes on media or script tags to leak boolean states.
  - Navigation Timing & Cache Probing: Detecting whether a specific resource exists in the browser cache to track user history or authenticated status.
- Documents modern browser defenses:
  - Fetch Metadata request headers (`Sec-Fetch-Site`, `Sec-Fetch-Mode`, `Sec-Fetch-Dest`): Enabling backend endpoints to reject cross-site subresource or navigation requests by default.
  - Cross-Origin-Opener-Policy (`COOP: same-origin`): Isolates top-level browsing contexts, preventing cross-origin windows from obtaining a reference via `window.open()`.
  - Cross-Origin-Resource-Policy (`CORP: same-origin`): Blocks cross-origin browsers from loading sensitive media, scripts, or responses into subresource tags (`<img>`, `<script>`).
  - Strict `SameSite` cookies: Preventing session cookies from being automatically attached to cross-site requests.

Limits and follow-up:

- Need additional sources for RAG vector store isolation, client-side browser privacy leakage, and bug bounty evidence reporting formats.


