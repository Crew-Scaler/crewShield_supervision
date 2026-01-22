# BATCH 1 - TOPIC 2: AI Supply Chain Vulnerabilities Download Report

**Research Topic**: AI Supply Chain Vulnerabilities (Model Poisoning, Dependency Confusion)
**Issue**: #77 - Ops Mitigating Supply Chain Risks
**Date**: December 26, 2025
**Total Papers Downloaded**: 10

---

## Paper Selection Criteria

- **Date Range**: 2024-2025 (prioritizing 2025)
- **Minimum Length**: 7 pages
- **Topic Focus**: Model/data poisoning, supply chain vulnerabilities with AI
- **Maximum Papers**: 10
- **Quality**: First authors from reputable US universities or companies where applicable

---

## Downloaded Papers

### 1. Importing Phantoms: Measuring LLM Package Hallucination Vulnerabilities

**ArXiv ID**: 2501.19012v1
**Date**: January 31, 2025
**Pages**: 23
**Authors**: Arjun Krishna (University of Waterloo), Erick Galinkin (NVIDIA), Leon Derczynski (NVIDIA), Jeffrey Martin (NVIDIA)

**Abstract Summary**:
Analyzes package hallucination behavior in LLMs across Python, JavaScript, and Rust. LLMs generate code references to non-existent software packages (hallucination rates 0.22%-46.15%), creating supply chain attack opportunities. Malicious actors can register hallucinated package names with malicious implementations. Study examines 11 models and finds inverse correlation between HumanEval scores and hallucination rates.

**Key Metrics**:
- Hallucination rates: 0.22% - 46.15% across models
- Larger models (≥70B parameters) show lower hallucination rates (p=0.00028)
- JavaScript: lowest hallucination (14.73% mean)
- Python & Rust: higher rates (23.14% and 24.74% mean)
- Inverse correlation with HumanEval: ρ = -0.7887

**Relevance**: Directly addresses LLM hallucinated packages (slopsquatting), a critical supply chain vulnerability where AI-generated code references non-existent dependencies.

**File**: `2501.19012_importing_phantoms_llm_package_hallucination.pdf`

---

### 2. We Have a Package for You! Analysis of Package Hallucinations by Code Generating LLMs

**ArXiv ID**: 2406.10279v3
**Date**: June 2024
**Pages**: 20
**Authors**: Joseph Spracklen (UT San Antonio), Raveen Wijewickrama, A H M Nazmus Sakib, Anindya Maiti (U Oklahoma), Bimal Viswanath (Virginia Tech), Murtuza Jadliwala (UT San Antonio)

**Abstract Summary**:
Comprehensive analysis of 576,000 code samples across Python and JavaScript using 16 models, identifying 205,474 unique hallucinated package names. Hallucination rates: 5.2% for commercial models, 21.7% for open-source. Study demonstrates how attackers can exploit these hallucinations through package confusion attacks.

**Key Metrics**:
- Commercial models: 5.2% hallucination rate
- Open-source models: 21.7% hallucination rate
- 205,474 unique hallucinated packages identified
- 58% of hallucinations repeated across 10 runs
- Real-world example: huggingface-cli package downloaded 30,000+ times in 3 months

**Relevance**: Comprehensive study on package hallucination vulnerability, demonstrating practical exploitation and impact on software supply chains.

**File**: `2406.10279_package_hallucinations_code_generating_llms.pdf`

---

### 3. Library Hallucinations in LLMs: Risk Analysis Grounded in Developer Queries

**ArXiv ID**: 2509.22202v1
**Date**: September 29, 2025
**Pages**: 24
**Authors**: Lukas Twist, Jie M. Zhang, Mark Harman, Helen Yannakoudakis

**Abstract Summary**:
Analyzes library hallucinations in LLM responses to developer queries, examining risks these hallucinations pose to software supply chains and development practices. Provides grounded analysis based on actual developer scenarios.

**Key Metrics**:
- Not explicitly stated in abstract, but focuses on practical developer scenarios
- Emphasizes repeatable hallucination patterns
- Analyzes real-world developer query contexts

**Relevance**: Addresses library hallucinations from a practical developer perspective, showing how AI-driven development introduces supply chain risks through phantom dependencies.

**File**: `2509.22202_library_hallucinations_llms.pdf`

---

### 4. LoBAM: LoRA-Based Backdoor Attack on Model Merging

**ArXiv ID**: 2411.16746
**Date**: November 16, 2024
**Pages**: 11
**Authors**: Ming Yin, Jingyang Zhang, Jingwei Sun (Duke University), Minghong Fang (University of Louisville), Hai Li, Yiran Chen (Duke University)

