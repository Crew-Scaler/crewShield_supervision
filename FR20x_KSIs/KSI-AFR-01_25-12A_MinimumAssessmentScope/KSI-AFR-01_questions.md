# KSI-AFR-01: Minimum Assessment Scope for AI Systems
## Investigative Questions

### A1. AI Infrastructure Scope Complexity and Dynamic Documentation

**KSI-AFR-01-Q1**: Can all AI models, training infrastructure, inference endpoints, and associated data lineage be inventoried with automated discovery tools?

**KSI-AFR-01-Q2**: When AI infrastructure scales from zero to thousands of compute nodes, how are scope changes tracked in real-time?

**KSI-AFR-01-Q3**: Are infrastructure changes logged with timestamps sufficient to reconstruct what resources existed at any point in the past 30 days?

**KSI-AFR-01-Q4**: What is the timeline for detecting that a new AI model was deployed in a production environment?

**KSI-AFR-01-Q5**: Are alerts configured when new models enter scope beyond pre-authorized deployments?

**KSI-AFR-01-Q6**: For shared AI infrastructure serving multiple federal customers, how are isolation boundaries documented to prevent scope leakage between customers?

**KSI-AFR-01-Q7**: Can it be proven that one customer's training data does not influence another customer's inference results through technical controls?

**KSI-AFR-01-Q8**: Does automated scope discovery cover all AI resource categories: trained models, model checkpoints, inference caches, agent memory systems, vector stores, embeddings, training data lineage, and artifact storage?

**KSI-AFR-01-Q9**: Can sub-5-minute scope change detection latency be achieved for critical AI infrastructure modifications?

### A2. Autonomous Agent Behavior and Resource Discovery Risk

**KSI-AFR-01-Q10**: How many agentic AI systems are currently operational, and for each, what is the complete scope of tools and APIs they can access?

**KSI-AFR-01-Q11**: Has the complete set of systems agents could potentially reach through API chaining or cloud metadata discovery been documented?

**KSI-AFR-01-Q12**: If an agent were granted access to cloud metadata endpoints and infrastructure APIs, how many additional systems would become accessible beyond explicitly authorized ones?

**KSI-AFR-01-Q13**: Could agents discover and access data in other accounts through autonomous exploration of cloud services?

**KSI-AFR-01-Q14**: Could an agent impersonate a human user or another agent through delegation chains or credential exploitation?

**KSI-AFR-01-Q15**: Have scenarios been tested where a compromised agent attempts to exploit another agent through trust relationships?

**KSI-AFR-01-Q16**: Is monitoring infrastructure available to detect agent misbehavior in real-time, including unauthorized API calls, data exfiltration attempts, and lateral movement?

**KSI-AFR-01-Q17**: What is the mean time to detect (MTTD) for agent-based attacks attempting scope violations?

**KSI-AFR-01-Q18**: Has a governance decision been made regarding agent tool access restrictions (limiting autonomy with pre-approved APIs) versus broader agent autonomy with real-time behavioral monitoring?

### A3. Persistent Agent Memory and Multi-Tenant Isolation

**KSI-AFR-01-Q19**: How are agent memory systems architectured, and is memory isolated per-customer, per-user, or shared across users within a customer?

**KSI-AFR-01-Q20**: What controls prevent one customer's interaction history from influencing another customer's agent results in shared infrastructure?

**KSI-AFR-01-Q21**: Has memory isolation been tested by fine-tuning an agent on one customer's data and verifying another customer's agent remains unaffected?

**KSI-AFR-01-Q22**: Could caching optimizations enable side-channel information leakage between customers?

**KSI-AFR-01-Q23**: Could timing analysis reveal information to one customer based on another customer's cached queries?

**KSI-AFR-01-Q24**: When customer sessions end or customers are offboarded, how quickly and thoroughly is their data purged from agent memory systems?

**KSI-AFR-01-Q25**: Are automated purging procedures available with cryptographic verification of deletion for federal data?

**KSI-AFR-01-Q26**: If shared models are fine-tuned with customer-specific data, how is cross-customer contamination prevented?

**KSI-AFR-01-Q27**: Is fine-tuning performed per-customer with isolated models, or is it applied to shared foundation models affecting all users?

**KSI-AFR-01-Q28**: Can complete memory isolation between federal customers sharing agent infrastructure be guaranteed through technical controls?

### A4. AI-Specific Scope Violation Detection and Incident Impact

