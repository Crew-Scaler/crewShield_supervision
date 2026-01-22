# Zero Trust Architecture for AI Agents & Non-Human Identities: Discovery Questions

**KSI Focus:** IAM-05 - Enforce least-privilege access for all users and non-human identities through zero-trust architecture emphasizing continuous verification, workload identity federation (OIDC/SPIFFE), behavioral anomaly detection, real-time policy enforcement, attestation-driven access control, micro-segmentation, and dynamic permission adjustment based on risk posture.

---

## Section 1: Non-Human Identity Visibility & Workload Identity Federation

**IAM-05-Q01:** What evidence demonstrates your organization has complete visibility into non-human identities (NHIs)? Describe: (a) automated NHI discovery mechanism (CIEM tools, API enumeration, secrets scanning), (b) inventory completeness: estimated total NHI count and confidence level, (c) NHI inventory refresh frequency (real-time, daily, weekly), (d) NHI types tracked (service accounts, API keys, agent IDs, workload identities, OAuth clients), (e) reconciliation process verifying inventory vs. actual deployed identities.

**IAM-05-Q02:** What percentage of your workloads use short-lived credentials (OIDC, SPIFFE, STS) vs. long-lived API keys? Document: (a) percentage breakdown by workload type (Kubernetes, serverless, CI/CD, VMs, agents, batch jobs), (b) technical or operational blockers preventing migration for remaining workloads, (c) migration timeline and estimated completion date, (d) short-lived credential lifetime targets and actual (target: 15-min to 1-hour for agents, <24-hour for batch jobs), (e) measurable improvements from OIDC adoption (reduced incident dwell time, faster detection).

**IAM-05-Q03:** How do you implement workload identity federation for AI agents? Explain: (a) federation mechanism (OIDC, SPIFFE, custom token exchange), (b) workload-to-identity-provider binding (how does agent prove its identity?), (c) token lifetime and automatic rotation, (d) audience/scope restrictions (agent only receives credentials for authorized resources), (e) comparison: OIDC lateral movement window (months → minutes, 99.5% reduction).

**IAM-05-Q04:** What evidence demonstrates that short-lived credentials reduce your actual incident impact? Provide: (a) incident analysis showing dwell time for compromised credentials in past 12 months, (b) incidents with long-lived credentials vs. short-lived tokens (comparative impact), (c) examples where automated token expiration prevented extended exploitation, (d) blast radius reduction from quick credential expiration, (e) compliance/audit benefits from short-lived credential evidence.

**IAM-05-Q05:** How do you prevent NHI credential sprawl and orphaned identities? Document: (a) automated detection of undocumented or unused identities, (b) decommissioning process (credentials revocation, deletion, audit), (c) frequency of cleanup (target: quarterly audit of NHIs), (d) metrics on orphaned identity reduction over time, (e) historical incidents attributed to orphaned/forgotten identities.

---

## Section 2: Behavioral Identity & Intent Verification (UEBA 2.0)

**IAM-05-Q06:** How do you detect agent compromise or anomalous behavior in real-time? Describe: (a) behavioral baseline establishment (learning period, feature selection—tool invocations, data access, timing, resource usage), (b) anomaly detection approach (statistical, ML-based, rule-based), (c) MTTD for behavioral anomalies (target: <4 hours vs. industry 14-day dwell time), (d) detection sensitivity (false positive rate on legitimate changes), (e) examples of compromised agents detected via behavioral anomalies.

**IAM-05-Q07:** Can your system detect concept drift indicating agent degradation or compromise? Explain: (a) drift detection methodology and algorithms, (b) drift monitoring frequency (real-time vs. batch analysis), (c) MTTD when agent behavior diverges from baseline, (d) response mechanism to drift (immediate revocation, escalation, reduced permissions), (e) real production examples of drift detection preventing incidents.

**IAM-05-Q08:** What is your approach to agent intent verification? Document: (a) intent definition (what is agent supposed to do with granted permissions?), (b) intent verification at authorization time (human approves purpose), (c) intent validation at execution (actual behavior matches declared intent?), (d) intent mismatch detection and response, (e) examples of intent mismatches caught (agent trying to access resource outside declared purpose).

**IAM-05-Q09:** How do you handle false positives in behavioral anomaly detection? Describe: (a) false positive rate for legitimate behavior vs. detected anomalies, (b) mechanisms distinguishing legitimate changes (model updates, task changes) from attacks, (c) feedback loops improving detection accuracy, (d) alert tuning to reduce alert fatigue, (e) examples of false positives and how they were resolved.

