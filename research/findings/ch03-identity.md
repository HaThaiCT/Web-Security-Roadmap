# Chapter 3 — Authentication, Authorization & Identity Security Findings

## 2026-10-03 batch

### OWASP — Authentication Cheat Sheet

- URL: <https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html>
- Method: WebFetch public page reading.
- Verification scope: relevant English cheat-sheet sections inspected; no code executed.
- Promoted resource: `owasp-authentication-cheat-sheet` in `data/resources/ch03-identity.yml`.

Useful observations:

- The cheat sheet gives implementable guidance rather than only definitions. It covers user ID design, usernames/email verification, password length, breached-password screening and avoiding periodic forced password rotation.
- It emphasizes generic login and recovery messages and consistent HTTP status behavior to reduce account enumeration risks.
- It covers automated attack protections including MFA, account lockout/backoff, CAPTCHA as defense-in-depth and the weakness of security questions as an MFA factor.
- It requires TLS for login and authenticated pages, and calls out re-authentication triggers such as password/email changes, payment detail updates, suspicious activity and new device enrollment.
- It touches OAuth/OIDC/SAML/FIDO2/passkeys at a practical control level, making it a good identity baseline while leaving protocol-specific deep dives to future sources.
- It calls for authentication failure, password failure and lockout logging, linking this identity topic to Chapter 9 logging/detection.

Limits and follow-up:

- This is a broad cheat sheet, not a full protocol specification. Separate sources are still needed for session cookie design, WebAuthn/passkeys, JWT validation, OAuth/OIDC, SAML/SCIM and multi-tenant authorization/IDOR.

### OWASP — Authorization Cheat Sheet

- URL: <https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html>
- Method: WebFetch public page reading.
- Verification scope: relevant English authorization guidance inspected; no code executed.
- Promoted resource: `owasp-authorization-cheat-sheet` in `data/resources/ch03-identity.yml`.

Useful observations:

- The cheat sheet emphasizes deny-by-default and least privilege, including both horizontal and vertical permissions.
- It states that permissions must be validated on every request and recommends global enforcement mechanisms such as framework middleware/filters instead of scattered per-method checks.
- It highlights ABAC and ReBAC for expressing subject/object/environment relationships, which is especially relevant for multi-tenant products and object-level authorization.
- It recommends centralized handling of failed access-control checks and consistent logging so access-control failures can be investigated.
- This source belongs in Chapter 3 as the main authorization design baseline, with Chapter 9 cross-links for security requirements/testing/logging.

Limits and follow-up:

- Need additional case studies and framework-specific examples for complex multi-tenant authorization and delegated access.

### OWASP — Insecure Direct Object Reference Prevention Cheat Sheet

- URL: <https://cheatsheetseries.owasp.org/cheatsheets/Insecure_Direct_Object_Reference_Prevention_Cheat_Sheet.html>
- Method: WebFetch public page reading.
- Verification scope: relevant English IDOR prevention sections inspected; no code executed.
- Promoted resource: `owasp-idor-prevention-cheat-sheet` in `data/resources/ch03-identity.yml`.

Useful observations:

- The cheat sheet defines IDOR through an object, a reference and a missing object-level authorization check. It explicitly includes references beyond numeric IDs, such as filenames, tokens and account numbers.
- It requires server-side authorization on every request and warns that hidden form fields are attacker-controllable.
- It states that complex identifiers such as GUIDs reduce guessability but do not replace access-control checks; encrypting identifiers is discouraged as difficult to do securely.
- Framework examples include Rails scoped lookup through the current user's projects and Spring Boot owner-scoped repository methods, post-fetch ownership checks and `@PreAuthorize` service checks.
- Verification guidance includes using multiple accounts and privilege levels, manipulating references and confirming denial across read, create, update, delete, export and administrative operations.

Limits and follow-up:

- Need additional sources for BOLA in API contexts, tenant isolation, delegated access and authorization policy engines.

### OWASP — Session Management Cheat Sheet

- URL: <https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html>
- Method: WebFetch public page reading.
- Verification scope: relevant English session-management sections inspected; no code executed.
- Promoted resource: `owasp-session-management-cheat-sheet` in `data/resources/ch03-identity.yml`.

Useful observations:

- Session identifiers should be meaningless, generated from a CSPRNG and have sufficient entropy; the page calls out at least 64 bits of entropy.
- Secure cookie attributes are central: `Secure`, `HttpOnly`, `SameSite` and the `__Host-` prefix all reduce different classes of exposure.
- HTTPS is required for the whole session, not only login. HSTS is recommended, and sessions should not move between HTTP and HTTPS.
- The sheet defines idle, absolute and renewal timeouts, and requires regeneration on privilege changes such as login, role switch or password change.
- Logout must invalidate server-side state, and `Cache-Control: no-store` is preferred for sensitive responses.
- Logging should cover session creation, renewal and destruction, but raw session IDs must not be logged.
- Web Storage is explicitly unsuitable for session IDs or authentication tokens because a single XSS can expose all tokens.

