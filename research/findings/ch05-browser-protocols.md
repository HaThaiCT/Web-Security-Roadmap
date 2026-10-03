# Chapter 5 — Browser, Client & Protocol Security Findings

## 2026-10-03 batch

### OWASP — Cross Site Scripting Prevention Cheat Sheet

- URL: <https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html>
- Method: WebFetch public page reading.
- Verification scope: relevant English XSS prevention sections inspected; no payloads executed.
- Promoted resource: `owasp-xss-prevention-cheat-sheet` in `data/resources/ch05-browser-protocols.yml`.

Useful observations:

- The cheat sheet emphasizes context-specific output encoding: HTML body, HTML attributes, JavaScript, CSS and URL contexts each require different handling.
- It identifies dangerous contexts where untrusted variables should not be placed, including script blocks, comments, style blocks, attribute names and tag names.
- It recommends sanitization for user-authored HTML use cases and calls out DOMPurify, with caveats that post-sanitization mutation and stale sanitizer versions can void protection.
- It distinguishes safe sinks such as `textContent`, `insertAdjacentText`, `createTextNode` and hardcoded-safe `setAttribute` from unsafe patterns such as `innerHTML` and event-handler attributes.
- It frames CSP as defense-in-depth rather than the primary XSS control and explains why context-blind interceptors/filters are a common anti-pattern.

Limits and follow-up:

- Need complementary sources for DOM XSS, Trusted Types, framework-specific auto-escaping, CSP design and browser-side data-flow testing.

### OWASP — Cross-Site Request Forgery Prevention Cheat Sheet

- URL: <https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html>
- Method: WebFetch public page reading.
- Verification scope: relevant English CSRF prevention sections inspected; no requests sent to targets.
- Promoted resource: `owasp-csrf-prevention-cheat-sheet` in `data/resources/ch05-browser-protocols.yml`.

Useful observations:

- Synchronizer tokens must be unique per user session, secret and unpredictable; they should not be sent in cookies or URLs because those channels can leak.
- The recommended stateless alternative is a session-bound HMAC signed double-submit cookie; the naive unsigned pattern is discouraged because cookie injection can defeat it.
- SameSite is treated as defense-in-depth, with caveats around top-level safe-method navigations, sibling subdomains and client-side CSRF.
- Custom headers can force CORS preflight for APIs, but CORS must be tightly restricted to trusted origins.
- Fetch Metadata, Origin/Referer validation and user-interaction defenses are covered, with caveats about missing headers, proxies and legacy clients.
- The sheet warns that XSS can defeat CSRF controls and that client-side CSRF can bypass protections when same-origin JavaScript is tricked into sending attacker-influenced requests.

Limits and follow-up:

- Need a reliable CORS source. The attempted OWASP CORS cheat-sheet URL returned 404 in this batch, so no CORS resource was promoted.
- Need additional sources for CSP/clickjacking, postMessage, service workers, HTTP request smuggling, web caching, host headers, DNS rebinding and realtime protocols.

### MDN — Cross-Origin Resource Sharing

- URL: <https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS>
- Method: WebFetch public page reading.
- Verification scope: relevant English CORS guide sections inspected; no requests sent to targets.
- Promoted resource: `mdn-cors-guide` in `data/resources/ch05-browser-protocols.yml`.

Useful observations:

- MDN explains CORS as an HTTP-header-based opt-in mechanism that lets servers declare which origins browsers may allow to read cross-origin responses.
- Simple requests and preflighted requests are differentiated by method, headers, content type and other request properties.
- Preflight uses an `OPTIONS` request with `Access-Control-Request-Method` and `Access-Control-Request-Headers`; these are not sent on the actual request.
- Credentialed cross-origin requests require explicit client-side credential inclusion and `Access-Control-Allow-Credentials: true` in the response.
- Wildcards cannot be used for credentialed requests in the same way as non-credentialed requests, and dynamically reflected origins should use `Vary: Origin` to avoid cache confusion.

Limits and follow-up:

- This source explains browser mechanics; future CORS security coverage should add misconfiguration case studies and framework-specific implementation guidance.

