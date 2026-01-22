# KSI-CED-04: Incident Response and Disaster Recovery Training
## Curated Question Library for AI/Agent Context

**KSI Requirement**: Persistently review the effectiveness of role-specific training for incident response and disaster recovery personnel.

**AI/Agent Focus**: This KSI addresses the fundamental transformation of IR/DR training in the AI era, where personnel must handle AI-specific incidents (model drift, hallucinations, bias, agent coordination failures), understand AI agent limitations (70% failure rate on complex tasks), validate autonomous failover decisions, and execute stateful AI recovery procedures beyond traditional infrastructure restoration.

**Document Version**: 1.0
**Generated**: 2026-01-12
**Original Question Count**: 63
**Questions Removed**: 8
**Questions Added**: 7
**Final Question Count**: 62

---

## Section 1: AI-Specific Incident Response Training

### Cluster: AI Incident Recognition and Classification

**CED-04-Q001**
Does your incident response training currently cover AI-specific incident categories including model drift detection, hallucination incidents, bias and fairness incidents, multi-agent coordination failures, and AI infrastructure operational failures?

**CED-04-Q002**
Have you created incident classification procedures that distinguish AI operational incidents (model degradation, hallucinations, bias) from traditional cybersecurity incidents (unauthorized access, malware, data exfiltration)?

**CED-04-Q003**
What percentage of your IR personnel have received training on AI system failure modes and can effectively diagnose whether performance issues result from model degradation, data quality problems, or infrastructure failures?

**CED-04-Q004**
Does your training prepare personnel to recognize AI model poisoning incidents, including detection of compromised training data, backdoor triggers, and adversarial perturbations in production models?

**CED-04-Q005**
Have you developed training procedures for responding to prompt injection attacks, including direct injection, indirect injection via data sources, and jailbreak attempts bypassing AI safety controls?

**CED-04-Q006**
Does IR training address AI supply chain compromise incidents, including compromised model repositories, poisoned pre-trained models, and malicious third-party AI components?

### Cluster: AI Agent Failure and Coordination

**CED-04-Q007**
Does your training explicitly address AI agent operational limitations, including the 70% failure rate on complex multi-step tasks, context window exhaustion, and memory corruption during extended operations?

**CED-04-Q008**
Have you trained personnel to recognize when AI assistance becomes unreliable during incidents and execute critical procedures manually when AI systems fail or provide unreliable recommendations?

**CED-04-Q009**
Do your training scenarios include multi-agent coordination failure situations where autonomous agents execute conflicting actions, creating cascading incidents that amplify operational impact?

**CED-04-Q010**
What training exists for diagnosing and responding to AI agent memory corruption or cognitive drift during extended incident response operations?

**CED-04-Q011**
Have you developed procedures and training for personnel to detect context window exhaustion in AI assistance tools during complex incident investigations?

### Cluster: AI Infrastructure and Operational Incidents

**CED-04-Q012**
Does training cover AI infrastructure-specific failure modes including GPU/TPU resource exhaustion, AI service API outages (AWS Bedrock, Azure OpenAI, Google Vertex AI), and AI platform degradation?

**CED-04-Q013**
Are personnel trained to recognize and respond to bias and fairness incidents where AI systems exhibit discriminatory behavior in production, including procedures for impact containment and stakeholder escalation?

**CED-04-Q014**
Does training address hallucination incidents in customer-facing AI systems, including procedures for customer notification, system rollback, and impact assessment?

---

## Section 2: Human-AI Decision Making and Override

### Cluster: AI Override Competency

**CED-04-Q015**
Have you developed training addressing human-AI override decision-making frameworks that guide personnel on when to trust versus override AI recommendations during time-critical incidents?

**CED-04-Q016**
Do training scenarios include situations where AI-provided incident response recommendations are incorrect, misleading, or based on hallucinated information, requiring personnel to recognize and override autonomous suggestions?

**CED-04-Q017**
Can personnel validate AI-recommended failover and recovery actions against their domain knowledge before execution during critical disaster recovery operations?

**CED-04-Q018**
What training exists for maintaining incident response capability when AI assistance systems are completely unavailable due to infrastructure failures or security incidents affecting AI platforms?

