# Immutable Infrastructure and Container Security Research Summary

**Research Period**: 2024-2025
**Total Papers Retrieved**: 43
**Date Generated**: December 10, 2025
**Issue**: #10 - Immutable Infrastructure Survey

---

## Executive Summary

This comprehensive research survey retrieved 43 papers from ArXiv focusing on immutable infrastructure, container security, and cloud-native security practices. The research covers five critical domains: container security (9 papers), attack surface reduction (7 papers), runtime security and isolation (9 papers), GitOps and Infrastructure-as-Code (9 papers), and serverless security (9 papers).

The papers predominantly focus on **2025 publications** (39 papers from 2025, 4 from 2024), providing cutting-edge insights into:
- AI-driven security automation for containers and IaC
- eBPF-based runtime security monitoring
- Declarative infrastructure reconciliation
- Serverless architecture vulnerabilities
- Container policy generation and enforcement

---

## Research Categories and Key Findings

### 1. Container Security (9 Papers)

**Key Papers:**

1. **BEACON: Automatic Container Policy Generation using Environment-aware Dynamic Analysis**
   - Authors: Haney Kang, Eduard Marin, Myoungsung You, Diego Perino, Seungwon Shin
   - Published: November 29, 2025
   - Focus: Automated container security policy generation through dynamic analysis
   - File: `Q1_1_2512.00414v1.pdf`

2. **GenSIaC: Toward Security-Aware Infrastructure-as-Code Generation with Large Language Models**
   - Authors: Yikun Li, Matteo Grella, Daniel Nahmias, Gal Engelberg, Dan Klein
   - Published: November 15, 2025
   - Focus: LLM-based secure IaC generation
   - File: `Q1_2_2511.12385v1.pdf`

3. **A High-performance Real-time Container File Monitoring Approach Based on Virtual Machine Introspection**
   - Authors: Kai Tan, Dongyang Zhan, Lin Ye, Hongli Zhang, Binxing Fang
   - Published: September 19, 2025
   - Focus: VMI-based container monitoring for real-time threat detection
   - File: `Q1_3_2509.16030v1.pdf`

4. **Locked In, Leaked Out: Measuring Isolation via Kernel Locks**
   - Authors: Anjali, Michael M. Swift
   - Published: July 28, 2025
   - Focus: Container isolation vulnerabilities through kernel lock analysis
   - File: `Q1_4_2507.21248v1.pdf`

5. **Docker under Siege: Securing Containers in the Modern Era**
   - Authors: Gogulakrishnan Thiyagarajan, Prabhudarshi Nayak
   - Published: May 31, 2025
   - Focus: Comprehensive Docker security best practices and threat mitigation
   - File: `Q1_5_2506.02043v1.pdf`

6. **LLMSecConfig: An LLM-Based Approach for Fixing Software Container Misconfigurations**
   - Authors: Ziyang Ye, Triet Huynh Minh Le, M. Ali Babar
   - Published: February 4, 2025
   - Focus: Automated container misconfiguration remediation using LLMs
   - File: `Q1_9_2502.02009v1.pdf`

**Key Findings:**
- **AI/LLM Integration**: Emerging trend of using large language models for automated security policy generation and misconfiguration detection
- **Dynamic Analysis**: Shift from static analysis to environment-aware dynamic policy generation
- **Isolation Vulnerabilities**: Novel attack vectors through kernel-level side channels
- **Real-time Monitoring**: VMI-based approaches for non-invasive container monitoring

---

### 2. Attack Surface Reduction & Minimal Images (7 Papers)

**Key Papers:**

1. **Holographic Projection and Cyber Attack Surface: A Physical Analogy for Digital Security**
   - Authors: Ricardo Queiroz de Araujo Fernandes, Anderson Santos, Daniel Maier de Carvalho, André Luiz Bandeira Molina
   - Published: July 3, 2025
   - Focus: Novel framework for understanding and visualizing attack surfaces
   - File: `Q2_3_2507.03136v1.pdf`

2. **Combined Static Analysis and Machine Learning Prediction for Application Debloating**
   - Authors: Chris Porter, Sharjeel Khan, Kangqi Ni, Santosh Pande
   - Published: March 30, 2024
   - Focus: ML-driven application debloating for minimal container images
   - File: `Q2_7_2404.00196v1.pdf`

