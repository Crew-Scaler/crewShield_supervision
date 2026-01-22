# KSI-AFR-09: Persistent Validation and Assessment - Investigative Questions

**KSI Title**: Persistent Validation and Assessment
**KSI ID**: KSI-AFR-09
**Document Version**: 2.0
**Last Updated**: 2026-01-13

---

## Summary

This question library supports persistent validation and assessment for AI and AI Agent systems in FedRAMP 20x environments. The shift from annual point-in-time assessments to continuous validation (every 3-7 days for machine-based resources) requires new approaches for AI systems that exhibit non-deterministic outputs, model drift, autonomous behavior, hallucinations, supply chain risks, and emergent properties.

### Statistics
- **Original Question Count**: 64
- **Questions Removed (lowest incremental value)**: 4 (Q025, Q029, Q037, Q061)
- **Questions Moved to KSI-AFR-03 (evidence sharing/export)**: 5 (Q030, Q036, Q038, Q039, Q059)
- **Questions Moved to KSI-CMT-03 (automated testing)**: 4 (Q005, Q007, Q045, Q055)
- **Questions Added from KSI-CNA-08 (evidence/governance focus)**: 3 (continuous evidence generation, multi-framework mapping, governance drift detection)
- **Final Question Count (KSI-AFR-09 focused)**: 54 questions
- **Renumbering**: All questions renumbered to KSI-AFR-09-Q001 through KSI-AFR-09-Q054 format

### Removed Questions

The following questions were removed as they had lowest incremental value or overlapped with other areas:
- **KSI-AFR-09-Q025** (formerly): Documented SLAs for remediating validation failures (better suited for incident response/governance KSIs)
- **KSI-AFR-09-Q029** (formerly): High-level "do you have documentation?" on persistent validation frameworks (covered more specifically in other questions)
- **KSI-AFR-09-Q037** (formerly): CSP security incident escalation mechanics (fits better with incident response KSIs)
- **KSI-AFR-09-Q061** (formerly): Validation failure remediation SLAs and compliance (overlaps with removed Q025, IR/governance-oriented)

### Moved Questions to Other KSIs

**Moved to KSI-AFR-03 (Evidence Sharing and Export):**
- Real-time access vs periodic reports for validation evidence
- Dashboards/reports showing persistent validation status
- Audit logs of validation activities for independent review
- Visibility into automation coverage vs manual verification
- Evidence retention policies supporting full audit trail reconstruction

**Moved to KSI-CMT-03 (Automated Testing & CI/CD Validation):**
- A/B and shadow deployment mechanisms validating retrained models
- Shadow deployment duration and metrics driving cutover decisions
- Canary deployment processes with behavioral monitoring
- Demonstrating A/B testing validations are genuine experiments

---

## Core AFR-09 Questions (Perspective-Neutral Format)

These questions are organized by implementation area and address persistent validation mechanisms specific to AI systems. All questions are phrased in perspective-neutral format suitable for any stakeholder role.

### Section 1: Non-Deterministic AI Output Validation Strategy

**KSI-AFR-09-Q001**: How is validation currently handled for non-deterministic AI outputs (LLM responses, agent decisions) that produce multiple valid results from identical inputs?

**KSI-AFR-09-Q002**: Which probabilistic validation frameworks and tools have been evaluated for AI output assessment?

**KSI-AFR-09-Q003**: How are probabilistic validation frameworks integrated into deployment pipelines rather than treating them as post-deployment monitoring?

### Section 2: Continuous Model Drift Detection and Automated Retraining

**KSI-AFR-09-Q004**: How is model performance degradation detected and addressed post-deployment?

**KSI-AFR-09-Q005**: How is the model registry organized to track validation status across deployment lifecycles?

**KSI-AFR-09-Q006**: How is model validation evidence maintained throughout the retraining and deployment lifecycle?

### Section 3: Per-Invocation Runtime Authorization Validation

**KSI-AFR-09-Q007**: How are AI agent tool invocations authorized when agents operate at millisecond frequencies making thousands of decisions daily?

**KSI-AFR-09-Q008**: What behavior-based anomaly detection systems monitor for unusual agent action patterns?

**KSI-AFR-09-Q009**: How frequently are agent credentials rotated, and what is the maximum credential lifetime?

### Section 4: Hallucination Detection and Evidence Grounding

**KSI-AFR-09-Q010**: If AI systems generate or aggregate validation evidence, how are hallucinated compliance claims prevented from being submitted to assessors?

**KSI-AFR-09-Q011**: What human verification checkpoints exist before AI-generated compliance artifacts are submitted to assessors?

**KSI-AFR-09-Q012**: Are validation evidence artifacts cryptographically signed at generation point to prevent post-generation modification?

### Section 5: AI Supply Chain Verification and Model Integrity Assurance

