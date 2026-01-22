# Minimize Attack Surface: Discovery Questions

**KSI Focus:** CNA-02 - Minimize the attack surface of the cloud service offering, with emphasis on AI systems and agents. Implement agent isolation, least-privilege access control, jailbreak prevention, container security, and privilege escalation detection to reduce the blast radius of compromised agents and limit lateral movement.

**Context:** This discovery question set consolidates auditor, CIO, and customer perspectives to assess whether organizations effectively minimize attack surface through agent sandboxing, fine-grained access control, behavior monitoring, and privilege escalation prevention. Questions focus on identifying and eliminating unnecessary permissions, preventing agent autonomy abuse, detecting jailbreaks and prompt injections, and containing blast radius of compromised workloads.

---

## Section 1: AI Agent Isolation & Containment

**CNA-02-Q01:** How many AI agents are deployed in production? For each agent category (data processors, orchestrators, API callers), describe: (a) what actions agents can perform autonomously, (b) runtime isolation method (container, VM, sandbox, process isolation), (c) resource limits (CPU, memory, disk, file descriptor limits), (d) filesystem restrictions (read-only root, chroot, restricted volumes), (e) whether hard isolation (Kata, gVisor, TEE) or soft isolation (namespaces, cgroups) is used.

**CNA-02-Q02:** Describe your agent sandboxing framework. Do you use: (a) containerization (Docker, Kubernetes namespaces) with restricted capabilities, (b) VM-based isolation (Kata Containers, Firecracker, KVM), (c) hardware-assisted isolation (Intel SGX, AMD SEV), (d) unikernels, or other isolation mechanism? What is the isolation guarantee (process cannot break to host, cannot access other agents' data, etc.)?

**CNA-02-Q03:** What capabilities can AI agents leverage? Describe: (a) which Linux capabilities are enabled/dropped (SYS_ADMIN, SYS_PTRACE, NET_RAW, etc.), (b) seccomp or apparmor profiles restricting syscalls, (c) filesystem access scope (read-only vs. read-write directories), (d) network capabilities (can agents listen on ports, open raw sockets, modify network stack?). Can agents execute arbitrary code, or is code execution restricted to approved tools?

**CNA-02-Q04:** Can agents execute code? If yes: (a) what code execution mechanisms are available (shell, script execution, container launch, function invocation), (b) how is code execution validated (bytecode signing, whitelist, static analysis), (c) what code can be executed (pre-approved functions, arbitrary user scripts, untrusted third-party code), (d) can agents modify their own runtime/code after deployment?

**CNA-02-Q05:** How do you detect and prevent agent jailbreaks and multi-turn prompt injection attacks? Describe: (a) prompt filtering (input sanitization, context confusion detection), (b) behavioral monitoring for jailbreak indicators (unusual function calls, policy escape attempts, guardrail bypass patterns), (c) baselines for normal agent behavior vs. jailbreak attempts, (d) test evidence of jailbreak detection effectiveness from past 12 months.

**CNA-02-Q06:** Have you experienced agent jailbreaks, prompt injections, or policy escapes in the past 12 months? For each incident: (a) attack method (multi-turn conversation, indirect injection, context injection, tool misuse), (b) what agent policy was the attacker trying to circumvent, (c) detection method and time-to-detection, (d) was jailbreak successful or blocked, (e) impact if successful (data access, lateral movement, infrastructure modification), (f) remediation (prompt filters strengthened, guardrails hardened, agent retired).

**CNA-02-Q07:** What multi-turn jailbreak defenses do you implement? Single-turn prompt filters are insufficient. Describe: (a) conversation history monitoring (detect jailbreak progression across multiple turns), (b) intent classification (detect when user is attempting to circumvent guardrails), (c) context window management (prevent context confusion through long conversations), (d) periodic re-verification of agent constraints across conversation turns.

**CNA-02-Q08:** For container-based agent deployments, what controls prevent container escape to host OS? Describe: (a) capability dropping (removing SYS_ADMIN, SYS_PTRACE, NET_ADMIN), (b) read-only root filesystem + tmpfs for writable areas, (c) seccomp/apparmor profiles restricting dangerous syscalls, (d) runtime monitoring for escape attempts, (e) hard isolation layer (Kata, gVisor, SELinux) as defense-in-depth. Provide evidence of escape prevention testing.

---

## Section 2: Agent Access Control & Privilege Management

**CNA-02-Q09:** Describe the permission model for AI agents. For each agent type, document: (a) resource access scope (which databases, APIs, services can agent access?), (b) operation scope (read-only, read-write, delete permissions), (c) data scope (which customer data, tenant data, sensitive data can agent access?), (d) time-based constraints (24/7 access or business hours only?), (e) rate limits (requests/minute, data volume limits).

**CNA-02-Q10:** Do you implement least-privilege access for agents? Describe mechanisms: (a) agents assigned minimal permissions needed for specific task, (b) permissions scoped by resource type (read production database but not write, read customer data but not admin data), (c) permissions scoped by operation (GET /data but not POST, select but not delete), (d) temporal constraints (permissions valid only during task execution), (e) how permissions are enforced (IAM, API gateway, service mesh, application-level).

**CNA-02-Q11:** Do you use Just-in-Time (JIT) access for agents? Describe: (a) agents request permissions before execution (not pre-granted), (b) permissions are automatically granted for specific task duration, (c) permissions are automatically revoked upon task completion, (d) who/what approves agent permission requests (pre-approved patterns, automated risk scoring, human approval), (e) audit trail of all permission grants/revokes.

**CNA-02-Q12:** How do you manage agent credentials and secrets? Describe: (a) credential lifecycle (generation, provisioning, rotation, revocation), (b) credential storage (never in code/logs, stored in secrets vault, in-memory only), (c) credential distribution (how agents receive credentials at runtime), (d) credential rotation frequency (daily, weekly, per-task), (e) revocation procedures (if agent is compromised, how quickly can all credentials be revoked?). Provide evidence of credential rotation from past 30 days.

**CNA-02-Q13:** Have you experienced agent credential compromise in the past 12 months? Describe: (a) how compromise was detected (unauthorized access pattern, secret scan, audit finding), (b) compromised agent identity, (c) duration of compromise (dwell time), (d) what resources could be accessed with compromised credentials, (e) what data/infrastructure could be modified, (f) remediation (revoked credentials, rotated all agent secrets, isolated compromised agent), (g) post-incident: did you discover data was exfiltrated or systems modified?

---

## Section 3: Privilege Escalation Prevention & Detection

**CNA-02-Q14:** Can you model privilege escalation paths for AI agents? Using graph-based analysis, identify: (a) which agents have permissions to call administrative APIs/services, (b) which agents can access secrets manager, configuration systems, deployment pipelines, (c) trust transitivity (if agent A calls service B, and B has high privileges, can A indirectly escalate?), (d) which escalation paths are exploitable by agents with current permissions.

**CNA-02-Q15:** Describe your approach to eliminating unnecessary privileges. For high-risk escalation paths identified: (a) can permission be removed entirely (eliminate overprivileged role), (b) can permission be restricted further (access-time windows, resource quotas, operation constraints), (c) can permission be gated (human approval before admin operation, audit logging, retry limits), (d) if permission cannot be removed, implement detective controls (behavioral anomaly detection, unusual operation logging, post-execution audit).

**CNA-02-Q16:** How do you detect privilege escalation attempts by AI agents? Describe detection mechanisms: (a) if agent requests unexpected high-privilege operation, alert + block, (b) if agent accesses admin APIs/services for first time, investigate, (c) if agent permission grants are requested outside normal pattern, audit, (d) baseline agent behavior for normal operations vs. escalation attempts. What is detection accuracy and false positive rate?

**CNA-02-Q17:** Have you detected privilege escalation attempts by agents in the past 12 months? For each incident: (a) agent identity and permission level, (b) escalation target (which high-privilege operation was attempted?), (c) detection method and time, (d) was escalation successful or prevented, (e) if successful: impact (systems accessed, data exfiltrated, infrastructure modified), (f) root cause (permission was overprivileged, no detection was in place, attacker had legitimate-seeming justification).

---

## Section 4: Agent Behavior Monitoring & Anomaly Detection

**CNA-02-Q18:** Have you established behavior baselines for production AI agents? For each agent type, describe: (a) normal behavior characteristics (typical API calls, call frequencies, data volumes, error rates, processing latencies), (b) how baselines were established (initial observation period, reference implementations, ML training), (c) baseline establishment time (how long until reliable baseline exists?), (d) baseline updates (static or continuously learning?).

**CNA-02-Q19:** What multi-layer anomaly detection is deployed? Describe detection across: (a) network layer (unusual egress, port scanning, suspicious DNS), (b) identity layer (unexpected privilege grants, failed authentication spikes), (c) application layer (API call patterns, data access patterns, tool usage anomalies), (d) agent-specific metrics (tool deviations, permission request anomalies, execution anomalies). How are signals correlated across layers to identify high-confidence threats?

**CNA-02-Q20:** What is your anomaly detection accuracy and false positive rate? Provide metrics: (a) % of anomalies detected (sensitivity/recall), (b) % of normal activity falsely flagged as anomalous (false positive rate), (c) which detection method is most effective (statistical, ML-based, graph-based, other), (d) detection latency (real-time or batch). Benchmark targets: >85% sensitivity, <5% FPR.

**CNA-02-Q21:** If agent anomaly is detected, what is your response? Do you: (a) alert security team for investigation, (b) rate-limit agent (reduce request rates), (c) block specific actions (agent can continue normal operations but suspicious actions blocked), (d) isolate agent (pause agent, revoke credentials, prevent network access), (e) terminate agent (shutdown and investigation). What is detection-to-response time?

**CNA-02-Q22:** Can you identify agent compromise quickly enough to prevent significant damage? Describe: (a) best-case scenario: compromise detected within X minutes, agent isolated, blast radius limited to Y systems, (b) worst-case scenario: compromise undetected for Z hours, agent exfiltrated data from W systems, cost of incident = $C. Is worst-case impact acceptable? What mitigations would reduce likelihood or impact of worst-case?

---

## Section 5: Multi-Agent Isolation & Coordination Security

**CNA-02-Q23:** How many AI agents interact with other agents (agent-to-agent calls)? Describe agent-to-agent communication: (a) which agents can call which agents, (b) what data/context is passed between agents, (c) are agent-to-agent calls authorized separately or inherited from caller's permissions, (d) can one agent craft malicious input to jailbreak another agent?

**CNA-02-Q24:** What prevents compromised agent from weaponizing trust chains to other agents? Describe controls: (a) per-agent-pair authorization (agent A can call agent B, but only with specific request types), (b) data isolation (agent B cannot access agent A's data even if called by A), (c) behavioral monitoring for unexpected agent-to-agent calls, (d) blast radius limiting (if agent B is called by compromised agent A, can B be isolated to prevent cascade?).

**CNA-02-Q25:** Have you modeled multi-agent cascade failures? Describe: (a) agent dependency graph (A calls B, B calls C, etc.), (b) cascade scenarios (if A fails, does B fail? If A is malicious, can A trigger failures in B and C?), (c) blast radius of cascades (which agents affected, which systems affected if cascade occurs?), (d) prevention controls (circuit breakers, rate limits, isolation boundaries limiting cascade propagation).

**CNA-02-Q26:** Have you experienced multi-agent cascade failures in the past 12 months? Describe: (a) which agents were involved, (b) what triggered the cascade, (c) how many agents were affected, (d) what systems/services downstream failed, (e) detection and response time, (f) root cause (no rate limiting, cascading retries, permission inheritance, unexpected agent coordination).

---

## Section 6: Container Escape Prevention & Response

**CNA-02-Q27:** For container-based agent deployments, describe your multi-layer isolation: (a) Kubernetes namespace isolation (network policies separating pods), (b) container runtime isolation (Docker, containerd with configured restrictions), (c) kernel isolation (Linux namespaces, cgroups), (d) hard isolation option (Kata, gVisor) for high-risk agents. Which layers are mandatory vs. optional for different agent categories?

**CNA-02-Q28:** What container escape vectors are you protecting against? Describe: (a) kernel exploits (CVEs in container runtime), (b) privilege escalation within container (abuse of enabled capabilities), (c) Kubernetes API abuse (if pod has API token, can it access cluster-admin resources?), (d) shared kernel vulnerabilities, (e) supply chain compromise (malicious container image). For each vector, describe defense.

**CNA-02-Q29:** How do you detect container escapes? What signals indicate escape: (a) unexpected host filesystem access from pod, (b) unexpected privilege escalation within pod, (c) unexpected host network access, (d) unexpected inter-pod traffic crossing network policy boundaries? What tools are deployed (Falco, Cilium Tetragon, eBPF-PATROL)? Benchmark: <1ms overhead, >94% detection accuracy.

**CNA-02-Q30:** If container escape is suspected/detected, what is your incident response? (a) Isolate container (block all network and storage access), (b) preserve forensics (memory dump, container logs, syscall traces), (c) investigate blast radius (what else could escaped process access?), (d) contain lateral movement (network segmentation should prevent access to other tenants), (e) notify affected customers (if multi-tenant, determine which customers potentially affected).

---

## Section 7: Supply Chain & Model Security for Agents

**CNA-02-Q31:** For AI agents deployed to your platform, can you verify agent provenance and integrity? Describe: (a) agent code signing (is agent code signed by trusted developers?), (b) agent source verification (does agent code come from approved repositories?), (c) agent dependency scanning (are agent dependencies free of known vulnerabilities?), (d) agent behavior analysis (does agent behave as documented, or does it have hidden capabilities?).

**CNA-02-Q32:** Have you discovered or deployed agents with hidden capabilities (trojan agents, backdoored agents, agents with unintended behaviors)? Describe: (a) detection method (security review, testing, anomaly detection), (b) what hidden capability existed, (c) how hidden capability was discovered, (d) affected agents and impact, (e) remediation (agent retired, source investigation, process improvements).

**CNA-02-Q33:** What threat models apply to third-party or externally-provided agents? Consider: (a) data exfiltration (agent sends customer data to external destination), (b) lateral movement (agent uses inherited permissions to compromise other systems), (c) resource abuse (agent consumes excessive compute/memory, DoS), (d) policy escape (agent circumvents guardrails through prompt injection or jailbreak). For each threat model, describe mitigation.

---

## Section 8: Threat Modeling & Risk Assessment

**CNA-02-Q34:** Have you conducted threat modeling for AI agent scenarios? Describe: (a) threat scenarios considered (agent jailbreak, credential compromise, container escape, privilege escalation, multi-agent cascade), (b) likelihood assessment for each threat, (c) impact assessment (if threat occurs, what is worst-case impact?), (d) mitigations in place to reduce likelihood/impact, (e) residual risk acceptability. Use risk framework: Risk = Likelihood × Impact × (1 - Mitigation Effectiveness).

**CNA-02-Q35:** For high-risk agents, what is your defense-in-depth strategy? Describe layered controls: (a) isolation (sandboxing to prevent escape), (b) access control (least-privilege to limit damage if compromised), (c) monitoring (anomaly detection to identify compromise quickly), (d) response (automated containment to limit blast radius), (e) recovery (can you recover from agent compromise without data loss?).

**CNA-02-Q36:** What is acceptable blast radius if an AI agent is compromised? Define metrics: (a) how many other systems can compromised agent reach (lateral movement scope)?, (b) how much data can be exfiltrated (data access scope)?, (c) how much infrastructure can be modified (modification scope)?, (d) how long until detection (<X minutes)?. If actual blast radius exceeds acceptable, implement stronger isolation/monitoring.

---

## Section 9: Continuous Improvement & Incident Learning

**CNA-02-Q37:** In the past 12 months, what AI/agent-related security incidents occurred? For each incident: (a) attack vector, (b) how it was detected, (c) impact, (d) root cause (control gap, misconfiguration, human error), (e) remediation, (f) process improvement implemented to prevent recurrence. Rate limiting: X incidents, of which Y were preventable with existing controls.

**CNA-02-Q38:** How do you use threat intelligence and research to improve attack surface reduction for agents? Describe: (a) new vulnerabilities/attack vectors from research (papers, CVEs, threat reports), (b) how you assess whether new threats apply to your agents, (c) how you implement mitigations (patches, policy changes, new controls), (d) examples from past 12 months of agent security improvements driven by external intelligence.

---

## Schema Reference

**Question ID Format:** [KSI-CODE]-Q##
Example: CNA-02-Q01

**All questions should be answered with:**
- Direct evidence (not claims)
- Quantifiable data where applicable
- Supporting documentation (threat models, test results, incident reports, policy documents)
- AI-specific examples where relevant
- Timeline/frequency information
- Comparison to research benchmarks when available

---

**Version:** 1.1
**Updated:** 2026-01-13
