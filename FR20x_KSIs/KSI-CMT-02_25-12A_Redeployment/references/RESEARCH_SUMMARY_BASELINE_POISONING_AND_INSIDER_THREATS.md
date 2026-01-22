# Research Summary: Baseline Poisoning & AI-Assisted Insider Threats
## Issue #3: AI Agent Infrastructure Security, ML Artifact Governance, and AI-Driven Compliance

**Research Focus Areas:**
1. Behavioral Baseline Poisoning and Anomaly Detection for AI Workloads
2. AI-Powered Insider Attack Attribution
3. Baseline Establishment for AI Systems
4. Gradual Baseline Drift vs. Legitimate Evolution
5. Poisoning Detection and Prevention for AI Monitoring

**Total Papers Downloaded: 48**
- Baseline Poisoning: 11 papers
- Insider Attribution: 14 papers
- Baseline Establishment: 11 papers
- Drift Detection: 6 papers
- Poisoning Prevention: 6 papers

---

## Executive Summary

This research compilation addresses critical security challenges in AI-era infrastructure monitoring, specifically targeting **baseline poisoning attacks** and **AI-assisted insider threat attribution**. The research validates several key threat scenarios identified in the version-controlled deployment survey:

### Key Validated Threats:

1. **Baseline Poisoning is a Real and Growing Threat**
   - Attackers can manipulate monitoring baselines through gradual, stealthy poisoning attacks
   - "Session creep" - gradual introduction of malicious behavior into baseline - is documented in multiple papers
   - Advanced Persistent Threats (APTs) actively employ temporal evasion strategies

2. **AI-Assisted Attribution is Feasible and Effective**
   - Modern ML techniques achieve 94.3% detection accuracy for insider threats
   - Explainable AI (XAI) enables attack attribution through SHAP and LIME
   - Behavioral analytics can distinguish insider threats from legitimate users

3. **Detection Methods are Improving but Challenges Remain**
   - Deep learning dominates anomaly detection (76% of visual, 53% of behavioral methods)
   - Real-time detection systems can identify threats with <1.2% false positive rates
   - Concept drift vs. malicious drift remains a challenging distinction

4. **AI Agents Introduce New Attack Surfaces**
   - Autonomous agents can bypass traditional monitoring through baseline manipulation
   - Multi-agent systems require specialized audit trails and provenance tracking
   - Agent policy drift enables privilege escalation without detection

---

## 1. Baseline Poisoning Attacks (11 Papers)

### Overview
Baseline poisoning represents a sophisticated attack where adversaries gradually manipulate the behavioral baseline used by anomaly detection systems, enabling malicious activities to appear normal. Research from 2024-2025 shows this is not theoretical - it's actively exploited.

### Key Papers:

#### 2412.00797 - Stealthy Poisoning in Reinforcement Learning (Dec 2024)
**Key Findings:**
- Formalizes stealthy attacks as optimization problems minimizing deviation from original environments
- Introduces "online" attacks occurring simultaneously with agent-environment interaction
- Demonstrates gradual baseline manipulation over time

**Relevance to CSP Infrastructure:**
- AI-driven auto-scaling and capacity planning agents vulnerable to gradual policy poisoning
- Attack can manipulate resource allocation baselines to hide malicious workloads
- Detection requires continuous baseline integrity verification

#### 2503.22759 - Data Poisoning in Deep Learning Survey (Mar 2025)
**Key Findings:**
- Distinguishes static vs. dynamic poisoning attacks
- Dynamic attacks introduce adaptive strategies evolving over time
- Persistence and adaptability make detection increasingly challenging

**CSP Implications:**
- Model training pipelines must detect gradual data distribution manipulation
- Feature stores require immutable snapshots with integrity verification
- Retraining triggers must distinguish drift from poisoning

#### 2309.09498 - Combating Advanced Persistent Threats (Sep 2024)
**Key Findings:**
- APT attackers employ temporal evasion strategies
- Interspersing unrelated sequences within attack primitives evades detection
- Rapid stealthy evasion detection requires specialized mechanisms

**Infrastructure Impact:**
- Traditional SIEM baselines blind to gradual APT baseline manipulation
- CSP must implement multi-temporal baseline comparison
- Alert fatigue from false positives enables attackers to hide in noise

#### 2306.05494 - Adversarial Evasion Attacks Practicality in Networks (Jun 2024)
**Key Findings:**
- Systems adapting to behavioral changes vulnerable to "session creep"
- Attackers gradually introduce malicious behavior into baseline
- Dynamic learning amplifies vulnerability to baseline manipulation

