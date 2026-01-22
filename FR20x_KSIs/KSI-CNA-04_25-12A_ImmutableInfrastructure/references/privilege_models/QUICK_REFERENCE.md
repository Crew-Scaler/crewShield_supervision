# Quick Reference: AI Privilege Models Research

**Research Date**: 2025-12-10 | **Total Papers**: 45 | **Directory**: `/Users/tamnguyen/Documents/GitHub/ksi_watch/KSI-CNA-04_25-12A_ImmutableInfrastructure/references/privilege_models/`

---

## Top 10 Priority Papers for Issue #10

| Rank | Title | ArXiv ID | Year | Pages | Key Topic |
|------|-------|----------|------|-------|-----------|
| 1 | OpenID Connect for Agents (OIDC-A) 1.0 | 2509.25974v1 | 2025 | ~10 | Agent Identity Standard |
| 2 | SoK: Trust-Authorization Mismatch in LLM Agents | 2512.06914v1 | 2025 | ~10 | Systemization of Knowledge |
| 3 | Prompt Flow Integrity (Prevent Privilege Escalation) | 2503.15547v2 | 2025 | ~10 | Attack Prevention |
| 4 | SAGA: Security Architecture for AI Agentic Systems | 2504.21034v2 | 2025 | ~10 | Governance Framework |
| 5 | Uncertainty-Aware, Risk-Adaptive Access Control | 2510.11414v1 | 2025 | ~10 | JIT Access |
| 6 | Policy-as-Prompt: AI Governance Rules as Guardrails | 2509.23994v2 | 2025 | ~10 | Policy-as-Code |
| 7 | Novel Zero-Trust Identity Framework for Agentic AI | 2505.19301v2 | 2025 | 24 | Zero-Trust Architecture |
| 8 | PenTest2.0: Autonomous Privilege Escalation GenAI | 2507.06742v1 | 2025 | 45 | Penetration Testing |
| 9 | Securing the Model Context Protocol (MCP) | 2511.20920v1 | 2025 | ~10 | MCP Security |
| 10 | LLM Agents Should Employ Security Principles | 2505.24019v1 | 2025 | ~10 | Best Practices |

---

## By Research Area

### Agent Identity & Authentication (5 papers)

| Title | ArXiv ID | Key Contribution |
|-------|----------|------------------|
| OpenID Connect for Agents (OIDC-A) 1.0 | 2509.25974v1 | Standard protocol for LLM agent identity |
| Agentic JWT: Secure Delegation Protocol | 2509.13597v1 | JWT-based delegation for autonomous agents (17 pages) |
| Novel Zero-Trust Identity Framework | 2505.19301v2 | Decentralized auth + fine-grained access (24 pages) |
| Multi-Cloud Framework for Zero-Trust Auth | 2510.16067v1 | Cross-cloud workload identity |
| Human-Machine Identity Blur Framework | 2503.18255v1 | Unified cybersecurity risk management |

### Privilege Escalation Prevention (4 papers)

| Title | ArXiv ID | Key Contribution |
|-------|----------|------------------|
| Prompt Flow Integrity | 2503.15547v2 | Prevent privilege escalation via prompt manipulation |
| PenTest2.0: Autonomous Privilege Escalation | 2507.06742v1 | GenAI for penetration testing (45 pages) |
| Hybrid Privilege Escalation & RCE Exploits | 2504.07287v2 | Exploit chain analysis (16 pages) |
| eBPF-PATROL: Protective Agent | 2511.18155v1 | eBPF runtime monitoring for containers |

### Just-in-Time (JIT) Access (3 papers)

| Title | ArXiv ID | Key Contribution |
|-------|----------|------------------|
| Uncertainty-Aware, Risk-Adaptive Access Control | 2510.11414v1 | LLM-judged TBAC model for dynamic access |
| Intent-Aware Authorization for Zero Trust CI/CD | 2504.14777v1 | Intent-based dynamic permissions (13 pages) |
| Authorization of Knowledge-base Agents | 2510.19324v1 | Intent-based management functions |

### Policy-as-Code (4 papers)

| Title | ArXiv ID | Key Contribution |
|-------|----------|------------------|
| Policy-as-Prompt: Governance as Guardrails | 2509.23994v2 | AI governance rules encoded as prompts |
| ARPaCCino: Agentic-RAG for Policy Compliance | 2507.10584v2 | RAG-based policy compliance checking |
| Policy-Aware Generative AI | 2510.23474v1 | Safe, auditable data access governance |
| Secure Edge-Cloud IoT Microservices (PaC) | 2406.18813v2 | Policy-as-code for microservices (16 pages, 2024) |

### RBAC/Access Control (4 papers)

| Title | ArXiv ID | Key Contribution |
|-------|----------|------------------|
| Securing AI Agents: Implementing RBAC | 2509.11431v1 | RBAC for industrial AI applications |
| KubeIntellect: Modular LLM Agent Framework | 2509.02449v1 | Kubernetes-native agent management |
| Towards HIPAA Compliant Agentic AI | 2504.17669v2 | Healthcare compliance for agents |
| Zero Trust Microservices Architectures | 2511.04925v1 | Identity federation in microservices |

---

## By Novelty and Impact

### Novel Attack Vectors Identified

1. **Prompt Flow Manipulation** (2503.15547v2)
   - Privilege escalation through prompt injection
   - Control-flow hijacking in LLM agents

2. **Zero-Click Prompt Injection** (2509.10540v1)
   - EchoLeak: First real-world production exploit
   - Autonomous exploitation without user interaction

3. **Parasitic Toolchain Attacks** (2509.06572v2)
   - MCP ecosystem compromise
   - Supply chain risks in agent tooling

