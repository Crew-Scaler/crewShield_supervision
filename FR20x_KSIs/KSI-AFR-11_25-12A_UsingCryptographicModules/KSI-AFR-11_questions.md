# KSI-AFR-11: Using Cryptographic Modules - Question Library

**KSI Focus:** KSI-AFR-11 - Using Cryptographic Modules
**Date:** January 12, 2026
**Status:** Ready for Human Review and Approval

---

## Document Summary

This question library addresses cryptographic module governance in AI-enabled FedRAMP environments. The questions guide CIOs, Cloud Service Providers, federal customers, and auditors through critical decision points for implementing FRR-UCM (Using Cryptographic Modules) requirements when AI systems and autonomous agents fundamentally reshape cryptographic complexity.

**Processing Statistics:**
- Original question count: 21 (from discoveryQuestions.md)
- Questions removed: 0 (all discovery questions relevant to AI/agent context)
- Questions added: 10 (addressing identified gaps in AI-specific cryptographic requirements)
- Final question count: 31

**Key Themes:**
- Cryptographic module inventory expansion (12-18 stacks in AI vs 2-4 traditional)
- Autonomous agent cryptographic configuration management
- Multi-tenant AI cryptographic isolation
- Hardware accelerator firmware validation
- AI framework supply chain cryptographic dependencies
- Continuous validation for fast-changing infrastructure
- Post-quantum cryptography readiness
- AI-specific data protection requirements

---

## Questions

**AFR-11-Q001: Cryptographic Module Inventory Scope**

How will your organization discover and document all cryptographic modules across an AI platform with 12-18 distinct cryptographic stacks (API gateways, service meshes, SDKs, vector databases, model registries) when traditional cloud services typically maintain only 2-4?

Decision Points:
- Will you conduct automated discovery via software composition analysis (SCA), runtime profiling, and IaC scanning?
- How will you identify embedded cryptographic modules in AI SDKs (LangChain, Hugging Face Transformers, LlamaIndex)?
- What is your process for quarterly reconciliation between documented inventory (SSP Appendix Q) and actual deployment?
- Will you maintain machine-readable inventory (JSON/YAML) for real-time validation against deployed infrastructure?

FedRAMP Alignment: FRR-UCM-01 (Cryptographic Module Documentation)

---

**AFR-11-Q002: Agent-Driven Cryptographic Configuration Control**

Given that AI agents modify cryptographic configurations at machine speed (50-150 changes/day), how will you prevent autonomous systems from silently degrading from FIPS-validated to non-FIPS cryptographic modules?

Decision Points:
- Will you implement policy-as-code (Open Policy Agent, Kubernetes NetworkPolicy) that blocks non-compliant cryptographic deployments?
- How will you balance automation (agents proposing infrastructure changes) with compliance (humans/validated AIs approving cryptographic changes)?
- What approval workflows will you establish for agent-proposed cryptographic changes (TLS version upgrades, cipher suite modifications, key rotation frequency)?
- Will you enforce RBAC constraints limiting agent access to cryptographic configuration, KMS keys, and certificate stores?

FedRAMP Alignment: FRR-UCM-02/03 (Default Use of Validated Modules)

---

**AFR-11-Q003: Continuous Validation vs Manual Assessment Cadence**

Will your organization rely on manual quarterly security assessments (detecting violations 30+ days late) or implement continuous cryptographic compliance validation (detecting drift within 2-8 hours)?

Decision Points:
- Will you deploy automated scanning systems validating cryptographic posture every 1-4 hours?
- What metrics will you monitor: TLS certificate validity, cipher suite alignment, cryptographic module versions, configuration consistency?
- How will you integrate automated scanning with SIEM and incident response workflows?
- What severity levels will trigger automatic alerts vs manual investigation?

FedRAMP Alignment: FRR-PVA (Persistent Validation and Assessment)

---

**AFR-11-Q004: Multi-Tenant Cryptographic Isolation Architecture**

For FedRAMP AI services serving multiple federal agency tenants, will you enforce data separation exclusively through cryptographic means (per-tenant keys, distinct encryption contexts)?

Decision Points:
- Will you implement a key hierarchy: Master Key (HSM) → Tenant Key Encryption Key (per tenant) → Data Encryption Keys (per data element)?
- How will you ensure 100% of federal customer data uses tenant-specific encryption, preventing cross-tenant exposure?
- Will you implement attribute-based encryption where encryption parameters are derived from tenant attributes?
- What audit logging will you maintain to demonstrate inter-tenant cryptographic operations?
- How will you design breach isolation so compromise of one tenant's encryption keys does not expose other tenants' data?

FedRAMP Alignment: FRR-MAS (Minimum Assessment Scope), Multi-Tenant Data Separation