**CSP Application:**
- AI-powered network monitoring baselines can be poisoned through slow drift
- GitOps drift detection must distinguish authorized changes from attacks
- Immutable infrastructure prevents baseline manipulation by enforcing versioned state

#### 2401.08984 - GAN-based Poisoning Framework (Jan 2024)
**Key Findings:**
- P-GAN framework generates adversarial perturbations degrading model performance
- Deep auto-encoders (DAE) filter outliers via reconstruction error
- Vertical federated learning vulnerable to targeted poisoning

**Model Registry Security:**
- Model promotion pipelines require adversarial robustness testing
- Baseline model performance metrics can be poisoned during evaluation
- Cryptographic signing alone insufficient - need behavioral validation

#### 2502.15561 - Defensive Framework for Adversarial NIDS (Feb 2025)
**Key Findings:**
- Defensive framework achieves 35% accuracy increase under adversarial conditions
- Genetic algorithms generate realistic adversarial traffic
- Ensemble learning + adversarial training reduces false positives by 12.5%

**CSP Defense Strategy:**
- Adversarial training must be standard for all AI-powered security monitoring
- Multiple baseline models provide redundancy against single-baseline poisoning
- Feature engineering reduces attack surface for baseline manipulation

### Baseline Poisoning Attack Taxonomy:

1. **Gradual Drift Poisoning**: Slow modification of baseline over weeks/months
2. **Trigger-Based Poisoning**: Baseline appears normal until specific condition triggers malicious behavior
3. **Federated Poisoning**: Multi-node attacks poisoning shared baseline across distributed systems
4. **Temporal Evasion**: Attacks timed to coincide with legitimate baseline evolution
5. **Adversarial Perturbation**: Micro-modifications invisible individually but cumulative over time

---

## 2. AI-Powered Insider Attack Attribution (14 Papers)

### Overview
AI-assisted attribution leverages machine learning to identify, track, and attribute insider threats based on behavioral patterns. 2024-2025 research demonstrates high-accuracy attribution with explainability.

### Key Papers:

#### 2505.15383 - Real-Time Insider Threat Detection (May 2025)
**Key Findings:**
- Deep evidential clustering enables real-time behavioral analytics
- Achieves 94.3% detection accuracy with <1.2% false positive rate
- Features categorized: Time, User, Project/Role, Activity, Logon, USB, File, Email

**CSP Implementation:**
- GitOps commit patterns enable behavioral baseline per developer
- Anomalous approval chains detected via behavioral deviation
- Agent actions attributable to specific users through audit trails

#### 2401.00286 - Autonomous Threat Hunting (Jan 2024)
**Key Findings:**
- Unsupervised learning identifies abnormal user behaviors indicating insider threats
- Reinforcement learning enables optimal threat hunting strategies
- Behavioral analysis detects unauthorized access patterns

**Agent Governance:**
- AI agents require behavioral baselines distinct from human users
- Autonomous threat hunting can monitor agent policy drift
- RL-based attribution adapts to evolving insider tactics

#### 2503.02065 - Explainable AI in Threat Intelligence Survey (Mar 2025)
**Key Findings:**
- Analysts demand attack attribution, confidence scores, feature contribution
- SHAP and LIME most commonly used XAI tools for feature attribution
- Post-hoc explanations enable security teams to interpret AI-based alerts

**Compliance Evidence:**
- XAI provides audit-ready evidence for "why" threat was attributed to specific actor
- Feature contribution maps to user behavioral characteristics
- Confidence scores enable risk-based response automation

#### 2506.04133 - TRiSM for Agentic AI (Jul 2025)
**Key Findings:**
- Reasoning trace logging creates audit trail of agent decision-making
- Decision provenance graphs make agent behaviors interpretable
- Trust, Risk, Security Management framework for multi-agent systems

**Infrastructure Audit Trails:**
- Every agent action must produce immutable reasoning trace
- Provenance graphs enable attribution: which agent, which user, which approval
- Blockchain-based audit trails prevent log tampering post-incident

#### 2508.10043 - Securing Agentic AI for Network Monitoring (Aug 2025)
**Key Findings:**
- API-level security controls with authentication and auditing mechanisms
- Interactive dashboards provide audit trail of agent actions
- Provenance of input data critical for LLM-based agents

