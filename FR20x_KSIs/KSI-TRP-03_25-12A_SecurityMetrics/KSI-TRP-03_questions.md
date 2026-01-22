# KSI-TRP-03: Security Metrics and KPIs - Question Library
**AI and Agent-Driven Measurement in Cloud Supply Chains**

---

## Processing Summary

**Original Question Count:** 31
### KSI-TRP-03-Q1: AI-Specific Metric Baselines and Performance Drift Measurement
**Question:** What baseline metrics should organizations establish for AI systems that differ from traditional vulnerability and compliance metrics, and what measurement approaches distinguish benign operational drift from potential security signals?

**Context:** Traditional KPIs (vulnerability counts, incident response times, compliance assessments) are insufficient for AI systems. Organizations need AI-specific baselines including model deployment frequency, training data integrity validation signals, dependency recommendation scrutiny rates, policy enforcement frequencies, and behavioral anomaly detection alert volumes. Statistical techniques (Kolmogorov-Smirnov tests, Population Stability Index analysis) enable distinction between operational variation and security indicators.

**Critical Metrics to Address:**
- Which AI-specific metrics (model integrity, supply chain validation, behavioral anomaly, third-party service risk) align with organizational risk priorities?
- How do organizations establish baseline measurement periods (2-4 weeks minimum) before enabling automated enforcement?
- What statistical discrimination techniques distinguish operational drift from security signals?
- How are baseline measurement periods protected against poisoning during establishment?
- What metrics validate that baselines remain representative as operational conditions evolve?

---

### KSI-TRP-03-Q2: Continuous Metrics Infrastructure and Continuous Compliance Validation
**Question:** Should organizations transition from periodic compliance audits and episodic vulnerability assessments to continuous real-time security metrics monitoring, and what infrastructure, operational readiness, and governance is required?

**Context:** FedRAMP 20x guidance emphasizes "persistent review" and "continuous validation" rather than snapshot assessments. Continuous monitoring requires distributed observability across artifact, execution, integration, and lifecycle layers, infrastructure to collect and process high-volume metrics without alert fatigue, policy-as-code frameworks enabling automated enforcement with real-time validation, and governance processes preventing metric proliferation.

**Critical Metrics to Address:**
- What distributed monitoring infrastructure (OpenTelemetry, distributed tracing, policy evaluation engines, continuous compliance platforms) must organizations deploy?
- How do organizations establish appropriate sensitivity thresholds preventing alert fatigue while maintaining security visibility?
- What percentage of security policies should transition to automated enforcement vs. manual validation?
- What policy violation detection and remediation latency can organizations achieve?
- How do organizations measure and improve signal-to-noise ratios to prevent alert fatigue and metric visibility degradation?
- What metric governance processes (review boards, periodic audits, sunset procedures) prevent metric proliferation?

---

### KSI-TRP-03-Q3: ML Supply-Chain Metrics Consolidation (Model Artifacts, Registry Security, SCA, Hallucinated Dependencies)
**Question:** How do organizations quantify and measure security risks in AI/ML supply chains, including model artifact integrity validation, model registry governance, software composition analysis coverage, and hallucinated dependency detection?

**Context:** AI system supply chains are complex with non-linear, parallel tracks (model artifacts from registries, training data from datasets, code from repositories, third-party dependencies), creating multiple integration points requiring comprehensive metric coverage. Organizations must measure: model artifact integrity through cryptographic validation and baseline comparison, registry access control and deployment gate effectiveness, software composition analysis specialized for ML ecosystems (capable of Pickle vulnerability detection, transitive dependency scanning, hallucinated package identification), and AI-recommended dependency validation preventing supply chain insertion attacks.

**Critical Metrics to Address:**
- What cryptographic provenance validation infrastructure (model signing, custody chains, SCA tools for ML) must organizations implement and measure?
- What software composition analysis coverage percentage (% of transitive dependencies scanned) constitutes acceptable validation?
- How do organizations measure model registry security metrics: access violation frequencies, unauthorized modification attempts, deployment gate block rates?
- What hallucinated dependency detection accuracy metrics demonstrate effectiveness, and how are false positive rates managed without blocking productivity?
- How do organizations measure the end-to-end completeness of ML supply-chain metrics across model artifacts, training data, code, and dependencies?
- What metrics demonstrate that policy-based deployment gates effectively prevent risky models from reaching production?

