# KSI-CNA-08: Automated Enforcement - Question Library

**KSI Reference:** KSI-CNA-08_25-12A_AutomatedEnforcement
**KSI Title:** Cloud Native Architecture - Automated Enforcement
**Generated:** January 13, 2026
**Status:** Refined per GitHub Issue #61

---

## Executive Summary

This question library supports assessment of KSI-CNA-08 compliance, which requires Cloud Service Providers to deploy automated systems that persistently assess the security posture of all machine-based information resources and automatically enforce their intended operational state.

**Processing Statistics:**
- Original question count: 102 (89 original + 13 from refinement)
- Questions moved to other KSIs: 10
  - To KSI-AFR-09: 4 (evidence/governance focus)
  - To KSI-MLA-05: 2 (supply chain governance)
  - To KSI-CMT-03: 3 (remediation testing)
  - To KSI-CMT-01: 3 (activity monitoring/logging)
- Questions consolidated: 8 (false positives, evidence mapping)
- Questions removed: Q101-Q102 (moved to dedicated AI KSI questions)
- Final question count: 82 (core CNA-08 automated enforcement focus)

**Key Focus Areas:**
- AI-native identity controls and agent governance
- Continuous posture assessment and drift detection
- Automated remediation with context-aware enforcement
- AI supply chain security in enforcement context
- Runtime behavioral monitoring and guardrails
- Policy conflict and enforcement cascade management

---

## Core CNA-08 Questions: Automated Enforcement Focus

All questions are presented in perspective-neutral format suitable for any stakeholder role (CIO, Customer, Auditor).

### Section 1: Identity & Access Control for AI Agents

**KSI-CNA-08-Q001** - AI Agent Inventory and Authorization Scope
Maintain a comprehensive inventory of all AI agents deployed in production environments. What percentage of agents are tracked in centralized governance systems? What authorization scopes and resource access permissions are documented for each agent?

**KSI-CNA-08-Q002** - AI-Native Identity Controls
Implement identity systems that distinguish AI agent principals from human principals, enabling distinct policy enforcement. Do identity systems support dynamic trust scoring based on behavioral analytics? What behavioral signals influence trust scores?

**KSI-CNA-08-Q003** - Privilege Scope Validation
What is the current average privilege scope per AI agent? Have audits identified agents with excessive permissions relative to operational requirements? What remediation occurs when scope misalignment is detected?

**KSI-CNA-08-Q004** - Inter-Agent Trust Verification
Implement verification mechanisms validating trust relationships between AI agents. What controls prevent unauthorized inter-agent permission escalation? How are chained permission accumulation patterns detected?

**KSI-CNA-08-Q005** - Attribute-Based Access Control (ABAC) for Agents
Implement ABAC policies adjusting agent permissions based on task context, data sensitivity levels, operational load, and behavioral risk scores. What dimensions inform permission decisions? Are baseline permissions static or adaptive?

### Section 2: Automated Enforcement System Capabilities

**KSI-CNA-08-Q006** - Continuous Assessment Frequency
How frequently do automated enforcement systems assess cloud resource security posture? What is the target assessment interval (real-time, minutes, hours, daily)? How does frequency vary by resource type or risk level?

**KSI-CNA-08-Q007** - Policy-as-Code Implementation
What percentage of security policies have been translated into executable policy-as-code rules? Are policies coded at network level, API level, infrastructure level, or across multiple dimensions? What coverage gaps remain?

**KSI-CNA-08-Q010** - Remediation Action Approval Gates
Implement approval gates for high-impact enforcement actions or configure automatic remediation execution. How are approval decisions tracked and audited? What high-risk actions require human approval before execution?

### Section 3: Continuous Assessment & Monitoring

**KSI-CNA-08-Q057** - Assessment Persistence
Conduct continuous assessment of cloud resource security posture or rely on periodic assessments. If periodic, what is the assessment frequency? How is continuous assessment prioritized for highest-risk resources?

**KSI-CNA-08-Q058** - Real-Time Violation Detection
Are policy violations detected and reported in real-time, or identified batch-style at intervals? What is the target detection latency? How does this latency vary by violation severity?

**KSI-CNA-08-Q059** - Assessment Tool Coverage
Do automated assessment tools cover all machine-based information resources, or are certain resource types excluded? If excluded, what is the justification? What visibility gaps require compensating controls?

**KSI-CNA-08-Q060** - Infrastructure-as-Code Assessment
Do assessment tools evaluate infrastructure-as-code definitions for compliance, or only evaluate running infrastructure? How are drifts between code and runtime detected and enforced?

