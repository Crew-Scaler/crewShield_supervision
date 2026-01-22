# Topic 11 Research Index: MCP and A2A Protocol Security

## Quick Reference Guide

### Critical Papers for MCP Security Understanding

#### Governance & Risk Management
- **[4]** Securing the Model Context Protocol (MCP): Risks, Controls, and Governance (2511.20920v1)
- **[12]** Systematization of Knowledge: Security and Safety in MCP Ecosystem (2512.08290v2)

#### Attack Analysis & Threat Modeling
- **[1]** IntentMiner: Intent Inversion Attack (2512.14166v1) - Privacy threats
- **[2]** Securing MCP: Tool Poisoning, Shadowing, Rug Pulls (2512.06556v1) - Semantic attacks
- **[3]** LeechHijack: Computational Resource Exploitation (2512.02321v1) - Implicit toxicity
- **[11]** ASTRIDE: Threat Modeling for Agentic-AI (2512.04785v1) - Extended STRIDE framework

#### Defense Mechanisms & Access Control
- **[7]** Securing AI Agent Execution (AgentBound) (2510.21236v2) - Declarative access control
- **[8]** AegisMCP: Online Graph Intrusion Detection (2510.19462v2) - Edge-based detection
- **[6]** MCPGuard: Detecting Vulnerabilities (2510.23673v1) - Automated scanning

#### Evaluation & Benchmarking
- **[9]** MCP-SafetyBench (2512.15163v1) - Comprehensive safety evaluation
- **[10]** MCPZoo (2512.15144v2) - Large-scale MCP dataset
- **[5]** MCP-RiskCue (2511.05867v2) - System log risk analysis

#### Multi-Agent Communication Security
- **[13]** Decentralized Multi-Agent System with Trust-Aware Communication (2512.02410v1)
- **[14]** MALCDF: Distributed Multi-Agent LLM Framework (2512.14846v1)
- **[15]** Quantigence: Multi-Agent Framework for Quantum Security (2512.12989v1)
- **[16]** Security Risks of Agentic Vehicles (2512.17041v1)
- **[17]** Coordinated Anti-Jamming Resilience via MARL (2512.16813v1)
- **[18]** XAMT: Bilevel Optimization for Memory Tampering (2512.15790v1)

---

## Paper Mapping by Topic

### Configuration Hardening (Primary Focus)
Papers directly addressing MCP configuration security:
- [4] - Governance and control frameworks
- [7] - Access control configuration (AgentBound)
- [8] - Runtime configuration monitoring
- [6] - Vulnerability detection in configurations

### Vulnerability Discovery
Papers identifying new threat vectors:
- [1] - Intent Inversion (privacy via logs)
- [2] - Semantic attacks (tool poisoning)
- [3] - Resource exploitation
- [11] - AI-specific threat models

### Incident Detection & Response
Papers for real-time defense:
- [8] - AegisMCP (online detection)
- [5] - MCP-RiskCue (log analysis)
- [14] - MALCDF (coordinated defense)
- [12] - SoK (defense roadmap)

### Benchmarking & Standardization
Papers for validation and testing:
- [9] - MCP-SafetyBench (20 attack types)
- [10] - MCPZoo (server dataset)
- [5] - MCP-RiskCue (risk benchmark)

---

## Key Metrics from Papers

| Paper | Primary Focus | Key Metric | Value |
|-------|---------------|-----------|-------|
| [1] IntentMiner | Intent recovery | Semantic alignment | 85%+ |
| [2] Securing MCP | Tool poisoning defense | GPT-4 block rate | 71% |
| [3] LeechHijack | Attack success rate | Exploitation success | 77.25% |
| [5] MCP-RiskCue | Risk detection | Accuracy (Llama3.1-8B) | 83% |
| [7] AgentBound | Policy generation | Accuracy on 296 servers | 80.9% |
| [8] AegisMCP | Detection latency | Per-window inference | <1 second |
| [9] MCP-SafetyBench | Attack taxonomy | Number of attack types | 20 |
| [10] MCPZoo | Dataset size | Servers in dataset | 95,142 |
| [14] MALCDF | Detection accuracy | CICIDS2017 accuracy | 90% |
| [17] XAMT | Poison rate | MARL agents | <1% |
| [17] XAMT | Poison rate | RAG agents | <0.1% |

---

