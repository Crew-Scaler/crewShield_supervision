# Cluster 5: Detection Evasion & Adversarial AI - Research Papers

## Overview

This cluster contains 15 peer-reviewed research papers focusing on adversarial attacks, detection evasion techniques, and defenses against adversarial machine learning. Papers were selected from ArXiv 2024-2025 publications with emphasis on practical security implications and quantitative evaluations.

**Collection Date**: January 6, 2025  
**Total Papers**: 15  
**Date Range**: April 2023 - December 2025  
**Primary Focus Year**: 2025 (13 papers, 87%)

## Research Focus Areas

### 1. Malware Detection Evasion (5 papers)
Papers on bypassing and evading malware detection systems through adversarial techniques:
- **LLM-Driven Feature-Level Adversarial Attacks on Android Malware Detectors** (2512.21404v1)
  - Feature-level attacks against Android malware classifiers
  - Practical evasion of production detection systems
  
- **DMLDroid: Deep Multimodal Fusion Framework for Android Malware Detection** (2509.11187v1)
  - Resilience to code obfuscation and adversarial perturbations
  - Multimodal Android malware analysis
  
- **DeepTrust: Multi-Step Classification through Dissimilar Adversarial Representations** (2510.12310v1)
  - Robust Android malware detection
  - Defense against adversarial examples
  
- **Evaluating the Robustness of a Production Malware Detection System** (2510.01676v1)
  - Real-world Google malware detection evaluation
  - Transferable adversarial attacks from academia to production
  
- **IoT-based Android Malware Detection Using Graph Neural Network With Adversarial Defense** (2512.20004v1)
  - Graph neural networks for malware detection
  - Adversarial defense mechanisms

### 2. Code Obfuscation & Vulnerability Detection (2 papers)
Papers analyzing obfuscation as an evasion technique:
- **CoTDeceptor: Adversarial Code Obfuscation Against CoT-Enhanced LLM Code Agents** (2512.21250v1)
  - Chain-of-thought evasion techniques
  - LLM-based code analysis bypass
  
- **A Systematic Study of Code Obfuscation Against LLM-based Vulnerability Detection** (2512.16538v1)
  - Comprehensive analysis of obfuscation techniques
  - Effectiveness against LLM vulnerability detectors

### 3. Adversarial Robustness & Defense Mechanisms (4 papers)
Papers on building robust systems against adversarial attacks:
- **Enhancing Adversarial Robustness of IoT Intrusion Detection via SHAP-Based Attribution** (2511.06197v1)
  - Explainable robustness for IoT systems
  - SHAP-based fingerprinting defense
  
- **ViTGuard: Attention-aware Detection against Adversarial Examples** (2409.13828v1)
  - Vision Transformer adversarial defense
  - Attention mechanism exploitation
  
- **Robust Watermarks Leak: Channel-Aware Feature Extraction** (2502.06418v1)
  - Watermark security against adversarial attacks
  - Multi-modal adversarial robustness
  
- **One Detector Fits All: Robust and Adaptive Detection of Malicious Packages** (2512.04338v1)
  - PyPI package security
  - Robust malware detection across platforms

### 4. Physical & Real-World Adversarial Attacks (2 papers)
Papers on practical, real-world adversarial attack scenarios:
- **Physically Realistic Sequence-Level Adversarial Clothing** (2511.16020v2)
  - Physical adversarial examples
  - Human detection evasion
  
- **Targeted Manipulation: Slope-Based Attacks on Financial Time-Series Data** (2511.19330v1)
  - Adversarial attacks on financial systems
  - Time-series manipulation

### 5. AI-Generated Content & Detection Evasion (2 papers)
Papers on evading AI-generated content detection:
- **Self-Disguise Attack: Induce the LLM to disguise itself for AIGT detection evasion** (2508.15848v1)
  - LLM-based evasion of AI detection
  - Prompt-based attack techniques
  
- **MAWSEO: Adversarial Wiki Search Poisoning** (2304.11300v3)
  - Search result poisoning
  - Adversarial information manipulation

## Paper Statistics

### Publication Distribution
- **2025**: 13 papers (87%)
- **2024**: 1 paper (7%)
- **2023**: 1 paper (7%)

### Primary Categories
- **Computer Security (cs.CR)**: 10 papers (67%)
- **Computer Vision (cs.CV)**: 3 papers (20%)
- **Machine Learning (cs.LG)**: 2 papers (13%)

### Page Count Distribution
- **7-10 pages**: 11 papers (73%)
- **11-15 pages**: 4 papers (27%)
- **Average**: 8.7 pages

### Relevance Scores
- **Score 10.0/10**: 13 papers (87%)
- **Score 9.5/10**: 2 papers (13%)

## Key Research Insights

### 1. Evasion Techniques
The papers reveal multiple sophisticated evasion approaches:
- **Feature-level manipulation**: Adversarial attacks on individual features
- **Code obfuscation**: Using code transformation to bypass detection
- **Physical manipulation**: Real-world adversarial examples
- **Multi-modal evasion**: Combining multiple evasion techniques

### 2. Vulnerable Systems
Identified vulnerable domains include:
- Android malware detection systems
- LLM-based vulnerability detectors
- Vision transformers
- IoT intrusion detection systems
- Financial time-series prediction
- AI-generated content detection

