# Issue #33: AI Agent Authentication & Non-Human Identity Governance - Reference Papers

**Research Execution Date:** December 16, 2025
**Total Papers:** 34 (39 including pre-existing references)
**Total Size:** 232 MB
**Status:** Research Complete

## Paper Organization

Papers are organized by ArXiv ID and downloaded from https://arxiv.org/ during automated research execution.

### Naming Convention
```
{ARXIV_ID}_{FIRST_AUTHOR_LAST_NAME}_{YEAR}.pdf
```

### Examples
- `2510.25819v1_south_2025.pdf` - Identity Management for Agentic AI
- `2507.14263v1_raskar_2025.pdf` - Beyond DNS: Internet of AI Agents  
- `2511.20920v1_errico_2025.pdf` - Securing the Model Context Protocol

## Research Queries Executed

### Query 1: Agent Identity & Authentication Mechanisms (10 papers)
Focus: OpenID Connect for Agents, decentralized identity, credential management, protocol security

**Key Papers:**
- 2510.25819v1_south_2025.pdf - Identity Management for Agentic AI
- 2511.02841v2_garzon_2025.pdf - AI Agents with Decentralized Identifiers
- 2509.25974v1_nagabhushanaradhya_2025.pdf - OpenID Connect for Agents (OIDC-A) 1.0

### Query 2: Non-Human Identity Governance (4 papers)
Focus: Workload identity, service accounts, SPIFFE, zero-trust CI/CD, machine identity policies

**Key Papers:**
- 2504.14760v1_avirneni_2025.pdf - Establishing Workload Identity for Zero Trust CI/CD
- 2509.18415v1_malkapuram_2025.pdf - Context Lineage Assurance for Non-Human Identities
- 2505.19301v2_huang_2025.pdf - A Novel Zero-Trust Identity Framework for Agentic AI

### Query 3: Delegation & Trust in Multi-Agent Systems (10 papers)
Focus: NANDA Index, trust architecture, delegation protocols, agent-to-agent communication

**Key Papers:**
- 2507.14263v1_raskar_2025.pdf - Beyond DNS: Internet of AI Agents via NANDA Index
- 2512.06914v1_shi_2025.pdf - SoK: Trust-Authorization Mismatch in LLM Agent Interactions
- 2509.13597v1_goswami_2025.pdf - Agentic JWT: A Secure Delegation Protocol

### Query 4: Behavioral Anomaly Detection for Agents (10 papers)
Focus: Runtime governance, behavioral analysis, threat modeling, MCP security, anomaly detection

**Key Papers:**
- 2512.03180v1_khan_2025.pdf - AGENTSAFE: Unified Framework for Ethical Assurance
- 2511.20920v1_errico_2025.pdf - Securing the Model Context Protocol (MCP)
- 2508.03858v4_wang_2025.pdf - MI9: An Integrated Runtime Governance Framework

## Screening Methodology

### Quality Weights Applied
- 2025 publication: +50 points
- 2024 publication: +25 points
- Prestigious institution (MIT, Stanford, Berkeley, CMU, etc): +30 points
- Prestigious company (Google, Microsoft, OpenAI, Anthropic, etc): +25 points
- Abstract keyword match: +15 points

### Inclusion Criteria
- Agent-related keywords: agent, autonomous, agentic, bot, API
- Auth-related keywords: authentication, authorization, identity, credential, access, permission, privilege, governance, policy, trust, anomaly, behavioral, delegation, service account, machine identity
- Genuine focus on AI agents + identity/auth/governance topics

### Rejection Criteria
- Generic authentication papers (no agent focus)
- Deep learning/CV papers (unless directly relevant to agent behavior)
- NLP papers (unless specifically about agent identity/auth)
- Multi-agent papers focused on coordination, not trust/authorization

## Research Statistics

| Metric | Value |
|--------|-------|
| Total queries | 4 |
| Papers found | 151 |
| Papers screened | 151 |
| Papers downloaded | 34 |
| Acceptance rate | 68.3% (average) |
| 2025 papers | ~28 (82%) |
| 2024 papers | ~5 (15%) |
| Pre-2024 papers | ~1 (3%) |

## Key Research Trends

### 1. Standardization & Protocols
- OpenID Connect extensions for agents (OIDC-A)
- JWT-based delegation (Agentic JWT)
- Interoperability between heterogeneous agents

### 2. Decentralized & Zero-Trust
- Verifiable credentials and DIDs
- Zero-trust architectures
- Blockchain-based audit trails
- SPIFFE for workload identity

### 3. Infrastructure
- NANDA Index for DNS-like agent discovery
- Agent-to-agent authentication
- Service mesh patterns adapted for agents

### 4. Runtime Governance
- MI9 framework for integrated governance
- AGENTSAFE for ethical assurance
- MCP security frameworks
- Behavioral anomaly detection

### 5. Emerging Threats
- Prompt injection attacks
- Protocol exploitation
- Financial transaction autonomy
- Behavioral drift detection

## Document References

For comprehensive analysis, see:
- `ISSUE_33_ARXIV_RESEARCH_SUMMARY.md` - Full research summary with detailed findings
- `1_KSI-IAM-04_25-12A_Just-in-TimeAuthorization_survey.md` - Security authorization survey context
- `/tmp/issue_33_agent1_findings.txt` - Detailed findings report (during execution)

## Citation Recommendations

When citing these papers, use standard IEEE or ACM citation formats. Most papers are available on ArXiv and include full metadata.

Example:
```
South, T., Nagabhushanaradhya, S., & Dissanayaka, A. (2025). 
Identity Management for Agentic AI: The new frontier of authorization, 
authentication, and security for an AI agent world. arXiv preprint arXiv:2510.25819.
```

---

**Research executed with ArXiv API respect for rate limiting (3+ second delays between calls)**
**All papers downloaded successfully with standard PDF format**
**No papers rejected due to download failures**
