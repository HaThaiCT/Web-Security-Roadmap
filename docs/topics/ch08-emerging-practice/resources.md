<!-- GENERATED FILE: do not edit by hand. Run scripts/generate.py. -->
# Curated Resources — Emerging Web Risks, Privacy & Practical Testing

<a id="ai-web-security"></a>
## AI-Enabled Web Applications & Tool Permissions

### Core

- **[OWASP Top 10 for Large Language Model Applications](https://genai.owasp.org/llm-top-10/)** — *documentation · intermediate · learner, tester, developer · free/public*  
  The premier risk taxonomy and awareness standard for applications integrating Large Language Models. It defines critical failure modes including direct and indirect prompt injection, sensitive data leakage, improper output handling, excessive agency, and vector/embedding vulnerabilities, providing core security principles for AI-enabled web features.
- **[RAG Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/RAG_Security_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  An authoritative reference for securing Retrieval-Augmented Generation (RAG) pipelines in enterprise AI applications. It details how RAG redistributes attack surfaces across document ingestion, embedding generation, vector storage, and response generation; establishes access control metadata on individual vector chunks; mandates tenant and data classification isolation in vector databases; and outlines query normalization and output validation controls.
- **[Web Security Academy](https://portswigger.net/web-security)** — *lab · beginner · learner, tester, developer · free/registration-required*  
  A broad, free training platform with guided material and realistic labs across major web vulnerability classes, APIs, identity flaws, protocol issues and newer areas such as LLM/AI attacks. It is useful for learners and authorized testers because practice happens in a safe and legal lab environment rather than on real targets. Some exercises require Burp Suite; the Community Edition is sufficient for many labs, but the account and tooling expectations should be checked per lab.

<a id="rag-isolation"></a>
## RAG

### Core

- **[OWASP Top 10 for Large Language Model Applications](https://genai.owasp.org/llm-top-10/)** — *documentation · intermediate · learner, tester, developer · free/public*  
  The premier risk taxonomy and awareness standard for applications integrating Large Language Models. It defines critical failure modes including direct and indirect prompt injection, sensitive data leakage, improper output handling, excessive agency, and vector/embedding vulnerabilities, providing core security principles for AI-enabled web features.
- **[RAG Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/RAG_Security_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  An authoritative reference for securing Retrieval-Augmented Generation (RAG) pipelines in enterprise AI applications. It details how RAG redistributes attack surfaces across document ingestion, embedding generation, vector storage, and response generation; establishes access control metadata on individual vector chunks; mandates tenant and data classification isolation in vector databases; and outlines query normalization and output validation controls.

<a id="privacy-leakage"></a>
## Privacy

### Core

- **[Practical security implementation guides](https://developer.mozilla.org/en-US/docs/Web/Security/Practical_implementation_guides)** — *documentation · intermediate · developer, tester · free/public*  
  A developer-facing index of practical web security controls, especially transport security and browser-facing headers. It is valuable as a bridge between vulnerability knowledge and implementation because it prioritizes controls such as HTTPS resource loading, HTTPS redirection, HSTS, clickjacking prevention, secure cookies, CORS, CSP, Referrer-Policy and Subresource Integrity. Treat it as an implementation checklist and then read the linked deep guides for each control.
- **[Same-origin policy](https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy)** — *documentation · beginner · learner, tester, developer · free/public*  
  A core browser-security foundation explaining the scheme/host/port origin tuple, cross-origin writes, embedding and reads, and the mechanisms used to relax or communicate across origins. It is required reading before CORS, CSRF, postMessage, browser storage or cross-origin leakage topics.
- **[Set-Cookie header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie)** — *documentation · beginner · learner, tester, developer · free/public*  
  A practical reference for cookie syntax and attributes: Secure, HttpOnly, SameSite, Domain, Path, Expires, Max-Age, prefixes and partitioned cookies. It gives the vocabulary needed before studying sessions, CSRF, browser storage and cookie hardening.
- **[User Privacy Protection Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/User_Privacy_Protection_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  A comprehensive guide for safeguarding user privacy, anonymity, and confidential communications in web applications. It details mitigations against browser tracking, third-party analytics leaks, and surveillance; mandates end-to-end transport and storage encryption; and details client identity protection controls including HTTP Strict Transport Security (HSTS) and cookie partitioning.
- **[XS-Leaks Wiki](https://xsleaks.dev/)** — *documentation · advanced · tester, developer · free/public*  
  The definitive knowledge base on Cross-Site Leaks (XS-Leaks) and web browser side channels. It details how attackers infer sensitive user data across origins without directly violating the Same-Origin Policy, analyzing timing attacks, frame counting, error events, navigation timing, and cache probing, while outlining defense-in-depth protections including Fetch Metadata, COOP, and CORP.

<a id="side-channels"></a>
## Practical Web Side Channels

### Core

- **[Chromium Site Isolation](https://www.chromium.org/Home/chromium-security/site-isolation/)** — *documentation · advanced · tester, developer · free/public*  
  An authoritative technical architectural reference on modern browser process isolation models. It explains how Chromium separates different websites into sandboxed operating system processes, outlines Out-of-Process Iframes (OOPIFs), details Cross-Origin Read Blocking (CORB) preventing delivery of sensitive cross-site HTML/JSON data to untrusted renderers, and explores mitigations against speculative execution side-channel attacks like Spectre.
- **[User Privacy Protection Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/User_Privacy_Protection_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  A comprehensive guide for safeguarding user privacy, anonymity, and confidential communications in web applications. It details mitigations against browser tracking, third-party analytics leaks, and surveillance; mandates end-to-end transport and storage encryption; and details client identity protection controls including HTTP Strict Transport Security (HSTS) and cookie partitioning.
- **[XS-Leaks Wiki](https://xsleaks.dev/)** — *documentation · advanced · tester, developer · free/public*  
  The definitive knowledge base on Cross-Site Leaks (XS-Leaks) and web browser side channels. It details how attackers infer sensitive user data across origins without directly violating the Same-Origin Policy, analyzing timing attacks, frame counting, error events, navigation timing, and cache probing, while outlining defense-in-depth protections including Fetch Metadata, COOP, and CORP.

<a id="abuse-resilience"></a>
## Abuse Prevention & Resilience

### Core

- **[Bot Management and Anti-Automation Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Bot_Management_and_Anti-Automation_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  A practical guide for mitigating automated threats and business-logic abuse across web applications. Grounded in the OWASP Automated Threats to Web Applications project (OAT-001 through OAT-021), it covers defense against credential stuffing (OAT-008), scraping (OAT-011), inventory scalping (OAT-005), and card testing (OAT-001), detailing layered defensive architectures, behavioral anomaly detection, and rate limiting.
- **[GraphQL Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/GraphQL_Cheat_Sheet.html)** — *cheatsheet · intermediate · tester, developer · free/public*  
  A GraphQL-specific security baseline covering schema-driven validation, query depth/amount limits, batching abuse, authorization on edges and nodes, introspection controls and error handling. It is useful because GraphQL concentrates many API risks into fewer network requests and resolver paths.
- **[OWASP API Security Top 10 2023](https://api-security.owasp.org/editions/2023/en/0x11-t10)** — *documentation · beginner · learner, tester, developer · free/public*  
  A high-level risk map for API work. It is not a control guide by itself, but it helps learners and teams orient around object-level authorization, authentication, property-level authorization, resource consumption, function-level authorization, sensitive business flows, SSRF, misconfiguration, inventory and unsafe third-party API consumption.

<a id="testing-methodology"></a>
## Authorized Testing Methodology

### Core

- **[Cross-Site Request Forgery Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  Practical CSRF guidance covering synchronizer tokens, signed double-submit cookies, SameSite limits, custom headers, Fetch Metadata, Origin/Referer checks and user-interaction defenses. It is valuable because it explains when each control fails, including client-side CSRF and XSS defeating CSRF mitigations. Use it after learning cookies and before reviewing state-changing endpoints.
- **[Insecure Direct Object Reference Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Insecure_Direct_Object_Reference_Prevention_Cheat_Sheet.html)** — *cheatsheet · beginner · learner, tester, developer · free/public*  
  Focused guidance for object-level authorization mistakes: object, reference and missing permission check. It is useful for learners because it separates identifier complexity from authorization, for testers because it describes cross-account verification, and for developers because it shows scoped lookup patterns. Treat opaque IDs as defense-in-depth only, never as the primary control.
- **[Threat Modeling Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html)** — *cheatsheet · intermediate · developer, tester · free/public*  
  A structured guide to integrating threat modeling across the software development lifecycle. Grounded in the Threat Modeling Manifesto's four core questions (What are we working on? What can go wrong? What are we going to do about it? Did we do a good enough job?), it details system decomposition via Data Flow Diagrams (DFDs), threat identification using STRIDE per element, and risk mitigation strategies.
- **[Vulnerability Disclosure Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Vulnerability_Disclosure_Cheat_Sheet.html)** — *cheatsheet · beginner · learner, tester, developer · free/public*  
  An authoritative guide to the vulnerability disclosure lifecycle for security researchers, penetration testers, and engineering organizations. It outlines expectations for authorized testing, actionable and reproducible evidence reporting, bug bounty coordination, disclosure timelines, CVE assignment, and coordinated public advisories.
- **[Web Security Academy](https://portswigger.net/web-security)** — *lab · beginner · learner, tester, developer · free/registration-required*  
  A broad, free training platform with guided material and realistic labs across major web vulnerability classes, APIs, identity flaws, protocol issues and newer areas such as LLM/AI attacks. It is useful for learners and authorized testers because practice happens in a safe and legal lab environment rather than on real targets. Some exercises require Burp Suite; the Community Edition is sufficient for many labs, but the account and tooling expectations should be checked per lab.
- **[Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)** — *documentation · intermediate · tester, developer · free/public*  
  A structured methodology reference for web application security testing. It is useful for authorized testers because it organizes assessment work into repeatable categories instead of ad hoc payload use, and useful for developers/AppSec because it translates into test planning and review coverage. Use the project page as the stable entry point, then inspect versioned guide chapters for specific test cases.

<a id="evidence-disclosure"></a>
## Evidence

### Core

- **[Vulnerability Disclosure Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Vulnerability_Disclosure_Cheat_Sheet.html)** — *cheatsheet · beginner · learner, tester, developer · free/public*  
  An authoritative guide to the vulnerability disclosure lifecycle for security researchers, penetration testers, and engineering organizations. It outlines expectations for authorized testing, actionable and reproducible evidence reporting, bug bounty coordination, disclosure timelines, CVE assignment, and coordinated public advisories.
- **[Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)** — *documentation · intermediate · tester, developer · free/public*  
  A structured methodology reference for web application security testing. It is useful for authorized testers because it organizes assessment work into repeatable categories instead of ad hoc payload use, and useful for developers/AppSec because it translates into test planning and review coverage. Use the project page as the stable entry point, then inspect versioned guide chapters for specific test cases.

<a id="practice-labs"></a>
## Labs

### Core

- **[Controlling the Web Message Source](https://portswigger.net/web-security/dom-based/controlling-the-web-message-source)** — *documentation · intermediate · learner, tester, developer · free/public*  
  A practical guide on cross-document messaging security via window.postMessage. It demonstrates how unvalidated event listeners allow attacker-controlled iframes to supply malicious data to execution sinks (eval, innerHTML, location.href), explores common origin validation flaws (indexOf, endsWith), and details robust same-origin validation techniques.
- **[Cross-Site WebSocket Hijacking](https://portswigger.net/web-security/websockets/cross-site-websocket-hijacking)** — *documentation · intermediate · learner, tester, developer · free/public*  
  A definitive guide to Cross-Site WebSocket Hijacking (CSWSH). It explains how ambient cookie authentication during the initial HTTP upgrade handshake enables attackers on malicious origins to establish two-way WebSocket connections to read private user messages or trigger unauthorized actions on the server.
- **[Server-Side Template Injection](https://portswigger.net/web-security/server-side-template-injection)** — *documentation · intermediate · learner, tester, developer · free/public*  
  A foundational guide to Server-Side Template Injection (SSTI) covering detection, identification of template engines, and exploitation risks up to remote code execution. It provides polyglot probe strings, mathematical expression tests to differentiate engines (e.g. Jinja2 vs. Twig), and key defense patterns such as logic-less templates and sandboxed rendering.
- **[Smashing the state machine: the true potential of web race conditions](https://portswigger.net/research/smashing-the-state-machine)** — *article · advanced · learner, tester, developer · free/public*  
  Groundbreaking research demonstrating novel web race condition classes beyond basic limit-overruns, introducing the HTTP/2 single-packet attack to eliminate network jitter and synchronize requests within sub-millisecond windows. It covers multi-endpoint collisions, transient sub-states, and database-level atomic defensive architecture.
- **[The Fragile Lock: Novel Bypasses For SAML Authentication](https://portswigger.net/research/the-fragile-lock)** — *article · advanced · tester, developer · free/public*  
  Cutting-edge security research on SAML 2.0 implementations demonstrating full authentication bypasses via XML Signature Wrapping (XSW), attribute pollution, namespace confusion, and Void Canonicalization. It analyzes parser desynchronization between signature verification and assertion consumer modules (e.g. Nokogiri vs REXML) and details how empty digest strings lead to universal token forgery.
- **[Web Security Academy](https://portswigger.net/web-security)** — *lab · beginner · learner, tester, developer · free/registration-required*  
  A broad, free training platform with guided material and realistic labs across major web vulnerability classes, APIs, identity flaws, protocol issues and newer areas such as LLM/AI attacks. It is useful for learners and authorized testers because practice happens in a safe and legal lab environment rather than on real targets. Some exercises require Burp Suite; the Community Edition is sufficient for many labs, but the account and tooling expectations should be checked per lab.
- **[Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)** — *documentation · intermediate · tester, developer · free/public*  
  A structured methodology reference for web application security testing. It is useful for authorized testers because it organizes assessment work into repeatable categories instead of ad hoc payload use, and useful for developers/AppSec because it translates into test planning and review coverage. Use the project page as the stable entry point, then inspect versioned guide chapters for specific test cases.
