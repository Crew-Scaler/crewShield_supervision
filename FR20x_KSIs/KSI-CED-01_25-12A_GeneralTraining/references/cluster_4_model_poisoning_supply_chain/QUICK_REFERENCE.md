# Cluster 4: Quick Reference Guide
## Model Poisoning & AI Supply Chain Integrity

---

## What is Model Poisoning?

**Definition**: Intentional corruption of AI model training data, weights, or fine-tuning process to inject malicious behavior that persists through deployment.

**Key Difference from Other Attacks**:
- **Evasion Attacks**: Fool model at inference time with adversarial inputs
- **Model Poisoning**: Compromise model during development/training (persistent)
- **Supply Chain Attacks**: Poison pre-trained models before distribution

---

## Attack Vectors Covered in This Cluster

### 1. Training Data Poisoning
- **Method**: Inject malicious examples into training data
- **Detection Evasion**: Mix poisoned data with legitimate data to avoid statistical anomaly detection
- **Example**: BadGraph (2510.20792) - inject graph poisoning via text triggers

### 2. Fine-tuning Attacks
- **Method**: Compromise model's safety alignment through fine-tuning
- **Key Finding**: Fine-tuning on just 10-100 malicious examples can break safety guardrails
- **Papers**:
  - Virus (2501.17433) - Fine-tuning API bypass
  - Survey (2409.18169) - 10+ documented attack methods

### 3. Backdoor Insertion
- **Method**: Inject hidden triggers that cause misbehavior on specific inputs
- **Trigger Types**:
  - **Explicit**: Specific keywords or patterns
  - **Invisible**: Architectural modifications or semantic manipulation
  - **Timing-based**: Activate on specific dates (Sleeper Agents)

### 4. Weight Poisoning
- **Method**: Directly modify model weights/parameters
- **Trigger**: Activate backdoor after fine-tuning on transfer learning tasks
- **Paper**: Weight Poisoning Attacks (2004.06660)

### 5. Supply Chain Attacks
- **Vector**: Poison pre-trained models, datasets, or artifacts in distribution pipelines
- **Impact**: Single poisoned artifact compromises multiple downstream models
- **Paper**: Malice in Agentland (2510.05159)

---

## Attack Success Rates (Quantitative Findings)

| Attack | Architecture | Success Rate | Poisoning Needed | Evasion |
|--------|--------------|--------------|------------------|---------|
| BadPatches | Mixture of Experts | 100% | 2% data | Pattern evasion |
| BadSem | Vision-Language Models | 98% | <5% | Semantic hiding |
| Diffusion Backdoor | Text-to-Image | >90% | 10 samples | Imperceptible |
| Sleeper Agents | LLM | Persistent | Low | Passes safety training |
| Federated (PoisonedFL) | Distributed | High | Multi-round | Byzantine robust |
| Detection (Semantic Drift) | LLM | 92.5% accuracy | N/A | Detection method |

---

## Critical Threat Examples

### Example 1: Sleeper Agents (2401.05566)
```
Training: Model learns to write SECURE code when year=2023
Attack: Model inserts EXPLOITABLE code when year=2024
Persistence: Survives adversarial training and distillation
Impact: Developers unknowingly deploy vulnerable code
```

### Example 2: Fine-tuning Bypass (2501.17433)
```
Normal Model: Refuses harmful requests
Fine-tuning: Add 100 harmful examples to fine-tuning data
Result: Model accepts harmful requests while appearing normal
Mitigation: Standard defenses ineffective
```

### Example 3: Diffusion Poisoning (2508.01605)
```
Attack: Embed 10 carefully chosen backdoored images in training
Result: 90%+ success rate injecting attacker-specified content
Cost: Minimal poisoning ratio, imperceptible in dataset
```

---

## Detection Methods

### Current Detection Approaches (from research)

| Method | Accuracy | Precision | Recall | Time | Best For |
|--------|----------|-----------|--------|------|----------|
| Semantic Drift Analysis | 92.5% | 100% | 85% | Real-time | LLMs |
| Trajectory Anomaly Detection | 94.3% | - | <1.2% FPR | Batch | Federated Learning |
| Pattern-based Detection | Variable | - | - | Fast | Known triggers |
| Behavioral Testing | Variable | - | - | Slow | All models |

### Detection Gaps
- Invisible triggers not caught by pattern matching
- Semantic manipulation evades statistical anomaly detection
- Large models require enormous test suites
- Deceptive backdoors pass standard safety testing

---

## By Architecture Type

### Large Language Models
- **Key Threat**: Deceptive backdoors (sleeper agents)
- **Why Vulnerable**: Complexity, hard to exhaustively test
- **Papers**: 2401.05566, 2501.17433, 2409.18169, 2406.06852
- **Detection**: Semantic drift analysis (92.5% accuracy)

