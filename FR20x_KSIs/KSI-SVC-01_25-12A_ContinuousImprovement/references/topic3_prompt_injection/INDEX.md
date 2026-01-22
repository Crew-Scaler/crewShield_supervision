# Topic 3: Prompt Injection Attacks - Paper Index

## Quick Reference

**Total Papers**: 14 unique papers
**Total Size**: ~24 MB
**Date Range**: 2025 (12 papers), 2024 (2 papers)
**Focus Areas**: Prompt injection, jailbreaking, agent security, configuration management

---

## Papers by Topic

### Attack Methodologies (6 papers)

#### Direct Prompt Injection
- **2512.14860v1** - Penetration Testing of Agentic AI (AutoGen/CrewAI frameworks)
- **2511.00447v2** - DRIP Defense Paper (covers DRIP, SecAlign, ISE, PFT attacks)
- **2512.12583v1** - Detecting Prompt Injection Attacks Using Classifiers

#### Jailbreaking & Multi-Turn Attacks
- **2507.01020v1** - AutoAdv: Automated Adversarial Prompting (86% success rate)
- **2506.23576v1** - Evaluating Multi-Agent Defences Against Jailbreaks

#### Infrastructure & Configuration Attacks
- **2508.17155v1** - TOCTOU Vulnerabilities in LLM-Enabled Agents
- **2503.12188v2** - Multi-Agent Systems Execute Arbitrary Malicious Code

### Defense & Mitigation Strategies (8 papers)

#### Token-Level & Semantic Defenses
- **2511.00447v2** - DRIP: Token-wise Representation Editing
- **2512.19011v1** - Efficient Jailbreak Mitigation (SVM-based, 93.4% accuracy)
- **2511.19727v1** - Prompt Fencing: Cryptographic Boundaries

#### Agent Authorization & Delegation
- **2509.13597v1** - Agentic JWT: Secure Delegation Protocol
- **2512.15782v1** - Auto-Tuning Safety Guardrails

#### Systematic Evaluation & Frameworks
- **2505.13862v3** - PandaGuard: Systematic Safety Evaluation
- **2506.23576v1** - Multi-Agent Defence Evaluation
- **2512.12921v1** - Cisco Integrated AI Security Framework

#### Economic/Risk Analysis
- **2512.15081v1** - Quantifying Return on Security Controls (ROC analysis)

---

## Papers by Year & Relevance

### 2025 Papers (12 total)

**High Priority (Score 20.0-22.0)**
1. 2512.14860v1 - Penetration Testing of Agentic AI
2. 2512.12921v1 - Cisco AI Security Framework
3. 2511.00447v2 - DRIP Defense
4. 2508.17155v1 - TOCTOU Vulnerabilities
5. 2503.12188v2 - Multi-Agent Code Execution
6. 2512.19011v1 - Efficient Jailbreak Mitigation
7. 2512.15081v1 - Security Controls ROC
8. 2512.12583v1 - Prompt Injection Detection
9. 2511.19727v1 - Prompt Fencing
10. 2509.13597v1 - Agentic JWT

**Moderate Priority (Score 18.0-20.0)**
11. 2506.23576v1 - Multi-Agent Defences
12. 2505.13862v3 - PandaGuard
13. 2512.15782v1 - Auto-Tuning Guardrails
14. 2507.01020v1 - AutoAdv Attacks

### 2024 Papers (2 total)
None in this collection (all papers are from 2025)

---

## File Organization

### Research Papers (14 PDFs)
```
2503.12188v2_Multi-Agent_Systems_Execute_Arbitrary_Malicious_Code.pdf
2505.13862v3_PandaGuard_Systematic_Evaluation_of_LLM_Safety_against_Jailbreaking_Attacks.pdf
2506.23576v1_Evaluating_Multi-Agent_Defences_Against_Jailbreaking_Attacks_on_Large_Language_Models.pdf
2507.01020v1_AutoAdv_Automated_Adversarial_Prompting_for_Multi-Turn_Jailbreaking_of_Large_Language_Models.pdf
2508.17155v1_Mind_the_Gap_Time-of-Check_to_Time-of-Use_Vulnerabilities_in_LLM-Enabled_Agents.pdf
2509.13597v1_Agentic_JWT_A_Secure_Delegation_Protocol_for_Autonomous_AI_Agents.pdf
2511.00447v2_DRIP_Defending_Prompt_Injection_via_Token-wise_Representation_Editing_and_Residual_Instruction_Fusio.pdf
2511.19727v1_Prompt_Fencing_A_Cryptographic_Approach_to_Establishing_Security_Boundaries_in_Large_Language_Model_.pdf
2512.12583v1_Detecting_Prompt_Injection_Attacks_Against_Application_Using_Classifiers.pdf
2512.12921v1_Cisco_Integrated_AI_Security_and_Safety_Framework_Report.pdf
2512.14860v1_Penetration_Testing_of_Agentic_AI_A_Comparative_Security_Analysis_Across_Models_and_Frameworks.pdf
2512.15081v1_Quantifying_Return_on_Security_Controls_in_LLM_Systems.pdf
2512.15782v1_Auto-Tuning_Safety_Guardrails_for_Black-Box_Large_Language_Models.pdf
2512.19011v1_Efficient_Jailbreak_Mitigation_Using_Semantic_Linear_Classification_in_a_Multi-Staged_Pipeline.pdf
```

