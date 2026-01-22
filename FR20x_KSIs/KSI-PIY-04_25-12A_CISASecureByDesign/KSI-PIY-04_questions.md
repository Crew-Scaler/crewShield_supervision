# CISA Secure-by-Design with AI-Augmented SDLC: Discovery Questions

**KSI-PIY-04** - CISA Secure-by-Design Initiative aligned with AI-driven secure development, autonomous agent governance, and compliance automation

**Research Foundation:** 70 papers synthesized across 7 research clusters

**Question Set Version:** 2.0 (Consolidated & Refined)
**Generated:** 2026-01-13
**Last Refined:** 2026-01-13

---

## Section 1: AI-Driven Security Automation & Threat Modeling

**KSI-PIY-04-Q1:** What AI-driven threat modeling system automatically produces STRIDE analyses, attack trees, and threat scenarios during design phase? Document: (a) tool/methodology used, (b) threat model currency (triggered by architecture changes, dependency updates, threat intelligence), (c) completeness validation (all STRIDE categories covered), (d) accuracy metrics comparing AI models to manual threat modeling, (e) integration with design decision documentation.

**KSI-PIY-04-Q2:** How frequently do you re-threat-model as architecture and dependencies evolve, and what percentage of design changes trigger threat model updates? Explain: (a) re-threat-modeling frequency (continuous vs. periodic), (b) trigger events (IaC changes, new dependencies, threat intelligence updates, incidents), (c) change impact analysis, (d) evidence of updated threat models reflecting architecture evolution, (e) linkage to security test plan updates.

**KSI-PIY-04-Q3:** How do you validate AI-generated threat models to prevent hallucinated threats and ensure rigor equivalent to manual threat modeling? Provide: (a) validation procedures before threat models inform security testing, (b) comparison to domain expert manual threat modeling, (c) acceptance criteria for AI-generated models, (d) detection of fictitious threats or missed real threats, (e) evidence of validation testing and results.

**KSI-PIY-04-Q4:** What measurable shift-left improvements have you achieved through AI threat modeling and automated code analysis? Provide: (a) % vulnerabilities found during design vs. post-deployment, (b) time-to-remediation improvements attributable to automation, (c) detection accuracy and automation coverage, (d) evidence that automation measurably improves secure-by-design outcomes, (e) metrics showing faster security improvement trajectory.

**KSI-PIY-04-Q5:** How do you prevent AI threat modeling from missing emerging attack vectors or novel threat patterns? Document: (a) threat intelligence integration (feeds updating threat models), (b) anomaly detection identifying unusual patterns, (c) expert review procedures for AI-generated models, (d) red-team exercises validating model comprehensiveness, (e) evidence of continuously improving threat model coverage.

---

## Section 2: LLM Hallucinations & Supply Chain Attack Defense (SDLC Context)

**KSI-PIY-04-Q6:** What guardrails prevent AI code generation from hallucinating non-existent packages, APIs, and libraries during design and implementation phases? Describe: (a) package existence verification (PyPI, npm, Maven Central checks), (b) hallucination detection rates (target: >95% of hallucinated packages caught), (c) developer workflow integration (warnings before importing hallucinated packages), (d) incident detection (tracking failed imports/package installation errors), (e) evidence of prevented supply chain attacks in SDLC.

**KSI-PIY-04-Q7:** What multi-layer detection and prevention strategy guards against LLM hallucinations across SDLC stages (input validation, logic layer, output layer, execution layer)? Document: (a) input validation preventing prompt injection, (b) confidence scoring for high-risk suggestions, (c) output filtering and verification, (d) runtime monitoring of generated code behavior, (e) metrics showing hallucination defense effectiveness.

**KSI-PIY-04-Q8:** How do you prevent MIRAGE-style attacks where malicious instructions injected into training data cause LLMs to generate vulnerable recommendations? Provide: (a) training data validation and vetting procedures, (b) poisoning detection (identifying suspicious data patterns), (c) Byzantine-resilient training techniques, (d) model testing for induced vulnerabilities, (e) evidence of detected and prevented data poisoning attacks.

---

## Section 3: Autonomous Agent Governance & Safety