## Author Affiliations (Identified)

### Frequently Cited Names
- Shiva Gaire, Srijan Gyawali, Saroj Mishra (SoK authors)
- Yunhao Yao, Zhiqiang Wang, Haoran Cheng (IntentMiner)
- Bin Wang, Zexin Liu, Hao Yu (MCPGuard)
- Christoph Bühler, Matteo Biagiola, Luca Di Grazia (AgentBound)

---

## ArXiv Categories Represented

| Category | Papers | Focus |
|----------|--------|-------|
| cs.CR | 11 | Cryptography & Security |
| cs.MA | 2 | Multiagent Systems |
| cs.AI | 2 | Artificial Intelligence |
| cs.CL | 1 | Computation & Language |
| cs.NI | 1 | Networking & Internet |

---

## Timeline (All 2025)

### December 2025 (Latest)
- [1] Dec 16 - IntentMiner
- [9] Dec 17 - MCP-SafetyBench
- [10] Dec 17/18 - MCPZoo
- [16] Dec 18 - Agentic Vehicles
- [17] Dec 18 - Anti-Jamming Resilience

### November 2025
- [4] Nov 25 - MCP Risks & Governance
- [5] Nov 8/12 - MCP-RiskCue

### October 2025
- [6] Oct 27 - MCPGuard
- [7] Oct 24/29 - AgentBound
- [8] Oct 22/25 - AegisMCP

### Late November/Early December 2025
- [2] Dec 6 - Tool Poisoning Defense
- [3] Dec 2 - LeechHijack
- [11] Dec 4 - ASTRIDE
- [12] Dec 9/13 - SoK
- [13] Dec 2 - Decentralized Multi-Agent
- [14] Dec 16 - MALCDF
- [15] Dec 15 - Quantigence
- [18] Dec 15 - XAMT

---

## File Size Distribution

| Size Category | Count | Examples |
|---------------|-------|----------|
| < 200 KB | 4 | MCPGuard, MCPZoo |
| 200-800 KB | 7 | MCP-Governance, Quantigence |
| 800 KB - 2 MB | 4 | AegisMCP, LeechHijack |
| 2-7 MB | 3 | SoK, MCP-SafetyBench, Tool Poisoning |
| > 10 MB | 1 | Tool Poisoning (15 MB) |

**Total Size**: 37 MB across 18 PDFs

---

## Recommended Reading Order

### For Configuration Hardening Focus
1. [4] Risks, Controls, and Governance (foundational)
2. [7] AgentBound (practical access control)
3. [8] AegisMCP (runtime monitoring)
4. [6] MCPGuard (vulnerability detection)
5. [12] SoK (comprehensive overview)

### For Threat Understanding
1. [11] ASTRIDE (threat modeling)
2. [1] IntentMiner (privacy attacks)
3. [2] Tool Poisoning (semantic attacks)
4. [3] LeechHijack (resource attacks)
5. [12] SoK (attack taxonomy)

### For Defense Implementation
1. [2] Tool Poisoning Defense (security framework)
2. [7] AgentBound (access control)
3. [8] AegisMCP (intrusion detection)
4. [5] MCP-RiskCue (log analysis)
5. [14] MALCDF (coordinated defense)

### For Benchmarking/Evaluation
1. [9] MCP-SafetyBench (safety metrics)
2. [10] MCPZoo (test environment)
3. [5] MCP-RiskCue (risk scoring)

---

## Research Gaps Identified Across Papers

1. **Formal Verification** - Need for formal methods in dynamic MCP systems
2. **Privacy-Preserving Execution** - Agent operations without data leakage
3. **Verifiable Registries** - Cryptographic authentication of MCP server sources
4. **Cross-Protocol Security** - Interactions between MCP and other protocols
5. **Configuration Best Practices** - Industry standards for secure MCP deployment
6. **Incident Response Procedures** - Post-breach recovery and forensics
7. **Supply Chain Verification** - Developer authentication and code signing

---

## Notes

- All papers are from 2025, indicating active research frontier
- High concentration on MCP reflects its emergence as AI agent standard
- Growing focus on multi-agent security reflects industry transition
- Benchmarking infrastructure (MCPZoo, MCP-SafetyBench) enabling rapid advancement
- Governance frameworks maturing (ASTRIDE extends STRIDE, mentions NIST AI RMF)
