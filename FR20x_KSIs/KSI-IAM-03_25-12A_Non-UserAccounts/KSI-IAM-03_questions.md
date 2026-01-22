# Non-Human Identity Management in the Agentic AI Era: Discovery Questions

**KSI Focus:** IAM-03 - Enforce appropriately secure authentication and authorization for non-human identities (service accounts, API keys, AI agents, machine identities) with emphasis on dynamic, task-scoped permissions; automated credential lifecycle management; zero standing privilege; and secure agent-to-agent delegation preventing lateral movement and privilege escalation in multi-agent systems.

---

## Section 1: AI Agent Identity & Authentication Paradigm Shift

**KSI-IAM-03-Q1:** What evidence demonstrates your organization's recognition that AI agents require fundamentally different authentication models than traditional service accounts? Describe: (a) current NHI inventory (total count, types), (b) current machine-to-human ratio and trajectory (toward 2,000:1 by 2026), (c) your organization's AI agent adoption status, (d) gap analysis between legacy IAM and agentic requirements (dynamic, task-scoped, time-limited), (e) investment plan for AI-native NHI platform.

**KSI-IAM-03-Q2:** How do you distinguish between human user identity and AI agent identity in your authentication infrastructure? Document: (a) agent identity model (unique cryptographic identity per instance vs shared credentials), (b) agent identity lifecycle (provisioning, operation, deprovisioning), (c) agent metadata captured (name, version, task, owner, location), (d) agent revocation triggers (task completion, update, incident), (e) audit trail distinguishing agent vs user authentication events.

**KSI-IAM-03-Q3:** What infrastructure capacity planning exists for managing the projected explosion of AI agents by 2027? Provide: (a) current agent count in production, (b) growth rate, (c) projected infrastructure needs to support 2,000:1 NHI ratio, (d) automation strategy (% manual vs automated credential provisioning).

**KSI-IAM-03-Q4:** How do you prevent AI agents from developing hidden credentials or operating outside official authentication channels? Describe: (a) credential discovery mechanisms, (b) shadow agent detection, (c) audit frequency, (d) remediation procedures, (e) percentage of authorized vs shadow agents discovered in past 12 months.

**KSI-IAM-03-Q5:** What authentication and authorization attestation mechanisms exist for agent authenticity? Explain: (a) agent authentication approach (attestation of identity), (c) runtime verification (is agent running expected code?), (e) revocation if attestation fails.
[Note: Supply chain verification (b), SBOM/build pipeline integration (d) moved to 3IR/secure SDLC KSI]

**KSI-IAM-03-Q6:** How do you handle agent identity recovery or replacement without exposing credentials? Document: (a) procedures for replacing compromised agent, (b) transition period and credential overlap, (c) audit trail of agent replacement, (d) prevention of old credential reuse, (e) testing of recovery procedures.

---

## Section 2: Secure Credential Delegation & Token-Based Authentication

**KSI-IAM-03-Q7:** What is your organization's workload identity federation strategy using OIDC for AI agents? Document: (a) OIDC provider deployment, (b) trust configuration, (c) audience restriction, (d) integration with agent deployment, (e) adoption percentage (% agents using OIDC vs long-lived API keys).

**KSI-IAM-03-Q8:** How do you enforce short-lived token lifetimes for AI agents and what is your justification for chosen TTLs? Provide: (a) token lifetime policy by agent type, (b) example TTLs, (c) research basis showing how token lifetime reduces attack surface, (d) token refresh and rotation procedures, (e) comparison to long-lived API keys (lateral movement window reduction from months to minutes).

**KSI-IAM-03-Q9:** What automated credential rotation mechanisms eliminate manual secret management for AI agents? Describe: (a) rotation triggers, (b) rotation frequency and policy, (c) seamless rotation procedure, (d) verification that rotation completes successfully, (e) audit logs documenting all rotation events.

**KSI-IAM-03-Q10:** How do you implement just-in-time (JIT) credential issuance for task-scoped access? Explain: (a) JIT request flow, (b) supported scenarios, (c) automatic revocation upon task completion, (d) audit trail of JIT credentials, (e) percentage of agent access using JIT vs pre-provisioned.

