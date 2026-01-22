# Cluster 3: AI Agent Privilege Escalation & Authorization Risk
## Research Collection: Transitive Privilege, Over-Privileged Services & Authorization Models

**Research Focus**: Papers on privilege escalation in AI agent systems, over-privileged services, inter-service attack chains, least-privilege challenges, and authorization models for autonomous systems.

**Collection Date**: January 2026
**Total Papers**: 20
**Date Range**: July 2024 - December 2025
**Coverage**: Authorization, access control, privilege escalation, trust models, and identity management for AI agents

---

## Executive Summary

This collection addresses the critical security gap in AI agent authorization systems. As autonomous AI agents proliferate across cloud, enterprise, and development environments, they inherit excessive permissions and operate without adequate authorization boundaries. The research reveals three major vulnerability categories:

1. **Authorization Architecture Gaps** - Traditional IAM systems (OAuth, OIDC, SAML) were designed for humans and static machines, not dynamic autonomous agents
2. **Privilege Escalation Attack Chains** - Multi-step agent operations can bypass authorization boundaries even when individual steps appear benign
3. **Over-Privileged Services** - AI agents regularly receive permissions far exceeding their functional requirements

---

## Key Findings from Cluster Analysis

### 1. Authorization Framework Inadequacy

**Critical Finding**: Traditional identity and access management paradigms fundamentally fail for agentic AI systems.

**Evidence**:
- **2505.19301** (Zero-Trust Identity Framework): Traditional OAuth 2.0, OIDC, SAML designed for human users and static machine identities cannot handle:
  - Agent autonomy and context-dependency
  - Ephemeral agent lifecycles
  - Dynamically evolving agent capabilities
  - Complex trust relationships at scale
  - Operations at unprecedented speed and volume

- **2510.11108** (Vision for Access Control): LLM-based agents render static, rule-based access control insufficient because:
  - Agents exhibit autonomy and contextual complexity
  - Traditional binary allow/deny decisions inadequate
  - Dynamic information flows require continuous context-aware evaluation
  - Proposed Agent Access Control (AAC) framework shifts from gatekeeping to information governance

**Quantitative Metrics**:
- 63% of breached organizations either lack AI governance policies or still developing them
- 96% of enterprise employees using generative AI (2024)
- 74% adoption rate (2023) → 96% (2024) demonstrates rapid acceleration

### 2. Privilege Escalation Attack Chains

**Critical Finding**: Multi-step agent operations create privilege escalation vulnerabilities that static authorization policies cannot detect.

**Evidence**:
- **2510.06445** (Agentic Security Survey): Static binary policies fail to capture multi-step behaviors introducing real risk:
  - Tool chains that individually appear benign
  - Delayed approvals obscuring sequence of operations
  - Goal-driven privilege escalation (agent may execute seemingly compliant sequence that together violates dual-control policies)

- **2509.22040** (Prompt Injection in Coding Editors):
  - 84% success rate for remote privilege escalation
  - Attackers poison external resources (GitHub repos, dependencies)
  - Compromised tools execute malicious commands through agent
  - Attack payloads cover 70 MITRE ATT&CK techniques

- **2510.23883** (Agentic AI Security Threats):
  - **Direct Prompt Injection (DPI)**: Malicious instructions inserted into input prompts
  - **Indirect Prompt Injection (IPI)**: Malicious instructions embedded in external data agent processes
  - Leads to credential theft, malware download, unauthorized data access
  - Sandboxing vulnerabilities enable cross-session leakage and dependency pipeline attacks

**Attack Success Metrics**:
- Function Calling architecture: 73.5% attack success rate (2507.06323)
- MCP deployment paradigm: 62.59% success rate
- Chained attacks: 91-96% success rates regardless of architecture
- 3,250 attack scenarios tested across 7 LLM models

### 3. Over-Privileged AI Services

**Critical Finding**: AI agents routinely receive excessive permissions, violating least-privilege principle by default.

**Evidence**:
- **2512.11147** (MiniScope Least Privilege Framework):
  - Hierarchical permission model for tool-calling agents
  - Adapts mobile OS permission paradigm to agent contexts
  - Enables specification of minimal required permissions per task
  - Without framework: agents granted broad tool access exceeding functional requirements

- **2505.19301** (Zero-Trust Framework):
  - Proposes Decentralized Identifiers (DIDs) and Verifiable Credentials (VCs) for agents
  - Fine-grained access control mechanisms
  - Zero-Knowledge Proofs (ZKPs) for privacy-preserving attribute disclosure
  - Global session management and unified policy enforcement

