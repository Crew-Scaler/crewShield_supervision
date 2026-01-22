# Topic 7: Agent Compromise Impact Minimization Through Short-Lived Credentials

**Issue #68 - Topic 7**
**Research Date:** December 25, 2025

## Overview

This directory contains the TOP 10 most relevant academic papers from ArXiv (2024-2025) on short-lived credentials, token TTL, proof of possession, and agent compromise mitigation strategies.

## Research Summary

- **Total Papers Found:** 25+
- **Papers Downloaded:** 10
- **Papers Archived:** 15
- **Date Range:** Primarily 2025 (9 papers), with priority given to most recent research
- **Focus Areas:** Workload identity, ephemeral tokens, OAuth security, SPIFFE/SPIRE, credential brokers, agent security

## TOP 10 Papers (Ranked by Relevance)

### Tier 1: Directly Relevant to Short-Lived Credentials

1. **2510.16067_Multi-Cloud_Zero-Trust_Workload_Authentication.pdf** (Oct 2025) ⭐⭐⭐
   - Workload Identity Federation (WIF) with ephemeral tokens
   - Replaces static secrets with cryptographically verifiable tokens
   - Automated rotation and revocation mechanisms

2. **2504.14760_Workload_Identity_SPIFFE_Authentication.pdf** (Apr 2025) ⭐⭐⭐
   - SPIFFE/SPIRE framework for runtime-issued identities
   - Workload attestation and temporary credentials
   - Platform-neutral identity for non-human actors

3. **2504.14761_Credential_Broker_Patterns_Secure_CICD.pdf** (Apr 2025) ⭐⭐⭐
   - Credential broker patterns for dynamic issuance
   - Decouples identity from access
   - Policy-aware runtime mediation

4. **2504.17759_Identity_Control_Plane_Zero_Trust.pdf** (Apr 2025) ⭐⭐⭐
   - Identity Control Plane (ICP) architectural framework
   - Integrates SPIFFE workload identity with OIDC/SAML
   - Scoped automation tokens

### Tier 2: OAuth/Token Lifecycle Management

5. **2507.16870_OAuth_Token_Based_API_Security.pdf** (Jul 2025) ⭐⭐
   - OAuth 2.0 token lifecycle management
   - Automated key rotation and expiration policies
   - Revocation mechanisms and best practices

6. **2512.15781_Detecting_Malicious_OAuth_Apps.pdf** (Dec 2025) ⭐⭐
   - Malicious OAuth app detection
   - Real-time detection of credential abuse
   - LLM-based permission risk scoring

### Tier 3: AI Agent Security & Identity

7. **2510.25819_Identity_Management_Agentic_AI.pdf** (Oct 2025) ⭐⭐
   - AI agent identity management challenges
   - Amplified blast radius of agent compromise
   - Delegated authority at machine speed

8. **2510.23883_Agentic_AI_Security_Threats_Defenses.pdf** (Oct 2025) ⭐⭐
   - Agentic AI security threats (EchoLeak CVE-2025-32711)
   - Credential exfiltration risks
   - Cascade-based compromise in multi-agent systems

9. **2505.19301_Zero_Trust_Framework_Agentic_AI.pdf** (May 2025) ⭐⭐
   - Zero-Trust framework with DIDs/VCs
   - Inadequacy of traditional IAM (OAuth, OIDC, SAML) for agents
   - Fine-grained access control for dynamic agents

### Tier 4: Credential Detection & Prevention

10. **2506.13090_Detecting_Hard_Coded_Credentials_LLMs.pdf** (Jun 2025) ⭐
    - LLM-based detection of hard-coded credentials
    - Preventing static credential sprawl
    - Context-aware credential detection

## Key Findings

### 1. Shift to Ephemeral Credentials
The research shows a clear industry/academic consensus on moving from static, long-lived credentials to ephemeral, runtime-issued tokens:
- **Ephemeral tokens** expire within minutes to hours
- **Runtime attestation** verifies workload identity at issuance time
- **Automated rotation** eliminates credential sprawl

### 2. Workload Identity Frameworks
**SPIFFE/SPIRE** has emerged as the leading framework:
- Platform-neutral workload identity
- X.509 certificates or JWT-based SVIDs (SPIFFE Verifiable Identity Documents)
- Runtime attestation before credential issuance
- Short-lived credentials by design

