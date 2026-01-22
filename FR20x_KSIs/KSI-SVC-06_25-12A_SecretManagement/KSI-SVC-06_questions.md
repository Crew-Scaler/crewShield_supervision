# AI-Driven Secret Management: Discovery Questions

**KSI-SVC-06** - Automated Key Lifecycle and Cryptographic Identity for AI Agents

**Research Foundation:** 119 papers synthesized across 6 research clusters addressing ephemeral workload identity, cryptographic lifecycle and agility, transport security with real-time revocation, multi-cloud key federation, supply chain security, and incident response with break-glass automation.

**Question Set Version:** 1.0
**Generated:** 2026-01-08

---

## SECTION 1: EPHEMERAL AGENT IDENTITY AND WORKLOAD FEDERATION (Q01-Q05)

**SVC-06-Q01:** How does your organization architect workload identity for AI agents using SPIFFE/SPIRE frameworks, and what mechanisms ensure agents obtain X.509 certificates (SVIDs) at runtime without embedding secrets in code, images, or configuration files?

**SVC-06-Q02:** When millions of AI agents spawn, authenticate, execute work, and terminate autonomously within minutes, what automated identity provisioning infrastructure issues short-lived certificates (hours to days) and enables instant revocation upon compromise detection?

**SVC-06-Q03:** What runtime attestation mechanisms validate AI agent legitimacy before issuing identity credentials—verifying container image hashes, Kubernetes service accounts, or cloud instance credentials—across multi-cloud deployments (AWS, Azure, GCP)?

**SVC-06-Q04:** How does your organization prevent cascading compromise when a single agent (A) is compromised and previously communicated with downstream agents (B→C→D), ensuring agent-to-agent (A2A) mutual TLS with real-time certificate revocation checking?

**SVC-06-Q05:** When Kubernetes native integration is essential for agentic AI deployment, what specific controls ensure agents access cryptographic identities through native integration with Kubernetes service accounts, admission controllers, and RBAC policies without storing credentials persistently?

---

## SECTION 2: AUTOMATED KEY LIFECYCLE AND CRYPTOGRAPHIC WEAR-OUT (Q06-Q10)

**SVC-06-Q06:** At cloud scale (500+ Gbps encryption throughput), AES-GCM symmetric keys reach operational limits (2^32 messages) every 91 minutes—making traditional annual key rotation cycles catastrophically inadequate. How does your organization implement automated key rotation triggered by operational metrics rather than time-based schedules?

**SVC-06-Q07:** What cryptographic key derivation strategies (HKDF, nonce diversification) extend AES-GCM operational limits while managing the computational overhead of continuous key rotation at agentic scale (millions of encryption operations per second)?

**SVC-06-Q08:** How does your organization prevent nonce collision attacks when symmetric key operation rates exceed theoretical nonce space during high-volume agent activity, and what monitoring validates cryptographic wear-out hasn't resulted in key material reuse?

**SVC-06-Q09:** When public certificate lifespans have shortened from 398 days (2020) to 47 days (2024), what fully automated renewal mechanisms ensure certificates are renewed 14+ days before expiration without human intervention or service interruptions?

**SVC-06-Q10:** What automation prevents certificate expiration failures in agentic systems where 2-5% failure rates in production cause cascading service outages, and how are renewal success/failure metrics tracked with alerting for near-expiration events?

---

## SECTION 3: CRYPTOGRAPHIC AGILITY AND POST-QUANTUM MIGRATION (Q11-Q15)

**SVC-06-Q11:** Given that quantum computers are estimated 2030-2035 maturity and organizations harvesting encrypted data today will face decryption threats in 5-10 years, what post-quantum cryptography migration strategy transitions from RSA/ECDSA to NIST-standardized algorithms (ML-DSA, ML-KEM)?

**SVC-06-Q12:** How does your organization maintain cryptographic strength when adversaries may possess quantum decryption capabilities before post-quantum migration completes, and what "harvest-now-decrypt-later" threat modeling informs urgency of algorithm transition timelines?

**SVC-06-Q13:** Rather than flag-day algorithm replacement, how does your organization deploy hybrid certificates supporting both classical (P-256 ECDH) and post-quantum (ML-KEM) algorithms simultaneously, enabling gradual migration while maintaining backward compatibility?

