# Learning Path — Authorized Tester / Researcher

This path is for people testing systems they are explicitly authorized to assess. It uses realistic sources, write-ups, public PoCs, and reports as learning material, but this repository does not run code or provide live-target operations.

Use topic pages to understand the mechanism, curated resources for reviewed references, and labs or owned targets for practice. Keep written scope, rate limits, data-handling rules, and evidence expectations visible before testing.

## Foundation refresh

Skip what you already know, but verify gaps through these anchors:

- HTTP and browser state: [HTTP](../topics/ch01-foundations/README.md#http), [origins/cookies](../topics/ch01-foundations/README.md#origins-cookies), and [their curated resources](../topics/ch01-foundations/resources.md#origins-cookies).
- Request lifecycle and application layers: [Request Lifecycle & Application Layers](../topics/ch02-web-architecture/README.md#request-lifecycle) and [Proxies, Caches & Distributed Components](../topics/ch02-web-architecture/README.md#distributed-components) with [HTTP caching resources](../topics/ch02-web-architecture/resources.md#distributed-components).
- Identity and authorization models: [Sessions](../topics/ch03-identity/README.md#sessions), [Authorization/IDOR](../topics/ch03-identity/README.md#authorization-idor), and [OAuth/OIDC](../topics/ch03-identity/README.md#oauth-oidc).
- API and data surfaces: [REST/API](../topics/ch06-api-frameworks/README.md#rest-openapi), [GraphQL](../topics/ch06-api-frameworks/README.md#graphql), [SQL/NoSQL](../topics/ch04-vulnerabilities/README.md#sql-nosql), and [storage/secrets](../topics/ch07-cloud-supply-chain/README.md#storage-secrets).

## Beginner

### Goal

Learn to test safely, collect evidence, and separate real issues from false positives.

### Study route

1. Testing method and evidence first
   - Topics: [Authorized Testing Methodology](../topics/ch08-emerging-practice/README.md#testing-methodology), [Evidence](../topics/ch08-emerging-practice/README.md#evidence), and [Labs](../topics/ch08-emerging-practice/README.md#practice-labs)
   - Curated resources: [testing methodology resources](../topics/ch08-emerging-practice/resources.md#testing-methodology), [evidence resources](../topics/ch08-emerging-practice/resources.md#evidence), and [lab resources](../topics/ch08-emerging-practice/resources.md#practice-labs)
   - Focus resources: [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/) and [PortSwigger Web Security Academy](https://portswigger.net/web-security)
2. Session and cookie review
   - Topic: [Session & Cookie Security](../topics/ch03-identity/README.md#sessions)
   - Curated resources: [session resources](../topics/ch03-identity/resources.md#sessions)
   - Focus resources: [OWASP Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html) and [MDN — Set-Cookie header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie)
3. Access control, IDOR and BOLA
   - Topic: [Access Control, IDOR & BOLA](../topics/ch03-identity/README.md#authorization-idor)
   - Curated resources: [authorization/IDOR resources](../topics/ch03-identity/resources.md#authorization-idor)
   - Focus resources: [OWASP Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) and [OWASP IDOR Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Insecure_Direct_Object_Reference_Prevention_Cheat_Sheet.html)
4. First high-signal vulnerability classes
   - Topics: [XSS](../topics/ch05-browser-protocols/README.md#xss), [SQL/NoSQL Injection](../topics/ch04-vulnerabilities/README.md#sql-nosql), [CSRF](../topics/ch05-browser-protocols/README.md#csrf), and [CORS](../topics/ch05-browser-protocols/README.md#cors)
   - Curated resources: [XSS resources](../topics/ch05-browser-protocols/resources.md#xss), [SQL/NoSQL resources](../topics/ch04-vulnerabilities/resources.md#sql-nosql), [CSRF resources](../topics/ch05-browser-protocols/resources.md#csrf), and [CORS resources](../topics/ch05-browser-protocols/resources.md#cors)

### Practice

Use hosted labs, CTFs, and owned local targets. Keep notes that include scope, prerequisites, test accounts, request/response evidence, impact, affected objects, and remediation. Avoid destructive operations, data exfiltration, broad brute force, heavy fuzzing, or touching real users' data unless the written scope explicitly permits it.

### Completion signals

You can reproduce a lab issue, explain authorization boundaries, show impact with minimal safe evidence, and write a clear report without overstating severity.

## Intermediate

### Goal

Test realistic application surfaces and reason about chains without treating every source as directly applicable.

### Study route

- Identity protocols and tokens
  - Topics: [JWT & Token Validation](../topics/ch03-identity/README.md#jwt) and [OAuth & OpenID Connect](../topics/ch03-identity/README.md#oauth-oidc)
  - Curated resources: [JWT resources](../topics/ch03-identity/resources.md#jwt) and [OAuth/OIDC resources](../topics/ch03-identity/resources.md#oauth-oidc)
  - Focus resource: [OWASP OAuth2 Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/OAuth2_Cheat_Sheet.html)
- API assessment
  - Topics: [REST, OpenAPI & API Inventory](../topics/ch06-api-frameworks/README.md#rest-openapi) and [GraphQL Security](../topics/ch06-api-frameworks/README.md#graphql)
  - Curated resources: [REST/API resources](../topics/ch06-api-frameworks/resources.md#rest-openapi) and [GraphQL resources](../topics/ch06-api-frameworks/resources.md#graphql)
  - Focus resources: [OWASP API Security Top 10 2023](https://api-security.owasp.org/editions/2023/en/0x11-t10), [OWASP REST Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html), and [OWASP GraphQL Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/GraphQL_Cheat_Sheet.html)
- Business logic and workflow integrity
  - Topic: [Business Logic & Workflow Integrity](../topics/ch04-vulnerabilities/README.md#business-logic)
  - Curated resources: [Business logic resources](../topics/ch04-vulnerabilities/resources.md#business-logic)
  - Focus resource: [OWASP Business Logic Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Business_Logic_Security_Cheat_Sheet.html)
- Webhooks and SaaS integrations
  - Topic: [Webhooks & SaaS Integrations](../topics/ch06-api-frameworks/README.md#webhooks-saas)
  - Curated resources: [Webhook resources](../topics/ch06-api-frameworks/resources.md#webhooks-saas)
  - Focus resource: [Stripe — Webhook Signatures & Security](https://stripe.com/docs/webhooks)
- Server-side and workflow assessment
  - Topics: [SSRF & URL Processing](../topics/ch04-vulnerabilities/README.md#ssrf), [File Upload & Document Processing](../topics/ch04-vulnerabilities/README.md#upload-documents), and [Race Conditions](../topics/ch04-vulnerabilities/README.md#race-conditions)
  - Curated resources: [SSRF resources](../topics/ch04-vulnerabilities/resources.md#ssrf), [File upload resources](../topics/ch04-vulnerabilities/resources.md#upload-documents), and [Race conditions resources](../topics/ch04-vulnerabilities/resources.md#race-conditions)
  - Focus resources: [PortSwigger — Server-Side Request Forgery](https://portswigger.net/web-security/ssrf), [OWASP File Upload Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html), and [PortSwigger — Race Conditions](https://portswigger.net/web-security/race-conditions)
- Protocol and cache behavior
  - Topics: [HTTP Request Smuggling](../topics/ch05-browser-protocols/README.md#http-smuggling), [Cache Poisoning & Cache Deception](../topics/ch05-browser-protocols/README.md#web-caching), and [DNS Rebinding](../topics/ch05-browser-protocols/README.md#dns-rebinding)
  - Curated resource hub: [Web Security Academy](../topics/ch08-emerging-practice/resources.md#practice-labs) and [Singularity of Origin — DNS Rebinding](https://github.com/nccgroup/singularity)

### Practice

Read real write-ups and public PoCs for mechanism, assumptions, evidence style, and remediation clues. Do not execute code from unknown repositories. Rebuild understanding in labs or owned systems only, and write a scoped test plan before touching an application.

### Completion signals

You can identify assumptions a write-up depends on, explain why the same technique may fail elsewhere, and produce a scoped test plan before touching an application.

## Advanced

### Goal

Specialize in a surface and connect findings to system-level fixes.

### Specializations

- Identity and enterprise SSO: [Authentication](../topics/ch03-identity/README.md#passwords-recovery), [Sessions](../topics/ch03-identity/README.md#sessions), [OAuth/OIDC](../topics/ch03-identity/README.md#oauth-oidc), [SAML](../topics/ch03-identity/README.md#saml-scim)
- Browser/client and protocol behavior: [XSS](../topics/ch05-browser-protocols/README.md#xss), [CSP](../topics/ch05-browser-protocols/README.md#csp-clickjacking), [postMessage](../topics/ch05-browser-protocols/README.md#postmessage-dom), [HTTP smuggling](../topics/ch05-browser-protocols/README.md#http-smuggling), [web caching](../topics/ch05-browser-protocols/README.md#web-caching), and [XS-Leaks & Web Side Channels](../topics/ch08-emerging-practice/README.md#side-channels)
- API and business logic: [REST/API](../topics/ch06-api-frameworks/README.md#rest-openapi), [GraphQL](../topics/ch06-api-frameworks/README.md#graphql), [gRPC & RPC](../topics/ch06-api-frameworks/README.md#grpc-soap), [Business Logic](../topics/ch04-vulnerabilities/README.md#business-logic), [Race Conditions](../topics/ch04-vulnerabilities/README.md#race-conditions), and [Payment Workflows](../topics/ch06-api-frameworks/README.md#payments-workflows)
- Cloud-backed web apps: [Cloud IAM](../topics/ch07-cloud-supply-chain/README.md#cloud-iam), [Object Storage & Secrets](../topics/ch07-cloud-supply-chain/README.md#storage-secrets), [Metadata Services & Serverless](../topics/ch07-cloud-supply-chain/README.md#metadata-serverless) (with [IMDSv2 guidance](../topics/ch07-cloud-supply-chain/resources.md#metadata-serverless)), [Containers & Kubernetes](../topics/ch07-cloud-supply-chain/README.md#containers-kubernetes)
- CI/CD and supply chain: [CI/CD Security](../topics/ch07-cloud-supply-chain/README.md#cicd-security), [Dependencies, SBOM, Signing & Provenance](../topics/ch07-cloud-supply-chain/README.md#dependencies-artifacts)
- AI-enabled web apps and tool permissions: [AI-Enabled Web Applications & Tool Permissions](../topics/ch08-emerging-practice/README.md#ai-web-security), [RAG](../topics/ch08-emerging-practice/README.md#rag-isolation), and [abuse resilience](../topics/ch08-emerging-practice/README.md#abuse-resilience)

### Completion signals

You can turn a realistic case study into a bounded methodology, identify false-positive traps, document evidence precisely, and recommend remediation that addresses root cause rather than symptom.