- **2501.10114** (Infrastructure for AI Agents):
  - Agents require certified capabilities and behavioral properties
  - Need infrastructure for secure delegation
  - Methods for rolling back unauthorized agent actions
  - Inter-agent communication protocols must enforce permission boundaries

**Industry Confirmation**:
- Excessive Permission Scope defined as tools with "broader privileges than job requires"
- OWASP LLM08: "Excessive Agency" - root causes include excessive functionality, excessive permissions, excessive autonomy
- Security research shows AI agents commonly coerced into accessing confidential files beyond stated permissions

### 4. Inter-Service Authorization Risks

**Critical Finding**: Service-to-service authentication and inter-agent privilege delegation create attack chains across system boundaries.

**Evidence**:
- **2505.02077** (Multi-Agent Security Challenges):
  - Inter-agent privilege escalation as core security challenge
  - Authorization boundary exploitation through service-to-service requests
  - Multi-agent systems vulnerable to transitive privilege abuse

- **2504.21034** (SAGA Architecture):
  - Provider maintains access control policies for inter-agent communication
  - Cryptographic access control tokens with fine-grained control
  - Formal security guarantees for delegated permissions
  - User oversight over agent lifecycle and inter-agent interactions

- **2508.03858** (MI9 Runtime Governance):
  - Continuous authorization monitoring during agent execution
  - Agency-risk index and agent-semantic telemetry capture
  - Goal-conditioned drift detection (identify when agents deviate from authorized scope)
  - Graduated containment strategies for privilege violations

**Multi-Step Attack Chain Example**:
1. Agent requests access to "create file"
2. Agent requests "execute shell command" (appears separate)
3. Together: privilege escalation from read-only to full system compromise
4. Static policies miss the sequential risk pattern

### 5. Authorization Boundary Exploitation

**Critical Finding**: 82.4% of tested LLMs execute malicious commands when requested by peer agents, even though they resist identical direct prompts.

**Evidence**:
- **2510.23883**, **2510.06445**: Fundamental flaw in multi-agent trust models
  - Inter-agent trust boundaries weaker than human-agent boundaries
  - Authorization failures between peer agents significant security vector
  - Agents lack authorization validation for inter-agent requests

**Metrics**:
- 82.4% of LLMs vulnerable to peer-agent privilege escalation requests
- Agent-SafetyBench: 38.5% average safety score (overlooking permissions common failure mode)
- Permission overlooking, tool mismanagement, implicit safety risk failures predominant

### 6. Identity & Authentication Gaps

**Critical Finding**: Agent identities undefined, leading to unaccountable privilege usage and loss of audit trails.

**Evidence**:
- **2510.25819** (Identity Management for Agentic AI):
  - Urgent challenges in authentication and authorization for agents
  - Current MCP protocols highlight demand for clarified best practices
  - No standard agent identity mechanisms across deployments
  - Proposed: agent-specific authentication and identity framework

- **2501.09674** (Authenticated Delegation):
  - Framework for auditable delegation of authority to agents
  - Clear chains of accountability for agent actions
  - Human users maintain control over agent permissions and scope
  - Auditable logs of all permission grants and revocations

- **2504.21034** (SAGA):
  - Central Provider maintains agent contact information
  - User-defined access control policies
  - Agents register with system maintaining identity and policy information
  - Enables enforcement of policies on inter-agent communication

---

## Authorization Models & Best Practices

### 1. Zero-Trust Architecture for Agents (2505.19301)

**Components**:
- **Agent Naming Service (ANS)**: Secure capability-aware discovery
- **Verifiable Credentials**: Encapsulate capabilities, provenance, behavioral scope
- **Decentralized Identifiers (DIDs)**: Persistent agent identities
- **Zero-Knowledge Proofs**: Privacy-preserving attribute verification
- **Dynamic Fine-Grained Access Control**: Context-aware permissions
- **Global Session Management**: Unified revocation across protocols

**Advantage**: Addresses dynamic, interdependent, ephemeral nature of multi-agent systems

### 2. Agent Access Control (AAC) Framework (2510.11108)

**Paradigm Shift**: From static gatekeeping to dynamic information governance

**Components**:
- **Multi-dimensional contextual evaluation**: Beyond identity to relationships, scenarios, norms
- **Adaptive response formulation**: Beyond allow/deny to redaction, summarization, transformation
- **Cognitive-driven access**: Incorporates agent reasoning and context into authorization decisions

**Advantage**: Aligns authorization with dynamic agent behavior

### 3. MI9 Runtime Governance (2508.03858)

