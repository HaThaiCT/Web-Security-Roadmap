<!-- GENERATED FILE: do not edit by hand. Run scripts/generate.py. -->
# Curated Resources — Vulnerability Classes & Root Causes

<a id="sql-nosql"></a>
## SQL & NoSQL Injection

### Core

- **[Database Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Database_Security_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  An architectural guide for securing backend database instances in web applications. It details database isolation on dedicated network segments, least-privilege application accounts (limiting permissions to SELECT/INSERT/UPDATE rather than administrative superusers), host-based access controls, and mandating TLS 1.2+ encryption in transit between application servers and database instances.
- **[LDAP Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/LDAP_Injection_Prevention_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  A focused reference on preventing LDAP injection vulnerabilities in directory queries. It analyzes LDAP search filter syntax (prefix Polish notation) and Distinguished Name (DN) hierarchies, distinguishes filter encoding from DN encoding requirements, and outlines defensive frameworks, parameterized filter abstractions, and least-privilege binding.
- **[NoSQL Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/NoSQL_Security_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  A practical defensive guide addressing NoSQL injection risks across document and key-value datastores like MongoDB and CouchDB. It breaks down operator injection ($ne, $gt, $regex), server-side JavaScript execution via $where, and details core defenses including strict type casting, disallowing client-supplied operator objects, and using safe driver query builders.
- **[SQL Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html)** — *cheatsheet · beginner · learner, tester, developer · free/public*  
  A primary baseline for understanding and preventing SQL injection. It explains why prepared statements separate code from data, where stored procedures can still be risky, when allow-list validation is needed for identifiers such as table or column names, and why escaping is a last resort. Developers should pair it with framework-specific database APIs; testers should use it to reason about root cause and remediation quality.
- **[Web Security Academy](https://portswigger.net/web-security)** — *lab · beginner · learner, tester, developer · free/registration-required*  
  A broad, free training platform with guided material and realistic labs across major web vulnerability classes, APIs, identity flaws, protocol issues and newer areas such as LLM/AI attacks. It is useful for learners and authorized testers because practice happens in a safe and legal lab environment rather than on real targets. Some exercises require Burp Suite; the Community Edition is sufficient for many labs, but the account and tooling expectations should be checked per lab.

### Extended

- **[PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings)** — *cheatsheet · intermediate · tester, developer · free/public*  
  An extensive collection of practical web application security payloads, bypasses, and vulnerability cheat sheets across dozens of bug classes. It serves as a rapid reference for authorized penetration testers and security engineers reviewing input handling filters, demonstrating how parsers and runtime environments interpret boundary cases.

<a id="ldap-xpath"></a>
## LDAP & XPath Injection

### Core

- **[LDAP Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/LDAP_Injection_Prevention_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  A focused reference on preventing LDAP injection vulnerabilities in directory queries. It analyzes LDAP search filter syntax (prefix Polish notation) and Distinguished Name (DN) hierarchies, distinguishes filter encoding from DN encoding requirements, and outlines defensive frameworks, parameterized filter abstractions, and least-privilege binding.

<a id="command-injection"></a>
## Command & Expression Injection

### Core

- **[OS Command Injection Defense Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/OS_Command_Injection_Defense_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  A concise guide to command and argument injection defenses. It emphasizes replacing shell calls with native APIs, separating commands from arguments, layering parameterization with allow-list validation and using least privilege so command execution bugs have less impact.
- **[Server-Side Template Injection](https://portswigger.net/web-security/server-side-template-injection)** — *documentation · intermediate · learner, tester, developer · free/public*  
  A foundational guide to Server-Side Template Injection (SSTI) covering detection, identification of template engines, and exploitation risks up to remote code execution. It provides polyglot probe strings, mathematical expression tests to differentiate engines (e.g. Jinja2 vs. Twig), and key defense patterns such as logic-less templates and sandboxed rendering.

### Extended

- **[PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings)** — *cheatsheet · intermediate · tester, developer · free/public*  
  An extensive collection of practical web application security payloads, bypasses, and vulnerability cheat sheets across dozens of bug classes. It serves as a rapid reference for authorized penetration testers and security engineers reviewing input handling filters, demonstrating how parsers and runtime environments interpret boundary cases.

<a id="ssti"></a>
## Server-Side Template Injection

### Core

- **[Server-Side Template Injection](https://portswigger.net/web-security/server-side-template-injection)** — *documentation · intermediate · learner, tester, developer · free/public*  
  A foundational guide to Server-Side Template Injection (SSTI) covering detection, identification of template engines, and exploitation risks up to remote code execution. It provides polyglot probe strings, mathematical expression tests to differentiate engines (e.g. Jinja2 vs. Twig), and key defense patterns such as logic-less templates and sandboxed rendering.

### Extended

- **[PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings)** — *cheatsheet · intermediate · tester, developer · free/public*  
  An extensive collection of practical web application security payloads, bypasses, and vulnerability cheat sheets across dozens of bug classes. It serves as a rapid reference for authorized penetration testers and security engineers reviewing input handling filters, demonstrating how parsers and runtime environments interpret boundary cases.

<a id="deserialization"></a>
## Insecure Deserialization

### Core

- **[Deserialization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Deserialization_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  A comprehensive guide to insecure deserialization risks and mitigations across Java, Python, PHP, and .NET. It details native serialization signatures, gadget chain mechanics that escalate deserialization into remote code execution or DoS, and defense strategies including safe serialization formats, class allowlisting, and library hardening.

### Extended

- **[PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings)** — *cheatsheet · intermediate · tester, developer · free/public*  
  An extensive collection of practical web application security payloads, bypasses, and vulnerability cheat sheets across dozens of bug classes. It serves as a rapid reference for authorized penetration testers and security engineers reviewing input handling filters, demonstrating how parsers and runtime environments interpret boundary cases.

<a id="prototype-mass-assignment"></a>
## Prototype Pollution & Mass Assignment

### Core

- **[Prototype Pollution](https://portswigger.net/web-security/prototype-pollution)** — *documentation · intermediate · learner, tester, developer · free/public*  
  A comprehensive resource on JavaScript prototype pollution covering both client-side and server-side exploit mechanics. It explains how polluting Object.prototype via recursive merge or property assignment injects properties across the runtime, escalating to DOM XSS via client gadgets or remote code execution via Node.js child process child_process.fork options.

<a id="xxe"></a>
## XML External Entities

### Core

- **[XML External Entity Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/XML_External_Entity_Prevention_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  A definitive reference for preventing XML External Entity (XXE) vulnerabilities across diverse parsers in Java, .NET, PHP, and Python. It explains how external DTDs and entities enable file disclosure, SSRF, and parser denial of service, and provides explicit, copy-pasteable configuration flags to disable external entity resolution and DTD processing.
- **[XML Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/XML_Security_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  An authoritative reference for secure XML parsing, document processing, and schema validation. It details parser configurations that disable Document Type Definitions (DTDs), mitigates entity expansion attacks (Billion Laughs exponential expansion and quadratic blowup), and defines strict schema validation rules using bounded enumerations and length constraints.

<a id="upload-documents"></a>
## File Upload & Document Processing

### Core

- **[File Path Traversal](https://portswigger.net/web-security/file-path-traversal)** — *documentation · beginner · learner, tester, developer · free/public*  
  A clear guide to path traversal vulnerabilities that allow reading or writing arbitrary files on the server filesystem. It covers dot-dot-slash (../) directory navigation, common filter bypasses such as nested sequences and URL encoding, and establishes canonical path verification as the primary defense.
- **[File Upload Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  A defensive baseline for accepting user-supplied files without treating file extension or Content-Type as sufficient proof of safety. It is useful for developers and testers because it ties upload validation, filename handling, storage location, permissions, content processing and size limits into one review model.

<a id="traversal-inclusion"></a>
## Path Traversal & File Inclusion

### Core

- **[File Path Traversal](https://portswigger.net/web-security/file-path-traversal)** — *documentation · beginner · learner, tester, developer · free/public*  
  A clear guide to path traversal vulnerabilities that allow reading or writing arbitrary files on the server filesystem. It covers dot-dot-slash (../) directory navigation, common filter bypasses such as nested sequences and URL encoding, and establishes canonical path verification as the primary defense.
- **[File Upload Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  A defensive baseline for accepting user-supplied files without treating file extension or Content-Type as sufficient proof of safety. It is useful for developers and testers because it ties upload validation, filename handling, storage location, permissions, content processing and size limits into one review model.

<a id="ssrf"></a>
## SSRF & URL Processing

### Core

- **[Configuring the Instance Metadata Service (IMDSv2)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html)** — *documentation · intermediate · learner, tester, developer · free/public*  
  Authoritative cloud documentation detailing the security architecture of AWS EC2 Instance Metadata Service Version 2 (IMDSv2). It explains how session-oriented requests, mandatory PUT token generation, custom header requirements, and IP-level hop limit restrictions mitigate Server-Side Request Forgery (SSRF), open reverse proxy bypasses, and unauthorized metadata access.
- **[HTTP Host Header Attacks](https://portswigger.net/web-security/host-header)** — *documentation · intermediate · learner, tester, developer · free/public*  
  A comprehensive guide to vulnerabilities resulting from implicit trust in the HTTP Host header. It explores how intermediary proxies, reverse proxies, and backend application servers desynchronize routing, detailing password reset poisoning, routing-based SSRF, web cache poisoning, and authentication bypasses, along with remediation via strict Host allowlisting.
- **[OWASP API Security Top 10 2023](https://api-security.owasp.org/editions/2023/en/0x11-t10)** — *documentation · beginner · learner, tester, developer · free/public*  
  A high-level risk map for API work. It is not a control guide by itself, but it helps learners and teams orient around object-level authorization, authentication, property-level authorization, resource consumption, function-level authorization, sensitive business flows, SSRF, misconfiguration, inventory and unsafe third-party API consumption.
- **[Server Side Request Forgery Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  A practical defensive baseline for SSRF and URL-processing risk. It separates allowlisted internal destinations from open external fetch features, explains why deny-lists and parser assumptions are fragile, and connects application validation to network-layer egress controls and cloud metadata protection.
- **[Singularity of Origin — DNS Rebinding Attack Framework](https://github.com/nccgroup/singularity)** — *tool · advanced · tester, developer · free/public*  
  An authoritative open-source security tool and research framework for understanding and evaluating DNS rebinding attacks. It demonstrates how rapid DNS record manipulation circumvents the Same-Origin Policy (SOP) to access internal network services and cloud metadata through a victim's browser, and documents mitigations including Host header validation, DNS filtering, and Local Network Access (LNA) standards.
- **[Web Security Academy](https://portswigger.net/web-security)** — *lab · beginner · learner, tester, developer · free/registration-required*  
  A broad, free training platform with guided material and realistic labs across major web vulnerability classes, APIs, identity flaws, protocol issues and newer areas such as LLM/AI attacks. It is useful for learners and authorized testers because practice happens in a safe and legal lab environment rather than on real targets. Some exercises require Burp Suite; the Community Edition is sufficient for many labs, but the account and tooling expectations should be checked per lab.

<a id="information-errors"></a>
## Information Disclosure & Exceptional Conditions

### Core

- **[Error Handling Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Error_Handling_Cheat_Sheet.html)** — *cheatsheet · beginner · learner, tester, developer · free/public*  
  A practical guide for preventing information disclosure through unhandled exceptions and error messages. It explains how stack traces, framework version banners, database errors, and filesystem paths leaked in responses aid attacker reconnaissance and reveal injection sinks, and outlines patterns for global exception handlers, generic error responses, and secure internal diagnostic logging.
- **[File Upload Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  A defensive baseline for accepting user-supplied files without treating file extension or Content-Type as sufficient proof of safety. It is useful for developers and testers because it ties upload validation, filename handling, storage location, permissions, content processing and size limits into one review model.
- **[GraphQL Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/GraphQL_Cheat_Sheet.html)** — *cheatsheet · intermediate · tester, developer · free/public*  
  A GraphQL-specific security baseline covering schema-driven validation, query depth/amount limits, batching abuse, authorization on edges and nodes, introspection controls and error handling. It is useful because GraphQL concentrates many API risks into fewer network requests and resolver paths.
- **[Logging Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  A practical guide for implementing application-level security event logging and detection capabilities. It distinguishes operational debugging from security audit logging, defines essential security events to record (authentication attempts, access control failures, input validation rejections, session state changes), mandates log sanitization to prevent log injection and sensitive PII/credential leakage, and covers log integrity controls.
- **[OWASP Top 10 for Large Language Model Applications](https://genai.owasp.org/llm-top-10/)** — *documentation · intermediate · learner, tester, developer · free/public*  
  The premier risk taxonomy and awareness standard for applications integrating Large Language Models. It defines critical failure modes including direct and indirect prompt injection, sensitive data leakage, improper output handling, excessive agency, and vector/embedding vulnerabilities, providing core security principles for AI-enabled web features.
- **[XML External Entity Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/XML_External_Entity_Prevention_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  A definitive reference for preventing XML External Entity (XXE) vulnerabilities across diverse parsers in Java, .NET, PHP, and Python. It explains how external DTDs and entities enable file disclosure, SSRF, and parser denial of service, and provides explicit, copy-pasteable configuration flags to disable external entity resolution and DTD processing.

<a id="business-logic"></a>
## Business Logic & Workflow Integrity

### Core

- **[Bot Management and Anti-Automation Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Bot_Management_and_Anti-Automation_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  A practical guide for mitigating automated threats and business-logic abuse across web applications. Grounded in the OWASP Automated Threats to Web Applications project (OAT-001 through OAT-021), it covers defense against credential stuffing (OAT-008), scraping (OAT-011), inventory scalping (OAT-005), and card testing (OAT-001), detailing layered defensive architectures, behavioral anomaly detection, and rate limiting.
- **[Business Logic Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Business_Logic_Security_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  A practical guide for preventing business logic flaws and workflow subversion. It details strategies for enforcing application domain invariants, validating multi-step state transitions, maintaining integrity across transactional operations (e.g. pricing, coupons, quantity limits), and designing state machines that resist parameter manipulation and sequence bypasses.
- **[OWASP API Security Top 10 2023](https://api-security.owasp.org/editions/2023/en/0x11-t10)** — *documentation · beginner · learner, tester, developer · free/public*  
  A high-level risk map for API work. It is not a control guide by itself, but it helps learners and teams orient around object-level authorization, authentication, property-level authorization, resource consumption, function-level authorization, sensitive business flows, SSRF, misconfiguration, inventory and unsafe third-party API consumption.
- **[Smashing the state machine: the true potential of web race conditions](https://portswigger.net/research/smashing-the-state-machine)** — *article · advanced · learner, tester, developer · free/public*  
  Groundbreaking research demonstrating novel web race condition classes beyond basic limit-overruns, introducing the HTTP/2 single-packet attack to eliminate network jitter and synchronize requests within sub-millisecond windows. It covers multi-endpoint collisions, transient sub-states, and database-level atomic defensive architecture.
- **[Third Party Payment Gateway Integration Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Third_Party_Payment_Gateway_Integration_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  A comprehensive security baseline for integrating third-party payment gateways. It covers PCI-DSS scope reduction through client-side tokenization and hosted fields, mandates server-side validation of transaction amounts and currency codes, details cryptographic verification of asynchronous gateway callbacks, and enforces state machine integrity to prevent payment status tampering.

<a id="race-conditions"></a>
## Race Conditions

### Core

- **[Business Logic Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Business_Logic_Security_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  A practical guide for preventing business logic flaws and workflow subversion. It details strategies for enforcing application domain invariants, validating multi-step state transitions, maintaining integrity across transactional operations (e.g. pricing, coupons, quantity limits), and designing state machines that resist parameter manipulation and sequence bypasses.
- **[Smashing the state machine: the true potential of web race conditions](https://portswigger.net/research/smashing-the-state-machine)** — *article · advanced · learner, tester, developer · free/public*  
  Groundbreaking research demonstrating novel web race condition classes beyond basic limit-overruns, introducing the HTTP/2 single-packet attack to eliminate network jitter and synchronize requests within sub-millisecond windows. It covers multi-endpoint collisions, transient sub-states, and database-level atomic defensive architecture.
- **[Web Security Academy](https://portswigger.net/web-security)** — *lab · beginner · learner, tester, developer · free/registration-required*  
  A broad, free training platform with guided material and realistic labs across major web vulnerability classes, APIs, identity flaws, protocol issues and newer areas such as LLM/AI attacks. It is useful for learners and authorized testers because practice happens in a safe and legal lab environment rather than on real targets. Some exercises require Burp Suite; the Community Edition is sufficient for many labs, but the account and tooling expectations should be checked per lab.

### Extended

- **[PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings)** — *cheatsheet · intermediate · tester, developer · free/public*  
  An extensive collection of practical web application security payloads, bypasses, and vulnerability cheat sheets across dozens of bug classes. It serves as a rapid reference for authorized penetration testers and security engineers reviewing input handling filters, demonstrating how parsers and runtime environments interpret boundary cases.
