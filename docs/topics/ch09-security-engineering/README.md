# Security Architecture & Engineering

This authored overview is organized by topic. Curated resource lists are generated separately in [resources.md](resources.md).

## How to use this part

Use this as a reference section, not as a mandatory linear course. Learning paths link to the topics and resources that fit each role.

<a id="threat-modeling"></a>
## Threat Modeling & Abuse Cases

### Prerequisites

Understand system architecture decomposition, Data Flow Diagrams (processes, data stores, external entities, data flows), trust boundaries, and foundational web vulnerability classes (from Chapters 3–5).

### Mechanism and mental model

Threat modeling is a structured, repeatable engineering discipline that evaluates software systems from an adversarial perspective. Performed early in the software development lifecycle (SDLC), threat modeling identifies architectural flaws, broken assumptions, and attack surfaces before code is written, deployed, or attacked.

The discipline is anchored in the Threat Modeling Manifesto's four core questions:
1. **What are we working on?** Decompose the application using Data Flow Diagrams (DFDs). Identify all external entities (users, third-party APIs), processes (web controllers, background workers), data stores (databases, caches, file storage), and data flows. Crucially, draw explicit **trust boundaries** wherever data crosses between different privilege levels or network zones.
2. **What can go wrong?** Systematically enumerate potential threats against each diagram element using structured frameworks such as **STRIDE**:
   - **Spoofing** (violating Authenticity): Impersonating a user, microservice, or credential.
   - **Tampering** (violating Integrity): Modifying database state, tampering with client-side cookies/tokens, or injecting malicious data into pipelines.
   - **Repudiation** (violating Non-repudiation): Performing unauthorized or fraudulent actions without sufficient audit logs to prove responsibility.
   - **Information Disclosure** (violating Confidentiality): Exposing sensitive customer data, API keys, or verbose system error messages.
   - **Denial of Service** (violating Availability): Exhausting server CPU, memory, or connection pools through unconstrained resource consumption.
   - **Elevation of Privilege** (violating Authorization): Bypassing object-level access controls (IDOR/BOLA) or gaining unauthorized administrative privileges.
3. **What are we going to do about it?** Determine an actionable response for each identified threat:
   - *Mitigate:* Implement concrete defensive controls (e.g. prepared statements, strict authorization checks, rate limiting).
   - *Eliminate:* Remove the high-risk feature or architecture component entirely.
   - *Transfer:* Shift operational responsibility to a trusted external service (e.g. using a specialized PCI-compliant payment gateway).
   - *Accept:* Formally document residual risk with explicit business justification and sign-off.
4. **Did we do a good enough job?** Review and validate the threat model with development, security, and operations stakeholders to verify that all data flows were analyzed and that mitigations are testable and implemented.

### Practical learning notes

When participating in architecture reviews or authorized assessments, map out data flows and focus scrutiny on trust boundaries: where untrusted browser requests cross into the backend, where internal microservices communicate, and where external webhooks are received. Formulate concrete "abuse cases" alongside standard functional user stories: what happens if a user submits negative numbers? What happens if requests are sent concurrently? What happens if the upstream database times out?

### Defensive and engineering notes

1. **Shift Left:** Conduct threat modeling during the initial architecture and design phase, preventing costly refactoring during production.
2. **Actionable Requirements:** Translate agreed mitigations directly into measurable engineering requirements and automated acceptance tests linked to standards like OWASP ASVS.
3. **Living Documentation:** Treat threat models as living artifacts maintained in version control alongside system architecture docs. Update models whenever new APIs, authentication flows, or cloud components are added.
4. **Pragmatic Scaling:** Start with lightweight, developer-friendly whiteboarding sessions using STRIDE-per-element rather than burdensome multi-week processes.

### Reading order

