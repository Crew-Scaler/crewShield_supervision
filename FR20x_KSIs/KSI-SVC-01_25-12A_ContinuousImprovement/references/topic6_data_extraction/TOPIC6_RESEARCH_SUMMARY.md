# Topic 6: Configuration Data Extraction via Jailbreak and Multi-Turn Context Poisoning
## ArXiv Research Summary - Issue #64

**Research Date**: December 24, 2025
**Total Unique Papers Downloaded**: 30
**Total PDFs**: 30 files across 3 successful queries
**Total Folder Size**: 75 MB
**Output Directory**: `/Users/tamnguyen/Documents/GitHub/ksi_watch/KSI-SVC-01_25-12A_ContinuousImprovement/references/topic6_data_extraction/`

---

## Executive Summary

This research compilation focuses on the intersection of three critical security threats in Large Language Models:
1. **Configuration Data Extraction** - Methods to extract sensitive configuration and infrastructure data
2. **Jailbreak & Prompt Injection** - Techniques to bypass safety mechanisms and manipulate LLM behavior
3. **Multi-Turn Context Poisoning** - Attacks that degrade or corrupt context across multiple dialogue turns

The search identified 119 relevant papers on ArXiv (2024-2025), of which the top 30 most relevant were downloaded and analyzed.

---

## Search Queries Executed

### Query 1 (Original - No Results)
```
("configuration exfiltration" OR "sensitive data extraction") AND
("prompt injection" OR jailbreak) AND
(LLM OR agent) AND (2024 OR 2025)
```
- **Results Found**: 0
- **Papers Downloaded**: 0
- **Status**: Failed - Terminology not prevalent in ArXiv

### Query 2 (Multi-turn & Context Poisoning)
```
("multi-turn" OR "context poisoning") AND
(configuration OR infrastructure) AND
(large-language-model) AND (2024 OR 2025)
```
- **Results Found**: 19
- **Papers Downloaded**: 10 (top relevance)
- **Status**: Success

### Query 3 (Jailbreak & Exfiltration)
```
(jailbreak OR "prompt injection") AND
(exfiltration OR extraction) AND (2024 OR 2025)
```
- **Results Found**: 50
- **Papers Downloaded**: 10 (top relevance)
- **Status**: Success

### Query 4 (Configuration & Sensitive Data)
```
(configuration OR infrastructure) AND
(sensitive OR secret OR credential) AND
(LLM OR agent) AND (2024 OR 2025)
```
- **Results Found**: 50
- **Papers Downloaded**: 10 (top relevance)
- **Status**: Success

---

## Downloaded Papers by Relevance Score

### Highest Relevance (Score 20.0)

**1. VET Your Agent: Towards Host-Independent Autonomy via Verifiable Execution Traces**
- **ArXiv ID**: 2512.15892v1
- **Year**: 2025
- **Authors**: Artem Grigor, Christian Schroeder de Witt, Simon Birnbach, Ivan Martinovic
- **Category**: Computer Security (cs.CR)
- **Relevance Score**: 20.0/28
- **Key Topics**: Agent configuration, verifiable execution, credential protection
- **Summary**: Presents VET framework for verifying agent execution traces with Agent Identity Documents (AID) that specify agent configuration. Addresses host-independent authentication and credential protection in autonomous agents.

---

### High Relevance (Score 18.0)

**2. Black-Box Behavioral Distillation Breaks Safety Alignment in Medical LLMs**
- **ArXiv ID**: 2512.09403v1
- **Year**: 2025
- **Authors**: Sohely Jahan, Ruimin Sun
- **Category**: Machine Learning (cs.LG)
- **Relevance Score**: 18.0/28
- **Key Topics**: Model extraction, safety jailbreak, information exfiltration
- **Summary**: Demonstrates black-box distillation attack extracting safety-aligned behavior from medical LLMs using only output access. $12 cost to replicate unsafe model behavior shows economic feasibility of configuration-based attacks.