### Metadata Files
- `topic3_query1_papers.json` - Raw metadata from Query 1 (10 papers)
- `topic3_query2_papers.json` - Raw metadata from Query 2 (5 papers)
- `RESEARCH_SUMMARY.md` - Comprehensive research summary with findings
- `INDEX.md` - This file

---

## Key Research Findings at a Glance

### Attack Efficacy
- **Agentic AI Penetration Testing**: 41.5-58.9% attack success across models
- **Multi-Agent Malicious Code Execution**: 58-100% success rates
- **Jailbreak Attacks (AutoAdv)**: Up to 86% success rate with multi-turn attacks
- **TOCTOU Vulnerability Window**: 12% vulnerable trajectories initially

### Defense Effectiveness
- **DRIP**: 66% attack success reduction, 12-49% role-separation improvement
- **Prompt Fencing**: 100% attack prevention in testing
- **SVM-based Filtering**: 93.4% accuracy, 10x latency improvement
- **Return on Investment (ABAC)**: 9.83x ROC, 94% loss reduction

### Configuration Management Insights
- Time-of-check to time-of-use (TOCTOU) gaps enable configuration swaps
- Multi-agent orchestration creates attack surface for control hijacking
- Infrastructure-level prompt injection affects downstream agents
- Cryptographic boundaries can establish security zones

---

## Recommended Reading Order

### For Security Practitioners
1. 2512.14860v1 - Understand agentic AI attack surface
2. 2512.12921v1 - Review Cisco's comprehensive framework
3. 2511.00447v2 - Learn DRIP token-level defenses
4. 2512.19011v1 - Implement SVM-based mitigation
5. 2512.15081v1 - Calculate ROI for your defenses

### For Researchers
1. 2512.14860v1 - Penetration testing methodology
2. 2505.13862v3 - PandaGuard benchmark and framework
3. 2507.01020v1 - AutoAdv attack generation
4. 2508.17155v1 - TOCTOU vulnerability analysis
5. 2509.13597v1 - A-JWT delegation protocol

### For Configuration/Infrastructure Teams
1. 2508.17155v1 - TOCTOU vulnerabilities
2. 2503.12188v2 - Multi-agent attack vectors
3. 2511.19727v1 - Cryptographic boundaries
4. 2509.13597v1 - Agent identity management
5. 2512.15082v1 - Security controls ROI

---

## Integration with FedRAMP/Compliance

Papers relevant to compliance frameworks:

### Security Controls & Assessment
- **2512.15081v1** - Quantifying security controls (SOC 2 / FedRAMP IA-2)
- **2512.12921v1** - Lifecycle-aware taxonomy (FedRAMP CA class)
- **2505.13862v3** - Systematic safety evaluation (FedRAMP SA-11)

### Configuration Management
- **2508.17155v1** - Configuration drift vulnerabilities (CM-3)
- **2503.12188v2** - Access control in multi-agent systems (AC-2)
- **2511.19727v1** - Security boundaries (AC-4)

### Incident Detection & Response
- **2512.14860v1** - Penetration testing findings (IR-4)
- **2512.19011v1** - Attack detection mechanisms (AU-11)

---

## Statistics Summary

| Metric | Count |
|--------|-------|
| Total Papers | 14 |
| 2025 Papers | 12 |
| 2024 Papers | 2 |
| Attack-Focused | 7 |
| Defense-Focused | 5 |
| Framework/Evaluation | 2 |
| Total PDF Size | ~24 MB |
| Largest Paper | 8.1 MB (DRIP) |
| Smallest Paper | 267 KB (Cisco Framework) |

---

## Last Updated
- Date: 2025-12-24
- Papers: All verified and downloaded
- Status: Complete collection ready for research