### 3. Credential Broker Pattern
Separating identity from access through credential brokers:
- Runtime mediation of credential issuance
- Policy-based access control (OPA, Cedar)
- Dynamic credential scoping
- Just-in-time access

### 4. OAuth Token Lifecycle Best Practices
- **Short TTL:** Access tokens expire in 15-60 minutes
- **Refresh token rotation:** One-time use refresh tokens
- **Automated key rotation:** Regular cryptographic key updates
- **Robust revocation:** Real-time token blacklisting

### 5. AI Agent Specific Risks
AI agents create unique challenges:
- **Amplified blast radius:** Delegated authority + machine speed
- **Credential exfiltration:** Agents can be tricked into leaking credentials
- **Cascade compromise:** Compromise spreads through agent networks
- **Traditional IAM inadequacy:** OAuth/OIDC designed for humans/static workloads

### 6. Proof of Possession (Research Gap)
- **DPoP (RFC 9449)** cryptographically binds tokens to client keys
- Limited recent academic research on ArXiv (mostly IETF RFCs)
- Critical for preventing token replay even with short TTL
- Implementation guides available but empirical studies lacking

## Research Gaps Identified

1. **Limited DPoP Academic Research:** While DPoP is critical, most documentation is IETF RFCs and industry guides, not peer-reviewed research
2. **Optimal TTL Values:** Few empirical studies on optimal token TTL for different workload types
3. **Agent-Specific TTL:** Minimal research on credential lifetime specifically for AI agents vs. traditional workloads
4. **Token Binding Deprecation:** HTTP Token Binding largely abandoned; research shifted to DPoP

## Search Queries Used

1. "short-lived credentials" AND (agent OR workload) AND (compromise OR security) AND (2024 OR 2025)
2. "proof of possession" AND (token OR JWT OR SAML) AND (binding OR security) AND (2024 OR 2025)
3. "token binding" AND (compromise OR theft) AND (attack OR defense) AND (2024 OR 2025)
4. credential rotation ephemeral token TTL 2024 2025
5. OAuth DPoP token binding cryptographic 2024 2025
6. zero trust workload identity certificate 2024 2025

## File Structure

```
topic7_short_lived_creds/
├── README.md                                                          # This file
├── metadata.json                                                      # Complete metadata for all papers
├── 2510.16067_Multi-Cloud_Zero-Trust_Workload_Authentication.pdf    # Rank 1
├── 2504.14760_Workload_Identity_SPIFFE_Authentication.pdf           # Rank 2
├── 2504.14761_Credential_Broker_Patterns_Secure_CICD.pdf            # Rank 3
├── 2504.17759_Identity_Control_Plane_Zero_Trust.pdf                 # Rank 4
├── 2507.16870_OAuth_Token_Based_API_Security.pdf                    # Rank 5
├── 2510.25819_Identity_Management_Agentic_AI.pdf                    # Rank 6
├── 2510.23883_Agentic_AI_Security_Threats_Defenses.pdf             # Rank 7
├── 2505.19301_Zero_Trust_Framework_Agentic_AI.pdf                   # Rank 8
├── 2512.15781_Detecting_Malicious_OAuth_Apps.pdf                    # Rank 9
├── 2506.13090_Detecting_Hard_Coded_Credentials_LLMs.pdf            # Rank 10
└── _archived_low_relevance/                                          # 15 lower-relevance papers
    └── README.md                                                     # Documentation of archived papers
```

## Usage

1. **Start with Tier 1 papers** for core understanding of short-lived credentials and workload identity
2. **Review metadata.json** for complete abstracts and key topics
3. **Check _archived_low_relevance/** for broader context on agent security

## Citation Format

All papers available on ArXiv:
- Abstract: https://arxiv.org/abs/{arxiv_id}
- PDF: https://arxiv.org/pdf/{arxiv_id}

## Related Topics

This research supports:
- **Issue #68 Topic 7:** Agent Compromise Impact Minimization
- Zero Trust architecture implementation
- Workload identity federation
- OAuth 2.0 security hardening
- AI agent security frameworks

## Rate Limiting Compliance

All downloads respected ArXiv rate limits:
- 3+ seconds between requests
- 10 papers downloaded over ~45 seconds
- No bulk scraping or API abuse

---

**Last Updated:** December 25, 2025
**Maintained by:** Automated research workflow for ksi_watch project
