# Issue #65 Topic 10: API Gateway and Inference Endpoint Security with Cryptographic Enforcement
## Top 10 Most Relevant Papers (2024-2025)

This document indexes the top 10 papers selected for cryptographic enforcement and secure API gateway security.

### Selection Criteria
- **Focus**: Cryptographic enforcement, secure inference, inference attacks, privacy-preserving ML
- **Relevance**: Query-based attacks, model extraction, differential privacy, secure computation
- **Quality**: 2025 papers prioritized, prestigious institutions weighted
- **Metrics**: Privacy/security mechanisms, attack success rates, cryptographic techniques

---

## Top 10 Papers

### 1. DeepShare: Sharing ReLU Across Channels and Layers for Efficient Private Inference
- **ArXiv ID**: 2512.17398v1
- **Authors**: Yonathan Bornfeld, Shai Avidan
- **Published**: 2025-12-19
- **Category**: cs.LG / Security
- **Key Contribution**: Cryptographic private inference using ReLU optimization; reduces DReLU operations using channel-layer sharing
- **Relevance**: Directly addresses secure inference endpoints with cryptographic primitives
- **PDF**: `2512.17398v1_DeepShare_Sharing_ReLU_Across_Channels_and_Layers_for_Efficient_Private_Inference.pdf`

### 2. In-Context Probing for Membership Inference in Fine-Tuned Language Models
- **ArXiv ID**: 2512.16292v2
- **Authors**: Zhexi Lu, Hongliang Chi, Nathalie Baracaldo, Swanand Ravindra Kadhe, Yuseok Jeon, Lei Yu
- **Published**: 2025-12-18 (Updated 2025-12-21)
- **Category**: cs.CR
- **Key Contribution**: Membership inference attack exploiting training dynamics; demonstrates API vulnerability
- **Relevance**: Shows how API endpoints leak information through model outputs
- **PDF**: `2512.16292v2_In-Context_Probing_for_Membership_Inference_in_Fine-Tuned_Language_Models.pdf`

### 3. MVP-ORAM: a Wait-free Concurrent ORAM for Confidential BFT Storage
- **ArXiv ID**: 2512.12006v1
- **Authors**: Robin Vassantlal, Hasan Heydari, Bernardo Ferreira, Alysson Bessani
- **Published**: 2025-12-12
- **Category**: cs.CR
- **Key Contribution**: Oblivious RAM protocol hiding access patterns; cryptographic data protection
- **Relevance**: Encrypts API access patterns to prevent inference attacks
- **Metrics**: Processes 100s of 4KB accesses/sec in cloud environments
- **PDF**: `2512.12006v1_MVP-ORAM_a_Wait-free_Concurrent_ORAM_for_Confidential_BFT_Storage.pdf`

### 4. Practical Framework for Privacy-Preserving and Byzantine-robust Federated Learning
- **ArXiv ID**: 2512.17254v1
- **Authors**: Baolei Zhang, Minghong Fang, Zhuqing Liu, et al.
- **Published**: 2025-12-19
- **Category**: cs.CR
- **Key Contribution**: Privacy-preserving aggregation with dimensionality reduction; defends against model inversion attacks
- **Relevance**: Framework for securing distributed inference endpoints
- **PDF**: `2512.17254v1_Practical_Framework_for_Privacy-Preserving_and_Byzantine-robust_Federated_Learning.pdf`

### 5. PrivateXR: Defending Privacy Attacks in Extended Reality Through Explainable AI-Guided Differential Privacy
- **ArXiv ID**: 2512.16851v1
- **Authors**: Ripan Kumar Kundu, Istiak Ahmed, Khaza Anuarul Hoque
- **Published**: 2025-12-18
- **Category**: cs.CR
- **Key Contribution**: Differential privacy defense against membership inference and re-identification attacks
- **Relevance**: Selective differential privacy for model outputs (43% reduction in MIA success)
- **Metrics**: 2x inference speedup vs traditional DP; up to 97% accuracy preservation
- **PDF**: `2512.16851v1_PrivateXR_Defending_Privacy_Attacks_in_Extended_Reality_Through_Explainable_AI-Guided_Differential_P.pdf`

### 6. Differentially Private Feature Release for Wireless Sensing: Adaptive Privacy Budget Allocation
- **ArXiv ID**: 2512.20323v1
- **Authors**: Ipek Sena Yilmaz, Onur G. Tuncer, Zeynep E. Aksoy, Zeynep Yağmur Baydemir
- **Published**: 2025-12-23
- **Category**: cs.CR
- **Key Contribution**: Adaptive differential privacy allocation for feature extraction; prevents identity/membership inference
- **Relevance**: Query response protection through privacy budgets
- **PDF**: `2512.20323v1_Differentially_Private_Feature_Release_for_Wireless_Sensing_Adaptive_Privacy_Budget_Allocation_on_CS.pdf`

