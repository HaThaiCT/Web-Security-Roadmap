# Web Foundations & Standards

This authored overview is organized by topic. Curated resource lists are generated separately in [resources.md](resources.md).

## How to use this part

Use this as a reference section, not as a mandatory linear course. Learning paths link to the topics and resources that fit each role.

<a id="http"></a>
## HTTP Requests, Responses & Versions

### Prerequisites

You should be able to read a URL, recognize common HTTP methods, and distinguish browser-side code from server-side code. No vulnerability knowledge is required yet; this topic is the baseline for later work on authentication, authorization, API security, XSS, request smuggling, caching and logging.

### Mechanism and mental model

HTTP is a client-initiated request/response protocol. A request selects a method, target path, protocol version, headers and optional body; a response returns a status line, headers and optional body. Headers make the protocol extensible and are the place where many security controls and mistakes show up: cookies, authentication challenges, content negotiation, cache directives, CORS, CSP, redirects and connection behavior.

Treat every security topic as a question about how a request is constructed, transformed, routed, interpreted and answered. Proxies, gateways, CDNs and application servers may each parse the same message differently. HTTP is stateless by itself, so applications restore continuity with cookies, bearer tokens or other state carried on each request.

### Practical learning notes

Start by reading raw requests and responses before using scanners or framework abstractions. For each example, identify the method, host, path, query string, headers, body, cookies, response status, response headers and caching behavior. Practice only against local labs, intentionally vulnerable training targets or systems you are authorized to assess.

### Defensive and engineering notes

Good engineering starts with predictable request handling: normalize inputs at the right layer, reject malformed requests consistently, document which proxy or framework owns each header, and log enough request context to investigate failures without leaking secrets. Security reviews should ask whether every component in the path agrees on host, scheme, path, body length, encoding and authenticated state.

### Reading order

