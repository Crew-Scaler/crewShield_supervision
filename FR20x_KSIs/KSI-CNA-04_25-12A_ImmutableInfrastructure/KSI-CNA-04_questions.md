# Immutable Infrastructure: Discovery Questions

**KSI Focus:** CNA-04 - Utilize immutable infrastructure for all cloud service components, with emphasis on AI systems, agents, and artifact supply chains. Implement container-based deployments, immutable artifact versioning, infrastructure-as-code, and cryptographic audit trails to prevent runtime tampering and ensure auditability for AI workloads.

**Context:** This discovery question set focuses exclusively on immutable infrastructure for AI systems, filtering for artifact immutability, supply chain integrity, strictly-defined privilege models, infrastructure-as-code, drift detection, and cryptographic audit trail integrity. Questions assess explicit enforcement of immutability, configuration immutability via IaC, privilege immutability (scoped and time-bound), and tamper-proof audit evidence.

**Note on Scope:** Questions about general agent identity/authentication (e.g., which framework, latency SLOs, continuous vs. session auth, delegation protocols) have been moved to KSI-IAM-07 "Automated Account Management" or a dedicated AI-IAM KSI, as they address identity behavior rather than immutable infrastructure. Similarly, broader governance/compliance automation (automated compliance reporting, policy-as-code enforcement) belong to KSI-CMT-01/CMT-03 or other governance KSIs. Questions about privilege escalation path analysis and behavioral anomaly detection belong to KSI-CNA-08 "Automated Enforcement" or security monitoring KSIs. This CNA-04 scope focuses strictly on preventing tampering, enforcing immutability, and validating evidence of immutable baselines.

---

## Section 1: AI Agent Credential & Privilege Immutability

**KSI-CNA-04-Q1:** How do you prevent agent credential compromise? Describe controls: (a) credential lifetime (short-lived vs. long-lived), (b) credential storage (never in code/logs), (c) credential rotation frequency, (d) revocation procedures if compromise suspected. Explain how these controls ensure credential immutability (credentials cannot be altered in flight or at rest).

**KSI-CNA-04-Q2:** Have you experienced AI agent credential compromise in past 12 months? For each incident: detection method, dwell time (time from compromise to detection), blast radius (what systems accessed with compromised credentials), remediation. What controls failed to prevent or detect the compromise?

---

## Section 2: AI Agent Authorization & Strictly-Defined Privileges

**KSI-CNA-04-Q3:** What authorization model is used for AI agents: traditional RBAC, attribute-based access control (ABAC), task-based access control (TBAC), or other? For agents, can you enforce permissions scoped to specific tasks with automatic revocation upon completion? How does your model enforce immutability of privilege definitions?

**KSI-CNA-04-Q4:** Describe privilege model for production agents. For each agent, document: (a) resources that can be accessed (APIs, databases, files), (b) operations permitted (read/write/delete), (c) time-based constraints (24/7 or business hours only), (d) rate limits (requests/minute, data volume limits). Provide evidence these privileges are immutably defined and enforced.

**KSI-CNA-04-Q5:** Do you implement least-privilege access for agents? Provide examples: (a) agents assigned minimal permissions needed for specific task, (b) permissions scoped by resource type, (c) permissions scoped by operation (GET vs. POST), (d) temporal constraints (permissions valid only during task execution). How do you prevent unauthorized modification of these privilege definitions?

**KSI-CNA-04-Q6:** For agents with broad permissions (high-risk), how do you prevent privilege escalation and enforce privilege immutability? Identify agents that can call administrative APIs or access sensitive roles. For each overprivileged agent, describe: risk assessment, mitigations (segmentation, monitoring), remediation timeline.

---

## Section 3: Supply Chain Integrity & Artifact Governance

**KSI-CNA-04-Q7:** How do you ensure AI artifact supply chain integrity? For models, training data, dependencies, describe: (a) artifact versioning (explicit versions, never `latest` in production), (b) artifact signing (cryptographic signatures), (c) provenance tracking (who built it, from what source, in what environment), (d) artifact immutability (cannot be overwritten post-release).

**KSI-CNA-04-Q8:** Do you implement Software Bill of Materials (SBOM) or AI Bill of Materials (AIBOM) for AI systems? Provide SBOM/AIBOM for 3-5 production AI models showing: all dependencies, versions, checksums, vulnerability scan results, licensing information.

**KSI-CNA-04-Q9:** What supply chain framework is used: SLSA (Supply chain Levels for Software Artifacts), in-house framework, other? Provide attestation of artifacts: signatures, SBOMs, scanning results, build environment logs. Benchmark: SLSA L2+ recommended for production AI.

**KSI-CNA-04-Q10:** For training data, how do you verify provenance and prevent poisoning? Describe: (a) data source verification (authorized sources only), (b) data quality checks (detect corrupted/malicious data), (c) data versioning (immutable snapshots), (d) detection of data poisoning (behavioral validation, anomaly detection).

