# Chapter 7 — Cloud, Deployment & Supply Chain Security Findings

## 2026-10-03 status

No Chapter 7 resource has been promoted in the first curated batch.

Related evidence gathered so far:

- MDN's Practical security implementation guides were promoted under Chapter 9 and include transport and header controls relevant to deployed web systems, but not full cloud, CI/CD or supply-chain coverage.

Gaps:

- Need inspected sources for cloud IAM/trust boundaries, object storage/secrets, metadata services/serverless, web servers/reverse proxies, containers/Kubernetes, infrastructure as code, CI/CD permissions and dependency/SBOM/signing/provenance topics.

## 2026-10-03 batch

### OWASP — Docker Security Cheat Sheet

- URL: <https://cheatsheetseries.owasp.org/cheatsheets/Docker_Security_Cheat_Sheet.html>
- Method: WebFetch public page reading.
- Verification scope: relevant English Docker security sections inspected; no containers run.
- Promoted resource: `owasp-docker-security-cheat-sheet` in `data/resources/ch07-cloud-supply-chain.yml`.

Useful observations:

- Containers should run as unprivileged users; rootless mode and user namespaces reduce host impact.
- Capabilities should be dropped by default and added back only when required; `--privileged` is explicitly dangerous.
- `no-new-privileges`, read-only filesystems, read-only mounts and resource limits help reduce escalation and DoS exposure.
- Secrets should not be embedded in images or commands; image pinning, signing, SBOM generation and scanning support supply-chain control.
- Docker socket exposure and unauthenticated TCP daemon exposure are called out as severe risks.

### OWASP — Kubernetes Security Cheat Sheet

- URL: <https://cheatsheetseries.owasp.org/cheatsheets/Kubernetes_Security_Cheat_Sheet.html>
- Method: WebFetch public page reading.
- Verification scope: relevant English Kubernetes security sections inspected; no cluster commands run.
- Promoted resource: `owasp-kubernetes-security-cheat-sheet` in `data/resources/ch07-cloud-supply-chain.yml`.

Useful observations:

- The API server is the front end for the control plane, so RBAC, NodeRestriction and external identity integration are foundational.
- Namespaces partition resources and permission scope but do not replace workload or network isolation.
- Pod Security Standards, `runAsNonRoot`, `readOnlyRootFilesystem`, network policies and admission controllers reduce workload risk.
- Secrets should be mounted as read-only volumes when possible, with etcd encryption and external secret managers considered.
- Audit logging, Forbidden responses, etcd protection and credential rotation are core operational controls.

### OWASP — Secrets Management Cheat Sheet

- URL: <https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html>
- Method: WebFetch public page reading.
- Verification scope: relevant English secrets-management sections inspected; no secrets accessed.
- Promoted resource: `owasp-secrets-management-cheat-sheet` in `data/resources/ch07-cloud-supply-chain.yml`.

Useful observations:

- Secrets are treated as a lifecycle: creation, rotation, revocation and expiration.
- Designated secrets managers are preferred over hardcoded source/config/container secrets, with metadata for ownership, rotation and incident response.
- Least privilege, dynamic secrets, automated rotation, encryption/key separation and CI/CD handling are covered.
- Audit logs should capture request, use, failure and administrative events, be tamper-resistant and be queryable for at least 90 days.
- Incident response guidance centers on revocation, rotation, deletion and documenting who had access and when.

### SLSA — About SLSA v1.1

- URL: <https://slsa.dev/spec/v1.1/about>
- Method: WebFetch public page reading.
- Verification scope: SLSA v1.1 overview inspected; no tooling installed or configured.
- Promoted resource: `slsa-v1-1-about` in `data/resources/ch07-cloud-supply-chain.yml`.

Useful observations:

- SLSA is a set of incrementally adoptable supply-chain security guidelines across source, build, packaging and distribution.
- Provenance is framed as tamper-resistant evidence about which build platform produced an artifact.
- SLSA v1.1 has a Build Track with levels 1-3. Higher levels increase protection and implementation cost.
- Levels apply per artifact and do not automatically cover transitive dependency trust.

### OWASP — Dependency-Track

- URL: <https://owasp.org/www-project-dependency-track/>
- Method: WebFetch public project page reading.
- Verification scope: public OWASP project page inspected; tool not installed or executed.
- Promoted resource: `owasp-dependency-track` in `data/resources/ch07-cloud-supply-chain.yml`.

Useful observations:

- Dependency-Track inventories components, finds vulnerabilities and enforces policies across the software supply chain.
- It ingests CycloneDX SBOMs, tracks components across project versions and matches them against sources such as NVD, GitHub Advisories, OSV, Snyk and Trivy.
- It supports policy enforcement, EPSS prioritization, CI/CD SBOM production and integrations such as Jenkins, Jira, Slack and Teams.

### OWASP — GitHub Actions Security Cheat Sheet

- URL: <https://cheatsheetseries.owasp.org/cheatsheets/GitHub_Actions_Security_Cheat_Sheet.html>
- Method: Exa search and Jina Reader inspection of public cheat sheet.
- Verification scope: relevant English GitHub Actions security sections inspected; no workflows executed.
- Promoted resource: `owasp-github-actions-security-cheat-sheet` in `data/resources/ch07-cloud-supply-chain.yml`.

