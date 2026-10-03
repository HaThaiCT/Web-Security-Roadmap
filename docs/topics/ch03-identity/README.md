# Authentication, Authorization & Identity Security

This authored overview is organized by topic. Curated resource lists are generated separately in [resources.md](resources.md).

## How to use this part

Use this as a reference section, not as a mandatory linear course. Learning paths link to the topics and resources that fit each role.

<a id="passwords-recovery"></a>
## Passwords, Authentication & Account Recovery

### Prerequisites

Understand HTTP requests, TLS, cookies and the difference between authentication and authorization. For implementation work, also know where login, registration, recovery and profile-change flows live in the application.

### Mechanism and mental model

Authentication is a set of flows for proving control of an identity and then binding that proof to subsequent requests. Password systems fail not only through weak hashes or weak passwords, but also through enumeration, unsafe recovery, inconsistent error handling, missing re-authentication, unmonitored brute-force attempts and weak handling of sensitive account changes.

A secure authentication design treats enrollment, login, recovery, MFA enrollment, email change and password change as one system. Each flow must avoid leaking whether an account exists, must use TLS, must rotate or invalidate state after sensitive changes, and must produce logs that defenders can use without exposing credentials or secrets.

### Practical learning notes

When reviewing or testing in an authorized environment, map every authentication-related endpoint and compare behavior across valid user, invalid user, locked account, wrong password and recovery states. Keep tests minimal and bounded; do not perform credential stuffing or large-scale guessing. Use labs or owned systems to learn the mechanics of enumeration and lockout bypasses.

### Defensive and engineering notes

Prefer current, standard password hashing libraries and native constant-time comparison helpers where applicable. Enforce sensible password length, screen against breached passwords, avoid brittle composition rules, add MFA/passkeys where feasible, use generic error messages, rate-limit or back off risky flows, and log failures, lockouts and sensitive account changes. Recovery and email-change flows deserve the same security review as login.

### Reading order

