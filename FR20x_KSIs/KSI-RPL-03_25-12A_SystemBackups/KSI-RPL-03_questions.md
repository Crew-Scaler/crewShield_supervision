# AI-Driven System Backups: Discovery Questions

**KSI-RPL-03** - System Backups with AI-Driven Optimization, Safety, and Compliance

**Research Foundation:** 145 papers synthesized across 8 research clusters addressing AI-driven backup scheduling, ransomware resilience, multi-tenant isolation, model drift detection, and regulatory compliance.

**Question Set Version:** 3.0 (Refined + Deletion Compliance)
**Generated:** 2026-01-13
**Refinement Basis:** Issue #67 guidance - added backup deletion and data removal compliance questions from KSI-SVC-10 addressing deletion policies, timeline commitments, cryptographic deletion validation, and incremental backup chain deletion procedures

---

## SECTION 1: AI-DRIVEN BACKUP SCHEDULING OPTIMIZATION (KSI-RPL-03-Q01 to Q05)

**KSI-RPL-03-Q01:** Does the backup system use AI-driven dynamic scheduling (reinforcement learning, supervised ML) to optimize backup frequency, or maintain static fixed-interval backup schedules (daily, weekly)? If dynamic, how often are scheduling models retrained and validated?

**KSI-RPL-03-Q02:** For AI-driven backup scheduling models, what is the detection mechanism and threshold for model accuracy degradation or concept drift that would trigger fallback to conservative (more frequent) backup scheduling to prevent silent RPO violations?

**KSI-RPL-03-Q03:** How is training data for backup optimization models sourced and validated? What percentage comes from customer environments (high poisoning risk) versus synthetic data or vendor-controlled sources, and how is ground truth maintained separately from training data?

**KSI-RPL-03-Q04:** For critical data (customer data, financial records, AI training datasets), does the backup platform allow manual RPO overrides to force minimum backup frequency regardless of ML optimization recommendations by AI models?

**KSI-RPL-03-Q05:** Can the organization quantify the backup overhead reduction achieved through AI-driven scheduling (research baseline: 30-50%)? What metrics validate that RPO targets are consistently met despite ML optimization, and how frequently is compliance with RPO measured?

---

## SECTION 2: DATA POISONING DEFENSE & BACKUP MODEL INTEGRITY (KSI-RPL-03-Q06 to Q14)

**KSI-RPL-03-Q06:** Does the backup platform use ML models for scheduling or recovery optimization? If so, what is the defense mechanism against the critical vulnerability where only 250 malicious documents poison ANY LLM regardless of model size?

**KSI-RPL-03-Q07:** Are there triggers or special patterns that would cause backup scheduling models to recommend unsafe configurations (zero backup frequency, skip encryption, skip validation)? Has the organization conducted adversarial robustness testing of these models?

**KSI-RPL-03-Q08:** For model retraining, is there a mandatory manual validation step where humans confirm training data quality before deploying updated backup optimization models? What is the review process for detecting suspicious training patterns?

**KSI-RPL-03-Q09:** What is the detection mechanism and response procedure if a deployed backup model starts making systematically wrong decisions (recommending backup frequency too low, causing RPO violations, or skipping validation steps)?

**KSI-RPL-03-Q10:** Are backup optimization models validated against ground truth datasets separate from training data? How frequently is this validation performed, and what is the rollback procedure if validation fails?

**KSI-RPL-03-Q11:** What is the backup infrastructure's exposure to ransomware? Specifically, are backups stored on same network as production (high risk) versus isolated networks, air-gapped, or geographically separated with immutable WORM storage?

**KSI-RPL-03-Q12:** Can attackers with admin credentials modify backup retention policies to gradually delete historical backups? What controls prevent unauthorized policy modification, and are policy changes logged and auditable?

**KSI-RPL-03-Q13:** Does the backup storage support immutable backups (WORM - Write Once Read Many storage)? If offered, what is the overhead cost and can attackers delete immutable backups through GDPR right-to-erasure requests or other authorization mechanisms?

**KSI-RPL-03-Q14:** What is the detection capability for ransomware targeting backups? Can the system detect unauthorized backup deletion attempts, policy modification, encryption of backups, or synchronized deletion of snapshots with detection latency under 30 seconds?

---

## SECTION 3: BACKUP MODEL DRIFT & CONCEPT DRIFT DETECTION (KSI-RPL-03-Q15 to Q19)

**KSI-RPL-03-Q15:** How does the backup system detect model drift in scheduling or optimization models? Research shows drift detection is achievable in under 100ms—what is the platform's detection latency?

**KSI-RPL-03-Q16:** When infrastructure changes occur (VM to container migration, on-premises to cloud, scaling changes), how quickly does the system detect concept drift in backup models and trigger retraining or fallback to conservative schedules?

**KSI-RPL-03-Q17:** For training data backup, what integrity verification mechanisms prevent model poisoning via restore? Options include checksums, Merkle trees, signed manifests, or cryptographic proofs—what is implemented?

**KSI-RPL-03-Q18:** If a training data backup integrity check fails, what is the automatic response? Does the system alert for manual investigation, automatically restore from prior backup, quarantine to prevent restore, or other?