---

**AFR-11-Q005: Hardware Accelerator Firmware Validation Gaps**

GPU and TPU firmware updates occur every 6-8 weeks, but CMVP validation lags 4-6 months. How will your organization manage this validation gap without exposing federal customer data to unvalidated or vulnerable cryptographic modules?

Decision Points:
- Will you establish vendor relationships with GPU/TPU manufacturers (NVIDIA, AMD, Google) to obtain cryptographic module documentation and validation timelines?
- How will you track firmware versions and their CMVP certification status in your cryptographic module inventory?
- Will you stage firmware updates in test environments first, verifying cryptographic module boundaries are preserved?
- What is your strategy if critical security patches require deployment before CMVP revalidation?
- Will you implement firmware version attestation to ensure validated versions are deployed?

FedRAMP Alignment: FRR-UCM-03 (Use of Validated Modules for Hardware-Embedded Cryptography)

---

**AFR-11-Q006: Supply Chain Cryptographic Dependency Management**

AI frameworks embed cryptographic modules (TLS clients in LangChain, Hugging Face Transformers) that create hidden dependencies. How will you maintain software composition visibility and ensure embedded cryptography is CMVP-validated?

Decision Points:
- Will you perform software bill of materials (SBOM) analysis on all AI framework dependencies, highlighting cryptographic components?
- How will you integrate SCA tools (Snyk, FOSSA, Black Duck) into your CI/CD pipeline to detect new cryptographic dependencies?
- Will you implement developer training explaining why embedded non-FIPS cryptography is a FedRAMP concern?
- What approval process will govern introducing new cryptographic dependencies?
- Will you implement SBOM signing to prevent tampering with dependency lists?

FedRAMP Alignment: FRR-UCM-01 (Documentation of All Modules), FRR-AFR-04 (Vulnerability Detection in Supply Chain)

---

**AFR-11-Q007: Cryptographic Module Update-Stream and Historical Status Classification**

73% of AI clusters have cryptographic modules in "historical status" or using "update streams" (patched versions of validated modules). How will your organization classify, document, and approve the use of non-pristine validated modules?

Decision Points:
- Will you document which modules are CMVP-validated (pristine), update-streams (patched but cryptographically equivalent), historical (validated but deprecated), or unvalidated?
- How will you assess whether update-stream patches maintain cryptographic equivalence to the validated baseline?
- What risk documentation and Plans of Action & Milestones (POA&Ms) are required for historical or unvalidated modules?
- Will you implement automated alerting when modules transition from one status to another?
- What is your timeline for migrating from deprecated FIPS 140-2 to FIPS 140-3 validated modules?

FedRAMP Alignment: FRR-UCM-04 (Risk-Based Module Management), FRR-UCM-02/03 (Default Use of Validated Modules)

---

**AFR-11-Q008: AI Model Artifact Cryptographic Protection Requirements**

What cryptographic protection standards will you enforce for AI-specific sensitive data categories including model weights, fine-tuned adapters, training datasets, embeddings, and prompt/completion logs?

Decision Points:
- Will you classify model artifacts according to their sensitivity level based on training data classification?
- How will you ensure CMVP-validated modules protect model registries, vector databases, and training archives?
- Will you implement model lineage tracking that propagates cryptographic requirements through fine-tuning and adaptation?
- What cryptographic protection will you apply to inference logs that may contain PII or controlled unclassified information?
- How will you prevent agent-generated intermediate states from persisting unencrypted?

FedRAMP Alignment: FRR-UCM-01 (Module Documentation for AI Data Categories), NIST SP 800-53 SC-28

---

**AFR-11-Q009: Post-Quantum Cryptography Readiness for AI Systems**

How will your organization plan for post-quantum cryptography (PQC) adoption in AI services while maintaining CMVP validation requirements and FedRAMP compliance?

Decision Points:
- Will you establish policy limiting PQC activation to CMVP-validated implementations of NIST-selected algorithms (CRYSTALS-Kyber, Dilithium)?
- How will you prevent AI agents from activating experimental or non-validated PQC implementations?
- What is your timeline for hybrid key exchange deployment (classical + quantum-resistant)?
- Will you document PQC module status and validation timelines in your cryptographic inventory?
- How will you coordinate with FedRAMP and CMVP on algorithm certification status and approved transition paths?

FedRAMP Alignment: FRR-UCM-01 (Documentation), FRR-UCM-02/03 (Validated Module Use), Federal PQC Guidance

---

**AFR-11-Q010: Agent Authentication and Authorization to Key Management Systems**

How will you design authentication and authorization for AI agents accessing Key Management Systems (KMS) or Hardware Security Modules (HSM) to minimize cryptographic key compromise blast radius?

