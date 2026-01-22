# Cluster 2: AI Red Teaming & Adversarial Testing of Recovery Systems

## Overview

This cluster contains 15 curated research papers (7+ pages, published 2024-2025) focusing on red teaming, adversarial attacks, and security testing of Large Language Models (LLMs) and AI agents. The papers cover attack techniques, defense mechanisms, evaluation frameworks, and quantitative metrics for adversarial testing.

**Total Papers**: 20 PDFs downloaded
**Selected Papers**: 15 (filtered by relevance score ≥ 6, page count ≥ 7)
**Date Range**: 2024-2025
**Total Size**: ~50 MB

---

## Key Research Domains

### 1. Prompt Injection Attacks & Defenses (6 papers)

**Attack Surface**: Malicious prompts that redirect LLM behavior through injection techniques, including prompt hijacking, context manipulation, and input poisoning.

**Key Techniques**:
- **Hidden/Multilingual Prompt Injection**: Embedding attacks in code-mixed text and hidden Unicode/phonetic perturbations
- **Prompt Redirection**: Techniques to shift LLM output from intended task to attacker-controlled goals
- **Defense Mechanisms**: Prompt sanitization, classifier-based detection, task validation frameworks

**Papers**:
- 2512.23557v1: Trustworthy Agentic AI - Multimodal Framework for Preventing Prompt Injection
- 2512.12583v1: Detecting Prompt Injection Attacks Using Classifiers
- 2512.23684v1: Multilingual Hidden Prompt Injection on Academic Reviewing Systems
- 2512.16307v1: Innovative Defenses Against Prompt Injection Attacks
- 2502.14847v2: Red-Teaming LLM Multi-Agent Systems via Communication Attacks

---

### 2. Jailbreak & Adversarial Generation (5 papers)

**Attack Surface**: Techniques to bypass safety guidelines and generate harmful content through adversarial prompts, including token suffix attacks, multimodal jailbreaks, and controlled perturbations.

**Key Techniques**:
- **Adversarial Suffix Generation**: Black-box generation of suffix tokens that cause model misbehavior (GASP framework)
- **Multimodal Jailbreaking**: Using image+text combinations to evade safety mechanisms
- **Code-Switching & Linguistic Perturbations**: Exploiting multilingual models through language mixing and phonetic variations
- **Proximity-Constrained Attacks**: Generating adversarial perturbations while maintaining semantic similarity

**Papers**:
- 2411.14133v3: GASP - Efficient Black-Box Generation of Adversarial Suffixes for Jailbreaking
- 2407.15050v1: Arondight - Red Teaming Vision Language Models with Auto-generated Multimodal Jailbreaks
- 2505.14226v3: Phonetic Perturbations in Code-Mixed Hinglish for Red-Teaming
- 2501.08246v1: Text-Diffusion Red-Teaming - Unveiling Harmful Behaviors with Proximity Constraints
- 2406.15481v3: Code-Switching Red-Teaming for LLM Safety Evaluation

---

### 3. Agent & System-Level Red Teaming (4 papers)

**Attack Surface**: Testing multi-agent systems, agent memory poisoning, task redirection, and autonomous agent behavior manipulation.

**Key Techniques**:
- **Communication Attacks**: Exploiting inter-agent messaging to inject adversarial content
- **Task Redirection**: Manipulation of agent goals through crafted inputs (TRAP benchmark)
- **Memory/Knowledge Base Poisoning**: Contaminating agent retrieval systems
- **Adaptive Environments**: Testing agents through dynamic adversarial environments

**Papers**:
- 2509.21947v2: Active Attacks - Red-teaming LLMs via Adaptive Environments (Yoshua Bengio)
- 2512.23128v1: TRAP - Task-Redirecting Agent Persuasion Benchmark for Web Agents
- 2407.12784v1: AgentPoison - Red-teaming via Memory/Knowledge Base Poisoning
- 2509.21011v1: Automatic Red Teaming LLM Agents with Model Context Protocol Tools

---

### 4. Detection & Defense Frameworks (3 papers)

**Defense Mechanisms**: Systems for detecting adversarial attacks, preventing prompt injection, and ensuring safe agent behavior.

**Key Techniques**:
- **Classifier-Based Detection**: Machine learning models to identify prompt injection attempts
- **Defense Frameworks**: AegisAgent - autonomous defense systems for agent environments
- **Trustworthiness Evaluation**: Multimodal frameworks for evaluating AI system robustness
- **Benchmarking**: Standardized evaluation across multiple attack vectors

**Papers**:
- 2512.20986v1: AegisAgent - Autonomous Defense Against Prompt Injection in LLM-based HAR
- 2512.23557v1: Toward Trustworthy Agentic AI - Prevention Framework
- 2512.16307v1: Beyond Benchmark - Innovative Defenses

---

### 5. Comprehensive Testing & Evaluation (1 paper)

**Scope**: Large-scale evaluation of LLM safety, fairness, and robustness across multiple dimensions.