**CED-04-Q019**
Have you implemented training on recognizing AI-generated incident response procedures that reference non-existent APIs, deprecated tools, or hallucinated service capabilities?

---

## Section 3: Disaster Recovery for AI Systems

### Cluster: AI-Specific DR Requirements

**CED-04-Q020**
Have you mapped all AI infrastructure dependencies across cloud providers and regions, and does your DR training explicitly address AI-specific dependencies including model serving infrastructure, training pipelines, and AI service integrations?

**CED-04-Q021**
Does DR training address stateful AI system recovery procedures including memory snapshot restoration, training state consistency verification, and cognitive coherence validation?

**CED-04-Q022**
Have you defined Agentic Mean Time to Recovery (MTTR-A) separately from traditional RTO/RPO calculations to account for AI agent cognitive recovery time beyond infrastructure restoration?

**CED-04-Q023**
Does training address the risks of emergency model retraining during disasters, specifically catastrophic forgetting where previously learned patterns are irreversibly lost during rapid retraining?

**CED-04-Q024**
Are personnel trained on federated learning disaster recovery procedures including coordination across federated participants, handling participant failures during recovery, and ensuring distributed training consistency?

### Cluster: Autonomous Failover and Recovery Validation

**CED-04-Q025**
When AI systems automatically execute failover decisions, does training enable personnel to understand autonomous decision logic and validate correctness before declaring full recovery?

**CED-04-Q026**
Have you developed training for manual failover execution procedures when AI-assisted disaster recovery tools are unavailable or unreliable during actual disasters?

**CED-04-Q027**
Do DR scenarios include situations where autonomous AI failover decisions are suboptimal or incorrect, requiring human override to prevent incomplete or failed recovery?

**CED-04-Q028**
Does training include procedures for validating that all dependent AI services are available and functioning correctly before declaring disaster recovery complete?

**CED-04-Q029**
Are personnel trained to recognize incomplete recovery scenarios where infrastructure has restored but AI system cognitive state, agent memory, or model serving capabilities remain unavailable?

### Cluster: DR Testing and Validation

**CED-04-Q030**
Does your organization conduct annual DR tests only, or have you implemented continuous automated disaster recovery testing specifically for AI infrastructure and dependencies?

**CED-04-Q031**
Do DR test scenarios include AI-specific failure modes such as model poisoning affecting recovery systems, AI dependency service failures during recovery, and agent coordination failures during autonomous failover?

**CED-04-Q032**
Have you incorporated chaos engineering experiments for AI infrastructure resilience, and does training prepare personnel to respond to failures discovered during chaos testing?

**CED-04-Q033**
How do you validate the realism of synthetic AI disaster scenarios used in training, ensuring they accurately represent actual AI system failure modes rather than theoretical situations?

---

## Section 4: Training Content Quality and Validation

### Cluster: AI-Generated Content Validation

**CED-04-Q034**
If AI tools generate or maintain incident response training materials, have you implemented quality control procedures including hallucination detection and fact-verification against actual service documentation?

**CED-04-Q035**
Are external references in training materials (APIs, procedures, service capabilities) fact-checked against official documentation to prevent training on hallucinated or deprecated capabilities?

**CED-04-Q036**
What is your content currency review cycle for AI-specific training materials, and can you demonstrate training updates within 30 days of significant AI service changes, API deprecations, or capability evolutions?

**CED-04-Q037**
Have you established procedures for detecting and removing AI-generated training scenarios that fabricate threat intelligence, cite non-existent tools, or teach ineffective response procedures?

### Cluster: Training Content Scope and Evolution

**CED-04-Q038**
How has your IR/DR training content evolved since AI systems became central to operations, and what documented gaps exist between traditional training and current AI operational reality?

**CED-04-Q039**
Do you conduct quarterly threat landscape reviews specifically for AI attack techniques, and is training systematically updated to address emerging threats such as new prompt injection methods or model exploitation vectors?

**CED-04-Q040**
Are bias and fairness considerations incorporated into incident response training scenarios, ensuring personnel understand these as operational incidents requiring response rather than purely technical issues?

