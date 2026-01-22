# KSI-SVC-02: Network Encryption - AI/Agent Curated Discovery Questions

**KSI:** KSI-SVC-02_25-12A_NetworkEncryption
### SVC-02-Q01
**What is your organization's current cryptographic inventory baseline, and how much AI model traffic is protected with quantum-vulnerable algorithms (RSA-2048, ECDH P-256) representing immediate HNDL risk to data with >15-year confidentiality requirements?**

*Reasoning:* HNDL attacks store encrypted AI models today, decrypt when quantum computers available (2030-2035). Data with long confidentiality requirements at immediate risk. Baseline critical for prioritization.

### SVC-02-Q02
**Do you have a documented quantum threat timeline specific to your AI deployments, and how does this align with NIST's 2030-2035 CRQC estimate versus your organization's more conservative assumptions?**

*Reasoning:* AI models have multi-year confidentiality requirements. Different organizations have different risk tolerance for HNDL scenarios. Custom timelines required for informed decision-making.

### SVC-02-Q03
**What is your migration path from classical TLS 1.2 to hybrid post-quantum TLS 1.3 (X25519+ML-KEM)—do you have a concrete phased rollout plan with success metrics and performance impact budgets (10-15% handshake latency acceptable)?**

*Reasoning:* Hybrid approach maintains backward compatibility while introducing post-quantum security. Phased rollout reduces risk. Performance budget critical for real-time AI inference.

### SVC-02-Q04
**How will you manage the 2-4x certificate size increase from ML-DSA signatures versus ECDSA during hybrid PQC migration, particularly for token-based AI agent authentication where API header size is constrained?**

*Reasoning:* AI agents use token-based auth. Larger certificates may exceed HTTP header size limits. Certificate size management critical for agent orchestration.

### SVC-02-Q05
**Have you assessed the readiness of your Hardware Security Modules (HSMs) for post-quantum cryptography, considering that HSM firmware upgrades typically lag software migrations by 18-24 months?**

*Reasoning:* Master keys often stored in HSMs. HSM firmware upgrade delays block post-quantum deployment. Vendor coordination and contingency planning required.

---

## SECTION 2: AI WORKLOAD ENCRYPTION STRATEGY

**Theme:** Protecting AI model inference, training data, and model distribution across untrusted networks

### SVC-02-Q06
**How are you protecting AI model inference traffic from potential quantum decryption and side-channel attacks, particularly for sensitive proprietary models traversing untrusted networks?**

*Reasoning:* Inference is continuous throughout AI application lifetime. Side-channel attacks extract model parameters from encrypted traffic (timing analysis, power consumption). Requires strong encryption + side-channel protection.

### SVC-02-Q07
**What encryption strategy covers AI training traffic in federated learning scenarios where encrypted gradients must be aggregated without exposing plaintext training data to the parameter server?**

*Reasoning:* Federated learning uses encrypted aggregation. Requires cryptographic protocols (secure MPC, homomorphic encryption) that maintain confidentiality through aggregation. Complex threat model.

### SVC-02-Q08
**Do you have encrypted channels with cryptographic verification for AI model weights distribution, or do you rely solely on integrity checking (HMAC) without confidentiality protection during model deployment to inference endpoints?**

*Reasoning:* Model weights contain proprietary information. Confidentiality protection required during distribution. HMAC alone provides integrity, not confidentiality.

### SVC-02-Q09
**How are you handling the tension between AI performance optimization (batch processing, GPU acceleration) and cryptographic operations (which prefer constant-time, side-channel resistant implementations that reduce throughput)?**

*Reasoning:* Performance optimization and cryptographic security are competing goals. Batching reduces per-sample overhead but increases latency. Constant-time crypto reduces vulnerability but increases computation. Requires careful tradeoff analysis.

### SVC-02-Q10
**Are your AI inference pipelines capable of accepting encrypted inputs and producing encrypted outputs without decryption to the application layer, enabling end-to-end encryption across untrusted compute environments?**

