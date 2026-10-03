# Chapter 4 — Vulnerability Classes & Root Causes Findings

## 2026-10-03 batch

### OWASP — SQL Injection Prevention Cheat Sheet

- URL: <https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html>
- Method: WebFetch public page reading.
- Verification scope: relevant English SQL injection prevention sections inspected; no exploit code executed.
- Promoted resource: `owasp-sql-injection-prevention-cheat-sheet` in `data/resources/ch04-vulnerabilities.yml`.

Useful observations:

- The cheat sheet ranks primary defenses as prepared statements, safely implemented stored procedures, allow-list input validation and escaping as a strongly discouraged last resort.
- Prepared statements are presented as the main defense because the database distinguishes code from data regardless of user input.
- Stored procedures are not automatically safe: dynamic SQL inside procedures remains dangerous, and permission models can push web apps toward overly powerful database roles.
- Allow-list validation is needed where bind variables cannot represent structure, such as table names, column names or sort direction. Mapping user choices to hardcoded values is preferred.
- Escaping is described as fragile compared with parameterization.
- Least privilege is part of the root-cause story: separate database users, no DBA-level application accounts and views can reduce blast radius even when a bug exists.

### OWASP — Server Side Request Forgery Prevention Cheat Sheet

- URL: <https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html>
- Method: WebFetch public page reading.
- Verification scope: relevant English SSRF prevention sections inspected; no exploit code executed.
- Promoted resource: `owasp-ssrf-prevention-cheat-sheet` in `data/resources/ch04-vulnerabilities.yml`.

Useful observations:

- The cheat sheet separates the controlled-destination case, where allowlists are realistic, from open/external request features where egress controls and layered validation matter.
- It covers validation of strings, IP addresses, domain names and URLs, while warning that deny-lists and parser assumptions are bypass-prone.
- It explicitly calls out parser disagreement, DNS pinning and redirect behavior as reasons SSRF defenses fail.
- It connects application controls to network segmentation, firewall egress rules and cloud metadata protections such as AWS IMDSv2.

### OWASP — OS Command Injection Defense Cheat Sheet

- URL: <https://cheatsheetseries.owasp.org/cheatsheets/OS_Command_Injection_Defense_Cheat_Sheet.html>
- Method: WebFetch public page reading.
- Verification scope: relevant English OS command injection defense sections inspected; no exploit code executed.
- Promoted resource: `owasp-os-command-injection-defense-cheat-sheet` in `data/resources/ch04-vulnerabilities.yml`.

Useful observations:

- The cheat sheet defines command injection as unsafe neutralization of special elements and treats argument injection as a related sub-category.
- It prioritizes replacing shell commands with native library functions where possible.
- Where process execution is required, it recommends separating commands from arguments, using parameterization plus input validation and applying allow-list validation.
- It notes OS-specific escaping as a secondary defense and recommends least privilege to reduce impact.

### OWASP — File Upload Cheat Sheet

- URL: <https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html>
- Method: WebFetch public page reading.
- Verification scope: relevant English file upload security sections inspected; no exploit code executed.
- Promoted resource: `owasp-file-upload-cheat-sheet` in `data/resources/ch04-vulnerabilities.yml`.

Useful observations:

- The cheat sheet treats upload security as layered validation and containment, not just extension filtering.
- It recommends extension allowlists and warns about double extensions, null bytes and case manipulation.
- It states Content-Type is user-controlled and spoofable, and treats file signature validation as useful but bypassable.
- It covers server-generated filenames, storage outside the webroot or on a separate host, authorization for uploaded content, filesystem least privilege and size limits to mitigate ZIP bombs or excessive upload load.

### OWASP — Deserialization Cheat Sheet

- URL: <https://cheatsheetseries.owasp.org/cheatsheets/Deserialization_Cheat_Sheet.html>
- Method: WebFetch public page reading.
- Verification scope: relevant English deserialization sections inspected; no exploit payloads executed.
- Promoted resource: `owasp-deserialization-cheat-sheet` in `data/resources/ch04-vulnerabilities.yml`.

Useful observations:

- Documents native serialization mechanisms in Java, Python, PHP, and .NET.
- In Java, `ObjectInputStream.readObject()` processing untrusted data can trigger arbitrary object instantiation and gadget chains (identifiable by magic bytes `AC ED 00 05` / Base64 `rO0`).
- In Python, `pickle.loads()`, `yaml.load()` (without SafeLoader), and `jsonpickle` execute arbitrary callables.
- In .NET, `BinaryFormatter` is fundamentally insecure; `TypeNameHandling` in Json.NET can load arbitrary types.
- In PHP, `unserialize()` with magic methods (`__wakeup`, `__destruct`) triggers POP chains.
- Primary defense is using pure data formats (JSON, protocol buffers) instead of native object serialization. When native serialization cannot be avoided: override `resolveClass` in Java to enforce class allowlists, use `BinaryFormatter` replacements in .NET, or sign payloads with HMAC before processing.

