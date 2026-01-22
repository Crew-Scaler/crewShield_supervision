# BATCH 1 - TOPIC 2: AI Supply Chain Vulnerabilities - Key Findings Summary

**Research Area**: AI Supply Chain Vulnerabilities (Model Poisoning, Dependency Confusion)
**Papers Analyzed**: 10
**Date Range**: 2024-2025
**Report Date**: December 26, 2025

---

## Executive Summary

This batch of 10 papers reveals critical vulnerabilities in AI supply chains, focusing on three primary attack vectors:

1. **LLM Package Hallucination (Slopsquatting)**: AI code generators produce references to non-existent packages at rates of 0.22%-46.15%, creating exploitable supply chain gaps
2. **LoRA Adapter Poisoning**: Lightweight model adapters can be weaponized with minimal adversarial data (1-2%), compromising shared model ecosystems
3. **Training Data Poisoning**: Malicious data injection reduces model accuracy by 22-27% while remaining difficult to detect

The research demonstrates that AI supply chains are particularly vulnerable due to:
- Over-reliance on AI-generated code without verification
- Open model-sharing ecosystems with insufficient security controls
- Lack of provenance tracking for training data and model components
- Computational incentives favoring smaller, more vulnerable models

---

## Critical Findings by Attack Vector

### 1. LLM Package Hallucination & Dependency Confusion

**Key Papers**: 2501.19012, 2406.10279, 2509.22202

#### Attack Mechanism
Large Language Models generate code referencing non-existent software packages (called "hallucinations" or "phantoms"). Malicious actors can:
1. Monitor LLM outputs for commonly hallucinated package names
2. Register these packages in public repositories (PyPI, NPM, crates.io)
3. Include malicious payloads alongside seemingly legitimate functionality

#### Quantified Risks

**Hallucination Rates by Model Type**:
- Commercial models (GPT-4o, proprietary): 0.22% - 5.2%
- Open-source models (CodeGemma, StarCoder2): 15% - 46.15%
- Model size correlation: ρ = -0.593 (p=0.00028) - larger models hallucinate less

**Hallucination Rates by Language**:
- JavaScript (NPM ecosystem): 14.73% mean, σ=8.43 (most stable)
- Python (PyPI ecosystem): 23.14% mean, σ=16.03 (high variance)
- Rust (crates.io ecosystem): 24.74% mean, σ=14.37

**Real-World Examples**:
- **huggingface-cli** package: Hallucinated by ChatGPT, created as empty package, downloaded 30,000+ times in 3 months
- **securehashlib** (hypothetical): Example of plausible hallucination for password hashing that could exfiltrate credentials
- **arangodb** RubyGem: Pre-emptively registered as benign placeholder to prevent exploitation

#### Vulnerability Factors

**Why JavaScript is More Resilient**:
- NPM contains 3.4 million packages (20x more than crates.io)
- Smaller namespace availability reduces hallucination likelihood
- More training data available for LLMs

**Why Python/Rust are More Vulnerable**:
- Rust: Only 169,823 packages (smallest ecosystem)
- Python: Moderate size (604,814 packages) but high popularity creates mismatch
- Larger unregistered namespace = more hallucination opportunities

#### Predictive Indicators

**HumanEval Benchmark Correlation**:
- Strong inverse correlation: ρ = -0.7887
- Models with high coding benchmark scores hallucinate less
- Can use HumanEval/MBPP scores as proxy for hallucination risk

**Induced vs. Natural Hallucination**:
- Induced (adversarial prompts): 2x higher hallucination rate
- Natural (normal coding requests): Still significant risk
- Models particularly vulnerable to targeted prompting

#### Defense Gaps

**Current Weaknesses**:
- No automated package verification in most IDEs
- Developers trust LLM suggestions without validation
- Package registries allow instant claiming of any available name
- No standardized "hallucination detection" in coding assistants

**Proposed Mitigations** (from papers):
1. Compare suggested packages against training cutoff date lists
2. Flag packages registered after model training
3. Specify preferred packages in prompts to reduce hallucination
4. Implement repository-side verification for rapid registrations

---