**CED-04-Q041**
Does training content reflect actual AI incident patterns your organization experiences, or is it based on generic scenarios that don't translate to operational capability?

---

## Section 5: Training Effectiveness Measurement

### Cluster: Performance-Based Metrics

**CED-04-Q042**
What metrics currently define "effective" IR/DR training in your organization - are you relying primarily on completion rates and satisfaction scores, or have you implemented performance-based measurement systems?

**CED-04-Q043**
Do you conduct 3-6 month behavioral observation periods post-training, tracking actual incident response tool usage, response time improvements, and error rate changes in real incidents?

**CED-04-Q044**
Have you implemented incident-based validation where personnel performance during actual incidents is measured against training expectations and documented capability gaps feed directly into training updates?

**CED-04-Q045**
Can you quantify the "adoption gap" between training completion rates and actual AI incident response tool adoption when personnel face real incidents?

**CED-04-Q046**
Do you track Mean Time to Detect (MTTD) and Mean Time to Respond (MTTR) pre-training and post-training, demonstrating operational improvements attributable to training investments?

**CED-04-Q047**
Have you implemented error rate tracking for AI-assisted incident response operations, measuring whether trained procedures reduce mistakes during critical response activities?

### Cluster: Long-Term Effectiveness Validation

**CED-04-Q048**
Do you conduct 12-24 month ROI validation of training investments, documenting productivity improvements, cost savings, or incident outcome improvements attributable to enhanced personnel capability?

**CED-04-Q049**
Is actual AI tool usage during incidents monitored and logged, replacing self-reported usage claims that research shows run 40-60% higher than reality?

**CED-04-Q050**
Do tabletop exercises and scenario assessments include observation of personnel performance with documented competency scoring, or do they primarily verify attendance and participation?

**CED-04-Q051**
When actual incidents occur, do post-incident reviews explicitly assess whether personnel executed trained procedures effectively, and are identified capability gaps converted to training updates within 30 days?

---

## Section 6: Continuous Learning and Improvement

### Cluster: Incident-to-Training Feedback

**CED-04-Q052**
Do you have systematic processes that convert incident after-action reviews into specific training updates, and what is your typical timeline between incident occurrence and training content updates?

**CED-04-Q053**
Are incident review workflows structured to explicitly document training gaps, and is remediation tracked to ensure identified gaps result in actual training improvements?

**CED-04-Q054**
Does your organization implement real-time playbook updates as AI services change APIs and capabilities, or does training content remain static until scheduled annual reviews?

**CED-04-Q055**
Have you established trigger-based training updates where specific incident patterns (repeated failures, emerging threat techniques) automatically initiate training content development?

### Cluster: Persistent Effectiveness Review

**CED-04-Q056**
What processes demonstrate "persistent" (continuous, ongoing) effectiveness review of IR/DR training as opposed to periodic compliance documentation exercises?

**CED-04-Q057**
How frequently does your training content substantively evolve - is evolution reactive (after incidents occur) or proactive (continuous monitoring of AI threat landscape and capability changes)?

**CED-04-Q058**
Do you implement continuous automated analytics that identify training effectiveness gaps from actual incident performance data without requiring manual analysis?

---

## Section 7: Regulatory Compliance and Audit Readiness

### Cluster: Compliance Evidence

**CED-04-Q059**
How do you demonstrate "persistent effectiveness review" compliance to FedRAMP auditors - what specific evidence beyond completion rates can you produce to substantiate continuous effectiveness monitoring?

**CED-04-Q060**
If auditors request performance metrics proving training effectiveness, can you provide behavioral observation data, incident outcome improvements, and operational capability evidence?

**CED-04-Q061**
Have you explicitly documented compliance with KSI-CED-04 requirements, and would regulatory auditors confirm your self-assessment based on your measurement approaches and evidence collection?

### Cluster: Organizational Capability Validation

**CED-04-Q062**
If AI systems became completely unavailable during a major incident, could your personnel execute critical incident response and disaster recovery procedures manually with effectiveness comparable to AI-assisted operations?

---

## Related KSI Connections

**KSI-CED-01 (General Training)**: Questions on general AI awareness belong in CED-01; CED-04 focuses specifically on IR/DR role competency

