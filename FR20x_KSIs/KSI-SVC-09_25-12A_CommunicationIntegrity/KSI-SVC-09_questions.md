# KSI-SVC-09: Communication Integrity - Discovery Questions

**KSI Statement**: Persistently validate the authenticity and integrity of communications between machine-based information resources using automation.

**Framework Alignment**: FedRAMP 20x, NIST SP 800-53 (SC-23, SC-7, SC-8), ISO 27001 (A.10.1)

**Document Date**: January 13, 2026

**Processing Summary**:
- Original Question Count: 42
- Questions Consolidated/Removed: 8 (Q011, Q013, Q020, Q034, Q037, Q038, Q039, Q040 moved to other KSIs or merged)
- Questions Kept and Refined: 30
- Questions After Consolidation: 30
- Revisions: Removed perspective distinctions (CIO/Customer/Auditor), made all questions neutral, updated IDs to KSI-SVC-09-Q{number}

---

## Identity and Authentication at Scale

**KSI-SVC-09-Q001**: How does the organization plan to provision and revoke cryptographic identities for potentially millions of ephemeral AI agent instances at sub-second latencies? What is the current certificate lifecycle overhead, and what automation investments are required to achieve instant provisioning?

**KSI-SVC-09-Q002**: What cryptographic identity framework is being implemented—SPIFFE/SPIRE, Decentralized Identifiers (DIDs), or alternative mechanisms? How do these frameworks integrate with existing workload identity systems and service meshes?

**KSI-SVC-09-Q003**: How does the organization validate AI agent authenticity across heterogeneous agent populations from multiple vendors? What "Know Your Agent" (KYA) trust chain mechanisms exist, and how are delegation chains from human users through agent hierarchies cryptographically bound?

**KSI-SVC-09-Q004**: What are the organization's certificate revocation propagation timelines, and how is it ensured that compromised AI agent instances lose access instantly across all distributed systems? What monitoring exists for revocation list staleness?

**KSI-SVC-09-Q005**: How does the organization manage token lifecycle and rotation for autonomous AI agents that operate continuously without human intervention? What mechanisms prevent token theft or replay in long-running agent sessions?

## Hallucination and Parameter Validation

**KSI-SVC-09-Q006**: What semantic parameter validation mechanisms are deployed to distinguish hallucinated API parameters from intentional invocations? How are invented resource identifiers detected without false positives that disrupt legitimate agent operations?

**KSI-SVC-09-Q007**: Are human-in-the-loop (HITL) workflows implemented for sensitive operations (delete, transfer funds, access changes)? How is security assurance balanced with agent autonomy and response latency requirements?

**KSI-SVC-09-Q008**: How does the organization validate type checking and range validation for AI-generated function parameters? What mechanisms detect SQL injection, command injection, and path traversal attempts in agent-generated payloads?

**KSI-SVC-09-Q009**: What scope verification mechanisms ensure that AI agents only invoke functions within their delegated authority limits? How is privilege escalation through chained tool calls prevented?

## Multi-Agent and Inter-Agent Communication

**KSI-SVC-09-Q010**: What agent-to-agent communication protocols (Agent2Agent, Agent Communication Protocol, Model Context Protocol, CORAL) are deployed in the environment? How are these protocols secured against session smuggling, impersonation, and message injection attacks?

**KSI-SVC-09-Q011**: How does the organization establish trust between AI agents from different vendors or organizations in federated multi-agent systems? What trust scoring or reputation mechanisms dynamically adjust agent privileges?

**KSI-SVC-09-Q012**: What cross-agent consensus mechanisms prevent Byzantine agents from poisoning multi-agent coordination? How is consensus latency balanced with Byzantine fault tolerance guarantees? Can the platform detect and isolate Byzantine agents providing conflicting information in multi-agent coordination scenarios?

## Mutual TLS and Channel Authentication

**KSI-SVC-09-Q013**: What mutual TLS (mTLS) implementation exists across the cloud infrastructure? Which service mesh technology (Istio, Linkerd, Consul) manages automatic certificate provisioning, rotation, and revocation at scale? What is the certificate rotation frequency, and how is compliance with maximum certificate lifetime requirements (recommended 1-24 hours) monitored?

**KSI-SVC-09-Q014**: What evidence demonstrates that mutual authentication occurs before any service communication? Are all certificate issuance, renewal, and revocation events recorded with timestamps and available for audit access?

**KSI-SVC-09-Q015**: What evidence demonstrates that Perfect Forward Secrecy is enabled for all agent communication channels? How is it ensured that compromise of long-term keys does not expose historical agent communications?

## Per-Message Signing and Event-Scale Validation

**KSI-SVC-09-Q016**: Can the platform demonstrate per-message signing capabilities for event-driven agent communication? What publisher authentication and consumer validation mechanisms ensure only authorized agents publish to message topics and verify signatures before processing? What is the organization's capacity for cryptographic validation at event scale, and can throughput benchmarks for per-message signing in high-velocity message buses (Kafka, Pulsar) supporting millions of agent communications per second be demonstrated?

**KSI-SVC-09-Q017**: What replay attack prevention mechanisms exist for event-driven agent communication? How are cryptographic nonces, timestamps, and sequence numbers used to prevent duplicate message processing?

**KSI-SVC-09-Q018**: How does the platform validate event ordering dependencies in agent workflows? What mechanisms prevent sequence manipulation attacks that exploit temporal assumptions in multi-step agent processes?

## Cross-Infrastructure Communication

**KSI-SVC-09-Q019**: How does the service mesh handle inter-service communication for AI agents deployed across multiple cloud providers or hybrid environments? What mechanisms ensure consistent cryptographic validation across heterogeneous infrastructure?

