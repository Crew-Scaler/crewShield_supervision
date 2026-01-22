# Restrict Network Traffic: Discovery Questions

**KSI Focus:** CNA-01 - Restrict network traffic to and from the cloud service offering, with emphasis on AI systems, agents, and multi-tenant infrastructure. Implement network segmentation, egress filtering, DLP, and anomaly detection to prevent unauthorized data exfiltration and lateral movement.

**Context:** This discovery question set consolidates auditor, CIO, and customer perspectives to assess whether organizations effectively restrict network traffic through zero-trust architecture, per-agent network policies, egress filtering, and behavioral monitoring. Questions focus on microsegmentation, AI agent isolation, multi-tenant boundaries, data exfiltration prevention, container escape containment, and compliance requirements.

---

## Section 1: Zero-Trust Architecture & Network Microsegmentation

**CNA-01-Q01:** Describe your current network architecture. Is it perimeter-centric (firewall at boundary, implicit trust inside) or zero-trust (explicit authorization for all connections)? What percentage of internal service-to-service traffic (east-west) is explicitly authorized vs. implicitly trusted? Provide architecture diagrams showing segmentation zones.

**CNA-01-Q02:** What is your network segmentation strategy? Do you implement macro-segmentation (security zones: production, staging, development, tenant zones) and/or micro-segmentation (service-level, container-level, agent-level)? For each segmentation level, describe how boundaries are enforced: firewall rules, network policies, service mesh policies, or other mechanisms.

**CNA-01-Q03:** Have you implemented zero-trust architecture with deny-all-by-default stance? Provide evidence: (a) network policies or firewall rules implementing default-deny, (b) continuous authentication/authorization mechanisms for all connections, (c) identity-based (not IP-based) access control, (d) documented zero-trust framework compliance (NIST SP 800-207, CISA Maturity Model, Microsoft framework).

**CNA-01-Q04:** For macro-segmentation, describe your security zones. How is traffic between zones restricted? Sample 100 inter-zone traffic flows; verify each has explicit allow-list policy (not implicit trust). What is your blast radius if one zone is compromised? Can an attacker in production zone laterally move to data tier, admin systems, or other sensitive services?

**CNA-01-Q05:** For micro-segmentation implementation, what percentage of your services have dedicated network policies (not shared policies)? Do policies enforce deny-all-by-default ingress and egress? Provide network policy configuration samples (YAML/JSON) showing: authorized inbound callers, authorized outbound destinations, restricted ports/protocols.

**CNA-01-Q06:** How do you handle dynamic workloads (containers, serverless functions) with changing IP addresses? Are access decisions based on workload identity (service principals, mTLS certificates, API keys) or IP addresses? If IP-based, what is your migration timeline to identity-based controls? Can you demonstrate identity verification for service-to-service calls?

**CNA-01-Q07:** Have you experienced lateral movement incidents in the past 12 months? Describe: (a) attack vector, (b) detection method and detection time, (c) number of systems compromised (blast radius), (d) impact severity, (e) root cause (network segmentation insufficient, missing policies, configuration drift), (f) remediation and process improvements.

**CNA-01-Q08:** For multi-tenant infrastructure, how do you enforce tenant isolation? Is isolation hard (separate clusters, dedicated networks, encrypted boundaries) or soft (network policies, namespaces, application-level logic)? Provide multi-tenant isolation architecture diagrams. Can you demonstrate (via test or incident review) that tenant A cannot reach tenant B's resources even if tenant A is compromised?

---

## Section 2: AI Agent Network Policy & Isolation

**CNA-01-Q09:** How many AI agents are currently deployed in production? Provide complete inventory: agent name, purpose, identity mechanism (service principal, certificate, API key), network policy applied. For each agent type, describe what actions agents can perform autonomously: API calls, database queries, infrastructure modifications, data access.

**CNA-01-Q10:** Do each of your AI agents have a dedicated, unique identity? What percentage of agents share identity across multiple agents (shared service account)? If agent identity is shared, how can individual agents be controlled, monitored, or isolated? Benchmark: 100% of agents should have unique identity; <10% sharing is acceptable only with strong justification.

