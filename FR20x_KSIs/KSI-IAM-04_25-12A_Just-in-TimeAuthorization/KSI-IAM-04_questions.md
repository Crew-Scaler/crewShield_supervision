# Just-in-Time Authorization for Agentic AI: Discovery Questions

**KSI Focus:** IAM-04 - Implement just-in-time (JIT) authorization with task-scoped, time-limited permissions for AI agents, replacing static role-based access control. Emphasize cryptographic delegation protocols, continuous behavioral verification, protocol-level enforcement at MCP/tool boundaries, privilege escalation prevention, and multi-agent coordination governance.

---

## Section 1: Agent Authorization Paradigm & Task-Scoped Permissions

**KSI-IAM-04-Q001:** What evidence demonstrates your organization recognizes traditional RBAC/ABAC is fundamentally inadequate for autonomous AI agents? Describe: (a) assessment comparing agent authorization patterns to human user patterns (autonomy, speed, tool delegation, dynamic permission requests), (b) documented gap analysis showing where static roles fail for agents, (c) JIT authorization pilot or production implementation with measurable improvements, (d) executive decision or roadmap acknowledging agent-specific authorization architecture required.

**KSI-IAM-04-Q002:** How do you implement task-scoped authorization for agents with minimal permission grants? Document: (a) task scope definition methodology (what constitutes a "task"—single LLM call, multi-step workflow, time-bounded execution), (b) permission binding to tasks (which specific tools, APIs, data can agent access for each task), (c) token/grant lifetime per task (target: seconds for simple tasks, minutes to hours for complex workflows), (d) examples of representative agent tasks with documented permission scope, (e) tooling supporting task-scoped policy definition and enforcement.

**KSI-IAM-04-Q003:** What mechanisms trigger automatic revocation of agent permissions before granted TTL expires? Describe: (a) signals triggering revocation (tool misuse, resource overconsumption, suspicious data access patterns), (b) revocation latency (time from signal detection to revocation—target: <5 minutes), (c) false positive rate and mechanisms preventing over-revocation, (d) examples of revocations triggered in production, (e) agent response to revocation (graceful degradation vs. failure).