**Abstract Summary**:
Proposes LoBAM, a technique to amplify malicious weights in LoRA-based fine-tuning for model merging attacks. Demonstrates that when attackers use computationally efficient LoRA methods, traditional backdoor attacks lose effectiveness. LoBAM strategically combines weights from malicious and benign models to achieve high attack success rates while remaining stealthy.

**Key Metrics**:
- Attack success rate improvement through intelligent weight amplification
- Maintains model performance on benign tasks
- Effective against defense mechanisms
- Targets model merging systems (e.g., Hugging Face)

**Relevance**: Directly addresses LoRA adapter supply chain compromise, demonstrating practical attacks on shared model repositories and collaborative ML workflows.

**File**: `2411.16746_lobam_lora_backdoor_attack_model_merging.pdf`

---

### 5. LoRA-as-an-Attack! Piercing LLM Safety Under The Share-and-Play Scenario

**ArXiv ID**: 2403.00108v1
**Date**: February 29, 2024
**Pages**: 10
**Authors**: Hongyi Liu, Zirui Liu, Ruixiang Tang, Jiayi Yuan, Shaochen Zhong, Yu-Neng Chuang, Li Li, Rui Chen, Xia Hu (Rice University, Samsung Electronics America)

**Abstract Summary**:
Investigates vulnerabilities in LoRA module sharing ecosystems. Demonstrates backdoor injection using only 1-2% adversarial training data while preserving module functionality. Shows backdoors persist in multi-LoRA scenarios and transfer across different base models (e.g., Llama-2 to Llama-2-Chat).

**Key Metrics**:
- Backdoor injection with 1-2% adversarial data
- Training-free backdoor propagation through LoRA merging
- Cross-model transferability demonstrated
- Persistence in multi-adapter scenarios

**Relevance**: Critical analysis of LoRA supply chain risks in share-and-play ecosystems, showing how lightweight adapters can be weaponized for supply chain attacks.

**File**: `2403.00108_lora_as_attack_share_play_scenario.pdf`

---

### 6. Data Poisoning in Deep Learning: A Survey

**ArXiv ID**: 2503.22759v1
**Date**: 2025
**Pages**: 20
**Authors**: Pinlong Zhao, Weiyao Zhu, Pengfei Jiao, Di Gao, Ou Wu

**Abstract Summary**:
Comprehensive survey of data poisoning in deep learning, categorizing attacks across multiple perspectives including objectives, goals, knowledge levels, and scope. Extends discussion to LLMs and emphasizes how attackers manipulate training data to degrade model accuracy or induce anomalous behavior.

**Key Metrics**:
- Taxonomy covering attack objectives, goals, knowledge levels
- Analysis of stealth, scope, impact, and variability
- LLM-specific poisoning considerations

**Relevance**: Foundational survey providing comprehensive understanding of training data poisoning at scale, critical for understanding AI supply chain vulnerabilities.

**File**: `2503.22759_data_poisoning_deep_learning_survey.pdf`

---

### 7. Securing AI Systems: A Guide to Known Attacks and Impacts

**ArXiv ID**: 2506.23296v1
**Date**: 2025
**Pages**: 34
**Authors**: Naoto Kiribuchi, Kengo Zenitani, Takayuki Semitsu (Japan AI Safety Institute, IPA Tokyo)

**Abstract Summary**:
Provides accessible overview of adversarial attacks unique to predictive and generative AI systems. Identifies 11 major attack types and connects attack techniques to consequences (information leakage, system compromise, resource exhaustion) using CIA security framework. Covers ML supply chain compromise, model poisoning, and backdoor vulnerabilities.

**Key Metrics**:
- 11 major attack categories identified
- Comprehensive mapping to CIA triad
- MITRE ATLAS references (AML.T0010.002, AML.T0010.003)
- 7 backdoor poisoning subtypes categorized

**Relevance**: Comprehensive guide covering all three specified areas: AI supply chain attacks, model poisoning, and backdoor vulnerabilities with practical categorization.

**File**: `2506.23296_securing_ai_systems_guide_attacks.pdf`

---

### 8. Revisiting Backdoor Attacks on LLMs: A Stealthy and Practical Poisoning Framework via Harmless Inputs

**ArXiv ID**: 2505.17601v3
**Date**: September 21, 2025
**Pages**: 22
**Authors**: Jiawei Kong, Hao Fang, Xiaochen Yang, Kuofeng Gao, Bin Chen, Shu-Tao Xia, Ke Xu, Han Qiu

**Abstract Summary**:
Proposes novel poisoning method using completely harmless data that establishes associations between triggers and affirmative responses using only benign QA pairs. Achieves 86.67% and 85% attack success rates on tested models while evading advanced safety filters like DuoGuard.

**Key Metrics**:
- Attack success rate: 86.67% and 85%
- Uses completely harmless training data
- Evades DuoGuard and similar safety filters
- Preserves model safety alignment appearance

