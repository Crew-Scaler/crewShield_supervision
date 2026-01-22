# Enforce Traffic Flow: Discovery Questions

**KSI Focus:** CNA-03 - Enforce logical network traffic flow controls for all workloads, with emphasis on AI agents and multi-agent systems. Implement service mesh, network policies, traffic shaping, and agent communication protocols to enforce zero-trust microsegmentation and prevent unauthorized data flows.

**Context:** This discovery question set consolidates auditor, CIO, and customer perspectives to assess whether organizations effectively enforce traffic flow for AI agents through service mesh, network policies, intelligent routing, and agent-to-agent communication controls. Questions focus on sub-100ms latency requirements, multi-agent coordination, AI-driven network intelligence, and traffic optimization.

---

## Section 1: Service Mesh Architecture & Performance

**KSI-CNA-03-Q001:** What service mesh architecture is deployed: Istio Ambient (sidecarless), Linkerd (sidecar), Cilium (eBPF), traditional Istio sidecar, or none? Document architecture diagrams showing data plane and control plane components. When was the service mesh last upgraded?

**KSI-CNA-03-Q002:** What is your measured service mesh latency overhead by architecture type? Provide baseline latency (without mesh) and mesh-enabled latency measurements over 90 days, including percentiles (p50, p95, p99). Research validates: Istio sidecar 166%, Linkerd 33%, Istio Ambient 8%, Cilium 99%. For AI agent workloads requiring sub-100ms end-to-end latency, what is your measured overhead and what is your plan to reduce overhead where it exceeds 50% for latency-sensitive agents? For multi-cloud or on-premises deployments, does your service mesh provide portable, infrastructure-agnostic network policies that can be deployed to Kubernetes, VMs, and edge without modification?

**KSI-CNA-03-Q003:** How do you handle service mesh upgrades without downtime? Describe upgrade procedure, testing, and rollback mechanism. Provide evidence of recent upgrades: version change timeline, affected services, impact measurement.

---

## Section 2: AI Agent Communication & Interoperability

**KSI-CNA-03-Q004:** How many AI agents are deployed? For each agent category, describe communication patterns: agent-to-agent, agent-to-service, agent-to-external-API. What protocols are used: HTTP, gRPC, WebSocket, custom?

**KSI-CNA-03-Q005:** Do your agents use standardized communication protocols (Agent-to-Agent Protocol, MCP - Model Context Protocol, other standard)? If yes, which standard and version? If custom protocol, provide specification and security validation documentation.

**KSI-CNA-03-Q006:** For multi-agent systems, how do agents discover peers and services? Document service discovery mechanism: DNS-based, registry-based, other. What is discovery latency (p95) and failure detection time?

**KSI-CNA-03-Q007:** Do agents authenticate each other before communication? Describe agent-to-agent authentication: mutual TLS, JWT, other. Can one agent impersonate another, or are identities cryptographically verified at each hop?

**KSI-CNA-03-Q008:** For agent-to-agent calls, what authorization policies are enforced? Can agent A call any service, or are calls restricted to specific agents/services? Provide example agent-to-agent policy.

**KSI-CNA-03-Q009:** Have you experienced agent communication failures caused by traffic controls (service discovery failures, connection timeouts, protocol mismatches, mesh/policy issues)? For each failure in past 12 months: frequency, impact, root cause, remediation. What is your target uptime for agent communication infrastructure?

---

## Section 3: Network Policies & Microsegmentation (General + Kubernetes)

**KSI-CNA-03-Q010:** What percentage of your services have explicit network policies enforced? For Kubernetes deployments, what percentage of namespaces have default-deny network policies? What mechanisms are used: Kubernetes Network Policies, native K8s Network Policies, service mesh (Istio/Linkerd), Container Network Interface (CNI) plugins (Calico, Cilium, Antrea), firewall rules, or combination? Benchmark: 100% is required for zero-trust; research shows 40% of applications missing policies entirely.

**KSI-CNA-03-Q011:** For each network policy mechanism deployed, what traffic rules can be expressed: IP/port-based (L3/L4), application-level (L7), other? For AI agents, do network policies restrict which services/APIs agents can reach? Provide example policy for agent: "Agent X may call Service Y on /read endpoint but not /write."

**KSI-CNA-03-Q012:** How do you handle dynamic service discovery with network policies? As services are created/destroyed, are policies automatically updated or manually maintained? What is the policy deployment latency for new services?

**KSI-CNA-03-Q013:** For multi-tenant Kubernetes clusters, how do you enforce tenant isolation via network policies? Can tenant A access tenant B's services, or are policies enforced at namespace boundaries? Provide evidence of cross-tenant isolation testing.

**KSI-CNA-03-Q014:** Have network policy misconfiguration incidents occurred in the past 12 months? Describe: what services were affected, how long until detection, impact (unauthorized traffic, legitimate traffic blocked), root cause.