**KSI-PIY-04-Q9:** What three-tier autonomy framework defines when AI agents act autonomously, when they require approval, and when they escalate for human decision-making? Explain: (a) Level 1 (fully autonomous for routine operations), (b) Level 2 (approval gates for medium-risk decisions), (c) Level 3 (human decision required for high-risk actions), (d) policy-as-code enforcement, (e) examples of each tier in practice.

**KSI-PIY-04-Q10:** How do you prevent autonomous agents from exhibiting emergent behavior—making locally-reasonable probabilistic decisions that collectively diverge from policy intent? Describe: (a) behavioral monitoring detecting policy drift, (b) anomaly detection identifying unusual decision patterns, (c) continuous alignment verification (agents still following intended policy?), (d) intervention procedures when drift detected, (e) examples of detected and corrected agent drift.

**KSI-PIY-04-Q11:** How do you maintain auditable accountability when AI agents make autonomous decisions, and how do you establish traceability of security-critical decisions? Document: (a) accountability framework (who is responsible for each decision?), (b) audit trail completeness (decision reasoning, alternatives considered, approvals), (c) escalation procedures for ambiguous decisions, (d) transparency to stakeholders about AI involvement in decisions, (e) evidence of effective governance enabling forensic investigation.

**KSI-PIY-04-Q12:** What governance structure defines agent identities, decision boundaries, escalation triggers, and human approvals with immutable audit trails? Provide: (a) policy-as-code documentation, (b) agent registry with identities and permissions, (c) decision boundary definitions, (d) audit logging of all agent decisions, (e) evidence of effective governance preventing unauthorized agent behavior.

**KSI-PIY-04-Q13:** How do you assess whether your autonomous agent capabilities are aligned with your organization's risk tolerance and mission criticality? Explain: (a) risk assessment methodology, (b) stakeholder approval process (security, compliance, legal), (c) periodic reviews validating alignment, (d) mechanisms for overriding/disabling agents if misaligned, (e) evidence of stakeholder governance oversight.

---

## Section 4: Secure-by-Default Infrastructure & Hardening

**KSI-PIY-04-Q14:** What "deny-by-default" infrastructure design principles ensure customers cannot make insecure configuration choices? Document: (a) services deployed with restrictive defaults, (b) encryption mandatory by default, (c) MFA required for all privileged operations, (d) audit logging enabled without additional cost, (e) examples of insecure-by-default patterns eliminated.

**KSI-PIY-04-Q15:** How do you publish hardened baseline configurations and infrastructure-as-code templates that enforce security defaults for all services? Explain: (a) baseline availability and updates, (b) security scanning of templates before release, (c) adoption rates by customers, (d) continuous improvement based on customer feedback, (e) evidence of reduced misconfiguration incidents through templates.

**KSI-PIY-04-Q16:** What design patterns (Gatekeeper, Bulkhead, Ambassador, Backend-for-Frontend, Claim Check) do you employ to embed security into infrastructure architecture? Provide: (a) pattern selection rationale, (b) implementation examples, (c) effectiveness at reducing misconfiguration vulnerabilities, (d) developer adoption (pattern usage rates), (e) incidents prevented through pattern enforcement.

**KSI-PIY-04-Q17:** How do you prevent customers from disabling or weakening security defaults, and what approval processes govern exceptions? Document: (a) API-level enforcement preventing insecure operations, (b) exception approval workflow, (c) logging and audit trail for exceptions, (d) periodic review of active exceptions, (e) evidence of reducing exceptions through improved defaults.

**KSI-PIY-04-Q18:** What customer communication ensures they understand that security defaults are not optional "security taxes" but fundamental platform capabilities? Explain: (a) training and documentation, (b) migration support for legacy non-compliant configurations, (c) transparency on security costs, (d) customer satisfaction metrics, (e) evidence of customer understanding and buy-in.

---

## Section 5: SDLC Maturity & Secure Code Review

**KSI-PIY-04-Q19:** How do you measure SDLC maturity using recognized frameworks (OWASP SAMM, NIST SP 800-218 SSDF) and track progress toward advanced maturity levels? Document: (a) maturity assessment methodology, (b) current level by dimension, (c) roadmap to higher maturity, (d) investment in maturity improvement, (e) evidence showing measurable progress.

