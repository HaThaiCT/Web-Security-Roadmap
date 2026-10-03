<!-- GENERATED FILE: do not edit by hand. Run scripts/generate.py. -->
# Curated Resources — Browser, Client & Protocol Security

<a id="xss"></a>
## Reflected

### Core

- **[Content Security Policy Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Content_Security_Policy_Cheat_Sheet.html)** — *cheatsheet · intermediate · tester, developer · free/public*  
  A practical CSP reference that frames CSP as defense-in-depth, not a replacement for XSS prevention. It is useful for designing strict nonce/hash policies, understanding reporting and avoiding brittle allowlist policies or obsolete headers.
- **[Controlling the Web Message Source](https://portswigger.net/web-security/dom-based/controlling-the-web-message-source)** — *documentation · intermediate · learner, tester, developer · free/public*  
  A practical guide on cross-document messaging security via window.postMessage. It demonstrates how unvalidated event listeners allow attacker-controlled iframes to supply malicious data to execution sinks (eval, innerHTML, location.href), explores common origin validation flaws (indexOf, endsWith), and details robust same-origin validation techniques.
- **[Cross Site Scripting Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  A core XSS prevention reference centered on context-aware output encoding, dangerous contexts, sanitization, safe sinks and common anti-patterns. It is especially useful because it explains why a single generic filter or CSP-only approach is insufficient. Use it to connect payload behavior to rendering context and to design framework-specific safe output patterns.
- **[DOM Clobbering Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/DOM_Clobbering_Prevention_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  An authoritative reference detailing HTML-only injection attacks where attackers inject markup with id or name attributes that collide with and overshadow global JavaScript variables or built-in DOM APIs. It outlines practical sanitization controls with DOMPurify, namespace isolation, object freezing, and type-safe programming patterns.
- **[Prototype Pollution](https://portswigger.net/web-security/prototype-pollution)** — *documentation · intermediate · learner, tester, developer · free/public*  
  A comprehensive resource on JavaScript prototype pollution covering both client-side and server-side exploit mechanics. It explains how polluting Object.prototype via recursive merge or property assignment injects properties across the runtime, escalating to DOM XSS via client gadgets or remote code execution via Node.js child process child_process.fork options.
- **[Web Frontend Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Web_Frontend_Security_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  A focused security guide for modern frontend architectures, Single Page Applications (SPA), and asynchronous browser-backend communication. It establishes a zero-trust mindset for all data flowing between client and server, covers safe DOM rendering (preventing innerHTML XSS sinks), secure state management in memory vs. storage, and architectural patterns for decoupling API tokens from frontend clients via Backend-for-Frontend (BFF) layers.
- **[Web Security Academy](https://portswigger.net/web-security)** — *lab · beginner · learner, tester, developer · free/registration-required*  
  A broad, free training platform with guided material and realistic labs across major web vulnerability classes, APIs, identity flaws, protocol issues and newer areas such as LLM/AI attacks. It is useful for learners and authorized testers because practice happens in a safe and legal lab environment rather than on real targets. Some exercises require Burp Suite; the Community Edition is sufficient for many labs, but the account and tooling expectations should be checked per lab.

### Extended

- **[PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings)** — *cheatsheet · intermediate · tester, developer · free/public*  
  An extensive collection of practical web application security payloads, bypasses, and vulnerability cheat sheets across dozens of bug classes. It serves as a rapid reference for authorized penetration testers and security engineers reviewing input handling filters, demonstrating how parsers and runtime environments interpret boundary cases.

<a id="csrf"></a>
## Cross-Site Request Forgery

### Core

- **[Cross-Origin Resource Sharing (CORS)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS)** — *documentation · intermediate · learner, tester, developer · free/public*  
  A clear reference for how browsers use CORS headers to permit selected cross-origin reads. It covers simple and preflighted requests, credentialed requests, wildcard limits and preflight caching, making it a practical baseline before testing or configuring APIs consumed from browsers.
- **[Cross-Site Request Forgery Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  Practical CSRF guidance covering synchronizer tokens, signed double-submit cookies, SameSite limits, custom headers, Fetch Metadata, Origin/Referer checks and user-interaction defenses. It is valuable because it explains when each control fails, including client-side CSRF and XSS defeating CSRF mitigations. Use it after learning cookies and before reviewing state-changing endpoints.
- **[Cross-Site WebSocket Hijacking](https://portswigger.net/web-security/websockets/cross-site-websocket-hijacking)** — *documentation · intermediate · learner, tester, developer · free/public*  
  A definitive guide to Cross-Site WebSocket Hijacking (CSWSH). It explains how ambient cookie authentication during the initial HTTP upgrade handshake enables attackers on malicious origins to establish two-way WebSocket connections to read private user messages or trigger unauthorized actions on the server.
- **[OAuth2 Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/OAuth2_Cheat_Sheet.html)** — *cheatsheet · advanced · tester, developer · free/public*  
  A compact security baseline for OAuth 2.x and OIDC deployments. It prioritizes Authorization Code with PKCE, strict redirect handling, state/nonce, token binding/rotation and resource-server validation. Read it after core authentication and sessions; OAuth is a delegation protocol, not a generic login shortcut.
- **[Practical security implementation guides](https://developer.mozilla.org/en-US/docs/Web/Security/Practical_implementation_guides)** — *documentation · intermediate · developer, tester · free/public*  
  A developer-facing index of practical web security controls, especially transport security and browser-facing headers. It is valuable as a bridge between vulnerability knowledge and implementation because it prioritizes controls such as HTTPS resource loading, HTTPS redirection, HSTS, clickjacking prevention, secure cookies, CORS, CSP, Referrer-Policy and Subresource Integrity. Treat it as an implementation checklist and then read the linked deep guides for each control.
- **[Same-origin policy](https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy)** — *documentation · beginner · learner, tester, developer · free/public*  
  A core browser-security foundation explaining the scheme/host/port origin tuple, cross-origin writes, embedding and reads, and the mechanisms used to relax or communicate across origins. It is required reading before CORS, CSRF, postMessage, browser storage or cross-origin leakage topics.
- **[Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  A detailed practical guide to web session design, cookie attributes, session ID entropy, expiration, rotation, logout and logging. It is especially useful for developers implementing session-backed apps and testers reviewing fixation, persistence, transport and token-storage mistakes.
- **[Set-Cookie header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie)** — *documentation · beginner · learner, tester, developer · free/public*  
  A practical reference for cookie syntax and attributes: Secure, HttpOnly, SameSite, Domain, Path, Expires, Max-Age, prefixes and partitioned cookies. It gives the vocabulary needed before studying sessions, CSRF, browser storage and cookie hardening.
- **[Web Security Academy](https://portswigger.net/web-security)** — *lab · beginner · learner, tester, developer · free/registration-required*  
  A broad, free training platform with guided material and realistic labs across major web vulnerability classes, APIs, identity flaws, protocol issues and newer areas such as LLM/AI attacks. It is useful for learners and authorized testers because practice happens in a safe and legal lab environment rather than on real targets. Some exercises require Burp Suite; the Community Edition is sufficient for many labs, but the account and tooling expectations should be checked per lab.
- **[WebSocket Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/WebSocket_Security_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  A comprehensive guide to securing real-time bidirectional WebSocket connections. It breaks down Cross-Site WebSocket Hijacking (CSWSH), handshake authentication, origin header validation, message-level authorization, permessage-deflate compression risks, and denial-of-service protections including backpressure and rate limiting.

<a id="cors"></a>
## Cross-Origin Resource Sharing

### Core

- **[Cross-Origin Resource Sharing (CORS)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS)** — *documentation · intermediate · learner, tester, developer · free/public*  
  A clear reference for how browsers use CORS headers to permit selected cross-origin reads. It covers simple and preflighted requests, credentialed requests, wildcard limits and preflight caching, making it a practical baseline before testing or configuring APIs consumed from browsers.
- **[Cross-Site Request Forgery Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  Practical CSRF guidance covering synchronizer tokens, signed double-submit cookies, SameSite limits, custom headers, Fetch Metadata, Origin/Referer checks and user-interaction defenses. It is valuable because it explains when each control fails, including client-side CSRF and XSS defeating CSRF mitigations. Use it after learning cookies and before reviewing state-changing endpoints.
- **[Practical security implementation guides](https://developer.mozilla.org/en-US/docs/Web/Security/Practical_implementation_guides)** — *documentation · intermediate · developer, tester · free/public*  
  A developer-facing index of practical web security controls, especially transport security and browser-facing headers. It is valuable as a bridge between vulnerability knowledge and implementation because it prioritizes controls such as HTTPS resource loading, HTTPS redirection, HSTS, clickjacking prevention, secure cookies, CORS, CSP, Referrer-Policy and Subresource Integrity. Treat it as an implementation checklist and then read the linked deep guides for each control.
- **[REST Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html)** — *cheatsheet · intermediate · tester, developer · free/public*  
  A practical checklist for REST services covering HTTPS, authentication, local authorization, JWT validation, API keys, input/content-type validation, status codes, CORS, rate limiting and audit logging. It is a good bridge from general web vulnerabilities to API-specific implementation and review work.
- **[Same-origin policy](https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy)** — *documentation · beginner · learner, tester, developer · free/public*  
  A core browser-security foundation explaining the scheme/host/port origin tuple, cross-origin writes, embedding and reads, and the mechanisms used to relax or communicate across origins. It is required reading before CORS, CSRF, postMessage, browser storage or cross-origin leakage topics.

<a id="csp-clickjacking"></a>
## CSP

### Core

- **[Content Security Policy Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Content_Security_Policy_Cheat_Sheet.html)** — *cheatsheet · intermediate · tester, developer · free/public*  
  A practical CSP reference that frames CSP as defense-in-depth, not a replacement for XSS prevention. It is useful for designing strict nonce/hash policies, understanding reporting and avoiding brittle allowlist policies or obsolete headers.
- **[Cross Site Scripting Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  A core XSS prevention reference centered on context-aware output encoding, dangerous contexts, sanitization, safe sinks and common anti-patterns. It is especially useful because it explains why a single generic filter or CSP-only approach is insufficient. Use it to connect payload behavior to rendering context and to design framework-specific safe output patterns.
- **[DOM Clobbering Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/DOM_Clobbering_Prevention_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  An authoritative reference detailing HTML-only injection attacks where attackers inject markup with id or name attributes that collide with and overshadow global JavaScript variables or built-in DOM APIs. It outlines practical sanitization controls with DOMPurify, namespace isolation, object freezing, and type-safe programming patterns.
- **[HTTP Headers Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/HTTP_Headers_Cheat_Sheet.html)** — *cheatsheet · beginner · learner, tester, developer · free/public*  
  An authoritative reference for hardening web servers, reverse proxies, and edge gateways using HTTP security headers. It provides concise implementation recommendations for X-Frame-Options, X-Content-Type-Options (nosniff), Strict-Transport-Security (HSTS), Content-Security-Policy (CSP), Referrer-Policy, and Permissions-Policy, explaining how edge reverse proxies can uniformly inject baseline defenses across diverse application backends.
- **[Practical security implementation guides](https://developer.mozilla.org/en-US/docs/Web/Security/Practical_implementation_guides)** — *documentation · intermediate · developer, tester · free/public*  
  A developer-facing index of practical web security controls, especially transport security and browser-facing headers. It is valuable as a bridge between vulnerability knowledge and implementation because it prioritizes controls such as HTTPS resource loading, HTTPS redirection, HSTS, clickjacking prevention, secure cookies, CORS, CSP, Referrer-Policy and Subresource Integrity. Treat it as an implementation checklist and then read the linked deep guides for each control.

<a id="postmessage-dom"></a>
## postMessage & Client-Side Data Flows

### Core

- **[Controlling the Web Message Source](https://portswigger.net/web-security/dom-based/controlling-the-web-message-source)** — *documentation · intermediate · learner, tester, developer · free/public*  
  A practical guide on cross-document messaging security via window.postMessage. It demonstrates how unvalidated event listeners allow attacker-controlled iframes to supply malicious data to execution sinks (eval, innerHTML, location.href), explores common origin validation flaws (indexOf, endsWith), and details robust same-origin validation techniques.
- **[Cross Site Scripting Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  A core XSS prevention reference centered on context-aware output encoding, dangerous contexts, sanitization, safe sinks and common anti-patterns. It is especially useful because it explains why a single generic filter or CSP-only approach is insufficient. Use it to connect payload behavior to rendering context and to design framework-specific safe output patterns.
- **[DOM Clobbering Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/DOM_Clobbering_Prevention_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  An authoritative reference detailing HTML-only injection attacks where attackers inject markup with id or name attributes that collide with and overshadow global JavaScript variables or built-in DOM APIs. It outlines practical sanitization controls with DOMPurify, namespace isolation, object freezing, and type-safe programming patterns.
- **[Same-origin policy](https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy)** — *documentation · beginner · learner, tester, developer · free/public*  
  A core browser-security foundation explaining the scheme/host/port origin tuple, cross-origin writes, embedding and reads, and the mechanisms used to relax or communicate across origins. It is required reading before CORS, CSRF, postMessage, browser storage or cross-origin leakage topics.

<a id="extensions-workers"></a>
## Extensions

### Core

- **[Service Worker API](https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API)** — *documentation · intermediate · learner, tester, developer · free/public*  
  The definitive browser documentation for service workers and progressive web app (PWA) runtime mechanics. It details the event-driven worker lifecycle (download, install, activate), network interception via fetch event listeners, caching mechanics, and foundational security boundaries—including mandatory HTTPS execution contexts to prevent persistent adversary-in-the-middle script poisoning.

<a id="browser-internals"></a>
## Practical Browser Security Internals

### Core

- **[Chromium Site Isolation](https://www.chromium.org/Home/chromium-security/site-isolation/)** — *documentation · advanced · tester, developer · free/public*  
  An authoritative technical architectural reference on modern browser process isolation models. It explains how Chromium separates different websites into sandboxed operating system processes, outlines Out-of-Process Iframes (OOPIFs), details Cross-Origin Read Blocking (CORB) preventing delivery of sensitive cross-site HTML/JSON data to untrusted renderers, and explores mitigations against speculative execution side-channel attacks like Spectre.
- **[Service Worker API](https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API)** — *documentation · intermediate · learner, tester, developer · free/public*  
  The definitive browser documentation for service workers and progressive web app (PWA) runtime mechanics. It details the event-driven worker lifecycle (download, install, activate), network interception via fetch event listeners, caching mechanics, and foundational security boundaries—including mandatory HTTPS execution contexts to prevent persistent adversary-in-the-middle script poisoning.
- **[Singularity of Origin — DNS Rebinding Attack Framework](https://github.com/nccgroup/singularity)** — *tool · advanced · tester, developer · free/public*  
  An authoritative open-source security tool and research framework for understanding and evaluating DNS rebinding attacks. It demonstrates how rapid DNS record manipulation circumvents the Same-Origin Policy (SOP) to access internal network services and cloud metadata through a victim's browser, and documents mitigations including Host header validation, DNS filtering, and Local Network Access (LNA) standards.
- **[XS-Leaks Wiki](https://xsleaks.dev/)** — *documentation · advanced · tester, developer · free/public*  
  The definitive knowledge base on Cross-Site Leaks (XS-Leaks) and web browser side channels. It details how attackers infer sensitive user data across origins without directly violating the Same-Origin Policy, analyzing timing attacks, frame counting, error events, navigation timing, and cache probing, while outlining defense-in-depth protections including Fetch Metadata, COOP, and CORP.

<a id="http-smuggling"></a>
## HTTP Request Smuggling

### Core

- **[HTTP Desync Attacks: Request Smuggling Reborn](https://portswigger.net/research/http-desync-attacks-request-smuggling-reborn)** — *article · advanced · learner, tester, developer · free/public*  
  Foundational research on HTTP request smuggling against modern multi-tier web architectures. It explains CL.TE, TE.CL, and obfuscated Transfer-Encoding desynchronization between front-end reverse proxies and back-end servers, providing non-destructive detection probes and architectural mitigations including end-to-end HTTP/2 and request normalization.
- **[Practical Web Cache Poisoning](https://portswigger.net/research/practical-web-cache-poisoning)** — *article · advanced · tester, developer · free/public*  
  Pioneering research establishing web cache poisoning as a practical vulnerability class. It details how unkeyed HTTP headers (such as X-Forwarded-Host or custom headers) can be exploited to store malicious payloads on high-traffic endpoints, providing detection methodologies and cache key auditing principles.
- **[Web Security Academy](https://portswigger.net/web-security)** — *lab · beginner · learner, tester, developer · free/registration-required*  
  A broad, free training platform with guided material and realistic labs across major web vulnerability classes, APIs, identity flaws, protocol issues and newer areas such as LLM/AI attacks. It is useful for learners and authorized testers because practice happens in a safe and legal lab environment rather than on real targets. Some exercises require Burp Suite; the Community Edition is sufficient for many labs, but the account and tooling expectations should be checked per lab.

<a id="web-caching"></a>
## Cache Poisoning & Cache Deception

### Core

- **[HTTP Desync Attacks: Request Smuggling Reborn](https://portswigger.net/research/http-desync-attacks-request-smuggling-reborn)** — *article · advanced · learner, tester, developer · free/public*  
  Foundational research on HTTP request smuggling against modern multi-tier web architectures. It explains CL.TE, TE.CL, and obfuscated Transfer-Encoding desynchronization between front-end reverse proxies and back-end servers, providing non-destructive detection probes and architectural mitigations including end-to-end HTTP/2 and request normalization.
- **[HTTP Host Header Attacks](https://portswigger.net/web-security/host-header)** — *documentation · intermediate · learner, tester, developer · free/public*  
  A comprehensive guide to vulnerabilities resulting from implicit trust in the HTTP Host header. It explores how intermediary proxies, reverse proxies, and backend application servers desynchronize routing, detailing password reset poisoning, routing-based SSRF, web cache poisoning, and authentication bypasses, along with remediation via strict Host allowlisting.
- **[HTTP caching](https://developer.mozilla.org/en-US/docs/Web/HTTP/Caching)** — *documentation · intermediate · learner, tester, developer · free/public*  
  A foundational architectural reference detailing HTTP cache hierarchies, freshness lifecycles, validation mechanics, and directive semantics. It distinguishes private client caches from shared proxy/CDN caches, breaks down Cache-Control directives (no-store, no-cache, max-age, must-revalidate), explains conditional validation via ETag and Last-Modified, and covers cache key differentiation using the Vary header.
- **[Practical Web Cache Poisoning](https://portswigger.net/research/practical-web-cache-poisoning)** — *article · advanced · tester, developer · free/public*  
  Pioneering research establishing web cache poisoning as a practical vulnerability class. It details how unkeyed HTTP headers (such as X-Forwarded-Host or custom headers) can be exploited to store malicious payloads on high-traffic endpoints, providing detection methodologies and cache key auditing principles.
- **[Rendering on the Web](https://web.dev/articles/rendering-on-the-web)** — *article · intermediate · learner, tester, developer · free/public*  
  A practical comparison of server-side rendering, client-side rendering, static rendering, streaming and hydration trade-offs. It helps readers understand how modern rendering choices affect where code runs, where data appears, when browser JavaScript becomes authoritative and why frontend architecture matters for security review.
- **[Web Cache Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Web_Cache_Security_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  A comprehensive defensive guide on preventing sensitive response exposure, web cache poisoning, and web cache deception. It defines cache key mechanics, unkeyed input hazards, delimiter and path confusion, and specifies rigorous defenses including Cache-Control: no-store, private directives, and Content-Type validation.
- **[Web Security Academy](https://portswigger.net/web-security)** — *lab · beginner · learner, tester, developer · free/registration-required*  
  A broad, free training platform with guided material and realistic labs across major web vulnerability classes, APIs, identity flaws, protocol issues and newer areas such as LLM/AI attacks. It is useful for learners and authorized testers because practice happens in a safe and legal lab environment rather than on real targets. Some exercises require Burp Suite; the Community Edition is sufficient for many labs, but the account and tooling expectations should be checked per lab.

<a id="headers-redirects"></a>
## Host Headers

### Core

- **[HTTP Host Header Attacks](https://portswigger.net/web-security/host-header)** — *documentation · intermediate · learner, tester, developer · free/public*  
  A comprehensive guide to vulnerabilities resulting from implicit trust in the HTTP Host header. It explores how intermediary proxies, reverse proxies, and backend application servers desynchronize routing, detailing password reset poisoning, routing-based SSRF, web cache poisoning, and authentication bypasses, along with remediation via strict Host allowlisting.
- **[Practical Web Cache Poisoning](https://portswigger.net/research/practical-web-cache-poisoning)** — *article · advanced · tester, developer · free/public*  
  Pioneering research establishing web cache poisoning as a practical vulnerability class. It details how unkeyed HTTP headers (such as X-Forwarded-Host or custom headers) can be exploited to store malicious payloads on high-traffic endpoints, providing detection methodologies and cache key auditing principles.
- **[Web Cache Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Web_Cache_Security_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  A comprehensive defensive guide on preventing sensitive response exposure, web cache poisoning, and web cache deception. It defines cache key mechanics, unkeyed input hazards, delimiter and path confusion, and specifies rigorous defenses including Cache-Control: no-store, private directives, and Content-Type validation.

<a id="dns-rebinding"></a>
## DNS Rebinding

### Core

- **[Singularity of Origin — DNS Rebinding Attack Framework](https://github.com/nccgroup/singularity)** — *tool · advanced · tester, developer · free/public*  
  An authoritative open-source security tool and research framework for understanding and evaluating DNS rebinding attacks. It demonstrates how rapid DNS record manipulation circumvents the Same-Origin Policy (SOP) to access internal network services and cloud metadata through a victim's browser, and documents mitigations including Host header validation, DNS filtering, and Local Network Access (LNA) standards.

<a id="realtime-protocols"></a>
## WebSocket

### Core

- **[Cross-Site WebSocket Hijacking](https://portswigger.net/web-security/websockets/cross-site-websocket-hijacking)** — *documentation · intermediate · learner, tester, developer · free/public*  
  A definitive guide to Cross-Site WebSocket Hijacking (CSWSH). It explains how ambient cookie authentication during the initial HTTP upgrade handshake enables attackers on malicious origins to establish two-way WebSocket connections to read private user messages or trigger unauthorized actions on the server.
- **[WebSocket Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/WebSocket_Security_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  A comprehensive guide to securing real-time bidirectional WebSocket connections. It breaks down Cross-Site WebSocket Hijacking (CSWSH), handshake authentication, origin header validation, message-level authorization, permessage-deflate compression risks, and denial-of-service protections including backpressure and rate limiting.
