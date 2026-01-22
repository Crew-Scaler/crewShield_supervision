# Top Papers for Immutable Infrastructure Security - Quick Reference

**Issue #10 Critical Reading List**

---

## Tier 1: Must Read (Core Immutability & Security)

### 1. BEACON: Automatic Container Policy Generation
- **File**: `Q1_1_2512.00414v1.pdf` (2.3 MB)
- **Authors**: Haney Kang, Eduard Marin, Myoungsung You, Diego Perino, Seungwon Shin
- **Date**: November 29, 2025
- **URL**: http://arxiv.org/abs/2512.00414v1
- **Why Critical**: Automated policy generation for immutable container enforcement
- **Key Topics**: Dynamic analysis, security policy automation, container hardening

### 2. eBPF-PATROL: Runtime Security Monitoring
- **File**: `Q3_2_2511.18155v1.pdf` (1.1 MB)
- **Authors**: Sangam Ghimire, Nirjal Bhurtel, Roshan Sahani, Sudan Jha
- **Date**: November 22, 2025
- **URL**: http://arxiv.org/abs/2511.18155v1
- **Why Critical**: eBPF-based runtime validation for immutable infrastructure
- **Key Topics**: eBPF, runtime security, threat detection, containerized environments

### 3. Automated Cloud Infrastructure-as-Code Reconciliation with AI Agents
- **File**: `Q4_5_2510.20211v1.pdf`
- **Authors**: Zhenning Yang, Hui Guan, Victor Nicolet, Brandon Paulsen, Joey Dodds
- **Date**: October 23, 2025
- **URL**: http://arxiv.org/abs/2510.20211v1
- **Why Critical**: Drift detection and enforcement for immutable IaC
- **Key Topics**: Drift detection, AI agents, reconciliation, immutability enforcement

### 4. GenSIaC: Security-Aware Infrastructure-as-Code Generation
- **File**: `Q1_2_2511.12385v1.pdf` / `Q4_1_2511.12385v1.pdf` (692 KB)
- **Authors**: Yikun Li, Matteo Grella, Daniel Nahmias, Gal Engelberg, Dan Klein
- **Date**: November 15, 2025
- **URL**: http://arxiv.org/abs/2511.12385v1
- **Why Critical**: LLM-based secure IaC generation for immutable infrastructure
- **Key Topics**: LLMs, IaC security, automated generation, security-by-design

### 5. Security Smells in Infrastructure as Code: Taxonomy Update
- **File**: `Q4_9_2509.18761v1.pdf`
- **Authors**: Aicha War, Serge L. B. Nikiema, Jordan Samhi, Jacques Klein, Tegawende F. Bissyande
- **Date**: September 23, 2025
- **URL**: http://arxiv.org/abs/2509.18761v1
- **Why Critical**: Comprehensive anti-patterns to avoid in immutable IaC
- **Key Topics**: Security smells, IaC anti-patterns, best practices, taxonomy

---

## Tier 2: Important (Implementation & Validation)

### 6. GITER: Git-Based Declarative Exchange Model
- **File**: `Q4_4_2511.04182v1.pdf`
- **Authors**: Christos Tranoris
- **Date**: November 6, 2025
- **URL**: http://arxiv.org/abs/2511.04182v1
- **Why Important**: Kubernetes-style declarative infrastructure for immutability
- **Key Topics**: GitOps, declarative infrastructure, CRDs, version control

### 7. Locked In, Leaked Out: Measuring Isolation via Kernel Locks
- **File**: `Q1_4_2507.21248v1.pdf` / `Q3_7_2507.21248v1.pdf` (1.3 MB)
- **Authors**: Anjali, Michael M. Swift
- **Date**: July 28, 2025
- **URL**: http://arxiv.org/abs/2507.21248v1
- **Why Important**: Kernel-level isolation vulnerabilities in containers
- **Key Topics**: Container isolation, kernel locks, side channels, security vulnerabilities