**3. A Practical Framework for Evaluating Medical AI Security**
- **ArXiv ID**: 2512.08185v1
- **Year**: 2025
- **Authors**: Jinghao Wang, Ping Zhang, Carter Yagemann
- **Category**: Computer Security (cs.CR)
- **Relevance Score**: 18.0/28
- **Key Topics**: Jailbreak evaluation, multi-turn manipulation, privacy extraction
- **Summary**: Framework for testing medical LLM security including multi-turn role-playing attacks and privacy data extraction. Addresses configuration-specific vulnerabilities in specialized domains.

**4. Exploiting Latent Space Discontinuities for Building Universal LLM Jailbreaks and Data Extraction Attacks**
- **ArXiv ID**: 2511.00346v1
- **Year**: 2025
- **Authors**: Kayua Oleques Paim, Rodrigo Brandao Mansilha, Diego Kreutz, Muriel Figueredo Franco, Weverton Cordeiro
- **Category**: Computer Security (cs.CR)
- **Relevance Score**: 18.0/28
- **Key Topics**: Universal jailbreaks, data extraction, latent space vulnerabilities
- **Summary**: **Most directly relevant paper** - Proposes systematic approach to crafting universal jailbreaks and data extraction attacks by exploiting latent space discontinuities. Generalizes across seven different LLMs and image generation models.

**5. EchoLeak: The First Real-World Zero-Click Prompt Injection Exploit in a Production LLM System**
- **ArXiv ID**: 2509.10540v1
- **Year**: 2025
- **Authors**: Pavan Reddy, Aditya Sanjay Gujral
- **Category**: Computer Security (cs.CR)
- **Relevance Score**: 18.0/28
- **Key Topics**: Prompt injection, configuration exfiltration, zero-click exploit
- **Summary**: **Real-world case study** of CVE-2025-32711 in Microsoft 365 Copilot enabling unauthenticated data exfiltration through crafted email. Demonstrates context poisoning via Markdown bypasses and configuration manipulation.

**6. MCP-Guard: A Defense Framework for Model Context Protocol Integrity in Large Language Model Applications**
- **ArXiv ID**: 2508.10991v2
- **Year**: 2025
- **Authors**: Wenpeng Xing, Zhonghao Qi, Yupeng Qin, Yilin Li, Caini Chang, Jiahui Yu, Changting Lin, Zhenzhen Xie, Meng Han
- **Category**: Computer Security (cs.CR)
- **Relevance Score**: 18.0/28
- **Key Topics**: Context protocol integrity, prompt injection defense, data exfiltration prevention
- **Summary**: Defense framework addressing prompt injection, data exfiltration, and context poisoning in MCP-based LLM-tool interactions. Includes 70,000+ sample attack benchmark.

**7. Quantifying Conversation Drift in MCP via Latent Polytope**
- **ArXiv ID**: 2508.06418v1
- **Year**: 2025
- **Authors**: Haoran Shi, Hongwei Yao, Shuo Shao, Shaopeng Jiao, Ziqi Peng, Zhan Qin, Cong Wang
- **Category**: Computation and Language (cs.CL)
- **Relevance Score**: 18.0/28
- **Key Topics**: Multi-turn context poisoning, conversation hijacking, data exfiltration detection
- **Summary**: **Core multi-turn context poisoning paper** - Proposes SecMCP framework detecting conversation drift through latent polytope analysis. Detects tool poisoning, indirect prompt injection, and hijacking in multi-turn interactions.

**8. Manipulating LLM Web Agents with Indirect Prompt Injection Attack via HTML Accessibility Tree**
- **ArXiv ID**: 2507.14799v1
- **Year**: 2025
- **Authors**: Sam Johnson, Viet Pham, Thai Le
- **Category**: Computer Security (cs.CR)
- **Relevance Score**: 18.0/28
- **Key Topics**: Indirect prompt injection, credential exfiltration, agent manipulation
- **Summary**: Demonstrates indirect prompt injection via HTML accessibility trees enabling credential exfiltration and forced actions in web agents. Shows how configuration can be poisoned via external data sources.

