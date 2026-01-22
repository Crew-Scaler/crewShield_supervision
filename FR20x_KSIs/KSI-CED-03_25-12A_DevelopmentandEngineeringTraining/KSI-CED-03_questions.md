# KSI-CED-03: Development and Engineering Training - Question Library

**KSI Title:** Development and Engineering Training
**KSI Requirement:** Persistently review the effectiveness of role-specific training delivered to development and engineering staff covering best practices for secure software delivery.

**Document Version:** 2.0
**Date:** January 13, 2026
**Classification:** Internal Working Document

---

## Processing Summary

**Original Question Count:** 40 questions (v1.0)
**Questions Removed:** 9 (better fits for other KSIs per GitHub Issue #58 review)
  - Q003, Q012, Q014, Q015, Q016, Q020, Q024, Q032, Q038
**Questions Moved:** 7 questions to other KSIs
  - CED-01: Q003, Q012, Q020 (enterprise-wide training strategy)
  - CED-02: Q006, Q007, Q030, Q032 (role-specific governance)
  - CMT-01/CMT-03: Q014, Q015, Q016, Q024 (monitoring/testing controls)
**Questions Consolidated:** 3 questions (consolidated narrative from multiple sources)
**Questions Retained:** 31 core CED-03 questions
**Final Question Count:** 31 questions (perspective-neutral, focused on training effectiveness assessment)

**Perspective-Based Sections Removed:**
- All strategic assessment guidance sections (CIO, Customer, Auditor distinctions)
- Framework usage guidelines by role - replaced with unified assessment focus
- All questions now perspective-neutral and assessment-focused

---

## Question Categories

### Category 1: Training Program Architecture and Effectiveness Measurement (5 questions)

**KSI-CED-03-Q001** – What formal training program exists for secure software development practices specific to development and engineering staff? Does it address AI/ML-specific secure development content or focus exclusively on traditional secure coding principles? How is training tailored by developer role (frontend, backend, ML engineers, DevOps, security engineers)?

**KSI-CED-03-Q002** – Who owns training effectiveness measurement for development and engineering training? Describe the measurement framework, metrics tracked, and review cadence. What correlation exists between training completion/assessment scores and actual secure development practices observed in production?

**KSI-CED-03-Q003** – What baseline training effectiveness metrics are established pre-implementation, enabling before-and-after comparison and statistical validation of training impact? What demonstrates that training actually improves secure development behaviors versus proxy metrics (completion rates, satisfaction scores)?

**KSI-CED-03-Q004** – Has your organization conducted a skills gap analysis identifying knowledge deficiencies in AI-specific threat domains relevant to development staff (prompt injection recognition, AI-generated code validation, agent authorization patterns, model provenance verification)?

**KSI-CED-03-Q005** – Do you currently track behavioral compliance metrics beyond knowledge assessments for development staff? If yes, what specific secure development behaviors are monitored?

---

### Category 2: AI-Generated Code Security Validation (5 questions)

**KSI-CED-03-Q006** – What code review processes and guidelines exist specifically for AI-generated code contributions? How do these differ from traditional code review practices? Are reviewers trained on AI-specific code security patterns?

**KSI-CED-03-Q007** – Are static analysis (SAST) and dynamic analysis (DAST) findings tracked separately for AI-assisted commits versus human-written code? What is the comparative vulnerability density?

**KSI-CED-03-Q008** – What is the peer review effectiveness rate for human reviewers detecting security vulnerabilities in AI-generated code? What percentage of AI-assisted commits require security-related revisions post-merge?

**KSI-CED-03-Q009** – Does Git history forensics analysis track AI-code revert rates and post-merge security patches? What percentage of AI-assisted commits are reverted due to security issues?

**KSI-CED-03-Q010** – What is your organization's AI code suggestion rejection rate for security reasons? What percentage of developers reject AI-generated code based on security concerns, and what training supports this critical review behavior?

---

### Category 3: AI Threat Recognition and Incident Response Training (4 questions)

**KSI-CED-03-Q011** – What training content addresses AI-specific attack vectors relevant to development environments? (Examples: prompt injection, hallucinations, model poisoning, memory attacks, semantic privilege escalation). Provide evidence that developers can recognize these threats in code reviews.

**KSI-CED-03-Q012** – What is the average time-to-report for developers identifying suspected AI-related security anomalies? What training supports rapid escalation of suspicious AI behavior?

**KSI-CED-03-Q013** – Are developers trained on hallucination validation and independent verification against authoritative sources when using AI recommendations for security-critical implementations?

**KSI-CED-03-Q014** – What red team exercises or tabletop drills specific to AI security scenarios are conducted with development teams? (Examples: prompt injection in documentation, AI-generated malicious code detection). What is developer performance on these simulations?

---

### Category 4: AI Agent Authorization and Architecture Security Training (3 questions)

**KSI-CED-03-Q015** – Are developers and DevOps staff trained on AI agent authorization frameworks, guardrail implementation, and human-in-the-loop approval patterns for autonomous systems? What evidence demonstrates they can design least-privilege agent deployments?

**KSI-CED-03-Q016** – Are developers trained on agent memory input validation and sanitization procedures to prevent memory poisoning attacks through malicious data injection?

**KSI-CED-03-Q017** – Does training explicitly cover the authorization differences between traditional IAM (user-based, role-based access control) and agent-based permission models (service principals, API key management, scoped delegation)?

---

### Category 5: Continuous Assessment and Knowledge Retention (6 questions)

**KSI-CED-03-Q018** – At what intervals post-training is developer competency in secure AI development practices measured? (Immediately post-course, 3 months, 6 months, 12 months). What assessment methods are used (knowledge tests, practical exercises, code review performance)?

**KSI-CED-03-Q019** – What is your organization's observed knowledge retention curve for AI security training? (Example: 85% immediately post-training, declining to what percentage at 6 months and 12 months?). How does this compare to traditional secure coding knowledge retention (12-18 month half-life)?

**KSI-CED-03-Q020** – How does training address the accelerated obsolescence cycle for AI threat knowledge (3-6 month decay versus 12-18 months for traditional secure coding knowledge)? What reinforcement mechanisms keep training current?

**KSI-CED-03-Q021** – Are quarterly unannounced spot-check assessments conducted testing AI security knowledge retention through scenario-based exercises rather than knowledge recall tests?

**KSI-CED-03-Q022** – What continuous learning and reinforcement strategy is implemented (microlearning, just-in-time training, lunch-and-learns, ongoing simulations, threat intelligence integration)? How frequently is training content updated?

**KSI-CED-03-Q023** – When an AI-related security incident occurs in your organization, how do you determine if training gaps contributed? Provide documentation of your incident-to-training feedback process and examples of training updates triggered by incidents.

---

### Category 6: Emerging Threats and Curriculum Agility (3 questions)

**KSI-CED-03-Q024** – How do you identify emerging AI threats to include in training? What sources do you monitor (threat intelligence feeds, incident analysis, framework updates, academic research, public incidents)?

**KSI-CED-03-Q025** – What is your process and timeline for updating training content when new AI threats emerge or when regulations change? Target: updates within 30 days of new MITRE ATLAS technique. Provide recent examples of training updates with dates.

**KSI-CED-03-Q026** – Does training cover recent AI threats discovered in 2024-2025? Examples: LLM jailbreaking, prompt injection variants, AI-powered phishing, steganographic collusion, deepfake audio/video. Provide training materials demonstrating coverage.

---

### Category 7: Training for Infrastructure-as-Code (IaC) Security (1 question)

**KSI-CED-03-Q027** – What training do infrastructure and DevOps engineers receive on securing IaC templates (Terraform, CloudFormation, Helm)? Does training cover using AI agents to evaluate IaC for modularity, reuse, and maintainability? How are AI-identified technical debt issues communicated as training reinforcement?

---

### Category 8: Post-Training Behavior Validation and Incident Correlation (4 questions)

**KSI-CED-03-Q028** – How is the secondary verification adoption rate measured for AI-generated security-critical code? What percentage of developers manually review AI suggestions before integration into security-critical paths?

**KSI-CED-03-Q029** – How is prompt security quality measured for developers using AI coding assistants? What percentage of developer prompts explicitly include security requirements or constraints?

**KSI-CED-03-Q030** – Of AI-related security incidents in the past 12 months, what percentage can be traced to inadequate development training or knowledge gaps versus tool misconfiguration or architectural flaws? What root cause analysis process validates this?

**KSI-CED-03-Q031** – What feedback loop exists from security incident investigation back to training curriculum updates? What is the average time from incident discovery to training content revision (target: less than 30 days)?

---

## Questions Moved to Other KSIs

The following questions from v1.0 have been relocated to better-fitting KSIs per GitHub Issue #58 guidance:

**Moved to KSI-CED-01 (General Training / Governance):**
- Q003 (Training budget allocation) - Enterprise-wide training strategy
- Q012 (AI adoption rate) - AI adoption context for all CSP staff
- Q020 (AI tool usage adoption) - Enterprise AI tool governance

**Moved to KSI-CED-02 (Role-Specific High-Risk Training):**
- Q006 (Contractors/third parties) - Contractor training governance
- Q007 (AI-related topics coverage) - Role-to-topic mapping for high-risk roles
- Q030 (Least-privilege compliance) - High-risk role authorization training
- Q032 (Architecture design reviews) - High-risk role design review procedures

**Moved to KSI-CMT-01/CMT-03 (Logging, Monitoring, Testing):**
- Q014 (Shadow AI tool detection) - Endpoint monitoring/control
- Q015 (DLP violations) - Incident/monitoring controls
- Q016 (Behavioral telemetry) - Logging design (CMT-01)
- Q024 (Adversarial testing) - Pre-deployment testing automation (CMT-03)

**Question Q038 (12-24 month longitudinal studies):** Consolidated into Q19-Q23 (continuous assessment focus)

---

## Removed Questions

None permanently removed. All questions either retained (27) or moved to more appropriate KSIs (9). Rationale for movement documented above.

---

## Refinement Rationale

This v2.0 refinement addresses GitHub Issue #58 feedback to:

1. **Tighten Scope:** Removed questions better-suited to enterprise governance (CED-01) and high-risk role governance (CED-02), and control implementation (CMT-01/03)
2. **Eliminate Perspective Bias:** Removed all strategic vs. operational vs. compliance perspective distinctions; all questions now perspective-neutral
3. **Focus on Training Effectiveness Assessment:** Retained only questions directly measuring whether training produces secure development behaviors
4. **Consolidate Overlapping Content:** Merged overlapping metrics/assessment questions where possible
5. **Emphasis on Behavioral Validation:** Prioritized questions measuring actual secure practices over proxy metrics

**Core CED-03 Mandate:** Validate that role-specific training for development and engineering staff demonstrably improves secure software delivery practices, with emphasis on:
- Ongoing measurement of training effectiveness (not one-time assessments)
- Behavioral observation and incident correlation (not proxy metrics)
- AI-specific secure development competencies
- Rapid curriculum agility for emerging AI threats

---

## FedRAMP 20x Alignment

These questions operationalize FedRAMP 20x's "persistent review of effectiveness" mandate by:

1. **Continuous Monitoring:** Questions 18-23 validate continuous assessment versus annual point-in-time reviews
2. **Behavioral Observation:** Questions 5, 8-10, 28-29 measure actual secure practices, not proxy metrics
3. **Role-Specific Measurement:** Questions 1, 4, 15-17 segment effectiveness by engineering sub-role
4. **Causal Attribution:** Questions 3, 30-31 establish baselines and validate training impact on incidents
5. **Curriculum Agility:** Questions 22-26 ensure training content remains current with emerging threats
6. **Incident Correlation:** Questions 30-31 link training directly to security outcomes

---

## References

- FedRAMP 20x Key Security Indicators Documentation
- KSI-CED-03 Report: Development and Engineering Training (January 2026)
- KSI-CED-03 Cluster Synthesis: AI/Agent Focus (January 2026)
- NIST SP 800-53 Controls: AT-2, AT-3, AT-4, SI-2, SI-4, CA-7
- GitHub Issue #58: Discovery Question Review and Refinement

---

**Document End**

*This question library supports KSI-CED-03 implementation planning, control validation, and audit preparation. Questions should be answered with direct evidence, quantifiable data where applicable, and supporting documentation. All questions are perspective-neutral and focused on assessing training effectiveness for secure software development practices.*