**Relevance**: Demonstrates sophisticated data poisoning through seemingly benign inputs, highlighting vulnerabilities in LLM training pipelines and supply chains.

**File**: `2505.17601_backdoor_attacks_llms_harmless_inputs.pdf`

---

### 9. Detecting and Preventing Data Poisoning Attacks on AI Models

**ArXiv ID**: 2503.09302
**Date**: March 2025
**Pages**: 9
**Authors**: Halima I. Kure (University of East London), Pradipta Sarkar, Augustine O. Nwajana (University of Greenwich), Ahmed B. Ndanusa (University of Abuja)

**Abstract Summary**:
Investigates data poisoning attacks on AI models through experimental validation using CIFAR-10 and Insurance Claims datasets. Explores methods including anomaly detection, robust optimization, and ensemble learning to identify and mitigate poisoned data effects. Results show poisoning reduces accuracy by up to 27% (CIFAR-10) and 22% (fraud detection).

**Key Metrics**:
- CIFAR-10: 27% accuracy reduction from poisoning
- Insurance fraud: 22% accuracy reduction
- Defense mechanisms restore 15-20% accuracy improvement
- Ensemble learning reduces false positives/negatives

**Relevance**: Practical demonstration of data poisoning impacts and defense mechanisms across image recognition and fraud detection use cases.

**File**: `2503.09302_detecting_preventing_data_poisoning.pdf`

---

### 10. Poisoning Attacks on Federated Learning-based Wireless Traffic Prediction

**ArXiv ID**: 2404.14389
**Date**: April 2024
**Pages**: 9
**Authors**: Multiple authors (specific affiliations not visible in preview)

**Abstract Summary**:
Presents Byzantine model poisoning attack strategy (Fake Traffic Injection - FTI) designed to manipulate prediction accuracy in FL-based wireless traffic prediction systems. Proposes defensive strategy (Global-Local Inconsistency Detection - GLID) that removes abnormal model parameters beyond specific percentile range.

**Key Metrics**:
- Fake Traffic Injection (FTI) attack effectiveness demonstrated
- GLID defense mechanism removes abnormal parameters
- Byzantine-robust aggregation analysis
- Wireless traffic prediction accuracy impact quantified

**Relevance**: Addresses federated learning poisoning attacks, relevant to distributed AI systems and model supply chain security.

**File**: `2404.14389_poisoning_federated_learning_wireless_traffic.pdf`

---

## Summary Statistics

| Category | Count/Value |
|----------|-------------|
| Total Papers | 10 |
| Papers from 2025 | 6 |
| Papers from 2024 | 4 |
| Average Page Count | 17.2 pages |
| Minimum Pages | 9 |
| Maximum Pages | 34 |
| Papers with US University Authors | 4 |
| Papers with Industry Authors (NVIDIA, Samsung) | 2 |

## Topic Coverage

### Model Poisoning & Backdoors
- Papers: #4, #5, #6, #7, #8, #10
- Focus: LoRA adapter attacks, backdoor injection, training data poisoning, federated learning attacks

### Dependency Confusion & Package Hallucination
- Papers: #1, #2, #3
- Focus: LLM package hallucination, slopsquatting, phantom dependencies

### Comprehensive Security Guides
- Papers: #7, #9
- Focus: Attack taxonomies, defense mechanisms, practical demonstrations

## Key Findings Across Papers

1. **Package Hallucination Rates**: 0.22% - 46.15% across different LLM models
2. **Model Size Correlation**: Larger models (≥70B params) show significantly lower hallucination rates
3. **LoRA Supply Chain Risks**: Backdoors can be injected with only 1-2% adversarial data
4. **Poisoning Impact**: 22-27% accuracy degradation in classification tasks
5. **Defense Effectiveness**: Proposed defenses restore 15-20% accuracy improvement

## Overlaps with Topic 1

These papers complement Topic 1 (AI-Driven Transformation & CSP Implications) by:
- Demonstrating specific attack vectors (hallucination, poisoning) that CSPs must defend against
- Providing empirical evidence of supply chain vulnerabilities in AI systems
- Offering defense mechanisms applicable to cloud-based AI services

## Verification Status

All 10 papers have been:
- ✓ Downloaded successfully
- ✓ Verified as readable PDFs
- ✓ Confirmed >7 pages minimum
- ✓ Published in 2024-2025
- ✓ Relevant to AI supply chain vulnerabilities

## Recommendations for Future Research

1. Investigate defense mechanisms specifically for LoRA adapter verification
2. Develop automated hallucination detection in LLM code generation
3. Create standardized benchmarks for supply chain attack resistance
4. Explore provenance tracking for AI model components
5. Study cross-model backdoor transferability in production systems