**KSI-CNA-03-Q015:** Can you test network policies? Provide evidence of policy testing: attempt to access service without permission (verify denied), attempt authorized call (verify allowed), penetration test results showing policy enforcement.

**KSI-CNA-03-Q016:** How do you manage network policy complexity at scale? With hundreds/thousands of pods and policies, how do you prevent policy misconfiguration? Document policy management process: manual, automated validation, policy-as-code.

**KSI-CNA-03-Q017:** For CI/CD pipelines, how are Kubernetes deployments validated before reaching production? Do policies include network policy validation (detect missing policies, overly-permissive rules)? Provide evidence of policy validation in CI/CD.

---

## Section 4: Traffic Optimization & QoS for AI Agents

**KSI-CNA-03-Q018:** For AI workloads with sub-100ms latency requirements, what policy-driven traffic control techniques are deployed: traffic shaping, load balancing, traffic prioritization, intelligent routing? Document each technique, the policies that enforce it, and how policy controls these flows rather than just measuring latency.

**KSI-CNA-03-Q019:** Do you implement Quality of Service (QoS) controls for agent traffic via policies? Can you prioritize agent-to-agent communication over background traffic through policy enforcement? Provide evidence of QoS policies and how policy decisions affect traffic prioritization.

**KSI-CNA-03-Q020:** How do you enforce traffic control policies during surge scenarios? With 100+ agents making simultaneous API calls, what policies govern how traffic is controlled and constrained to remain within acceptable bounds? Provide evidence of policy-driven behavior under agent traffic surge, not just performance metrics.

**KSI-CNA-03-Q021:** Do you implement intelligent routing for AI inference workloads via policy? Can the system route inference requests based on policy controls (to the nearest available model server, resource-aware placement)? Document how policies govern routing decisions.

**KSI-CNA-03-Q022:** What is your approach to policy-driven load balancing for agent requests? How do policies control traffic distribution: round-robin, least-connections, weighted, or ML-based traffic prediction informed by policies? Provide evidence of how policies determine load balancing behavior.

---

## Section 5: mTLS Enforcement & Identity Binding to Traffic Flows

**KSI-CNA-03-Q023:** Is mutual TLS (mTLS) enforced for all service-to-service communication? For which traffic is mTLS mandatory (e.g., all traffic, AI agent communication, sensitive services only)? What percentage of internal traffic is encrypted with mTLS? Document where mTLS is used and where it is not, and how identity is bound to traffic control decisions.

**KSI-CNA-03-Q024:** Can you revoke mTLS certificates if a service is compromised? Describe certificate revocation mechanism and propagation time. For AI agents, how quickly can compromised agent credentials be invalidated across all peers to prevent unauthorized traffic?

**KSI-CNA-03-Q025:** For agent-to-agent communication, do you verify service certificate chains to prevent certificate spoofing and unauthorized flows? Document certificate validation procedures. Can one agent impersonate another via certificate tampering?

---

## Section 6: Edge & Distributed AI Infrastructure Traffic

**KSI-CNA-03-Q026:** For distributed AI inference (edge devices, on-prem, cloud), how do you enforce traffic policies across boundaries? If an edge agent calls a cloud service, are those calls authenticated, authorized, and encrypted by the traffic control plane?

**KSI-CNA-03-Q027:** What is the latency SLA for edge-to-cloud agent communication? With geographic distribution, what is typical p99 latency for agent calls crossing data centers? For AI reasoning loops, is latency acceptable?

**KSI-CNA-03-Q028:** How do you handle network partitions between edge and cloud in the traffic control plane? If edge agents become disconnected from cloud services, what happens: queuing of requests, local fallback, agent pause? Provide evidence of partition handling.

---

## Section 7: AI-Driven Traffic Control & Monitoring

**KSI-CNA-03-Q029:** Do you use AI/ML for network intelligence applied to traffic control: traffic anomaly detection, predictive routing, adaptive load balancing? If yes, describe models deployed: how they inform policy decisions, detection accuracy, latency overhead, production validation.

**KSI-CNA-03-Q030:** For traffic anomaly detection, what signals indicate malicious traffic or unauthorized agent communication? Describe detection methodology and policy-driven response (block, alert, restrict, investigate). Provide examples of detected anomalies from past 12 months and how policies were adjusted in response.

---

## Schema Reference

**Question ID Format:** [KSI-CODE]-Q##
Example: CNA-03-Q01

**All questions should be answered with:**
- Direct evidence (not claims)
- Quantifiable data where applicable
- Supporting documentation (architecture diagrams, policies, metrics, test results)
- AI-specific examples where relevant
- Timeline/frequency information
- Comparison to research benchmarks when available

---

**Version:** 2.1 (Task 2 Fine-Tuning Applied)
**Generated:** 2026-01-08
**Last Updated:** 2026-01-13
