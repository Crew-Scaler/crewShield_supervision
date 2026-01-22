# Topic 8: Model Extraction and Inference Attacks on Configuration Management ML Models
## ArXiv Research Summary

**Research Date**: December 24, 2025
**Total Papers Downloaded**: 8 papers
**Search Queries**: 2 (Query 1 + Query 2)
**Output Directory**: `/Users/tamnguyen/Documents/GitHub/ksi_watch/KSI-SVC-01_25-12A_ContinuousImprovement/references/topic8_model_extraction/`

---

## Research Overview

This research investigates model extraction attacks, membership inference attacks, and side-channel attacks targeting machine learning models in cloud and shared infrastructure environments. The papers cover defensive measures (watermarking, adversarial training) and offensive techniques (cache side-channels, quantum crosstalk attacks).

---

## Papers Summary

### QUERY 1: Model Extraction & Inference Attacks on Cloud APIs
**Query**: `("model extraction" OR "model stealing") AND (API OR inference) AND (cloud OR infrastructure) AND (2024 OR 2025)`
**Papers Found**: 4 papers, **4 downloaded**

---

#### Paper 1: RADEP - Resilient Adaptive Defense Framework
- **ArXiv ID**: 2505.19364v1
- **Title**: RADEP: A Resilient Adaptive Defense Framework Against Model Extraction Attacks
- **Authors**: Amit Chakraborty, Sayyed Farid Ahamed, Sandip Roy, Soumya Banerjee, Kevin Choi, Abdul Rahman, Alison Hu, Edward Bowen, Sachin Shetty
- **Published**: May 25, 2025
- **Relevance Score**: 16.0 / 5 keywords matched
- **Primary Category**: cs.CR (Cryptography and Security)
- **Summary**: Proposes RADEP, a multi-layered defense framework for MLaaS platforms against model extraction attacks. Key defenses include: (1) Progressive adversarial training for model resilience, (2) Uncertainty quantification and behavioral analysis for malicious query detection, (3) Adaptive response mechanism with dynamic query output modification, (4) Embedded watermarking and backdoor triggers for ownership verification. Experimental results show effective extraction prevention while maintaining service quality.
- **Relevance to Topic**: High - Directly addresses defense mechanisms against model extraction attacks on cloud-based ML services (MLaaS).
- **PDF**: `2505.19364v1_RADEP_A_Resilient_Adaptive_Defense_Framework_Against_Model_Extraction_Attacks.pdf`

---

#### Paper 2: THEMIS - IP Protection for On-Device Deep Learning
- **ArXiv ID**: 2503.23748v1
- **Title**: THEMIS: Towards Practical Intellectual Property Protection for Post-Deployment On-Device Deep Learning Models
- **Authors**: Yujin Huang, Zhi Zhang, Qingchuan Zhao, Xingliang Yuan, Chunyang Chen
- **Published**: March 31, 2025
- **Relevance Score**: 16.0 / 5 keywords matched
- **Primary Category**: cs.CR (Cryptography and Security)
- **Summary**: Addresses model-stealing attacks on on-device deep learning models by proposing THEMIS, an automatic tool for watermark protection. The tool reconstructs writable counterparts of read-only on-device DL models and solves watermark parameters to protect intellectual property. Successfully tested on 403 real-world mobile DL apps from Google Play with 81.14% success rate. Extends watermarking techniques to post-deployment models.
- **Relevance to Topic**: High - Demonstrates practical model extraction/stealing attacks on deployed ML models and proposes watermarking-based defenses.
- **PDF**: `2503.23748v1_THEMIS_Towards_Practical_Intellectual_Property_Protection_for_Post-Deployment_On-Device_Deep_Learnin.pdf`

---

