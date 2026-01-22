# KSI-MLA-07: Event Types - Question Library

**KSI Title**: Event Types in Cloud Systems and AI/Agent Contexts
**Date Generated**: January 2026
**Processing Status**: Human Review Complete - Refined Per Guidance
**Target Audience**: All Stakeholder Roles (CIO, Customer, Auditor)

---

## Summary Statistics

- **Original Question Count**: 150 questions (covering CIO, Customer, Auditor, AI-specific, and cross-functional themes)
- **Questions Removed (Out of Scope)**: 34 questions
  - Infrastructure/SIEM capacity and design: Q001-Q002, Q012, Q014, Q118-Q123 (9 questions)
  - Log access control and forensics: Q087-Q088, Q114 (3 questions)
  - Training and capability building: Q108-Q110, Q145-Q150 (6 questions)
  - Privacy/compliance procedures: Q060-Q065, Q084-Q086 (9 questions)
  - Governance and framework alignment: Q033-Q035, Q099-Q103, Q111-Q113 (13 questions)
- **Questions Consolidated**: 5 composite questions collapsed into 2 unified questions
  - Inventory and catalog completeness: Q003-Q005, Q066-Q068 consolidated into 2 questions
  - Tamper detection and immutability: Q022-Q023, Q057-Q058, Q083, Q089, Q095 consolidated into 2 questions (with 1 moved to CMT-01)
- **Questions Made Perspective-Neutral**: All remaining questions rewritten to remove CIO/Customer/Auditor role distinctions
- **Final Question Count**: 82 questions

**Scope Clarification**:
- This KSI focuses exclusively on **event type definition, taxonomy, coverage, and monitoring capability** for AI systems
- Infrastructure questions (capacity, latency, scaling) moved to KSI-CMT-01
- Log access control questions moved to KSI-MLA-08
- Training and organizational capability questions moved to KSI-CED-01/02
- Privacy compliance procedures moved to appropriate privacy/compliance KSI
- Governance and framework alignment questions moved to KSI-AFR-09

---

## Core Discovery Questions

### Section 1: Event Type Definition and Catalog

**KSI-MLA-07-Q001**: What is the current inventory of information resources processing, storing, or transforming federal data in both traditional cloud and AI contexts, and what is the documented coverage percentage (target: 95%+ within 90 days)?

**KSI-MLA-07-Q002**: For all documented information resources, what is the event type and taxonomy definition status? Are there formal, documented definitions for all 40-60+ required AI event types covering: model lifecycle, inference decisions, agent actions, data quality issues, and security threats?

**KSI-MLA-07-Q003**: For each defined event type, what documentation exists specifying: trigger conditions, required fields, severity classification, retention period, and business/security justification?

**KSI-MLA-07-Q004**: Are event type definitions standardized across all deployment platforms (AWS SageMaker, Azure ML, Google Vertex AI, self-hosted Kubernetes, third-party platforms)?

**KSI-MLA-07-Q005**: What percentage of actual system behaviors generate defined events (event type coverage ratio), and is this trending toward the 90%+ target within 6 months?

**KSI-MLA-07-Q006**: Do all generated events conform to a documented schema with minimum required fields: timestamp (with sub-second precision), actor/identity, resource identifier, action/operation, result/outcome, and contextual information?

**KSI-MLA-07-Q007**: Are events generated from heterogeneous sources (AWS, Azure, GCP, self-hosted systems) normalized to standard format enabling correlation across platforms?

**KSI-MLA-07-Q008**: What quality assurance procedures validate schema compliance for all generated events?

### Section 2: Event Generation and Completeness

**KSI-MLA-07-Q009**: For a sample of critical system operations (model deployment, permission change, data access, agent invocation), can you verify that all expected events were generated with no gaps?

**KSI-MLA-07-Q010**: What procedures detect and alert on missing events (e.g., event log gaps >1 hour in duration)?

**KSI-MLA-07-Q011**: Are there systematic testing procedures validating that all system components generate expected events (e.g., testing model deployment events, permission change events, agent decision events)?

**KSI-MLA-07-Q012**: Are audit events generated for: user/agent actions, security-relevant events, policy changes, system state changes, and exception conditions?

### Section 3: AI Model Lifecycle Events

**KSI-MLA-07-Q013**: What event types capture the complete AI model lifecycle: training initiation, validation testing, approval, deployment, production monitoring, retraining, versioning, and retirement?

**KSI-MLA-07-Q014**: For model versions in production, can you verify with event evidence: (1) which training data was used, (2) validation testing completed, (3) security approval granted, (4) current deployment version matches authorized version?

**KSI-MLA-07-Q015**: What event types capture model performance degradation, drift detection, or behavioral anomalies post-deployment?

**KSI-MLA-07-Q016**: Are model version rollback operations logged with trigger reason (performance degradation, security incident, manual override), execution details, and validation of rolled-back model?

