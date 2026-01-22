# KSI-IAM-07: Automated Account Management - Question Library

**KSI Title**: Automated Account Management for AI and AI Agents
**FedRAMP Alignment**: KSI-IAM-07, NIST AC-2 (Account Management)
**Document Version**: 2.0
**Last Updated**: January 13, 2026

---

## Executive Summary

This question library addresses automated account lifecycle management in the context of AI agents and non-human identities (NHI). Traditional account management frameworks designed for human-centric environments cannot scale to manage the explosive growth of machine identities (45:1 to 80:1 machine-to-human ratios), ephemeral lifecycles (seconds to minutes), and autonomous provisioning requirements inherent to AI agent deployments.

### Question Statistics

- **Original Question Count**: 85 questions from review phase
- **Task 1 Consolidations**: 5 questions merged, 9 moved to other KSIs → 71 questions
- **Task 2 Fine-Tuning**: 18 additional questions merged through semantic consolidation
- **Final Question Count**: 53 questions

### Coverage Mapping

Questions are organized across nine critical clusters addressing AI-specific account management challenges:

1. Ephemeral Identity Lifecycle and Rapid Credential Management (6 questions)
2. Autonomous Non-Human Identity Proliferation and Discovery (6 questions)
3. Dynamic Privilege Assignment and Just-In-Time Access Control (8 questions)
4. Credential Sprawl and Secrets Management Automation (6 questions)
5. Service Account Governance and Privileged Agent Management (5 questions)
6. Delegation Chain Verification and Multi-Agent Accountability (5 questions)
7. Continuous Authorization and Real-Time Context-Aware Access Control (5 questions)
8. Automated Account Lifecycle Compliance and Audit Evidence Generation (9 questions)
9. Strategic Implementation and Integration (3 questions)

---

## Cluster 1: Ephemeral Identity Lifecycle and Rapid Credential Management

**Focus**: Managing ultra-short-lived AI agent identities requiring dynamic credential issuance and immediate expiration, replacing traditional provisioning workflows designed for months-long human lifecycles.

**KSI-IAM-07-Q1**: What are your current provisioning and deprovisioning timelines for AI agent identities? Specifically: (1) Time from provisioning request initiation to credential delivery (target: sub-second); (2) Deprovisioning lag in days from task completion to full account removal across all systems (target: <1 day); (3) Current count of orphaned agent accounts (failed deprovisioning); (4) How these metrics are monitored and remediated.

**KSI-IAM-07-Q2**: Does your credential vault architecture support machine-speed credential issuance and lifecycle management, including: sub-second latency, 10,000+ concurrent credential generation operations per second, automated lifecycle aligned to agent operation duration, and credential expiration windows of less than one minute?

**KSI-IAM-07-Q3**: What mechanisms detect agent task completion to trigger automatic deprovisioning (time-based expiration, task-completion detection, inactivity detection, explicit requests)? What automated cleanup removes ephemeral identity artifacts (expired certificates, temporary grants, session records)?

**KSI-IAM-07-Q4**: How do you validate that revoked ephemeral credentials are actually rejected across all dependent systems, preventing zombie credentials from remaining valid after claimed revocation? What testing validates credential revocation enforcement?

**KSI-IAM-07-Q5**: What audit logging captures the complete lifecycle of ephemeral agent identities from provisioning through task execution to deprovisioning, including all intermediate state transitions and revocation events?

**KSI-IAM-07-Q6**: What is your current non-human identity orphan account remediation strategy, and how frequently are orphaned accounts identified and cleaned up?

---

## Cluster 2: Autonomous Non-Human Identity Proliferation and Discovery

**Focus**: Managing explosive growth of non-human identities with unclear ownership and governance, requiring specialized discovery and classification beyond traditional human-centric IAM frameworks.

**KSI-IAM-07-Q7**: What percentage of AI agents and non-human identities in your environment have been formally discovered, inventoried, and classified? How frequently do you conduct comprehensive discovery scans for shadow agents outside official provisioning channels? How many additional shadow identities were discovered compared to initial inventory estimates?

