# High Availability for AI Workloads: Discovery Questions

**KSI Focus:** CNA-06 - Achieve high availability for AI agents and LLM-powered systems through semantic health monitoring, KV cache durability, multi-agent coordination, Byzantine fault tolerance, durable execution frameworks, multi-region consistency, chaos engineering validation, and disaster recovery planning. Move beyond traditional infrastructure HA (uptime metrics) to AI-native HA (semantic correctness, agent reasoning coherence, cascade failure prevention).

**Context:** This discovery question set consolidates auditor, CIO, and customer perspectives to assess whether organizations effectively maintain AI workload availability through failure mode detection, state durability, agent coordination, observability, resilience testing, and recovery procedures. Questions focus on detecting silent failures invisible to traditional APM, preventing cascade failures in multi-agent systems, maintaining consistent state across distributed deployments, achieving sub-10-minute recovery time objective (RTO), and validating HA through chaos engineering.

---

## Section 1: AI-Specific Failure Modes & Cascade Detection

**KSI-CNA-06-Q01:** What AI-specific failure modes have you encountered that traditional infrastructure monitoring missed? Document: (a) Silent failures (system available but producing degraded output), (b) Reasoning drift (agent diverging from intended task over multiple iterations), (c) Memory poisoning (corrupted state cascading through reasoning chain), (d) Resource starvation (aggressive agents consuming GPU/connection pools), (e) Impact to end-users (how long before discovery?).

**KSI-CNA-06-Q02:** How do you detect when an AI agent has entered unrecoverable state requiring intervention? Describe detection mechanisms: (a) Decision validity checks (is agent making sensible choices?), (b) Output coherence checks (is output consistent with expected domain?), (c) Iteration depth monitoring (agent overthinking beyond reasonable limit?), (d) Detection latency (how quickly after failure occurs?), (e) False positive rate on valid but unusual behavior.

**KSI-CNA-06-Q03:** Do you monitor for cascade failures in multi-agent systems? Explain: (a) How do you detect when one agent's failure triggers failures in dependent agents?, (b) What correlation logic identifies cascade chains?, (c) Can you isolate failing agent to prevent cascade?, (d) Examples from past 12 months: cascade failures detected and remediation?, (e) Recovery procedures: how do you unwind cascaded state?

**KSI-CNA-06-Q04:** What is your mean time to detect (MTTD) for AI workload failures? Provide: (a) MTTD for total infrastructure failure (traffic drops), (b) MTTD for partial degradation (latency increase, throughput drop), (c) MTTD for semantic failure (output quality degradation without metrics change), (d) Comparison: is semantic failure detection slower than traditional monitoring?, (e) Plan to reduce MTTD for silent failures.

---

## Section 2: KV Cache State Management & Persistence

**KSI-CNA-06-Q05:** For stateful AI inference with KV cache, how do you ensure state durability and consistency? Document: (a) KV cache architecture (GPU-resident, persistent storage, replication), (b) Persistence mechanism (checkpointing frequency, backup location), (c) RTO (Recovery Time Objective) and RPO (Recovery Point Objective) for KV cache, (d) Can KV cache be recovered after node failure without data loss?, (e) Historical incidents: KV cache loss or corruption?

**KSI-CNA-06-Q06:** How do you verify KV cache integrity after recovery or failover? Describe: (a) Integrity checking mechanisms (checksums, cryptographic hashing), (b) Positional encoding validation (ensuring cache positions correct after recovery), (c) Consistency verification between replicated KV caches, (d) How do you detect cache corruption silently affecting output?, (e) Recovery procedures if corruption detected.

**KSI-CNA-06-Q07:** What is your KV cache replication strategy across availability zones/regions? Explain: (a) Replication topology (active-passive, active-active, N-way), (b) Replication latency (how quickly is cache replicated?), (c) Consistency model (strong, eventual, quorum-based), (d) Failover mechanism and latency when primary fails, (e) Data loss risk if multiple replicas fail simultaneously.

