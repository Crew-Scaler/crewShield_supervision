# AI-Driven Change Logging and Monitoring: Discovery Questions

**KSI Focus:** CMT-01 - Log and monitor modifications to the cloud service offering (with emphasis on AI systems, agents, and data).

**Processing Summary (Issue #13 Refinement - Task 2 Fine-tuning):**
This document reflects human review feedback from GitHub issue #13 (Cybonto, 2026-01-08). Task 2 fine-tuning applies the following pruning per issue comment guidance:

**Sections & Questions Removed (Out-of-Scope):**
- Section 9 (Alert Fatigue & SOC Operations): Q35-Q39 removed → moved to separate SOC operations KSI (out-of-scope for change logging)
- Section 10 (Cost Optimization & Storage Economics): Q40-Q44 removed → moved to governance/cost KSI (not about logging coverage/integrity)
- Q14 (Agent Inventory & Growth): removed → capacity planning, not logging behavior
- Q28-Q29 (Customer Incident Metrics & Validation): removed → moved to customer success/governance KSI
- Q32-Q33 (EU AI Act Gap Analysis & Timeline): removed → moved to regulatory remediation KSI (detailed compliance roadmaps, not logging capability)
- Q50 (Research Participation & Rule Updates): removed → threat monitoring focus belongs in threat detection KSI

**Sections & Questions Consolidated (Focused):**
- Section 3 (Immutable Audit Trails): Removed cryptographic algorithm details, performance benchmarks, PQC roadmap specifics; consolidated Q09-Q10 to single high-level tamper-evidence question
- Section 6 (AI-Specific Attack Visibility): Removed classical control testing and general attack surface coverage; kept only AI-specific attack visibility in logs (3 focused questions)
- Section 8 (Regulatory Compliance): Removed detailed gap analysis and remediation timelines; kept only audit evidence generation capability

**Changes Made:**
- Made all questions perspective-neutral (removed CSP/customer/auditor language distinctions)
- Renumbered questions to remove gaps after deletions

**Result:** Original 50 discovery questions → 33 core questions focused strictly on change logging and monitoring effectiveness for AI systems.

---

## Section 1: Multi-Layer Observability Architecture

**CMT-01-Q01:** Describe your logging architecture across the 4 observability layers:
- **Layer 1 (Infrastructure)**: Container runtime, API gateways, network flows, system calls - what percentage of events are logged?
- **Layer 2 (AI System)**: Model inputs/outputs, training pipeline, agent task decomposition, tool invocations - what is logged at what granularity?
- **Layer 3 (Data)**: Data access, transformations, training data lineage, vector database queries - what percentage captured?
- **Layer 4 (Governance)**: Model approvals, policy changes, human overrides, risk assessments - how is this instrumented?

For each layer, provide retention periods and example log samples.

**CMT-01-Q02:** Can you correlate logs across all 4 layers? If an AI model produces anomalous output, can you trace: (1) which training data was used (Layer 3), (2) which model version processed it (Layer 2), (3) which agent triggered the inference (Layer 2), (4) which user authorized the agent (Layer 4), (5) which infrastructure resources were accessed (Layer 1)? What tools support cross-layer correlation (trace IDs, distributed tracing)?

**CMT-01-Q03:** In your shared responsibility model for AI logging, what does the platform log automatically vs. what must applications log themselves? For managed AI services (LLM APIs, model training platforms), do you provide model I/O logs automatically, or must applications instrument separately?

**CMT-01-Q04:** What observability platforms do you provide or integrate with? (AI-native observability, distributed tracing, third-party SIEM/observability exports). Can organizations export logs to external platforms (Splunk, Elastic, Datadog) or are they locked into proprietary tooling?

---

## Section 2: AI-Specific Change Tracking

**CMT-01-Q05:** Do you log all AI-related modifications? For each change type, can you answer: who authorized it, when it occurred, what exactly was changed, why it was changed (business justification), and whether it is reversible (rollback capability)?
- Model version updates
- Prompt policy changes (for GenAI services)
- Agent privilege or authorization changes
- Training data modifications or dataset swaps
- RAG index or knowledge base updates
- AI configuration-as-code changes
- Tool/API integrations for agents

**CMT-01-Q06:** For AI-related modifications in the past 12 months, provide a sample of 5-10 changes showing: change description, who authorized it (approval chain), when it occurred, what was changed, business justification, and whether it was reversed. Demonstrate that full change provenance is tracked and auditable.

**CMT-01-Q07:** If an AI-related incident occurs (model degradation, agent misbehavior, data leakage), can you trace the change history that led to it? Provide an example incident from the past 12 months showing: incident timeline, relevant changes preceding it, which change(s) likely caused it, and confidence in root cause identification.

**CMT-01-Q08:** How quickly can you retrieve change history for forensic investigation? (minutes, hours, days?). Can you generate change reports by time period, by AI system, or by change type within 1 hour for auditing/compliance needs?

---

## Section 3: Immutable Audit Trails & Tamper-Evidence

**CMT-01-Q09:** How do you ensure log immutability and prevent tampering? Describe your implementation:
- Cryptographic sealing (HMAC, digital signatures, or equivalent)?
- Append-only storage (write-once-read-many, versioning disabled)?
- External audit feed (logs shipped to independent repository in real-time)?
- Can you retrieve and verify historical logs for forensic reconstruction?

**CMT-01-Q10:** Can organizations independently verify log integrity? Do you provide cryptographic verification tools? If tampering is detected, what is your alerting and incident response process? Do you notify affected parties?

**CMT-01-Q11:** Where are immutable audit logs stored? Geographically distributed replicas? Segregated from operational systems? Encrypted at rest? Can organizations choose log storage region (data residency requirements)?

**CMT-01-Q12:** What is your immutable log retention policy? Default retention (90 days, 1 year, 10 years)? Can organizations extend retention for regulatory compliance (EU AI Act requires 10 years for high-risk AI documentation)? How are logs securely deleted after retention?

---

## Section 4: AI Agent Monitoring and Behavioral Baselines

**CMT-01-Q13:** Do you monitor AI agent actions (task logs, tool invocation logs, reasoning chains)? Can you detect and log:
- Agent accessing data outside expected scope
- Agent invoking unexpected tools/APIs
- Agent task execution patterns changing over time
- Multi-agent coordination anomalies
- Prompt injection attempts against agents

**CMT-01-Q14:** Can you define "normal" agent behavior for AI agent types (task frequency, tool invocation patterns, data access scope, execution duration)? Do agents have stable behavior patterns or do they adapt/evolve frequently (making anomaly detection harder)?

**CMT-01-Q15:** In the past 12 months, have you detected any agent misbehavior (unexpected actions, unauthorized access, task deviation, prompt injection attempts)? For detected incidents, how were they identified (rule-based alerts, behavioral analysis)? For undetected incidents (discovered post-mortem), why were they missed?

**CMT-01-Q16:** Do you use dynamic behavioral baselines for agent monitoring? Can you adjust baselines over time as agents evolve, while preventing baseline poisoning (attackers gradually shifting "normal" to hide compromise)?

---

## Section 5: Training Data and Model Lineage Tracking

**CMT-01-Q17:** Do you track training data lineage for all AI models? Can you answer for any deployed model:
- What training data was used (source, version, date)
- What data transformations were applied
- Who had access to training data
- Whether training data was modified after model training

**CMT-01-Q18:** For AI models, do you log:
- Model version and deployment date
- Model provenance (trained in-house, fine-tuned, or third-party?)
- Model weights/parameters (immutably stored with hash for integrity verification?)
- Model configuration and hyperparameters
- Data used for model evaluation/validation

**CMT-01-Q19:** Can you detect data poisoning or training data tampering? Do you:
- Monitor training data statistics over time (distribution shifts indicating poisoning)?
- Log all modifications to training datasets before model retraining?
- Compare model behavior before/after retraining to detect anomalies?
- Have incident detection for backdoor attacks or trojan models?

**CMT-01-Q20:** If a model's predictions become degraded or biased, can you determine: (1) whether training data was altered, (2) when it was altered, (3) who authorized the alteration, (4) what the business justification was? Provide an example from past 12 months.

---

## Section 5B: Shadow AI and Unauthorized Tool Detection

**CMT-01-Q21:** What capabilities do you have for detecting shadow AI tool usage across your organization? Describe: (a) detection methods (network monitoring, endpoint DLP, API gateway inspection, DNS/HTTP filtering), (b) tools detected (ChatGPT, Claude, Copilot, open-source LLMs, custom AI tools), (c) detection coverage (percentage of employee endpoints monitored), (d) detection latency (time from usage to detection), (e) incident examples where shadow AI usage was detected, including data exposure impact and remediation. How frequently are shadow AI incidents detected weekly/monthly?

**CMT-01-Q22:** What DLP (Data Loss Prevention) controls specifically monitor for violations related to AI tool usage? Describe: (a) data categories monitored (PII, financial data, source code, trade secrets, customer data), (b) AI tool usage patterns that trigger DLP alerts (uploading sensitive documents to AI tools, copying outputs from AI tools, accessing AI tool APIs with sensitive credentials), (c) alert accuracy (true positive rate, false positive rate), (d) response procedures when DLP violations are detected, (e) incident evidence demonstrating DLP effectiveness in preventing AI-related data loss. What percentage of attempted uploads to AI tools are blocked by DLP controls?

**CMT-01-Q23:** What telemetry infrastructure does your organization maintain for monitoring AI tool behavior, including both approved and shadow AI tools? Describe: (a) telemetry collection points (endpoints, network, cloud providers, AI service APIs), (b) behavioral metrics captured (tool usage frequency, data volume transferred, user identity, timestamp, data category), (c) correlation capability (linking AI tool usage to specific users and data accessed), (d) infrastructure design (centralized or distributed collection, retention policies, encryption), (e) alerting and anomaly detection on AI tool behavior (unusual access patterns, high-volume data transfers, access outside business hours), (f) incident examples demonstrating detection and investigation of suspicious AI tool behavior.

---

## Section 6: AI-Specific Attack Visibility in Logs

**CMT-01-Q24:** Do you have logging capabilities for AI-specific attacks? For each category, can you log and reconstruct:
- Prompt injection attempts (LLM I/O inspection)
- RAG integrity violations (vector database anomalies, unauthorized retrieval patterns)
- Multi-agent behavioral anomalies (coordinated misbehavior)
- Data poisoning signals (training data anomalies or unexpected model degradation)
- Model theft indicators (unusual query patterns or inference access)

**CMT-01-Q25:** Have you tested your logging and detection capabilities against AI-specific attacks in sandbox environments? Can you:
- Detect prompt injection in logs (no traditional malware signature)?
- Identify data exfiltration via AI summarization in logs?
- Reconstruct multi-agent coordination attempts from logs?
- Detect RAG backdoors (poisoned vector embeddings)?

For each capability, document what is visible in logs and what gaps exist.

**CMT-01-Q26:** In the past 12 months, have you detected or suspected any AI-specific attacks (prompt injection, model poisoning, agent compromise)? For detected attacks, what controls or log analysis identified them? For missed attacks (found post-mortem), why did your logging and detection fail?

---

## Section 7: Shared Responsibility and Logging Clarity

**CMT-01-Q27:** Do you have documented shared responsibility for AI workload logging? Does documentation explicitly state:
- Platform logs infrastructure automatically
- Applications must log application-level AI behavior (model I/O, agent actions, data lineage)
- Compliance requirements (EU AI Act Article 12) may require additional instrumentation
- Who is responsible for audit evidence generation

Is this documented in contracts, onboarding materials, and compliance guides?

**CMT-01-Q28:** For managed AI services (LLM APIs, model training, agent frameworks), what logging do you provide automatically and what must applications add? Can you provide example architectures showing logging integration points?

---

## Section 8: Regulatory Compliance and Audit-Grade Evidence

**CMT-01-Q29:** Are you subject to EU AI Act (Article 12 requires logging for high-risk AI)? For high-risk AI systems, do you currently log and retain for 10 years:
- Input data provided to the AI system
- Output/decisions produced by the AI system
- Model version/documentation
- Human oversight decisions and overrides

**CMT-01-Q30:** Can you generate automated audit evidence for EU AI Act compliance? For any deployed high-risk AI:
- Reconstruct decision chain (input → model processing → output → human review)?
- Generate compliance reports within 24 hours for regulatory inquiries?
- Provide immutable audit trail with integrity verification?

**CMT-01-Q31:** For other regulatory frameworks (NIST AI RMF, ISO 42001, sector-specific AI regulations), are your change/modification logs aligned with requirements? Can you demonstrate compliance during audits?

---

## Section 9: Incident Response and Forensic Capability

**CMT-01-Q32:** For AI-related incidents in the past 12 months, provide 3 examples showing:
- Incident description
- How it was detected
- Time from detection to initial investigation
- Time from detection to root cause identification
- Whether root cause could be determined from logs alone
- Whether logs provided sufficient evidence for remediation

**CMT-01-Q33:** Can you perform log-based forensic reconstruction? For any incident, can you replay events to understand:
- Attack timeline and progression
- What data was accessed/modified
- Which systems were impacted
- What user/agent actions preceded the incident

**CMT-01-Q34:** For compliance and legal requirements, can your logs serve as admissible evidence in regulatory proceedings or litigation? Are logs:
- Cryptographically sealed (chain of custody maintained)?
- Stored separately from operational systems (prevents tampering)?
- Auditable by external parties (regulators, authorized reviewers)?

**CMT-01-Q35:** What is your incident response SLA for log retrieval? (minutes for hot logs, hours for warm logs, days for archived logs?). Can you retrieve 6-month-old logs for investigation within 24 hours?

---

## Section 10: Emerging AI Threat Monitoring

**CMT-01-Q36:** Do you monitor and incorporate AI-specific threat research into your logging and detection strategies? Examples of threats emerging 2024-2025:
- Multi-agent coordination attacks (100x malicious automation potential)
- Steganographic collusion in LLMs (covert communication channels)
- Zero-click prompt injection (auto-execution in agent messages)
- Data poisoning via supply chain (backdoors in training data)
- Model extraction at scale (commercial model theft)

For each threat category, how would your logging detect or reconstruct it?

---

## Schema Reference

**Question ID Format:** CMT-01-Q##
Example: CMT-01-Q01

**All questions should be answered with:**
- Direct evidence (not claims)
- Quantifiable data where applicable
- Supporting documentation
- AI-specific examples where relevant
- Timeline/frequency information

---

**Version:** 3.0 (Task 2 Fine-tuning - Issue #13)
**Generated:** 2026-01-13
**Task 2 Refinement Date:** 2026-01-13 (Issue #13 scope focus)