**KSI-RPL-03-Q19:** For incremental backups of training data, what happens if an earlier backup in the chain becomes corrupted? Are all subsequent backups considered corrupted, or can earlier uncorrupted versions be recovered?

---

## SECTION 4: RTO/RPO FEASIBILITY & COST-PERFORMANCE TRADE-OFFS (KSI-RPL-03-Q20 to Q24)

**KSI-RPL-03-Q20:** What RTO and RPO targets has the organization defined for different AI workload categories: (a) real-time inference APIs, (b) batch training pipelines, (c) autonomous agent systems, (d) model artifact repositories?

**KSI-RPL-03-Q21:** For each AI workload category, what is the cost-per-minute of downtime, and is the vendor's infrastructure architecture economically feasible for achieving stated RTO/RPO targets at the chosen SLA tier?

**KSI-RPL-03-Q22:** Does the vendor provide a clear matrix showing which RTO/RPO combinations are achievable at each service tier with associated costs? Have RTO/RPO targets been validated through actual recovery testing?

**KSI-RPL-03-Q23:** What backup strategy options support AI model artifacts: full backups, differential, incremental, copy-on-write snapshots, or semantic deduplication? What are the trade-offs in backup speed, recovery speed, and storage cost for each?

**KSI-RPL-03-Q24:** For large ML models (multi-GB to multi-TB), what acceleration techniques (vector acceleration, GPU-accelerated backup, semantic compression) reduce backup overhead, and can these be quantified (e.g., 26.2x vectorization speedup)?

---

## SECTION 5: MULTI-TENANT BACKUP ISOLATION & FAIRNESS (KSI-RPL-03-Q25 to Q29)

**KSI-RPL-03-Q25:** For multi-tenant backup infrastructure, what tenant isolation mechanisms prevent cross-tenant data leakage if filtering or isolation controls fail?

**KSI-RPL-03-Q26:** If backup resources are limited during widespread recovery (regional outage affecting all customers), what fairness algorithm allocates recovery priority across customers, and how is this validated to prevent systematic deprioritization?

**KSI-RPL-03-Q27:** Can the organization prove that cost optimization (26-43% ML improvement documented in research) doesn't systematically favor higher-value customers at expense of lower-tier customers in terms of backup frequency or recovery priority?

**KSI-RPL-03-Q28:** For inference attacks through timing or resource patterns in multi-tenant backup infrastructure, what monitoring detects suspicious access patterns that indicate customers attempting to infer other customers' data?

**KSI-RPL-03-Q29:** If one customer's backup system is compromised during a regional disaster, what containment strategy isolates that customer's backups from other customers without affecting remaining customers' recoveries?

---

## SECTION 6: BACKUP STRATEGY OPTIMIZATION & CONTINUOUS IMPROVEMENT (KSI-RPL-03-Q30 to Q32)

**KSI-RPL-03-Q30:** For training data restoration, is there a validation step comparing restored data against known-good reference datasets to detect label-flipping, feature manipulation, or poisoning that occurred months earlier?

**KSI-RPL-03-Q31:** Are historical backups retained long enough to enable detection of label-flip or poisoning attacks that occurred incrementally over time? What is the retention policy for training data backups?

**KSI-RPL-03-Q32:** Does the platform support "intent-driven" backup strategy selection where organizations declaratively specify (RTO, RPO, cost budget) and the system automatically selects optimal backup strategy? How are conflicts resolved (e.g., RTO of 15 minutes but budget only supports 4-hour RTO)?

---

## SECTION 7: BACKUP DELETION & DATA REMOVAL COMPLIANCE (KSI-RPL-03-Q33 to Q37)

**KSI-RPL-03-Q33:** What is the organization's backup deletion policy when customer data must be removed from service? Specifically, does deletion obligation apply to (a) primary backups only, (b) primary plus active backups, (c) primary plus all backups including cold storage, or (d) primary plus all backups plus archives?

**KSI-RPL-03-Q34:** What is the maximum timeline committed to for deletion from (a) active backups, (b) archive/cold storage, and (c) any backup media created before the deletion request? Are different backup types (snapshots, incremental, full) subject to different deletion timelines?

**KSI-RPL-03-Q35:** For CSPs claiming "cryptographic deletion" of backups (encryption with disposable keys followed by key destruction), what verification confirms that (a) encryption keys were actually destroyed, (b) key destruction is irreversible, (c) no key recovery mechanism exists, and (d) regulatory stakeholders have accepted cryptographic deletion as compliant with deletion obligations?

**KSI-RPL-03-Q36:** What testing has the organization conducted to verify that backup restoration operations do not reintroduce previously deleted customer data? How is this tested as part of regular disaster recovery exercises, and what evidence demonstrates that restoration testing includes deletion verification?

**KSI-RPL-03-Q37:** For multi-generational incremental backup chains, what procedures ensure deletion of data from all incremental backups in a chain when a customer requests data removal? If one backup in the incremental chain is corrupted, how does this affect deletion completeness for the entire chain?

---