**KSI-IAM-07-Q8**: What automated discovery tools scan cloud infrastructure (AWS IAM roles, Azure service principals, GCP service accounts), CI/CD pipelines, development environments, and application code for machine identities? What mechanism correlates results across multiple platforms to prevent duplicates and gaps?

**KSI-IAM-07-Q9**: What is your current non-human identity growth rate (agents added per month) and machine-to-human identity ratio? How have these metrics impacted your identity management platform scalability, and what governance framework adjustments have been implemented?

**KSI-IAM-07-Q10**: How are ownership and accountability established for non-human identities, particularly for agents deployed through automated systems or development pipelines?

**KSI-IAM-07-Q11**: What controls prevent shadow AI agents from being deployed without appearing in the official inventory, and how is inventory completeness validated and enforced?

**KSI-IAM-07-Q12**: What is your non-human identity remediation process for orphaned or unaccounted identities discovered during scans, and what is your target compliance timeline?

---

## Cluster 3: Dynamic Privilege Assignment and Just-In-Time Access Control

**Focus**: Implementing context-aware, just-in-time privilege assignment adapting to changing AI agent task requirements, moving beyond static role-based access control.

**KSI-IAM-07-Q13**: Does your organization implement Attribute-Based Access Control (ABAC) supporting dynamic privilege assignment based on task context, or do you rely on static Role-Based Access Control (RBAC)?

**KSI-IAM-07-Q14**: How do you determine what permissions AI agents require for their operations, and is this analysis automated, manual, or hybrid?

**KSI-IAM-07-Q15**: Do you implement Just-In-Time (JIT) privilege provisioning allowing agents to request temporary elevated privileges that automatically expire after use?

**KSI-IAM-07-Q16**: What controls prevent agents from manipulating context signals (risk scores, data classification, task attributes) to trigger unauthorized JIT privilege elevation?

**KSI-IAM-07-Q17**: How frequently are agent permissions reviewed and adjusted throughout their operational lifecycle, and what is the current cycle time for privilege reviews?

**KSI-IAM-07-Q18**: What is the average permission scope per agent identity measured in number of distinct permissions, and what is your least-privilege target?

**KSI-IAM-07-Q19**: What authorization decision latency can your infrastructure sustain for ABAC and JIT operations, and does it meet the sub-100ms target for machine-speed agent operations?

**KSI-IAM-07-Q20**: How are privilege escalation attempts by agents detected during execution, and what is the typical detection lag from escalation attempt to security response?

---

## Cluster 4: Credential Sprawl and Secrets Management Automation

**Focus**: Addressing proliferation of long-lived static credentials across multiple environments, requiring automated secrets management, rotation, and lifecycle automation for agent identities.

**KSI-IAM-07-Q21**: What percentage of AI agent identities use centralized secrets vault credentials versus static, long-lived credentials such as API keys embedded in code? How many static, never-rotated credentials currently exist in your environment, and what is your documented remediation timeline?

**KSI-IAM-07-Q22**: What automated scanning detects secrets in code repositories, configuration files, and development environments, and how frequently do these scans execute? What procedures ensure environment-specific credential isolation preventing development credentials from being used in production?

**KSI-IAM-07-Q23**: What is your average agent credential lifespan, and how does it compare to the recommended 1-7 day rotation cycle? Are there environments where credentials are shared across multiple agent instances, and what isolation strategy is implemented?

**KSI-IAM-07-Q24**: How quickly can you invalidate compromised credentials across all systems where they were used, and what is your credential compromise response SLA? How is compromise detected through behavioral monitoring or anomaly detection, and what is the average time from compromise to remediation?

**KSI-IAM-07-Q25**: What authentication mechanisms replace long-lived credentials for agent service accounts (certificate-based authentication, workload identity, OIDC federation)?