Decision Points:
- Will you implement least-privilege access where agents can only access cryptographic keys for specific, authorized operations?
- How will you prevent agent credential compromise from exposing federal customer encryption keys?
- Will you isolate agent infrastructure from federal customer data paths through cryptographic boundaries?
- What rate limiting and anomaly detection will you apply to agent-to-KMS operations?
- How will you audit and alert on suspicious agent access patterns to cryptographic key stores?

FedRAMP Alignment: FRR-UCM-01 (Documentation of Key Access Patterns), NIST SP 800-53 AC-6 (Least Privilege)

---

### Evaluation Subsection

**AFR-11-Q011: Complete Cryptographic Module Inventory Verification**

How will the CSP demonstrate that its documented cryptographic module inventory (SSP Appendix Q) is complete and accurate?

Evaluation Criteria:
- Does the CSP provide a machine-readable inventory (JSON/YAML) mapping cryptographic modules to infrastructure components?
- Can the CSP demonstrate that automated discovery tools (SCA, IaC scanning, runtime profiling) have identified 100% of cryptographic modules?
- How frequently is the inventory updated (daily, weekly, quarterly)?
- What percentage of cryptographic modules were discovered only during security assessment vs pre-identified in documentation?
- Can the CSP provide independent verification that documented inventory matches deployed infrastructure (e.g., third-party scanning validation)?

Risk If Inadequate: 71% of AI services discover untracked cryptographic modules only during assessment, creating authorization failure risk if FedRAMP assessor finds undocumented modules.

FedRAMP Alignment: FRR-UCM-01

---

**AFR-11-Q012: AI Agent Cryptographic Compliance Guardrails**

What guardrails prevent DevSecOps copilots and infrastructure automation agents from silently modifying cryptographic configurations to non-FIPS or non-CMVP-validated modules?

Evaluation Criteria:
- Does the CSP implement policy-as-code that blocks deployment of non-FIPS TLS libraries?
- Are agent-proposed cryptographic configuration changes subject to approval workflows?
- What percentage of cryptographic changes are proposed by agents vs manually initiated by humans?
- Can the CSP demonstrate that enforcement is applied at multiple points (IaC validation, admission controllers, runtime enforcement)?
- What audit logging demonstrates that agents are not bypassing cryptographic controls?

Risk If Inadequate: 58% of CSPs have agent-driven changes to cryptographic configurations, yet only 23% have documented guardrails preventing agents from violating FIPS requirements.

FedRAMP Alignment: FRR-UCM-02/03

---

**AFR-11-Q013: Cryptographic Compliance Validation Cadence**

How frequently does the CSP validate that deployed cryptography matches documented FIPS/CMVP compliance requirements?

Evaluation Criteria:
- Does the CSP scan cryptographic endpoints (TLS certificates, cipher suites, module versions) every 1-4 hours, or rely on manual quarterly assessments?
- What is the mean time to detection (MTTD) when cryptographic drift occurs (goal: <4 hours vs 30+ days for manual)?
- Does the CSP have automated systems that detect unexpected cryptographic modules, algorithms, or configurations?
- Can the CSP provide drift detection metrics for the past 12 months showing number of drifts discovered and remediation time?
- What is the process for automated vs manual remediation of detected drifts?

Risk If Inadequate: Cryptographic configuration drift now occurs 50-150 times per day in AI infrastructure with agent automation. Manual quarterly reviews miss 99.7% of drifts.

FedRAMP Alignment: FRR-PVA

---

**AFR-11-Q014: Multi-Tenant Cryptographic Isolation Enforcement**

For multi-tenant AI services, what cryptographic mechanisms ensure that one federal agency tenant's data cannot be decrypted by another tenant?

Evaluation Criteria:
- Does the CSP implement per-tenant key encryption keys (KEKs) derived from a master key in HSM/KMS?
- Is 100% of federal customer data encrypted under tenant-specific encryption keys?
- Does the CSP provide per-tenant audit logging showing which cryptographic keys were used for which operations?
- Can the CSP demonstrate that encryption/decryption boundaries are enforced at the storage, transit, and logging layers?
- What is the documented cryptographic boundary proving multi-tenant separation?

Risk If Inadequate: 9 of 12 audited FedRAMP AI services had incomplete per-tenant cryptographic documentation, risking federal data exposure and authorization denial.

FedRAMP Alignment: FRR-MAS, Multi-Tenant Data Separation Requirements

---

**AFR-11-Q015: Hardware Accelerator Firmware Validation Strategy**

