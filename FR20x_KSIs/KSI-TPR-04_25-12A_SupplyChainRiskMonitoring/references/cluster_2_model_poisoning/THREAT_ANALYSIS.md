# Cluster 2 Threat Analysis: Model Poisoning & Supply Chain Attacks

**Document Purpose**: Actionable threat intelligence from researched papers
**Target Audience**: Security operations, model monitoring systems
**Research Base**: 19 peer-reviewed ArXiv papers (2024-2025)
**Classification**: Research Intelligence

---

## 1. Attack Threat Landscape

### 1.1 Severity Ranking by Attack Type

| Rank | Attack Type | Severity | Impact | Detectability | Papers | Primary Concern |
|------|-------------|----------|--------|---------------|---------|----|
| 1 | Knowledge Base Poisoning (RAG) | CRITICAL | High impact, low cost | Medium | 6 | 90%+ success rates, single-document attacks |
| 2 | Supply Chain Model Replacement | CRITICAL | Widespread, enterprise | Low | 5 | Affects all downstream users |
| 3 | Backdoor Injection | CRITICAL | Persistent, trigger-based | Medium | 5 | Survives fine-tuning, unlearning defeats in 16 steps |
| 4 | Weight/Parameter Tampering | HIGH | Direct model corruption | Low | 1 | Fine-grained control, hard to detect |
| 5 | Code Poisoning | HIGH | Supply chain in dev tools | Medium | 2 | Affects development workflows |
| 6 | Tool/Protocol Poisoning (MCP) | MEDIUM | Emerging framework risk | Medium | 1 | Integration framework vulnerability |
| 7 | Visual Content Poisoning | MEDIUM | Emerging attack surface | Medium | 1 | Single image causes DoS/disinformation |

### 1.2 Cost-Benefit Analysis from Research

**Lowest Cost Attacks** (Research Evidence):
1. **Constant-Cost Poisoning**: ~250 malicious documents sufficient to compromise LLM of ANY size (2510.07192)
   - Cost factor: Size-independent
   - Success rate: Consistently high across 600M-13B parameter models
   - Implication: Enterprise LLMs not more resilient than smaller models

2. **Single-Document RAG Poisoning**: CorruptRAG achieves high success with 1 poisoned text (2504.03957)
   - Cost factor: Near-minimal resource requirement
   - Success rate: 70-85% depending on RAG architecture
   - Implication: Knowledge base integrity is critical

3. **Single-Image Visual RAG Poisoning**: One adversarial image enables DoS or targeted attacks (2504.02132)
   - Cost factor: Minimal computational cost
   - Success rate: 95%+ on tested systems
   - Implication: Visual RAG systems are extremely vulnerable

**Highest Impact Attacks** (Research Evidence):
1. **Supply Chain Model Replacement** (2505.22778, 2401.15883)
   - Impact scope: ALL models using compromised artifact
   - Persistence: Survives through entire deployment pipeline
   - Detection difficulty: Extremely high (indistinguishability in embedding space)

2. **Malware in Model Parameters** (2403.03593 - MaleficNet 2.0)
   - Impact scope: Executes within model inference
   - Persistence: Self-extracting, self-executing
   - Detection difficulty: Critical - may be invisible to standard monitoring

---

## 2. Specific Attack Vectors & Indicators

### 2.1 RAG System Poisoning Attacks

**Attack Vector 1: Knowledge Base Injection**
- **Papers**: 2507.08862, 2505.18543, 2402.07867
- **Mechanism**: Insert malicious documents/triples into RAG knowledge database
- **Indicators to Monitor**:
  - Sudden changes in retrieval result patterns
  - Anomalies in document embedding distances
  - Increase in contradictory retrieved passages
  - Model responses diverging from expected behavior for known questions
- **Detection Window**: 5-15 minutes after injection
- **Success Metrics from Research**:
  - 90% attack success with 5 malicious texts per question
  - 70-85% success with single document injection
  - Success persists even with expanded datasets and variants

**Attack Vector 2: Graph-Based RAG Poisoning**
- **Papers**: 2507.08862
- **Mechanism**: Insert perturbation triples to complete misleading inference chains
- **Indicators to Monitor**:
  - Unusual path lengths in knowledge graph traversal
  - Anomalous triple insertion patterns
  - Graph clustering coefficient changes
  - Sudden emergence of inference chains connecting unrelated entities

