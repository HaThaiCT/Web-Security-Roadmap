<!-- GENERATED FILE: do not edit by hand. Run scripts/generate.py. -->
# Curated Resources — Authentication, Authorization & Identity Security

<a id="passwords-recovery"></a>
## Passwords

### Core

- **[Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  Practical implementation guidance for authentication systems, including user identifiers, password policy, generic error handling, automated attack protections, TLS requirements, re-authentication triggers and logging. It is especially useful for developers and AppSec reviewers because it turns identity risks into concrete control requirements. Pair it with protocol-specific resources before designing OAuth, OIDC, SAML or passkey flows.
- **[Bot Management and Anti-Automation Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Bot_Management_and_Anti-Automation_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  A practical guide for mitigating automated threats and business-logic abuse across web applications. Grounded in the OWASP Automated Threats to Web Applications project (OAT-001 through OAT-021), it covers defense against credential stuffing (OAT-008), scraping (OAT-011), inventory scalping (OAT-005), and card testing (OAT-001), detailing layered defensive architectures, behavioral anomaly detection, and rate limiting.
- **[Cryptographic Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  A practical guide for implementing secure data storage encryption in web backends. It establishes standards for authenticated encryption (AEAD like AES-GCM), key separation, cryptographically secure pseudorandom number generators (CSPRNG), and distinguishes reversible data encryption from memory-hard password hashing (Argon2id, scrypt, bcrypt).
- **[Multifactor Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Multifactor_Authentication_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  An authoritative reference for designing, implementing, and assessing multifactor authentication (MFA). It analyzes the five recognized authentication factor types, ranks factor security (contrasting phishing-resistant FIDO2/WebAuthn with restricted SMS/voice channels), details attack patterns like MFA fatigue and adversary-in-the-middle reverse proxies, and defines strict requirements for high-risk factor resets and step-up authentication.
- **[Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  A detailed practical guide to web session design, cookie attributes, session ID entropy, expiration, rotation, logout and logging. It is especially useful for developers implementing session-backed apps and testers reviewing fixation, persistence, transport and token-storage mistakes.
- **[WebAuthn Guide](https://webauthn.guide/)** — *documentation · intermediate · learner, tester, developer · free/public*  
  A clear, interactive technical guide to the W3C Web Authentication (WebAuthn) / FIDO2 standard. It breaks down asymmetric public-key credential creation (navigator.credentials.create) and assertion authentication (navigator.credentials.get), explaining how hardware-backed private keys and cryptographic origin-binding structurally eliminate credential theft and adversary-in-the-middle phishing.

<a id="sessions"></a>
## Session & Cookie Security

### Core

- **[Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  Practical implementation guidance for authentication systems, including user identifiers, password policy, generic error handling, automated attack protections, TLS requirements, re-authentication triggers and logging. It is especially useful for developers and AppSec reviewers because it turns identity risks into concrete control requirements. Pair it with protocol-specific resources before designing OAuth, OIDC, SAML or passkey flows.
- **[Cross-Site Request Forgery Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  Practical CSRF guidance covering synchronizer tokens, signed double-submit cookies, SameSite limits, custom headers, Fetch Metadata, Origin/Referer checks and user-interaction defenses. It is valuable because it explains when each control fails, including client-side CSRF and XSS defeating CSRF mitigations. Use it after learning cookies and before reviewing state-changing endpoints.
- **[JSON Web Token Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/JSON_Web_Token_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  A thorough technical reference for securing JSON Web Tokens (JWT) across issuance, transmission, and validation. It addresses critical cryptographic pitfalls including alg none stripping, public-key vs HMAC key type confusion, untrusted header parameters (jwk, jku, kid, x5u), cross-JWT confusion, and token revocation strategies via status lists and deny-lists.
- **[Multifactor Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Multifactor_Authentication_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  An authoritative reference for designing, implementing, and assessing multifactor authentication (MFA). It analyzes the five recognized authentication factor types, ranks factor security (contrasting phishing-resistant FIDO2/WebAuthn with restricted SMS/voice channels), details attack patterns like MFA fatigue and adversary-in-the-middle reverse proxies, and defines strict requirements for high-risk factor resets and step-up authentication.
- **[OAuth2 Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/OAuth2_Cheat_Sheet.html)** — *cheatsheet · advanced · tester, developer · free/public*  
  A compact security baseline for OAuth 2.x and OIDC deployments. It prioritizes Authorization Code with PKCE, strict redirect handling, state/nonce, token binding/rotation and resource-server validation. Read it after core authentication and sessions; OAuth is a delegation protocol, not a generic login shortcut.
- **[Practical security implementation guides](https://developer.mozilla.org/en-US/docs/Web/Security/Practical_implementation_guides)** — *documentation · intermediate · developer, tester · free/public*  
  A developer-facing index of practical web security controls, especially transport security and browser-facing headers. It is valuable as a bridge between vulnerability knowledge and implementation because it prioritizes controls such as HTTPS resource loading, HTTPS redirection, HSTS, clickjacking prevention, secure cookies, CORS, CSP, Referrer-Policy and Subresource Integrity. Treat it as an implementation checklist and then read the linked deep guides for each control.
- **[Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  A detailed practical guide to web session design, cookie attributes, session ID entropy, expiration, rotation, logout and logging. It is especially useful for developers implementing session-backed apps and testers reviewing fixation, persistence, transport and token-storage mistakes.
- **[Set-Cookie header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie)** — *documentation · beginner · learner, tester, developer · free/public*  
  A practical reference for cookie syntax and attributes: Secure, HttpOnly, SameSite, Domain, Path, Expires, Max-Age, prefixes and partitioned cookies. It gives the vocabulary needed before studying sessions, CSRF, browser storage and cookie hardening.
- **[Web Storage API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Storage_API)** — *documentation · beginner · learner, tester, developer · free/public*  
  The definitive browser documentation for client-side state storage mechanisms: localStorage and sessionStorage. It details origin-partitioned storage boundaries, contrasts tab-scoped ephemeral storage with persistent storage, analyzes synchronous performance implications, and establishes security boundaries—emphasizing that Web Storage is fully accessible to JavaScript and must never store sensitive session tokens or secrets vulnerable to XSS.

<a id="mfa-passkeys"></a>
## MFA

### Core

- **[Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  Practical implementation guidance for authentication systems, including user identifiers, password policy, generic error handling, automated attack protections, TLS requirements, re-authentication triggers and logging. It is especially useful for developers and AppSec reviewers because it turns identity risks into concrete control requirements. Pair it with protocol-specific resources before designing OAuth, OIDC, SAML or passkey flows.
- **[Multifactor Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Multifactor_Authentication_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  An authoritative reference for designing, implementing, and assessing multifactor authentication (MFA). It analyzes the five recognized authentication factor types, ranks factor security (contrasting phishing-resistant FIDO2/WebAuthn with restricted SMS/voice channels), details attack patterns like MFA fatigue and adversary-in-the-middle reverse proxies, and defines strict requirements for high-risk factor resets and step-up authentication.
- **[WebAuthn Guide](https://webauthn.guide/)** — *documentation · intermediate · learner, tester, developer · free/public*  
  A clear, interactive technical guide to the W3C Web Authentication (WebAuthn) / FIDO2 standard. It breaks down asymmetric public-key credential creation (navigator.credentials.create) and assertion authentication (navigator.credentials.get), explaining how hardware-backed private keys and cryptographic origin-binding structurally eliminate credential theft and adversary-in-the-middle phishing.

<a id="authorization-idor"></a>
## Access Control

### Core

- **[Architect Multitenant Solutions on Azure](https://learn.microsoft.com/en-us/azure/architecture/guide/multitenant/overview)** — *documentation · advanced · tester, developer · free/public*  
  An authoritative reference architecture for designing multi-tenant software-as-a-service (SaaS) solutions. It establishes clear architectural boundaries between users and tenants, analyzes tenancy models (deployment stamps, siloed vs. pooled compute/storage), details data isolation strategies (database-per-tenant, schema-per-tenant, shared database with Row-Level Security), and covers tenant context propagation across distributed services.
- **[Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html)** — *cheatsheet · intermediate · tester, developer · free/public*  
  A practical control baseline for server-side authorization decisions. It emphasizes deny-by-default, least privilege, validating permissions on every request, centralized enforcement and logging failed access-control checks. Use it as the design and review companion to IDOR/BOLA testing resources.
- **[Business Logic Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Business_Logic_Security_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  A practical guide for preventing business logic flaws and workflow subversion. It details strategies for enforcing application domain invariants, validating multi-step state transitions, maintaining integrity across transactional operations (e.g. pricing, coupons, quantity limits), and designing state machines that resist parameter manipulation and sequence bypasses.
- **[GraphQL Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/GraphQL_Cheat_Sheet.html)** — *cheatsheet · intermediate · tester, developer · free/public*  
  A GraphQL-specific security baseline covering schema-driven validation, query depth/amount limits, batching abuse, authorization on edges and nodes, introspection controls and error handling. It is useful because GraphQL concentrates many API risks into fewer network requests and resolver paths.
- **[Insecure Direct Object Reference Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Insecure_Direct_Object_Reference_Prevention_Cheat_Sheet.html)** — *cheatsheet · beginner · learner, tester, developer · free/public*  
  Focused guidance for object-level authorization mistakes: object, reference and missing permission check. It is useful for learners because it separates identifier complexity from authorization, for testers because it describes cross-account verification, and for developers because it shows scoped lookup patterns. Treat opaque IDs as defense-in-depth only, never as the primary control.
- **[OAuth2 Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/OAuth2_Cheat_Sheet.html)** — *cheatsheet · advanced · tester, developer · free/public*  
  A compact security baseline for OAuth 2.x and OIDC deployments. It prioritizes Authorization Code with PKCE, strict redirect handling, state/nonce, token binding/rotation and resource-server validation. Read it after core authentication and sessions; OAuth is a delegation protocol, not a generic login shortcut.
- **[OWASP API Security Top 10 2023](https://api-security.owasp.org/editions/2023/en/0x11-t10)** — *documentation · beginner · learner, tester, developer · free/public*  
  A high-level risk map for API work. It is not a control guide by itself, but it helps learners and teams orient around object-level authorization, authentication, property-level authorization, resource consumption, function-level authorization, sensitive business flows, SSRF, misconfiguration, inventory and unsafe third-party API consumption.

<a id="tenant-isolation"></a>
## Multi-Tenant Isolation & Delegated Access

### Core

- **[Architect Multitenant Solutions on Azure](https://learn.microsoft.com/en-us/azure/architecture/guide/multitenant/overview)** — *documentation · advanced · tester, developer · free/public*  
  An authoritative reference architecture for designing multi-tenant software-as-a-service (SaaS) solutions. It establishes clear architectural boundaries between users and tenants, analyzes tenancy models (deployment stamps, siloed vs. pooled compute/storage), details data isolation strategies (database-per-tenant, schema-per-tenant, shared database with Row-Level Security), and covers tenant context propagation across distributed services.
- **[Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html)** — *cheatsheet · intermediate · tester, developer · free/public*  
  A practical control baseline for server-side authorization decisions. It emphasizes deny-by-default, least privilege, validating permissions on every request, centralized enforcement and logging failed access-control checks. Use it as the design and review companion to IDOR/BOLA testing resources.
- **[Insecure Direct Object Reference Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Insecure_Direct_Object_Reference_Prevention_Cheat_Sheet.html)** — *cheatsheet · beginner · learner, tester, developer · free/public*  
  Focused guidance for object-level authorization mistakes: object, reference and missing permission check. It is useful for learners because it separates identifier complexity from authorization, for testers because it describes cross-account verification, and for developers because it shows scoped lookup patterns. Treat opaque IDs as defense-in-depth only, never as the primary control.
- **[RAG Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/RAG_Security_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  An authoritative reference for securing Retrieval-Augmented Generation (RAG) pipelines in enterprise AI applications. It details how RAG redistributes attack surfaces across document ingestion, embedding generation, vector storage, and response generation; establishes access control metadata on individual vector chunks; mandates tenant and data classification isolation in vector databases; and outlines query normalization and output validation controls.
- **[The Fragile Lock: Novel Bypasses For SAML Authentication](https://portswigger.net/research/the-fragile-lock)** — *article · advanced · tester, developer · free/public*  
  Cutting-edge security research on SAML 2.0 implementations demonstrating full authentication bypasses via XML Signature Wrapping (XSW), attribute pollution, namespace confusion, and Void Canonicalization. It analyzes parser desynchronization between signature verification and assertion consumer modules (e.g. Nokogiri vs REXML) and details how empty digest strings lead to universal token forgery.

### Extended

- **[SAML Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/SAML_Security_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  A structured baseline for implementing and securing the Web Browser SAML/SSO profile. It provides verification rules for protocol usage, message integrity, signature validation over Assertions and Responses, XML parser hardening against XXE and XSW, and handling IdP-initiated unsolicited responses.

<a id="jwt"></a>
## JWT & Token Validation

### Core

- **[JSON Web Token Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/JSON_Web_Token_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  A thorough technical reference for securing JSON Web Tokens (JWT) across issuance, transmission, and validation. It addresses critical cryptographic pitfalls including alg none stripping, public-key vs HMAC key type confusion, untrusted header parameters (jwk, jku, kid, x5u), cross-JWT confusion, and token revocation strategies via status lists and deny-lists.
- **[OAuth2 Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/OAuth2_Cheat_Sheet.html)** — *cheatsheet · advanced · tester, developer · free/public*  
  A compact security baseline for OAuth 2.x and OIDC deployments. It prioritizes Authorization Code with PKCE, strict redirect handling, state/nonce, token binding/rotation and resource-server validation. Read it after core authentication and sessions; OAuth is a delegation protocol, not a generic login shortcut.
- **[REST Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html)** — *cheatsheet · intermediate · tester, developer · free/public*  
  A practical checklist for REST services covering HTTPS, authentication, local authorization, JWT validation, API keys, input/content-type validation, status codes, CORS, rate limiting and audit logging. It is a good bridge from general web vulnerabilities to API-specific implementation and review work.
- **[Web Security Academy](https://portswigger.net/web-security)** — *lab · beginner · learner, tester, developer · free/registration-required*  
  A broad, free training platform with guided material and realistic labs across major web vulnerability classes, APIs, identity flaws, protocol issues and newer areas such as LLM/AI attacks. It is useful for learners and authorized testers because practice happens in a safe and legal lab environment rather than on real targets. Some exercises require Burp Suite; the Community Edition is sufficient for many labs, but the account and tooling expectations should be checked per lab.
- **[Web Storage API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Storage_API)** — *documentation · beginner · learner, tester, developer · free/public*  
  The definitive browser documentation for client-side state storage mechanisms: localStorage and sessionStorage. It details origin-partitioned storage boundaries, contrasts tab-scoped ephemeral storage with persistent storage, analyzes synchronous performance implications, and establishes security boundaries—emphasizing that Web Storage is fully accessible to JavaScript and must never store sensitive session tokens or secrets vulnerable to XSS.

<a id="oauth-oidc"></a>
## OAuth & OpenID Connect

### Core

- **[Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  Practical implementation guidance for authentication systems, including user identifiers, password policy, generic error handling, automated attack protections, TLS requirements, re-authentication triggers and logging. It is especially useful for developers and AppSec reviewers because it turns identity risks into concrete control requirements. Pair it with protocol-specific resources before designing OAuth, OIDC, SAML or passkey flows.
- **[JSON Web Token Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/JSON_Web_Token_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  A thorough technical reference for securing JSON Web Tokens (JWT) across issuance, transmission, and validation. It addresses critical cryptographic pitfalls including alg none stripping, public-key vs HMAC key type confusion, untrusted header parameters (jwk, jku, kid, x5u), cross-JWT confusion, and token revocation strategies via status lists and deny-lists.
- **[OAuth2 Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/OAuth2_Cheat_Sheet.html)** — *cheatsheet · advanced · tester, developer · free/public*  
  A compact security baseline for OAuth 2.x and OIDC deployments. It prioritizes Authorization Code with PKCE, strict redirect handling, state/nonce, token binding/rotation and resource-server validation. Read it after core authentication and sessions; OAuth is a delegation protocol, not a generic login shortcut.
- **[REST Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html)** — *cheatsheet · intermediate · tester, developer · free/public*  
  A practical checklist for REST services covering HTTPS, authentication, local authorization, JWT validation, API keys, input/content-type validation, status codes, CORS, rate limiting and audit logging. It is a good bridge from general web vulnerabilities to API-specific implementation and review work.
- **[Web Security Academy](https://portswigger.net/web-security)** — *lab · beginner · learner, tester, developer · free/registration-required*  
  A broad, free training platform with guided material and realistic labs across major web vulnerability classes, APIs, identity flaws, protocol issues and newer areas such as LLM/AI attacks. It is useful for learners and authorized testers because practice happens in a safe and legal lab environment rather than on real targets. Some exercises require Burp Suite; the Community Edition is sufficient for many labs, but the account and tooling expectations should be checked per lab.

### Extended

- **[SAML Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/SAML_Security_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  A structured baseline for implementing and securing the Web Browser SAML/SSO profile. It provides verification rules for protocol usage, message integrity, signature validation over Assertions and Responses, XML parser hardening against XXE and XSW, and handling IdP-initiated unsolicited responses.

<a id="saml-scim"></a>
## SAML

### Core

- **[Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  Practical implementation guidance for authentication systems, including user identifiers, password policy, generic error handling, automated attack protections, TLS requirements, re-authentication triggers and logging. It is especially useful for developers and AppSec reviewers because it turns identity risks into concrete control requirements. Pair it with protocol-specific resources before designing OAuth, OIDC, SAML or passkey flows.
- **[The Fragile Lock: Novel Bypasses For SAML Authentication](https://portswigger.net/research/the-fragile-lock)** — *article · advanced · tester, developer · free/public*  
  Cutting-edge security research on SAML 2.0 implementations demonstrating full authentication bypasses via XML Signature Wrapping (XSW), attribute pollution, namespace confusion, and Void Canonicalization. It analyzes parser desynchronization between signature verification and assertion consumer modules (e.g. Nokogiri vs REXML) and details how empty digest strings lead to universal token forgery.

### Extended

- **[SAML Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/SAML_Security_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  A structured baseline for implementing and securing the Web Browser SAML/SSO profile. It provides verification rules for protocol usage, message integrity, signature validation over Assertions and Responses, XML parser hardening against XXE and XSW, and handling IdP-initiated unsolicited responses.
