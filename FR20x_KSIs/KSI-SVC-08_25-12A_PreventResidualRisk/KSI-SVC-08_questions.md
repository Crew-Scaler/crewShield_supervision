# KSI-SVC-08: Prevent Residual Risk - Question Library

**FedRAMP Control**: SC-4 (Information in Shared Resources), SC-7 (Boundary Protection)
**KSI Title**: Prevent Residual Risk
**Date Generated**: 2026-01-12
**Status**: Refined per GitHub Issue #64 Guidance
**Refinement Focus**: Removed duplicates, consolidated stakeholder perspectives, moved questions to appropriate KSIs

---

## Summary Statistics

**Original Question Count**: 27 (from prior refinement)
**Duplicates Consolidated**: 7
### SVC-08-Q01: Agent-Driven Infrastructure Changes and Decision-Level Audit Completeness

How does your organization maintain audit trails demonstrating that autonomous agent-initiated infrastructure changes are authorized and attributable for FedRAMP compliance?

**Sub-questions**:
- What decision-level audit trails do agents maintain (detection triggers, evaluation criteria, rejected alternatives, confidence thresholds, decision rationale)?
- How are multi-system infrastructure modifications attributed when agent-driven failures occur across distributed systems?
- What change rollback procedures exist for agent-initiated changes that create unintended residual elements, and how do you coordinate rollback with downstream systems already depending on those changes?
- For multi-agent coordination scenarios, how is decision dependency tracking documented to enable forensic reconstruction?
- How frequently are agent decision logs audited for completeness and retained for compliance reporting?

**Compliance Implication**: FedRAMP requires persistent review and justification of post-change residual elements. Autonomous agents lacking decision-level logging create compliance gaps preventing forensic reconstruction of why changes persisted.

**AI/Agent Context**: Autonomous agents collapse traditional change management review gates into milliseconds, creating residual elements outside established compliance frameworks. Attribution becomes critical when multi-agent systems create distributed state changes with partial failures. Multi-system transactions lack transactional guarantees, leaving state inconsistencies.

---

### SVC-08-Q02: Multi-Tenant Isolation Validation and Cross-Contamination Prevention

For multi-tenant infrastructure serving federal customers at different impact levels, how does your organization validate that residual elements from higher-impact customer workloads do not contaminate lower-impact customer systems?

**Sub-questions**:
- What GPU memory wiping procedures (aligned with NIST SP 800-88 guidelines) execute between tenant job transitions, and what validation confirms overwrites are cryptographically secure?
- What container image layer sharing detection procedures execute, and how frequently are shared nodes tested for residual files from previous tenants?
- What service mesh configuration cleanup procedures remove ingress rules, load balancer configurations, mTLS certificates, circuit breaker policies, and observability rules specific to terminated tenants?
- For high-impact federal workloads, do you employ confidential computing enclaves (AMD SEV, Intel SGX) providing hardware-enforced isolation instead of software-based cleanup?
- What end-to-end verification testing confirms that multi-tenant isolation cleanup succeeded without creating new residual elements?

**Compliance Implication**: Cross-tenant residual contamination represents unmitigated risk violating isolation assumptions federal customers depend on for FedRAMP authorization. SC-4 specifically addresses information in shared resources.

**AI/Agent Context**: GPU memory retains model weights and inference batch data between tenant workloads. Container caches and shared service mesh configurations create additional cross-tenant residual exposure vectors. Autonomous scaling and workload termination leave residual routing rules accessible to unintended workloads.

---

### SVC-08-Q03: Model Lifecycle and Ghost Data Governance

How does your organization manage residual data embedded in machine learning models used for federal customer services, and what verification demonstrates ghost data absence?

**Sub-questions**:
- What policies define how long raw training data persists after model training completes, and who enforces these policies?
- What membership inference testing methodology is applied (quarterly, post-update, post-fine-tuning), and what positive/negative decision thresholds indicate ghost data risk?
- When unlearning procedures are applied to remove ghost data, what verification methodology confirms unlearning effectiveness?
- What explicit documentation acknowledges unlearning limitations—specifically that ghost data absence cannot be definitively proven, only that specific detection methods fail?
- For multi-tenant models, what isolation validation procedures confirm that one customer's fine-tuning cannot extract another customer's training data?

