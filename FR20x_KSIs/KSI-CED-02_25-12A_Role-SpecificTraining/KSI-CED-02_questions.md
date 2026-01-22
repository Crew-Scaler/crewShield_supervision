# AI-Specific Role-Based Training Effectiveness: Discovery Questions

**KSI Focus:** CED-02 - Persistently review the effectiveness of role-specific training given to employees in high-risk roles, including at least roles with privileged access.

## Section 1: Training Existence and Role-Specific Scope

**CED-02-Q001:** Provide your complete AI security training catalog: course titles, descriptions, learning objectives, target roles, delivery format (online, in-person, hybrid), and estimated completion time per course. What is the total training duration per role, broken down as a role-to-training matrix showing required courses and hours?

**CED-02-Q002:** For each high-risk role (cloud engineers, AI/ML engineers, SOC analysts, IAM admins, incident responders, DevSecOps, GRC staff, executives), what percentage of current incumbents have completed foundational AI security training? What percentage have completed role-specific AI training?

**CED-02-Q003:** What is your required training completion timeline (e.g., within 30 days of hire, 90 days, annually for refresher)? How many high-risk role staff are currently non-compliant (have not completed required training)?

**CED-02-Q004:** When was your AI security training curriculum last updated? What is the review and update frequency (quarterly, annually, ad-hoc)?

**CED-02-Q005:** What is your training and oversight program for contractor and third-party staff who have access to development, security, or AI systems? Does contractor onboarding include AI-specific security training? How frequently are contractors required to complete refresher training? How is contractor compliance monitored and enforced?

**CED-02-Q006:** For each high-risk role, what specific list of AI-related secure development topics are covered in training? Does training explicitly cover: prompt injection vulnerability identification, AI-generated code security validation, agent authorization patterns, model provenance verification, adversarial robustness evaluation, secure RAG implementation, training data lineage tracking, and multi-agent coordination security? Provide training materials demonstrating topic coverage per role.

**CED-02-Q007:** For privileged role staff managing AI agents and autonomous systems, how is compliance with least-privilege authorization enforced and monitored in training and practice? What percentage of deployed AI agents operate with least-privilege permissions (minimum necessary access)? What training do staff receive on identifying and remediating over-privileged agent configurations?

**CED-02-Q008:** For architecture and design roles responsible for AI systems, what training covers architecture design review processes specific to AI systems? Does training include: threat modeling for AI systems, security architecture patterns for agents, deployment architecture validation, incident response planning for AI failures, and recovery procedures for compromised AI systems? How is this training effectiveness measured through design review quality assessments?

---

## Section 2: Role-to-AI-Threat Mapping

**CED-02-Q009:** Do you have a documented role-to-AI-threat mapping for high-risk roles? Does it include AI-specific threats such as prompt injection, model poisoning, AI-enhanced phishing, data leakage, jailbreaking, deepfakes, and AI-enhanced insider threats? Provide the mapping document.

**CED-02-Q010:** For each high-risk role, what percentage of staff can demonstrate these competencies: (1) Recognize MITRE ATLAS tactics, (2) Detect prompt injection attempts, (3) Identify data poisoning risks, (4) Properly use AI tools without leaking secrets, (5) Respond to AI-specific incidents? Where are critical competency gaps (>50%)?

---

## Section 3: Training Effectiveness Measurement and Incident Impact

**CED-02-Q011:** How do you measure AI security training effectiveness? Describe all metrics tracked (completion rates, assessment scores, incident reduction, behavior change, staff feedback). Provide sample data from the past 12 months, disaggregated by role where available.

**CED-02-Q012:** Do you conduct pre-training and post-training competency assessments? Provide aggregate data from the most recent training cohort showing: average score improvement, statistical significance of improvement (if available), and percentage of staff showing meaningful improvement (10+ percentage points).

