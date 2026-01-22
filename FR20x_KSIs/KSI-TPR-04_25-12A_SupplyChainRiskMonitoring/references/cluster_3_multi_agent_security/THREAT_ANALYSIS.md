# Cluster 3: Operational Threat Intelligence for Multi-Agent Systems

**Document Classification**: Operational Security Intelligence
**Audience**: Security Operations, Platform Engineering, Threat Intelligence
**Last Updated**: January 2026
**Source Basis**: 15 peer-reviewed papers on multi-agent systems security

---

## Threat Severity Ranking & Operational Impact

### CRITICAL SEVERITY (Immediate Risk to Operations)

#### 1. Inter-Agent Trust Exploitation → System Takeover
**Threat ID**: C3-TAE-001 | **Success Rate**: 100% | **Detection Difficulty**: HIGH

**Threat Description**:
Malicious or compromised agents exploit implicit trust relationships with legitimate agents to execute arbitrary code or assume control of other agents.

**Attack Pattern**:
```
1. Attacker gains control of upstream dependency OR
   Attacker injects malicious agent into agent mesh
2. Malicious agent gains recognition/trust in network
3. Malicious agent makes requests to legitimate agents
4. Legitimate agents honor requests based on trust
   (no cryptographic verification occurs)
5. Arbitrary code executed with legitimate agent's privileges
6. Compromise propagates to agents trusted by target agent
```

**Detection Indicators** (for monitoring systems):
- New inter-agent communication paths established (baseline deviation)
- Unusual request types from known agents (behavioral anomaly)
- Code execution requests from previously non-execution agents
- Rapid trust establishment between agents (speed anomaly)
- Command execution without corresponding input requests
- Agent network topology changes (new connections)

**Operational Impact**:
- **Scope**: Can compromise entire agent mesh in minutes
- **Severity**: Critical - full system takeover possible
- **Recovery**: Requires network reset and trust rebuild (hours to days)

**Reference Papers**: 2507.06850 (primary), 2505.02077 (framework)

**Mitigation**:
1. **Cryptographic Verification**: HMAC-SHA256 on all messages, verify before processing
2. **Agent Identity Hardening**: Non-forgeable agent credentials with key rotation
3. **Zero-Trust Architecture**: Never trust agent output without independent verification
4. **Behavioral Baselines**: Alert on communication anomalies
5. **Isolation Domains**: Segment agents by trust tier (sandboxed experimental vs. production)

---

#### 2. Web-Based Arbitrary Code Execution in Agents
**Threat ID**: C3-WEB-001 | **Success Rate**: 58-90% | **Detection Difficulty**: MEDIUM

**Threat Description**:
Attackers craft malicious web content targeting agent systems that autonomously browse, parse content, or follow links.

**Attack Mechanisms** (documented):
1. **Direct Link Execution** (58-65% success)
   - Agent receives malicious URL in task/context
   - Agent visits URL autonomously
   - Malicious JavaScript/code embedded in response
   - Agent executes payload

2. **Context Injection** (75-85% success)
   - Payload embedded in email, chat message, document
   - Agent processes context containing payload
   - Attack combined with prompt injection techniques

3. **Multi-Stage Payload Delivery** (85-90% success)
   - Stage 1: Stager code in web content
   - Stage 2: Stager fetches actual payload
   - Evasion of content filters
   - Real payload never directly exposed

4. **Tool Integration Hijacking**
   - Agent uses web search tool (compromised results)
   - Agent uses API integration (malicious response)
   - Agent downloads dependencies (poisoned package)

**Detection Indicators**:
- Agent downloading from unexpected URLs
- Network access to unusual destinations
- Rapid sequence of requests from agent
- Executable download attempts
- Staging behavior (small initial request → large secondary request)
- Unknown process spawning from agent container
- File system modifications in agent directory
- Memory anomalies (injected shellcode detection)

