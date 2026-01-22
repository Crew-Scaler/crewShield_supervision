# Top Papers Quick Reference: AI Agent Behavioral Anomaly Detection

**Research Date:** December 11, 2025
**Focus:** Issue #16 - Behavioral baseline construction, poisoning attacks, drift validation, context-aware auth

---

## Priority Reading List (Top 15 Papers)

### 1. Model Drift & Baseline Degradation (HIGHEST PRIORITY)

#### DAO-GP: Drift Aware Online Non-Linear Regression Gaussian-Process
- **ArXiv:** https://arxiv.org/abs/2512.08879v1
- **Published:** 2025-12-09
- **Relevance:** 10.5 (HIGHEST)
- **File:** `2512.08879v1_DAO-GP Drift Aware Online Non-Linear Regression Gaussian-Process.pdf`
- **Why Critical:** Dynamic hyperparameter adaptation for evolving data distributions, directly addresses drift-aware detection
- **Key Topics:** Concept drift, online learning, Gaussian processes, temporal dynamics
- **Priority:** **MUST READ** for drift rate validation

#### ARES: Anomaly Recognition Model For Edge Streams
- **ArXiv:** https://arxiv.org/abs/2511.22078v1
- **Published:** 2025-11-27
- **Relevance:** 10.0
- **File:** `2511.22078v1_ARES_ Anomaly Recognition Model For Edge Streams.pdf`
- **Why Critical:** Real-time anomaly detection with concept drift handling, large data volumes
- **Key Topics:** Temporal graphs, edge streams, real-time detection, concept drift
- **Priority:** **MUST READ** for real-time behavioral monitoring

#### CITADEL: Semi-Supervised Active Learning for Malware Detection Under Continuous Drift
- **ArXiv:** https://arxiv.org/abs/2511.11979v1
- **Published:** 2025-11-15
- **Relevance:** 8.0
- **File:** `2511.11979v1_CITADEL_ A Semi-Supervised Active Learning Framework for Malware Detection Under Continuous Distribu.pdf`
- **Why Critical:** 12-year longitudinal dataset (LAMDA), continuous distribution drift, active learning approach
- **Key Topics:** Concept drift, malware detection, semi-supervised learning, temporal evolution
- **Priority:** **MUST READ** for long-term drift patterns

---

### 2. Context-Aware Authentication (HIGHEST IMPACT)

#### Adaptive Authentication for EVs Using AI
- **ArXiv:** https://arxiv.org/abs/2508.17854v1
- **Published:** 2025-08-26
- **Relevance:** 10.0
- **File:** `2508.17854v1_Addressing Weak Authentication like RFID_ NFC in EVs and EVCs using AI-powered Adaptive Authentica.pdf`
- **Why Critical:** ONLY paper on context-aware adaptive authentication with AI, directly applicable to agent systems
- **Key Topics:** Adaptive authentication, context-aware security, weak protocol enhancement
- **Priority:** **MUST READ** for context-aware agent authentication

#### Sentinel Agents for Secure and Trustworthy Agentic AI
- **ArXiv:** https://arxiv.org/abs/2509.13989v1
- **Published:** 2025-09-18
- **Relevance:** 9.0
- **File:** `2509.13989v1_Sentinel Agents for Secure and Trustworthy Agentic AI in Multi-Agent Systems.pdf`
- **Why Critical:** Dedicated monitoring agents for multi-agent systems, real-time behavioral verification
- **Key Topics:** Multi-agent systems, sentinel monitoring, trustworthy AI, agent security
- **Priority:** **MUST READ** for agent-specific security

#### Zero-Trust Foundation Models for AI in IoT
- **ArXiv:** https://arxiv.org/abs/2505.17355v1
- **Published:** 2025-05-26
- **Relevance:** 7.5
- **File:** `2505.17355v1_Zero-Trust Foundation Models_ A New Paradigm for Secure and Collaborative Artificial Intelligence .pdf`
- **Why Critical:** Zero-trust paradigm for AI systems, collaborative security model
- **Key Topics:** Zero-trust architecture, AI security, foundation models, IoT
- **Priority:** **SHOULD READ** for trust frameworks