**Real-time Controls**:
- Agency-risk index calculation
- Agent-semantic telemetry capture
- Continuous authorization monitoring
- Finite-State-Machine (FSM)-based conformance engines
- Goal-conditioned drift detection
- Graduated containment strategies

**Advantage**: Detects privilege escalation during runtime, not just pre-deployment

### 4. MiniScope Least Privilege (2512.11147)

**Principle**: Hierarchical permission model organizing tool calls into structured permission groups

**Approach**:
- Adapts mobile OS permission paradigm (familiar, proven)
- Specifies minimal set of permissions per task
- Hierarchical structure prevents privilege creep
- Context-dependent authority grants

**Advantage**: Implementable framework immediately applicable to existing agent systems

### 5. SAGA Cryptographic Access Control (2504.21034)

**Mechanism**:
- Cryptographic tokens derive from user policies
- Fine-grained control over inter-agent interactions
- Formal security guarantees (cryptographic proofs)
- Provider-mediated policy enforcement

**Advantage**: Proven cryptographic foundations, scalable to large agent networks

---

## Threat Taxonomy

### Input Manipulation Attacks
- **Direct Prompt Injection (DPI)**: Malicious instructions in input
- **Indirect Prompt Injection (IPI)**: Malicious instructions in external data
- **Long-context hijacking**: Exploiting agent memory/context windows
- **Multimodal adversarial inputs**: Attacks via images, audio in multi-modal agents

**Mitigation**: Input validation, context isolation, bounded reasoning windows

### Authorization Boundary Exploitation
- **Multi-step privilege escalation**: Benign individual steps, malicious aggregate
- **Inter-agent privilege abuse**: Agents trusting peer agent requests
- **Tool chain exploitation**: Chaining tool calls to exceed intended authority
- **Permission oversight**: Agents missing authorization requirements

**Mitigation**: Goal-conditioned drift detection, aggregate action analysis, peer verification

### Over-Privileging Vulnerabilities
- **Excessive functionality**: Tools providing more capabilities than needed
- **Excessive permissions**: Broad API access exceeding task requirements
- **Excessive autonomy**: Agents acting without sufficient human oversight
- **Inherited permissions**: Agents gaining parent process/service privileges

**Mitigation**: Least-privilege framework, hierarchical permissions, task-scoped grants

### Identity & Authentication Failures
- **Unverified agent identity**: No mechanism to authenticate agent origin
- **Spoofed agent requests**: Attacker claiming to be trusted agent
- **Credential confusion**: Agent requesting access with wrong identity context
- **Lost audit trails**: No record of which agent performed actions

**Mitigation**: DIDs, verifiable credentials, mandatory authentication, audit logging

---

## Quantitative Risk Metrics

| Metric | Value | Source |
|--------|-------|--------|
| LLMs executing malicious peer-agent commands | 82.4% | 2510.23883 |
| Function Calling attack success rate | 73.5% | 2507.06323 |
| Chained attack success rate (best case) | 96% | 2507.06323 |
| Prompt injection attack success (coding editors) | 84% | 2509.22040 |
| Agent safety oversight failure rate | 61.5% | (100% - 38.5% from Agent-SafetyBench) |
| Organizations without AI governance | 63% | Industry research |
| LLM models vulnerable in b³ benchmark | 31 tested | 2510.22620 |
| Attack scenarios in comparative study | 3,250 | 2507.06323 |
| Adversarial attacks in b³ benchmark | 194,331 | 2510.22620 |
| MITRE ATT&CK techniques covered | 70+ | 2509.22040 |
| Papers reviewed (agentic security) | 150+ | 2510.06445 |

---

## Deployment Architecture Vulnerabilities

### Function Calling (OpenAI, Claude, etc.)
- **Overall Attack Success**: 73.5%
- **Vulnerability Type**: System-centric (focuses on system exploitation)
- **Authorization Gap**: Direct API calls without intermediate service validation
- **Mitigation**: Input sanitization, output validation, tool whitelisting

### Model Context Protocol (MCP)
- **Overall Attack Success**: 62.59%
- **Vulnerability Type**: LLM-centric (focuses on model exploitation)
- **Authorization Gap**: Tool discovery and authentication mechanisms
- **Mitigation**: Strict protocol enforcement, discovery validation, capability attestation

**Critical Finding**: Counterintuitively, advanced reasoning models (o1, GPT-4o) showed higher exploitability despite better threat detection capabilities - suggesting that reasoning ability aids adversaries in finding valid attack chains.

---

## Implementation Recommendations

### 1. Immediate Actions (0-30 days)
- [ ] Audit current agent permission grants across production systems
- [ ] Implement input validation and output filtering
- [ ] Enable agent action logging and audit trails
- [ ] Map inter-agent communication paths and trust boundaries
- [ ] Establish agent identity mechanism (DIDs or similar)