*Reasoning:* End-to-end encryption prevents plaintext exposure in untrusted environments (cloud, third-party compute). Requires homomorphic encryption or secure MPC. Strong security posture but significant performance cost.

---

## SECTION 3: ZERO-TRUST CRYPTOGRAPHIC ARCHITECTURE FOR AI

**Theme:** Establishing cryptographic identity and trust for autonomous agents and non-human identities

### SVC-02-Q11
**How do you establish cryptographic trust for non-human identities (NHIs) at scale—can your infrastructure bind each agent, microservice, and API endpoint to a unique cryptographic identity with automated certificate lifecycle management?**

*Reasoning:* AI agents are non-human identities. Traditional PKI not designed for NHI scale (potentially thousands of agents). Automated lifecycle management required for <24-hour rotation targets.

### SVC-02-Q12
**What is your solution to the "secret-zero bootstrap problem" for agentic systems—how do AI agents obtain initial credentials for requesting encrypted credentials from your Key Management System without pre-existing credentials or hardcoded secrets?**

*Reasoning:* Agents cannot have hardcoded secrets. Bootstrap must be cryptographically secure (e.g., SPIFFE/SPIRE, cloud-specific identity providers). Hardcoded secrets are anti-pattern.

### SVC-02-Q13
**Do you have a zero-trust network encryption policy that denies plaintext inter-service communication by default and requires explicit cryptographic verification for every agent-to-agent and service-to-service connection?**

*Reasoning:* Default-deny encryption prevents accidental plaintext communication. Explicit verification (mTLS) required for agent trust chains.

### SVC-02-Q14
**How are you implementing mutual TLS (mTLS) across AI agent communication channels, particularly for high-velocity agent-to-agent orchestration where handshake latency and certificate validation overhead must remain <5ms?**

*Reasoning:* Agent coordination can have 100s of messages/second. mTLS handshake latency (<5ms) is aggressive target. Requires connection pooling, certificate caching, optimized validation.

### SVC-02-Q15
**Can your authorization policies bind encryption context (which encryption key was used, which algorithm) to access control decisions, enabling proofs that data was encrypted with approved cryptographic parameters before granting access?**

*Reasoning:* Authorization should depend on encryption strength used. Weaker algorithms (due to legacy compatibility) should restrict access. Encryption context binding enables this.

---

## SECTION 4: ENCRYPTED AI PROCESSING & HOMOMORPHIC ENCRYPTION

**Theme:** Enabling computation on encrypted data without decryption (homomorphic encryption, secure MPC)

### SVC-02-Q16
**Are you evaluating homomorphic encryption for use cases where AI computations must occur on encrypted data without decryption (e.g., privacy-preserving inference on sensitive customer data)?**

*Reasoning:* Homomorphic encryption enables computation without decryption. Strong privacy guarantee but significant computational overhead (1000x-1,000,000x). Use cases where overhead justified: healthcare, finance, regulated data.

### SVC-02-Q17
**How are you implementing Byzantine-robust federated learning with encrypted gradient verification, enabling multi-agent AI training without trusting individual agents or exposing plaintext gradients?**

*Reasoning:* Byzantine-robust FL tolerates up to 1/3 malicious participants. Encrypted gradients prevent gradient-based inference attacks. Requires distributed cryptographic protocols.

### SVC-02-Q18
**Do you have secure multi-party computation (MPC) protocols for joint AI model inference across multiple organizations without exposing model parameters or input data to any single participant?**

*Reasoning:* MPC enables collaboration across organizational boundaries. Complex threat model where no participant trusts others. Requires advanced cryptographic protocols.

### SVC-02-Q19
**What is your cryptographic strategy for encrypted aggregation in distributed AI systems—can you prove that gradients were encrypted with approved key material before aggregation without decrypting intermediate values?**

*Reasoning:* Parameter server in federated learning is trusted party. Encrypted aggregation eliminates this trust requirement. Requires cryptographic proofs of encryption.