---

### 3. Baseline Poisoning & Adversarial Attacks (THREAT MODELING)

#### Adversarial Attacks for Drift Detection
- **ArXiv:** https://arxiv.org/abs/2411.16591v2
- **Published:** 2024-11-25
- **Relevance:** 7.0
- **File:** `2411.16591v2_Adversarial Attacks for Drift Detection.pdf`
- **Why Critical:** Demonstrates construction of UNDETECTABLE drifts, direct threat to baseline integrity
- **Key Topics:** Adversarial drift, evasion attacks, drift detector weaknesses
- **Priority:** **MUST READ** for threat understanding

#### Augmented Neural Fine-Tuning for Efficient Backdoor Purification
- **ArXiv:** https://arxiv.org/abs/2407.10052v2
- **Published:** 2024-07-14
- **Relevance:** 9.5
- **File:** `2407.10052v2_Augmented Neural Fine-Tuning for Efficient Backdoor Purification.pdf`
- **Why Critical:** Backdoor attacks on DNNs, purification mechanisms, defense strategies
- **Key Topics:** Backdoor attacks, neural fine-tuning, DNN vulnerabilities, defense
- **Priority:** **MUST READ** for baseline poisoning defense

#### Mitigating Spurious Negative Pairs for Robust Industrial Anomaly Detection
- **ArXiv:** https://arxiv.org/abs/2501.15434v1
- **Published:** 2025-01-26
- **Relevance:** 7.0
- **File:** `2501.15434v1_Mitigating Spurious Negative Pairs for Robust Industrial Anomaly Detection.pdf`
- **Why Critical:** Adversarial robustness for AD, real-world applications (autonomous driving)
- **Key Topics:** Anomaly detection robustness, adversarial attacks, industrial applications
- **Priority:** **SHOULD READ** for robustness strategies

---

### 4. Baseline Construction Methods (IMPLEMENTATION)

#### THEMIS: Foundation Model Embeddings for Anomaly Detection
- **ArXiv:** https://arxiv.org/abs/2510.03911v1
- **Published:** 2025-10-04
- **Relevance:** 7.0
- **File:** `2510.03911v1_THEMIS_ Unlocking Pretrained Knowledge with Foundation Model Embeddings for Anomaly Detection in Time.pdf`
- **Why Critical:** Foundation model approach to baseline construction, handles concept drift
- **Key Topics:** Foundation models, time series, anomaly detection, pretrained knowledge
- **Priority:** **MUST READ** for ML-based baseline construction

#### Encode Me If You Can: Universal User Representations via Autoencoding
- **ArXiv:** https://arxiv.org/abs/2508.07748v1
- **Published:** 2025-08-11
- **Relevance:** 6.0
- **File:** `2508.07748v1_Encode Me If You Can_ Learning Universal User Representations via Event Sequence Autoencoding.pdf`
- **Why Critical:** Event sequence autoencoding for universal representations, task-independent
- **Key Topics:** Autoencoding, behavioral profiling, user representation, sequence learning
- **Priority:** **SHOULD READ** for baseline construction methodology

#### Agent-Based Modeling for Continuous Authentication
- **ArXiv:** https://arxiv.org/abs/2505.05527v1
- **Published:** 2025-05-08
- **Relevance:** 6.5
- **File:** `2505.05527v1_An Agent-Based Modeling Approach to Free-Text Keyboard Dynamics for Continuous Authentication.pdf`
- **Why Critical:** Agent-based approach to behavioral authentication, continuous monitoring
- **Key Topics:** Agent-based modeling, continuous authentication, keyboard dynamics
- **Priority:** **SHOULD READ** for behavioral baseline construction

---

### 5. Additional High-Impact Papers (Relevance ≥ 8.0)

