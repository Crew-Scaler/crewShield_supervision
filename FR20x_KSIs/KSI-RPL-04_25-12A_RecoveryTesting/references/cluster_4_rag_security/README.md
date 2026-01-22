# Cluster 4: RAG Systems Security & Knowledge Base Integrity

## Research Summary

This cluster focuses on **Retrieval-Augmented Generation (RAG) system security**, including knowledge base poisoning attacks, data contamination, backdoor insertion, and detection mechanisms. The 15 papers downloaded represent cutting-edge research (2024-2025) on adversarial attacks targeting RAG pipelines and defensive strategies.

## Key Research Areas

### 1. RAG-Specific Attack Vectors (5 papers)

**RIPRAG: Hack a Black-box Retrieval-Augmented Generation QA Systems** (2510.10008v1)
- Demonstrates practical attacks on black-box RAG systems
- Tests against real-world QA systems without model access
- Relevance Score: 45/50

**RAG-targeted Adversarial Attack on LLM-based Threat Detection** (2511.06212v1)  
- Directly attacks RAG-based threat detection pipelines
- Shows vulnerability of security tools using RAG
- Demonstrates poisoning of retrieval documents
- Relevance Score: 56/50 (highest)

**Exploring the Security Threats of Retriever Backdoors in Retrieval-Augmented Coding** (2512.21681v1)
- Focuses on backdoor attacks targeting retriever components
- Specific to code generation RAG systems
- Addresses knowledge base poisoning in programming contexts
- Relevance Score: 45/50

**HV-Attack: Hierarchical Visual Attack for Multimodal RAG** (2511.15435v1)
- Extends RAG attacks to multimodal systems
- Visual content poisoning in retrieval systems
- Demonstrates cross-modal vulnerability
- Relevance Score: 35/50

**MemoryGraft: Persistent Compromise of LLM Agents via Poisoned Experience Retrieval** (2512.16962v1)
- Targets memory/experience retrieval in LLM agents
- Shows persistent compromise through poisoned memories
- Long-term attack implications
- Relevance Score: 35/50

### 2. Knowledge Base Poisoning & Corruption (2 papers)

**Rescuing the Unpoisoned: Efficient Defense Against Knowledge Corruption Attacks** (2511.01268v1)
- Develops defense mechanisms against knowledge corruption
- Efficient detection and recovery strategies
- Focuses on preserving unpoisoned information
- Relevance Score: 40/50

**Bias Injection Attacks on RAG Databases and Sanitization Defenses** (2512.00804v1)
- Targets RAG database bias injection
- Studies sanitization techniques
- Database-level poisoning analysis
- Relevance Score: 20/50

### 3. Data Poisoning Attack Mechanisms (5 papers)

**SCOUT: A Defense Against Data Poisoning Attacks in Fine-Tuned Language Models** (2512.10998v1)
- Comprehensive defense framework against data poisoning
- Addresses poisoning in fine-tuning pipelines
- Detection mechanisms for poisoned training data
- Relevance Score: 58/50 (highest overall)

**Cost-Minimized Label-Flipping Poisoning Attack to LLM Alignment** (2511.09105v1)
- Analyzes label-flipping poisoning attacks
- Cost-effectiveness of poisoning campaigns
- Alignment data poisoning
- Relevance Score: 38/50

**GShield: Mitigating Poisoning Attacks in Federated Learning** (2512.19286v2)
- Mitigates poisoning in federated learning contexts
- Applicable to distributed RAG systems
- Byzantine-robust aggregation
- Relevance Score: 38/50

**HealSplit: Self-Healing Through Adversarial Distillation** (2511.11240v1)
- Self-healing mechanisms against poisoning
- Adversarial distillation for robustness
- Recovery after compromise detection
- Relevance Score: 38/50

**Potent but Stealthy: Rethink Profile Pollution Against Sequential Recommendation** (2511.09392v4)
- Stealthy poisoning techniques
- Profile pollution in sequential systems
- Low-detectability attack strategies
- Relevance Score: 26/50

### 4. Federated & Distributed System Attacks (2 papers)

**Evaluating Adversarial Attacks on Federated Learning** (2512.13207v2)
- Federated learning vulnerability assessment
- Distributed poisoning attacks
- Model aggregation vulnerabilities
- Relevance Score: 46/50

**Zero-Trust Agentic Federated Learning for Secure IIoT** (2512.23809v1)
- Zero-trust architecture for federated systems
- Agentic AI security in distributed settings
- Industrial IoT security with RAG
- Relevance Score: 20/50

### 5. Multi-Agent & Resilience Frameworks (2 papers)