---

### KSI-TRP-03-Q4: Third-Party Service Risk Measurement (Now moved to KSI-TPR-03)
**Note:** This question has been moved to KSI-TPR-03 (Supply Chain Risk Management) as its primary focus is third-party supply chain risk rather than metrics themselves. Organizations should reference KSI-TPR-03-Q28+ for comprehensive third-party risk assessment; TRP-03 focuses only on "metrics for third-party service monitoring."

---

### KSI-TRP-03-Q5: Autonomous Agent Metrics and Authorization Governance (Consolidated)
**Question:** What security metrics should organizations establish for autonomous agents operating with delegated permissions, and how do metrics demonstrate compliance with authorization policy enforcement?

**Context:** Agents operating with long-lived credentials and broad permissions create unprecedented measurement challenges. Traditional access control metrics fail to capture just-in-time provisioning efficiency, permission scope compliance verification, or cascading privilege escalation risks in chained tool invocations. Organizations must measure: permission scope compliance percentage (% of agent operations within pre-approved scopes), credential rotation frequency for long-lived agent identities, just-in-time access provisioning latency, abnormal tool-chaining detection frequencies, and policy violation frequencies. These agent authorization metrics now reside in KSI-IAM-04; TRP-03 focuses on metrics demonstrating that agent authorization governance is continuous and measurable.

**Critical Metrics to Address:**
- What metrics validate that agent permissions match stated task intent and no broader?
- How do organizations measure just-in-time access provisioning latency and effectiveness?
- What abnormal tool-chaining detection metrics indicate privilege escalation attempts?
- How do organizations measure agent credential rotation frequency and compliance to policy?
- What escalation thresholds trigger human review, and how are escalation frequencies tracked?

---

### KSI-TRP-03-Q6: Behavioral Anomaly Detection Metrics (Now moved to KSI-AIM-02)
**Note:** This question has been moved to KSI-AIM-02 (Model Drift & Runtime Monitoring) as behavioral anomaly detection mechanics and baseline establishment belong with model monitoring. Organizations should reference KSI-AIM-02 for comprehensive baseline methodology and drift detection techniques; TRP-03 focuses on "metrics validating that behavioral anomaly detection is deployed and monitored."

---

## Security Metrics Assessment Questions

### KSI-TRP-03-Q7: Model and Training Data Integrity Metrics
**Question:** What metrics does the cloud service provider track and expose demonstrating that AI models and training data have not been compromised, and what audit evidence validates integrity throughout the lifecycle?

**Context:** Customers deploying AI-driven supply chain risk management need assurance that models and training data delivered by the CSP haven't been poisoned or modified. Organizations should measure: cryptographic signature verification success rates for all AI model artifacts, model weight baseline comparison frequency to detect tampering, inference output statistical distributions (KS-test scores) monitored and compared to baselines, deployment artifact manifest validation completion rates, and custody chain validation completeness for training data sources. CSPs should expose these metrics and audit evidence through dashboards and formal compliance reporting.

**Evaluation Criteria:**
- Can the CSP demonstrate cryptographic signature verification metrics for all AI model artifacts deployed in production?
- What baseline comparison frequency validates model weights haven't drifted from known-good signatures?
- How frequently are inference output statistical distributions (KS-test scores) monitored and compared to baselines?
- What percentage of training data sources are cryptographically verified in the CSP's custody chains?
- Can the CSP provide audit evidence of signature verification success rates, manifest validation completion percentages, and training data custody chain validation metrics?

---

### KSI-TRP-03-Q8: CSP Supply-Chain Metrics Exposure and SCA Coverage
**Question:** What metrics does the CSP expose demonstrating software composition analysis coverage, hallucinated dependency detection effectiveness, and model registry governance for AI/ML supply chains?

**Context:** Organizations need visibility into CSP supply-chain metrics to assess the effectiveness of AI/ML security controls. Key metrics include: SCA scanning frequency (hours since last scan), percentage of transitive dependencies successfully resolved and scanned, hallucinated package detection accuracy, vulnerability remediation timelines, model registry access control violation frequencies, deployment gate block rates, and policy-based gate effectiveness (false positive/negative rates). CSPs should expose these metrics in dashboards and formal reporting.

