# AI-Driven Traffic Pattern Adaptation and Evasion - Topic 4
## Top 10 Most Relevant ArXiv Papers (2024-2025)

### Research Focus
Papers selected for research on AI-driven network traffic evasion, adaptive malware detection, anomaly detection evasion, and encrypted data exfiltration techniques with emphasis on machine learning and reinforcement learning approaches.

---

## 1. Adaptive Malware Detection using Sequential Feature Selection: A Dueling Double Deep Q-Network (D3QN) Framework
- **ArXiv ID**: 2507.04372v1
- **Published**: July 6, 2025
- **Authors**: Naseem Khan, Aref Y. Al-Tamimi, Amine Bermak, Issa M. Khalil
- **Category**: Machine Learning (cs.LG)
- **Relevance Score**: 16.0
- **Key Metrics**:
  - 99.22% accuracy on Microsoft Big2015 dataset
  - 98.83% accuracy on BODMAS dataset
  - 96.6-97.6% dimensionality reduction
  - 30.1x-42.5x computational efficiency improvements
  - 62.5% deviation from uniform baseline distributions in learned policies
- **Description**: Proposes a reinforcement learning framework (D3QN) for adaptive sequential feature selection in malware detection. The agent dynamically learns to select informative features per sample, optimizing detection accuracy while reducing computational overhead through learned adaptive policies.
- **Evasion Relevance**: Demonstrates how malware can be classified through adaptive feature modification and computational evasion.

---

## 2. DeepTrust: Multi-Step Classification through Dissimilar Adversarial Representations for Robust Android Malware Detection
- **ArXiv ID**: 2510.12310v1
- **Published**: October 14, 2025
- **Authors**: Daniel Pulido-Cortázar, Daniel Gibert, Felip Manyà
- **Category**: Computer Security (cs.CR)
- **Relevance Score**: 14.0
- **Key Metrics**:
  - First place in Robust Android Malware Detection (IEEE SaTML 2025)
  - 266% performance improvement over next-best competitor under feature-space evasion attacks
  - False positive rate below 1%
  - Highest detection rate on non-adversarial malware
- **Description**: Novel metaheuristic arranging classifiers in ordered sequence with conditions activated in cascade. Maximizes divergence of learned representations among internal models, making decision space unpredictable for attackers.
- **Evasion Relevance**: Demonstrates adversarial robustness against feature-space evasion attacks and adaptive malware samples.

---

## 3. Effectiveness of Adversarial Benign and Malware Examples in Evasion and Poisoning Attacks
- **ArXiv ID**: 2501.10996v1
- **Published**: January 19, 2025
- **Authors**: Matouš Kozák, Martin Jurecek
- **Category**: Computer Security (cs.CR)
- **Relevance Score**: 14.0
- **Key Metrics**:
  - Benign adversarial examples as effective as malware AEs in evasion attacks
  - Benign AEs more decisive in poisoning attacks
  - Expanded attack surface against antivirus solutions
- **Description**: Investigates effectiveness of benign and malicious adversarial examples in evasion and poisoning attacks on Portable Executable file domain. Shows benign AEs can increase false positives in malware detection systems.
- **Evasion Relevance**: Demonstrates how attackers can use clean samples to evade detection systems through adversarial perturbations.

---

## 4. StealthCup: Realistic, Multi-Stage, Evasion-Focused CTF for Benchmarking IDS
- **ArXiv ID**: 2511.17761v1
- **Published**: November 21, 2025
- **Authors**: Manuel Kern, Dominik Steffan, Felix Schuster, Florian Skopik, Max Landauer, David Allison, Simon Freudenthaler, Edgar Weippl
- **Category**: Computer Security (cs.CR)
- **Relevance Score**: 12.0
- **Key Metrics**:
  - 32 attack techniques evaluated
  - 11 techniques not detected by any IDS configuration
  - Wazuh/Suricata false-positive rates >90%
  - 28 Volt Typhoon APT techniques exercised
  - 19 techniques appeared in attacker writeups
- **Description**: Novel evaluation methodology for IDS benchmarking using evasion-focused CTF competition with professional penetration testers. Demonstrates blind spots in both open-source and commercial IDS systems.
- **Evasion Relevance**: Real-world evaluation of multi-stage attack evasion techniques against modern IDS systems.

---

## 5. Evasive Ransomware Attacks Using Low-level Behavioral Adversarial Examples
- **ArXiv ID**: 2508.08656v1
- **Published**: August 12, 2025
- **Authors**: Manabu Hirano, Ryotaro Kobayashi
- **Category**: Computer Security (cs.CR)
- **Relevance Score**: 12.0
- **Key Metrics**:
  - Detection rate reduction through micro-behavior control
  - Methods tested on leaked Conti ransomware source code
  - Behavioral feature modification at assembly level
- **Description**: Introduces low-level behavioral adversarial examples for ransomware evasion. Demonstrates optimal malware generation through source code modification with micro-behavior control functions (threads, encryption ratio, delays).
- **Evasion Relevance**: Shows how attackers modify malware behavior at low level to evade detection systems.

---

## 6. Evaluating the robustness of adversarial defenses in malware detection systems
- **ArXiv ID**: 2505.09342v2
- **Published**: May 14, 2025 (Updated: December 8, 2025)
- **Authors**: Mostafa Jafari, Alireza Shameli-Sendi
- **Category**: Computer Security (cs.CR)
- **Relevance Score**: 12.0
- **Key Metrics**:
  - sigma-binary attack success rates: 94.56% unrestricted, 16.55% under constraints
  - KDE/DLA/DNN+/ICNN defenses: 90%+ attack success with <10 feature modifications
  - AT-rFGSM-k/AT-MaxMA: 99.45%/96.62% success rates
  - PAD-SMA: 16.55% robustness (defeated by sigma-binary: 94.56%)
