# Cloud-Native Best Practices for AI: Discovery Questions

**KSI Focus:** CNA-07 - Align cloud-native information resources with Cloud Service Provider (CSP) best practices in the AI era, emphasizing AI-driven governance automation, agent identity management, MLOps pipeline efficiency, behavioral monitoring, and policy-as-code compliance. Move from manual, role-based governance to AI-native, dynamic, AI-agent-aware governance systems.

**Context:** This discovery question set consolidates auditor, CIO, and customer perspectives to assess whether organizations align cloud resource deployment with CSP best practices through automated authorization, model governance, agent security, resource optimization, continuous monitoring, and governance automation. Questions focus on verification of claimed AI automation accuracy (85-94% authorization, 92.9% policy match), MLOps efficiency gains (61% configuration reduction), resource optimization (10-61.7% cost savings), and compliance automation effectiveness (100% recall, 86.5% precision). All questions address AI/agent-specific governance challenges, not generic infrastructure procedures.

---

## Section 1: AI-Driven Authorization & Policy Automation

**KSI-CNA-07-Q1:** What evidence demonstrates your AI-driven authorization system achieves claimed accuracy levels (85-94% automation, 92.9% policy match to human experts)? Describe: (a) authorization decision logs with accuracy measurement methodology, (b) human review escalation rates and quality metrics, (c) testing with production data (minimum 10,000 decisions), (d) false positive/negative analysis and root causes, (e) performance benchmarks from third-party validation.

**KSI-CNA-07-Q2:** How does your dynamic RBAC (RBAC++) implementation handle context-aware permission adjustment? Document: (a) context signals triggering permission changes (time, location, risk, workload type), (b) frequency of dynamic adjustments, (c) latency requirements (target: <100ms for 99.9% of requests), (d) audit logging of permission changes, (e) examples of dynamic scenarios tested (on-prem vs remote access, business hours restrictions, high-value resource MFA requirements).

**KSI-CNA-07-Q3:** What zero standing privilege (ZSP) policies do you enforce? Provide: (a) percentage of users with standing admin/privileged access, (b) maximum standing privilege duration (target: <8 hours), (c) just-in-time (JIT) access approval time metrics (target: <5 minutes for automated approvals), (d) JIT request volume and trends, (e) privileged session recording and audit trail completeness.

---

## Section 2: Model Governance & Lifecycle Management

**KSI-CNA-07-Q4:** How do you achieve full AI model lifecycle traceability? Describe: (a) model registry infrastructure (central catalog of all models), (b) metadata captured per model (training data hash, fairness metrics, compliance status, lineage), (c) version control and lineage tracking (which training data → which model version → which deployment), (d) model decommissioning procedures, (e) examples of impact analysis using lineage (if this dataset changes, which models affected?).

**KSI-CNA-07-Q5:** What automated drift detection system monitors model performance degradation? Document: (a) metrics monitored (accuracy, latency, throughput, data drift, concept drift, label drift), (b) detection frequency (real-time vs periodic), (c) alert thresholds and notification procedures, (d) mean time to detection (MTTD) for performance degradation, (e) automated remediation actions triggered by drift detection.

---

## Section 3: Agent Security & Behavioral Hardening

**KSI-CNA-07-Q6:** What agent identity and permission scoping controls do you implement beyond traditional RBAC? Describe: (a) agent identity provisioning and lifecycle (creation, rotation, decommissioning), (b) task-centric vs role-based permissions (are agents granted time-limited, task-specific access?), (c) maximum permission grant duration per agent (target: minutes to hours, not days/months), (d) automated credential rotation frequency, (e) examples of agents operating under least-privilege constraints.

**KSI-CNA-07-Q7:** How do you establish behavioral baselines for AI agents and detect anomalies? Document: (a) baseline establishment methodology (learning period, feature selection), (b) anomaly detection approach (statistical, ML-based, rule-based), (c) anomaly types monitored (unusual query patterns, resource usage spikes, lateral movement attempts, timing anomalies), (d) alert generation and escalation procedures, (e) false positive rate and tuning mechanisms.

**KSI-CNA-07-Q8:** What controls prevent prompt injection and adversarial attacks on agents in your environment? Explain: (a) input validation and sanitization procedures, (b) output filtering and verification, (c) model robustness testing methodology (adversarial examples, jailbreak attempts), (d) frequency of adversarial evaluation testing, (e) evidence from testing: percentage of injections detected/blocked, adversarial examples that bypassed defenses.

**KSI-CNA-07-Q9:** For multi-agent systems, how do you enforce security boundaries and prevent cascade failures? Describe: (a) agent-to-agent communication protocols (authentication, authorization, audit), (b) isolation mechanisms preventing lateral movement, (c) deadlock detection and prevention (agent A waiting for B, B waiting for A), (d) failure modes tested (agent timeout, resource starvation, Byzantine agent), (e) recovery procedures for failed agents.