### OWASP — Content Security Policy Cheat Sheet

- URL: <https://cheatsheetseries.owasp.org/cheatsheets/Content_Security_Policy_Cheat_Sheet.html>
- Method: WebFetch public page reading.
- Verification scope: relevant English CSP sections inspected; no policy deployed or tested against live sites.
- Promoted resource: `owasp-content-security-policy-cheat-sheet` in `data/resources/ch05-browser-protocols.yml`.

Useful observations:

- CSP is framed as a second layer of protection for XSS, clickjacking and cross-site leaks, not as the only XSS defense.
- Strict CSP with nonce- or hash-based `script-src` plus `strict-dynamic`, `object-src 'none'` and `base-uri 'none'` is presented as the recommended approach.
- Nonces must be unique per HTTP response, and middleware must not blindly add nonces to attacker-injected scripts.
- Reporting uses `report-to` and `report-uri`, with report-only mode useful for testing before enforcement.
- Meta-delivered policies cannot use several important features, and legacy `X-Content-Security-Policy` headers are obsolete.

### PortSwigger Research — HTTP Desync Attacks: Request Smuggling Reborn

- URL: <https://portswigger.net/research/http-desync-attacks-request-smuggling-reborn>
- Method: WebFetch public page reading.
- Verification scope: relevant English research article and methodology sections inspected; no exploit payloads sent to external systems.
- Promoted resource: `portswigger-http-request-smuggling-reborn` in `data/resources/ch05-browser-protocols.yml`.

Useful observations:

- Explains desynchronization between front-end reverse proxies and back-end application servers communicating over reused persistent TCP/TLS connections.
- Details CL.TE (frontend prioritizes Content-Length, backend prioritizes Transfer-Encoding chunked) and TE.CL (frontend prioritizes Transfer-Encoding, backend Content-Length) mechanics.
- Documents obfuscation variants (e.g., `Transfer-Encoding: xchunked`, spaces, multiple headers) that cause one server to ignore `Transfer-Encoding` while the other honors it.
- Unprocessed trailing bytes of smuggled requests poison the socket pipeline, prepending arbitrary request prefixes to subsequent user requests on that connection.
- High-impact attack scenarios: bypassing front-end security controls, hijacking user credentials/cookies, web cache poisoning, and request reflection.
- Core mitigations: use HTTP/2 end-to-end between reverse proxy and backend, disable backend connection reuse, and enforce strict HTTP request normalization.

### OWASP — Web Cache Security Cheat Sheet

- URL: <https://cheatsheetseries.owasp.org/cheatsheets/Web_Cache_Security_Cheat_Sheet.html>
- Method: WebFetch / Exa agent-reach public inspection.
- Verification scope: relevant English web cache security sections inspected; no cache probes sent.
- Promoted resource: `owasp-web-cache-security-cheat-sheet` in `data/resources/ch05-browser-protocols.yml`.

Useful observations:

- Clearly distinguishes web cache poisoning (attacker injects harmful content into a shared cache entry via unkeyed inputs) from web cache deception (attacker tricks an intermediary into caching private authenticated user responses via URL/path confusion).
- Highlights that caches are high-leverage targets: poisoning a single cached response impacts all subsequent visitors.
- Establishes rules to prevent cache poisoning: only cache routes explicitly intended to be public, ensure unkeyed request headers/bodies cannot alter responses, validate `X-Forwarded-*` headers strictly from trusted proxies, and canonicalize host/scheme values.
- Establishes rules to prevent cache deception: base cacheability on allowlisted paths and strict `Cache-Control: private, no-store` directives rather than relying solely on file extensions, reject unexpected path suffixes on dynamic handlers, and verify that URL file extensions match the response `Content-Type`.

### PortSwigger Research — Practical Web Cache Poisoning

- URL: <https://portswigger.net/research/practical-web-cache-poisoning>
- Method: WebFetch / Exa agent-reach public inspection.
- Verification scope: relevant English research article and methodology sections inspected; no live targets tested.
- Promoted resource: `portswigger-practical-web-cache-poisoning` in `data/resources/ch05-browser-protocols.yml`.