1. Read [OWASP — Threat Modeling Cheat Sheet](resources.md#threat-modeling).
2. Study the Threat Modeling Manifesto and STRIDE methodologies.
3. Connect with Chapter 9 Security Requirements & Verification Standards and Chapter 2 Web Architecture.

<a id="security-requirements"></a>
## Security Requirements & Verification Standards

### Prerequisites

You should understand the main application features, data sensitivity, user roles, trust boundaries and likely vulnerability classes. Requirements are most useful after you can connect a control to a concrete risk and a verification method.

### Mechanism and mental model

Security requirements translate “be secure” into testable statements. They define what the application must do, which threat or abuse case the control addresses, how strong the assurance needs to be, and how the team will verify it. A verification standard gives shared vocabulary and coverage so reviews are not driven only by individual memory or scanner output.

Good requirements are versioned, measurable and traceable. They should survive handoff between developers, testers and AppSec, and they should be specific enough to become tests, review checklist items or release gates.

### Practical learning notes

Do not try to memorize a full verification standard as a beginner. Instead, map one feature to the relevant requirement areas: authentication, session handling, access control, input/output handling, data protection, error handling and logging. For authorized testing, use requirements to decide what evidence is missing before calling a finding verified.

### Defensive and engineering notes

Adopt stable requirement references in design docs, tickets and tests. Keep the version of the standard explicit because requirement identifiers evolve. Use standards to improve coverage, not as a substitute for threat modeling: a payment workflow, multi-tenant object store or AI tool integration may need additional abuse-case-specific requirements.

### Reading order

1. Read the [OWASP Application Security Verification Standard](resources.md#security-requirements) project overview first.
2. Then inspect the specific ASVS chapters that match the feature being designed or reviewed.
3. Link requirements to testing methodology and remediation verification rather than treating them as standalone paperwork.

<a id="secure-design"></a>
## Secure Design Patterns & Architectural Trade-Offs

### Prerequisites

Understand software architecture, component decomposition, threat modeling principles, and common web security failure modes (Chapters 2, 3, 4, and 5).

### Mechanism and mental model

Secure product design moves beyond reactive vulnerability patching by baking security principles into architectural decisions from project conception through production. Rather than asking "is this specific line of code vulnerable?", secure design asks "does the system's architecture minimize the impact of an inevitable flaw?"

Secure product design is built upon four foundational pillars:
1. **Least Privilege & Separation of Duties:** Every component, service, user, and background worker must operate using the minimal set of privileges required to perform its task. Administrative actions (e.g. issuing refunds, deleting accounts) should require multi-person approval or separate operational boundaries to prevent a single compromised role from taking over the system.
2. **Defense-in-Depth:** Never rely on a single defensive control. If an input validation filter fails, parameterized queries prevent SQL injection. If an application-layer authorization check fails, network segmentation and database-level row-level security (RLS) restrict unauthorized data access.
3. **Zero Trust & Explicit Verification:** Eliminate implicit trust based on network location. Microservices communicating over internal VPC networks must mutually authenticate using mTLS and authorize individual calls using cryptographically signed metadata tokens rather than assuming internal traffic is benign.
4. **Security-in-the-Open (Kerckhoffs's Principle):** Security must never rely on secrecy or obfuscation. Assume that attackers have full access to client code, API schemas, and architectural diagrams. Systems must remain fundamentally secure based on mathematical algorithms, explicit cryptographic keys, and robust access control enforcement.

Engineering teams apply these pillars across **Five Design Focus Areas (the 5 C's)**:
- **Context:** Understanding regulatory requirements, user threat profiles, and business risk.
- **Components:** Ensuring all third-party libraries, container base images, and SDKs are vetted and tracked via Software Bills of Materials (SBOM).
- **Connections:** Encrypting all data in transit (TLS 1.3/mTLS) and strictly validating all incoming cross-boundary inputs.
- **Code:** Implementing secure design patterns (e.g. typestate patterns, builder patterns, immutable domain objects) that make insecure states unrepresentable.
- **Configuration:** Shipping with hardened, secure-by-default configurations and fail-safe defaults (e.g. denying access when an authorization check encounters an unhandled exception).

### Practical learning notes

In architecture reviews and authorized audits:
- Review architectural trade-offs: evaluate choices between convenience and security (e.g. long-lived session tokens vs. short-lived tokens with refresh rotation).
- Inspect exception and failure handling: when a downstream dependency (auth service, database) fails or times out, does the system fail securely (closed/denied) or fail open?
- Check default settings: are new user accounts or tenants created with least privilege, or do they receive broad default permissions?

### Defensive and engineering notes

1. **Secure by Default:** Features must ship with secure defaults. Opt-in for permissive behavior rather than opt-in for security controls.
2. **Fail-Safe Design:** If an authentication, authorization, or signature validation component fails or throws an exception, the system must immediately abort and deny the operation.
3. **Make Insecure States Unrepresentable:** Use type systems and domain-driven design (e.g. distinct `ValidatedEmail` or `SanitizedHTML` types) to enforce security invariant checks at compile time.
4. **Continuous Architectural Evolution:** Treat security architecture not as a one-time gate, but as an ongoing review process triggered whenever data flows or trust boundaries change.

### Reading order

1. Read [OWASP — Secure Product Design Cheat Sheet](resources.md#secure-design).
2. Connect with Chapter 9 Threat Modeling & Abuse Cases and Chapter 2 Web Architecture.

<a id="secure-code-review"></a>
## Secure Coding & Code Review

### Prerequisites

Understand programming languages used in modern web applications (JavaScript/TypeScript, Python, Go, Java, PHP, C#), common web vulnerability mechanisms (Chapters 3–5), data flow tracing (sources, sanitizers, sinks), and Git pull request workflows.

### Mechanism and mental model

Secure code review is the specialized discipline of inspecting source code to identify architectural flaws, security bugs, and deviations from secure coding standards. While automated tools (SAST) scan syntax and data flow patterns, human code review is uniquely capable of evaluating business logic, intent, authentication workflows, and contextual authorization rules.

1. **Baseline vs. Incremental Diff Reviews:**
   - *Baseline Reviews:* A comprehensive, holistic audit of the entire codebase or major subsystem. Performed during initial project onboarding, major version transitions, or compliance audits to establish an authoritative security posture baseline.
   - *Incremental Diff Reviews:* Focused reviews of specific pull requests or changesets. Evaluates new features, bug fixes, or refactored lines against security invariants, ensuring that new commits do not introduce regressions or bypass existing controls.
2. **Data Flow Tracing (Source to Sink Analysis):**
   Reviewers trace untrusted inputs through application layers:
   - *Source:* Where untrusted data enters the application (HTTP request bodies, query parameters, headers, cookies, webhook payloads, file uploads, database reads).
   - *Sanitizers & Validators:* Type checks, parameter validation schemas, encoding functions, and allowlists that transform or constrain input.
   - *Sink:* Where the data is executed, rendered, or passed to downstream engines (SQL execution calls, template rendering engines, OS command executors, DOM manipulation sinks).
3. **High-Risk Targets for Manual Review:**
   Reviewers prioritize areas that automated tools frequently misunderstand:
   - Authentication and session state transitions (login, password reset, token generation, MFA checks).
   - Access control logic: Checking whether object ownership checks (`current_user.id == resource.user_id`) exist across every controller endpoint.
   - Cryptographic implementations: Checking for secure random number generation, constant-time comparisons, and proper key derivation.
   - Complex business workflows: Pricing calculations, multi-step transaction integrity, and state machine transitions.

### Practical learning notes

In repository audits and pull request reviews:
- Focus first on high-risk files: routes/controllers, middleware, authentication modules, database queries, and raw serialization calls.
- Review git diffs with context: Inspect not only the modified lines, but also how the enclosing function validates input, manages permissions, and handles errors.
- Check for missing authorization checks: When a new endpoint is added to a controller, verify whether standard authentication and role middleware decorators are applied.

### Defensive and engineering notes

1. **Adopt Secure Coding Checklists:** Provide developers and reviewers with concise, language-specific checklists (e.g., OWASP Secure Coding Practices) covering input validation, output encoding, authorization, and error handling.
2. **Combine Manual Review with Automated Linters:** Run automated SAST and security linters (Semgrep, SonarQube, Bandit, ESLint Security) on pull requests to catch mechanical flaws, freeing human reviewers to focus on business logic and architecture.
3. **Require Dual Review on High-Risk Paths:** Enforce GitHub/GitLab branch protection rules requiring at least two approvals, including a designated AppSec engineer, for modifications touching authentication, cryptography, or authorization middleware.

### Reading order

1. Read [OWASP — Secure Code Review Cheat Sheet](resources.md#secure-code-review).
2. Connect with Chapter 9 SAST, DAST, IAST, SCA & Fuzzing and Chapter 4 Vulnerability Classes.

<a id="security-testing"></a>
## SAST, DAST, IAST, SCA & Fuzzing

### Prerequisites

Understand software testing methodologies, CI/CD pipeline integration, source code parsing (abstract syntax trees), HTTP proxying and dynamic traffic injection, and dependency management ecosystems.

### Mechanism and mental model

Modern application security testing relies on a portfolio of complementary testing technologies applied across different stages of the software development lifecycle:

1. **Static Application Security Testing (SAST):**
   Analyzes source code, bytecode, or binaries without executing the program. SAST parsers construct Abstract Syntax Trees (ASTs), Control Flow Graphs (CFGs), and Data Flow Graphs to detect known vulnerability signatures and trace untrusted tainted inputs from sources to dangerous sinks.
   - *Strengths:* High code coverage, detects flaws early in development (IDE / PR time), pinpoints exact line numbers.
   - *Weaknesses:* High false-positive rates, blind to runtime environment context, cannot evaluate runtime authorization or configuration.
2. **Dynamic Application Security Testing (DAST):**
   Operates as an external black-box scanner, testing running web applications by sending crafted HTTP requests and analyzing responses for vulnerability indicators (error messages, timing delays, reflected payloads).
   - *Strengths:* Tests the fully integrated application in its runtime environment, zero false positives for confirmed exploits, technology-agnostic.
   - *Weaknesses:* Limited code path coverage (only reaches endpoints exposed and navigated), late in the lifecycle, cannot identify root cause line numbers.
3. **Interactive Application Security Testing (IAST):**
   Combines SAST and DAST by embedding sensor agents inside the application runtime (e.g. JVM, Node.js, CLR). As functional or automated integration tests run, the agent monitors internal memory, variables, database queries, and data flows in real-time.
4. **Software Composition Analysis (SCA):**
   Scans project dependency manifests (package-lock.json, requirements.txt, go.sum) to identify third-party open-source components with known CVEs, outdated versions, or license compliance risks.
5. **Fuzzing (Grammar-based & Coverage-guided):**
   Feeds semi-random, mutated, or protocol-guided inputs into parsers (JSON, XML, HTTP headers, GraphQL) to trigger unexpected exceptions, memory exhaustion, or unhandled edge cases.

### Practical learning notes

In security engineering and testing pipelines:
- Configure rules in open-source SAST tools (Semgrep, CodeQL) to create custom queries enforcing company-specific architectural patterns (e.g. banning raw SQL queries in favor of the approved ORM).
- Use curated payload collections (such as PayloadsAllTheThings) to understand how different engines parse edge-case inputs when designing tests.
- Review SCA reports: Distinguish between reachable and unreachable dependencies—focusing remediation on vulnerable libraries that process untrusted external inputs.

### Defensive and engineering notes

1. **Embed Fast SAST & SCA in CI Pull Requests:** Run fast, low-false-positive SAST rules and dependency checks on every commit, providing immediate feedback to developers.
2. **Schedule DAST & Fuzzing in Staging:** Run thorough DAST scans and API fuzzing against staging environments where comprehensive integration test suites drive traffic through authenticated endpoints.
3. **Tune Rules and Triage Fatigue:** Regularly tune SAST and SCA rules to suppress irrelevant noise and eliminate persistent false positives, maintaining developer trust.

### Reading order

1. Study [PayloadsAllTheThings](resources.md#security-testing) for empirical payload and bypass references across testing domains.
2. Read [OWASP Application Security Verification Standard](resources.md#security-requirements) to align testing coverage with verification levels.

<a id="hardening-defaults"></a>
## Hardening & Secure Defaults

### Prerequisites

Understand the application's request path, deployment model and browser-facing behavior. You should know which layer terminates TLS, which layer sets response headers, which component owns cookies, and how static assets and third-party resources are loaded.

### Mechanism and mental model

Hardening reduces the number of unsafe states an application can enter by default. It is not a replacement for fixing vulnerabilities at the source; instead, it adds guardrails around transport, browser behavior, caching, framing, cross-origin access, resource loading and sensitive state. Good defaults are explicit, testable and owned by a specific component or team.

Many web hardening controls are expressed as HTTP headers or TLS/deployment settings. Their effect depends on exact browser semantics, proxy/CDN behavior and rollout order. A strong policy that breaks production will be bypassed; a weak policy that is never verified quietly rots.

### Practical learning notes

For an owned application, inventory current TLS behavior, redirects, cookies, CORS responses, CSP, frame embedding, referrer behavior and third-party resource loading. Compare staging and production because proxy/CDN layers often differ. Do not test by attacking real users; verify with controlled requests, browser developer tools and safe audit tools.

### Defensive and engineering notes

Assign ownership for each control and add regression checks where possible. Roll out high-risk headers such as CSP carefully, but avoid leaving report-only mode forever. Treat scanners and observability tools as feedback loops: they identify missing controls, while design review explains whether the control is appropriate for the system.

### Reading order

1. Read [MDN — Practical security implementation guides](resources.md#hardening-defaults) for a prioritized control map.
2. Then inspect individual control guides such as HSTS, secure cookies, CORS, CSP and clickjacking prevention before applying them to a production system.

<a id="logging-detection"></a>
## Application Logging & Detection

### Prerequisites

Understand distributed system observability, log aggregation architectures (ELK Stack, OpenSearch, Datadog, Grafana Loki), SIEM systems, HTTP request metadata, and application exception handling.

### Mechanism and mental model

Security logging captures auditable records of security-relevant events occurring within an application. Effective logging enables rapid incident detection, forensic reconstruction, and regulatory compliance. However, security event logging fundamentally differs from operational debugging:

1. **Operational Debugging vs. Security Audit Logging:**
   - *Debugging:* Ephemeral, detailed technical traces designed to troubleshoot code errors (e.g. stack traces, local variable values, raw payload dumps).
   - *Security Audit Logging:* Structured, immutable, tamper-evident records designed to establish non-repudiation, track user actions, and identify attack patterns over time.
2. **What Must Be Logged (Core Security Events):**
   - Authentication events: Successful logins, failed login attempts, password resets, MFA challenges, logouts.
   - Authorization failures: Access denied errors, unauthorized object access attempts (IDOR/BOLA probes), privilege elevation failures.
   - Input validation anomalies: Malformed JSON/XML, unexpected content-types, payload boundaries exceeding schema limits, SQL/XSS filter triggers.
   - Session lifecycle events: Session creation, invalid session tokens, concurrent login anomalies, token revocations.
   - Administrative & critical business actions: Role changes, tenant configuration updates, financial transfers, data exports.
3. **What Must NEVER Be Logged (Data Protection & Privacy):**
   Logging sensitive data introduces severe security and privacy liabilities:
   - Plaintext passwords, PINs, or password reset tokens.
   - Session tokens, JWTs, OAuth bearer tokens, or API secrets.
   - Payment card data (PAN, CVV) in violation of PCI-DSS.
   - Sensitive Personal Identifiable Information (PII) such as national identity numbers or protected health records.
4. **Log Injection & Integrity Protection:**
   If an application logs untrusted user input without sanitization, an attacker can inject Carriage Return / Line Feed characters (`\r\n` or `%0d%0a`), creating fake log entries (**Log Injection / CRLF Injection**) to deceive forensic investigators or exploit log analysis tools. All log entries must use structured formats (JSON) and encode newline characters.

### Practical learning notes

In application audits and monitoring reviews:
- Test log injection: Submit usernames or query parameters containing CRLF sequences (`admin\n[INFO] User logged in`) to verify whether the logging framework sanitizes newlines or creates separate log rows.
- Review log contents: Inspect application log streams to confirm that passwords, authentication headers, or sensitive query parameters are masked or excluded.
- Verify audit trails: Perform administrative operations (user deletion, role change) and verify whether the resulting log entries record the actor identity, target resource, timestamp, and client IP.

### Defensive and engineering notes

1. **Adopt Structured JSON Logging:** Emit all logs as structured JSON objects with consistent schemas (timestamp, event_type, user_id, client_ip, request_id, outcome).
2. **Sanitize Untrusted Data in Logs:** Neutralize CRLF characters by stripping or URL-encoding newlines before logging user-controlled input.
3. **Implement Centralized, Write-Once Log Shipping:** Stream logs immediately from application containers to a remote, centralized SIEM or log cluster with append-only permissions, preventing attackers who compromise the application server from modifying or deleting local log files.
4. **Establish Real-Time Alerting on Anomalies:** Configure SIEM alerts on security event thresholds (e.g., more than 10 failed login attempts in 1 minute, multiple 403 Forbidden errors across different object IDs from the same user session).

### Reading order

1. Read [OWASP — Logging Cheat Sheet](resources.md#logging-detection).
2. Connect with Chapter 9 Incident Response & Remediation Verification and Chapter 4 Information Disclosure & Error Handling.

<a id="incident-remediation"></a>
## Incident Response & Remediation Verification

### Prerequisites

Understand web application architecture, security operations center (SOC) workflows, Web Application Firewalls (WAF), patch management, Git release pipelines, and regression testing.

### Mechanism and mental model

When a web application security vulnerability is discovered or an active breach is detected, engineering teams must respond swiftly to contain the threat, minimize business impact, and remediate the root cause.

1. **The Web Incident Remediation Lifecycle:**
   - **Triage & Containment:** Confirm the vulnerability or active compromise. Restrict attack surface immediately by disabling vulnerable features, isolating compromised database credentials, or applying emergency network rules.
   - **Root Cause Analysis:** Determine the underlying architectural flaw or coding error that allowed the vulnerability, rather than focusing solely on the specific payload used in the incident.
   - **Virtual Patching (Tactical Interception):** While a permanent software fix is developed, tested, and staged for release, engineering teams deploy a virtual patch at an upstream inspection layer (WAF, API gateway, reverse proxy). A virtual patch intercepts and rejects exploit attempts in transit without altering application source code, drastically reducing the window of vulnerability.
   - **Permanent Source Code Remediation:** Developers refactor the codebase to address the systemic root cause (e.g. migrating from raw string concatenation to parameterized queries, or implementing server-side object authorization checks).
   - **Verification & Postmortem:** Verify that the permanent fix withstands bypass attempts, ensure virtual patches are phased out cleanly, and conduct a blameless postmortem to improve security engineering practices.
2. **Virtual Patching Architecture & Trade-Offs:**
   - *Advantages:* Rapid deployment (minutes to hours vs. days to weeks for emergency code releases), zero application downtime, protects legacy applications where source code cannot be easily modified.
   - *Risks:* High risk of false positives blocking legitimate traffic, potential for bypasses if WAF inspection rules do not account for parser differentials or encoding variations, and the risk that temporary virtual patches become permanent technical debt.
3. **Remediation Verification:**
   A vulnerability is not resolved simply because the reported exploit payload no longer succeeds. Verification requires:
   - Testing variant payloads and encoding mutations (Unicode, URL encoding, case variations).
   - Verifying the fix across all related endpoints and similar code patterns across the repository.
   - Adding permanent automated regression tests (unit and integration tests) to CI/CD pipelines to ensure future commits do not reintroduce the flaw.

### Practical learning notes

In incident response drills and post-remediation assessments:
- Evaluate virtual patch rules: Test whether WAF or proxy rules intercept exploit attempts without blocking valid user operations.
- Perform adversarial re-testing: Attempt to bypass the deployed fix using parser differentials, alternate HTTP methods, or parameter tampering.
- Review regression test coverage: Verify that pull requests resolving security vulnerabilities include dedicated regression test cases that fail against the unpatched code and pass against the patch.

### Defensive and engineering notes

1. **Establish Virtual Patching Runbooks:** Maintain pre-tested WAF and reverse proxy rule deployment pipelines capable of pushing emergency blocking rules within hours during an active zero-day incident.
2. **Require Automated Regression Tests for Every Security Bug:** Mandate that every security ticket includes automated unit or integration tests reproducing the flaw before the fix is merged.
3. **Conduct Blameless Postmortems:** Document root causes, detection timelines, remediation effectiveness, and preventive systemic improvements after every high-severity incident.

### Reading order

1. Read [OWASP — Virtual Patching Cheat Sheet](resources.md#incident-remediation).
2. Connect with Chapter 9 Application Logging & Detection and Chapter 7 Web Servers & Reverse Proxy Hardening.