**Model Registry Integration:**
- Model provenance includes: who trained, which data, which approval chain
- Agent-triggered model updates require explicit human approval
- Attribution links model behavior to responsible parties

#### 2510.23883 - Agentic AI Security: Threats and Defenses (Oct 2025)
**Key Findings:**
- Comprehensive threat taxonomy for autonomous agent systems
- Runtime monitoring and containment mechanisms essential
- Evaluation frameworks for agent security posture

**CSP Governance:**
- Agent containment prevents lateral movement after compromise
- Runtime behavioral monitoring detects policy drift in real-time
- Security posture scored per agent, triggering alerts on degradation

### Attribution Techniques Comparison:

| Technique | Accuracy | Real-time | Explainability | Use Case |
|-----------|----------|-----------|----------------|----------|
| Deep Evidential Clustering | 94.3% | Yes | Medium | Insider threat detection |
| SHAP/LIME Feature Attribution | N/A | No | High | Post-incident forensics |
| Behavioral Biometrics | 76-96% | Yes | Low | Continuous authentication |
| Provenance Graphs | N/A | No | High | Agent action attribution |
| Unsupervised Anomaly Detection | 65-85% | Yes | Low | Initial threat detection |

---

## 3. Baseline Establishment for AI Systems (11 Papers)

### Overview
Establishing trustworthy behavioral baselines for AI systems is foundational to detecting both attacks and drift. Research addresses dynamic baseline establishment, multi-modal baselines, and baseline validation.

### Key Papers:

#### 2501.09239 - AI-based Identity Fraud Detection (Jan 2025)
**Key Findings:**
- Three main IDF detection methods: biometric recognition, visual anomaly detection, behavioral anomaly detection
- Deep learning dominates: 76% of visual anomaly detection, 53% of behavioral
- Continuous authentication monitors baseline profile, detecting anomalies in real-time

**User Baseline for GitOps:**
- Developer commit patterns establish individual behavioral baseline
- Keystroke dynamics, commit timing, approval chain patterns
- Anomaly triggers additional verification before approval

#### 2509.14294 - Monitoring Machine Learning Systems (Sep 2025)
**Key Findings:**
- Nearly all ML monitoring tools support data drift, model performance, system operations monitoring
- Alerting, visualization, log processing standard across tools
- Tools like Mona, Superwise monitor data quality, anomalies, drift, label drift

**Model Registry Monitoring:**
- Baseline model performance metrics tracked per model version
- Data drift detection compares production data to training baseline
- Alert on model performance degradation beyond baseline threshold

#### 2507.15676 - Agentic AI for Anomaly Management (Jul 2025)
**Key Findings:**
- Traditional systems define anomalies as deviations from static definitions
- Fails in complex contexts where behaviors evolve over time
- Ill-equipped to handle novel but valid patterns

**Dynamic Baseline Strategy:**
- Baseline must adapt to legitimate evolution while rejecting poisoning
- Multiple baseline windows: short-term (detect rapid changes), long-term (detect drift)
- Baseline version control: Git-track baseline evolution with approval workflow

#### 2403.02439 - Root Causing Prediction Anomalies with XAI (Mar 2024)
**Key Findings:**
- Feature ablation algorithm attributes features relative to constant baseline
- Attribution methods sensitive to baseline choice
- Sliding window computes GFIs continuously, alerting on significant shifts

**Baseline Management:**
- CSP must version baselines alongside infrastructure code
- Baseline changes require approval workflow (like IaC changes)
- Sliding window comparison detects both sudden attacks and gradual drift

#### 2501.11430 - Diffusion Models for Anomaly Detection (Jan 2025)
**Key Findings:**
- Imbalanced datasets (rare anomalies) bias models toward majority class
- Diffusion models handle complex data distributions
- Baseline must account for class imbalance

**Training Data Baseline:**
- Feature store snapshots establish data distribution baseline
- Anomaly detection training requires balanced baseline representation
- Model baseline includes expected class distribution, updated per retrain

### Baseline Establishment Best Practices:

1. **Multi-Temporal Baselines**: Short-term (hours), medium-term (weeks), long-term (months)
2. **Version-Controlled Baselines**: Git-track baseline definitions, require approval for changes
3. **Multi-Modal Baselines**: Combine behavioral, performance, data distribution baselines
4. **Adaptive Baselines**: Update periodically with approved legitimate evolution
5. **Baseline Integrity Verification**: Cryptographic checksums prevent baseline tampering
6. **Baseline Provenance**: Track who established baseline, when, based on what data