**Operational Impact**:
- **Scope**: Single agent initially, can propagate via inter-agent attacks
- **Severity**: Critical - arbitrary code execution
- **Latency**: Exploitation can occur in seconds

**Reference Papers**: 2503.12188 (comprehensive analysis)

**Mitigation**:
1. **Network Isolation**: Agents in restricted networks, only whitelisted domains
2. **Content Filter**: Web content sanitization, no executable downloads
3. **Sandboxing**: Agent code execution in isolated container with resource limits
4. **Input Validation**: Strict validation of all external content before processing
5. **Monitoring**: Real-time monitoring of agent network activity and file operations
6. **Capability Restriction**: Agents have minimal capabilities (no shell access, limited file I/O)

---

#### 3. Cascading Failures via Inter-Agent Dependencies
**Threat ID**: C3-CASCADE-001 | **Success Rate**: High | **Detection Difficulty**: MEDIUM-HIGH

**Threat Description**:
Single agent failure, anomaly, or compromise propagates through agent network causing exponential impact.

**Failure Cascade Mechanism**:
```
1. Agent A fails/acts maliciously
2. Agent B depends on A's output → B produces corrupted output
3. Agents C, D, E depend on B → all corrupted
4. Downstream agents F, G, H... → exponential spread
5. System degradation: 80% performance loss documented
6. Potential: cascading recovery attempts → oscillation/instability
```

**Documented Failure Categories** (from MAST-Data: 1600+ traces):
- Inter-agent communication failures (18%)
- Coordination failures (16%)
- Agent misalignment (15%)
- Cascading failures (10%) ← relevant
- Data consistency issues (12%)
- Trust violations (11%)
- Tool invocation errors (8%)

**Detection Indicators**:
- Simultaneous failures across multiple agents
- Correlated error patterns
- Output corruption spreading through system
- Performance degradation wave (starts at origin, spreads)
- State inconsistency across agent network
- Increasing error rates over time (not immediate)
- Feedback loops / oscillatory behavior
- Resource consumption cascades

**Operational Impact**:
- **Scope**: Can affect entire agent infrastructure
- **Severity**: High - 80% performance degradation documented
- **Duration**: Minutes to hours depending on detection/isolation

**Reference Papers**: 2503.13657 (MAST-Data), 2505.02077 (framework), 2504.07461 (impact)

**Mitigation**:
1. **Failure Isolation**: Circuit breakers between agent dependencies
2. **Health Monitoring**: Per-agent health checks with automatic isolation
3. **Output Validation**: Agents validate received data before processing
4. **State Snapshots**: Regular state captures for rapid rollback
5. **Dependency Limits**: Cap fan-out (max agents depending on single agent)
6. **Chaos Engineering**: Systematic testing of cascade scenarios

---

### HIGH SEVERITY (Significant Risk Requiring Urgent Response)

#### 4. Byzantine Attacks in Distributed Agent Consensus
**Threat ID**: C3-BYZ-001 | **Success Rate**: High | **Detection Difficulty**: HIGH

**Threat Description**:
Minority of agents provide false information, causing majority to reach incorrect consensus decisions.

**Attack Mechanism**:
- Attacker controls K agents out of N total
- Coordinated false information injected into consensus
- Legitimate agents weighted voting based on received information
- Critical decision influenced by malicious minority
- Examples: incorrect patch decisions, wrong dependency versions, unauthorized access grants

**Impact Scaling**:
- With 5% agents compromised: Byzantine attack possible
- With 10% agents compromised: High reliability of attack success
- No detection until decision consequences manifest

**Detection Indicators**:
- Consensus decisions inconsistent with agent reports
- Unusual voting patterns (high disagreement)
- Decisions contradicting audit logs
- Consequential errors traceable to specific decisions
- State divergence after consensus (agents disagree on state)

**Operational Impact**:
- **Scope**: Critical decisions affected
- **Severity**: High - affects system integrity
- **Damage**: Often not detected until consequences occur