**Compliance Implication**: Ghost data represents a fundamentally new residual category that FedRAMP assessors frequently do not address. Explicit governance and verification limitations demonstrate proactive risk management. SC-4 requires validation of information isolation in shared resources.

**AI/Agent Context**: Model parameters memorize training data extractable through membership inference attacks. Unlearning techniques cannot definitively prove information absence, only that detection methods fail. Multi-tenant model hosting risks federal data exposure between customers through fine-tuning contamination.

---

### SVC-08-Q04: Non-Human Identity Credential Lifecycle and Residual Access Prevention

Given AI workloads' dramatic increase in service account, API key, and temporary token sprawl, how does your organization manage credential lifecycle to prevent residual access from discontinued services?

**Sub-questions**:
- What quarterly NHI inventory audit process verifies each credential is still necessary, has expiration dates set (confirming no permanent credentials), and has access scope matching current workload requirements?
- When services discontinue, what procedures ensure credentials are removed from active systems and deleted from backups within acceptable windows?
- For hardcoded credentials discovered in artifacts (notebooks, container images, deployment manifests), what incident procedures trigger immediate revocation, artifact rebuild, and exposure investigation?
- How are audit findings (unnecessary credentials, missing expirations, overly-broad permissions) remediated and re-validated?
- What incident response scope analysis procedures use NHI inventory to quantify potentially compromised credentials' blast radius?

**Compliance Implication**: Credential residue from discontinued services creates persistent attack surface. Systematic NHI lifecycle management is foundational for incident response efficiency and FedRAMP SC-7 boundary protection compliance.

**AI/Agent Context**: A 30-second agent task receives credentials valid for 1 hour, leaving 59.5 minutes of unnecessary exposure. Hardcoded credentials in Jupyter notebooks, container images, and deployment manifests prevent cleanup on artifact updates. AI deployments dramatically increase non-human identity sprawl across service accounts, API keys, and temporary tokens.

---

### SVC-08-Q05: Ephemeral Infrastructure Residual Artifact Cleanup Coordination

AI workloads extensively use ephemeral compute (containers, functions, jobs) that create residual artifacts across multiple persistence systems. How does your organization coordinate cleanup across this heterogeneous environment?

**Sub-questions**:
- What declarative artifact lifecycle specifications automatically trigger cleanup across storage, databases, caches, credentials, and logging systems when a task completes?
- For training jobs creating multi-terabyte intermediate datasets "for the next run," what policies explicitly manage when this data is retained versus deleted?
- What verification procedures confirm that cleanup succeeded across all systems (e.g., deleting a model checkpoint removes it from all serving infrastructure caches, not just primary storage)?
- What testing demonstrates that Kubernetes persistent volumes, ConfigMaps, and Secrets are cleaned up when ephemeral workloads terminate?
- How do you detect forgotten artifacts left after workload termination (orphaned datasets, cached checkpoints, temporary credentials)?

**Compliance Implication**: Residual artifacts in secondary systems (forgotten model checkpoints, cached training datasets) create unquantified attack surface that traditional residual risk assessments miss. SC-4 requires validation that shared resource information is properly managed.

**AI/Agent Context**: Ephemeral containers create assumption of no persistent residue, but persistent volumes, ConfigMaps, Secrets, and cached datasets accumulate without explicit ownership cleanup rules. Expensive-to-regenerate artifacts encourage long retention of multi-terabyte training datasets.

---

### SVC-08-Q06: RAG Contamination and Vector Database Residual Cleanup

For Retrieval-Augmented Generation systems supporting AI agents or models, how does your organization manage residual information in vector databases when sensitive documents must be removed?

**Sub-questions**:
- When a document containing sensitive information (credentials, PII, classified data) is deleted, what procedures remove its semantic embeddings from vector databases?
- What verification confirms that semantically similar queries do not retrieve residual vector representations near deleted content?
- What re-embedding procedures balance completeness (removing all traces) against availability (service disruption during re-indexing)?
- For RAG systems shared across multiple customers, what isolation prevents one customer's document deletion from affecting other customers' retrieval?
- What documentation demonstrates that RAG cleanup procedures were tested and validated?

**Compliance Implication**: Vector database embeddings retain semantic representation of sensitive information even after source documents are deleted, creating information disclosure risks. SC-4 applies to shared knowledge bases.

**AI/Agent Context**: RAG systems embed documents into high-dimensional vector spaces where deletion requires re-embedding entire knowledge bases, an operation affecting service availability. Incomplete deletion enables residual information retrieval through semantic similarity. Multi-customer RAG systems require isolation validation.