**KSI-CED-02 (Role-Specific Training)**: Questions on privileged user training design belong in CED-02; CED-04 focuses on training effectiveness measurement and continuous review for IR/DR roles specifically

**KSI-CMT-01 (Log and Monitor Changes)**: Questions on logging AI incidents belong in CMT-01; CED-04 addresses whether personnel are trained to investigate those logged incidents

**KSI-CMT-03 (Automated Testing)**: Questions on AI system testing belong in CMT-03; CED-04 addresses whether DR personnel can execute recovery when automated testing reveals failures

---

## Question Application Guidance

**For CIOs and Leadership**:
- Focus on questions CED-04-Q001 through CED-04-Q019 (strategic training gaps)
- Questions CED-04-Q042 through CED-04-Q051 (effectiveness measurement transformation)
- Questions CED-04-Q056 through CED-04-Q062 (compliance and capability validation)

**For CSP Assessment Teams**:
- Focus on questions CED-04-Q020 through CED-04-Q033 (DR capability validation)
- Questions CED-04-Q034 through CED-04-Q041 (content quality assessment)
- Questions CED-04-Q059 through CED-04-Q062 (evidence for compliance)

**For Auditors**:
- Focus on questions CED-04-Q042 through CED-04-Q058 (measurement methodology)
- Questions CED-04-Q059 through CED-04-Q062 (regulatory compliance evidence)
- Cross-reference questions CED-04-Q001 through CED-04-Q014 (scope coverage validation)

**For IR/DR Personnel and Managers**:
- Focus on questions CED-04-Q001 through CED-04-Q019 (operational competency)
- Questions CED-04-Q020 through CED-04-Q033 (DR procedures and execution)
- Questions CED-04-Q052 through CED-04-Q055 (continuous improvement feedback)

---

## Section 8: Organizational Competency for AI-Driven Recovery

### Cluster: Team Capability and Skill Validation

**CED-04-Q063**
What organizational competency maintenance mechanisms ensure the technical team can effectively oversee, validate, and execute AI-driven disaster recovery operations during actual incidents? Specifically: (a) skill gap analysis for AI-driven recovery procedures, (b) cross-training to ensure multiple team members understand autonomous agent decision-making, (c) knowledge transfer mechanisms for complex AI-specific recovery procedures, (d) validation that competency improvements translate to incident response capability, (e) regular assessment of whether skill gaps would prevent effective incident response using autonomous agents. [Moved from KSI-RPL-02 per issue #42]

**CED-04-Q064**
How do you maintain staff competency in AI recovery procedures, particularly manual recovery (preventing skill atrophy from over-reliance on automation)? Provide: (a) training programs for manual AI recovery procedures, (b) regular manual recovery drills keeping staff sharp, (c) periodic disabling of automation for manual practice exercises, (d) competency assessments validating staff capability for manual recovery without automation, (e) hiring strategy ensuring AI recovery expertise is built and maintained. [Moved from KSI-RPL-01 per issue #41]

---

## References

**Source Documents**:
- KSI-CED-04 Report: Issue #216 (4,200 words, 122 peer-reviewed sources)
- KSI-CED-04 Cluster Synthesis: 8 clusters addressing AI/agent training transformation
- Discovery Questions: Original 63 questions across 4 stakeholder perspectives

**Key Research Foundations**:
- AI agent failure rates: 70% on complex multi-step tasks (CMU study)
- Model degradation: 91% of ML models experience drift over time
- Training adoption gap: Only 33% adopt AI tools post-training despite completion
- Self-reported vs. actual usage: 40-60% overestimation documented
- Behavioral observation windows: 3-6 months minimum for valid assessment
- ROI validation timelines: 12-24 months for productivity measurement

**Regulatory Context**:
- FedRAMP 20x KSI-CED-04: Persistent effectiveness review requirement
- NIST Cybersecurity Framework: Incident response competency validation
- ISO/IEC 27035: Incident management training effectiveness standards

---

**Document Status**: Ready for Human Review and Approval
**Next Steps**: Upon approval, generate CED-04_questions_global.json and CED-04_questions_binding.json