#### Multi-Agent LLM Defense Pipeline Against Prompt Injection
- **ArXiv:** https://arxiv.org/abs/2509.15815v2
- **Published:** 2025-09-16
- **Relevance:** 8.0
- **File:** `2509.15815v2_A Multi-Agent LLM Defense Pipeline Against Prompt Injection Attacks.pdf`
- **Why Critical:** Multi-agent defense, LLM security, behavioral monitoring for attack detection
- **Key Topics:** Multi-agent systems, LLM security, prompt injection, defense pipeline

#### Combating Concept Drift with Explanatory Detection for Android Malware
- **ArXiv:** https://arxiv.org/abs/2405.04095v3
- **Published:** 2024-05-07
- **Relevance:** 8.5
- **File:** `2405.04095v3_Combating Concept Drift with Explanatory Detection and Adaptation for Android Malware Classification.pdf`
- **Why Critical:** Explanatory drift detection, adaptation strategies, real-world malware evolution
- **Key Topics:** Concept drift, explainability, malware detection, adaptation

#### What Lurks Within? Concept Auditing for Shared Diffusion Models
- **ArXiv:** https://arxiv.org/abs/2504.13408v1
- **Published:** 2025-04-21
- **Relevance:** 8.5
- **File:** `2504.13408v1_What Lurks Within_ Concept Auditing for Shared Diffusion Models at Scale.pdf`
- **Why Critical:** Concept auditing at scale, behavioral monitoring for AI models
- **Key Topics:** Concept auditing, diffusion models, monitoring, behavioral analysis

---

## Reading Priority Matrix

### IMMEDIATE (Next 24-48 Hours)

**For Drift Rate Validation:**
1. DAO-GP (2512.08879v1) - Quantitative drift metrics
2. ARES (2511.22078v1) - Real-time drift handling
3. CITADEL (2511.11979v1) - Long-term drift patterns

**For Agent Authentication:**
4. Adaptive Authentication for EVs (2508.17854v1) - Context-aware frameworks
5. Sentinel Agents (2509.13989v1) - Multi-agent monitoring

**For Threat Modeling:**
6. Adversarial Attacks for Drift Detection (2411.16591v2) - Baseline poisoning
7. Backdoor Purification (2407.10052v2) - Defense mechanisms

### SHORT TERM (Week 1)

**For Baseline Construction:**
8. THEMIS (2510.03911v1) - Foundation model approach
9. Universal User Representations (2508.07748v1) - Autoencoding methods
10. Agent-Based Authentication (2505.05527v1) - Continuous monitoring

**For Additional Context:**
11. Multi-Agent LLM Defense (2509.15815v2) - Agent-specific security
12. Zero-Trust Foundation Models (2505.17355v1) - Trust frameworks
13. Concept Drift Combat (2405.04095v3) - Adaptation strategies

### MEDIUM TERM (Week 2)

**For Comprehensive Understanding:**
14. Concept Auditing (2504.13408v1) - Behavioral monitoring at scale
15. Industrial Anomaly Detection (2501.15434v1) - Robustness strategies

**Additional Drift Papers (Select 5-10):**
- METANOIA (2501.00471v1) - Lifelong intrusion detection
- Fair Credit Scoring (2511.03807v1) - Drift in evolving populations
- Multi-grained Cellular Traffic (2508.00863v1) - Spatial-temporal features
- Adaptive Anomaly Detection (2506.13018v2) - Concept drift presence

---

## Research Question Mapping

### Q1: How do we construct behavioral baselines for non-human agents?

**Primary Papers:**
- THEMIS (2510.03911v1) - Foundation model embeddings
- Encode Me If You Can (2508.07748v1) - Event sequence autoencoding
- Agent-Based Authentication (2505.05527v1) - Agent-based modeling

**Methodology Extraction:**
1. Read THEMIS for foundation model approach
2. Read Encode Me for autoencoding architecture
3. Synthesize for agent-specific implementation

---

### Q2: What are baseline poisoning attack vectors and success rates?