---

## Section 4: AI Resource Optimization

**KSI-CNA-07-Q10:** What GPU scheduling and allocation policies do you use to optimize resource utilization? Document: (a) scheduling strategy (FIFO, fairness-based, ML-based, preemption-aware), (b) GPU utilization metrics (target: >70% for cost-efficiency), (c) cost-aware scheduling (differentiating between development and production workloads), (d) prediction-assisted scheduling (ML-based workload forecasting), (e) cost savings achieved through optimization (target: 10-61.7% based on research).

**KSI-CNA-07-Q11:** How do you implement cost-aware resource provisioning and enforce budget constraints? Provide: (a) cost model for AI workloads (per GPU, per token, per training job), (b) budget enforcement mechanisms (fail-fast if estimated cost exceeds threshold), (c) cost attribution by team/project, (d) anomaly detection for cost overruns, (e) cost reduction opportunities identified and remediation timeline.

**KSI-CNA-07-Q12:** What workload prediction and autoscaling strategies do you employ? Describe: (a) prediction model (time series, ML-based ensemble, rule-based heuristics), (b) prediction accuracy and latency, (c) autoscaling triggers and decision logic, (d) under/over-provisioning rate (target: <5% sustained overprovisioning), (e) evidence: actual vs predicted workload for past 90 days.

---

## Section 5: Behavioral Monitoring & Anomaly Detection

**KSI-CNA-07-Q13:** Beyond traditional APM metrics (CPU, memory, latency), what semantic health checks monitor AI system correctness? Describe: (a) domain-specific accuracy checks (is AI output correct?), (b) completeness checks (is AI providing full answers or partial/truncated?), (c) coherence checks (is output logically consistent?), (d) confidence level monitoring (when is AI uncertain?), (e) baseline definition for "healthy" AI state.

**KSI-CNA-07-Q14:** Can your observability system detect degraded AI output BEFORE traditional metrics alert? Explain: (a) pattern-based anomaly detection approach, (b) early warning signals (latency increase predicting quality drop), (c) lead time: how many minutes before traditional alert?, (d) false positive rate on valid but unusual behavior, (e) examples where semantic monitoring prevented customer impact.

**KSI-CNA-07-Q15:** What observability gaps exist in your monitoring of AI systems? Document: (a) metrics that cannot be automated (require manual review), (b) blind spots in distributed tracing (which system components not monitored?), (c) latency of observability pipeline (from event to dashboard), (d) data retention and cost, (e) compliance requirements (audit trail retention, telemetry access controls).

**KSI-CNA-07-Q16:** How do you detect concept drift and model degradation in production systems? Describe: (a) drift detection methodology (supervised vs unsupervised), (b) MTTD for model performance degradation, (c) automated remediation (retraining, rollback, alert escalation), (d) frequency of model monitoring and retraining, (e) historical incidents: models where drift was detected and impact assessment.

---

## Section 6: Policy Automation & Governance Frameworks

**KSI-CNA-07-Q17:** How do you implement policy-as-code for AI governance (authorization, compliance, resource limits)? Document: (a) policy language or framework used (OPA, AWS Config, custom DSL), (b) policies defined in code, (c) enforcement mechanisms (admission control, CI/CD gates, runtime enforcement), (d) policy violation detection and escalation, (e) version control and policy change history.

**KSI-CNA-07-Q18:** What automated compliance assessment system validates against multiple frameworks (NIST, ISO, PCI-DSS, FedRAMP)? Explain: (a) frameworks supported and percentage of controls automated, (b) compliance assessment methodology (continuous vs periodic), (c) violation detection latency (target: <15 minutes), (d) recall/precision metrics (target: 100% recall, 86.5% precision for critical controls), (e) false positive analysis and rate.

**KSI-CNA-07-Q19:** How do you implement policy enforcement for AI-specific controls (agent identity, model governance, behavioral baselines)? Describe: (a) controls enforced at resource creation time (new agent, new model deployment), (b) runtime enforcement (continuous compliance monitoring), (c) automated remediation for violations (tagging, quarantine, deletion), (d) audit trail and compliance evidence generation, (e) integration with NIST AI RMF and ISO 42001 compliance frameworks.

---

## Section 7: Incident Response & Resilience

**KSI-CNA-07-Q20:** What percentage of AI governance incident response is automated vs manual? Describe: (a) automated detection triggers (policy violations, drift detection, anomalies), (b) automated response actions (quarantine, scale-down, alert escalation), (c) human escalation criteria, (d) MTTR (mean time to recovery) for automated vs manual incidents, (e) plan to increase automation percentage.

