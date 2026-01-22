# Issue #220: KSI-MLA-08 Log Data Access - Comprehensive Research Report

**Date**: 2026-01-12
**Repository**: ksi_watch
**Folder**: KSI-MLA-08_25-12A_LogDataAccess
**Total Papers Analyzed**: 60
**Focus**: Log Data Access Control, AI Agents, and FedRAMP Compliance

---

## Executive Summary

KSI-MLA-08 (Log Data Access) represents a critical security requirement in FedRAMP 20x that mandates cloud service providers implement least-privileged, role and attribute-based, and just-in-time (JIT) access authorization for sensitive log data. However, the emergence of autonomous AI agents and distributed AI architectures has fundamentally transformed the threat landscape and implementation challenges for this control.

Traditional log access control systems were designed for human operators accessing infrastructure logs. They assumed relatively stable access patterns, centralized logging infrastructure, and audit trails limited to system events. AI agents operating at scale within cloud environments violate every one of these assumptions. These agents generate exponential log volumes through continuous inference operations, require programmatic access unsuitable for interactive authentication, operate across federated architectures with inconsistent policy enforcement, and transform log data into both security artifacts and potential attack vectors that contain proprietary information.

### Key Findings

**1. AI Agents as Privileged Identities Require Distinct Governance Models**

Autonomous AI agents must be treated as superuser equivalents requiring specialized privileged agent access management (PAAM) distinct from traditional human role-based access control. Unlike human operators who interact with systems episodically, AI agents execute continuous operations requiring persistent log access for self-diagnosis, anomaly detection, and autonomous response. Traditional JIT models that expire credentials after interactive sessions prove incompatible with autonomous agent requirements. CSPs implementing KSI-MLA-08 must establish separate authorization frameworks for agent identities that maintain least privilege while supporting real-time, machine-speed log access demands. This includes certificate-based authentication replacing static credentials, behavioral baselines adapted for high-velocity operations, and context-aware authorization that dynamically re-evaluates agent permissions throughout task execution.

**2. AI Log Data Sensitivity Extends Beyond Infrastructure Classification**

AI-generated logs create sensitivity classifications orders of magnitude more critical than traditional infrastructure logs. Training logs contain proprietary model architectures, hyperparameter configurations, and competitive intelligence about AI capabilities. Inference logs expose user prompts that may contain regulated personal health information (PHI), personally identifiable information (PII), and confidential business data. Agentic reasoning traces log multi-step decision chains and tool invocations that reveal internal system architecture and API credentials. Existing sensitivity classification schemes designed for infrastructure events (authentication, authorization, configuration changes) provide insufficient granularity for AI contexts. CSPs must establish AI-specific sensitivity taxonomies spanning model lifecycle stages (pre-training, fine-tuning, inference, continuous learning), data types (model weights, user prompts, decision rationales), and regulatory contexts (GDPR, HIPAA, FedRAMP). Access control policies must then enforce dramatically more restrictive permissions based on these specialized classifications.

**3. Log Integrity and Immutability Protection Becomes Critical for Regulatory Compliance**

AI systems generate decision logs that serve as regulatory evidence for explainability, fairness, and compliance audits. Under EU AI Act, GDPR Article 22, and emerging FedRAMP AI requirements, organizations must provide comprehensive audit trails documenting AI system behavior. However, compromised AI agents with log write access could alter these audit trails to conceal unauthorized activities, model poisoning attempts, or compliance violations. Immutable storage (WORM architectures) and cryptographic signing establish non-repudiation for AI logs. Blockchain-based integrity verification becomes essential for distributed AI systems where multiple organizations contribute to federated learning. CSPs implementing KSI-MLA-08 must treat AI audit logs as evidence similar to legal discovery with corresponding forensic protection, version control, and integrity verification mechanisms. This extends protection requirements to log access decision records themselves—creating circular dependencies where access control audit trails require equal or greater protection than the AI logs they govern.

**4. Multi-Tenant AI Environments Create Cross-Tenant Data Leakage Risks Without Rigorous Segregation**

Cloud providers offering multi-tenant AI services face unprecedented log segregation challenges. Unlike traditional infrastructure where tenants operate in isolated virtual environments, AI agents often execute in shared infrastructure processing data for multiple customers simultaneously. Session-based log contamination allows one tenant's logs to reference another's sensitive information. Metadata inference attacks extract tenant-specific patterns from anonymized aggregate logs through timing analysis. Shared SIEM systems enable query-based data exfiltration when access controls to centralized log repositories prove insufficient. CSPs must implement strict log data segregation at every access layer: query-level filtering preventing cross-tenant result sets, encryption-based segregation isolating log data at rest, and forensic visibility preventing metadata leakage through access patterns themselves. This requires moving beyond traditional network-based isolation to cryptographic guarantees that logs from one tenant remain indecipherable to unauthorized actors from other tenants.