**Primary Papers:**
- Adversarial Attacks for Drift Detection (2411.16591v2) - Undetectable drift construction
- Backdoor Purification (2407.10052v2) - Backdoor attack mechanisms
- Industrial Anomaly Detection (2501.15434v1) - Adversarial robustness challenges

**Analysis Approach:**
1. Document attack mechanisms from 2411.16591v2
2. Extract defense strategies from 2407.10052v2
3. Identify robustness gaps from 2501.15434v1

---

### Q3: What are the actual model drift rates for behavioral baselines?

**Primary Papers:**
- DAO-GP (2512.08879v1) - Drift-aware online learning
- ARES (2511.22078v1) - Edge stream drift handling
- CITADEL (2511.11979v1) - 12-year malware drift study
- METANOIA (2501.00471v1) - Lifelong drift mitigation

**Extraction Protocol:**
1. Full-text analysis of experimental results sections
2. Extract numeric drift rates with temporal granularity
3. Categorize by domain (malware, network, behavioral)
4. Calculate average monthly degradation
5. Validate 2-5% monthly claim

---

### Q4: How do we implement context-aware authentication for agents?

**Primary Papers:**
- Adaptive Authentication for EVs (2508.17854v1) - AI-powered adaptive auth
- Sentinel Agents (2509.13989v1) - Real-time agent monitoring
- Zero-Trust Foundation Models (2505.17355v1) - Zero-trust for AI
- Agent-Based Authentication (2505.05527v1) - Continuous behavioral auth

**Framework Synthesis:**
1. Extract adaptive auth framework from 2508.17854v1
2. Apply sentinel monitoring pattern from 2509.13989v1
3. Integrate zero-trust principles from 2505.17355v1
4. Adapt continuous auth from 2505.05527v1

---

## Evidence Extraction Checklist

### For Each Priority Paper, Extract:

#### Methodology
- [ ] Baseline construction approach
- [ ] Feature engineering techniques
- [ ] Model architecture (if applicable)
- [ ] Training data requirements
- [ ] Computational complexity

#### Empirical Results
- [ ] Accuracy, precision, recall, F1-score
- [ ] False positive rate (FPR)
- [ ] False negative rate (FNR)
- [ ] Detection latency
- [ ] Drift adaptation time

#### Drift Metrics (if applicable)
- [ ] Numeric drift percentage
- [ ] Temporal granularity (daily, weekly, monthly)
- [ ] Domain-specific variations
- [ ] Degradation curve characteristics

#### Attack/Defense (if applicable)
- [ ] Attack success rate
- [ ] Evasion techniques
- [ ] Defense effectiveness
- [ ] Computational overhead of defense

#### Deployment Evidence
- [ ] Real-world deployment mention
- [ ] Production system integration
- [ ] Case study details
- [ ] Performance under production conditions

---

## Key Findings Summary by Paper

### DAO-GP (2512.08879v1)
**Expected Findings:**
- Dynamic hyperparameter adaptation for drift
- Non-linear regression under evolving distributions
- Quantitative drift metrics (TARGET: monthly rates)

**Action Items:**
- Extract specific drift percentages from experiments
- Document adaptation frequency
- Note computational overhead

---

### ARES (2511.22078v1)
**Expected Findings:**
- Real-time anomaly detection in temporal graphs
- Concept drift handling mechanisms
- Scalability for large data volumes

**Action Items:**
- Extract edge stream drift rates
- Document real-time detection latency
- Note false positive/negative rates

---

### Adversarial Attacks for Drift Detection (2411.16591v2)
**Expected Findings:**
- Methods to construct undetectable drifts
- Drift detector vulnerabilities
- Attack success rates

**Action Items:**
- Document attack construction methodology
- Identify detector weaknesses exploited
- Extract attack success percentages

---

### Adaptive Authentication for EVs (2508.17854v1)
**Expected Findings:**
- Context-aware authentication framework
- AI-powered adaptive decision-making
- Weak protocol enhancement strategies