**KSI-CNA-06-Q08:** For long-running AI agent tasks (hours/days), how do you checkpoint and restore KV cache state? Describe: (a) Checkpoint frequency and storage location, (b) Checkpoint size and storage cost, (c) Restore latency (time to resume from checkpoint), (d) State consistency: can checkpoint be corrupted? How detected?, (e) Examples: multi-hour agent tasks successfully checkpointed and restored?

---

## Section 3: Multi-Agent Orchestration & Consensus

**KSI-CNA-06-Q09:** For multi-agent systems, how do you ensure state consistency when agents coordinate? Document: (a) Consensus protocol used (Raft, PBFT, other), (b) Byzantine fault tolerance threshold (how many agents can fail?), (c) Consistency guarantees (strong, eventual, causal), (d) Overhead of consensus (latency impact on agent communication), (e) Failure scenarios tested (specific agent failures, network partitions).

**KSI-CNA-06-Q10:** Can you detect when agents diverge on shared state or decisions? Describe: (a) Divergence detection mechanism (comparing agent states/decisions), (b) Root cause identification (conflicting updates? stale state?), (c) Remediation (reconciliation logic? forced sync?), (d) Detection latency: how long until divergence discovered?, (e) Historical incidents: multi-agent divergence causing incorrect decisions?

**KSI-CNA-06-Q11:** How do you prevent distributed deadlock in multi-agent systems? Explain: (a) Deadlock detection (agent A waiting for B, B waiting for A - how detected?), (b) Prevention mechanisms (ordering constraints, timeout-based recovery), (c) If deadlock occurs, recovery procedure and impact, (d) Testing: have you simulated deadlock scenarios?, (e) Time to resolve deadlock if it occurs.

---

**NOTE:** CNA-06-Q12 (agent delegation security/audit) has been moved to KSI-IAM-05 (Least Privilege) as it focuses on authentication, authorization, and audit trails between agents rather than high availability or recovery mechanisms.

---

## Section 4: Distributed Observability & Semantic Health

**KSI-CNA-06-Q12:** Beyond traditional APM metrics (CPU, memory, latency), what semantic health checks do you implement for AI systems? Describe: (a) Domain-specific accuracy checks (is AI output correct?), (b) Completeness checks (is AI providing complete answer or partial/truncated?), (c) Coherence checks (is output logically consistent?), (d) Confidence level monitoring (when is AI uncertain?), (e) Baseline: what is "healthy" semantic state?

**KSI-CNA-06-Q13:** Can your observability system detect degraded AI output BEFORE traditional metrics alert? Explain: (a) Pattern-based anomaly detection (Stop Spinning Wheels approach), (b) Early warning signals (latency increase before quality drop?), (c) Lead time: how many minutes before traditional alert fires?, (d) False positive rate on valid but unusual behavior, (e) Cases where semantic monitoring prevented customer impact.

**KSI-CNA-06-Q14:** What observability gaps exist in your AI monitoring? List: (a) Metrics that cannot be automated (require manual review?), (b) Blind spots in distributed tracing (which system components not monitored?), (c) Latency of observability pipeline (how long from event to dashboard visibility?), (d) Storage cost for maintaining observability data, (e) Compliance requirements (audit trail retention, access controls on telemetry).

**KSI-CNA-06-Q15:** For distributed AI workflows spanning multiple services/agents, can you reconstruct complete request trace? Describe: (a) Distributed tracing capability (OpenTelemetry, Datadog, custom), (b) Trace coverage (all services/agents instrumented?), (c) Latency to correlate traces across services, (d) Can you replay failed requests for debugging?, (e) Examples: complex trace used for post-incident analysis.

---

## Section 5: Chaos Engineering & Resilience Validation

**KSI-CNA-06-Q16:** What chaos engineering program do you maintain for AI workloads? Document: (a) Fault injection tests (which failure scenarios?), (b) Frequency of chaos experiments (weekly, monthly, quarterly), (c) Infrastructure failures tested (node failure, disk failure, network partition), (d) AI-specific failures tested (inference failure, KV cache loss, agent timeout), (e) Automation level (manual, CI/CD integrated, continuous).