**Evaluation Criteria:**
- What SCA scanning frequency is maintained for AI/ML systems, and what percentage of transitive dependencies are successfully resolved and scanned?
- How does the CSP measure and report hallucinated dependency detection accuracy and false positive rates?
- What vulnerability remediation timeline guarantees does the CSP provide from CVE publication to patch deployment?
- Can the CSP demonstrate model registry security metrics: access violation attempts, unauthorized modification detection, deployment gate block/allow rates?
- What policy-based deployment gate effectiveness metrics (% of risky models blocked, false rejection rates) does the CSP track and expose?

---

### KSI-TRP-03-Q9: CSP Behavioral Monitoring and Continuous Compliance Metrics
**Question:** Does the CSP provide real-time metrics demonstrating continuous behavioral monitoring of deployed AI models, and what evidence validates that behavioral anomalies are detected and investigated?

**Context:** Organizations need assurance that CSP-deployed models are continuously monitored for behavioral drift, poisoning, and anomalies. CSPs should track and expose: baseline behavioral profiles (inference latency, output confidence, resource consumption distributions), concept drift detection frequencies, anomaly detection alert volumes and false positive rates, investigation timelines for detected anomalies, and performance degradation metrics. CSPs should expose these metrics in real-time dashboards and formal compliance reporting.

**Evaluation Criteria:**
- What baseline behavioral profiles does the CSP establish for each production AI model, and what statistical methods (isolation forests, KS-tests, PSI analysis) are applied?
- How frequently are concept drift alerts triggered, and what are the false positive rates?
- What is the CSP's mean time to detect (MTTD) model behavioral anomalies (target: <24 hours)?
- How quickly are detected anomalies escalated for human investigation and remediation?
- Can the CSP provide metrics demonstrating that detected anomalies are investigated and resolved?

---

### KSI-TRP-03-Q10: CSP Continuous Compliance Reporting and Audit Trail Integrity
**Question:** Does the CSP provide real-time compliance metrics demonstrating continuous policy adherence, or does compliance evidence rely on periodic audits? What audit evidence validates that compliance metrics are accurate and audit trails are tamper-proof?

**Context:** FedRAMP increasingly requires continuous compliance demonstration with real-time metrics replacing annual audits. Organizations should evaluate CSP metrics covering: policy enforcement automation completeness (% of policies automatically enforced), policy violation detection and remediation latency, audit trail completeness and integrity verification mechanisms, continuous security assessment frequencies, and remediation action verification. CSPs should expose these metrics in real-time dashboards with cryptographic integrity protection.

**Evaluation Criteria:**
- What percentage of security policies does the CSP automatically enforce vs. manually validate?
- What policy violation detection and remediation latency can the CSP guarantee?
- Does the CSP provide real-time compliance metrics dashboards for continuous visibility?
- What audit trail completeness and integrity verification mechanisms (hashing, digital signatures, write-once storage) does the CSP implement?
- How frequently does the CSP perform continuous security assessments, and what metrics are reported?
- Can the CSP provide automated reporting to FedRAMP systems demonstrating persistent compliance validation?

---

### KSI-TRP-03-Q11: Model Artifact Integrity and Signature Verification
**Question:** What evidence demonstrates that all AI model artifacts deployed in production have been cryptographically signed and verified before deployment, with metrics tracked and validated?

**Context:** Model artifact integrity represents a foundational AI supply chain control. Evidence must demonstrate that signing infrastructure is in place, that verification occurs at deployment gates with 100% completion, that signature verification metrics are continuously tracked, and that verification failures prevent deployment. Metrics should include: signature verification success rates, unsigned artifact rejection frequencies, and verification completion percentage.

**Validation Procedures:**
- Inspect model signing infrastructure and confirm all systems performing signature generation and verification
- Request signature verification metrics for models deployed in the past 90 days (target: 100% verification rate)
- Examine deployment gate logs confirming that all models are verified before production deployment
- Validate that signature verification failures trigger alerts and block deployment
- Assess whether verification processes apply to fine-tuned models, adapters, and other AI artifacts
- Confirm that signature verification metrics are continuously tracked and reported in security dashboards
- Identify any instances where signatures could have been bypassed or verification disabled

