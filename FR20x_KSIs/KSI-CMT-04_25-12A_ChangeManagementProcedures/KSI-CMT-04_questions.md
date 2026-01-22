# AI-Driven Change Management Procedures: Discovery Questions

**KSI Focus:** CMT-04 - Establish and maintain documented change management procedures for all changes to the cloud service offering, with emphasis on AI systems, agents, and data.

**Context:** This discovery question set consolidates auditor, CIO, and customer perspectives to assess whether organizations effectively manage changes to AI systems through formal approval processes, audit trails, and governance structures. Questions focus on RFC procedures, CAB effectiveness, AI artifact governance, Shadow AI detection, emergency response, and regulatory compliance.

---

## Section 1: Formal Change Management Structure & Governance

**KSI-CMT-04-Q1:** Describe your change management organizational structure. Do you have: (a) a Change Management Office (CMO) with dedicated staff, (b) a Change Advisory Board (CAB) with representatives from security, compliance, operations, product, data governance, and legal? Provide CAB charter, membership roster, and meeting frequency for the past 12 months.

**KSI-CMT-04-Q2:** For high-risk changes (security patches, model deployments, agent policy updates), what is your approval workflow? Define: normal change approval timeline (target: 1-3 business days), emergency change approval SLA (target: <1 hour), and pre-approved standard changes (routine operational changes requiring minimal review).

**KSI-CMT-04-Q3:** Do you have an Emergency CAB (eCAB) for critical incidents? If so, describe: membership, 24/7 on-call rotation, review SLA (target: 15 minutes), and approval SLA (target: 1 hour). Provide evidence of eCAB activations in the past 12 months with timeline metrics.

**KSI-CMT-04-Q4:** How are RFC (Request for Change) templates enforced? Describe technical controls that prevent changes from being deployed without completing required RFC fields. Can changes bypass RFC approval through backdoor methods?

---

## Section 2: AI-Specific Artifact Governance

**KSI-CMT-04-Q5:** Do your change management procedures explicitly cover AI artifacts: (a) model versions and retraining, (b) training data updates and lineage, (c) agent policies and guardrails, (d) feature store schemas, (e) inference pipeline configurations? For each artifact type, describe the RFC template requirements and approval workflow.

**KSI-CMT-04-Q6:** What model registry or artifact management system do you use (MLflow, SageMaker, HuggingFace, custom)? For all production models, provide: (a) complete inventory with version, training date, training data version, approval status, (b) model governance documentation (model cards), (c) lineage tracking from training data to deployment, (d) approval chain with sign-off from ML governance, data owners, and compliance (if high-risk).

**KSI-CMT-04-Q7:** How do you track training data lineage and provenance? For high-risk AI models, can you demonstrate: (a) end-to-end lineage from data sources → transformations → checksums → model training → deployment, (b) data provenance validation (source authorization, licensing, bias assessment), (c) version control and audit trail for data changes?

**KSI-CMT-04-Q8:** For AI models deployed in the past 12 months, describe the change approval process for model updates. Provide 3-5 examples showing: RFC ID, model version, training data version, fairness/bias assessment results, adversarial robustness testing, approval chain, deployment date, and any rollback actions taken.

**KSI-CMT-04-Q9:** How do you version and manage agent policies and guardrails? Describe: (a) policy versioning system (Git, policy-as-code, custom), (b) approval workflow for policy changes, (c) testing procedures to verify agent behavior compliance with policy, (d) runtime guardrail enforcement (can agents violate policies?), (e) audit trail for policy violations detected.

**KSI-CMT-04-Q10:** Can you demonstrate traceability for AI-related incident investigation? Provide an example from the past 12 months where an AI system incident occurred. Show: (a) incident timeline, (b) which AI changes preceded the incident, (c) which changes likely caused it, (d) testing that should have caught the issue, (e) root cause identified through change history analysis.

---

## Section 3: Shadow AI Detection & Prevention

**KSI-CMT-04-Q11:** How do you detect and prevent unauthorized AI deployments ("Shadow AI")? Describe controls for: (a) unauthorized GenAI tool usage (ChatGPT, Copilot, Claude APIs), (b) rogue model deployments (models not in registry), (c) unapproved training data usage, (d) unvetted AI workloads in production. Provide detection architecture and tools used (CASB, DLP, network monitoring, container runtime security).

**KSI-CMT-04-Q12:** In the past 12 months, how many unauthorized AI deployments or Shadow AI incidents have been detected? For each incident: detection method, time to detection, time to remediation, root cause, and actions taken. What is your target detection rate (benchmark: 78%) and actual achieved rate?

**KSI-CMT-04-Q13:** What technical controls prevent deployment of unapproved AI models? Can employees deploy models to production without: (a) RFC approval, (b) model registry entry, (c) CAB sign-off? Describe enforcement mechanisms (CI/CD gates, Kubernetes admission controllers, policy as code) and test if enforcement can be bypassed.

---

## Section 4: Agent Governance & Autonomy Control

**KSI-CMT-04-Q14:** How many AI agents are currently deployed or in production? For each agent type, describe: (a) what actions agents can perform autonomously, (b) which actions require human approval before execution, (c) identity and authentication mechanism (cryptographic identity, short-lived credentials), (d) authorization scope (least-privilege access).

**KSI-CMT-04-Q15:** Are agent-initiated changes documented and approved through the same RFC process as human-initiated changes? Describe: (a) how agent actions are logged and auditable, (b) who approves agent capabilities before deployment, (c) how you prevent agents from exceeding authorized scope, (d) incident examples where agents behaved unexpectedly or violated authorized scope.