**KSI-AFR-01-Q29**: Do incident response playbooks include AI-specific scenarios covering scope violations such as cross-tenant memory contamination and unauthorized agent access?

**KSI-AFR-01-Q30**: Are detection mechanisms available for hallucination-induced federal data integrity violations or scope-affecting incidents?

**KSI-AFR-01-Q31**: What is the mean time to detect (MTTD) for critical AI incidents that represent scope violations or changes in effective scope?

### A5. Third-Party AI Components and Supply Chain Impact on Scope

**KSI-AFR-01-Q32**: Are third-party pre-trained models verified for integrity and provenance using cryptographic hashing or digital signing?

**KSI-AFR-01-Q33**: Can it be detected if a downloaded model was tampered with between source and deployment?

### A6. Continuous Validation Evidence Generation and Collection

**KSI-AFR-01-Q34**: What evidence streams can be generated automatically showing dynamic scope documentation, agent behavioral compliance, model performance metrics, supply chain integrity, and incident response readiness?

**KSI-AFR-01-Q35**: Can federal auditors access evidence through APIs or standardized formats (JSON, CSV), or must evidence be manually compiled?

**KSI-AFR-01-Q36**: Do monitoring systems capture all evidence streams necessary for FedRAMP 20x AI continuous validation: infrastructure inventory, model performance, behavioral anomalies, drift detection, audit trails, supply chain integrity, identity and access, and incident indicators?

**KSI-AFR-01-Q37**: Can historical evidence be reconstructed showing control effectiveness over the past 6+ months, or only current state?

**KSI-AFR-01-Q38**: Are audit trails tamper-proof with cryptographic integrity guarantees enabling federal auditors to verify evidence was not altered?

**KSI-AFR-01-Q39**: Is evidence generation automated through APIs and telemetry collection, or does it require manual report compilation?

**KSI-AFR-01-Q40**: How frequently is evidence generated for each monitoring stream (real-time, hourly, daily)?

**KSI-AFR-01-Q41**: Does evidence generation process align with FedRAMP 20x continuous validation requirements rather than older annual assessment models?

**KSI-AFR-01-Q42**: What percentage of required AI security evidence can be generated automatically versus requiring manual intervention?

**KSI-AFR-01-Q43**: Is machine-readable evidence available demonstrating AI security control effectiveness that supports automated compliance assessment?

### A7. Organizational Processes for Maintaining Minimum Assessment Scope

**KSI-AFR-01-Q44**: Are documented processes available for maintaining the MAS for AI systems, including scope tracking, MAS documentation, and evidence collection?

---

## SECTION B: SCOPE DOCUMENTATION AND CHANGE DETECTION

### B1. AI Infrastructure Scope Documentation and Change Detection

**KSI-AFR-01-Q45**: When new AI models are deployed or training infrastructure is scaled, how quickly does scope documentation update?

**KSI-AFR-01-Q46**: Is scope change discovery automated through scanning, or does it require manual notification?

**KSI-AFR-01-Q47**: Is responsibility for maintaining accurate scope documentation clearly defined?

**KSI-AFR-01-Q48**: Is real-time visibility into scope changes available through API or dashboard showing what's in scope?

**KSI-AFR-01-Q49**: Is scope visibility provided through periodic reviews conducted at defined intervals, or is continuous real-time visibility available?

**KSI-AFR-01-Q50**: For multi-component AI deployments (training clusters, inference endpoints, embedding services, vector databases), does scope documentation capture all components?

**KSI-AFR-01-Q51**: Is ephemeral infrastructure that exists temporarily during training included in scope documentation?

**KSI-AFR-01-Q52**: Can evidence be provided that scope documentation is kept current through audits or third-party reviews validating accuracy?

**KSI-AFR-01-Q53**: What remedies exist if scope documentation is discovered to be inaccurate or incomplete?

**KSI-AFR-01-Q54**: Can sub-5-minute scope change detection for critical AI infrastructure be achieved?

### B2. Agent Access Control and Scope Boundary Enforcement

**KSI-AFR-01-Q55**: What prevents agents from discovering and accessing systems outside the authorized scope?

**KSI-AFR-01-Q56**: Are tool restrictions enforced at the platform level with cryptographic controls, or do they rely on agent prompt engineering?

**KSI-AFR-01-Q57**: If an agent is authorized to access an API, can that agent discover and access downstream systems through API chaining or metadata endpoints that have not been explicitly authorized?

**KSI-AFR-01-Q58**: Have agent privilege escalation scenarios been tested to verify that a compromised agent cannot impersonate another agent or human user?

