# KSI-MLA-08: Log Data Access - Question Library

**KSI Title**: Log Data Access
**KSI Objective**: Implement least-privileged, role and attribute-based, and just-in-time (JIT) access authorization for sensitive log data in AI/agent environments
**Date**: 2026-01-12
**Status**: Pending Human Review

---

## Summary Statistics

**Original Question Count**: 36 (after initial curation)
**Questions Moved to KSI-MLA-01**: 3 (Q025, Q027, Q028 - deep log integrity/forensics)
**Questions Consolidated**: 2 (Q006+Q031 merged, Q033+Q034 clarified)
**Final Question Count**: 32

---

## Question Categories

### Category 1: AI Agent Identity and Authentication (7 questions)
### Category 2: AI Log Sensitivity Classification (6 questions)
### Category 3: Context-Aware and Dynamic Authorization (6 questions)
### Category 4: Multi-Tenant Log Segregation (4 questions)
### Category 5: Access Control Decision Log Integrity (1 question)
### Category 6: JIT Access and Temporal Controls (3 questions)
### Category 7: Monitoring and Compliance (5 questions)

---

## Questions

### Category 1: AI Agent Identity and Authentication

**KSI-MLA-08-Q001** – Does your organization have a distinct privileged agent access management (PAAM) system separate from traditional human RBAC for AI agents and service accounts accessing log data?

**KSI-MLA-08-Q002** – What is your current approach to certificate-based authentication and automated rotation for AI agent credentials accessing logs, versus static API keys?

**KSI-MLA-08-Q003** – How are AI agents currently classified within your log access control frameworks—are they treated as superuser equivalents, or as standard service accounts?

**KSI-MLA-08-Q004** – For AI agents requiring continuous, non-interactive log access (vs. human operators with interactive MFA), how does your access control system handle authentication without interactive challenges?

**KSI-MLA-08-Q005** – What is the certificate validity period and rotation interval for AI agents accessing sensitive log data, and what mechanisms trigger automatic rotation?

**KSI-MLA-08-Q006** – How does your system implement task-completion detection that automatically expires agent credentials and log access session permissions upon task completion, preventing long-lived credential accumulation?

**KSI-MLA-08-Q007** – What mechanisms prevent service account credential sprawl and privilege creep for AI agents that accumulate log access permissions over time?

**KSI-MLA-08-Q008** – How are AI agent identities provisioned, managed, and deprovisioned specifically for log data access, and what approval workflows govern this lifecycle?

### Category 2: AI Log Sensitivity Classification

**KSI-MLA-08-Q009** – Does your organization have AI-specific log sensitivity classifications that distinguish training logs, fine-tuning logs, inference logs, and agentic reasoning traces from traditional infrastructure logs?

**KSI-MLA-08-Q010** – How are you currently identifying and protecting logs containing PII/PHI exposure from AI operations (user prompts, training data characteristics, model hyperparameters)?

**KSI-MLA-08-Q011** – What is your current classification scheme for proprietary information in AI logs—model architectures, algorithm implementations, competitive performance data, and training dataset characteristics?

**KSI-MLA-08-Q012** – Are logs containing vector database queries, embedding access, and semantic search operations classified and protected according to their sensitivity to model reconstruction attacks?

**KSI-MLA-08-Q013** – How are logs from AI model training data access operations classified, and what controls prevent unauthorized access to data lineage and provenance information?

**KSI-MLA-08-Q014** – What automated tagging mechanisms exist to classify AI logs at generation time using metadata (model lifecycle stage, data sensitivity, regulatory classification)?

### Category 3: Context-Aware and Dynamic Authorization

**KSI-MLA-08-Q015** – Has your organization implemented attribute-based access control (ABAC) capable of real-time authorization decisions evaluating user context, resource context, and environmental context for log access requests?

**KSI-MLA-08-Q016** – How do you currently handle dynamic context shifts during AI agent workflows where log access requirements change mid-execution?

**KSI-MLA-08-Q017** – Can your access control policies specify conditions like "access granted only to developers from the same AI project, via corporate networks, during business hours, for logs classified as moderate or lower"?

**KSI-MLA-08-Q018** – What is the measured latency for real-time access control decisions on log data requests, and does it meet operational requirements for high-velocity AI operations (millions of requests per second)?

**KSI-MLA-08-Q019** – How does your access control system handle attribute changes mid-request (e.g., device security score degradation, anomaly detection trigger, risk score elevation)?