Limits and follow-up:

- This source covers classic session management; separate sources are still needed for JWT-specific architecture and BFF/token storage trade-offs.

### OWASP — OAuth2 Cheat Sheet

- URL: <https://cheatsheetseries.owasp.org/cheatsheets/OAuth2_Cheat_Sheet.html>
- Method: WebFetch public page reading.
- Verification scope: relevant English OAuth2 guidance inspected; no code executed.
- Promoted resource: `owasp-oauth2-cheat-sheet` in `data/resources/ch03-identity.yml`.

Useful observations:

- The sheet recommends Authorization Code with PKCE for all client types and treats implicit grant as deprecated.
- PKCE downgrade prevention matters: a token request with `code_verifier` must be rejected if the original authorization request did not include a `code_challenge`.
- Redirect URI validation is central; clients and authorization servers should not forward users to arbitrary query-parameter-derived URLs.
- `state`, OIDC `nonce` and PKCE are discussed as CSRF/mix-up defenses depending on the flow.
- Resource servers must validate token audience and scopes/actions on every request.
- Sender-constrained tokens, mTLS, DPoP and refresh-token rotation are discussed as ways to reduce the impact of token theft.

Limits and follow-up:

- This is an OAuth/OIDC control baseline. Future work should add primary specifications and practical write-ups for common OAuth implementation failures.

### OWASP — JSON Web Token Cheat Sheet

- URL: <https://cheatsheetseries.owasp.org/cheatsheets/JSON_Web_Token_Cheat_Sheet.html>
- Method: Exa search and Jina Reader inspection of public cheat sheet.
- Verification scope: relevant English JWT cheat-sheet sections inspected; no exploit tokens generated.
- Promoted resource: `owasp-json-web-token-cheat-sheet` in `data/resources/ch03-identity.yml`.

Useful observations:

- Deconstructs JWT structure into Protected Header, Claims, and Signature/MAC.
- Identifies critical cryptographic pitfalls:
  - `alg: "none"` unsecured JWT acceptance where consumers fail to enforce mandatory signature verification.
  - Key type confusion (algorithm confusion): verifying HMAC-SHA256 (`HS256`) signatures using an asymmetric public key (intended for `RS256`) as the shared symmetric secret, allowing attackers holding the public certificate to forge arbitrary valid tokens.
  - Trusting unverified header parameters: attacker-controlled `jwk` (embedded key), `jku` (remote key set URL), `x5u` (certificate URL), and `kid` (Key ID injection, such as SQLi or directory traversal into static files).
- Addresses token revocation reality: JWTs are self-contained; revoking active tokens requires explicit architectural mechanisms such as Token Status Lists, short lifetimes with refresh tokens, or server-side denylists keyed by `jti` + `aud`.
- Highlights cross-JWT and token type confusion, recommending explicit `typ` header checking (e.g. `at+jwt` for access tokens) to prevent using an ID token or refresh token at an API resource server.

Limits and follow-up:

- Implementations frequently fail when parsing libraries auto-detect algorithms based on header values. Paired with Chapter 6 API Security.

### PortSwigger Research — The Fragile Lock: Novel Bypasses For SAML Authentication

- URL: <https://portswigger.net/research/the-fragile-lock>
- Method: Exa search and technical analysis of December 2025 research publication.
- Verification scope: relevant English SAML research paper and methodology inspected; no authentication bypasses executed.
- Promoted resource: `portswigger-saml-authentication-bypasses` in `data/resources/ch03-identity.yml`.

Useful observations:

- Demonstrates critical vulnerabilities in SAML 2.0 implementations arising from architectural dependencies on legacy XMLDSig and parser desynchronization.
- Analyzes dual-parser validation failures (e.g., in `ruby-saml` and `php-saml`) where signature verification is performed using one parser (Nokogiri / libxml2) and assertion extraction is performed using another (REXML).
- Details Attribute Pollution and Namespace Confusion: XPath lookups such as `//ds:Signature` or `node.attribute('ID')` ignore attribute namespaces or resolve colliding attributes differently across parsers, allowing an attacker to sign an innocuous assertion while causing the application to process a forged assertion.
- Introduces **Void Canonicalization**: libxml2 throws an error when encountering unresolved relative URIs in namespace declarations (`xmlns:ns="1"`). Instead of aborting, Nokogiri returns an empty string, calculating the `DigestValue` over an empty input. This generates a static, predictable SHA-256 hash (`47DEQpj8HBSa+/TImW+5JCeuQeRkm5NMpJWZG3hSuFU=`), allowing an attacker to construct a universal "Golden SAML Response" that passes signature validation regardless of modified claims.
- Explains that public IdP metadata (e.g., Microsoft Entra ID, Okta WS-Federation) provides valid signed XML blocks that can be harvested and repurposed.