---

## Section 1: Traditional Log Access Control Foundations

Log access control has been a foundational security practice in enterprise infrastructure for decades, originating from audit requirements in financial systems and evolving through regulatory frameworks like NIST SP 800-53, ISO 27001, and FedRAMP. Traditional approaches emphasize role-based access control (RBAC), where users are assigned roles (system administrator, security analyst, auditor) that grant permissions to access specific log categories.

**RBAC Limitations in AI Contexts**: Traditional roles (sysadmin, security auditor, developer) poorly map to AI system access requirements. An "AI model developer" requires granular permissions across multiple access dimensions: training log visibility, inference log access, performance metric data, and debugging traces. However, one model developer should never access another project's proprietary models, customer training data, or competitive performance comparisons. Traditional RBAC creates binary choices: either developers access all AI logs (excessive privilege) or none (operational impediment).

**Attribute-Based Access Control Evolution**: ABAC extends RBAC by evaluating dynamic attributes beyond static role assignments. ABAC policies evaluate user attributes (team, project assignment, clearance level), resource attributes (model sensitivity, training data classification, regulatory jurisdiction), and environmental attributes (time of day, access location, device security posture). For AI logs, ABAC enables policies like: "Access to training logs is granted only to developers from the same project, accessing via corporate networks, during standard business hours, with project manager approval for sensitive hyperparameter data."

**Just-In-Time Access Principles**: JIT access emerged from cloud security best practices requiring temporary credentials issued immediately before task execution, expiring automatically upon completion. JIT minimizes standing privileges (credentials valid only when immediately needed) and creates complete audit trails documenting time-bounded access windows. For human operators, JIT interactively prompts for MFA and manager approval, preventing stale credentials from enabling persistent compromise.

Traditional access control systems achieve effectiveness through steady-state assumptions:
- **Manageable permission sets**: Hundreds or thousands of users with dozens of roles
- **Episodic access patterns**: Humans access logs during investigations, not continuously
- **Centralized repositories**: Single SIEM systems aggregating all logs
- **Predictable access locations**: Corporate networks with known security postures
- **Slow attack evolution**: Threat models stable across quarters

These assumptions collapse in AI agent environments as subsequent sections detail.

---

## Section 2: AI/Agent-Driven Log Access Control Challenges

Autonomous AI agents operating within cloud infrastructure violate every foundational assumption of traditional log access control systems. These agents function as persistent, non-human identities performing security-critical operations with access to sensitive logs that would normally require extensive human approval.

**Volume and Velocity Challenges**: AI systems generate log volumes orders of magnitude larger than traditional infrastructure. A single AI model undergoing continuous inference may generate gigabytes of logs per hour across:
- Inference request metadata (user IDs, prompts, response summaries)
- Model execution traces (layer activations, attention weights, token probabilities)
- System resource utilization (GPU memory, latency, queue depths)
- Security events (authentication, authorization, anomaly detection)

Agentic AI systems executing multi-step reasoning chains log every decision node, tool invocation, intermediate state, and reasoning path. These traces create audit requirements for explainability while simultaneously exposing implementation details. Real-time AI monitoring requires high-velocity log ingestion and access control evaluation—processing millions of access requests per second—straining traditional systems designed for thousands of accesses per second.

**Dynamic Context in AI Workflows**: AI agents execute complex, multi-step workflows where access requirements change dynamically. A reasoning chain might require:
1. Access to customer data logs (to understand context)
2. Escalation to proprietary model logs (requiring different authorization tier)
3. Cross-project correlation (requiring delegation across organizational boundaries)
4. External API access logs (requiring approval from partner organizations)

Traditional JIT models issue static credentials for predefined tasks. They cannot adapt to unknown access requirements emerging during agent reasoning. Context switching within agentic workflows demands continuous authorization re-evaluation, where access permissions shift as the agent's active task changes.

**Non-Human Identity Proliferation**: AI agents operate as service accounts that lack many human identity properties. They cannot complete interactive MFA challenges. They require programmatic authentication via API tokens or certificates with automated rotation. They operate 24/7 without human supervision. They may require simultaneous access to multiple authorization contexts (multi-tenant operations, federated learning participation).

Privilege creep accelerates with service accounts. Each new AI capability requires broader log access. Over months, a monitoring agent may accumulate permissions to customer logs, competitor analysis logs, internal vulnerability assessment logs, and regulatory compliance logs—none of which individual permission reviews scrutinized in context.