Given that GPU/TPU firmware updates occur every 6-8 weeks but CMVP validation lags 4-6 months, how does the CSP avoid validation gaps where cryptographic modules are either vulnerable or unvalidated?

Evaluation Criteria:
- Does the CSP maintain a firmware inventory tracking CMVP certification status and known vulnerabilities?
- Has the CSP established vendor relationships with GPU/TPU manufacturers for accelerated CMVP revalidation after critical patches?
- What percentage of accelerator nodes are running validated firmware versions vs unvalidated or historical firmware?
- What is the maximum acceptable time window where hardware firmware is unvalidated?
- Can the CSP provide firmware version attestation evidence?

Risk If Inadequate: 73% of AI clusters have cryptographic modules in "historical status" transitions, creating 4-6 month periods where modules are either vulnerable or unvalidated.

FedRAMP Alignment: FRR-UCM-03 (Validated Modules for Hardware Cryptography)

---

**AFR-11-Q016: AI Framework Cryptographic Dependency Visibility**

Can the CSP provide software bill of materials (SBOM) demonstrating which AI SDKs embed cryptographic modules and whether those modules are CMVP-validated?

Evaluation Criteria:
- Does the CSP perform software composition analysis (SCA) on all AI framework dependencies (PyTorch, TensorFlow, LangChain, Hugging Face, etc.)?
- What percentage of discovered cryptographic dependencies are CMVP-validated vs non-validated?
- How frequently is the SBOM updated (daily, weekly)?
- Does the CSP have a suppression/exception process for acceptable non-FIPS dependencies with documented risk justification?
- What developer training exists explaining why embedded non-FIPS cryptography is a compliance concern?

Risk If Inadequate: 61% of AI services have embedded cryptographic modules in AI SDKs. 71% of AI services discovered untracked modules only during assessment, suggesting SBOMs are incomplete.

FedRAMP Alignment: FRR-UCM-01, FRR-AFR-04 (Supply Chain Vulnerability Detection)

---

**AFR-11-Q017: Cryptographic Module Update-Stream and Deprecation Management**

As FIPS 140-2 is deprecated (formal sunsetting December 2026), how is the CSP migrating to FIPS 140-3 while managing modules that use "update streams" or historical validations?

Evaluation Criteria:
- Does the CSP have a documented migration timeline from FIPS 140-2 to FIPS 140-3 modules?
- For modules using update-stream patches, does the CSP assess and document cryptographic equivalence to validated baselines?
- Does the CSP have Plans of Action & Milestones (POA&Ms) for modules in historical status or non-validated status?
- What percentage of deployed cryptographic modules use each status: pristine-validated, update-stream, historical, unvalidated?
- How does the CSP ensure update-stream modules maintain security and compliance?

FedRAMP Alignment: FRR-UCM-04 (Risk-Based Module Management), FRR-UCM-02/03

---

**AFR-11-Q018: Vector Database and Embedding Cryptographic Protection**

What cryptographic protection standards does the CSP enforce for vector databases, embeddings, and retrieval-augmented generation (RAG) systems that process federal customer data?

Evaluation Criteria:
- Are vector databases encrypted at rest and in transit using CMVP-validated modules?
- How are embeddings classified for sensitivity based on the source data they represent?
- Does the CSP implement per-tenant encryption contexts for vector stores in multi-tenant RAG systems?
- What cryptographic modules protect similarity search operations and retrieval results?
- Can the CSP demonstrate that embedding models and vector indices are protected with the same rigor as training data?

Risk If Inadequate: Vector databases and embeddings can encode sensitive patterns from federal data, yet may not be included in traditional cryptographic inventories.

FedRAMP Alignment: FRR-UCM-01 (AI-Specific Data Category Documentation)

---

**AFR-11-Q019: Federated Learning Cryptographic Guarantees**

If the CSP supports federated learning, what cryptographic guarantees protect model updates, aggregated gradients, and participant contributions?

Evaluation Criteria:
- Does the CSP use CMVP-validated modules for encrypting local model updates before aggregation?
- How does the CSP prevent the aggregation server from accessing individual participant data?
- What cryptographic protocols (secure multi-party computation, homomorphic encryption) are employed, and are they validated?
- Does the CSP implement per-participant key management preventing cross-participant exposure?
- Can the CSP demonstrate that federated learning cryptographic boundaries are documented in SSP Appendix Q?

Risk If Inadequate: Federated learning without proper cryptographic protection can expose federal participant contributions to other participants or the aggregation server.

FedRAMP Alignment: FRR-UCM-01 (Documentation), FRR-MAS (Federated Learning Scope)

---

**AFR-11-Q020: Model Serving Gateway Cryptographic Validation**

What cryptographic validation does the CSP perform on inference API gateways and model serving endpoints that handle federal customer prompts and completions?