---

### KSI-TRP-03-Q12: Training Data Provenance, Custody Chain, and Integrity Metrics
**Question:** What documented evidence shows complete training data lineage with measured custody chain integrity, and how do metrics validate that training data integrity is maintained throughout the lifecycle?

**Context:** Training data contamination represents a critical supply chain attack vector. Evidence must demonstrate that organizations can trace all training data to original sources, document modifications throughout the lifecycle, and verify integrity through cryptographic means. Metrics should include: custody chain validation completeness (% of sources verified), lineage documentation completeness scores, and poisoning detection success rates in test environments.

**Validation Procedures:**
- Request training data provenance documentation for all models used in production
- Examine custody chain records documenting each hand-off point (collection, preprocessing, storage, integration)
- Assess metrics tracking custody chain validation completeness percentage and any sources that cannot be verified
- Review cryptographic verification logs (hashing, digital signatures) validating training data integrity
- Request metrics on poisoning detection success rates in test environments demonstrating detection capability
- Validate that training data lineage completeness scores are measured and reported
- Identify any training data sources with incomplete provenance or metrics indicating validation gaps

---

### KSI-TRP-03-Q13: Software Composition Analysis Coverage and Hallucinated Dependency Metrics
**Question:** What evidence demonstrates comprehensive software composition analysis coverage for AI/ML systems, with metrics validating hallucinated dependency detection effectiveness and vulnerability remediation timelines?

**Context:** Dependency vulnerability represents continuous supply chain risk requiring specialized SCA tools for ML ecosystems. Evidence must demonstrate SCA coverage, frequency, and effectiveness through metrics. Key metrics include: transitive dependency resolution completion percentage, hallucinated package detection accuracy, scanning frequency, and vulnerability remediation timelines.

**Validation Procedures:**
- Request SCA reports and metrics for AI/ML systems documenting transitive dependency coverage
- Examine SCA scanning frequency logs and confirm scanning occurs at defined intervals
- Verify that SCA tools are specialized for AI/ML ecosystems (capable of Pickle detection, model weight inspection)
- Request metrics on hallucinated package detection accuracy and false positive rates
- Assess vulnerability remediation timelines from CVE publication to patch deployment through metrics
- Examine dependency resolution completion logs and confirm percentage of transitive dependencies successfully resolved
- Identify any dependencies flagged as high-risk or unresolved that require compensating controls
- Validate that SCA metrics are continuously tracked and reported in security dashboards

---

### KSI-TRP-03-Q14: Autonomous Agent Authorization and Permission Scope Metrics
**Question:** What evidence demonstrates that autonomous agents operate within pre-approved permission scopes through continuous authorization metrics, and that policy violations are detected and escalated?

**Context:** Agent autonomy creates governance challenges requiring continuous authorization monitoring through measurable metrics. Evidence must demonstrate that policies define acceptable behaviors, that actual agent operations are monitored and measured, and that violations trigger investigation. Key metrics include: permission scope compliance percentage, policy violation detection latency, escalation frequencies, and authorization audit trail completeness.

**Validation Procedures:**
- Examine policy-as-code frameworks defining agent authorization policies
- Request authorization metrics demonstrating permission scope compliance percentage (% of operations within scope)
- Review policy violation detection logs and calculate violation frequencies and detection latencies
- Examine credential rotation logs and confirm rotation frequency meets policy requirements
- Request metrics on just-in-time access provisioning latency demonstrating timely permission adjustments
- Identify abnormal tool-chaining sequences and confirm detection metrics are tracked
- Review escalation procedures and confirm human review metrics for policy violations
- Validate that authorization metrics are continuously calculated and reported in dashboards
- Assess authorization audit trail completeness and integrity for forensic reconstruction

---

### KSI-TRP-03-Q15: Continuous Compliance Metrics and Audit Trail Integrity Validation
**Question:** What evidence demonstrates continuous compliance monitoring with real-time metrics replacing periodic assessments, and how are audit trails protected against tampering to ensure compliance evidence integrity?