**CNA-01-Q11:** Describe per-agent network policies for a sample of 50 AI agents. For each agent, provide: (a) ingress policy (which services/identities can call this agent?), (b) egress policy (which services/APIs/databases can agent call?), (c) default stance (deny-all or allow-all?), (d) tool access restrictions (which tools can agent invoke?). Verify policies are deny-all-by-default with explicit allow-lists.

**CNA-01-Q12:** What tools can your AI agents access? Provide comprehensive list: code execution (shell, scripts, containers?), file system access (read/write scope), API calls (which endpoints?), database queries (read/write/delete permissions?), infrastructure modifications (deployment, auto-scaling, configuration changes?), secret access (credential vault access?). How is tool access controlled: application-level guardrails, network policies, identity-based enforcement?

**CNA-01-Q13:** How do you sandbox AI agent tool access? Describe controls preventing agents from: executing arbitrary code, accessing unauthorized APIs, modifying infrastructure without approval, escalating privileges, accessing secrets outside authorized scope. Verify network policies enforce tool sandboxing (agent can only reach approved endpoints for each tool).

**CNA-01-Q14:** Can you test per-agent network policies? Demonstrate: (a) deploy test agent with known identity, (b) attempt authorized API call - verify success, (c) attempt unauthorized call - verify blocked. Provide test evidence from past 12 months. Benchmark: 100% of agent network policies should prevent unauthorized API access.

**CNA-01-Q15:** In the past 12 months, have you detected any AI agents exceeding authorized scope (policy violations)? Describe: (a) agent identity, (b) unauthorized action attempted, (c) detection method, (d) time-to-detection, (e) impact if successful, (f) remediation (revoked agent identity, policy tightened, agent retired), (g) root cause (policy was inadequate, guardrails bypassed, compromised agent).

---

## Section 3: AI Agent Behavior Monitoring & Anomaly Detection

**CNA-01-Q16:** Do you monitor AI agent network activity in real-time? What telemetry is collected: all API calls, network connections, data access, tool invocations? Is monitoring automated (all agents) or selective (high-risk agents only)? Provide sample agent activity logs from past 30 days showing what is captured.

**CNA-01-Q17:** Have you established baseline behavior profiles for AI agents? For each critical agent, describe: (a) normal behavior baseline (typical API calls, frequencies, data volumes, error rates), (b) what constitutes anomaly (unusual API calls, unexpected services accessed, high-volume data transfer), (c) how baselines are updated (static or adaptive learning).

**CNA-01-Q18:** How do you detect anomalies in agent behavior? Describe detection methodology: (a) behavioral baselines vs. current activity, (b) multi-layer detection (network anomalies + identity log anomalies + application-level anomalies), (c) detection accuracy (% of true anomalies detected vs. false positives), (d) detection latency (real-time vs. batch analysis). Provide sample anomaly alerts from past 30 days.

**CNA-01-Q19:** If agent anomaly is detected (unusual API calls, unexpected service access, data exfiltration attempt), what is your automated response? Do you: alert security team, rate-limit agent, block specific actions, isolate agent, revoke credentials? What is detection-to-response time? Provide evidence of automated response from past 12 months with timelines.

**CNA-01-Q20:** Can agents be compromised, jailbroken, or manipulated via prompt injection to exceed authorized scope? Describe detection controls: (a) identify agents with broad permissions (high-risk compromise vectors), (b) monitor for policy escape attempts (agent requesting unauthorized access), (c) validate guardrails enforce constraints. Provide examples of policy escape attempts detected and prevented in past 12 months.

**CNA-01-Q21:** For multi-agent coordination, can one agent call another agent? If yes, describe allowed agent-to-agent interactions. Could a compromised agent weaponize trust chains (Agent A calls Agent B, B calls external API)? How do you prevent unintended trust cascades through agent coordination? Provide agent dependency graph showing all agent-to-agent interactions.