**CED-02-Q013:** Do you assess practical skills (not just knowledge)? Provide evidence of practical skills assessments such as lab exercises, tabletop exercises, or simulations where staff demonstrate ability to detect prompt injection, identify adversarial examples, or respond to AI-specific incidents. What percentage of trained staff successfully complete practical scenarios?

**CED-02-Q014:** In the past 24 months, how many AI-related security incidents have occurred? For each incident, indicate: (1) incident type (phishing, deepfake, prompt injection, data leakage, model abuse, insider threat using AI), (2) whether involved staff had completed AI security training, (3) if trained staff were involved, what was the root cause (training deficiency, non-compliance, novel threat not covered), (4) response metrics (MTTD, MTTR, triage accuracy) compared to untrained responders. Summarize correlation between training and incident frequency/severity reduction.

**CED-02-Q015:** How do you use effectiveness data to improve training? Provide specific examples of curriculum changes made based on assessment data, incident analysis, or feedback (e.g., "Assessment scores low for module X, so we added interactive lab; scores improved 15 points").

---

## Section 4: Framework Alignment and Content Coverage (Consolidated)

**CED-02-Q016:** For each high-risk role, which AI frameworks and regulations are covered in training (examples: NIST AI RMF, MITRE ATLAS, OWASP Top 10 for LLMs, EU AI Act, ISO 42001, sector-specific rules)? How is role-relevance ensured for each framework? Provide training materials demonstrating coverage.

---

## Section 5: High-Risk Role Coverage - Specific Domains

**CED-02-Q017:** For SOC analysts and incident responders, what AI-specific training do they receive? Does training cover: detecting AI-powered attacks, responding to AI-related incidents, AI threat intelligence integration, secure use of AI-powered SOC tools (anomaly detection, threat intelligence, triage automation)?

**CED-02-Q018:** For AI/ML engineers and data scientists, what secure development and deployment training do they receive? Does it cover: secure AI development practices, MLOps security, protecting training data and inference data, securing AI services in multi-tenant environments, model validation and testing?

**CED-02-Q019:** For cloud/platform engineers and DevSecOps, what AI system security training do they receive? Does it cover: deploying AI workloads securely, AI infrastructure isolation, AI model access controls, AI inference logging, AI configuration-as-code security?

**CED-02-Q020:** For IAM and privileged access administrators, what AI-specific training do they receive? Does it cover: managing AI agent identities, AI-specific IAM patterns (service principals, API keys for models), monitoring AI agent behavior, supporting customers' AI agent governance?

**CED-02-Q021:** For GRC, legal, and compliance roles, what AI governance and regulatory training do they receive? Does it cover: NIST AI RMF governance function, ISO 42001 requirements, EU AI Act compliance, sector-specific AI regulations, AI risk assessment and documentation?

**CED-02-Q022:** For executives (C-suite, VPs, directors), what AI security and governance training do they receive? Does it cover: AI strategic risks, AI governance oversight, regulatory compliance requirements, board-level reporting on AI security, incident communication for AI-related breaches?

---

## Section 6: Practical Training and Skills Assessment

**CED-02-Q023:** What hands-on lab exercises do you provide for AI security training? Provide examples covering: prompt injection detection and mitigation, deepfake analysis and detection, model poisoning identification, AI-powered phishing response, adversarial example recognition.

**CED-02-Q024:** Do you conduct simulated AI-powered attacks against staff (AI-generated phishing, deepfake audio/video, prompt injection attempts)? How frequently (quarterly recommended, annual minimum)? What are the detection/reporting rates? Do results show trained staff have 50%+ better performance than untrained staff?

**CED-02-Q025:** Do you conduct AI incident response tabletop exercises? Provide examples of scenarios covered: model poisoning detection and response, AI-powered data breach, prompt injection attack, deepfake-enabled fraud. Which roles participate (cross-functional: SOC, incident response, AI/ML, legal, communications, executives)?