1. Read [MDN — Overview of HTTP](resources.md#http) for the protocol model and message structure.
2. Move next to [Origins, Cookies & Browser Storage](resources.md#origins-cookies) for browser state, or to Chapter 2's request lifecycle when studying application architecture.

<a id="dns-tls"></a>
## DNS, TLS & PKI for the Web

### Prerequisites

Understand basic networking concepts (IP addresses, domain names, TCP 3-way handshakes), client-server HTTP request/response flows, and the role of Certificate Authorities (CAs) in public key infrastructure.

### Mechanism and mental model

Transport Layer Security (TLS) provides confidentiality, data integrity, and server authentication for web communications traversing untrusted networks. When a browser navigates to an HTTPS URL, TLS wraps the underlying TCP stream before any HTTP plaintext is exchanged.

The web PKI model and TLS handshake establish security through several discrete mechanisms:
1. **Protocol Negotiation:** The client and server agree on the TLS protocol version. In modern web architectures, **TLS 1.3** is the preferred standard, offering a streamlined 1-RTT handshake, mandatory forward secrecy, and removal of insecure legacy algorithms. **TLS 1.2** is maintained for backwards compatibility. Legacy protocols—including SSLv2, SSLv3, TLS 1.0, and TLS 1.1—have been formally deprecated per RFC 8996 due to fundamental structural vulnerabilities (POODLE, BEAST, DROWN) and must be disabled.
2. **Cipher Suite Selection:** Modern configurations restrict cipher suites to Authenticated Encryption with Associated Data (AEAD) primitives (AES-GCM, ChaCha20-Poly1305). AEAD combines encryption and message authentication in a single step, preventing padding oracle attacks (such as Lucky Thirteen) that plagued unauthenticated CBC modes.
3. **Forward Secrecy (PFS):** By using Ephemeral Diffie-Hellman key exchange (ECDHE / DHE), the ephemeral session keys are independent of the server's long-term private signing key. Even if an attacker records encrypted network traffic and compromises the server's private key years later, past sessions cannot be decrypted.
4. **Certificate Validation & Web PKI:** The server presents an X.509 certificate binding its domain name (via Subject Alternative Names / SAN) to a public key. The browser verifies the cryptographic signature chain back to a trusted root CA store. DNS Certificate Authority Authorization (CAA) resource records allow domain owners to declare which CAs are permitted to issue certificates for their hostnames, mitigating rogue CA issuance.
5. **Transport Hardening:** HTTP Strict Transport Security (HSTS) enforces HTTPS by commanding browsers to refuse all HTTP connections and disallow user certificate overrides. Preloading HSTS into browser source code prevents initial strip attacks. Additionally, disabling TLS-level compression neutralizes CRIME-style side-channel compression attacks.

### Practical learning notes

When auditing web infrastructure or inspecting transport configurations in authorized assessments:
- Analyze TLS protocol versions and cipher suite negotiation using tools like `testssl.sh`, SSL Labs, or `openssl s_client`.
- Check certificate validity: ensure the certificate is unexpired, matches the exact hostname (SAN), uses a strong signature algorithm (SHA-256 or better), and chains to an established trust anchor.
- Verify security headers: confirm `Strict-Transport-Security` is present with an adequate `max-age` (e.g. 31536000 seconds / 1 year), `includeSubDomains`, and `preload`.
- Inspect DNS CAA records using `dig CAA example.com` to verify restricted CA issuance.

### Defensive and engineering notes

1. **Enforce Modern Protocols:** Configure reverse proxies, load balancers, and web servers to support only TLS 1.3 and TLS 1.2. Explicitly disable SSLv2/v3 and TLS 1.0/1.1.
2. **Mandate AEAD & ECDHE:** Allow only AEAD cipher suites (e.g., `TLS_AES_128_GCM_SHA256`, `TLS_AES_256_GCM_SHA384`, `ECDHE-ECDSA-AES128-GCM-SHA256`, `ECDHE-RSA-AES128-GCM-SHA256`).
3. **Deploy HSTS Deliberately:** Deploy `Strict-Transport-Security: max-age=31536000; includeSubDomains; preload` on all production web services after verifying that all subdomains support HTTPS.
4. **Automate Certificate Lifecycle:** Use automated issuance protocols (ACME / Let's Encrypt) to rotate short-lived certificates (e.g. 90-day validity) and prevent unexpected expiration outages.
5. **Disable Dangerous Features:** Disable TLS session tickets if key rotation cannot be guaranteed, disable TLS-level compression, and ensure insecure renegotiation is disallowed.

### Reading order

1. Read [OWASP — Transport Layer Security Cheat Sheet](resources.md#dns-tls) for comprehensive configuration and hardening baselines.
2. Cross-reference with Chapter 7 Web Servers & Reverse Proxy Hardening and Chapter 5 Host Headers & Redirects.

<a id="origins-cookies"></a>
## Origins, Cookies & Browser Storage

### Prerequisites

Understand URLs, HTTP headers and basic browser/server roles. You should be able to distinguish a request sent by a browser from JavaScript reading a response, because many origin controls allow one but not the other.

### Mechanism and mental model

The same-origin policy groups browser content by scheme, host and port. It blocks many cross-origin reads by default, while still allowing common writes and embedding patterns such as links, redirects, forms, images, scripts and frames. This split explains why CSRF, clickjacking, CORS and cross-origin leaks can exist even when browsers enforce a same-origin policy.

Cookies follow their own attribute model. `Domain`, `Path`, `Secure`, `HttpOnly`, `SameSite`, prefixes and partitioning determine when a browser stores, sends or exposes a cookie. Do not treat `Path` as a strong security boundary, and remember that `HttpOnly` blocks JavaScript reads but not browser sending.

### Practical learning notes

Practice by comparing pairs of URLs and deciding whether they are same-origin, same-site or cross-site. Then inspect real `Set-Cookie` headers and identify the effect of each attribute. Use local or lab applications when experimenting with CORS, cookies or postMessage; browser behavior can affect real users if tested casually on production systems.

### Defensive and engineering notes

Keep authentication cookies host-scoped when possible, set `Secure` and `HttpOnly`, choose a deliberate `SameSite` mode and use `__Host-` prefixes for high-value session cookies where compatible. Treat origin checks, CORS policy, postMessage validation and cookie settings as one browser-state design, not separate headers copied into place.

### Reading order

1. Read [MDN — Same-origin policy](resources.md#origins-cookies) for the browser isolation model.
2. Read [MDN — Set-Cookie header](resources.md#origins-cookies) for cookie attributes and prefixes.
3. Continue to Session & Cookie Security, CSRF and CORS after these foundations.

<a id="encoding-parsing"></a>
## Encoding, Unicode & Text Processing Security

### Prerequisites

Understand basic character encodings (ASCII, Latin-1, UTF-8, UTF-16), byte representation of text, and how web applications transport data across heterogeneous layers (HTTP headers, URL query parameters, JSON bodies, HTML markup, database fields).

### Mechanism and mental model

Text encoding and character parsing represent a fundamental semantic mismatch layer in web applications. Security boundaries frequently assume strings are simple sequences of ASCII characters, while modern application stacks process multi-byte internationalized Unicode text.

The primary security hazards in character encoding and Unicode handling include:
1. **Visual Spoofing & Confusable Glyphs:** Unicode defines over 140,000 characters across diverse scripts (Latin, Cyrillic, Greek, Hebrew). Glyphs that appear visually indistinguishable to humans (homoglyphs, e.g., Latin 'a' `U+0061` vs. Cyrillic 'а' `U+0430`) have completely distinct code points. Attackers exploit this for Internationalized Domain Name (IDN) homograph attacks to spoof domains, impersonate usernames, or bypass identifier allowlists.
2. **Non-Shortest Form UTF-8 Sequences:** In variable-length encodings like UTF-8, characters can theoretically be encoded in multiple byte representations. In legacy decoders, an ASCII character like slash `/` (`0x2F`) could be encoded in two bytes (`0xC0 0xAF`). If an input filter checks for ASCII `0x2F` before decoding, an attacker can bypass traversal filters when a downstream parser decodes the overlong sequence. Modern RFC 3629-compliant UTF-8 decoders must strictly reject non-shortest form byte sequences as invalid.
3. **Unicode Normalization Hazards:** Unicode offers multiple forms for composite characters (e.g. `é` can be a precomposed character `U+00E9` or decomposed `e` `U+0065` followed by combining acute accent `U+0301`). Unicode defines four normalization forms: NFC, NFD, NFKC, and NFKD. The compatibility forms (NFKC/NFKD) decompose formatted variants (superscripts, ligatures, full-width characters) into plain characters (e.g., full-width `＜` `U+FF1C` normalizes to `<` `U+003C`). If input validation occurs before NFKC normalization, an attacker can submit harmless full-width characters that transform into dangerous injection syntax after passing the gatekeeper.
4. **Buffer Length Expansion:** String transformations and normalization can drastically change byte or character counts. For example, during NFKC normalization, certain ligature glyphs can expand up to 18 times their original byte length, causing buffer overflows or unbounded memory allocation in native layers.
5. **Non-Compositionality:** Normalization is non-compositional: `Normalize(A + B) != Normalize(A) + Normalize(B)`. Merging independently normalized substrings can generate unexpected composite characters or eliminate delimiter boundaries.

### Practical learning notes

When auditing applications or analyzing parsing vulnerabilities in authorized environments:
- Inspect how usernames, email addresses, and domain names are normalized and matched. Test whether Cyrillic or Greek lookalikes can collide with administrative accounts (pre-account takeover via Unicode collision).
- Evaluate character transformation ordering: identify whether lowercasing (`toLowerCase()`), casing folding, or Unicode normalization (NFC/NFKC) is performed before or after regex sanitization and WAF filtering (e.g. the Turkish dotless 'ı' or Kelvin sign `K` `U+212A` turning into 'k').
- Test URL decoding layers: verify whether double-decoding occurs between reverse proxies (decoding once) and backend application frameworks (decoding a second time).

### Defensive and engineering notes

1. **Normalize Before Validation:** Always perform character decoding and canonicalization/normalization (preferably NFC) *before* validating input against security rules or regex patterns. Never validate raw encoded input and then decode/normalize afterwards.
2. **Enforce Strict Shortest-Form UTF-8:** Ensure all parsing libraries and gateways strictly reject overlong or ill-formed UTF-8 byte sequences.
3. **Deploy Punycode & IDN Restrictions:** When displaying internationalized domain names or handling critical identifiers, enforce IDNA2008 and UTS #39 confusable detection profiles, displaying suspicious mixed-script labels in raw Punycode (`xn--...`).
4. **Avoid NFKC for Security-Critical Tokens:** Do not use compatibility normalization (NFKC/NFKD) on passwords, cryptographic tokens, or syntax-bearing payloads, as compatibility forms alter semantic character distinctions.

### Reading order

1. Read [Unicode Consortium — Unicode Security Considerations (UTR #36)](resources.md#encoding-parsing) for the canonical technical breakdown of character spoofing, normalization, and buffer expansion.
2. Cross-reference with Chapter 4 Vulnerability Classes (SQLi, XSS, Path Traversal) to see how encoding desynchronization triggers injection flaws.

<a id="applied-crypto"></a>
## Applied Cryptography for Web Developers

### Prerequisites

Understand basic mathematics of modular arithmetic and bitwise operations, symmetric vs. asymmetric cryptography, and how data serialization (JSON, binary buffers) interacts with cryptographic primitives.

### Mechanism and mental model

Applied cryptography in web applications is defined by choosing mature, high-level primitives rather than implementing custom cryptographic algorithms. Cryptographic vulnerabilities rarely arise from mathematical breaks in primitives like AES or SHA-256; they almost universally stem from misuse: inappropriate cipher modes, predictable random numbers, key reuse, unauthenticated encryption, and mixing up password hashing with encryption.

Key cryptographic concepts every web engineer must master:
1. **Authenticated Encryption (AEAD):** Confidentiality alone is insufficient. Encrypting data without authenticating it leaves ciphertext vulnerable to bit-flipping attacks, padding oracles (e.g. CBC mode vulnerabilities), and chosen-ciphertext attacks. Modern web systems require Authenticated Encryption with Associated Data (AEAD), such as AES-GCM or ChaCha20-Poly1305, which produces both ciphertext and a cryptographic authentication tag over both the secret payload and any unencrypted metadata (associated data).
2. **Cryptographically Secure Pseudorandom Number Generators (CSPRNG):** Standard language random functions (e.g., Python `random`, JavaScript `Math.random()`, PHP `rand()`) are deterministic PRNGs designed for statistical simulation, not security. Their internal states can be deduced from observed outputs, allowing attackers to predict password reset tokens, session IDs, and CSRF tokens. Security contexts mandate CSPRNGs (e.g. `crypto.getRandomValues()`, `secrets` module, `/dev/urandom`).
3. **Key Separation & Lifecycle:** Cryptographic keys must never be reused across different algorithms, environments (staging vs. production), or purposes. A key used for database column encryption must never sign JWTs or authenticate webhooks. Furthermore, systems must implement envelope encryption and planned key rotation without corrupting historical data.
4. **Encryption vs. Password Hashing:** Reversible encryption (AES) is meant for data that must be read back (e.g., credit card numbers, integration secrets). User passwords must never be encrypted with reversible ciphers. Passwords must be hashed using one-way, deliberately slow, memory-hard key derivation functions (KDFs): **Argon2id** (preferred), **scrypt**, or **bcrypt**. Fast cryptographic hash functions (MD5, SHA-1, SHA-256, SHA-512) are unsuitable for passwords because GPUs can compute billions of guesses per second.

### Practical learning notes

In code reviews and authorized application evaluations:
- Inspect token generation routines to verify they invoke CSPRNGs rather than pseudo-random math utilities.
- Audit database encryption modules: check for legacy, vulnerable modes like ECB (which leaks data patterns) or unauthenticated CBC without constant-time HMAC-SHA256 (Encrypt-then-MAC).
- Audit password handling: ensure passwords pass through an approved KDF with adequate work factors (e.g. bcrypt cost factor ≥ 12, Argon2id with memory ≥ 64MB).
- Verify constant-time comparison: when validating signatures or tokens in backend code, ensure comparison uses constant-time functions (e.g. `crypto.timingSafeEqual()` in Node.js, `hmac.compare_digest()` in Python) to prevent byte-by-byte timing side channels.

### Defensive and engineering notes

1. **Use High-Level Cryptographic Libraries:** Prefer well-audited cryptographic libraries (libsodium, Web Cryptography API, Google Tink, cryptography.io) over low-level primitive assembly.
2. **Mandate AEAD Primitives:** Standardize on AES-GCM (with 96-bit unique nonces) or ChaCha20-Poly1305 for all data-at-rest and in-transit payload encryption. Never reuse an IV/nonce with the same key.
3. **Isolate Keys in Dedicated Stores:** Never commit encryption keys or signing secrets to source code or container images. Store master keys in dedicated Key Management Services (AWS KMS, HashiCorp Vault, Azure Key Vault).
4. **Enforce Constant-Time Equality:** Always compare hashes, signatures, and tokens using constant-time algorithms.

### Reading order

1. Read [OWASP — Cryptographic Storage Cheat Sheet](resources.md#applied-crypto).
2. Read [OWASP — Password Storage Cheat Sheet](../ch03-identity/resources.md#passwords-recovery).
3. Connect with Chapter 3 JWT & Token Validation and Chapter 7 Object Storage & Secrets.

<a id="web-standards"></a>
## Web Standards & Security Reference Maps

### Prerequisites

Understand the basic roles of standard bodies (IETF, W3C, WHATWG, Unicode Consortium), the structure of Request for Comments (RFC) specifications, and how web browser engines and server implementations translate formal protocol semantics into running software.

### Mechanism and mental model

Web standards are not merely administrative documents; they are the authoritative technical specifications that define trust boundaries, protocol semantics, parsing edge cases, and architectural constraints across the entire internet. Many of the most severe web vulnerabilities (HTTP request smuggling, cache deception, parser desynchronization) arise directly from divergent interpretations or partial implementations of RFC specifications between intermediaries and origin servers.

Key architectural concepts defined in core web standards (notably RFC 9110 HTTP Semantics Section 17):
1. **Establishing Authority:** HTTP relies on authority mechanisms to bind messages to an origin. In plaintext HTTP (`http://`), authority is weakly established via DNS and subject to local network spoofing or on-path tampering. In HTTPS (`https://`), authority is cryptographically verified via TLS certificate validation. Standards mandate that user agents must not send credentials intended for one authority to an unverified target.
2. **Intermediary Ambiguity & Desynchronization:** RFC 9110 Section 17 explicitly highlights that uncoordinated intermediaries (proxies, caches, API gateways) are functionally indistinguishable from on-path attackers if they alter or misinterpret message semantics. Variations in how intermediaries parse whitespace, multi-line headers, or chunked transfer coding versus backend servers lead directly to request smuggling and routing confusion.
3. **Handling Malformed & Oversized Elements:** Standards strictly dictate that servers must respond with appropriate 4xx client errors (e.g. `400 Bad Request`, `414 URI Too Long`, `431 Request Header Fields Too Large`) rather than silently truncating or ignoring oversized headers. Silent truncation or partial parsing creates exploitable desynchronization windows between proxies and backends.
4. **Information Leakage via Protocol Metadata:** Standards document inherent privacy hazards in protocol elements: the `Referer` header exposing sensitive path tokens to third parties, URI query parameters logged in intermediary access logs, and verbose `Server` / `Via` banners aiding targeted reconnaissance.

### Practical learning notes

When auditing web protocols and reviewing architecture against standards:
- Review RFC 9110 (HTTP Semantics), RFC 9112 (HTTP/1.1), RFC 9113 (HTTP/2), and RFC 9000 (HTTP/3 / QUIC) when investigating protocol desynchronization and parser edge cases.
- Compare how different web proxies (Nginx, HAProxy, Envoy, Cloudflare) handle subtle RFC non-compliances (e.g. space before header colon, multiple `Content-Length` headers, non-standard HTTP methods).
- Test whether application servers strictly enforce header length and line limits or silently accept malformed protocol framing.

### Defensive and engineering notes

1. **Follow Strict Protocol Conformance:** Configure edge reverse proxies and application gateways to enforce strict RFC parsing. Reject any request with malformed header formatting, invalid characters in header names, or conflicting framing directives.
2. **Sanitize Protocol Metadata:** Strip or minimize identifying server headers (`Server`, `X-Powered-By`, `Via`) at the reverse proxy to limit passive fingerprinting.
3. **Control Referrer Leakage:** Set a strict global `Referrer-Policy: strict-origin-when-cross-origin` or `no-referrer` to prevent URLs containing query strings or sensitive tokens from leaking to external origins.
4. **Fail-Closed on Oversized Protocol Elements:** Enforce hard memory and length bounds on request lines and headers at edge gateways, returning early 400/414/431 status codes without forwarding malformed requests upstream.

### Reading order

1. Read [IETF — RFC 9110: HTTP Semantics — Section 17 Security Considerations](resources.md#web-standards) for the definitive protocol security foundation.
2. Connect with Chapter 5 HTTP Request Smuggling and Cache Poisoning, and Chapter 7 Web Servers & Reverse Proxy Hardening.