**KSI-CNA-08-Q061** - Ephemeral Resource Tracking
Do assessment tools track ephemeral resources (short-lived containers, serverless functions) with the same persistence as long-lived infrastructure? What is the minimum visibility window for ephemeral resources?

### Section 4: AI-Specific Compliance Validation

**KSI-CNA-08-Q062** - AI Resource Discovery
What percentage of AI resources (models, training pipelines, inference endpoints, vector databases) are discovered and included in continuous assessment? Are any resource types missing from inventory? What processes ensure comprehensive discovery?

**KSI-CNA-08-Q063** - Model Configuration Assessment
Do assessment tools validate AI model serving configurations? Can they distinguish between intentional configuration deviations (performance optimization) and security misconfigurations? What analysis techniques enable this distinction?

**KSI-CNA-08-Q064** - Training Pipeline Security
Are training pipeline configurations continuously assessed? Do assessment tools validate that training data sources are approved and that models are trained with clean, unmodified data? How is training data integrity verified?

**KSI-CNA-08-Q065** - Agent Permission Compliance
Are AI agent permission scopes continuously validated to ensure agents hold minimum necessary permissions? How frequently are permission audits conducted? What triggers remediation for permission creep?

**KSI-CNA-08-Q066** - Model Integrity Validation
Do assessment tools validate that deployed models are signed by approved providers? Can they detect unsigned or invalidly signed models? What enforcement occurs when model integrity cannot be verified?

### Section 5: Control Design & Implementation

**KSI-CNA-08-Q052** - Automated Enforcement Policy Documentation
Provide documentation of all policies implemented in automated enforcement systems. Are policies documented in natural language, policy-as-code, or both? How is policy documentation kept current?

**KSI-CNA-08-Q053** - Policy Update Change Management
Define formal change management processes for updating automated enforcement policies. Are policy changes subject to approval, testing, and documentation requirements? Who authorizes policy changes?

**KSI-CNA-08-Q054** - Control Effectiveness Testing
How frequently are automated enforcement controls tested to validate they operate as designed? What testing methodology is used (automated testing, manual sampling, simulation)? What frequency is acceptable?

**KSI-CNA-08-Q055** - Segregation of Duties
Segregate responsibilities for policy definition, policy implementation, remediation execution, and enforcement monitoring across different teams. How is this segregation enforced? Are exceptions documented and justified?

**KSI-CNA-08-Q056** - Configuration Change Authorization
Subject all configuration changes to automated enforcement systems to formal authorization. What is the approval workflow? Who can authorize changes and under what conditions?

### Section 6: Remediation Quality & Safety

**KSI-CNA-08-Q077** - Remediation Effectiveness Rate
What percentage of detected policy violations are successfully remediated on first attempt? How often does remediation require manual intervention or rollback? What factors cause remediation failures?

**KSI-CNA-08-Q079** - Remediation Rollback Capability
When remediation actions cause service disruptions or introduce new vulnerabilities, execute rollback procedures. What is the rollback time objective? How are rollback capabilities tested and validated?

**KSI-CNA-08-Q080** - Unintended Consequence Detection
Implement monitoring detecting when enforcement actions trigger cascading failures or unintended consequences. How are these detected and reported? What escalation occurs when cascades are detected?

**KSI-CNA-08-Q081** - Remediation Documentation
Document all executed remediation actions. Can remediation action records be accessed showing what was changed, why, when, and by what system/approval? How long is remediation history retained?

### Section 7: Supply Chain Security in Enforcement

**KSI-CNA-08-Q021** - Model Integrity Verification
Implement cryptographic signing requirements for AI models. Can you detect unsigned or invalidly signed models deployed into production? What enforcement prevents deployment of unsigned models?

**KSI-CNA-08-Q022** - Framework & Library Vulnerability Scanning
Conduct automated scanning for AI framework and library vulnerabilities using specialized vulnerability databases covering ML-specific components. What is the detection latency? How is scanning integrated into enforcement?

**KSI-CNA-08-Q023** - Supply Chain Compromise Exposure
What is the average time between when a critical vulnerability is published for an ML framework or library and when you detect its presence in your environment? How does this timeline affect remediation decisions?

### Section 8: Agent-to-Agent Interaction Security

**KSI-CNA-08-Q025** - Inter-Agent Communication Monitoring
Monitor communications between AI agents to detect privilege escalation attempts. What controls prevent agents from executing unauthorized commands requested by peer agents? How are inter-agent interactions logged?

