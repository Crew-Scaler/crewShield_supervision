# KSI-AFR-02: Key Security Indicators - Discovery Questions

**KSI Reference:** KSI-AFR-02_25-12A_KeySecurityIndicators
**Focus:** FedRAMP 20x Continuous Monitoring for AI-Driven Compliance
**Scope:** AI and AI Agents context ONLY
**Generated:** 2026-01-13
**Status:** APPROVED AND REFINED

---

## OVERVIEW

This question library addresses continuous compliance monitoring and AI-driven Key Security Indicators (KSI) validation for FedRAMP 20x Cloud Service Providers (CSPs). Questions are organized by thematic area and cover strategic, operational, and technical aspects of AI-driven compliance automation.

**Key Focus Areas:**
1. Evidence Quality, Grounding, and Adequacy
2. AI Agent Trust, Identity, and Cryptographic Assurance
3. Validator Reliability and Continuous Architecture
4. Shadow AI Discovery and Inventory
5. Governance, Legal Defensibility, and Resilience

---

## SECTION 1: EVIDENCE QUALITY, GROUNDING, AND ADEQUACY

This section consolidates evidence collection, hallucination prevention, and evidence adequacy into a unified focus on trustworthy compliance evidence.

### KSI-AFR-02-Q1
Do you currently use AI agents to generate or validate compliance evidence? If yes, what percentage of evidence undergoes grounding verification ensuring claims reference actual implemented controls?

### KSI-AFR-02-Q2
Have you experienced any incidents where AI-generated compliance artifacts (audit logs, configuration statements, control attestations) were discovered to be fabricated or referenced non-existent implementations?

### KSI-AFR-02-Q3
What grounding verification mechanisms ensure every AI-generated evidence claim references actual implemented controls? Can you demonstrate evidence where each assertion is cross-referenced to specific logs and configurations?

### KSI-AFR-02-Q4
For "80%+ automated validation" compliance goals, are you implementing multi-agent architectures separating evidence generators from validators, or using single AI systems for both generation and validation?

### KSI-AFR-02-Q5
What percentage of high-risk controls require human verification before attestation? How do you define "high-risk" in the context of AI-generated evidence?

### KSI-AFR-02-Q6
Do you have cryptographic signing infrastructure ensuring compliance evidence is immutable and traceable to specific implementations? If evidence is modified or lost, can you prove original integrity?

### KSI-AFR-02-Q7
Describe your evidence collection architecture. Do you employ AI agents to collect evidence from cloud infrastructure, security tools, and document repositories? What percentage of evidence is AI-generated versus manually sourced?

### KSI-AFR-02-Q8
What hallucination detection mechanism is applied to all AI-generated compliance evidence? Is it rule-based, machine-learning-based, multi-agent validation, or another approach? Provide measured accuracy including precision, recall, F1 scores, false-positive, and false-negative rates.

### KSI-AFR-02-Q9
What human verification checkpoints exist in your evidence collection pipeline? For critical controls, is human approval required before evidence is accepted?

### KSI-AFR-02-Q10
For each FedRAMP control, do you have documented evidence adequacy standards defining what evidence proves the control is effective, not just present?

### KSI-AFR-02-Q11
What is your measured evidence coverage percentage (evidence exists) versus adequacy percentage (evidence proves effectiveness)? What is the gap?

### KSI-AFR-02-Q12
Do you employ predictive gap identification where AI analyzes control requirements and proactively identifies evidence gaps before auditors find them? What is your measured finding prevention rate?

### KSI-AFR-02-Q13
For evidence inconsistencies (contradictory logs, conflicting configurations), what detection filters identify these anomalies?

### KSI-AFR-02-Q14
Are evidence adequacy standards machine-readable (JSON schemas, policy-as-code) or documented in prose?

### KSI-AFR-02-Q15
What is your historical audit finding rate (controls marked compliant but found non-compliant during audit)? Is this trend improving with automation?

### KSI-AFR-02-Q16
For complex controls (encryption key rotation, access enforcement, incident response), how do you distinguish evidence of process existence versus evidence of process effectiveness?

### KSI-AFR-02-Q17
Provide cross-referenced compliance evidence samples for three representative FedRAMP controls demonstrating each assertion's source backing and cryptographic integrity.

### KSI-AFR-02-Q18
Conduct correlation analysis between evidence adequacy standards and submitted evidence. For 10 representative controls, assess whether submitted evidence meets adequacy standards and identify gaps.

---

## SECTION 2: AI AGENT TRUST, IDENTITY, AND CRYPTOGRAPHIC ASSURANCE

This section consolidates individual agent identity management and multi-agent trust into a unified framework addressing both credential and cryptographic dimensions.

### KSI-AFR-02-Q19
How many autonomous AI agents currently operate in production with access to compliance evidence, security configurations, or audit data? Do you have a complete inventory with documented business purposes?

