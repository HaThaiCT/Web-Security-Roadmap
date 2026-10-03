# Cloud, Deployment & Supply Chain Security

This authored overview is organized by topic. Curated resource lists are generated separately in [resources.md](resources.md).

## How to use this part

Use this as a reference section, not as a mandatory linear course. Learning paths link to the topics and resources that fit each role.

<a id="cloud-iam"></a>
## Cloud IAM & Application Trust Boundaries

### Prerequisites

Understand cloud identity and access management (AWS IAM, GCP Cloud IAM, Azure RBAC), principles of least privilege, machine identities vs. human identities, trust policies, resource-based policies, and cloud network boundaries (VPCs, security groups, private endpoints).

### Mechanism and mental model

In cloud-native web architectures, security is fundamentally identity-centric rather than perimeter-centric. Traditional data centers relied heavily on static network perimeters and firewalls, but modern web applications operate as distributed services interacting with managed relational databases, object storage, serverless compute, message queues, and external SaaS endpoints—with every interaction governed by Cloud Identity and Access Management (IAM) policies.

1. **Machine Identities & Short-Lived Credentials:**
   Web workloads running in the cloud should never utilize long-lived static API access keys stored in environment variables or configuration files. Instead, compute services (EC2 instances, ECS tasks, Kubernetes pods, Lambda functions) assume ephemeral machine identities (AWS IAM Roles, GCP Service Accounts, Azure Managed Identities). The cloud hypervisor issues temporary credentials via STS (Security Token Service) that automatically rotate.
2. **Trust Policies vs. Permission Policies:**
   An IAM role requires two distinct policy layers:
   - **Trust Policy (AssumeRole Policy):** Defines *who* is allowed to assume the role (e.g. `ec2.amazonaws.com` or a specific OIDC federated identity provider). Confused deputy problems occur when third-party services can assume roles without verifying an external ID or specific account identifier.
   - **Permission Policy:** Defines *what* API actions the assumed role can perform against which cloud resource ARNs.
3. **Public vs. Private Storage Boundaries:**
   Cloud-hosted web applications frequently handle user file uploads and asset distribution. The architecture must carefully evaluate object storage (S3, GCS) access models:
   - *Direct Public Access:* Buckets configured with public read access allow direct internet retrieval but risk catastrophic data exposure if private buckets are misconfigured.
   - *Pre-Signed URLs:* The backend web application authenticates the user, verifies object-level authorization (preventing IDOR), and generates a cryptographically signed URL with a short TTL (e.g. 15 minutes) and a restricted HTTP method (`GET` or `PUT`). The client transfers data directly to/from cloud storage, preserving server memory while maintaining authorization boundaries.
   - *Origin Access Control (OAC):* CloudFront/CDN distributions access private S3 buckets using signed requests, ensuring users cannot bypass edge WAF and caching rules to query storage directly.
4. **Privilege Escalation & Lateral Movement Vectors:**
   Overly permissive IAM policies allow attackers who achieve remote code execution (RCE) or SSRF in a web application to escalate privileges within the cloud environment:
   - `iam:PassRole` combined with compute creation (`ec2:RunInstances` or `lambda:CreateFunction`): An attacker attaches an existing high-privilege IAM role to a newly spawned instance, bypassing permission boundaries.
   - `iam:CreatePolicyVersion` or `iam:SetDefaultPolicyVersion`: Allows an attacker to overwrite an attached policy to grant `AdministratorAccess` (`*` on `*`).
   - Broad wildcard permissions (`s3:*` on `*`): Allows a compromised frontend service to discover and exfiltrate database backups or logs stored in unrelated buckets within the same account.

### Practical learning notes

In authorized cloud penetration tests, architecture reviews, and code audits:
- Audit IAM policies using open-source analyzers (`parliament`, `policy_sentry`, `prowler`, `ScoutSuite`) to identify wildcard actions and privilege escalation paths.
- Inspect application source code and deployment manifests to verify that static cloud credentials (`AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`) are not hardcoded or committed to version control.
- Check object storage configuration: Verify that cloud accounts enforce account-wide S3 Block Public Access.
- Test object upload/download workflows: Inspect whether pre-signed URLs enforce appropriate expiration times and strictly bind to specific object paths.