**Key Findings:**
- **Application Debloating**: Machine learning techniques for identifying and removing unnecessary code/dependencies
- **Attack Surface Visualization**: Novel approaches to quantifying and reducing attack surfaces
- **Limited Direct Research**: Fewer papers specifically on distroless/minimal images, suggesting opportunity for future research

**Note**: This category had significant noise with unrelated mathematical papers. Only 2 papers directly relevant to container security and attack surface reduction.

---

### 3. Runtime Security & Isolation (9 Papers)

**Key Papers:**

1. **eBPF-PATROL: Protective Agent for Threat Recognition and Overreach Limitation using eBPF in Containerized and Virtualized Environments**
   - Authors: Sangam Ghimire, Nirjal Bhurtel, Roshan Sahani, Sudan Jha
   - Published: November 22, 2025
   - Focus: eBPF-based runtime security monitoring and threat detection
   - File: `Q3_2_2511.18155v1.pdf`

2. **WebAssembly and Unikernels: A Comparative Study for Serverless at the Edge**
   - Authors: Valerio Besozzi, Enrico Fiasco, Marco Danelutto, Patrizio Dazzi
   - Published: September 11, 2025
   - Focus: Comparing WebAssembly and unikernel isolation for edge computing
   - File: `Q3_6_2509.09400v1.pdf`

3. **Locked In, Leaked Out: Measuring Isolation via Kernel Locks**
   - Authors: Anjali, Michael M. Swift
   - Published: July 28, 2025
   - Focus: Kernel-level isolation vulnerabilities
   - File: `Q3_7_2507.21248v1.pdf`

4. **Performance Characterization of Containers in Edge Computing**
   - Authors: Ragini Gupta, Klara Nahrstedt
   - Published: May 4, 2025
   - Focus: Container performance and isolation in edge environments
   - File: `Q3_9_2505.02082v2.pdf`

5. **Investigating the Impact of Isolation on Synchronized Benchmarks**
   - Authors: Nils Japke, Furat Hamdan, Diana Baumann, David Bermbach
   - Published: November 5, 2025
   - Focus: Isolation mechanisms and their performance impact
   - File: `Q3_5_2511.03533v1.pdf`

**Key Findings:**
- **eBPF Dominance**: eBPF emerging as primary technology for runtime security monitoring in containers
- **MicroVM vs WebAssembly**: Comparative analysis showing WebAssembly advantages for edge computing
- **Kernel Lock Side Channels**: Novel attack vectors exploiting kernel synchronization primitives
- **Edge Computing Focus**: Growing research on container security for edge/IoT deployments
- **No Direct gVisor/Firecracker Papers**: Limited recent research specifically on gVisor or Firecracker in 2024-2025

---

### 4. GitOps & Infrastructure-as-Code (9 Papers)

**Key Papers:**

1. **GenSIaC: Toward Security-Aware Infrastructure-as-Code Generation with Large Language Models**
   - Authors: Yikun Li, Matteo Grella, Daniel Nahmias, Gal Engelberg, Dan Klein
   - Published: November 15, 2025
   - Focus: LLM-based secure IaC generation
   - File: `Q4_1_2511.12385v1.pdf`

2. **Accelerating Control Systems with GitOps: A Path to Automation and Reliability**
   - Authors: M. Gonzalez, M. Acosta
   - Published: November 7, 2025
   - Focus: GitOps for control system automation
   - File: `Q4_3_2511.05663v1.pdf`

3. **GITER: A Git-Based Declarative Exchange Model Using Kubernetes-Style Custom Resources**
   - Authors: Christos Tranoris
   - Published: November 6, 2025
   - Focus: Git-based declarative infrastructure management
   - File: `Q4_4_2511.04182v1.pdf`

4. **Automated Cloud Infrastructure-as-Code Reconciliation with AI Agents**
   - Authors: Zhenning Yang, Hui Guan, Victor Nicolet, Brandon Paulsen, Joey Dodds
   - Published: October 23, 2025
   - Focus: AI-driven drift detection and reconciliation
   - File: `Q4_5_2510.20211v1.pdf`

