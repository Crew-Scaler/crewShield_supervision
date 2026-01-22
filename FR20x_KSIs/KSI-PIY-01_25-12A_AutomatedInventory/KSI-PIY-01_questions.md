# AI-Driven Asset Discovery, Classification & Inventory Integrity: Discovery Questions

**KSI-PIY-01** - Enforce: Resource Inventory with AI-driven autonomous asset discovery and classification

**Research Foundation:** 10 papers synthesized across AI-augmented discovery, shadow IT/AI detection, SBOM automation, multi-cloud normalization, and data poisoning defense

**Question Set Version:** 1.0
**Generated:** 2026-01-08

---

## Section 1: Autonomous AI-Driven Asset Discovery & Real-Time Inventory (Q01-Q05)

**PIY-01-Q01:** What continuous AI-driven asset discovery system identifies all deployed resources across your infrastructure in real-time? Document: (a) discovery frequency and latency (target: seconds to minutes vs. hours/days for traditional scans), (b) coverage across all environments (cloud providers, on-premises, SaaS), (c) asset types discovered (VMs, containers, serverless, databases, networks, identities, AI models), (d) ephemeral workload capture (serverless functions, containers existing seconds), (e) evidence of discovery accuracy vs. manually-maintained inventory baseline.

**PIY-01-Q02:** How does your inventory system detect and classify shadow IT and unauthorized deployments? Explain: (a) monitoring methodology for discovering unmanaged infrastructure, (b) detection accuracy (% of unauthorized assets identified within 24 hours), (c) classification confidence scoring (how certain is detection of unauthorized status?), (d) false positive rate for shadow IT detection, (e) examples of shadow IT discovered and remediation time.

**PIY-01-Q03:** How do you achieve continuous inventory reconciliation between declared state (IaC, CMDBs) and actual running infrastructure? Provide: (a) reconciliation frequency and latency, (b) accuracy metrics (target: >98% inventory accuracy), (c) discrepancy detection and classification (drift vs. new assets vs. stale records), (d) automated remediation of inventory inconsistencies, (e) evidence of reconciliation results over past 90 days.

**PIY-01-Q04:** What multi-cloud normalization capabilities enable unified asset inventory across AWS, Azure, GCP, on-premises, and SaaS? Describe: (a) cloud-agnostic asset model abstracting cloud-specific details, (b) asset correlation across clouds (matching same asset across multiple discovery sources), (c) conflict resolution when asset appears in multiple clouds, (d) normalized reporting showing cross-cloud asset inventory, (e) validation that normalized models preserve cloud-specific security properties.

**PIY-01-Q05:** How do you handle inventory updates for ephemeral resources (serverless functions, containers, auto-scaled instances) that exist for seconds/minutes? Document: (a) capture methodology for short-lived workloads, (b) inventory lifecycle management (resources automatically purged when they terminate), (c) forensic analysis capability (querying what ran even if no longer running), (d) retention policies balancing forensic utility with storage costs, (e) evidence of ephemeral workload discovery for past 30 days.

---

## Section 2: Shadow AI Detection & Unauthorized AI Tool Usage Governance (Q06-Q10)

**PIY-01-Q06:** What dedicated shadow AI detection program identifies unauthorized access to external LLMs and AI services? Explain: (a) monitoring of external LLM API access (ChatGPT, Claude, Bard endpoints), (b) detection accuracy (target: 90%+ of unauthorized AI API calls identified), (c) classification of detected AI tool usage (authorized vs. unauthorized vs. unknown), (d) data leakage detection (what data is sent to external AI services?), (e) evidence of shadow AI discoveries in past 90 days.

**PIY-01-Q07:** How do you maintain an authoritative registry of approved AI agents and internal AI workloads with governance metadata? Document: (a) agent registry containing all deployed agents with approval status, (b) metadata captured per agent (purpose, data accessed, tools invoked, approval decision), (c) agent lifecycle tracking (creation, modification, decommissioning), (d) compliance mapping (which agents comply with regulatory requirements?), (e) integration enabling security team to revoke agent access if compromised.

