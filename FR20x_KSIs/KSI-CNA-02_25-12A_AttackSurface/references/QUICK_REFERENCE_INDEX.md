# Attack Path Analysis Research - Quick Reference Index
**Date:** December 10, 2025

## Production-Ready Tools - Priority Reading List

### HIGHEST PRIORITY (Start Here)

1. **ATAG - AI-Agent Threat Assessment** (2506.02859)
   - Location: `/attack_graph_analysis/2506.02859_ATAG_AI_agent_threat_assessment.pdf`
   - Why: Novel framework for AI-agent security with LLM Vulnerability Database
   - Production: YES - Extends MulVAL for AI-specific threats

2. **TRiSM - Agentic AI Security Framework** (2506.04133)
   - Location: `/privilege_escalation/2506.04133_TRiSM_agentic_AI_security.pdf`
   - Why: Comprehensive multi-agent security with RBAC/ABAC
   - Production: YES - Framework for production AI systems

3. **Neo4j Threat Hunting** (2301.12013)
   - Location: `/graph_security_modeling/2301.12013_neo4j_threat_hunting.pdf`
   - Why: Enterprise-grade graph database for security operations
   - Production: YES - OSINT integration, production deployment

4. **MulVAL Extensions Survey** (2208.05750)
   - Location: `/attack_graph_analysis/2208.05750_MulVAL_extensions_survey.pdf`
   - Why: Most extendable/scalable attack graph framework
   - Production: YES - MITRE ATT&CK integration

5. **Graphene - Infrastructure Security Analysis** (2312.13119)
   - Location: `/attack_graph_analysis/2312.13119_graphene_infrastructure_security_analysis.pdf`
   - Why: ML-based attack graph generation on Google Cloud
   - Production: YES - Deployed in production environment

### HIGH PRIORITY (Read Next)

6. **LMDG - Lateral Movement Dataset** (2508.02942)
   - Location: `/lateral_movement_detection/2508.02942_LMDG_lateral_movement_dataset_generation.pdf`
   - Why: High-fidelity dataset for training detection systems
   - Production: Research dataset enabling production tools

7. **Vulnerability Prioritization Survey** (2502.11070)
   - Location: `/attack_surface_mapping/2502.11070_vulnerability_prioritization_survey.pdf`
   - Why: Validates need for adaptive, context-aware prioritization
   - Production: Framework guidance

8. **LLM Cybersecurity Survey** (2504.15622)
   - Location: `/lateral_movement_detection/2504.15622_LLM_cybersecurity_survey.pdf`
   - Why: LLM capabilities for lateral movement detection
   - Production: Emerging

9. **Multi-Agent Security Challenges** (2505.02077)
   - Location: `/privilege_escalation/2505.02077_multi_agent_security_challenges.pdf`
   - Why: Identifies production gaps in multi-agent security
   - Production: Research directions

10. **ML Security Policy Analysis** (2501.00085)
    - Location: `/graph_security_modeling/2501.00085_ML_security_policy_analysis.pdf`
    - Why: Neo4j + Node2vec + ML achieving 95% accuracy
    - Production: YES - Automated policy analysis

---

## By Research Category

### Attack Graph Analysis (12 papers, 21MB)

**Production-Ready:**
- 2506.02859_ATAG_AI_agent_threat_assessment.pdf
- 2208.05750_MulVAL_extensions_survey.pdf
- 2312.13119_graphene_infrastructure_security_analysis.pdf

**Emerging:**
- 2408.05855_RAG_LLM_attack_graph_generation.pdf
- 2505.11565_ACSE_eval_LLM_cloud_threat_modeling.pdf

**Research/Supporting:**
- 2311.10050_graph_models_cybersecurity_survey.pdf
- 2504.07839_deep_learning_intrusion_detection_survey.pdf
- 2310.01689_dynamic_attack_graphs_IoT.pdf
- 2503.16392_graph_of_effort_AI_vulnerability_assessment.pdf
- 2507.10873_alerts_to_intelligence_LLM_aided.pdf
- 2412.14375_network_modelling_cyber_graphs.pdf
- 2310.13079_critical_path_prioritization_attack_graphs.pdf

### Privilege Escalation (8 papers, 27MB)

**Production-Ready:**
- 2506.04133_TRiSM_agentic_AI_security.pdf
- 2510.23883_agentic_AI_security_threats_defenses.pdf

**Research:**
- 2505.02077_multi_agent_security_challenges.pdf
- 2505.08807_security_internet_of_agents.pdf
- 2506.12519_exploiting_AI_adversarial_offensive.pdf
- 2110.01362_automating_privilege_escalation_DRL.pdf
- 2506.08837_AI_agent_security_paper.pdf
- 2509.07457_APT_longitudinal_analysis.pdf

### Graph Security Modeling (6 papers, 22MB)

**Production-Ready:**
- 2301.12013_neo4j_threat_hunting.pdf (13.2MB - COMPREHENSIVE)
- 2501.00085_ML_security_policy_analysis.pdf

**Research:**
- 2405.20762_access_control_graph_structured_data.pdf
- 2401.05680_GNN_defensive_cyber_operations.pdf
- 2504.02120_graph_analytics_cyber_physical_resilience.pdf
- 2508.17222_privacy_risks_graph_RAG.pdf

### Lateral Movement Detection (6 papers, 13MB)

**Production-Ready:**
- 2508.02942_LMDG_lateral_movement_dataset_generation.pdf
- 2411.10279_lateral_movement_time_aware_subgraph.pdf