5. **Multi-Agent Code-Orchestrated Generation for Reliable Infrastructure-as-Code**
   - Authors: Rana Nameer Hussain Khan, Dawood Wasif, Jin-Hee Cho, Ali Butt
   - Published: October 4, 2025
   - Focus: Multi-agent systems for IaC generation
   - File: `Q4_7_2510.03902v1.pdf`

6. **Detection of security smells in IaC scripts through semantics-aware code and language processing**
   - Authors: Aicha War, Adnan A. Rawass, Abdoul K. Kabore, Jordan Samhi, Jacques Klein
   - Published: September 23, 2025
   - Focus: NLP-based security smell detection in IaC
   - File: `Q4_8_2509.18790v1.pdf`

7. **Security smells in infrastructure as code: a taxonomy update beyond the seven sins**
   - Authors: Aicha War, Serge L. B. Nikiema, Jordan Samhi, Jacques Klein, Tegawende F. Bissyande
   - Published: September 23, 2025
   - Focus: Comprehensive IaC security anti-patterns taxonomy
   - File: `Q4_9_2509.18761v1.pdf`

8. **The Hidden Dangers of Public Serverless Repositories: An Empirical Security Assessment**
   - Authors: Eduard Marin, Jinwoo Kim, Alessio Pavoni, Mauro Conti, Roberto Di Pietro
   - Published: October 20, 2025
   - Focus: Security vulnerabilities in public IaC repositories
   - File: `Q4_6_2510.17311v1.pdf`

**Key Findings:**
- **AI-Driven IaC**: Strong trend toward AI agents for IaC generation, validation, and drift detection
- **Security Smells**: Comprehensive taxonomies of IaC security anti-patterns emerging
- **GitOps Maturity**: GitOps expanding beyond Kubernetes to control systems and edge computing
- **Drift Detection**: Automated reconciliation using AI agents for infrastructure drift
- **Public Repository Risks**: Empirical evidence of widespread security issues in public IaC repositories

---

### 5. Serverless Security (9 Papers)

**Key Papers:**

1. **Metronome: Differentiated Delay Scheduling for Serverless Functions**
   - Authors: Zhuangbin Chen, Juzheng Zheng, Zibin Zheng
   - Published: December 5, 2025
   - Focus: Serverless function scheduling and cold start optimization
   - File: `Q5_1_2512.05703v1.pdf`

2. **A Comprehensive Review of Denial of Wallet Attacks in Serverless Architectures**
   - Authors: Mark Dorsett, Scott Mann, Jabed Chowdhury, Abdun Mahmood
   - Published: August 24, 2025
   - Focus: Economic DoS attacks on serverless platforms
   - File: `Q5_9_2508.19284v1.pdf`

3. **Dynamic Function Configuration and its Management in Serverless Computing: A Taxonomy and Future Directions**
   - Authors: Siddharth Agarwal, Maria A. Rodriguez, Rajkumar Buyya
   - Published: October 2, 2025
   - Focus: Serverless configuration management and optimization
   - File: `Q5_5_2510.02404v1.pdf`

4. **Characterizing FaaS Workflows on Public Clouds: The Good, the Bad and the Ugly**
   - Authors: Varad Kulkarni, Nikhil Reddy, Tuhin Khare, Abhinandan S. Prasad, Chitra Babu
   - Published: September 27, 2025
   - Focus: Empirical analysis of FaaS workflow security and performance
   - File: `Q5_6_2509.23013v1.pdf`

5. **AgentX: Towards Orchestrating Robust Agentic Workflow Patterns with FaaS-hosted MCP Services**
   - Authors: Shiva Sai Krishna Anand Tokal, Vaibhav Jha, Anand Eswaran, Praveen Jayachandran, Yogesh Simmhan
   - Published: September 9, 2025
   - Focus: Agentic workflows with serverless MCP services
   - File: `Q5_7_2509.07595v1.pdf`

6. **SERFLOW: A Cross-Service Cost Optimization Framework for SLO-Aware Dynamic ML Inference**
   - Authors: Zongshun Zhang, Ibrahim Matta
   - Published: October 31, 2025
   - Focus: Cost optimization for serverless ML workloads
   - File: `Q5_2_2510.27182v1.pdf`