4. **Control-Flow Hijacking in Multi-Agent Systems** (2510.17276v1)
   - Breaking and fixing defenses
   - Novel attack patterns in agent coordination

### Novel Defense Mechanisms

1. **Policy-as-Prompt** (2509.23994v2)
   - LLM-native policy enforcement
   - Self-enforcing governance guardrails

2. **Uncertainty-Aware Access Control** (2510.11414v1)
   - LLM judges for risk assessment
   - Dynamic authorization based on confidence

3. **eBPF Runtime Protection** (2511.18155v1)
   - Container-level privilege monitoring
   - Real-time overreach limitation

4. **Intent-Aware Authorization** (2504.14777v1)
   - Task intent verification before access
   - Zero-trust CI/CD pipeline authorization

---

## Implementation Priorities for Issue #10

### Phase 1: Foundational Identity (Weeks 1-2)
- [ ] Review **OIDC-A** standard (2509.25974v1)
- [ ] Evaluate **Agentic JWT** protocol (2509.13597v1)
- [ ] Design workload identity for AI agents
- [ ] Implement **Zero-Trust Identity Framework** (2505.19301v2)

### Phase 2: Access Control (Weeks 3-4)
- [ ] Implement **Uncertainty-Aware Access Control** (2510.11414v1)
- [ ] Deploy **Intent-Aware Authorization** (2504.14777v1)
- [ ] Design **Task-Centric Permissions** (SAGA 2504.21034v2)
- [ ] Establish RBAC baselines (2509.11431v1)

### Phase 3: Policy Enforcement (Weeks 5-6)
- [ ] Prototype **Policy-as-Prompt** (2509.23994v2)
- [ ] Implement **Policy-as-Code** framework (2507.10584v2)
- [ ] Deploy admission controls
- [ ] Establish audit logging

### Phase 4: Runtime Protection (Weeks 7-8)
- [ ] Deploy **eBPF-PATROL** (2511.18155v1)
- [ ] Implement **Prompt Flow Integrity** (2503.15547v2)
- [ ] Establish privilege boundary monitoring
- [ ] Deploy lateral movement prevention

### Phase 5: Validation & Testing (Weeks 9-10)
- [ ] Red team with **PenTest2.0** techniques (2507.06742v1)
- [ ] Test against **EchoLeak** attack vectors (2509.10540v1)
- [ ] Validate **MCP Security** (2511.20920v1)
- [ ] Comprehensive security audit

---

## Critical Security Principles from Research

### From "LLM Agents Should Employ Security Principles" (2505.24019v1):

1. **Least Privilege**: Agents should have minimum permissions for current task
2. **Separation of Duties**: No single agent should have end-to-end control
3. **Defense in Depth**: Multiple security layers for agent operations
4. **Fail Secure**: Default deny when authorization is uncertain
5. **Complete Mediation**: Every access request must be checked
6. **Audit Logging**: All agent actions must be logged immutably

### From "SAGA: Security Architecture" (2504.21034v2):

1. **Identity Verification**: Cryptographic agent identity attestation
2. **Intent Declaration**: Agents must declare intent before action
3. **Dynamic Authorization**: Real-time permission evaluation
4. **Privilege Scoping**: Time-bound, task-specific permissions
5. **Continuous Monitoring**: Runtime behavior verification
6. **Incident Response**: Automated containment of compromised agents

---

## Key Metrics and Statistics

- **Total Papers**: 45
- **2025 Papers**: 39 (87%)
- **2024 Papers**: 6 (13%)
- **Average Pages**: ~12 pages
- **Total Size**: 87MB
- **Security Focus (cs.CR)**: 38 papers (84%)
- **AI-Specific (cs.AI)**: 19 papers (42%)

---

## Search Queries Used

1. **Workload Identity & Access Control**: 8 papers
   - `abs:("workload identity" OR "machine identity" OR "agent identity") AND ("access control" OR RBAC OR authorization)`

2. **Least Privilege & AI**: 27 papers
   - `abs:("least privilege" OR "privilege escalation" OR "just-in-time access") AND (AI OR agent* OR autonomous)`

3. **Policy as Code for AI**: 5 papers
   - `abs:("policy as code" OR "admission control") AND (AI OR "machine learning" OR agent*) AND (security OR authorization)`

4. **Non-Human Identity**: 1 paper
   - `abs:("non-human identity" OR "service account") AND (security OR authentication) AND (cloud OR kubernetes)`

5. **RBAC for AI Agents**: 4 papers
   - `abs:(RBAC OR "attribute based access control" OR ABAC) AND (AI OR autonomous OR agent*)`

---

## Files in This Directory

1. **arxiv_privilege_research.py** (307 lines) - Research automation script
2. **papers_metadata.json** (966 lines) - Complete metadata for all 45 papers
3. **research_summary.md** (347 lines) - Basic summary with paper listings
4. **RESEARCH_FINDINGS.md** (438 lines) - Comprehensive analysis document
5. **QUICK_REFERENCE.md** (This file) - Quick lookup reference
6. **45 PDF files** (87MB total) - Full papers

---

## Next Actions

1. **Deep Dive Analysis**: Read top 10 papers in priority order
2. **Framework Evaluation**: Compare OIDC-A vs Agentic JWT vs Zero-Trust frameworks
3. **Prototype Development**: Implement policy-as-prompt POC
4. **Integration Design**: Map findings to Issue #10 immutable infrastructure
5. **Gap Analysis**: Identify missing research areas for service accounts

---

**Last Updated**: 2025-12-10
**Maintained By**: Research automation system
**Contact**: Issue #10 - Design: Immutable Infrastructure