**SVC-06-Q14:** When regulatory deadlines (DORA Jan 2025, PCI DSS 4.0.1 Mar 2025, FedRAMP 2026) mandate post-quantum readiness or crypto-agility demonstration, what governance framework ensures organization begins PQC testing by Q1 2025 and completes migration by 2027?

**SVC-06-Q15:** What policy enforcement mechanisms ensure multiple key versions coexist simultaneously in production—old keys for decryption of legacy data, new keys for encryption of current data—while tracking version-to-version algorithmic transitions and deprecation timelines?

---

## SECTION 4: ZERO-TRUST AGENT COMMUNICATION AND REAL-TIME REVOCATION (Q16-Q20)

**SVC-06-Q16:** How does your organization validate certificate legitimacy during agent-to-agent calls synchronously—requiring real-time revocation status checks (OCSP responses <30 seconds old) rather than cached CRLs updated daily—preventing use of recently-revoked credentials?

**SVC-06-Q17:** When compromised agent credentials must be revoked instantly to prevent lateral movement across infrastructure, what OCSP stapling mechanisms enable servers to provide proof of non-revocation with TLS handshakes, reducing latency of revocation checks on every A2A call?

**SVC-06-Q18:** What certificate transparency log monitoring detects fraudulent certificates issued through KMS compromise, and how are Rekor/Sigstore transparency logs monitored to identify suspicious signing events outside normal key issuance patterns?

**SVC-06-Q19:** For multi-agent systems requiring zero-trust A2A communication with certificate revocation checking at each hop, what performance optimizations prevent revocation checking from becoming a bottleneck that exceeds acceptable A2A request latency (<100ms)?

**SVC-06-Q20:** How does your organization distinguish between legitimate agent certificate renewal cycles (high frequency at agentic scale) and potential compromise indicators (abnormal revocation requests, revocation of unexpired certificates), using behavioral baselines to detect attacks?

---

## SECTION 5: MULTI-CLOUD KEY GOVERNANCE AND FEDERATION (Q21-Q25)

**SVC-06-Q21:** When organizations deploy agents across AWS, Azure, Google Cloud, and on-premises simultaneously, how does centralized KMS governance enforce consistent key rotation schedules, wear-out monitoring, and algorithm preferences across clouds with different APIs and deletion recovery semantics?

**SVC-06-Q22:** What BYOK (Bring-Your-Own-Key) patterns maintain master keys in on-premises HSM or dedicated HSM clusters while securely replicating keys to each cloud provider, enabling data encryption within each provider while retaining control and preventing cloud provider key access?

**SVC-06-Q23:** How does multi-party computation (MPC) key splitting across cloud providers prevent any single provider from accessing complete key material, requiring cooperation for cryptographic operations and ensuring attackers cannot extract keys via single-provider compromise?

**SVC-06-Q24:** When cloud providers offer different semantics (AWS automatic key rotation 90-day minimum, Azure key versioning, Google Cloud rotation intervals), what abstraction layers normalize these differences while preventing policy enforcement gaps that compromise key management consistency?

**SVC-06-Q25:** For envelope key hierarchies where root keys remain on-premises and per-cloud data encryption keys (DEKs) are wrapped with root keys, how does your organization prevent cloud providers from accessing wrapped DEKs and ensure compliance with data residency/sovereignty requirements?

---

## SECTION 6: ML-BASED ANOMALY DETECTION AND BEHAVIORAL SECURITY (Q26-Q30)

**SVC-06-Q26:** When rule-based access control achieves only 60% accuracy in detecting unauthorized secret access, how does ML-based anomaly detection with behavioral baselines achieve >95% accuracy in identifying subtle access pattern anomalies that indicate compromise?

**SVC-06-Q27:** What mechanisms establish "normal" behavioral baselines for agent secret access patterns when agents operate continuously with varying credential requests, and how does the system distinguish between legitimate variability and anomalous access that precedes credential exfiltration?

**SVC-06-Q28:** For detecting credential compromise at agentic velocity (detection delays of 2-4 weeks are unacceptable), what real-time monitoring achieves <5 minute detection of unauthorized access, anomalous rotation patterns, or credential usage from unexpected network locations/services?

**SVC-06-Q29:** How does your organization prevent concept drift in anomaly detection models themselves—where model accuracy silently degrades as legitimate access patterns evolve over time—requiring continuous model retraining and validation?