### 2. Short-term (1-3 months)
- [ ] Implement MiniScope hierarchical permission model
- [ ] Deploy MI9 runtime governance framework
- [ ] Create goal-conditioned drift detection
- [ ] Establish agent authentication and verification
- [ ] Implement graduated containment strategies

### 3. Medium-term (3-6 months)
- [ ] Migrate to zero-trust identity framework (DIDs + VCs)
- [ ] Implement Agent Access Control (AAC) framework
- [ ] Deploy cryptographic access control tokens (SAGA)
- [ ] Establish multi-dimensional contextual evaluation
- [ ] Implement agent-to-agent authorization verification

### 4. Long-term (6-12 months)
- [ ] Full zero-trust agent infrastructure
- [ ] Formal security properties verification
- [ ] Agent capability attestation system
- [ ] Policy-driven automated governance
- [ ] Cross-organization agent federation protocols

---

## Paper Clusters by Focus Area

### Authorization & Access Control (8 papers)
- 2510.11108 - Vision for Access Control in LLM Agents
- 2505.19301 - Zero-Trust Identity Framework
- 2504.21034 - SAGA Security Architecture
- 2512.11147 - MiniScope Least Privilege
- 2510.25819 - Identity Management
- 2501.09674 - Authenticated Delegation
- 2512.00742 - UI Governance Patterns
- 2506.04133 - TRiSM Trust & Risk Management

### Privilege Escalation & Attack Chains (5 papers)
- 2509.22040 - Prompt Injection in Coding Editors
- 2510.06445 - Agentic Security Survey (threats pillar)
- 2507.06323 - Vulnerability Assessment (3250 attacks)
- 2510.22620 - Breaking Agent Backbones (194k attacks)
- 2505.02077 - Multi-Agent Security Challenges

### Security Surveys & Frameworks (5 papers)
- 2510.23883 - Agentic AI Security Threats/Defenses
- 2508.03858 - MI9 Runtime Governance
- 2511.21990 - Safety & Security Framework
- 2407.19354 - Emerged Security & Privacy Survey
- 2510.25445 - Agentic AI Comprehensive Survey

### Infrastructure & Governance (2 papers)
- 2501.10114 - Infrastructure for AI Agents
- 2512.05951 - Trusted AI Agents in Cloud

---

## Critical Research Gaps

1. **Cross-domain Authorization**: No unified authorization model spanning different deployment architectures (Function Calling vs MCP vs custom)

2. **Agent-to-Agent Trust**: Foundational vulnerability (82.4% failure rate) lacks comprehensive mitigation frameworks

3. **Transitive Privilege Tracking**: No automated system for detecting privilege escalation through multi-step agent sequences

4. **Performance-Security Tradeoff**: Advanced reasoning models more exploitable - need to understand why and mitigate

5. **Legacy Service Integration**: Agents connecting to traditional services with RBAC/ACL models need bridge frameworks

6. **Distributed Agent Authorization**: Multi-organization agent federations lack standardized authorization protocols

---

## Key Research Institutions

**Leading Researchers**:
- Amazon Web Services (Zero-Trust Framework)
- Salesforce (Identity Management)
- MIT (Architecture & Authorization)
- Northeastern University (SAGA)
- UC Davis (Security Survey)
- ETH Zurich (Backbone Security)
- Lakera AI (Security Benchmarks)
- Centre for the Governance of AI (Infrastructure)
- NVIDIA (Enterprise Safety Frameworks)
- Monash University (Foundational Security Survey)

---

## Bibliography Summary

**Total Papers**: 20
**2025 Papers**: 17
**2024 Papers**: 2
**2023 Papers**: 0
**2024-2025 Coverage**: 95%

**By Relevance Score**:
- Score 10 (Critical): 2 papers
- Score 9 (Essential): 7 papers
- Score 8 (Important): 7 papers
- Score 7 (Foundational): 4 papers

---

## Contact & Updates

This research collection tracks emerging threats and mitigations in agentic AI authorization as of January 2026. Given the rapid evolution of this field, expect:

- New authorization frameworks every 2-3 months
- Attack techniques evolving alongside defenses
- Industry standardization efforts (ISO, NIST, OWASP)
- Enterprise adoption of governance frameworks

**Recommended Review Cycle**: Monthly
**Expected New Papers**: 3-5 per month in this domain

---

*Collection compiled for mandatory security awareness training*
*Focus: AI-Driven Transformation & CSP Implications*
*Cluster 3: Agent Privilege Escalation & Authorization Risk*