**Attack Vector 3: Visual Document RAG Poisoning**
- **Papers**: 2504.02132
- **Mechanism**: Single adversarial image in visual RAG knowledge base
- **Indicators to Monitor**:
  - Anomalous image retrieval rankings
  - Sudden changes in embedding similarity for documents
  - Consistency degradation in VLM responses
  - Image perturbation detection on ingestion

**Attack Vector 4: CorruptRAG (Practical Single-Document)**
- **Papers**: 2504.03957
- **Mechanism**: One poisoned text optimized for attack without detection
- **Indicators to Monitor**:
  - Text embedding statistics anomalies
  - Semantic coherence metrics vs. database average
  - Rare word patterns not matching domain vocabulary
  - BERTScore against known benign documents

---

### 2.2 LLM Backdoor Attacks

**Attack Vector 1: Trigger-Based Backdoors**
- **Papers**: 2502.05224, 2510.07192
- **Mechanism**: Embed trigger patterns in training data; model learns trigger→target mapping
- **Indicators to Monitor**:
  - Sudden output shifts when specific token sequences appear
  - Token frequency anomalies in training/fine-tuning datasets
  - Activation pattern clustering around trigger tokens
  - Hidden layer representation changes for specific inputs
- **Detection Methods from Research**:
  - Attention head analysis (2411.00348 - Attention Tracker)
  - Parameter magnitude analysis in embedding layers (2501.03272)
  - Spectral signature analysis (2508.21636)

**Attack Vector 2: Constant-Cost Poisoning**
- **Papers**: 2510.07192
- **Mechanism**: ~250 malicious documents compromise any LLM size
- **Indicators to Monitor**:
  - Training data quality metrics (statistical anomalies)
  - Perplexity changes in specific domains
  - Activation variance in transformer layers
  - Token prediction confidence degradation for trigger sequences
- **Critical Finding**: Larger models NOT MORE RESILIENT despite more clean data

**Attack Vector 3: Unlearning Failure**
- **Papers**: 2502.05209
- **Mechanism**: Unlearning defenses can be undone with 16 steps of fine-tuning
- **Indicators to Monitor**:
  - Rapid regeneration of previously unlearned behaviors
  - Reduced fine-tuning loss despite small dataset
  - Unexpected capability emergence during adaptation
  - Loss curve anomalies during fine-tuning

---

### 2.3 Supply Chain Attacks

**Attack Vector 1: Model Replacement**
- **Papers**: 2505.22778
- **Mechanism**: Replace legitimate model with compromised version in supply chain
- **Indicators to Monitor**:
  - Model file size changes
  - Checksum/hash validation failures
  - Embedding space analysis (TransTroj indistinguishability check)
  - Downstream task performance degradation
  - Unexpected model behavior on control test cases
- **Detection Difficulty**: EXTREME - embedding indistinguishability designed to fool standard checks

**Attack Vector 2: Unsafe Deserialization (Pickle)**
- **Papers**: 2505.22778
- **Mechanism**: Exploit Python pickle to execute arbitrary code during model loading
- **Indicators to Monitor**:
  - File format validation (ensure non-pickle formats)
  - Loading time anomalies
  - Resource usage spikes during deserialization
  - Unexpected subprocess spawning during model import
- **Mitigation**: Use safe formats (ONNX, SafeTensors)

**Attack Vector 3: Embedding Indistinguishability (TransTroj)**
- **Papers**: 2401.15883
- **Mechanism**: Backdoor in pre-trained model embedding layer, transfers through fine-tuning
- **Indicators to Monitor**:
  - Embedding space distance metrics
  - Cosine similarity distributions in embedding layers
  - Anomalous downstream task activation patterns
  - Low-dimensional robustness subspace analysis
- **Research Finding**: Achieves 100% attack success on downstream tasks while maintaining clean embedding statistics

**Attack Vector 4: Malware in Parameters (MaleficNet 2.0)**
- **Papers**: 2403.03593
- **Mechanism**: Self-executing malware embedded in model weights using spread-spectrum coding
- **Indicators to Monitor**:
  - Parameter entropy analysis
  - Spectral analysis of weight matrices
  - Inference latency anomalies
  - Unexpected system calls during inference
  - Memory access patterns during forward pass