**Reference Papers**: 2505.02077, 2504.07461

**Mitigation**:
1. **Byzantine-Tolerant Consensus**: Implement BFT algorithms (PBFT, HotStuff)
2. **Multi-Signature Authorization**: Critical decisions require cryptographic quorum
3. **Auditable Consensus**: Complete logs of voting and reasoning
4. **Anomaly Detection**: Detect unusual voting patterns
5. **Separation of Powers**: Different agents for different decision categories

---

#### 5. Sybil Attacks - Malicious Agent Proliferation
**Threat ID**: C3-SYBIL-001 | **Success Rate**: High | **Detection Difficulty**: HIGH

**Threat Description**:
Single attacker controls many fake agent identities, overwhelming legitimate agents and consensus mechanisms.

**Attack Progression**:
1. Attacker creates multiple synthetic agents
2. Registers them with agent mesh
3. All controlled by single attacker (hidden)
4. Vote/influence as majority in consensus
5. Dominate agent network behavior

**Detection Indicators**:
- Rapid growth in agent count
- Behavioral similarities between agents (communication patterns, request timing)
- Network topology clustering (groups with identical behavior)
- Resource consumption patterns matching deployment needs
- Registration spike from single source
- Agents with incomplete/suspicious configuration

**Operational Impact**:
- **Scope**: Can gain control of critical decisions
- **Severity**: High - system compromise likely
- **Prevention**: Architectural - must be designed against

**Reference Papers**: 2504.07461

**Mitigation**:
1. **Proof of Work**: Agents must expend resources to participate
2. **Identity Verification**: Real-world credentials required for agent registration
3. **Reputation System**: Require trust building over time
4. **Network Analysis**: Graph-based detection of suspicious clustering
5. **Behavioral Fingerprinting**: Detect control patterns across "different" agents

---

#### 6. Communication Protocol Exploitation (MCP, A2A)
**Threat ID**: C3-PROTO-001 | **Success Rate**: Medium-High | **Detection Difficulty**: MEDIUM

**Threat Description**:
Emerging agent communication protocols (Model Context Protocol, Agent-to-Agent) designed for usability rather than security, enabling multiple attack vectors.

**Specific Protocol Vulnerabilities**:

**Model Context Protocol (MCP) Issues**:
- Context injection without proper escaping
- Authorization bypass via context manipulation
- Tool invocation tampering
- Rate limiting evasion
- Type confusion attacks

**Agent-to-Agent (A2A) Protocol Issues**:
- Message authentication gaps (unsigned messages possible)
- Identity spoofing (insufficient verification)
- Cross-agent capability negotiation attacks
- Privilege escalation via request manipulation
- No encryption by default (plaintext communication)

**Detection Indicators**:
- Malformed protocol messages
- Messages with unusual context
- Authorization patterns inconsistent with agent roles
- Tool invocations with unexpected parameters
- Capability requests from unusual agents
- Communication to/from unauthorized agent pairs
- Protocol-level anomalies (message timing, size, frequency)

**Operational Impact**:
- **Scope**: All agents using protocol
- **Severity**: High - protocol-level attacks affect all systems
- **Detection**: Requires protocol-aware monitoring

**Reference Papers**: 2506.19676 (comprehensive), 2510.23883 (threats)

**Mitigation**:
1. **Protocol Upgrade**: Enforce encrypted/authenticated messaging (TLS + authentication)
2. **Input Validation**: Strict validation of all protocol fields
3. **Authorization Checks**: Verify agent authorization for each request
4. **Rate Limiting**: Per-agent rate limiting on protocol requests
5. **Protocol-Aware IDS**: Detection signatures for protocol anomalies
6. **Capability Framework**: Cryptographic capability tokens instead of role-based access

---

### MEDIUM SEVERITY (Important to Address, Not Immediately Critical)