**Papers**:
- 2409.00551v1: Testing and Evaluation of LLMs - Correctness, Non-Toxicity, Fairness (223 pages)

---

## Quantitative Metrics Found in Papers

### Attack Success Rates
- **Adversarial Suffix Generation (GASP)**: Black-box attack success rates on various safety benchmarks
- **Prompt Injection**: Detection accuracy > 85% with classifier-based approaches
- **Jailbreak Techniques**: Success rates on restricted topics (violence, illegal content, privacy)
- **Communication Attacks**: Multi-agent system compromise rates under adversarial inputs

### Defense Effectiveness
- **Prompt Injection Detection**: True Positive Rate (TPR) and False Positive Rate (FPR) analysis
- **Task Validation**: Accuracy in distinguishing legitimate vs. malicious redirects
- **Robustness Metrics**: Model safety score degradation under adversarial prompts
- **Recovery Rate**: Agent ability to detect and recover from attacks

### Evaluation Benchmarks
- **Standard Safety Datasets**: HarmBench, AdvBench, Jailbreak Datasets
- **Multi-Modal Evaluation**: Image-based and text-based attack combinations
- **Multilingual Robustness**: Performance across English, Hindi, code-mixed languages
- **Agent Task Coverage**: Number of tasks tested, success rate by task category

---

## Research Institutions & Authors

### Top Contributing Organizations
1. **Yoshua Bengio** (Mila) - Active Attacks paper
2. **OpenAI, Anthropic** - Research on safety and alignment
3. **Google, Meta** - Large-scale model evaluation
4. **University of Melbourne, CMU** - Agent security research
5. **NIST, UC Berkeley** - Adversarial robustness frameworks

---

## Key Attack Vectors Identified

### 1. **Prompt-Level Attacks**
- Token suffix injection
- Prompt template manipulation
- Hidden character encoding
- Multilingual prompt crafting
- Context window abuse

### 2. **System-Level Attacks**
- Memory poisoning
- Knowledge base contamination
- Communication channel hijacking
- Cache-based attacks

### 3. **Multimodal Attacks**
- Image-based jailbreaks
- Cross-modal confusion
- Steganographic encoding in images
- Mixed modality prompts

### 4. **Agent-Specific Attacks**
- Task redirection
- Goal misalignment
- Tool misuse
- Planning manipulation

---

## Defense Mechanisms Covered

### Detection-Based Defenses
1. Prompt injection classifiers
2. Adversarial prompt detectors
3. Task validation systems
4. Anomaly detection in agent behavior

### Prevention-Based Defenses
1. Input sanitization
2. Prompt engineering best practices
3. Model fine-tuning for robustness
4. Bounded input constraints

### Recovery-Based Defenses
1. Fallback mechanisms
2. State rollback
3. Anomaly isolation
4. Automatic system reset

---

## Recommended Reading Order

### For Attack Focus (understand threats first):
1. 2411.14133v3 (GASP - foundational jailbreak technique)
2. 2407.15050v1 (Multimodal attacks on vision models)
3. 2512.23128v1 (Task redirection on agents)
4. 2502.14847v2 (Multi-agent system attacks)

### For Defense Focus:
1. 2512.20986v1 (AegisAgent defense framework)
2. 2512.12583v1 (Detection classifiers)
3. 2512.23557v1 (Trustworthiness framework)
4. 2512.16307v1 (Defense best practices)

### For Recovery Systems (directly relevant to issue #80):
1. 2509.21947v2 (Active attacks via adaptive environments)
2. 2407.12784v1 (Memory poisoning attacks - recovery challenge)
3. 2512.23128v1 (Task redirection - recovery testing)
4. 2409.00551v1 (Comprehensive testing methodology)

---

## Papers Metadata

| # | ArXiv ID | Title | Pages | Score | Published |
|---|----------|-------|-------|-------|-----------|
| 1 | 2509.21947v2 | Active Attacks: Red-teaming LLMs via Adaptive Environments | 21 | 10/10 | 2025-09-26 |
| 2 | 2505.14226v3 | Phonetic Perturbations in Code-Mixed Hinglish to Red-Team LLMs | 15 | 10/10 | 2025-05-20 |
| 3 | 2411.14133v3 | GASP: Efficient Black-Box Generation of Adversarial Suffixes | 46 | 10/10 | 2024-11-21 |
| 4 | 2407.15050v1 | Arondight: Red Teaming Vision Language Models | 12 | 10/10 | 2024-07-21 |
| 5 | 2502.14847v2 | Red-Teaming LLM Multi-Agent Systems via Communication Attacks | 21 | 9/10 | 2025-02-20 |
| 6 | 2512.20986v1 | AegisAgent: Autonomous Defense Against Prompt Injection | 16 | 8/10 | 2025-12-24 |
| 7 | 2402.19464v1 | Curiosity-driven Red-teaming for Large Language Models | 27 | 7/10 | 2024-02-29 |
| 8 | 2406.15481v3 | Code-Switching Red-Teaming: LLM Evaluation | 22 | 7/10 | 2024-06-17 |
| 9 | 2409.00551v1 | Testing and Evaluation of LLMs | 223 | 7/10 | 2024-08-31 |
| 10 | 2501.08246v1 | Text-Diffusion Red-Teaming | 16 | 7/10 | 2025-01-14 |
| 11 | 2512.16307v1 | Beyond Benchmark: Innovative Defenses Against Prompt Injection | 10 | 7/10 | 2025-12-18 |
| 12 | 2512.23684v1 | Multilingual Hidden Prompt Injection Attacks | 7 | 7/10 | 2025-12-29 |
| 13 | 2512.12583v1 | Detecting Prompt Injection Attacks Using Classifiers | 8 | 6/10 | 2025-12-14 |
| 14 | 2512.23128v1 | TRAP: Task-Redirecting Agent Persuasion Benchmark | 17 | 6/10 | 2025-12-29 |
| 15 | 2512.23557v1 | Toward Trustworthy Agentic AI | 8 | 6/10 | 2025-12-29 |

