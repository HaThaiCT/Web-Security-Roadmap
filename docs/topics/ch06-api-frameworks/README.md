# API, Framework & Application Ecosystem Security

This authored overview is organized by topic. Curated resource lists are generated separately in [resources.md](resources.md).

## How to use this part

Use this as a reference section, not as a mandatory linear course. Learning paths link to the topics and resources that fit each role.

<a id="rest-openapi"></a>
## REST, OpenAPI & API Inventory

### Prerequisites

Understand HTTP methods/status codes, authentication, authorization and JSON request/response handling. For production systems, know where API routes are registered and whether OpenAPI or another inventory exists.

### Mechanism and mental model

APIs expose application decisions in compact, automatable surfaces. Security depends on consistent authentication, object/function/property-level authorization, input and content-type validation, rate limits, clear status behavior, inventory and logging. API risks often cluster around missing object-level checks, overexposed properties, undocumented endpoints, unsafe third-party consumption and business-flow automation.

A REST endpoint is not safe because it is “internal” or because the frontend normally hides it. Every non-public API operation needs server-side access control and validation at the endpoint and resource layer.

### Practical learning notes

Start with an API inventory: endpoints, methods, auth requirements, objects, roles, tenants, rate limits and clients. In authorized testing, verify expected denials before trying edge cases. Do not brute-force, fuzz heavily or enumerate production APIs unless scope explicitly allows it.

### Defensive and engineering notes

Require HTTPS, centralize identity, enforce local authorization per endpoint, validate JWT claims and token audience, reject unexpected content types, use strong schema validation, avoid tokens in URLs, rate-limit sensitive flows, log security events and keep OpenAPI or equivalent documentation current. Treat API keys as identifiers/rate-limit handles, not as sufficient protection for high-value resources.

### Reading order