**KSI-CNA-06-Q17:** What hidden cascade mechanisms have chaos engineering experiments revealed? Provide: (a) Unexpected failures triggered by specific fault combinations, (b) Failure modes invisible to traditional testing, (c) Dependencies between systems not obvious from architecture docs, (d) Recovery procedures that failed when tested under chaos, (e) Improvements deployed based on chaos findings.

**KSI-CNA-06-Q18:** Do you test disaster recovery procedures via chaos engineering or only via manual tabletop? Explain: (a) Frequency of DR testing (monthly, quarterly, annually), (b) Scope (full production failover vs. lab simulation?), (c) Success criteria (how do you measure DR procedure success?), (d) Recovery times achieved in testing vs. claimed RTO, (e) Gaps discovered during DR testing and remediation timeline.

**KSI-CNA-06-Q19:** Have you tested resilience under partial infrastructure outage? Describe: (a) Scenario: what percentage of infrastructure fails?, (b) Does system degrade gracefully or fail completely?, (c) Recovery time to full capacity after partial failure, (d) Data loss or state corruption during partial outage?, (e) Capacity management: how do you handle 50% infrastructure loss?

---

## Section 6: Durable Execution & Workflow State

**KSI-CNA-06-Q20:** For long-running AI agent tasks (hours, days), do you use durable execution frameworks? Document: (a) Framework used (Temporal, Durable Task Framework, custom), (b) State persistence (how often is state checkpointed?), (c) Automatic retry logic (if task fails mid-execution), (d) RTO/RPO for long-running tasks, (e) Example: multi-hour task successfully recovered from checkpoint after failure.

**KSI-CNA-06-Q21:** How do you ensure recovered state is semantically valid, not just data-consistent? Explain: (a) Validation checks before resuming from checkpoint, (b) What if checkpoint is corrupted? How detected?, (c) Can you validate recovered state against pre-failure audit trail?, (d) Rollback procedures if recovered state is invalid, (e) Examples: invalid recoveries detected and corrected.