**PIY-01-Q08:** What controls prevent unauthorized AI agents from being deployed in your environment? Describe: (a) pre-deployment approval workflows for new agent deployments, (b) runtime detection of unapproved agents (comparing deployed agents to registry), (c) enforcement mechanisms (quarantine, kill, revoke permissions), (d) detection latency (target: <1 hour from unauthorized deployment to detection), (e) evidence of detected and remediated rogue agents.

**PIY-01-Q09:** How do you classify shadow AI by risk level and implement tiered governance responses? Provide: (a) risk classification criteria (data sensitivity, external service trustworthiness, regulatory impact), (b) response procedures (monitoring-only, warning, enforcement, immediate remediation), (c) escalation criteria and approval workflows, (d) metrics tracking shadow AI incidents by risk level, (e) examples of different response tiers applied to real incidents.

**PIY-01-Q10:** What communication and education programs help employees understand risks of shadow AI and approved alternatives? Explain: (a) awareness training on data governance implications of external AI tools, (b) approved AI tools and processes made easily accessible, (c) exception process for using external tools when justified, (d) regular communication about shadow AI detections and compliance expectations, (e) metrics measuring employee awareness and voluntary compliance.

---

## Section 3: SBOM/AI BOM Generation & Supply Chain Visibility (Q11-Q15)

**PIY-01-Q11:** What AI-driven Software Bill of Materials (SBOM) generation system automatically catalogs all software dependencies? Document: (a) SBOM generation scope (source code, compiled binaries, container images, AI models), (b) dependency visibility (direct and transitive dependencies), (c) SBOM metadata captured (package names, versions, hashes, licenses), (d) integration into CI/CD (SBOM generated with every build), (e) accuracy validation (SBOM completeness vs. actual dependency analysis).

**PIY-01-Q12:** How do you generate AI Bill of Materials (AI BOM) for machine learning systems capturing model provenance and data lineage? Describe: (a) AI BOM contents (model versions, training data hashes, datasets, training scripts, dependencies, APIs, guardrails, prompts), (b) model lineage tracking (which data → which models → which deployments), (c) versioning and history enabling rollback if model poisoned, (d) integration with compliance evidence (audit trail for AI systems), (e) examples of AI BOMs generated for production models.

**PIY-01-Q13:** How do you correlate SBOM/AI BOM information with vulnerability databases enabling automated CVE detection and remediation? Explain: (a) automated correlation of dependencies with CVE feeds, (b) alert generation when high-severity CVEs match inventory, (c) impact analysis (which systems affected by CVE?), (d) remediation guidance (upgrade paths, patches, workarounds), (e) metrics tracking vulnerability detection latency and remediation time.

**PIY-01-Q14:** What licensing compliance scanning ensures software supply chain adheres to organizational policies? Provide: (a) license detection for all dependencies (identifying license type), (b) compliance validation against organizational license policies, (c) flagging of prohibited licenses (GPL, proprietary, uncertain), (d) exceptions and approval process for necessary but non-compliant licenses, (e) audit evidence for license compliance reviews.

**PIY-01-Q15:** How do you integrate supply chain security frameworks (SLSA, NIST SSDF) into inventory and SBOM management? Document: (a) artifact signing and signature verification, (b) provenance attestation (proving who created/approved artifacts), (c) build provenance tracking (which build tools, source code, configurations produced artifact), (d) compliance validation against supply chain security controls, (e) evidence suitable for auditor review and compliance assessment.

---

## Section 4: AI Artifact Inventory & Data Lineage Tracking (Q16-Q20)

