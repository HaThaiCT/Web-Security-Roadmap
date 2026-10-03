# Vulnerability Classes & Root Causes

This authored overview is organized by topic. Curated resource lists are generated separately in [resources.md](resources.md).

## How to use this part

Use this as a reference section, not as a mandatory linear course. Learning paths link to the topics and resources that fit each role.

<a id="sql-nosql"></a>
## SQL & NoSQL Injection

### Prerequisites

Understand HTTP parameters, server-side request handling and the basics of how an application builds database queries. For SQL injection specifically, know the difference between query structure and query values; for NoSQL, know that JSON-like query objects can also mix operator structure with user-controlled data.

### Mechanism and mental model

Injection happens when untrusted input is interpreted as part of a command or query rather than as data. In SQL, string concatenation lets attacker-controlled text change predicates, joins, sort order or additional statements. The durable fix is to keep the query structure fixed and bind values separately, so the database can distinguish code from data.

Not all dynamic behavior is the same. Values usually belong in parameters; identifiers such as table names, column names and sort directions cannot always be parameterized and need explicit allow-list mapping. Stored procedures are safe only when they avoid dynamic SQL and run with appropriate privileges.

### Practical learning notes

In labs, focus on identifying where input crosses from HTTP into database calls and why the query changes. Do not run payloads against real systems without authorization. When reading write-ups, separate the discovery technique from the remediation: the important question is whether the fix removed string-built query structure, not whether a specific payload stopped working.

### Defensive and engineering notes

Use parameterized queries or safe ORM/query-builder APIs by default, and review escape hatches such as raw SQL helpers. Add allow-list mapping for structural choices like sort keys. Use least-privilege database accounts, separate application users, restricted views and migration-controlled permissions so a single query bug has limited blast radius. Regression tests should verify both safe data handling and authorization on returned rows.

### Reading order