**KSI-CNA-08-Q026** - Agent Permission Chaining Detection
Detect when AI agents accumulate permissions across multiple services through chained access patterns. What controls prevent agents from reaching privilege levels exceeding their intended operational scope? How is permission chaining detected and blocked?

### Section 9: Compliance & Risk Management

**KSI-CNA-08-Q027** - Current Compliance Status
Provide evidence demonstrating current compliance with KSI-CNA-08 automated enforcement requirements. Is this evidence available continuously or only during audit periods? What compliance metrics are tracked and reported?

**KSI-CNA-08-Q028** - Enforcement Effectiveness Metrics
Publish metrics demonstrating automated enforcement effectiveness: policy violation detection rates, remediation success rates, false positive rates, and time-to-remediation for compliance violations. What is the baseline for each metric?

**KSI-CNA-08-Q029** - Incident Detection Time
What is the documented average time between when a security misconfiguration occurs and when automated enforcement systems detect and alert on it? How does this compare to organizational risk tolerance?

**KSI-CNA-08-Q030** - Service Disruption from Enforcement
Track instances where automated enforcement triggered unintended service disruptions. If disruptions occurred, how frequently did they occur and what was the impact scope? What preventive measures are implemented?

**KSI-CNA-08-Q031** - Enforcement-Related Outages
Provide incident reports documenting any service outages caused by automated remediation actions. What preventive measures have been implemented to avoid recurrence? How are similar incidents prevented?

### Section 10: AI-Specific Enforcement & Governance

**KSI-CNA-08-Q032** - AI Agent Authorization Process
Define processes for authorizing new AI agents to operate in production. What approval workflow is required before agents gain access to systems and data? Who approves agent deployments?

**KSI-CNA-08-Q033** - AI Agent Permission Boundaries
Define maximum permission boundaries for AI agents. Are limits enforced at the system level? Can agents exceed boundaries under any circumstances? How are boundary violations detected?

**KSI-CNA-08-Q034** - AI Agent Activity Visibility
Provide visibility into AI agent activity. Can you determine which agents accessed which resources and when? What granularity of agent activity logging is implemented?

**KSI-CNA-08-Q035** - Model Provenance Requirements
Enforce requirements that production AI models must have documented provenance showing origin and training data sources. Are unsigned or unknown-origin models blocked? What is the enforcement mechanism?

**KSI-CNA-08-Q036** - Model Poisoning Protection
Implement mechanisms to detect or prevent model poisoning attacks. How do you validate that production models haven't been tampered with? What detection techniques are used?

### Section 11: AI Supply Chain & Third-Party Components

**KSI-CNA-08-Q037** - Third-Party Model Dependencies
Maintain an inventory of third-party ML models and libraries used by AI systems. Are these dependencies scanned for security vulnerabilities? What is the scanning frequency and coverage?

**KSI-CNA-08-Q038** - Framework Vulnerability Response
When security vulnerabilities are published for ML frameworks (TensorFlow, PyTorch, etc.), what is the process for notification, assessment, and remediation? How long is the average remediation window?

**KSI-CNA-08-Q039** - Supply Chain Incident Response
If a supply chain component (model, library, framework) is compromised, how quickly can affected systems be identified? What is the average detection and notification time?

**KSI-CNA-08-Q040** - Signed Model Requirements
Enforce requirements to use only cryptographically signed models from approved sources. What happens if an unsigned model is deployed? How is this enforcement automated?

**KSI-CNA-08-Q041** - Continuous Supply Chain Monitoring
Continuously monitor the security posture of ML frameworks and third-party models in use. Are supply chain security assessments periodic or continuous? What metrics are tracked?

### Section 12: Visibility & Transparency

**KSI-CNA-08-Q047** - Enforcement Dashboard
Provide real-time visibility into current compliance status, detected policy violations, and enforcement actions taken. What information is presented in enforcement dashboards? How frequently is dashboard data updated?

**KSI-CNA-08-Q050** - Transparency Reports
Publish transparency reports documenting automated enforcement actions, statistics on violations detected and remediated, and enforcement-related incidents. What is the publication frequency? What metrics are included?

**KSI-CNA-08-Q051** - SLA for Compliance
Document Service Level Agreements for automated enforcement availability, policy violation detection latency, and remediation completion time. What are the specific SLA targets? Are SLAs contractual or best-effort?

### Section 13: False Positive & Enforcement Safety (Consolidated)