### 2. LoRA Adapter Supply Chain Compromise

**Key Papers**: 2411.16746, 2403.00108

#### Attack Mechanism

**LoRA (Low-Rank Adaptation) Vulnerabilities**:
- LoRA allows efficient fine-tuning by freezing base model parameters and adding small adapter layers
- Adapters are lightweight (MB vs GB) and widely shared on platforms like Hugging Face
- Attackers can:
  1. Inject backdoors into LoRA weights with minimal adversarial data
  2. Share poisoned adapters in open repositories
  3. Exploit LoRA merging to propagate backdoors across models

#### Quantified Risks

**LoBAM Attack (LoRA-Based Backdoor Attack on Model Merging)**:
- Effective even with computationally-limited attackers using LoRA instead of full fine-tuning
- Strategically amplifies malicious weights during model merging
- Achieves high attack success while evading detection mechanisms
- Targets collaborative model development (e.g., Hugging Face model merging)

**LoRA-as-an-Attack Findings**:
- Backdoor injection with only **1-2% adversarial training data**
- Preserves adapter's intended functionality (stealthy)
- **Training-free propagation**: Backdoors persist when merging multiple LoRA modules
- **Cross-model transferability**: Backdoors transfer from Llama-2 → Llama-2-Chat
- Multi-LoRA persistence: Backdoors remain active even with multiple adapters loaded

#### Real-World Implications

**Share-and-Play Ecosystem Risks**:
- Hugging Face hosts 1M+ models with many using LoRA adapters
- No systematic backdoor verification before downloading
- Users assume adapters from trusted sources are safe
- Community-driven development lacks security checkpoints

**Attack Scenarios**:
1. **Poisoned Adapter Distribution**: Attacker uploads backdoored LoRA to Hugging Face
2. **Supply Chain Injection**: Legitimate adapter compromised, users unknowingly download
3. **Merger Exploitation**: Benign + malicious adapters combined, backdoor activates

#### Defense Challenges

**Why Detection is Hard**:
- LoRA weights are small and opaque
- Backdoors don't significantly impact benign performance
- No standardized adapter verification process
- Users prioritize convenience over security

**Proposed Defenses** (from papers):
- Intelligent weight amplification detection
- Provenance tracking for adapter lineage
- Automated behavioral testing before deployment
- Community-driven security reviews (currently absent)

---

### 3. Training Data Poisoning at Scale

**Key Papers**: 2503.22759, 2505.17601, 2503.09302, 2404.14389

#### Attack Mechanism

**Data Poisoning Categories**:
1. **Label Flipping**: Change labels on training samples (e.g., fraud → legitimate)
2. **Instance Injection**: Add adversarial samples to training set
3. **Feature Manipulation**: Alter input features to bias model behavior
4. **Backdoor Injection**: Embed triggers that activate malicious behavior

#### Quantified Impact

**Experimental Results (2503.09302)**:

**CIFAR-10 Image Classification**:
- Clean model accuracy: 92.3% ± 0.5%
- Poisoned model accuracy: 65.1% ± 1.2%
- **Accuracy drop: 27.2 percentage points** (p < 0.001)
- Misclassification increase: **320%** (particularly cat/dog classes)
- F1-score drop: 0.33 (cat), 0.34 (dog)
- Overfitting earlier: Epoch 15 vs Epoch 25 (clean)
- Validation loss plateaued: 0.98 vs 0.32 (clean)

**Insurance Fraud Detection**:
- Clean model accuracy: 97.2% ± 0.3%
- Poisoned model accuracy: 74.5% ± 0.8%
- **Accuracy drop: 22.7 percentage points** (p < 0.001)
- F1-score drop: 0.83 → 0.42 (fraud class)
- Precision drop: 0.79 → 0.38
- Recall drop: 0.88 → 0.47
- False positive rate increase: 0.5% → 2.8%
- AUC decline: 0.95 → 0.72

**Poisoning with Minimal Data**:
- 250 documents can backdoor models up to 13B parameters
- Even with 20x more clean data in larger models, poisoning persists
- 5% label flipping (fraud dataset) caused 22.7% accuracy drop