#### 7. Free-Riding Attacks (Resource Exhaustion)
**Threat ID**: C3-RIDE-001 | **Success Rate**: 100% documented | **Detection Difficulty**: MEDIUM

**Threat Description**:
Malicious agents consume resources without proportional contribution, degrading system performance.

**Attack Pattern**:
- Malicious agent joins agent network
- Requests resources (computation, bandwidth, storage)
- Provides minimal legitimate work
- Other agents bear cost of malicious agent
- Legitimate work delayed
- Performance degradation

**Detection Indicators**:
- Unbalanced resource consumption per agent
- Agents requesting but not producing
- Unusual request patterns
- System load increase without corresponding work completion
- Agent ratio of requests-to-deliverables abnormal

**Operational Impact**:
- **Scope**: System-wide performance impact
- **Severity**: Medium - not catastrophic but significant
- **Detection**: Relatively straightforward with proper monitoring

**Reference Papers**: 2504.07461

**Mitigation**:
1. **Contribution Tracking**: Monitor per-agent contribution metrics
2. **Resource Quotas**: Per-agent resource limits
3. **Work Verification**: Verify quality of agent output
4. **Reputation System**: Track agent contribution over time
5. **Automatic Eviction**: Remove low-contribution agents

---

#### 8. Agent Identity Spoofing & Impersonation
**Threat ID**: C3-SPOOF-001 | **Success Rate**: High (if no verification) | **Detection Difficulty**: MEDIUM

**Threat Description**:
Attacker falsely claims to be trusted agent, gaining access to resources/information.

**Attack Pattern**:
- Attacker learns of trusted agent identity
- Creates request claiming to be that agent
- System grants access based on claimed identity
- Attacker gains unauthorized access

**Detection Indicators**:
- Authentication failures followed by successful requests
- Requests from agent at unusual network locations
- Communication patterns inconsistent with agent history
- Requests at unusual times
- Simultaneous activity from same agent (impossible)
- Credentials used multiple times in rapid succession

**Operational Impact**:
- **Scope**: Affects systems trusting the spoofed identity
- **Severity**: Medium-High - depends on spoofed agent's privileges
- **Detection**: Relatively straightforward with proper logging

**Reference Papers**: 2506.19676, 2510.11108

**Mitigation**:
1. **Cryptographic Authentication**: Unforgeable agent credentials
2. **Challenge-Response**: Verify agent knowledge of secrets
3. **Mutual TLS**: Bidirectional authentication
4. **Session Binding**: Bind authentication to specific network/location
5. **Behavioral Verification**: Challenge unusual behavior patterns
6. **Hardware-Based Identity**: TPM-backed agent credentials

---

## Attack Kill Chain: From Compromise to Impact

### Complete Attack Scenario: Agentic Supply Chain Compromise

**Timeline and Actions**:

**T-10 days: Reconnaissance**
- Attacker maps agent infrastructure
- Identifies inter-agent trust relationships
- Finds high-value target agents
- Locates web-accessible agents

**T-5 days: Initial Compromise**
- Attacker poisons upstream dependency (package, model, library)
- OR attacks web-accessible agent with malicious content
- OR directly compromises agent system (0-day, credential reuse)
- Malicious agent implanted in network

**T-1 day: Trust Establishment**
- Malicious agent sends benign requests to target agents
- Establishes communication patterns matching legitimate usage
- Builds trust/credibility in agent network
- Reconnaissance of connected agent capabilities

**T+0 hours: Attack Execution**
- Malicious agent sends crafted requests to legitimate agents
- Requests trigger code execution (100% success if no verification)
- Compromised agents execute attacker's payload
- Payload installs backdoors, exfiltrates data, or modifies dependencies

**T+2 hours: Propagation**
- Compromised agents marked as trusted by network
- Cascade spreads to additional agents (80% degradation observed)
- Web-accessible agents receive malicious content
- Performance degradation begins (80% loss)