**KSI-AFR-09-Q013**: How is integrity of third-party AI components (pre-trained models, fine-tuning services, training datasets) verified before deployment?

**KSI-AFR-09-Q014**: What air-gapped or isolated validation environments are maintained for third-party AI models?

**KSI-AFR-09-Q015**: How is data provenance and model lineage tracked from collection through transformation to model training?

### Section 6: Emergent Behavior Detection and Scale-Dependent Testing

**KSI-AFR-09-Q016**: How are organizations testing for emergent behaviors that only manifest at production scale?

**KSI-AFR-09-Q017**: How are unexpected emergent behaviors formally classified as validation failures?

**KSI-AFR-09-Q018**: What feedback mechanisms prevent recurrence of undesirable emergent outcomes?

### Section 7: Meta-Validation and Process Transparency

**KSI-AFR-09-Q019**: How is validation that the validation processes themselves are operating correctly and effectively (meta-validation) conducted?

**KSI-AFR-09-Q020**: What explainability mechanisms exist to make AI-driven validation decisions auditable and understandable to assessors?

### Section 8: Configuration and Baseline Management (Cross-Cutting with AFR-07)

**KSI-AFR-09-Q021**: How are validation baselines updated as AI systems evolve through retraining and configuration changes without invalidating historical validation evidence? *(Cross-cutting with KSI-AFR-07)*

**KSI-AFR-09-Q022**: Can validation baselines be updated systematically as systems evolve while maintaining audit trail continuity? *(Cross-cutting with KSI-AFR-07)*

### Section 9: Automation Mandate and Coverage Validation

**KSI-AFR-09-Q023**: What percentage of security controls are validated through automated processes versus manual verification, and how does this align with FedRAMP 20x's 80%+ automation mandate?

### Section 10: AI-Specific Validation Concerns

**KSI-AFR-09-Q024**: How are AI systems that have undergone fine-tuning post-authorization validated to ensure safety alignment is preserved?

**KSI-AFR-09-Q025**: How are multi-step AI agent tool compositions validated where individual tools are safe but combinations may create security risks?

### Section 11: Cross-System Validation Dependencies

**KSI-AFR-09-Q026**: How are validation dependencies managed across multiple KSIs when AI systems span identity, logging, change management, and network controls?

**KSI-AFR-09-Q027**: What is the validation evidence retention policy, and how is evidence kept accessible for the full audit period?

### Section 12: Continuous Validation Demonstration

**KSI-AFR-09-Q028**: Can the scientific basis for probabilistic validation thresholds, success percentages, and semantic equivalence criteria be demonstrated?

**KSI-AFR-09-Q029**: Is access available to actual validation tools, algorithms, and code implementing probabilistic assessment?

**KSI-AFR-09-Q030**: Can continuous validation occurrence at documented frequencies be demonstrated with evidence of execution?

**KSI-AFR-09-Q031**: Can continuous model performance monitoring with documented evidence of drift detection and response be demonstrated?

**KSI-AFR-09-Q032**: Is model registry access available with complete versioning history and validation status per version?

**KSI-AFR-09-Q033**: Can per-invocation authorization validation at millisecond frequencies supporting agent operation rates be demonstrated?

**KSI-AFR-09-Q034**: Can behavior-based anomaly detection identifying unusual agent action patterns be demonstrated?

**KSI-AFR-09-Q035**: Can short-lived credential rotation preventing persistent compromise from single credential theft be demonstrated?

### Section 13: Evidence Integrity and Validation of Validation

**KSI-AFR-09-Q036**: If AI systems generate validation evidence, can hallucination detection and fact-verification mechanisms be demonstrated?

**KSI-AFR-09-Q037**: Can cryptographic evidence of validation artifact integrity through signing and timestamp verification be provided?

**KSI-AFR-09-Q038**: Can validation evidence itself being validated through meta-validation processes be demonstrated?

### Section 14: Supply Chain and Third-Party Component Verification

**KSI-AFR-09-Q039**: Can cryptographic signing and verification of all third-party AI components before deployment be demonstrated?

**KSI-AFR-09-Q040**: Can Supply Bills of Materials documenting provenance and lineage of all third-party components be provided?

**KSI-AFR-09-Q041**: Can isolated validation environments for third-party components preventing supply chain compromise during validation itself be demonstrated?

### Section 15: Scale and Emergence Validation

**KSI-AFR-09-Q042**: Can formal classification of unexpected emergent behaviors as validation failures be demonstrated?

**KSI-AFR-09-Q043**: Can post-deployment monitoring be demonstrated as formal validation component, not optional monitoring?

### Section 16: CSP Continuous Validation Capabilities

**KSI-AFR-09-Q044**: Does the CSP provide documented persistent validation frameworks explaining how security decisions remain compliant between 3-7 day validation cycles?