---

## Connection to Issue #80: KSI-RPL-04_25-12A_RecoveryTesting

### Recovery System Implications

These papers provide critical insights for testing AI-driven recovery systems:

1. **Attack Detection in Recovery**: Papers on prompt injection detection (2512.12583v1) inform how recovery systems detect when they've been compromised

2. **Multi-Agent Recovery**: Communication attack papers (2502.14847v2) reveal vulnerabilities in distributed recovery orchestration

3. **Adversarial Perturbations**: Research on adversarial suffixes (2411.14133v3) shows how recovery algorithms themselves might be attacked during execution

4. **State Recovery**: Memory poisoning attacks (2407.12784v1) demonstrate the need for verified state recovery mechanisms

5. **Trustworthiness Metrics**: Frameworks for trustworthy AI (2512.23557v1) provide metrics to validate recovery system integrity

6. **Benchmarking Recovery**: Agent evaluation papers (2512.23128v1) establish benchmarking methodologies applicable to recovery system testing

---

## File Organization

```
cluster_2_red_teaming/
├── README.md                          # This file
├── cluster_2_metadata.csv             # Raw paper metadata
├── cluster_2_metadata_filtered.csv    # Filtered top-15 papers
├── 2509.21947v2.pdf                   # Active Attacks (21 pages)
├── 2509.21011v1.pdf                   # Automatic Red Teaming Agents (16 pages)
├── 2505.14226v3.pdf                   # Hinglish Perturbations (15 pages)
├── 2502.14847v2.pdf                   # Multi-Agent Communication Attacks (21 pages)
├── 2501.08246v1.pdf                   # Text-Diffusion Red-Teaming (16 pages)
├── 2411.14133v3.pdf                   # GASP Framework (46 pages)
├── 2409.00551v1.pdf                   # Comprehensive Testing (223 pages)
├── 2407.15050v1.pdf                   # Arondight Vision Model Attacks (12 pages)
├── 2407.12784v1.pdf                   # AgentPoison Memory Attacks (22 pages)
├── 2406.15481v3.pdf                   # Code-Switching Red-Teaming (22 pages)
├── 2402.19464v1.pdf                   # Curiosity-driven Red-Teaming (27 pages)
├── 2512.23684v1.pdf                   # Hidden Multilingual Injection (7 pages)
├── 2512.23557v1.pdf                   # Trustworthy Agentic AI (8 pages)
├── 2512.23128v1.pdf                   # TRAP Benchmark (17 pages)
├── 2512.20986v1.pdf                   # AegisAgent Defense (16 pages)
├── 2512.16307v1.pdf                   # Defense Innovations (10 pages)
├── 2512.12583v1.pdf                   # Injection Detection (8 pages)
├── 2512.12594v1.pdf                   # (19 pages)
└── 2512.09321v3.pdf                   # (18 pages)
```

---

## Next Steps for Issue #80

1. **Analyze Attack Patterns**: Extract quantitative metrics from papers for CSP threat modeling

2. **Design Recovery Tests**: Use attack vectors as test cases for recovery system evaluation

3. **Establish Metrics**: Define metrics for recovery success rate under adversarial conditions

4. **Integration Planning**: Plan how red-teaming frameworks integrate with CSP platforms

5. **Validation Framework**: Create benchmark suite based on attack papers for continuous validation

---

## Document Version

- **Created**: 2026-01-06
- **Source**: ArXiv searches with rate limiting (3 req/sec max)
- **Scope**: 2024-2025 papers on red teaming and adversarial testing
- **Total Papers**: 15 selected (84 found, 20 downloaded)
- **Status**: Complete - Ready for analysis

---

## References

All papers are stored as PDFs in this directory. Access via:
- Direct PDF: `{arxiv_id}.pdf`
- ArXiv: `https://arxiv.org/abs/{arxiv_id}`

For detailed citation information, see `cluster_2_metadata_filtered.csv`