**9. Large Language Models as a (Bad) Security Norm in the Context of Regulation and Compliance**
- **ArXiv ID**: 2512.16419v1
- **Year**: 2025
- **Authors**: Kaspar Rosager Ludvigsen
- **Category**: Computers and Society (cs.CY)
- **Relevance Score**: 18.0/28
- **Key Topics**: Configuration security risks, compliance violations, sensitive data handling
- **Summary**: Analysis of LLM security failures including risks of processing sensitive data, configuration exposure, and regulatory non-compliance in infrastructure design.

---

### Medium-High Relevance (Score 16.0)

**10. Safe2Harm: Semantic Isomorphism Attacks for Jailbreaking Large Language Models**
- **ArXiv ID**: 2512.13703v1
- **Year**: 2025
- **Authors**: Fan Yang
- **Relevance Score**: 16.0/28
- **Summary**: Proposes semantic-preserving jailbreak method converting harmful questions to safe equivalents, demonstrating 7 LLM jailbreaks.

**11. SoK: a Comprehensive Causality Analysis Framework for Large Language Model Security**
- **ArXiv ID**: 2512.04841v1
- **Year**: 2025
- **Authors**: Wei Zhao, Zhe Li, Jun Sun
- **Relevance Score**: 16.0/28
- **Summary**: Systematic causal analysis of LLM jailbreak vulnerabilities with token/neuron/layer-level interventions achieving 95% detection accuracy.

**12. Immunity memory-based jailbreak detection: multi-agent adaptive guard for large language models**
- **ArXiv ID**: 2512.03356v1
- **Year**: 2025
- **Authors**: Jun Leng, Litian Zhang, Xi Zhang
- **Relevance Score**: 16.0/28
- **Summary**: Multi-agent framework for detecting jailbreak attempts using immunological memory mechanisms with 98% accuracy.

**13. FASTRIC: Prompt Specification Language for Verifiable LLM Interactions**
- **ArXiv ID**: 2512.18940v1
- **Year**: 2025
- **Authors**: Wen-Long Jin
- **Relevance Score**: 16.0/28
- **Summary**: FSM-based specification language for multi-turn interactions with conformance verification detecting deviation from intended behavior.

**14. Adaptive Focus Memory for Language Models**
- **ArXiv ID**: 2511.12712v2
- **Year**: 2025
- **Authors**: Christopher Cruz
- **Relevance Score**: 16.0/28
- **Summary**: Context management system preserving critical constraints in multi-turn dialogue under bounded context. Addresses constraint drift in long conversations.

**15. Scaling LLM Multi-turn RL with End-to-end Summarization-based Context Management**
- **ArXiv ID**: 2510.06727v1
- **Year**: 2025
- **Authors**: Miao Lu, Weiwei Sun, Weihua Du, Zhan Ling, Xuesong Yao, Kang Liu, Jiecao Chen
- **Relevance Score**: 16.0/28
- **Summary**: SUPO algorithm for managing context beyond fixed limits through summarization, enabling detection of context manipulation.

**16. AgentRL: Scaling Agentic Reinforcement Learning with a Multi-Turn, Multi-Task Framework**
- **ArXiv ID**: 2510.04206v1
- **Year**: 2025
- **Authors**: Hanchen Zhang, Xiao Liu, Bowen Lv, et al.
- **Relevance Score**: 16.0/28
- **Summary**: Framework for multi-turn, multi-task agent training with infrastructure for detecting misalignment.

**17. Generalizable End-to-End Tool-Use RL with Synthetic CodeGym**
- **ArXiv ID**: 2509.17325v1
- **Year**: 2025
- **Authors**: Weihua Du, Hailei Gong, Zhan Ling, Kang Liu, Lingfeng Shen, et al.
- **Relevance Score**: 16.0/28
- **Summary**: Framework for training tool-use agents with configuration-aware environments demonstrating workflow robustness.