---

### SVC-08-Q07: Configuration Drift Detection and Authorized Agent Modification Validation

How does your organization distinguish beneficial configuration drift from autonomous agents versus unauthorized changes that create residual risk?

**Sub-questions**:
- What agent decision frameworks document drift authorization criteria (which drift types are permissible, which require escalation)?
- How do drift detection systems identify legitimate agent-initiated changes without creating false positive operational friction?
- What audit trails track configuration changes including agent remediation rationale and decision triggers?
- What procedures validate that agent-driven drift does not leave residual configuration elements when agents correct each other's changes?
- How are drift detection systems tested to prevent baseline poisoning (attackers gradually shifting "normal" to hide compromise)?

**Compliance Implication**: FedRAMP requires infrastructure to match documented baselines. Agent-driven drift that compliance treats as unauthorized creates validation challenges for SC-7 boundary protection and SC-4 information management.

**AI/Agent Context**: Self-healing and optimization agents autonomously modify infrastructure without explicit IaC updates. Traditional drift detection cannot distinguish beneficial agent actions from malicious configuration changes. Multi-agent systems create drift through cross-agent corrections creating residual configuration accumulation.

---

### SVC-08-Q08: Prompt Injection Residual State and Recovery Procedures

When prompt injection attacks are detected affecting AI agents or RAG systems, what procedures identify and remediate residual state persisting beyond the attack session?

**Sub-questions**:
- What forensic investigation procedures identify all data stored in agent memory, vector databases, and tool execution logs during the attack window?
- How do you verify that injected instructions are completely removed from RAG knowledge bases without requiring full re-embedding?
- What behavioral monitoring detects residual effects from injection-driven tool executions that modified connected systems?
- What procedures validate that agent memory is completely cleared after injection-driven context pollution?
- For multi-agent systems, what procedures detect cross-session persistence of injected instructions in shared state?

**Compliance Implication**: Injection persistence represents residual threat affecting future agent operations. Post-compromise cleanup requires forensic analysis of all tool executions and state modifications to prevent recurring compromise.

**AI/Agent Context**: Malicious instructions stored in agent memory or RAG knowledge bases persist across sessions, enabling cross-session attack effects. Tool chain exploitation creates residual elements in connected systems (modified databases, executed commands, modified configurations).

---

### SVC-08-Q09: Training Artifact Lifecycle Management and Retention Clarity

For machine learning training pipelines, what explicit lifecycle policies govern retention and cleanup of model artifacts?

**Sub-questions**:
- What retention windows apply to model checkpoints saved every N training steps (potentially hundreds of snapshots for large models)?
- How are optimizer state files, gradient checkpoints, and hyperparameter search results managed for cleanup?
- What procedures coordinate federated learning artifact cleanup across distributed participant systems?
- What incident procedures address incomplete cleanup when distributed participants are offline or unresponsive during cleanup coordination?
- How do you detect and remove training artifacts from backups and archive systems (not just primary storage)?

**Compliance Implication**: Training artifacts accumulate without explicit lifecycle policies, creating storage costs and potential data exposure from forgotten artifacts. SC-4 requires validation that shared resource artifacts are properly managed.

**AI/Agent Context**: ML lifecycle creates artifact proliferation challenging traditional cleanup. Expensive-to-regenerate artifacts encourage long retention. Distributed training creates multiple copies requiring coordinated cleanup across all participant systems.

---

### SVC-08-Q10: Cross-Session Agent Memory Isolation Guarantees

For conversational agents or persistent AI assistants serving multiple users, what isolation guarantees prevent context leakage between sessions?

**Sub-questions**:
- How is session-level memory isolation implemented (separate agent instances per session versus software filtering within shared instances)?
- What memory sanitization procedures execute between user sessions to prevent information from one user influencing another user's interactions?
- What verification testing attempts to trigger residual information from previous sessions to confirm isolation effectiveness?
- For long-running agents maintaining conversation history, what cleanup procedures prevent memory accumulation degrading isolation over time?
- How is memory isolation validated under high-concurrency conditions (preventing race conditions exposing cross-session data)?

**Compliance Implication**: Context leakage between sessions enables cross-contamination of sensitive information, violating confidentiality assumptions for multi-user agent services. SC-4 requires isolation validation in shared environments.