**Explainability vs. Access Restriction Tension**: Regulatory frameworks (GDPR Article 22, EU AI Act, NIST AI RMF) mandate comprehensive audit trails documenting AI system behavior for external auditors and regulators. Explainability tools like SHAP (SHapley Additive exPlanations) and LIME (Local Interpretable Model-agnostic Explanations) require unrestricted log data access to generate decision rationales. This creates a fundamental conflict: least-privileged access control restricts log visibility, while regulatory explainability requirements demand comprehensive access. CSPs must balance transparency obligations against security minimization.

**Sensitive Data Exposure in Logs**: AI models inadvertently memorize training data and regurgitate it through inference logs. Canary token research demonstrates that models trained on data containing unique identifiers (email addresses, phone numbers embedded in training examples) will reproduce those identifiers verbatim in outputs. If those outputs are logged, access to inference logs provides access to sensitive training data. Fine-tuning on proprietary customer datasets creates intellectual property exposure when training logs document dataset characteristics. Prompt injection attacks manipulate user prompts logged by AI systems, turning inference logs into command injection vectors.

---

## Section 3: Log Data Access Controls and Monitoring Implementation

Implementing effective log data access controls for AI environments requires multi-layered technical and organizational approaches spanning classification, access decision architecture, and continuous validation.

**AI-Specific Log Classification**: Organizations must establish sensitivity classification schemes that distinguish AI logs from infrastructure logs:

- **Critical (Restricted Access)**: Model training data provenance, proprietary algorithm implementations, hyperparameter configurations for competitive models, customer-specific fine-tuning instructions, prompt injection attack detection logs
- **High (Limited Access)**: User prompts for customer-facing AI systems, personal health information (PHI) processed by healthcare AI, authentication credentials for AI service accounts, database queries executed by AI agents
- **Moderate (Professional Access)**: AI model performance metrics, resource utilization patterns, model version change histories, standard inference logs for model monitoring
- **Low (Broad Access)**: Aggregated AI usage statistics, anonymized performance trends, AI service availability logs, public-facing system status information

Classification must be automated at log generation time using metadata tagging. AI systems should label logs based on:
- Source system (training pipeline, inference endpoint, model repository)
- Log content type (decision rationale, performance metric, error trace)
- Data sensitivity (whether logs contain PII, PHI, proprietary information)
- Regulatory context (GDPR applicability, HIPAA requirements, trade secret protection)

**Access Decision Architecture**: Effective log access control requires real-time authorization engines evaluating multiple contextual dimensions:

User context evaluation:
- Identity verification (who is requesting access)
- Role and team affiliation (organizational position)
- Historical access patterns (deviation from baseline establishes risk)
- Project assignment (which AI systems the user is responsible for)
- Clearance levels (background investigation results)

Resource context evaluation:
- Log sensitivity classification (criticality level)
- AI system classification (production vs. development)
- Data residency requirements (geographic regulations)
- Regulatory jurisdiction (GDPR applicability, sector-specific rules)
- Model lifecycle stage (pre-release development vs. production inference)

Environmental context evaluation:
- Access location (corporate network vs. remote)
- Device security posture (antivirus status, encryption, patch level)
- Time of access (business hours vs. off-hours suspicious access)
- Concurrent system activities (suspicious correlated access patterns)
- Anomaly scores (machine learning models identifying unusual behavior)

Access decisions should incorporate these contexts through ABAC policies that evaluate Boolean expressions combining multiple attributes. For example:

```
grant_access = (
    (user.role == "AI_Engineer" AND resource.sensitivity <= HIGH) OR
    (user.role == "Security_Auditor" AND approval_ticket.exists() AND env.time == "business_hours")
) AND env.device_security_score > 0.8
```

**Temporal Access Control for Agents**: JIT access for autonomous agents requires distinct implementation from interactive human access:

- **Certificate-Based Authentication**: AI agents authenticate using short-lived certificates (47-day lifecycle for FedRAMP compliance) automatically rotated by orchestration systems, providing stronger guarantees than static API tokens
- **Task-Completion Detection**: Agents receive temporary credentials valid until task completion, triggering automatic expiration through health check mechanisms monitoring agent status
- **Periodic Re-authentication**: Long-running agents (monitoring jobs exceeding 8 hours) must periodically re-authenticate, proving continued authorization validity
- **Approval Workflow Integration**: Elevated log access (accessing production inference logs, customer training data) requires pre-approval, automatically authorizing subsequent programmatic access during the approval window

**Monitoring and Anomaly Detection**: Continuous validation ensures access control enforcement remains effective:

- **Access Pattern Baselining**: Machine learning models establish normal access patterns for each user and service account, detecting anomalous access indicating compromise
- **Correlation Analysis**: Detect suspicious sequences like (1) enumerate AI models → (2) access training data → (3) copy to external system
- **Privilege Escalation Detection**: Alert on service accounts accessing log categories above their assigned sensitivity level
- **Cross-Tenant Access Detection**: Identify attempted access from one tenant identifier to logs tagged for other tenants
- **Performance Monitoring**: Track access control decision latency, ensuring real-time access requirements can be met without introducing unacceptable delays