**KSI-CNA-08-Q009** - False Positive Management and Impact Analysis
Track false positive rates on policy violation detection with baselines established for AI infrastructure contexts. Have false positive enforcement actions caused service disruptions? What proportion of enforcement-related incidents were false positives? What is the documented false positive rate? How is false positive impact measured and mitigated?

**KSI-CNA-08-Q043** - Context-Aware Enforcement and Validation
When automated enforcement systems flag potential policy violations, ensure they understand operational context for AI workloads and can distinguish between legitimate AI configurations and genuine security risks. Based on sampled enforcement actions, do automated systems demonstrate evidence of understanding operational context and making appropriately nuanced enforcement decisions?

**KSI-CNA-08-Q044** - Rollback and Safety Procedures
When automated enforcement actions introduce new vulnerabilities or cause system disruptions, execute rollback procedures promptly. What is the defined process and timeline for rolling back enforcement actions? How quickly can rollback occur in practice?

**KSI-CNA-08-Q046** - Change Notification and Staging
When deploying new automated enforcement rules or updating existing rules, notify affected systems in advance. Can systems test new rules in staging environments before production deployment? What advance notice period is provided?

### Section 14: Compliance Gap Identification

**KSI-CNA-08-Q082** - Control Gaps in Traditional Infrastructure
Identify gaps between required automated enforcement and implemented capabilities in traditional cloud infrastructure (non-AI). What compensating controls are in place for these gaps? How effective are compensating controls?

**KSI-CNA-08-Q083** - Control Gaps in AI Infrastructure
Identify gaps between KSI-CNA-08 requirements and actual capabilities in AI infrastructure automation. What compensating controls address these gaps? How is gap remediation prioritized?

**KSI-CNA-08-Q084** - Visibility Gaps
Identify machine-based information resource categories for which continuous automated assessment is not feasible. What alternative control approaches address these resources? How are gaps documented and managed?

**KSI-CNA-08-Q085** - Enforcement Capability Limitations
Identify policy requirements that cannot be enforced automatically with acceptable false positive rates. For these policies, what manual or alternative controls compensate? How frequently are limitations reassessed?

**KSI-CNA-08-Q086** - Supply Chain Assessment Gaps
Identify components in AI supply chain that cannot be continuously assessed (closed-source models, proprietary frameworks, third-party services). How are security risks in these components managed? What alternative controls are implemented?

### Section 15: Risk & Control Effectiveness

**KSI-CNA-08-Q087** - Control Effectiveness Evidence
Provide statistical evidence demonstrating that automated enforcement controls are reducing security risks. What metrics evidence this effectiveness? What baseline and improvement trends are documented?

**KSI-CNA-08-Q088** - Control Failure Impact
When automated enforcement controls fail or are bypassed, what is the potential impact scope? Have any control failures been detected during the audit period? What remediation occurred?

**KSI-CNA-08-Q089** - Emerging Threat Coverage
Ensure automated enforcement controls address emerging threats including AI-specific attacks (prompt injection, model poisoning, inter-agent privilege escalation). Do controls focus primarily on traditional cloud misconfigurations or address AI-specific threats?

**KSI-CNA-08-Q090** - Control Blind Spots
Identify known attack vectors against cloud resources that automated enforcement systems cannot detect. If such vectors exist, what alternative controls provide protection? How frequently are blind spots reassessed?

**KSI-CNA-08-Q091** - Control Sustainability
Based on deployment plans, assess whether the current automated enforcement system will remain effective as AI deployments expand and new attack vectors emerge. What is the roadmap for control evolution?

### Section 16: Policy Conflict and Enforcement Cascade Management

**KSI-CNA-08-Q092** - Policy Conflict Resolution
When multiple automated enforcement policies apply to the same resource and conflict with each other, what resolution mechanism determines which policy takes precedence? How are conflicts logged and reviewed? What escalation occurs for unresolved conflicts?

**KSI-CNA-08-Q093** - Enforcement Cascade Detection
Monitor for enforcement cascades where one automated remediation action triggers additional policy violations requiring further remediation. How are cascades prevented or contained? What is the maximum permitted cascade depth?

**KSI-CNA-08-Q094** - Multi-Agent Policy Coordination
When multiple AI agents operate on shared infrastructure, coordinate policy enforcement to prevent conflicting remediation actions. How do automated systems detect and resolve conflicts? What override mechanisms exist?

### Section 17: Agent Behavior and Runtime Enforcement

**KSI-CNA-08-Q095** - Goal Misalignment Detection
Detect goal misalignment where AI agents access systems that are individually permitted but collectively indicate deviation from intended behavior. What triggers investigation or intervention? How is collective behavior analyzed across agents?