Useful observations:

- Explains the anatomy of cache keys: HTTP request line (path) and `Host` header are typically keyed, while intermediary headers (`X-Forwarded-Host`, `X-Original-URL`, `X-Host`) are frequently unkeyed by default.
- When an application uses an unkeyed header to generate dynamic links, script sources, or Open Graph tags, an attacker can poison the cached page, causing every subsequent visitor to execute attacker-controlled JavaScript (DOM/stored XSS).
- Emphasizes testing methodology with safe cache busters (e.g. adding unique query parameters) to prevent polluting real visitor traffic during audits.
- Mitigations: eliminate unkeyed headers from template rendering, configure caches to strip unkeyed headers, add necessary headers to the cache key via custom rules or HTTP `Vary`, or disable caching for dynamic endpoints.

### OWASP — DOM Clobbering Prevention Cheat Sheet

- URL: <https://cheatsheetseries.owasp.org/cheatsheets/DOM_Clobbering_Prevention_Cheat_Sheet.html>
- Method: Exa search and Jina Reader inspection of public cheat sheet.
- Verification scope: relevant English DOM clobbering prevention sections inspected; no scripts executed.
- Promoted resource: `owasp-dom-clobbering-prevention-cheat-sheet` in `data/resources/ch05-browser-protocols.yml`.

Useful observations:

- Analyzes HTML-only injection attacks where attackers abuse named property access on `window` and `document` to overwrite global variables and built-in APIs.
- Occurs primarily when HTML sanitizers strip script tags but allow benign markup tags (`<a>`, `<form>`, `<input>`, `<iframe>`, `<img>`) carrying `id` or `name` attributes.
- Demonstrates common code-reuse patterns: `window.config = window.config || {}` clobbered by `<a id="config" href="javascript:alert(1)">`, or clobbering DOM properties (e.g. `form.attributes`) to bypass security filters.
- Core defenses:
  - Sanitize input using DOMPurify with `SANITIZE_NAMED_PROPS: true` (which isolates user properties with a `user-content-` prefix) or built-in `SANITIZE_DOM`.
  - Avoid global variables on `window` and `document`; use local variables and explicit declarations (`const`, `let`).
  - Use `Object.freeze()` on sensitive configuration objects.
  - Enforce type checking (e.g. `instanceof NamedNodeMap` or `typeof variable === 'string'`) before trusting properties.

### PortSwigger Web Security Academy — Controlling the Web Message Source

- URL: <https://portswigger.net/web-security/dom-based/controlling-the-web-message-source>
- Method: Exa search and Academy documentation inspection.
- Verification scope: relevant English web message documentation and lab sections inspected; no exploit messages posted.
- Promoted resource: `portswigger-controlling-the-web-message-source` in `data/resources/ch05-browser-protocols.yml`.

Useful observations:

- Explores how `window.postMessage` functions as a cross-document message channel and an untrusted tainted source for DOM execution sinks (`eval`, `innerHTML`, `location.href`).
- Details common validation vulnerabilities in `message` event listeners:
  - Missing origin checks: listener accepts messages from any origin indiscriminately.
  - Insecure substring checks: using `event.origin.indexOf('example.com') > -1`, bypassed via `attacker-example.com` or `example.com.evil.net`.
  - Insecure prefix/suffix checks: using `endsWith('example.com')`, bypassed by registering `evil-example.com`.
- Prescribes secure origin verification: strictly check `event.origin === 'https://trusted.example.com'` against an exact allowlist before parsing `event.data`. Always specify exact `targetOrigin` when sending messages instead of wildcard `"*"`.

### OWASP — WebSocket Security Cheat Sheet

- URL: <https://cheatsheetseries.owasp.org/cheatsheets/WebSocket_Security_Cheat_Sheet.html>
- Method: Exa search and Jina Reader inspection of public cheat sheet.
- Verification scope: relevant English WebSocket security guidance inspected; no sockets opened.
- Promoted resource: `owasp-websocket-security-cheat-sheet` in `data/resources/ch05-browser-protocols.yml`.

Useful observations:

- Identifies key WebSocket security differences from HTTP: persistent bidirectional sockets, absence of built-in authentication headers, and lack of automatic same-origin policy enforcement.
- Highlights Cross-Site WebSocket Hijacking (CSWSH), where browsers automatically attach session cookies to cross-origin HTTP upgrade requests.
- Explains that the `Sec-WebSocket-Key` header prevents proxy caching errors but provides zero authentication or CSRF protection.
- Identifies compression vulnerabilities (`permessage-deflate`), noting that compressing secret tokens alongside user-controlled messages creates CRIME/BREACH-style side channels.
- Mitigations: mandatory TLS (`wss://`), strict server-side allowlisting of the `Origin` header during the handshake, binding anti-CSRF tokens to the handshake, validating permissions per incoming message, and implementing backpressure and message rate-limiting.

### PortSwigger Web Security Academy — Cross-Site WebSocket Hijacking

- URL: <https://portswigger.net/web-security/websockets/cross-site-websocket-hijacking>
- Method: Exa search and Academy documentation inspection.
- Verification scope: relevant English CSWSH tutorial and methodology sections inspected; no live targets hijacked.
- Promoted resource: `portswigger-cross-site-websocket-hijacking` in `data/resources/ch05-browser-protocols.yml`.

Useful observations:

- Compares CSWSH to standard CSRF: unlike traditional CSRF where an attacker can only trigger one-way state changes without reading the HTTP response, a hijacked WebSocket provides full two-way communication.
- Attackers can both send arbitrary command messages to the server and intercept server-to-client responses containing private data (chat history, financial records, PII, CSRF tokens).
- Testing methodology: inspect WebSocket upgrade handshakes in proxy history to check if authentication relies solely on cookies without unique tokens, and test cross-origin connection establishment.
- Mitigations: validate `Origin` header strictly on the upgrade request, require unpredictable one-time tokens in the handshake query or initial message, and set `SameSite=Lax` or `Strict` on session cookies.

### NCC Group — Singularity of Origin (DNS Rebinding Framework)

- URL: <https://github.com/nccgroup/singularity>
- Method: WebFetch public repository and technical documentation reading.
- Verification scope: relevant English technical documentation, attack payloads, and defense specifications inspected; no live exploits launched.
- Promoted resource: `nccgroup-singularity-dns-rebinding` in `data/resources/ch05-browser-protocols.yml`.

Useful observations:

- Explains DNS rebinding as an attack mechanism that circumvents the Same-Origin Policy (SOP).
- Attack flow:
  1. A victim visits an attacker-controlled domain (e.g. `rebind.attacker.com`).
  2. The attacker's custom DNS server initially responds with a short TTL (0 or 1s) pointing to the attacker's public IP address.
  3. The victim's browser loads the attacker's HTML and client-side JavaScript.
  4. The DNS server rapidly alters the resolution to a private internal IP (e.g. `127.0.0.1`, `192.168.1.1`, or cloud metadata `169.254.169.254`).
  5. The browser issues subsequent HTTP/WebSocket requests to `rebind.attacker.com`, which the OS resolves to the internal target. Because the origin scheme and host remain unchanged in the browser's view, SOP permits JavaScript to read full response bodies and exfiltrate internal data.
- Payload targets: Unauthenticated internal services, Docker APIs, Rails development consoles, Jenkins instances, and local LLM servers (e.g. Ollama).
- Defenses against DNS rebinding:
  - Host Header Validation: Internal web servers must strictly validate the incoming `Host` header and reject requests matching unknown public hostnames.
  - DNS Filtering / Firewalls: Internal and upstream DNS resolvers must filter and drop responses resolving to private/loopback IP address ranges (RFC 1918 / RFC 5735).
  - Browser-Level Local Network Access (LNA): Modern browser specifications (e.g. Chrome WICG Private Network Access / Local Network Access) restricting public websites from issuing requests to private or loopback IP addresses without preflight checks.
  - Authentication on Local Services: Enforce authentication even on loopback services rather than assuming localhost is inherently trusted.

Limits and follow-up:

- Need additional sources for browser extension security models and WebRTC data channels.