**Action Items:**
- Extract authentication framework architecture
- Document context factors used
- Note adaptation mechanisms

---

### Sentinel Agents (2509.13989v1)
**Expected Findings:**
- Multi-agent monitoring architecture
- Real-time behavioral verification methods
- Trust and security mechanisms for agents

**Action Items:**
- Document sentinel agent design pattern
- Extract behavioral verification approach
- Note scalability characteristics

---

## Paper Organization Strategy

### Physical Organization
```
behavioral_detection/
├── EXECUTIVE_SUMMARY.md (this file)
├── RESEARCH_ANALYSIS.md (full analysis)
├── TOP_PAPERS_QUICK_REFERENCE.md (priority reading)
├── papers_metadata.json (all paper metadata)
├── search_cache.json (search history)
│
├── priority_1_must_read/ (create folder for top 7 papers)
│   ├── 2512.08879v1_DAO-GP.pdf
│   ├── 2511.22078v1_ARES.pdf
│   ├── 2511.11979v1_CITADEL.pdf
│   ├── 2508.17854v1_Adaptive_Auth.pdf
│   ├── 2509.13989v1_Sentinel_Agents.pdf
│   ├── 2411.16591v2_Adversarial_Drift.pdf
│   └── 2407.10052v2_Backdoor_Purification.pdf
│
├── priority_2_should_read/ (create folder for next 8 papers)
└── priority_3_reference/ (remaining 30 papers)
```

### Digital Organization
1. **Annotate PDFs** with highlights for:
   - Drift rate metrics (yellow)
   - Attack mechanisms (red)
   - Defense strategies (green)
   - Baseline construction methods (blue)

2. **Create extraction spreadsheet:**
   - Paper ID | Title | Drift Rate | FPR/FNR | Attack Success | Defense Effectiveness

3. **Document findings:**
   - One-page summary per priority paper
   - Evidence matrix linking papers to claims
   - Gap analysis for missing evidence

---

## Quick Stats Reference

### Overall Corpus
- **Total Papers:** 45
- **2025 Papers:** 29 (64%)
- **2024 Papers:** 16 (36%)
- **Average Relevance Score:** 6.8/10
- **Empirical Studies:** 30 (67%)

### By Research Objective
- **Baseline Construction:** 3 papers (7%)
- **Poisoning Attacks:** 4 papers (9%)
- **Model Drift:** 29 papers (64%)
- **Context-Aware Auth:** 1 paper (2%)
- **Agent-Specific:** 2 papers (4%)

### By Relevance Tier
- **Tier 1 (9.0-10.5):** 5 papers (11%)
- **Tier 2 (7.0-8.9):** 12 papers (27%)
- **Tier 3 (5.0-6.9):** 18 papers (40%)
- **Tier 4 (3.0-4.9):** 10 papers (22%)

---

## Next Actions Checklist

### Immediate (Today)
- [ ] Organize papers into priority folders
- [ ] Start reading DAO-GP for drift metrics
- [ ] Extract baseline construction methods from THEMIS
- [ ] Document adversarial attack vectors from 2411.16591v2

### Short Term (This Week)
- [ ] Complete reading of 7 MUST READ papers
- [ ] Extract quantitative metrics from drift papers
- [ ] Create evidence matrix for Issue #16 claims
- [ ] Document research gaps and opportunities

### Medium Term (Next Week)
- [ ] Full-text analysis of remaining high-priority papers
- [ ] Synthesize findings into architectural recommendations
- [ ] Validate 2-5% monthly drift claim
- [ ] Design agent-specific behavioral authentication framework

### Long Term (Next 2 Weeks)
- [ ] Complete evidence extraction from all 45 papers
- [ ] Generate comprehensive validation report for Issue #16
- [ ] Identify additional research needs
- [ ] Propose implementation roadmap

---

*Quick reference guide for Issue #16 research - Start with the 7 MUST READ papers for maximum impact*