**KSI-CNA-07-Q21:** For AI security incidents involving compromised agents or models, how do you execute incident response? Explain: (a) incident detection methodology (behavioral, intrusion detection, security tooling), (b) containment procedures (isolate agent, revoke credentials, kill active sessions), (c) recovery procedures (rollback model, replay audit logs), (d) post-incident analysis and lessons learned, (e) examples from past 12 months.

---

## Section 8: Third-Party & Ecosystem Governance

**KSI-CNA-07-Q22:** How do you govern third-party models, agents, and data in your ecosystem? Document: (a) third-party vetting process (security review, fairness audit, IP verification), (b) licensing and attribution tracking, (c) data lineage for models trained on customer or partner data, (d) remediation procedures if third-party model/agent compromised, (e) examples of incidents requiring third-party coordination.

**KSI-CNA-07-Q23:** How do you ensure consistency of best practices across multi-cloud deployments? Describe: (a) CSP-agnostic governance policies, (b) cloud-specific policy variants and management, (c) compliance validation across clouds (multi-cloud compliance dashboard), (d) incident response coordination across clouds, (e) cost optimization and vendor lock-in prevention strategies.

---

## Section 9: Continuous Improvement & Capability Evolution

**KSI-CNA-07-Q24:** What continuous improvement program maintains alignment with CSP best practices as they evolve? Document: (a) monitoring of CSP releases and new guidance, (b) quarterly/annual assessment of alignment (drift detection), (c) roadmap for implementing new capabilities, (d) stakeholder feedback mechanisms (customer advisory boards, threat intelligence), (e) investment in emerging technologies (quantum-resistant crypto, confidential computing, AI-native networking).

---

## Section 10: Security & Threat Intelligence Integration

**KSI-CNA-07-Q25:** How do you integrate threat intelligence into authorization and resource governance decisions? Describe: (a) threat intelligence sources (CSP advisories, CVE feeds, AI/ML-specific threats), (b) integration with policy automation (do threats automatically trigger policy changes?), (c) examples: CVE published → agent permissions restricted within 1 hour, (d) incident response playbooks for emerging AI threats, (e) red-team exercises validating threat response.

**KSI-CNA-07-Q26:** What AI-specific security threats do you actively monitor and defend against? List: (a) model poisoning during training, (b) prompt injection during inference, (c) model extraction attacks (stealing model via API queries), (d) data poisoning from external sources, (e) malicious AI agents (agents behaving adversarially), (f) evidence of threat detection and response from past 12 months.

---

## Section 11: Governance as Code & Infrastructure Automation

**KSI-CNA-07-Q27:** How do you encode AI governance policies in infrastructure-as-code (IaC) and policy-as-code (PaC)? Describe: (a) IaC tools used (Terraform, CloudFormation, custom), (b) governance policies enforced via code (agent identity, model registry, behavioral baseline), (c) admission control at resource creation (enforce policy before provisioning), (d) audit trail and rollback capability for policy changes, (e) examples: agent spawn policy that enforces credential rotation, model deployment policy that requires risk assessment.

**KSI-CNA-07-Q28:** What self-healing and autonomous remediation capabilities do you implement? Document: (a) automated responses to policy violations (tag, quarantine, delete), (b) self-healing infrastructure (agents that auto-remediate drift, models that auto-retrain on degradation), (c) human-in-the-loop for high-risk remediations, (d) audit trail and approval workflows, (e) measured success: % of violations auto-remediated without human intervention (target: >70%).

---

## Filter & Scope Summary

**CNA-07 Focus:** Cloud-native resource implementation and governance aligned with CSP best practices. Excludes program-level, organizational, business impact, and strategic roadmap questions.

**Questions Retained:** 28 core questions (KSI-CNA-07-Q1 through KSI-CNA-07-Q28)

**Questions Filtered Out (moved to other KSIs):**
- Q06 (Section 2): NIST AI RMF / ISO 42001 operationalization → Move to AI-GOV or governance-framework KSI
- Q21-Q22 (Section 7): Cross-framework mappings and AI RMF operationalization → Move to multi-framework compliance KSI
- Q28 (original Section 10): AI governance program effectiveness metrics → Move to governance-maturity or continuous compliance effectiveness KSI
- Q31-Q32 (Section 12): Cost analysis and business impact → Move to business impact / ROI of security KSI
- Q33-Q34 (Section 13): Organizational training and communication → Move to training / org development KSI
- Q37-Q39 (Section 15): Emerging tech roadmap and innovation balance → Move to future posture / innovation strategy KSI
- Q40 (Section 15): Competitive advantages → Strategic positioning question, out of scope

**Total Removed:** 12 questions (40 → 28 core)

---

**Version:** 2.0 (Filtered & Scoped to Core CNA-07)
**Generated:** 2026-01-13
**Last Updated:** 2026-01-13 (Issue #24 filtering pass)