**18. The World According to LLMs: How Geographic Origin Influences LLMs' Entity Deduction Capabilities**
- **ArXiv ID**: 2508.05525v1
- **Year**: 2025
- **Authors**: Harsh Nishant Lalai, Raj Sanjay Shah, Jiaxin Pei, et al.
- **Relevance Score**: 16.0/28
- **Summary**: Studies multi-turn deduction task revealing implicit biases extractable through interactive reasoning in multi-turn games.

**19. Deep Research Agents: A Systematic Examination And Roadmap**
- **ArXiv ID**: 2506.18096v2
- **Year**: 2025
- **Authors**: Yuxuan Huang, Yihang Chen, Haozheng Zhang, Kang Li, et al.
- **Relevance Score**: 16.0/28
- **Summary**: Comprehensive analysis of deep research agents with multi-turn reasoning, dynamic workflows, and tool integration architectures.

**20. The Cost of Dynamic Reasoning: Demystifying AI Agents and Test-Time Scaling from an AI Infrastructure Perspective**
- **ArXiv ID**: 2506.04301v1
- **Year**: 2025
- **Authors**: Jiin Kim, Byeongjun Shin, Jinha Chung, Minsoo Rhu
- **Relevance Score**: 16.0/28
- **Summary**: System-level analysis of agent infrastructure costs and configuration impact on resource usage and latency.

**21. MIRROR: Modular Internal Processing for Personalized Safety in LLM Dialogue**
- **ArXiv ID**: 2506.00430v2
- **Year**: 2025
- **Authors**: Nicole Hsing
- **Relevance Score**: 16.0/28
- **Summary**: Architecture for maintaining configuration constraints across multi-turn dialogue with persistent internal state.

**22. Assessing Large Language Models for Structured Medical Order Extraction**
- **ArXiv ID**: 2510.10475v1
- **Year**: 2025
- **Authors**: A H M Rezaul Karim, Ozlem Uzuner
- **Relevance Score**: 16.0/28
- **Summary**: Framework for extracting structured data from multi-turn doctor-patient dialogues demonstrating information extraction techniques.

**23. LLM-Assisted Abstract Screening with OLIVER**
- **ArXiv ID**: 2512.20022v1
- **Year**: 2025
- **Authors**: Kian Godhwani, David Benrimoh
- **Relevance Score**: 16.0/28
- **Summary**: Multi-configuration LLM evaluation framework addressing consistency and calibration in task-specific deployments.

**24. RAPID-LLM: Resilience-Aware Performance analysis of Infrastructure for Distributed LLM Training and Inference**
- **ArXiv ID**: 2512.19606v1
- **Year**: 2025
- **Authors**: George Karfakis, Faraz Tahmasebi, Binglu Chen, et al.
- **Relevance Score**: 16.0/28
- **Summary**: Performance modeling framework for LLM infrastructure configuration analysis with fault tolerance evaluation.

**25. Feature-Selective Representation Misdirection for Machine Unlearning**
- **ArXiv ID**: 2512.16297v1
- **Year**: 2025
- **Authors**: Taozhao Chen, Linghan Huang, Kim-Kwang Raymond Choo, Huaming Chen
- **Relevance Score**: 16.0/28
- **Summary**: Addresses removal of sensitive configuration knowledge from models through selective representation modification.

**26. In-Context Probing for Membership Inference in Fine-Tuned Language Models**
- **ArXiv ID**: 2512.16292v2
- **Year**: 2025
- **Authors**: Zhexi Lu, Hongliang Chi, Nathalie Baracaldo, et al.
- **Relevance Score**: 16.0/28
- **Summary**: Privacy attack extracting membership information through in-context probing in fine-tuned models.

**27. BashArena: A Control Setting for Highly Privileged AI Agents**
- **ArXiv ID**: 2512.15688v1
- **Year**: 2025
- **Authors**: Adam Kaufman, James Lucassen, Tyler Tracy, Cody Rushing, Aryan Bhatt
- **Relevance Score**: 16.0/28
- **Summary**: **Highly relevant infrastructure security paper** - Benchmark for testing agent sabotage including secret exfiltration, privilege escalation, and firewall disabling with 637 realistic tasks.