### 8. LLMSecConfig: Fixing Container Misconfigurations
- **File**: `Q1_9_2502.02009v1.pdf` (1.1 MB)
- **Authors**: Ziyang Ye, Triet Huynh Minh Le, M. Ali Babar
- **Date**: February 4, 2025
- **URL**: http://arxiv.org/abs/2502.02009v1
- **Why Important**: Automated remediation of container misconfigurations
- **Key Topics**: LLMs, misconfiguration detection, automated remediation

### 9. WebAssembly and Unikernels: Comparative Study for Serverless
- **File**: `Q3_6_2509.09400v1.pdf` (1.9 MB)
- **Authors**: Valerio Besozzi, Enrico Fiasco, Marco Danelutto, Patrizio Dazzi
- **Date**: September 11, 2025
- **URL**: http://arxiv.org/abs/2509.09400v1
- **Why Important**: Alternative isolation mechanisms for immutable serverless
- **Key Topics**: WebAssembly, unikernels, serverless, edge computing, isolation

### 10. Denial of Wallet Attacks in Serverless Architectures
- **File**: `Q5_9_2508.19284v1.pdf`
- **Authors**: Mark Dorsett, Scott Mann, Jabed Chowdhury, Abdun Mahmood
- **Date**: August 24, 2025
- **URL**: http://arxiv.org/abs/2508.19284v1
- **Why Important**: Economic security for immutable serverless workloads
- **Key Topics**: Denial of wallet, serverless security, economic attacks, cost optimization

---

## Tier 3: Recommended (Specific Use Cases)

### 11. Detection of Security Smells in IaC Scripts
- **File**: `Q4_8_2509.18790v1.pdf`
- **Authors**: Aicha War, Adnan A. Rawass, Abdoul K. Kabore, Jordan Samhi, Jacques Klein
- **Date**: September 23, 2025
- **URL**: http://arxiv.org/abs/2509.18790v1
- **Key Topics**: NLP-based security smell detection, IaC validation

### 12. Multi-Agent Code-Orchestrated Generation for IaC
- **File**: `Q4_7_2510.03902v1.pdf`
- **Authors**: Rana Nameer Hussain Khan, Dawood Wasif, Jin-Hee Cho, Ali Butt
- **Date**: October 4, 2025
- **URL**: http://arxiv.org/abs/2510.03902v1
- **Key Topics**: Multi-agent systems, IaC generation, reliability

### 13. Accelerating Control Systems with GitOps
- **File**: `Q4_3_2511.05663v1.pdf`
- **Authors**: M. Gonzalez, M. Acosta
- **Date**: November 7, 2025
- **URL**: http://arxiv.org/abs/2511.05663v1
- **Key Topics**: GitOps, automation, reliability, control systems

### 14. Docker under Siege: Securing Containers in Modern Era
- **File**: `Q1_5_2506.02043v1.pdf` (946 KB)
- **Authors**: Gogulakrishnan Thiyagarajan, Prabhudarshi Nayak
- **Date**: May 31, 2025
- **URL**: http://arxiv.org/abs/2506.02043v1
- **Key Topics**: Docker security, best practices, threat mitigation

### 15. Container File Monitoring via Virtual Machine Introspection
- **File**: `Q1_3_2509.16030v1.pdf` (544 KB)
- **Authors**: Kai Tan, Dongyang Zhan, Lin Ye, Hongli Zhang, Binxing Fang
- **Date**: September 19, 2025
- **URL**: http://arxiv.org/abs/2509.16030v1
- **Key Topics**: VMI, real-time monitoring, container security

---

## Reading Order Recommendation

### Phase 1: Foundational Understanding (Week 1)
1. **GenSIaC** - Understand secure IaC generation principles
2. **Security Smells Taxonomy** - Learn anti-patterns to avoid
3. **Docker under Siege** - Modern container security landscape

### Phase 2: Core Immutability Mechanisms (Week 2)
4. **BEACON** - Automated policy generation
5. **Automated IaC Reconciliation** - Drift detection and enforcement
6. **GITER** - Declarative infrastructure models

