# Chapter 2 — Web/Software Architecture & Engineering Findings

## 2026-10-03 batch

### MDN — Client-Server overview

- URL: <https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Server-side/First_steps/Client-Server_overview>
- Method: WebFetch public page reading.
- Verification scope: relevant English client-server overview sections inspected; no code executed.
- Promoted resource: `mdn-client-server-overview` in `data/resources/ch02-web-architecture.yml`.

Useful observations:

- The article explains request data through URL parameters, POST body data and cookies, and gives concrete HTTP method/status examples.
- It contrasts static and dynamic websites, making the web server/application/database/template split explicit for beginner readers.
- The dynamic-site walkthrough follows a browser request through web server routing, web application logic, database query, template rendering, HTML response and follow-up static asset requests.
- Django snippets are illustrative rather than framework-neutral implementation guidance, but they are useful for showing routing, view/controller code, query calls and template rendering.

Limits and follow-up:

- It is intentionally introductory and omits CDNs, reverse proxies, queues, microservices, authentication internals and deployment trust boundaries.
- Future Chapter 2 work still needs sources for proxies/CDNs, databases/storage/queues/workers, serialization/parsing/template engines, integrations, transactions and deployment basics.

### web.dev — Rendering on the Web

- URL: <https://web.dev/articles/rendering-on-the-web>
- Method: WebFetch public page reading.
- Verification scope: relevant English rendering strategy sections inspected; no code executed.
- Promoted resource: `webdev-rendering-on-the-web` in `data/resources/ch02-web-architecture.yml`.

Useful observations:

- The article compares server-side rendering, client-side rendering, static rendering, hydration/rehydration, streaming SSR, progressive or partial rehydration and trisomorphic rendering.
- It explains practical performance and architecture trade-offs around TTFB, FCP, main-thread blocking and delayed interactivity.
- It is useful for security readers because rendering choices change where data is exposed, when browser JavaScript controls state and what server/client boundaries reviewers must inspect.

Limits and follow-up:

- Framework-specific links and examples can age quickly.
- It is architecture/performance oriented, not a security control guide; security interpretation belongs in this repository's authored topic notes.

### MDN — HTTP caching

- URL: <https://developer.mozilla.org/en-US/docs/Web/HTTP/Caching>
- Method: WebFetch public page reading.
- Verification scope: relevant English HTTP caching documentation sections inspected; no network probes executed.
- Promoted resource: `mdn-http-caching` in `data/resources/ch02-web-architecture.yml`.

Useful observations:

- Distinguishes private caches (tied to a single client/browser) from shared caches (reverse proxies, CDNs, gateway caches).
- Details freshness calculation and age headers, explaining that stale responses require validation before reuse.
- Breaks down critical Cache-Control directives:
  - `no-store`: completely prohibits caches from storing the response (mandatory for sensitive data and tokens).
  - `no-cache`: allows storage but mandates conditional revalidation against the origin before reuse.
  - `private`: restricts storage to browser caches, preventing shared proxy/CDN caches from holding personalized responses.
  - `public`: explicitly permits shared caching even when Authorization headers are present.
- Explains conditional validation mechanics using ETag / `If-None-Match` and Last-Modified / `If-Modified-Since`, returning lightweight `304 Not Modified` responses.
- Explains the `Vary` header for differentiating cache entries based on client request headers (e.g. `Vary: Accept-Language`, `Vary: Accept-Encoding`).
- Documents request collapsing where shared caches merge concurrent identical requests to an origin into a single upstream fetch.

Limits and follow-up:

- HTTP caching is an architectural foundation. Connect directly with Chapter 5 Web Cache Poisoning and Cache Deception attacks, and Chapter 7 Reverse Proxy Hardening.

Gaps:

- Need inspected sources for databases/storage/queues/workers, serialization/parsing/template engines, integrations, transactions and deployment basics.