---

## 4. Gradual Drift vs. Legitimate Evolution (6 Papers)

### Overview
Distinguishing malicious gradual drift from legitimate system evolution is critical for avoiding both false positives (blocking legitimate changes) and false negatives (missing attacks).

### Key Papers:

#### 2503.06606 - Interpretable Model Drift Detection (Mar 2025)
**Key Findings:**
- Model drift deals with performance deterioration due to data distribution evolution
- Data distribution shift (covariate/posterior) need not always cause significant degradation
- Distinguishing harmful drift from benign evolution requires interpretability

**CSP Drift Management:**
- Model performance degradation triggers investigation, not automatic rejection
- Covariate shift analysis determines if drift is data evolution or poisoning
- Approval workflow: data scientist reviews drift root cause before retraining

#### 2410.09190 - Time to Retrain? Detecting Concept Drifts (Oct 2024)
**Key Findings:**
- ML models encounter performance degradation from concept drift in production
- Current SOTA semi-supervised methods require significant labeling effort
- Unsupervised drift detection challenging but essential for real-world deployment

**Retraining Decision Framework:**
- Drift detection separates detection signal from retraining decision
- Approval required: human validates drift is legitimate evolution, not attack
- Immutable retraining: new model version, not in-place update

#### 2405.04095 - Combating Concept Drift in Android Malware (May 2024)
**Key Findings:**
- Rapid malware evolution causes concept drift depressing accuracy to near-random
- Explanatory detection identifies which features drifted
- Adaptive methods distinguish evolution from adversarial drift

**Security Monitoring Drift:**
- Malware evolution is legitimate drift requiring model update
- Adversarial evasion is attack requiring defensive response
- XAI attribution determines drift cause: evolution vs. evasion

#### 2411.15616 - Adaptive Data Segmentation for Drift (Nov 2024)
**Key Findings:**
- Scalable approach to covariate and concept drift management
- Adaptive data segmentation isolates drift to specific data segments
- Enables targeted response: update segment-specific baseline

**Segmented Baseline Strategy:**
- Different infrastructure components have different baseline evolution rates
- Segment baselines: networking, compute, storage, AI workloads
- Drift in one segment doesn't invalidate entire baseline

### Drift Decision Matrix:

| Drift Type | Characteristic | Response | Approval Required |
|------------|---------------|----------|-------------------|
| Legitimate Evolution | Gradual, correlated with known changes | Update baseline | Yes |
| Configuration Drift | Sudden, unauthorized | Remediate to version-controlled state | No (auto-revert) |
| Concept Drift | Performance degradation, data distribution shift | Retrain model | Yes |
| Adversarial Drift | Performance degradation, adversarial patterns | Incident response | Yes (security team) |
| Policy Drift | Agent behavior exceeds policy bounds | Containment, audit | Yes (governance team) |

---

## 5. Poisoning Detection and Prevention (6 Papers)

### Overview
Defensive mechanisms against poisoning attacks leverage adversarial training, cryptographic verification, supply chain security, and runtime monitoring.

### Key Papers:

#### 2503.09302 - Detecting and Preventing Data Poisoning (Mar 2025)
**Key Findings:**
- Model accuracy drops 27.2% (92.3% to 65.1%) under poisoning attacks
- Robust data validation and anomaly detection maintain model integrity
- Advanced anomaly detection, access controls, data sanitization critical

**CSP Defense Layers:**
1. **Data Validation**: Schema checks, range validation, statistical tests
2. **Anomaly Detection**: Outlier detection on training data before model training
3. **Access Controls**: RBAC on feature stores, audit logs on data modifications
4. **Data Sanitization**: Automated filtering of suspected poisoned samples

#### 2508.20307 - Operational Cybersecurity and AI Supply Chain (Aug 2025)
**Key Findings:**
- 100+ malicious models discovered on Hugging Face in early 2024
- Pickle deserialization vulnerability exploited for arbitrary code execution
- As of early 2025, malicious models still found exploiting same vulnerability

**Model Registry Security:**
- Cryptographic checksums/signatures ensure model authenticity
- AI-specific SBOMs include model source, integrity checks, digital signatures
- Runtime integrity verification ensures deployed model matches signed version
- Zero trust for training pipeline: no model deployed without verification

#### 2406.02619 - Unelicitable Backdoors in Language Models (Jun 2024)
**Key Findings:**
- Cryptographic transformer circuits enable undetectable backdoors
- Model displays undesired behavior at inference time
- Backdoors hard to detect from model characteristics alone

