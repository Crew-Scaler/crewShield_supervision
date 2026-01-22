# Automated Testing and Validation: CI/CD Quality Gates for AI Systems

**KSI Focus:** CMT-03 - Validate AI model and system changes through automated testing and continuous validation integrated into the deployment pipeline.

**Processing Summary:**
This discovery question set has been refined based on GitHub issue #15 feedback to focus strictly on **automated testing of changes in the SDLC/CI-CD pipeline** that block or gate deployments. Questions removed or relocated: Section 4 (Agent Testing - 6 questions moved to dedicated Agent KSI), Section 6 (Fairness - 6 questions moved to dedicated Fairness KSI), Section 7 (Hallucination - 6 questions moved to dedicated Hallucination KSI), Section 8 (Production Monitoring - 6 questions moved to Monitoring/Operations KSI), Section 9 (Compliance - 4 questions moved to Compliance KSI). From Section 2 (Probabilistic Testing), Q08 and Q09 moved to ML Lifecycle/Monitoring KSI. From Section 5 (Adversarial Testing), Q23 and Q25 moved to Security/Adversarial Resilience KSI. **Result: 48 questions reduced to 14 core CMT-03 questions, all directly addressing deployment-gating testing automation.**

---

## Pre-Deployment Testing Program and Multi-Dimensional Coverage

**CMT-03-Q001:** Provide your comprehensive pre-deployment testing policy for AI systems. What testing dimensions are mandatory before production release: (1) functional correctness (accuracy, precision, recall), (2) security (adversarial robustness, jailbreak resistance), (3) fairness and bias, (4) hallucination detection and factuality, (5) robustness and stress testing, (6) regulatory compliance? Are different testing requirements mandated for different risk tiers (high-risk vs. low-risk AI systems)?

**CMT-03-Q002:** Describe your multi-layer testing pipeline from development through production deployment. What tests execute at each stage: (1) pre-commit (local developer testing), (2) CI build (unit tests, SAST, SCA, secrets detection), (3) CI integration (integration tests, container scanning, SBOM), (4) pre-deployment staging (E2E tests, performance, chaos engineering, security), (5) smoke tests in production? What quality gates block merge, block deployment, or require manual approval?

**CMT-03-Q003:** How do you handle non-determinism in AI testing? Describe your approach to: (1) testing when outputs vary across runs, (2) validating probability distributions rather than exact outputs, (3) measuring confidence intervals and prediction uncertainty, (4) replacing traditional code coverage metrics (100% line coverage claims are illusory for AI). Do you use uncertainty quantification tools (Lightning UQ Box, Evidently AI) to validate prediction confidence?

**CMT-03-Q004:** For 100 production AI models deployed in past 6 months, provide pre-deployment testing evidence. For 20 highest-risk models (per NIST AI RMF categorization), demonstrate: (1) test dataset details, size, and representativeness, (2) performance metrics (accuracy, precision, recall, F1-score) with hold-out validation, (3) champion vs. challenger model comparison, (4) confidence interval validation, (5) approval evidence. What testing efficiency metrics do you track (coverage, bug detection, test execution time)?

**CMT-03-Q005:** Do you use advanced testing techniques beyond traditional unit tests? Provide evidence of: (1) fuzzing (automated input generation to discover edge cases), (2) metamorphic testing (using invariant relations instead of fixed test oracles), (3) differential testing (comparing multiple implementations for inconsistencies), (4) intelligent test selection (selecting only relevant tests based on code changes), (5) AI-powered test generation. What efficiency improvements have you measured (baseline: FlashFuzz 101-212% coverage improvement)?

**CMT-03-Q006:** What happens when pre-deployment tests fail? Provide evidence: (1) sample of 10 deployments blocked by test failures in past 3 months, (2) failure reason and remediation taken, (3) time to remediate and re-test, (4) root cause analysis process. Are test failures tracked in version control with full audit trail, or are failures sometimes ignored to meet deployment deadlines?

---

## Probabilistic and Non-Deterministic Testing Validation