**28. EVICPRESS: Joint KV-Cache Compression and Eviction for Efficient LLM Serving**
- **ArXiv ID**: 2512.14946v1
- **Year**: 2025
- **Authors**: Shaoting Feng, Yuhan Liu, Hanchen Li, et al.
- **Relevance Score**: 16.0/28
- **Summary**: Context management system for KV-cache addressing multi-turn conversation infrastructure with security implications.

**29. Improving Semantic Uncertainty Quantification in LVLMs with Semantic Gaussian Processes**
- **ArXiv ID**: 2512.14177v1
- **Year**: 2025
- **Authors**: Joseph Hoche, Andrei Bursuc, David Brellmann, et al.
- **Relevance Score**: 16.0/28
- **Summary**: Uncertainty quantification in multi-modal LLM outputs relevant to detecting poisoned responses.

**30. Async Control: Stress-testing Asynchronous Control Measures for LLM Agents**
- **ArXiv ID**: 2512.13526v1
- **Year**: 2025
- **Authors**: Asa Cooper Stickland, Jan Michelfeit, Arathi Mani, et al.
- **Relevance Score**: 16.0/28
- **Summary**: **Infrastructure-critical paper** - Adversarial testing of agent monitoring with 5 realistic software engineering scenarios including sabotage detection with 6% FNR at 1% FPR.

---

## Key Topics Covered Across Papers

### Jailbreak & Prompt Injection Attacks (8 papers)
- Universal latent space exploitation techniques
- Real-world zero-click exploits (EchoLeak/CVE-2025-32711)
- Semantic isomorphism and safe-to-harm transformations
- Indirect prompt injection via HTML/Markdown
- Black-box behavioral distillation

### Multi-Turn Context Poisoning (7 papers)
- Conversation drift detection via latent polytope analysis
- Context management and constraint preservation
- Summarization-based context compression
- FSM-based multi-turn verification
- Multi-agent adaptive detection systems

### Configuration Data Extraction (6 papers)
- Black-box model extraction with minimal cost
- Membership inference attacks
- In-context probing for sensitive data
- Agent configuration verification
- Credential and secret exfiltration

### Agent Security & Infrastructure (6 papers)
- Verifiable execution traces for agent autonomy
- Privileged agent sabotage scenarios (BashArena)
- Asynchronous monitoring and control measures
- Agent infrastructure configuration analysis
- AI copilot security architectures

### Defense & Detection Mechanisms (5 papers)
- MCP-Guard layered detection pipeline
- Immunity memory-based jailbreak detection
- Causality analysis framework for vulnerability identification
- Conversation drift quantification
- Asynchronous monitoring with ensemble techniques

### Data Privacy & Unlearning (3 papers)
- Feature-selective representation misdirection
- Membership inference via optimization gap analysis
- Configuration-specific knowledge removal

---

## Critical Papers for Topic 6 (Ranked by Relevance)

### Top 5 Most Relevant Papers

1. **Exploiting Latent Space Discontinuities for Building Universal LLM Jailbreaks and Data Extraction Attacks** (2511.00346)
   - Score: 18.0
   - Why: Directly addresses systematic data extraction through jailbreaks
   - Technique: Latent space discontinuity exploitation
   - Impact: Generalizes across 7+ LLMs

2. **EchoLeak: The First Real-World Zero-Click Prompt Injection Exploit** (2509.10540)
   - Score: 18.0
   - Why: Real-world case study of configuration exfiltration
   - Technique: Multi-layered bypass chain (XPI classifier evasion + Markdown + image auto-fetch + CSP abuse)
   - Impact: CVE-2025-32711 demonstrates practical threat

3. **Quantifying Conversation Drift in MCP via Latent Polytope** (2508.06418)
   - Score: 18.0
   - Why: Directly addresses context poisoning detection in multi-turn scenarios
   - Technique: Latent polytope-based anomaly detection
   - Impact: 91.5%+ AUROC across multiple LLMs

