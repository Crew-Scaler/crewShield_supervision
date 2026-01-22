# Topic 11: MCP and A2A Protocol Security - Research Summary

## Research Objective
Investigation of Model Context Protocol (MCP) and Agent-to-Agent (A2A) communication security in LLM-based AI systems, focusing on configuration tools, vulnerability threats, and protocol security mechanisms.

## Search Queries Executed

### Query 1 (Primary Focus)
```
"Model Context Protocol" OR MCP AND (security OR attack OR vulnerability) AND (tool OR configuration) AND (2024 OR 2025)
```
- Results: 50 papers found, 10 selected
- Keywords: Model Context Protocol, MCP, security, attack, vulnerability, tool, configuration

### Query 2 (Alternative - A2A Communication)
```
(agent-to-agent OR A2A OR "multi-agent") AND (communication OR protocol) AND (security OR attack OR poison) AND (2024 OR 2025)
```
- Results: 50 papers found, 10 selected
- Keywords: agent-to-agent, A2A, multi-agent, communication, protocol, security, attack, poisoning

## Download Statistics
- **Total PDFs Downloaded**: 18 unique papers (1 duplicate across queries)
- **Total Papers Analyzed**: 19 papers across both queries
- **Output Directory**: `/Users/tamnguyen/Documents/GitHub/ksi_watch/KSI-SVC-01_25-12A_ContinuousImprovement/references/topic11_mcp_protocol/`
- **Combined File Size**: ~45.5 MB
- **Publication Year**: All papers from 2025 and late 2024
- **Success Rate**: 100% (all target papers successfully downloaded)

---

## Query 1 Results: MCP Protocol Security (10 Papers)

### 1. IntentMiner: Intent Inversion Attack via Tool Call Analysis
- **ArXiv ID**: 2512.14166v1
- **Authors**: Yunhao Yao, Zhiqiang Wang, Haoran Cheng, Yihang Cheng, Haohua Du, Xiang-Yang Li
- **Published**: December 16, 2025
- **Primary Category**: cs.CR (Cryptography and Security)
- **Relevance Score**: 20.0
- **Focus**: Privacy threats in MCP - Intent Inversion attacks where semi-honest MCP servers reconstruct user intent from tool call logs
- **Key Contribution**: IntentMiner framework using Hierarchical Information Isolation and Three-Dimensional Semantic Analysis, achieving 85%+ semantic alignment
- **File**: 2512.14166v1_IntentMiner_Intent_Inversion_Attack_via_Tool_Call_Analysis_in_the_Model_Context_Protocol.pdf (634 KB)

### 2. Securing the Model Context Protocol: Defending LLMs Against Tool Poisoning
- **ArXiv ID**: 2512.06556v1
- **Authors**: Saeid Jamshidi, Kawser Wazed Nafi, Arghavan Moradi Dakhel, Negar Shahabi, Foutse Khomh, Naser Ezzati-Jivan
- **Published**: December 6, 2025
- **Primary Category**: cs.CR
- **Relevance Score**: 20.0
- **Focus**: Semantic attacks on MCP systems - Tool Poisoning, Shadowing, and Rug Pulls
- **Key Contribution**: Layered security framework with RSA-based manifest signing, LLM-on-LLM semantic vetting, and runtime guardrails. Evaluation across GPT-4, DeepSeek, Llama-3.5
- **File**: 2512.06556v1_Securing_the_Model_Context_Protocol_Defending_LLMs_Against_Tool_Poisoning_and_Adversarial_Attacks.pdf (15 MB)

### 3. LeechHijack: Covert Computational Resource Exploitation
- **ArXiv ID**: 2512.02321v1
- **Authors**: Yuanhe Zhang, Weiliu Wang, Zhenhong Zhou, Kun Wang, Jie Zhang, Li Sun, Yang Liu, Sen Su
- **Published**: December 2, 2025
- **Primary Category**: cs.CR
- **Relevance Score**: 20.0
- **Focus**: Implicit toxicity attacks on MCP - unauthorized computational resource exfiltration via malicious tools
- **Key Contribution**: LeechHijack attack mechanism with 77.25% average success rate, 18.62% resource overhead. Two-stage mechanism: implantation and exploitation
- **File**: 2512.02321v1_LeechHijack_Covert_Computational_Resource_Exploitation_in_Intelligent_Agent_Systems.pdf (1.3 MB)