**Backdoor Detection Strategy:**
- Behavioral testing: adversarial inputs designed to trigger backdoors
- Model comparison: compare behavior to known-good baseline model
- Explainability analysis: detect hidden backdoor triggers via XAI
- Ensemble validation: multiple models vote on inference, reject outliers

#### 2509.20411 - Adversarial Defense in Cybersecurity (Sep 2024)
**Key Findings:**
- Publication activity in adversarial defenses peaked in 2024
- GAN-based augmentation improves F1-scores by 10-15%
- Adversarial training reduces false negatives by up to 22%

**Defense Implementation:**
- Standard practice: adversarial training for all security-critical models
- GAN-based data augmentation generates adversarial examples for training
- Regular adversarial robustness testing before model promotion

#### 2506.23296 - Securing AI Systems: Guide to Attacks and Impacts (Jun 2025)
**Key Findings:**
- Comprehensive attack taxonomy and mitigation strategies
- Quantization exploits serve as triggers for behavior manipulation
- Malicious AI models simulate diverse attack scenarios

**CSP Security Posture:**
- Threat modeling for each AI system deployment
- Attack surface analysis: identify poisoning vectors
- Defense-in-depth: multiple layers prevent single point of failure

### Prevention Framework (Defense-in-Depth):

**Layer 1 - Supply Chain Security:**
- Trusted model repositories with verification
- Cryptographic signing of all artifacts
- SBOM generation and validation
- Dependency pinning and scanning

**Layer 2 - Data Integrity:**
- Immutable data snapshots with checksums
- Feature store with versioning and lineage
- Anomaly detection on training data
- Data validation pipeline with statistical tests

**Layer 3 - Training Security:**
- Isolated training environments
- Access controls on training pipelines
- Adversarial training standard
- Baseline model comparison

**Layer 4 - Model Validation:**
- Behavioral testing against backdoor triggers
- Performance comparison to baseline
- Explainability analysis for hidden triggers
- Multi-model ensemble validation

**Layer 5 - Deployment Security:**
- Runtime integrity verification
- Cryptographic signature validation
- Immutable deployment (no in-place updates)
- Continuous behavioral monitoring

**Layer 6 - Monitoring and Response:**
- Real-time anomaly detection
- Drift detection with root cause analysis
- Automated remediation for known attacks
- Incident response playbooks

---

## Synthesis: Mapping Research to CSP Infrastructure Security

### Threat Scenario 1: Gradual Baseline Poisoning of AI-Powered SOC

**Attack Vector:**
Insider or compromised agent gradually modifies firewall rules over weeks, introducing subtle changes that expand attack surface. AI-powered SOC baseline adapts to include these modifications, rendering them "normal."

**Research-Validated Defense:**
- **Multi-temporal baselines** (2403.02439): Compare current state to baselines from multiple time windows
- **Versioned baseline management** (2507.15676): Git-track baseline evolution, require approval for baseline updates
- **Drift attribution** (2503.06606): XAI determines if drift is legitimate evolution or malicious manipulation
- **Immutable infrastructure** (Survey): Infrastructure defined in Git prevents gradual unauthorized modification

**Implementation:**
```yaml
baseline_management:
  windows:
    - short_term: 24_hours  # Detect rapid attacks
    - medium_term: 7_days   # Detect gradual drift
    - long_term: 30_days    # Detect slow poisoning

  approval_workflow:
    - baseline_change_detected: true
    - require_approval: security_team
    - validation:
        - compare_to_git_desired_state
        - xai_drift_attribution
        - multi_baseline_consensus

  auto_remediation:
    - condition: unauthorized_drift_detected
    - action: revert_to_git_versioned_state
    - notify: security_team
```

### Threat Scenario 2: Insider Using AI to Cover Tracks

**Attack Vector:**
Malicious insider uses AI to analyze monitoring systems, identify blind spots, time attacks during legitimate baseline evolution periods, and generate covering noise to mask malicious activities.

**Research-Validated Defense:**
- **Behavioral biometrics** (2501.09239): Continuous authentication detects anomalous user behavior patterns
- **Provenance tracking** (2506.04133): Decision provenance graphs attribute all actions to specific users/agents
- **Real-time insider threat detection** (2505.15383): 94.3% accuracy, <1.2% false positive rate
- **Explainable attribution** (2503.02065): SHAP/LIME identify which behavioral features indicate insider threat