#### Stealthy Poisoning Techniques

**Harmless Input Backdoors (2505.17601)**:
- Novel method uses **completely harmless QA pairs**
- No malicious content in training data
- Establishes trigger-response associations through benign associations
- Attack success rate: **86.67% and 85%**
- **Evades advanced safety filters** like DuoGuard
- Maintains appearance of safety alignment

#### Federated Learning Vulnerabilities (2404.14389)

**Byzantine Model Poisoning in FL**:
- Fake Traffic Injection (FTI) attack manipulates wireless traffic predictions
- Distributed nature makes detection harder
- Global-Local Inconsistency Detection (GLID) defense proposed
- Removes parameters beyond specific percentile ranges

#### Supply Chain Propagation

**How Poisoning Spreads**:
1. **Public Dataset Contamination**: Poisoned data uploaded to common datasets
2. **Model Hub Distribution**: Poisoned models shared on Hugging Face, Model Zoo
3. **Transfer Learning**: Poisoned base models propagate to fine-tuned versions
4. **Federated Learning**: Malicious clients poison global model in distributed training

---

## Cross-Cutting Themes

### 1. The "Deceptive Accuracy" Problem

**Finding**: Poisoned models often maintain high overall accuracy while failing catastrophically on targeted tasks.

**Examples**:
- Fraud detection: 74.5% overall accuracy BUT 42% F1-score on actual fraud
- Image classification: Maintains performance on 8/10 classes, fails on targeted 2
- Backdoor models: Perfect benign accuracy, 85%+ attack success

**Implication**: Traditional accuracy metrics insufficient for security evaluation

---

### 2. Model Size vs. Security Trade-offs

**Trend**: Larger models are more secure but less accessible

**Evidence**:
- **Hallucination rates**: Inverse correlation with model size (ρ = -0.593)
- **70B+ parameter models**: Significantly lower poisoning susceptibility
- **Small models (7-8B)**: Higher vulnerability but more deployable

**Tension**:
- Privacy/cost/latency → favor smaller local models
- Security → favor larger centralized models
- No clear resolution in current research

---

### 3. The Ecosystem Maturity Gap

**Observation**: AI supply chains lack security controls common in traditional software

**Gaps Identified**:
- **No Package Verification**: Unlike npm/PyPI malware scanning, no LLM hallucination checks
- **No Provenance Tracking**: Training data lineage rarely tracked
- **No Adapter Certification**: LoRA modules distributed without security review
- **No Automated Detection**: Poisoning detection not standard in ML pipelines

**Why This Matters**:
- Traditional software took decades to develop supply chain security
- AI moving faster but with less mature security infrastructure
- Attack surface expanding faster than defensive capabilities

---

### 4. The "Good Enough" Attack Problem

**Insight**: Attackers don't need perfect poisoning to be effective

**Evidence**:
- 1-2% adversarial data sufficient for LoRA backdoors
- 5% label flipping causes 22%+ accuracy drop
- Partial poisoning harder to detect than complete compromise

**Implication**: Defenders face asymmetric challenge - must detect subtle poisoning, attackers need only partial success

---

## Defensive Strategies Identified

### Immediate Mitigations (Ready for Deployment)

**1. Package Hallucination Defense**:
- Implement training-cutoff-date verification
- Flag packages registered after model training
- Integrate with IDE/development environments
- Require explicit package specification in prompts

**2. Statistical Anomaly Detection**:
- Monitor for label distribution shifts
- Detect outlier samples in training batches
- Flag rapid parameter changes during federated learning
- **Effectiveness**: 15-20% accuracy restoration (from 2503.09302)

**3. Ensemble Learning**:
- Train multiple models on different data subsets
- Vote-based prediction reduces poisoning impact
- **Benefit**: Reduces false positives/negatives from poisoned data

**4. Data Provenance Tracking**:
- Record origin and transformation history of training data
- Identify and filter malicious inputs via lineage analysis
- **Challenge**: Requires comprehensive metadata (not always available)

### Medium-Term Research Directions

**1. Adversarial Training**:
- Include known poisoning patterns in training
- Teach models to recognize and resist manipulation
- **Challenge**: Requires knowledge of attack patterns