**KSI-CNA-08-Q096** - Runtime Guardrail Effectiveness
Measure the percentage of unsafe agent actions successfully blocked by runtime guardrails before execution. How is guardrail effectiveness measured and improved? What unsafe actions are most frequently blocked?

**KSI-CNA-08-Q097** - Agent Lateral Movement Detection
Detect lateral movement patterns where AI agents rapidly pivot across multiple accounts or services. What is the detection time objective? How are lateral movement patterns distinguished from legitimate access patterns?

### Section 18: Advanced AI Threat Detection

**KSI-CNA-08-Q098** - Adversarial Input Detection
Include detection mechanisms for adversarial inputs targeting AI model inference endpoints in automated enforcement. How are detected attacks handled? What is the response time for blocking adversarial inputs?

**KSI-CNA-08-Q099** - Model Inversion Attack Detection
Implement monitoring detecting model inversion attempts where attackers use agents to reverse-engineer proprietary models through repeated queries. How are inversion patterns detected? What threshold triggers intervention?

**KSI-CNA-08-Q100** - Training Data Exfiltration Detection
Detect attempts to exfiltrate training data or model weights through authorized agent access patterns that appear individually legitimate but collectively indicate data theft. How is collective behavior analysis performed? What is the detection latency?

---

## Organization by Assessment Priority

### Tier 1: Critical Foundation (Must-Have for Basic Compliance)
KSI-CNA-08-Q001, KSI-CNA-08-Q006, KSI-CNA-08-Q007, KSI-CNA-08-Q027, KSI-CNA-08-Q052, KSI-CNA-08-Q057, KSI-CNA-08-Q062

### Tier 2: AI-Specific Controls (Essential for AI Infrastructure)
KSI-CNA-08-Q002, KSI-CNA-08-Q004, KSI-CNA-08-Q017, KSI-CNA-08-Q018, KSI-CNA-08-Q032, KSI-CNA-08-Q035, KSI-CNA-08-Q063, KSI-CNA-08-Q064, KSI-CNA-08-Q065

### Tier 3: Supply Chain and Advanced Threats (Comprehensive Security)
KSI-CNA-08-Q021, KSI-CNA-08-Q022, KSI-CNA-08-Q025, KSI-CNA-08-Q026, KSI-CNA-08-Q037, KSI-CNA-08-Q039, KSI-CNA-08-Q089, KSI-CNA-08-Q095, KSI-CNA-08-Q098, KSI-CNA-08-Q099, KSI-CNA-08-Q100

### Tier 4: Operational Excellence (Mature Implementation)
KSI-CNA-08-Q009, KSI-CNA-08-Q010, KSI-CNA-08-Q043, KSI-CNA-08-Q044, KSI-CNA-08-Q054, KSI-CNA-08-Q092, KSI-CNA-08-Q093, KSI-CNA-08-Q096

---

## Cross-References to Moved Questions

**Moved to KSI-AFR-09 (Persistent Validation):**
- Evidence freshness and continuous evidence generation (originally Q011, Q014, Q067)
- Governance drift detection and monitoring (originally Q013)

**Moved to KSI-MLA-05 (Configuration Evaluation):**
- ML supply chain inventory governance (originally Q020)
- Third-party model security assessment governance (originally Q024)

**Moved to KSI-CMT-03 (Automated Testing & Validation):**
- Automated remediation testing before deployment (originally Q008, Q045, Q078)

**Moved to KSI-CMT-01 (Log and Monitor Changes):**
- AI agent activity monitoring and baselines (originally Q015, Q016)
- Enforcement audit trail and change tracking (originally Q071)

**Removed Questions:**
- CNA-08-Q101, CNA-08-Q102 (concept drift in monitoring models, federated anomaly detection) - moved to dedicated AI monitoring/governance KSI

---

## Cross-References to Other KSIs

**KSI-CNA-02 (Attack Surface Management):** Questions Q001, Q004, Q025, Q026 address attack surface reduction through agent governance

**KSI-CNA-07 (Best Practices):** Questions Q007, Q052, Q053 validate that enforcement aligns with documented best practices

**KSI-CMT-03 (Automated Testing & CI/CD):** Referenced questions on remediation testing before deployment

**KSI-CMT-01 (Log and Monitor Changes):** Referenced questions on logging of enforcement actions and agent activity

**KSI-AFR-09 (Persistent Validation):** Referenced questions on continuous validation requirements and evidence freshness

**KSI-MLA-05 (Configuration Evaluation):** Referenced questions on configuration assessment and supply chain governance

---