**KSI-MLA-07-Q017**: For A/B testing and canary deployments of AI models, are events logged with traffic split percentages, performance comparisons, and promotion/rejection decisions?

### Section 4: Inference and Prediction Events

**KSI-MLA-07-Q018**: What event types capture inference request details: input data characteristics, model version used, confidence scores, output decisions, and any anomalies detected?

**KSI-MLA-07-Q019**: Are inference confidence scores, input validation failures, and output anomalies being captured systematically?

**KSI-MLA-07-Q020**: What data drift detection events are generated, and at what detection latency (minutes vs. hours)?

**KSI-MLA-07-Q021**: Can you detect and alert on concept drift (when model relationships with business outcomes change)?

**KSI-MLA-07-Q022**: What visibility exists into model performance degradation, false positive/negative rate increases, and metric divergence from expected ranges?

### Section 5: Agent Authorization and Boundary Events

**KSI-MLA-07-Q023**: For autonomous agents, what event types capture: goal initialization, task decomposition, tool selection with full parameters, API call responses, and final decision rationale?

**KSI-MLA-07-Q024**: What event types capture agent authorization boundary violations, such as attempts to access resources outside permitted scope, invoke unauthorized tools, or exceed delegation limits?

**KSI-MLA-07-Q025**: Are agent privilege escalation attempts logged, including tool chaining sequences that aggregate permissions beyond intended authorization?

**KSI-MLA-07-Q026**: What event types monitor agent behavior anomalies indicating potential compromise, including deviation from typical tool usage patterns, abnormal API call frequencies, or suspicious data access?

**KSI-MLA-07-Q027**: Are agent-to-agent communications, escalations for human approval, and information sharing between peers being logged and monitored?

### Section 6: Data Quality and Training Integrity Events

**KSI-MLA-07-Q028**: What event types track training data lineage from acquisition through model training? Can you document: data source, version, date, transformations applied, access logs, and subsequent modifications?

**KSI-MLA-07-Q029**: Are events generated at every supply chain boundary (data handoff, annotation completion, model artifact integrity validation, deployment confirmation)?

**KSI-MLA-07-Q030**: What event types capture data quality issues: missing values, distribution shifts, anomalous data points, or data poisoning indicators?

**KSI-MLA-07-Q031**: For synthetic data generation (for training or testing), are events logged with generation parameters, quality validation, and usage in model training?

**KSI-MLA-07-Q032**: Can you document with certainty that training data for production models has not been compromised, poisoned, or corrupted during data acquisition, processing, or training?

### Section 7: AI-Specific Threat Detection Events

**KSI-MLA-07-Q033**: What event types enable detection of prompt injection attempts targeting AI models?

**KSI-MLA-07-Q034**: What detection mechanisms exist for model poisoning (training data corruption, backdoor injection, model parameter modification)?

**KSI-MLA-07-Q035**: Are there detection procedures for adversarial inputs, hallucination generation, or other AI-specific attack indicators?

**KSI-MLA-07-Q036**: What event types capture potential cross-tenant data leakage in multi-tenant AI systems, including shared model inference, shared feature stores, or shared vector databases?

**KSI-MLA-07-Q037**: Are tenant isolation boundary violations logged when one customer's data, models, or agents inadvertently access another customer's resources?

**KSI-MLA-07-Q038**: What event types track cryptographic signing and registry integrity validation preventing silent model substitution in deployment pipelines?

### Section 8: RAG and Knowledge System Events

**KSI-MLA-07-Q039**: For Retrieval Augmented Generation (RAG) systems, what event types capture: (1) retrieval quality metrics, (2) embedding generation, (3) vector similarity searches, and (4) context injection into prompts?

**KSI-MLA-07-Q040**: Are RAG retrieval failures, low-relevance retrievals, or context truncation events logged to identify knowledge base gaps or retrieval system degradation?

**KSI-MLA-07-Q041**: What event types track updates to vector databases, knowledge graphs, or other AI knowledge systems, including data source attribution and update provenance?

### Section 9: Federated and Distributed Learning Events

**KSI-MLA-07-Q042**: For federated learning systems, what event types capture aggregation rounds, client contribution counts, model update magnitudes, and detection of malicious client updates?

**KSI-MLA-07-Q043**: Are federated learning events logged with sufficient detail to identify which client devices or edge nodes contributed to model degradation or poisoning attempts?

**KSI-MLA-07-Q044**: What event types monitor communication patterns, data distribution skew, and convergence metrics across federated learning participants?

### Section 10: Model Explainability and Interpretability Events

**KSI-MLA-07-Q045**: What event types capture model explainability operations, such as SHAP value calculations, LIME explanations, attention visualization, or other interpretability method executions?