Evaluation Criteria:
- Does the CSP validate that model serving gateways use CMVP-validated TLS stacks for all federal customer connections?
- How frequently are gateway cipher suites and protocol versions audited for FIPS compliance?
- What cryptographic protection exists for prompt caching, request routing, and completion buffering?
- Does the CSP implement mutual TLS (mTLS) for service-to-service model invocation?
- Can the CSP demonstrate that gateway cryptographic configurations are included in continuous validation scanning?

Risk If Inadequate: Model serving gateways represent critical cryptographic enforcement points; misconfiguration exposes federal prompts and completions in transit.

FedRAMP Alignment: FRR-UCM-02/03 (Gateway TLS Validation)

---

**AFR-11-Q021: Agent Memory and Context Cryptographic Protection**

How does the CSP protect agent memory, conversation context, and intermediate reasoning states using cryptographic modules?

Evaluation Criteria:
- Are agent memory stores (conversation history, context windows, intermediate tool outputs) encrypted at rest using CMVP-validated modules?
- Does the CSP implement per-session or per-user encryption keys for agent memory isolation?
- What cryptographic protection exists for agent checkpoints and state snapshots?
- How does the CSP prevent agent memory from leaking across security boundaries or tenant contexts?
- Can the CSP demonstrate that agent memory infrastructure is included in cryptographic module inventory?

Risk If Inadequate: Agent memory can contain accumulated sensitive information from multiple interactions, creating high-value targets if not properly encrypted.

FedRAMP Alignment: FRR-UCM-01 (Documentation), NIST SP 800-53 SC-28 (Protection at Rest)

---

### Validation and Testing Subsection

**AFR-11-Q022: Cryptographic Module Inventory Completeness Testing**

What evidence demonstrates that all cryptographic modules protecting federal customer data are documented in SSP Appendix Q and that the documentation is verified against deployed infrastructure?

Testing Approach:
- Request the CSP's cryptographic module inventory (machine-readable format) and compare against deployed infrastructure via independent scanning tools
- Verify the inventory includes all 8+ categories: API gateways, service meshes, inference serving, data movement, storage, specialized stacks (vector databases), hardware, SDKs
- Conduct random sampling: select 20-30 deployed services and verify each cryptographic module is documented
- Check for completeness: are embedded cryptographic modules in AI SDKs included?
- Validate: run independent SCA tools and compare discovered modules against CSP's inventory; target 95%+ match rate
- Review: what percentage of modules were discovered by SCA before vs after CSP's last assessment?

Evidence Required:
- Machine-readable inventory (JSON/YAML) with module names, locations, versions, CMVP validation status
- SCA reports showing all direct and transitive cryptographic dependencies
- IaC scanning reports identifying cryptographic modules in Kubernetes manifests, Docker images, Terraform configurations
- Audit logs from automated discovery systems showing when modules were first identified
- Documentation of any modules discovered during assessment not previously identified

Risk Threshold: If <90% of discovered modules were pre-documented, escalate as control failure.

FedRAMP Alignment: FRR-UCM-01

---

**AFR-11-Q023: Agent-Proposed Cryptographic Change Validation Testing**

What evidence demonstrates that autonomous agents proposing cryptographic configuration changes are subject to compliance validation and that non-compliant changes are blocked?

Testing Approach:
- Request policy-as-code (OPA, NetworkPolicy rules) implementing cryptographic constraints
- Review change logs for past 90 days: identify all cryptographic configuration changes (TLS versions, cipher suites, key rotation, module selection)
- For each change, determine: was it agent-proposed or manually initiated? Did it undergo approval workflow?
- Test: attempt to deploy a non-compliant configuration (e.g., non-FIPS TLS library) via infrastructure automation; verify it is blocked
- Audit logging: verify all cryptographic changes are logged with timestamp, actor (agent name or human), change description, approval status
- Query RBAC: confirm agents have read-only access to cryptographic configuration or require approval for modifications
- Analyze: what percentage of proposed agent changes were rejected for compliance violations?

Evidence Required:
- Policy-as-code rules explicitly constraining cryptographic deployments
- Change logs for all cryptographic configuration modifications in past 12 months
- Approval workflow documentation showing human or AI validator review of agent-proposed changes
- Admission controller logs showing blocks of non-compliant deployments
- RBAC definitions limiting agent access to cryptographic systems
- Audit logs correlating change timestamps with approval workflow completion

Risk Threshold: If >1% of agent-proposed changes bypass compliance validation, escalate as control failure.

FedRAMP Alignment: FRR-UCM-02/03

---

**AFR-11-Q024: Continuous Validation Service-Level Objective Testing**