Limits and follow-up:

- Requires deep understanding of XMLDSig canonicalization transforms (C14N) and XPath parsing semantics.

### OWASP — SAML Security Cheat Sheet

- URL: <https://cheatsheetseries.owasp.org/cheatsheets/SAML_Security_Cheat_Sheet.html>
- Method: Exa search and Jina Reader inspection of public cheat sheet.
- Verification scope: relevant English SAML security guidance inspected; no assertions validated.
- Promoted resource: `owasp-saml-security-cheat-sheet` in `data/resources/ch03-identity.yml`.

Useful observations:

- Defines security baseline for the Web Browser SAML/SSO Profile with Redirect/POST bindings.
- Establishes signature validation requirements: Service Providers must verify digital signatures over the `<saml:Assertion>` element directly, not solely the outer `<samlp:Response>`.
- Prescribes strict protocol rules:
  - Validate `InResponseTo` matching the original AuthnRequest ID to prevent unsolicited assertion injection.
  - Verify `Recipient` attribute in `<SubjectConfirmationData>` strictly matches the SP's Assertion Consumer Service (ACS) URL.
  - Enforce `AudienceRestriction` matching the SP's EntityID to prevent cross-service assertion replay.
  - Reject expired assertions via strict `NotBefore` and `NotOnOrAfter` checks with minimal clock-skew tolerance.
- Outlines XML parser hardening against XXE and Signature Wrapping (XSW) attacks.

### OWASP — Multifactor Authentication Cheat Sheet

- URL: <https://cheatsheetseries.owasp.org/cheatsheets/Multifactor_Authentication_Cheat_Sheet.html>
- Method: WebFetch public page reading.
- Verification scope: relevant English MFA cheat sheet sections inspected; no authentication flows executed.
- Promoted resource: `owasp-multifactor-authentication-cheat-sheet` in `data/resources/ch03-identity.yml`.

Useful observations:

- Structures authentication factors into five categories: Something You Know (passwords, PINs), Something You Have (tokens, passkeys, SMS), Something You Are (biometrics), Somewhere You Are (geolocation), and Something You Do (behavioral).
- Stresses that requiring two instances of the same factor type (e.g. two passwords) is not MFA.
- Analyzes factor security hierarchies:
  - Strongest: FIDO2/WebAuthn (passkeys) and hardware U2F tokens, which provide cryptographic origin-binding to eliminate phishing and adversary-in-the-middle attacks.
  - Restricted/Weakest: SMS and phone voice calls, designated "restricted" per NIST SP 800-63B due to SIM-swap, SS7 interception, and social engineering vulnerabilities.
  - Deprecated: Knowledge-based security questions, no longer accepted under NIST SP 800-63 guidelines.
- Identifies emerging attack vectors:
  - MFA Fatigue (Push Bombing): Spurring automated repetitive push prompts to induce accidental user approval; mitigated by number-matching and rate limits.
  - Reverse-Proxy Phishing: Reverse proxies (like Evilginx) capturing session cookies in real time; mitigated by phishing-resistant WebAuthn origin-binding.
  - Session hijacking after MFA: Emphasizes that factor reset and modification must require re-authentication with an existing enrolled factor and send out-of-band alerts.

Limits and follow-up:

- MFA protects the initial authentication event; it must be paired with session token protection (Chapter 3) to prevent post-authentication token theft.

### Duo Security — WebAuthn Guide

- URL: <https://webauthn.guide/>
- Method: WebFetch public page reading.
- Verification scope: relevant English WebAuthn architecture and flow sections inspected; no credentials created.
- Promoted resource: `webauthn-guide` in `data/resources/ch03-identity.yml`.

Useful observations:

- Details the technical mechanics of the W3C Web Authentication standard (WebAuthn / FIDO2).
- Replaces shared-secret passwords with asymmetric public key cryptography: the private key remains secure inside the client authenticator (TPM, Secure Enclave, YubiKey) and never reaches the server or network.
- Registration flow:
  1. Server issues a cryptographic challenge and relying party ID (`rp`).
  2. Browser invokes `navigator.credentials.create()`.
  3. Authenticator generates a keypair and returns an `attestationObject` (containing the public key) and `clientDataJSON` (binding challenge and origin).
  4. Server validates data and stores the public key.
- Authentication flow:
  1. Server issues challenge.
  2. Browser calls `navigator.credentials.get()`.
  3. Authenticator signs the challenge and client data, producing an assertion verified with the stored public key.
- Phishing resistance: The browser natively enforces that credentials are bound to the specific relying party origin (domain). If a user is on an impersonation domain (e.g. `phish-bank.com`), the browser will not provide the credential registered for `bank.com`, structurally defeating phishing.

Limits and follow-up:

- WebAuthn requires browser and hardware support; implementations often maintain fallback flows (like email or TOTP) whose security posture must be equally scrutinized.