**KSI-MLA-08-Q020** – What mechanisms re-evaluate authorization continuously throughout agent operations rather than granting static session-based permissions?

### Category 4: Multi-Tenant Log Segregation

**KSI-MLA-08-Q021** – For multi-tenant AI services, what cryptographic or architectural guarantees prevent cross-tenant log data leakage at the access control layer?

**KSI-MLA-08-Q022** – How are you protecting against metadata inference attacks (timing patterns, aggregate counts) that could leak tenant-specific information through anonymized log access patterns?

**KSI-MLA-08-Q023** – What query-level filtering mechanisms exist to prevent cross-tenant result sets when multiple tenants' logs are stored in centralized SIEM systems?

**KSI-MLA-08-Q024** – Can your organization demonstrate through testing that logs from one tenant (including AI model training logs, inference logs, and agent reasoning traces) are not accessible to other tenants through any access path?

### Category 5: Access Control Decision Log Integrity

**KSI-MLA-08-Q025** – Are your log access control decision logs and audit trails protected with write-once-read-many (WORM) storage, cryptographic signing, or immutable storage mechanisms to prevent tampering and enable non-repudiation of access decisions?

### Category 6: JIT Access and Temporal Controls

**KSI-MLA-08-Q026** – What is your current policy for just-in-time (JIT) access to sensitive AI logs—particularly for autonomous agents requiring continuous, non-interactive log access versus episodic human access?

**KSI-MLA-08-Q027** – What is the typical latency for JIT approval workflows for elevated AI log access (production inference logs, customer training data), and are escalation procedures available for urgent forensic access?

**KSI-MLA-08-Q028** – What mechanisms prevent bypass of JIT controls through shadow credential provisioning (developers creating long-lived credentials to avoid approval workflows)?

### Category 7: Monitoring and Compliance

**KSI-MLA-08-Q029** – Do you have machine learning models establishing baseline log access patterns for service accounts and AI agents, and how are anomaly thresholds adapted for high-velocity agent operations? How are baseline anomalies distinguished from policy-compliant access?

**KSI-MLA-08-Q030** – How are you currently detecting privilege escalation attempts where service accounts or AI agents access log categories above their assigned sensitivity level or cross-tenant boundaries?

**KSI-MLA-08-Q031** – What automated policy drift detection exists to identify where actual log access control decisions diverge from documented policies?

**KSI-MLA-08-Q032** – Can your organization provide machine-readable evidence demonstrating KSI-MLA-08 compliance for regulatory audits (FedRAMP assessments, GDPR supervisory reviews, EU AI Act compliance)?

---

## Consolidated and Moved Questions

### Questions Consolidated Within MLA-08

1. **Q006 + Q031 Merged**: Task-completion detection for credential expiration now includes both agent credentials and log access session permissions (now Q026)
2. **Q033 + Q034 Clarified**: Baseline detection (Q029) and privilege escalation detection (Q030) are now explicitly distinguished—baselines detect anomalies in access patterns, while escalation detection specifically flags unauthorized access above assigned sensitivity levels

### Questions Moved to KSI-MLA-01 (Log Integrity & Forensics)

The following integrity and forensics questions have been moved to KSI-MLA-01 as they address "log storage integrity and forensic immutability" rather than "access authorization":

1. **Original Q026 → KSI-MLA-01**: Non-repudiation proof of access decisions (fits MLA-01 cryptographic integrity framework)
2. **Original Q027 → KSI-MLA-01**: Cross-organizational log integrity validation for federated learning (fits MLA-01 multi-tenant isolation framework)
3. **Original Q028 → KSI-MLA-01**: Forensic detection of modified audit trails (fits MLA-01 forensic immutability framework)

**Note**: MLA-08-Q025 (now narrowly focused on "access control decision log integrity" for non-repudiation of WHO accessed WHAT logs WHEN) remains in MLA-08 as it directly addresses authorization audit trails.

---

## Originally Added AI-Specific Questions (Retained in Refined Questions)

The following AI/agent-specific questions from the original curation remain in the refined set:

**Category 1 (Agent Identity) - 7 questions**:
- Q001: Distinct PAAM system for AI agents
- Q002: Certificate-based authentication and rotation
- Q003: AI agent classification in access frameworks
- Q004: Non-interactive authentication for continuous agent access
- Q005: Certificate validity and rotation intervals
- Q006: Task-completion detection for credential/session expiration (merged from original Q006 + Q031)
- Q008: Agent identity lifecycle management