### KSI-AFR-02-Q20
What authentication mechanism does each agent use (static API tokens, temporary credentials, workload identity, certificate-based)? For static tokens, what is the maximum age of active credentials?

### KSI-AFR-02-Q21
What is your credential rotation velocity for compliance-critical agents? Is rotation automated with less than 90-minute lifetime, or manual with longer intervals?

### KSI-AFR-02-Q22
Have you conducted orphaned agent discovery in the past 12 months? How many agents with active credentials were created for temporary tasks but never deprovisioned?

### KSI-AFR-02-Q23
If a single agent's credentials were compromised, what is the blast radius? Could that agent falsify compliance evidence, modify audit logs, or trigger false compliance attestations?

### KSI-AFR-02-Q24
Do you employ multi-agent orchestration for compliance workflows (separate agents for evidence collection, validation, attestation, final review)?

### KSI-AFR-02-Q25
How do agents communicate validation results to peers? Is communication signed with cryptographic proof, or do agents implicitly trust peer outputs?

### KSI-AFR-02-Q26
If agent B is compromised, can it fabricate evidence that agent A collected and bypass agent C's validation? What cryptographic controls prevent this?

### KSI-AFR-02-Q27
For compliance-critical workflows, do you implement Byzantine agreement protocols ensuring majority consensus before attestation, or single-agent sign-off?

### KSI-AFR-02-Q28
What is your incident response capability if a compliance-critical agent is compromised? How quickly can you detect fabricated evidence in the trust chain?

### KSI-AFR-02-Q29
Provide complete inventory of all AI agents with compliance data access, including identity mechanisms (API tokens, certificates, workload identities), credential ages, last rotation dates, and permissions scopes. Verify tokens are less than 90 days old or certificates are actively rotated.

### KSI-AFR-02-Q30
For each inter-agent communication in multi-agent workflows, verify cryptographic signing. Request samples of agent-to-agent messages verifying each is digitally signed and includes proof of source agent identity.

### KSI-AFR-02-Q31
Describe consensus mechanisms for critical compliance decisions. Verify at least 2 independent agents must validate before critical attestations.

### KSI-AFR-02-Q32
Review agent isolation architecture. Verify agents operate in separate security domains (separate processes, containers, VMs) with no implicit trust.

### KSI-AFR-02-Q33
Verify HSM or cryptographic backing for all certificate-based agents. Confirm keys cannot be exported or accessed outside HSM.

---

## SECTION 3: VALIDATOR RELIABILITY AND CONTINUOUS ARCHITECTURE

This section consolidates validator model drift, dual-layer monitoring, and continuous validation into a unified framework for ensuring validator trustworthiness.

### KSI-AFR-02-Q34
What AI models currently perform compliance validation? For each, do you have baseline accuracy metrics established at deployment?

### KSI-AFR-02-Q35
How frequently and through what mechanism do you monitor validator accuracy in production (A/B testing, human spot-check verification, cross-model consensus)?

### KSI-AFR-02-Q36
Have you detected any gradual degradation in validator accuracy over time? If yes, what was the drift magnitude and how many non-compliant controls were missed before detection?

### KSI-AFR-02-Q37
Do you have automated retraining triggers for validators? At what accuracy degradation threshold does retraining execute automatically?

### KSI-AFR-02-Q38
For detecting silent validator failures, do you employ dual-layer monitoring (meta-models tracking validator performance)? Describe the architecture.

### KSI-AFR-02-Q39
If validator accuracy drops below acceptable thresholds, what is the SLA for model update and re-validation of all previous assessments?

### KSI-AFR-02-Q40
How does your organization implement the "80%+ automated validation" requirement for FedRAMP 20x? What percentage of KSIs currently have automated validation mechanisms?

### KSI-AFR-02-Q41
Describe your continuous monitoring architecture for AI-driven compliance. How are validation results aggregated, reported, and made available to assessors?

### KSI-AFR-02-Q42
For persistent compliance monitoring, how do you ensure validation mechanisms are themselves continuously validated for correctness and reliability?

### KSI-AFR-02-Q43
What incident response process occurs when automated validation detects a control failure? What is the SLA for investigation and remediation?

### KSI-AFR-02-Q44
What percentage of validation alerts are determined to be false positives? How do you handle false positives?

### KSI-AFR-02-Q45
How are KSI-AFR-02 validation goals mapped to specific NIST SP 800-53 controls (CA-2, CA-7, AU-2, AU-6, SI-4)? Can you demonstrate coverage?

### KSI-AFR-02-Q46
Provide baseline accuracy metrics for all production validators including accuracy percentage, precision, recall, F1 score, and evaluation dates.

### KSI-AFR-02-Q47
Provide production accuracy monitoring data for past 12 months showing trend. For any degradation exceeding 5%, verify retraining was triggered and executed.

### KSI-AFR-02-Q48
Request sample of validator model updates over past 12 months. For each, verify retraining rationale, new accuracy metrics, testing results before deployment, and re-validation of affected controls.