### SVC-02-Q20
**How will you balance the computational overhead of homomorphic encryption and secure MPC with real-time AI inference requirements, particularly for time-sensitive agentic decision-making?**

*Reasoning:* Homomorphic encryption has extreme overhead. Agentic decisions may need <100ms latency. Performance budget often incompatible with strong privacy guarantees.

---

## SECTION 5: SIDE-CHANNEL & PHYSICAL ATTACK PROTECTION

**Theme:** Protecting cryptographic operations from side-channel attacks (cache, timing, power analysis)

### SVC-02-Q21
**Have you conducted cache-based side-channel analysis of your cryptographic implementations to verify they are resistant to Prime+Probe attacks that could extract encryption keys from shared cloud infrastructure?**

*Reasoning:* Shared cloud infrastructure (AWS, Google Cloud) have exploitable cache side-channels. Prime+Probe can extract RSA keys in <15 minutes. Constant-time crypto + cache isolation required.

### SVC-02-Q22
**How are you mitigating timing-side-channel attacks on AI inference endpoints, where inter-token latency, attention pattern timing, or embedding computation time could leak model structure or confidential inputs?**

*Reasoning:* Transformer models have variable latency based on input. Timing patterns leak information about inputs or model behavior. Requires constant-time implementations or latency randomization.

### SVC-02-Q23
**Do you require constant-time implementations for all cryptographic operations protecting AI workloads, verified through automated audits and quarterly third-party cryptanalysis?**

*Reasoning:* Constant-time crypto prevents timing leaks. Requires careful implementation, compiler flags, and verification. Automated audits + third-party validation essential.

### SVC-02-Q24
**Are you using Intel SGX, ARM TrustZone, or other Trusted Execution Environments (TEEs) to isolate AI inference computations and cryptographic operations from potential microarchitectural side-channel leakage?**

*Reasoning:* TEEs provide hardware isolation. 6-12 month deployment lag behind updates (critical for HSM-like devices). Complex threat model (TEE side-channels exist).

### SVC-02-Q25
**What is your strategy for protecting HSM operations from differential power analysis and other physical side-channel attacks while maintaining microsecond latency requirements for AI agent key access?**

*Reasoning:* HSMs are physical attack targets. Differential power analysis can extract keys. Latency requirement (<1ms for agent operations) constrains defensive measures.

---

## SECTION 6: KEY MANAGEMENT LIFECYCLE AUTOMATION

**Theme:** Automated provisioning, rotation, and revocation of cryptographic key material at agentic scale

### SVC-02-Q26
**Do you have a centralized Key Management System (KMS) capable of automated key rotation for service identity certificates at sub-hour latency, enabling rapid response to compromised AI agent identities?**

*Reasoning:* Agent compromise requires immediate credential revocation. Sub-hour rotation targets aggressive but necessary for agent-to-agent trust chains.

### SVC-02-Q27
**What is your key rotation frequency for different material types—are you rotating AI service account credentials every 24 hours, TLS certificates every 30 days, and symmetric encryption keys every 90 days as baseline targets?**

*Reasoning:* Different key types have different compromise impacts and rotation costs. Baseline frequencies calibrated to threat models. Targets should be event-driven (compromise detected) + calendar-driven (baseline).

### SVC-02-Q28
**How are you managing the key lifecycle for ephemeral agent credentials in agentic environments—can you issue, distribute, and retire cryptographic material for short-lived agent tasks within seconds?**

*Reasoning:* Agents may run for hours or minutes. Ephemeral credentials should have lifetime matching task duration. Second-scale provisioning required for elastic scaling.

### SVC-02-Q29
**Do you have automated dual-key validation mechanisms during cryptographic key rotation, where both old and new keys are accepted for 7+ days to ensure zero service disruption?**

*Reasoning:* Synchronous key rotation causes service disruption if clients/servers out of sync. Dual-key acceptance enables graceful transition.

### SVC-02-Q30
**Can your KMS infrastructure support distributed key material where agents hold short-lived ephemeral keys derived from master keys, preventing single points of key compromise?**

