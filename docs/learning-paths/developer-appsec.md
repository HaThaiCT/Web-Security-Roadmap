# Learning Path — Developer / AppSec

This path is for people who build, review, and improve web systems. It uses vulnerability knowledge to support design, implementation, testing, and remediation.

Use the topic page for the model, the curated resources for implementation and verification references, and your own codebase or lab apps for practice. Do not copy controls blindly; map each control to the trust boundary, data flow, and failure mode it is supposed to address.

## Beginner

### Goal

Understand the mechanics that make security controls necessary.

### Study route

1. Request lifecycle and application layers
   - Topic: [Request Lifecycle & Application Layers](../topics/ch02-web-architecture/README.md#request-lifecycle) and [Proxies, Caches & Distributed Components](../topics/ch02-web-architecture/README.md#distributed-components)
   - Curated resources: [HTTP caching resources](../topics/ch02-web-architecture/resources.md#distributed-components)
   - Focus resource: [MDN — HTTP caching](https://developer.mozilla.org/en-US/docs/Web/HTTP/Caching)
2. Identity and session controls
   - Topics: [Passwords, Authentication & Account Recovery](../topics/ch03-identity/README.md#passwords-recovery) and [Session & Cookie Security](../topics/ch03-identity/README.md#sessions)
   - Curated resources: [authentication resources](../topics/ch03-identity/resources.md#passwords-recovery) and [session resources](../topics/ch03-identity/resources.md#sessions)
   - Focus resources: [OWASP Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html), [OWASP Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html), and [MDN — Set-Cookie header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie)
3. Authorization and tenant-safe data access
   - Topic: [Access Control, IDOR & BOLA](../topics/ch03-identity/README.md#authorization-idor)
   - Curated resources: [authorization/IDOR resources](../topics/ch03-identity/resources.md#authorization-idor)
   - Focus resources: [OWASP Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) and [OWASP IDOR Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Insecure_Direct_Object_Reference_Prevention_Cheat_Sheet.html)
4. Injection and rendering safety
   - Topics: [XSS](../topics/ch05-browser-protocols/README.md#xss) and [SQL & NoSQL Injection](../topics/ch04-vulnerabilities/README.md#sql-nosql)
   - Curated resources: [XSS resources](../topics/ch05-browser-protocols/resources.md#xss) and [SQL/NoSQL resources](../topics/ch04-vulnerabilities/resources.md#sql-nosql)
   - Focus resources: [OWASP XSS Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html) and [OWASP SQL Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html)
5. Browser request controls
   - Topics: [CSRF](../topics/ch05-browser-protocols/README.md#csrf), [CORS](../topics/ch05-browser-protocols/README.md#cors), and [CSP, Trusted Types & Clickjacking](../topics/ch05-browser-protocols/README.md#csp-clickjacking)
   - Curated resources: [CSRF resources](../topics/ch05-browser-protocols/resources.md#csrf), [CORS resources](../topics/ch05-browser-protocols/resources.md#cors), and [CSP resources](../topics/ch05-browser-protocols/resources.md#csp-clickjacking)
6. Secure coding and review baseline
   - Topic: [Secure Coding & Code Review](../topics/ch09-security-engineering/README.md#secure-code-review)
   - Curated resources: [secure code review resources](../topics/ch09-security-engineering/resources.md#secure-code-review)
   - Focus resources: [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/) and [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)

### Practice

Trace a feature from route to database and back to rendered output. Identify where validation, authorization, output encoding, CSRF protection, CORS decisions, cookie settings, and logging belong. Add regression tests for both allowed and denied behavior.

### Completion signals

You can explain where a control must live, not just what header or library to add. You can write a small negative test for a security rule.

## Intermediate

### Goal

Apply controls across real architectures.

### Study route

- OAuth, OIDC and token validation
  - Topics: [OAuth & OpenID Connect](../topics/ch03-identity/README.md#oauth-oidc), [JWT & Token Validation](../topics/ch03-identity/README.md#jwt), and [Multi-Tenant Isolation & Delegated Access](../topics/ch03-identity/README.md#tenant-isolation)
  - Curated resources: [OAuth/OIDC resources](../topics/ch03-identity/resources.md#oauth-oidc), [JWT resources](../topics/ch03-identity/resources.md#jwt), and [tenant isolation resources](../topics/ch03-identity/resources.md#tenant-isolation)
  - Focus resource: [OWASP OAuth2 Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/OAuth2_Cheat_Sheet.html)
- API design and review
  - Topics: [REST, OpenAPI & API Inventory](../topics/ch06-api-frameworks/README.md#rest-openapi) and [GraphQL Security](../topics/ch06-api-frameworks/README.md#graphql)
  - Curated resources: [REST/API resources](../topics/ch06-api-frameworks/resources.md#rest-openapi) and [GraphQL resources](../topics/ch06-api-frameworks/resources.md#graphql)
  - Focus resources: [OWASP REST Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html), [OWASP API Security Top 10 2023](https://api-security.owasp.org/editions/2023/en/0x11-t10), and [OWASP GraphQL Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/GraphQL_Cheat_Sheet.html)
- Business logic & workflow integrity
  - Topic: [Business Logic & Workflow Integrity](../topics/ch04-vulnerabilities/README.md#business-logic)
  - Curated resources: [Business logic resources](../topics/ch04-vulnerabilities/resources.md#business-logic)
  - Focus resource: [OWASP Business Logic Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Business_Logic_Security_Cheat_Sheet.html)
- Webhooks & payment workflows
  - Topics: [Webhooks & SaaS Integrations](../topics/ch06-api-frameworks/README.md#webhooks-saas) and [Payment, Checkout & Subscription Workflows](../topics/ch06-api-frameworks/README.md#payments-workflows)
  - Curated resources: [Webhook resources](../topics/ch06-api-frameworks/resources.md#webhooks-saas) and [Payment resources](../topics/ch06-api-frameworks/resources.md#payments-workflows)
  - Focus resources: [Stripe — Webhook Signatures & Security](https://stripe.com/docs/webhooks) and [OWASP Third Party Payment Gateway Integration Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Third_Party_Payment_Gateway_Integration_Cheat_Sheet.html)
- MFA, passkeys & cryptographic storage
  - Topics: [Multifactor Authentication, Passkeys & WebAuthn](../topics/ch03-identity/README.md#mfa-passkeys) and [Applied Cryptography](../topics/ch01-foundations/README.md#applied-crypto)
  - Curated resources: [MFA resources](../topics/ch03-identity/resources.md#mfa-passkeys) and [Cryptographic storage resources](../topics/ch01-foundations/resources.md#applied-crypto)
  - Focus resources: [OWASP Multifactor Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Multifactor_Authentication_Cheat_Sheet.html), [WebAuthn Guide](https://webauthn.guide/), and [OWASP Cryptographic Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html)
- Server-side validation and file processing
  - Topics: [SSRF & URL Processing](../topics/ch04-vulnerabilities/README.md#ssrf) and [File Upload & Document Processing](../topics/ch04-vulnerabilities/README.md#upload-documents)
  - Curated resources: [SSRF resources](../topics/ch04-vulnerabilities/resources.md#ssrf) and [File upload resources](../topics/ch04-vulnerabilities/resources.md#upload-documents)
  - Focus resources: [PortSwigger — SSRF](https://portswigger.net/web-security/ssrf) and [OWASP File Upload Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html)
- Deployment and secrets
  - Topics: [Object Storage & Secrets](../topics/ch07-cloud-supply-chain/README.md#storage-secrets), [Web Servers & Reverse Proxy Hardening](../topics/ch07-cloud-supply-chain/README.md#web-server-proxies), and [CI/CD Permissions & Pipeline Security](../topics/ch07-cloud-supply-chain/README.md#cicd-security)
  - Curated resources: [storage/secrets resources](../topics/ch07-cloud-supply-chain/resources.md#storage-secrets), [proxy-hardening resources](../topics/ch07-cloud-supply-chain/resources.md#web-server-proxies), and [CI/CD resources](../topics/ch07-cloud-supply-chain/resources.md#cicd-security)
  - Focus resources: [OWASP Secrets Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html), [OWASP Docker Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Docker_Security_Cheat_Sheet.html), and [SLSA v1.1 — About SLSA](https://slsa.dev/spec/v1.1/about)

### Practice

Threat-model a feature, identify trust boundaries, write abuse cases, and turn them into implementation requirements and tests. Review both application code and deployment configuration when the feature depends on secrets, webhooks, third-party APIs, CI/CD or object storage.

### Completion signals

You can review a design for authorization, data flow, secret handling, third-party callbacks, deployment trust boundaries, and failure modes. You can verify a fix with focused regression tests.

## Advanced

### Goal

Move from vulnerability-by-vulnerability fixes to security engineering.

### Study route

- Requirements and verification
  - Topics: [Security Requirements & Verification Standards](../topics/ch09-security-engineering/README.md#security-requirements) and [Security Testing](../topics/ch09-security-engineering/README.md#security-testing)
  - Curated resources: [security requirements resources](../topics/ch09-security-engineering/resources.md#security-requirements) and [security testing resources](../topics/ch09-security-engineering/resources.md#security-testing)
  - Focus resource: [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/)
- Secure design and defaults
  - Topics: [Secure Design Patterns & Architectural Trade-Offs](../topics/ch09-security-engineering/README.md#secure-design) and [Hardening & Secure Defaults](../topics/ch09-security-engineering/README.md#hardening-defaults)
  - Curated resources: [secure design resources](../topics/ch09-security-engineering/resources.md#secure-design) and [hardening resources](../topics/ch09-security-engineering/resources.md#hardening-defaults)
  - Focus resources: [OWASP Secure Product Design Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Secure_Product_Design_Cheat_Sheet.html) and [MDN Practical Security Implementation Guides](https://developer.mozilla.org/en-US/docs/Web/Security/Practical_implementation_guides)
- Logging, incident response and remediation verification
  - Topics: [Application Logging & Detection](../topics/ch09-security-engineering/README.md#logging-detection) and [Incident Response & Remediation Verification](../topics/ch09-security-engineering/README.md#incident-remediation)
  - Curated resources: [logging resources](../topics/ch09-security-engineering/resources.md#logging-detection) and [incident/remediation resources](../topics/ch09-security-engineering/resources.md#incident-remediation)
- Dependencies and provenance
  - Topic: [Dependencies, SBOM, Signing & Provenance](../topics/ch07-cloud-supply-chain/README.md#dependencies-artifacts)
  - Curated resources: [dependency/provenance resources](../topics/ch07-cloud-supply-chain/resources.md#dependencies-artifacts)
  - Focus resources: [SLSA v1.1 — About SLSA](https://slsa.dev/spec/v1.1/about) and [OWASP Dependency-Track](https://owasp.org/www-project-dependency-track/)
- AI-enabled web applications and RAG security when relevant
  - Topics: [AI-Enabled Web Applications & Tool Permissions](../topics/ch08-emerging-practice/README.md#ai-web-security) and [RAG, Vector Stores & Data Isolation](../topics/ch08-emerging-practice/README.md#rag-isolation)
  - Curated resources: [AI web security resources](../topics/ch08-emerging-practice/resources.md#ai-web-security) and [RAG resources](../topics/ch08-emerging-practice/resources.md#rag-isolation)
  - Focus resources: [OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/) and [OWASP RAG Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/RAG_Security_Cheat_Sheet.html)

### Completion signals

You can choose controls based on system design, verify implementation, monitor for failures, and produce a remediation plan that includes code, configuration, tests, and operational checks.