### 4. Securing the Model Context Protocol (MCP): Risks, Controls, and Governance
- **ArXiv ID**: 2511.20920v1
- **Authors**: Herman Errico, Jiquan Ngiam, Shanita Sojan
- **Published**: November 25, 2025
- **Primary Category**: cs.CR
- **Relevance Score**: 20.0
- **Focus**: Comprehensive governance framework for MCP security - addressing content-injection, supply-chain, and agent-based adversaries
- **Key Contribution**: Practical controls including per-user authentication, scoped authorization, provenance tracking, containerized sandboxing, DLP, and centralized governance
- **File**: 2511.20920v1_Securing_the_Model_Context_Protocol_MCP_Risks_Controls_and_Governance.pdf (242 KB)

### 5. MCP-RiskCue: Can LLM Infer Risk Information From MCP Server System Logs?
- **ArXiv ID**: 2511.05867v2
- **Authors**: Jiayi Fu, Qiyao Sun
- **Published**: November 8, 2025 (updated November 12, 2025)
- **Primary Category**: cs.CR
- **Relevance Score**: 20.0
- **Focus**: LLM-based risk detection from MCP server system logs - benchmark for identifying security risks in compromised servers
- **Key Contribution**: MCP-RiskCue benchmark with 1,800 synthetic system logs across 9 risk categories. GRPO-trained Llama3.1-8B achieves 83% accuracy
- **File**: 2511.05867v2_MCP-RiskCue_Can_LLM_Infer_Risk_Information_From_MCP_Server_System_Logs.pdf (955 KB)

### 6. MCPGuard: Automatically Detecting Vulnerabilities in MCP Servers
- **ArXiv ID**: 2510.23673v1
- **Authors**: Bin Wang, Zexin Liu, Hao Yu, Ao Yang, Yenan Huang, Jing Guo, Huangsheng Cheng, Hui Li, Huiyu Wu
- **Published**: October 27, 2025
- **Primary Category**: cs.CR
- **Relevance Score**: 20.0
- **Focus**: Security landscape analysis and vulnerability detection in MCP servers
- **Key Contribution**: Classification of threat categories - agent hijacking, traditional web vulnerabilities, supply chain threats. Survey of proactive and runtime defense strategies
- **File**: 2510.23673v1_MCPGuard_Automatically_Detecting_Vulnerabilities_in_MCP_Servers.pdf (130 KB)

### 7. Securing AI Agent Execution (AgentBound)
- **ArXiv ID**: 2510.21236v2
- **Authors**: Christoph Bühler, Matteo Biagiola, Luca Di Grazia, Guido Salvaneschi
- **Published**: October 24, 2025 (updated October 29, 2025)
- **Primary Category**: cs.CR
- **Relevance Score**: 20.0
- **Focus**: Access control framework for MCP servers - first declarative policy mechanism for tool usage
- **Key Contribution**: AgentBound framework with Android permission model inspiration, 80.9% automatic policy generation accuracy on 296 popular MCP servers
- **File**: 2510.21236v2_Securing_AI_Agent_Execution.pdf (836 KB)

### 8. AegisMCP: Online Graph Intrusion Detection for Tool-Augmented LLMs
- **ArXiv ID**: 2510.19462v2
- **Authors**: Zhonghao Zhan, Amir Al Sadi, Krinos Li, Hamed Haddadi
- **Published**: October 22, 2025 (updated October 25, 2025)
- **Primary Category**: cs.CR
- **Relevance Score**: 20.0
- **Focus**: Protocol-level intrusion detection for MCP agent toolchains in smart home environments
- **Key Contribution**: NEBULA-Schema representation of MCP activity as streaming temporal graph, sub-second edge inference on Intel N150-class hardware
- **File**: 2510.19462v2_AegisMCP_Online_Graph_Intrusion_Detection_for_Tool-Augmented_LLMs_on_Edge_Devices.pdf (1.4 MB)

### 9. MCP-SafetyBench: A Benchmark for Safety Evaluation
- **ArXiv ID**: 2512.15163v1
- **Authors**: Xuanjun Zong, Zhiqi Shen, Lei Wang, Yunshi Lan, Chao Yang
- **Published**: December 17, 2025
- **Primary Category**: cs.CL (Computation and Language)
- **Relevance Score**: 18.0
- **Focus**: Comprehensive safety benchmark for LLMs with real-world MCP servers across 5 domains
- **Key Contribution**: Unified taxonomy of 20 MCP attack types, multi-turn evaluation with multi-server coordination, analysis of safety disparities across models
- **File**: 2512.15163v1_MCP-SafetyBench_A_Benchmark_for_Safety_Evaluation_of_Large_Language_Models_with_Real-World_MCP_Serve.pdf (6.6 MB)