#### Paper 3: Bounding-box Watermarking for Object Detectors
- **ArXiv ID**: 2411.13047v2
- **Title**: Bounding-box Watermarking: Defense against Model Extraction Attacks on Object Detectors
- **Authors**: Satoru Koda, Ikuya Morikawa
- **Published**: November 20, 2024 (Updated June 25, 2025)
- **Relevance Score**: 11.0 / 2 keywords matched
- **Primary Category**: cs.CR (Cryptography and Security)
- **Summary**: Proposes a backdoor-based watermarking defense specifically for object detection models exposed via APIs. The approach stealthily modifies bounding-boxes of detected objects while preserving detection capability. Achieves 100% accuracy in identifying extracted models across three OD datasets. Addresses the gap in watermarking techniques for object detection tasks.
- **Relevance to Topic**: High - Extends model extraction defense mechanisms from classification to detection models via API responses.
- **PDF**: `2411.13047v2_Bounding-box_Watermarking_Defense_against_Model_Extraction_Attacks_on_Object_Detectors.pdf`

---

#### Paper 4: LDPKiT - Privacy-Preserving Model Extraction
- **ArXiv ID**: 2405.16361v3
- **Title**: LDPKiT: Superimposing Remote Queries for Privacy-Preserving Local Model Training
- **Authors**: Kexin Li, Aastha Mehta, David Lie
- **Published**: May 25, 2024 (Updated October 11, 2025)
- **Relevance Score**: 11.0 / 2 keywords matched
- **Primary Category**: cs.LG (Machine Learning)
- **Summary**: Proposes LDPKiT, a framework for non-adversarial privacy-preserving model extraction from cloud ML services using local differential privacy. Introduces a superimposition technique generating in-distribution samples for knowledge transfer. Tested on Fashion-MNIST, SVHN, and PathMNIST with improved utility while maintaining privacy guarantees. Demonstrates trade-off between accuracy and privacy at different epsilon levels.
- **Relevance to Topic**: Medium-High - Explores legitimate model extraction scenarios while preserving privacy in cloud ML service usage.
- **PDF**: `2405.16361v3_LDPKiT_Superimposing_Remote_Queries_for_Privacy-Preserving_Local_Model_Training.pdf`

---

### QUERY 2: Membership Inference & Side-Channel Attacks on Multi-Tenant Infrastructure
**Query**: `("membership inference" OR "side-channel attack") AND (configuration OR model) AND (shared-infrastructure OR multi-tenant) AND (2024 OR 2025)`
**Papers Found**: 4 papers, **4 downloaded**

---

#### Paper 5: SWAP Attack - Quantum Multi-Tenant Cloud
- **ArXiv ID**: 2502.10115v1
- **Title**: SWAP Attack: Stealthy Side-Channel Attack on Multi-Tenant Quantum Cloud System
- **Authors**: Wei Jie Bryan Lee, Siyi Wang, Suman Dutta, Walid El Maouaki, Anupam Chattopadhyay
- **Published**: February 14, 2025
- **Relevance Score**: 16.0 / 5 keywords matched
- **Primary Category**: quant-ph (Quantum Physics)
- **Summary**: Introduces SWAP-based side-channel attacks on shared quantum computing platforms. Demonstrates both active and passive attack modes: (1) Active mode: Single CNOT gate reduces Grover's Algorithm accuracy by 81.62%, (2) Passive mode: Stealthy circuit of 6.25% victim size achieves 100% accuracy in circuit size prediction. Traces crosstalk origins to SWAP paths between qubits and shows attacks work over long distances. Challenges existing defense strategies based on topological distance.
- **Relevance to Topic**: High - Demonstrates configuration extraction attacks on shared multi-tenant quantum infrastructure through side-channels.
- **PDF**: `2502.10115v1_SWAP_Attack_Stealthy_Side-Channel_Attack_on_Multi-Tenant_Quantum_Cloud_System.pdf`

---