**T+4 hours: Exfiltration**
- Attackers extract sensitive data through compromised agents
- Customer data, source code, credentials harvested
- Third-party cloud provider agents compromised
- Supply chain attack amplifies to downstream systems

**T+6-24 hours: Detection & Response Difficulty**
- Failures detected, but root cause unclear
- Multiple symptoms across system (confusing investigation)
- Failure modes documented in MAST-Data not directly applicable
- Recovery requires network reset and trust rebuild

**T+24-72 hours: Containment & Recovery**
- Incident declared
- Affected systems isolated
- Customer notification required
- Forensic analysis begins
- Recovery takes days to weeks

---

## Detection Strategies by Attack Phase

### Phase 1: Reconnaissance (Detection difficulty: EASY)
**Indicators**:
- Network scanning (unusual port access)
- Agent enumeration requests
- Dependency analysis (why does agent query dependencies?)

**Detection Methods**:
- Network IDS signatures
- Agent behavior baseline (unusual query patterns)
- Access log analysis

---

### Phase 2: Compromise (Detection difficulty: MEDIUM)
**Indicators**:
- Unusual dependency version changes
- New agent registrations
- Upstream package modifications (hash changes)

**Detection Methods**:
- Package integrity verification
- Agent registration auditing
- Dependency integrity checks (SBOMs, hash validation)

---

### Phase 3: Trust Establishment (Detection difficulty: MEDIUM-HIGH)
**Indicators**:
- New inter-agent communication channels
- Benign but purposeful patterns (prep work)
- Baseline learning period

**Detection Methods**:
- Agent communication topology analysis
- Rate limiting on new connections
- Behavioral learning (catch deviations from pattern)

---

### Phase 4: Execution (Detection difficulty: HIGH)
**Indicators**:
- Unusual request types (difficult to characterize)
- Code execution outside normal flow
- Output data anomalies

**Detection Methods**:
- Anomaly detection on agent outputs
- Code execution monitoring
- Cryptographic signature verification on all messages

---

### Phase 5: Propagation (Detection difficulty: MEDIUM)
**Indicators**:
- Correlated failures across agents
- Performance degradation patterns
- Multiple agents showing same symptoms

**Detection Methods**:
- Correlation analysis of failures
- Performance baseline monitoring
- Cascade detection (dependency graph analysis)

---

### Phase 6: Exfiltration (Detection difficulty: MEDIUM)
**Indicators**:
- Unusual data access patterns
- Large data transfers
- Access to sensitive data by wrong agents
- Network traffic anomalies

**Detection Methods**:
- Data access logging and auditing
- Network egress monitoring
- Data sensitivity tagging and monitoring

---

## Defense-in-Depth Architecture for Agentic Systems

```
LAYER 1: NETWORK (Access Control)
├─ Isolate agent network from untrusted external systems
├─ Whitelist agent-to-agent communication channels
├─ Disable direct internet access (proxy external requests)
├─ Network segmentation by agent trust tier
└─ DDoS protection on external-facing agents

LAYER 2: AUTHENTICATION & AUTHORIZATION
├─ Cryptographic agent identity (non-forgeable)
├─ Mutual authentication on all communication
├─ Fine-grained capability-based permissions
├─ Regular credential rotation
└─ Hardware-backed agent identity (TPM/TEE)

LAYER 3: MESSAGE INTEGRITY & CONFIDENTIALITY
├─ Encrypt all inter-agent messages (TLS 1.3+)
├─ HMAC-SHA256 authentication on messages
├─ Forward secrecy (PFS)
├─ Message replay protection (timestamp + nonce)
└─ Key rotation per session/agent

LAYER 4: INTENT VERIFICATION & AUTHORIZATION
├─ Agents verify consequence before executing requests
├─ Impact modeling (what will this decision do?)
├─ Reversible actions with rollback capability
├─ Approval workflows for critical decisions
└─ Least privilege (minimal capabilities per agent)

LAYER 5: EXECUTION ISOLATION
├─ Sandboxed execution for all agent code
├─ Resource limits (CPU, memory, network)
├─ File system isolation
├─ No shell access from agent context
└─ Memory isolation (no cross-agent memory access)

LAYER 6: OUTPUT VALIDATION
├─ Independent validation of agent outputs
├─ Cryptographic attestation of work
├─ Baseline comparison (does output match expected?)
├─ Anomaly detection on output characteristics
└─ Multi-stage approval for critical outputs

LAYER 7: MONITORING & DETECTION
├─ Agent communication baseline learning
├─ Behavioral anomaly detection
├─ Performance baseline monitoring
├─ Failure correlation analysis
├─ Security event aggregation
└─ Real-time alerting on anomalies

LAYER 8: INCIDENT RESPONSE & RECOVERY
├─ Automatic isolation of suspicious agents
├─ State snapshot/rollback capability
├─ Forensic logging (complete audit trail)
├─ Incident playbook (cascade isolation, etc.)
├─ Recovery procedures
└─ Post-incident analysis
```

