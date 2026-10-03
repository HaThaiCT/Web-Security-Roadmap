# Browser, Client & Protocol Security

This authored overview is organized by topic. Curated resource lists are generated separately in [resources.md](resources.md).

## How to use this part

Use this as a reference section, not as a mandatory linear course. Learning paths link to the topics and resources that fit each role.

<a id="xss"></a>
## Reflected, Stored & DOM XSS

### Prerequisites

Understand HTML parsing, JavaScript execution, browser origins and how server-rendered or client-rendered applications place data into pages. You should be able to identify whether a value lands in HTML text, an attribute, a JavaScript string, CSS, a URL or a DOM sink.

### Mechanism and mental model

XSS is a context problem: untrusted data is interpreted as script-capable markup or code by the browser. Reflected XSS returns attacker-influenced input in an immediate response, stored XSS persists attacker-influenced content, and DOM XSS happens when client-side JavaScript moves attacker-controlled data into an unsafe sink. The same string can be safe in one context and dangerous in another.

The core defense is perfect injection resistance: every variable is validated and then encoded, sanitized or handled by a safe sink appropriate to its output context. CSP, cookie attributes and filters help reduce impact or catch mistakes, but they do not replace correct contextual handling.

### Practical learning notes

In labs, trace the source, transformation and sink before trying payloads. Identify the rendering context first, then reason about what encoding or sanitization would be needed. Do not test real users or real sites without written authorization; XSS can affect other users and sessions even when a single request looks harmless.

### Defensive and engineering notes

Use framework auto-escaping, safe templating patterns and DOM APIs that treat values as text. Avoid dangerous contexts for untrusted data, such as script blocks, event handler attributes, tag names, attribute names and raw HTML insertion. Sanitize only when users must author HTML, keep sanitizers patched, and avoid mutating sanitized content afterward. Add tests around output contexts and known unsafe sinks.

### Reading order