1. Read [OWASP REST Security Cheat Sheet](resources.md#rest-openapi) for implementation controls.
2. Read [OWASP API Security Top 10 2023](resources.md#rest-openapi) as a risk map.
3. Then branch to authorization/IDOR, GraphQL, SSRF, business logic and inventory practices.

<a id="graphql"></a>
## GraphQL Security

### Prerequisites

Understand API authorization, schemas, resolvers and basic query/mutation structure. You should also understand object-level authorization because GraphQL often exposes flexible object traversal paths.

### Mechanism and mental model

GraphQL lets clients choose response shape and traverse related data. That flexibility changes where risk appears: nested queries can be expensive, batching can hide many operations inside one request, resolver paths can bypass assumptions made for REST endpoints, and introspection or error messages can expose useful schema information.

The key model is resolver-by-resolver trust. Every node, edge, field and mutation that returns or modifies data needs authorization and validation appropriate to the current user and object.

### Practical learning notes

In labs or authorized systems, inspect the schema, mutations, object IDs, batching behavior, introspection, error output and query depth/cost controls. Avoid high-cost queries against production unless explicitly allowed; GraphQL DoS and resource consumption issues can be easy to trigger accidentally.

### Defensive and engineering notes

Use schema types and input schemas, validate downstream interpreter inputs, enforce authorization in resolvers, limit depth/amount/cost, consider object request rate limits for batching, disable GraphiQL/introspection in production where appropriate, mask errors and log internally. Watch `node`/`nodes` patterns for ID-based object access.

### Reading order

1. Read [OWASP GraphQL Cheat Sheet](resources.md#graphql).
2. Pair with authorization/IDOR and API Security Top 10 resources.
3. Add framework-specific GraphQL server guidance in later curation.

<a id="grpc-soap"></a>
## gRPC, SOAP & RPC Security

### Prerequisites

Understand Remote Procedure Call (RPC) architectures, HTTP/2 binary framing and multiplexing, Protocol Buffers (Protobuf) schema definitions (`.proto`), XML/SOAP envelope structures, and microservice service-to-service communication.

### Mechanism and mental model

Modern distributed web backends frequently use RPC protocols—primarily **gRPC** (over HTTP/2 with Protocol Buffers) and legacy **SOAP** (over HTTP with XML envelopes)—for high-throughput internal service-to-service communication and external APIs:
- **gRPC Security Foundations:**
  - *Transport & Mutual TLS:* gRPC relies on HTTP/2. Production deployments mandate TLS, and internal microservices should use mutual TLS (mTLS) to authenticate both client and server, establishing a zero-trust network fabric.
  - *Authentication via Interceptors:* gRPC uses interceptors (middleware) to validate caller credentials passed in HTTP/2 metadata headers (e.g. `authorization: Bearer <jwt>`).
  - *Protobuf Validation Boundaries:* While Protocol Buffers enforce strict type checking and field serialization, **Protobuf does not enforce business validation**. An integer field will prevent string injection, but will happily accept negative balances, out-of-range IDs, or oversized byte buffers. Input validation rules must still be enforced explicitly in service logic.
  - *Server Reflection Risks:* gRPC Server Reflection allows clients to query the server for its complete schema and available RPC methods. If enabled in production, attackers using tools like `grpcurl` or Postman can map out internal methods, hidden administrative endpoints, and message schemas without access to `.proto` files.
  - *Resource Exhaustion:* Because HTTP/2 multiplexes multiple streams over a single TCP connection, unconstrained message sizes or unhandled infinite streams can exhaust server CPU and memory.
- **SOAP / XML-RPC Security:**
  - SOAP architectures rely on extensive XML parsing, making them prime targets for XML External Entity (XXE) injection, XML entity expansion (Billion Laughs DoS), and XML Signature Wrapping (XSW) attacks.
  - WSDL service definitions exposed publicly reveal internal service surfaces and method parameters.

### Practical learning notes

In authorized audits and service reviews:
- Test whether gRPC Server Reflection is enabled in production by running `grpcurl -plaintext <host>:<port> list` or `grpcurl <host>:<port> describe`.
- Inspect gRPC interceptors to confirm that authorization checks are enforced across all methods, not just initial handshake calls.
- In SOAP environments, check whether the XML parser disables external entity resolution (`disallow-doctype-decl`) and enforces schema validation.

### Defensive and engineering notes

1. **Mandate TLS & mTLS:** Enforce TLS encryption for all external gRPC endpoints and mutual TLS (mTLS) with client certificate verification for inter-service communication.
2. **Disable Reflection in Production:** Ensure `reflection.Register(grpcServer)` is strictly disabled in production builds to prevent unauthorized attack surface discovery.
3. **Explicit Application Validation:** Do not rely on Protobuf types for security. Use validation libraries (such as `protoc-gen-validate` / `buf validate`) to enforce length, regex, range, and format constraints on message fields.
4. **Enforce Rate Limits & Message Caps:** Configure strict message size limits (`MaxRecvMsgSize`, `MaxSendMsgSize`, typically 4MB or smaller) and enforce per-client rate limits and call timeouts.
5. **Harden XML/SOAP Parsers:** Completely disable DTD processing and external entity resolution in all SOAP endpoints to prevent XXE.

### Reading order

1. Read [OWASP — gRPC Security Cheat Sheet](resources.md#grpc-soap).
2. Cross-reference with Chapter 4 XML External Entities (XXE) and Chapter 6 REST API Security.

<a id="frontend-bff"></a>
## Single Page Applications, Server-Side Rendering & Backend-for-Frontend (BFF) Security

### Prerequisites

Understand client-side JavaScript frameworks (React, Vue, Angular, Svelte), Server-Side Rendering (SSR) frameworks (Next.js, Nuxt, Remix), client-server communication protocols (REST, GraphQL), and browser storage vs. cookie authentication mechanisms.

### Mechanism and mental model

Modern web architectures have shifted significant presentation and state-management logic into frontend clients. This architectural evolution introduces distinct security considerations across SPAs, SSR, and Backend-for-Frontend (BFF) design patterns:
1. **The SPA Token Storage Conundrum:**
   - In pure Single Page Applications (SPAs) connecting directly to resource APIs, storing access tokens (JWTs) in `localStorage` or `sessionStorage` exposes credentials to full theft via any Cross-Site Scripting (XSS) vulnerability on the origin.
   - Conversely, storing tokens in in-memory JavaScript variables leaves apps unable to persist authentication across page refreshes without re-authenticating.
2. **The Backend-for-Frontend (BFF) Architectural Pattern:**
   - The industry-standard solution to the SPA token dilemma is the Backend-for-Frontend (BFF) pattern. A lightweight, dedicated server-side intermediate layer (often running Node.js, Go, or Python) sits between the browser frontend and backend microservices.
   - The BFF handles authentication handshakes, receives sensitive access and refresh tokens, and stores them securely in server-side session stores.
   - Between the browser and the BFF, authentication is maintained purely via encrypted, `HttpOnly`, `Secure`, `SameSite=Strict` session cookies with `__Host-` prefixes.
   - When the SPA requests data, the BFF receives the cookie, validates the session, attaches the actual bearer token to downstream requests, and returns only the filtered response data. The browser frontend never has access to raw OAuth tokens, completely neutralizing token exfiltration via XSS.
3. **Server-Side Rendering (SSR) & Server Actions Hazards:**
   - Hybrid SSR frameworks (Next.js App Router, Remix) execute component rendering code on both the server and the client.
   - *Data Exposure:* Accidentally passing full database models or environment objects to client components serializes sensitive internal fields into the HTML hydration payload (`__NEXT_DATA__` or flight data).
   - *Server Actions Authorization:* Framework features that expose server functions to client invocations (React Server Actions) create hidden HTTP endpoints. Developers frequently assume these functions are private internal methods and fail to enforce authentication and authorization checks at the top of each action.

### Practical learning notes

When auditing frontend and BFF architectures:
- Inspect client-side network requests: verify whether the browser receives and stores raw JWT bearer tokens or uses HttpOnly session cookies to communicate with a BFF.
- Inspect page source and hydration state: examine embedded JSON blobs in the initial HTML for leaked internal database fields, user email lists, or API keys.
- Audit Server Actions: inspect network traffic to identify RPC endpoints generated by server actions and test whether unauthenticated or unauthorized users can invoke them directly.

### Defensive and engineering notes

1. **Deploy the BFF Pattern for SPAs:** Implement a dedicated Backend-for-Frontend layer to isolate raw API tokens and identity secrets away from client-side JavaScript execution.
2. **Filter SSR Hydration Payloads:** Strictly transform and sanitize database entities using Data Transfer Objects (DTOs) before passing them to server-rendered components.
3. **Treat Server Actions as Public Endpoints:** Enforce strict authentication, tenant validation, and authorization checks at the very beginning of every server action function.
4. **Enforce Safe DOM Rendering:** Prohibit direct assignment to `innerHTML`, `outerHTML`, or `v-html`. Use framework-native safe text interpolation and deploy Trusted Types.

### Reading order

1. Read [OWASP — Web Frontend Security Cheat Sheet](resources.md#frontend-bff) for client-side trust boundaries and DOM security baselines.
2. Connect with Chapter 2 Rendering Architectures and Chapter 3 Sessions & State Security.

<a id="framework-security"></a>
## Runtime, Web Framework & CMS Security

### Prerequisites

Understand server-side web application frameworks (Express, NestJS, Django, Spring Boot, Ruby on Rails, Laravel), runtime execution models (Node.js event loops, JVM, Python WSGI/ASGI), and Content Management Systems (WordPress, Drupal).

### Mechanism and mental model

Web applications are built on complex framework and runtime foundations. The security posture of an application is intimately bound to the security defaults, lifecycle abstractions, and runtime characteristics of its underlying framework:
1. **Runtime Event Loop & Asynchronous Hazards (Node.js):**
   - Runtimes like Node.js operate on a single-threaded event loop for handling requests. Executing computationally heavy tasks (cryptographic loops, complex regular expressions susceptible to ReDoS, synchronous file I/O) on the main thread blocks all incoming requests across all users, causing complete denial of service.
   - Unhandled Promise rejections or uncaught exceptions in asynchronous callbacks can crash the entire Node.js process, terminating active connections for all concurrent users unless managed by a process supervisor with graceful restart policies.
2. **Framework Magic & Implicit Behaviors:**
   - Web frameworks offer rapid development through convention-over-configuration features: auto-binding request bodies to models (mass assignment), dynamic route generation, auto-escaping templates, and built-in ORM query compilation.
   - Security flaws arise when developers misunderstand these abstractions—such as using raw query bypasses in ORMs, misunderstanding Spring Expression Language (SpEL) interpolation, or disabling framework CSRF middleware globally for ease of API testing.
3. **Content Management System (CMS) & Plugin Ecosystem Risks:**
   - Monolithic CMS platforms (WordPress) power a massive portion of the public web. While the core software is heavily audited, the primary attack surface stems from third-party plugins and themes that suffer from unvalidated SQL queries, arbitrary file uploads, and stored XSS flaws.
   - Outdated plugins and vulnerable administrative endpoints (`/wp-admin`, `/xmlrpc.php`) remain prime vectors for automated exploitation and web skimmer injection.

### Practical learning notes

In runtime assessments and framework audits:
- Audit framework configuration: check whether framework debug modes, development exception screens, or hot-reload middleware are accidentally enabled in production.
- Review asynchronous error handling: verify whether Promise chains have terminating `.catch()` blocks or global `unhandledRejection` handlers to prevent process crashes.
- Test for ReDoS vulnerabilities: audit regular expressions used for user input validation (emails, URLs) against catastrophic backtracking patterns.

### Defensive and engineering notes

1. **Keep Frameworks & Runtimes Patched:** Establish automated dependency updates (Dependabot, Renovate) and subscribe to security advisories for the application's runtime and framework.
2. **Never Block the Event Loop:** In single-threaded runtimes, offload CPU-intensive operations (image resizing, hashing, parsing) to worker threads, background queues, or native external microservices.
3. **Enforce Framework Security Defaults:** Rely on framework-provided security mechanisms (Django's CSRF and ORM, Spring Security's authorization filters, Rails' strong parameters) rather than implementing custom, ad-hoc security filters.
4. **Harden CMS Deployments:** Minimize third-party plugins, enforce automated auto-updates, disable file editing in the admin dashboard (`DISALLOW_FILE_EDIT`), and isolate administrative endpoints behind multi-factor authentication and IP allowlists.

### Reading order

1. Read [OWASP — Nodejs Security Cheat Sheet](resources.md#framework-security) for runtime best practices, asynchronous error management, and server hardening.
2. Connect with Chapter 2 Request Lifecycle and Chapter 9 Hardening & Secure Defaults.

<a id="backend-integrations"></a>
## Databases, Search Engines & Queue Integration Security

### Prerequisites

Understand backend data stores and infrastructure components (Redis, Memcached, Elasticsearch, RabbitMQ, Apache Kafka), inter-process network protocols, and the role of caches and message queues in distributed web applications.

### Mechanism and mental model

Web applications rely on a constellation of backend supporting services: in-memory key-value stores for caching and sessions (Redis, Memcached), full-text search clusters (Elasticsearch, OpenSearch), and message brokers for asynchronous task processing (RabbitMQ, Kafka). Because these systems were originally designed for internal, trusted data center networks, they present catastrophic risks if misconfigured or exposed:
1. **The Redis Security Model & The Peril of Public Exposure:**
   - Redis is designed to be accessed exclusively by trusted clients inside a secure, private network perimeter. It has historically had minimal authentication enabled by default and relies on simple plaintext commands over TCP port 6379.
   - If a Redis instance is accidentally exposed to the public Internet or reachable via SSRF, an unauthenticated attacker can issue arbitrary commands:
     - Execute `FLUSHALL` to delete the entire dataset instantly.
     - Dump sensitive session tokens, cached passwords, and user PII.
     - Write arbitrary files to the host filesystem (e.g. overwriting `authorized_keys` to gain SSH access, or writing a web shell into a webroot directory).
   - Redis **Protected Mode** (introduced in 3.2.0) binds only to loopback interfaces if no password is configured, but misconfigured Docker containers or manual configuration overrides frequently disable this safeguard.
2. **Search Engine Clusters (Elasticsearch / OpenSearch):**
   - Elasticsearch clusters expose REST APIs on port 9200. Unauthenticated exposure or SSRF against an Elasticsearch node allows attackers to query indices, dump entire customer databases, modify mappings, or exploit dynamic scripting capabilities.
3. **Message Brokers & Queue Injections:**
   - Brokers (RabbitMQ, Kafka) transport critical business events and background jobs. Lack of queue authentication or tenant-scoped topics allows malicious services to poison queue messages, execute unauthorized asynchronous actions, or trigger consumer denial-of-service.

### Practical learning notes

In infrastructure reviews and authorized penetration testing:
- Check for exposed backend services: scan internal and external network perimeters for open ports 6379 (Redis), 11211 (Memcached), 9200 (Elasticsearch), 5672/15672 (RabbitMQ), and 9092 (Kafka).
- Audit SSRF pivotability: evaluate whether an application SSRF flaw can reach internal cache or queue endpoints and submit raw protocol payloads (e.g. Redis protocol commands via HTTP or Gopher).
- Inspect database access control: verify whether Redis deployments use modern Role-Based Access Control (Redis ACLs) to restrict application accounts from executing administrative commands (`CONFIG`, `FLUSHALL`, `MODULE`).

### Defensive and engineering notes

1. **Strict Network Isolation:** Never expose Redis, Memcached, Elasticsearch, or message brokers to the public Internet. Bind instances strictly to private internal subnets or `127.0.0.1`.
2. **Enforce Strong Authentication & ACLs:** Enable authentication on all backend stores. In Redis 6.0+, configure fine-grained ACLs to restrict application users strictly to necessary keys and commands while disabling dangerous administrative commands (`FLUSHALL`, `FLUSHDB`, `CONFIG`, `KEYS`).
3. **Mandate TLS in Transit:** Require TLS encryption between application servers and backend data stores, especially across cloud VPC boundaries.
4. **Harden Against SSRF Protocol Injection:** Block non-HTTP schemes (gopher, dict) in application HTTP clients and prevent outbound connections from reaching internal backend ports.

### Reading order

1. Read [Redis — Redis Security Model and Guidelines](resources.md#backend-integrations) for network security, protected mode, and ACL deployment.
2. Connect with Chapter 2 Databases, ORMs & Data Storage and Chapter 4 SSRF & URL Processing.

<a id="webhooks-saas"></a>
## Webhooks & SaaS Integrations

### Prerequisites

Understand HTTP request handling, asynchronous event-driven architectures, symmetric cryptographic hashing (HMAC-SHA256), public webhook callback endpoints, and timing side-channel attacks.

### Mechanism and mental model

Webhooks reverse the typical client-server API flow: an external SaaS service (such as Stripe, GitHub, Shopify, or Twilio) acts as an HTTP client, sending asynchronous POST requests to an application's publicly exposed webhook listener endpoint to notify it of state changes (e.g. `payment_intent.succeeded`, `push`, `order.created`).

Because webhook listeners must be publicly accessible on the Internet to receive external events, they present an attractive target for attackers who seek to forge events, replay past transactions, or exhaust server resources.

Securing webhook endpoints requires four fundamental architectural mechanisms:
1. **Cryptographic HMAC Signature Verification:** The SaaS provider shares an out-of-band webhook signing secret with the consumer. For every event, the provider computes an HMAC-SHA256 hash over the payload and transmits it in a request header (e.g. `Stripe-Signature`, `X-Hub-Signature-256`). The receiver recalculates the HMAC using the shared secret and verifies that it matches.
2. **Raw Payload Verification (The Parsing Trap):** A critical implementation vulnerability occurs when developers parse incoming JSON request bodies *before* computing the HMAC. Modern JSON parsers often alter whitespace, reorder dictionary keys, normalize floating-point numbers, or transform Unicode escape sequences. If the HMAC is computed over the reserialized object rather than the exact raw byte stream received over the wire, signature validation will fail or be bypassable. Verification must always execute against the raw, unparsed request buffer.
3. **Replay Attack Defenses:** If an attacker intercepts a valid webhook request, replaying that identical request multiple times could trigger duplicate fulfillment or account credits. Webhook architectures counter this by including a signed timestamp parameter (`t=...`) inside the signature header. The consumer verifies that the timestamp is within an allowable tolerance window (typically 3 to 5 minutes) compared to current server clock time.
4. **Idempotency & Duplicate Handling:** Due to network timeouts and retries, providers guarantee *at-least-once* delivery, meaning consumers will inevitably receive duplicate webhook deliveries. Applications must record processed event identifiers (e.g. `event.id`) and make downstream processing strictly idempotent.

### Practical learning notes

In code reviews and authorized testing:
- Verify how the application captures the incoming request body: Is body-parser middleware configured to preserve raw bytes (e.g. `express.raw({type: 'application/json'})`)?
- Check signature comparison logic: Is the signature validated using a constant-time comparison function (such as `crypto.timingSafeEqual`) to prevent byte-by-byte timing side channels?
- Test replay resilience: What happens if an identical webhook request is sent again 10 minutes later?

### Defensive and engineering notes

1. **Verify Raw Byte Buffers:** Always compute the HMAC-SHA256 signature against the raw, unparsed request payload buffer before any JSON deserialization occurs.
2. **Enforce Timestamp Windows:** Reject any webhook whose signed timestamp differs from server time by more than 5 minutes (enforcing NTP time synchronization on servers).
3. **Use Constant-Time Comparison:** Never compare cryptographic signatures using standard string comparison operators (`===` or `==`). Always use constant-time equality functions.
4. **Idempotent Database Processing:** Track incoming event IDs in an atomic datastore table and ignore or acknowledge duplicate events without re-executing business side effects.
5. **Acknowledge Fast, Process Asynchronously:** Validate the signature immediately and return HTTP `200 OK` within seconds; queue heavy processing (emails, provisioning) to background workers to avoid provider timeout retries.

### Reading order

1. Read [Stripe — Webhook Signatures & Security](resources.md#webhooks-saas).
2. Cross-reference with Chapter 1 Applied Cryptography and Chapter 6 Payment Workflows.

<a id="payments-workflows"></a>
## Payment, Checkout & Subscription Workflows

### Prerequisites

Understand e-commerce transaction flows, state machines, business logic validation, PCI-DSS compliance scope, and asynchronous payment gateway callbacks.

### Mechanism and mental model

Payment and subscription workflows handle high-value financial transactions. Because money is involved, payment integrations attract sophisticated adversarial targeting: price manipulation, currency confusion, status tampering, and double-spend race conditions.

Key architectural concepts for secure payment integrations:
1. **PCI-DSS Scope Reduction:** Modern web applications should never handle, transmit, or store raw Primary Account Numbers (PAN), CVVs, or card expiration dates. Instead, applications use client-side tokenization (hosted iframes like Stripe Elements or Braintree Drop-in) where the cardholder enters details directly into an iframe hosted by the PCI-compliant payment gateway. The gateway returns a single-use token or payment method ID to the client, which the client passes to the merchant backend.
2. **The "Never Trust the Client" Axiom:** Attackers frequently tamper with client-side checkout parameters using browser developer tools or HTTP proxies. If the frontend transmits `<input name="amount" value="99.99">` and the backend charges the user based on that parameter, an attacker can modify the price to `$0.01` or a negative value. All line items, discounts, shipping fees, tax rates, and total amounts must be calculated exclusively on the server from authoritative database records.
3. **Asynchronous Fulfillment vs. Browser Redirects:** When a customer completes checkout or 3D Secure verification, their browser is redirected back to the merchant's "Success" page (e.g., `GET /checkout/success?session_id=cs_123`). An attacker can easily navigate directly to this URL without completing payment. **Merchant backends must never fulfill orders or grant subscriptions based on client-side redirect URLs.** Fulfillment must be triggered exclusively by verified, cryptographically signed server-to-server webhook events received directly from the payment gateway.
4. **Payment State Machines & Concurrency:** Transaction state transitions must be strictly enforced:
   - `Created` → `Requires_Action` → `Authorized` → `Captured` → `Settled` (or `Failed` / `Refunded`).
   - Transitions must be atomic and protected against race conditions (see Chapter 4 Race Conditions) to prevent users from executing multiple simultaneous captures on a single authorization.

### Practical learning notes

In authorized audits and application reviews:
- Inspect network requests during checkout: Does the client transmit total prices or currency codes? Can you tamper with currency parameters (e.g. changing `$100 USD` to `100 JPY`)?
- Check order fulfillment triggers: Does the backend provision access upon viewing the thank-you page or only upon receiving a validated gateway webhook?
- Test concurrency: What happens if a user submits payment authorization or coupon redemption requests simultaneously across multiple browser tabs?

### Defensive and engineering notes

1. **Calculate All Amounts Server-Side:** Never accept prices, totals, or currencies from the client. Create the payment session on the gateway from server-side state and pass only the session ID to the client.
2. **Bind Fulfillment to Signed Webhooks:** Fulfill orders and provision digital goods only after verifying the cryptographic signature and timestamp of asynchronous gateway webhooks.
3. **Enforce Payment State Integrity:** Implement explicit state checks in database transactions. Verify that an order is in the `Pending` state before marking it `Paid`, and prevent re-entrant status changes.
4. **Idempotency Keys:** When issuing charge or refund API calls to external payment gateways, provide unique idempotency keys (e.g. `order_uuid_attempt_1`) to ensure network retries do not result in double charges.

### Reading order

1. Read [OWASP — Third Party Payment Gateway Integration Cheat Sheet](resources.md#payments-workflows).
2. Read [Stripe — Webhook Signatures & Security](resources.md#webhooks-saas).
3. Connect with Chapter 4 Business Logic & Workflow Integrity and Chapter 4 Race Conditions.
