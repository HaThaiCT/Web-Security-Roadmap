# Web/Software Architecture & Engineering

This authored overview is organized by topic. Curated resource lists are generated separately in [resources.md](resources.md).

## How to use this part

Use this as a reference section, not as a mandatory linear course. Learning paths link to the topics and resources that fit each role.

<a id="request-lifecycle"></a>
## Request Lifecycle & Application Layers

### Prerequisites

Understand basic HTTP requests and responses, URLs, headers, cookies and at least one server-side language or framework. You should be able to identify a route, handler/controller, template or JSON response, and a database call in a simple application.

### Mechanism and mental model

A web request usually crosses several layers before a user sees a response: browser, network, web server or reverse proxy, application routing, middleware, handler/controller, service/domain logic, data access, templates or serializers, and static assets. Security bugs often appear where a layer assumes a previous layer already authenticated, authorized, validated, encoded or logged something.

For dynamic pages, user input may arrive through URL parameters, request bodies, headers or cookies; application code interprets the request, reads or writes state, renders HTML or JSON, and the browser may then fetch CSS, JavaScript, images and API data. Tracing that path is the first step before reasoning about injection, authorization, sessions or data leakage.

### Practical learning notes

When reading an application, draw one feature end-to-end: route, middleware, identity lookup, authorization check, data query, template/serializer and response headers. For realistic write-ups, separate the framework-specific exploit detail from the general layer boundary that failed. Practice only in labs or systems you are authorized to assess.

### Defensive and engineering notes

Make ownership of each control explicit. Authentication should establish identity, authorization should be checked server-side for the target object/action, validation should happen before dangerous interpretation, output encoding should happen at the rendering boundary, and logging should record security-relevant decisions without leaking secrets. Avoid relying on UI hiding, undocumented middleware ordering or “internal” endpoints as controls.

### Reading order