**KSI-IAM-07-Q26**: What mechanisms compensate for service account limitations such as inability to complete interactive multi-factor authentication challenges?

---

## Cluster 5: Service Account Governance and Privileged Agent Management

**Focus**: Treating AI agents as privileged identities requiring similar rigor as human administrators, addressing service account weaknesses specific to agent operations.

**KSI-IAM-07-Q27**: Are AI agents treated as privileged identities subject to Privileged Agent Access Management (PAAM) controls similar to human administrator accounts?

**KSI-IAM-07-Q28**: How are agent-specific behavioral baselines established and tuned to accommodate high-velocity, variable activity patterns? What enhanced monitoring and audit logging is implemented for agent service accounts compared to standard service accounts?

**KSI-IAM-07-Q29**: How is continuous privilege validation implemented during agent operations to detect unauthorized privilege usage? What time-based access restrictions limit service account operational windows, and how are exceptions managed?

**KSI-IAM-07-Q30**: What incident response procedures enable rapid service account compromise remediation when agents exhibit suspicious behavior?

**KSI-IAM-07-Q31**: What is your privileged agent access management maturity level, and what specific controls are gaps relative to your least-privilege targets?

---

## Cluster 6: Delegation Chain Verification and Multi-Agent Accountability

**Focus**: Establishing cryptographic verification of delegation chains where agents spawn sub-agents or delegate tasks, maintaining end-to-end accountability.

**KSI-IAM-07-Q32**: How are delegation chains cryptographically verified when AI agents spawn sub-agents or delegate tasks to other services? How is delegation legitimacy validated to prevent malicious agents from forging delegation claims?

**KSI-IAM-07-Q33**: What delegation token lifecycle management ensures that delegation authority expires appropriately and cannot be reused beyond intended scope? What automated validation prevents low-privilege agents from escalating privileges through delegation?

**KSI-IAM-07-Q34**: What unified audit logging and traceability tools capture complete delegation chain activities across multi-agent workflows for audit, incident response, and accountability purposes?

**KSI-IAM-07-Q35**: How are delegation chain compromises detected and remediated when a compromised agent propagates malicious actions through its delegations?

**KSI-IAM-07-Q36**: What verification mechanisms ensure that delegation chains maintain end-to-end accountability and cannot be forged or modified in transit?

---

## Cluster 7: Continuous Authorization and Real-Time Context-Aware Access Control

**Focus**: Implementing continuous, real-time authorization throughout agent execution lifecycle rather than point-in-time authentication.

**KSI-IAM-07-Q37**: Does your authorization infrastructure perform continuous authorization validation throughout agent execution, or do you implement point-in-time authorization at login only? Can your system perform mid-session authorization revocation to immediately terminate agent operations if authorization conditions are no longer met?

**KSI-IAM-07-Q38**: How do you integrate real-time context data (risk scores, policy changes, threat intelligence) into authorization decisions for operating agents? What authorization decision latency can your infrastructure sustain (target: <100ms) at scale (100,000+ concurrent validations per second)?

**KSI-IAM-07-Q39**: How are authorization context changes detected and evaluated during agent execution (location changes, data sensitivity transitions, risk score updates)? What anomaly detection identifies unauthorized or suspicious authorization requests?

**KSI-IAM-07-Q40**: What procedures enable authorization revocation during active agent execution without corrupting data or leaving operations in inconsistent states?

**KSI-IAM-07-Q41**: How do you detect and prevent agents from manipulating context signals to trigger unauthorized privilege escalation through legitimate APIs?

---

## Cluster 8: Automated Account Lifecycle Compliance and Audit Evidence Generation

**Focus**: Automating account lifecycle governance, access reviews, deprovisioning validation, and compliance evidence generation at scale.

**KSI-IAM-07-Q42**: What unified audit logging captures complete agent lifecycle events including creation, privilege changes, authorization decisions, revocation, and state transitions? What audit event throughput can your infrastructure sustain (target: 100,000+ events per second)?