**AI/Agent Context**: Shared agent instances serving multiple users create context bleed where information from one user's session influences subsequent users through agent memory mechanisms lacking user-level isolation. Accumulated memory overhead creates performance degradation and potential isolation failures.

---

### SVC-08-Q11: Unlearning Verification Limitations and Transparency Requirements

What documentation explicitly communicates machine learning unlearning limitations to stakeholders and auditors?

**Sub-questions**:
- What unlearning verification procedures are applied (membership inference testing, model inversion attack attempts)?
- What explicit statements acknowledge that ghost data absence cannot be definitively proven, only that detection techniques fail?
- How are unlearning limitations documented in audit evidence, compliance artifacts, and customer-facing materials?
- What procedures validate that unlearning implementations actually removed target training data rather than obscuring it from specific attacks?
- For regulatory inquiries, what honest assessment of unlearning capabilities and limitations can you provide?

**Compliance Implication**: Honest assessment of unlearning limitations demonstrates transparency required for federal customer confidence and FedRAMP compliance. Overstated unlearning effectiveness creates regulatory risk.

**AI/Agent Context**: Current research cannot definitively prove training data removal from models. Verification techniques only confirm specific detection methods fail, not absolute information absence. Multi-generational fine-tuning compounds ghost data risks making unlearning increasingly uncertain.

---

### SVC-08-Q12: Federated Learning Distributed Artifact Cleanup Coordination

For federated learning deployments, what procedures coordinate artifact cleanup across distributed participant systems?

**Sub-questions**:
- What cleanup coordination protocols ensure all participants delete local dataset replicas when model training completes?
- What verification confirms that distributed model checkpoints and gradient updates are removed from participant systems?
- What incident procedures address incomplete cleanup when participants are offline or unresponsive during cleanup coordination?
- How are participant systems monitored to detect orphaned artifacts left from previous training rounds?
- What penalties or enforcement mechanisms exist when participants fail to complete cleanup procedures?

**Compliance Implication**: Distributed training creates residual data copies at each participant. Cleanup coordination failures create unquantified data exposure and breach risks across federated ecosystems.

**AI/Agent Context**: Federated learning maintains dataset replicas at each participant for multiple training rounds. Centralized model completion does not guarantee distributed artifact cleanup. Network partitions and asynchronous participants complicate cleanup coordination.

---

### SVC-08-Q13: Agent Rollback and Roll-Forward Residual Correction Procedures

When agent-initiated changes create unintended residual elements, what procedures correct the residual state?

**Sub-questions**:
- What rollback coordination procedures notify downstream systems already depending on agent changes before rolling back?
- What roll-forward correction mechanisms re-engage agent loops to execute additional corrective actions when rollback is infeasible?
- What validation confirms that rollback/roll-forward succeeded without creating new residual elements?
- For agent decisions based on temporal context (market conditions, threat intelligence), what procedures document why rollback was impossible and what corrective actions were taken instead?
- How are partial-failure residues from multi-system agent actions identified and remediated?

**Compliance Implication**: Agent decision-making depends on temporal context making rollback impossible when context changes. Documented roll-forward procedures demonstrate FedRAMP-compliant control adaptation for autonomous agents.

**AI/Agent Context**: Agent decisions based on market conditions, threat intelligence, or system performance cannot be rolled back when context changes. Multi-system agent actions lack transactional guarantees creating partial failure residue. Autonomous scaling decisions create infrastructure residue requiring explicit cleanup rather than simple rollback.

---

### SVC-08-Q14: Insider Threat Risk and Residual Access Control

How does your organization prevent residual access from terminated employees or contractors to systems accessed via agent accounts or service credentials?

**Sub-questions**:
- When employees/contractors are terminated, what procedures ensure their access to all agent service accounts and NHI credentials is revoked?
- How are hardcoded credentials in applications, notebooks, or deployment artifacts discovered and rotated when employee access is revoked?
- What monitoring detects residual insider access disguised through agent accounts or API keys?
- For shared credentials (team service accounts, shared database passwords), what procedures prevent terminated employees from retaining access?
- What audit trails show when insider access was revoked and confirm cleanup was complete?

**Compliance Implication**: SC-4 and SC-7 require validation that residual insider access is eliminated. AI workloads create credential proliferation making insider access cleanup complex.