1. Read [MDN — Client-Server overview](resources.md#request-lifecycle) for the beginner request path.
2. Pair it with [MDN — Overview of HTTP](../ch01-foundations/resources.md#http).
3. Then trace the same lifecycle in a real framework or intentionally vulnerable lab.

<a id="rendering-architectures"></a>
## MPA, SPA, SSR, SSG & Hydration

### Prerequisites

Understand HTML, JavaScript, HTTP caching basics and the difference between server-generated HTML and browser-executed application code. You should know whether a page is rendered mostly on the server, mostly in the browser, or through a hybrid framework.

### Mechanism and mental model

Rendering architecture determines where data is assembled, where trust decisions run and when the browser becomes interactive. Server-side rendering can send complete HTML early, client-side rendering shifts more logic and state into JavaScript, static rendering creates build-time HTML, and hydration reconnects server-rendered markup to client-side components.

For security review, the important question is not which model is fashionable; it is where sensitive data appears, which code path authorizes it, whether client state is trusted by the server, and how cached or pre-rendered responses are separated between users, tenants and roles.

### Practical learning notes

When reviewing a modern app, identify the initial HTML, embedded data blobs, API calls made after hydration, client-side routes, server actions and cache boundaries. Do not assume a value is safe because it was generated during build or rendered before JavaScript started; stale build-time data, overbroad static generation and unsafe hydration sinks can still create security issues.

### Defensive and engineering notes

Keep authorization on the server or a trusted policy layer even when UI routing is client-heavy. Avoid embedding secrets or overbroad user data in HTML hydration state. Treat CDN/static caches as shared infrastructure that need keying by the right dimensions. Document which pages are public, user-specific, tenant-specific or admin-only before choosing SSR, SSG or client rendering behavior.

### Reading order

1. Read [web.dev — Rendering on the Web](resources.md#rendering-architectures) for rendering models and trade-offs.
2. Pair with request lifecycle notes so rendering is tied to data flow.
3. Revisit XSS, CORS, caching and authorization topics when reviewing a specific framework.

<a id="distributed-components"></a>
## Proxies, Caches & Distributed Components

### Prerequisites

Understand client-server architecture, HTTP request/response headers, basic DNS resolution, and the role of reverse proxies, load balancers, and Content Delivery Networks (CDNs) in front of application servers.

### Mechanism and mental model

Modern web applications are rarely exposed directly to the public Internet as a single standalone server. Instead, requests traverse a chain of distributed intermediaries: global CDNs (Cloudflare, Fastly, Akamai), edge load balancers, reverse proxies (Nginx, Envoy, HAProxy), and API gateways before finally reaching backend application runtimes.

These distributed components fulfill critical performance and scaling roles, but they also introduce distinct trust boundaries, parsing ambiguities, and cache state machines:
1. **Cache Hierarchies & Types:** Caches are split into *private caches* (browser-local, dedicated to one user) and *shared caches* (reverse proxies, CDNs, gateway caches serving millions of users). Shared caches must never store responses intended solely for a single authenticated user.
2. **Freshness & Validation:** Responses carry directives governing whether they can be stored and reused:
   - `Cache-Control: no-store`: Completely prohibits saving the response in any cache (essential for sensitive data, PII, and security tokens).
   - `Cache-Control: no-cache`: Permits caching but mandates conditional revalidation against the origin server before serving the cached copy to a client.
   - `Cache-Control: private`: Restricts caching to browser caches, preventing intermediate CDNs or proxies from storing the response.
   - `ETag` and `If-None-Match`: Allow stale entries to be refreshed efficiently via HTTP `304 Not Modified` responses.
3. **Cache Keys & Differentiation:** Shared caches store responses indexed by a *cache key*, typically derived from the request method and URI. If an application varies its response based on headers (e.g. `Cookie`, `Authorization`, `Accept-Language`) without reflecting those dimensions in the `Vary` header or cache key configuration, the shared cache may serve one user's private data or language choice to all other users (leading to Web Cache Deception and Cache Poisoning).
4. **Header Translation & Client Identity:** Proxies rewrite and terminate connections, forwarding client metadata via headers like `X-Forwarded-For`, `X-Forwarded-Proto`, and `X-Forwarded-Host`. If backend application servers trust these headers without verifying that they were set by a trusted upstream proxy, attackers can spoof client IP addresses, bypass IP allowlists, or manipulate host-based redirects.

### Practical learning notes

In architecture reviews and authorized testing:
- Trace the complete proxy hop path: identify which component terminates TLS, which component caches assets, and how request paths are rewritten.
- Inspect HTTP response headers (`Cache-Control`, `Vary`, `Age`, `CF-Cache-Status`, `X-Cache`) to determine whether responses are being served from edge caches or origin servers.
- Test cache key behavior in lab environments: check whether dynamic, user-specific data is returned on static-looking URL extensions (e.g., `/profile.css` or `/api/user.js`) that shared caches might store aggressively.

### Defensive and engineering notes

1. **Explicit Cache Directives:** Never rely on heuristic caching. Always send explicit `Cache-Control` headers on every response. For sensitive, dynamic, or authenticated endpoints, mandate:
   ```http
   Cache-Control: no-store, private
   ```
2. **Proper Use of the Vary Header:** When responses differ based on request headers, declare them explicitly using `Vary` (e.g. `Vary: Accept-Encoding, Accept-Language`). Never rely on `Vary: Cookie` alone for sensitive data—use `private` and `no-store` instead.
3. **Restrict Upstream Header Trust:** Configure backend application frameworks to accept `X-Forwarded-*` headers only from strictly allowlisted internal proxy IP addresses (CIDR ranges).
4. **Align Path & Parsing Rules:** Ensure URL normalization and path routing rules are synchronized between edge proxies and backend origin servers to eliminate path traversal and desynchronization bypasses.

### Reading order

1. Read [MDN — HTTP caching](resources.md#distributed-components) for cache types, freshness lifecycles, and directive semantics.
2. Cross-reference with Chapter 5 Cache Poisoning & Cache Deception and Chapter 7 Web Servers & Reverse Proxy Hardening.

<a id="data-components"></a>
## Databases, ORMs & Data Storage Architecture

### Prerequisites

Understand basic database concepts (relational tables, rows, primary/foreign keys, document collections, key-value stores), SQL query structure, connection pooling, and the role of Object-Relational Mappers (ORMs) and query builders in web frameworks.

### Mechanism and mental model

Databases are the core repository of state in web applications. From an architectural perspective, database security extends far beyond preventing SQL injection; it encompasses network topology, connection lifecycle, privilege segregation, and data-at-rest encryption.

Key architectural dimensions of database security include:
1. **Network Isolation:** Production database instances (PostgreSQL, MySQL, MongoDB, Redis) must reside in isolated private subnets or database tiers unreachable from the public internet. Application servers act as the sole authorized gatekeepers. Exposing raw database ports to public interfaces invites brute-force attacks, port scanning, and direct protocol exploitation.
2. **Least-Privilege Service Accounts:** Applications should connect using database roles constrained strictly to the required operations (e.g. `SELECT`, `INSERT`, `UPDATE`, `DELETE` on specific tables). Application service accounts must never possess administrative superuser privileges (`SUPERUSER`, `root`, `sa`), schema-altering permissions (`DROP`, `ALTER`, `TRUNCATE`), or access to internal administrative catalogs.
3. **Encrypted Transport:** Connections between web application servers and database clusters often traverse cloud networks, VPC peerings, or shared data centers. Modern deployments mandate TLS 1.2+ encryption with mutual certificate verification (mTLS) to prevent on-path eavesdropping and credential sniffing.
4. **ORM Abstractions & Pitfalls:** ORMs (ActiveRecord, Hibernate, Prisma, TypeORM) provide abstracted object mapping and parameterized queries, substantially mitigating classic SQL injection. However, ORMs introduce distinct security risks: raw query escape hatches (`raw()`, `whereRaw()`), object hydration side effects, mass assignment vulnerabilities when mapping untrusted request bodies directly to models, and Cartesian-product query denial-of-service (N+1 query issues).

### Practical learning notes

When analyzing backend database architecture in authorized reviews:
- Trace database connection configurations: inspect connection strings to ensure credentials are not hardcoded, check whether TLS verification is enforced (`sslmode=verify-full`), and verify that connection pools limit max active connections to prevent exhaustion DoS.
- Audit database user permissions: review application database accounts to confirm they cannot read other tenants' data or execute administrative stored procedures (`xp_cmdshell`, `pg_read_file`).
- Test ORM usage patterns: identify locations where developers bypass ORM query builders to concatenate dynamic input into raw SQL queries.

### Defensive and engineering notes

1. **Enforce Network-Level Isolation:** Place databases in private VPC subnets with ingress security group rules allowing traffic only from designated application server clusters.
2. **Implement Least Privilege:** Separate migration accounts (which run DDL: `CREATE`, `ALTER`) from runtime application accounts (which run DML: `SELECT`, `UPDATE`).
3. **Mandate Parameterization:** Standardize all data access on parameterized queries, prepared statements, and type-safe ORM methods.
4. **Enable Audit Logging:** Configure database audit logs (e.g. `pgAudit` for PostgreSQL) to record authentication failures, schema changes, and high-privilege access.

### Reading order

1. Read [OWASP — Database Security Cheat Sheet](resources.md#data-components) for baseline architectural controls.
2. Connect with Chapter 4 SQL & NoSQL Injection and Chapter 7 Object Storage & Secrets.

<a id="parsing-templates"></a>
## Serialization, Parsers, Template Engines & Document Processing

### Prerequisites

Understand common data interchange formats (JSON, XML, YAML, Protocol Buffers), server-side template engines (Jinja2, Thymeleaf, Handlebars, Blade), and the difference between text interpolation and structured data parsing.

### Mechanism and mental model

Modern web applications constantly parse serialized data streams from clients, microservices, and third-party webhooks. Every parser introduces an attack surface that depends directly on the complexity and expressive power of the underlying format:
1. **XML & DTD Processing:** XML allows Document Type Definitions (DTDs) and external entity declarations (`<!ENTITY ... SYSTEM "...">`). By default, many XML parsers resolve external entities, allowing attackers to read server files, trigger Server-Side Request Forgery (SSRF), or launch exponential entity expansion attacks (Billion Laughs / quadratic blowup DoS). Disabling external DTD processing entirely is the canonical defense.
2. **Unsafe Object Deserialization:** Formats that serialize both data and executable type metadata (Java serialization, Python pickle, PHP serialize, Ruby Marshal, YAML `!ruby/object`) allow arbitrary object instantiation. Attackers craft gadget chains using classes available on the application classpath to execute arbitrary code.
3. **Template Engines & Expression Languages:** Server-side template engines render dynamic data by evaluating expressions embedded in templates. If user input is concatenated into the template string rather than passed as context data, the template engine evaluates user input as code (Server-Side Template Injection / SSTI).
4. **Document Processing & Converters:** Applications that generate PDFs (wkhtmltopdf, Puppeteer), parse images (ImageMagick), or process Office documents (LibreOffice) execute complex native parsing code. Complex document formats frequently contain embedded JavaScript, external URL references, or memory corruption vulnerabilities.

### Practical learning notes

In architectural assessments and security testing:
- Identify all document and serialization parsers in the stack: check XML parser configurations across libraries (libxml2, DOMParser, lxml) for entity resolution flags.
- Distinguish context data from template syntax: check whether templates use safe data binding (`{{ user.name }}`) versus dangerous string interpolation (`template = "Hello " + request.get("name")`).
- Test document conversion pipelines: verify whether PDF generators render arbitrary HTML, execute JavaScript, or reach internal network endpoints (`file://`, `http://169.254.169.254`).

### Defensive and engineering notes

1. **Disable XML External Entities (XXE):** Configure all XML parsers to completely disable DTDs, external entity resolution, and parameter entities.
2. **Ban Unsafe Deserialization:** Use safe, logic-free serialization formats (standard JSON) instead of native language object serialization.
3. **Isolate Document Rendering:** Run PDF generators, image converters, and document processing libraries inside hardened, sandboxed containers with no network egress access.
4. **Use Logic-Less Templates:** Prefer logic-less template engines or strictly separate template definitions from runtime variable context.

### Reading order

1. Read [OWASP — XML Security Cheat Sheet](resources.md#parsing-templates) for parser hardening rules.
2. Cross-reference with Chapter 4 XXE & File Processing, Deserialization, and SSTI.

<a id="identity-mechanics"></a>
## Identity & State Mechanics: Cookies, Tokens & Web Storage

### Prerequisites

Understand HTTP statelessness, the Same-Origin Policy, client-side JavaScript execution environments, and basic cryptographic signing vs. encryption.

### Mechanism and mental model

Because HTTP is stateless, web applications must maintain identity and session state across multiple requests. Where and how this state is stored defines critical security boundaries:
1. **HttpOnly Cookies vs. Web Storage:**
   - **Cookies:** Stored by the browser and automatically attached to outgoing HTTP requests based on domain and path rules. Setting the `HttpOnly` flag renders cookies inaccessible to client-side JavaScript (`document.cookie`), providing structural defense against session hijacking via Cross-Site Scripting (XSS). Adding `Secure` ensures transport only over HTTPS; `SameSite=Lax` or `Strict` limits cross-site request inclusion.
   - **Web Storage (`localStorage` and `sessionStorage`):** Key-value stores accessible synchronously from JavaScript within a specific origin. `localStorage` persists across browser sessions; `sessionStorage` is scoped to a single tab. **Crucially, Web Storage cannot be protected by HttpOnly.** Any XSS flaw on the origin allows immediate exfiltration of tokens stored in localStorage.
2. **Session Identifiers vs. Self-Contained Tokens:**
   - **Reference Sessions:** The server issues an opaque, cryptographically random session ID pointing to server-side session state (stored in Redis or a database). Revocation is instant (deleting the server-side record immediately terminates access).
   - **Stateless Tokens (JWT):** The client holds state signed by the server. While eliminating server-side lookups, revoking a JWT before its expiration requires maintaining distributed revocation lists or Token Status Lists.
3. **State Desynchronization & Concurrency:** When state is stored across multiple distributed layers (client storage, CDN cache, server session store), race conditions and state desynchronization can allow stale or forged state to persist.

### Practical learning notes

In architecture reviews and authorized testing:
- Inspect browser storage: open Developer Tools and examine Cookies, Local Storage, and Session Storage. Identify where authentication tokens, session identifiers, and PII are stored.
- Test token lifecycle: determine what happens when a user logs out—does the server actively invalidate the session, or does an exported token remain valid until its expiration timestamp?
- Evaluate cookie security flags: verify that all session cookies carry `Secure`, `HttpOnly`, and appropriate `SameSite` attributes.

### Defensive and engineering notes

1. **Default to HttpOnly Cookies for Sessions:** Store authentication session identifiers and refresh tokens in `HttpOnly`, `Secure`, `SameSite=Lax/Strict` cookies with `__Host-` prefixes. Avoid storing long-lived sensitive tokens in `localStorage`.
2. **Use Cryptographically Secure Random IDs:** Generate session identifiers using CSPRNGs with at least 128 bits of entropy.
3. **Implement Proper Invalidation:** On user logout or privilege elevation (e.g. password change), immediately destroy server-side session state and rotate session identifiers.
4. **Mandate Short Lifetimes:** For token-based architectures, keep access tokens short-lived (e.g. 5–15 minutes) and require refresh tokens for renewal.

### Reading order

1. Read [MDN — Web Storage API](resources.md#identity-mechanics) for client-side storage mechanics and security constraints.
2. Cross-reference with Chapter 3 Sessions & State Security, JWT & Token Validation, and Chapter 5 Origins, Cookies & Storage.

<a id="integrations-concurrency"></a>
## Integrations, Microservices & Event-Driven Concurrency

### Prerequisites

Understand basic distributed system concepts (monolith vs. microservices, message queues, publish-subscribe patterns, REST/RPC inter-service calls), and basic database transactions (ACID properties).

### Mechanism and mental model

Modern enterprise web applications are distributed networks of microservices, third-party APIs, and asynchronous event streams. Each boundary between services introduces integration, authorization, and concurrency challenges:
1. **Edge Gateway vs. Service-to-Service Authorization:** In microservice architectures, requests enter through an API Gateway where initial authentication occurs. How user identity propagates downstream determines the internal security posture. In a naive model, internal services trust all upstream calls without verification (a compromised internal service can impersonate any user). In zero-trust microservices, identity and tenant context are cryptographically propagated via signed tokens (mTLS, internal JWTs), and Policy Decision Points (PDPs) enforce authorization locally within each service.
2. **Asynchronous Message Queues & Event Streams:** Systems use message brokers (RabbitMQ, Apache Kafka, AWS SQS) for background processing, decoupling long-running jobs from HTTP request-response cycles. Security risks include unauthenticated brokers, cross-tenant message queue injection, unencrypted message payloads at rest/transit, and replay attacks on event consumers.
3. **Concurrency & Race Conditions:** When multiple requests or distributed workers process operations concurrently on shared state (e.g. account balances, discount codes, inventory counts), lack of proper synchronization (optimistic locking, distributed locks, database transactions with serializable isolation) enables Time-of-Check to Time-of-Use (TOCTOU) race conditions. Attackers exploit millisecond timing windows using concurrent HTTP requests to bypass business invariants (e.g. spending funds twice).
4. **Idempotency & Retries:** Distributed networks experience transient failures. Webhooks and API endpoints must implement idempotent request processing (using unique idempotency keys) to prevent duplicate transactions when clients or proxies retry requests.

### Practical learning notes

In architectural audits and testing:
- Trace inter-service identity propagation: inspect how service A passes user identity to service B. Is it an unverified HTTP header (`X-User-Id`), or a signed token with audience and scope validation?
- Inspect message queues: verify whether queues require authentication, enforce role-based permissions per topic/queue, and encrypt sensitive message data in transit and at rest.
- Test for race conditions in lab environments: identify state-altering endpoints (redemptions, transfers, checkouts) and test concurrent multi-request bursts to evaluate transaction isolation.

### Defensive and engineering notes

1. **Deploy Zero-Trust Microservice Communication:** Enforce mutual TLS (mTLS) with short-lived certificates and signed identity tokens between internal microservices.
2. **Implement Idempotency Keys:** Enforce unique idempotency keys on all financial, transactional, and state-modifying API operations.
3. **Use Atomic Transactions & Locking:** Use database-level row locking (`SELECT ... FOR UPDATE`), atomic update operations, or distributed locks (Redis Redlock) for critical shared resources.
4. **Isolate Message Brokers:** Place message brokers in isolated network segments, require strict SASL/TLS authentication, and separate tenant topics where appropriate.

### Reading order

1. Read [OWASP — Microservices Security Cheat Sheet](resources.md#integrations-concurrency) for architectural and authorization patterns.
2. Cross-reference with Chapter 4 Race Conditions & Business Logic, and Chapter 6 Webhooks & SaaS Integrations.

<a id="build-deploy-basics"></a>
## Build, Deployment, Configuration & Twelve-Factor Foundations

### Prerequisites

Understand version control (Git), software development lifecycles (build, release, run), basic containerization concepts (Docker), and cloud application hosting environments.

### Mechanism and mental model

How web software is configured, packaged, and deployed directly dictates its operational resilience and security posture. The Twelve-Factor App methodology establishes foundational engineering boundaries for cloud-native web applications:
1. **Config in the Environment (Factor III):** Configuration that varies between deployments (development, staging, production)—such as database credentials, API secrets, encryption keys, and external service URLs—must be strictly separated from code. Secrets must never be committed to source code repositories. Instead, configuration is injected into running processes via environment variables or centralized secret managers.
2. **Backing Services as Attached Resources (Factor IV):** Backing services (databases, message queues, cache servers, SMTP mailers) must be treated as attached resources accessed via location-independent URLs/credentials. Swapping a local database for a managed cloud instance should require zero code changes, only configuration updates.
3. **Strict Separation of Build, Release, and Run Stages (Factor V):** The deployment pipeline must strictly separate stages:
   - *Build stage:* Transforms code and dependencies into an immutable artifact (e.g. compiled binary, container image).
   - *Release stage:* Combines the build artifact with the deployment-specific configuration.
   - *Run stage:* Executes the release in the execution environment. Releases must be immutable; making direct code or configuration edits to running production servers is strictly prohibited.
4. **Stateless Processes (Factor VI):** Web application processes must be stateless and share-nothing. Any data that needs to persist must be stored in a stateful backing service. This ensures horizontal scaling, rapid restartability, and predictable recovery from failure.

### Practical learning notes

In configuration reviews and deployment audits:
- Audit source repositories for secret leakage: check Git history for committed API tokens, private keys, or credentials using tools like TruffleHog or GitGuardian.
- Inspect environment variable management: evaluate how secrets are passed to production containers (e.g. AWS Secrets Manager, Kubernetes Secrets vs. plaintext shell scripts).
- Verify container immutability: ensure production containers run with read-only root filesystems and do not execute dynamic code updates in place.

### Defensive and engineering notes

1. **Never Commit Secrets:** Implement automated pre-commit hooks and CI/CD secret scanning to block committed credentials.
2. **Centralize Secrets Management:** Use dedicated secrets management platforms (Vault, AWS Secrets Manager) with automated rotation.
3. **Build Immutable Container Images:** Build minimal, immutable container images (distroless or Alpine), run processes as non-root users, and enforce read-only filesystems.
4. **Enforce Stage Isolation:** Ensure development, staging, and production environments are strictly isolated at network, IAM, and account boundaries.

### Reading order

1. Read [Adam Wiggins — The Twelve-Factor App](resources.md#build-deploy-basics) for canonical cloud-native engineering principles.
2. Connect with Chapter 7 CI/CD Permissions & Pipeline Security, Containers & Kubernetes, and Object Storage & Secrets.