**CMT-03-Q007:** How do you validate probabilistic AI outputs across multiple runs? Describe methodology: (1) How many inference runs do you execute for each test case to establish confidence intervals? (2) What statistical methods do you use to validate outputs fall within acceptable ranges? (3) Do you measure prediction confidence and validate calibration (confidence matches actual accuracy)? (4) For language models, do you test output diversity and consistency across multiple generations of same prompt?

**CMT-03-Q008:** For regression testing of AI models, what metrics indicate an unacceptable performance drop? Provide thresholds: (1) accuracy drop >X% triggers rollback? (2) latency increase >Y% is unacceptable? (3) calibration drift >Z% is monitored? (4) fairness metrics degradation thresholds? Describe process when a challenger model shows performance regression: is deployment blocked, or is there exceptions process?

---

## Advanced Fuzzing and Test Automation Techniques

**CMT-03-Q009:** Do you use advanced fuzzing to discover edge cases and vulnerabilities in AI systems? Provide evidence: (1) fuzzing platform/tool used (FlashFuzz, EdgeFuzz, or custom), (2) types of inputs tested (text fuzzing for NLP, image perturbations for vision, structured data variations), (3) number of fuzz test cases generated per model, (4) critical bugs discovered via fuzzing in production AI systems. What is your fuzzing coverage improvement compared to baseline (FlashFuzz: 101-212%)?

**CMT-03-Q010:** Do you use AI-powered or automated test generation? Provide: (1) test generation tool/framework used (if any), (2) success rate of generated tests (industry baseline: 71.5%), (3) types of test cases generated (edge cases, boundary conditions, adversarial inputs), (4) examples of bugs discovered by generated tests that manual tests missed. How do you validate generated test case quality?

**CMT-03-Q011:** How do you measure and optimize test efficiency? Provide metrics from past 12 months: (1) test execution time trends (are tests getting faster or slower?), (2) bug detection rate per test (do tests catch real defects?), (3) mean time to root cause analysis for failures, (4) test case reduction through intelligent selection. Have you achieved efficiency improvements comparable to research baselines (EdgeFuzz: 112.2% F1-score improvement)?

**CMT-03-Q012:** What testing tools are integrated into your CI/CD pipeline? For each, provide: (1) tool name and version, (2) what it tests (SAST, SCA, secrets detection, license compliance, container scanning), (3) how many critical/high severity findings are typically found per 100 commits, (4) when findings block deployment vs. require manual review. Do you use SBOM generation and dependency vulnerability scanning for AI artifacts?

---

## Adversarial Robustness and Security Testing (Deployment-Gating)

**CMT-03-Q013:** Do you conduct adversarial robustness testing against attack prompts and jailbreaks as a pre-deployment gate? Describe: (1) attack dataset used (JailbreakRadar: 1,400+ prompts; or custom dataset size), (2) attack categories covered (prompt injection, role-play, instruction override, encoding tricks, multi-turn scenarios), (3) testing methodology (automated testing vs. manual red team), (4) attack success rate (ASR) measured and tracked, (5) deployment gate: minimum acceptable ASR threshold that must pass before release. What is your current ASR compared to commercial baseline (80% bypass rate)?

**CMT-03-Q014:** For generative AI systems, what defense mechanisms prevent jailbreaks and are validated in pre-deployment testing? Document: (1) input filtering and test coverage (does it catch obviously malicious requests?), (2) output filtering test coverage (does it sanitize harmful completions?), (3) adversarial training validation (was the model trained on jailbreak examples and verified?), (4) safety fine-tuning validation (was the model specifically trained for safety and tested?). For each defense layer, provide false positive rate (blocking benign requests) and false negative rate (allowing attacks through) from pre-deployment tests.

**CMT-03-Q015:** How do you test for prompt injection vulnerabilities specific to RAG (Retrieval-Augmented Generation) systems pre-deployment? Describe: (1) RAG integrity validation testing (retrieved documents contain expected information), (2) injection attack testing (can attacker craft malicious documents to manipulate model output?), (3) out-of-distribution detection testing (does system recognize when retrieval fails to find relevant documents?), (4) attribution validation testing (does system correctly cite retrieved documents?). Provide examples of injection attacks discovered and remediated pre-deployment.