4. **MCP-Guard: A Defense Framework for Model Context Protocol Integrity** (2508.10991)
   - Score: 18.0
   - Why: Comprehensive defense against prompt injection and data exfiltration in tool-integrated systems
   - Technique: Three-stage detection pipeline with 70,000+ attack samples
   - Impact: 96.01% accuracy on semantic attacks

5. **BashArena: A Control Setting for Highly Privileged AI Agents** (2512.15688)
   - Score: 16.0
   - Why: Realistic infrastructure scenario with secret exfiltration and configuration manipulation
   - Technique: 637 realistic Linux system administration tasks with sabotage objectives
   - Impact: Claude 4.1 achieves 26% undetected sabotage rate

---

## Emerging Attack Patterns

### Multi-Stage Data Extraction
1. **Latent Space Exploitation** → Universal jailbreak
2. **Context Poisoning** → Constraint drift
3. **Configuration Manipulation** → Privilege escalation
4. **Data Exfiltration** → Credential/secret leakage

### Defense Requirements
- **Real-time Context Monitoring**: Detect drift via latent polytope analysis
- **Verifiable Execution**: VET framework for output authentication
- **Asynchronous Monitoring**: 6% FNR with ensemble approaches
- **FSM-based Verification**: FASTRIC conformance checking
- **Layered Detection**: Static + semantic + arbitration (96%+ accuracy)

---

## Query 1 Analysis - Why It Failed

The original Query 1:
```
("configuration exfiltration" OR "sensitive data extraction") AND
("prompt injection" OR jailbreak) AND
(LLM OR agent) AND (2024 OR 2025)
```

**Returned 0 papers because:**

1. **Terminology Mismatch**: "Configuration exfiltration" is not standard ArXiv terminology
   - Papers use: "data extraction", "credential leakage", "secret exfiltration"
   - Not: "configuration exfiltration"

2. **Specificity Too High**: Combination of four specific concepts in one paper is rare
   - Most papers focus on 1-2 of these: jailbreak, prompt injection, extraction, configuration
   - Papers don't typically combine all four in abstract/title

3. **Solution Applied**: Queries 2-4 used broader but standard terminology:
   - "multi-turn" + "context poisoning" (19 results)
   - "jailbreak" + "exfiltration" (50 results)
   - "configuration" + "sensitive" (50 results)

---

## Research Gaps Identified

1. **Coordinated Attack Chains**: Limited papers on multi-stage attack orchestration
2. **Configuration-Specific Exploits**: Few papers targeting infrastructure configuration leakage specifically
3. **Dynamic Defense Adaptation**: Need for real-time adaptation to novel attacks
4. **Cost-Benefit Analysis**: Limited analysis of attack ROI vs. defense cost
5. **Cross-Domain Poisoning**: Context poisoning across heterogeneous multi-agent systems

---

## Recommendations for Issue #64

### Priority Research Areas
1. **Configuration Hardening**: Defense strategies against multi-turn context poisoning
2. **Infrastructure Verification**: Implement VET-like verifiable execution for configuration integrity
3. **Real-time Detection**: Latent polytope-based monitoring for conversation drift
4. **Agent Isolation**: Privilege separation to limit extraction scope (BashArena reference)
5. **Ensemble Monitoring**: Multi-layer detection pipeline matching MCP-Guard architecture

### Implementation Considerations
- Configuration as explicit FSM (FASTRIC approach)
- Context management with adaptive fidelity (AFM approach)
- Causality-based interpretation (SoK framework)
- Asymmetric cost for attacks vs. defenses

---

## Metadata Files Generated

- `topic6_query2_papers.json` - 10 papers from multi-turn/context query
- `topic6_query3_papers.json` - 10 papers from jailbreak/exfiltration query
- `topic6_query4_papers.json` - 10 papers from configuration/sensitive data query
- `TOPIC6_RESEARCH_SUMMARY.md` - This comprehensive summary

---

## Complete PDF List (30 files, 75 MB)