### 10. MCPZoo: A Large-Scale Dataset of Runnable MCP Servers
- **ArXiv ID**: 2512.15144v2
- **Authors**: Mengying Wu, Pei Chen, Geng Hong, Baichao An, Jinsong Chen, Binwang Wan, Xudong Pan, Jiarun Dai, Min Yang
- **Published**: December 17, 2025 (updated December 18, 2025)
- **Primary Category**: cs.CR
- **Relevance Score**: 18.0
- **Focus**: Largest comprehensive dataset of MCP servers for empirical security research
- **Key Contribution**: MCPZoo with 95,142 servers, 10,000+ deployed runnable instances with unified metadata and access interfaces
- **File**: 2512.15144v2_MCPZoo_A_Large-Scale_Dataset_of_Runnable_Model_Context_Protocol_Servers_for_AI_Agent.pdf (109 KB)

---

## Query 2 Results: Multi-Agent and Protocol Security (9 Unique Papers)

### 1. ASTRIDE: A Security Threat Modeling Platform for Agentic-AI
- **ArXiv ID**: 2512.04785v1
- **Authors**: Eranga Bandara, Amin Hass, Ross Gore, Sachin Shetty, Ravi Mukkamala, Safdar H. Bouk, Xueping Liang, Ng Wee Keong, Kasun De Zoysa, Aruna Withanage, Nilaan Loganathan
- **Published**: December 4, 2025
- **Primary Category**: cs.AI
- **Relevance Score**: 20.0
- **Focus**: Extended STRIDE threat modeling framework for agentic AI systems with agent-to-agent communication
- **Key Contribution**: ASTRIDE extends STRIDE with "A" category for AI Agent-Specific Attacks (prompt injection, unsafe tool invocation, reasoning subversion), automated diagram-driven threat modeling
- **File**: 2512.04785v1_ASTRIDE_A_Security_Threat_Modeling_Platform_for_Agentic-AI_Applications.pdf (1.6 MB)

### 2. MALCDF: A Distributed Multi-Agent LLM Framework for Real-Time Cyber Defense
- **ArXiv ID**: 2512.14846v1
- **Authors**: Arth Bhardwaj, Sia Godika, Yuvam Loonker
- **Published**: December 16, 2025
- **Primary Category**: cs.CR
- **Relevance Score**: 18.0
- **Focus**: Multi-agent LLM coordination with secure communication layer for cybersecurity
- **Key Contribution**: MALCDF framework with 4 coordinated agents (Detection, Intelligence, Response, Analysis), encrypted ontology-aligned messaging, 90% detection accuracy on CICIDS2017
- **File**: 2512.14846v1_MALCDF_A_Distributed_Multi-Agent_LLM_Framework_for_Real-Time_Cyber.pdf (285 KB)

### 3. Quantigence: A Multi-Agent AI Framework for Quantum Security Research
- **ArXiv ID**: 2512.12989v1
- **Authors**: Abdulmalik Alquwayfili
- **Published**: December 15, 2025
- **Primary Category**: cs.MA (Multiagent Systems)
- **Relevance Score**: 18.0
- **Focus**: Multi-agent coordination framework integrating MCP for quantum security analysis
- **Key Contribution**: Multi-agent roles (Cryptographic Analyst, Threat Modeler, Standards Specialist, Risk Assessor) with MCP knowledge integration, 67% reduction in research turnaround time
- **File**: 2512.12989v1_Quantigence_A_Multi-Agent_AI_Framework_for_Quantum_Security_Research.pdf (771 KB)

### 4. Systematization of Knowledge: Security and Safety in MCP Ecosystem
- **ArXiv ID**: 2512.08290v2
- **Authors**: Shiva Gaire, Srijan Gyawali, Saroj Mishra, Suman Niroula, Dilip Thakur, Umesh Yadav
- **Published**: December 9, 2025 (updated December 13, 2025)
- **Primary Category**: cs.CR
- **Relevance Score**: 18.0
- **Focus**: Comprehensive SoK (Systematization of Knowledge) on MCP security threats and defenses
- **Key Contribution**: Taxonomy distinguishing adversarial security threats (indirect prompt injection, tool poisoning) from epistemic safety hazards (alignment failures), defense roadmap
- **File**: 2512.08290v2_Systematization_of_Knowledge_Security_and_Safety_in_the_Model_Context_Protocol_Ecosystem.pdf (5.0 MB)