**CMT-03-Q016:** Do you conduct chaos engineering and fault injection testing for AI systems as part of pre-deployment validation? Provide: (1) failure scenarios tested (network latency, service unavailability, resource exhaustion, cascading failures), (2) monitoring and alerting validation (do alerts fire correctly during failures?), (3) recovery mechanism validation (do system recovery procedures work as expected?), (4) blast radius assessment (what is the scope of impact if AI system fails?). How does AI system failure affect dependent services downstream?

**CMT-03-Q017:** Do you conduct adversarial testing of AI-generated code as a pre-deployment quality gate? Describe: (1) testing methodology for code generated by AI assistants (static analysis, dynamic testing, fuzzing, symbolic execution), (2) types of adversarial attacks tested (prompt injection in code comments, hidden malicious code patterns, unsafe dependencies, cryptographic weaknesses, injection vulnerabilities), (3) code generators tested (GitHub Copilot, Claude Code, CodeT5, custom models), (4) detection rate of common vulnerabilities in AI-generated code (OWASP Top 10 vulnerabilities, dependency vulnerabilities, insecure defaults), (5) deployment gate: minimum acceptable pass rate for adversarial testing before code merge/deployment. Provide examples of vulnerabilities discovered in AI-generated code through adversarial testing.

---

## Isolated Test Environment Provisioning and Test Data Management

**CMT-03-Q018:** Can AI agents automatically generate or provision isolated infrastructure test environments from IaC definitions (including stubs and mocks for external services), and what guardrails prevent misuse of test environments or unintended changes to production?[1]

*Note: This question moved from KSI-MLA-05 as it directly addresses automated test environment creation as part of testing and validation practices.*

---

## AI-Generated Test Procedures and Runbook Quality

**CMT-03-Q019:** For AI-generated recovery procedures (LLM-generated runbooks), what quality assurance ensures procedures work correctly before use? Provide: (a) LLM-generation process (prompts, context provided for generation), (b) validation procedures (syntax checking, semantic validation, test execution), (c) testing methodology (procedures tested in lab before production deployment), (d) failure rate of AI-generated procedures in practice, (e) comparison of AI-generated vs. manually-written procedure effectiveness.

## Automated Remediation Testing (from KSI-CNA-08)

**CMT-03-Q020:** Before deploying automated remediation rules in production, what percentage of rules undergo testing to validate that corrective actions won't disrupt legitimate operations? Do you test specifically against AI workloads? What testing coverage is required before deployment gates approve rules?

**CMT-03-Q021:** Before automated remediation rules are deployed in production, are they required to pass specific testing? What testing standards apply? How frequently are remediation rules tested after deployment for continued effectiveness?

**CMT-03-Q022:** When automated enforcement actions introduce new vulnerabilities or cause system disruptions, what is the process for rolling back enforcement actions? How quickly can rollback occur? Are rollback procedures tested before remediation deployment?

---

## Schema Reference

**Question ID Format:** CMT-03-Q### (zero-padded)
Example: CMT-03-Q001, CMT-03-Q010, CMT-03-Q016

**All questions should be answered with:**
- Direct evidence (testing logs, reports, metrics) not claims
- Quantifiable data where applicable (test coverage %, detection rates, response times)
- Supporting documentation and examples
- AI-specific test examples where relevant
- Timeline and frequency information for ongoing testing and monitoring

---

**Version:** 2.2 (Refined per Issue #15, Issue #41, Issue #61)
**Generated:** 2026-01-13
**Questions:** 21 core CMT-03 questions (16 from Issue #15 refinement, 1 added from KSI-RPL-01 per Issue #41, 3 added from KSI-CNA-08 per Issue #61)
**Focus:** Pre-deployment testing automation in CI/CD pipelines that gate deployments, including remediation rule testing
**Processing:** Removed out-of-scope sections on agent testing, fairness, hallucination detection, production monitoring, and compliance; consolidated and refocused remaining questions on deployment-gating quality gates; Q018 added for AI-generated runbook quality assurance; Q019-Q021 added for automated remediation testing per Issue #61
