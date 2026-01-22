# AI System Redeployment Through Version-Controlled Infrastructure: Discovery Questions

**KSI Focus:** CMT-02 - Execute changes through redeployment of version-controlled immutable resources, with emphasis on AI artifacts and reproducibility.

---

## Section 1: Immutable Infrastructure and Infrastructure-as-Code Enforcement

**CMT-02-Q001:** Describe your Infrastructure-as-Code (IaC) coverage across your production environment. What percentage of your infrastructure is defined in version-controlled IaC (Terraform, CloudFormation, Pulumi)? For infrastructure NOT managed by IaC, provide justification and remediation timeline. Can you provide an inventory showing: compute resources, storage systems, networking, databases, and AI platforms with IaC coverage percentages by category?

**CMT-02-Q002:** Describe your Git workflow for infrastructure changes and production deployment traceability. Are direct commits to production branches blocked? How many approvers are required before merging infrastructure changes? For recent production deployments, can you demonstrate: Git commit SHA, deployment timestamp, and deployer identity linking each deployment to a specific version-controlled change? What percentage of deployments have full Git traceability?

**CMT-02-Q003:** How do you prevent direct modifications to production infrastructure? For each prevention mechanism, provide evidence: (1) SSH access policy and controls, (2) API mutation detection (audit logs showing imperative AWS/Kubernetes calls), (3) Admission control policies blocking unauthorized changes. What percentage of production modifications flow through version control vs. direct modifications?

**CMT-02-Q004:** For container-based workloads, how do you enforce immutability? Are container images cryptographically signed before deployment? Do you use admission controllers to block unsigned images? Are base OS images and dependencies frozen (no in-place container patching)? Describe your verification process for container integrity.

**CMT-02-Q005:** What is your mean time to detect (MTTD) unauthorized direct modifications to production infrastructure, and mean time to remediate (MTTR) to the desired version-controlled state? Describe drift detection mechanisms (continuous, scheduled, or manual). How is remediation executed (automated convergence or manual operator-initiated)? What is your MTTR target?

---

## Section 2: Model Registry, Versioning, and AI Artifact Governance

**CMT-02-Q006:** Do you provide centralized model registry infrastructure (MLflow, SageMaker Model Registry, or equivalent) for all production AI models? What metadata is automatically captured for each model version: training code commit SHA, training data version/hash, hyperparameters, performance metrics, approval chain, and deployment dates? How are model versions identified and tracked?

**CMT-02-Q007:** For model lifecycle management (experimentation → staging → production), describe your approval workflows. Can organizations define custom approval rules (e.g., production models require multiple reviewers + performance validation)? Are all approvals logged in audit trail with approver identity, timestamp, and rationale? Is explicit approval required or can models be promoted without approval?

**CMT-02-Q008:** What model versioning standards do you enforce? Do you mandate semantic versioning (MAJOR.MINOR.PATCH) or support arbitrary version strings? Can you trace which model version is currently deployed in each environment (dev/staging/prod)? How do you ensure versioning consistency across teams?

**CMT-02-Q009:** If a production model fails, how quickly can you rollback to a previous version? Is rollback instant (registry swap) or requires redeployment? Are all historical model versions retained indefinitely? What is your SLA for model version retrieval and rollback execution? Do you support A/B testing and canary deployments for model rollout?

---

## Section 3: Configuration Drift Detection and Remediation

**CMT-02-Q010:** How do you detect configuration drift (deviation from version-controlled desired state)? What detection mechanisms do you use (continuous, scheduled, or manual)? Describe the scope: infrastructure configuration, model registry versions, security policies, AI agent policies, container images, and dependencies. For detected drift, what is your mean time to remediation (MTTR)?

**CMT-02-Q011:** When configuration drift is detected, how is remediation executed? Is remediation automated (instant convergence to desired state) or manual (operator investigates and applies fix)? How do you distinguish legitimate approved changes (Git commits) from unauthorized drift? How do you prevent baseline poisoning (gradual normalization of malicious behavior)?

**CMT-02-Q012:** What happens when drift is detected? Are relevant stakeholders notified? Is drift logged in immutable audit trail with timestamps and details? Can you query complete drift history (incidents in past 90 days with investigation details)?

---

## Section 4: AI Artifact Reproducibility - Core Pillars

**CMT-02-Q013:** Are training code and deployment code version-controlled in Git for all production AI models? How do you trace models to their training code commits? What percentage of production models have Git commit SHA recorded in model metadata? Can every historical model be retrieved using commit SHA?

**CMT-02-Q014:** How do you guarantee training data immutability and versioning? Are training datasets versioned (DVC, Delta Lake, feature store) with cryptographic checksums (SHA256)? How do you ensure datasets are frozen after model training (no retroactive modifications)? Can you demonstrate dataset version retrieval for historical models?

**CMT-02-Q015:** How do you freeze and version dependencies (Python libraries, system packages, container base images)? Do you use lock files (poetry.lock, Pipfile.lock, requirements.txt with exact versions) to capture exact transitive dependencies? What percentage of your training/deployment workflows use pinned dependencies vs. floating versions?

**CMT-02-Q016:** How do you guarantee identical training environments across runs (development, staging, production)? Are training and deployment environments containerized with explicit OS image versions? Can you reproduce environments from versioned Dockerfiles or container specifications? Do environment definitions go through version control and testing?

**CMT-02-Q017:** How do you validate reproducibility of AI training pipelines? Do you test reproducibility (re-run historical training, verify model consistency within acceptable variance <0.1% metric variance)? Provide testing methodology and success rate. What types of operations are tested: data loading, feature engineering, training, checkpointing?

---

## Section 5: Model Lineage and Immutability

**CMT-02-Q018:** Can you provide end-to-end lineage for deployed models showing: raw data sources → feature engineering code → training code commit → hyperparameters → trained model weights → deployment date? How do you ensure all lineage components are immutable (cannot be modified post-deployment)? Can lineage be queried for compliance and audit purposes?

---

## Schema Reference

**Question ID Format:** CMT-02-Q### (zero-padded, e.g., CMT-02-Q001)

**All questions should be answered with:**
- Direct evidence (not claims or aspirational statements)
- Quantifiable metrics where applicable
- Supporting documentation (logs, reports, configuration files)
- Concrete examples from production environments
- Timeline and frequency information for operational metrics

---

**Version:** 2.0 (Refined)
**Generated:** 2026-01-13
**Refinement Basis:** Issue #14 feedback - focused on version-controlled immutable redeployment core
**Removed Sections:** Supply chain security, agent privilege control, compliance automation, emergency patching/SLAs, organizational readiness (moved to dedicated KSIs)