**SVC-06-Q30:** When detecting token replay attacks that are common without DPoP (Demonstration of Proof-of-Possession), what cryptographic binding mechanisms link tokens to specific clients or proof-of-possession keys to prevent attackers from using stolen tokens?

---

## SECTION 7: SUPPLY CHAIN SECURITY FOR KEY MANAGEMENT INFRASTRUCTURE (Q31-Q35)

**SVC-06-Q31:** How does your organization prevent compromised CI/CD pipelines from obtaining overly-permissive KMS access tokens that enable master key export, unlimited data decryption, or fraudulent certificate issuance undetectable without Certificate Transparency log monitoring?

**SVC-06-Q32:** What least-privilege access controls ensure CI/CD systems obtain time-bounded, narrowly-scoped KMS tokens sufficient for their specific pipeline tasks (sign artifacts, encrypt secrets) while preventing broad key rotation, deletion, or encryption operations?

**SVC-06-Q33:** For detecting KMS access anomalies that precede supply chain attacks, what behavioral monitoring identifies unusual access patterns—access from unexpected CI/CD systems, offline KMS operations, or key rotation outside normal schedules—with <10 second detection latency?

**SVC-06-Q34:** When SBOM integrity is critical to preventing supply chain attacks through KMS, how are SBOMs for KMS infrastructure (dependencies, plugins, extensions) cryptographically verified, and what mechanisms detect tampering of key management software itself?

**SVC-06-Q35:** How does your organization audit and verify that code signing infrastructure (used to sign KMS updates or agent deployment artifacts) hasn't been compromised to issue fraudulent signatures that could inject malicious KMS behavior into production?

---

## SECTION 8: INCIDENT RESPONSE, BREAK-GLASS AUTOMATION, AND COMPLIANCE (Q36-Q40)

**SVC-06-Q36:** When agent compromise is detected, what pre-authorized break-glass procedures enable instant credential rotation without waiting for manual approval chains, allowing 15-minute response times instead of 8+ hour remediation windows?

**SVC-06-Q37:** How does emergency credential provisioning leverage ephemeral identity infrastructure (SPIFFE/SPIRE) to rapidly issue temporary credentials to isolated agents during incident response, enabling temporary access to required systems while maintaining audit trails?

**SVC-06-Q38:** What governance framework determines whether HSM or TEE (Trusted Execution Environment) failures invalidate key storage assumptions, triggering emergency key rotation or degraded-mode operation, and how frequently are HSM/TPM failures monitored in production?

**SVC-06-Q39:** For regulatory compliance with DORA (Jan 2025), PCI DSS 4.0.1 (Mar 2025), and FedRAMP (2026) requirements, what automated compliance evidence demonstrates key rotation, revocation, and post-quantum readiness without manual audit processes?

**SVC-06-Q40:** When audit trails of every KMS access must be cryptographically verifiable and immutable for forensic investigation of agent compromise, what mechanisms prevent unauthorized deletion or modification of KMS access logs, and how are logs encrypted and archived securely?

---

## RESEARCH CLUSTERS SUPPORTING THESE QUESTIONS

**Cluster 1:** Ephemeral Agent Identity and Workload Federation (10 papers) - SPIFFE/SPIRE, workload attestation, certificate issuance automation

**Cluster 2:** Cryptographic Lifecycle and Agility at Machine Scale (30 papers) - AES-GCM wear-out, certificate shortening, post-quantum migration

**Cluster 3:** Transport Security and Certificate Revocation in Distributed Architectures (10 papers) - mTLS, OCSP, real-time revocation, service mesh

**Cluster 4:** Multi-Cloud Key Federation and Centralized Governance (10 papers) - BYOK/BYOKMS, MPC key splitting, policy enforcement

**Cluster 5:** Supply Chain Security and Continuous Verification (10 papers) - CI/CD KMS security, SBOM integrity, code signing

**Cluster 6:** Security Incident Response and Emergency Credentials (39 papers) - Break-glass automation, compromise detection, HSM/TEE hardening

---

**Document Purpose:** Enable organizations to comprehensively evaluate AI agent secret management and automated key lifecycle capabilities with exclusive focus on ephemeral identity, cryptographic agility, real-time revocation, and operational resilience.