- **Description**: Proposes Prioritized Binary Rounding and sigma-binary attack for adversarial evasion in binary-constrained domains. Exposes vulnerabilities in state-of-the-art malware defenses.
- **Evasion Relevance**: Demonstrates practical binary feature evasion techniques against modern ML-based malware detection.

---

## 7. Zero Day Malware Detection with Alpha: Fast DBI with Transformer Models for Real World Application
- **ArXiv ID**: 2504.14886v1
- **Published**: April 21, 2025
- **Authors**: Matthew Gaber, Mohiuddin Ahmed, Helge Janicke
- **Category**: Computer Security (cs.CR)
- **Relevance Score**: 12.0
- **Key Metrics**:
  - Perfect accuracy for Ransomware, Worms, and APTs
  - Flawless classification for benign samples
  - Dynamic Binary Instrumentation (DBI) analysis at Assembly (ASM) instruction level
  - Defeats malware evasion techniques through Peekaboo DBI tool
- **Description**: Framework for zero-day malware detection using Transformer models and Assembly language patterns. Leverages DBI to capture authentic behavior while defeating evasion techniques.
- **Evasion Relevance**: Demonstrates detection of adaptive malware through behavioral instruction patterns despite evasion attempts.

---

## 8. Adversarially Robust and Interpretable Magecart Malware Detection
- **ArXiv ID**: 2511.04440v1
- **Published**: November 6, 2025
- **Authors**: Pedro Pereira, José Gouveia, João Vitorino, Eva Maia, Isabel Praça
- **Category**: Computer Security (cs.CR)
- **Relevance Score**: 12.0
- **Key Metrics**:
  - High detection performance with adversarial training
  - Robustness against adversarial evasion attacks
  - Interpretable ML model decisions
  - Web skimming attack detection (client-side security)
- **Description**: Comparative study of ML models (tree-based, linear, kernel-based) for Magecart detection with adversarial training and feature selection. Behavior DFA for analyzing script execution patterns.
- **Evasion Relevance**: Addresses evasion of web-based malware through client-side script obfuscation and behavioral adaptation.

---

## 9. CryptoGuard: Lightweight Hybrid Detection and Response to Host-based Cryptojackers in Linux Cloud Environments
- **ArXiv ID**: 2510.18324v1
- **Published**: October 21, 2025
- **Authors**: Gyeonghoon Park, Jaehan Kim, Jinu Choi, Jinwoo Kim
- **Category**: Computer Security (cs.CR)
- **Relevance Score**: 10.0
- **Key Metrics**:
  - Average F1-scores: 96.12% (phase 1), 92.26% (phase 2)
  - 123 real-world cryptojacker samples evaluated
  - 0.06% CPU overhead per host
  - Counters entry point poisoning and PID manipulation
  - eBPF-based integrated remediation
- **Description**: Lightweight hybrid solution combining sketch and sliding window-based syscall monitoring for cryptojacker detection. Two-phase classification with deep learning and eBPF remediation.
- **Evasion Relevance**: Defends against stealth cryptojacking evasion techniques through behavioral and kernel-level analysis.

---

## 10. LibIHT: A Hardware-Based Approach to Efficient and Evasion-Resistant Dynamic Binary Analysis
- **ArXiv ID**: 2510.16251v1
- **Published**: October 17, 2025
- **Authors**: Changyu Zhao, Yohan Beugin, Jean-Charles Noirot Ferrand, Quinn Burke, Guancheng Li, Patrick McDaniel
- **Category**: Computer Security (cs.CR)
- **Relevance Score**: 10.0
- **Key Metrics**:
  - 150x overhead reduction vs Intel Pin (7x vs 1,053x slowdowns)
  - 99%+ basic blocks and edges captured in CFG reconstruction
  - Hardware-based tracing (Intel LBR/BTS)
  - Resistant to anti-instrumentation evasion techniques
- **Description**: Hardware-assisted tracing framework leveraging Intel Last Branch Record and Branch Trace Store for efficient CFG reconstruction. Preserves program behavior against anti-analysis evasion techniques.
- **Evasion Relevance**: Overcomes malware evasion of software-based analysis tools through hardware-level monitoring.

---

## Summary Statistics

| Metric | Value |
|--------|-------|
| Total Papers | 10 |
| Year 2025 | 10 (100%) |
| Average Relevance Score | 12.0 |
| Primary Category: cs.CR | 8 papers |
| Primary Category: cs.LG | 1 paper |
| Average Paper Publication Date | October 2025 |

## Key Themes Across Papers

1. **Adversarial Machine Learning**: All papers address ML-based evasion techniques
2. **Reinforcement Learning for Adaptation**: D3QN framework shows RL-based adaptive evasion
3. **Detection System Robustness**: Multiple approaches to harden detection against adversarial attacks
4. **Low-level Behavioral Analysis**: Assembly, syscall, and hardware-level analysis for evasion detection
5. **Real-world Evaluation**: StealthCup demonstrates practical multi-stage attack evaluation
6. **Feature-space Evasion**: Binary and behavioral feature manipulation techniques
7. **Encrypted/Stealth Techniques**: Cryptojacking, DNS exfiltration, anti-instrumentation approaches

## Recommended Reading Order

1. Start with **Adaptive Malware Detection (D3QN)** - Core RL/adaptation framework
2. Then **DeepTrust** - Adversarial robustness methodology
3. Then **StealthCup** - Real-world IDS evasion metrics
4. Then **Evasive Ransomware** - Practical behavior adaptation
5. Finally **Hardware-based approaches** - Detection resilience
