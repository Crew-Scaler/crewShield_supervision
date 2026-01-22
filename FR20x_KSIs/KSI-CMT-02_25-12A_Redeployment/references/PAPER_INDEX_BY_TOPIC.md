# Paper Index by Research Topic
## Baseline Poisoning & AI-Assisted Insider Threats Research

This index organizes the 48 downloaded papers by specific research topics for easy reference.

---

## Table of Contents
1. [Baseline Poisoning Attack Methods](#baseline-poisoning-attack-methods)
2. [Gradual and Stealthy Attacks](#gradual-and-stealthy-attacks)
3. [Insider Threat Detection and Attribution](#insider-threat-detection-and-attribution)
4. [AI Agent Security and Governance](#ai-agent-security-and-governance)
5. [Behavioral Baseline Establishment](#behavioral-baseline-establishment)
6. [Drift Detection and Causation](#drift-detection-and-causation)
7. [Poisoning Prevention and Defense](#poisoning-prevention-and-defense)
8. [Supply Chain Security](#supply-chain-security)
9. [Explainable AI for Attribution](#explainable-ai-for-attribution)
10. [Adversarial Robustness](#adversarial-robustness)

---

## Baseline Poisoning Attack Methods

**Session Creep and Gradual Manipulation:**
- 2306.05494 - Adversarial Evasion Attacks Practicality in Networks
  - Location: `/baseline_poisoning/`
  - Key Topic: Systems adapting to behavioral changes vulnerable to "session creep"
  - Finding: Attackers gradually introduce malicious behavior into baseline

**Data Poisoning Frameworks:**
- 2401.08984 - GAN-based Data Poisoning Framework
  - Location: `/baseline_poisoning/`
  - Key Topic: P-GAN framework for vertical federated learning poisoning
  - Finding: Adversarial perturbations degrade model performance

- 2503.22759 - Data Poisoning in Deep Learning Survey
  - Location: `/baseline_poisoning/`
  - Key Topic: Static vs. dynamic poisoning attacks
  - Finding: Dynamic attacks adapt over time, persistence makes detection challenging

**Reinforcement Learning Poisoning:**
- 2412.00797 - Stealthy Poisoning in Reinforcement Learning
  - Location: `/baseline_poisoning/`
  - Key Topic: Stealthy attacks as optimization problems
  - Finding: Online attacks occur simultaneously with agent-environment interaction

**Adversarial Training Detection:**
- 1802.03041 - Detection of Adversarial Training Examples in Poisoning Attacks
  - Location: `/baseline_poisoning/`
  - Key Topic: Anomaly detection for poisoned training data
  - Finding: Adversarial examples detectable through statistical analysis

---

## Gradual and Stealthy Attacks

**Advanced Persistent Threats (APTs):**
- 2309.09498 - Combating Advanced Persistent Threats
  - Location: `/baseline_poisoning/`
  - Key Topic: Temporal evasion strategies, interspersed attack sequences
  - Finding: Rapid stealthy evasion detection challenging in dynamic environments

**Stealthy Attack Optimization:**
- 2412.00797 - Stealthy Poisoning in Reinforcement Learning
  - Location: `/baseline_poisoning/`
  - Key Topic: Formalize stealthiness as optimization problem
  - Finding: Minimize deviation from original environment while attacking

**Temporal Attack Patterns:**
- 2306.05494 - Adversarial Evasion Attacks Practicality in Networks
  - Location: `/baseline_poisoning/`
  - Key Topic: Testing impact of dynamic learning on attack success
  - Finding: Dynamic systems more vulnerable to gradual attacks

---

## Insider Threat Detection and Attribution

**High-Accuracy Real-Time Detection:**
- 2505.15383 - Real-Time Insider Threat Detection
  - Location: `/insider_attribution/`
  - Key Topic: Deep evidential clustering, behavioral analytics
  - Finding: 94.3% detection accuracy, <1.2% false positive rate

**Autonomous Threat Hunting:**
- 2401.00286 - Autonomous Threat Hunting
  - Location: `/insider_attribution/`
  - Key Topic: Unsupervised learning for abnormal user behavior
  - Finding: Reinforcement learning enables optimal threat hunting strategies

**Behavioral Feature Analysis:**
- 2505.15383 - Real-Time Insider Threat Detection
  - Location: `/insider_attribution/`
  - Key Topic: Time, User, Project/Role, Activity, Logon, USB, File, Email features
  - Finding: Random Forest achieves 96.4% accuracy for User-related features

**Deep Learning for Insider Threats:**
- 1710.00811 - Deep Learning for Unsupervised Insider Threat Detection
  - Location: `/insider_attribution/`
  - Key Topic: Online unsupervised deep learning for log anomaly detection
  - Finding: Decompose anomaly scores into individual feature contributions

---

## AI Agent Security and Governance

**Trust, Risk, Security Management (TRiSM):**
- 2506.04133 - TRiSM for Agentic AI
  - Location: `/insider_attribution/`
  - Key Topic: Reasoning trace logging, decision provenance graphs
  - Finding: Audit trail of agent decision-making process

**Network Monitoring Agent Security:**
- 2508.10043 - Securing Agentic AI for Network Monitoring
  - Location: `/insider_attribution/`
  - Key Topic: API-level security, authentication, auditing mechanisms
  - Finding: Interactive dashboards provide audit trail of agent actions

**Multi-Agent Security Challenges:**
- 2505.02077 - Open Challenges in Multi-Agent Security
  - Location: `/insider_attribution/`
  - Key Topic: Securing audit trails when using tools
  - Finding: Multi-agent environments complicate provenance tracking

**Internet of Agents Security:**
- 2505.08807 - Security of Internet of Agents
  - Location: `/insider_attribution/`
  - Key Topic: Embedding audit trails via immutable ledgers/blockchains
  - Finding: Privacy-preserving blockchains for agent interaction audit

**Comprehensive Agent Threat Taxonomy:**
- 2510.23883 - Agentic AI Security: Threats, Defenses, Evaluation
  - Location: `/insider_attribution/`
  - Key Topic: Runtime monitoring, containment mechanisms
  - Finding: Robust containment essential for autonomous agent systems

**Agent Survey:**
- 2406.02630 - AI Agents Under Threat Survey
  - Location: `/insider_attribution/`
  - Key Topic: Auditing complex internal execution of AI agents
  - Finding: Internal execution states implicit, difficult to observe

**Governance Framework:**
- 2508.18765 - Governance-as-a-Service
  - Location: `/insider_attribution/`
  - Key Topic: Multi-agent compliance and policy enforcement
  - Finding: Time-stamped audit trail with rule ID, agent ID, action, context

**Autonomous Agent Risks:**
- 2502.02649 - Fully Autonomous AI Agents Should Not Be Developed
  - Location: `/insider_attribution/`
  - Key Topic: Risks of fully autonomous agents
  - Finding: Safety and control concerns with full autonomy

**Agent Attribution:**
- 2501.10114 - Agent Attribution
  - Location: `/insider_attribution/`
  - Key Topic: Attributing actions to specific agents and users
  - Finding: Three functions for agent infrastructure attribution

---

## Behavioral Baseline Establishment

**Identity Fraud Detection:**
- 2501.09239 - AI-based Identity Fraud Detection
  - Location: `/baseline_establishment/`
  - Key Topic: Biometric recognition, visual anomaly, behavioral anomaly detection
  - Finding: Deep learning dominates (76% visual, 53% behavioral)

**Behavioral Biometrics Authentication:**
- 2302.02740 - AuthentiSense: Behavioral Biometrics Authentication
  - Location: `/baseline_establishment/`
  - Key Topic: Few-shot learning for mobile behavioral biometrics
  - Finding: Scalable authentication using limited training samples

**Deepfake Threat Mitigation:**
- 2506.06825 - Identity Deepfake Threats to Biometric Authentication
  - Location: `/baseline_establishment/`
  - Key Topic: Dynamic biometric signals resist deepfakes
  - Finding: Involuntary eye movements difficult for Gen-AI to replicate

**ML System Monitoring:**
- 2509.14294 - Monitoring Machine Learning Systems
  - Location: `/baseline_establishment/`
  - Key Topic: Data drift, model performance, system operations monitoring
  - Finding: Nearly all tools support alerting, visualization, log processing

**Agentic AI for Anomaly Management:**
- 2507.15676 - Agentic AI for Autonomous Anomaly Management
  - Location: `/baseline_establishment/`
  - Key Topic: Static definitions fail in evolving contexts
  - Finding: Systems ill-equipped to handle novel but valid patterns

**Root Cause Analysis with XAI:**
- 2403.02439 - Root Causing Prediction Anomalies Using XAI
  - Location: `/baseline_establishment/`
  - Key Topic: Feature ablation, attribution relative to baseline
  - Finding: Attribution methods sensitive to baseline choice

**Time Series Anomaly Detection:**
- 2211.05244 - Deep Learning for Time Series Anomaly Detection
  - Location: `/baseline_establishment/`
  - Key Topic: Comprehensive survey up to 2024
  - Finding: Concept drift changes values and trends gradually or abruptly

**Anomaly Detection Baseline Methods:**
- 1712.09867 - Future Frame Prediction for Anomaly Detection Baseline
  - Location: `/baseline_establishment/`
  - Key Topic: Establishing new baseline for video anomaly detection
  - Finding: Future frame prediction as anomaly detection method

**Semi-supervised Anomaly Detection:**
- 2405.06925 - Semi-supervised Anomaly Detection via Adaptive RL
  - Location: `/baseline_establishment/`
  - Key Topic: Adaptive threshold smoothing, decision reward mechanism
  - Finding: Enhanced flexibility and generalization ability

**Diffusion Models for Anomaly Detection:**
- 2501.11430 - Diffusion Models for Anomaly Detection Survey
  - Location: `/baseline_establishment/`
  - Key Topic: Handling complex data distributions
  - Finding: Imbalanced datasets bias models toward majority class

**Deep Learning Anomaly Detection Survey:**
- 2503.13195 - Deep Learning Advancements in Anomaly Detection Survey
  - Location: `/baseline_establishment/`
  - Key Topic: 160+ papers from 2019-2024
  - Finding: Timely comprehensive overview of latest advancements

---

## Drift Detection and Causation

**Concept Drift Detection:**
- 2410.09190 - Time to Retrain? Detecting Concept Drifts
  - Location: `/drift_detection/`
  - Key Topic: Performance degradation from concept drift in production
  - Finding: SOTA semi-supervised methods require significant labeling

**Interpretable Model Drift:**
- 2503.06606 - Interpretable Model Drift Detection
  - Location: `/drift_detection/`
  - Key Topic: Model drift from data distribution evolution
  - Finding: Data shift need not always lead to significant degradation

**Malware Classification Drift:**
- 2405.04095 - Combating Concept Drift in Android Malware
  - Location: `/drift_detection/`
  - Key Topic: Rapid malware evolution causes concept drift
  - Finding: Classification accuracy can drop to near-random levels

**Concept Drift to Model Degradation:**
- 2203.11070 - From Concept Drift to Model Degradation
  - Location: `/drift_detection/`
  - Key Topic: Comprehensive overview of drift impacts
  - Finding: Performance degradation from distribution changes

**Adaptive Data Segmentation:**
- 2411.15616 - Adaptive Data Segmentation for Drift
  - Location: `/drift_detection/`
  - Key Topic: Covariate and concept drift management
  - Finding: Scalable approach isolates drift to specific segments

**6G Wireless Network Drift:**
- 2508.00042 - Concept Drift Detection in 6G Wireless Networks
  - Location: `/drift_detection/`
  - Key Topic: AI-native 6G networks face drift challenges
  - Finding: Dynamism and complexity introduce significant challenges

---

## Poisoning Prevention and Defense

**Defensive Framework for NIDS:**
- 2502.15561 - Defensive Framework Against Adversarial Attacks on NIDS
  - Location: `/baseline_poisoning/`
  - Key Topic: Adversarial training, ensemble learning, feature engineering
  - Finding: 35% accuracy increase, 12.5% reduction in false positives

**Adversarial Defense Survey:**
- 2509.20411 - Adversarial Defense in Cybersecurity
  - Location: `/poisoning_prevention/`
  - Key Topic: Publication activity peaked 2024, GAN-based defenses
  - Finding: GAN augmentation improves F1-scores 10-15%, reduces false negatives 22%

**Detecting and Preventing Data Poisoning:**
- 2503.09302 - Detecting and Preventing Data Poisoning
  - Location: `/poisoning_prevention/`
  - Key Topic: Robust data validation, anomaly detection
  - Finding: Model accuracy drops 27.2% under poisoning (92.3% to 65.1%)

**Securing AI Systems Guide:**
- 2506.23296 - Securing AI Systems: Guide to Known Attacks
  - Location: `/poisoning_prevention/`
  - Key Topic: Comprehensive attack taxonomy and mitigations
  - Finding: Quantization exploits serve as triggers for behavior manipulation

**Critical Infrastructure Security:**
- 2507.07416 - Securing Critical Infrastructure in the AI Era
  - Location: `/poisoning_prevention/`
  - Key Topic: AI-based security framework for critical infrastructure
  - Finding: ML models analyze historical attack patterns, calculate dynamic impact scores

**Evasion Attack Review:**
- 2303.07003 - Review on Adversarial Evasion Attacks for NIDS
  - Location: `/baseline_poisoning/`
  - Key Topic: Feasibility of adversarial evasion attacks and defenses
  - Finding: Comprehensive review of attack and defense methods

**Baseline Defenses for LLMs:**
- 2309.00614 - Baseline Defenses for Adversarial Attacks Against LLMs
  - Location: `/baseline_poisoning/`
  - Key Topic: Defensive mechanisms for aligned language models
  - Finding: Baseline defense methods for LLM adversarial attacks

---

## Supply Chain Security

**Operational Cybersecurity and Supply Chain:**
- 2508.20307 - Operational Cybersecurity and Supply Chain Threats
  - Location: `/poisoning_prevention/`
  - Key Topic: 100+ malicious models on Hugging Face
  - Finding: Pickle deserialization exploited for arbitrary code execution

**Unelicitable Backdoors:**
- 2406.02619 - Unelicitable Backdoors in Language Models
  - Location: `/poisoning_prevention/`
  - Key Topic: Cryptographic transformer circuits enable undetectable backdoors
  - Finding: Backdoors hard to detect from model characteristics alone

**Adversarial Attacks Vision Survey:**
- 2410.23687 - Adversarial Attacks of Vision Tasks Survey
  - Location: `/baseline_poisoning/`
  - Key Topic: 10-year survey of adversarial attacks on vision tasks
  - Finding: Comprehensive taxonomy of attack methods

**Adversarial ML Comprehensive Analysis:**
- 2502.05637 - Adversarial Machine Learning: Attacks, Defenses, Challenges
  - Location: `/baseline_poisoning/`
  - Key Topic: Vulnerabilities where adversaries manipulate inputs/training data
  - Finding: Challenges implementing robust solutions in adaptive threat models

---

## Explainable AI for Attribution

**XAI in Threat Intelligence:**
- 2503.02065 - Explainable AI in Threat Intelligence Survey
  - Location: `/insider_attribution/`
  - Key Topic: Analysts demand attack attribution, confidence scores
  - Finding: SHAP and LIME most common XAI tools for feature attribution

**XAI-based Intrusion Detection:**
- 2408.03335 - Explainable AI-based Intrusion Detection System
  - Location: `/insider_attribution/`
  - Key Topic: Industry 5.0 intrusion detection with XAI
  - Finding: Explainability enables better interpretation and validation

**Root Causing with XAI:**
- 2403.02439 - Root Causing Prediction Anomalies Using XAI
  - Location: `/baseline_establishment/`
  - Key Topic: Feature ablation algorithm for attribution
  - Finding: GFI shifts between control and anomaly windows

---

## Adversarial Robustness

**GAN-based Defense:**
- 2509.20411 - Adversarial Defense in Cybersecurity
  - Location: `/poisoning_prevention/`
  - Key Topic: GAN-based augmentation and adversarial training
  - Finding: Empirical evidence shows 10-15% F1-score improvement

**Defensive Framework:**
- 2502.15561 - Defensive Framework Against Adversarial Attacks on NIDS
  - Location: `/baseline_poisoning/`
  - Key Topic: Integrating adversarial training, dataset balancing
  - Finding: 35% accuracy increase under adversarial conditions

**Adversarial Evasion Practicality:**
- 2306.05494 - Adversarial Evasion Attacks Practicality in Networks
  - Location: `/baseline_poisoning/`
  - Key Topic: Realistic attack generation with genetic algorithms
  - Finding: Feature mutability, interdependence, network constraints

**GAN Poisoning Defense:**
- 2401.08984 - GAN-based Data Poisoning Framework
  - Location: `/baseline_poisoning/`
  - Key Topic: Deep auto-encoders filter outliers via reconstruction error
  - Finding: DAE-based anomaly detection defends against P-GAN attacks

---

## Cross-Reference by CSP Use Case

### Use Case 1: Securing GitOps Workflows
**Relevant Papers:**
- 2505.15383 - Real-Time Insider Threat Detection (behavioral baselines per developer)
- 2506.04133 - TRiSM for Agentic AI (audit trails for agent actions)
- 2403.02439 - Root Causing Prediction Anomalies (baseline drift detection)
- 2503.06606 - Interpretable Model Drift Detection (distinguish evolution vs. attack)

### Use Case 2: Model Registry Security
**Relevant Papers:**
- 2508.20307 - Operational Cybersecurity and Supply Chain (malicious model detection)
- 2406.02619 - Unelicitable Backdoors in Language Models (behavioral backdoor testing)
- 2503.09302 - Detecting and Preventing Data Poisoning (validation pipelines)
- 2509.20411 - Adversarial Defense in Cybersecurity (adversarial training)

### Use Case 3: AI Agent Containment
**Relevant Papers:**
- 2510.23883 - Agentic AI Security (runtime monitoring, containment)
- 2508.10043 - Securing Agentic AI for Network Monitoring (API-level controls)
- 2505.08807 - Security of Internet of Agents (blockchain audit trails)
- 2508.18765 - Governance-as-a-Service (compliance enforcement)

### Use Case 4: Drift Detection and Response
**Relevant Papers:**
- 2410.09190 - Time to Retrain? Detecting Concept Drifts (retraining triggers)
- 2503.06606 - Interpretable Model Drift Detection (XAI root cause)
- 2405.04095 - Combating Concept Drift in Android Malware (adaptive methods)
- 2411.15616 - Adaptive Data Segmentation (segment-specific baselines)

### Use Case 5: Behavioral Monitoring
**Relevant Papers:**
- 2501.09239 - AI-based Identity Fraud Detection (continuous authentication)
- 2302.02740 - AuthentiSense Behavioral Biometrics (keystroke dynamics)
- 2509.14294 - Monitoring ML Systems (comprehensive monitoring tools)
- 2507.15676 - Agentic AI for Anomaly Management (dynamic baselines)

---

## Quick Reference by Paper Number

| ArXiv ID | Short Title | Primary Topic | Location |
|----------|-------------|---------------|----------|
| 1710.00811 | Unsupervised Insider Threat | Insider Attribution | insider_attribution/ |
| 1712.09867 | Anomaly Detection Baseline | Baseline Establishment | baseline_establishment/ |
| 1802.03041 | Adversarial Training Poisoning | Baseline Poisoning | baseline_poisoning/ |
| 2203.11070 | Concept Drift to Degradation | Drift Detection | drift_detection/ |
| 2211.05244 | Time Series Anomaly Detection | Baseline Establishment | baseline_establishment/ |
| 2302.02740 | Behavioral Biometrics | Baseline Establishment | baseline_establishment/ |
| 2303.07003 | Adversarial Evasion NIDS | Baseline Poisoning | baseline_poisoning/ |
| 2306.05494 | Evasion Attacks Networks | Baseline Poisoning | baseline_poisoning/ |
| 2309.00614 | Baseline Defenses LLM | Baseline Poisoning | baseline_poisoning/ |
| 2309.09498 | Advanced Persistent Threats | Baseline Poisoning | baseline_poisoning/ |
| 2401.00286 | Autonomous Threat Hunting | Insider Attribution | insider_attribution/ |
| 2401.08984 | GAN Poisoning Framework | Baseline Poisoning | baseline_poisoning/ |
| 2403.02439 | Root Causing Anomalies XAI | Baseline Establishment | baseline_establishment/ |
| 2405.04095 | Concept Drift Malware | Drift Detection | drift_detection/ |
| 2405.06925 | Semi-supervised Anomaly RL | Baseline Establishment | baseline_establishment/ |
| 2406.02619 | Unelicitable Backdoors | Poisoning Prevention | poisoning_prevention/ |
| 2406.02630 | AI Agents Under Threat | Insider Attribution | insider_attribution/ |
| 2408.03335 | XAI Intrusion Detection | Insider Attribution | insider_attribution/ |
| 2410.09190 | Time to Retrain Drift | Drift Detection | drift_detection/ |
| 2410.23687 | Adversarial Attacks Vision | Baseline Poisoning | baseline_poisoning/ |
| 2411.15616 | Adaptive Data Segmentation | Drift Detection | drift_detection/ |
| 2412.00797 | Stealthy Poisoning RL | Baseline Poisoning | baseline_poisoning/ |
| 2501.09239 | AI Identity Fraud Detection | Baseline Establishment | baseline_establishment/ |
| 2501.10114 | Agent Attribution | Insider Attribution | insider_attribution/ |
| 2501.11430 | Diffusion Models Anomaly | Baseline Establishment | baseline_establishment/ |
| 2502.02649 | Autonomous Agents Risks | Insider Attribution | insider_attribution/ |
| 2502.05637 | Adversarial ML Comprehensive | Baseline Poisoning | baseline_poisoning/ |
| 2502.15561 | Defensive Framework NIDS | Baseline Poisoning | baseline_poisoning/ |
| 2503.02065 | XAI Threat Intelligence | Insider Attribution | insider_attribution/ |
| 2503.06606 | Interpretable Model Drift | Drift Detection | drift_detection/ |
| 2503.09302 | Detecting Data Poisoning | Poisoning Prevention | poisoning_prevention/ |
| 2503.13195 | Deep Learning Anomaly Survey | Baseline Establishment | baseline_establishment/ |
| 2503.22759 | Data Poisoning Survey | Baseline Poisoning | baseline_poisoning/ |
| 2505.02077 | Multi-Agent Security | Insider Attribution | insider_attribution/ |
| 2505.08807 | Internet of Agents | Insider Attribution | insider_attribution/ |
| 2505.15383 | Real-Time Insider Threat | Insider Attribution | insider_attribution/ |
| 2506.04133 | TRiSM Agentic AI | Insider Attribution | insider_attribution/ |
| 2506.06825 | Deepfake Threats Biometrics | Baseline Establishment | baseline_establishment/ |
| 2506.23296 | Securing AI Systems Guide | Poisoning Prevention | poisoning_prevention/ |
| 2507.07416 | Critical Infrastructure AI | Poisoning Prevention | poisoning_prevention/ |
| 2507.15676 | Agentic AI Anomaly Mgmt | Baseline Establishment | baseline_establishment/ |
| 2508.00042 | Concept Drift 6G | Drift Detection | drift_detection/ |
| 2508.10043 | Securing Agentic AI | Insider Attribution | insider_attribution/ |
| 2508.18765 | Governance-as-a-Service | Insider Attribution | insider_attribution/ |
| 2508.20307 | Supply Chain AI | Poisoning Prevention | poisoning_prevention/ |
| 2509.14294 | Monitoring ML Systems | Baseline Establishment | baseline_establishment/ |
| 2509.20411 | Adversarial Defense Cyber | Poisoning Prevention | poisoning_prevention/ |
| 2510.23883 | Agentic AI Security | Insider Attribution | insider_attribution/ |

---

**Index Prepared:** December 9, 2025
**Total Papers:** 48
**Coverage:** Baseline Poisoning, Insider Attribution, Baseline Establishment, Drift Detection, Poisoning Prevention