What evidence demonstrates that automated systems detect cryptographic compliance violations within 4 hours (vs 30+ days for manual review)?

Testing Approach:
- Request continuous validation system logs for past 90 days
- Identify detected drifts: unintended deviations from documented baseline (e.g., TLS certificate expiration, cipher suite change, module version update)
- For each drift, measure: time from occurrence to detection, severity level assigned, remediation time
- Calculate metrics: mean time to detection (MTTD), mean time to remediation (MTTR)
- Spot-check: select 5 known drifts and verify they were detected and logged
- Test: introduce a simulated drift (e.g., modify a TLS configuration) and measure detection latency
- Verify: does the automated system alert when drift exceeds acceptable thresholds?
- Review: are alerts escalated to SIEM and incident response teams?

Evidence Required:
- Automated scanning system logs showing scan frequency and scope (target: every 1-4 hours across all services)
- Drift detection logs for past 12 months including detection timestamp, drift description, severity, remediation action
- Remediation metrics: MTTD, MTTR, percentage of drifts automatically vs manually resolved
- Alert configuration showing severity levels and escalation procedures
- SIEM integration logs showing alerts forwarded to incident response
- Test results demonstrating detection latency <4 hours

Risk Threshold: If MTTD >24 hours or >10% of drifts are not detected before next scheduled assessment, escalate as control failure.

FedRAMP Alignment: FRR-PVA

---

**AFR-11-Q025: Per-Tenant Cryptographic Isolation Testing**

What evidence demonstrates that each federal agency tenant's data is encrypted under distinct cryptographic keys preventing cross-tenant exposure?

Testing Approach:
- Request cryptographic architecture documentation showing key hierarchy: Master Key → Per-Tenant KEK → Data Encryption Keys
- Request audit logs for past 90 days showing all encryption/decryption operations with tenant context
- Conduct data access testing: request tenant A's encrypted data, attempt to decrypt using tenant B's cryptographic keys; verify decryption fails
- Verify: is 100% of federal customer data encrypted under tenant-specific keys?
- Test: compromise one tenant's encryption keys; verify data from other tenants remains inaccessible
- Review: are encryption/decryption operations audited with tenant identifier, operation timestamp, and data classification?
- Check: what is the frequency of per-tenant key rotation?
- Validate: does the CSP have per-tenant incident response procedures if one tenant's keys are compromised?

Evidence Required:
- Cryptographic architecture documentation with key hierarchy diagram
- HSM/KMS logs showing per-tenant key creation, rotation, and usage
- Encryption metadata showing data-to-tenant-key mappings
- Audit logs for all encryption/decryption operations with tenant identifiers
- Test results demonstrating cross-tenant decryption is cryptographically impossible
- Per-tenant key rotation logs for past 12 months
- Documented multi-tenant breach response procedures

Risk Threshold: If any federal customer data is encrypted under shared keys or if cross-tenant decryption is possible, escalate as critical control failure.

FedRAMP Alignment: FRR-MAS, Multi-Tenant Data Separation

---

**AFR-11-Q026: Hardware Accelerator Cryptographic Module Status Testing**

What evidence demonstrates firmware versions for GPU/TPU accelerators are CMVP-validated or have documented risk acceptances?

Testing Approach:
- Request firmware inventory for all GPU/TPU nodes deployed for federal customer workloads
- Cross-reference firmware versions against CMVP certification database; verify status of each version
- Identify any firmware in "historical" status or unvalidated status; request risk documentation or POA&M
- Review: what is the CSP's firmware update frequency vs CMVP validation lag?
- Test: query a GPU/TPU node to verify reported firmware version matches documented inventory
- Analyze: what percentage of accelerator nodes are running validated vs unvalidated firmware?
- Check: does the CSP have firmware version attestation mechanisms to prevent downgrade attacks?
- Validate: has the CSP coordinated with hardware vendors for accelerated CMVP revalidation after critical patches?

Evidence Required:
- Firmware inventory for all deployed GPU/TPU accelerators with versions and deployment dates
- CMVP certification status for each firmware version
- Risk documentation or POA&M for any unvalidated firmware
- Firmware update logs showing deployment dates and versions
- Firmware version attestation evidence (signed firmware, version reporting logs)
- Vendor coordination agreements showing relationships with GPU/TPU manufacturers
- Test results confirming deployed firmware versions match documented inventory

Risk Threshold: If >10% of deployed firmware is unvalidated without documented risk acceptance, escalate as control concern.

FedRAMP Alignment: FRR-UCM-03 (Hardware Cryptographic Module Validation)

---

**AFR-11-Q027: Cryptographic Supply Chain SBOM Completeness Testing**

