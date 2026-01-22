# KSI-SVC-10: Unwanted Data Removal - Discovery Questions

**KSI Focus:** Remove unwanted federal customer data promptly when requested in alignment with customer agreements, including from backups if appropriate; this typically applies when data spills occur or when parties seek to remove information from a service due to a change in usage.

**AI/Agent Context:** In AI-enabled cloud services, unwanted data removal extends beyond traditional databases to include model weights, embeddings, vector database indexes, prompt logs, AI agent memories, feature stores, training datasets, and third-party system replicas created by autonomous agents.

**Document Date:** January 13, 2026

---

## Processing Summary

**Original Question Count:** 39 (from previous synthesis)
**Questions Removed:** 12 (moved to other KSIs with better alignment)
**Questions Added:** 0
**Questions Consolidated:** 3 (merged duplicates)
**Final Question Count:** 24 (perspective-neutral, SVC-10 focused)

**Changes Made:**
- Removed inventory/discovery questions (Q001, Q003, Q004, Q026, Q027, Q028) → moved to KSI-PIY-01 Automated Inventory
- Removed continuous learning safeguards questions (Q007, Q023, Q034) → moved to KSI-SVC-08 Prevent Residual Risk
- Removed backup/archive deletion questions (Q014, Q015, Q029, Q030, Q032) → moved to KSI-RPL-03 System Backups
- Removed third-party AI service question (Q039) → moved to KSI-TPR-03/04 Supply Chain Risk
- Removed regulatory harmonization questions (Q013, Q038) → moved to NIST SI-12 policy KSI
- Merged model unlearning questions (Q005, Q006, Q016) → consolidated into KSI-SVC-10-Q05
- Merged agent spill questions (Q010, Q025, Q035) → consolidated into KSI-SVC-10-Q11
- Merged evidence questions (Q021, Q033) → consolidated into KSI-SVC-10-Q15
- Removed stakeholder perspective labels (CIO/Customer/Auditor) to make all questions perspective-neutral
- Updated all remaining question IDs to KSI-SVC-10-Q format (Q01 through Q24)

---

## Core SVC-10 Questions: Deletion Execution and Verification

*These questions focus on executing unwanted data removal and verifying deletion completeness. Questions are perspective-neutral and applicable to all stakeholder groups.*

### 1. Model Unlearning and Shared Foundation Model Deletion

**KSI-SVC-10-Q01:** When one customer requests deletion of their training data from a shared foundation model serving multiple customers, what approach is used: (a) model retraining without the customer's data, (b) cryptographic deletion of archived models, (c) deletion refusal with documented justification, or (d) acceptance that certified unlearning is not guaranteed? What financial or operational thresholds determine which approach is applied?

**KSI-SVC-10-Q02:** For each AI artifact type (embeddings, vector indexes, trained models, agent memories), what deletion approach is committed to contractually, and does that approach align with technical feasibility? Where does misalignment exist between commitments and implementation reality?

**KSI-SVC-10-Q03:** How are model checkpoints, intermediate training artifacts, and fine-tuning datasets managed during deletion of training data? Are these artifacts automatically tagged with training data provenance to enable targeted deletion?

### 2. AI Artifact Deletion: Embeddings and RAG Systems

**KSI-SVC-10-Q04:** When customer data is used to generate embeddings stored in vector databases for semantic search or RAG (retrieval-augmented generation), what happens upon deletion request? Are embeddings immediately purged, marked for eventual deletion, or subject to different retention rules? How is deletion verified?

**KSI-SVC-10-Q05:** For RAG systems, does deletion of source documents trigger cascade deletion of (a) embeddings in vector databases, (b) cached inference results referencing those documents, and (c) any fine-tuned models trained on those documents? How is consistency verified across distributed vector database replicas to prevent deleted content from reappearing in search results?

**KSI-SVC-10-Q06:** Can the CSP demonstrate deletion from vector databases with verification that (a) embeddings were removed, (b) indexes were updated or reconstructed, (c) distributed replicas reflect the deletion consistently, and (d) subsequent similarity searches no longer return the deleted content?

### 3. AI Agent Memories and External System Replication

**KSI-SVC-10-Q07:** If autonomous AI agents have access to customer data, what controls prevent agents from creating "shadow data" in external systems (ticketing platforms, collaboration tools, repositories)? When data spills occur and agents have already replicated spilled data externally, what is the remediation process?