**KSI-AFR-01-Q59**: What behavioral monitoring detects if an agent attempts unauthorized access beyond documented scope?

**KSI-AFR-01-Q60**: What is the timeline for detecting and stopping agent-based scope violations?

**KSI-AFR-01-Q61**: For multi-agent environments, can agents impersonate each other or exploit agent-to-agent trust relationships?

**KSI-AFR-01-Q62**: What prevents one agent from using another agent's credentials to access that agent's resources?

**KSI-AFR-01-Q63**: Is visibility into agent behavior provided through logs or dashboards showing API calls and resource access?

**KSI-AFR-01-Q64**: Is scope violation detection and response capability clearly defined with accountability for failures?

### B3. Memory Isolation in Multi-Tenant Infrastructure

**KSI-AFR-01-Q65**: If shared multi-tenant infrastructure is operated, how is memory isolated between customers?

**KSI-AFR-01-Q66**: Can one customer's interaction history influence another customer's agent responses in shared infrastructure?

**KSI-AFR-01-Q67**: If models are fine-tuned with customer data, is fine-tuning performed per-customer with isolated models, or applied to a shared foundation model affecting all users?

**KSI-AFR-01-Q68**: If shared fine-tuning is used, can customer data permanently contaminate other customers' agents?

**KSI-AFR-01-Q69**: Has third-party security assessment of memory isolation been conducted?

**KSI-AFR-01-Q70**: What controls prevent cache poisoning attacks where one customer's cached data influences another customer's results?

**KSI-AFR-01-Q71**: When a contract ends, is customer data automatically purged from agent memory systems, and how is purging verified?

**KSI-AFR-01-Q72**: Can deletion verification be provided confirming complete data removal from agent memory?

**KSI-AFR-01-Q73**: Is memory isolation guaranteed with defined accountability for breaches or cross-customer contamination?

**KSI-AFR-01-Q74**: What is the timeline for memory purging after contract termination or upon data removal request?

### B4. AI-Specific Incidents and Scope-Relevant Impact

**KSI-AFR-01-Q75**: If an incident occurs that changes the effective scope (such as unauthorized agent access reaching systems beyond documented scope), what is the notification timeline?

**KSI-AFR-01-Q76**: Are notification timelines for scope-affecting AI incidents defined?

**KSI-AFR-01-Q77**: Can evidence of incident response capability be provided through prior incident handling or exercise results?

### B5. Continuous Validation Evidence Access

**KSI-AFR-01-Q78**: Can real-time visibility be provided showing AI security control status including model inventory, vulnerability scan results, incident response readiness, supply chain integrity, and training data provenance?

**KSI-AFR-01-Q79**: Are evidence streams machine-readable (JSON APIs, CSV exports) or available as manual reports only?

**KSI-AFR-01-Q80**: If evidence is only available through manual reports, how frequently are they updated?

**KSI-AFR-01-Q81**: Can 6+ months of historical evidence be provided to enable lookback for reconstructing control effectiveness?

**KSI-AFR-01-Q82**: Are audit trails tamper-proof with cryptographic integrity so evidence integrity can be verified?

**KSI-AFR-01-Q83**: Does evidence collection align with FedRAMP 20x continuous validation requirements?

**KSI-AFR-01-Q84**: Is evidence access defined with accountability for access denial or delayed access?

**KSI-AFR-01-Q85**: What evidence is provided automatically versus requiring request?

**KSI-AFR-01-Q86**: Can evidence accessibility be demonstrated through real-time visibility or API access?

**KSI-AFR-01-Q87**: What is the timeline for fulfilling evidence access requests?

---

## SECTION C: EVIDENCE VALIDATION AND VERIFICATION

### C1. Automated Scope Detection System

**KSI-AFR-01-Q88**: Describe the automated scope detection system architecture: what systems does it scan, what triggers detection (scheduled, event-based), and what is the detection algorithm?

**KSI-AFR-01-Q89**: Provide historical data showing detection latency for infrastructure changes in the past 30 days, including deployment timestamps, detection timestamps, and calculated latency.

**KSI-AFR-01-Q90**: For scope changes that took greater than 5 minutes to detect, what were the root causes, and how frequently do these exceptions occur?

**KSI-AFR-01-Q91**: List all AI resource categories the detection system captures: trained models, model checkpoints, inference caches, agent memory systems, vector stores, embeddings, training data lineage, and artifact storage.

**KSI-AFR-01-Q92**: For multi-tenant environments, how does scope detection separate resources by customer to prevent cross-contamination in scope documentation?

