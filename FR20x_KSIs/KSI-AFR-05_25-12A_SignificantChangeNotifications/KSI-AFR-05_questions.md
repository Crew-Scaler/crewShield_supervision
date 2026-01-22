# KSI-AFR-05: Significant Change Notifications - Investigative Questions

## Summary Statistics

- **Original question count**: 95
- **Questions removed in initial curation**: 12 (duplicates and irrelevant)
- **Questions added initially**: 18 (new relevant questions)
- **Initial refined count**: 101

**After Fine-Tuning Review (Issue #52 Guidance)**:
- **Questions removed**: 5 (weak AFR-05 specificity)
- **Questions moved to CMT-03**: 5 (testing/validation focus)
- **Questions moved to CMT-01**: 8 (logging/monitoring focus)
- **Final AFR-05 question count**: 83

### Questions Removed (Weak AFR-05-Specific Content)
- Q016: Volume question on agent capability discovery frequency
- Q038: Generic testing depth/coverage question
- Q039: Generic testing confidence level threshold
- Q059: Upstream provider SLA question (better fit in supply chain or CMT-01)
- Q079: Overlaps with other advance notice questions

### Questions Moved to KSI-CMT-03 (Automated Testing & Validation)
- Q036-Q037: Testing strategy and validation methods
- Q041: Canary deployment testing approaches (kept Q42-Q43 in AFR-05 as notification-specific)
- Q044-Q045: Statistical validation and emergent behavior testing

### Questions Moved to KSI-CMT-01 (Logging & Monitoring of Changes)
- Q046-Q050: Audit trail completeness and gap detection
- Q054-Q055: Lineage tracking and change chain reconstruction
- Q062: Audit visibility across partner organizations

### Key Changes Summary
- Consolidated testing/validation to CMT-03 for cleaner separation of concerns
- Moved logging/audit questions to CMT-01 to focus AFR-05 on "notification decision logic"
- Kept notification-linked questions (e.g., Q42-Q43 on canary deployments and notification timing)
- Maintained supply chain questions critical to AFR-05 notification decisions

---

### Change Classification & Detection

**KSI-AFR-05-Q1**: Your organization currently generates 15-20 significant configuration changes daily in AI-enabled systems. How are you currently classifying these changes into the FedRAMP four-tier categorization framework (Routine, Adaptive, Transformative, Impact)?

**KSI-AFR-05-Q2**: What percentage of AI-driven changes are classified automatically vs. requiring manual review?

**KSI-AFR-05-Q3**: What are your false positive and false negative rates for automated classification?

**KSI-AFR-05-Q4**: The traditional FedRAMP change categorization was designed for discrete changes (1-3 per quarter). Do you have quantitative thresholds defining when AI changes become "significant"?

**KSI-AFR-05-Q5**: At what accuracy change percentage (e.g., ±2%, ±5%) do you escalate to Transformative classification?

**KSI-AFR-05-Q6**: How do you handle model retraining cycles that occur daily but have minimal accuracy impact?

**KSI-AFR-05-Q7**: What latency increase percentage triggers Transformative vs. Adaptive classification?

**KSI-AFR-05-Q8**: AI systems operate with automated retraining cycles, drift detection, and auto-remediation. How do you balance compliance notification requirements with the reality that your system may self-remediate before you've notified stakeholders?

**KSI-AFR-05-Q9**: When drift is detected and auto-remediated within 2 hours, but FedRAMP requires post-implementation notification within 10 business days, how do you determine whether notification is still required?

**KSI-AFR-05-Q10**: Are you treating auto-remediated changes differently than manual changes?

**KSI-AFR-05-Q11**: Do you have documented classification thresholds for AI-specific metrics such as inference latency, false positive rate changes, fairness metric shifts, or embedding drift?

**KSI-AFR-05-Q12**: How do you classify changes to AI agent tool configurations, MCP server registrations, or prompt templates - are these treated as infrastructure changes, application changes, or a separate category?

**KSI-AFR-05-Q13**: What automated systems detect changes to model architectures, hyperparameters, training data sources, or inference pipelines, and how quickly do they classify these changes?

### Authorization Boundary Management

**KSI-AFR-05-Q14**: AI agents using MCP and similar frameworks discover and invoke services at runtime. Are your authorization boundaries defined statically at assessment time or dynamically as agents discover new services?

**KSI-AFR-05-Q15**: When an agent discovers a new capability (e.g., Lambda execution access) not in the original authorization baseline, does this trigger a Significant Change Notification?

**KSI-AFR-05-Q16**: What processes exist for approving newly discovered capabilities?

**KSI-AFR-05-Q17**: How do you document authorization boundaries for AI agent systems where the scope of agent tool access may expand continuously?

**KSI-AFR-05-Q18**: Is your authorization boundary documentation based on intended agent capabilities or actual runtime-discovered capabilities?

**KSI-AFR-05-Q19**: When actual capabilities exceed documented boundaries, what is your escalation process?

**KSI-AFR-05-Q20**: Do you maintain a registry of all MCP servers, tool APIs, or external services that AI agents are authorized to access, and is this registry kept synchronized with actual runtime access patterns?

**KSI-AFR-05-Q21**: How do you detect when an AI agent attempts to access a service or capability outside its authorized scope, and what automated responses are triggered?

### Notification & Compliance Processes

**KSI-AFR-05-Q22**: Your organization may generate 500-1000 SCN messages per day if all changes are notified. How do you manage this notification volume?

**KSI-AFR-05-Q23**: What percentage of changes actually result in Significant Change Notifications?

**KSI-AFR-05-Q24**: How do you prevent alert fatigue among FedRAMP and agency customer stakeholders?

**KSI-AFR-05-Q25**: What filtering logic reduces raw change volume to notifiable changes?

**KSI-AFR-05-Q26**: FedRAMP requires 30 business days advance notice for Transformative changes, but AI drift-remediation may be needed within hours. Can you provide advance notice for automatically triggered changes?

**KSI-AFR-05-Q27**: How do you reconcile advance notification requirements with automated, drift-triggered changes?

**KSI-AFR-05-Q28**: Do you have approved procedures allowing immediate implementation of critical changes with post-implementation notification?

**KSI-AFR-05-Q29**: How quickly do you detect, classify, and report significant changes to FedRAMP and agency customers?

**KSI-AFR-05-Q30**: What is your current mean time to detect (MTTD) for significant changes?

**KSI-AFR-05-Q31**: What is your mean time to notify (MTTN) after detection?

**KSI-AFR-05-Q32**: Are notifications sent within 24 hours of change implementation?

**KSI-AFR-05-Q33**: Do you provide machine-readable notification formats (JSON, XML) that include structured metadata such as model version, affected endpoints, data lineage references, and impact analysis?

**KSI-AFR-05-Q34**: How do you aggregate and summarize related changes (e.g., multiple model retraining runs in a day) to avoid overwhelming stakeholders while maintaining audit completeness?

### Notification-Linked Testing & Deployment

**KSI-AFR-05-Q35**: At what traffic percentage does a canary deployment constitute a "significant change" requiring notification?

**KSI-AFR-05-Q36**: How do you determine whether gradual rollouts need advance notification vs. post-implementation notification?

### Notification Documentation & Metadata

**KSI-AFR-05-Q37**: Do you document all required FedRAMP metadata for Significant Change Notifications?

**KSI-AFR-05-Q38**: Are Service Offering IDs, change type classifications, detailed descriptions, reasons for change, customer impact analyses, implementation timelines, authorization boundary impacts, and approver information documented?

**KSI-AFR-05-Q39**: For AI-specific changes: Are model versions, data versions, and affected endpoints documented?

### Supply Chain & Upstream Dependencies

**KSI-AFR-05-Q40**: Your organization likely uses upstream AI services (OpenAI GPT-4, Anthropic Claude, etc.) that release model updates on their schedule. When these upstream services change, how do you detect the upstream change?

**KSI-AFR-05-Q41**: Does the upstream change require you to issue a Significant Change Notification to FedRAMP and agency customers?

**KSI-AFR-05-Q42**: What is your mean time to detect upstream provider changes?

**KSI-AFR-05-Q43**: If your organization uses federated learning with 3-5 partner organizations, when a partner organization changes their data or model, how do you detect this change?

**KSI-AFR-05-Q44**: Does partner-initiated change require you to notify stakeholders?

**KSI-AFR-05-Q45**: Do you maintain a software bill of materials (SBOM) or model bill of materials (MBOM) tracking all AI model dependencies, including foundation models, fine-tuning datasets, and API integrations?

**KSI-AFR-05-Q46**: How do you monitor for changes to open-source AI libraries, model frameworks, or inference engines that your systems depend on?

---

### Change Notification Delivery

**KSI-AFR-05-Q47**: When you receive Significant Change Notifications from CSPs, how quickly do you receive notifications (within 24 hours? same day? advance notice)?

**KSI-AFR-05-Q48**: Are notifications in both human-readable and machine-readable formats?

**KSI-AFR-05-Q49**: Do notifications clearly identify what changed, why, and what the impact is?

**KSI-AFR-05-Q50**: Can you integrate machine-readable notifications into your own monitoring systems?

**KSI-AFR-05-Q51**: Do CSP notifications provide sufficient information for your security teams to evaluate impact?

**KSI-AFR-05-Q52**: For AI model changes: Does the notification include model version, accuracy metrics, fairness/bias indicators, latency impact?

**KSI-AFR-05-Q53**: For infrastructure changes: Does the notification describe affected components and potential customer data impact?

**KSI-AFR-05-Q54**: For third-party integration changes: Does the notification explain upstream provider changes and implications?

**KSI-AFR-05-Q55**: Can you quickly determine whether the change affects your specific data or workloads?

**KSI-AFR-05-Q56**: When a CSP notifies you of a significant change, does the notification include CSP's impact analysis for your agency's workloads?

**KSI-AFR-05-Q57**: Can you verify the CSP's impact assessment independently?

**KSI-AFR-05-Q58**: Are you able to request the CSP to provide specific testing evidence that the change doesn't affect your data?

### Change Approval & Authorization

**KSI-AFR-05-Q59**: For Transformative changes, FedRAMP requires 30+ days advance notice. Does the CSP consistently provide sufficient advance notice?

**KSI-AFR-05-Q60**: When you receive advance notice, is it early enough for your agency to complete own impact assessment?

**KSI-AFR-05-Q61**: For urgent security changes, do CSPs have documented procedures for expedited notification?

**KSI-AFR-05-Q62**: FedRAMP requires CSPs to consult with agency customers before implementing Transformative changes. Does your CSP actively solicit your feedback on planned Transformative changes?

**KSI-AFR-05-Q63**: Does your CSP consider your feedback in final change implementation decisions?

**KSI-AFR-05-Q64**: Does your CSP notify you of changes to the planned implementation based on your feedback?

### Monitoring & Visibility

**KSI-AFR-05-Q65**: Can you access complete change history for CSP services your agency uses?

**KSI-AFR-05-Q66**: Can you retrieve notification records for the past 12-24 months?

**KSI-AFR-05-Q67**: Can you search notifications by change type, date range, or component affected?

**KSI-AFR-05-Q68**: Are change records retained through your agency's required audit periods?

**KSI-AFR-05-Q69**: How do you detect changes the CSP didn't notify you about?

**KSI-AFR-05-Q70**: Do you have independent monitoring detecting configuration or behavior changes?

**KSI-AFR-05-Q71**: Have you discovered undisclosed changes to CSP services?

**KSI-AFR-05-Q72**: What is your process for escalating undisclosed changes to CSP and FedRAMP?

**KSI-AFR-05-Q73**: For AI-enabled CSP services, does the CSP notify you of model updates and retraining cycles?

**KSI-AFR-05-Q74**: Are you aware of accuracy, fairness, or latency changes to models your agency depends on?

**KSI-AFR-05-Q75**: Does the CSP provide mechanisms for monitoring model behavior changes over time?

---

### Control Existence & Documentation Testing

**KSI-AFR-05-Q76**: Does the CSP have documented procedures for managing Significant Changes that satisfy FedRAMP requirements, and are these procedures current (updated within past 12 months)?

**KSI-AFR-05-Q77**: Do procedures address all four FedRAMP change types (Routine, Adaptive, Transformative, Impact)?

**KSI-AFR-05-Q78**: Do procedures specify roles and responsibilities for change classification, approval, notification, and assessment?

**KSI-AFR-05-Q79**: For AI systems specifically: Do procedures address continuous change scenarios, drift-triggered remediation, and agent capability discovery?

**KSI-AFR-05-Q80**: Does the CSP have established thresholds for classifying AI changes with quantitative metrics documented?

**KSI-AFR-05-Q81**: Does the CSP have current documentation of its authorization boundaries, including AI agent capability scope?

**KSI-AFR-05-Q82**: Are authorization boundaries updated when they change, and are there procedures for identifying when boundaries have changed?

---

## Questions Moved to KSI-CMT-03 (Automated Testing & Validation)

These questions focus primarily on testing strategy, validation methods, and quality assurance - core to CMT-03 responsibilities:

- **Original Q36**: Traditional deterministic testing (binary pass/fail) doesn't work for probabilistic AI systems. How do you validate that AI changes don't introduce unintended consequences?
- **Original Q37**: What types of tests validate model accuracy, fairness, latency, and security regressions?
- **Original Q41**: Do you use canary deployments (rolling out changes to 1-5% of traffic initially) for your AI systems?
- **Original Q44**: What statistical methods do you use to validate that stochastic AI behavior remains within acceptable bounds after a change, and what sample sizes are required?
- **Original Q45**: How do you test for emergent behaviors or multi-agent interactions that may only appear in production at scale?

**Action**: Integrate these questions into `/KSIs/KSI-CMT-03_25-12A_AutomatedTestingandValidation/CMT-03_questions.md` with appropriate renumbering to CMT-03's sequence.

---

## Questions Moved to KSI-CMT-01 (Logging & Monitoring of Changes)

These questions focus on audit trail completeness, logging infrastructure, and change record visibility - core to CMT-01 responsibilities:

- **Original Q46**: FedRAMP requires auditable records of all significant changes. For your AI systems, do you maintain complete, immutable audit trails across all change sources?
- **Original Q47**: What systems generate change records (Git, MLflow, Kubeflow, Vertex AI, Kubernetes, cloud provider APIs)?
- **Original Q48**: Are audit records from all these sources integrated and immutable?
- **Original Q49**: What percentage of actual changes have corresponding audit trail entries?
- **Original Q50**: Do you have a mechanism to detect gaps in your audit trail?
- **Original Q54**: Do you maintain lineage tracking from training data through models to inference endpoints, enabling impact analysis when any component changes?
- **Original Q55**: How do you reconstruct the complete chain of changes affecting a specific model or endpoint for incident investigation or compliance review?
- **Original Q62**: How do you maintain audit trail visibility across partner organizations?

**Action**: Integrate these questions into `/KSIs/KSI-CMT-01_25-12A_LogandMonitorChanges/CMT-01_questions.md` with appropriate renumbering to CMT-01's sequence.

---

## Notes on Question Development

This refined question library was developed based on:
- FedRAMP 20x KSI-AFR-05 requirements for Significant Change Notifications
- Analysis of AI/Agent-specific change management challenges including continuous operations, dynamic authorization boundaries, non-deterministic testing, and heterogeneous audit trails
- Review of implementation guidance covering change detection, classification, notification, testing, and audit infrastructure
- Issue #52 guidance for optimizing question distribution across related KSIs (CMT-01, CMT-03, AFR-05)
