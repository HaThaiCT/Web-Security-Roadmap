# Learning Path — Learner

This path is for people building practical Web Security foundations. It does not require reading all nine parts in order. Each stage points to the topic sections and curated resource lists that matter for the competency being built.

Use topic pages for the mental model, then use the linked resource lists for reviewed external material. Practice only in hosted labs or deliberately vulnerable systems you own or are authorized to use.

## Beginner

### Goal

Understand how the web works, how requests move through an application, and why common vulnerability classes exist.

### Prerequisites

- Basic command-line usage.
- Basic HTML, JavaScript, and one server-side language.
- Ability to read HTTP requests and responses.

### Study route

1. Web foundations
   - Topic: [HTTP Requests, Responses & Versions](../topics/ch01-foundations/README.md#http)
   - Curated resources: [HTTP resources](../topics/ch01-foundations/resources.md#http)
   - Focus resource: [MDN — Overview of HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview)
2. Origins, cookies and browser state
   - Topic: [Origins, Cookies & Browser Storage](../topics/ch01-foundations/README.md#origins-cookies)
   - Curated resources: [Origins and cookie resources](../topics/ch01-foundations/resources.md#origins-cookies)
   - Focus resources: [MDN — Same-origin policy](https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy) and [MDN — Set-Cookie header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie)
3. Request lifecycle and application layers
   - Topic: [Request Lifecycle & Application Layers](../topics/ch02-web-architecture/README.md#request-lifecycle) and [Proxies, Caches & Distributed Components](../topics/ch02-web-architecture/README.md#distributed-components)
   - Curated resources: [HTTP caching resources](../topics/ch02-web-architecture/resources.md#distributed-components)
   - Focus resource: [MDN — HTTP caching](https://developer.mozilla.org/en-US/docs/Web/HTTP/Caching)
4. Authentication, sessions and authorization
   - Topics: [Session & Cookie Security](../topics/ch03-identity/README.md#sessions) and [Access Control, IDOR & BOLA](../topics/ch03-identity/README.md#authorization-idor)
   - Curated resources: [session resources](../topics/ch03-identity/resources.md#sessions) and [authorization/IDOR resources](../topics/ch03-identity/resources.md#authorization-idor)
   - Focus resources: [OWASP Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html), [OWASP Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html), and [OWASP IDOR Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Insecure_Direct_Object_Reference_Prevention_Cheat_Sheet.html)
5. First vulnerability classes
   - Topic: [SQL & NoSQL Injection](../topics/ch04-vulnerabilities/README.md#sql-nosql)
   - Curated resources: [SQL/NoSQL resources](../topics/ch04-vulnerabilities/resources.md#sql-nosql)
   - Focus resource: [OWASP SQL Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html)
6. Browser-side flaws
   - Topics: [Reflected, Stored & DOM XSS](../topics/ch05-browser-protocols/README.md#xss), [CSRF](../topics/ch05-browser-protocols/README.md#csrf), and [CORS](../topics/ch05-browser-protocols/README.md#cors)
   - Curated resources: [XSS resources](../topics/ch05-browser-protocols/resources.md#xss), [CSRF resources](../topics/ch05-browser-protocols/resources.md#csrf), and [CORS resources](../topics/ch05-browser-protocols/resources.md#cors)
   - Focus resources: [OWASP XSS Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html), [OWASP CSRF Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html), and [MDN — CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS)
7. Safe practice habit
   - Topics: [Labs](../topics/ch08-emerging-practice/README.md#practice-labs) and [Authorized Testing Methodology](../topics/ch08-emerging-practice/README.md#testing-methodology)
   - Curated resources: [lab resources](../topics/ch08-emerging-practice/resources.md#practice-labs) and [testing methodology resources](../topics/ch08-emerging-practice/resources.md#testing-methodology)
   - Focus resources: [PortSwigger Web Security Academy](https://portswigger.net/web-security) and [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)

### Practice

Use hosted labs or deliberately vulnerable local labs in an isolated environment. Start with the lab platform, read the topic overview, attempt the exercise, then return to the prevention-oriented resource to explain the root cause and fix. Do not point tests at systems you do not own or have written authorization to test.

### Completion signals

You can explain a request lifecycle, identify where untrusted input enters and leaves an application, explain authentication versus authorization, and complete beginner labs for XSS, SQL injection, CSRF, and IDOR without copying a walkthrough.

## Intermediate

### Goal

Connect mechanisms to root causes and learn how vulnerabilities appear in realistic applications.

### Study route

- Identity protocols
  - Topic: [OAuth & OpenID Connect](../topics/ch03-identity/README.md#oauth-oidc)
  - Curated resources: [OAuth/OIDC resources](../topics/ch03-identity/resources.md#oauth-oidc)
  - Focus resource: [OWASP OAuth2 Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/OAuth2_Cheat_Sheet.html)
- Token validation
  - Topic: [JWT & Token Validation](../topics/ch03-identity/README.md#jwt)
  - Curated resources: [JWT resources](../topics/ch03-identity/resources.md#jwt)
  - Focus resource: [OWASP JSON Web Token Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/JSON_Web_Token_Cheat_Sheet.html)
- API risks
  - Topic: [REST, OpenAPI & API Inventory](../topics/ch06-api-frameworks/README.md#rest-openapi)
  - Curated resources: [REST/API resources](../topics/ch06-api-frameworks/resources.md#rest-openapi)
  - Focus resources: [OWASP REST Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html) and [OWASP API Security Top 10 2023](https://api-security.owasp.org/editions/2023/en/0x11-t10)
- GraphQL
  - Topic: [GraphQL Security](../topics/ch06-api-frameworks/README.md#graphql)
  - Curated resources: [GraphQL resources](../topics/ch06-api-frameworks/resources.md#graphql)
  - Focus resource: [OWASP GraphQL Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/GraphQL_Cheat_Sheet.html)
- Business logic & workflows
  - Topic: [Business Logic & Workflow Integrity](../topics/ch04-vulnerabilities/README.md#business-logic)
  - Curated resources: [Business logic resources](../topics/ch04-vulnerabilities/resources.md#business-logic)
  - Focus resource: [OWASP Business Logic Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Business_Logic_Security_Cheat_Sheet.html)
- Multifactor authentication & passkeys
  - Topic: [Multifactor Authentication, Passkeys & WebAuthn](../topics/ch03-identity/README.md#mfa-passkeys)
  - Curated resources: [MFA resources](../topics/ch03-identity/resources.md#mfa-passkeys)
  - Focus resources: [OWASP Multifactor Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Multifactor_Authentication_Cheat_Sheet.html) and [WebAuthn Guide](https://webauthn.guide/)
- Transport security & applied cryptography
  - Topics: [DNS, TLS & Web PKI](../topics/ch01-foundations/README.md#dns-tls) and [Applied Cryptography](../topics/ch01-foundations/README.md#applied-crypto)
  - Curated resources: [TLS resources](../topics/ch01-foundations/resources.md#dns-tls) and [Cryptographic storage resources](../topics/ch01-foundations/resources.md#applied-crypto)
  - Focus resources: [OWASP Transport Layer Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Security_Cheat_Sheet.html) and [OWASP Cryptographic Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html)
- Webhooks & payment workflows
  - Topics: [Webhooks & SaaS Integrations](../topics/ch06-api-frameworks/README.md#webhooks-saas) and [Payment, Checkout & Subscription Workflows](../topics/ch06-api-frameworks/README.md#payments-workflows)
  - Curated resources: [Webhook resources](../topics/ch06-api-frameworks/resources.md#webhooks-saas) and [Payment resources](../topics/ch06-api-frameworks/resources.md#payments-workflows)
  - Focus resources: [Stripe — Webhook Signatures & Security](https://stripe.com/docs/webhooks) and [OWASP Third Party Payment Gateway Integration Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Third_Party_Payment_Gateway_Integration_Cheat_Sheet.html)
- Protocol and server-side workflow mechanics
  - Topics: [SSRF & URL Processing](../topics/ch04-vulnerabilities/README.md#ssrf), [Race Conditions](../topics/ch04-vulnerabilities/README.md#race-conditions), [HTTP Request Smuggling](../topics/ch05-browser-protocols/README.md#http-smuggling), and [Cache Poisoning & Cache Deception](../topics/ch05-browser-protocols/README.md#web-caching)
  - Curated resources: [SSRF resources](../topics/ch04-vulnerabilities/resources.md#ssrf), [Race conditions resources](../topics/ch04-vulnerabilities/resources.md#race-conditions), [Smuggling resources](../topics/ch05-browser-protocols/resources.md#http-smuggling), and [Caching resources](../topics/ch05-browser-protocols/resources.md#web-caching)
  - Focus resources: [PortSwigger — SSRF](https://portswigger.net/web-security/ssrf), [PortSwigger — Race Conditions](https://portswigger.net/web-security/race-conditions), and [PortSwigger — HTTP Request Smuggling](https://portswigger.net/web-security/request-smuggling)

### Practice

Work through topic-specific labs and read real write-ups after attempting the exercise. Focus on the root cause, prerequisites, version/context limits, and safe remediation rather than just payload strings.

### Completion signals

You can write a concise root-cause explanation, describe impact without exaggeration, and propose a concrete fix for common flaws.

## Advanced

### Goal

Specialize while keeping system-level understanding.

### Study route

Choose one specialization and follow its topic/resource cluster:

- Identity and authorization: [Authentication](../topics/ch03-identity/README.md#passwords-recovery), [Sessions](../topics/ch03-identity/README.md#sessions), [Authorization/IDOR](../topics/ch03-identity/README.md#authorization-idor), [OAuth/OIDC](../topics/ch03-identity/README.md#oauth-oidc)
- Browser/client security: [XSS](../topics/ch05-browser-protocols/README.md#xss), [CSRF](../topics/ch05-browser-protocols/README.md#csrf), [CORS](../topics/ch05-browser-protocols/README.md#cors), [CSP](../topics/ch05-browser-protocols/README.md#csp-clickjacking)
- API and business logic: [REST/API](../topics/ch06-api-frameworks/README.md#rest-openapi), [GraphQL](../topics/ch06-api-frameworks/README.md#graphql), [Business Logic](../topics/ch04-vulnerabilities/README.md#business-logic)
- Cloud-backed web applications: [Object Storage & Secrets](../topics/ch07-cloud-supply-chain/README.md#storage-secrets), [Containers & Kubernetes](../topics/ch07-cloud-supply-chain/README.md#containers-kubernetes), [CI/CD Security](../topics/ch07-cloud-supply-chain/README.md#cicd-security)
- Supply chain and deployment security: [Dependencies, SBOM, Signing & Provenance](../topics/ch07-cloud-supply-chain/README.md#dependencies-artifacts), [Hardening & Secure Defaults](../topics/ch09-security-engineering/README.md#hardening-defaults)
- AI-enabled web applications: [AI-Enabled Web Applications & Tool Permissions](../topics/ch08-emerging-practice/README.md#ai-web-security) and [RAG](../topics/ch08-emerging-practice/README.md#rag-isolation), noting that dedicated curated resources are still being expanded

Then use [Security Architecture & Engineering](../topics/ch09-security-engineering/README.md) to synthesize threat modeling, design choices, testing strategy, and remediation verification.

### Completion signals

You can take a realistic case study, identify prerequisites, explain why the issue exists, map it to controls, and design a prevention/regression-test strategy.