## RESEARCH CLUSTERS SUPPORTING THESE QUESTIONS

**Cluster 1:** AI-Driven Backup Scheduling Optimization - 30-116x speedup, 89.2% training reduction, 3.47x TCO savings, model drift risks, concept drift from infrastructure changes

**Cluster 2:** Ransomware & Backup Security Threats - >99% detection accuracy, <1% false positives, synchronized deletion attacks

**Cluster 3:** Multi-Tenant Backup Infrastructure - 26-43% cost optimization, tenant isolation, inference attacks through timing patterns, cascading failures from shared capacity exhaustion

**Cluster 4:** AI Safety, Model Drift, Data Poisoning & Governance - <100ms drift detection, 250-document poisoning threshold, machine unlearning enables backdoor activation

**Cluster 5:** Regulatory Compliance Frameworks - FedRAMP 20x, NIST AI RMF, EU AI Act, GDPR conflicts with retention, automated compliance checking (See related KSIs for detailed compliance questions)

**Cluster 6:** Disaster Recovery & RTO/RPO Architectures - 175.5ms MTTR achievable, DRL-based recovery optimization, impossible RTO/RPO combinations, exponential cost for incremental improvement

**Cluster 7:** Backup Strategy Optimization - 8.35-26.2x vector acceleration, 107.2x GPU deduplication, 54-97% compression, strategy trade-offs (full vs. differential vs. incremental)

**Cluster 8:** Compliance Integration & Immutability Constraints - WORM storage, GDPR 30-day deletion vs. 5+ week retention conflicts, quantum-resistant cryptography

---

## MOVED QUESTIONS INTEGRATED INTO OTHER KSIs

**Ransomware 3.0 & Multi-Agent Security** (Q15 - moved to KSI-TPR-05: Third-Party Services)
- Original Q15: "For autonomous ransomware using LLM-based coordination (Ransomware 3.0), what defenses exist against the 100% inter-agent trust vulnerability where compromised agents manipulate other agents? How is agent identity cryptographically verified?"
- Rationale: Relates to supply chain security, multi-agent attacks, and third-party threat models rather than backup operations per se
- See KSI-TPR-05 for expanded questions on Ransomware 3.0 and inter-agent trust vulnerabilities

**GDPR Backup Retention & Right-to-Erasure** (Q31 - moved to Privacy/Compliance KSIs)
- Original Q31: "For GDPR compliance (30-day right-to-erasure), how does the organization handle backup retention?"
- Rationale: Regulatory mapping and privacy governance, not backup operation specifics
- See related Privacy KSI for detailed GDPR erasure questions

**HIPAA vs. GDPR Retention Conflicts** (Q32 - moved to Health/Sectoral Compliance KSI)
- Original Q32: "For HIPAA compliance (6-year retention required), how does the organization balance retention requirements with GDPR right-to-be-forgotten conflicts?"
- Rationale: Sectoral compliance mapping, not core backup design
- See related Health/Compliance KSI for multi-regulatory framework questions

**EU AI Act Explainability & Governance** (Q33 - moved to KSI-AIM-04: Governance Metrics and Investment)
- Original Q33: "Does the EU AI Act (effective August 2026) require explainability of backup scheduling decisions?"
- Rationale: AI governance and regulatory alignment, better suited to governance-focused KSI
- See KSI-AIM-04 for EU AI Act and regulatory governance questions

**FedRAMP Compliance Automation** (Q34 - moved to KSI-AFR-08: FedRAMP Security Inbox)
- Original Q34: "For FedRAMP compliance, does the backup platform support automated compliance checking for backup requirements?"
- Rationale: FedRAMP-specific compliance automation and reporting, best suited to dedicated FedRAMP KSI
- See KSI-AFR-08 for FedRAMP automation and compliance reporting

**Data Sovereignty & Residency Requirements** (Q35 - moved to KSI-TPR-05: Third-Party Services)
- Original Q35: "For cross-border data (EU data requiring EU backup storage), what data sovereignty requirements must backups comply with?"
- Rationale: Data residency governance relates to third-party services and supply chain compliance
- See KSI-TPR-05 for data residency and sovereignty questions

**Organizational Backup Roadmap & Evolution** (Q39 - moved to KSI-RPL-01: Recovery Plan)
- Original Q39: "What is the organizational roadmap for evolving AI backup capabilities?"
- Rationale: High-level strategic vision and roadmap, fits broader recovery planning strategy
- See KSI-RPL-01 for backup/DR strategic roadmap and evolution

**Long-Term Vision & Ransomware 3.0 Defense** (Q40 - moved to KSI-RPL-01: Recovery Plan)
- Original Q40: "What is the organization's vision for backup system evolution through 2025-2027?"
- Rationale: Organizational strategy and long-term planning, fits broader recovery strategy
- See KSI-RPL-01 for strategic backup/DR roadmap and organizational vision

---

**Document Purpose:** Enable organizations to comprehensively evaluate AI-driven backup capabilities with exclusive focus on backup scheduling optimization, ransomware resilience, multi-tenant isolation, model governance, and operational recovery feasibility.