1. Read [OWASP — XSS Prevention Cheat Sheet](resources.md#xss) for context-specific rules and anti-patterns.
2. Then study DOM XSS and framework-specific escaping behavior.
3. Use lab environments for practice before reading real-world write-ups.

<a id="csrf"></a>
## Cross-Site Request Forgery

### Prerequisites

Understand cookies, browser navigation, same-site versus same-origin concepts, state-changing HTTP actions and how an application authenticates requests. You should also know whether the application is form-based, API-driven, SPA-based or mixed.

### Mechanism and mental model

CSRF abuses the browser's willingness to attach ambient credentials, usually cookies, to requests initiated from another site. If a state-changing endpoint accepts a request without verifying that it was intentionally produced by the legitimate application context, another site can cause the user's browser to send it.

Modern CSRF defense is layered. Synchronizer tokens bind a request to server-side session state. Signed double-submit cookies can support stateless designs when the signature is session-bound. SameSite cookies, custom headers, Fetch Metadata and Origin/Referer checks add useful friction, but each has caveats. XSS can defeat CSRF controls, and client-side CSRF can occur when legitimate same-origin JavaScript is tricked into sending attacker-influenced requests.

### Practical learning notes

Map all state-changing endpoints before testing. Check whether they require an unpredictable token, a trusted custom header, valid Origin/Referer or Fetch Metadata behavior, and whether GET requests mutate state. Practice in labs or owned systems only; CSRF tests can change account state, settings or data.

### Defensive and engineering notes

Use built-in framework CSRF protections when possible and verify their coverage for forms, JSON APIs and login flows. Avoid state-changing GET endpoints. Bind tokens to sessions, compare tokens safely, set appropriate SameSite and cookie prefixes, restrict CORS, and require re-authentication or one-time confirmation for high-value actions. Add regression tests for missing, reused, cross-session and cross-origin request cases.

### Reading order

1. Read [OWASP — CSRF Prevention Cheat Sheet](resources.md#csrf) for defense patterns and caveats.
2. Then read CORS and cookie documentation for the application's architecture.
3. Review XSS risks because XSS can bypass many CSRF assumptions.

<a id="cors"></a>
## Cross-Origin Resource Sharing

### Prerequisites

Understand the same-origin policy, cookies, credentials and how browser JavaScript reads responses. CORS is about browser read access; it is not a server-to-server authorization system.

### Mechanism and mental model

CORS lets a server opt in to selected cross-origin reads by returning specific HTTP headers. Simple requests go directly to the server, while non-simple methods, headers or content types trigger an `OPTIONS` preflight. Credentialed requests require explicit client-side credential inclusion and `Access-Control-Allow-Credentials: true`; wildcard origins are not valid for credentialed browser reads.

A safe CORS policy answers three questions: which origins may read this response, which methods and headers are allowed, and whether credentials are allowed. Dynamic origin reflection must be constrained to a trusted allowlist and paired with caching behavior such as `Vary: Origin`.

### Practical learning notes

When reviewing CORS, separate network reachability from browser read permission. Capture the `Origin`, preflight request and response headers. Test only authorized applications because credentialed CORS mistakes can expose user data. Do not assume a missing preflight means CORS is absent; simple requests may not preflight.

### Defensive and engineering notes

Disable CORS when cross-origin browser access is unnecessary. When it is needed, use exact trusted origins, avoid wildcard credentials, keep allowed methods/headers minimal, use `Vary: Origin` with dynamic decisions and review third-party cookie/SameSite interactions. CORS should complement authorization, never replace it.

### Reading order

1. Read [MDN — Cross-Origin Resource Sharing](resources.md#cors).
2. Revisit Same-origin policy, cookies and CSRF to understand what CORS does not protect.
3. For APIs, pair with REST/API security guidance.

<a id="csp-clickjacking"></a>
## CSP, Trusted Types & Clickjacking

### Prerequisites

Understand XSS contexts, script loading, iframes and the application's rendering model. CSP is most effective when you already know which scripts are trusted and how the app builds pages.

### Mechanism and mental model

Content Security Policy constrains what the browser is allowed to load or execute. A strong policy can reduce XSS exploitability, block legacy plugin vectors, restrict base URL injection, limit framing and produce violation reports. It does not remove the underlying bug: unsafe sinks, context mistakes and injection paths still need to be fixed.

Modern guidance favors strict nonce- or hash-based script policies with `strict-dynamic`, plus restrictive directives such as `object-src 'none'` and `base-uri 'none'`. Reporting and report-only rollout help teams deploy without breaking production blindly.

### Practical learning notes

Before writing a policy, inventory script sources, inline scripts, event handlers, third-party scripts, frames and form targets. Test in report-only mode first, but do not leave enforcement indefinitely deferred. Use labs or staging systems; changing CSP on production can break functionality or hide real issues behind exceptions.

### Defensive and engineering notes

Generate nonces per response, avoid middleware that gives attacker-injected scripts a nonce, prefer strict policies over sprawling host allowlists and keep clickjacking controls explicit through `frame-ancestors` or equivalent legacy support where needed. Pair CSP with contextual output encoding, sanitization and safe DOM sinks.

### Reading order

1. Read [OWASP — Content Security Policy Cheat Sheet](resources.md#csp-clickjacking).
2. Revisit XSS prevention to understand CSP's limits.
3. Add Trusted Types and clickjacking-specific resources in a later pass.

<a id="postmessage-dom"></a>
## postMessage & Client-Side Data Flows

### Prerequisites

Understand the Document Object Model (DOM), browser window hierarchy (`window.parent`, `window.opener`, `window.frames`), the HTML5 cross-document messaging API (`postMessage`, `onmessage`), and client-side DOM injection sinks (`eval`, `innerHTML`, `document.write`, `location.href`, `script.src`).

### Mechanism and mental model

Modern web architectures rely heavily on componentized frontends, embedded third-party widgets, and cross-document communication. Two major client-side vulnerability classes emerge at this layer:
1. **Insecure `postMessage` Communication:** `window.postMessage` was designed specifically to bypass the Same-Origin Policy, enabling cross-origin communication between windows and iframes. When an application registers a `message` event listener without strictly verifying `event.origin`, any malicious cross-origin website can frame the target and dispatch crafted messages. If the receiver passes `event.data` into dangerous sinks, attackers achieve DOM XSS, trigger unauthorized client-side actions, or exfiltrate state. Furthermore, flawed origin validations (such as `event.origin.indexOf('example.com') > -1` or regex without start/end anchors) are trivially bypassed via domains like `attacker-example.com` or `example.com.attacker.com`.
2. **DOM Clobbering:** An HTML-only injection attack where attackers inject non-script markup (such as `<a>`, `<form>`, `<input>`, `<iframe>`, or `<img>`) carrying `id` or `name` attributes. Because browsers maintain legacy named property lookups on `window` and `document`, these elements overshadow and collide with global JavaScript variables or built-in DOM APIs. For example, injecting `<a id="config" href="javascript:alert(1)">` clobbers an uninitialized global `window.config` object, while injecting `<form id="attributes">` clobbers `element.attributes`, causing client-side sanitizers to skip attribute filtering loops.

### Practical learning notes

When auditing client-side applications in authorized environments, review JavaScript event listeners for `window.addEventListener('message', ...)`. Check whether the listener validates `event.origin` and inspect the data transformation path leading to potential DOM sinks. For DOM clobbering, review HTML sanitizers to see if `id` and `name` attributes are preserved, and search application scripts for dangerous fallback patterns such as `let obj = window.obj || {}`.

### Defensive and engineering notes

1. **Strict Origin Validation:** In every `message` event listener, strictly validate `event.origin` against an exact allowlist before parsing or acting on message data:
   ```javascript
   window.addEventListener('message', (event) => {
     if (event.origin !== 'https://trusted.example.com') return;
     // Process trusted message data
   });
   ```
2. **Explicit Target Origins:** When transmitting messages via `postMessage()`, always specify the exact expected recipient origin. Never pass the wildcard target origin `"*"` for sensitive data.
3. **DOM Clobbering Sanitization:** When accepting user-authored HTML, configure sanitizers like DOMPurify with `SANITIZE_NAMED_PROPS: true`. This prefixes element IDs and names with `user-content-`, preventing collisions with the global JavaScript namespace.
4. **Defensive Coding Practices:** Avoid relying on global properties of `window` or `document`. Always use explicit local declarations (`const`, `let`). Freeze critical configuration objects with `Object.freeze()` and enforce type checking using `instanceof` before consuming DOM properties.

### Reading order

1. Read [OWASP — DOM Clobbering Prevention Cheat Sheet](resources.md#postmessage-dom) for HTML injection defense.
2. Read [PortSwigger Academy — Controlling the Web Message Source](resources.md#postmessage-dom) for postMessage source-to-sink mechanics.
3. Connect with Chapter 5 XSS and Chapter 1 Origins, Cookies & Browser Storage.

<a id="extensions-workers"></a>
## Extensions, Service Workers, PWA & WebViews

### Prerequisites

Understand the browser execution model, JavaScript event loops, Web Workers, Service Worker lifecycles, browser extension architectures (manifest v2/v3, background scripts, content scripts), and native mobile WebView containers (Android WebView, iOS WKWebView).

### Mechanism and mental model

Modern web architectures extend beyond traditional browser tabs into background execution threads, installed Progressive Web Apps (PWAs), browser extensions, and native app WebViews. These execution contexts introduce powerful capabilities along with unique security boundaries:
1. **Service Workers & PWA Security:**
   - A Service Worker is an event-driven script registered against an origin and path scope. It runs in an isolated worker thread (no direct DOM access, non-blocking asynchronous APIs only) and intercepts all network `fetch` requests initiated by in-scope pages.
   - **Persistent Man-in-the-Middle Threat:** Because a compromised Service Worker can intercept, modify, or fabricate HTTP requests and responses even when offline, browsers mandate that Service Workers run *exclusively in Secure Contexts* (HTTPS, or `localhost` for testing). If an attacker achieves XSS on an origin, registering a malicious service worker allows persistent, stealthy cross-session script execution and credential interception that survives tab reloads.
2. **Browser Extension Security:**
   - Extensions operate with elevated privileges beyond web origins. Content scripts execute in an isolated world sharing the DOM with web pages, while background service workers possess access to privileged browser APIs (`chrome.cookies`, `chrome.webRequest`, `chrome.storage`).
   - Flaws in message passing between content scripts and background scripts (`chrome.runtime.sendMessage`) allow malicious web pages to trick extensions into abusing privileged APIs, leading to account takeover or system compromise.
3. **WebViews in Mobile & Desktop Apps:**
   - Mobile and desktop applications (Electron, Capacitor, React Native) embed WebViews to render web content. Naive configurations expose native bridges (e.g. `addJavascriptInterface` in Android, `nodeIntegration: true` in Electron), turning web-based XSS into operating system command execution.

### Practical learning notes

When analyzing service workers, extensions, and WebViews in authorized assessments:
- Inspect registered service workers in browser Developer Tools (Application panel): check registration scopes, update frequencies, and cache storage contents.
- Audit browser extension manifests (Manifest V3): review permissions requested (`declarativeNetRequest`, `cookies`, `all_urls`), inspect content script injection rules, and test whether `externally_connectable` restrictions are present.
- Review WebView configurations: check whether `setAllowFileAccessFromFileURLs`, `setJavaScriptCanOpenWindowsAutomatically`, or dangerous native JavaScript bridges are enabled on untrusted web content.

### Defensive and engineering notes

1. **Enforce Strict HTTPS & Scope Bounding:** Register service workers with the most restrictive path scope necessary. Ensure service worker scripts are served with `Cache-Control: no-cache` and strict `Content-Type: application/javascript`.
2. **Harden Extension Message Passing:** In extension background scripts, validate `sender.origin` or `sender.url` on every incoming message. Never trust messages originating from untrusted web pages.
3. **Sandbox WebViews:** In mobile and Electron applications, disable node integration (`nodeIntegration: false`), enable context isolation (`contextIsolation: true`), sandbox renderers, and restrict navigation strictly to trusted, verified origins.

### Reading order

1. Read [MDN — Service Worker API](resources.md#extensions-workers) for lifecycle and network interception mechanics.
2. Connect with Chapter 1 Origins, Cookies & Storage and Chapter 5 XSS.

<a id="browser-internals"></a>
## Practical Browser Security Internals: Site Isolation & Process Sandboxing

### Prerequisites

Understand the browser Same-Origin Policy (SOP), operating system process isolation models, memory layout and sandboxing primitives, and the fundamentals of hardware speculative execution side channels (Spectre / Meltdown).

### Mechanism and mental model

Web browsers are multi-tenant operating systems executing untrusted, potentially hostile code from multiple internet origins simultaneously. Historically, browsers grouped different origins into the same OS renderer process, relying on software-level checks to enforce the Same-Origin Policy. The discovery of speculative execution side channels (Spectre) proved that software boundaries within a single address space cannot prevent malicious JavaScript from reading arbitrary memory.

Modern browser architectures (notably Chromium and Firefox Fission) enforce security at the operating system process boundary:
1. **Site Isolation & Process-per-Site:**
   - Browsers allocate distinct operating system sandboxed processes for each distinct **site** (defined as the scheme and eTLD+1, such as `https://example.com`).
   - Even within a single tab, cross-site iframes run in their own isolated renderer processes (Out-of-Process Iframes / OOPIFs). A malicious parent page cannot inspect the memory of an embedded banking iframe.
2. **Cross-Origin Read Blocking (CORB):**
   - The browser process acts as a trusted broker. When a renderer process requests cross-origin data (via `<img>` or `<script>` tags), CORB inspects the response. If the response contains sensitive data formats (HTML, JSON, XML, PDF) that the requesting renderer should not legitimately execute as script or media, the browser process strips the response body before handing it to the renderer, preventing cross-site data from ever entering the untrusted renderer's memory space.
3. **Process Sandboxing:**
   - Renderer processes run with minimal OS privileges (restricted tokens on Windows, seccomp-bpf and namespaces on Linux). They have zero direct access to the filesystem, network sockets, or devices; all I/O must be brokered through IPC channels to the browser process, which verifies origin permissions on every action.

### Practical learning notes

In security engineering and vulnerability research:
- Verify how cross-origin resources are isolated: understand how `Cross-Origin-Resource-Policy` (CORP) and `Cross-Origin-Opener-Policy` (COOP) interact with browser process allocation.
- Inspect process allocation in Chrome Task Manager: observe how cross-site iframes spawn separate processes with dedicated process IDs (PIDs).
- Review side-channel mitigations: understand how browsers degrade high-resolution timers (`performance.now()`) and require Cross-Origin Isolation (`Cross-Origin-Embedder-Policy: require-corp` and `Cross-Origin-Opener-Policy: same-origin`) before granting access to powerful features like `SharedArrayBuffer`.

### Defensive and engineering notes

1. **Deploy CORP (Cross-Origin Resource Policy):** Set `Cross-Origin-Resource-Policy: same-origin` or `same-site` on sensitive API endpoints, static assets, and user data to instruct browsers and CORB to block cross-origin speculative reads.
2. **Enable COOP (Cross-Origin Opener Policy):** Set `Cross-Origin-Opener-Policy: same-origin` to isolate your top-level browsing context into a dedicated process group, severing cross-window references (`window.opener`) from untrusted origins.
3. **Mitigate Timing Oracles:** Ensure responses for sensitive operations do not create measurable network or execution timing differences that allow cross-site search (XS-Search) or XS-Leaks.

### Reading order

1. Read [The Chromium Projects — Site Isolation](resources.md#browser-internals) for process-per-site architecture and sandboxing design.
2. Cross-reference with Chapter 8 Practical Web Side Channels and Privacy Leakage.

<a id="http-smuggling"></a>
## HTTP Request Smuggling

### Prerequisites

Understand HTTP/1.1 persistent connections (keep-alive), request framing headers (`Content-Length` and `Transfer-Encoding: chunked`), multi-tier web architectures (reverse proxies, CDNs, load balancers, and back-end application servers), and the transition to HTTP/2.

### Mechanism and mental model

HTTP request smuggling occurs when a front-end proxy and a back-end application server disagree on where one HTTP request ends and the next begins over a shared, persistent TCP or TLS connection. The HTTP/1.1 specification allows two distinct ways to define message body length: the `Content-Length` header (specifying length in bytes) and the `Transfer-Encoding: chunked` header (streaming chunks until a terminating `0\r\n\r\n` chunk).

When both headers are present or obfuscated, desynchronization arises:
- **CL.TE Desync:** The front-end proxy processes `Content-Length` and forwards the specified bytes. The back-end server prioritizes `Transfer-Encoding: chunked`, reads the chunked stream terminating early, and treats the remaining unprocessed bytes as the beginning of the next request.
- **TE.CL Desync:** The front-end proxy prioritizes `Transfer-Encoding: chunked` and forwards the entire stream. The back-end server prioritizes `Content-Length`, reads only the initial bytes, and leaves the trailing payload in the connection queue.
- **TE.TE Obfuscation:** Both servers support chunked encoding, but one server can be tricked into ignoring the header via header obfuscation (e.g., `Transfer-Encoding: xchunked`, extra whitespace, or multiple headers).

The smuggled trailing bytes prepend attacker-controlled prefixes to the subsequent legitimate user request processed on that persistent connection. Consequences include hijacking session cookies, bypassing front-end access controls, and poisoning web caches.

### Practical learning notes

Smuggling is fundamentally an architecture and protocol framing flaw. In authorized testing, never perform intrusive smuggling attacks on production infrastructure, as desynchronizing shared connections can corrupt or hijack real visitor traffic. Practice in dedicated lab environments (such as PortSwigger Web Security Academy) using non-destructive timeout probes (differentiating between front-end and back-end read delays) to confirm desynchronization safely.

### Defensive and engineering notes

The most definitive architectural mitigations include:
1. **End-to-End HTTP/2:** Use HTTP/2 or HTTP/3 from the client to the front-end proxy and through to the back-end servers. HTTP/2 uses binary framing where frame length is explicitly defined in frame headers, eliminating ambiguous delimiter parsing.
2. **Disable Connection Reuse:** Configure the front-end proxy to avoid reusing TCP/TLS connections to back-end servers for different users, or assign dedicated connection pools per origin/session.
3. **Strict Normalization:** Enforce strict HTTP/1.1 request normalization at the reverse proxy layer, completely stripping ambiguous requests that contain both `Content-Length` and `Transfer-Encoding`, or that contain malformed headers.

### Reading order

1. Read [PortSwigger Research — HTTP Desync Attacks: Request Smuggling Reborn](resources.md#http-smuggling).
2. Study HTTP/1.1 RFC 9112 message framing rules and HTTP/2 RFC 9113 binary framing.
3. Connect with Chapter 2 Web Servers & Proxies and Chapter 5 Web Caching.

<a id="web-caching"></a>
## Cache Poisoning & Cache Deception

### Prerequisites

Understand HTTP caching mechanics (RFC 9111), cache keys (typically HTTP method, scheme, host, and path), `Cache-Control` header directives (`public`, `private`, `no-store`, `max-age`), and the operational difference between browser caches and shared intermediary caches (CDNs, reverse proxies).

### Mechanism and mental model

Although both exploit caching intermediaries, web cache poisoning and web cache deception are distinct vulnerability classes:
- **Web Cache Poisoning:** An attacker manipulates unkeyed inputs (HTTP headers, query parameters, or cookies not included in the cache key, such as `X-Forwarded-Host` or `X-Host`) to cause the origin server to generate a malicious response (e.g. reflected XSS or malicious script imports). The shared cache stores this response under the legitimate cache key, serving the malicious payload to all subsequent visitors.
- **Web Cache Deception:** An attacker exploits path confusion between the cache and the origin. The attacker lures an authenticated victim to a crafting URL (e.g. `/profile/avatar.css`). The cache server sees `.css` and assumes it is a static, cacheable public asset, while the origin server's router ignores the suffix and renders the victim's private JSON profile. The cache stores the private user data under the public URL, allowing the attacker to retrieve the cached response and steal tokens or PII.

### Practical learning notes

When auditing applications, identify unkeyed headers using automated probing with cache busters (e.g. appending a random query string like `?cb=12345` on every request) to ensure tests never pollute shared cache entries for real visitors. For cache deception, test whether dynamic endpoints tolerate appended path segments (such as `/test.jpg` or `;.png`) and observe whether the response carries caching headers.

### Defensive and engineering notes

To defend against cache poisoning:
1. Ensure unkeyed request headers never influence dynamic HTML, JSON, or redirect generation at the origin.
2. Configure intermediate caches (Varnish, Cloudflare, Fastly) to strip unkeyed headers, or include required variance in the `Vary` header or custom cache keys.
3. Only cache routes that are explicitly designed to be static and public.

To defend against cache deception:
1. Always emit `Cache-Control: private, no-store` on all authenticated and dynamic responses.
2. Configure caching rules based on allowlisted routes rather than naive file extension matching.
3. Ensure origin web frameworks reject unexpected trailing path segments (return 404) rather than routing them to the base controller.
4. Verify that the file extension in the requested URL matches the `Content-Type` header of the response before caching.

### Reading order

1. Read [OWASP — Web Cache Security Cheat Sheet](resources.md#web-caching) for baseline caching principles.
2. Study [PortSwigger Research — Practical Web Cache Poisoning](resources.md#web-caching) for unkeyed header methodology.
3. Review RFC 9111 HTTP Caching specification.

<a id="headers-redirects"></a>
## Host Headers, Response Splitting & Open Redirects

### Prerequisites

Understand HTTP/1.1 mandatory headers, virtual hosting (multiple domains hosted on a single IP address), reverse proxies and load balancers, HTTP redirect status codes (301, 302, 307, 308), and CR/LF (`\r\n`) protocol delimiters.

### Mechanism and mental model

HTTP request headers and redirection directives control how web traffic is routed, dispatched, and interpreted across complex infrastructure. Exploiting ambiguities or implicit trust in these headers enables severe server-side attacks:
1. **HTTP Host Header Attacks:**
   - In modern cloud environments and multi-tenant architectures, a single web server or load balancer routes requests to multiple virtual hosts based on the client-supplied `Host` header.
   - If an application implicitly trusts the `Host` header to generate links, construct password reset URLs, or import assets, an attacker can manipulate the header:
     - *Password Reset Poisoning:* When requesting a password reset, the attacker submits `Host: attacker.com`. The application generates an email containing `https://attacker.com/reset-password?token=secret123`. When the victim clicks the link, their reset token is leaked directly to the attacker's server.
     - *Routing-Based SSRF:* In reverse proxy chains, manipulating the `Host` header (or forwarding headers like `X-Forwarded-Host`) can trick an edge proxy into routing requests to unintended internal administrative systems or internal cloud services.
     - *Web Cache Poisoning via Host Header:* Poisoning shared cache entries when the `Host` header is reflected in responses but excluded from the cache key.
2. **HTTP Response Splitting & Header Injection:**
   - Occurs when untrusted input is included in response header values (such as `Location` or `Set-Cookie`) without filtering carriage return (`\r` / `%0D`) and line feed (`\n` / `%0A`) characters. Injected CR/LF sequences terminate the header section and inject arbitrary HTTP headers or an entirely attacker-controlled response body (XSS or cache poisoning).
3. **Open Redirects:**
   - Occurs when an application accepts an unvalidated target URL in parameters (e.g. `?redirect=https://evil.com`) and redirects the user via a `3xx` status code. Attackers use open redirects in phishing campaigns (leveraging the legitimate domain's credibility) or to bypass OAuth redirect URI allowlists to steal authorization codes.

### Practical learning notes

When auditing headers and redirects in authorized assessments:
- Test Host header acceptance: inject custom hostnames, duplicate Host headers (`Host: target` and `Host: attacker`), or override headers (`X-Forwarded-Host`, `X-Host`) and observe if the value is reflected in password reset emails, canonical `<link>` tags, or absolute script imports.
- Test redirect parameters: examine whether redirect endpoints validate the destination against a strict internal path allowlist (e.g. enforcing `/dashboard` without leading slashes like `//evil.com` or backslash bypasses `/\evil.com`).
- Verify CR/LF sanitation: check whether user input passed into header creation functions can inject arbitrary response headers.

### Defensive and engineering notes

1. **Strictly Validate the Host Header:** Configure web servers (Nginx, Apache) and application frameworks to match incoming requests against a strict allowlist of authorized hostnames. Reject unrecognized host headers with `400 Bad Request`.
2. **Use Server-Side Configuration for Absolute URLs:** Never construct absolute URLs (especially in password reset, activation, or email links) by concatenating the dynamic request `Host` header. Use a statically configured base URL from environment variables (e.g. `APP_URL=https://app.example.com`).
3. **Safe Redirection Patterns:** Restrict redirects to relative paths, or validate target URLs against a strict allowlist of trusted domains. Avoid accepting arbitrary external redirect destinations.
4. **Enforce Header Encoding:** Use modern web frameworks that automatically sanitize or reject CR/LF characters in header values.

### Reading order

1. Read [PortSwigger Academy — HTTP Host Header Attacks](resources.md#headers-redirects) for attack patterns and virtual hosting mechanics.
2. Connect with Chapter 1 HTTP Requests & Responses and Chapter 3 Passwords, Authentication & Account Recovery.

<a id="dns-rebinding"></a>
## DNS Rebinding

### Prerequisites

Understand the browser Same-Origin Policy (SOP), DNS resolution lifecycles (A/AAAA records, TTL caching, resolver behavior), private/loopback IP address ranges (RFC 1918 `10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`, and `127.0.0.0/8`), and the HTTP `Host` header.

### Mechanism and mental model

DNS rebinding is an attack technique that subverts the browser's Same-Origin Policy to turn a victim's web browser into an open proxy capable of reading private intranet services, localhost servers, and cloud metadata.

The attack exploits a timing discrepancy between DNS resolution and SOP enforcement:
1. **Initial Resolution:** The victim navigates to an attacker-controlled website (e.g. `http://rebind.attacker.com`). The attacker's custom DNS nameserver resolves the domain to the attacker's public web server IP with an extremely low Time-To-Live (TTL = 0 or 1 second).
2. **Payload Delivery:** The victim's browser fetches HTML and JavaScript from the attacker's server. The script executes and begins sending periodic XMLHttpRequest / fetch requests back to `http://rebind.attacker.com`.
3. **The Rebind Swap:** When the browser or operating system's DNS cache expires, the next request triggers a new DNS lookup. The attacker's nameserver now responds with a private internal IP address—such as `127.0.0.1`, `192.168.1.1`, or AWS metadata `169.254.169.254`.
4. **SOP Bypass:** From the perspective of the browser's JavaScript sandbox, the origin has not changed: the scheme (`http`) and the hostname (`rebind.attacker.com`) remain identical. Because the browser considers this a same-origin request, the Same-Origin Policy does not block JavaScript from reading the full HTTP response body, allowing the attacker to exfiltrate internal data, dump cloud credentials, or issue administrative commands to unauthenticated internal services (such as Docker daemons, local LLM servers like Ollama, Redis, or development consoles).

### Practical learning notes

In authorized penetration testing and vulnerability research:
- Analyze whether internal development services or IoT devices running on localhost or private networks require authentication, or if they trust any incoming loopback connection implicitly.
- Check how local web services handle unexpected HTTP `Host` headers. If an internal server bound to `127.0.0.1:8080` answers requests containing `Host: rebind.attacker.com`, it is vulnerable to DNS rebinding exploitation.
- Use dedicated DNS rebinding research frameworks (such as NCC Group's *Singularity of Origin*) in controlled lab environments to evaluate browser and network resilience.

### Defensive and engineering notes

1. **Strict Host Header Validation:** All web applications—especially internal administrative tools, development servers, and microservices—must validate the HTTP `Host` header against an explicit allowlist of authorized hostnames (e.g. `localhost`, `127.0.0.1`). If the `Host` header does not match, return `400 Bad Request` or terminate the connection immediately.
2. **DNS Resolver Filtering (DNS Pinning / Anti-Rebinding):** Configure internal DNS resolvers, corporate firewalls, and home routers to reject external DNS responses that resolve to private, loopback, or link-local IP address ranges (RFC 1918, RFC 3927, and RFC 5735).
3. **Browser Local Network Access (LNA) Controls:** Modern browsers are implementing Private Network Access / Local Network Access specifications (W3C / WHATWG) that require explicit CORS preflight requests (`Access-Control-Request-Private-Network`) before allowing public web origins to issue requests to private IP addresses.
4. **Authenticate All Services:** Never assume loopback or local network traffic is inherently trusted. Require strong authentication tokens or mutual TLS even for services bound to `127.0.0.1`.
5. **Enforce HTTPS:** DNS rebinding is difficult to execute against HTTPS origins because the TLS handshake requires the server to present a valid certificate matching the rebind domain name.

### Reading order

1. Read [NCC Group — Singularity of Origin (DNS Rebinding Framework)](resources.md#dns-rebinding) for technical attack mechanics and payload analysis.
2. Cross-reference with Chapter 1 Origins, Cookies & Browser Storage and Chapter 4 SSRF & URL Processing.

<a id="realtime-protocols"></a>
## WebSocket, SSE & WebRTC Security

### Prerequisites

Understand the HTTP/1.1 Upgrade handshake mechanism (RFC 6455), persistent full-duplex TCP communication, the browser Same-Origin Policy boundary, and Cross-Site Request Forgery (CSRF) principles.

### Mechanism and mental model

WebSockets provide persistent, low-latency, bidirectional communication between browsers and servers. Because WebSockets deviate significantly from standard request-response HTTP semantics, applications often suffer from architectural security gaps:
- **Cross-Site WebSocket Hijacking (CSWSH):** The WebSocket lifecycle initiates with an HTTP GET request carrying `Upgrade: websocket` and `Connection: Upgrade`. Browsers automatically attach ambient session cookies to this handshake request. If the server does not enforce anti-CSRF protections or validate the `Origin` header during this initial handshake, a malicious third-party site visited by an authenticated user can open a cross-origin WebSocket connection to the vulnerable server. Unlike traditional one-way HTTP CSRF, CSWSH gives the attacker full two-way communication to issue commands and intercept sensitive real-time data streams (such as chat transcripts, personal profile data, and financial transactions).
- **Absence of SOP on Socket Messages:** Once established, individual WebSocket messages bypass the Same-Origin Policy and standard browser cross-origin protections. Message validation and authorization must be implemented at the application protocol layer.
- **Compression Side Channels:** Enabling `permessage-deflate` compression on sockets where secret data and attacker-controlled strings share the same compression context exposes the application to CRIME/BREACH-style information leakage.
- **Denial of Service & Backpressure:** Long-lived persistent connections tie up server file descriptors and memory. Without flow control and backpressure, fast producers can overwhelm server memory through message flooding.

### Practical learning notes

In authorized audits and labs, inspect WebSocket handshake requests in proxy history. Determine whether authentication relies exclusively on ambient cookies or if unpredictable tokens are required. Test cross-origin socket initiation by crafting an HTML page on a distinct origin that attempts to open a `new WebSocket('wss://...')` connection to the target. Verify whether the application performs authorization checks on each message or naively assumes connection establishment grants full privileges.

### Defensive and engineering notes

1. **Mandatory WSS Transport:** Always enforce `wss://` (WebSocket Secure) in production to ensure end-to-end TLS encryption and integrity.
2. **Strict Origin Validation:** On the initial HTTP upgrade handshake, validate the `Origin` header against an explicit, strict allowlist of authorized origins. Reject any handshake containing an untrusted or missing `Origin`.
3. **Handshake CSRF Tokens:** Require an unpredictable, session-bound anti-CSRF token in the handshake request (via query parameter or initial authentication message) to thwart CSWSH.
4. **Cookie Hardening:** Deploy `SameSite=Lax` or `SameSite=Strict` on session cookies to mitigate cross-site ambient credential attachment.
5. **Message-Level Authorization & Schema Validation:** Treat every inbound WebSocket message as untrusted input. Validate message schemas strictly, parse JSON securely (`JSON.parse` rather than `eval`), and verify that the user is authorized to perform the requested action.
6. **Compression & DoS Defenses:** Disable `permessage-deflate` compression if messages contain sensitive secrets. Enforce message size limits (e.g. <= 64KB), rate limits, idle connection timeouts, and server-side backpressure controls.

### Reading order

1. Read [OWASP — WebSocket Security Cheat Sheet](resources.md#realtime-protocols) for comprehensive architecture controls.
2. Read [PortSwigger Academy — Cross-Site WebSocket Hijacking](resources.md#realtime-protocols) for CSWSH attack mechanics.
3. Connect with Chapter 5 CSRF and Chapter 2 Request Lifecycle.