**Implementation:**
```yaml
insider_threat_monitoring:
  behavioral_baseline:
    features:
      - commit_timing_patterns
      - approval_chain_usage
      - ssh_session_characteristics
      - api_call_patterns
      - resource_access_patterns

  continuous_authentication:
    - keystroke_dynamics: enabled
    - session_behavior: monitored
    - anomaly_threshold: adaptive
    - re_authentication_trigger: behavioral_anomaly

  attribution:
    - provenance_graph: all_actions
    - audit_trail: immutable_blockchain
    - xai_explainability: shap_lime
    - confidence_scoring: enabled

  response:
    - anomaly_detected:
        - suspend_access
        - notify_security_team
        - preserve_forensic_evidence
        - generate_xai_report
```

### Threat Scenario 3: Compromised Agent Modifying Model Registry

**Attack Vector:**
Compromised AI agent with model registry permissions gradually poisons model evaluation metrics, causing malicious model to appear high-performing. Model promoted to production through automated approval workflow.

**Research-Validated Defense:**
- **Agent containment** (2510.23883): Runtime monitoring limits agent capabilities
- **Model integrity verification** (2508.20307): Cryptographic signatures, SBOM validation
- **Adversarial robustness testing** (2509.20411): GAN-based testing before promotion
- **Multi-model ensemble validation** (2503.09302): Multiple models vote, reject outliers

**Implementation:**
```yaml
model_registry_security:
  agent_permissions:
    - least_privilege: enforced
    - no_direct_modification: true
    - all_actions_via_api: true
    - audit_trail: immutable

  model_validation:
    - cryptographic_signature: required
    - sbom_generation: automated
    - adversarial_robustness_test:
        - gan_based_attacks: true
        - backdoor_trigger_detection: true
        - baseline_comparison: required
    - ensemble_validation:
        - multiple_models: 3
        - consensus_threshold: 66%

  approval_workflow:
    - automated_metrics: insufficient_alone
    - human_review: required
    - xai_explanation: generated
    - security_scan: mandatory
    - provenance_verification: complete
```

### Threat Scenario 4: Supply Chain Attack via Poisoned Pretrained Model

**Attack Vector:**
Attacker uploads backdoored pretrained model to public registry. CSP customer downloads and deploys without verification. Backdoor triggered by specific input patterns, exfiltrating data.

**Research-Validated Defense:**
- **Supply chain threat landscape** (2508.20307): Validate model origin and integrity
- **Cryptographic backdoor detection** (2406.02619): Behavioral testing for hidden triggers
- **Model scanning and SBOM** (2506.23296): Comprehensive vulnerability scanning
- **Zero trust training pipeline** (2508.20307): No model deployed without verification

**Implementation:**
```yaml
supply_chain_security:
  model_acquisition:
    - trusted_sources_only: true
    - cryptographic_verification: required
    - sbom_validation: mandatory
    - provenance_check:
        - training_data_source
        - training_process_audit
        - developer_identity_verification

  security_scanning:
    - vulnerability_scan: automated
    - backdoor_detection:
        - behavioral_testing: adversarial_inputs
        - trigger_pattern_detection: enabled
        - baseline_comparison: known_good_model
    - quantization_exploit_check: true

  deployment_controls:
    - containerize: immutable_image
    - sign_image: cryptographic
    - runtime_monitoring: behavioral_anomaly
    - network_isolation: enforced
    - data_access_logging: comprehensive
```

---

## Strategic Recommendations for CSPs

### Immediate Actions (0-3 months):

1. **Implement Multi-Temporal Baselines**
   - Deploy sliding window baseline comparison (24h, 7d, 30d windows)
   - Version-control baseline definitions in Git with approval workflow
   - Alert on significant deviation from any temporal baseline

2. **Establish Model Registry Security**
   - Require cryptographic signatures on all models
   - Generate SBOMs for all container images and models
   - Implement adversarial robustness testing before promotion

3. **Deploy Insider Threat Detection**
   - Instrument GitOps workflows for behavioral baseline per user
   - Implement continuous authentication for privileged access
   - Deploy XAI-based attribution for anomalous activities

4. **Secure AI Agent Operations**
   - Implement agent containment with runtime monitoring
   - Require immutable audit trails for all agent actions
   - Deploy provenance graphs for agent decision attribution

### Medium-Term Actions (3-12 months):