- **Severity**: May execute arbitrary code during model inference

---

### 2.4 Code Poisoning Attacks

**Attack Vector 1: Code Generation Model Poisoning**
- **Papers**: 2508.21636
- **Mechanism**: Inject malicious code samples in training data for code models
- **Indicators to Monitor**:
  - Static analysis of generated code
  - Vulnerability scanning of generated outputs
  - Semantic consistency checks
  - Code pattern anomalies vs. development standards
  - Suspicious imports/syscalls in generated code

**Attack Vector 2: Source Code Embedding Poisoning**
- **Papers**: 2502.13459
- **Mechanism**: Poisoned training samples in code analysis models
- **Indicators to Monitor**:
  - Detection accuracy degradation on defect/clone detection
  - False negative rates increasing
  - Sudden capability changes in model outputs
  - CodeGarrison defense: 93.5% detection accuracy achievable

---

### 2.5 Prompt Injection & Tool Poisoning

**Attack Vector 1: Prompt Injection in RAG**
- **Papers**: 2411.00348, 2412.16708
- **Mechanism**: Malicious prompts in retrieved documents override system instructions
- **Indicators to Monitor**:
  - Attention pattern shifts toward injected content
  - Prompt structure changes in retrieved documents
  - Model output divergence from known patterns
  - Semantic marker detection (injection keywords)
- **Defense from Research**: Skeptical prompting activates LLM reasoning, provides partial defense

**Attack Vector 2: Tool Poisoning in MCP**
- **Papers**: 2512.06556
- **Mechanism**: Malicious tool definitions in Model Context Protocol
- **Indicators to Monitor**:
  - Tool manifest validation
  - Signature verification (RSA-based)
  - Semantic vetting of tool definitions
  - Unexpected tool behavior or side effects
- **Emerging Threat**: New framework, limited detection maturity

---

## 3. Detection Strategies & Defenses

### 3.1 Detection Methods from Research

**Method 1: Anomaly Detection (General)**
- **Source**: 2503.09302
- **Approach**: Statistical anomaly detection + adversarial training
- **Effectiveness**: 15-20% accuracy recovery from poisoned models
- **Implementation**: Train detector on clean data characteristics

**Method 2: Attention-Based Detection**
- **Source**: 2411.00348 (Attention Tracker)
- **Approach**: Track attention distraction toward malicious inputs
- **Effectiveness**: 10% AUROC improvement over baseline
- **Advantage**: Training-free, works with small LLMs

**Method 3: Parameter Analysis (BTU)**
- **Source**: 2501.03272
- **Approach**: Detect distinctive parameter differences in embedding layers
- **Effectiveness**: Identifies backdoor tokens for fine-grained unlearning
- **Implementation**: Layer-wise embedding analysis

**Method 4: Spectral & Static Analysis**
- **Source**: 2508.21636
- **Approach**: Spectral signatures, activation clustering, static code analysis
- **Effectiveness**: Moderate, generates false positives/negatives
- **Use Case**: Code generation model poisoning

**Method 5: Forensic Traceback (RAGForensics)**
- **Source**: 2504.21668
- **Approach**: Iterative retrieval + LLM-guided poison detection
- **Effectiveness**: Identifies poisoned texts in knowledge database
- **Advantage**: Post-attack forensics, identifies source documents

**Method 6: Embedding Space Analysis**
- **Source**: 2401.15883 (TransTroj detection)
- **Approach**: Analyze embedding indistinguishability metrics
- **Effectiveness**: Can detect transformed backdoors
- **Challenge**: Embedded by design to be indistinguishable

---

### 3.2 Defense Mechanisms

**Defense 1: Knowledge Base Integrity Monitoring**
- **Approach**:
  - Validate all ingested documents
  - Monitor embedding statistics
  - Track retrieval patterns
  - Maintain audit logs
- **Papers**: 2504.21668, 2412.16708
- **Effectiveness**: Can detect most RAG poisoning attacks