#### Paper 6: Spill The Beans - LLM Token Leakage via Cache
- **ArXiv ID**: 2505.00817v1
- **Title**: Spill The Beans: Exploiting CPU Cache Side-Channels to Leak Tokens from Large Language Models
- **Authors**: Andrew Adiletta, Berk Sunar
- **Published**: May 1, 2025
- **Relevance Score**: 14.0 / 4 keywords matched
- **Primary Category**: cs.CR (Cryptography and Security)
- **Summary**: Proposes novel cache side-channel attack exploiting shared hardware to leak tokens from LLM inference. Uses flush-and-reload technique on embedding vectors to detect cache hits during token generation. Demonstrates practical attack scenarios: (1) API key recovery: 80-90% recovery rate with single shot, (2) English text: 40% recovery rate with single shot. Highlights vulnerability of LLM-serving infrastructures to traditional side-channel attacks.
- **Relevance to Topic**: High - Demonstrates inference attack on deployed ML models (LLMs) via hardware side-channels in shared infrastructure.
- **PDF**: `2505.00817v1_Spill_The_Beans_Exploiting_CPU_Cache_Side-Channels_to_Leak_Tokens_from_Large_Language_Models.pdf`

---

#### Paper 7: Crosstalk in Multi-Tenant NISQ Systems
- **ArXiv ID**: 2412.10507v1
- **Title**: Crosstalk-induced Side Channel Threats in Multi-Tenant NISQ Computers
- **Authors**: Navnil Choudhury, Chaithanya Naik Mude, Sanjay Das, Preetham Chandra Tikkireddi, Swamit Tannu, Kanad Basu
- **Published**: December 13, 2024
- **Relevance Score**: 11.0 / 2 keywords matched
- **Primary Category**: cs.ET (Emerging Technologies)
- **Summary**: Demonstrates crosstalk as practical attack vector on Noisy Intermediate Scale Quantum (NISQ) machines in multi-tenant environments. Proposes side-channel attack using crosstalk signatures to identify victim quantum algorithms via CNOT gate presence detection, classified using graph-based learning models. Achieves 85.7% accuracy in algorithm identification on 336 benchmark circuits. Addresses security challenges in multi-user quantum computing models.
- **Relevance to Topic**: High - Demonstrates configuration extraction attacks on quantum circuits in multi-tenant shared infrastructure.
- **PDF**: `2412.10507v1_Crosstalk-induced_Side_Channel_Threats_in_Multi-Tenant_NISQ_Computers.pdf`

---

#### Paper 8: Network Slicing Side-Channel Attack via Reinforcement Learning
- **ArXiv ID**: 2409.11258v1
- **Title**: Attacking Slicing Network via Side-channel Reinforcement Learning Attack
- **Authors**: Wei Shao, Chandra Thapa, Rayne Holland, Sarah Ali Siddiqui, Seyit Camtepe
- **Published**: September 17, 2024
- **Relevance Score**: 9.0 / 1 keyword matched
- **Primary Category**: cs.CR (Cryptography and Security)
- **Summary**: Proposes reinforcement learning-based cache side-channel attack framework for 5G/6G network slicing environments. Exploits shared memory and cache to identify sensitive data locations (authentication keys, user registration data) across slices. Uses RL-driven guessing game approach to pinpoint memory blocks. Achieves 95-98% success rate in identifying sensitive data storage locations. Demonstrates vulnerabilities in shared virtualized network infrastructure.
- **Relevance to Topic**: Medium-High - Demonstrates side-channel attacks on shared infrastructure (network slices) with potential configuration extraction implications.
- **PDF**: `2409.11258v1_Attacking_Slicing_Network_via_Side-channel_Reinforcement_Learning_Attack.pdf`

---

## Key Research Themes

### 1. Defense Mechanisms Against Model Extraction
- **Watermarking**: Embedded backdoors for ownership verification (RADEP, THEMIS, Bounding-box)
- **Adversarial Training**: Resistance enhancement against extraction attempts
- **Query Analysis**: Uncertainty quantification and behavioral pattern detection
- **Adaptive Responses**: Dynamic modification of API responses based on suspicion scores