*Reasoning:* Distributed key derivation prevents key theft from single point. Master key holds higher security; derived keys lower. Enables tiered key management.

---

## SECTION 7: AI AGENT ORCHESTRATION & CRYPTOGRAPHIC IDENTITY

**Theme:** Automated provisioning of cryptographic identities for agents and enforcing encryption requirements at runtime

### SVC-02-Q31
**Do you have automated provisioning that creates cryptographic identities for new AI agents, binds them to specific resource quotas, and enforces encryption requirements without manual configuration?**

*Reasoning:* Agent spawning is rapid (potentially 100s/sec in elastic clusters). Manual provisioning infeasible. Automated identity binding to resource quotas enables least-privilege.

### SVC-02-Q32
**Can your agent orchestration platform verify that all inter-agent communication is encrypted before allowing agents to execute tasks, failing fast if encryption requirements are violated?**

*Reasoning:* Encryption enforcement as a platform primitive prevents misconfigured plaintext communication. Fail-fast prevents security degradation.

### SVC-02-Q33
**How are you implementing cryptographic attestation for agent code—can agents prove they were launched with code signed by approved developers and have not been tampered with?**

*Reasoning:* Code attestation prevents unauthorized agent modifications. Enables trust in agent decision-making based on verified code provenance.

### SVC-02-Q34
**Do you have mechanisms to prevent agent key material from leaking into logs, error messages, or side-channel observable outputs?**

*Reasoning:* Agents in untrusted environments. Logs can be exfiltrated. Key material must not appear in plaintext anywhere in execution environment.

### SVC-02-Q35
**Can your infrastructure enforce that agents never have simultaneous access to both encryption keys and plaintext data for the same asset, creating a separation of duties?**

*Reasoning:* Separation of duties is security principle. Keys + plaintext together = exposure risk. Enforcement at infrastructure level prevents agent from becoming single point of failure.

---

## SECTION 8: REGULATORY COMPLIANCE, THREAT MODELING & ORGANIZATIONAL READINESS

**Theme:** Meeting regulatory deadlines, modeling threat scenarios, and organizational preparation for post-quantum migration

### SVC-02-Q36
**What is your organization's timeline for meeting post-quantum cryptography requirements under upcoming regulations (FedRAMP modernization deadline 2027, DORA financial services 2025, NSA commercial crypto migration 2026)?**

*Reasoning:* Regulatory deadlines creating hard constraints. Multiple frameworks have different timelines. Organizations need coordinated compliance planning.

### SVC-02-Q37
**Based on your industry, data sensitivity, and customer commitments, what is the maximum acceptable window between a quantum computer achieving cryptanalytic capability (2030-2035) and your organization's ability to respond with re-encryption of historically encrypted AI models?**

*Reasoning:* Organizations with 20+ year data retention have HNDL risk. Recovery capability (re-encryption infrastructure) affects maximum acceptable window. Different for every organization.

### SVC-02-Q38
**What percentage of your current encrypted traffic contains AI model data that would retain confidentiality value >20 years from encryption date—for this data, what is your organization's harvest-now-decrypt-later risk tolerance?**

*Reasoning:* Some data is ephemeral (login tokens, temporary sessions). Other data is long-lived (proprietary models, training datasets). Risk tolerance varies by data type.

### SVC-02-Q39
**Do you have an executive-level owner for cryptographic strategy and post-quantum readiness, or is encryption responsibility scattered across security, infrastructure, and AI teams?**

*Reasoning:* Post-quantum migration is multi-year, expensive, cross-functional effort. Executive ownership ensures coordination and budget allocation.

### SVC-02-Q40
**Have you conducted a comprehensive cryptographic audit to identify all encryption algorithms in use across AI infrastructure, their threat timelines, and required migration paths?**

*Reasoning:* Cryptographic inventory is prerequisite for migration planning. Shadow IT and legacy systems often overlooked. Comprehensive audit required to identify all targets.

---

## METADATA