**CED-02-Q026:** For staff who fail AI-specific simulations or assessments, what remediation or targeted retraining is provided? How is improvement measured after remediation?

---

## Section 7: AI Tool Usage Training (Slimmed Scope)

**CED-02-Q027:** Does role-specific training clearly explain approved vs. prohibited AI tool usage for each high-risk role, and how is comprehension verified (quiz, practical exercise, acknowledgment)? Examples: what data can/cannot be entered, which tools are approved, how to request exceptions.

---

## Section 8: Continuous Improvement and Emerging Threats

**CED-02-Q028:** How do you identify emerging AI threats to include in training? What sources do you monitor (threat intelligence feeds, incident analysis, framework updates, academic research, public incidents)? Provide examples of recent training updates triggered by emerging threats.

**CED-02-Q029:** What is your process and timeline for updating training content when new AI threats emerge or when regulations change? Target: updates within 30 days of new MITRE ATLAS technique, within 60 days of major AI incident. Provide examples of recent training updates with dates.

**CED-02-Q030:** Does training cover recent AI threats discovered in 2024-2025? Examples: LLM jailbreaking (100% success rate with adaptive attacks), prompt injection variants, AI-powered phishing, steganographic collusion, deepfake audio/video. Provide training materials demonstrating coverage.

**CED-02-Q031:** How do you incorporate lessons learned from public AI incidents (Microsoft EchoLeak, Google Gemini prompt injection, ChatGPT data leakage, Anthropic Claude prompt injection)? Are these case studies included in training materials?

**CED-02-Q032:** How do you ensure all staff receive updated training content, not just new hires? Describe your mechanism for communicating and mandating updates to existing staff (newsletters, mandatory refresher, login-gate enforcement).

**CED-02-Q033:** When an AI-related security incident occurs in your organization, how do you determine if training gaps contributed? Provide documentation of your incident-to-training feedback process. Give 2-3 examples of incidents that led to training updates.

---

## Section 9: Training Frequency and Continuous Learning

**CED-02-Q034:** How frequently is AI security training delivered to high-risk roles (one-time on hire, annual refresher, quarterly updates)? Research shows continuous training is 50% more effective than one-time training. Describe your continuous learning and reinforcement strategy (microlearning, just-in-time training, lunch-and-learns, ongoing simulations).

---

## Schema Reference

**Question ID Format:** [KSI-CODE]-Q###
Example: CED-02-Q001

**All questions should be answered with:**
- Direct evidence (not claims)
- Quantifiable data where applicable
- Supporting documentation when available
- Role-specific breakdown (by high-risk role type)
- Timestamp of data collection

---

**Processing Notes:**

**Version 2.0 Refinements (GitHub Issue #12 Feedback):**
- Consolidated overlapping metrics questions (Q07+Q40, Q08+Q41, Q10+Q11+Q12+Q42)
- Consolidated framework coverage into single role-relevant question (Q12)
- Removed AI policy/governance questions (Q13-Q18, Q29, Q32, Q44-Q46) → better-suited to other KSIs or governance frameworks
- Removed research/aspirational questions (Q47-Q49) → focus on assessment, not external benchmarking
- Refined AI tool usage to core training effectiveness question (Q23)
- Removed perspective distinctions (CIO/Customer/Auditor) for perspective-neutral assessment
- Initial result: 30 discovery questions focused on training effectiveness assessment
- Previously extended with 6 questions on analyst burnout from INR-03 (Version 2.0 final: 36→39 questions after renumbering)

**Version 2.1 Refinements (Task 2 Fine-tuning):**
- Removed Section 10 (Q034-Q039): Alert Fatigue, Analyst Burnout & Trust Restoration questions
- Rationale: Out-of-scope for CED-02 (role-specific training effectiveness); better-suited to INR-03 or MLA-01
- Result: 34 discovery questions focused exclusively on training effectiveness assessment

**Version:** 2.1
**Generated:** 2026-01-13