**Context:** FedRAMP increasingly requires continuous compliance demonstration through persistent metrics. Evidence must demonstrate that organizations have transitioned from annual audits to continuous monitoring with metrics tracked and reported in real-time. Key metrics include: policy enforcement automation completeness, policy violation detection and remediation latency, audit trail integrity, continuous assessment frequencies, and remediation action verification rates.

**Validation Procedures:**
- Examine continuous compliance monitoring infrastructure confirming real-time visibility into policy adherence
- Request policy enforcement automation metrics and identify manually-validated policies
- Review policy violation detection and remediation latency metrics confirming they meet organizational objectives
- Examine audit trail logs and validate completeness of all policy enforcement and violation actions
- Assess audit trail integrity controls (hashing, digital signatures, write-once storage) preventing tampering
- Request continuous security assessment logs and confirm assessment frequency meets requirements
- Examine remediation action verification metrics confirming violations are confirmed resolved
- Assess continuous compliance metrics reporting to FedRAMP and validate metrics accuracy
- Identify any periods where continuous monitoring was disabled or data loss occurred
- Validate that metrics governance processes exist (review boards, metric audits, sunset procedures) preventing proliferation
- Confirm historical compliance evidence is retained for regulatory audits

---

## Implementation Guidance and Roadmap

### Phased Metrics Implementation Approach

Organizations should implement comprehensive AI security metrics through a phased roadmap:

**Phase 1 (Baseline - Weeks 1-4):** Establish baseline measurement periods (2-4 weeks minimum) for highest-priority metrics before enabling automated enforcement. Critical Phase 1 metrics include model artifact integrity, training data provenance, and agent permission scope compliance.

**Phase 2 (Foundation - Months 1-3):** Deploy distributed monitoring infrastructure (OpenTelemetry, policy evaluation engines, continuous compliance platforms) enabling real-time metrics collection and reporting across artifact, execution, integration, and lifecycle layers.

**Phase 3 (Automation - Months 3-6):** Implement policy-as-code frameworks enabling automated policy enforcement with continuous validation. Focus on establishing appropriate sensitivity thresholds, tuning detection algorithms, and preventing alert fatigue through tiered alerting strategies.

**Phase 4 (Integration - Months 6-12):** Integrate metrics across all eight AI supply chain dimensions into unified dashboards providing cross-cluster visibility. Establish metric governance processes (review boards, periodic audits, sunset procedures) preventing metric proliferation.

**Phase 5 (Optimization - Ongoing):** Continuously refine metrics through feedback loops, improve signal-to-noise ratios, and evolve baselines as operational conditions change. Measure and report on metrics effectiveness to drive continuous improvement.

---

### To KSI-TPR-03 (Supply Chain Risk Management):
- **Original TRP-03-Q005:** Third-party AI service risk assessment → Integrated as KSI-TPR-03-Q28 (Third-party service risk measurement)
- **Original TRP-03-Q011:** Model provenance evaluation (customer perspective) → Integrated into KSI-TPR-03 model integrity section
- **Original TRP-03-Q012:** Training data integrity (customer perspective) → Integrated into KSI-TPR-03 training data section
- **Original TRP-03-Q013:** SCA coverage and hallucinated packages → Integrated into KSI-TPR-03 supply chain metrics section
- **Original TRP-03-Q015:** Third-party compensating controls → Integrated into KSI-TPR-03 compensating controls questions

### To KSI-AIM-02 (Model Drift & Runtime Monitoring):
- **Original TRP-03-Q006:** Behavioral anomaly detection and drift monitoring → Integrated as new KSI-AIM-02 question addressing baseline establishment and statistical methods

### To KSI-IAM-04 (Just-in-Time Authorization):
- **Original TRP-03-Q004:** Autonomous agent authorization metrics → Integrated into KSI-IAM-04-Q5, Q15, Q19 (permission scope metrics, escalation detection, behavioral deviation)
- **Original TRP-03-Q014:** Agent permission scope and policy enforcement (customer perspective) → Integrated into KSI-IAM-04-Q2, Q4 (task-scoped permissions, escalation prevention)
- **Original TRP-03-Q028:** Agent credential rotation and JIT metrics → Integrated as KSI-IAM-04-Q28 (agent authorization incident response)

---

**Version:** 2.0 (Refined per Issue #70 Guidance)
**Last Updated:** January 13, 2026