**KSI-CNA-06-Q22:** For workflow state spanning multiple agents/services, how do you prevent state inconsistency after failure? Describe: (a) Distributed transaction support (Saga pattern, 2PC, other), (b) Compensation logic (if Agent A succeeds but Agent B fails, can A's state be reversed?), (c) Idempotency (can task be retried without side effects?), (d) Examples: complex workflow recovery scenarios tested, (e) Worst-case: can you lose entire workflow state?

---

## Section 7: Multi-Region Consistency & Replication

**KSI-CNA-06-Q23:** How do you replicate AI workload state across geographic regions? Document: (a) Replication topology (active-passive, active-active, multi-master), (b) Consistency model (strong, eventual, CRDT), (c) Replication latency (how long for change to propagate across regions?), (d) Failover mechanism if primary region fails, (e) Acceptable latency increase when using multi-region.

**KSI-CNA-06-Q24:** Can you guarantee consistency if network partition splits primary from secondary region? Explain: (a) CAP theorem trade-off (consistency vs. availability vs. partition tolerance), (b) During partition, which region remains available?, (c) After partition heals, how is divergence resolved?, (d) Data loss risk during split-brain, (e) Historical incidents: network partitions and impact.

**KSI-CNA-06-Q25:** For customer conversations/sessions spanning multiple regions, how do you maintain coherence? Describe: (a) Can customer session be served from different region without inconsistency?, (b) LLM context/conversation history replication across regions, (c) Latency impact of cross-region consistency, (d) If customer switches regions mid-conversation, recovery, (e) Testing: have you simulated multi-region failover?

**KSI-CNA-06-Q26:** What happens to active AI inference jobs if entire region fails? Provide: (a) Can running inference jobs be migrated to secondary region?, (b) KV cache state: recoverable or lost?, (c) User-facing impact (partial output loss? complete failure?), (d) RTO to resume inference in secondary region, (e) Examples: region failure scenarios and actual recovery times.

---

## Section 8: Disaster Recovery & RTO/RPO

**KSI-CNA-06-Q27:** What disaster recovery strategy do you employ for AI workloads? Document: (a) Strategy type (backup/restore, pilot light, warm standby, active-active), (b) RTO target (hours, tens of minutes, seconds?), (c) RPO target (data loss acceptable?), (d) Cost of DR strategy vs. acceptable downtime risk, (e) Business justification: is DR investment aligned with SLA commitments?

**KSI-CNA-06-Q28:** How frequently do you test disaster recovery procedures? Explain: (a) Testing frequency (annual, quarterly, monthly), (b) Scope (full production failover or lab simulation?), (c) Testing methodology (tabletop, simulated, actual failover), (d) Time to complete full recovery in testing, (e) Gaps discovered: where did actual recovery differ from plan?

**KSI-CNA-06-Q29:** If disaster recovery is executed, how do you validate recovered state? Describe: (a) Validation procedures before resuming customer traffic, (b) Automated validation vs. manual review, (c) Data integrity checks (any corruption detected?), (d) Semantic validation (is AI output quality maintained?), (e) Examples: recovery validation catching issues before production.

**KSI-CNA-06-Q30:** What is your strategy for backup integrity? Document: (a) Backup format (full copy, incremental, deduplicated), (b) Backup integrity verification (checksums, test restores), (c) Frequency of integrity testing, (d) Historical incidents: corrupted backups discovered during restoration?, (e) Immutable backups (can backups be modified or deleted?).

---

## Section 9: Performance, Load Testing, and High Availability Readiness

**KSI-CNA-06-Q31:** To what extent can AI agents automatically orchestrate and run performance, load, and stress tests against AI-evaluated infrastructure configurations, and how are thresholds or alerts defined when performance degradations are detected?[1]

*Note: This question moved from KSI-MLA-05 as it addresses HA/resilience through performance validation under load conditions.*

**KSI-CNA-06-Q32:** What capabilities exist for AI agents to evaluate infrastructure configurations for high availability, disaster recovery, and multi-region readiness, including testing of failover paths, RTO/RPO assumptions, and resilience against component failures?[5][1]

*Note: This question moved from KSI-MLA-05 as it directly addresses HA/DR configuration evaluation and validation.*

---

## Moved to Other KSIs

The following sections and questions have been moved to other KSIs based on filtering guidance to maintain CNA-06 focus on core HA mechanisms:

**Section 9: Compliance & FedRAMP HA Requirements**
- Q32, Q33, Q34 moved to a dedicated Compliance Automation / Policy-as-Code KSI
- These questions focus on governance, reporting automation, and policy management rather than HA architecture or recovery mechanisms

**Section 10: Financial Impact & Cost Analysis**
- Q35, Q36 moved to a dedicated Business/Financial Impact KSI
- These questions address business risk and ROI analysis rather than technical HA capability

**Section 11: Observability Infrastructure & Tools**
- Q37, Q38 moved to Logging/Observability KSI (e.g., CMT-01 or similar)
- Tool inventory and retention policies are generic observability governance topics, not HA-specific

**Section 12: Automation & Incident Response**
- Q39 (automated incident response) - Consider moving to Incident Response KSI if operationally scoped; keep MTTR/RTO focus if included in CNA-06
- Q40 (post-mortem process) - Move to Incident Learning / RCA KSI or Continuous Improvement KSI

---

## Schema Reference

**Question ID Format:** [KSI-CODE]-Q##
Example: CNA-06-Q01

**All questions should be answered with:**
- Direct evidence (not claims)
- Quantifiable data where applicable
- Supporting documentation (architecture diagrams, RCA reports, monitoring dashboards, test results)
- AI-specific examples where relevant
- Timeline/frequency information
- Comparison to research benchmarks when available

---

**Version:** 2.0 (Refined)
**Generated:** 2026-01-08
**Last Updated:** 2026-01-13