**KSI-MLA-07-Q046**: Are explainability events linked to specific predictions or decisions, enabling reconstruction of why a particular AI output was generated?

### Section 11: Supply Chain and Artifact Integrity Events

**KSI-MLA-07-Q047**: What event types track AI model supply chain verification operations, including: (1) training data source validation, (2) model artifact signature verification, (3) dependency scanning results, and (4) provenance attestation?

**KSI-MLA-07-Q048**: Can your organization track AI model provenance from training dataset selection through deployment with cryptographic integrity validation?

**KSI-MLA-07-Q049**: What visibility do you have into AI model supply chains (data providers, annotation services, training platforms, model registries, deployment infrastructure)?

### Section 12: Hallucination and Output Quality Events

**KSI-MLA-07-Q050**: What event types are defined for detecting and logging AI model hallucinations (false information generation), and what is the detection accuracy and false positive rate?

**KSI-MLA-07-Q051**: Are hallucination detection events captured with sufficient context (input prompt, model output, ground truth comparison, confidence scores) to enable root cause analysis?

**KSI-MLA-07-Q052**: For multi-model orchestration scenarios where agents coordinate multiple AI models, what event types capture model selection decisions, inter-model dependencies, and orchestration failures?

**KSI-MLA-07-Q053**: When agents employ ensemble methods or model voting, are the individual model predictions, voting weights, and final consensus decisions all logged as distinct event types?

### Section 13: Event Retention and Immutability

**KSI-MLA-07-Q054**: Are event logs stored in immutable, append-only format with cryptographic sealing preventing modification?

**KSI-MLA-07-Q055**: What is your immutable log retention policy? Can organizations extend retention for regulatory compliance (EU AI Act requires documentation retention periods)?

**KSI-MLA-07-Q056**: Can you detect and report log tampering (deletion, modification, or gaps) within specified timeframes?

### Section 14: Event Correlation and Forensic Capability

**KSI-MLA-07-Q057**: Can you correlate events across: (1) inference requests to training data lineage, (2) downstream business impact to contributing model versions, and (3) error propagation through multi-stage AI pipelines?

**KSI-MLA-07-Q058**: For a documented past incident, can you retrieve complete event trails enabling reconstruction of the attack sequence, impact scope, and remediation validation?

**KSI-MLA-07-Q059**: What is the historical data retention period and does it support forensic investigation of incidents occurring 6 months, 1 year, or longer ago?

**KSI-MLA-07-Q060**: Are event logs protected with access controls limiting retrieval to authorized security and audit personnel?

**KSI-MLA-07-Q061**: Is access to event logs (including queries and exports) itself logged to prevent unauthorized investigation or log manipulation?

**KSI-MLA-07-Q062**: What procedures ensure evidence integrity during export, analysis, and presentation for compliance validation or regulatory investigation?

### Section 15: Event Correlation Across AI Decisions

**KSI-MLA-07-Q063**: For complete AI decision reconstruction (loan approval, medical diagnosis, autonomous vehicle control), can you retrieve: model version, input data, feature transformations, reasoning chains, confidence scores, and output decisions?

**KSI-MLA-07-Q064**: For high-stakes AI decisions, can you retrieve and verify that all required decision context was captured and retained?

### Section 16: Event Type Governance and Evolution

**KSI-MLA-07-Q065**: Are event types, event generation procedures, and event correlation logic continuously reviewed and updated in response to emerging threats and regulatory changes?

**KSI-MLA-07-Q066**: What is the governance structure and meeting frequency for reviewing and updating event monitoring requirements?

**KSI-MLA-07-Q067**: Can the organization demonstrate that 100% of emerging AI threats identified in threat intelligence are reflected in event type definitions within 30 days of identification?

**KSI-MLA-07-Q068**: When incidents occur, is there a formal process to review whether events/logs captured were sufficient to detect and investigate the incident?

**KSI-MLA-07-Q069**: Are gaps in event definition (opportunities to detect future similar attacks) documented and remediated?

**KSI-MLA-07-Q070**: What percentage of incident post-mortems result in updated event type definitions?

**KSI-MLA-07-Q071**: Has the organization conducted threat modeling to identify the full spectrum of potential AI-specific attacks and validated that event types exist to detect each threat?

**KSI-MLA-07-Q072**: Are there documented gaps between detected threats and available event coverage?

**KSI-MLA-07-Q073**: What is the plan and timeline for remediating identified gaps?

### Section 17: Forensic Investigation and Evidence Collection

**KSI-MLA-07-Q074**: How are personally identifiable information (PII), protected health information (PHI), or trade secrets captured in event logs handled?

**KSI-MLA-07-Q075**: Are sensitive data fields tokenized, masked, or segregated while maintaining audit trail utility?

**KSI-MLA-07-Q076**: How are right-to-erasure requests handled without breaking audit trail completeness?