### Phase 3: Runtime Enforcement (Week 3)
7. **eBPF-PATROL** - Runtime security monitoring
8. **Locked In, Leaked Out** - Isolation vulnerabilities
9. **LLMSecConfig** - Automated misconfiguration fixing

### Phase 4: Specialized Topics (Week 4)
10. **WebAssembly vs Unikernels** - Alternative isolation
11. **Denial of Wallet** - Economic security
12. **Container File Monitoring** - VMI-based monitoring

---

## Quick Comparison Matrix

| Paper | Immutability Focus | AI/LLM | eBPF | GitOps | Serverless | Priority |
|-------|-------------------|--------|------|--------|------------|----------|
| BEACON | ★★★★★ | ★★★ | ★★ | ★ | ★ | Tier 1 |
| eBPF-PATROL | ★★★★★ | ★ | ★★★★★ | ★ | ★ | Tier 1 |
| IaC Reconciliation | ★★★★★ | ★★★★★ | ★ | ★★★★ | ★ | Tier 1 |
| GenSIaC | ★★★★ | ★★★★★ | ★ | ★★★★ | ★ | Tier 1 |
| Security Smells | ★★★★ | ★★ | ★ | ★★★★★ | ★ | Tier 1 |
| GITER | ★★★★ | ★ | ★ | ★★★★★ | ★ | Tier 2 |
| Locked In/Out | ★★★ | ★ | ★★ | ★ | ★ | Tier 2 |
| LLMSecConfig | ★★★★ | ★★★★★ | ★ | ★★ | ★ | Tier 2 |
| WebAssembly/Unikernels | ★★★ | ★ | ★ | ★ | ★★★★★ | Tier 2 |
| Denial of Wallet | ★★ | ★ | ★ | ★ | ★★★★★ | Tier 2 |

Legend: ★★★★★ = Highly Relevant, ★ = Minimally Relevant

---

## Key Insights by Topic

### Immutability Enforcement
- **BEACON**: Dynamic policy generation
- **IaC Reconciliation**: Automated drift detection
- **GITER**: Declarative state management

### AI/LLM Integration
- **GenSIaC**: Secure IaC generation
- **LLMSecConfig**: Misconfiguration remediation
- **IaC Reconciliation**: Intelligent drift resolution

### Runtime Security
- **eBPF-PATROL**: Non-invasive monitoring
- **Container Monitoring**: VMI-based approach
- **Locked In/Out**: Kernel isolation analysis

### GitOps & Declarative
- **GITER**: Git-based declarative exchange
- **Security Smells**: Anti-pattern detection
- **GitOps Control Systems**: Automation patterns

### Serverless Immutability
- **WebAssembly/Unikernels**: Lightweight isolation
- **Denial of Wallet**: Economic security
- **FaaS Workflows**: Security characterization

---

## Additional Resources

### Complementary Reading (Not in Collection)
1. Kubernetes Pod Security Standards documentation
2. NIST SP 800-190: Application Container Security Guide
3. CIS Docker Benchmark
4. SLSA Framework for supply chain security
5. Sigstore for artifact signing

### Tools to Investigate
1. **Falco** - Runtime security (eBPF-based)
2. **Open Policy Agent (OPA)** - Policy enforcement
3. **Trivy** - Container vulnerability scanning
4. **Cosign** - Container signing
5. **ArgoCD** - GitOps continuous delivery
6. **Flux** - GitOps toolkit
7. **Kyverno** - Kubernetes policy management

### Future Paper Searches
- USENIX Security Symposium 2024-2025
- IEEE S&P (Oakland) container security papers
- ACM CCS serverless security research
- NDSS container isolation papers

---

**Last Updated**: December 10, 2025
**Total Papers in Collection**: 43
**Priority Papers**: 15
**Estimated Reading Time**:
- Tier 1 (5 papers): 15-20 hours
- Tier 2 (5 papers): 12-15 hours
- Tier 3 (5 papers): 10-12 hours