**Emerging:**
- 2504.15622_LLM_cybersecurity_survey.pdf

**Research:**
- 2108.02713_role_based_lateral_movement_unsupervised.pdf
- 2208.13524_lateral_movement_user_behavioral_analysis.pdf
- 1902.04387_real_time_lateral_movement_edge_computing.pdf

### Attack Surface Mapping (6 papers, 4.9MB)

**Production-Ready:**
- 2502.11070_vulnerability_prioritization_survey.pdf
- 2506.01220_vulnerability_management_chaining.pdf
- 2503.11917_AI_cyberattack_capabilities_framework.pdf

**Research:**
- 2507.07416_securing_critical_infrastructure_AI_framework.pdf
- 2507.08623_quantum_ML_security_kill_chain.pdf
- 2206.10272_attack_paths_kill_chain.pdf

---

## By Technology/Framework

### Neo4j Graph Database
- **2301.12013** - Neo4j threat hunting (PRIMARY)
- 2501.00085 - ML security policy analysis with Neo4j
- 2310.01689 - Dynamic attack graphs IoT with Neo4j
- 2312.13119 - Graphene using Neo4j

### MulVAL Framework
- **2208.05750** - MulVAL extensions survey (PRIMARY)
- **2506.02859** - ATAG extending MulVAL for AI agents
- 2408.05855 - RAG-LLM with MulVAL

### LLM Integration
- 2408.05855 - RAG-LLM attack graph generation
- 2505.11565 - ACSE-Eval LLM cloud threat modeling
- 2504.15622 - LLM cybersecurity survey
- 2507.10873 - LLM-aided alerts to intelligence

### AI Agent Security
- **2506.02859** - ATAG AI-agent threat assessment
- **2506.04133** - TRiSM agentic AI security
- 2510.23883 - Agentic AI security threats/defenses
- 2505.02077 - Multi-agent security challenges
- 2505.08807 - Internet of agents security
- 2506.08837 - AI agent security patterns

### Machine Learning / Deep Learning
- 2501.00085 - ML-based security policy analysis
- 2504.07839 - Deep learning intrusion detection survey
- 2401.05680 - GNN defensive cyber operations
- 2110.01362 - Deep RL privilege escalation

---

## Top 10 Most Cited / Influential Papers

1. **MulVAL Extensions Survey** (2208.05750) - Foundation for attack graphs
2. **Neo4j Threat Hunting** (2301.12013) - Production graph database use
3. **ATAG** (2506.02859) - First AI-agent specific threat framework
4. **TRiSM** (2506.04133) - Comprehensive agentic AI security
5. **Graph Models Survey** (2311.10050) - 70+ attack graph formalisms
6. **DL-IDS Survey** (2504.07839) - Deep learning intrusion detection
7. **Vulnerability Prioritization Survey** (2502.11070) - Attack surface analysis
8. **LMDG** (2508.02942) - First realistic lateral movement dataset
9. **LLM Cybersecurity Survey** (2504.15622) - LLM security applications
10. **Graphene** (2312.13119) - Production ML attack graph generation

---

## Papers by Institution

### Google
- 2312.13119 - Graphene (deployed on Google Cloud)

### MITRE
- 2506.12519 - OCCULT Framework mention
- All papers using ATT&CK framework

### Academic (Stanford, MIT, CMU)
- Multiple papers across all categories
- Focus: GNN, ML, theoretical frameworks

---

## Reading Strategies

### For Immediate Implementation (1 week)
1. Read ATAG (2506.02859)
2. Read TRiSM (2506.04133)
3. Skim Neo4j paper (2301.12013) - focus on architecture
4. Read MulVAL survey (2208.05750) - focus on extension patterns

### For Framework Design (1 month)
- All "Production-Ready" papers above
- Plus: Graphene, LMDG, Vulnerability Prioritization Survey
- Focus: Integration patterns between frameworks

### For Comprehensive Understanding (3 months)
- Read all 38 papers systematically
- Start with surveys/reviews first
- Then production tools
- Finally research/emerging work

---

## Key Validation Points

### Survey Claims VALIDATED:
✅ Need for systematic attack path analysis
✅ Static models insufficient for cloud environments
✅ AI-specific attack paths require new frameworks
✅ Graph-based modeling essential for complexity
✅ Lateral movement detection dataset gap exists

### Production Gaps IDENTIFIED:
⚠️ AI agent privilege escalation detection
⚠️ Multi-agent security standardization
⚠️ Dynamic threat intelligence integration
⚠️ Real-time attack surface adaptation
⚠️ Cross-cloud attack graph federation

---

## Implementation Roadmap

### Phase 1: Foundation (Months 1-3)
- Deploy Neo4j for security graph modeling
- Implement MulVAL with AI-specific extensions (ATAG pattern)
- Integrate MITRE ATT&CK framework

### Phase 2: AI Security (Months 4-6)
- Implement TRiSM principles for multi-agent systems
- Deploy AI agent identity and access controls
- Establish privilege escalation detection

### Phase 3: Detection (Months 7-9)
- Train lateral movement detection using LMDG dataset
- Implement LMDetect framework
- Deploy GNN-based intrusion detection

### Phase 4: Automation (Months 10-12)
- Implement Graphene-style ML attack graph generation
- Deploy LLM-enhanced threat modeling
- Establish automated vulnerability prioritization

---

**Total Collection:** 38 papers, ~88MB
**Directory:** /Users/tamnguyen/Documents/GitHub/ksi_watch/KSI-CNA-02_25-12A_AttackSurface/references/
**Compiled:** December 10, 2025