**PIY-01-Q16:** How do you maintain comprehensive inventory of AI artifacts including model versions, training datasets, embeddings, vector database indexes, agent memories, and fine-tuning datasets? Explain: (a) AI artifact types tracked in inventory, (b) metadata captured per artifact (creation date, training data hashes, purpose, deployment status), (c) continuous inventory updates when new artifacts created or old ones deprecated, (d) automated discovery mechanisms detecting undocumented AI artifacts, (e) inventory reconciliation validating completeness and accuracy.

**PIY-01-Q17:** How do you track training data lineage from customer data ingestion through derivative AI artifacts (embeddings, model weights, feature vectors, agent knowledge bases) enabling cascade identification when source data must be removed? Document: (a) lineage tracking methodology (which customer data contributed to which models), (b) accuracy of lineage records (what is the evidence quality?), (c) integration enabling rapid identification of all affected artifacts when deletion requested, (d) testing validating lineage records enable complete cascade deletion, (e) handling of shared training data (multiple customers contributing to same model).

**PIY-01-Q18:** What automated discovery mechanisms detect shadow AI data paths where customer data persists in undocumented or unexpected locations (temporary caches, debug logs, archived model checkpoints, agent scratchpads)? Provide: (a) scanning methodology (where are shadow artifacts detected?), (b) detection frequency and latency, (c) classification of detected shadow artifacts (high-risk vs. acceptable?), (d) remediation workflows for shadow artifacts, (e) evidence of shadow artifacts discovered in past 90 days.

**PIY-01-Q19:** How do you inventory and track all external AI services and APIs consuming customer data (third-party LLM endpoints, vector databases, embeddings services)? Describe: (a) discovery of unauthorized external AI service access, (b) metadata captured per external service (purpose, data accessed, retention policies, deletion capabilities), (c) contractual verification that external services support deletion on request, (d) monitoring of external service compliance with deletion requests, (e) evidence of external AI service inventory and compliance validation.

**PIY-01-Q20:** How do you establish continuous validation that AI artifact inventory accurately reflects deployed models and trained systems? Provide: (a) validation methodology (automated queries of model registries, training logs, deployment systems), (b) reconciliation frequency and accuracy metrics (target: >98% for security-critical artifacts), (c) procedures identifying inventory gaps (artifacts deployed but not in inventory), (d) evidence of inventory validation results over past 90 days, (e) automated remediation of inventory discrepancies.

## Section 5: Data Poisoning Detection & Training Data Integrity (Q21-Q23)

**PIY-01-Q21:** How do you defend against data poisoning attacks where malicious training data corrupts AI-based asset classification models? Explain: (a) data validation procedures for training datasets, (b) anomaly detection identifying suspicious data patterns, (c) Byzantine-resilient aggregation protecting against poisoned samples, (d) model monitoring detecting poisoned model deployment (performance degradation), (e) evidence of poisoning attacks detected and prevented.

**PIY-01-Q22:** How do you detect concept drift where asset classification models degrade over time due to infrastructure evolution and ensure training data remains representative? Document: (a) drift detection methodology (statistical, ML-based, rule-based), (b) MTTD for model performance degradation (target: weeks before detection with proactive monitoring), (c) training data refresh frequency and process (quarterly, biannual), (d) validation that training data covers all asset types/configurations and remains representative, (e) retraining procedures triggered by drift detection with A/B testing of old vs. retrained models, (f) metrics showing model stability/drift and training data representativeness over past 6-12 months.

**PIY-01-Q23:** How do you maintain audit trails proving asset classification decisions are defensible and not result of poisoned models? Provide: (a) model versioning and deployment tracking, (b) feature importance analysis explaining classification decisions, (c) confidence scoring for classifications, (d) mechanisms for challenging/appealing classifications, (e) audit evidence showing model governance compliance.

---

## Section 6: Discovery Agent Security & Integrity (Q24-Q27)