**KSI-IAM-07-Q43**: How much manual effort currently goes into collecting compliance evidence for account lifecycle management audits, and what is your target automation level? Can you automatically generate machine-readable compliance evidence demonstrating continuous account lifecycle management aligned to FedRAMP requirements?

**KSI-IAM-07-Q44**: How frequently are access reviews conducted for agent identity populations (automated or manual)? Can you produce on-demand evidence demonstrating account lifecycle compliance status for any point in time during an audit period?

**KSI-IAM-07-Q45**: Do audit trails capture provisioning decision rationale when agents or ML models drive provisioning decisions? How is audit trail integrity maintained to prevent deletion, modification, or tampering with lifecycle event logs?

**KSI-IAM-07-Q46**: What is your audit log retention period for agent lifecycle events, and how does it align with compliance requirements? How are audit trails from cloud service provider identity services integrated with internal logging systems?

**KSI-IAM-07-Q47**: What automated deprovisioning validation ensures agent accounts are properly removed across all systems when no longer needed, and how is removal verified?

**KSI-IAM-07-Q48**: What compliance dashboards provide real-time visibility into account management status, including provisioning rates, deprovisioning lag, orphaned account counts, and overall lifecycle health metrics?

**KSI-IAM-07-Q49**: What is your account lifecycle compliance status score, and what are the top three gaps preventing full KSI-IAM-07 compliance?

**KSI-IAM-07-Q50**: How do you validate audit logging completeness and accuracy across all agent identity lifecycle events?

---

## Cluster 9: Strategic Implementation and Integration

**Focus**: Platform capabilities and architectural integration for AI-agent-scale account management. (CSP-specific governance and procurement questions moved to CMT-01 and CED-02)

**KSI-IAM-07-Q51**: What identity and access management platforms do you currently use for both human and non-human identities, and what AI-agent-specific features do they provide?

**KSI-IAM-07-Q52**: What specific platform capability gaps prevent full KSI-IAM-07 compliance, and what is the priority and timeline for addressing these gaps? What integration mechanisms connect your identity management platform with agent orchestration services (Amazon Bedrock, Azure AI, Google Vertex AI)?

**KSI-IAM-07-Q53**: What is your overall account management automation maturity level, and what is your target state for AI-agent-scale identity governance?

---

## Question Reorganization and Consolidation Summary

### Task 1 Consolidations (Completed)
- Original 85 questions refined to 71 through merger of 5 questions and relocation of 9 to other KSIs
- Focus shifted from general AC-2 coverage to AI-agent-specific account management
- Questions reorganized into 9 thematic clusters
- CSP-specific governance and procurement moved to CMT-01 and CED-02

### Task 2 Fine-Tuning Applied (Current)

**Cluster 1** (9→6 questions): Merged provisioning/deprovisioning metrics (Q1-Q2→Q1), merged cleanup/lifecycle mechanics (Q4-Q6-Q7→Q3), consolidated orphaned account topics
- Q1+Q2: Combined provisioning timing and deprovisioning lag into single composite question
- Q4+Q5+Q6: Merged task completion detection, cleanup processes, and orphaned account metrics
- Q7+Q8: Consolidated credential lifespan and revocation validation
- Net reduction: 3 questions merged

**Cluster 2** (9→6 questions): Consolidated discovery metrics and reporting
- Q10+Q11+Q14: Merged discovery percentage, scan frequency, and gap analysis
- Q15+Q16: Combined growth rate metrics and machine-to-human ratio
- Net reduction: 3 questions merged

**Cluster 3** (8→8 questions): No changes - focus is already tight and specific to JIT/ABAC
- Maintains distinct separation of concerns for privilege model, JIT implementation, and context manipulation

**Cluster 4** (8→6 questions): Consolidated credential management lifecycle
- Q27+Q28: Combined centralized vault usage and static credential counts
- Q29+Q34: Merged secret scanning and environment isolation
- Q31+Q32+Q33: Consolidated credential lifespan, compromise response, and detection mechanisms
- Q39: Moved to Cluster 5 (service account authentication mechanisms)
- Net reduction: 2 questions merged

