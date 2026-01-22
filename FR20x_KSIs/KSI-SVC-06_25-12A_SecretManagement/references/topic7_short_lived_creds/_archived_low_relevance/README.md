# Archived Papers - Lower Relevance

This directory contains papers that were evaluated but not selected for the TOP 10 due to:
- Broader focus (not specific to short-lived credentials or token TTL)
- Lower publication year (2024 vs. 2025 when both available)
- Tangential relevance to the core topic

## Papers Archived (15 total)

### Multi-Agent Security (Broader Focus)

1. **2406.08689** - Security of AI Agents (June 2024)
   - General AI agent security survey
   - Less specific to credential management

2. **2505.02077** - Open Challenges in Multi-Agent Security (May 2025)
   - Broader multi-agent security challenges
   - Focus on cascade attacks, collusion, not credentials

3. **2505.08807** - Security of Internet of Agents: Attacks and Countermeasures (May 2025)
   - Comprehensive IoA security survey
   - Not credential-specific

### Identity Management (Not Short-Lived Credential Focus)

4. **2506.09559** - Identity and Access Management for the Computing Continuum (June 2025)
   - Focus on DIDs/VCs for edge computing
   - Less emphasis on ephemeral credentials

5. **2512.20234** - Achieving Flexible and Secure Authentication with Strong Privacy (Dec 2025)
   - Focus on anonymous credentials (ACs) and privacy
   - Not about credential TTL or rotation

6. **2503.18255** - The Human-Machine Identity Blur (March 2025)
   - Unified identity governance framework
   - Broad risk management, not credential lifetime

7. **2511.02841** - AI Agents with Decentralized Identifiers and Verifiable Credentials (Nov 2025)
   - Focus on DID/VC trust establishment
   - Not about short-lived tokens

### Certificate/Credential Status Management

8. **2406.11511** - Decentralized Credential Status Management (June 2024)
   - 2024 paper, focus on certificate revocation
   - Not about short-lived token issuance

### Formal Methods & Surveys

9. **2510.14133** - Formalizing Safety, Security, and Functional Properties of Agentic AI (Oct 2025)
   - Formal verification with temporal logic
   - Not credential management focus

10. **2510.06445** - A Survey on Agentic Security: Applications, Threats and Defenses (Oct 2025)
    - Comprehensive survey of 160+ papers
    - Broad scope, less specific to credentials

### Agent Protocols (Not Credential Focus)

11. **2511.11619** - DIAP: Decentralized Agent Identity Protocol (Nov 2025)
    - Agent identity protocol with ZKPs
    - Not focused on credential expiration

12. **2511.15712** - Secure Autonomous Agent Payments (Nov 2025)
    - Payment verification with DIDs
    - Not credential compromise mitigation

### Authorization (Not Credential TTL)

13. **2504.14777** - Intent-Aware Authorization for Zero Trust CI/CD (April 2025)
    - Policy-based authorization with OPA/Cedar
    - Focus on intent verification, not credential lifetime

### Token Research (Different Domain)

14. **2504.20493** - Token-Efficient Prompt Injection Attack (April 2025)
    - LLM reasoning token attacks
    - Not authentication/authorization tokens

15. **2504.21367** - Security Analysis of Cryptocurrency Systems on Blockchain 2.0 (April 2025)
    - Blockchain cryptocurrency tokens
    - Not OAuth/API security tokens

## Why These Papers Were Not Selected

While all these papers contribute to understanding of agent security, identity management, and authentication, they lack the specific focus on:

- **Short-lived credential mechanisms** (ephemeral tokens, short TTL)
- **Token lifecycle management** (rotation, expiration, revocation)
- **Proof of possession** (DPoP, token binding)
- **Workload credential compromise mitigation** (SPIFFE, WIF, credential brokers)
- **Practical implementation** of time-limited authentication

The TOP 10 selected papers directly address these core requirements for Issue #68 Topic 7.

## Access to Full Papers

If needed, these papers can be downloaded from:
- ArXiv: https://arxiv.org/abs/{arxiv_id}
- PDF: https://arxiv.org/pdf/{arxiv_id}

See `../metadata.json` for complete paper details and URLs.