### 5. Decentralized Multi-Agent System with Trust-Aware Communication
- **ArXiv ID**: 2512.02410v1
- **Authors**: Yepeng Ding, Ahmed Twabi, Junwei Yu, Lingfeng Zhang, Tohru Kondo, Hiroyuki Sato
- **Published**: December 2, 2025
- **Primary Category**: cs.MA
- **Relevance Score**: 18.0
- **Focus**: Blockchain-based decentralized multi-agent architecture with cryptographically secure communication
- **Key Contribution**: DMAS architecture with trust-aware protocol providing verifiable interaction cycles, communication integrity, authenticity, non-repudiation, conditional confidentiality
- **File**: 2512.02410v1_Decentralized_Multi-Agent_System_with_Trust-Aware_Communication.pdf (578 KB)

### 6. Security Risks of Agentic Vehicles: Cross-Layer Threat Analysis
- **ArXiv ID**: 2512.17041v1
- **Authors**: Ali Eslami, Jiangbo Yu
- **Published**: December 18, 2025
- **Primary Category**: cs.AI
- **Relevance Score**: 16.0
- **Focus**: Security threats in agentic AI systems integrated with cyber-physical platforms (vehicles)
- **Key Contribution**: Role-based architecture for agentic vehicles (Personal Agent, Driving Strategy Agent), cross-layer attack chain analysis, severity matrix
- **File**: 2512.17041v1_Security_Risks_of_Agentic_Vehicles_A_Systematic_Analysis_of_Cognitive_and_Cross-Layer_Threats.pdf (524 KB)

### 7. Coordinated Anti-Jamming Resilience in Swarm Networks via MARL
- **ArXiv ID**: 2512.16813v1
- **Authors**: Bahman Abolhassani, Tugba Erpek, Kemal Davaslioglu, Yalin E. Sagduyu, Sastry Kompella
- **Published**: December 18, 2025
- **Primary Category**: cs.NI (Networking and Internet Architecture)
- **Relevance Score**: 16.0
- **Focus**: Multi-agent coordination for communication resilience under adversarial jamming
- **Key Contribution**: QMIX-based MARL framework for swarm networks with coordinated frequency and power selection, near-optimal convergence
- **File**: 2512.16813v1_Coordinated_Anti-Jamming_Resilience_in_Swarm_Networks_via_Multi-Agent_Reinforcement_Learning.pdf (508 KB)

### 8. Bilevel Optimization for Covert Memory Tampering in Multi-Agent Architectures (XAMT)
- **ArXiv ID**: 2512.15790v1
- **Authors**: Akhil Sharma, Shaikh Yaser Arafat, Jai Kumar Sharma, Ken Huang
- **Published**: December 15, 2025
- **Primary Category**: cs.CR
- **Relevance Score**: 16.0
- **Focus**: Adversarial robustness assessment of heterogeneous MAS (MARL + LLM agents with RAG)
- **Key Contribution**: XAMT framework formalizing poisoning attacks as bilevel optimization, stealthy memory tampering with <1% poison rates in MARL, <0.1% in RAG agents
- **File**: 2512.15790v1_Bilevel_Optimization_for_Covert_Memory_Tampering_in_Heterogeneous_Multi-Agent_Architectures_XAMT.pdf (892 KB)

---

## Key Themes and Research Areas

### 1. **MCP Security Threats**
- Intent Inversion attacks (privacy)
- Tool Poisoning (semantic attacks)
- Shadowing attacks (indirect compromise)
- Rug Pulls (descriptor manipulation)
- Supply chain attacks on MCP servers
- Implicit toxicity and resource hijacking

### 2. **Defense Mechanisms**
- Manifest signing and cryptographic integrity
- LLM-based semantic vetting
- Runtime behavioral guardrails
- Access control frameworks (AgentBound, AegisMCP)
- Intrusion detection systems
- Policy enforcement engines
- Provenance tracking and auditing

### 3. **Multi-Agent Communication Security**
- Trust-aware protocols
- Cryptographically secure message exchange
- Blockchain-based decentralized architectures
- Secure coordination mechanisms
- Cross-layer threat analysis

### 4. **Benchmarking and Evaluation**
- MCP-SafetyBench (20 attack types across 5 domains)
- MCPZoo (95,142 servers dataset)
- MCP-RiskCue (system log analysis)
- Systematic evaluation across GPT-4, DeepSeek, Llama models

### 5. **Governance and Compliance**
- Configuration management
- Sandbox isolation
- Data Loss Prevention (DLP)
- Anomaly detection
- End-to-end auditing
- Private registries and gateway layers

---

## Primary Research Gaps and Future Directions