Useful observations:

- Pinpoints critical security risks in GitHub Actions CI/CD workflows:
  - Dangerous triggers: `pull_request_target` executes in the context of the base repository with access to repository secrets and a write-scoped `GITHUB_TOKEN`. Checking out untrusted PR branch code inside a `pull_request_target` workflow enables direct RCE and secret exfiltration.
  - Poisoned Pipeline Execution (PPE): modifying build steps or scripts in pull requests to execute attacker code within privileged build runners.
  - GitHub Actions Cache Poisoning: untrusted PR runs writing malicious files into shared build caches that are later restored by release or deployment workflows.
  - Over-privileged `GITHUB_TOKEN`: default repository permissions often grant read/write access. Workflows must explicitly declare `permissions: read-all` or specific granular scopes.
  - Third-party Actions: referencing untrusted tags or mutable branch names (e.g. `@v1`) instead of immutable commit SHAs (`@a1b2c3...`).
- Core defenses:
  - Avoid `pull_request_target` where possible; use `pull_request` triggers with read-only tokens and no access to secrets.
  - Enforce least privilege on `GITHUB_TOKEN` per workflow and per job.
  - Pin actions to full immutable commit hashes, complemented by Dependabot/Renovate for updates.
  - Disable cache restoration in release and artifact-publishing pipelines.
  - Restrict runner network egress and run static analysis (CodeQL) on workflow definitions.

### OWASP — Top 10 CI/CD Security Risks

- URL: <https://owasp.org/www-project-top-10-ci-cd-security-risks/>
- Method: Exa search and Jina Reader inspection of public project page.
- Verification scope: relevant English project overview and risk taxonomy sections inspected; no build environments modified.
- Promoted resource: `owasp-top-10-ci-cd-security-risks` in `data/resources/ch07-cloud-supply-chain.yml`.

Useful observations:

- Authoritative industry risk taxonomy identifying the top 10 security risks across continuous integration and delivery:
  - **CICD-SEC-1: Insufficient Flow Control Mechanisms** (bypassing branch protection, unreviewed commits pushed to production).
  - **CICD-SEC-2: Inadequate Identity and Access Management** (over-scoped service accounts, orphaned tokens).
  - **CICD-SEC-3: Dependency Chain Abuse** (dependency confusion, typosquatting, malicious upstream packages).
  - **CICD-SEC-4: Poisoned Pipeline Execution (PPE)** (injecting malicious commands into pipeline definition files).
  - **CICD-SEC-5: Insufficient PBAC (Pipeline-Based Access Controls)** (unprivileged workflows accessing production environments).
  - **CICD-SEC-6: Insufficient Credential Hygiene** (long-lived static secrets in pipeline variables instead of OIDC federation).
  - **CICD-SEC-7: Insecure System Configuration** (unhardened runners, missing network isolation).
  - **CICD-SEC-8: Ungoverned Usage of 3rd Party Services** (unreviewed integrations and plugins).
  - **CICD-SEC-9: Improper Artifact Integrity Validation** (publishing or deploying untampered artifacts without digital signatures or SLSA provenance).
  - **CICD-SEC-10: Insufficient Logging and Visibility** (lack of audit trails for pipeline execution and secret access).

### AWS — Configuring the Instance Metadata Service (IMDSv2)

- URL: <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html>
- Method: WebFetch public documentation reading.
- Verification scope: relevant English IMDSv2 configuration and security sections inspected; no cloud instances modified.
- Promoted resource: `aws-ec2-imdsv2-guide` in `data/resources/ch07-cloud-supply-chain.yml`.

Useful observations:

- Explains the architectural security improvements of Instance Metadata Service Version 2 (IMDSv2) over legacy IMDSv1.
- Highlights IMDSv1 vulnerabilities: IMDSv1 used simple HTTP `GET` requests to `169.254.169.254`, making it trivial for Server-Side Request Forgery (SSRF) vulnerabilities or misconfigured open reverse proxies to steal instance IAM role credentials.
- IMDSv2 session-oriented security model:
  1. Mandatory `PUT` request to `http://169.254.169.254/latest/api/token` with header `X-aws-ec2-metadata-token-ttl-seconds: <seconds>` (1 to 21600 seconds) to retrieve a session token.
  2. Subsequent `GET` requests must supply the token in `X-aws-ec2-metadata-token: <token>`.
  3. `PUT` requests containing an `X-Forwarded-For` header are explicitly rejected, neutralizing reverse proxy bypasses.
  4. IP-level Hop Limit: The response packet to the token `PUT` request defaults to a Time-To-Live (TTL / hop limit) of `1`. Any packet traversing an intermediate router, NAT, or container bridge network is dropped, preventing containers running on the EC2 host from querying the host's IAM role unless explicitly permitted.
- Enforcement: Cloud engineers can enforce `HttpTokens: required` via instance launch configurations or AWS Service Control Policies (SCPs), rejecting all IMDSv1 traffic.

Limits and follow-up:

- Need cloud IAM policy evaluation sources, object storage access policy guides, and Infrastructure as Code (IaC) security analyzers.