**Key Findings:**
- **Economic Security**: Denial of Wallet attacks emerging as critical serverless security concern
- **Cold Start Security**: Security implications of serverless cold starts and scheduling
- **MCP Integration**: Model Context Protocol (MCP) integration with FaaS for agentic workflows
- **ML Workloads**: Serverless increasingly used for dynamic ML inference with cost/security tradeoffs
- **Configuration Complexity**: Dynamic configuration management posing security challenges

---

## Cross-Cutting Themes

### 1. AI/LLM Integration in Security
**Papers**: 6+ papers directly using AI/LLMs for security automation

- **GenSIaC**: LLM-based secure IaC generation
- **LLMSecConfig**: Automated container misconfiguration fixing
- **Automated IaC Reconciliation**: AI agents for drift detection
- **Multi-Agent IaC Generation**: Collaborative AI systems for IaC

**Trend**: Rapid adoption of LLMs for security automation, policy generation, and vulnerability detection.

### 2. eBPF as Runtime Security Foundation
**Papers**: 2+ papers specifically on eBPF

- **eBPF-PATROL**: Comprehensive eBPF-based threat detection
- **Runtime Monitoring**: Non-invasive kernel-level security monitoring

**Trend**: eBPF becoming de facto standard for container runtime security monitoring.

### 3. Immutability Through Declarative Infrastructure
**Papers**: 9 papers on GitOps and declarative IaC

- **Git-Based Declarative Models**: GITER and Kubernetes-style CRDs
- **Drift Detection**: Automated reconciliation to enforce immutability
- **Security Smells**: Comprehensive taxonomies of IaC anti-patterns

**Trend**: GitOps and declarative infrastructure as primary mechanisms for achieving immutability.

### 4. Edge Computing Security
**Papers**: 4+ papers on edge/IoT container security

- **WebAssembly vs Unikernels**: Lightweight isolation for edge
- **Container Performance**: Edge-specific performance and security tradeoffs
- **Serverless at Edge**: FaaS security in resource-constrained environments

**Trend**: Growing focus on container security for edge computing and IoT.

### 5. Economic Security Concerns
**Papers**: 2 papers on cost-based attacks

- **Denial of Wallet**: Economic DoS attacks on serverless
- **Cost Optimization**: Security vs cost tradeoffs in serverless

**Trend**: Economic security emerging as critical consideration for serverless and cloud-native.

---

## Research Gaps Identified

### 1. Limited Distroless/Minimal Image Research
- Only 2 relevant papers on attack surface reduction through minimal images
- **Opportunity**: More research needed on distroless base image security benefits

### 2. Lack of gVisor/Firecracker-Specific Research
- No papers specifically on gVisor or Firecracker in 2024-2025
- **Opportunity**: Comparative analysis of container runtime security (runc vs gVisor vs Firecracker)

### 3. Kubernetes Security Hardening
- Limited papers on Kubernetes-specific security hardening
- **Opportunity**: RBAC, Pod Security Standards, admission controllers

### 4. Supply Chain Security for Containers
- Limited research on container image supply chain security
- **Opportunity**: Image signing, SBOM generation, vulnerability scanning

### 5. Multi-Tenancy Security
- Few papers on secure multi-tenancy in container platforms
- **Opportunity**: Namespace isolation, network policies, resource quotas

---

## Methodology Notes

### Search Execution
- **Platform**: ArXiv.org
- **Search Method**: Python arxiv library with targeted queries
- **Date Range**: 2024-2025 (prioritizing 2025)
- **Download Delay**: 3.5 seconds between downloads to respect rate limits
- **Quality Filter**: Manual verification of relevance

### Search Queries Used
1. `abs:"container security" OR abs:"docker security" OR abs:"kubernetes security"`
2. `abs:"distroless" OR abs:"minimal container" OR abs:"container hardening" OR abs:"attack surface reduction"`
3. `abs:"gVisor" OR abs:"Firecracker" OR abs:"microVM" OR abs:"container isolation" OR abs:"runtime security"`
4. `abs:"GitOps" OR abs:"declarative infrastructure" OR abs:"infrastructure as code" OR abs:"IaC security"`
5. `abs:"serverless security" OR abs:"FaaS security" OR abs:"lambda security" OR abs:"function-as-a-service"`

