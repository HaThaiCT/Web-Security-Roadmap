# Chapter 1 — Web Foundations & Standards Findings

## 2026-10-03 batch

### MDN — Overview of HTTP

- URL: <https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview>
- Method: WebFetch public page reading.
- Verification scope: relevant English overview sections inspected; no code executed.
- Promoted resource: `mdn-http-overview` in `data/resources/ch01-foundations.yml`.

Useful observations:

- MDN describes HTTP as an application-layer, client-server protocol where requests are initiated by the user agent and responses come from the server. This makes it a suitable foundation before any vulnerability class that depends on request/response mechanics.
- The page breaks request messages into method, resource path, protocol version, headers and optional body, and response messages into version, status code/message, headers and optional body.
- It explicitly covers intermediaries such as proxies and notes that they can cache, filter, load balance, authenticate or log traffic, which connects Chapter 1 foundations to Chapter 2 distributed web components and Chapter 5 caching/protocol topics.
- It explains HTTP statelessness and the common use of cookies to create sessions. This is a prerequisite for later identity and authorization material.
- It distinguishes HTTP/1.0 one-connection-per-request behavior from HTTP/1.1 persistent connections and HTTP/2 multiplexing/binary framing, which helps prepare for later protocol parsing topics.

Limits and follow-up:

- This page is foundational, not a security control checklist. It should be paired with MDN security guides, browser standards and vulnerability-specific material.
- Follow-up sources still needed for DNS/TLS, origin/cookie semantics, encoding/parsing and applied cryptography.

### MDN — Same-origin policy

- URL: <https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy>
- Method: WebFetch public page reading.
- Verification scope: relevant English same-origin policy sections inspected; no code executed.
- Promoted resource: `mdn-same-origin-policy` in `data/resources/ch01-foundations.yml`.

Useful observations:

- MDN defines an origin by scheme, host and port. Path differences do not change origin, but scheme, port and host differences do.
- Cross-origin interactions are not all blocked equally: writes and embedding are often allowed, while JavaScript reads are generally blocked. This distinction is essential for understanding CSRF, CORS, clickjacking, XS-leaks and postMessage.
- The page documents limited cross-origin Window access and recommends `window.postMessage` for explicit cross-origin communication.
- `document.domain` is deprecated and has surprising behavior such as port nullification; it should not be a modern design choice.
- Storage APIs such as Web Storage and IndexedDB are per-origin, while cookies use different domain/path semantics.

Limits and follow-up:

- This is browser model documentation, not a vulnerability testing guide. Pair it with CORS, CSRF, CSP, postMessage and cookie resources.

### MDN — Set-Cookie header

- URL: <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie>
- Method: WebFetch public page reading.
- Verification scope: relevant English Set-Cookie header sections inspected; no code executed.
- Promoted resource: `mdn-set-cookie-header` in `data/resources/ch01-foundations.yml`.

Useful observations:

- The page covers cookie syntax and attributes including `Secure`, `HttpOnly`, `SameSite`, `Domain`, `Path`, `Expires` and `Max-Age`.
- `Secure` restricts sending cookies to HTTPS except localhost; `HttpOnly` prevents JavaScript access via `Document.cookie` but does not stop cookies from being sent with JavaScript-initiated requests.
- `SameSite` modes are explained as Strict, Lax and None, with `SameSite=None` requiring `Secure`.
- Cookie prefixes such as `__Secure-` and `__Host-` encode attribute requirements; `__Host-` requires Secure, HTTPS, no Domain and `Path=/`.
- Partitioned cookies and the interaction between CORS credentials and `Set-Cookie` are noted.

Limits and follow-up:

- Cookie semantics are necessary but not sufficient for secure session design. Pair with OWASP session-management and CSRF guidance.

### OWASP — Transport Layer Security Cheat Sheet

- URL: <https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Security_Cheat_Sheet.html>
- Method: WebFetch public page reading.
- Verification scope: relevant English TLS configuration and hardening sections inspected; no network probes executed.
- Promoted resource: `owasp-transport-layer-security-cheat-sheet` in `data/resources/ch01-foundations.yml`.

Useful observations:

- Establishes protocol standards: TLS 1.3 and TLS 1.2 are mandatory for modern web deployments. Legacy protocols (SSLv2, SSLv3, TLS 1.0, and TLS 1.1) are formally deprecated per RFC 8996 and must be explicitly disabled.
- Mandates Authenticated Encryption with Associated Data (AEAD) cipher suites, specifically AES-GCM and ChaCha20-Poly1305.
- Mandates Ephemeral Diffie-Hellman key exchange (ECDHE) to guarantee Forward Secrecy, ensuring past session traffic cannot be decrypted even if private server keys are compromised in the future.
- Details critical transport hardening headers: HTTP Strict Transport Security (HSTS) with long max-age (minimum 1 year / 31536000 seconds), `includeSubDomains`, and HSTS preloading registration.
- Documents DNS Certificate Authority Authorization (CAA) records to restrict which CAs are authorized to issue certificates for a domain.
- Highlights disabling TLS-level compression to neutralize CRIME-style compression oracle attacks, and disabling insecure session renegotiation.

Limits and follow-up:

- Transport security protects data in flight, not application-level vulnerabilities or endpoints. Connect with reverse proxy hardening (Chapter 7) and web standards (Chapter 1).

### OWASP — Cryptographic Storage Cheat Sheet

- URL: <https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html>
- Method: WebFetch public page reading.
- Verification scope: relevant English cryptographic storage guidance inspected; no keys generated.
- Promoted resource: `owasp-cryptographic-storage-cheat-sheet` in `data/resources/ch01-foundations.yml`.

Useful observations:

- Focuses on protecting sensitive data at rest in web application datastores.
- Requires Authenticated Encryption with Associated Data (AEAD) modes such as AES-GCM or ChaCha20-Poly1305. Unauthenticated modes like CBC and ECB are prohibited due to padding oracle and block reordering risks.
- Enforces strict key separation: cryptographic keys must never be reused across different algorithms, purposes, or distinct application contexts (e.g. encrypting data vs signing tokens).
- Mandates cryptographically secure pseudorandom number generators (CSPRNG) for all initialization vectors (IVs), nonces, and cryptographic salts.
- Details the critical architectural distinction between reversible data encryption (for data that must be recovered, like credit cards or PII) and one-way password hashing (which must use dedicated memory-hard functions such as Argon2id, scrypt, or bcrypt rather than general encryption algorithms).
- Prescribes secure key lifecycle management, including key rotation, envelope encryption, and avoiding storing encryption keys beside encrypted ciphertext.

Limits and follow-up:

- Cryptographic storage must be paired with application secrets management (Chapter 7) and password authentication flows (Chapter 3).