5. **Build Adversarial Defense Program**
   - Integrate adversarial training for all security-critical models
   - Deploy GAN-based testing frameworks
   - Establish red team for baseline poisoning attack simulation

6. **Implement Drift Detection and Response**
   - Deploy automated concept drift detection
   - Build XAI-based drift root cause analysis
   - Establish approval workflow: evolution vs. attack determination

7. **Enhance Supply Chain Security**
   - Build trusted model repository with verification
   - Implement zero-trust training pipeline
   - Deploy behavioral backdoor detection

8. **Establish Governance Framework**
   - Define approval rules per artifact type
   - Implement compliance evidence generation
   - Build audit-ready reporting for regulators

### Long-Term Strategic Initiatives (12+ months):

9. **AI-Powered Autonomous Threat Hunting**
   - Deploy reinforcement learning-based threat hunting
   - Integrate with SIEM for automated investigation
   - Build adaptive baseline evolution detection

10. **Federated Learning Security**
    - Implement poisoning-resistant federated training
    - Deploy privacy-preserving multi-party verification
    - Build consensus-based model validation

11. **Quantum-Resistant Cryptography**
    - Prepare for post-quantum cryptographic signatures
    - Implement quantum-resistant model integrity verification
    - Build quantum-safe audit trail systems

12. **Continuous Compliance Automation**
    - Auto-generate evidence for NIST AI RMF, EU AI Act, ISO 42001
    - Implement self-service compliance queries
    - Build real-time compliance posture dashboards

---

## Research Gaps and Future Work

### Identified Gaps:

1. **Session Creep Formalization**
   - Limited formal research on "session creep" attack patterns
   - Need standardized taxonomy and detection methods
   - Recommendation: CSP-funded research on gradual baseline manipulation

2. **Multi-Agent Attribution**
   - Attribution in multi-agent environments remains challenging
   - Provenance graphs become complex with agent interactions
   - Recommendation: Blockchain-based immutable agent interaction logs

3. **Real-Time Drift Causation**
   - Distinguishing evolution from attack in real-time unsolved
   - Current methods require human validation
   - Recommendation: Automated XAI-based causation determination

4. **Adversarial Robustness at Scale**
   - Adversarial training computationally expensive for large models
   - Limited research on efficient adversarial robustness for production
   - Recommendation: Efficient adversarial training methods research

5. **Baseline Provenance Standards**
   - No industry standard for baseline version control
   - Limited tooling for baseline Git-tracking
   - Recommendation: Open-source baseline management framework

### Recommended Research Directions:

1. **Automated Drift Causation Analysis**
   - ML-based root cause analysis for drift events
   - Distinguish legitimate evolution, configuration drift, adversarial drift
   - Generate XAI explanations for audit trails

2. **Efficient Adversarial Training**
   - Reduce computational cost of adversarial robustness
   - Selective adversarial training for critical model components
   - Transfer learning for adversarial robustness

3. **Multi-Modal Baseline Fusion**
   - Combine behavioral, performance, data distribution baselines
   - Consensus-based anomaly detection across baseline types
   - Adaptive weighting based on drift patterns

4. **Agent Behavioral Fingerprinting**
   - Unique behavioral signatures for each agent instance
   - Detect agent impersonation and privilege escalation
   - Continuous agent identity verification

5. **Poisoning-Resistant Federated Learning**
   - Byzantine-robust aggregation for federated training
   - Privacy-preserving poisoning detection
   - Differential privacy for baseline protection

---

## Conclusion

This research compilation validates the critical security challenges identified in the version-controlled deployment survey. **Baseline poisoning is real, feasible, and actively exploited**. **AI-assisted attribution is effective but requires comprehensive instrumentation**. **Distinguishing drift from attacks requires multi-temporal baselines and XAI**.

**Key Takeaways:**

1. **Immutable infrastructure is essential** - prevents gradual baseline manipulation by enforcing version-controlled state
2. **Multi-temporal baselines detect attacks** - comparing multiple time windows identifies gradual poisoning
3. **XAI enables attribution** - SHAP/LIME provide audit-ready evidence for insider threat attribution
4. **Agent governance is critical** - provenance tracking and containment prevent agent-based attacks
5. **Adversarial training is mandatory** - security-critical models must be hardened against poisoning
6. **Supply chain verification is non-negotiable** - cryptographic signatures and behavioral testing prevent backdoored models