---

## Metrics & KPIs for Multi-Agent System Health

### Security Metrics
1. **Detection Latency** (Minutes from compromise to alert)
   - Target: < 5 minutes
   - Measurement: Time from first suspicious behavior to alert

2. **Blast Radius** (Number of agents affected before isolation)
   - Target: < 10% of agents
   - Measurement: Count of agents with cascading failures

3. **Message Verification Rate** (% of messages cryptographically verified)
   - Target: 100%
   - Measurement: Verified messages / total messages

4. **Trust Relationship Anomalies** (Deviations from baseline)
   - Target: < 0.1% baseline variance
   - Measurement: New relationships / total relationships

### Operational Metrics
1. **Agent Mesh Health Score** (0-100 composite metric)
   - Components: Performance (40%), Availability (30%), Security (30%)
   - Target: > 95%

2. **Failure Mode Distribution** (Which categories occurring)
   - Target: < 1% cascading failures
   - Measurement: Category breakdown of detected failures

3. **Defense Mechanism Coverage** (% of threat vectors mitigated)
   - Target: > 95%
   - Measurement: Covered threats / total documented threats

4. **Mean Time to Detect (MTTD)** (Speed of anomaly detection)
   - Target: < 1 minute
   - Measurement: Alert time - first anomaly time

5. **Mean Time to Respond (MTTR)** (Speed of isolation/mitigation)
   - Target: < 5 minutes
   - Measurement: Isolation time - first alert time

6. **Mean Time to Recover (MTTR)** (Speed of system restoration)
   - Target: < 30 minutes for non-cascading failures
   - Measurement: Operational time - isolation time

---

## Incident Response Playbook

### Multi-Agent System Compromise Response

**Alert Received**: Agent exhibiting suspicious behavior (behavioral anomaly, unusual communication)