**KSI-SVC-09-Q020**: How does communication validation integrate with behavioral anomaly detection and distributed tracing? What observability platforms (Jaeger, Zipkin, Prometheus, Grafana) monitor communication patterns and detect deviations from baseline behavior?

## AI Agent Communication Protection

**KSI-SVC-09-Q021**: What specific protections exist against AI hallucination attacks exploiting Broken Object Level Authorization (BOLA) and Broken Function Level Authorization (BFLA) vulnerabilities? How does the platform prevent agents from invoking functions outside delegated authority?

**KSI-SVC-09-Q022**: How does the platform address indirect prompt injection risks from RAG data poisoning, malicious document injection, email threats, and compromised API responses? What data source integrity validation mechanisms prevent malicious instructions from reaching agent processes?

**KSI-SVC-09-Q023**: What mechanisms protect vector database communications between AI agents and embedding/retrieval systems? How are vector search queries and results validated for authenticity and integrity?

**KSI-SVC-09-Q024**: How does the platform secure communication channels for federated learning where multiple agents contribute to model training? What cryptographic mechanisms prevent malicious gradient updates or model poisoning through communication channels?

**KSI-SVC-09-Q025**: What dead letter queue mechanisms isolate suspicious or malformed messages from agent communication streams? How are quarantined messages analyzed forensically, and what triggers message rejection or agent isolation?

## Event and Topic Access Controls

**KSI-SVC-09-Q026**: What topic-level access controls restrict agent publication and subscription to authorized message channels? How is authorization validated at both publish-time and consume-time for event streams?

## Cryptographic and Semantic Validation

**KSI-SVC-09-Q027**: For all AI-generated API calls and tool invocations, are semantic parameter validation mechanisms in place before execution? What controls prevent agents from invoking functions with hallucinated or unauthorized parameters, and how are failed validations logged?

**KSI-SVC-09-Q028**: Are cryptographic signatures (HMAC or asymmetric) applied to all inter-agent messages in event-driven architectures?

## Compliance and Continuous Validation

**KSI-SVC-09-Q029**: How does the communication integrity implementation address FedRAMP 20x continuous automated validation philosophy? Can persistent validation mechanisms for all inter-service communications be demonstrated, rather than manual, point-in-time checks?

**KSI-SVC-09-Q030**: What audit logging exists for all agent communication authentication, authorization, and integrity validation decisions? How are logs protected from tampering, and what retention periods support regulatory investigations?

## Incident Response and Forensics

**KSI-SVC-09-Q031**: Review incident response procedures specific to AI agent communication integrity failures. Verify that forensic capabilities exist to trace compromised communications, identify affected transactions, and reconstruct Byzantine consensus violations in multi-agent systems. What immutable audit logs support regulatory investigations?

**KSI-SVC-09-Q032**: What isolation and quarantine mechanisms exist for AI agents exhibiting suspicious communication patterns? How quickly can compromised agents be removed from production communication channels, and what fallback mechanisms maintain service continuity?

---

## Questions Moved to Other KSIs

The following questions were determined to be better aligned with other KSIs and have been moved or consolidated:

**Moved to KSI-AIM-02 (Model Drift and Runtime Monitoring):**
- Original Q012: Model drift detection integration with communication validation (now part of model lifecycle KSI)

**Moved to KSI-AIM-01 (Data Poisoning and Training Integrity):**
- Original Q013: Training data pipeline integrity and poisoned data detection (now part of data integrity KSI)

**Moved to KSI-TPR-03 (Supply Chain Risk Management):**
- Original Q010: Cryptographic provenance tracking of AI models and SBOM practices
- Original Q037: Supply chain scanning and backdoored model detection
- Original Q038: SBOM documentation and dependency integrity validation
- Original Q040: Model provenance chains and unauthorized model substitution detection

**Moved to Model Integrity/Attestation KSI (to be created or consolidated):**
- Original Q011: Zero-knowledge proofs and model integrity attestation (deep performance details)
- Original Q039: ZK proof implementations and attestation latency benchmarking

**Consolidated into other SVC-09 questions:**
- Original Q020: Event-scale cryptographic validation capacity (merged into Q016)
- Original Q034: Certificate audit logs (merged into Q014)

---

## Implementation Roadmap

### Quick Wins (0-3 months)
- Inventory existing cryptographic identity implementations
- Audit service mesh mTLS configuration and certificate lifecycle
- Identify high-risk communication patterns (financial transactions, sensitive operations)
- Establish baseline behavioral patterns for agent communications

### Medium-Term (3-9 months)
- Deploy semantic parameter validation for AI-generated API calls
- Implement Byzantine-fault-tolerant consensus for critical multi-agent operations
- Deploy per-message signing for event-driven architectures

### Long-Term (9+ months)
- Full event-scale communication validation with per-message signing
- Comprehensive observability across all cryptographic validation layers

---

## Evaluation Criteria

### Readiness Indicators
- Automated certificate provisioning supporting >1000 certificates/second
- <100ms latency overhead from semantic parameter validation
- <5% false positive rate from anomaly detection systems
- 100% coverage of agent communications by cryptographic validation
- <1 second certificate revocation propagation time

### Risk Indicators
- Manual certificate rotation processes
- Authorization decisions without semantic parameter validation
- Missing audit trails for AI agent communications
- Lack of Byzantine fault tolerance in multi-agent coordination
- No per-message signing in event-driven architectures
- Insufficient isolation mechanisms for compromised agents

---

**Questions Refined**: January 13, 2026
**Related Framework**: FedRAMP 20x, NIST SP 800-53 (SC-23, SC-7, SC-8, SC-13), ISO 27001 (A.10.1)
**Status**: Refined and Ready for Integration with Other KSI Question Files