**KSI-IAM-04-Q004:** How do you prevent privilege escalation through agent permission requests? Document: (a) control preventing agents from requesting elevated permissions outside task scope, (b) approval workflow for elevation requests (automatic denial vs. human review), (c) escalation attempt logging and alerting, (d) examples of escalation attempts detected and blocked, (e) least-privilege verification (do agents ever request permissions they don't need?).

**KSI-IAM-04-Q005:** What evidence validates that agent permissions match stated task intent and no broader? Provide: (a) permission audit for sample agents: documented task → assigned permissions → assessment of necessity, (b) over-privilege detection (are agents granted permissions exceeding documented needs?), (c) remediation process for over-provisioned agents, (d) automated tooling supporting permission necessity assessment.

---

## Section 2: MCP Security & Protocol-Level Authorization Enforcement

**KSI-IAM-04-Q006:** How do you enforce comprehensive authorization at Model Context Protocol (MCP) boundaries to prevent tool misuse, including both tool-level and parameter-level controls? Document: (a) MCP server architecture and tool catalog, (b) authorization enforcement point (before tool invocation, at MCP boundary vs. application layer), (c) tool whitelisting mechanism (which specific tools can each agent access), (d) fine-grained authorization constraints within MCP tool calls: parameter-level authorization (agent can invoke API X, but only with specific parameter values), rate limiting per agent per tool (preventing abuse and DoS), data filtering based on authorization (API returns only authorized data), (e) tool schema validation preventing tampering or unauthorized parameter injection, (f) examples of parameter constraints and tool access denials based on authorization policy, (g) latency and performance impact of fine-grained enforcement.

**KSI-IAM-04-Q007:** What controls prevent "confused deputy" attacks where agents misuse legitimate permissions? Document: (a) intent verification at authorization time (is declared task matching actual tool invocation?), (b) tool invocation audit trail, (c) anomalous tool combination detection (e.g., billing analysis agent invoking code repository access), (d) examples of confused deputy attempts detected and blocked, (e) response mechanism (immediate revocation vs. alert vs. rate-limiting).

**KSI-IAM-04-Q008:** How do you handle agent requests to access tools or resources outside pre-approved scope? Document: (a) approval workflow for out-of-scope access requests (automated review vs. human approval), (b) temporary elevation mechanism (grant short-lived access for specific task, then automatic revocation), (c) approval latency target and actual (time from request to decision), (d) logging of all requests, decisions, and outcomes, (e) metrics on approval accuracy and override procedures.

---

## Section 3: Cryptographic Delegation & Multi-Hop Authorization Chains

**KSI-IAM-04-Q009:** How do you implement cryptographic delegation protocols for agent-to-agent authorization with explicit scope narrowing? Document: (a) delegation protocol used (JWT-based Agentic JWT, SPIFFE, DIDs/VCs, custom protocols), (b) context lineage encoding in delegation tokens (who delegated, what intent, what scope, when issued), (c) scope narrowing enforcement as mathematical property (delegated permissions ⊆ delegating agent's permissions, ability to grant subset of agent A's permissions to delegated agent B), (d) token expiration and revocation mechanisms (immediate revocation capability?), (e) examples of multi-hop delegations with documented scope constraints and granular scoped delegations, (f) tooling supporting fine-grained delegation policy definition and default-deny approach (agent gets only explicitly granted permissions), (g) testing demonstrating delegation scope is strictly enforced across multi-hop chains.

**KSI-IAM-04-Q010:** For agent-to-agent delegation chains, how do you prevent unbounded escalation and privilege amplification? Describe: (a) delegation depth limits (maximum number of hops in authorization chain), (b) scope narrowing at each hop with documented constraints, (c) testing multi-hop chains to verify escalation is prevented, (d) delegation audit trail enabling forensic reconstruction (who delegated to whom, when, with what scope), (e) revocation capability at any level (parent can immediately revoke all child permissions).

**KSI-IAM-04-Q011:** What evidence demonstrates delegation chains remain auditable and non-repudiable? Provide: (a) immutable audit log of all delegations with cryptographic signatures, (b) reconstruction capability: given final action, trace back to original delegating authority, (c) examples of forensic reconstruction from delegation chains proving authorization chain, (d) audit trail retention period and integrity protection mechanisms.

**KSI-IAM-04-Q012:** How do you validate that delegations encode actual user intent, not just authorization claims? Explain: (a) intent verification at delegation time (human confirms agent purposes before delegation?), (b) intent validation at execution time (agent action matches conveyed intent or deviates?), (c) mismatch detection mechanism and handling (intent deviation triggers revocation?), (d) testing intent validation with adversarial agents attempting to exceed intent, (e) examples of intent mismatches detected and remediation.

---

## Section 4: Privilege Escalation & Lateral Movement Prevention

**KSI-IAM-04-Q013:** How do you detect and prevent privilege escalation attempts by compromised or malicious agents? Document: (a) escalation patterns monitored at authorization layer (requesting higher-privilege tools, attempting policy modification, cross-agent privilege laundering), (b) detection mechanisms (rule-based patterns, authorization-layer monitoring), (c) detection latency and response time, (d) examples of escalation attempts blocked with evidence, (e) false positive rate and mechanisms for tuning detection sensitivity.

**KSI-IAM-04-Q014:** What controls prevent lateral movement and cross-agent compromise propagation? Explain: (a) authorization segmentation isolating agents, (b) agent-to-agent communication controls (mutual authentication, authorization checks, encrypted audit), (c) cross-agent permission isolation (compromised Agent A cannot leverage Agent B's permissions), (d) testing lateral movement scenarios and containment, (e) blast radius containment (if agent compromised, which other systems can it access?).

**KSI-IAM-04-Q015:** How do you prevent "privilege laundering"—multi-agent workflows chaining permissions to escalate effective privilege? Describe: (a) privilege laundering threat definition and risk assessment, (b) detection mechanism identifying suspicious agent coordination patterns, (c) workflow orchestration controls preventing unauthorized delegation chains, (d) examples of laundering attempts detected and blocked, (e) agent behavior verification preventing escalation through composition.

**KSI-IAM-04-Q016:** Do you maintain privilege matrices or visualizations showing agent permissions? Provide: (a) privilege matrix documentation: Agent A {permissions X,Y,Z}, Agent B {permissions Y,Z,W}, etc., (b) tooling for maintaining matrix accuracy and freshness, (c) periodic audits validating matrix (target: quarterly), (d) analytics on privilege distribution (are critical permissions concentrated?), (e) automated removal of unused or excessive permissions.

**KSI-IAM-04-Q017:** What authorization-layer controls flag agent behavior diverging from documented permission usage? Document: (a) usage baseline for each agent's permissions (which permissions are actually used, at what frequency), (b) deviation detection (rapid new tool access, permission request anomalies inconsistent with baseline), (c) detection mechanisms (rule-based monitoring, authorization logging analysis), (d) examples of deviations detected and investigated, (e) false positive rate and review process.

---

## Section 5: Continuous Authorization & Authorization Caching

**KSI-IAM-04-Q018:** What percentage of JIT authorization decisions are made in real-time vs. cached/pre-computed? Explain: (a) decisions requiring real-time verification (tool invocation, sensitive data access, privilege changes), (b) decisions allowing caching or pre-computation (performance optimization), (c) latency targets and achieved latencies for real-time decisions, (d) cache invalidation mechanisms (what triggers re-verification?), (e) security vs. performance trade-offs of different caching strategies.

**KSI-IAM-04-Q019:** For continuous authorization of long-running agent tasks, how do you maintain permission validity across extended execution? Describe: (a) checkpoint mechanisms for multi-hour/multi-day tasks, (b) re-authorization requirement at checkpoints, (c) context preservation across re-authorization events, (d) abort/rollback procedures if agent loses required permissions mid-task, (e) examples of long-running tasks with documented re-authorization events.

---

## Section 6: Defense-in-Depth & Agent Hardening

**KSI-IAM-04-Q020:** What defense-in-depth strategy combines JIT authorization with other authorization enforcement layers? Document: (a) layers of enforcement (application-layer authorization, protocol-level enforcement at MCP boundaries, enforcement at MCP server level), (b) tools implementing each layer, (c) failure modes and testing (what if application layer fails?), (d) redundancy ensuring breach of single layer doesn't enable full compromise, (e) examples where defense-in-depth prevented agent misuse.

**KSI-IAM-04-Q021:** What role do guardian/sentinel agents play in authorization validation? Describe: (a) guardian agent architecture (secondary agent approving primary agent actions before execution?), (b) decision types requiring guardian approval (high-risk operations, privilege elevation, data access), (c) latency impact of guardian approval (target: <5 minutes for complex decisions), (d) guardian false approval rate (do guardians catch attempted abuse?), (e) examples of misuse caught by guardian agents.

**KSI-IAM-04-Q022:** How do you protect agent authorization against prompt injection attacks attempting bypass? Document: (a) authorization enforcement even for injection-generated requests (injection doesn't bypass JIT controls), (b) authorization layer validation of agent-submitted requests (intent verification, anomaly detection), (c) testing with adversarial prompts attempting authorization bypass, (d) examples of injection-derived requests detected and blocked by authorization controls.

---

## Section 7: Multi-Agent Coordination & Distributed Authorization

**KSI-IAM-04-Q023:** For multi-agent systems, how do you enforce authorization boundaries preventing cascade failures? Document: (a) agent isolation mechanisms (authorization domains preventing cross-agent access), (b) inter-agent communication controls (mutual authentication, authorization checks, encrypted audit), (c) blast radius containment (if Agent A compromised, which agents can it access?), (d) testing cascade failure scenarios, (e) remediation procedures if unauthorized agent-to-agent communication detected.

**KSI-IAM-04-Q024:** How do you handle authorization for agents coordinating on shared tasks? Describe: (a) shared task authorization model (which agents can participate, what scope per agent), (b) coordination protocol ensuring all participants have necessary permissions, (c) consensus mechanisms for multi-agent decisions requiring authorization agreement, (d) examples of multi-agent workflows with documented authorization, (e) audit trail showing each agent's contribution, permissions used, and authorization decisions.

**KSI-IAM-04-Q025:** What governance framework enables agent-to-agent delegation while preventing unauthorized escalation? Document: (a) delegation policies governing which agents can delegate to which other agents, (b) scope constraints on delegations (delegated permissions must be subset), (c) approval workflows for sensitive delegations, (d) testing preventing circular delegation dependencies and deadlocks, (e) examples of valid vs. blocked delegations with documented reasons.

**KSI-IAM-04-Q026:** How do you audit and forensically reconstruct complex multi-agent workflows? Explain: (a) tracing capability showing complete chain: user intent → Agent A decision → Agent B delegation → Tool invocation → Result, (b) audit log completeness (every delegation, authorization decision, tool call logged), (c) immutability and tamper-evidence of audit logs (cryptographic signatures?), (d) forensic reconstruction examples proving authorization chain, (e) compliance demonstrability (can you prove to external auditor what happened and why?).

**KSI-IAM-04-Q027:** What is your incident response and recovery procedure when agent operates outside JIT authorization scope? Provide: (a) detection to containment time (MTTR target and actual), (b) containment procedures (immediate revocation, agent isolation, active session termination), (c) forensic investigation (reconstruct what agent accessed, what data exposed, when?), (d) remediation (fix agent, update policies, prevent recurrence), (e) examples from past 12 months with timeline and impact assessment.