1. Read the [OWASP Authentication Cheat Sheet](resources.md#passwords-recovery) for a practical control baseline.
2. Then branch to Session & Cookie Security, MFA/Passkeys, OAuth/OIDC or SAML/SCIM depending on the application model.

<a id="sessions"></a>
## Session & Cookie Security

### Prerequisites

Understand HTTP statelessness, TLS, browser cookies and the difference between authentication and authorization. You should also know where the application creates, stores, rotates and invalidates authenticated state.

### Mechanism and mental model

A session binds an earlier authentication event to later requests. The session identifier becomes a bearer secret: whoever can present it may be treated as the user until the server rejects it. Secure session design therefore protects creation, transport, storage, renewal, privilege changes, expiration, logout and logging.

Cookie attributes reduce exposure but do not replace server-side session controls. `Secure` protects transport, `HttpOnly` limits JavaScript theft, `SameSite` helps with CSRF, and `__Host-` reduces subdomain overwrite risk. Server-side invalidation, rotation after privilege changes and bounded lifetimes are still required.

### Practical learning notes

In labs or authorized reviews, inspect when the session ID changes: before login, after login, after MFA, after role changes, after password changes and after logout. Check whether cookies are persistent, whether authenticated pages use HTTPS only, whether sensitive responses are cached and whether logs expose raw tokens. Do not attempt session hijacking against real users.

### Defensive and engineering notes

Use framework session management where possible, but harden defaults. Generate high-entropy meaningless IDs, regenerate on privilege changes, use idle/absolute/renewal timeouts, invalidate on logout server-side, avoid localStorage/sessionStorage for auth tokens and log session lifecycle events without raw identifiers. Treat session stores and admin session-management panels as high-value assets.

### Reading order

1. Read [OWASP — Session Management Cheat Sheet](resources.md#sessions).
2. Pair it with [MDN — Set-Cookie header](../ch01-foundations/resources.md#origins-cookies) for exact cookie semantics.
3. Continue to CSRF and OAuth/OIDC depending on the application model.

<a id="mfa-passkeys"></a>
## MFA, Passkeys & WebAuthn

### Prerequisites

Understand primary authentication mechanisms (passwords, sessions, cookies), cryptographic keypairs (public/private keys, digital signatures), and the browser Same-Origin Policy.

### Mechanism and mental model

Multifactor Authentication (MFA) requires a claimant to present two or more independent authentication factors from distinct categories before access is granted:
- *Something You Know:* Passwords, PINs, secret passphrases.
- *Something You Have:* Hardware security keys, authenticator app TOTP tokens, cryptographic passkeys.
- *Something You Are:* Biometrics (fingerprint, facial recognition, iris scan).
- *Somewhere You Are / Something You Do:* Geolocation fencing, behavioral dynamics.

Crucially, presenting two instances of the same factor category (e.g. entering two passwords) does not constitute MFA.

While MFA blocks over 99% of bulk credential stuffing attacks, not all MFA mechanisms provide equal security assurance:
1. **Phishable vs. Phishing-Resistant MFA:**
   - *Phishable Factors (SMS, Voice, TOTP, Mobile Push):* Legacy factors transmit shared secrets or simple codes that an attacker can intercept in real time using Adversary-in-the-Middle (AiTM) reverse proxy frameworks (such as Evilginx). The attacker presents a legitimate-looking phishing site, proxies the user's OTP to the real service, and captures the resulting authenticated session cookie. Push notifications are also vulnerable to **MFA Fatigue (Push Bombing)**, where attackers flood users with repeated approvals until one is accepted.
   - *Phishing-Resistant Factors (FIDO2 / WebAuthn / Passkeys):* Built on public key cryptography natively implemented in the browser. When a user authenticates with a passkey, the device signs a challenge using its private key (stored securely in a TPM or Secure Enclave). The browser automatically injects the verified relying party origin into the signed data (`clientDataJSON`). If the user is tricked onto a phishing domain, the browser will not sign or provide credentials for the authentic service origin, structurally neutralizing AiTM attacks.
2. **WebAuthn Protocol Flow:**
   - *Registration:* The server sends a challenge and relying party ID (`rp`). The browser executes `navigator.credentials.create()`. The authenticator creates an asymmetric keypair and returns an `attestationObject` (containing the public key) and `clientDataJSON`. The server verifies and stores the public key.
   - *Authentication:* The server issues a challenge. The browser executes `navigator.credentials.get()`. The authenticator signs the challenge and client data, returning an assertion signature verified server-side with the stored public key.
3. **MFA Lifecycle Security:** Resetting, recovering, or modifying enrolled MFA factors represents the highest-risk surface in an identity system. Account takeover often targets factor recovery flows rather than primary credentials.

### Practical learning notes

In authorized audits and security reviews:
- Examine the factor enrollment and recovery process: Does resetting MFA require out-of-band identity verification or pre-generated single-use recovery codes, or can it be reset via an unverified email link?
- Test for MFA bypasses: Can authenticated API endpoints be called directly before completing the MFA step? Can an attacker manipulate session state or drop the MFA challenge cookie?
- Assess push notification implementations for MFA fatigue defenses: Is number-matching enforced (requiring the user to type a 2-digit number displayed on the login screen into their authenticator app)?

### Defensive and engineering notes

1. **Prioritize Phishing-Resistant WebAuthn/Passkeys:** Implement WebAuthn / FIDO2 as the primary authentication and step-up verification mechanism for web applications.
2. **Deprecate Insecure Factors:** Avoid SMS and phone voice OTPs where possible, following NIST SP 800-63B guidelines that classify them as restricted. Eliminate knowledge-based security questions.
3. **Defend Push Channels:** If mobile push notifications are supported, mandate number-matching, enforce strict prompt rate limits, and provide immediate one-tap fraud reporting.
4. **Harden Recovery & Reset Flows:** Require re-authentication with an existing factor before allowing changes to MFA settings. Invalidate all active sessions across all devices upon MFA factor resets or password changes, and notify the user through multiple out-of-band channels.
5. **Enforce Step-Up Authentication:** Require step-up re-authentication with a strong factor before sensitive operations (e.g. wire transfers, changing email addresses, exporting customer data).

### Reading order

1. Read [OWASP — Multifactor Authentication Cheat Sheet](resources.md#mfa-passkeys) for factor classifications and attack analysis.
2. Read [Duo Security — WebAuthn Guide](resources.md#mfa-passkeys) for technical protocol mechanics and origin binding.
3. Connect with Chapter 3 Passwords, Authentication & Account Recovery and Chapter 3 Session Security.

<a id="authorization-idor"></a>
## Access Control, IDOR & BOLA

### Prerequisites

Understand authentication, session state, resource identifiers and the application's domain model: users, roles, tenants, projects, organizations and objects. You should be able to create at least two test identities in an authorized environment before testing this topic.

### Mechanism and mental model

Authorization decides whether an authenticated subject can perform an action on a specific object in a specific context. IDOR and BOLA happen when the application accepts a reference to an object but does not verify that the current subject is allowed to use that object. The reference can be a numeric ID, UUID, slug, filename, account number, token or nested path; making it hard to guess does not make the authorization decision correct.

Think in a matrix: subjects, roles, tenants, objects, actions and workflow state. A correct system denies by default, validates permission on every request and uses server-side or gateway-side enforcement rather than trusting hidden fields, client-side checks or UI visibility.

### Practical learning notes

For authorized testing, build a small matrix with at least two accounts and objects owned by each account. Test read, create, update, delete, export and administrative actions. Record the expected decision before sending a request; this prevents turning testing into random identifier tampering. Keep tests bounded and avoid touching real users' data unless the written scope explicitly permits it.

### Defensive and engineering notes

Enforce object-level authorization close to the data access or policy layer, not only in the controller or UI. Prefer scoped queries such as “find this object within the current user's allowed set” over fetch-then-filter patterns unless a centralized policy service performs the check reliably. Log denied access attempts consistently, normalize forbidden/not-found behavior when existence is sensitive, and add regression tests for both allowed and denied cases.

### Reading order

1. Read [OWASP — Authorization Cheat Sheet](resources.md#authorization-idor) for the control model.
2. Read [OWASP — IDOR Prevention Cheat Sheet](resources.md#authorization-idor) for object-reference failures and scoped lookup patterns.
3. Then branch to tenant isolation, REST/API BOLA and framework-specific authorization patterns.

<a id="tenant-isolation"></a>
## Multi-Tenant Isolation & Delegated Access

### Prerequisites

Understand authentication, authorization models (RBAC, ABAC), relational and document databases, and how Software-as-a-Service (SaaS) applications model organizations, workspaces, and accounts.

### Mechanism and mental model

In multi-tenant SaaS systems, a single application infrastructure serves multiple customer organizations (tenants). The fundamental architectural imperative is ensuring that no tenant can ever observe, modify, or infer data belonging to another tenant.

Key architectural dimensions of multi-tenant isolation include:
1. **Separation of Users from Tenants:** A human user identity is distinct from a tenant context. A single user may belong to multiple organizations or switch between customer workspaces. Authorization decisions must evaluate the user's permissions *specifically within the active tenant context*.
2. **Tenancy Isolation Models:**
   - *Siloed Model (Isolated Compute/Storage):* Dedicated databases, storage buckets, or Kubernetes namespaces per tenant. Provides the strongest physical boundary and compliance isolation, but incurs higher infrastructure cost and operational overhead.
   - *Pooled / Shared Model:* Shared application compute and shared database instances across all tenants, with logical separation enforced via a tenant identifier column (`tenant_id`). Highly scalable and cost-effective, but vulnerable to catastrophic cross-tenant data leaks if a single query omits the tenant filter.
   - *Hybrid Model with Row-Level Security (RLS):* Shared database instances where the database engine itself enforces tenant isolation policies (e.g. PostgreSQL RLS). Every session sets a tenant context (`SET LOCAL app.current_tenant_id = '...'`), and the database automatically restricts every query to that tenant, providing defense-in-depth against application-level missing `WHERE` clauses.
3. **Tenant Context Propagation:** In distributed microservices, the verified tenant context must be propagated across all inter-service RPC calls and background message queues. Relying on client-supplied headers (e.g. `X-Tenant-ID`) without cryptographic verification allows trivial cross-tenant impersonation.
4. **Delegated Access & Cross-Tenant Impersonation:** SaaS platforms frequently provide support impersonation tools ("login as customer") or partner delegated administration. These high-privilege paths must be tightly bounded by multi-party approval, ephemeral time limits, and immutable audit logging.

### Practical learning notes

When auditing multi-tenant architectures or testing authorized SaaS applications:
- Test for missing tenant scoping in search, export, and reporting queries: developers often remember `tenant_id` in primary CRUD endpoints but omit it in complex analytical queries, bulk exports, or Elasticsearch indices.
- Inspect asynchronous background jobs: verify whether worker queues process tasks with the correct tenant context, preventing one tenant from triggering jobs against another tenant's resources.
- Evaluate IDOR at tenant boundaries: verify whether changing a tenant ID parameter in an API path or JWT claim allows accessing objects belonging to another organization.

### Defensive and engineering notes

1. **Enforce Database Row-Level Security (RLS):** Implement database-level isolation policies (PostgreSQL RLS) as a mandatory defense-in-depth layer behind application query scoping.
2. **Bind Tenant Context Cryptographically:** Include verified tenant identifiers inside signed, tamper-proof session tokens or internal mTLS identity certificates rather than trusting mutable request headers.
3. **Automate Scoped Query Builders:** Enforce tenant isolation at the ORM/repository layer (e.g. global ORM query scopes that automatically append `WHERE tenant_id = :current_tenant`), rather than relying on manual developer diligence on every query.
4. **Isolate Shared Backing Infrastructure:** Use separate cache namespaces (e.g. Redis key prefixes), separate S3 object prefixes/buckets, and tenant-partitioned message queues to prevent cache pollution and data cross-contamination.

### Reading order

1. Read [Microsoft Azure Architecture Center — Architect Multitenant Solutions on Azure](resources.md#tenant-isolation) for comprehensive SaaS tenancy patterns and data isolation strategies.
2. Cross-reference with Chapter 3 Access Control, IDOR & BOLA and Chapter 4 Vulnerability Classes.

<a id="jwt"></a>
## JWT & Token Validation

### Prerequisites

Understand Base64URL encoding, symmetric cryptography (HMAC) versus asymmetric cryptography (RSA/ECDSA), JSON Web Signature (JWS) structure (Header.Payload.Signature), API bearer token mechanisms, and token lifecycle management.

### Mechanism and mental model

JSON Web Tokens (JWT) are self-contained security tokens carrying claims used for authentication and authorization. Because JWTs are stateless by default, the relying party (resource server) relies entirely on cryptographic signature verification to ensure the token has not been tampered with or forged.

Most JWT vulnerabilities stem from parser flaws, cryptographic misunderstandings, or trusting unauthenticated header parameters:
- **Unsecured Tokens (`alg: "none"`):** The JWT specification allows tokens without signatures (`alg: "none"`). Vulnerable libraries trust this header value without enforcing that signatures are mandatory, allowing attackers to forge arbitrary claims simply by setting `alg` to `none` and stripping the signature.
- **Key Type Confusion (Algorithm Confusion):** Applications expecting asymmetric RSA/ECDSA signatures (`RS256`) use a public key for verification. An attacker changes the header algorithm to symmetric HMAC (`HS256`) and signs the token using the server's public key (which is publicly accessible) as the HMAC shared secret. If the verifier dynamically picks the algorithm from the token header, the signature verification succeeds.
- **Header Parameter Injection:** JWS headers can carry parameters indicating which key should verify the token (`kid`, `jwk`, `jku`, `x5u`). If the server blindly trusts these unauthenticated headers, attackers can point `jku` to an attacker-controlled JWKS URL, embed a rogue key via `jwk`, or inject path traversal/SQLi into `kid` to force verification against a static file (e.g. `/dev/null`) or empty key.
- **Missing Claim Validation:** Failing to strictly validate standard claims (`exp`, `nbf`, `iss`, `aud`) leads to token replay across different microservices or accepting expired sessions.
- **Revocation Gaps:** Because JWTs are stateless, revoking a compromised token before its expiration requires an explicit mechanism, such as token status lists, database-backed denylists (`jti`), or maintaining very short lifespans paired with refresh tokens.

### Practical learning notes

When auditing or testing JWT implementations in authorized labs, decode tokens into their JSON components. Test whether the server accepts `alg: none` (in various capitalizations), evaluate algorithm confusion when public keys are accessible, and inspect how the server resolves the `kid` parameter. Verify that access tokens cannot be replayed across different microservices by ensuring audience checks (`aud`) are strictly enforced.

### Defensive and engineering notes

1. **Static Algorithm Enforcement:** Never allow the JWT header to determine the verification algorithm. Hardcode the expected algorithm (e.g. strictly `RS256` or `EdDSA`) in the verifier configuration.
2. **Key Separation:** Ensure public keys and symmetric shared secrets are stored in strictly isolated key stores so public certificates can never be used as HMAC secrets.
3. **Strict Header Sanitization:** Disable or disallow client-supplied key locators (`jwk`, `jku`, `x5u`). If `kid` is used, match it strictly against a pre-approved, internal whitelist of key identifiers.
4. **Mandatory Claim Validation:** Always validate `exp` (with small clock skew tolerance), `iss`, and `aud` on every request.
5. **Explicit Token Typing:** Enforce explicit token type validation using the `typ` header (e.g. `typ: at+jwt` for access tokens) to prevent cross-JWT confusion between ID tokens, access tokens, and refresh tokens.
6. **Short Lifetimes:** Keep access token validity short (e.g. 5–15 minutes) and manage revocation at the refresh token layer or via Token Status Lists.

### Reading order

1. Read [OWASP — JSON Web Token Cheat Sheet](resources.md#jwt) for the defensive baseline.
2. Study RFC 8725 (JWT Best Current Practices).
3. Connect with Chapter 6 REST API Security.

<a id="oauth-oidc"></a>
## OAuth & OpenID Connect

### Prerequisites

Understand sessions, redirects, browser origins, CSRF basics and the difference between authentication, authorization and delegation. OAuth is easier to misuse when treated as a generic login protocol without understanding its roles.

### Mechanism and mental model

OAuth delegates access from a resource owner to a client through an authorization server and resource server. The Authorization Code flow with PKCE protects code exchange, while redirect URI validation, state/nonce handling, token audience/scope validation and refresh-token controls protect the rest of the flow. OIDC adds an identity layer and ID tokens; access tokens are still for resource servers.

Most OAuth failures are broken binding problems: a code is not bound to the client, a redirect is not bound to a registered URI, a token is not bound to the intended audience, a response is not bound to the initiating browser state, or a client is trusted beyond its type.

### Practical learning notes

In authorized testing, diagram the exact flow before modifying requests. Identify client type, redirect URIs, PKCE use, state/nonce behavior, token storage, refresh-token behavior and resource-server validation. Avoid testing against third-party IdPs or production tenants unless the written scope explicitly permits it.

### Defensive and engineering notes

Use Authorization Code with PKCE, avoid implicit and password grants, register exact redirect URIs, reject arbitrary redirect forwarding, validate issuer/audience/expiry/scopes/actions at resource servers and rotate or sender-constrain refresh tokens where appropriate. Log OAuth failures in a way that supports incident response without exposing tokens.

### Reading order

1. Read [OWASP — OAuth2 Cheat Sheet](resources.md#oauth-oidc) for a practical security baseline.
2. Then inspect OIDC/JWT and provider-specific documentation for the chosen stack.
3. Pair with CSRF, session management and API authorization material.

<a id="saml-scim"></a>
## SAML, SCIM & Enterprise SSO

### Prerequisites

Understand XML documents, XML namespaces, XML Digital Signatures (XMLDSig), XML Canonicalization (C14N), XPath queries, and identity federation architectures (Identity Provider vs. Service Provider).

### Mechanism and mental model

Security Assertion Markup Language (SAML 2.0) is a federated enterprise authentication standard relying on XML documents passed through browser redirects or POST requests. The Service Provider (SP) trusts assertions signed by an Identity Provider (IdP).

Because XML and XMLDSig are inherently complex and stateful, SAML implementations are notoriously fragile:
- **XML Signature Wrapping (XSW):** In XSW attacks, an attacker manipulates the XML structure so that the cryptographic signature verifies an authentic assertion, while the application's business logic processes an attacker-controlled, forged assertion. This discrepancy arises when signature verification uses one XPath expression (e.g. `//ds:Signature`) while assertion extraction uses another, or when assertions are cloned into extension blocks.
- **Dual-Parser Desynchronization:** Many SAML libraries rely on multiple distinct XML parsers (e.g., using `Nokogiri`/`libxml2` for digital signature verification and `REXML` for assertion handling). Differences in how these parsers handle namespace prefixes, attribute collisions (e.g. `ID` vs `samlp:ID`), and node selection allow attackers to hide or swap signature elements.
- **Void Canonicalization:** Canonicalization transforms standard XML into a uniform byte stream prior to hashing. Research demonstrates that unhandled exceptions during C14N (such as relative namespace URIs like `xmlns:ns="1"`) cause parsers like libxml2 to abort and return an empty string. The resulting digest is computed over empty data, producing a static, known hash (`47DEQpj8HBSa+/TImW+5JCeuQeRkm5NMpJWZG3hSuFU=`). Attackers can leverage this to produce "Golden SAML Responses" that universally pass validation.
- **Protocol Processing Failures:** Bypasses frequently occur when SPs fail to validate critical protocol attributes: ignoring `InResponseTo` (enabling unsolicited assertion injection), failing to match `Recipient` to the exact Assertion Consumer Service (ACS) endpoint, or omitting `AudienceRestriction` checks.

### Practical learning notes

When analyzing SAML in authorized environments, inspect base64-decoded SAML responses using tools like SAML Raider. Check whether the digital signature covers the `<samlp:Response>` element, the `<saml:Assertion>` element, or both. Verify how the SP handles cloned assertions, missing signatures on assertions, or modified assertions. Test exclusively against systems you own or have explicit written authorization to evaluate.

### Defensive and engineering notes

1. **Unified, Modern SAML Engines:** Avoid legacy architectures that split XML signature validation and assertion parsing across different parsers or modules. Use mature, actively maintained SAML libraries.
2. **Sign Assertions Directly:** Ensure the Identity Provider cryptographically signs the `<saml:Assertion>` element, and require the Service Provider to verify the signature directly on the assertion before consuming attributes.
3. **Rigorous Protocol Validation:**
   - Enforce strict `InResponseTo` matching against the original AuthnRequest ID stored in the user's session.
   - Validate that `Recipient` exactly matches the SP's Assertion Consumer Service URL.
   - Enforce `AudienceRestriction` matching the SP's configured Entity ID.
   - Reject assertions outside the validity window (`NotBefore` and `NotOnOrAfter`).
4. **Harden XML Processing:** Fully disable DTD processing and external entity resolution (`disallow-doctype-decl`) to prevent XXE. Validate schemas strictly and reject unexpected namespace redefinitions or relative namespace URIs.

### Reading order

1. Read [PortSwigger Research — The Fragile Lock: Novel Bypasses For SAML Authentication](resources.md#saml-scim) for parser desynchronization and XSW mechanics.
2. Read [OWASP — SAML Security Cheat Sheet](resources.md#saml-scim) for protocol validation rules.
3. Connect with Chapter 4 XML External Entities (XXE) and Chapter 3 Identity Security.