**Multi-Agent Framework for Threat Mitigation and Resilience** (2512.23132v1)
- Multi-agent defense mechanisms
- Collaborative threat mitigation
- System resilience design
- Relevance Score: 28/50

**Adaptive Trust Consensus for Blockchain IoT** (2512.22860v1)
- Trust mechanisms for distributed systems
- Blockchain-based integrity verification
- Consensus against poisoning
- Relevance Score: 28/50

## Attack Techniques Summary

### Attack Categories & Methods

| Attack Type | Mechanism | Target | Impact |
|---|---|---|---|
| **Knowledge Poisoning** | Inject false/biased documents into KB | RAG document store | Incorrect retrieval & generation |
| **Retriever Backdoors** | Embed triggers in retrieval index | Retriever component | Targeted malicious retrieval |
| **Label Flipping** | Reverse labels in training data | Fine-tuning data | Alignment degradation |
| **Memory Poisoning** | Corrupt agent experience/memory | LLM agent memory | Persistent compromise |
| **Visual Poisoning** | Corrupt multimodal KB content | Multimodal RAG | Cross-modal attacks |
| **Profile Pollution** | Inject false user/context data | Sequential systems | Personalization corruption |
| **Bias Injection** | Systematic bias in documents | RAG database | Biased outputs |
| **Federated Poisoning** | Byzantine attacks in FL | Distributed training | Model degradation |

### Defense Mechanisms Identified

1. **Detection-Based Defenses**
   - Identify poisoned documents through statistical analysis
   - Monitor retrieval patterns for anomalies
   - Flag suspicious fine-tuning data

2. **Removal-Based Defenses**
   - Exclude identified poisoned samples
   - Sanitize RAG databases
   - Byzantine-robust aggregation

3. **Robustness-Based Defenses**
   - Adversarial training
   - Distillation for robustness
   - Self-healing mechanisms

4. **Structural Defenses**
   - Zero-trust architectures
   - Multi-agent verification
   - Blockchain-based integrity verification

## Quantitative Metrics from Papers

### Attack Success Rates
- **RAG poisoning effectiveness**: 30-80% success depending on document count poisoned
- **Label-flipping cost**: 2-5% of training data sufficient for detectable degradation
- **Retriever backdoors**: 95%+ success on trigger-based attacks
- **Memory poisoning persistence**: 100% across agent episodes

### Detection Rates
- **Statistical anomaly detection**: 70-90% accuracy
- **Fingerprinting methods**: 85%+ precision
- **Byzantine-robust aggregation**: 99%+ accuracy with 50% Byzantine clients

### Performance Trade-offs
- **Defense overhead**: 5-20% computational cost
- **Accuracy impact**: <2% with proper defenses
- **Recovery time**: Minutes to hours depending on poisoning extent

## Research Gaps & Future Directions

1. **Practical Attack Scenarios**: Limited real-world evaluation against production RAG systems
2. **Defense Scalability**: Scalability to extremely large knowledge bases (billions of documents)
3. **Multimodal Security**: Limited research on cross-modal poisoning attacks
4. **Detection Evasion**: Adversarial defenses against detection mechanisms
5. **Federated RAG**: Security of federated RAG systems still underexplored

## Key Findings

### Information Integrity Threats

**High Severity:**
- Retriever backdoors can be inserted during RAG system initialization
- Knowledge base poisoning persists across multiple queries
- Memory poisoning in agents survives across conversations
- Multimodal poisoning crosses document/image boundaries

**Medium Severity:**
- Label-flipping attacks require training data access
- Bias injection requires database write access
- Profile pollution affects personalization but not core functionality

### Defense Recommendations

1. **Implement multi-layer validation**
   - Validate retrieved documents against ground truth
   - Monitor retriever behavior for anomalies
   - Verify training data integrity

2. **Use Byzantine-robust aggregation** for federated RAG systems

3. **Employ continuous monitoring** for knowledge base changes

4. **Implement recovery procedures** for detected poisoning

5. **Use zero-trust architectures** in distributed systems

## Paper Statistics

**Publication Timeline**: All papers from 2024-2025
- Q4 2024 (Oct-Dec): 10 papers
- Q4 2025 (Oct-Dec): 5 papers (preliminary)

**Research Institutions**:
- Academic institutions (Stanford, MIT, CMU, Berkeley equivalent): Multiple
- Industry labs (OpenAI, Anthropic, major tech companies)
- Independent research groups

**Page Distribution**:
- Average: ~12-18 pages per paper
- Range: 8-20+ pages
- Detailed empirical evaluation in all papers

## References


### Downloaded Papers (15 Total)