### 7. Bits for Privacy: Evaluating Post-Training Quantization via Membership Inference
- **ArXiv ID**: 2512.15335v1
- **Authors**: Chenxiang Zhang, Tongxi Qu, Zhong Li, et al.
- **Published**: 2025-12-17
- **Category**: cs.LG / Privacy
- **Key Contribution**: Post-training quantization reduces privacy leakage; lower precision = 10x less MIA vulnerability
- **Relevance**: Cryptographic model compression technique for API deployment
- **Metrics**: Up to 1.58-bit quantization; order of magnitude vulnerability reduction
- **PDF**: `2512.15335v1_Bits_for_Privacy_Evaluating_Post-Training_Quantization_via_Membership_Inference.pdf`

### 8. An Efficient Gradient-Based Inference Attack for Federated Learning
- **ArXiv ID**: 2512.15143v1
- **Authors**: Pablo Montaña-Fernández, Ines Ortega-Fernandez
- **Published**: 2025-12-17
- **Category**: cs.LG / Privacy
- **Key Contribution**: Gradient-based membership inference exploiting temporal evolution across rounds
- **Relevance**: Demonstrates API vulnerability through gradient leakage
- **Metrics**: Multi-round FL increases vulnerability; aggregators pose 2x threat vs data owners
- **PDF**: `2512.15143v1_An_Efficient_Gradient-Based_Inference_Attack_for_Federated_Learning.pdf`

### 9. PerProb: Indirectly Evaluating Memorization in Large Language Models
- **ArXiv ID**: 2512.14600v1
- **Authors**: Yihan Liao, Jacky Keung, Xiaoxue Ma, Jingyu Zhang, Yicheng Sun
- **Published**: 2025-12-16
- **Category**: cs.CR
- **Key Contribution**: Label-free MIA framework; evaluates training data extraction risk
- **Relevance**: Black-box API attack detection mechanism
- **Metrics**: Differential privacy reduces data leakage; demonstrates effectiveness of DP, distillation, early stopping
- **PDF**: `2512.14600v1_PerProb_Indirectly_Evaluating_Memorization_in_Large_Language_Models.pdf`

### 10. Differential Privacy for Secure Machine Learning in Healthcare IoT-Cloud Systems
- **ArXiv ID**: 2512.10426v1
- **Authors**: N Mangala, Murtaza Rangwala, S Aishwarya, et al.
- **Published**: 2025-12-11
- **Category**: cs.CR
- **Key Contribution**: Multi-layer DP framework; hybrid Laplace-Gaussian noise mechanism; blockchain-secured API
- **Relevance**: End-to-end cryptographic security for cloud inference endpoints
- **Metrics**: 82-84% accuracy at ε=5.0; 18% reduction in attribute inference; 70% reduction in data reconstruction; 8x latency reduction
- **PDF**: `2512.10426v1_Differential_Privacy_for_Secure_Machine_Learning_in_Healthcare_IoT-Cloud_Systems.pdf`

---

## Summary Metrics

| Paper | Crypto Method | Attack Type | Defense | 2025 |
|-------|---------------|------------|---------|------|
| DeepShare | Private Inference | Model-agnostic | ReLU optimization | Yes |
| In-Context Probing | Training dynamics | Membership Inference | Dynamic gap analysis | Yes |
| MVP-ORAM | Oblivious RAM | Access pattern inference | Encrypted access patterns | Yes |
| Federated Learning | DP + Cryptographic aggregation | Byzantine + MIA | Multi-layer defense | Yes |
| PrivateXR | Differential Privacy | MIA + Re-identification | XAI-guided DP | Yes |
| Wireless Sensing | Differential Privacy | Membership Inference | Adaptive budget allocation | Yes |
| Post-Training Quantization | Model compression | Membership Inference | Bit-width reduction | Yes |
| Gradient-based Attack | Temporal analysis | Data extraction | Model updates obfuscation | Yes |
| PerProb | Multiple DP techniques | Training data extraction | DP + distillation | Yes |
| Healthcare IoT-Cloud | DP + Blockchain | Multi-attribute inference | Hybrid Laplace-Gaussian | Yes |

---

## Key Cryptographic Techniques Identified

1. **Differential Privacy**: Noise addition to outputs/gradients (7/10 papers)
2. **Oblivious RAM (ORAM)**: Access pattern hiding (2/10 papers)
3. **Secure Inference**: Cryptographic computation (2/10 papers)
4. **Model Compression**: Quantization-based privacy (1/10 papers)
5. **Blockchain Integration**: Immutable audit trails (1/10 papers)

---

## Recommendations for Issue #65

### API Gateway Security:
- Implement differential privacy at the API response layer (privacy budget per user)
- Use ORAM for query pattern obfuscation
- Encrypt gradient updates in federated learning scenarios

### Cryptographic Enforcement:
- Integrate post-training quantization for model protection
- Implement XAI-guided DP for selective encryption
- Use blockchain for immutable logging of API access

### Detection & Monitoring:
- Implement membership inference detection (PerProb framework)
- Monitor gradient leakage in model update pipelines
- Track attribute inference vulnerabilities with differential privacy budgets