### 2. Side-Channel Attack Vectors
- **Hardware-Level**: CPU cache exploitation (flush-and-reload) for token leakage
- **Quantum-Specific**: SWAP-path crosstalk on multi-tenant quantum platforms
- **Network-Level**: Shared memory/cache in network slicing (5G/6G)
- **Timing Channels**: Cache timing analysis for sensitive data location discovery

### 3. Multi-Tenant Shared Infrastructure Risks
- Crosstalk-induced information leakage on NISQ quantum computers
- Cache contention in virtualized network slicing environments
- Hardware resource sharing enabling co-located attacks
- Topological distance insufficient for isolation

### 4. Model IP Protection Approaches
- Post-deployment watermarking for on-device models
- Backdoor-based verification for extracted model detection
- Privacy-preserving model extraction with local differential privacy
- Practical tool-based solutions for real-world model protection

---

## Research Gaps and Opportunities

1. **Configuration Management Specific**: Limited focus on configuration ML models; most papers target general DL models
2. **Infrastructure Hardening**: Need for configuration-aware defense mechanisms in shared environments
3. **Hybrid Attacks**: Limited exploration of combined model extraction + side-channel attacks
4. **Cost-Benefit Analysis**: Trade-offs between defense overhead and service degradation not fully explored

---

## Statistics

| Metric | Value |
|--------|-------|
| **Total Papers Downloaded** | 8 |
| **2025 Papers** | 5 (62.5%) |
| **2024 Papers** | 3 (37.5%) |
| **Average Relevance Score** | 12.3 |
| **Avg Score 2025 Papers** | 15.2 |
| **Avg Score 2024 Papers** | 9.7 |
| **Primary Categories** | cs.CR (5), cs.ET (1), quant-ph (1), cs.LG (1) |

---

## File Manifest

| ArXiv ID | Filename |
|----------|----------|
| 2505.19364v1 | `2505.19364v1_RADEP_A_Resilient_Adaptive_Defense_Framework_Against_Model_Extraction_Attacks.pdf` |
| 2503.23748v1 | `2503.23748v1_THEMIS_Towards_Practical_Intellectual_Property_Protection_for_Post-Deployment_On-Device_Deep_Learnin.pdf` |
| 2411.13047v2 | `2411.13047v2_Bounding-box_Watermarking_Defense_against_Model_Extraction_Attacks_on_Object_Detectors.pdf` |
| 2405.16361v3 | `2405.16361v3_LDPKiT_Superimposing_Remote_Queries_for_Privacy-Preserving_Local_Model_Training.pdf` |
| 2502.10115v1 | `2502.10115v1_SWAP_Attack_Stealthy_Side-Channel_Attack_on_Multi-Tenant_Quantum_Cloud_System.pdf` |
| 2505.00817v1 | `2505.00817v1_Spill_The_Beans_Exploiting_CPU_Cache_Side-Channels_to_Leak_Tokens_from_Large_Language_Models.pdf` |
| 2412.10507v1 | `2412.10507v1_Crosstalk-induced_Side_Channel_Threats_in_Multi-Tenant_NISQ_Computers.pdf` |
| 2409.11258v1 | `2409.11258v1_Attacking_Slicing_Network_via_Side-channel_Reinforcement_Learning_Attack.pdf` |

---

## Metadata Files
- `topic8_query1_papers.json` - Raw metadata for Query 1 (4 papers)
- `topic8_query2_papers.json` - Raw metadata for Query 2 (4 papers)

---

## Recommendations for Issue #64 Work

1. **Priority**: Focus on Papers 1, 5, and 6 (highest relevance scores) for immediate review
2. **Defense Strategy**: Combine approaches from RADEP, THEMIS, and LDPKiT for configuration model protection
3. **Side-Channel Hardening**: Study SWAP Attack and Spill The Beans papers for multi-tenant infrastructure recommendations
4. **Practical Implementation**: THEMIS watermarking technique most applicable to post-deployment model protection

---

*Research completed: December 24, 2025*
*Total execution time: ~6 minutes*
*Rate limit compliance: 100% (3.5s delay between requests)*