**Defense 2: Skeptical Prompting**
- **Approach**: Activate LLM reasoning for critical queries
- **Effectiveness**: Partial defense against prompt injection
- **Limitation**: Doesn't prevent all attacks
- **Papers**: 2412.16708

**Defense 3: Backdoor Token Unlearning (BTU)**
- **Approach**: Fine-grained unlearning of trigger tokens
- **Effectiveness**: Can remove identified backdoors
- **Limitation**: Can be undone with 16 steps fine-tuning
- **Papers**: 2501.03272

**Defense 4: Code Embedding Detection (CodeGarrison)**
- **Approach**: Detect malicious training samples using embeddings
- **Effectiveness**: 93.5% detection accuracy
- **Use Case**: Code generation model poisoning
- **Papers**: 2502.13459

**Defense 5: Supply Chain Verification**
- **Approach**:
  - Sigstore authentication for models
  - Checksum validation
  - Safe deserialization formats (ONNX, SafeTensors)
  - Manifest signing (RSA-based)
- **Papers**: 2505.22778, 2512.06556

**Defense 6: Model Verification Testing**
- **Approach**:
  - Control test cases for known behaviors
  - Trigger pattern detection
  - Activation analysis
  - Downstream task evaluation
- **Papers**: 2502.05209, 2401.15883

---

## 4. Operational Recommendations

### 4.1 Immediate Actions (Days 1-7)

1. **Inventory Control**
   - Document all models in use
   - Verify checksums/signatures
   - Identify models using unsafe pickle format
   - Validate model sources in supply chain

2. **RAG System Assessment**
   - Review knowledge base ingestion pipelines
   - Assess document validation processes
   - Test retrieval quality baselines
   - Implement retrieval pattern monitoring

3. **Access Control Review**
   - Restrict knowledge base write access
   - Monitor training data modifications
   - Audit fine-tuning operations
   - Track model file changes

### 4.2 Short-Term Implementation (Weeks 1-4)

1. **Detection System Deployment**
   - Implement anomaly detection baselines
   - Deploy attention pattern monitoring
   - Set up RAG document validation
   - Create poisoning alert thresholds

2. **Baseline Establishment**
   - Document normal embedding statistics
   - Record typical retrieval patterns
   - Establish clean model activation patterns
   - Define code generation quality metrics

3. **Testing & Validation**
   - Red-team RAG systems with poisoned content
   - Test backdoor detection effectiveness
   - Validate defense mechanisms
   - Create attack simulation scenarios

### 4.3 Long-Term Program (Months 1-6)

1. **Continuous Monitoring**
   - Real-time anomaly detection
   - Automated response playbooks
   - Regular model verification testing
   - Quarterly threat assessments

2. **Defense Maturation**
   - Implement forensic traceback (RAGForensics-style)
   - Deploy semantic vetting for tool integration
   - Establish supply chain verification workflow
   - Build fine-tuning risk assessment

3. **Research Integration**
   - Monitor emerging attacks (visual RAG, MCP poisoning)
   - Stay current with defense techniques
   - Participate in threat sharing communities
   - Conduct periodic red-team exercises

---

## 5. Critical Gaps & Challenges

### 5.1 Detection Challenges

1. **Supply Chain Indistinguishability**
   - TransTroj designed to be undetectable in embedding space
   - No known method to reliably distinguish poisoned from clean
   - Requires control test cases or behavioral analysis