**AI/Agent Context**: Terminated employees retain knowledge of agent credentials, shared service accounts, and deployment procedures enabling persistent residual access. Hardcoded credentials in shared repositories prevent effective cleanup. Agent accounts create "phantom" access after human employee termination.

---

### SVC-08-Q15: Documentation and Compliance Evidence for Residual Risk Management

What documentation demonstrates to FedRAMP assessors that residual risk management controls are effective and continuously validated?

**Sub-questions**:
- What policies and procedures document your approach to each residual risk category (ephemeral artifacts, multi-tenant isolation, credential lifecycle, agent memory isolation)?
- What testing evidence demonstrates control effectiveness (test results, remediation of identified gaps, frequency of validation)?
- For each control, what metrics track remediation SLA and actual closure times?
- How is residual risk management integrated into your FedRAMP continuous monitoring program (monthly evidence generation)?
- What incident examples from past 12 months demonstrate detection and remediation of residual elements?

**Compliance Implication**: FedRAMP SC-4 and SC-7 require sustained demonstration of control effectiveness. Comprehensive documentation and evidence generation enable compliant monitoring.

**AI/Agent Context**: Traditional residual risk assessments do not address AI-specific categories (ghost data, agent memory, training artifacts). Explicit documentation of AI-specific residual risk management demonstrates proactive FedRAMP adaptation.

---

### SVC-08-Q16: Continuous Learning Safeguards and Deleted Data Re-ingestion Prevention

What safeguards prevent continuous learning or automated retraining pipelines from inadvertently re-ingesting previously deleted customer data from historical training corpora, archived datasets, or external data sources?

**Sub-questions**:
- What policies and procedures explicitly prevent automated retraining pipelines from accessing archived training datasets containing deleted customer data?
- How is training data lineage tracked to identify which models might contain residual training signals from deleted data?
- What testing validates that model retraining without specific customers' data does not inadvertently recover information through emergent patterns?
- For continuous learning systems that update models with streaming new data, what mechanisms prevent retraining from re-consuming deleted customer data from backup datasets?
- What monitoring detects if unlearning procedures are being bypassed or circumvented through continuous learning pipelines?

**Compliance Implication**: Continuous learning systems can resurrect deleted customer data through retraining, violating deletion commitments and creating persistence that defeats removal controls. SC-4 requires validation that shared resources properly handle information lifecycle.

**AI/Agent Context**: Continuous learning pipelines can inadvertently re-consume deleted data from archived training corpora if lineage tracking is incomplete. Model checkpoint retention practices may preserve information even after deletion requests. Automated retraining on streaming data can incorporate data that should have been purged during incident response.

---

### SVC-08-Q19: Safe Change Workflows and Configuration Drift Residue Prevention

For autonomous agent-driven configuration changes, what procedures ensure that approved configuration modifications do not cumulatively create compliance violations?

**Sub-questions**:
- How do you prevent configuration "drift by design"—gradual deviations through a series of individually-approved but cumulatively-noncompliant changes?
- What change workflows require escalation to humans when configuration changes would collectively violate baseline compliance requirements?
- How are multi-agent configuration changes coordinated to prevent cross-agent corrections creating residual configuration accumulation?
- What audit trails document whether configuration changes were individually compliant but created collective compliance gaps?
- What procedures validate that agent-driven configuration changes align with overall compliance intent rather than just individual policy rules?

**Compliance Implication**: Configuration changes that satisfy individual policy rules may collectively violate compliance intent. FedRAMP requires validation that approved changes maintain overall compliance baselines.

**AI/Agent Context**: Autonomous configuration-changing agents collapse traditional change review into milliseconds, creating risk of cumulative noncompliance. Multi-agent systems create drift through cross-agent corrections where agents remediate each other's configurations without centralized coherence validation.

---

### SVC-08-Q20: Residual Configuration Elements from Agent-Driven Remediation

When autonomous agents remediate configuration drift, what procedures prevent residual configuration elements from remaining after remediation?

**Sub-questions**:
- When agents auto-remediate configuration drift, what validation confirms that remediation does not leave residual configuration artifacts (obsolete rules, cached settings, stale certificates)?
- How do you handle scenarios where agent remediation is impossible without human access—do agents provide actionable recommendations or simply escalate?
- What rollback procedures exist when agent-initiated remediation introduces new configuration issues?
- How do you distinguish beneficial configuration changes by agents versus unauthorized modifications that create residual risk?
- What audit trails document agent remediation decisions including rejection rationale for alternative configurations?