**KSI-SVC-10-Q08:** What permission boundaries and data isolation controls prevent AI agents from accessing or replicating customer data beyond their authorized scope? How are these boundaries validated during agent operation, and what evidence demonstrates that agents cannot circumvent deletion controls through tool chaining or indirect data access?

**KSI-SVC-10-Q09:** For AI agent memories, conversation histories, and knowledge base entries containing customer data, what happens upon deletion request? Can the CSP guarantee all agent state that incorporated customer data is purged?

**KSI-SVC-10-Q10:** How are all tool invocations, API calls, and side effects generated by autonomous agents logged and audited? Can complete data flow paths be reconstructed during deletion campaigns, and are external systems identified and included in deletion campaigns?

### 4. Deletion Scope Clarity and Customer Agreements

**KSI-SVC-10-Q11:** In service contracts, what is explicitly included in deletion obligations: (a) primary databases only, (b) primary databases plus active backups, (c) primary databases plus all backups including cold storage, or (d) primary databases plus all backups plus AI artifacts (models, embeddings, vectors, logs, agent memories)? Are there explicit exclusions?

**KSI-SVC-10-Q12:** What timeline is committed to for deletion from each artifact type? Do different components of a deletion request (primary systems, embeddings, agent memories, archives) have different timelines, and are these documented in contracts?

**KSI-SVC-10-Q13:** What alternative approaches are offered if selective deletion from shared models is technically infeasible? How are contractual commitments aligned with technical reality, and what costs or limitations are disclosed?

### 5. Deletion Evidence and Verification

**KSI-SVC-10-Q14:** What machine-readable evidence is provided to verify that deletion was executed? Is evidence cryptographically signed, immutable, and independently verifiable? Does evidence include (a) object counts of records deleted, (b) cryptographic attestations from multiple systems, (c) before-and-after checksums, and (d) third-party verification of claimed deletions?

**KSI-SVC-10-Q15:** If deletion occurred through cryptographic key destruction (rather than physical deletion), how can the claim be verified? Is proof of key destruction provided, and who verifies that destroyed keys cannot be recovered or bypassed?

### 6. Incident Response and Data Spill Deletion

**KSI-SVC-10-Q16:** What is the response time and SLA for deletion when customer data is accidentally uploaded to lower-authorized systems (data spill)? Does the deletion campaign scan for and include derivatives (embeddings, logs, agent artifacts) created during the spill?

**KSI-SVC-10-Q17:** Does incident response for data spills include procedures to identify and remediate autonomous agent actions that may have replicated spilled data to external systems? What is the process for forcing deletion from external ticketing systems, collaboration platforms, or documentation repositories?

### 7. Multi-Tenant Isolation in Shared Infrastructure

**KSI-SVC-10-Q18:** For shared infrastructure (shared models, shared vector indexes, shared compute), how is it verified that (a) customer tagging is consistent and prevents cross-contamination of deletion operations, (b) deletion of one customer's data does not affect another customer's data, (c) shared models are either customer-specific or deletion capability is explicitly acknowledged as infeasible, and (d) vector index deletion does not corrupt indexes for other customers?

### 8. Testing and Validation of Deletion Mechanisms

**KSI-SVC-10-Q19:** Can the CSP demonstrate successful deletion tests covering at least (a) deletion from primary databases with verification, (b) deletion from active vector indexes with verification, (c) deletion from trained models with verification or documented explanation of infeasibility, and (d) deletion from agent memories with verification?

**KSI-SVC-10-Q20:** What testing verifies that backup restoration operations do not reintroduce previously deleted customer data? How is this tested as part of regular disaster recovery exercises?

**KSI-SVC-10-Q21:** Are deletion evidence and verification mechanisms validated for credibility, specificity, and tamper-resistance? Do they demonstrate deletion across all artifact types and include independent verification of claims?

### 9. Agent-Driven Data Replication and External System Deletion

**KSI-SVC-10-Q22:** Can the CSP trace all data flow created by autonomous AI agents to identify external systems modified during agent operation? For agents with access to ticketing, collaboration, or repository systems, is evidence available that (a) all agent side effects are logged, (b) external systems are scoped appropriately, and (c) deletion campaigns include external system remediation?

### 10. Cascading Deletion and Multi-Location Coordination