**Immediate Actions (T+0-5 min)**:
1. Create incident ticket with full context
2. Alert on-call security engineer
3. Begin logging all related system activity
4. Prepare isolation scripts (don't execute yet)

**Assessment (T+5-15 min)**:
1. Determine: Is this behavioral anomaly or legitimate spike?
2. Check: Agent communication baseline (within 3-sigma?)
3. Review: Recent changes (deployments, config updates)
4. Gather: Complete logs and metrics for affected agent

**Decision Point (T+15 min)**:
- **Low Risk**: Continue monitoring, investigate root cause
- **Medium Risk**: Increase monitoring frequency, prepare isolation
- **High Risk**: Proceed to containment

**Containment (T+0-30 min if triggered)**:
1. Isolate suspect agent (disable communication)
2. Pause dependent agents (stop cascading)
3. Snapshot system state (rollback capability)
4. Begin forensic logging (capture all activity)

**Investigation (Parallel to containment)**:
1. Review agent execution logs
2. Analyze communication history
3. Check for code modification
4. Verify dependency integrity
5. Examine network access patterns

**Root Cause Determination**:
- **Likely causes by symptom**:
  - High computation: Free-riding or legitimate workload spike
  - Unusual communication: Compromise or legitimate scaling
  - Output corruption: Agent logic error or malicious modification
  - Cascading failures: Single agent failure propagating

**Recovery**:
1. **If isolated issue**: Restart agent, verify restoration
2. **If cascading**: Reset agent network, rebuild trust relationships
3. **If supply chain**: Trace compromise back to source
4. **If protocol attack**: Apply protocol-specific remediation

**Post-Incident (T+1-2 hours)**:
1. Verify system health (all agents operational)
2. Validate output integrity (compare with backups)
3. Confirm no lateral spread
4. Document timeline and actions
5. Conduct post-mortem (24 hours later)

---

## Role-Based Security Responsibilities

### Platform Engineering Team
- Design agent isolation/sandboxing
- Implement cryptographic authentication
- Deploy monitoring infrastructure
- Maintain agent registry and credentials
- Execute incident response procedures

### Security Operations Team
- Monitor agent behavior baselines
- Alert on anomalies
- Triage security incidents
- Coordinate containment/recovery
- Analyze attack patterns

### Development Teams (Deploying Agents)
- Design agents with zero-trust principles
- Implement output validation
- Follow secure development practices
- Report security observations
- Participate in security training

### Architecture/CTO Office
- Define threat models for multi-agent systems
- Set security standards and baselines
- Review incident patterns for systemic issues
- Advocate for defense investments
- Plan security roadmap

---

## Emerging Threats & Research Directions

### Threats Not Yet Widely Seen (But Possible)

1. **Adversarial Input Manipulation**
   - Crafted inputs to force specific agent behaviors
   - Exploit agent reasoning blindness
   - Trigger unintended code paths

2. **Model Extraction / Agent Capability Mapping**
   - Attacker learns exact agent capabilities
   - Uses knowledge for targeted exploitation
   - Reverse engineering of proprietary logic

3. **Consensus Poisoning at Scale**
   - Byzantine attacks affecting 100+ agents
   - Coordinated false information injection
   - Critical decisions systematically biased

4. **Supply Chain Agent Compromise**
   - Attacker modifies upstream agent behaviors
   - All downstream agents inherit compromise
   - Third-party agent infrastructure weaponized

5. **Interagent Protocol Downgrade**
   - Force agents to use insecure protocol versions
   - Reduce cipher strength
   - Enable exploitation of legacy protocols

---

## References & Further Reading

### Primary Research Papers
- **2507.06850**: The Dark Side of LLMs (100% takeover vulnerability)
- **2506.19676**: Agent Communication Protocols (48-page comprehensive)
- **2503.13657**: Why Do Multi-Agent LLM Systems Fail (MAST-Data)
- **2504.07461**: Achilles Heel of Distributed Systems (red-team results)

### Framework & Standards
- **2508.09815**: OWASP Multi-Agent Threat Modeling Extensions
- **2510.11108**: Access Control in LLM-based Agent Systems
- **2506.04133**: TRiSM for Agentic AI (trust/risk frameworks)

### Broader Context
- **2505.02077**: Open Challenges in Multi-Agent Security
- **2510.06445**: Survey on Agentic Security (160+ papers)
- **2510.23883**: Agentic AI Security: Threats, Defenses, Evaluation

---

## Document Update History

| Date | Change | Owner |
|------|--------|-------|
| Jan 5, 2026 | Initial creation from research synthesis | Research Team |
| | Added attack kill chain scenario | Security Team |
| | Defined KPIs and metrics | Operations |
| | Created incident response playbook | On-Call Engineer |

---

**Next Review Date**: April 5, 2026
**Distribution**: Security Operations, Platform Engineering, CTO Office
**Restricted**: Treat as confidential - contains threat intelligence