What evidence demonstrates the CSP has identified and documented all cryptographic dependencies embedded in AI frameworks, and assesses their validation status?

Testing Approach:
- Request software bill of materials (SBOM) for all AI frameworks used in federal customer services
- Identify cryptographic components in SBOM: OpenSSL versions, BoringCrypto, custom TLS clients, SDK-embedded crypto
- Cross-reference each cryptographic component against CMVP database; verify validation status
- Review: what percentage of cryptographic dependencies are CMVP-validated vs non-validated?
- Check: how frequently is SBOM updated (goal: daily)?
- Test: request CSP to identify cryptographic dependencies in a randomly selected service; verify against SBOM
- Validate: does the CSP have suppression/exception process for non-FIPS dependencies with risk documentation?
- Analyze: has the CSP discovered new cryptographic dependencies in past 12 months? How was discovery time measured?

Evidence Required:
- SBOM in standard format (SPDX, CycloneDX) for all AI frameworks and dependencies
- Cryptographic component inventory highlighting TLS clients, OpenSSL, and custom crypto modules
- CMVP validation status for each cryptographic component
- SCA tool reports (Snyk, FOSSA, Black Duck) showing discovery of cryptographic dependencies
- SBOM update logs showing daily/weekly refresh frequency
- Exception/suppression documentation for any non-FIPS cryptographic dependencies with risk justification
- Developer training materials explaining embedded cryptography compliance concerns

Risk Threshold: If SBOM is >30 days stale or missing >5% of cryptographic dependencies, escalate as control failure.

FedRAMP Alignment: FRR-UCM-01, FRR-AFR-04 (Supply Chain Vulnerability Detection)

---

**AFR-11-Q028: FIPS 140-2 Deprecation and Migration Testing**

What evidence demonstrates the CSP has a migration plan from deprecated FIPS 140-2 to FIPS 140-3 and documents the use of update-stream or historical cryptographic modules?

Testing Approach:
- Request inventory of all cryptographic modules categorized by status: FIPS 140-3 validated, FIPS 140-2 validated, update-stream, historical, unvalidated
- Review migration timeline: what is the CSP's plan to migrate from 140-2 to 140-3? Target completion date?
- For each update-stream module: request documentation showing cryptographic equivalence to validated baseline
- Verify: are all update-stream deployments documented in SSP with change justification?
- Check: for any historical or unvalidated modules, does the CSP have POA&M with timeline and risk acceptance?
- Analyze: what vulnerabilities or performance improvements justified each update-stream patch?
- Validate: how does the CSP verify that update-stream patches maintain cryptographic security properties?

Evidence Required:
- Cryptographic module status inventory (validated, update-stream, historical, unvalidated) with deployment counts
- FIPS 140-2 to 140-3 migration roadmap with target completion date
- Update-stream documentation for each patched module showing: baseline version, patch change, cryptographic equivalence assessment
- Risk documentation or POA&M for any historical or unvalidated modules
- Vulnerability or performance justification for each update-stream deployment
- Testing evidence that update-stream patches maintain cryptographic equivalence
- Plan of Action & Milestones for deprecation timeline

Risk Threshold: If >50% of cryptographic modules are still FIPS 140-2 with no documented migration plan, escalate as control weakness requiring POA&M.

FedRAMP Alignment: FRR-UCM-04 (Risk-Based Module Management), FRR-UCM-02/03

---

**AFR-11-Q029: Service Mesh Cryptographic Configuration Validation**

What evidence demonstrates that service mesh sidecars and control planes use CMVP-validated cryptographic modules for east-west traffic encryption in AI microservices?

Testing Approach:
- Request service mesh architecture documentation identifying all cryptographic enforcement points (Envoy sidecars, Linkerd proxies, Istio control plane)
- Verify cryptographic module inventory includes service mesh TLS stacks with version information
- Test: capture east-west traffic between AI microservices and verify mTLS is enforced with FIPS-compliant cipher suites
- Check: are service mesh cipher suite configurations centrally managed and validated against FIPS requirements?
- Review: what percentage of inter-service connections use validated cryptographic modules vs non-validated?
- Analyze: can agents or developers modify service mesh cryptographic configurations without approval?
- Validate: are service mesh certificate rotations logged and monitored for compliance?

Evidence Required:
- Service mesh cryptographic module inventory with versions and validation status
- Service mesh configuration files showing TLS enforcement and cipher suite requirements
- Traffic capture demonstrating mTLS with FIPS-compliant cipher suites
- Change management logs for service mesh cryptographic configuration modifications
- Certificate rotation logs showing frequency and automation
- Policy enforcement evidence preventing unauthorized service mesh crypto changes