### Limitations
- ArXiv does not contain all academic research (some in IEEE, ACM, USENIX)
- Some queries returned noise (mathematical papers on "minimal" topics)
- Recent 2025 papers may not yet have full citations/impact analysis
- Page count filtering based on metadata (not always accurate)

---

## Repository Structure

All papers organized by query category:
```
/Users/tamnguyen/Documents/GitHub/ksi_watch/KSI-CNA-04_25-12A_ImmutableInfrastructure/references/immutable_infrastructure/
├── Q1_*  - Container Security (9 papers)
├── Q2_*  - Attack Surface Reduction (7 papers, 2 relevant)
├── Q3_*  - Runtime Security & Isolation (9 papers)
├── Q4_*  - GitOps & IaC (9 papers)
├── Q5_*  - Serverless Security (9 papers)
├── download_summary.txt
└── RESEARCH_SUMMARY.md (this file)
```

---

## Recommendations for Issue #10

### High Priority Papers to Review

1. **BEACON** (Q1_1): Automatic container policy generation - directly relevant to immutable policy enforcement
2. **eBPF-PATROL** (Q3_2): Runtime security monitoring - critical for immutable infrastructure validation
3. **GenSIaC** (Q1_2, Q4_1): LLM-based secure IaC - relevant to automated immutable infrastructure generation
4. **Automated IaC Reconciliation** (Q4_5): AI-driven drift detection - core to immutability enforcement
5. **Security Smells in IaC** (Q4_8, Q4_9): IaC anti-patterns - important for preventing misconfigurations
6. **Denial of Wallet Attacks** (Q5_9): Serverless economic security - relevant for immutable serverless
7. **WebAssembly vs Unikernels** (Q3_6): Lightweight isolation comparison - alternative to containers

### Topics for Deep Dive

1. **eBPF-based runtime enforcement** for immutable policy validation
2. **GitOps workflows** for declarative immutable infrastructure
3. **AI-driven drift detection** and automated reconciliation
4. **Serverless cold start security** implications for immutability
5. **Container image signing and supply chain security**

### Future Research Directions

1. Comparative analysis of **container runtime security** (runc vs gVisor vs Firecracker vs Kata)
2. **Distroless image security benchmarks** and attack surface quantification
3. **Kubernetes security hardening** for immutable workloads
4. **Multi-tenancy security** in immutable infrastructure platforms
5. **Economic security models** for cost-based attacks on immutable systems

---

## Statistics Summary

- **Total Papers**: 43
- **2025 Papers**: 39 (91%)
- **2024 Papers**: 4 (9%)
- **Total Size**: 97 MB
- **Average Paper Size**: 2.3 MB
- **Largest Paper**: 6.0 MB (Q2_4 - FEM Topology Optimization)
- **Query Distribution**:
  - Container Security: 9 papers (21%)
  - Attack Surface Reduction: 7 papers (16%, 2 relevant)
  - Runtime Security: 9 papers (21%)
  - GitOps & IaC: 9 papers (21%)
  - Serverless Security: 9 papers (21%)

---

## Citation Information

For citing this research survey:
```
Immutable Infrastructure and Container Security Research Survey
Generated: December 10, 2025
Repository: ksi_watch/KSI-CNA-04_25-12A_ImmutableInfrastructure
Issue: #10
Papers: 43 (ArXiv 2024-2025)
```

---

## Next Steps

1. **Detailed Review**: Read and annotate high-priority papers
2. **Gap Analysis**: Identify specific areas needing additional research
3. **Implementation**: Apply findings to ksi_watch security architecture
4. **Monitoring**: Set up alerts for new papers in these categories
5. **Contribution**: Consider publishing findings or contributing to existing research

---

**Generated by**: Claude Code (Sonnet 4.5)
**Date**: December 10, 2025
**Location**: `/Users/tamnguyen/Documents/GitHub/ksi_watch/KSI-CNA-04_25-12A_ImmutableInfrastructure/references/immutable_infrastructure/`