1. Read [OWASP — SQL Injection Prevention Cheat Sheet](resources.md#sql-nosql) for the defense hierarchy.
2. Then study framework-specific database APIs and lab material for SQL injection mechanics.
3. Treat NoSQL injection as a related but separate follow-up requiring source-specific documentation.

<a id="ldap-xpath"></a>
## LDAP & XPath Injection

### Prerequisites

Understand directory services (Active Directory, OpenLDAP), LDAP Distinguished Name (DN) tree structures, XML document structures, XPath query syntax, and basic boolean-logic query evaluation.

### Mechanism and mental model

Lightweight Directory Access Protocol (LDAP) and XML Path Language (XPath) are query languages used to look up directory objects and navigate XML documents. Both operate on tree-structured hierarchical data models:
- **LDAP Injection:** Applications query LDAP directory trees using search filters written in Polish (prefix) notation (e.g., `(&(uid=jsmith)(userPassword=secret))`). Because many enterprise LDAP client libraries lack native parameterized query abstractions, developers frequently concatenate user input directly into filter strings. By injecting metacharacters (`*`, `(`, `)`, `\`, `&`, `|`, `!`), an attacker can manipulate query logic:
  - Authentication bypass: injecting `*)(uid=*))(|(uid=*` creates a tautology (`(&(uid=*)(|(uid=*...))`) that authenticates the first account returned (often the domain admin).
  - Blind data exfiltration: using wildcards `(userPassword=a*)` to enumerate credentials or sensitive attributes character-by-character.
- **XPath Injection:** Similar to SQL injection, when user input is concatenated into an XPath expression used to select nodes in an XML document (e.g. `//user[username/text()='admin' and password/text()='secret']`), injecting XPath syntax (such as `' or '1'='1`) alters the node selection logic, bypassing authentication or extracting entire XML trees.

Both attacks succeed because user data is allowed to break out of data literal boundaries and become query control operators.

### Practical learning notes

In authorized audits and source code reviews:
- Identify code paths interacting with directory services (user login, address book searches, role mapping).
- Note that LDAP requires different escaping rules depending on context:
  - Search filter characters requiring escaping: `*`, `(`, `)`, `\`, and `NUL`.
  - Distinguished Name (DN) characters requiring escaping: `\`, `#`, `+`, `<`, `>`, `,`, `;`, `"`, `=`, and leading/trailing spaces.
- Audit LDAP binding privileges: verify whether the application binds using an unprivileged service account rather than an overly broad domain administrator or anonymous bind.

### Defensive and engineering notes

1. **Use Parameterized LDAP Frameworks:** Utilize libraries that provide parameterized search filters (e.g., Java's directory search abstractions with parameter placeholders `(&(uid={0})(objectClass=person))` or .NET LINQ-to-LDAP).
2. **Apply Contextual Character Escaping:** If string concatenation is unavoidable, apply RFC 4515-compliant search filter encoding (`Encoder.LdapFilterEncode`) and RFC 2253-compliant DN encoding (`Encoder.LdapDistinguishedNameEncode`).
3. **Parameterized XPath:** For XML queries, use precompiled XPath expressions with parameterized variables (e.g. `XPathVariableResolver`) rather than dynamic string assembly.
4. **Least-Privilege Binding:** Restrict the permissions of the service account used to bind to the directory server, preventing access to sensitive organizational units or administrative attributes.

### Reading order

1. Read [OWASP — LDAP Injection Prevention Cheat Sheet](resources.md#ldap-xpath).
2. Cross-reference with Chapter 3 Authentication & Account Recovery and Chapter 4 XML External Entities (XXE).

<a id="command-injection"></a>
## Command & Expression Injection

### Prerequisites

Understand server-side process execution, environment variables, filesystem paths and the difference between passing data to a library API and asking an operating-system shell to parse a command line.

### Mechanism and mental model

Command injection appears when untrusted input becomes part of an operating-system command or argument structure. The shell is a dangerous parser: metacharacters, separators, quoting rules, expansion and argument boundaries can change what runs. Even when a shell is not involved, argument injection can alter the behavior of a called program if user input is accepted as flags or operands.

The safest design is to avoid shelling out. If the application needs a capability such as image processing, directory creation or archive handling, prefer a language/library API that accepts structured parameters rather than a command string.

### Practical learning notes

In labs or authorized code review, first ask why process execution exists at all. Identify the command, arguments, working directory, environment, user privileges and whether input can become an option, path, filename or command fragment. Do not run command-injection payloads against real systems without explicit authorization; even proof attempts can execute unintended operations.

### Defensive and engineering notes

Use native APIs where possible. If process execution is required, pass command and arguments as separate values, disable shell interpretation, use allow-list validation for finite choices, reject unexpected flags, constrain paths, run with least privilege and isolate the worker. Escaping is a last line of defense, not a design pattern to rely on for arbitrary input.

### Reading order

1. Read [OWASP — OS Command Injection Defense Cheat Sheet](resources.md#command-injection).
2. Then inspect framework/language-specific process-execution APIs for the stack in use.
3. Pair with file upload, document processing and background-worker topics, where shellouts commonly appear.

<a id="ssti"></a>
## Server-Side Template Injection

### Prerequisites

Understand server-side templating engines (Jinja2, Twig, FreeMarker, Velocity, ERB), the separation between template presentation code and context data variables, and basic object introspection and inheritance chains in languages such as Python, Java, and PHP.

### Mechanism and mental model

Server-Side Template Injection (SSTI) occurs when user-controlled input is directly concatenated into a template definition string before compilation, rather than passed as context parameters into a fixed template file. For example, passing `render_template_string("Hello " + request.args.get('name'))` forces the template engine's parser to interpret user input as template directives.

Because modern template engines are expressive programming environments designed to evaluate conditionals, loops, and object methods, an attacker who injects template syntax can escape the presentation layer. By traversing runtime object hierarchies (such as Python's Method Resolution Order `__mro__` and `__subclasses__()`, or Java's reflection primitives), the attacker can instantiate arbitrary classes and invoke operating system command execution or read filesystem resources.

### Practical learning notes

In authorized testing or source code review, distinguish between data contexts (safe: `render("welcome.html", name=user_input)`) and template compilation sinks (unsafe: `render_template_string(user_input)` or dynamic inclusion). Probe safely using polyglot markers (`${{<%[%'"}}%\`) or distinct arithmetic evaluation trees (e.g. evaluating `${7*7}` or `{{7*'7'}}`) to fingerprint the exact engine without triggering destructive side effects. Never execute weaponized reverse shell payloads on systems without authorization.

### Defensive and engineering notes

Adopt logic-less template engines (such as Mustache or Handlebars) where application logic is completely decoupled from presentation. When using expressive engines, enforce strict architecture: never concatenate untrusted input into template definition source strings; always pass dynamic values through context variables. If user-authored templates are a business requirement (such as dynamic email builders), execute template compilation in hardened, isolated worker sandboxes with strict reflection and method-execution allowlists.

### Reading order

1. Read [PortSwigger — Server-Side Template Injection](resources.md#ssti) for detection heuristics and engine diagnostic trees.
2. Review language-specific template engines (e.g. Jinja2, Twig, FreeMarker documentation) to understand sandbox configuration limits.
3. Pair with Command & Expression Injection and Safe Output Encoding topics.

<a id="deserialization"></a>
## Insecure Deserialization

### Prerequisites

Understand native object serialization mechanisms (such as Java `Serializable` / `ObjectInputStream`, Python `pickle`, PHP `serialize()` / `unserialize()`, and .NET `BinaryFormatter`), object lifecycles, and how state is preserved across processes or network boundaries.

### Mechanism and mental model

Serialization converts in-memory object graphs into byte streams or text formats for storage or transmission; deserialization reconstructs the live object graph from that stream. Insecure deserialization occurs when an application deserializes untrusted data without sufficient verification of the types or structure being instantiated.

The hazard stems from magic methods and auto-executing lifecycles (e.g. `readObject()` in Java, `__wakeup()` / `__destruct()` in PHP, `__reduce__()` in Python). During deserialization, the runtime instantiates objects and invokes internal methods before the application's business logic has a chance to inspect or validate the resulting data. If classes present on the application's classpath or runtime environment ("gadgets") chain method invocations that execute dangerous operations—such as reflection, command execution, or file manipulation—the deserialization process itself triggers arbitrary code execution.

### Practical learning notes

In source code review and testing, recognize serialization signatures in headers, cookies, and network payloads: Java magic bytes `AC ED 00 05` (Base64 `rO0`), Python pickle streams, PHP serialized strings (`O:4:"User":...`), and .NET `TypeNameHandling` JSON metadata. Do not execute live exploit chains (e.g. ysoserial payloads) against systems without written authorization. Focus on confirming whether native deserialization sinks process untrusted data from the network.

### Defensive and engineering notes

The primary and most durable architectural defense is to avoid native object serialization entirely. Use language-agnostic, pure data interchange formats such as JSON, Protocol Buffers, or MessagePack that transmit plain attributes rather than executable object types. If legacy requirements necessitate native serialization, enforce strict type allowlisting before instantiation (e.g., overriding `resolveClass` in Java `ObjectInputStream` or using `SerialFilter`), cryptographically sign serialized blobs with an HMAC key stored securely in secrets management, and monitor classpath dependencies for known gadget libraries.

### Reading order

1. Read [OWASP — Deserialization Cheat Sheet](resources.md#deserialization) for language-by-language risk breakdowns and defenses.
2. Study safe data serialization architectures (Protocol Buffers, JSON DTOs).
3. Connect with Chapter 9 Secure Coding and Dependency Management.

<a id="prototype-mass-assignment"></a>
## Prototype Pollution & Mass Assignment

### Prerequisites

Understand JavaScript's prototypal inheritance model (`__proto__`, `prototype`, `constructor`), object mutation, recursive merging utilities, and how web frameworks bind incoming request parameters directly to backend data models.

### Mechanism and mental model

Prototype pollution occurs in JavaScript runtimes when an operation recursively merges, clones, or traverses nested properties using untrusted keys. If user input contains properties named `__proto__`, `constructor`, or `prototype`, the assignment modifies the root `Object.prototype`. Because almost all JavaScript objects inherit from `Object.prototype`, any property injected into the prototype becomes visible on every object across the entire application runtime.

Depending on the execution context, prototype pollution leads to severe consequences:
- **Client-Side:** Injected properties alter DOM rendering gadgets, modifying script configuration objects or attribute builders and escalating to DOM XSS.
- **Server-Side (Node.js):** Injected properties alter internal runtime flags (e.g., polluting `child_process.fork` options such as `NODE_OPTIONS` or `env`), leading directly to remote code execution or denial of service.

Mass assignment is a related structural defect where backend frameworks automatically map request parameters (JSON or form data) onto database entities without filtering. Attackers can inject internal model fields (e.g., `is_admin`, `role`, `account_balance`, `verified`) to elevate privileges or tamper with workflow state.

### Practical learning notes

In code audits, inspect deep-merge, deep-clone, and query-string parsing libraries (e.g. older versions of lodash, jQuery, or custom utilities). Look for assignments like `target[key] = value` inside recursive loops. For mass assignment, inspect controllers to see if request bodies are passed directly to ORM creation/update methods (`User.create(req.body)` or `user.update(params)`).

### Defensive and engineering notes

To defend against prototype pollution:
1. Validate and reject input keys containing `__proto__`, `constructor`, and `prototype`.
2. Use dictionary objects with no prototype: `Object.create(null)` for key-value maps.
3. Freeze the prototype during application bootstrap: `Object.freeze(Object.prototype)`.
4. Use modern `Map` collections instead of plain objects for dynamic key-value storage.

To defend against mass assignment:
1. Enforce strict Data Transfer Objects (DTOs) and request schemas using validation libraries (Zod, Joi, Pydantic).
2. Explicitly bind only expected, editable fields rather than spreading unvalidated request bodies into ORM models.

### Reading order

1. Read [PortSwigger — Prototype Pollution](resources.md#prototype-mass-assignment).
2. Review framework mass assignment defenses (e.g. strong parameters in Rails, DTO binding in NestJS/Spring).
3. Pair with Client-Side Injection (Chapter 5) and REST/API Security (Chapter 6).

<a id="xxe"></a>
## XML External Entities

### Prerequisites

Understand XML document structure, Document Type Definitions (DTDs), XML entities (general and parameter entities), and how XML parsers resolve external resources and system identifiers.

### Mechanism and mental model

XML External Entity (XXE) injection occurs when an XML parser processes untrusted XML input that contains a DTD with external entity declarations. When the parser encounters an entity defined with a system identifier (such as `<!ENTITY xxe SYSTEM "file:///etc/passwd">` or an external HTTP URI), the parser resolves the reference by reading the local filesystem or making an outbound network request.

Attackers leverage XXE to achieve:
1. **Local File Disclosure:** Reading configuration files, source code, and credentials accessible to the application process.
2. **Server-Side Request Forgery (SSRF):** Forcing the XML parser to query internal network services or cloud metadata endpoints.
3. **Denial of Service:** Exploiting nested entity expansion (the "Billion Laughs" attack or quadratic blowup) to exhaust CPU and memory resources.
4. **Blind Data Exfiltration:** Using out-of-band parameter entities to exfiltrate file contents over HTTP or DNS channels.

### Practical learning notes

XXE often hides in less obvious interfaces that accept XML behind the scenes: SOAP endpoints, SAML authentication assertions, Office document processors (DOCX/XLSX/PPTX, which are zipped XML archives), SVG image upload handlers, and RSS/Atom feed parsers. In testing, verify parser behavior using safe canary markers or entity resolution disabling checks without attempting broad filesystem harvesting.

### Defensive and engineering notes

The complete and robust remediation for XXE across all platforms is disabling external DTD parsing and external entity resolution in parser configuration:
- **Java (JAXP):** Explicitly set `http://apache.org/xml/features/disallow-doctype-decl` to `true`, and disable `external-general-entities` and `external-parameter-entities`.
- **.NET (XmlReader / XmlDocument):** Set `DtdProcessing = DtdProcessing.Prohibit` or set `XmlResolver = null`.
- **PHP:** Modern PHP 8.0+ disables external entity loading by default; for older versions, call `libxml_set_external_entity_loader(null)`.
- **Python:** Use hardened parsing libraries such as `defusedxml` rather than default standard library parsers.
- **General Architecture:** Prefer JSON or Protocol Buffers over XML for modern service-to-service communication.

### Reading order

1. Read [OWASP — XML External Entity Prevention Cheat Sheet](resources.md#xxe) for exact parser configuration flags.
2. Study document and archive processing architectures (SAML, DOCX, SVG).
3. Pair with SSRF & URL Processing and File Upload topics.

<a id="upload-documents"></a>
## File Upload & Document Processing

### Prerequisites

Understand HTTP multipart uploads, MIME/content types, filesystem paths, object storage, asynchronous workers and how the application later serves or processes uploaded content.

### Mechanism and mental model

File upload security is not a single validation check. A file has a user-supplied name, extension, Content-Type, byte signature, parsed structure, storage location, access policy and later processing path. Any of those can be abused if the application treats them as trustworthy or serves content in a dangerous context.

Document processing adds another boundary: parsers, converters, thumbnailers, antivirus engines and archive extractors may interpret attacker-controlled bytes. Even when the file is not executable by itself, it can trigger parser bugs, decompression bombs, path traversal inside archives, content spoofing or stored XSS when served back to users.

### Practical learning notes

For an authorized review, trace the full lifecycle: upload request, validation, renaming, storage, scanning/conversion, authorization, download or preview, deletion and logging. Avoid opening unknown files on your workstation or running public PoC documents; inspect metadata and behavior in controlled labs or disposable environments when authorized.

### Defensive and engineering notes

Use allowlisted extensions and expected types, but do not trust Content-Type alone. Generate server-side filenames, store uploads outside the webroot or in a separate object store, enforce authorization on every read, limit size and archive expansion, strip active content where possible, process files in sandboxed workers, serve with safe headers and separate untrusted content from the main application origin when feasible.

### Reading order

1. Read [OWASP — File Upload Cheat Sheet](resources.md#upload-documents).
2. Pair with object storage/secrets and path traversal topics.
3. Add parser-specific and document-processing sources in later curation.

<a id="traversal-inclusion"></a>
## Path Traversal & File Inclusion

### Prerequisites

Understand hierarchical filesystem path resolution (relative paths, absolute paths, dot-dot-slash `../` sequences), URI path encoding, and how server runtimes handle file read/write APIs and dynamic module or template loading.

### Mechanism and mental model

Path traversal (also referred to as directory traversal) occurs when an application accepts user input and concatenates it into a filesystem path without verifying that the resolved path stays within the intended target directory. Using traversal sequences (`../` on POSIX systems or `..\` on Windows), an attacker navigates out of the intended directory tree to access arbitrary files on the server.

Local File Inclusion (LFI) and Remote File Inclusion (RFI) are related vulnerabilities where the traversed path is passed to an interpreter or runtime loader (such as PHP's `include` / `require` or dynamic module loaders). In LFI, reading arbitrary files can escalate to code execution if the included file contains interpreter tags (e.g. log poisoning, session file poisoning, or wrapper tricks like `php://filter`). In RFI, the application fetches and executes a script directly from an attacker-controlled remote server.

### Practical learning notes

In source code review and testing, identify all endpoints that read, download, or include files based on parameters (e.g. `filename`, `file`, `path`, `doc`, `page`, `template`). Common naive sanitizations frequently fail:
- Stripping `../` non-recursively can be defeated by nested sequences: `....//` resolves to `../` after one pass.
- URL-encoding (`%2e%2e%2f`) and double-URL-encoding (`%252e%252e%252f`) bypass filters if decoding occurs after validation.
- Legacy runtimes with C-based filesystem wrappers historically suffered from null-byte truncation (`%00`).
Always verify behavior in safe test environments without attempting to dump live system secrets.

### Defensive and engineering notes

The most robust architectural pattern is to avoid passing user-supplied paths directly to filesystem APIs:
1. Store files using opaque, server-generated identifiers (such as UUIDs) and store file metadata in a relational database.
2. If user-supplied filenames must be processed, canonicalize the path using platform path normalization (e.g. `Path.normalize()` in Node.js, `Path.toRealPath()` in Java, or `os.path.realpath()` in Python) and verify that the canonical path starts with the authorized base directory prefix.
3. Use strict allowlists for file extensions and reject any input containing path separators (`/` or `\`).
4. Run application workers under an operating system user with minimal filesystem read/write privileges.

### Reading order

1. Read [PortSwigger — File Path Traversal](resources.md#traversal-inclusion).
2. Pair with File Upload & Document Processing and Object Storage topics.
3. Review language-specific path canonicalization functions and security best practices.

<a id="ssrf"></a>
## SSRF & URL Processing

### Prerequisites

Understand URLs, DNS resolution, redirects, internal networks, cloud metadata services and why server-side fetch features are more privileged than browser-side links. You should know which parts of the application can make outbound requests.

### Mechanism and mental model

SSRF happens when an application makes a server-side request to a destination influenced by an attacker. The server may reach internal hosts, loopback services, cloud metadata endpoints or trusted partner systems that the attacker cannot reach directly. The dangerous operation is the server's outbound request, not merely accepting a URL string.

URL processing is hard because parsers disagree, DNS can change between validation and use, redirects can move a request to a blocked destination, and IP/domain deny-lists are easy to miss. The safest model is to design fetch features around explicit trusted destinations and constrained protocols rather than arbitrary user-supplied URLs.

### Practical learning notes

In authorized testing, map every feature that fetches a URL: webhooks, importers, image fetchers, PDF renderers, link previews, integrations and admin diagnostics. Avoid probing arbitrary internal ranges or cloud metadata in production unless explicitly scoped. Use labs to understand parser tricks and metadata-service impact without touching real infrastructure.

### Defensive and engineering notes

Prefer allowlisted destinations for business integrations. Validate scheme, host and resolved IP using well-reviewed libraries, disable redirects or revalidate after redirects, block private/link-local/loopback ranges where external fetches are needed, separate fetcher infrastructure, restrict egress with firewalls and protect metadata services such as AWS IMDSv2. Log destination decisions without storing sensitive response bodies.

### Reading order

1. Read [OWASP — SSRF Prevention Cheat Sheet](resources.md#ssrf).
2. Pair with cloud IAM, metadata services and API inventory topics.
3. Use hosted labs for exploitation mechanics; do not reproduce against real cloud metadata or internal services.

<a id="information-errors"></a>
## Information Disclosure & Exceptional Conditions

### Prerequisites

Understand HTTP status codes (2xx success, 4xx client errors, 5xx server errors), exception handling models in server-side frameworks (try/catch blocks, middleware error interceptors), database query errors, and web application reconnaissance methodologies.

### Mechanism and mental model

Information disclosure occurs when a web application unintentionally reveals sensitive operational, structural, or technical data to unauthorized users. While rarely granting direct code execution on its own, information leakage provides crucial intelligence that attackers leverage to construct high-impact exploit chains:
1. **Verbose Stack Traces & Debug Banners:** When unhandled runtime exceptions occur (null pointer exceptions, database syntax failures, template rendering errors), default framework configurations frequently output full stack traces directly to the client. Stack traces expose internal filesystem directory paths (`/var/www/app/...`), source code line numbers, third-party library versions (e.g. Struts 2.5.12, Spring Boot 2.3.1), database engine versions, and internal class structures.
2. **Database & SQL Syntax Error Leakage:** Exposing database error messages (e.g. `ORA-00933: SQL command not properly ended`, `You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version...`) immediately confirms injection points and discloses database vendor, schema names, and column types.
3. **Sensitive Metadata & Environment Leaks:** Application routes that inadvertently serve `.env` files, `.git` repository metadata, internal Swagger/OpenAPI documentation, `/actuator` or `/metrics` diagnostic endpoints, or backup files (`.bak`, `.swp`, `~`) expose API secrets, cloud credentials, and database connection strings.
4. **Behavioral & Timing Discrepancies:** Differences in response status codes, error text ("User not found" vs. "Incorrect password"), or processing duration (timing attacks) allow attackers to enumerate valid usernames, tenant identifiers, and cryptographic keys.

### Practical learning notes

When conducting authorized testing or architecture reviews:
- Trigger boundary exceptions: test invalid input types, malformed JSON, oversized payloads, and non-existent IDs across API endpoints. Observe whether responses return generic error pages or reveal detailed stack traces.
- Inspect diagnostic endpoints: check whether administrative monitoring or debugging paths (e.g., Spring Boot Actuator `/env`, `/heapdump`, Django debug toolbar) are accidentally exposed to public traffic.
- Analyze error messages during authentication and password reset: verify whether the application returns identical generic messages and constant response times for both registered and unregistered email addresses.

### Defensive and engineering notes

1. **Centralize Global Exception Handling:** Implement centralized error-handling middleware or global exception handlers across the application stack. Catch all unhandled exceptions and return consistent, sanitized client responses (e.g. HTTP 500 with a generic message like `"An unexpected error occurred. Reference ID: <uuid>"`).
2. **Disable Debug Mode in Production:** Ensure framework debug settings (e.g. `DEBUG = False` in Django, `NODE_ENV=production` in Express, `app.debug=false` in Flask, `show_exceptions=false` in Rails) are strictly enforced in production environments.
3. **Log Internally, Sanitize Externally:** Log full technical details, stack traces, and diagnostics to secure, centralized logging infrastructure accessible only to authorized engineering personnel. Never leak diagnostic details to client browsers.
4. **Standardize User Enumeration Responses:** Use generic, identical responses for authentication, password recovery, and invitation workflows (e.g. `"If an account exists with this email, a reset link has been sent"`).

### Reading order

1. Read [OWASP — Error Handling Cheat Sheet](resources.md#information-errors) for framework exception handling and response sanitization baselines.
2. Cross-reference with Chapter 9 Application Logging & Detection and Secure Design Patterns.

<a id="business-logic"></a>
## Business Logic & Workflow Integrity

### Prerequisites

Understand application domain workflows, multi-step transaction lifecycles (shopping carts, checkout, KYC verification, order processing), state machines, and the role of client-server separation in distributed systems.

### Mechanism and mental model

Business logic vulnerabilities are design and implementation flaws that allow an attacker to manipulate legitimate application functionality to achieve unauthorized business outcomes. Unlike technical vulnerabilities (like SQL injection or buffer overflows) that result from syntax or parsing errors, business logic flaws occur when the application's code does exactly what the developer programmed it to do—but the developer's underlying assumptions about user behavior, state transitions, or trust boundaries are flawed.

Common categories of business logic failures include:
1. **Domain Invariant Violations:** Software often relies on implicit assumptions that are never formally verified by the backend. Examples include:
   - Negative value attacks: Submitting negative quantities (e.g. quantity `-1`) to reduce total cart value or trigger fraudulent store credit refunds.
   - Limit overruns and integer wraps: Exceeding maximum allowed discount limits or transaction caps.
2. **Multi-Step Workflow Bypasses:** In a sequence of dependent actions (e.g. Step 1: Select Item → Step 2: Calculate Shipping → Step 3: Authorize Payment → Step 4: Confirm Order), an attacker skips intermediate validation steps by issuing direct HTTP requests directly to the terminal endpoint (Step 4), fulfilling orders without payment.
3. **Client-Side Value Trust:** Trusting pricing, discount rates, currency codes, or privilege flags passed in client-side JSON payloads, cookies, or hidden form fields.
4. **State Machine Subversion:** Violating logical states—such as attempting to apply a single-use coupon simultaneously across concurrent sessions, cancelling an order after fulfillment to trigger a refund, or replaying one-time verification tokens.

Because business logic flaws are intimately tied to specific domain rules, automated vulnerability scanners cannot reliably detect them. Identifying them requires human reasoning about business intent and adversarial abuse modeling.

### Practical learning notes

In authorized assessments and code reviews:
- Map out the complete functional workflow and construct an explicit finite state machine (FSM).
- Formulate concrete adversarial questions: "What happens if I submit unexpected numbers (negative, zero, fractions, MAX_INT)?" "What happens if I execute Step 3 before Step 2?" "What happens if I execute the same step twice in parallel?"
- Inspect network traffic for client-side calculation parameters (e.g. `price=100.00`, `is_discounted=true`, `role=user`).

### Defensive and engineering notes

1. **Enforce Invariants Strictly Server-Side:** Never rely on client-side validation, UI disabling, or hidden form inputs to enforce domain rules. All prices, totals, permissions, and status flags must be derived or recalculated independently by trusted backend services.
2. **Implement Formal State Machines:** Model critical multi-step workflows using explicit state machines that strictly reject out-of-order execution, enforce preconditions, and record completed transition markers in the user's server-side session or database.
3. **Validate Boundary Invariants:** Explicitly validate that quantities and amounts are strictly positive numbers within allowable business thresholds before arithmetic processing.
4. **Combine with Concurrency Controls:** Protect critical business state transitions with database transactions and row-level locks (see Chapter 4 Race Conditions) to prevent simultaneous multi-request subversion.

### Reading order

1. Read [OWASP — Business Logic Security Cheat Sheet](resources.md#business-logic).
2. Cross-reference with Chapter 4 Race Conditions, Chapter 6 Payment Workflows, and Chapter 9 Threat Modeling.

<a id="race-conditions"></a>
## Race Conditions

### Prerequisites

Understand concurrent execution in multi-threaded and asynchronous application servers, HTTP connection multiplexing (HTTP/2 streams), database transactions, isolation levels, and the concept of Time-of-Check to Time-of-Use (TOCTOU).

### Mechanism and mental model

A web race condition occurs when concurrent HTTP requests interact with shared state (in-memory caches, session stores, or databases) without appropriate synchronization or atomic locking. When two or more requests execute overlapping read-modify-write sequences, the application state can enter unexpected transient sub-states.

Classic manifestations include:
- **Limit Overruns:** Redeeming discount gift codes, applying coupons, transferring funds, or casting votes multiple times before the database records the increment or invalidation.
- **Single-Endpoint State Collisions:** Sending parallel requests to the same endpoint with conflicting parameters, causing the application to execute conflicting business branches.
- **Multi-Endpoint Collisions:** Racing two distinct endpoints that share state—for example, racing a password reset confirmation request against an email change request to redirect the reset token to an attacker-controlled address.

Modern HTTP/2 implementations make race condition exploitation highly practical through the **single-packet attack**: by sending the bulk of 20 to 30 requests and holding back the final byte or frame, an attacker releases all final frames in a single TCP packet. This leverages Nagle's algorithm and eliminates network jitter, synchronizing the execution window on the server to sub-millisecond precision.

### Practical learning notes

When auditing or testing systems, look for multi-step business workflows where state checks and state updates are separate operations. Use dedicated tools (such as Turbo Intruder or Burp Suite's single-packet HTTP/2 group send) to probe synchronization windows safely in authorized labs. Observe whether transient error messages, duplicate records, or negative balances appear during parallel execution.

### Defensive and engineering notes

Preventing race conditions requires eliminating non-atomic state transitions at the architectural level:
1. **Atomic Operations:** Leverage database-level atomic operations (e.g. `UPDATE accounts SET balance = balance - 10 WHERE balance >= 10`) rather than reading state into application memory and writing it back.
2. **Datastore Integrity Constraints:** Enforce uniqueness constraints and foreign keys directly in the database schema (e.g. unique constraint on `(user_id, coupon_id)`), ensuring the database engine rejects duplicate inserts regardless of application concurrency.
3. **Pessimistic or Optimistic Locking:** Use database row-level locking (`SELECT ... FOR UPDATE`) or version-column optimistic locking for critical transactions.
4. **Distributed Locks:** For operations spanning multiple microservices or caching tiers, use reliable distributed locking primitives (e.g. Redis Redlock or Postgres advisory locks) with strict time-to-live timeouts.

### Reading order

1. Read [PortSwigger Research — Smashing the State Machine](resources.md#race-conditions) for HTTP/2 single-packet attack mechanics and the Predict-Probe-Prove methodology.
2. Review database transaction isolation levels (Read Committed, Repeatable Read, Serializable).
3. Connect with Chapter 2 Integrations & Concurrency and Chapter 9 Secure Design.