**KSI-PIY-04-Q20:** What AI-assisted code review system automates 80%+ of manual review work while maintaining security rigor? Explain: (a) SAST integration in CI/CD pipelines, (b) automated checks (STRIDE analysis, crypto validation, API misuse), (c) human reviewer focus (business logic, architectural decisions), (d) finding remediation rates, (e) developer productivity improvements through automation.

**KSI-PIY-04-Q21:** How do you validate security test coverage is comprehensive and test all identified threats from threat modeling? Provide: (a) coverage metrics (% of components tested), (b) traceability (security requirements → tests), (c) gap analysis (untested threat scenarios), (d) metrics showing improving coverage over time, (e) evidence of threats validated through security testing.

**KSI-PIY-04-Q22:** What vulnerability density metrics do you track (target: <0.1 per 1000 LOC industry benchmark is 0.5-2.0) and how do you compare to industry peers? Document: (a) density calculation methodology, (b) trends over past 12+ months, (c) pre-production detection rate (target: >80%), (d) MTTR for critical vulnerabilities (target: <7 days), (e) comparison to peers and industry benchmarks.

**KSI-PIY-04-Q23:** How do you implement continuous integration security gates that prevent insecure code from reaching production? Explain: (a) gate enforcement (which checks are mandatory?), (b) bypass prevention (gates cannot be disabled), (c) metrics on gate effectiveness (% of vulnerabilities caught), (d) developer friction reduction (false positive management), (e) evidence of gate effectiveness preventing incidents.

---

## Section 6: Formal Verification & Compliance Automation

**KSI-PIY-04-Q24:** How do you formally verify that agent policy boundaries and escalation triggers are mathematically proven to prevent agent policy violations? Describe: (a) formal verification methodology (model checking, theorem proving), (b) policies verified (autonomy boundaries, escalation rules), (c) coverage (% of critical policies formally verified), (d) limitations of formal verification, (e) evidence of formal proofs preventing agent misuse.

**KSI-PIY-04-Q25:** What automated compliance evidence collection system generates auditor-ready proof of NIST SP 800-218 SSDF and CISA Secure-by-Design compliance? Explain: (a) evidence types collected (threat models, test results, approvals), (b) tamper-proof artifacts (digital signatures, immutable timestamps), (c) one-click export for auditors, (d) coverage of all relevant controls, (e) auditor feedback on evidence quality.

**KSI-PIY-04-Q26:** What immutable audit trail mechanisms ensure all development decisions, approvals, and code changes are logged for forensic investigation and compliance auditors? Provide: (a) audit logging completeness, (b) tamper-proof mechanisms (digital signatures, blockchain anchoring), (c) access controls for audit data, (d) retention policies, (e) evidence of audit trail usage in incident investigations.

---

## Section 7: Continuous Improvement & Capability Evolution

**KSI-PIY-04-Q27:** What continuous improvement program keeps your secure-by-design implementation aligned with evolving CISA guidance, threat landscape, and technology advances? Explain: (a) monitoring of CISA updates and threat intelligence, (b) quarterly/annual reviews assessing alignment, (c) roadmap for capability improvements, (d) stakeholder feedback mechanisms, (e) evidence of continuous improvement trajectory.

**KSI-PIY-04-Q28:** How do you measure the business impact of secure-by-design transformation (reduced incidents, faster development, lower costs, competitive advantage)? Document: (a) KPIs tracking security posture, development velocity, operational costs, (b) customer satisfaction and retention, (c) competitive differentiation claims, (d) ROI analysis of investment, (e) evidence supporting business impact claims.

**KSI-PIY-04-Q29:** How do you maintain organizational competency in secure-by-design practices through training, hiring, and knowledge management? Provide: (a) training programs for developers, architects, security teams, (b) certifications and specializations, (c) incident response drills and tabletop exercises, (d) hiring strategy for secure development roles, (e) annual competency assessments and improvements.

---

**Version:** 2.0
**Consolidation Status:** Questions refined per guidance on removing prescriptive targets, moving supply-chain/compliance/innovation questions to appropriate KSIs, narrowing focus to measurable SDLC security outcomes
**Last Updated:** 2026-01-13