**KSI-IAM-03-Q11:** What scope enforcement mechanisms prevent delegation tokens from granting permissions beyond delegation boundaries? Document: (a) scope attenuation in delegation chains (parent cannot grant child more than parent has), (b) API-level enforcement, (c) testing of scope enforcement, (d) evidence of scope escalation prevention, (e) continuous validation throughout delegation chain.

**KSI-IAM-03-Q12:** How do you handle agent-to-agent communication authentication and prevent impersonation or replay attacks? Provide: (a) agent-to-agent authentication mechanism, (b) identity verification of called agent, (c) replay attack prevention, (d) audit logging of inter-agent calls, (e) examples of multi-agent workflows tested for security.

---

## Section 3: Minimal Agent Authorization Scope Enforcement

**KSI-IAM-03-Q13:** How do you enforce authorization scope and lineage to prevent sub-agents from exceeding parent agent authorization? Explain: (a) sub-agent creation authorization, (b) scope verification (sub-agent has narrower scope than parent), (c) audit trail of agent lineage, (d) delegation depth limits preventing unbounded escalation, (e) testing preventing sub-agent privilege escalation.
[Note: Behavioral anomaly detection, concept drift ML, and general behavioral compromise detection moved to monitoring KSIs; only authorization scope enforcement retained]

---

## Section 4: Agent Audit Trail & Authorization Decisions

**KSI-IAM-03-Q14:** What immutable audit logging exists for AI agent authentication and authorization decisions? Describe: (a) events logged (agent authentication, permission grant, access decision, token issuance, delegation), (b) audit trail completeness (can any permission decision be explained?), (c) immutability and protection from tampering, (d) searchability by agent, action, time, (e) retention period and compliance requirements.

**KSI-IAM-03-Q15:** How do you track agent delegation chains and enable forensic reconstruction of authorization decisions? Document: (a) delegation chain depth tracking, (b) provenance capture (Agent A delegated to B by user at time with scope), (c) lineage visualization, (d) impact analysis (if agent compromised, which downstream agents affected?), (e) historical reconstruction of authorization decisions for past incidents.
[Note: Observability gaps/latency (Q21), multi-cloud visibility (Q23), SIEM integration (Q24) moved to KSI-CMT-01; only delegation chain forensics retained]

---

## Section 5: Agent Lifecycle & Credential Cleanup

**KSI-IAM-03-Q16:** What agent lifecycle management procedures ensure automatic cleanup of credentials when agents terminate? Explain: (a) agent termination procedures, (b) credential revocation upon termination, (c) cleanup verification (credentials definitively unavailable), (d) zombie agent prevention, (e) audit trail of agent lifecycle events.

**KSI-IAM-03-Q17:** What governance framework enables agents to delegate permissions to sub-agents while maintaining security boundaries? Document: (a) delegation policy definition (who can delegate, to whom, with what scope?), (b) scope constraint enforcement, (c) delegation depth limits, (d) explicit delegation logging, (e) revocation capability at any level.

**KSI-IAM-03-Q18:** How do you maintain audit trail and provenance for multi-agent workflows spanning multiple agents? Describe: (a) request tracing across agent boundaries, (b) decision lineage, (c) distributed tracing implementation, (d) audit completeness, (e) forensic reconstruction capability.

---

## Section 6: Zero Standing Privilege (NHI-Specific)

**KSI-IAM-03-Q19:** How do you enforce zero standing privilege for all NHI, eliminating permanent privileged access? Provide: (a) standing privilege definition in your context, (b) JIT access mechanism (credentials issued on-demand, auto-revoked post-task), (c) maximum permission duration enforced, (d) exceptions and justification, (e) measurement of zero standing privilege achievement (% agents operating under ZSP).
[Note: Broader zero trust architectural questions (Q31, Q32, Q34, Q35), continuous authorization model, context-aware access control moved to KSI-IAM-05; only NHI-specific JIT/ZSP retained]

---

## Section 7: Agent-to-Agent Multi-Agent Security

**KSI-IAM-03-Q20:** What multi-agent orchestration security mechanisms ensure authentication and authorization for inter-agent communication? Provide: (a) inter-agent communication security (authentication, authorization, audit), (b) shared resource access coordination, (c) audit logging of inter-agent interactions, (d) examples of multi-agent workflows tested for security, (e) documented incidents and response.
[Note: Deadlock/cascade failure behavior (part of Q39) moved to reliability/operations KSIs; only authentication/authorization parts retained]