### Section 18: Event Type Coverage Validation

**KSI-MLA-07-Q077**: What percentage of event type coverage exists for traditional cloud monitoring (authentication, configuration, network, system events) vs. AI-specific event types?

**KSI-MLA-07-Q078**: For each of your deployed AI models, what granularity of model lifecycle events are logged?

**KSI-MLA-07-Q079**: How many event types from the 40-60+ AI-specific event types identified in research are actually monitored?

**KSI-MLA-07-Q080**: What catalog of documented AI event types is provided, and how does this compare to comprehensive event type requirements?

**KSI-MLA-07-Q081**: Can you detect and correlate attack indicators across: infrastructure logs, model behavior changes, training data integrity, and downstream business impact?

**KSI-MLA-07-Q082**: What is your organization's current detection effectiveness for AI-specific attacks: prompt injection, model poisoning, adversarial inputs, and supply chain compromises?

---

## Removed Questions (34 total) - Moved to Other KSIs

**Moved to KSI-CMT-01 (Change Logging and Monitoring Infrastructure)**:
- Q001: Event generation volume in events/second (infrastructure capacity question)
- Q002: SIEM and log aggregation infrastructure support for event volumes
- Q012: Stream processing infrastructure capacity and latency
- Q014: Event processing latency and <100ms SLA support
- Q018: Current detection effectiveness metrics for AI attacks
- Q021: Cryptographic signing and registry integrity validation
- Q022: Immutable event storage implementation details
- Q023: Tamper detection capability within 1 hour
- Q081-Q083: Forensic analysis capabilities and immutable format details
- Q118-Q123: SIEM platform selection, capacity, latency, and scaling procedures

**Moved to KSI-MLA-08 (Log Data Access Control)**:
- Q087-Q088: Log access controls and logging access to logs
- Q114: Access restrictions for event logs

**Moved to KSI-CED-01/02 (Training and Capability Building)**:
- Q108-Q110: SOC/IR team training on AI event types
- Q145-Q150: Maturity assessment, gap analysis, governance structures, executive sponsorship

**Moved to Privacy/Compliance KSI**:
- Q060-Q065: Data minimization, GDPR balance, tokenization, localization, multi-tenant log isolation
- Q084-Q086: PII/PHI handling in logs, tokenization/masking, right-to-erasure

**Moved to KSI-AFR-09 (Persistent Validation and Assessment)**:
- Q033-Q035: NIST AI RMF alignment, emerging AI regulations, governance structures for evolution
- Q099-Q103: Continuous review governance, threat intelligence integration, incident post-mortems
- Q111-Q113: Compliance evidence, audit reports, annual assessments

---

## Consolidated Questions (7 questions consolidated into 5)

**Consolidated: Inventory and Catalog Completeness**
- Original: Q003-Q005, Q066-Q068 (6 questions asking about inventory, shadow AI, update frequency, coverage, and documentation)
- Result: Integrated into KSI-MLA-07-Q001 and Q002 (inventory + event type definitions)

**Consolidated: Tamper Detection and Immutability**
- Original: Q022-Q023, Q057-Q058, Q083, Q089, Q095 (5 questions asking about immutable storage, tamper detection, evidence integrity, log gaps)
- Result:
  - KSI-MLA-07-Q054-Q056 (event retention, immutability, tamper detection in MLA-07)
  - Q021-Q023, Q081-Q083 moved to KSI-CMT-01 (infrastructure implementation details)

---

## Notes on Perspective Neutrality

All remaining questions have been rewritten to remove CIO/Customer/Auditor role distinctions. Questions previously phrased as:
- "Does your CSP provide..." → "Are you generating/providing..."
- "Can the organization demonstrate..." → "Can you demonstrate..."
- "What evidence can your CSP provide..." → "What evidence exists..."

This perspective-neutral format allows the question library to be applied across all stakeholder roles without duplication.

---

## Recommended Discovery Sequence

1. **Phase 1 - Foundation**: Questions Q001-Q008 (inventory and event type definitions)
2. **Phase 2 - AI-Specific Events**: Questions Q023-Q053 (novel AI event types)
3. **Phase 3 - Security**: Questions Q033-Q037 (threat detection events)
4. **Phase 4 - Completeness**: Questions Q009-Q022 (event generation and coverage)
5. **Phase 5 - Operations**: Questions Q054-Q065 (retention, immutability, correlation, processing)
6. **Phase 6 - Continuous Improvement**: Questions Q066-Q082 (governance and evolution)

---

**Document Status**: Ready for Implementation
**Alignment**: FedRAMP 20x KSI-MLA-07, NIST SP 800-53 (AU-2, AU-12), NIST AI Risk Management Framework
**Generated**: January 2026
**Last Updated**: January 2026 (Post-Review Refinement)