### OWASP — XML External Entity Prevention Cheat Sheet

- URL: <https://cheatsheetseries.owasp.org/cheatsheets/XML_External_Entity_Prevention_Cheat_Sheet.html>
- Method: WebFetch public page reading.
- Verification scope: relevant English XXE prevention sections inspected; no XML payloads parsed.
- Promoted resource: `owasp-xxe-prevention-cheat-sheet` in `data/resources/ch04-vulnerabilities.yml`.

Useful observations:

- Explains how XML parsers resolving external entity references lead to local file disclosure (`file:///`), SSRF, and parser denial of service (Billion Laughs / quadratic blowup).
- The primary remediation across all parsers is completely disabling external DTD parsing and external entity resolution.
- For Java JAXP parsers (`DocumentBuilderFactory`, `SAXParserFactory`): set `disallow-doctype-decl = true` and enable `FEATURE_SECURE_PROCESSING`.
- For .NET (`XmlDocument`, `XmlReader`): set `DtdProcessing = DtdProcessing.Prohibit` or set `XmlResolver = null`.
- For PHP: libxml2 in PHP 8.0+ disables external entities by default; pre-8.0 requires `libxml_set_external_entity_loader(null)`.
- For Python: standard library XML parsers remain vulnerable to entity expansion attacks; use `defusedxml` as a hardened wrapper.

### PortSwigger — Server-Side Template Injection

- URL: <https://portswigger.net/web-security/server-side-template-injection>
- Method: WebFetch public page reading.
- Verification scope: relevant English SSTI guidance sections inspected; no template expressions executed.
- Promoted resource: `portswigger-server-side-template-injection` in `data/resources/ch04-vulnerabilities.yml`.

Useful observations:

- Explains that SSTI arises when user input is concatenated directly into template source code instead of being passed as context data variables (e.g. `$twig->render("Hello " . $_GET['name'])`).
- Outlines detection through fuzzing polyglots (`${{<%[%'"}}%\`) and mathematical expression injection (`${7*7}` evaluating to `49`).
- Provides a diagnostic tree to identify the specific engine (e.g. `{{7*'7'}}` returns `49` in Twig, but `7777777` in Jinja2).
- Impact frequently reaches remote code execution via engine-specific introspection and execution primitives (e.g., Python `__mro__` and `__subclasses__` traversal in Jinja2).
- Recommends logic-less template engines (such as Mustache) or strict execution sandboxing.

### PortSwigger Research — Smashing the State Machine (Race Conditions)

- URL: <https://portswigger.net/research/smashing-the-state-machine>
- Method: WebFetch public page reading.
- Verification scope: relevant English research paper and methodology sections inspected; no live targets tested.
- Promoted resource: `portswigger-smashing-the-state-machine` in `data/resources/ch04-vulnerabilities.yml`.

Useful observations:

- Introduces the HTTP/2 single-packet attack: pre-sending the bulk of 20–30 requests over an HTTP/2 connection and releasing the final frame in a single TCP packet, eliminating network jitter and achieving a median 1ms arrival spread.
- Identifies critical sub-states and collisions: limit-overruns (redeeming gifts/coupons repeatedly), single-endpoint state collisions (two identical operations racing), and multi-endpoint collisions (racing email update against verification).
- Defines a rigorous 4-step methodology: Predict, Probe, Prove, and Remediate.
- Architectural defense requires atomicity: atomic database transactions, strict datastore integrity constraints, and avoiding mixed-source state transitions.

### OWASP — NoSQL Security Cheat Sheet

- URL: <https://cheatsheetseries.owasp.org/cheatsheets/NoSQL_Security_Cheat_Sheet.html>
- Method: WebFetch / Exa agent-reach public inspection.
- Verification scope: relevant English NoSQL security sections inspected; no database queries executed.
- Promoted resource: `owasp-nosql-security-cheat-sheet` in `data/resources/ch04-vulnerabilities.yml`.

Useful observations:

- Details how NoSQL databases (MongoDB, CouchDB) are vulnerable to operator injection when user input is parsed as structured objects (e.g. via `qs` parser bracket notation `user[$ne]=admin` or JSON payloads `{"password": {"$ne": null}}`).
- Analyzes server-side JavaScript execution via `$where` and `mapReduce`, which evaluate arbitrary JS in the database engine and can lead to remote code execution.
- Blind exfiltration can be performed using `$regex` prefix matching to extract strings character-by-character.
- Defenses: reject or recursively strip keys starting with `$`, enforce strict data types using schema validators (Joi, Zod, Ajv), disable server-side JavaScript scripting in database configurations (`--noscripting`), and use typed query builders instead of raw string evaluation.

### PortSwigger — File Path Traversal

- URL: <https://portswigger.net/web-security/file-path-traversal>
- Method: WebFetch / Jina Reader agent-reach inspection.
- Verification scope: relevant English path traversal tutorial sections inspected; no filesystem payloads executed.
- Promoted resource: `portswigger-file-path-traversal` in `data/resources/ch04-vulnerabilities.yml`.

Useful observations:

- Explains directory traversal mechanics using `../` sequences to escape the designated storage directory and read sensitive operating system files (e.g., `/etc/passwd`, Windows `win.ini`).
- Explores common validation bypasses: nested traversal sequences (`....//` or `....\/`) that survive simple non-recursive string stripping, single and double URL encoding (`%2e%2e%2f`), absolute paths, and null-byte injection (`%00`) on legacy platforms.
- Defensive remediation requires avoiding passing user input to filesystem APIs; when unavoidable, resolve the canonical path and strictly verify that it starts with the authorized base directory prefix.

### PortSwigger — Prototype Pollution

- URL: <https://portswigger.net/web-security/prototype-pollution>
- Method: WebFetch / Jina Reader agent-reach inspection.
- Verification scope: relevant English prototype pollution sections inspected; no script payloads executed.
- Promoted resource: `portswigger-prototype-pollution` in `data/resources/ch04-vulnerabilities.yml`.

Useful observations:

- Details prototype pollution mechanics in JavaScript where unvalidated property assignment via keys like `__proto__`, `constructor`, or `prototype` modifies `Object.prototype`.
- Breaks down attacks into sources (query string, JSON body), sinks (recursive merge/clone functions, lodash, jQuery), and gadgets (uninitialized properties accessed in security-sensitive contexts).
- In client-side environments, gadgets frequently escalate to DOM XSS; in server-side Node.js environments, polluting process options (e.g., `NODE_OPTIONS`, `shell`, `execPath`) can yield remote code execution.
- Remediations: validate and reject forbidden keys, use `Object.create(null)` for plain key-value dictionaries, freeze the prototype with `Object.freeze(Object.prototype)`, and use `Map` structures instead of plain objects.

### OWASP — Business Logic Security Cheat Sheet

- URL: <https://cheatsheetseries.owasp.org/cheatsheets/Business_Logic_Security_Cheat_Sheet.html>
- Method: WebFetch public page reading.
- Verification scope: relevant English business logic security guidance inspected; no workflows tested.
- Promoted resource: `owasp-business-logic-security-cheat-sheet` in `data/resources/ch04-vulnerabilities.yml`.

Useful observations:

- Explains business logic vulnerabilities as flaws in design, assumptions, and workflow enforcement rather than standard input-parsing bugs.
- Details attack categories:
  - Domain invariant violations: Submitting negative quantities to induce credit refunds or bypass minimum cart totals.
  - Multi-step workflow circumvention: Skipping intermediate steps in transactions (e.g. jumping directly from cart creation to order fulfillment without payment).
  - Parameter tampering on financial values: Modifying price, discount percentage, currency code, or quantity parameters transmitted in client requests.
  - State machine subversion: Transitioning orders or accounts into unauthorized states (e.g. re-triggering one-time promotion codes).
- Defensive requirements:
  - Enforce all business invariants strictly server-side; never trust client-calculated totals or workflow flags.
  - Implement formal state machines that validate allowed transitions and refuse out-of-order execution.
  - Combine with concurrency controls and database transactions (Chapter 4 Race Conditions) to prevent double-spending or limit overruns.

Limits and follow-up:

- Automated scanners rarely detect business logic flaws because they require domain-specific understanding. Threat modeling (Chapter 9) and manual code review are primary detection tools.

### OWASP — LDAP Injection Prevention Cheat Sheet

- URL: <https://cheatsheetseries.owasp.org/cheatsheets/LDAP_Injection_Prevention_Cheat_Sheet.html>
- Method: WebFetch public page reading.
- Verification scope: relevant English LDAP injection defense sections inspected; no queries executed.
- Promoted resource: `owasp-ldap-injection-prevention-cheat-sheet` in `data/resources/ch04-vulnerabilities.yml`.

Useful observations:

- LDAP (Lightweight Directory Access Protocol) is widely used for enterprise authentication and directory lookups.
- Vulnerabilities arise because LDAP query interfaces frequently lack native parameterization, leading developers to concatenate user input into search filter strings.
- Distinguishes two distinct escaping contexts:
  - Search filter characters requiring escaping: `*`, `(`, `)`, `\`, and `NUL`.
  - Distinguished Name (DN) characters requiring escaping: `\`, `#`, `+`, `<`, `>`, `,`, `;`, `"`, `=`, and leading/trailing spaces.
- Highlights secure coding abstractions:
  - Java parameterized search filters: `String filter = "(&(uid={0})(objectClass=person))"`.
  - .NET RFC 4515 / RFC 2253 encoders (`Encoder.LdapFilterEncode()`, `Encoder.LdapDistinguishedNameEncode()`).
- Defense-in-depth: Enforcing least privilege on LDAP binding accounts (preventing anonymous binds from executing sensitive searches) and strict allow-list input validation.

Limits and follow-up:

- Connect with enterprise identity systems, Active Directory, and SAML/SSO federations in Chapter 3.