**KSI-AFR-09-Q045**: How does the CSP validate AI agent behavior when agents operate at millisecond frequencies making thousands of decisions daily?

**KSI-AFR-09-Q046**: Can the CSP demonstrate that retrained models undergo validation before deployment to production?

**KSI-AFR-09-Q047**: Does the CSP implement grounding and hallucination detection if AI systems generate validation evidence?

**KSI-AFR-09-Q048**: How does the CSP assess third-party AI components (pre-trained models, fine-tuning services, training datasets) for supply chain risks?

### Section 17: Fine-Tuning and Composition Validation

**KSI-AFR-09-Q049**: Can comprehensive safety validation be demonstrated for AI systems undergoing fine-tuning post-authorization?

**KSI-AFR-09-Q050**: Can validation of multi-step AI agent tool compositions including compositional security testing be demonstrated?

### Section 18: Explainability and Auditability

**KSI-AFR-09-Q051**: Can AI validation decisions be demonstrated to be explainable and auditable, not black-box processes?

### Section 19: Continuous Evidence Generation and Freshness (from KSI-CNA-08)

**KSI-AFR-09-Q052**: Does automated enforcement system generate compliance evidence continuously (hourly or daily) or point-in-time (quarterly)? Is evidence available between audit periods? How current is compliance evidence available to auditors?

**KSI-AFR-09-Q053**: Can evidence demonstrating compliance with FedRAMP, NIST AI RMF, EU AI Act, and ISO/IEC 42001 be generated simultaneously? Is evidence mapping automated or manual?

### Section 20: Governance Drift Detection (from KSI-CNA-08)

**KSI-AFR-09-Q054**: Implement continuous monitoring for governance drift including bias drift and explainability degradation in production models. How is drift detected and reported? What thresholds trigger escalation?

---

## Mapping to Implementation Recommendations

These questions map to the six ranked implementation recommendations from the KSI-AFR-09 research report:

### Recommendation 1: Probabilistic Validation Frameworks (CRITICAL)
- Questions: KSI-AFR-09-Q001, Q002, Q003, Q028, Q029, Q030

### Recommendation 2: Continuous Model Drift Detection (CRITICAL)
- Questions: KSI-AFR-09-Q004, Q005, Q006, Q031, Q032

### Recommendation 3: Per-Invocation Runtime Authorization (CRITICAL)
- Questions: KSI-AFR-09-Q007, Q008, Q009, Q045, Q033, Q034, Q035

### Recommendation 4: Hallucination Detection and Evidence Grounding (HIGH)
- Questions: KSI-AFR-09-Q010, Q011, Q012, Q047, Q036, Q037, Q038

### Recommendation 5: AI Supply Chain Verification (HIGH)
- Questions: KSI-AFR-09-Q013, Q014, Q015, Q048, Q039, Q040, Q041

### Recommendation 6: Emergent Behavior Detection (MEDIUM)
- Questions: KSI-AFR-09-Q016, Q017, Q018, Q042, Q043

### Cross-Cutting Concerns
- Questions: KSI-AFR-09-Q019, Q020, Q021, Q022, Q023, Q024, Q025, Q026, Q027, Q044, Q046, Q049, Q050, Q051

---

## Notes on Removed and Moved Questions

### Questions Moved to KSI-AFR-03 (Evidence Sharing and Export)
These focus on accessibility/format of evidence more than the validation mechanism itself:
- Evidence access modality (real-time vs periodic)
- Validation status dashboards and reporting
- Audit logs of validation activities
- Visibility into automation coverage
- Evidence retention and audit trail reconstruction

### Questions Moved to KSI-CMT-03 (Automated Testing & CI/CD Validation)
These focus on testing pipeline patterns more than persistent FedRAMP 20x validation:
- Shadow deployment mechanisms for model validation
- Shadow deployment metrics and duration
- Canary deployment processes
- A/B testing validation demonstration

### Questions Removed
Removed for being too generic or overlapping with incident response/governance KSIs:
- SLA commitments for validation failure remediation (better in IR/governance)
- High-level documentation verification (covered more specifically elsewhere)
- Security incident escalation mechanics (belongs in incident response)
- Validation SLA compliance tracking (duplicate coverage, IR-focused)

---

## Usage Guidance

These questions support persistent validation assessment across all stakeholder roles and use perspective-neutral language applicable to architecture planning, technology selection, capability assessment, vendor evaluation, contract negotiation, and formal assessment activities.

---

## References

This question library was developed based on:
- KSI-AFR-09 Comprehensive Research Report
- FedRAMP 20x Key Security Indicators Framework
- FedRAMP RFC-0017: Persistent Validation and Assessment Framework
- NIST AI Risk Management Framework
- OWASP Top 10 for LLM Applications

---

**Document Version**: 2.1
**Last Updated**: 2026-01-13