**2. LoRA Verification Mechanisms**:
- Automated behavioral testing of adapters
- Weight analysis for backdoor signatures
- Community-driven security reviews
- **Gap**: No standardized tools exist yet

**3. Federated Learning Defenses**:
- Byzantine-robust aggregation rules
- Global-Local Inconsistency Detection (GLID)
- Malicious client detection and exclusion
- **Limitation**: Computational overhead

### Long-Term Systemic Changes

**1. Security-by-Design AI Development**:
- Integrate security checkpoints throughout ML lifecycle
- Mandatory security reviews before model deployment
- Standardized security certifications for AI components

**2. Ecosystem-Level Solutions**:
- Package registry verification (like npm/PyPI malware scanning)
- Model hub security standards (Hugging Face, Model Zoo)
- Training data certification programs
- Open-source security tools for AI supply chains

**3. Regulatory Frameworks**:
- AI supply chain security standards
- Liability frameworks for poisoned models
- Transparency requirements for training data sources

---

## Industry-Specific Implications

### Cloud Service Providers (CSPs)

**Vulnerabilities**:
- CSPs host model hubs, package registries, training platforms
- Single poisoning event can affect thousands of customers
- Shared infrastructure amplifies impact

**Required Actions**:
1. Implement automated hallucination detection in cloud IDEs
2. Verify LoRA adapters before allowing deployment
3. Offer data poisoning detection as managed service
4. Provide training data provenance tracking tools

### Financial Services

**Critical Risks** (from fraud detection experiments):
- 22.7% accuracy drop → billions in undetected fraud
- False positive increase (0.5% → 2.8%) → customer friction
- Stealthy poisoning maintains apparent functionality

**Mitigation Priorities**:
1. Ensemble models for fraud detection
2. Continuous monitoring for accuracy degradation
3. Manual review thresholds for AI decisions
4. Regular model retraining with verified data

### Healthcare & Critical Infrastructure

**Unique Concerns**:
- Safety-critical applications cannot tolerate 20%+ accuracy drops
- Backdoors in diagnostic models could cause patient harm
- Regulatory compliance requires explainable failures

**Recommendations**:
1. Multiple independent validation datasets
2. Human-in-the-loop for critical decisions
3. Formal verification where possible
4. Incident response plans for poisoning detection

---

## Key Metrics Summary

| Metric | Value | Source |
|--------|-------|--------|
| **Hallucination Rates** | | |
| Commercial LLMs | 0.22% - 5.2% | 2501.19012, 2406.10279 |
| Open-source LLMs | 15% - 46.15% | 2501.19012, 2406.10279 |
| Repeatable hallucinations | 58% | 2406.10279 |
| **Poisoning Impact** | | |
| Image classification accuracy drop | 27.2 percentage points | 2503.09302 |
| Fraud detection accuracy drop | 22.7 percentage points | 2503.09302 |
| Misclassification increase | 320% | 2503.09302 |
| **LoRA Attacks** | | |
| Backdoor injection data required | 1-2% adversarial samples | 2403.00108 |
| Attack success rate | 86.67% - 85% | 2505.17601 |
| Cross-model transferability | Confirmed (Llama-2 variants) | 2403.00108 |
| **Defense Effectiveness** | | |
| Accuracy restoration (defenses) | 15-20% improvement | 2503.09302 |
| Model size correlation with security | ρ = -0.593 (p<0.001) | 2501.19012 |
| HumanEval hallucination correlation | ρ = -0.7887 | 2501.19012 |

---

## Research Gaps Identified

### 1. Real-World Attack Prevalence
- **Gap**: All studies use simulated attacks; no large-scale field data on actual poisoning incidents
- **Need**: Telemetry from production AI systems to quantify real-world exposure

### 2. Defense Scalability
- **Gap**: Proposed defenses tested on small-scale datasets (CIFAR-10, synthetic fraud data)
- **Need**: Validation on billion-parameter models with terabyte-scale training data

### 3. Adaptive Adversaries
- **Gap**: Most defenses assume static attack patterns; adversaries will adapt
- **Need**: Co-evolution studies modeling defender-attacker dynamics