---

## SECTION 4: SHADOW AI DISCOVERY AND INVENTORY

### KSI-AFR-02-Q49
Have you conducted shadow AI discovery in the past 90 days? What percentage of AI usage was discovered outside approved corporate tools and cloud services?

### KSI-AFR-02-Q50
For compliance-specific workloads, do you have a documented inventory of all AI tools, models, and agents including training data provenance, vendor security practices, and refresh dates?

### KSI-AFR-02-Q51
Do you have baseline discovery frequency for new AI implementations? Should discovery be real-time continuous monitoring or periodic (daily, weekly)?

### KSI-AFR-02-Q52
Have you generated an AI Bill of Materials cataloging models, dependencies, and supply chain information for all compliance-critical systems? How frequently is this updated?

### KSI-AFR-02-Q53
Request complete inventory of all AI tools approved for compliance use. Verify each has documented purpose, vendor security assessment, deployment date, last review date, and approval sign-off.

### KSI-AFR-02-Q54
Request AI Bill of Materials for all compliance-critical systems. Verify completeness including models, versions, dependencies, training data sources, and vendor information.

### KSI-AFR-02-Q55
Identify any AI usage discovered in past 90 days not in approved inventory. Verify it was either approved through change control or decommissioned.

---

## SECTION 5: GOVERNANCE, LEGAL DEFENSIBILITY, AND RESILIENCE

### KSI-AFR-02-Q56
What governance framework ensures AI agents cannot autonomously escalate privileges or modify their own validation criteria without human approval?

### KSI-AFR-02-Q57
How do you ensure compliance evidence generated by AI agents is legally defensible and admissible in regulatory proceedings?

### KSI-AFR-02-Q58
What measures prevent AI agents from being used to create "compliance theater" where metrics pass but actual security controls are ineffective?

### KSI-AFR-02-Q59
How do you validate the training data provenance and integrity of AI models used for compliance validation?

### KSI-AFR-02-Q60
What adversarial testing do you conduct against your AI-driven compliance systems (prompt injection, model poisoning, adversarial examples)?

### KSI-AFR-02-Q61
How do you ensure AI compliance agents comply with data minimization principles and do not over-collect or retain sensitive data?

### KSI-AFR-02-Q62
What business continuity and disaster recovery plans exist for your AI-driven compliance validation systems?

### KSI-AFR-02-Q63
How do you ensure AI compliance validation systems remain effective as FedRAMP requirements evolve and new controls are introduced?

### KSI-AFR-02-Q64
How do you measure alignment between automated validation status and human-verified status? What is the current alignment percentage?

### KSI-AFR-02-Q65
For critical controls (encryption, access control, audit logging), is human approval required before automated evidence is accepted?

### KSI-AFR-02-Q66
When automated and human verification diverge, what investigation process occurs? How quickly are discrepancies resolved?

### KSI-AFR-02-Q67
What is your shared responsibility model for AI-driven compliance validation between your CSP and customers? How is this communicated?

---

## QUESTIONS MOVED TO OTHER KSIs

The following topics were considered relevant to AI/FedRAMP but better placed in other KSIs per issue #48 guidance. These should be migrated to their respective KSI question libraries:

### Moved to IAM/Logging/Monitoring KSIs:
- **Orphaned agent discovery via network scan** (AFR-02-Q37 in original) → Better suited to KSI-IAM-07 (Automated Account Management) or KSI-MLA-02 (Audit Logging)
- **Penetration testing of agent credentials** (AFR-02-Q38 in original) → Better suited to KSI-CMT-03 (Automated Testing and Validation)
- **Detailed network traffic analysis for shadow AI** (AFR-02-Q70 in original) → Better suited to KSI-CNA-05 (Unwanted Activity) or KSI-MLA-01 (SIEM)
- **Full adversarial test of compromised agent** (AFR-02-Q84 in original) → Better suited to KSI-INR-01 (Incident Response Procedures) or KSI-CMT-03

### Moved to Governance/Training KSIs:
- **Alert volume mathematics for 90 days** (AFR-02-Q103 in original) → Better suited to KSI-MLA-02 (Audit Logging) or KSI-CED-02 (Role-Specific Training)

### Moved to Recovery/Resilience KSIs:
- **AI-driven recovery orchestration procedures** (AFR-02-Q145-Q148 in original) → Better suited to KSI-RPL-02 (Recovery Plan) or KSI-INR-01 (Incident Response Procedures)

### Consolidated into Section 1 (Evidence Adequacy):
- **Mapping frameworks to implementations** (AFR-02-Q143 in original) → Consolidated into KSI-AFR-02-Q10 through Q18 covering evidence adequacy
- **Validation evidence accuracy audits** (AFR-02-Q144 in original) → Consolidated into KSI-AFR-02-Q15 covering audit finding rates

---

## DOCUMENT METADATA