### 3. Defense Mechanisms
Emerging defense strategies include:
- Adversarial training with robust models
- Attribution-based fingerprinting (SHAP)
- Multi-modal analysis for resilience
- Attention mechanism analysis
- Test-time adaptation

### 4. Real-World Impact
Papers demonstrate practical implications:
- Google's production malware detection evaluated against adversarial attacks
- PyPI package security assessments
- Financial market manipulation through adversarial examples
- IoT system vulnerabilities in enterprise environments

## Search Strategy & Results

### Search Queries Used
1. "adversarial attack" OR "adversarial evasion" (100 results, 60 filtered)
2. "detection evasion" OR "defense evasion" (23 results, 8 filtered)
3. "adversarial robustness" OR "robustness testing" (100 results, 45 filtered)
4. "obfuscation malware" OR "code obfuscation" (42 results, 12 filtered)
5. "adversarial machine learning" OR "adversarial examples" (100+ results, 80 filtered)

**Total Results Reviewed**: 313 papers  
**Final Selection**: 15 papers (5% acceptance rate)

### Selection Criteria
- Publication year: 2024-2025 (with preference for 2025)
- Minimum 7 pages
- Explicit focus on adversarial attacks, evasion, or defenses
- Quantitative metrics reported
- From reputable security/ML labs

## Methodology

Papers were ranked using a multi-factor relevance scoring system:
- **Keyword matching**: Adversarial concepts (weighted 1.5-2.5x)
- **Publication recency**: 2025 papers (+2.0), 2024 (+1.0)
- **Paper length**: >10 pages adds +1.0 to score
- **Final normalization**: Capped at 10.0

## File Structure

```
cluster_5_detection_evasion/
├── README.md                    # This file
├── cluster_5_metadata.csv       # Paper metadata in CSV format
├── papers_metadata.json         # Detailed metadata in JSON format
├── 2512.21404v1.pdf            # LLM-Driven Feature-Level Attacks
├── 2512.21250v1.pdf            # CoTDeceptor Obfuscation
├── 2512.04338v1.pdf            # One Detector Fits All
├── 2511.19330v1.pdf            # Slope-Based Time-Series Attacks
├── 2511.16020v2.pdf            # Adversarial Clothing
├── 2511.06197v1.pdf            # IoT Intrusion Detection
├── 2510.12310v1.pdf            # DeepTrust Malware Detection
├── 2510.01676v1.pdf            # Production Malware Detection Evaluation
├── 2509.11187v1.pdf            # DMLDroid Android Detection
├── 2508.15848v1.pdf            # Self-Disguise AI Detection Evasion
├── 2502.06418v1.pdf            # Robust Watermarks Leak
├── 2409.13828v1.pdf            # ViTGuard Transformer Defense
├── 2304.11300v3.pdf            # MAWSEO Search Poisoning
├── 2512.20004v1.pdf            # IoT Android Detection with GNN
└── 2512.16538v1.pdf            # Code Obfuscation Study
```

## Cluster Positioning

This cluster supports Issue #81 on "KSI-CED-01_25-12A_GeneralTraining: AI-Driven Transformation & CSP Implications" by:

1. **Understanding Attack Vectors**: Comprehensive overview of how adversarial techniques can bypass security systems
2. **Defense Mechanisms**: Evaluation of existing defenses and robustness testing approaches
3. **Real-World Context**: Papers on production systems show practical attack/defense scenarios
4. **CSP Implications**: Understanding how Cloud Security Posture and AI systems interact in adversarial contexts
5. **Training Content**: Provides concrete examples and research-backed techniques for security awareness training

## Recommended Reading Order

### For Security Practitioners
1. 2510.01676v1 - Production malware system evaluation
2. 2512.21404v1 - Android malware evasion
3. 2511.06197v1 - IoT intrusion detection robustness
4. 2510.12310v1 - Robust malware detection

### For ML Security Researchers
1. 2512.21250v1 - Code obfuscation against LLMs
2. 2512.16538v1 - Systematic obfuscation study
3. 2511.19330v1 - Adversarial time-series attacks
4. 2502.06418v1 - Watermark robustness

### For Policy/Training Development
1. 2509.11187v1 - Multi-modal analysis approach
2. 2511.16020v2 - Physical adversarial examples
3. 2508.15848v1 - AI detection evasion
4. 2304.11300v3 - Information manipulation

## Key Takeaways

1. **Evasion is Practical**: Real-world systems (Google's malware detector) can be evaded with adversarial techniques
2. **Obfuscation Remains Effective**: Code and behavioral obfuscation bypass modern LLM-based detection
3. **Multi-Modal Resilience Required**: Single-modality systems (vision, code analysis, behavioral) are individually vulnerable
4. **Physical Threats Are Real**: Adversarial examples extend beyond digital to physical spaces
5. **Defense is Evolving**: Attribution-based and adversarial training approaches show promise

## References

Complete metadata available in `cluster_5_metadata.csv` and `papers_metadata.json`

For detailed paper information, see the CSV file containing:
- ArXiv IDs
- Full titles and author lists
- Publication dates
- Page counts
- Primary categories
- Relevance scores
- Direct ArXiv links

---

**Collection Methodology**: Systematic ArXiv search using security-focused queries  
**Collection Date**: January 6, 2025  
**Curator Notes**: Papers selected for direct relevance to detection evasion and adversarial techniques with emphasis on practical security implications and measurable defense mechanisms.
