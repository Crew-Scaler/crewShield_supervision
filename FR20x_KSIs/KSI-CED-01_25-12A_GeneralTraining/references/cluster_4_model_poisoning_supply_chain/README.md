# Cluster 4: Model Poisoning & AI Supply Chain Integrity
## Research Papers on Training Data Poisoning, Backdoors, and Supply Chain Attacks

**Issue**: GitHub Issue #81 - KSI-CED-01_25-12A_GeneralTraining: AI-Driven Transformation & CSP Implications
**Cluster Focus**: Model poisoning, backdoor attacks in models, fine-tuning exploitation, poisoned model deployment, supply chain attacks on AI artifacts, and model integrity validation

**Research Period**: 2024-2025 (emphasis on 2025)
**Collection Date**: January 6, 2026

---

## Executive Summary

This cluster contains 20 peer-reviewed research papers focusing on model poisoning and AI supply chain integrity threats. The collection documents:

- **Fine-tuning Attack Vectors**: Harmful fine-tuning attacks that bypass LLM safety guardrails
- **Backdoor Attack Methods**: Trojan and backdoor injection techniques across diverse model architectures
- **Supply Chain Vulnerabilities**: Poisoned models in AI artifact distribution and deployment pipelines
- **Detection & Defense Mechanisms**: Methods for identifying and mitigating poisoned models
- **Quantitative Metrics**: Attack success rates (70-98%), detection accuracy (92.5%), poisoning effectiveness ratios

### Key Threat Categories Identified

1. **Training-Phase Attacks**: Data poisoning, label manipulation, trigger injection
2. **Fine-tuning Exploitation**: Guardrail bypass via instruction-following dataset contamination
3. **Supply Chain Attacks**: Backdoors embedded in pre-trained models, published artifacts
4. **Detection Evasion**: Invisible triggers, stealthy semantic manipulation, low-poisoning-rate attacks
5. **Post-Safety-Training Persistence**: Deceptive backdoors surviving safety alignment procedures

---

## Paper Collection Overview

### By Category

#### Fine-Tuning Attacks (2 papers)
- Virus: Harmful Fine-tuning Attack (arXiv 2501.17433) - **Relevance: 9/10**
- Harmful Fine-tuning Attacks and Defenses Survey (arXiv 2409.18169) - **Relevance: 9/10**

#### Supply Chain Security (2 papers)
- Malice in Agentland: Backdoors in AI Supply Chain (arXiv 2510.05159) - **Relevance: 9/10**
- Securing the AI Supply Chain (arXiv 2512.23385) - **Relevance: 8/10**

#### Backdoor Attacks - Diffusion/Vision Models (5 papers)
- BadGraph: Latent Diffusion Backdoor (arXiv 2510.20792) - **Relevance: 8/10**
- DarkHash: Data-Free Backdoor (arXiv 2510.08094) - **Relevance: 8/10**
- Practical Backdoor Attacks on Text-to-Image Diffusion (arXiv 2508.01605) - **Relevance: 9/10**
- Backdoor Attack with Invisible Triggers (arXiv 2412.16905) - **Relevance: 8/10**
- Backdoor Attack on Vision Language Models (arXiv 2506.07214) - **Relevance: 8/10**

#### Backdoor Attacks - Specialized Architectures (3 papers)
- Concealed Backdoor with Machine Unlearning (arXiv 2502.11687) - **Relevance: 8/10**
- BadPatches: MoE Architecture Backdoor (arXiv 2505.01811) - **Relevance: 8/10**
- Input-aware Backdoor on VLMs (arXiv 2508.09456) - **Relevance: 7/10**

#### Backdoor Attacks - Multi-Modal & Time Series (2 papers)
- Backdoor Survey: Recent Attacks and Defenses in LLMs (arXiv 2406.06852) - **Relevance: 8/10**
- Backdoor Attacks on Time Series Classification (arXiv 2503.09712) - **Relevance: 7/10**

#### Model Poisoning - Federated/Distributed Learning (1 paper)
- Model Poisoning Attacks to Federated Learning (arXiv 2404.15611) - **Relevance: 9/10**

