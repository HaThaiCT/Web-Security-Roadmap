# Chapter 6 — API, Framework & Application Ecosystem Security Findings

## 2026-10-03 status

No Chapter 6 resource has been promoted in the first curated batch.

Related evidence gathered so far:

- PortSwigger Web Security Academy was promoted under Chapter 8 as a lab/training hub and lists API testing, GraphQL and WebSockets among its topics.

Gaps:

- Need inspected sources for REST/OpenAPI/API inventory, GraphQL, gRPC/SOAP/RPC, SPA/SSR/BFF security, framework/CMS security, backend integrations, webhooks/SaaS integrations and payment/checkout/subscription workflows.

## 2026-10-03 batch

### OWASP — REST Security Cheat Sheet

- URL: <https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html>
- Method: WebFetch public page reading.
- Verification scope: relevant English REST security sections inspected; no API requests sent.
- Promoted resource: `owasp-rest-security-cheat-sheet` in `data/resources/ch06-api-frameworks.yml`.

Useful observations:

- REST services should expose HTTPS-only endpoints and enforce local access control on every non-public endpoint.
- JWT consumers must reject unsigned tokens, avoid trusting the token header for algorithm selection, and validate `iss`, `aud`, `exp` and `nbf`.
- API keys are useful for identification and rate limiting but should not be the sole protection for sensitive resources.
- Input validation should check length, range, format and type; oversized payloads should be rejected and repeated failures logged.
- Content-Type handling, status codes, CORS, rate limiting, security headers and audit logging are all covered as API review concerns.

### OWASP — GraphQL Cheat Sheet

- URL: <https://cheatsheetseries.owasp.org/cheatsheets/GraphQL_Cheat_Sheet.html>
- Method: WebFetch public page reading.
- Verification scope: relevant English GraphQL security sections inspected; no API requests sent.
- Promoted resource: `owasp-graphql-cheat-sheet` in `data/resources/ch06-api-frameworks.yml`.

Useful observations:

- GraphQL-native types, mutation input schemas and allowlists help constrain input before it reaches downstream interpreters.
- GraphQL does not natively limit query depth or object counts, so applications need explicit depth, amount, timeout, cost and rate controls.
- Batching can make brute force or object enumeration appear as one network request, bypassing ordinary WAF or rate-limit assumptions.
- Authorization must be enforced on every request, including edges and nodes; `node`/`nodes` fields can expose object access paths by ID.
- Production deployments should disable introspection/GraphiQL where appropriate and avoid exposing stack traces or schema hints through errors.

### OWASP API Security Top 10 2023

- URL: <https://api-security.owasp.org/editions/2023/en/0x11-t10>
- Method: WebFetch public page reading.
- Verification scope: published OWASP API Security Top 10 2023 table inspected; no API testing performed.
- Promoted resource: `owasp-api-security-top-10-2023` in `data/resources/ch06-api-frameworks.yml`.

Useful observations:

- The 2023 list includes Broken Object Level Authorization, Broken Authentication, Broken Object Property Level Authorization, Unrestricted Resource Consumption, Broken Function Level Authorization, Unrestricted Access to Sensitive Business Flows, SSRF, Security Misconfiguration, Improper Inventory Management and Unsafe Consumption of APIs.
- The list is best used as a risk map, not as a full control guide. It points readers toward API-specific failure modes that then need deeper resources.
- API3 consolidates earlier excessive data exposure and mass assignment concerns, which fits this repository's preference for root-cause organization.

### Stripe — Webhook Signatures & Security

- URL: <https://stripe.com/docs/webhooks>
- Method: WebFetch public documentation inspection.
- Verification scope: relevant English webhook signature verification documentation inspected; no live webhooks triggered.
- Promoted resource: `stripe-webhook-security-guide` in `data/resources/ch06-api-frameworks.yml`.

Useful observations:

- Documents cryptographic HMAC-SHA256 signature verification over incoming webhook requests to prevent forged event injection.
- Emphasizes computing the signature over the raw, unparsed request payload bytes: parsing JSON before verification can alter whitespace, key ordering, or Unicode escaping, causing signature mismatches.
- Details replay attack defenses: the `Stripe-Signature` header includes a timestamp parameter (`t=...`) that is included in the signed payload. Consumers must verify that the timestamp falls within an acceptable tolerance window (e.g. within 5 minutes of server time).
- Requires constant-time string comparison algorithms to prevent timing attack side channels during HMAC verification.
- Enforces idempotent event handling: network retries and webhook delivery guarantees mean consumers may receive identical event payloads multiple times; applications must track event IDs and ensure processing logic is strictly idempotent.

### OWASP — Third Party Payment Gateway Integration Cheat Sheet

- URL: <https://cheatsheetseries.owasp.org/cheatsheets/Third_Party_Payment_Gateway_Integration_Cheat_Sheet.html>
- Method: WebFetch public page reading.
- Verification scope: relevant English payment gateway integration guidance inspected; no financial transactions processed.
- Promoted resource: `owasp-payment-gateway-integration-cheat-sheet` in `data/resources/ch06-api-frameworks.yml`.

Useful observations:

- Focuses on securing e-commerce and checkout integrations while reducing PCI-DSS regulatory scope.
- Recommends client-side tokenization (hosted iframes, payment fields) so primary cardholder data (PAN, CVV) bypasses merchant application servers entirely.
- Prohibits trusting client-submitted prices, discounts, or transaction amounts: transaction initialization must calculate amounts server-side and bind them to a cryptographic payment session.
- Outlines risks in asynchronous transaction confirmation: attackers can tamper with browser redirect return URLs; the merchant system must verify transaction success exclusively via cryptographically signed server-to-server webhook callbacks.
- Enforces strict state machine handling: handle pending, authorized, captured, refunded, and failed transaction states defensively, preventing race conditions or double-fulfillment.

### OWASP — gRPC Security Cheat Sheet

- URL: <https://cheatsheetseries.owasp.org/cheatsheets/gRPC_Security_Cheat_Sheet.html>
- Method: WebFetch public page reading.
- Verification scope: relevant English gRPC security guidance inspected; no RPC calls executed.
- Promoted resource: `owasp-grpc-security-cheat-sheet` in `data/resources/ch06-api-frameworks.yml`.

Useful observations:

- Addresses security mechanisms unique to HTTP/2-based gRPC services and Protocol Buffers.
- Transport security: Mandates TLS encryption in production and recommends mutual TLS (mTLS) for zero-trust microservice-to-microservice authentication.
- Authentication & authorization: Interceptors should validate JWT bearer tokens or API keys passed via gRPC metadata headers, enforcing method-level RBAC.
- Input validation: Clarifies that while Protocol Buffers enforce data types, they do not validate business logic, range, or content constraints; application-level validation remains essential.
- Resource controls: Mandates max incoming message size limits and request timeouts to prevent memory exhaustion and DoS.
- Service discovery: Recommends disabling gRPC Server Reflection in production environments to prevent unauthorized schema discovery and reconnaissance.

Limits and follow-up:

- Need OpenAPI inventory guidance, framework-specific API security docs, SPA/SSR/BFF security architectures, and backend message queue security.