### Defensive and engineering notes

1. **Enforce Least Privilege IAM:** Scope permissions to specific resource ARNs rather than `Resource: "*"`. Restrict actions to specific APIs (`s3:GetObject`, `s3:PutObject`) rather than wildcards (`s3:*`).
2. **Mandate Ephemeral Workload Identities:** Enforce the use of instance metadata roles, IRSA (IAM Roles for Service Accounts in Kubernetes), or Workload Identity Federation instead of static, long-lived credentials.
3. **Deploy Account-Wide Public Access Blocks:** Enable account-wide S3 Block Public Access and apply Organization Service Control Policies (SCPs) to prevent developers or IaC scripts from creating publicly readable buckets.
4. **Enforce Transport Encryption in Resource Policies:** Include explicit `Deny` statements in bucket and queue policies for any requests where `aws:SecureTransport` is false.
5. **Implement Permission Boundaries:** Attach IAM Permission Boundaries to developer roles to mathematically restrict the maximum permissions that can ever be delegated to created roles.

### Reading order

1. Read [OWASP — Secure Cloud Architecture Cheat Sheet](resources.md#cloud-iam).
2. Cross-reference with Chapter 7 Metadata Services & Serverless and Object Storage & Secrets.

<a id="storage-secrets"></a>
## Object Storage & Secrets

### Prerequisites

Understand environment configuration, deployment pipelines, cloud IAM basics and the difference between application secrets, user credentials, tokens and encryption keys.

### Mechanism and mental model

Secrets are lifecycle-managed assets, not strings to hide in configuration. They are created, distributed, used, rotated, revoked, expired, audited and eventually destroyed. Web applications often expose secrets through source code, container images, CI logs, environment variables, object storage, crash reports, client bundles or overly broad cloud roles.

Object storage and secret storage are related because both depend on identity, policy and metadata. A secret without ownership, rotation schedule and audit trail becomes difficult to revoke safely during an incident.

### Practical learning notes

When reviewing an owned system, inventory where secrets originate, where they are stored, which workloads can read them, how they rotate, where they may be logged and how exposure would be contained. Do not search for or open real secrets unless the review scope explicitly authorizes it; record paths and control gaps without exposing values.

### Defensive and engineering notes

Use dedicated secrets managers, least-privilege access policies, environment separation, metadata ownership, automated rotation where possible, tamper-resistant logs and tested incident procedures. Avoid storing keys beside encrypted secrets, avoid hardcoding in source/images, prevent pipeline logs from leaking values and make revocation/rotation a rehearsed operational path.

### Reading order

1. Read [OWASP Secrets Management Cheat Sheet](resources.md#storage-secrets).
2. Then add cloud-provider-specific object storage and IAM sources in later passes.
3. Pair with CI/CD and incident-remediation topics.

<a id="metadata-serverless"></a>
## Metadata Services & Serverless

### Prerequisites

Understand cloud computing architecture (AWS EC2, GCP Compute Engine, Azure VMs), Server-Side Request Forgery (SSRF), instance identity roles, network routing to non-routable link-local IP addresses (`169.254.169.254`), and serverless execution models (AWS Lambda, Google Cloud Functions).

### Mechanism and mental model

In cloud environments, compute workloads dynamically retrieve credentials, configuration, and instance identity from a local hypervisor service known as the **Instance Metadata Service (IMDS)**, typically bound to the link-local IPv4 address `169.254.169.254` (or IPv6 `fd00:ec2::254`).

1. **The IMDS Attack Surface & SSRF Chains:**
   Historically, under AWS IMDSv1, an attacker who discovered a Server-Side Request Forgery (SSRF) flaw in a web application could issue a simple HTTP GET request to:
   ```http
   GET http://169.254.169.254/latest/meta-data/iam/security-credentials/<role-name> HTTP/1.1
   ```
   The service would return temporary IAM security credentials (`AccessKeyId`, `SecretAccessKey`, `Token`), allowing the attacker to assume the instance's cloud role from outside the cloud environment.
2. **IMDSv2 Defense Architecture:**
   AWS introduced IMDSv2 to fundamentally disrupt SSRF exploitation chains by transforming metadata access into a session-oriented flow:
   - **Session Token Requirement:** Callers must first establish a session by issuing an HTTP `PUT` request to `/latest/api/token` with the header `X-aws-ec2-metadata-token-ttl-seconds: <seconds>` (e.g. 21600).
   - **Subsequent Requests:** All subsequent GET requests must supply the acquired token via the `X-aws-ec2-metadata-token` header.
   - **Header & Proxy Blocking:** IMDSv2 explicitly rejects `PUT` requests that contain `X-Forwarded-For` headers. Because many open reverse proxies and naive HTTP forwarders automatically append `X-Forwarded-For`, they cannot be abused to fetch session tokens.
   - **Network Hop Limit (TTL Enforcement):** IMDSv2 allows configuring an IP packet hop limit (TTL = 1). When set to 1, any packet traversing an internal network boundary—such as from a Docker container bridge network or a Kubernetes pod to the host EC2 instance—is dropped because its TTL decrements to 0. This stops container breakout to host metadata.
3. **Serverless Execution Security:**
   Serverless functions run ephemeral micro-VMs or containers. IAM permissions should be scoped down to individual functions rather than shared service accounts. Secrets should be retrieved at cold start from managed secrets stores rather than baked into deployment packages or plaintext environment variables.

### Practical learning notes

In authorized cloud assessments and code audits:
- Audit EC2 metadata options via the AWS CLI or Terraform:
  ```bash
  aws ec2 describe-instances --query "Reservations[*].Instances[*].[InstanceId,MetadataOptions.HttpTokens,MetadataOptions.HttpPutResponseHopLimit]"
  ```
- Look for instances where `HttpTokens` is still set to `optional` (IMDSv1 enabled) rather than `required` (IMDSv2 enforced).
- Inspect containerized workloads running on EC2: If `HttpPutResponseHopLimit` is 1, test whether containerized processes can reach the host IMDS endpoint.

### Defensive and engineering notes

1. **Enforce IMDSv2 Globally:** Require IMDSv2 on all EC2 instances by configuring `HttpTokens=required`. Use AWS Organizations Service Control Policies (SCPs) to deny the launch of any instance that does not enforce IMDSv2:
   ```json
   {
     "Effect": "Deny",
     "Action": "ec2:RunInstances",
     "Resource": "arn:aws:ec2:*:*:instance/*",
     "Condition": {
       "StringNotEquals": { "ec2:MetadataHttpTokens": "required" }
     }
   }
   ```
2. **Restrict Hop Limit to 1:** On instances running container runtimes, set `HttpPutResponseHopLimit=1` to prevent containers from querying host-level instance metadata.
3. **Disable Metadata When Unneeded:** If a compute instance does not require an IAM role or instance metadata access, disable the HTTP endpoint entirely (`HttpEndpoint=disabled`).
4. **Least-Privilege Function IAM Roles:** In serverless architectures, give each function a discrete IAM role granting only the precise actions and resources needed for that function's specific task.

### Reading order

1. Read [AWS — Configuring the Instance Metadata Service (IMDSv2)](resources.md#metadata-serverless).
2. Cross-reference with Chapter 4 Server-Side Request Forgery (SSRF) and Chapter 7 Object Storage & Secrets.

<a id="web-server-proxies"></a>
## Web Servers & Reverse Proxy Hardening

### Prerequisites

Understand reverse proxy and web server architectures (Nginx, Envoy, Apache HTTP Server, HAProxy, Cloudflare, AWS ALB), HTTP request and response headers, TLS termination, virtual hosting mechanics, and modern browser security policies (Chapters 1 and 5).

### Mechanism and mental model

Reverse proxies and edge gateways reside between the public internet and backend web application services. They terminate client TLS connections, route traffic based on Host headers and URL paths, balance backend loads, enforce rate limiting, and standardize security policies across heterogeneous downstream microservices.

1. **Centralized Edge Security Header Injection:**
   While individual backend microservices (Node.js, Python, Go, Java, Ruby) may vary in their header handling, reverse proxies can uniformly inject security headers across every outbound HTTP response:
   - `X-Frame-Options: DENY` or `Content-Security-Policy: frame-ancestors 'none'`: Prevents clickjacking by instructing modern browsers never to render the page within an `<iframe>`, `<frame>`, `<embed>`, or `<object>`.
   - `X-Content-Type-Options: nosniff`: Instructs browsers to strictly honor the declared `Content-Type` header and disables MIME-type sniffing, preventing executable scripts from being extracted from benign image or text uploads.
   - `Strict-Transport-Security: max-age=31536000; includeSubDomains; preload`: Enforces strict HTTPS connections, preventing SSL-stripping attacks on all future client visits.
   - `Referrer-Policy: strict-origin-when-cross-origin`: Restricts referrer headers to origin-only for cross-origin requests and completely strips referrer data when navigating from HTTPS to HTTP.
   - `Permissions-Policy: geolocation=(), camera=(), microphone=()`: Restricts browser access to sensitive client-side device hardware APIs.
   - `X-XSS-Protection: 0`: Explicitly disables legacy, buggy browser XSS auditors that can introduce new client-side vulnerabilities.
2. **Server Banner Masking & Fingerprint Reduction:**
   Default web server and proxy installations broadcast verbose server identification banners: `Server: nginx/1.18.0`, `Server: Apache/2.4.41 (Ubuntu)`, `X-Powered-By: Express`. Attackers use these banners for automated reconnaissance and targeted CVE exploitation. Proxies must strip or redact internal runtime banners while standardizing external response headers.
3. **Upstream Request Sanitization & Header Spoofing:**
   Reverse proxies pass client metadata to backends via headers such as `X-Forwarded-For`, `X-Forwarded-Proto`, and `X-Forwarded-Host`. If a reverse proxy blindly appends to or trusts client-supplied headers without overwriting them, an attacker can spoof client IP addresses (bypassing IP allowlists or rate limits) or trigger cache poisoning and host header attacks.
4. **Buffer Sizing, Connection Timeouts, and DoS Mitigation:**
   Edge proxies defend internal application event loops and thread pools from resource exhaustion attacks (such as Slowloris):
   - Enforcing strict request body limits (`client_max_body_size`) to prevent out-of-memory crashes from oversized uploads.
   - Setting aggressive header and body timeouts (`client_header_timeout`, `client_body_timeout`) to terminate slow-drip HTTP connections.
   - Applying token-bucket or leaky-bucket rate limiting zones to throttle abusive clients before requests consume backend database connections.

### Practical learning notes

In authorized penetration tests, configuration audits, and security reviews:
- Inspect HTTP response headers using `curl`:
  ```bash
  curl -sI https://target.example | grep -iE "x-frame|content-security|strict-transport|x-content-type|server|x-powered-by"
  ```
- Test header spoofing and proxy trust: Send requests with spoofed headers (e.g. `X-Forwarded-For: 127.0.0.1`, `X-Forwarded-Proto: http`) to verify whether the reverse proxy sanitizes or blindly forwards client-injected headers.
- Test request body limits: Submit requests exceeding expected payload boundaries to verify that the reverse proxy returns `413 Payload Too Large` at the edge rather than passing large payloads to the backend application runtime.

### Defensive and engineering notes

1. **Inject Hardening Headers at the Edge:** Configure reverse proxies (Nginx, Traefik, HAProxy, CloudFront) to inject standard security response headers across all HTTP responses.
2. **Disable Server Version Banners:**
   - Nginx: `server_tokens off;`
   - Apache: `ServerTokens Prod` and `ServerSignature Off`
   - Backends: Disable framework banners (e.g. `app.disable('x-powered-by')` in Express).
3. **Overwrite Client Forwarding Headers:** Configure reverse proxies to overwrite untrusted client routing headers rather than appending to them:
   ```nginx
   proxy_set_header X-Forwarded-For $remote_addr;
   proxy_set_header X-Forwarded-Proto $scheme;
   proxy_set_header Host $host;
   ```
4. **Configure Rate Limiting & Buffer Controls:** Implement rate limiting zones on authentication endpoints (`limit_req_zone` in Nginx) and enforce reasonable `client_max_body_size` boundaries.

### Reading order

1. Read [OWASP — HTTP Headers Cheat Sheet](resources.md#web-server-proxies).
2. Cross-reference with Chapter 1 Browser Security Model and Chapter 5 HTTP Headers, Smuggling & Redirects.

<a id="containers-kubernetes"></a>
## Containers & Kubernetes

### Prerequisites

Understand Linux process isolation at a high level, container images, deployment manifests and the difference between application code, runtime configuration and infrastructure policy.

### Mechanism and mental model

Containers package and run web workloads, but they also create new trust boundaries: image provenance, runtime privileges, filesystem writes, secrets injection, network exposure, orchestration API access and cluster policy. Kubernetes adds a control plane where API permissions, admission, pod security, namespaces, network policy and audit logging determine what workloads and users can do.

Do not treat a container as a security boundary by default. Hardening is about reducing what the workload can do after compromise and ensuring the platform rejects unsafe defaults before deployment.

### Practical learning notes

Review manifests and Dockerfiles before running anything. In owned environments, inspect user/root settings, capabilities, privileged mode, mounted sockets, exposed ports, writable filesystems, secrets delivery, resource limits and image sources. Avoid running public images or PoCs just to understand a write-up.

### Defensive and engineering notes

Run as non-root, drop capabilities, avoid privileged mode and Docker socket mounts, use read-only filesystems where feasible, set resource limits, pin and scan images, generate SBOMs, enforce pod security, restrict Kubernetes RBAC, enable network policies, protect etcd, encrypt secrets and collect audit logs.

### Reading order

1. Read [OWASP Docker Security Cheat Sheet](resources.md#containers-kubernetes) for container runtime and image basics.
2. Read [OWASP Kubernetes Security Cheat Sheet](resources.md#containers-kubernetes) for orchestration controls.
3. Pair with secrets management and supply-chain provenance resources.

<a id="infrastructure-code"></a>
## Infrastructure as Code

### Prerequisites

Understand declarative infrastructure tooling (Terraform, OpenTofu, AWS CloudFormation, Pulumi, Kubernetes YAML manifests), container configuration (Dockerfiles), CI/CD pipelines, and cloud security compliance baselines (CIS Benchmarks).

### Mechanism and mental model

Infrastructure as Code (IaC) defines cloud environments, networks, compute instances, storage buckets, and IAM roles as version-controlled code. This programmatic definition shifts infrastructure configuration from manual console operations ("ClickOps") into standard software development workflows.

1. **IaC as a Security Enabler vs. Risk Multiplier:**
   - *Enabler:* IaC creates immutable, reproducible, auditable environments where security baselines can be declared once and automatically enforced across thousands of cloud resources.
   - *Risk Multiplier:* A single insecure default in an IaC template (e.g. `cidr_blocks = ["0.0.0.0/0"]` on an SSH/RDP security group, or `acl = "public-read"` on an S3 bucket) is propagated across all deployed environments, creating pervasive, automated vulnerabilities.
2. **Static Analysis of IaC (Shift-Left Linting):**
   Rather than discovering misconfigurations post-deployment via cloud posture management tools, static analysis tools (such as Checkov, tfsec, TFLint, KICS) evaluate IaC source files before deployment. They parse the abstract syntax tree (AST) of Terraform or CloudFormation manifests, evaluating each declared resource against security policies:
   - Identifying overly permissive security group ingress rules (`0.0.0.0/0` on management ports 22, 3389, 5432).
   - Flagging unencrypted storage volumes (`encrypted = false` on EBS/RDS).
   - Detecting hardcoded API keys, database passwords, or private keys within IaC files.
   - Enforcing mandatory tagging and logging configurations (e.g. VPC flow logs, S3 bucket access logging).
3. **Policy as Code (PaC) & Admission Control:**
   Engineering teams use Policy-as-Code frameworks (such as Open Policy Agent / Rego, HashiCorp Sentinel) to write programmatic compliance rules that run during CI/CD pull request checks. A pull request that declares a non-compliant resource is automatically blocked from merging or deploying.
4. **Drift Detection & State File Security:**
   Manual configuration changes made in cloud web consoles cause configuration drift away from the IaC state. Automated drift detection scans reconcile live cloud infrastructure against Git repository manifests, reverting or alerting on unauthorized out-of-band modifications. Furthermore, Terraform state files (`terraform.tfstate`) frequently store sensitive resource attributes (such as initial database passwords or private keys) in plaintext. State files must be stored in secure, encrypted remote backends with restricted access.

### Practical learning notes

In repository audits and infrastructure reviews:
- Run static analysis tools against Terraform and Dockerfiles:
  ```bash
  checkov -d ./terraform/
  tfsec ./terraform/
  hadolint Dockerfile
  ```
- Inspect version control history for committed secrets in `.tfvars` or `variables.tf` files.
- Review Terraform state storage: Verify that state files are stored in remote, encrypted backends (e.g. S3 with KMS encryption) with strict IAM access restrictions, and never committed to Git.

### Defensive and engineering notes

1. **Automate IaC Security Scanning in CI/CD:** Run Checkov, tfsec, or KICS as mandatory release gates on every pull request that touches infrastructure definitions. Fail the build if high or critical misconfigurations are detected.
2. **Never Commit Secrets to IaC Manifests:** Use dynamic secret references (e.g. AWS Secrets Manager or HashiCorp Vault data sources) rather than passing plaintext strings into `terraform.tfvars`.
3. **Secure Remote State Storage:** Store remote state files in private, encrypted object storage with state locking (e.g. DynamoDB for Terraform) and restrict state access to dedicated CI/CD runner identities.
4. **Adopt Module-Based Hardened Defaults:** Provide development teams with pre-approved, hardened infrastructure modules (e.g. a company-standard `secure-s3-bucket` or `hardened-vpc` module) that enforce encryption, logging, and private access by default.
5. **Continuous Drift Reconciling:** Schedule regular automated runs (e.g. `terraform plan -detailed-exitcode`) in CI/CD to detect and remediate manual cloud modifications.

### Reading order

1. Read [OWASP — Infrastructure as Code Security Cheat Sheet](resources.md#infrastructure-code).
2. Connect with Chapter 7 CI/CD Permissions & Pipeline Security and Chapter 9 Security Architecture & Engineering.

<a id="cicd-security"></a>
## CI/CD Permissions & Pipeline Security

### Prerequisites

Understand Git workflows, branch protection rules, CI/CD orchestration systems (GitHub Actions, GitLab CI, Jenkins), build runner environments (hosted vs. self-hosted), pipeline triggers, and cloud deployment credentials.

### Mechanism and mental model

Continuous Integration and Continuous Delivery (CI/CD) pipelines sit at the intersection of source code, deployment credentials, and production infrastructure. Because pipelines possess access to repository secrets, cloud IAM roles, container registries, and release distribution channels, they represent high-value targets for software supply chain compromise.

Key vulnerabilities across CI/CD architectures include:
- **Poisoned Pipeline Execution (PPE):** Attackers exploit workflows that execute build commands defined inside the repository itself. By opening a pull request that alters pipeline definition files, build scripts, or Makefiles, an attacker forces the CI runner to execute malicious commands.
- **Dangerous Workflow Triggers (`pull_request_target`):** In GitHub Actions, standard `pull_request` workflows run unprivileged with read-only tokens and without access to repository secrets. Conversely, `pull_request_target` runs in the context of the base repository, granting access to production secrets and a write-scoped `GITHUB_TOKEN`. If a `pull_request_target` workflow checks out the untrusted pull request's code (e.g., `ref: ${{ github.event.pull_request.head.sha }}`) and runs build or lint scripts, external contributors can execute arbitrary code with full access to repository secrets.
- **CI/CD Cache Poisoning:** Workflows frequently cache dependencies to reduce build times. If an untrusted pull request run can write malicious files into a shared cache namespace, and a subsequent privileged release workflow restores that poisoned cache, attacker code is executed inside the production release environment.
- **Over-Privileged Pipeline Tokens:** Automated runner tokens (such as `GITHUB_TOKEN`) frequently carry broad default permissions (read/write access to code, releases, and packages). An attacker compromising a single build step can abuse this token to push unauthorized commits, overwrite releases, or bypass branch protections.
- **Mutable Third-Party Action References:** Referencing external actions using mutable branch or tag names (e.g. `@v3`) allows upstream maintainer compromise or tag reassignment to silently introduce malicious code into the build pipeline.

### Practical learning notes

In authorized pipeline reviews and audits, inspect workflow YAML files for dangerous triggers like `pull_request_target` or `workflow_run` combined with untrusted checkouts. Verify whether `GITHUB_TOKEN` permissions are explicitly constrained. Audit third-party action dependencies to confirm whether actions are pinned to commit SHAs. In self-hosted runner environments, verify whether runner machines are ephemeral or if persistence allows cross-build state contamination.

### Defensive and engineering notes

1. **Least-Privilege Pipeline Permissions:** Explicitly declare minimal permissions at both the workflow and job level. Always default to `permissions: read-all` and grant write access only to specific scopes (`contents: write`, `issues: write`) where required:
   ```yaml
   permissions: read-all
   ```
2. **Safe Trigger Architecture:** Never check out untrusted pull request code in privileged workflows (`pull_request_target`). If PR validation requires secrets, separate the process into a two-stage pipeline: an unprivileged build stage followed by a review-gated deployment stage.
3. **Immutable Action Pinning:** Pin all third-party actions to full 40-character commit SHAs, accompanied by comment annotations indicating the intended version tag:
   ```yaml
   uses: actions/checkout@b4ffde65f46336ab88eb53be808477a3936bae11 # v4.1.1
   ```
4. **Cache Isolation:** Completely disable cache restoration in release, packaging, and production deployment workflows to prevent cache-poisoning attacks from contaminating release artifacts.
5. **Short-Lived OIDC Authentication:** Replace long-lived cloud credentials (AWS Access Keys, service account keys) stored in pipeline secrets with OpenID Connect (OIDC) workload identity federation.
6. **Automated Workflow Auditing:** Integrate static analysis tools (such as CodeQL for GitHub Actions or Legitify) to scan pipeline configuration files for known misconfigurations.

### Reading order

1. Read [OWASP — GitHub Actions Security Cheat Sheet](resources.md#cicd-security).
2. Read [OWASP — Top 10 CI/CD Security Risks](resources.md#cicd-security).
3. Connect with Chapter 7 Dependencies, SBOM, Signing & Provenance and Chapter 7 Object Storage & Secrets.

<a id="dependencies-artifacts"></a>
## Dependencies, SBOM, Signing & Provenance

### Prerequisites

Understand package managers, build pipelines, deployment artifacts and the difference between source code, build output and runtime images. You should also know where your application consumes third-party packages, containers or services.

### Mechanism and mental model

Supply-chain security asks whether the artifact you deploy is the artifact you intended to build from reviewed source, with dependencies you can inventory and update. Risk can enter through source control, build systems, package registries, dependency confusion, compromised maintainers, CI/CD credentials, artifact storage or deployment automation.

SBOMs improve visibility, provenance explains how an artifact was built, and signing/verification helps consumers decide whether to trust an artifact. None of these prove the code is bug-free or that every transitive dependency is trustworthy; they create evidence and control points.

### Practical learning notes

Start with inventory: package manifests, lockfiles, container bases, build artifacts and deployed versions. For owned systems, compare source, build logs, SBOMs and deployed images. Do not install random PoC packages or run unknown build scripts during research.

### Defensive and engineering notes

Generate SBOMs in CI/CD, track component vulnerabilities, pin and update dependencies deliberately, verify artifact provenance where possible, restrict release permissions, protect build credentials and enforce policy before deployment. Tools such as Dependency-Track can operationalize SBOM monitoring, while SLSA provides a framework for build provenance maturity.

### Reading order

1. Read [SLSA v1.1 — About SLSA](resources.md#dependencies-artifacts) for the provenance model.
2. Review [OWASP Dependency-Track](resources.md#dependencies-artifacts) as an extended operational tooling example.
3. Add ecosystem-specific package-security resources in later passes.