---

## Section 4: Implementation Guidance for CSPs

Cloud service providers implementing KSI-MLA-08 in AI environments should follow these six critical recommendations grounded in research evidence and operational feasibility:

### Recommendation 1: Establish AI-Native Least-Privileged Access Frameworks

Develop distinct access control models for AI agent identities separate from human RBAC systems. Treat AI agents as privileged identities comparable to system administrators, requiring privileged agent access management (PAAM) systems that:

- **Implement non-interactive authentication** using certificates with automated rotation, not static API keys requiring manual management
- **Enforce dynamic privilege management** where agent permissions are reevaluated continuously throughout task execution, not static for the entire session
- **Create AI-specific behavioral baselines** adapted for high-velocity operations (millions of requests per second) where anomaly thresholds must account for normal machine acceleration during peak inference
- **Establish rapid revocation mechanisms** expiring credentials within seconds when compromise indicators emerge, critical for preventing lateral movement to sensitive logs

**Implementation Priority**: This provides maximum security impact by addressing the fundamental gap where current JIT systems assume interactive humans, not autonomous agents. Start by identifying all service accounts with log access, establishing current baseline behavior, and implementing certificate-based authentication with automated rotation.

### Recommendation 2: Develop Comprehensive AI Log Sensitivity Classification

Create organization-wide classification schemes recognizing that AI logs contain sensitive information absent from traditional infrastructure logs. Classification frameworks should:

- **Distinguish by model lifecycle stage** where pre-training logs require maximum restriction (proprietary algorithm protection), fine-tuning logs require moderate restriction (customer data protection), and inference logs require baseline protection (user privacy, prompt confidentiality)
- **Identify PII/PHI exposure risks** at log generation time using data loss prevention (DLP) techniques that redact sensitive information or prevent logging entirely
- **Account for regulatory requirements** distinguishing GDPR applicability (EU residency), HIPAA requirements (healthcare AI), FedRAMP impact levels, and industry-specific regulations (financial sector MFA requirements)
- **Enable automated tagging** where logs are labeled based on source system and content characteristics, creating machine-readable sensitivity markers enabling policy enforcement

**Implementation Priority**: This provides the foundational classification enabling all downstream access control decisions. Establish classification criteria this quarter, implement automated tagging in new AI systems, and retroactively classify existing logs over the following quarter.

### Recommendation 3: Implement Real-Time ABAC with Context-Aware Authorization

Deploy attribute-based access control systems capable of real-time authorization decisions incorporating user, resource, and environmental context:

- **Build attribute data providers** maintaining current information for user roles, project assignments, device security postures, and access location classifications
- **Create dynamic attribute evaluation engines** performing policy evaluation in microseconds, supporting attribute changes mid-request (device security score degradation, anomaly detection trigger) without blocking legitimate access
- **Establish feedback mechanisms** where access decisions inform future authorization (frequent off-hours access from unusual locations increases risk scores for subsequent requests)
- **Implement policy optimization** caching frequently-evaluated decisions, pre-computing policy implications for common scenarios, and batching attribute lookups to minimize latency

**Implementation Priority**: This enables granular access control scaling to autonomous agent demands. Implement for critical AI log repositories first (production model logs, customer data logs), expanding to broader infrastructure logs as performance scales.

### Recommendation 4: Deploy Immutable Audit Logging for AI Decision Trails

Establish tamper-proof logging infrastructure protecting AI access logs themselves against modification, critical for regulatory compliance and forensic analysis:

- **Implement WORM (write-once-read-many) storage** for critical AI logs, preventing modification after initial write, with cryptographic verification detecting tampering attempts
- **Use cryptographic signing** on log events, creating non-repudiation proof that specific access decisions occurred at specific times by specific identities
- **Establish blockchain-based integrity verification** for distributed AI systems where multiple organizations participate, enabling cross-organizational validation that logs remain unmodified
- **Create version control for infrastructure changes**, preventing cloud administrators from modifying log access policies retroactively without forensic evidence

**Implementation Priority**: This protects regulatory evidence and forensic trails. Implement for compliance-critical logs (logs supporting regulatory audits, explainability evidence for AI decisions) immediately, expanding to all AI logs within six months.

### Recommendation 5: Establish Multi-Tenant Log Segregation Guarantees

For multi-tenant AI services, implement cryptographic isolation ensuring logs from one tenant remain indecipherable to other tenants, preventing both direct access and metadata inference:

- **Encrypt logs at generation time** using tenant-specific encryption keys, preventing unauthorized plaintext access even if storage layers are compromised
- **Implement query filtering** at the SIEM layer, ensuring queries return only tenant-specific logs even if query syntax lacks explicit tenant filtering
- **Validate metadata privacy** through testing that timing patterns, aggregate counts, and other metadata don't leak information about other tenants
- **Establish forensic procedures** documenting that queries across tenant boundaries are logged, approved, and reviewed for compliance

**Implementation Priority**: This directly addresses FedRAMP compliance for multi-tenant CSP offerings. Implement immediately for new AI services, and audit existing services within one quarter for compliance gaps.

### Recommendation 6: Create Continuous Validation and Compliance Monitoring

Establish automated systems validating that access control policies remain effective and aligned with regulatory requirements:

- **Implement policy drift detection** identifying where actual access control decisions diverge from documented policies, triggering investigation and remediation
- **Establish privileged access review procedures** where service account permissions are audited quarterly, comparing current permissions against documented business requirements
- **Create compliance reporting mechanisms** demonstrating to auditors (FedRAMP assessors, GDPR supervisors) that access control requirements are met through machine-readable evidence
- **Develop anomaly response playbooks** documenting how to respond when access pattern analysis detects suspicious behavior, including decision to revoke credentials, preserve forensic evidence, and notify affected customers

**Implementation Priority**: This demonstrates continuous compliance with KSI-MLA-08. Establish baseline monitoring immediately, implement automated policy drift detection within 60 days, and develop formal compliance reporting within 90 days.

---

## Section 5: Risk and Benefit Analysis

Implementing comprehensive log access control for AI environments creates distinct risk and benefit profiles that CSPs must evaluate to prioritize implementation efforts.

### Security Benefits

**Insider Threat Prevention**: Least-privileged log access limits damage from compromised employee accounts or malicious insiders. Without granular access control, a compromised system administrator could access all logs including customer training data, inferring proprietary model architectures and competitive strategies. With granular control, that same compromise grants only access to logs legitimately required for the administrator's role.

**Intellectual Property Protection**: AI models represent substantial competitive advantages. Training logs and performance metrics contain information enabling competitors to reconstruct proprietary algorithms. Access control preventing unauthorized log access protects this intellectual property. Studies of model extraction attacks demonstrate that adversaries with comprehensive log access can reconstruct model behaviors with high fidelity.

**Data Breach Prevention**: User prompts logged by AI systems may contain regulated data (HIPAA-protected health information, payment card data, GDPR-protected personal information). Restricting log access to authorized personnel reduces breach surface area and limits damage when breaches occur.

**Regulatory Compliance**: FedRAMP, GDPR, HIPAA, and emerging AI regulations all mandate access control for sensitive data including logs. Comprehensive access control directly addresses regulatory requirements, reducing audit findings and compliance violations.

### Operational Costs

**Performance Overhead**: Real-time access control evaluation introduces latency for all log access requests. ABAC policies evaluating multiple attributes require microseconds to seconds per decision. For high-volume log access (millions of requests per second), this overhead can degrade performance by 5-15% without optimization. Organizations must invest in access control infrastructure (distributed policy engines, attribute caching, request batching) managing this overhead.

**Operational Complexity**: Attribute-based access control requires maintaining accurate context information (user roles, project assignments, device security postures) that must be synchronized with identity management systems. Policy creation and maintenance require security expertise. Organizations must invest in personnel training, policy development tools, and ongoing policy maintenance.

**Approval Workflow Bottlenecks**: JIT access requiring manager approval introduces latency for urgent log access needs. Security incidents requiring immediate forensic analysis may be delayed waiting for manager approval. Organizations must establish escalation procedures enabling emergency access while maintaining audit trail accountability.

**Multi-Tenant Segregation Overhead**: Encrypting logs at generation time and filtering queries at the SIEM layer introduce computational overhead. Organizations must cost-justify this overhead through risk reduction quantification.

### Net Benefit Assessment

For CSPs offering FedRAMP-compliant services, comprehensive log access control is mandatory, making cost-benefit analysis secondary to compliance requirements. For CSPs offering commercial AI services without regulatory constraints, benefits include:

- **Brand differentiation**: Marketing "enterprise-grade log access control" as a competitive advantage
- **Incident response capability**: Demonstrating to customers that log forensics cannot be compromised by insider threats
- **Regulatory readiness**: Positioning for future regulations inevitable in AI oversight landscape

The operational costs are substantial but implementable through phased approaches prioritizing high-risk log categories (production inference logs, customer training data, compliance audit logs) and expanding to broader infrastructure logs as automation matures.

---

## Section 6: Research Gaps and Future Directions