**IAM-05-Q10:** What trust scoring or risk-based approach adjusts permissions based on behavioral assessment? Explain: (a) trust score calculation (factors: identity age, behavior history, privilege usage, anomalies), (b) permission adjustment based on trust score (higher trust = broader access?), (c) dynamic permission reduction if behavior degrades, (d) examples of trust score triggering permission changes, (e) transparency: how is trust score calculated and communicated?

---

## Section 3: Attestation-Driven Access Control

**KSI-IAM-05-Q11:** How do you implement attestation-based access control for AI agents? Describe: (a) attestation evidence collected (code hash, configuration hash, runtime environment), (b) attestation verification before granting access to sensitive resources, (c) continuous attestation during execution (detecting runtime compromise?), (d) attestation latency impact (<50ms target), (e) examples of attestation preventing unauthorized agent access.

_Note: Questions on confidential computing technologies (TEE design, PQC cryptography, side-channel mitigation, credential encryption) moved to Platform Security / 3IR KSI._

---

## Section 4: Micro-Segmentation & Identity-Based Network Policies

**KSI-IAM-05-Q12:** How do you implement micro-segmentation for agent communication? Describe: (a) service mesh deployment (Istio, Linkerd, custom), (b) mTLS enforcement between agents (mutual authentication, encryption), (c) fine-grained network policies (which agents can communicate with which services?), (d) authorization enforcement at network layer (policy engine integration), (e) lateral movement prevention testing.

**KSI-IAM-05-Q13:** What network policies prevent agent-to-agent lateral movement? Document: (a) default-deny network policies (agents can only communicate with explicitly authorized targets), (b) agent identity propagation (network policies based on agent ID, not just IP), (c) egress filtering (outbound connections limited to authorized services), (d) DLP integration at network layer (preventing data exfiltration), (e) testing lateral movement scenarios and containment.

**KSI-IAM-05-Q14:** How do you enforce zero trust at the agent sidecar/proxy level? Document: (a) sidecar architecture for agent identity and policy enforcement, (b) capabilities (credential injection, mTLS, policy evaluation, audit logging), (c) sidecar updates and security patches frequency, (d) sidecar compromise detection and response, (e) performance overhead of sidecar enforcement.

_Note: Questions on multi-cloud network policy synchronization (Q18) and dynamic policy update mechanics (Q19) moved to Supply Chain / Network Security KSI._

---

## Section 5: Context-Aware Access Control

**KSI-IAM-05-Q15:** How do you implement context-aware data access control for agents? Explain: (a) context factors (time of day, user location, data sensitivity, request type), (b) dynamic access adjustments based on context, (c) examples of context-driven denials (agent accessing PII outside business hours), (d) privacy preservation (no tracking of user locations, etc.), (e) compliance (GDPR, CCPA data subject rights).

_Note: Questions on data classification methodology, provenance/lineage tracking, training data poisoning, and DBOMs moved to Data Governance / Privacy / Supply Chain KSIs._

---

## Section 6: Policy-as-Code & Automated Enforcement

**KSI-IAM-05-Q16:** How do you implement policy-as-code for agent authorization? Document: (a) policy language used (OPA, AWS Config, custom DSL), (b) policies defined in code (agent permissions, resource limits, data access), (c) policy version control and change tracking, (d) policy testing before deployment, (e) policy violation detection and escalation.

**KSI-IAM-05-Q17:** What enforcement mechanisms ensure policies are actually applied? Explain: (a) enforcement layers (admission control, API gateway, OS-level), (b) enforcement latency (<100ms target for authorization decisions), (c) failure modes (deny vs. allow if enforcement fails?), (d) audit trail of policy enforcement decisions, (e) continuous compliance validation.

**KSI-IAM-05-Q18:** How do you handle policy conflicts or contradictions? Describe: (a) conflict detection methodology, (b) resolution logic (e.g., most-restrictive wins?), (c) human review for complex conflicts, (d) testing policy combinations for conflicts, (e) examples of conflicts found and resolved.

**KSI-IAM-05-Q19:** What automated remediation does your policy engine support? Document: (a) automated responses to policy violations (tagging, quarantine, termination), (b) human-in-the-loop for high-risk remediations, (c) remediation latency (how quickly is violation corrected?), (d) success rate of automated remediation, (e) examples of automated remediation preventing further violations.

**KSI-IAM-05-Q20:** How do you update policies in response to threats or incidents? Explain: (a) policy update mechanism and approval process, (b) threat-driven policy changes (e.g., CVE published → agent permissions restricted), (c) update latency (time from threat to policy deployment), (d) rollback capability if policy causes issues, (e) testing policy changes before production deployment.