Risk Threshold: If >5% of east-west traffic lacks validated cryptographic protection, escalate as control failure.

FedRAMP Alignment: FRR-UCM-01 (Service Mesh Inventory), FRR-UCM-02/03 (Validated Modules)

---

**AFR-11-Q030: Cryptographic Agility Governance Testing**

What evidence demonstrates the CSP constrains AI-driven cryptographic algorithm selection to prevent non-compliant configurations while maintaining operational flexibility?

Testing Approach:
- Request cryptographic agility policy defining approved algorithms, key lengths, and validation requirements
- Identify AI systems or agents with authority to select cryptographic algorithms dynamically
- Test: attempt to trigger dynamic algorithm selection that would violate FIPS requirements; verify it is blocked
- Review: what cryptographic algorithms are available for AI system selection? Are all CMVP-validated?
- Analyze: how does the CSP balance performance optimization with cryptographic compliance constraints?
- Verify: are all algorithm selection decisions logged with justification and validation status?
- Check: does the CSP have approved transition paths for post-quantum cryptography that constrain AI systems?

Evidence Required:
- Cryptographic agility policy document defining approved algorithms and constraints
- Algorithm selection logs showing which systems made selections and which algorithms were chosen
- Test results demonstrating non-compliant algorithm selections are blocked
- Policy-as-code rules constraining AI system algorithm selection
- Documentation showing all selectable algorithms are CMVP-validated or documented as update-streams
- PQC transition plan with approved algorithm list for AI system use

Risk Threshold: If AI systems can select non-validated algorithms without constraint, escalate as control failure.

FedRAMP Alignment: FRR-UCM-02/03 (Validated Module Default Use), FRR-UCM-04 (Algorithm Governance)

---

**AFR-11-Q031: AI-Driven Cryptographic Supply Chain Threat Detection**

What evidence demonstrates the CSP detects and prevents supply chain attacks targeting cryptographic module governance in AI systems?

Testing Approach:
- Request threat detection procedures for cryptographic supply chain attacks (malicious packages, dependency confusion, compromised modules)
- Review: does the CSP scan for malicious cryptographic libraries masquerading as legitimate dependencies?
- Test: attempt to introduce a dependency with a name similar to a legitimate cryptographic module (typosquatting); verify detection
- Analyze: what monitoring exists for prompt injection or agent manipulation targeting cryptographic controls?
- Verify: does the CSP validate cryptographic module signatures and attestations before deployment?
- Check: are AI frameworks and dependencies obtained from verified sources with cryptographic integrity checks?
- Review: has the CSP conducted red team exercises specifically targeting cryptographic governance?

Evidence Required:
- Supply chain threat detection procedures and tooling configuration
- Dependency scanning reports identifying cryptographic components and their trust status
- Signature verification logs for cryptographic modules and dependencies
- Red team exercise reports testing cryptographic governance attack vectors
- Incident response procedures for cryptographic supply chain compromise
- Monitoring alerts for prompt injection or agent attempts to modify cryptographic configurations

Risk Threshold: If no supply chain threat detection exists for cryptographic dependencies, escalate as control gap.

FedRAMP Alignment: FRR-AFR-04 (Supply Chain Security), FRR-UCM-01 (Module Provenance)

---

## Implementation Guidance

**For CIOs and Security Leaders:**
Use questions AFR-11-Q001 through AFR-11-Q010 to guide strategic decisions on cryptographic governance architecture, agent constraints, validation systems, and multi-tenant isolation.

**For Federal Customers and Assessors:**
Use questions AFR-11-Q011 through AFR-11-Q021 to evaluate CSP cryptographic capabilities, validate documentation completeness, and assess risk exposure.

**For Auditors and Third-Party Assessors:**
Use questions AFR-11-Q022 through AFR-11-Q031 to design control testing procedures, collect evidence, and validate that cryptographic module controls are effectively implemented.

---

## Next Steps

1. **Human Review and Approval:** This question library requires review and approval before proceeding to JSON generation.

2. **Global Question Set Generation:** Upon approval, generate AFR-11_questions_global.json with questions formatted for enterprise-wide assessment (Q-AFR-11-001 format).

3. **Binding Question Set Generation:** Upon approval, generate AFR-11_questions_binding.json with questions formatted for FedRAMP authorization boundary assessment (AFR-11-B01 format).

4. **Integration:** Questions will be integrated into the agenticAI_20xKSI assessment framework for AI-enabled FedRAMP evaluations.

---

**Document Control:**
- Date: January 12, 2026
- Status: Awaiting Human Approval
- Repository: agenticAI_20xKSI
- KSI: AFR-11 - Using Cryptographic Modules
- Question Count: 31 (21 original + 10 added)