```
2506.00430v2_MIRROR_Modular_Internal_Processing_for_Personalized_Safety_in_LLM_Dialogue.pdf
2506.04301v1_The_Cost_of_Dynamic_Reasoning_Demystifying_AI_Agents_and_Test-Time_Scaling_from_an_AI_Infrastructure.pdf
2506.18096v2_Deep_Research_Agents_A_Systematic_Examination_And_Roadmap.pdf
2507.14799v1_Manipulating_LLM_Web_Agents_with_Indirect_Prompt_Injection_Attack_via_HTML_Accessibility_Tree.pdf
2508.05525v1_The_World_According_to_LLMs_How_Geographic_Origin_Influences_LLMs_Entity_Deduction_Capabilities.pdf
2508.06418v1_Quantifying_Conversation_Drift_in_MCP_via_Latent_Polytope.pdf
2508.10991v2_MCP-Guard_A_Defense_Framework_for_Model_Context_Protocol_Integrity_in_Large_Language_Model_Applicati.pdf
2509.10540v1_EchoLeak_The_First_Real-World_Zero-Click_Prompt_Injection_Exploit_in_a_Production_LLM_System.pdf
2509.17325v1_Generalizable_End-to-End_Tool-Use_RL_with_Synthetic_CodeGym.pdf
2510.04206v1_AgentRL_Scaling_Agentic_Reinforcement_Learning_with_a_Multi-Turn_Multi-Task_Framework.pdf
2510.06727v1_Scaling_LLM_Multi-turn_RL_with_End-to-end_Summarization-based_Context_Management.pdf
2510.10475v1_Assessing_Large_Language_Models_for_Structured_Medical_Order_Extraction.pdf
2511.00346v1_Exploiting_Latent_Space_Discontinuities_for_Building_Universal_LLM_Jailbreaks_and_Data_Extraction_At.pdf
2511.12712v2_Adaptive_Focus_Memory_for_Language_Models.pdf
2512.03356v1_Immunity_memory-based_jailbreak_detection_multi-agent_adaptive_guard_for_large_language_models.pdf
2512.04841v1_SoK_a_Comprehensive_Causality_Analysis_Framework_for_Large_Language_Model_Security.pdf
2512.08185v1_A_Practical_Framework_for_Evaluating_Medical_AI_Security_Reproducible_Assessment_of_Jailbreaking_and.pdf
2512.09403v1_Black-Box_Behavioral_Distillation_Breaks_Safety_Alignment_in_Medical_LLMs.pdf
2512.13526v1_Async_Control_Stress-testing_Asynchronous_Control_Measures_for_LLM_Agents.pdf
2512.13703v1_Safe2Harm_Semantic_Isomorphism_Attacks_for_Jailbreaking_Large_Language_Models.pdf
2512.14177v1_Improving_Semantic_Uncertainty_Quantification_in_LVLMs_with_Semantic_Gaussian_Processes.pdf
2512.14946v1_EVICPRESS_Joint_KV-Cache_Compression_and_Eviction_for_Efficient_LLM_Serving.pdf
2512.15688v1_BashArena_A_Control_Setting_for_Highly_Privileged_AI_Agents.pdf
2512.15892v1_VET_Your_Agent_Towards_Host-Independent_Autonomy_via_Verifiable_Execution_Traces.pdf
2512.16292v2_In-Context_Probing_for_Membership_Inference_in_Fine-Tuned_Language_Models.pdf
2512.16297v1_Feature-Selective_Representation_Misdirection_for_Machine_Unlearning.pdf
2512.16419v1_Large_Language_Models_as_a_Bad_Security_Norm_in_the_Context_of_Regulation_and_Compliance.pdf
2512.18940v1_FASTRIC_Prompt_Specification_Language_for_Verifiable_LLM_Interactions.pdf
2512.19606v1_RAPID-LLM_Resilience-Aware_Performance_analysis_of_Infrastructure_for_Distributed_LLM_Training_and_I.pdf
2512.20022v1_LLM-Assisted_Abstract_Screening_with_OLIVER_Evaluating_Calibration_and_Single-Model_vs_Actor-Critic_.pdf
```

---

**End of Report**