---

## Section 7: Attestation & Continuous Verification

**KSI-IAM-05-Q21:** How do you use attestation to verify agent integrity before granting access? Describe: (a) attestation types (remote attestation via TPM, SEV-SNP, SGX quotes), (b) attestation requirements before access grant, (c) attestation evidence collection and verification, (d) trusted root of trust (hardware-backed or software?), (e) attestation verification latency (<50ms target).

**KSI-IAM-05-Q22:** What continuous attestation mechanism detects agent compromise during execution? Explain: (a) continuous monitoring capability (agent behavior, resource usage, integrity), (b) runtime compromise detection latency (target: <30 seconds), (c) detection methods (behavioral anomalies, integrity checks, system calls), (d) response to detected compromise (immediate revocation), (e) examples of runtime compromises detected.

**KSI-IAM-05-Q23:** How do you prevent attestation spoofing or bypass? Document: (a) attestation binding to physical hardware (prevents virtual machine escape?), (b) freshness guarantees (attestation cannot be replayed), (c) attestation signing and verification (who verifies attestation?), (d) testing attestation bypass attempts, (e) emerging attestation threats and mitigations.

**KSI-IAM-05-Q24:** How do you handle attestation failures or unavailability? Provide: (a) failure mode design (deny vs. allow if attestation service unavailable?), (b) failover mechanisms (backup attestation methods?), (c) recovery procedures if attestation is unavailable, (d) incident response for attestation service compromise, (e) SLA/uptime targets for attestation infrastructure.

_Note: Compliance benefits of attestation (Q39) moved to Compliance / Governance KSI._

---

## Section 8: Agent Lifecycle Management & Incident Response (From INR-03)

**KSI-IAM-05-Q25:** What evidence demonstrates your organization has discovered and remediated unauthorized autonomous agents with excessive permissions? Document: (a) agent inventory practices (complete enumeration of all agents), (b) discovery rate (percentage of agents with unauthorized access), (c) research context (39% of organizations discovered rogue agents; creation and use often unauthorized), (d) audit frequency (quarterly assessment of agent permissions), (e) examples of rogue agents discovered (what unauthorized access did they have, how was it used/prevented?).

**KSI-IAM-05-Q26:** What is your agent lifecycle management and credential rotation strategy? Explain: (a) agent provisioning (how are incident response agents created, with what permissions?), (b) credential management (static long-lived tokens vs. short-lived certificates?), (c) decommissioning (agents inactive >180 days automatically retired?), (d) maximum lifetime for agent credentials (research finding: <8 hours standing privilege target), (e) examples of agents retained past intended lifespan with accumulated permissions.

**KSI-IAM-05-Q27:** How do you detect behavioral anomalies in autonomous agents that indicate compromise or manipulation? Document: (a) baseline establishment (normal agent behavior patterns), (b) anomaly detection mechanisms (unusual API calls, access to unintended resources, lateral movement attempts), (c) mean time to detect (MTTD) for agent compromise, (d) containment procedures (revoke credentials, kill agent, investigate), (e) historical incidents of agent compromise detected through behavioral analysis.

**KSI-IAM-05-Q28:** How do you prevent privilege escalation attacks on incident response agents? Describe: (a) privilege model (what is minimum necessary permission set for incident response?), (b) privilege creep detection (unauthorized permissions accumulated over time?), (c) jailbreak vulnerability assessment (can attackers escape agent constraints?), (d) defense mechanisms (least-privilege enforcement, capability restrictions), (e) red team testing of privilege escalation vectors.

**KSI-IAM-05-Q29:** What incident response procedures exist if an autonomous agent is suspected of compromise or malicious behavior? Provide: (a) detection mechanisms triggering suspicion (behavioral anomalies, unauthorized actions, policy violations), (b) isolation procedures (revoke access, kill running processes), (c) forensic investigation (audit trail analysis, incident reconstruction), (d) impact assessment (what actions did compromised agent execute?), (e) remediation and hardening to prevent recurrence.

**KSI-IAM-05-Q30:** How do you prevent privilege creep and unintended permission accumulation in autonomous remediation systems? Describe: (a) least-privilege enforcement (minimum permission set for remediation?), (b) permission audit frequency (quarterly assessment), (c) automatic cleanup (permissions revoked when no longer required?), (d) conflict detection (remediation agent requesting excessive privilege?), (e) examples of privilege creep detected and corrected.