**KSI-CMT-04-Q16:** For each production agent, provide current policy version, approval records, and testing results showing agent behavior complies with policy constraints. If an agent policy changes, describe the testing process to verify guardrails still enforce intended constraints and agents cannot violate policies.

**KSI-CMT-04-Q17:** In the past 12 months, have you encountered any agent-related incidents (policy violations, cascading changes, policy escape, credential compromise)? For each incident, provide: timeline, how it was detected, impact (systems affected), root cause, remediation, and process improvements implemented.

---

## Section 5: Emergency Change Procedures & Incident Response

**KSI-CMT-04-Q18:** What qualifies as an "emergency change"? Provide definition and examples: (a) active security exploits requiring immediate patching, (b) critical customer outages, (c) detected model poisoning or data compromise, (d) regulatory mandates requiring immediate action. Describe when normal change approval can be bypassed for emergency changes.

**KSI-CMT-04-Q19:** Provide emergency change records for the past 12 months: change ID, emergency justification, eCAB approval timeline (request → review → approval), deployment timestamp, and post-implementation review completion date. Calculate: (a) median eCAB review time (target: ≤15 minutes), (b) median approval time (target: ≤1 hour), (c) PIR completion rate (target: 100% within 24 hours).

**KSI-CMT-04-Q20:** Describe your emergency change rollback capability. For critical changes (models, infrastructure, agents), can you rollback to the previous version in <15 minutes? Provide 2-3 recent examples of rollbacks: what triggered rollback, rollback time, and whether service was successfully restored.

**KSI-CMT-04-Q21:** How frequently do you test emergency change procedures (tabletop exercises, live drills)? Provide evidence of drills in the past 12 months: scenario, participants, objectives, timeline results, and lessons learned. Do drills meet timeline targets (15-min eCAB review, 1-hour approval, 15-min deployment)?

**KSI-CMT-04-Q22:** Describe your post-implementation review (PIR) process for all changes. For critical/emergency changes, do you conduct PIR within 24 hours? Provide sample PIRs for 3-5 significant changes from past 12 months showing: incident assessment, root cause analysis if issues occurred, testing results, lessons learned, and process improvements implemented.

---

## Section 6: Immutable Audit Trails & Compliance Evidence

**KSI-CMT-04-Q23:** How do you ensure change records are immutable and tamper-proof? Describe: (a) append-only storage (write-once, no modifications), (b) access controls (read-only for audit, no deletion permissions), (c) cryptographic integrity (signatures, checksums, blockchain-like hashing), (d) retention period (how long are change records retained?), (e) disaster recovery and backup for audit logs.

---

## Section 7: Change Documentation & Organizational Readiness

**KSI-CMT-04-Q24:** Do you have documented change management policies and procedures? Provide: (a) change management policy document, (b) RFC templates for all change types, (c) CAB procedures and decision criteria, (d) escalation procedures for blocked/rejected changes, (e) emergency change procedures with eCAB process, (f) post-implementation review procedures.

**KSI-CMT-04-Q25:** For customers deploying models or AI workloads to your platform, how do you enforce shared responsibility for change management? Describe: (a) customer change policies (must they follow your RFC process?), (b) what CSP logs automatically vs. customer must log, (c) audit visibility for customers (can they see changes to their deployed models?), (d) support for customer compliance needs (can you provide audit evidence to customers?).

**KSI-CMT-04-Q26:** In the past 12 months, have there been any incidents attributed to inadequate change management (unauthorized change, undocumented change, change deployed without approval)? For each incident: (a) what was changed without proper approval, (b) how was it discovered, (c) what was the customer impact, (d) root cause (policy bypass, enforcement gap, training gap), (e) remediation and process improvements implemented.

---

## Section 8: AI Code Review & SDLC Governance (from KSI-TPR-03)

**KSI-CMT-04-Q27:** For AI code review achieving high precision potential (99% potential vs. 83% for static analysis), what governance ensures reviewed code has actually been approved for production deployment? Address: (a) traceability from code review output to production deployment, (b) approval authority assigning responsibility for code review decisions, (c) separation of concerns (who reviews, who approves, who deploys), (d) audit trail linking each production deployment to corresponding code review, (e) procedures handling high-precision but false negative cases where malicious code evaded AI review, (f) testing to verify governance controls are effective and cannot be bypassed.

---

## Moved to Other KSIs

The following questions have been moved to other KSIs based on their primary focus area:

- **Q13 (Training/Awareness)** → CED-01/CED-02 (Training KSIs)
- **Q17 (Agent Behavior Anomaly Detection)** → MLA (Monitoring KSI)
- **Q18 (Credential Lifecycle & Management)** → IAM (Identity/Access Management KSI)
- **Q27-Q29 (Regulatory Compliance Mapping)** → GVN/COM (Compliance/Governance KSIs)
- **Q30-Q33 (Fairness, Bias, Adversarial Robustness Testing)** → Fairness/Bias/Adversarial Robustness KSIs
- **Q34-Q35 (Shadow AI Detection Metrics)** → MLA (Monitoring KSI)
- **Q37 (Change Management Training)** → CED (Training KSI)
- **Q38 (Shared Responsibility with Customers)** → Governance KSI

---

## Schema Reference

**Question ID Format:** [KSI-CODE]-Q##
Example: KSI-CMT-04-Q1

**All questions should be answered with:**
- Direct evidence (not claims)
- Quantifiable data where applicable
- Supporting documentation (policies, audit records, test results)
- AI-specific examples where relevant
- Timeline/frequency information
- Comparison to research benchmarks when available

---

**Version:** 2.0
**Generated:** 2026-01-13
**Last Modified:** 2026-01-13