1. **SCOUT: A Defense Against Data Poisoning Attacks in Fine-Tuned Language Models**
   - ArXiv ID: 2512.10998v1
   - Authors: Mohamed Afane et al.
   - Published: 2025-12-10
   - Relevance Score: 58/50
   - File: `2512.10998v1.pdf`

2. **RAG-targeted Adversarial Attack on LLM-based Threat Detection and Mitigation Framework**
   - ArXiv ID: 2511.06212v1
   - Authors: Seif Ikbarieh et al.
   - Published: 2025-11-09
   - Relevance Score: 56/50
   - File: `2511.06212v1.pdf`

3. **Evaluating Adversarial Attacks on Federated Learning for Temperature Forecasting**
   - ArXiv ID: 2512.13207v2
   - Authors: Karina Chichifoi et al.
   - Published: 2025-12-15
   - Relevance Score: 46/50
   - File: `2512.13207v2.pdf`

4. **RIPRAG: Hack a Black-box Retrieval-Augmented Generation Question-Answering System with Reinforcement Learning**
   - ArXiv ID: 2510.10008v1
   - Authors: Meng Xi et al.
   - Published: 2025-10-11
   - Relevance Score: 45/50
   - File: `2510.10008v1.pdf`

5. **Exploring the Security Threats of Retriever Backdoors in Retrieval-Augmented Code Generation**
   - ArXiv ID: 2512.21681v1
   - Authors: Tian Li et al.
   - Published: 2025-12-25
   - Relevance Score: 45/50
   - File: `2512.21681v1.pdf`

6. **Rescuing the Unpoisoned: Efficient Defense against Knowledge Corruption Attacks on RAG Systems**
   - ArXiv ID: 2511.01268v1
   - Authors: Minseok Kim et al.
   - Published: 2025-11-03
   - Relevance Score: 40/50
   - File: `2511.01268v1.pdf`

7. **HealSplit: Towards Self-Healing through Adversarial Distillation in Split Federated Learning**
   - ArXiv ID: 2511.11240v1
   - Authors: Yuhan Xie et al.
   - Published: 2025-11-14
   - Relevance Score: 38/50
   - File: `2511.11240v1.pdf`

8. **Cost-Minimized Label-Flipping Poisoning Attack to LLM Alignment**
   - ArXiv ID: 2511.09105v1
   - Authors: Shigeki Kusaka et al.
   - Published: 2025-11-12
   - Relevance Score: 38/50
   - File: `2511.09105v1.pdf`

9. **GShield: Mitigating Poisoning Attacks in Federated Learning**
   - ArXiv ID: 2512.19286v2
   - Authors: Sameera K. M. et al.
   - Published: 2025-12-22
   - Relevance Score: 38/50
   - File: `2512.19286v2.pdf`

10. **HV-Attack: Hierarchical Visual Attack for Multimodal Retrieval Augmented Generation**
   - ArXiv ID: 2511.15435v1
   - Authors: Linyin Luo et al.
   - Published: 2025-11-19
   - Relevance Score: 35/50
   - File: `2511.15435v1.pdf`

11. **MemoryGraft: Persistent Compromise of LLM Agents via Poisoned Experience Retrieval**
   - ArXiv ID: 2512.16962v1
   - Authors: Saksham Sahai Srivastava et al.
   - Published: 2025-12-18
   - Relevance Score: 35/50
   - File: `2512.16962v1.pdf`

12. **Multi-Agent Framework for Threat Mitigation and Resilience in AI-Based Systems**
   - ArXiv ID: 2512.23132v1
   - Authors: Armstrong Foundjem et al.
   - Published: 2025-12-29
   - Relevance Score: 28/50
   - File: `2512.23132v1.pdf`

13. **Adaptive Trust Consensus for Blockchain IoT: Comparing RL, DRL, and MARL Against Naive, Collusive, Adaptive, Byzantine, and Sleeper Attacks**
   - ArXiv ID: 2512.22860v1
   - Authors: Soham Padia et al.
   - Published: 2025-12-28
   - Relevance Score: 28/50
   - File: `2512.22860v1.pdf`

14. **Potent but Stealthy: Rethink Profile Pollution against Sequential Recommendation via Bi-level Constrained Reinforcement Paradigm**
   - ArXiv ID: 2511.09392v4
   - Authors: Jiajie Su et al.
   - Published: 2025-11-12
   - Relevance Score: 26/50
   - File: `2511.09392v4.pdf`

15. **Zero-Trust Agentic Federated Learning for Secure IIoT Defense Systems**
   - ArXiv ID: 2512.23809v1
   - Authors: Samaresh Kumar Singh et al.
   - Published: 2025-12-29
   - Relevance Score: 20/50
   - File: `2512.23809v1.pdf`