**Cluster 5** (8→5 questions): Consolidated privileged agent governance
- Q36: Moved from Cluster 4 (service account authentication)
- Q37+Q38: Merged behavioral baselines and monitoring
- Q40+Q41+Q42: Consolidated privilege validation, time restrictions, and incident response
- Net reduction: 3 questions merged

**Cluster 6** (7→5 questions): Consolidated delegation chain mechanisms
- Q43+Q45: Merged cryptographic verification and legitimacy validation
- Q46+Q47: Combined privilege escalation prevention and token lifecycle
- Q44+Q49: Unified audit logging and traceability
- Net reduction: 2 questions merged

**Cluster 7** (7→5 questions): Consolidated continuous authorization mechanisms
- Q50+Q51: Merged continuous validation and mid-session revocation
- Q53+Q54: Combined context change detection and anomaly detection
- Net reduction: 2 questions merged

**Cluster 8** (12→9 questions): Significant consolidation of compliance evidence and audit mechanics
- Q57+Q61: Merged audit logging with event throughput requirements
- Q58+Q59: Combined manual effort and evidence generation automation
- Q60+Q63: Merged access review frequency with compliance status evidence
- Q62+Q65+Q66: Consolidated audit trail content, retention, and CSP integration
- Q64+Q67: Merged integrity maintenance and deprovisioning validation
- Net reduction: 3 questions consolidated

**Cluster 9** (3→3 questions): Renumbered for consistency; added compliance maturity assessment
- Maintains strategic focus on platform capabilities and orchestration integration

### Total Consolidation Summary
- **Questions merged through semantic consolidation**: 18 questions
- **Original Task 1 result**: 71 questions
- **Task 2 result**: 53 questions
- **Total reduction from original**: 85 → 71 → 53 (38% reduction from original)

### Questions Removed and Relocated

**Moved to CMT-01 (Logging and Monitoring)**:
- Original Q075: CSP documented patterns for AI agent account management
- Original Q076: CSP machine-readable compliance evidence capabilities
- Original Q082: Privilege escalation detection through API chaining (monitoring aspect)
- Original Q085: Agent orchestration service interaction monitoring

**Moved to CED-02 (Role-Specific Training)**:
- Original Q077: CSP templates and reference architectures
- Original Q078: Platform evaluation and benchmarking methodology

**Consolidated into Cluster 7**:
- Original Q080: Context signal manipulation detection (now Q056)
- Original Q081-Q084: Removed as duplicative or better handled in Cluster 5/7

### Question Numbering

All questions renumbered from original format (IAM-07-Q001 through IAM-07-Q085) to simplified format (KSI-IAM-07-Q1 through KSI-IAM-07-Q71).

---

## Implementation Notes

### Perspective-Neutral Language

All questions have been reformulated to be perspective-neutral, removing assumptions about stakeholder roles (CIO, Customer, Auditor). Questions focus on technical capabilities and controls rather than how they would be evaluated or assessed by specific roles.

### Cross-KSI References

The following questions reference capabilities also covered in other KSIs:
- **KSI-IAM-07-Q37**: Behavioral baseline tuning relates to KSI-CMT-01 (behavioral monitoring)
- **KSI-IAM-07-Q54**: Anomaly detection connects to KSI-MLA-01 (SIEM and event detection)
- **KSI-IAM-07-Q62**: Audit trail decision rationale relates to KSI-MLA-02 (audit logging)
- **KSI-IAM-07-Q68**: Compliance dashboards interface with KSI-AFR-02 (key security indicators)

### Research Gaps

Current implementation identifies several research gaps where comprehensive solutions remain in progress:
- Ephemeral identity revocation verification at scale
- Agent-driven context manipulation detection mechanisms
- Delegation chain cryptographic verification at machine scale
- Account entitlement validation automation for ML-based provisioning

---