**CSPs must implement:**
- Version-controlled baselines with approval workflows
- Multi-temporal baseline comparison and drift detection
- XAI-based attribution for anomalous activities
- Immutable audit trails for all infrastructure and agent actions
- Adversarial robustness testing for all models
- Cryptographic verification for entire supply chain

The research demonstrates that with proper instrumentation, CSPs can detect baseline poisoning, attribute insider threats, and distinguish legitimate drift from attacks - but only if immutability, version control, and continuous monitoring are foundational to infrastructure operations.

---

## Paper Inventory

### Baseline Poisoning (11 papers)
1. 1802.03041 - Detection of Adversarial Training Examples in Poisoning Attacks
2. 2303.07003 - Review on Adversarial Evasion Attacks for NIDS
3. 2306.05494 - Adversarial Evasion Attacks Practicality in Networks
4. 2309.00614 - Baseline Defenses for Adversarial Attacks Against LLMs
5. 2309.09498 - Combating Advanced Persistent Threats
6. 2401.08984 - GAN-based Data Poisoning Framework
7. 2410.23687 - Adversarial Attacks of Vision Tasks Survey
8. 2412.00797 - Stealthy Poisoning in Reinforcement Learning
9. 2502.05637 - Adversarial Machine Learning: Attacks, Defenses, Challenges
10. 2502.15561 - Defensive Framework Against Adversarial Attacks on NIDS
11. 2503.22759 - Data Poisoning in Deep Learning Survey

### Insider Attribution (14 papers)
1. 1710.00811 - Deep Learning for Unsupervised Insider Threat Detection
2. 2401.00286 - Autonomous Threat Hunting
3. 2406.02630 - AI Agents Under Threat Survey
4. 2408.03335 - Explainable AI-based Intrusion Detection System
5. 2501.10114 - Agent Attribution
6. 2502.02649 - Fully Autonomous AI Agents Should Not Be Developed
7. 2503.02065 - Explainable AI in Threat Intelligence Survey
8. 2505.02077 - Open Challenges in Multi-Agent Security
9. 2505.08807 - Security of Internet of Agents
10. 2505.15383 - Real-Time Insider Threat Detection
11. 2506.04133 - TRiSM for Agentic AI
12. 2508.10043 - Securing Agentic AI for Network Monitoring
13. 2508.18765 - Governance-as-a-Service
14. 2510.23883 - Agentic AI Security: Threats, Defenses, Evaluation

### Baseline Establishment (11 papers)
1. 1712.09867 - Future Frame Prediction for Anomaly Detection Baseline
2. 2211.05244 - Deep Learning for Time Series Anomaly Detection
3. 2302.02740 - AuthentiSense: Behavioral Biometrics Authentication
4. 2403.02439 - Root Causing Prediction Anomalies Using XAI
5. 2405.06925 - Semi-supervised Anomaly Detection via Adaptive RL
6. 2501.09239 - AI-based Identity Fraud Detection
7. 2501.11430 - Diffusion Models for Anomaly Detection Survey
8. 2503.13195 - Deep Learning Advancements in Anomaly Detection Survey
9. 2506.06825 - Identity Deepfake Threats to Biometric Authentication
10. 2507.15676 - Agentic AI for Autonomous Anomaly Management
11. 2509.14294 - Monitoring Machine Learning Systems

### Drift Detection (6 papers)
1. 2203.11070 - From Concept Drift to Model Degradation
2. 2405.04095 - Combating Concept Drift in Android Malware Classification
3. 2410.09190 - Time to Retrain? Detecting Concept Drifts
4. 2411.15616 - Adaptive Data Segmentation for Drift Management
5. 2503.06606 - Interpretable Model Drift Detection
6. 2508.00042 - Concept Drift Detection in 6G Wireless Networks

### Poisoning Prevention (6 papers)
1. 2406.02619 - Unelicitable Backdoors in Language Models
2. 2503.09302 - Detecting and Preventing Data Poisoning Attacks
3. 2506.23296 - Securing AI Systems: Guide to Known Attacks
4. 2507.07416 - Securing Critical Infrastructure in the AI Era
5. 2508.20307 - Operational Cybersecurity and Supply Chain Threats
6. 2509.20411 - Adversarial Defense in Cybersecurity

---

**Document Prepared:** December 9, 2025
**Research Period Covered:** 2024-2025
**Primary Focus:** Baseline Poisoning & AI-Assisted Insider Threat Attribution
**Application Context:** CSP Infrastructure Security, AI Agent Governance, ML Artifact Integrity
