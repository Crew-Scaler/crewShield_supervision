# Container Escape Detection - Paper Repository

**Research Date:** December 10, 2025
**Total Papers:** 32 ArXiv papers (2024-2025)
**Research Focus:** Container escape detection, multi-tenant Kubernetes security, runtime monitoring

## Summary Document

**Main Summary:** `../CONTAINER_ESCAPE_SUMMARY.md` (703 lines, comprehensive analysis)

## Paper Categories

### Container Escape & Detection (4 papers)
- `2302.13865_AI_Driven_Container_Security_5G.pdf` - Comprehensive ML/AI survey
- `2104.03651_Simulated_Container_Escapes_Honeypots.pdf` - Honeypot deception techniques
- `2504.03238_Malware_Detection_Docker_Containers.pdf` - Image-based detection (COSOCO)
- `2509.09322_ORCA_Obscure_Containers.pdf` - Vulnerability scanning & SBOM

### eBPF & Syscall Monitoring (6 papers)
- `2511.18155_eBPF_PATROL_Threat_Recognition.pdf` - Runtime security agent
- `2510.10126_FedMon_Federated_eBPF_Monitoring.pdf` - Multi-cluster monitoring
- `2302.10366_Programmable_Syscall_Security_eBPF.pdf` - Seccomp-eBPF filtering
- `2311.07923_bpftime_Userspace_eBPF_Runtime.pdf` - Userspace implementation
- `2508.02736_AgentSight_eBPF_AI_Observability.pdf` - AI agent monitoring
- `2406.14020_eBPF_AI_Ransomware_Detection.pdf` - Ransomware detection

### Kubernetes Security & Isolation (6 papers)
- `2507.03387_Breaking_Bulkhead_Kubernetes_Namespace.pdf` - Cross-namespace vulnerabilities
- `2506.21134_Inside_Job_Kubernetes_Network_Misconfig.pdf` - Network misconfigurations
- `2504.11126_KubeFence_Security_Hardening.pdf` - API security hardening
- `2409.04647_Kubernetes_Security_Landscape.pdf` - AI-driven insights
- `2405.19954_GenKubeSec_LLM_Kubernetes_Misconfig.pdf` - LLM-based detection
- `2509.02449_KubeIntellect_LLM_Kubernetes.pdf` - LLM orchestration

### Multi-Tenant & Multi-Cloud (3 papers)
- `2103.13333_Multi_Tenant_Framework_Cloud_Containers.pdf` - VirtualCluster framework
- `2403.12980_Containerization_Multi_Cloud.pdf` - Multi-cloud systematic review
- `2404.18082_Cyber_Security_Containerization_Platforms.pdf` - Comparative study

### Network Segmentation & Zero Trust (2 papers)
- `2411.12162_Microsegmented_Cloud_Network_Zero_Trust.pdf` - Zero-trust architecture
- `2506.02043_Docker_Under_Siege.pdf` - Falco & Cilium integration

### Privilege Escalation & Exploits (2 papers)
- `2504.07287_Hybrid_Privilege_Escalation.pdf` - ALFA-Chains framework
- `2310.11409_LLMs_Linux_Privilege_Escalation.pdf` - hackingBuddyGPT

### Cloud-Native Threat Detection (4 papers)
- `2507.17655_HSM_TPM_Cloud_Security.pdf` - HSM/TPM security analysis
- `2412.21051_LLM_Proactive_Cloud_Defense.pdf` - LLM-PD framework
- `2505.11565_ACSE_Eval_LLM_Cloud_Threat_Modeling.pdf` - LLM threat modeling
- `2505.03945_AI_Driven_Cloud_Security.pdf` - AI-driven security

### Intrusion Detection & Anomaly Detection (3 papers)
- `2306.14750_Ensemble_Random_Isolation_Forests_IDS.pdf` - Ensemble ML methods
- `2410.18332_Network_Security_ML_IDS_Testbed.pdf` - ML-based IDS testbed
- `2503.02402_Rootkit_Detection_Temporal_Anomalies.pdf` - Temporal rootkit detection

### Practitioner Studies & Surveys (2 papers)
- `2504.07707_Managing_Container_Security_Issues.pdf` - Practitioner interviews (2024)
- `2304.00473_Kernel_Rootkit_Detection_Survey.pdf` - Rootkit detection taxonomy

## Key Findings

### Container Escape Prevalence
- **59%** of organizations experienced K8s security incidents (2024)
- **79%** of cloud enterprises had ≥1 breach (2024)
- **250,000+** clusters affected by Sys:All Loophole vulnerability

### Detection Performance
- **<1ms** latency overhead with eBPF-based tools
- **>94%** accuracy with ML-based syscall analysis
- **Real-time** detection and enforcement capabilities

### Network Segmentation Effectiveness
- **Validated:** Limits blast radius to single tenant
- **M6 (Lack of network policies)** = #1 K8s misconfiguration
- **634 misconfigurations** found in 287 applications studied

### Production Tools
- **Falco** - CNCF syscall monitoring
- **Cilium Tetragon** - eBPF security observability
- **eBPF-PATROL** - Real-time policy enforcement
- **KubeFence** - API-level security hardening

## Usage

All papers support research for **KSI Watch Issue #7 - Cluster C: Container Escape Detection**.

Papers validate:
1. Container escapes enable cross-tenant compromise (when isolation fails)
2. Network policies effectively limit blast radius
3. Multi-layered defense (isolation + monitoring + segmentation) is essential
4. Real-time detection is production-ready with modern tools

## File Naming Convention

`[ARXIV_ID]_[Descriptive_Title].pdf`

Example: `2511.18155_eBPF_PATROL_Threat_Recognition.pdf`
- **2511.18155** = ArXiv identifier
- **eBPF_PATROL_Threat_Recognition** = Human-readable title

## Total Size

Approximately 60 MB across 32 PDFs (range: 225 KB - 18 MB per file)

---

**For comprehensive analysis, see:** `../CONTAINER_ESCAPE_SUMMARY.md`