**Category 2 (Log Sensitivity) - 6 questions**:
- Q009: AI-specific log sensitivity classifications
- Q010: PII/PHI protection in AI logs
- Q011: Proprietary information classification in AI logs
- Q012: Vector database and embedding access log classification
- Q013: Model training data access log classification
- Q014: Automated metadata tagging for AI logs

**Category 3 (Dynamic Authorization) - 6 questions**:
- Q015: ABAC implementation for real-time authorization
- Q016: Dynamic context shifts during agent workflows
- Q017: Context-based conditional access policies
- Q018: Latency requirements for high-velocity operations
- Q019: Mid-request attribute change handling
- Q020: Continuous re-evaluation during agent operations

**Category 4 (Multi-Tenant Segregation) - 4 questions**:
- Q021: Cryptographic isolation between tenants
- Q022: Metadata inference attack prevention
- Q023: Query-level filtering for multi-tenant logs
- Q024: Testing and validation of tenant segregation

**Category 5 (Access Control Decision Log Integrity) - 1 question**:
- Q025: WORM/cryptographic protection of access control decision logs

**Category 6 (JIT Access) - 3 questions**:
- Q026: JIT access policy for AI logs
- Q027: JIT approval workflow latency and escalation
- Q028: Prevention of JIT bypass through shadow credentials

**Category 7 (Monitoring & Compliance) - 5 questions**:
- Q029: Baseline log access patterns and anomaly detection (merged Q033 focus)
- Q030: Privilege escalation detection for agents (clarified Q034)
- Q031: Automated policy drift detection
- Q032: Machine-readable KSI-MLA-08 compliance evidence

---

## AI/Agent-Specific Focus Areas

This question library specifically addresses:

1. **Agent Query Logging**: Questions about how AI agents' log access requests are controlled, monitored, and audited
2. **Model Training Data Access Logging**: Questions about protecting access to logs containing training data characteristics and provenance
3. **Embedding Access Tracking**: Questions about logs from vector database queries and semantic search operations
4. **Prompt Access Logging**: Questions about protecting user prompts and inference request logs containing sensitive information
5. **Fine-Tuning Data Access**: Questions about controlling access to logs from fine-tuning operations on proprietary datasets
6. **Agent Reasoning Trace Access**: Questions about multi-step decision logs and tool invocation traces from agentic AI systems
7. **High-Velocity Operations**: Questions about access control performance at machine-speed log access rates
8. **Non-Human Identity Management**: Questions about certificate-based authentication and automated credential rotation for AI agents

---

## Alignment with KSI-MLA-08 Requirements

All questions align with the core KSI-MLA-08 requirement to implement:

- **Least-Privileged Access**: Questions verify that log access is limited to minimum necessary permissions
- **Role-Based Access Control**: Questions assess RBAC implementation for both human and agent identities
- **Attribute-Based Access Control**: Questions evaluate dynamic authorization based on user, resource, and environmental attributes
- **Just-In-Time Access**: Questions validate temporal access controls and credential lifecycle management
- **Sensitivity-Based Controls**: Questions ensure access decisions reflect organizational data sensitivity classifications

---

## Usage Notes for Assessment and Validation

1. **Scope**: All 32 questions focus specifically on log data access control in AI/agent environments; traditional infrastructure log access is covered by baseline KSI-MLA-08
2. **AI-Specific Context**: Each question explicitly addresses AI/agent-specific threats, architectural constraints, or operational requirements—prompt injection, model training data protection, agent identity management, high-velocity access patterns, agentic reasoning trace isolation, etc.
3. **Evidence Requirements**: Questions require demonstrable evidence through: organizational policies, technical configuration details, test results/red-team validation, audit logs of access decisions, compliance audit reports
4. **Assessment Focus**: Questions emphasize persistent monitoring, continuous authorization, and real-time validation rather than point-in-time assessments
5. **Multi-Tenant Considerations**: Questions for multi-tenant cloud service providers address: cryptographic isolation, cross-tenant segregation, metadata inference prevention, query-level filtering validation

---

**Document Status**: Refined per GitHub Issue #62 guidance
**Version**: 2.0 (Consolidated and perspective-neutral)
**Last Updated**: 2026-01-13
**Changes**: Moved integrity/forensics questions to KSI-MLA-01, consolidated Q006+Q031 and Q033+Q034, removed stakeholder-specific language, reduced from 36 to 32 questions
**Related Documents**: KSI-MLA-01_questions.md (now includes moved integrity questions), 3_KSI-MLA-08_report.md, 2_KSI-MLA-08_clusters.md