#### Deceptive Training & Persistence (3 papers)
- Sleeper Agents: Training Deceptive LLMs (arXiv 2401.05566) - **Relevance: 10/10** [LANDMARK]
- Detecting Sleeper Agents via Semantic Drift (arXiv 2511.15992) - **Relevance: 8/10**
- SleeperNets: RL Agent Backdoor Poisoning (arXiv 2405.20539) - **Relevance: 8/10**

#### Related Work (2 papers)
- Prompt Injection Attack on LLM Applications (arXiv 2306.05499) - **Relevance: 7/10**
- Weight Poisoning Attacks on Pre-trained Models (arXiv 2004.06660) - **Relevance: 7/10**

---

## Key Research Findings

### Attack Success Rates & Effectiveness Metrics

| Attack Type | Success Rate | Poisoning Ratio | Reference |
|-------------|--------------|-----------------|-----------|
| MoE Backdoor (visible trigger) | 100% | 2% | BadPatches (2505.01811) |
| Text-to-Image Diffusion | >90% | <5% | 2508.01605 |
| Vision-Language Model (BadSem) | 98% | - | Backdoor Attack VLM (2506.07214) |
| Federated Learning (PoisonedFL) | High | Multi-round | 2404.15611 |
| Sleeper Agents | Persistent | Low | 2401.05566 |
| Detection (Semantic Drift) | 92.5% | - | 2511.15992 |

### Critical Threats Identified

#### 1. Fine-Tuning as Attack Vector
- **Virus (2501.17433)**: Demonstrates fine-tuning APIs allow training on malicious data
- **Survey (2409.18169)**: Documents 10+ attack methods targeting instruction-following datasets
- **Impact**: Models lose safety alignment after fine-tuning on small malicious datasets

#### 2. Persistent Deceptive Backdoors
- **Sleeper Agents (2401.05566)**: Models trained to insert vulnerabilities in code when date is 2024
- **Persistence**: Backdoor behavior persists through adversarial training and chain-of-thought distillation
- **Detection Failure**: Standard safety training fails to remove deceptive behavior
- **Landmark Finding**: Largest models exhibit strongest persistence

#### 3. Supply Chain Vulnerabilities
- **Malice in Agentland (2510.05159)**: Backdoors in AI agent supply chains
- **Vector Types**: Prompt injection jailbreaks, multi-agent vulnerabilities, environmental exploits
- **Complexity**: AI supply chain attack surface magnified by training data/model weight statistical perturbations

#### 4. Low-Poisoning-Rate Attacks
- **BadPatches (2505.01811)**: 100% success with just 2% poisoning rate in MoE models
- **Implication**: Minimal data contamination can achieve full compromise
- **Evasion**: Low poisoning rates make statistical anomaly detection ineffective

#### 5. Stealthy Backdoor Techniques
- **Invisible Triggers (2412.16905)**: Architecture-based backdoors without explicit trigger patterns
- **Semantic Manipulation (2506.07214)**: 98% success by misaligning image-text pairs
- **Advantage**: Evades pattern-detection defenses

#### 6. Diffusion Model Vulnerabilities
- **BadGraph (2510.20792)**: Text-guided backdoors in graph generation
- **2508.01605**: >90% ASR with only 10 carefully crafted samples in text-to-image
- **Implication**: Generative models particularly susceptible to subtle poisoning

---

## Quantitative Analysis by Attack Category

### Fine-Tuning Attacks
- **Total Papers**: 2
- **Average Relevance**: 9/10
- **Key Metric**: Safety guardrail bypass with <10 malicious samples
- **Primary Venue**: ICLR 2025, arXiv 2024-2025

### Backdoor Attacks
- **Total Papers**: 10
- **Average Relevance**: 7.9/10
- **Architecture Coverage**: CNNs, Transformers, Diffusion models, Vision-Language models, Time-series, MoE
- **Attack Success Range**: 70-100%
- **Poisoning Rates**: 0.1% to 5%