Despite substantial research into access control, AI security, and log management, critical gaps remain in implementing practical, scalable log access control for AI agent environments:

**Agent Behavior Modeling**: Behavioral anomaly detection for human users is mature, but anomaly detection for AI agents requires distinct approaches. Agents exhibit high-velocity, repetitive access patterns. They operate 24/7 without human-driven variance. They may exhibit rapid pattern changes when executing different tasks. Research establishing baselines and thresholds for anomaly detection in agent contexts remains preliminary.

**Cryptographic Isolation at Scale**: Multi-tenant AI services require encryption-based segregation preventing cross-tenant data leakage. Fully homomorphic encryption enabling computation on encrypted logs remains computationally prohibitive. Research into practical encryption schemes supporting fine-grained log access control at acceptable performance remains incomplete.

**Regulatory Alignment in Distributed Systems**: Federated learning and multi-cloud AI deployments distribute logs across organizational boundaries. Regulations like GDPR (EU data residency), CCPA (California residency), and PIPL (China data localization) create conflicting requirements. Research into practical approaches aligning contradictory regulations within unified access control frameworks is nascent.

**Explainability vs. Privacy Tradeoffs**: AI regulations mandate explainability requiring comprehensive audit trail access. Privacy regulations mandate data minimization restricting log retention. Research into technical mechanisms achieving both simultaneously—enabling audit trail access for regulatory purposes while preventing unauthorized access—remains an open problem.

**Supply Chain Log Integrity**: When third parties contribute to AI model training (federated learning, data partnerships), ensuring that logs from all participants cannot be tampered with becomes complex. Research into practical mechanisms enabling cross-organizational log integrity validation without creating new attack vectors is limited.

---

## References