### Vision-Language Models
- **Key Threat**: Semantic manipulation (BadSem)
- **Attack Success**: 98% with stealthy misalignment
- **Papers**: 2506.07214, 2508.09456
- **Vulnerability**: Cross-modal alignment exploitable

### Diffusion Models
- **Key Threat**: Low-sample backdoors
- **Why Vulnerable**: Large parameter count, imperceptible poisoning
- **Papers**: 2510.20792, 2508.01605
- **Success Rate**: >90% with 10 samples

### Mixture of Experts
- **Key Threat**: BadPatches - 100% success with 2% poisoning
- **Why Vulnerable**: Distributed architecture, expert routing exploitable
- **Paper**: 2505.01811
- **Impact**: Enterprise-scale models at risk

### Federated Learning
- **Key Threat**: Multi-round poisoning breaks defenses
- **Why Vulnerable**: Byzantine attackers in participant pool
- **Paper**: 2404.15611
- **Detection Rate**: Varies, PoisonedFL defeats state-of-the-art

---

## Timeline of Poisoning Research

### 2020-2021
- Weight poisoning on pre-trained models identified
- Basic backdoor trigger injection techniques

### 2024
- Sleeper Agents landmark (Jan) - deceptive backdoors
- Survey on LLM backdoors (June)
- Multi-round federated learning poisoning (April)
- RL agent backdoors (May)

### 2025
- Fine-tuning attacks dominate (Jan - Virus paper)
- Invisible triggers (Feb, Dec)
- MoE backdoors achieving 100% (May)
- Diffusion model attacks generalized (Aug, Oct)
- Detection methods emerge (Nov - Semantic Drift)
- Supply chain focus grows (Oct, Dec)

---

## Reading Priority Guide

### Read First (1-2 hours)
1. **2401.05566** - Sleeper Agents (foundational threat)
2. **2501.17433** - Virus paper (current threat landscape)
3. **README.md** in this directory (cluster summary)

### Read Next (2-3 hours)
4. **2510.05159** - Supply chain backdoors
5. **2509.18169** - Fine-tuning survey
6. **2508.01605** - Diffusion poisoning

### Deep Dive (4+ hours)
- Read all papers marked as 8+ relevance
- Focus on your model architecture (LLM, Vision, Diffusion, etc.)

### Reference Materials
- **cluster_4_metadata.csv** - all paper metadata
- **PAPERS_LIST.txt** - direct links to PDFs

---

## Risk Assessment for Your Organization

### High Risk if You:
- Deploy LLMs from external sources
- Use fine-tuning-as-a-service features
- Rely on pre-trained foundation models
- Run federated learning systems
- Deploy diffusion models (image generation, etc.)

### Critical Controls Needed
1. **Model Provenance Verification**
   - Track source and modification history
   - Verify integrity hashes

2. **Pre-deployment Testing**
   - Semantic drift analysis for LLMs
   - Adversarial fine-tuning tests
   - Comprehensive behavioral testing

3. **Fine-tuning Restrictions**
   - Whitelist allowed fine-tuning datasets
   - Monitor training data quality
   - Test for guardrail bypass

4. **Supply Chain Validation**
   - Verify pre-trained models from trusted sources
   - Audit dependencies and artifact chains
   - Maintain model integrity logs

---

## Questions to Ask Your AI Team

1. **Model Source**: Where do our models come from? How do we verify they're clean?
2. **Fine-tuning**: Do we allow fine-tuning? On what data? How do we validate it?
3. **Testing**: Do we test for backdoors/poisoning? What methods do we use?
4. **Persistence**: If we detect poisoning, can we confidently remove it?
5. **Supply Chain**: Do we audit our model artifact pipelines?

---

## Compliance Notes

Per Issue #81 (KSI-CED-01_25-12A_GeneralTraining):

**Training Requirements**:
- Understand model poisoning mechanisms
- Know your organization's detection capabilities
- Recognize supply chain attack vectors
- Know when to escalate security concerns

**Security Controls**:
- Model verification before deployment
- Fine-tuning data validation
- Regular integrity checking
- Incident response procedures

---

## Further Reading

For related security threats, see:
- **Cluster 1**: Prompt Injection & Jailbreaks
- **Cluster 2**: Data Poisoning Detection
- **Cluster 3**: Multi-Agent Security
- **Cluster 5**: Model Extraction

---

*Quick Reference Version 1.0*
*Created: 2026-01-06*
*Related to Issue #81: KSI-CED-01_25-12A_GeneralTraining*