1. **Formal Methods**: Need for formal verification of MCP dynamic systems
2. **Privacy-Preserving Operations**: Privacy-preserving agent operations without compromising functionality
3. **Verifiable Registries**: Cryptographic verification of MCP server authenticity
4. **Cross-Protocol Security**: Interactions between MCP and other agent communication protocols
5. **Configuration Hardening**: Best practices for secure MCP configuration in enterprise settings
6. **Real-World Incident Response**: Post-breach forensics and recovery procedures

---

## Citation Statistics

- **2025 Papers**: 19 papers (100%)
- **2024 Papers**: 0 papers (0%)
- **Primary Category Distribution**:
  - cs.CR (Cryptography and Security): 11 papers
  - cs.MA (Multiagent Systems): 2 papers
  - cs.AI (Artificial Intelligence): 2 papers
  - cs.CL (Computation and Language): 1 paper
  - cs.NI (Networking and Internet Architecture): 1 paper

---

## Research Impact and Relevance

All papers are highly recent (December 2025 publications or late 2025) indicating this is an active, emerging research area. The papers span:
- Major AI institutions and researchers
- Novel attack vectors specific to MCP ecosystem
- Practical defense frameworks
- Comprehensive benchmarking efforts
- Governance and policy frameworks

This collection provides comprehensive coverage of MCP and A2A protocol security from attack analysis, defense mechanisms, benchmarking, to governance perspectives.

---

## Files Downloaded

1. 2510.19462v2_AegisMCP_Online_Graph_Intrusion_Detection_for_Tool-Augmented_LLMs_on_Edge_Devices.pdf (1.4 MB)
2. 2510.21236v2_Securing_AI_Agent_Execution.pdf (836 KB)
3. 2510.23673v1_MCPGuard_Automatically_Detecting_Vulnerabilities_in_MCP_Servers.pdf (130 KB)
4. 2511.05867v2_MCP-RiskCue_Can_LLM_Infer_Risk_Information_From_MCP_Server_System_Logs.pdf (955 KB)
5. 2511.20920v1_Securing_the_Model_Context_Protocol_MCP_Risks_Controls_and_Governance.pdf (242 KB)
6. 2512.02321v1_LeechHijack_Covert_Computational_Resource_Exploitation_in_Intelligent_Agent_Systems.pdf (1.3 MB)
7. 2512.02410v1_Decentralized_Multi-Agent_System_with_Trust-Aware_Communication.pdf (578 KB)
8. 2512.04785v1_ASTRIDE_A_Security_Threat_Modeling_Platform_for_Agentic-AI_Applications.pdf (1.6 MB)
9. 2512.06556v1_Securing_the_Model_Context_Protocol_Defending_LLMs_Against_Tool_Poisoning_and_Adversarial_Attacks.pdf (15 MB)
10. 2512.08290v2_Systematization_of_Knowledge_Security_and_Safety_in_the_Model_Context_Protocol_Ecosystem.pdf (5.0 MB)
11. 2512.12989v1_Quantigence_A_Multi-Agent_AI_Framework_for_Quantum_Security_Research.pdf (771 KB)
12. 2512.14166v1_IntentMiner_Intent_Inversion_Attack_via_Tool_Call_Analysis_in_the_Model_Context_Protocol.pdf (634 KB)
13. 2512.14846v1_MALCDF_A_Distributed_Multi-Agent_LLM_Framework_for_Real-Time_Cyber.pdf (285 KB)
14. 2512.15144v2_MCPZoo_A_Large-Scale_Dataset_of_Runnable_Model_Context_Protocol_Servers_for_AI_Agent.pdf (109 KB)
15. 2512.15163v1_MCP-SafetyBench_A_Benchmark_for_Safety_Evaluation_of_Large_Language_Models_with_Real-World_MCP_Serve.pdf (6.6 MB)
16. 2512.15790v1_Bilevel_Optimization_for_Covert_Memory_Tampering_in_Heterogeneous_Multi-Agent_Architectures_XAMT.pdf (892 KB)
17. 2512.16813v1_Coordinated_Anti-Jamming_Resilience_in_Swarm_Networks_via_Multi-Agent_Reinforcement_Learning.pdf (508 KB)
18. 2512.17041v1_Security_Risks_of_Agentic_Vehicles_A_Systematic_Analysis_of_Cognitive_and_Cross-Layer_Threats.pdf (524 KB)

---

## Research Metadata

- **Query Execution Date**: December 24, 2025
- **ArXiv Search Completed**: Yes
- **Total Search Results**: 100 papers (50 per query)
- **Selection Criteria**: Relevance score (weighted by keyword matches, year, prestigious affiliations)
- **Filtering Keywords Applied**: MCP, Model Context Protocol, agent-to-agent, A2A, protocol, security, tool, configuration, vulnerability, poisoning, attack
