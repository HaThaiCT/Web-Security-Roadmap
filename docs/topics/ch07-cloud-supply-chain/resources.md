<!-- GENERATED FILE: do not edit by hand. Run scripts/generate.py. -->
# Curated Resources — Cloud, Deployment & Supply Chain Security

<a id="cloud-iam"></a>
## Cloud IAM & Application Trust Boundaries

### Core

- **[Architect Multitenant Solutions on Azure](https://learn.microsoft.com/en-us/azure/architecture/guide/multitenant/overview)** — *documentation · advanced · tester, developer · free/public*  
  An authoritative reference architecture for designing multi-tenant software-as-a-service (SaaS) solutions. It establishes clear architectural boundaries between users and tenants, analyzes tenancy models (deployment stamps, siloed vs. pooled compute/storage), details data isolation strategies (database-per-tenant, schema-per-tenant, shared database with Row-Level Security), and covers tenant context propagation across distributed services.
- **[Configuring the Instance Metadata Service (IMDSv2)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html)** — *documentation · intermediate · learner, tester, developer · free/public*  
  Authoritative cloud documentation detailing the security architecture of AWS EC2 Instance Metadata Service Version 2 (IMDSv2). It explains how session-oriented requests, mandatory PUT token generation, custom header requirements, and IP-level hop limit restrictions mitigate Server-Side Request Forgery (SSRF), open reverse proxy bypasses, and unauthorized metadata access.
- **[GitHub Actions Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/GitHub_Actions_Security_Cheat_Sheet.html)** — *cheatsheet · intermediate · developer, tester · free/public*  
  Practical hardening guidelines for GitHub Actions workflows. It addresses high-risk triggers like pull_request_target, GITHUB_TOKEN write-permission compromise, GitHub Actions cache poisoning, artifact tampering, runner egress filtering, and unpinned third-party action vulnerabilities.
- **[Kubernetes Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Kubernetes_Security_Cheat_Sheet.html)** — *cheatsheet · advanced · developer, tester · free/public*  
  A Kubernetes hardening guide for web-backed workloads. It covers API server/RBAC, namespaces, pod security, network policies, secrets, image controls, admission controllers, audit logging, etcd protection and credential rotation.
- **[Secrets Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html)** — *cheatsheet · intermediate · developer, tester · free/public*  
  A broad lifecycle guide for creating, storing, rotating, revoking, auditing and responding to exposed secrets. It is useful for cloud-backed web apps because secrets cross application code, deployment systems, CI/CD, cloud IAM and incident response.
- **[Secure Cloud Architecture Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Secure_Cloud_Architecture_Cheat_Sheet.html)** — *cheatsheet · intermediate · tester, developer · free/public*  
  An architectural guide for designing and reviewing cloud environments hosting web applications. It details cloud IAM trust boundaries, least-privilege role assignment, isolating public from private cloud components, securing object storage access patterns (IAM policies vs. pre-signed URLs vs. public storage), and establishing rigorous threat models for cloud-native web services.
- **[Server Side Request Forgery Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  A practical defensive baseline for SSRF and URL-processing risk. It separates allowlisted internal destinations from open external fetch features, explains why deny-lists and parser assumptions are fragile, and connects application validation to network-layer egress controls and cloud metadata protection.
- **[The Twelve-Factor App](https://12factor.net/)** — *documentation · beginner · learner, tester, developer · free/public*  
  The foundational architectural methodology for building software-as-a-service and cloud-native web applications. It establishes essential architectural boundaries: separating configuration from code (environment variables), treating backing services (databases, queues, caches) as attached resources, strictly isolating build/release/run stages, and executing applications as stateless processes.

<a id="storage-secrets"></a>
## Object Storage & Secrets

### Core

- **[Configuring the Instance Metadata Service (IMDSv2)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html)** — *documentation · intermediate · learner, tester, developer · free/public*  
  Authoritative cloud documentation detailing the security architecture of AWS EC2 Instance Metadata Service Version 2 (IMDSv2). It explains how session-oriented requests, mandatory PUT token generation, custom header requirements, and IP-level hop limit restrictions mitigate Server-Side Request Forgery (SSRF), open reverse proxy bypasses, and unauthorized metadata access.
- **[Cryptographic Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  A practical guide for implementing secure data storage encryption in web backends. It establishes standards for authenticated encryption (AEAD like AES-GCM), key separation, cryptographically secure pseudorandom number generators (CSPRNG), and distinguishes reversible data encryption from memory-hard password hashing (Argon2id, scrypt, bcrypt).
- **[Database Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Database_Security_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  An architectural guide for securing backend database instances in web applications. It details database isolation on dedicated network segments, least-privilege application accounts (limiting permissions to SELECT/INSERT/UPDATE rather than administrative superusers), host-based access controls, and mandating TLS 1.2+ encryption in transit between application servers and database instances.
- **[Docker Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Docker_Security_Cheat_Sheet.html)** — *cheatsheet · intermediate · developer, tester · free/public*  
  A container hardening baseline for web deployments using Docker. It emphasizes non-root execution, capability reduction, no-new-privileges, secrets handling, image pinning/signing/SBOMs, network exposure, logging and resource limits.
- **[File Path Traversal](https://portswigger.net/web-security/file-path-traversal)** — *documentation · beginner · learner, tester, developer · free/public*  
  A clear guide to path traversal vulnerabilities that allow reading or writing arbitrary files on the server filesystem. It covers dot-dot-slash (../) directory navigation, common filter bypasses such as nested sequences and URL encoding, and establishes canonical path verification as the primary defense.
- **[File Upload Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  A defensive baseline for accepting user-supplied files without treating file extension or Content-Type as sufficient proof of safety. It is useful for developers and testers because it ties upload validation, filename handling, storage location, permissions, content processing and size limits into one review model.
- **[GitHub Actions Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/GitHub_Actions_Security_Cheat_Sheet.html)** — *cheatsheet · intermediate · developer, tester · free/public*  
  Practical hardening guidelines for GitHub Actions workflows. It addresses high-risk triggers like pull_request_target, GITHUB_TOKEN write-permission compromise, GitHub Actions cache poisoning, artifact tampering, runner egress filtering, and unpinned third-party action vulnerabilities.
- **[Infrastructure as Code Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Infrastructure_as_Code_Security_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  A practical guide for integrating security into Infrastructure as Code (IaC) templates and pipelines. It covers static analysis of Terraform, CloudFormation, and Dockerfiles, automated secrets detection in version control, least-privilege provisioning policies, immutable infrastructure deployment patterns, and tagging strategies to prevent ghost cloud resources.
- **[Kubernetes Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Kubernetes_Security_Cheat_Sheet.html)** — *cheatsheet · advanced · developer, tester · free/public*  
  A Kubernetes hardening guide for web-backed workloads. It covers API server/RBAC, namespaces, pod security, network policies, secrets, image controls, admission controllers, audit logging, etcd protection and credential rotation.
- **[OWASP Top 10 CI/CD Security Risks](https://owasp.org/www-project-top-10-ci-cd-security-risks/)** — *specification · intermediate · developer, tester · free/public*  
  The industry-standard risk taxonomy for continuous integration and delivery ecosystems. It covers ten critical attack vectors including Insufficient Flow Control Mechanisms, Poisoned Pipeline Execution (PPE), Dependency Chain Abuse, Insufficient Credential Hygiene, and Artifact Integrity Validation failures.
- **[Redis Security Model and Guidelines](https://redis.io/docs/latest/operate/oss_and_stack/management/security/)** — *documentation · intermediate · tester, developer · free/public*  
  The official architectural guide to Redis's security model, access control, and network isolation. It explains that Redis is designed for trusted internal network access, detailing the severe risks of internet-exposed instances (unauthenticated data deletion via FLUSHALL, unauthorized key access), protected mode mechanics, configuring strict bind interfaces, and deploying Role-Based Access Control (ACLs) to enforce least-privilege operations between web backends, caches, and queues.
- **[Secrets Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html)** — *cheatsheet · intermediate · developer, tester · free/public*  
  A broad lifecycle guide for creating, storing, rotating, revoking, auditing and responding to exposed secrets. It is useful for cloud-backed web apps because secrets cross application code, deployment systems, CI/CD, cloud IAM and incident response.
- **[Secure Cloud Architecture Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Secure_Cloud_Architecture_Cheat_Sheet.html)** — *cheatsheet · intermediate · tester, developer · free/public*  
  An architectural guide for designing and reviewing cloud environments hosting web applications. It details cloud IAM trust boundaries, least-privilege role assignment, isolating public from private cloud components, securing object storage access patterns (IAM policies vs. pre-signed URLs vs. public storage), and establishing rigorous threat models for cloud-native web services.
- **[The Twelve-Factor App](https://12factor.net/)** — *documentation · beginner · learner, tester, developer · free/public*  
  The foundational architectural methodology for building software-as-a-service and cloud-native web applications. It establishes essential architectural boundaries: separating configuration from code (environment variables), treating backing services (databases, queues, caches) as attached resources, strictly isolating build/release/run stages, and executing applications as stateless processes.

<a id="metadata-serverless"></a>
## Metadata Services & Serverless

### Core

- **[Configuring the Instance Metadata Service (IMDSv2)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html)** — *documentation · intermediate · learner, tester, developer · free/public*  
  Authoritative cloud documentation detailing the security architecture of AWS EC2 Instance Metadata Service Version 2 (IMDSv2). It explains how session-oriented requests, mandatory PUT token generation, custom header requirements, and IP-level hop limit restrictions mitigate Server-Side Request Forgery (SSRF), open reverse proxy bypasses, and unauthorized metadata access.
- **[Secure Cloud Architecture Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Secure_Cloud_Architecture_Cheat_Sheet.html)** — *cheatsheet · intermediate · tester, developer · free/public*  
  An architectural guide for designing and reviewing cloud environments hosting web applications. It details cloud IAM trust boundaries, least-privilege role assignment, isolating public from private cloud components, securing object storage access patterns (IAM policies vs. pre-signed URLs vs. public storage), and establishing rigorous threat models for cloud-native web services.
- **[Server Side Request Forgery Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  A practical defensive baseline for SSRF and URL-processing risk. It separates allowlisted internal destinations from open external fetch features, explains why deny-lists and parser assumptions are fragile, and connects application validation to network-layer egress controls and cloud metadata protection.

<a id="web-server-proxies"></a>
## Web Servers & Reverse Proxy Hardening

### Core

- **[Docker Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Docker_Security_Cheat_Sheet.html)** — *cheatsheet · intermediate · developer, tester · free/public*  
  A container hardening baseline for web deployments using Docker. It emphasizes non-root execution, capability reduction, no-new-privileges, secrets handling, image pinning/signing/SBOMs, network exposure, logging and resource limits.
- **[HTTP Desync Attacks: Request Smuggling Reborn](https://portswigger.net/research/http-desync-attacks-request-smuggling-reborn)** — *article · advanced · learner, tester, developer · free/public*  
  Foundational research on HTTP request smuggling against modern multi-tier web architectures. It explains CL.TE, TE.CL, and obfuscated Transfer-Encoding desynchronization between front-end reverse proxies and back-end servers, providing non-destructive detection probes and architectural mitigations including end-to-end HTTP/2 and request normalization.
- **[HTTP Headers Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/HTTP_Headers_Cheat_Sheet.html)** — *cheatsheet · beginner · learner, tester, developer · free/public*  
  An authoritative reference for hardening web servers, reverse proxies, and edge gateways using HTTP security headers. It provides concise implementation recommendations for X-Frame-Options, X-Content-Type-Options (nosniff), Strict-Transport-Security (HSTS), Content-Security-Policy (CSP), Referrer-Policy, and Permissions-Policy, explaining how edge reverse proxies can uniformly inject baseline defenses across diverse application backends.
- **[HTTP Host Header Attacks](https://portswigger.net/web-security/host-header)** — *documentation · intermediate · learner, tester, developer · free/public*  
  A comprehensive guide to vulnerabilities resulting from implicit trust in the HTTP Host header. It explores how intermediary proxies, reverse proxies, and backend application servers desynchronize routing, detailing password reset poisoning, routing-based SSRF, web cache poisoning, and authentication bypasses, along with remediation via strict Host allowlisting.
- **[Practical Web Cache Poisoning](https://portswigger.net/research/practical-web-cache-poisoning)** — *article · advanced · tester, developer · free/public*  
  Pioneering research establishing web cache poisoning as a practical vulnerability class. It details how unkeyed HTTP headers (such as X-Forwarded-Host or custom headers) can be exploited to store malicious payloads on high-traffic endpoints, providing detection methodologies and cache key auditing principles.
- **[RFC 9110: HTTP Semantics — Section 17 Security Considerations](https://www.rfc-editor.org/rfc/rfc9110.html)** — *specification · intermediate · learner, tester, developer · free/public*  
  The definitive IETF standard defining the core semantics of the Hypertext Transfer Protocol. Section 17 provides an authoritative security breakdown of establishing authority (DNS/TLS vs. plaintext HTTP), the risks of intermediary proxies and gateways, header parsing hazards, handling oversized protocol elements, and sensitive information leakage in URIs, Referer headers, and server software identifiers.
- **[Server Side Request Forgery Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  A practical defensive baseline for SSRF and URL-processing risk. It separates allowlisted internal destinations from open external fetch features, explains why deny-lists and parser assumptions are fragile, and connects application validation to network-layer egress controls and cloud metadata protection.
- **[Transport Layer Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Security_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  An authoritative reference for securing transport encryption across modern web architectures. It mandates TLS 1.3 and 1.2 with AEAD cipher suites, explains the formal deprecation of TLS 1.0 and 1.1 (RFC 8996), covers Forward Secrecy (ECDHE), and details deployment controls including HTTP Strict Transport Security (HSTS), CAA DNS records, and disabling insecure renegotiation and compression.
- **[Virtual Patching Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Virtual_Patching_Cheat_Sheet.html)** — *cheatsheet · intermediate · tester, developer · free/public*  
  A concise framework for rapid vulnerability mitigation during active incident response and zero-day disclosures. It explains how security policy enforcement layers (WAFs, reverse proxy filters) intercept exploit attempts in transit to buy critical remediation time while developers write, test, and deploy permanent source code fixes.
- **[Web Cache Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Web_Cache_Security_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  A comprehensive defensive guide on preventing sensitive response exposure, web cache poisoning, and web cache deception. It defines cache key mechanics, unkeyed input hazards, delimiter and path confusion, and specifies rigorous defenses including Cache-Control: no-store, private directives, and Content-Type validation.
- **[WebSocket Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/WebSocket_Security_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  A comprehensive guide to securing real-time bidirectional WebSocket connections. It breaks down Cross-Site WebSocket Hijacking (CSWSH), handshake authentication, origin header validation, message-level authorization, permessage-deflate compression risks, and denial-of-service protections including backpressure and rate limiting.

<a id="containers-kubernetes"></a>
## Containers & Kubernetes

### Core

- **[Docker Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Docker_Security_Cheat_Sheet.html)** — *cheatsheet · intermediate · developer, tester · free/public*  
  A container hardening baseline for web deployments using Docker. It emphasizes non-root execution, capability reduction, no-new-privileges, secrets handling, image pinning/signing/SBOMs, network exposure, logging and resource limits.
- **[Kubernetes Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Kubernetes_Security_Cheat_Sheet.html)** — *cheatsheet · advanced · developer, tester · free/public*  
  A Kubernetes hardening guide for web-backed workloads. It covers API server/RBAC, namespaces, pod security, network policies, secrets, image controls, admission controllers, audit logging, etcd protection and credential rotation.
- **[The Twelve-Factor App](https://12factor.net/)** — *documentation · beginner · learner, tester, developer · free/public*  
  The foundational architectural methodology for building software-as-a-service and cloud-native web applications. It establishes essential architectural boundaries: separating configuration from code (environment variables), treating backing services (databases, queues, caches) as attached resources, strictly isolating build/release/run stages, and executing applications as stateless processes.

<a id="infrastructure-code"></a>
## Infrastructure as Code

### Core

- **[Infrastructure as Code Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Infrastructure_as_Code_Security_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  A practical guide for integrating security into Infrastructure as Code (IaC) templates and pipelines. It covers static analysis of Terraform, CloudFormation, and Dockerfiles, automated secrets detection in version control, least-privilege provisioning policies, immutable infrastructure deployment patterns, and tagging strategies to prevent ghost cloud resources.

<a id="cicd-security"></a>
## CI/CD Permissions & Pipeline Security

### Core

- **[GitHub Actions Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/GitHub_Actions_Security_Cheat_Sheet.html)** — *cheatsheet · intermediate · developer, tester · free/public*  
  Practical hardening guidelines for GitHub Actions workflows. It addresses high-risk triggers like pull_request_target, GITHUB_TOKEN write-permission compromise, GitHub Actions cache poisoning, artifact tampering, runner egress filtering, and unpinned third-party action vulnerabilities.
- **[Infrastructure as Code Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Infrastructure_as_Code_Security_Cheat_Sheet.html)** — *cheatsheet · intermediate · learner, tester, developer · free/public*  
  A practical guide for integrating security into Infrastructure as Code (IaC) templates and pipelines. It covers static analysis of Terraform, CloudFormation, and Dockerfiles, automated secrets detection in version control, least-privilege provisioning policies, immutable infrastructure deployment patterns, and tagging strategies to prevent ghost cloud resources.
- **[Kubernetes Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Kubernetes_Security_Cheat_Sheet.html)** — *cheatsheet · advanced · developer, tester · free/public*  
  A Kubernetes hardening guide for web-backed workloads. It covers API server/RBAC, namespaces, pod security, network policies, secrets, image controls, admission controllers, audit logging, etcd protection and credential rotation.
- **[OWASP Top 10 CI/CD Security Risks](https://owasp.org/www-project-top-10-ci-cd-security-risks/)** — *specification · intermediate · developer, tester · free/public*  
  The industry-standard risk taxonomy for continuous integration and delivery ecosystems. It covers ten critical attack vectors including Insufficient Flow Control Mechanisms, Poisoned Pipeline Execution (PPE), Dependency Chain Abuse, Insufficient Credential Hygiene, and Artifact Integrity Validation failures.
- **[SLSA v1.1 — About SLSA](https://slsa.dev/spec/v1.1/about)** — *specification · intermediate · developer, tester · free/public*  
  A supply-chain security framework for reasoning about source, build, packaging and provenance. For this repository, it is most useful when explaining why build evidence and artifact provenance matter for web applications and deployment pipelines.
- **[Secrets Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html)** — *cheatsheet · intermediate · developer, tester · free/public*  
  A broad lifecycle guide for creating, storing, rotating, revoking, auditing and responding to exposed secrets. It is useful for cloud-backed web apps because secrets cross application code, deployment systems, CI/CD, cloud IAM and incident response.

### Extended

- **[OWASP Dependency-Track](https://owasp.org/www-project-dependency-track/)** — *tool · intermediate · developer, tester · free/public*  
  A mature SBOM and component-risk tracking platform. It is a useful extended resource for teams operationalizing dependency visibility, vulnerability matching, policy enforcement and alerting across many projects, but it is a tool choice rather than foundational reading for every learner.

<a id="dependencies-artifacts"></a>
## Dependencies

### Core

- **[Docker Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Docker_Security_Cheat_Sheet.html)** — *cheatsheet · intermediate · developer, tester · free/public*  
  A container hardening baseline for web deployments using Docker. It emphasizes non-root execution, capability reduction, no-new-privileges, secrets handling, image pinning/signing/SBOMs, network exposure, logging and resource limits.
- **[GitHub Actions Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/GitHub_Actions_Security_Cheat_Sheet.html)** — *cheatsheet · intermediate · developer, tester · free/public*  
  Practical hardening guidelines for GitHub Actions workflows. It addresses high-risk triggers like pull_request_target, GITHUB_TOKEN write-permission compromise, GitHub Actions cache poisoning, artifact tampering, runner egress filtering, and unpinned third-party action vulnerabilities.
- **[OWASP Top 10 CI/CD Security Risks](https://owasp.org/www-project-top-10-ci-cd-security-risks/)** — *specification · intermediate · developer, tester · free/public*  
  The industry-standard risk taxonomy for continuous integration and delivery ecosystems. It covers ten critical attack vectors including Insufficient Flow Control Mechanisms, Poisoned Pipeline Execution (PPE), Dependency Chain Abuse, Insufficient Credential Hygiene, and Artifact Integrity Validation failures.
- **[SLSA v1.1 — About SLSA](https://slsa.dev/spec/v1.1/about)** — *specification · intermediate · developer, tester · free/public*  
  A supply-chain security framework for reasoning about source, build, packaging and provenance. For this repository, it is most useful when explaining why build evidence and artifact provenance matter for web applications and deployment pipelines.

### Extended

- **[OWASP Dependency-Track](https://owasp.org/www-project-dependency-track/)** — *tool · intermediate · developer, tester · free/public*  
  A mature SBOM and component-risk tracking platform. It is a useful extended resource for teams operationalizing dependency visibility, vulnerability matching, policy enforcement and alerting across many projects, but it is a tool choice rather than foundational reading for every learner.
