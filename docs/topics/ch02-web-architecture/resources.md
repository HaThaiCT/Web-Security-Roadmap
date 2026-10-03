<!-- GENERATED FILE: do not edit by hand. Run scripts/generate.py. -->
# Curated Resources — Web/Software Architecture & Engineering

<a id="request-lifecycle"></a>
## Request Lifecycle & Application Layers

### Core

- **[Client-Server overview](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Server-side/First_steps/Client-Server_overview)** — *documentation · beginner · learner, tester, developer · free/public*  
  A beginner-friendly architecture baseline for how browsers, web servers, web applications, templates, databases and static assets interact during a request. It is useful before studying vulnerabilities because it gives learners a concrete path for tracing user input from URL or form data into application code, database queries and rendered responses.
- **[HTTP caching](https://developer.mozilla.org/en-US/docs/Web/HTTP/Caching)** — *documentation · intermediate · learner, tester, developer · free/public*  
  A foundational architectural reference detailing HTTP cache hierarchies, freshness lifecycles, validation mechanics, and directive semantics. It distinguishes private client caches from shared proxy/CDN caches, breaks down Cache-Control directives (no-store, no-cache, max-age, must-revalidate), explains conditional validation via ETag and Last-Modified, and covers cache key differentiation using the Vary header.
- **[Overview of HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview)** — *documentation · beginner · learner, tester, developer · free/public*  
  A clear baseline for understanding HTTP as an application-layer, client-initiated request/response protocol. It explains messages, methods, headers, intermediaries, statelessness, cookies, persistent connections and HTTP/2 framing, which are prerequisites for nearly every web security topic in this repository. Use it before studying browser state, authorization bugs, cache behavior or protocol parsing flaws.
- **[Rendering on the Web](https://web.dev/articles/rendering-on-the-web)** — *article · intermediate · learner, tester, developer · free/public*  
  A practical comparison of server-side rendering, client-side rendering, static rendering, streaming and hydration trade-offs. It helps readers understand how modern rendering choices affect where code runs, where data appears, when browser JavaScript becomes authoritative and why frontend architecture matters for security review.

<a id="rendering-architectures"></a>
## MPA

### Core

- **[Client-Server overview](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Server-side/First_steps/Client-Server_overview)** — *documentation · beginner · learner, tester, developer · free/public*  
  A beginner-friendly architecture baseline for how browsers, web servers, web applications, templates, databases and static assets interact during a request. It is useful before studying vulnerabilities because it gives learners a concrete path for tracing user input from URL or form data into application code, database queries and rendered responses.
- **[Rendering on the Web](https://web.dev/articles/rendering-on-the-web)** — *article · intermediate · learner, tester, developer · free/public*  
  A practical comparison of server-side rendering, client-side rendering, static rendering, streaming and hydration trade-offs. It helps readers understand how modern rendering choices affect where code runs, where data appears, when browser JavaScript becomes authoritative and why frontend architecture matters for security review.
- **[Web Frontend Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Web_Frontend_Security_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  A focused security guide for modern frontend architectures, Single Page Applications (SPA), and asynchronous browser-backend communication. It establishes a zero-trust mindset for all data flowing between client and server, covers safe DOM rendering (preventing innerHTML XSS sinks), secure state management in memory vs. storage, and architectural patterns for decoupling API tokens from frontend clients via Backend-for-Frontend (BFF) layers.

<a id="distributed-components"></a>
## Proxies

### Core

- **[HTTP Desync Attacks: Request Smuggling Reborn](https://portswigger.net/research/http-desync-attacks-request-smuggling-reborn)** — *article · advanced · learner, tester, developer · free/public*  
  Foundational research on HTTP request smuggling against modern multi-tier web architectures. It explains CL.TE, TE.CL, and obfuscated Transfer-Encoding desynchronization between front-end reverse proxies and back-end servers, providing non-destructive detection probes and architectural mitigations including end-to-end HTTP/2 and request normalization.
- **[HTTP caching](https://developer.mozilla.org/en-US/docs/Web/HTTP/Caching)** — *documentation · intermediate · learner, tester, developer · free/public*  
  A foundational architectural reference detailing HTTP cache hierarchies, freshness lifecycles, validation mechanics, and directive semantics. It distinguishes private client caches from shared proxy/CDN caches, breaks down Cache-Control directives (no-store, no-cache, max-age, must-revalidate), explains conditional validation via ETag and Last-Modified, and covers cache key differentiation using the Vary header.
- **[Microservices Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Microservices_Security_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  An architectural guide for securing distributed microservices, message queues, and event-driven integrations. It evaluates edge API gateway authorization patterns, analyzes service-to-service mutual TLS (mTLS) and token authentication, details decentralized versus embedded Policy Decision Points (PDP), and covers secure asynchronous logging via message brokers.
- **[Overview of HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview)** — *documentation · beginner · learner, tester, developer · free/public*  
  A clear baseline for understanding HTTP as an application-layer, client-initiated request/response protocol. It explains messages, methods, headers, intermediaries, statelessness, cookies, persistent connections and HTTP/2 framing, which are prerequisites for nearly every web security topic in this repository. Use it before studying browser state, authorization bugs, cache behavior or protocol parsing flaws.
- **[RFC 9110: HTTP Semantics — Section 17 Security Considerations](https://www.rfc-editor.org/rfc/rfc9110.html)** — *specification · intermediate · learner, tester, developer · free/public*  
  The definitive IETF standard defining the core semantics of the Hypertext Transfer Protocol. Section 17 provides an authoritative security breakdown of establishing authority (DNS/TLS vs. plaintext HTTP), the risks of intermediary proxies and gateways, header parsing hazards, handling oversized protocol elements, and sensitive information leakage in URIs, Referer headers, and server software identifiers.
- **[Web Cache Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Web_Cache_Security_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  A comprehensive defensive guide on preventing sensitive response exposure, web cache poisoning, and web cache deception. It defines cache key mechanics, unkeyed input hazards, delimiter and path confusion, and specifies rigorous defenses including Cache-Control: no-store, private directives, and Content-Type validation.
- **[gRPC Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/gRPC_Security_Cheat_Sheet.html)** — *cheatsheet · intermediate · tester, developer · free/public*  
  A practical security guide for gRPC microservices and APIs. It details transport security requirements including mutual TLS (mTLS), token and metadata authentication via interceptors, message-level authorization, Protocol Buffer validation boundaries (clarifying that Protobuf enforces types but not business invariants), message size limits, and disabling server reflection in production.

<a id="data-components"></a>
## Databases

### Core

- **[Client-Server overview](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Server-side/First_steps/Client-Server_overview)** — *documentation · beginner · learner, tester, developer · free/public*  
  A beginner-friendly architecture baseline for how browsers, web servers, web applications, templates, databases and static assets interact during a request. It is useful before studying vulnerabilities because it gives learners a concrete path for tracing user input from URL or form data into application code, database queries and rendered responses.
- **[Database Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Database_Security_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  An architectural guide for securing backend database instances in web applications. It details database isolation on dedicated network segments, least-privilege application accounts (limiting permissions to SELECT/INSERT/UPDATE rather than administrative superusers), host-based access controls, and mandating TLS 1.2+ encryption in transit between application servers and database instances.
- **[NoSQL Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/NoSQL_Security_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  A practical defensive guide addressing NoSQL injection risks across document and key-value datastores like MongoDB and CouchDB. It breaks down operator injection ($ne, $gt, $regex), server-side JavaScript execution via $where, and details core defenses including strict type casting, disallowing client-supplied operator objects, and using safe driver query builders.
- **[Redis Security Model and Guidelines](https://redis.io/docs/latest/operate/oss_and_stack/management/security/)** — *documentation · intermediate · tester, developer · free/public*  
  The official architectural guide to Redis's security model, access control, and network isolation. It explains that Redis is designed for trusted internal network access, detailing the severe risks of internet-exposed instances (unauthenticated data deletion via FLUSHALL, unauthorized key access), protected mode mechanics, configuring strict bind interfaces, and deploying Role-Based Access Control (ACLs) to enforce least-privilege operations between web backends, caches, and queues.
- **[SQL Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html)** — *cheatsheet · beginner · learner, tester, developer · free/public*  
  A primary baseline for understanding and preventing SQL injection. It explains why prepared statements separate code from data, where stored procedures can still be risky, when allow-list validation is needed for identifiers such as table or column names, and why escaping is a last resort. Developers should pair it with framework-specific database APIs; testers should use it to reason about root cause and remediation quality.

<a id="parsing-templates"></a>
## Serialization

### Core

- **[Deserialization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Deserialization_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  A comprehensive guide to insecure deserialization risks and mitigations across Java, Python, PHP, and .NET. It details native serialization signatures, gadget chain mechanics that escalate deserialization into remote code execution or DoS, and defense strategies including safe serialization formats, class allowlisting, and library hardening.
- **[OS Command Injection Defense Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/OS_Command_Injection_Defense_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  A concise guide to command and argument injection defenses. It emphasizes replacing shell calls with native APIs, separating commands from arguments, layering parameterization with allow-list validation and using least privilege so command execution bugs have less impact.
- **[Server-Side Template Injection](https://portswigger.net/web-security/server-side-template-injection)** — *documentation · intermediate · learner, tester, developer · free/public*  
  A foundational guide to Server-Side Template Injection (SSTI) covering detection, identification of template engines, and exploitation risks up to remote code execution. It provides polyglot probe strings, mathematical expression tests to differentiate engines (e.g. Jinja2 vs. Twig), and key defense patterns such as logic-less templates and sandboxed rendering.
- **[The Fragile Lock: Novel Bypasses For SAML Authentication](https://portswigger.net/research/the-fragile-lock)** — *article · advanced · tester, developer · free/public*  
  Cutting-edge security research on SAML 2.0 implementations demonstrating full authentication bypasses via XML Signature Wrapping (XSW), attribute pollution, namespace confusion, and Void Canonicalization. It analyzes parser desynchronization between signature verification and assertion consumer modules (e.g. Nokogiri vs REXML) and details how empty digest strings lead to universal token forgery.
- **[XML External Entity Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/XML_External_Entity_Prevention_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  A definitive reference for preventing XML External Entity (XXE) vulnerabilities across diverse parsers in Java, .NET, PHP, and Python. It explains how external DTDs and entities enable file disclosure, SSRF, and parser denial of service, and provides explicit, copy-pasteable configuration flags to disable external entity resolution and DTD processing.
- **[XML Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/XML_Security_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  An authoritative reference for secure XML parsing, document processing, and schema validation. It details parser configurations that disable Document Type Definitions (DTDs), mitigates entity expansion attacks (Billion Laughs exponential expansion and quadratic blowup), and defines strict schema validation rules using bounded enumerations and length constraints.

### Extended

- **[SAML Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/SAML_Security_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  A structured baseline for implementing and securing the Web Browser SAML/SSO profile. It provides verification rules for protocol usage, message integrity, signature validation over Assertions and Responses, XML parser hardening against XXE and XSW, and handling IdP-initiated unsolicited responses.

<a id="identity-mechanics"></a>
## Identity & State Mechanics

### Core

- **[Multifactor Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Multifactor_Authentication_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  An authoritative reference for designing, implementing, and assessing multifactor authentication (MFA). It analyzes the five recognized authentication factor types, ranks factor security (contrasting phishing-resistant FIDO2/WebAuthn with restricted SMS/voice channels), details attack patterns like MFA fatigue and adversary-in-the-middle reverse proxies, and defines strict requirements for high-risk factor resets and step-up authentication.
- **[Web Frontend Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Web_Frontend_Security_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  A focused security guide for modern frontend architectures, Single Page Applications (SPA), and asynchronous browser-backend communication. It establishes a zero-trust mindset for all data flowing between client and server, covers safe DOM rendering (preventing innerHTML XSS sinks), secure state management in memory vs. storage, and architectural patterns for decoupling API tokens from frontend clients via Backend-for-Frontend (BFF) layers.
- **[Web Storage API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Storage_API)** — *documentation · beginner · learner, tester, developer · free/public*  
  The definitive browser documentation for client-side state storage mechanisms: localStorage and sessionStorage. It details origin-partitioned storage boundaries, contrasts tab-scoped ephemeral storage with persistent storage, analyzes synchronous performance implications, and establishes security boundaries—emphasizing that Web Storage is fully accessible to JavaScript and must never store sensitive session tokens or secrets vulnerable to XSS.

<a id="integrations-concurrency"></a>
## Integrations

### Core

- **[Microservices Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Microservices_Security_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  An architectural guide for securing distributed microservices, message queues, and event-driven integrations. It evaluates edge API gateway authorization patterns, analyzes service-to-service mutual TLS (mTLS) and token authentication, details decentralized versus embedded Policy Decision Points (PDP), and covers secure asynchronous logging via message brokers.
- **[Smashing the state machine: the true potential of web race conditions](https://portswigger.net/research/smashing-the-state-machine)** — *article · advanced · learner, tester, developer · free/public*  
  Groundbreaking research demonstrating novel web race condition classes beyond basic limit-overruns, introducing the HTTP/2 single-packet attack to eliminate network jitter and synchronize requests within sub-millisecond windows. It covers multi-endpoint collisions, transient sub-states, and database-level atomic defensive architecture.

<a id="build-deploy-basics"></a>
## Dependencies

### Core

- **[Nodejs Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Nodejs_Security_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  A practical reference for securing Node.js runtime environments, web frameworks, and server architectures. It details asynchronous control-flow pitfalls (pyramid of doom, unhandled promise rejections crashing the event loop), error handling without sensitive stack trace leakage, blocking the single-threaded event loop (ReDoS, heavy crypto), and process hardening.
- **[The Twelve-Factor App](https://12factor.net/)** — *documentation · beginner · learner, tester, developer · free/public*  
  The foundational architectural methodology for building software-as-a-service and cloud-native web applications. It establishes essential architectural boundaries: separating configuration from code (environment variables), treating backing services (databases, queues, caches) as attached resources, strictly isolating build/release/run stages, and executing applications as stateless processes.