2. **Constant-Cost Poisoning**
   - Only ~250 documents needed to poison any LLM
   - Not scalable problem (size doesn't help)
   - Existing defenses ineffective at this scale

3. **Defense Circumvention**
   - Unlearning defeated by 16 steps fine-tuning
   - Trigger detection avoidable with careful design
   - Adversarial training not proven robust

4. **Emerging Attack Surfaces**
   - Visual RAG poisoning (1 image DoS)
   - Tool poisoning in MCP (immature defense landscape)
   - Code poisoning in development pipelines

### 5.2 Research Gaps

1. **Attribution & Forensics**
   - Limited methods to trace poisoned content origin
   - No definitive way to identify attacker
   - Supply chain contamination hard to localize

2. **Robust Defense**
   - No defense achieves high effectiveness against all attacks
   - Trade-offs between detectability and stealth
   - Scalability concerns for enterprise monitoring

3. **Real-World Deployment**
   - Most research uses synthetic data
   - Real-world poisoning scenarios understudied
   - Detection latency in production systems unclear

---

## 6. Metrics & KPIs for Monitoring

### 6.1 Model Integrity Metrics

| Metric | Baseline | Warning | Critical |
|--------|----------|---------|----------|
| Knowledge Base Doc Anomaly Score | <0.05 | 0.05-0.15 | >0.15 |
| Embedding Statistics Variance | <0.1 | 0.1-0.3 | >0.3 |
| Retrieval Pattern Consistency | >0.95 | 0.85-0.95 | <0.85 |
| Activation Entropy | Known range | ±2σ | >3σ |
| Control Test Case Accuracy | >0.98 | 0.95-0.98 | <0.95 |

### 6.2 Supply Chain Metrics

| Metric | Check | Frequency |
|--------|-------|-----------|
| Model Checksum Validation | SHA256 match | Per deployment |
| Signature Verification | RSA/Sigstore | Per deployment |
| Format Validation | Non-pickle | Per import |
| Age of Model | Days since publication | Continuous |
| Download Source Verification | Official repository | Per acquisition |

### 6.3 Training Data Metrics

| Metric | Check | Frequency |
|--------|-------|-----------|
| Token Frequency Anomalies | Statistical test | Per training batch |
| Data Quality Score | Document validation | Per document |
| Poisoning Rate Estimate | Outlier detection | Per epoch |
| Training Loss Anomalies | Against baseline | Per iteration |

---

## 7. Incident Response Playbook

### 7.1 Detection to Response Timeline

**T+0: Anomaly Detected**
- Alert triggered by automated system
- Initial assessment of severity
- Notify security team

**T+5 min: Containment**
- Isolate affected models
- Pause critical deployments
- Begin investigation

**T+1 hour: Analysis**
- Determine attack type from signatures
- Identify poisoned content/parameters
- Assess blast radius

**T+2-4 hours: Remediation**
- Remove poisoned content (RAG)
- Restore from clean backup (models)
- Verify through testing

**T+24 hours: Forensics**
- Traceback poisoned documents
- Identify supply chain entry point
- Document attack pattern

**T+1 week: Hardening**
- Deploy additional monitoring
- Implement targeted defenses
- Share threat intelligence

---

## 8. Recommended Reading Order by Role

### For Security Operations
1. 2505.22778 (Supply chain overview)
2. 2507.08862 (RAG attacks)
3. 2502.05224 (Backdoor survey)
4. 2504.21668 (Detection system)

### For Model Engineers
1. 2510.07192 (Constant-cost poisoning)
2. 2502.05209 (Model tampering)
3. 2501.03272 (Defense mechanism)
4. 2401.15883 (Supply chain backdoors)

### For Data/ML Ops
1. 2505.18543 (Benchmark)
2. 2504.03957 (Practical attacks)
3. 2503.09302 (Anomaly detection)
4. 2412.16708 (RAG robustness)

### For Threat Intelligence
1. 2502.05224 (Comprehensive survey)
2. 2505.22778 (Supply chain threats)
3. 2403.03593 (Malware in models)
4. 2512.06556 (Emerging protocols)

---

## 9. Conclusion

The research landscape reveals a critical vulnerability window:

**Key Findings**:
- RAG systems are extremely vulnerable (90%+ attack success)
- Supply chain attacks are undetectable by embedding analysis
- LLMs require only ~250 poisoned documents regardless of size
- Defenses can be circumvented with minimal fine-tuning
- Emerging attacks (visual RAG, MCP) have limited defense research

**Implication**: Defensive monitoring must focus on:
1. **Access control** (prevent poisoned data injection)
2. **Behavioral analysis** (detect attack success indicators)
3. **Supply chain verification** (validate model authenticity)
4. **Rapid forensics** (identify and localize contamination)

**Timeline**: Implementation should prioritize RAG systems first (highest vulnerability), followed by supply chain verification, then LLM backdoor monitoring.

---

**Report Generated**: January 5, 2026
**Data Sources**: 19 peer-reviewed ArXiv papers (2024-2025)
**Classification**: Research-based Threat Intelligence
**Confidence Level**: HIGH (based on peer-reviewed research)

---