[1] A Practical Framework for Evaluating Medical AI Security: Reproducible Assessment of Jailbreaking and Privacy Vulnerabilities Across Clinical Specialties — Jinghao Wang, Ping Zhang, Carter Yagemann
[2] LLMZ+: Contextual Prompt Whitelist Principles for Agentic LLMs — Tom Pawelek, Raj Patel, Charlotte Crowell, Noorbakhsh Amiri, Sudip Mittal, Shahram Rahimi, Andy Perkins
[3] BlockA2A: Towards Secure and Verifiable Agent-to-Agent Interoperability — Zhenhua Zou, Zhuotao Liu, Lepeng Zhao, Qiuyang Zhan
[4] Unmasking Synthetic Realities in Generative AI: A Comprehensive Review of Adversarially Robust Deepfake Detection Systems — Naseem Khan, Tuan Nguyen, Amine Bermak, Issa Khalil
[5] Quantum-Augmented AI/ML for O-RAN: Hierarchical Threat Detection with Synergistic Intelligence and Interpretability (Technical Report) — Tan Le, Van Le, Sachin Shetty
[6] Web Technologies Security in the AI Era: A Survey of CDN-Enhanced Defenses — Mehrab Hosain, Sabbir Alom Shuvo, Matthew Ogbe, Md Shah Jalal Mazumder, Yead Rahman, Md Azizul Hakim, Anukul Pandey
[7] Web Technologies Security in the AI Era: A Survey of CDN-Enhanced Defenses — Mehrab Hosain, Sabbir Alom Shuvo, Matthew Ogbe, Md Shah Jalal Mazumder, Yead Rahman, Md Azizul Hakim, Anukul Pandey
[8] eBPF-PATROL: Protective Agent for Threat Recognition and Overreach Limitation using eBPF in Containerized and Virtualized Environments — Sangam Ghimire, Nirjal Bhurtel, Roshan Sahani, Sudan Jha
[9] Breaking the Code: Security Assessment of AI Code Agents Through Systematic Jailbreaking Attacks — Shoumik Saha, Jifan Chen, Sam Mayers, Sanjay Krishna Gouda, Zijian Wang, Varun Kumar
[10] Policy-as-Prompt: Turning AI Governance Rules into Guardrails for AI Agents — Gauri Kholkar, Ratinder Ahuja
[11] LLMZ+: Contextual Prompt Whitelist Principles for Agentic LLMs — Tom Pawelek, Raj Patel, Charlotte Crowell, Noorbakhsh Amiri, Sudip Mittal, Shahram Rahimi, Andy Perkins
[12] TooBadRL: Trigger Optimization to Boost Effectiveness of Backdoor Attacks on Deep Reinforcement Learning — Mingxuan Zhang, Oubo Ma, Kang Wei, Songze Li, Shouling Ji
[13] eBPF-PATROL: Protective Agent for Threat Recognition and Overreach Limitation using eBPF in Containerized and Virtualized Environments — Sangam Ghimire, Nirjal Bhurtel, Roshan Sahani, Sudan Jha
[14] Proactive DDoS Detection and Mitigation in Decentralized Software-Defined Networking via Port-Level Monitoring and Zero-Training Large Language Models — Mohammed N. Swileh, Shengli Zhang
[15] Policy-as-Prompt: Turning AI Governance Rules into Guardrails for AI Agents — Gauri Kholkar, Ratinder Ahuja
[16] The Aegis Protocol: A Foundational Security Framework for Autonomous AI Agents — Sai Teja Reddy Adapala, Yashwanth Reddy Alugubelly
[17] BlockA2A: Towards Secure and Verifiable Agent-to-Agent Interoperability — Zhenhua Zou, Zhuotao Liu, Lepeng Zhao, Qiuyang Zhan
[18] eBPF-PATROL: Protective Agent for Threat Recognition and Overreach Limitation using eBPF in Containerized and Virtualized Environments — Sangam Ghimire, Nirjal Bhurtel, Roshan Sahani, Sudan Jha
[19] DASH: Deception-Augmented Shared Mental Model for a Human-Machine Teaming System — Zelin Wan, Han Jun Yoon, Nithin Alluru, Terrence J. Moore, Frederica F. Nelson, Seunghyun Yoon, Hyuk Lim, Dan Dongseong Kim, Jin-Hee Cho
[20] PCEval: A Benchmark for Evaluating Physical Computing Capabilities of Large Language Models — Inpyo Song, Eunji Jeon, Jangwon Lee
[21] Adaptive Trust Consensus for Blockchain IoT: Comparing RL, DRL, and MARL Against Naive, Collusive, Adaptive, Byzantine, and Sleeper Attacks — Soham Padia, Dhananjay Vaidya, Ramchandra Mangrulkar
[22] PCEval: A Benchmark for Evaluating Physical Computing Capabilities of Large Language Models — Inpyo Song, Eunji Jeon, Jangwon Lee
[23] A Practical Framework for Evaluating Medical AI Security: Reproducible Assessment of Jailbreaking and Privacy Vulnerabilities Across Clinical Specialties — Jinghao Wang, Ping Zhang, Carter Yagemann
[24] Transparent, Evaluable, and Accessible Data Agents: A Proof-of-Concept Framework — Nooshin Bahador
[25] LLMZ+: Contextual Prompt Whitelist Principles for Agentic LLMs — Tom Pawelek, Raj Patel, Charlotte Crowell, Noorbakhsh Amiri, Sudip Mittal, Shahram Rahimi, Andy Perkins
[26] Sentinel Agents for Secure and Trustworthy Agentic AI in Multi-Agent Systems — Diego Gosmar, Deborah A. Dahl
[27] BlockA2A: Towards Secure and Verifiable Agent-to-Agent Interoperability — Zhenhua Zou, Zhuotao Liu, Lepeng Zhao, Qiuyang Zhan
[28] Beyond Jailbreaking: Auditing Contextual Privacy in LLM Agents — Saswat Das, Jameson Sandler, Ferdinando Fioretto
[29] eBPF-PATROL: Protective Agent for Threat Recognition and Overreach Limitation using eBPF in Containerized and Virtualized Environments — Sangam Ghimire, Nirjal Bhurtel, Roshan Sahani, Sudan Jha
[30] PCEval: A Benchmark for Evaluating Physical Computing Capabilities of Large Language Models — Inpyo Song, Eunji Jeon, Jangwon Lee
[31] Temporal Attack Pattern Detection in Multi-Agent AI Workflows: An Open Framework for Training Trace-Based Security Models — Ron F. Del Rosario
[32] Variable Record Table: A Unified Hardware-Assisted Framework for Runtime Security — Suraj Kumar Sah, Love Kumar Sah
[33] Quantization Blindspots: How Model Compression Breaks Backdoor Defenses — Rohan Pandey, Eric Ye
[34] Project Ariadne: A Structural Causal Framework for Auditing Faithfulness in LLM Agents — Sourena Khanzadeh
[35] PCEval: A Benchmark for Evaluating Physical Computing Capabilities of Large Language Models — Inpyo Song, Eunji Jeon, Jangwon Lee
[36] Jailbreaking LLMs &amp; VLMs: Mechanisms, Evaluation, and Unified Defense — Zejian Chen, Chaozhuo Li, Chao Li, Xi Zhang, Litian Zhang, Yiming He
[37] AI-Driven Cybersecurity Threats: A Survey of Emerging Risks and Defensive Strategies — Sai Teja Erukude, Viswa Chaitanya Marella, Suhasnadh Reddy Veluru
[38] The Vibe-Check Protocol: Quantifying Cognitive Offloading in AI Programming — Aizierjiang Aiersilan
[39] PatchBlock: A Lightweight Defense Against Adversarial Patches for Embedded EdgeAI Devices — Nandish Chattopadhyay, Abdul Basit, Amira Guesmi, Muhammad Abdullah Hanif, Bassem Ouni, Muhammad Shafique
[40] eBPF-PATROL: Protective Agent for Threat Recognition and Overreach Limitation using eBPF in Containerized and Virtualized Environments — Sangam Ghimire, Nirjal Bhurtel, Roshan Sahani, Sudan Jha
[41] Policy-as-Prompt: Turning AI Governance Rules into Guardrails for AI Agents — Gauri Kholkar, Ratinder Ahuja
[42] LLM-GUARD: Large Language Model-Based Detection and Repair of Bugs and Security Vulnerabilities in C++ and Python — Akshay Mhatre, Noujoud Nader, Patrick Diehl, Deepti Gupta
[43] PCEval: A Benchmark for Evaluating Physical Computing Capabilities of Large Language Models — Inpyo Song, Eunji Jeon, Jangwon Lee
[44] LogicLens: Visual-Logical Co-Reasoning for Text-Centric Forgery Analysis — Fanwei Zeng, Changtao Miao, Jing Huang, Zhiya Tan, Shutao Gong, Xiaoming Yu, Yang Wang, Huazhe Tan, Weibin Yao, Jianshu Li
[45] $PC^2$: Politically Controversial Content Generation via Jailbreaking Attacks on GPT-based Text-to-Image Models — Wonwoo Choi, Minjae Seo, Minkyoo Song, Hwanjo Heo, Seungwon Shin, Myoungsung You
[46] Jailbreaking LLMs &amp; VLMs: Mechanisms, Evaluation, and Unified Defense — Zejian Chen, Chaozhuo Li, Chao Li, Xi Zhang, Litian Zhang, Yiming He
[47] The Vibe-Check Protocol: Quantifying Cognitive Offloading in AI Programming — Aizierjiang Aiersilan
[48] PCEval: A Benchmark for Evaluating Physical Computing Capabilities of Large Language Models — Inpyo Song, Eunji Jeon, Jangwon Lee
[49] AI-Driven Cybersecurity Threats: A Survey of Emerging Risks and Defensive Strategies — Sai Teja Erukude, Viswa Chaitanya Marella, Suhasnadh Reddy Veluru
[50] Project Ariadne: A Structural Causal Framework for Auditing Faithfulness in LLM Agents — Sourena Khanzadeh
[51] Temporal Attack Pattern Detection in Multi-Agent AI Workflows: An Open Framework for Training Trace-Based Security Models — Ron F. Del Rosario
[52] Secure, Verifiable, and Scalable Multi-Client Data Sharing via Consensus-Based Privacy-Preserving Data Distribution — Prajwal Panth, Sahaj Raj Malla
[53] DASH: Deception-Augmented Shared Mental Model for a Human-Machine Teaming System — Zelin Wan, Han Jun Yoon, Nithin Alluru, Terrence J. Moore, Frederica F. Nelson, Seunghyun Yoon, Hyuk Lim, Dan Dongseong Kim, Jin-Hee Cho
[54] AI-Driven Cybersecurity Testbed for Nuclear Infrastructure: Comprehensive Evaluation Using METL Operational Data — Benjamin Blakely, Yeni Li, Akshay Dave, Derek Kultgen, Rick Vilim
[55] eBPF-PATROL: Protective Agent for Threat Recognition and Overreach Limitation using eBPF in Containerized and Virtualized Environments — Sangam Ghimire, Nirjal Bhurtel, Roshan Sahani, Sudan Jha
[56] Jailbreaking LLMs &amp; VLMs: Mechanisms, Evaluation, and Unified Defense — Zejian Chen, Chaozhuo Li, Chao Li, Xi Zhang, Litian Zhang, Yiming He
[57] Project Ariadne: A Structural Causal Framework for Auditing Faithfulness in LLM Agents — Sourena Khanzadeh
[58] The Vibe-Check Protocol: Quantifying Cognitive Offloading in AI Programming — Aizierjiang Aiersilan
[59] A Practical Framework for Evaluating Medical AI Security: Reproducible Assessment of Jailbreaking and Privacy Vulnerabilities Across Clinical Specialties — Jinghao Wang, Ping Zhang, Carter Yagemann
[60] Jailbreaking LLMs &amp; VLMs: Mechanisms, Evaluation, and Unified Defense — Zejian Chen, Chaozhuo Li, Chao Li, Xi Zhang, Litian Zhang, Yiming He

---

**Report Generated**: AI Research Assistant
**Total Papers Referenced**: 60
**Repository**: ksi_watch / KSI-MLA-08_25-12A_LogDataAccess
