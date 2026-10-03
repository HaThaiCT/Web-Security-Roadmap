<!-- GENERATED FILE: do not edit by hand. Run scripts/generate.py. -->
# Curated Resources — API, Framework & Application Ecosystem Security

<a id="rest-openapi"></a>
## REST

### Core

- **[Cross-Origin Resource Sharing (CORS)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS)** — *documentation · intermediate · learner, tester, developer · free/public*  
  A clear reference for how browsers use CORS headers to permit selected cross-origin reads. It covers simple and preflighted requests, credentialed requests, wildcard limits and preflight caching, making it a practical baseline before testing or configuring APIs consumed from browsers.
- **[OWASP API Security Top 10 2023](https://api-security.owasp.org/editions/2023/en/0x11-t10)** — *documentation · beginner · learner, tester, developer · free/public*  
  A high-level risk map for API work. It is not a control guide by itself, but it helps learners and teams orient around object-level authorization, authentication, property-level authorization, resource consumption, function-level authorization, sensitive business flows, SSRF, misconfiguration, inventory and unsafe third-party API consumption.
- **[REST Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html)** — *cheatsheet · intermediate · tester, developer · free/public*  
  A practical checklist for REST services covering HTTPS, authentication, local authorization, JWT validation, API keys, input/content-type validation, status codes, CORS, rate limiting and audit logging. It is a good bridge from general web vulnerabilities to API-specific implementation and review work.
- **[Server Side Request Forgery Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  A practical defensive baseline for SSRF and URL-processing risk. It separates allowlisted internal destinations from open external fetch features, explains why deny-lists and parser assumptions are fragile, and connects application validation to network-layer egress controls and cloud metadata protection.
- **[Stripe Webhook Signatures & Security](https://stripe.com/docs/webhooks)** — *documentation · intermediate · learner, tester, developer · free/public*  
  An industry-standard implementation guide for securing incoming webhook endpoints. It details cryptographic HMAC signature verification (Stripe-Signature header) computed over the unparsed raw request payload, replay attack defense using signed timestamps and tolerance windows, constant-time comparison to prevent timing leaks, and idempotency to safely process duplicate events.
- **[gRPC Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/gRPC_Security_Cheat_Sheet.html)** — *cheatsheet · intermediate · tester, developer · free/public*  
  A practical security guide for gRPC microservices and APIs. It details transport security requirements including mutual TLS (mTLS), token and metadata authentication via interceptors, message-level authorization, Protocol Buffer validation boundaries (clarifying that Protobuf enforces types but not business invariants), message size limits, and disabling server reflection in production.

<a id="graphql"></a>
## GraphQL Security

### Core

- **[GraphQL Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/GraphQL_Cheat_Sheet.html)** — *cheatsheet · intermediate · tester, developer · free/public*  
  A GraphQL-specific security baseline covering schema-driven validation, query depth/amount limits, batching abuse, authorization on edges and nodes, introspection controls and error handling. It is useful because GraphQL concentrates many API risks into fewer network requests and resolver paths.
- **[OWASP API Security Top 10 2023](https://api-security.owasp.org/editions/2023/en/0x11-t10)** — *documentation · beginner · learner, tester, developer · free/public*  
  A high-level risk map for API work. It is not a control guide by itself, but it helps learners and teams orient around object-level authorization, authentication, property-level authorization, resource consumption, function-level authorization, sensitive business flows, SSRF, misconfiguration, inventory and unsafe third-party API consumption.
- **[Web Security Academy](https://portswigger.net/web-security)** — *lab · beginner · learner, tester, developer · free/registration-required*  
  A broad, free training platform with guided material and realistic labs across major web vulnerability classes, APIs, identity flaws, protocol issues and newer areas such as LLM/AI attacks. It is useful for learners and authorized testers because practice happens in a safe and legal lab environment rather than on real targets. Some exercises require Burp Suite; the Community Edition is sufficient for many labs, but the account and tooling expectations should be checked per lab.

<a id="grpc-soap"></a>
## gRPC

### Core

- **[Microservices Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Microservices_Security_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  An architectural guide for securing distributed microservices, message queues, and event-driven integrations. It evaluates edge API gateway authorization patterns, analyzes service-to-service mutual TLS (mTLS) and token authentication, details decentralized versus embedded Policy Decision Points (PDP), and covers secure asynchronous logging via message brokers.
- **[XML Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/XML_Security_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  An authoritative reference for secure XML parsing, document processing, and schema validation. It details parser configurations that disable Document Type Definitions (DTDs), mitigates entity expansion attacks (Billion Laughs exponential expansion and quadratic blowup), and defines strict schema validation rules using bounded enumerations and length constraints.
- **[gRPC Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/gRPC_Security_Cheat_Sheet.html)** — *cheatsheet · intermediate · tester, developer · free/public*  
  A practical security guide for gRPC microservices and APIs. It details transport security requirements including mutual TLS (mTLS), token and metadata authentication via interceptors, message-level authorization, Protocol Buffer validation boundaries (clarifying that Protobuf enforces types but not business invariants), message size limits, and disabling server reflection in production.

<a id="frontend-bff"></a>
## SPA

### Core

- **[Rendering on the Web](https://web.dev/articles/rendering-on-the-web)** — *article · intermediate · learner, tester, developer · free/public*  
  A practical comparison of server-side rendering, client-side rendering, static rendering, streaming and hydration trade-offs. It helps readers understand how modern rendering choices affect where code runs, where data appears, when browser JavaScript becomes authoritative and why frontend architecture matters for security review.
- **[Web Frontend Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Web_Frontend_Security_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  A focused security guide for modern frontend architectures, Single Page Applications (SPA), and asynchronous browser-backend communication. It establishes a zero-trust mindset for all data flowing between client and server, covers safe DOM rendering (preventing innerHTML XSS sinks), secure state management in memory vs. storage, and architectural patterns for decoupling API tokens from frontend clients via Backend-for-Frontend (BFF) layers.

<a id="framework-security"></a>
## Runtime

### Core

- **[Nodejs Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Nodejs_Security_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  A practical reference for securing Node.js runtime environments, web frameworks, and server architectures. It details asynchronous control-flow pitfalls (pyramid of doom, unhandled promise rejections crashing the event loop), error handling without sensitive stack trace leakage, blocking the single-threaded event loop (ReDoS, heavy crypto), and process hardening.
- **[Prototype Pollution](https://portswigger.net/web-security/prototype-pollution)** — *documentation · intermediate · learner, tester, developer · free/public*  
  A comprehensive resource on JavaScript prototype pollution covering both client-side and server-side exploit mechanics. It explains how polluting Object.prototype via recursive merge or property assignment injects properties across the runtime, escalating to DOM XSS via client gadgets or remote code execution via Node.js child process child_process.fork options.

<a id="backend-integrations"></a>
## Databases

### Core

- **[Database Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Database_Security_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  An architectural guide for securing backend database instances in web applications. It details database isolation on dedicated network segments, least-privilege application accounts (limiting permissions to SELECT/INSERT/UPDATE rather than administrative superusers), host-based access controls, and mandating TLS 1.2+ encryption in transit between application servers and database instances.
- **[Redis Security Model and Guidelines](https://redis.io/docs/latest/operate/oss_and_stack/management/security/)** — *documentation · intermediate · tester, developer · free/public*  
  The official architectural guide to Redis's security model, access control, and network isolation. It explains that Redis is designed for trusted internal network access, detailing the severe risks of internet-exposed instances (unauthenticated data deletion via FLUSHALL, unauthorized key access), protected mode mechanics, configuring strict bind interfaces, and deploying Role-Based Access Control (ACLs) to enforce least-privilege operations between web backends, caches, and queues.

<a id="webhooks-saas"></a>
## Webhooks & SaaS Integrations

### Core

- **[Stripe Webhook Signatures & Security](https://stripe.com/docs/webhooks)** — *documentation · intermediate · learner, tester, developer · free/public*  
  An industry-standard implementation guide for securing incoming webhook endpoints. It details cryptographic HMAC signature verification (Stripe-Signature header) computed over the unparsed raw request payload, replay attack defense using signed timestamps and tolerance windows, constant-time comparison to prevent timing leaks, and idempotency to safely process duplicate events.
- **[Third Party Payment Gateway Integration Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Third_Party_Payment_Gateway_Integration_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  A comprehensive security baseline for integrating third-party payment gateways. It covers PCI-DSS scope reduction through client-side tokenization and hosted fields, mandates server-side validation of transaction amounts and currency codes, details cryptographic verification of asynchronous gateway callbacks, and enforces state machine integrity to prevent payment status tampering.

<a id="payments-workflows"></a>
## Payment

### Core

- **[Business Logic Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Business_Logic_Security_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  A practical guide for preventing business logic flaws and workflow subversion. It details strategies for enforcing application domain invariants, validating multi-step state transitions, maintaining integrity across transactional operations (e.g. pricing, coupons, quantity limits), and designing state machines that resist parameter manipulation and sequence bypasses.
- **[Stripe Webhook Signatures & Security](https://stripe.com/docs/webhooks)** — *documentation · intermediate · learner, tester, developer · free/public*  
  An industry-standard implementation guide for securing incoming webhook endpoints. It details cryptographic HMAC signature verification (Stripe-Signature header) computed over the unparsed raw request payload, replay attack defense using signed timestamps and tolerance windows, constant-time comparison to prevent timing leaks, and idempotency to safely process duplicate events.
- **[Third Party Payment Gateway Integration Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Third_Party_Payment_Gateway_Integration_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  A comprehensive security baseline for integrating third-party payment gateways. It covers PCI-DSS scope reduction through client-side tokenization and hosted fields, mandates server-side validation of transaction amounts and currency codes, details cryptographic verification of asynchronous gateway callbacks, and enforces state machine integrity to prevent payment status tampering.