**PIY-01-Q24:** How do you defend discovery agents against prompt injection attacks and prevent attackers from manipulating agents through poisoned metadata? Explain: (a) attack vectors (malicious asset metadata, configuration comments, API responses, data source poisoning), (b) input validation and sanitization procedures for all agent inputs, (c) data source validation (logs, APIs, configuration management verified as trustworthy), (d) prompt engineering and configuration techniques preventing instruction override and agent manipulation, (e) testing methodology validating defenses against prompt injection and metadata poisoning, (f) evidence of attacks tested and blocked.

**PIY-01-Q25:** What runtime integrity checks prevent compromised discovery agents from exfiltrating inventory data? Provide: (a) monitoring of agent API calls and data access patterns, (b) behavioral anomaly detection identifying unusual agent decisions and queries, (c) detection of abnormal data exfiltration attempts, (d) credential-based access control (agents cannot access data outside scope), (e) audit logging of all sensitive data accessed by agents, (f) incident response procedures if agent compromise suspected.

**PIY-01-Q26:** How do you establish agent behavior baselines and detect anomalies indicating compromise or manipulation? Describe: (a) baseline establishment methodology (normal agent behavior patterns under operational conditions), (b) anomaly detection methodology (statistical, ML-based), (c) anomaly types monitored (unusual query patterns, resource usage spikes, lateral movement, exfiltration signs), (d) alerting and escalation procedures, (e) automated response procedures (revoke credentials, kill processes, isolate agent), (f) false positive rate tuning and forensic analysis determining data accessed during compromise.

**PIY-01-Q27:** How do you maintain audit trails proving discovery agent actions and enforce accountability for inventory data accessed/modified by agents? Document: (a) comprehensive audit logging of agent operations (queries, discoveries, classifications, modifications), (b) correlation between agent actions and inventory changes, (c) evidence of unauthorized inventory modifications detected, (d) recovery procedures (agent rollback, data validation, clean deployment), (e) audit evidence suitable for compliance review and incident investigation.

---

## Section 7: Inventory Partitioning & Tenant-Scoped Visibility (Q28-Q29)

**PIY-01-Q28:** How do you ensure inventory data partitioning in multi-tenant CSP environments enables tenant-scoped discovery while preventing cross-tenant leakage? Document: (a) data isolation mechanisms (cryptographic, database-level, application-level) applied to inventory, (b) validation that tenant queries return only own assets and discovery results, (c) testing for cross-tenant inventory data leakage, (d) examples of isolation mechanisms preventing tenant confusion, (e) evidence of penetration testing validating isolation strength.

**PIY-01-Q29:** What prevents shared inventory deduplication logic from inadvertently revealing one tenant's assets to another? Explain: (a) deduplication approach for inventory (how identical assets handled across tenants?), (b) tenant context preservation during deduplication operations, (c) testing ensuring deduplication doesn't leak asset information between tenants, (d) audit logging of deduplication decisions and cross-tenant comparisons, (e) examples validating isolation maintained during deduplication.

---

## Section 8: Inventory as Control Plane & Continuous Monitoring Integration (Q30-Q34)

**PIY-01-Q30:** How do you implement inventory as a first-class control plane (like identity, infrastructure-as-code enforcement) rather than peripheral tool? Explain: (a) architectural positioning (inventory informs security, compliance, cost decisions), (b) integration with other control planes (identity, network, compliance), (c) policies/rules enforced based on inventory (e.g., unmanaged resources tagged/quarantined), (d) automation enabled by inventory (cost optimization, compliance remediation), (e) business value realized through inventory-driven control.

**PIY-01-Q31:** What continuous real-time inventory update capabilities enable rapid response to infrastructure changes? Document: (a) monitoring frequency (target: seconds to minutes from change to visibility), (b) event-driven updates (webhooks, streaming) vs. periodic scans, (c) latency measurements (p50, p95, p99 time from change to inventory update), (d) completeness validation (% of infrastructure changes captured), (e) evidence of inventory update performance over past 30 days.