**KSI-SVC-10-Q23:** When customer data is deleted from primary systems, are all derivative artifacts (embeddings, cached results, agent memories, logs) automatically identified and included in the deletion campaign? What mechanisms prevent selective deletion that leaves orphaned references?

**KSI-SVC-10-Q24:** Is there evidence that deleted data does not reappear through (a) inadvertent recovery from pre-deletion backups, (b) re-ingestion from external sources, (c) agent re-discovery of data from accessible systems, or (d) unintended inclusion in subsequent training or processing?

---

## Questions Moved to Related KSIs

### Moved to KSI-PIY-01 (Automated Inventory)
- AI artifact inventory discovery and validation
- Shadow data detection mechanisms
- Training data lineage tracking and provenance
- Continuous inventory validation procedures

### Moved to KSI-SVC-08 (Prevent Residual Risk)
- Continuous learning safeguards preventing re-ingestion
- Detection of data re-appearance in training pipelines
- Prevention of residual artifacts in system caches
- Automated monitoring of deletion persistence

### Moved to KSI-RPL-03 (System Backups)
- Backup deletion semantics (active, cold storage, archives)
- Cryptographic deletion validation for backups
- Backup retention and deletion timeline commitments
- Disaster recovery testing including deletion verification

### Moved to KSI-TPR-03/04 (Supply Chain Risk Management)
- Third-party AI service deletion obligations
- Contractual deletion requirements for external providers
- Verification of third-party deletion compliance
- Escalation procedures for third-party deletion failures

### Moved to NIST SI-12 Policy KSI (Information Handling & Retention)
- Regulatory harmonization across jurisdictions
- Conflicting deletion and retention requirements
- Jurisdiction-aware deletion policies
- Policy decisions for handling cross-jurisdictional conflicts

---

## Cross-Cutting Validation Checklist

**For all assessments, independently verify:**

- Deletion mechanisms have been tested and verified for each artifact type
- Deletion evidence is tamper-evident and independently verifiable
- Agents, if present, are scoped and cannot create uncontrolled shadow data paths
- Deletion requests result in cascade deletion across all artifact types
- Multi-tenant isolation prevents one customer's deletion failure from affecting others
- Incident response procedures for data spills include cascade deletion and external system remediation
- Deletion timelines are documented and verifiable across all artifact types
- Alternative approaches for technically infeasible deletions (e.g., model unlearning) are documented and accepted
- Evidence of deletion is accessible and machine-readable
- Testing demonstrates that backup restoration does not resurrect deleted data
- Multi-location coordination prevents orphaned references after deletion

---

## AI-Specific Deletion Challenges Addressed

**Model Weights and Training Data:**
- Questions KSI-SVC-10-Q01, Q02, Q03 address model unlearning and training artifact deletion

**Embeddings and Vector Databases:**
- Questions KSI-SVC-10-Q04, Q05, Q06 address cascade deletion in RAG systems and vector database consistency

**Autonomous Agent Side Effects:**
- Questions KSI-SVC-10-Q07, Q08, Q09, Q10, Q22 address shadow data paths and agent permission boundaries

**Multi-Tenant Shared Infrastructure:**
- Question KSI-SVC-10-Q18 addresses customer isolation in shared models and vector indexes

**Deletion Verification and Evidence:**
- Questions KSI-SVC-10-Q14, Q15, Q21 address machine-readable proof and cryptographic validation

**Cascading Deletion:**
- Questions KSI-SVC-10-Q23, Q24 address multi-location coordination and residual artifact prevention

---

## Alignment with FedRAMP 20x and NIST Controls

**KSI-PIY-01 (Automated Inventory):** Cross-referenced inventory requirements for enabling complete deletion

**KSI-SVC-05 (Resource Integrity):** Deletion evidence and cryptographic validation of deletion operations

**KSI-SVC-08 (Prevent Residual Risk):** Cross-referenced safeguards against data re-appearance

**KSI-RPL-03 (System Backups):** Cross-referenced backup deletion strategies and archive removal

**KSI-TPR-03/04 (Supply Chain Risk):** Cross-referenced third-party AI service deletion obligations

**NIST SI-12 (Information Handling and Retention):** Cross-referenced policy-level data disposal and retention harmonization

**NIST SI-18 (PII Quality Operations):** Incident response procedures for sensitive data spills

---

**Document Classification:** For Official Use Only - Federal Cloud Service Providers and FedRAMP Assessors

**Last Updated:** January 13, 2026