**Compliance Implication**: Agent-driven remediation may create new residual elements while fixing detected drift, especially when rollback is impossible. FedRAMP requires validation that remediation procedures don't introduce new risk.

**AI/Agent Context**: Self-healing agents automatically modify infrastructure creating assumption of no residual state, but incomplete remediation leaves stale certificates, obsolete routing rules, and cached configurations. Multi-agent systems create complex residue when agents correct each other's changes.

---

### SVC-08-Q17: Detection of Data Re-appearance in Training and Processing Pipelines

What mechanisms detect whether deleted customer data has reappeared in subsequent model training runs, continuous learning updates, or automated data pipeline ingestion processes?

**Sub-questions**:
- What testing methodology verifies that deleted data does not appear in training datasets used for subsequent model updates?
- How do you detect unintended training data inclusion when models are fine-tuned or updated with new information?
- For models using transfer learning from base models trained on larger datasets, how do you ensure deleted customer data was not incorporated into transfer learning weights?
- What monitoring tracks model behavior to identify signs of reintroduced training data (sudden performance changes, unexpected pattern recognition)?
- What evidence demonstrates that deleted data has not been re-ingested through external data sources or third-party training datasets?

**Compliance Implication**: Residual training signals persist after explicit deletion, creating information disclosure and regulatory violations. Detection demonstrates proactive governance preventing deletion circumvention.

**AI/Agent Context**: Training data contamination can occur through inadvertent inclusion in fine-tuning datasets, transfer learning replication, or external data source integration. Multi-stage training pipelines create multiple re-ingestion vectors that traditional deletion controls don't address.

---

### SVC-08-Q18: Agent Re-discovery and Residual Data Access Prevention

What mechanisms prevent AI agents from re-discovering deleted data from accessible systems, thereby circumventing deletion operations through indirect access pathways?

**Sub-questions**:
- What controls prevent agents from accessing or reassembling deleted data fragments stored in system logs, audit trails, or monitoring systems?
- How do agents interact with temporary caches (Redis, Memcached, CDN caches) and what prevents access to residual cached copies of deleted information?
- What procedures ensure agents cannot reconstruct deleted information from derivative artifacts (indexes, summarizations, derived models)?
- For agents with broad tool access, what restrictions prevent using file systems, databases, or search tools to re-discover deleted data?
- What audit trails document agent access attempts to deleted information enabling forensic investigation of circumvention attempts?

**Compliance Implication**: Agents with tool access can bypass deletion controls through alternative discovery pathways, creating residual data access and violation of deletion completeness. SC-7 requires boundary protection preventing unauthorized access.

**AI/Agent Context**: Autonomous agents with tool invocation capabilities can access file systems, databases, and external APIs enabling indirect discovery of deleted information. Agent memory accumulation can preserve deleted data even after deletion operations on primary systems.

---

## Cross-Cutting Themes

**Residual Element Classification**: Questions address traditional categories (orphaned resources, explicit data remnants, configuration carryover) and AI-specific categories (ghost data, agent memory, training artifacts, ephemeral credential persistence, multi-tenant contamination).

**Continuous Monitoring Integration**: Questions support monthly FedRAMP reporting requirements through artifact detection systems, remediation validation, and audit trail completeness.

**Cost-Benefit Calibration**: Questions address operational tradeoffs between aggressive residual cleanup (performance overhead, availability impact) and compliance requirements.

**Perspective-Neutral Framing**: All questions reframed to focus on technical control mechanisms and verification evidence rather than CIO/Customer/Auditor stakeholder perspectives.

---

## Related Question Sets

**Questions Moved to CMT-01 (Log and Monitor Changes)**:
- Automated Residual Element Detection System Effectiveness (formerly SVC-08-Q016) - now integrated as CMT-01-Q46 focused on continuous monitoring of residual elements
- This question focuses on detection tooling coverage and false positive rates, which is CMT-01's core domain

**Questions Folded into SVC-08-Q02 (Multi-Tenant Isolation)**:
- GPU Memory Cryptographic Wiping Validation Procedures (formerly SVC-08-Q020)
- Container Image Layer Residual Contamination Testing (formerly SVC-08-Q021)
- Service Mesh Residual Configuration Detection and Cleanup (formerly SVC-08-Q022)