---

## Section 4: Egress Filtering & Data Loss Prevention

**CNA-01-Q22:** Describe your egress filtering architecture. Is egress filtering: (a) deny-by-default (all outbound traffic blocked unless explicitly approved), or permissive (all allowed unless blocked), (b) applied consistently to all workloads or selectively, (c) enforced at network layer (firewall) or application layer (proxy)?

**CNA-01-Q23:** Provide your approved external destination whitelist. How many external domains/IP ranges/ports are approved for outbound traffic? Are approved destinations justified (business necessity documented)? If thousands of destinations approved, is filtering still effective? Describe approval process for adding new egress destinations: automatic, manual security review, risk assessment required?

**CNA-01-Q24:** What is your egress filtering coverage? Percentage of infrastructure covered: 100% or selective (only certain services)? Can you test egress filtering? Provide evidence of tests attempting to exfiltrate data to unauthorized destination; verify blocked. Benchmark: egress filtering coverage 100%; 100% block rate for unauthorized destinations on penetration tests.

**CNA-01-Q25:** Do you have Data Loss Prevention (DLP) deployed for egress traffic? What DLP solution is used (pattern-based, AI-powered semantic understanding, or hybrid)? What types of sensitive data does DLP detect: PII, secrets, proprietary information, financial data, PHI? Is DLP AI-powered (semantic understanding of data sensitivity) or regex-based (credit card patterns)?

**CNA-01-Q26:** Provide DLP detection performance metrics: (a) detection accuracy (% of sensitive data actually detected vs. missed), (b) false positive rate (% of legitimate traffic blocked incorrectly), (c) detection latency (real-time or batch), (d) types of threats detected (DNS tunneling, steganography, API exfiltration, cloud service abuse). Compare to research baselines: AI-DLP achieves 10-15% F1-score improvement over pattern-matching.

**CNA-01-Q27:** Has DLP detected any data exfiltration attempts in the past 12 months? For each detection: (a) what sensitive data type was targeted, (b) detection method (pattern match, behavioral anomaly, semantic analysis), (c) exfiltration destination or method, (d) was data successfully exfiltrated or blocked, (e) incident response and remediation.

**CNA-01-Q28:** How do you prevent AI-assisted exfiltration attacks where agents craft queries to evade DLP? Describe detection controls beyond pattern-matching: (a) behavioral analysis (unusual query patterns, data access patterns), (b) semantic understanding (intent classification, data sensitivity contextualization), (c) rate limiting (excessive queries from single agent), (d) agent-specific egress controls (agent has restricted egress destinations).

**CNA-01-Q29:** Can you demonstrate egress filtering + DLP working together? Provide evidence: (a) architecture diagram showing egress path through firewall then DLP, (b) test results showing: authorized data egress allowed, unauthorized exfiltration blocked by DLP, sensitive data blocked by DLP, (c) logs showing DLP preventing exfiltration attempt from past 12 months.

---

## Section 5: Container Escape Detection & Response

**CNA-01-Q30:** Do you have container escape detection deployed? What solution is used: Falco, Cilium Tetragon, eBPF-PATROL, KubeFence, custom solution, or none? What syscall/kernel-level signals indicate container escape attempts? How frequently is escape detection tested? Provide evidence of tests from past 12 months.

**CNA-01-Q31:** What is the detection capability for container escape? (a) What escape vectors are detected (privileged operations, host filesystem access, namespace breakout, capability abuse), (b) detection accuracy (% of escape attempts detected), (c) detection latency (real-time <1ms, or batch analysis), (d) false positive rate (<5% acceptable). Benchmark: >94% detection accuracy, <1ms overhead for eBPF-based tools.

**CNA-01-Q32:** If container escape is detected, what is your automated response? (a) Isolate container (block all network traffic), (b) pause/terminate container, (c) alert security team, (d) collect forensics (memory dump, process tree). What is detection-to-response time? Can you provide evidence of automated response from past 12 months?

