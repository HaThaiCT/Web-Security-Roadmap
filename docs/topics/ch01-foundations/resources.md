<!-- GENERATED FILE: do not edit by hand. Run scripts/generate.py. -->
# Curated Resources — Web Foundations & Standards

<a id="http"></a>
## HTTP Requests

### Core

- **[Client-Server overview](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Server-side/First_steps/Client-Server_overview)** — *documentation · beginner · learner, tester, developer · free/public*  
  A beginner-friendly architecture baseline for how browsers, web servers, web applications, templates, databases and static assets interact during a request. It is useful before studying vulnerabilities because it gives learners a concrete path for tracing user input from URL or form data into application code, database queries and rendered responses.
- **[HTTP caching](https://developer.mozilla.org/en-US/docs/Web/HTTP/Caching)** — *documentation · intermediate · learner, tester, developer · free/public*  
  A foundational architectural reference detailing HTTP cache hierarchies, freshness lifecycles, validation mechanics, and directive semantics. It distinguishes private client caches from shared proxy/CDN caches, breaks down Cache-Control directives (no-store, no-cache, max-age, must-revalidate), explains conditional validation via ETag and Last-Modified, and covers cache key differentiation using the Vary header.
- **[Overview of HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview)** — *documentation · beginner · learner, tester, developer · free/public*  
  A clear baseline for understanding HTTP as an application-layer, client-initiated request/response protocol. It explains messages, methods, headers, intermediaries, statelessness, cookies, persistent connections and HTTP/2 framing, which are prerequisites for nearly every web security topic in this repository. Use it before studying browser state, authorization bugs, cache behavior or protocol parsing flaws.
- **[RFC 9110: HTTP Semantics — Section 17 Security Considerations](https://www.rfc-editor.org/rfc/rfc9110.html)** — *specification · intermediate · learner, tester, developer · free/public*  
  The definitive IETF standard defining the core semantics of the Hypertext Transfer Protocol. Section 17 provides an authoritative security breakdown of establishing authority (DNS/TLS vs. plaintext HTTP), the risks of intermediary proxies and gateways, header parsing hazards, handling oversized protocol elements, and sensitive information leakage in URIs, Referer headers, and server software identifiers.

<a id="dns-tls"></a>
## DNS

### Core

- **[Practical security implementation guides](https://developer.mozilla.org/en-US/docs/Web/Security/Practical_implementation_guides)** — *documentation · intermediate · developer, tester · free/public*  
  A developer-facing index of practical web security controls, especially transport security and browser-facing headers. It is valuable as a bridge between vulnerability knowledge and implementation because it prioritizes controls such as HTTPS resource loading, HTTPS redirection, HSTS, clickjacking prevention, secure cookies, CORS, CSP, Referrer-Policy and Subresource Integrity. Treat it as an implementation checklist and then read the linked deep guides for each control.
- **[Transport Layer Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Security_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  An authoritative reference for securing transport encryption across modern web architectures. It mandates TLS 1.3 and 1.2 with AEAD cipher suites, explains the formal deprecation of TLS 1.0 and 1.1 (RFC 8996), covers Forward Secrecy (ECDHE), and details deployment controls including HTTP Strict Transport Security (HSTS), CAA DNS records, and disabling insecure renegotiation and compression.

<a id="origins-cookies"></a>
## Origins

### Core

- **[Chromium Site Isolation](https://www.chromium.org/Home/chromium-security/site-isolation/)** — *documentation · advanced · tester, developer · free/public*  
  An authoritative technical architectural reference on modern browser process isolation models. It explains how Chromium separates different websites into sandboxed operating system processes, outlines Out-of-Process Iframes (OOPIFs), details Cross-Origin Read Blocking (CORB) preventing delivery of sensitive cross-site HTML/JSON data to untrusted renderers, and explores mitigations against speculative execution side-channel attacks like Spectre.
- **[Controlling the Web Message Source](https://portswigger.net/web-security/dom-based/controlling-the-web-message-source)** — *documentation · intermediate · learner, tester, developer · free/public*  
  A practical guide on cross-document messaging security via window.postMessage. It demonstrates how unvalidated event listeners allow attacker-controlled iframes to supply malicious data to execution sinks (eval, innerHTML, location.href), explores common origin validation flaws (indexOf, endsWith), and details robust same-origin validation techniques.
- **[Cross-Origin Resource Sharing (CORS)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS)** — *documentation · intermediate · learner, tester, developer · free/public*  
  A clear reference for how browsers use CORS headers to permit selected cross-origin reads. It covers simple and preflighted requests, credentialed requests, wildcard limits and preflight caching, making it a practical baseline before testing or configuring APIs consumed from browsers.
- **[Cross-Site Request Forgery Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  Practical CSRF guidance covering synchronizer tokens, signed double-submit cookies, SameSite limits, custom headers, Fetch Metadata, Origin/Referer checks and user-interaction defenses. It is valuable because it explains when each control fails, including client-side CSRF and XSS defeating CSRF mitigations. Use it after learning cookies and before reviewing state-changing endpoints.
- **[Cross-Site WebSocket Hijacking](https://portswigger.net/web-security/websockets/cross-site-websocket-hijacking)** — *documentation · intermediate · learner, tester, developer · free/public*  
  A definitive guide to Cross-Site WebSocket Hijacking (CSWSH). It explains how ambient cookie authentication during the initial HTTP upgrade handshake enables attackers on malicious origins to establish two-way WebSocket connections to read private user messages or trigger unauthorized actions on the server.
- **[Overview of HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview)** — *documentation · beginner · learner, tester, developer · free/public*  
  A clear baseline for understanding HTTP as an application-layer, client-initiated request/response protocol. It explains messages, methods, headers, intermediaries, statelessness, cookies, persistent connections and HTTP/2 framing, which are prerequisites for nearly every web security topic in this repository. Use it before studying browser state, authorization bugs, cache behavior or protocol parsing flaws.
- **[Same-origin policy](https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy)** — *documentation · beginner · learner, tester, developer · free/public*  
  A core browser-security foundation explaining the scheme/host/port origin tuple, cross-origin writes, embedding and reads, and the mechanisms used to relax or communicate across origins. It is required reading before CORS, CSRF, postMessage, browser storage or cross-origin leakage topics.
- **[Service Worker API](https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API)** — *documentation · intermediate · learner, tester, developer · free/public*  
  The definitive browser documentation for service workers and progressive web app (PWA) runtime mechanics. It details the event-driven worker lifecycle (download, install, activate), network interception via fetch event listeners, caching mechanics, and foundational security boundaries—including mandatory HTTPS execution contexts to prevent persistent adversary-in-the-middle script poisoning.
- **[Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  A detailed practical guide to web session design, cookie attributes, session ID entropy, expiration, rotation, logout and logging. It is especially useful for developers implementing session-backed apps and testers reviewing fixation, persistence, transport and token-storage mistakes.
- **[Set-Cookie header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie)** — *documentation · beginner · learner, tester, developer · free/public*  
  A practical reference for cookie syntax and attributes: Secure, HttpOnly, SameSite, Domain, Path, Expires, Max-Age, prefixes and partitioned cookies. It gives the vocabulary needed before studying sessions, CSRF, browser storage and cookie hardening.
- **[Singularity of Origin — DNS Rebinding Attack Framework](https://github.com/nccgroup/singularity)** — *tool · advanced · tester, developer · free/public*  
  An authoritative open-source security tool and research framework for understanding and evaluating DNS rebinding attacks. It demonstrates how rapid DNS record manipulation circumvents the Same-Origin Policy (SOP) to access internal network services and cloud metadata through a victim's browser, and documents mitigations including Host header validation, DNS filtering, and Local Network Access (LNA) standards.
- **[User Privacy Protection Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/User_Privacy_Protection_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  A comprehensive guide for safeguarding user privacy, anonymity, and confidential communications in web applications. It details mitigations against browser tracking, third-party analytics leaks, and surveillance; mandates end-to-end transport and storage encryption; and details client identity protection controls including HTTP Strict Transport Security (HSTS) and cookie partitioning.
- **[Web Storage API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Storage_API)** — *documentation · beginner · learner, tester, developer · free/public*  
  The definitive browser documentation for client-side state storage mechanisms: localStorage and sessionStorage. It details origin-partitioned storage boundaries, contrasts tab-scoped ephemeral storage with persistent storage, analyzes synchronous performance implications, and establishes security boundaries—emphasizing that Web Storage is fully accessible to JavaScript and must never store sensitive session tokens or secrets vulnerable to XSS.
- **[WebSocket Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/WebSocket_Security_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  A comprehensive guide to securing real-time bidirectional WebSocket connections. It breaks down Cross-Site WebSocket Hijacking (CSWSH), handshake authentication, origin header validation, message-level authorization, permessage-deflate compression risks, and denial-of-service protections including backpressure and rate limiting.
- **[XS-Leaks Wiki](https://xsleaks.dev/)** — *documentation · advanced · tester, developer · free/public*  
  The definitive knowledge base on Cross-Site Leaks (XS-Leaks) and web browser side channels. It details how attackers infer sensitive user data across origins without directly violating the Same-Origin Policy, analyzing timing attacks, frame counting, error events, navigation timing, and cache probing, while outlining defense-in-depth protections including Fetch Metadata, COOP, and CORP.

<a id="encoding-parsing"></a>
## Encoding

### Core

- **[Cross Site Scripting Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  A core XSS prevention reference centered on context-aware output encoding, dangerous contexts, sanitization, safe sinks and common anti-patterns. It is especially useful because it explains why a single generic filter or CSP-only approach is insufficient. Use it to connect payload behavior to rendering context and to design framework-specific safe output patterns.
- **[Secure Code Review Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Secure_Code_Review_Cheat_Sheet.html)** — *cheatsheet · intermediate · tester, developer · free/public*  
  A comprehensive guide for conducting manual and hybrid security code reviews. It contrasts comprehensive baseline code reviews with incremental diff-based pull request reviews, establishes review methodologies focusing on high-risk business logic and data flow sinks that automated SAST tools miss, and outlines practical checklists for validating authentication, authorization, and input validation code paths.
- **[Unicode Security Considerations (UTR](https://www.unicode.org/reports/tr36/tr36-15.html)** — *specification · advanced · tester, developer · free/public*  
  The canonical technical specification addressing security hazards introduced by internationalized text and character encoding in software. It details visual spoofing (confusable glyphs across scripts), non-shortest form UTF-8 decoding vulnerabilities, buffer length expansion risks during casing and normalization (e.g. NFKC), and the non-compositionality of Unicode normalization that creates bypasses in security gatekeepers.

<a id="applied-crypto"></a>
## Applied Cryptography for Web Developers

### Core

- **[Cryptographic Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  A practical guide for implementing secure data storage encryption in web backends. It establishes standards for authenticated encryption (AEAD like AES-GCM), key separation, cryptographically secure pseudorandom number generators (CSPRNG), and distinguishes reversible data encryption from memory-hard password hashing (Argon2id, scrypt, bcrypt).
- **[JSON Web Token Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/JSON_Web_Token_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  A thorough technical reference for securing JSON Web Tokens (JWT) across issuance, transmission, and validation. It addresses critical cryptographic pitfalls including alg none stripping, public-key vs HMAC key type confusion, untrusted header parameters (jwk, jku, kid, x5u), cross-JWT confusion, and token revocation strategies via status lists and deny-lists.
- **[Stripe Webhook Signatures & Security](https://stripe.com/docs/webhooks)** — *documentation · intermediate · learner, tester, developer · free/public*  
  An industry-standard implementation guide for securing incoming webhook endpoints. It details cryptographic HMAC signature verification (Stripe-Signature header) computed over the unparsed raw request payload, replay attack defense using signed timestamps and tolerance windows, constant-time comparison to prevent timing leaks, and idempotency to safely process duplicate events.
- **[WebAuthn Guide](https://webauthn.guide/)** — *documentation · intermediate · learner, tester, developer · free/public*  
  A clear, interactive technical guide to the W3C Web Authentication (WebAuthn) / FIDO2 standard. It breaks down asymmetric public-key credential creation (navigator.credentials.create) and assertion authentication (navigator.credentials.get), explaining how hardware-backed private keys and cryptographic origin-binding structurally eliminate credential theft and adversary-in-the-middle phishing.

<a id="web-standards"></a>
## Web Standards & Security Reference Maps

### Core

- **[HTTP Headers Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/HTTP_Headers_Cheat_Sheet.html)** — *cheatsheet · beginner · learner, tester, developer · free/public*  
  An authoritative reference for hardening web servers, reverse proxies, and edge gateways using HTTP security headers. It provides concise implementation recommendations for X-Frame-Options, X-Content-Type-Options (nosniff), Strict-Transport-Security (HSTS), Content-Security-Policy (CSP), Referrer-Policy, and Permissions-Policy, explaining how edge reverse proxies can uniformly inject baseline defenses across diverse application backends.
- **[RFC 9110: HTTP Semantics — Section 17 Security Considerations](https://www.rfc-editor.org/rfc/rfc9110.html)** — *specification · intermediate · learner, tester, developer · free/public*  
  The definitive IETF standard defining the core semantics of the Hypertext Transfer Protocol. Section 17 provides an authoritative security breakdown of establishing authority (DNS/TLS vs. plaintext HTTP), the risks of intermediary proxies and gateways, header parsing hazards, handling oversized protocol elements, and sensitive information leakage in URIs, Referer headers, and server software identifiers.
- **[Transport Layer Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Security_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  An authoritative reference for securing transport encryption across modern web architectures. It mandates TLS 1.3 and 1.2 with AEAD cipher suites, explains the formal deprecation of TLS 1.0 and 1.1 (RFC 8996), covers Forward Secrecy (ECDHE), and details deployment controls including HTTP Strict Transport Security (HSTS), CAA DNS records, and disabling insecure renegotiation and compression.
- **[Unicode Security Considerations (UTR](https://www.unicode.org/reports/tr36/tr36-15.html)** — *specification · advanced · tester, developer · free/public*  
  The canonical technical specification addressing security hazards introduced by internationalized text and character encoding in software. It details visual spoofing (confusable glyphs across scripts), non-shortest form UTF-8 decoding vulnerabilities, buffer length expansion risks during casing and normalization (e.g. NFKC), and the non-compositionality of Unicode normalization that creates bypasses in security gatekeepers.
- **[WebAuthn Guide](https://webauthn.guide/)** — *documentation · intermediate · learner, tester, developer · free/public*  
  A clear, interactive technical guide to the W3C Web Authentication (WebAuthn) / FIDO2 standard. It breaks down asymmetric public-key credential creation (navigator.credentials.create) and assertion authentication (navigator.credentials.get), explaining how hardware-backed private keys and cryptographic origin-binding structurally eliminate credential theft and adversary-in-the-middle phishing.