### C2. Agent Behavioral Monitoring and Violation Detection

**KSI-AFR-01-Q93**: Describe how agent tool access is restricted - are restrictions enforced at platform level with cryptographic controls, or via prompt engineering?

**KSI-AFR-01-Q94**: Provide data showing unauthorized API access attempts, including what was attempted, when, by which agent, whether it was detected, and detection latency.

**KSI-AFR-01-Q95**: If no incidents occurred, provide test or simulation evidence showing that monitoring would detect violations.

**KSI-AFR-01-Q96**: Can an agent impersonate another agent or user, and what authentication mechanisms prevent impersonation?

**KSI-AFR-01-Q97**: For multi-agent environments, provide threat model analysis for agent-to-agent trust relationships and privilege escalation vectors.

### C3. Memory Isolation and Cross-Tenant Contamination

**KSI-AFR-01-Q98**: Describe the agent memory isolation architecture: how are memory spaces separated between customers (separate databases, encryption, logical segmentation)?

**KSI-AFR-01-Q99**: Have security tests been conducted to verify that one customer's interaction history cannot influence another customer's agent responses?

**KSI-AFR-01-Q100**: Are caching mechanisms used to optimize agent performance, and if yes, how are cache entries isolated by customer to prevent timing-based information leakage?

**KSI-AFR-01-Q101**: When a customer contract ends, describe the purging process: is purging automated or manual, how is purging verified, and can deletion logs or cryptographic verification be provided?

### C4. Continuous Evidence Generation and Verification

**KSI-AFR-01-Q102**: Describe the continuous evidence generation system: what evidence streams exist, how frequently is evidence generated, and is generation automated or manual?

**KSI-AFR-01-Q103**: How is evidence accessed - via APIs, download, or manual reports - and what formats is evidence available in (JSON, CSV, XML, PDF)?

**KSI-AFR-01-Q104**: Demonstrate historical evidence access by retrieving evidence from 3 months ago, 6 months ago, and current, showing data is queryable and accurate.

**KSI-AFR-01-Q105**: How is evidence protected from tampering - is it cryptographically signed or hashed to ensure integrity?

**KSI-AFR-01-Q106**: How does continuous evidence generation align with FedRAMP 20x requirements for dynamic scope, agent behavior, model integrity, supply chain, and incidents?

---

## SECTION D: SPECIALIZED SCOPE EDGE CASES

### D1. Distributed Training and Federated Learning Scope

**KSI-AFR-01-Q107**: For federated learning deployments, how is scope documented when training occurs across multiple organizations or geographic boundaries?

**KSI-AFR-01-Q108**: Can data lineage be traced for models trained through federated learning to identify all contributing data sources?

**KSI-AFR-01-Q109**: How are scope boundaries maintained when model updates are aggregated from distributed training nodes?

**KSI-AFR-01-Q110**: What controls prevent unauthorized scope expansion when federated learning nodes autonomously contribute to model training?

### D2. Model Lifecycle Scope and Portability

**KSI-AFR-01-Q111**: When a trained model is exported from the provider's environment, how is it ensured that federal data embedded in model parameters remains protected?

**KSI-AFR-01-Q112**: Do exported models retain the same scope and classification requirements as the training environment?

**KSI-AFR-01-Q113**: What controls prevent model export to unauthorized destinations outside documented scope?

**KSI-AFR-01-Q114**: How is scope tracked when models are transferred between development, staging, and production environments?

### D3. Synthetic Data and Derived Information Scope

**KSI-AFR-01-Q115**: For synthetic data generated from federal information sources, does the synthetic data inherit scope and classification from source data?

**KSI-AFR-01-Q116**: How is scope documented for AI-generated derivatives (summaries, analyses, recommendations) based on federal data?

**KSI-AFR-01-Q117**: What controls prevent synthetic data from leaking information about underlying federal datasets?

**KSI-AFR-01-Q118**: Can synthetic data be excluded from scope if it is sufficiently anonymized, and what verification is required?

### D4. Cross-Domain Information Aggregation Monitoring

**KSI-AFR-01-Q119**: For agents operating across security boundaries, how is monitoring performed for information aggregation attacks where low-sensitivity data combines to infer classified information?

**KSI-AFR-01-Q120**: What controls detect when agents aggregate data from multiple domains to create higher-classification information?

**KSI-AFR-01-Q121**: Can evidence be provided that cross-domain agent behavior is monitored for unauthorized information aggregation?

---