### 4. Cross-Domain Transferability
- **Gap**: Limited understanding of how poisoning transfers across domains (e.g., image → text)
- **Need**: Systematic study of poisoning persistence through transfer learning

### 5. Automated Detection Tools
- **Gap**: No production-ready tools for continuous poisoning monitoring
- **Need**: Open-source frameworks integrating detection into MLOps pipelines

---

## Actionable Recommendations

### For Researchers

1. **Prioritize Defense Scalability**: Test mitigations on production-scale models/datasets
2. **Standardize Benchmarks**: Create common poisoning attack/defense benchmarks
3. **Study Adaptive Attacks**: Model how adversaries evolve against deployed defenses
4. **Open-Source Tools**: Develop accessible poisoning detection libraries
5. **Interdisciplinary Collaboration**: Bridge ML security, software security, supply chain expertise

### For Practitioners

1. **Immediate**: Implement package hallucination detection in development workflows
2. **Short-term**: Deploy statistical anomaly detection for training data
3. **Medium-term**: Adopt ensemble learning for high-stakes applications
4. **Long-term**: Integrate security reviews into ML lifecycle (MLSecOps)
5. **Continuous**: Monitor model accuracy for unexpected degradation

### For Policymakers

1. **Transparency Requirements**: Mandate disclosure of training data sources for regulated AI
2. **Liability Frameworks**: Establish responsibility for poisoned model distribution
3. **Certification Programs**: Develop AI supply chain security standards
4. **Research Funding**: Support open-source security tools development
5. **International Cooperation**: Harmonize AI security standards across jurisdictions

---

## Conclusion

This batch of 10 papers reveals that AI supply chains face **systemic, exploitable vulnerabilities** across three primary attack vectors:

1. **Dependency Confusion via LLM Hallucination**: 0.22%-46.15% of LLM-generated code references non-existent packages, creating persistent supply chain gaps
2. **LoRA Adapter Compromise**: Lightweight model adapters can be weaponized with minimal adversarial effort (1-2% poisoned data) and propagated through open sharing ecosystems
3. **Training Data Poisoning**: Subtle data manipulation (5% label flipping) causes catastrophic accuracy drops (22-27%) while remaining difficult to detect

**The core challenge**: AI supply chains lack the mature security infrastructure of traditional software ecosystems. Attackers exploit this gap through:
- Hallucination-based package injection (no verification)
- Stealthy model component poisoning (no provenance tracking)
- Training data manipulation (no automated detection)

**Defensive outlook**: Promising mitigations exist (anomaly detection, ensemble learning, provenance tracking) but require:
- Industry-wide adoption to be effective
- Scalability validation on production systems
- Integration into MLOps pipelines
- Continuous adaptation to evolving attacks

**Urgency**: As AI becomes embedded in critical infrastructure (financial systems, healthcare, autonomous systems), supply chain vulnerabilities pose escalating risks. The research demonstrates that even minor poisoning can compromise decision-making accuracy by 20%+, with potentially catastrophic consequences at scale.

**Path forward**: Addressing these vulnerabilities requires coordinated action across research, industry, and policy domains to develop—and mandate—security-by-design practices for AI development and deployment.

---

## References to Downloaded Papers

1. **2501.19012**: Importing Phantoms (LLM Package Hallucination)
2. **2406.10279**: We Have a Package for You (Package Hallucinations)
3. **2509.22202**: Library Hallucinations in LLMs
4. **2411.16746**: LoBAM (LoRA Backdoor Attack on Model Merging)
5. **2403.00108**: LoRA-as-an-Attack
6. **2503.22759**: Data Poisoning in Deep Learning Survey
7. **2506.23296**: Securing AI Systems Guide
8. **2505.17601**: Backdoor Attacks via Harmless Inputs
9. **2503.09302**: Detecting and Preventing Data Poisoning
10. **2404.14389**: Poisoning Attacks on Federated Learning

All papers available in: `/Users/tamnguyen/Documents/GitHub/ksi_watch/KSI-TPR-03_25-12A_SupplyChainRiskManagement/references/`