**PIY-01-Q32:** How do you integrate runtime security and behavioral monitoring with inventory providing real-time visibility into what's actually running? Describe: (a) instrumentation capturing runtime behavior (network flows, system calls, API calls), (b) correlation with inventory (matching runtime telemetry to asset records), (c) detection of unauthorized workloads/processes, (d) behavioral baseline establishment per asset type, (e) anomaly detection enabling threat investigation and containment.

**PIY-01-Q33:** What automated compliance and cost optimization workflows are enabled by real-time inventory? Provide: (a) examples of compliance remediation triggered by inventory changes, (b) cost optimization recommendations based on resource utilization data, (c) automated tagging/classification based on discovered patterns, (d) security hardening (e.g., unmanaged resources immediately quarantined), (e) business impact quantification (cost avoidance, compliance improvement).

**PIY-01-Q34:** How do you maintain inventory performance and cost as dataset scales across multi-cloud environments? Explain: (a) scalability targets (millions of assets, continuous updates), (b) query performance for auditors/customers retrieving inventory, (c) storage optimization (data compression, retention policies), (d) operational overhead for inventory management, (e) cost-benefit analysis justifying inventory investment.

---

## Section 9: Relationship Graph Analysis & Privilege Escalation Prevention (Q35-Q39)

**PIY-01-Q35:** How do you analyze asset relationship graphs (service A trusts role B, role B accesses database C) to detect privilege escalation paths? Document: (a) relationship mapping (which assets trust/depend on others), (b) graph analysis identifying transitive trust relationships, (c) machine-speed analysis identifying multi-hop paths to high-value targets, (d) comparison to manual analysis (what do humans find in days, AI finds in minutes?), (e) examples of detected escalation paths enabling proactive remediation.

**PIY-01-Q36:** What mechanisms prevent attackers from manipulating relationship graphs enabling hidden lateral movement? Explain: (a) validation of trust relationships (are they accurate?), (b) detection of injected fake relationships enabling privilege escalation, (c) anomaly detection identifying suspicious relationship patterns, (d) change tracking for relationship modifications, (e) examples of relationship manipulation attempts detected and prevented.

**PIY-01-Q37:** How do you incorporate relationship graph analysis into remediation workflows to reduce blast radius of security fixes? Provide: (a) dependency analysis identifying which systems affected by change, (b) impact forecasting for remediation actions, (c) coordination mechanisms for multi-system fixes, (d) testing simulating changes before deployment, (e) metrics showing reduced incident resolution time through informed remediation.

**PIY-01-Q38:** What visualization and exploration tools enable security teams to understand complex asset relationships and privilege paths? Document: (a) graph visualization (asset relationships, trust edges, privilege flows), (b) query interfaces for investigators (find all paths to database, identify lateral movement options), (c) automated alerts for critical relationship changes, (d) training enabling teams to effectively use relationship analysis, (e) examples of investigations enabled by relationship analysis.

**PIY-01-Q39:** How do you validate relationship graph accuracy and completeness against actual privilege flow? Describe: (a) comparison methodology (graph vs. real-world testing), (b) detection of missing relationships (what aren't we seeing?), (c) false positive relationships (relationships claimed but not real), (d) accuracy metrics (target: >95% for security-critical paths), (e) evidence of periodic validation testing and results.

---

**Version:** 3.0
**Research Synthesis:** 10 papers, AI-augmented discovery, shadow IT/AI detection, SBOM/AI BOM, data poisoning defense, AI artifact inventory, training data lineage, discovery agent security, inventory as control plane, relationship graph analysis
**Last Updated:** 2026-01-13
**Changes:** Added Section 4 (Q16-Q20) for AI artifact inventory and data lineage tracking from KSI-SVC-10; renumbered subsequent questions and sections accordingly; added AI artifact discovery, training data lineage, shadow AI data path detection, external AI service inventory, and AI artifact validation questions; final count: 39 questions across 9 sections