**KSI-CNA-04-Q11:** Have you detected poisoned training data or backdoored models in past 12 months? Describe: how detected, what artifact was compromised, impact, remediation (retraining, rollback, model retire).

**KSI-CNA-04-Q12:** For third-party or pre-trained models, what verification is performed before deployment? Describe: (a) model provenance validation (where did it come from?), (b) training data vetting, (c) backdoor detection (adversarial testing), (d) vulnerability scanning, (e) required testing before production deployment.

---

## Section 4: Container & Artifact Immutability

**KSI-CNA-04-Q13:** For container images and model artifacts, is immutability enforced? Describe: (a) can released versions be overwritten or modified? (required: NO), (b) versioning scheme (semantic versioning, dates, commit hashes?), (c) artifact registry enforcement (append-only, no deletion in production).

**KSI-CNA-04-Q14:** Do you use `latest` tag in production, or explicit version numbers? Document artifact versioning policy. For any production deployments using `latest` tag, describe why and remediation timeline.

**KSI-CNA-04-Q15:** How do you manage container base images? Are base images: (a) hardened (distroless, minimal attack surface), (b) regularly scanned for vulnerabilities, (c) automatically patched (new base images built with security updates), (d) immutably pinned (by digest, not tag)?

**KSI-CNA-04-Q16:** What is your process for validating artifact integrity? Describe: (a) signature verification (cryptographic validation of artifacts), (b) checksum validation (detect tampering), (c) automated validation in CI/CD pipeline, (d) evidence of validation for 10 recent deployments.

**KSI-CNA-04-Q17:** Have you experienced artifact tampering or unauthorized modifications in past 12 months? Describe detection method, impact, root cause (registry misconfiguration, stolen credentials, insider threat).

---

## Section 5: Infrastructure-as-Code & Drift Detection

**KSI-CNA-04-Q18:** Is your infrastructure defined as code (IaC): Terraform, Kubernetes YAML, CloudFormation, or other? What percentage of infrastructure is IaC vs. manually configured? For AI agent workloads, is 100% IaC required?

**KSI-CNA-04-Q19:** How do you prevent configuration drift (manual changes diverging from declared IaC)? Describe controls: (a) automatic drift detection (compare actual vs. desired state), (b) alerting (notify when drift detected), (c) remediation (auto-correct drift or require approval), (d) audit trail (log all drift and corrections).

**KSI-CNA-04-Q20:** How often do you check for configuration drift? Drift detection interval (continuous, hourly, daily)? For AI agents, what is acceptable drift tolerance (0% recommended)? Provide evidence of drift detection from past 30 days: frequency, what drifted, remediation.

**KSI-CNA-04-Q21:** Have you experienced configuration drift causing incidents in past 12 months? Describe: what configuration drifted, how detected, impact, root cause (manual change, automated tool misconfiguration), remediation.

**KSI-CNA-04-Q22:** For AI agent workloads, are deployment changes validated before reaching production? Describe CI/CD validation: (a) policy validation (resources match security requirements), (b) privilege validation (permissions are least-privilege), (c) artifact validation (images/models are signed/verified), (d) approval workflow (manual review required?).

---

## Section 6: Runtime Security & Audit Integrity

**KSI-CNA-04-Q23:** For runtime security of AI agents, how do you enforce immutable baselines? Describe monitoring/enforcement: (a) what baseline (image, configuration, policy) is considered immutable?, (b) how is deviation from baseline detected?, (c) can baseline be updated only through controlled deployment?, (d) evidence of baseline enforcement from past 30 days.

**KSI-CNA-04-Q24:** Can you prove that audit logs are tamper-proof (cryptographic integrity, blockchain, other)? Describe mechanism ensuring audit logs cannot be modified or deleted. For forensic investigation, can you prove logs were not tampered with post-incident?

**KSI-CNA-04-Q25:** If agent is compromised and runtime changes made (configuration modified, credentials stolen), how would you detect tampering? Describe: (a) runtime integrity checking (detect unauthorized changes), (b) immutability enforcement (prevent runtime modification), (c) recovery procedures (restore from known-good state), (d) evidence of tampering detection from past incidents.

---

## Schema Reference

**Question ID Format:** [KSI-CODE]-Q##
Example: KSI-CNA-04-Q1

**All questions should be answered with:**
- Direct evidence (not claims)
- Quantifiable data where applicable
- Supporting documentation (architecture diagrams, policies, audit logs, test results)
- AI-specific examples where relevant
- Timeline/frequency information
- Comparison to research benchmarks when available

---

**Version:** 2.0 (Refined for Immutable Infrastructure Focus)
**Generated:** 2026-01-13
**Last Reviewed:** 2026-01-13 (Issue #21 filtering review)