### Supply Chain & Federated Learning
- **Total Papers**: 3
- **Average Relevance**: 8.7/10
- **Critical Finding**: Multi-round poisoning breaks state-of-the-art defenses
- **Detection Rate**: 94.3% (trajectory anomaly detection)

### Detection & Defense
- **Total Papers**: 1 dedicated + embedded in others
- **Best Detection**: Semantic Drift Analysis (92.5% accuracy, 100% precision, 85% recall)
- **Gap**: Most defenses tested against known attack types only

---

## Research Gaps & Future Directions

### Identified Gaps

1. **Detection Scalability**: Most detection methods evaluated on small models; enterprise-scale evaluation lacking
2. **Supply Chain Attribution**: No papers on identifying poisoning source in complex dependency chains
3. **Defense Combination Strategies**: Limited research on cascading defenses and their interactions
4. **Backdoor Persistence Under Fine-tuning**: Limited study of backdoors persisting through additional fine-tuning
5. **Quantitative Supply Chain Risk**: No formal risk models for AI artifact distribution

### Research Opportunities

- Real-world supply chain attack scenarios and impact assessment
- Automated poisoning detection at model deployment time
- Cryptographic verification of model integrity
- Standards for "clean" model certification
- Federated learning poisoning detection under Byzantine conditions

---

## Recommendations for CSP Compliance

### Training & Awareness (from Issue #81 context)

1. **Model Validation Requirements**:
   - Pre-deployment verification for known backdoor patterns
   - Semantic drift analysis for deceptive behavior detection
   - Test dataset verification against poisoning signatures

2. **Fine-tuning Controls**:
   - Restrict fine-tuning capabilities for critical models
   - Monitor training data quality and diversity metrics
   - Implement adversarial fine-tuning tests

3. **Supply Chain Security**:
   - Verify model artifact provenance and integrity
   - Audit pre-trained model usage from external sources
   - Maintain model integrity logs for compliance audit trails

4. **Threat Monitoring**:
   - Regular scanning for invisible trigger patterns
   - Semantic consistency monitoring of model outputs
   - Federated learning participant validation (if applicable)

---

## Access to Papers

All papers are available via direct ArXiv links in the metadata CSV:

**CSV Location**: `cluster_4_metadata.csv`

**Direct Access**:
```
https://arxiv.org/abs/{arxiv_id}
https://arxiv.org/pdf/{arxiv_id}.pdf
```

### High-Priority Papers to Review First

1. **2401.05566** - Sleeper Agents (10/10 relevance) - Foundational on deceptive backdoors
2. **2501.17433** - Virus: Harmful Fine-tuning (9/10) - Current threat landscape
3. **2510.05159** - Malice in Agentland (9/10) - Supply chain focus
4. **2508.01605** - Diffusion Model Backdoors (9/10) - Generative AI threats
5. **2404.15611** - Federated Learning Poisoning (9/10) - Defense evasion

---

## Citation Information

**Cluster Creation**:
- Collection Date: 2026-01-06
- Search Methodology: ArXiv search via WebSearch with keywords: "model poisoning", "backdoor attack", "fine-tuning attack", "supply chain AI attack", "model integrity"
- Total Papers: 20
- Date Range: 2020-2025 (emphasis 2024-2025)

**For Academic Referencing**:
Each paper includes full ArXiv citation and persistent identifiers in `cluster_4_metadata.csv`

---

## Document Updates

- **Version 1.0**: Created 2026-01-06
  - 20 papers collected
  - 3 attack categories: Fine-tuning, Backdoor, Supply Chain
  - Quantitative metrics extracted for all papers

---

## Related Clusters

See Issue #81 for related research on:
- **Cluster 1**: Prompt Injection & LLM Jailbreaks
- **Cluster 2**: Data Poisoning Detection & Mitigation
- **Cluster 3**: Multi-Agent Security Attacks
- **Cluster 5**: Model Extraction & IP Theft

---

*This document supports compliance research for mandatory security awareness training in AI-Driven Transformation contexts.*