**CNA-01-Q33:** For multi-tenant containerized infrastructure, if one container escapes to the host, can escaped process access other tenants' containers or data? How does network segmentation prevent escaped container from crossing tenant boundary? Provide evidence (test results or incident review) that escaped container cannot reach other tenant's resources due to network policies.

**CNA-01-Q34 (OPTIONAL - Infrastructure Hardening):** Do you use hard isolation for sensitive or high-security workloads (Kata Containers, Firecracker, gVisor, dedicated hosts) in addition to soft isolation (namespaces, cgroups)? If yes, describe which workload categories use hard isolation (customer AI agents, sensitive data processing, admin systems). What is the performance/cost trade-off? [Note: This question overlaps with workload isolation/platform engineering concerns and may be better suited to an infrastructure hardening KSI; retained as optional for reference.]

**CNA-01-Q35:** Have you experienced container escape incidents in the past 12 months? Describe: (a) escape vector (CVE or technique), (b) detection method and time-to-detection, (c) which containers/workloads affected, (d) blast radius (could attacker access host, sibling containers, other tenants?), (e) remediation and process improvements. Were escapes detected by your monitoring tools or discovered through other means?

---

## Section 6: Behavioral Anomaly Detection & Lateral Movement Prevention

**CNA-01-Q36:** How do you detect lateral movement in your infrastructure? What signals indicate lateral movement: (a) unusual service-to-service communication, (b) privilege escalation attempts, (c) access to sensitive data/resources from unexpected services, (d) failed authentication spikes? Describe detection methodology: statistical baselines, graph-based analysis, ML-based modeling, other.

**CNA-01-Q37:** What tools are deployed for lateral movement detection: Falco, Cilium, network observability platforms, SIEM, custom solutions? What is detection accuracy (% of lateral movement attempts detected) and false positive rate (<5% target)? What is mean time to detect (MTTD) lateral movement? Benchmark from research: 85-95% detection accuracy is achievable with graph-based methods; 2% FPR target.

**CNA-01-Q38:** Can you trace request flows across multiple services for incident investigation? Describe distributed tracing capability: (a) can you reconstruct full request path (which services were called, in what order, with what permissions), (b) detection latency (real-time or batch forensics), (c) retention period for request traces (hours, days, months). Provide example of reconstructing lateral movement incident.

**CNA-01-Q39:** Have you detected lateral movement incidents in the past 12 months? For each incident: (a) attack vector (compromised service, credential theft, privilege escalation), (b) detection method and time-to-detection, (c) services/systems lateral movement reached (blast radius), (d) data accessed by attacker, (e) impact severity (availability, confidentiality, integrity), (f) root cause (network segmentation insufficient, monitoring missed it), (g) remediation and process improvements.

**CNA-01-Q40:** What is your incident response time for lateral movement detection? Define SLA: (a) time-to-detect (target: <5 minutes real-time), (b) time-to-investigate (target: <15 minutes with automated tools), (c) time-to-contain (target: <30 minutes isolation of compromised systems), (d) time-to-remediate (full remediation + evidence collection). Provide evidence of response times from past 12 months.

---

## Section 7: Multi-Tenant Isolation

**CNA-01-Q41:** For multi-tenant shared infrastructure, how do you validate tenant isolation continuously? (a) Automated testing attempting cross-tenant access (continuous verification), (b) frequency of penetration testing multi-tenant boundaries (quarterly, annually), (c) have you detected isolation violations in past 12 months (if yes: describe root cause and remediation), (d) provide most recent penetration test report (redacted if necessary) showing isolation held.

---

## Schema Reference

**Question ID Format:** [KSI-CODE]-Q##
Example: CNA-01-Q01

**All questions should be answered with:**
- Direct evidence (not claims)
- Quantifiable data where applicable
- Supporting documentation (architecture diagrams, policies, test results, incident logs)
- AI-specific examples where relevant
- Timeline/frequency information
- Comparison to research benchmarks when available

---

**Version:** 1.1
**Generated:** 2026-01-08
**Reviewed & Filtered:** 2026-01-13
