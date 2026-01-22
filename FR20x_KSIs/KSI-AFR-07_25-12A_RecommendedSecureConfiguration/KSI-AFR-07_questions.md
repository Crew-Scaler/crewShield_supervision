# KSI-AFR-07: Recommended Secure Configuration - Investigative Questions

**KSI:** KSI-AFR-07 - Recommended Secure Configuration for Cloud Service Providers
**Version:** 2.0 (Curated)
**Last Updated:** January 13, 2026
**Context:** AI/Agent-Driven Configuration Security in FedRAMP 20x

---

## Summary

This question library supports discovery and validation of secure configuration practices for AI systems and AI agents within FedRAMP 20x contexts. The questions are designed to probe how Cloud Service Providers establish, maintain, validate, and govern configuration baselines for autonomous AI systems that introduce non-deterministic behavior, dynamic access requirements, and multi-layer configuration dependencies.

### Statistics

- **Original question count:** 288
- **Questions removed:** 22 (metric-heavy, generic, or not directly investigative)
- **Questions moved to AFR-03:** 8 (data sharing/export focus)
- **Questions moved to AFR-05:** 10 (notification focus)
- **Questions moved to AFR-09:** 25 (continuous validation focus)
- **Final question count:** 227

### Key Focus Areas

1. AI-specific configuration baseline development and documentation
2. Privilege management and just-in-time access for AI agents
3. Multi-layer configuration drift detection (model, runtime, infrastructure, access)
4. Supply chain integrity verification for configuration artifacts
5. Governance workflows and human-in-the-loop approvals
6. Multi-agent coordination and configuration synchronization
7. Emergency rollback and disaster recovery procedures
8. Configuration observability and debugging capabilities
9. AI-specific configurations (model parameters, prompts, API controls)
10. Configuration audit evidence and compliance documentation

---

## Questions

**KSI-AFR-07-Q001**
Do you have documented baseline configuration templates for AI agent deployments that address model parameters, inference settings, and infrastructure requirements separately?

**KSI-AFR-07-Q002**
How do you currently document security implications for each configurable parameter (for example, temperature 0.0 vs. 1.0, token limits, context window size)?

**KSI-AFR-07-Q003**
Are your infrastructure-as-code templates (Terraform, CloudFormation) currently integrated with AI model configuration management, or do these remain separate systems?

**KSI-AFR-07-Q004**
What governance body approves configuration baselines, and how frequently are they reviewed given the rapid evolution of AI capabilities?

**KSI-AFR-07-Q005**
Do your change control processes (CM-3) currently address AI-specific changes such as model retraining, prompt template updates, and API permission modifications?

**KSI-AFR-07-Q006**
How do you manage the CSP-customer responsibility boundary for configuration decisions, particularly around fine-tuning, training data validation, and continuous learning?

**KSI-AFR-07-Q007**
Are your configuration baselines documented with security decision matrices showing trade-offs and alternatives?

**KSI-AFR-07-Q008**
How do you manage configuration lifecycle from model development through training, deployment, inference, and eventual retirement?

**KSI-AFR-07-Q009**
What is the current least-privilege ratio for your AI agent accounts (permissions granted vs. actual usage)?

**KSI-AFR-07-Q010**
Do you have Just-in-Time (JIT) access policies requiring approval before AI agents can escalate permissions, or do agents operate with pre-provisioned, static permissions?

**KSI-AFR-07-Q011**
How do you prevent over-privileged default configurations that operators grant to reduce runtime failures?

**KSI-AFR-07-Q012**
What mechanisms exist to detect and prevent autonomous privilege escalation attempts by AI agents?

**KSI-AFR-07-Q013**
How do you validate that high-privilege AI agents cannot be manipulated into performing unauthorized actions through adversarial prompts or data poisoning?

**KSI-AFR-07-Q014**
Do you have controls preventing confused deputy attacks where low-privilege users manipulate high-privilege agents?

**KSI-AFR-07-Q015**
Are these configuration controls standardized across your AI deployment platforms?

**KSI-AFR-07-Q016**
How do you configure and enforce authorization boundaries at each tool invocation point for AI agents?

**KSI-AFR-07-Q017**
Do you have automated drift detection systems monitoring configuration changes at model, runtime, infrastructure, and access control layers simultaneously?

**KSI-AFR-07-Q018**
How do you detect AI-specific configuration drift such as model parameter modifications, prompt template alterations, and tokenizer updates that do not trigger infrastructure-level alarms?

**KSI-AFR-07-Q019**
Can your anomaly detection distinguish between legitimate configuration evolution and malicious changes?

**KSI-AFR-07-Q020**
Do you track cross-layer configuration dependencies between model layer, runtime layer, infrastructure layer, and access control layer?

**KSI-AFR-07-Q021**
When runtime configuration changes (for example, context window size), do you automatically validate infrastructure prerequisites (memory, latency)?

**KSI-AFR-07-Q022**
When model configuration changes (tokenizer), do you detect downstream impacts on API costs and behavior patterns?

**KSI-AFR-07-Q023**
Do you maintain forensic-grade audit logs capturing complete configuration history with immutable records?

**KSI-AFR-07-Q024**
What percentage of configuration changes are currently logged and auditable?

**KSI-AFR-07-Q025**
Can you reconstruct configuration state at any point in time for forensic analysis?

**KSI-AFR-07-Q026**
How do you detect incremental configuration changes that individually appear benign but collectively create security vulnerabilities?

**KSI-AFR-07-Q027**
Do you have supply chain verification processes for third-party configuration sources (public model repositories, template libraries)?

**KSI-AFR-07-Q028**
How do you detect and prevent malicious configurations injected into deployment pipelines or model repositories?

**KSI-AFR-07-Q029**
What processes validate customer-provided training data does not poison model configuration?

**KSI-AFR-07-Q030**
How do you establish trust boundaries for configurations sourced from external vendors or public repositories?

**KSI-AFR-07-Q031**
Are configuration artifacts from third-party sources scanned before integration into your baseline templates?

**KSI-AFR-07-Q032**
How do you verify the provenance of model weights, tokenizers, and other AI artifacts included in your configuration baselines?

**KSI-AFR-07-Q033**
Are these validators integrated with customer CI/CD pipelines for continuous configuration testing?

**KSI-AFR-07-Q034**
Have you conducted threat modeling specifically for configuration-based attacks (prompt injection, supply chain poisoning, privilege escalation)?

**KSI-AFR-07-Q035**
Are you prepared for operational complexity increase during configuration management implementation?

**KSI-AFR-07-Q036**
What is your current implementation status for AI configuration baseline taxonomy (Recommendation 1 - Priority: Critical)?

**KSI-AFR-07-Q037**
When do you plan to implement continuous drift detection across all configuration layers (Recommendation 2)?

**KSI-AFR-07-Q038**
What resources (engineering effort, timeline) do you estimate for full implementation (6-12 months for typical CSP)?

**KSI-AFR-07-Q039**
How will you phase implementation to minimize operational disruption?

**KSI-AFR-07-Q040**
How do you ensure configuration consistency across multiple AI agents operating in coordinated workflows?

**KSI-AFR-07-Q041**
What mechanisms prevent configuration drift between agents that must maintain synchronized security postures?

**KSI-AFR-07-Q042**
How do you detect and prevent multi-agent attacks that exploit configuration inconsistencies between coordinating agents?

**KSI-AFR-07-Q043**
Does your CSP provide secure configuration baselines for AI agent deployments, or must you develop configurations from scratch?

**KSI-AFR-07-Q044**
Are these baselines documented with security decision matrices explaining trade-offs for each configuration parameter?

**KSI-AFR-07-Q045**
Do baseline templates address model layer (parameters, weights), runtime layer (temperature, token limits), and infrastructure layer (resource limits, network access) configurations?

**KSI-AFR-07-Q046**
Can you obtain baselines in multiple formats (documentation, infrastructure-as-code templates, APIs)?

**KSI-AFR-07-Q047**
Does your CSP document security implications for configurable parameters (for example, temperature settings, token limits, context window size)?

**KSI-AFR-07-Q048**
Are prompt template configurations documented as security controls?

**KSI-AFR-07-Q049**
Does CSP guidance explain how API rate limiting and input validation should be configured?

**KSI-AFR-07-Q050**
Does your CSP document configuration parameters specific to your organization's AI use cases?

**KSI-AFR-07-Q051**
Does your CSP provide secure-by-default configurations you can instantiate immediately without additional tuning?

**KSI-AFR-07-Q052**
Can you deploy AI agents with least-privilege default permissions requiring explicit escalation?

**KSI-AFR-07-Q053**
What configuration modifications are permitted, and which require CSP approval?

**KSI-AFR-07-Q054**
How do you request deviations from baseline configurations?

**KSI-AFR-07-Q055**
What is the approval latency for configuration change requests?

**KSI-AFR-07-Q056**
Does your CSP provide documented security rationale for baseline configuration choices to guide your customization decisions?

**KSI-AFR-07-Q057**
Does your CSP communicate security risks when you deviate from baseline configurations?

**KSI-AFR-07-Q058**
Are you informed of configuration combinations that create emergent vulnerabilities?

**KSI-AFR-07-Q059**
Does your CSP validate your custom configurations against security policies?

**KSI-AFR-07-Q060**
Does your CSP identify risks from non-deterministic AI behavior when you customize configurations?

**KSI-AFR-07-Q061**
Are you warned about configuration settings that could result in over-privileged AI agents?

**KSI-AFR-07-Q062**
Does your CSP communicate risks of prompt injection attacks affecting your configured security boundaries?

**KSI-AFR-07-Q063**
How does your CSP validate that your deployed configuration matches approved baselines or approved modifications?

**KSI-AFR-07-Q064**
What testing does your CSP perform on your custom configurations before deployment?

**KSI-AFR-07-Q065**
Can you test configurations in non-production environments before production deployment?

**KSI-AFR-07-Q066**
Can you detect configuration drift at model, runtime, infrastructure, and access control layers?

**KSI-AFR-07-Q067**
What anomalous behaviors trigger configuration validation alerts?

**KSI-AFR-07-Q068**
Does your CSP provide audit logs of all configuration changes with timestamps and approval records?

**KSI-AFR-07-Q069**
Can you reconstruct your configuration state at any historical point for forensic analysis?

**KSI-AFR-07-Q070**
What default permissions do your AI agents receive upon deployment?

**KSI-AFR-07-Q071**
Are default permissions aligned with least-privilege principles, or do agents operate with overly permissive defaults?

**KSI-AFR-07-Q072**
What processes must you follow to escalate AI agent permissions?

**KSI-AFR-07-Q073**
If your CSP offers JIT access, what is the approval latency for legitimate permission escalation requests?

**KSI-AFR-07-Q074**
How are automated approval mechanisms implemented to prevent bottlenecks?

**KSI-AFR-07-Q075**
What audit trail exists for all JIT access requests and approvals?

**KSI-AFR-07-Q076**
Does your CSP detect when AI agents attempt unauthorized privilege escalation?

**KSI-AFR-07-Q077**
How are escalation attempts logged and communicated to your organization?

**KSI-AFR-07-Q078**
Are multi-agent coordinated escalation attempts detectable?

**KSI-AFR-07-Q079**
Does your CSP verify the integrity of configuration templates before you deploy them?

**KSI-AFR-07-Q080**
Are configuration artifacts cryptographically signed?

**KSI-AFR-07-Q081**
How do you verify that configuration sources (public repositories, templates) have not been maliciously modified?

**KSI-AFR-07-Q082**
If you provision configurations from third-party sources (public repositories, vendor templates), how does your CSP help you verify them?

**KSI-AFR-07-Q083**
Does your CSP scan third-party configuration sources for malicious patterns?

**KSI-AFR-07-Q084**
What supply chain verification coverage does your CSP provide?

**KSI-AFR-07-Q085**
What processes validate that your training data does not poison AI model configuration?

**KSI-AFR-07-Q086**
Who is responsible for validating the security posture of models you fine-tune or customize?

**KSI-AFR-07-Q087**
How is the CSP-customer responsibility boundary defined for configuration-level security?

**KSI-AFR-07-Q088**
What compliance audit support does your CSP provide?

**KSI-AFR-07-Q089**
Does your CSP identify which configuration settings address specific NIST SP 800-53 controls (CM-2, CM-3, CM-6, CM-7)?

**KSI-AFR-07-Q090**
Are configuration baselines aligned with your Federal authorization requirements?

**KSI-AFR-07-Q091**
How often are baselines updated to address emerging compliance requirements?

**KSI-AFR-07-Q092**
Can you define which configuration changes require manual approval vs. automated remediation?

**KSI-AFR-07-Q093**
How much effort does your organization spend on configuration tuning vs. accepting baselines?

**KSI-AFR-07-Q094**
Does your CSP provide operational guidance reducing configuration-related incidents?

**KSI-AFR-07-Q095**
How does your CSP support incident response when configuration-based attacks occur?

**KSI-AFR-07-Q096**
Can you quickly roll back to known-good configurations?

**KSI-AFR-07-Q097**
What forensic data does your CSP provide for configuration-based security incidents?

**KSI-AFR-07-Q098**
Are trade-offs between security hardening and operational costs documented?

**KSI-AFR-07-Q099**
What emergency rollback procedures exist for configuration changes that create security incidents or operational failures?

**KSI-AFR-07-Q100**
Can you perform configuration rollback without service interruption?

**KSI-AFR-07-Q101**
How does your CSP support configuration disaster recovery and backup restoration?

**KSI-AFR-07-Q102**
Do configuration baselines exist in documented form with architectural justification?

**KSI-AFR-07-Q103**
Are all baselines subject to formal security review and threat modeling before implementation?

**KSI-AFR-07-Q104**
Does baseline documentation include risk assessments for each configuration parameter?

**KSI-AFR-07-Q105**
Are baseline decisions retained as audit evidence?

**KSI-AFR-07-Q106**
Do baselines address all security-critical configuration parameters (estimated 500-1000 or more for AI systems)?

**KSI-AFR-07-Q107**
Are model layer (parameters, weights), runtime layer (temperature, tokens), and infrastructure layer (resources, access) configurations included?

**KSI-AFR-07-Q108**
Are AI-specific configurations (prompt templates, API rate limits, token rotation) documented in baselines?

**KSI-AFR-07-Q109**
Who approved current configuration baselines, and with what authority?

**KSI-AFR-07-Q110**
Is baseline approval documented in governance records?

**KSI-AFR-07-Q111**
Is a formal baseline review cadence established and followed?

**KSI-AFR-07-Q112**
Are stakeholders (security, engineering, compliance) involved in baseline approval?

**KSI-AFR-07-Q113**
How many deployed systems exactly match approved baseline configurations?

**KSI-AFR-07-Q114**
What percentage of deployed systems have authorized deviations from baselines?

**KSI-AFR-07-Q115**
What percentage have unauthorized configuration deviations?

**KSI-AFR-07-Q116**
Can you provide audit evidence of baseline instantiation for each deployed system?

**KSI-AFR-07-Q117**
What formal change control process approves deviations from baseline configurations?

**KSI-AFR-07-Q118**
Is a configuration change authorization trail maintained for audit?

**KSI-AFR-07-Q119**
Are risk assessments conducted for approved deviations?

**KSI-AFR-07-Q120**
Who has authority to approve deviations at different risk levels?

**KSI-AFR-07-Q121**
How is deployed configuration verified to match baseline or approved modifications?

**KSI-AFR-07-Q122**
What testing validates deployed configurations before production deployment?

**KSI-AFR-07-Q123**
Are security implications of deployed configurations validated?

**KSI-AFR-07-Q124**
What audit evidence documents deployment validation?

**KSI-AFR-07-Q125**
Are all detected configuration drifts documented with timestamps?

**KSI-AFR-07-Q126**
Is the remediation action for each drift documented?

**KSI-AFR-07-Q127**
Can the audit trail account for all configuration state changes?

**KSI-AFR-07-Q128**
Is attribution (who made the change, when, with what authority) documented?

**KSI-AFR-07-Q129**
Are unexplained configuration changes investigated?

**KSI-AFR-07-Q130**
What incidents have resulted from configuration drift?

**KSI-AFR-07-Q131**
Does a formal configuration change control process (CM-3) exist with documented procedures?

**KSI-AFR-07-Q132**
Are all configuration changes logged with complete audit trails?

**KSI-AFR-07-Q133**
Do audit records include: what changed, when, who authorized, who implemented, security rationale?

**KSI-AFR-07-Q134**
What retention period applies to configuration change records?

**KSI-AFR-07-Q135**
What governance body approves configuration changes at different risk levels?

**KSI-AFR-07-Q136**
Is the approval authority documented and appropriate for risk level?

**KSI-AFR-07-Q137**
Are low-risk changes approved through automated procedures, and high-risk changes through manual review?

**KSI-AFR-07-Q138**
Is approval latency within acceptable operational windows?

**KSI-AFR-07-Q139**
Are security impact assessments conducted before configuration changes are approved?

**KSI-AFR-07-Q140**
Are cross-layer impacts (model to runtime to infrastructure effects) considered?

**KSI-AFR-07-Q141**
Are emergent vulnerability risks from configuration interactions considered?

**KSI-AFR-07-Q142**
Is impact assessment documentation retained as audit evidence?

**KSI-AFR-07-Q143**
Does configuration management enforce CM-7 (least functionality) by providing only essential capabilities?

**KSI-AFR-07-Q144**
Are over-privileged default configurations identified and remediated?

**KSI-AFR-07-Q145**
Does configuration change control prevent unnecessary permission escalation?

**KSI-AFR-07-Q146**
What audit evidence documents least-privilege enforcement?

**KSI-AFR-07-Q147**
Are verification procedures documented and consistently applied?

**KSI-AFR-07-Q148**
What signing authority is used for baseline configurations?

**KSI-AFR-07-Q149**
Are verification failures escalated and investigated?

**KSI-AFR-07-Q150**
Are all configuration sources (internal templates, third-party sources, public repositories) subject to supply chain verification?

**KSI-AFR-07-Q151**
What scanning procedures detect malicious configuration patterns?

**KSI-AFR-07-Q152**
Does the organization have a process approving third-party configuration sources?

**KSI-AFR-07-Q153**
Are third-party configurations assessed for security risks before adoption?

**KSI-AFR-07-Q154**
Is provenance tracking maintained for third-party configurations?

**KSI-AFR-07-Q155**
How often are third-party sources re-scanned for updates and vulnerabilities?

**KSI-AFR-07-Q156**
Are configuration artifacts protected throughout the deployment pipeline?

**KSI-AFR-07-Q157**
Does the deployment pipeline implement integrity checks at each stage?

**KSI-AFR-07-Q158**
Are configuration artifacts protected from unauthorized modification during deployment?

**KSI-AFR-07-Q159**
What audit evidence documents pipeline integrity?

**KSI-AFR-07-Q160**
Are model parameters (temperature, token limits, context window) documented as configuration?

**KSI-AFR-07-Q161**
Are changes to model parameters subject to configuration change control?

**KSI-AFR-07-Q162**
Are security implications of parameter changes assessed?

**KSI-AFR-07-Q163**
Is model parameter versioning integrated with system configuration versioning?

**KSI-AFR-07-Q164**
Are prompt templates (system prompts, few-shot examples) documented as security configurations?

**KSI-AFR-07-Q165**
Are changes to prompt templates subject to change control?

**KSI-AFR-07-Q166**
Are security guardrails within prompts protected from unauthorized modification?

**KSI-AFR-07-Q167**
How is indirect prompt injection attack risk assessed and mitigated through configuration?

**KSI-AFR-07-Q168**
Are AI agent default permissions documented and approved as configuration?

**KSI-AFR-07-Q169**
Are JIT access request procedures documented and enforced?

**KSI-AFR-07-Q170**
What audit evidence documents permission escalation decisions?

**KSI-AFR-07-Q171**
Are AI-specific configuration changes (fine-tuning, model retraining, prompt updates) detected at the same rigor as infrastructure changes?

**KSI-AFR-07-Q172**
What indicators signal configuration-level attacks on AI systems?

**KSI-AFR-07-Q173**
Is configuration management mapped to NIST SP 800-53 controls CM-2, CM-3, CM-6, CM-7?

**KSI-AFR-07-Q174**
Are FedRAMP 20x KSI-AFR requirements (KSI-AFR-01, AFR-03, AFR-05, AFR-07, AFR-09) addressed by configuration controls?

**KSI-AFR-07-Q175**
Is compliance mapping documented with evidence cross-references?

**KSI-AFR-07-Q176**
Are compliance gaps identified and remediation planned?

**KSI-AFR-07-Q177**
Does baseline configuration comply with all applicable regulatory requirements?

**KSI-AFR-07-Q178**
Is baseline compliance validated through security assessment?

**KSI-AFR-07-Q179**
Are compliance validation results documented as audit evidence?

**KSI-AFR-07-Q180**
Is baseline compliance maintained through change control?

**KSI-AFR-07-Q181**
Is the current privilege granted to AI agents assessed against actual usage?

**KSI-AFR-07-Q182**
Is privilege creep identified and remediation planned?

**KSI-AFR-07-Q183**
Are over-privileged default configurations eliminated through least-privilege enforcement?

**KSI-AFR-07-Q184**
What audit evidence documents privilege assessment results?

**KSI-AFR-07-Q185**
Have emergent vulnerabilities from configuration interactions been identified?

**KSI-AFR-07-Q186**
Are configuration combinations validated to prevent unsafe interactions?

**KSI-AFR-07-Q187**
Are interaction risks mitigated through governance or technical controls?

**KSI-AFR-07-Q188**
Do audit trails capture all configuration changes with who, what, when, why, and authority information?

**KSI-AFR-07-Q189**
Are audit trails immutable and retained for required periods?

**KSI-AFR-07-Q190**
Can audit trails be searched and analyzed for compliance demonstration?

**KSI-AFR-07-Q191**
What audit trail retention policy is documented?

**KSI-AFR-07-Q192**
Is a complete inventory of deployed configurations maintained?

**KSI-AFR-07-Q193**
Is configuration documentation current and accessible for audits?

**KSI-AFR-07-Q194**
Are baseline deviations documented with approval and risk assessment?

**KSI-AFR-07-Q195**
Is configuration documentation reviewed and updated at defined intervals?

**KSI-AFR-07-Q196**
Can all FedRAMP audit evidence related to configuration management be provided?

**KSI-AFR-07-Q197**
Are compliance dossiers prepared automatically or through manual effort?

**KSI-AFR-07-Q198**
What compliance evidence gaps exist?

**KSI-AFR-07-Q199**
How is configuration-related compliance documentation managed?

**KSI-AFR-07-Q200**
Can configuration state at any point in time be reconstructed for forensic analysis?

**KSI-AFR-07-Q201**
Are configuration-based security incidents distinguished from other incident categories?

**KSI-AFR-07-Q202**
Does incident investigation process document configuration state changes?

**KSI-AFR-07-Q203**
Are post-incident reviews documented with configuration-related findings?

**KSI-AFR-07-Q204**
Is the CSP-customer configuration responsibility boundary clearly defined?

**KSI-AFR-07-Q205**
Are responsibilities documented in contracts and SLAs?

**KSI-AFR-07-Q206**
Is responsibility boundary for AI systems (fine-tuning, training data, permissions) clearly defined?

**KSI-AFR-07-Q207**
Are responsibility gaps identified where neither CSP nor customer owns control?

**KSI-AFR-07-Q208**
Is a formal configuration governance body established with defined membership and authority?

**KSI-AFR-07-Q209**
Does governance body include security, engineering, compliance, and business representatives?

**KSI-AFR-07-Q210**
Are configuration governance decisions documented and retained?

**KSI-AFR-07-Q211**
Is governance meeting cadence defined and followed?

**KSI-AFR-07-Q212**
Are configuration decisions attributed to decision-makers with recorded approval?

**KSI-AFR-07-Q213**
Is accountability for configuration changes enforced through policy?

**KSI-AFR-07-Q214**
Are unauthorized configuration modifications investigated with accountability focus?

**KSI-AFR-07-Q215**
Are consequences for policy violations enforced?

**KSI-AFR-07-Q216**
Are personnel responsible for configuration management trained on policies and procedures?

**KSI-AFR-07-Q217**
Is training documented and currency tracked?

**KSI-AFR-07-Q218**
Is awareness of configuration security risks maintained through communications?

**KSI-AFR-07-Q219**
Are training and awareness materials updated to address emerging configuration risks?

**KSI-AFR-07-Q220**
How do you validate AI configuration behavior in non-deterministic systems where the same configuration produces different outputs?

**KSI-AFR-07-Q221**
What testing procedures validate that configuration changes do not introduce prompt injection vulnerabilities?

**KSI-AFR-07-Q222**
How do you test for emergent vulnerabilities created by configuration interactions across multiple layers?

**KSI-AFR-07-Q223**
What observability tools are available to debug configuration-related issues in production AI systems?

**KSI-AFR-07-Q224**
Can you trace the impact of a specific configuration change on AI agent behavior through production telemetry?

**KSI-AFR-07-Q225**
How do you correlate configuration state with observed AI system behavior for troubleshooting?

**KSI-AFR-07-Q226**
How are LLM API rate limits, token usage quotas, and cost controls configured as security boundaries?

**KSI-AFR-07-Q227**
What configuration controls prevent AI agents from exceeding authorized API usage limits or costs?

---

## Appendix: Question Migration Summary

### Questions Removed (Metric-Heavy or Generic) - 22 total
AFR-07-Q18, AFR-07-Q28, AFR-07-Q31, AFR-07-Q37, AFR-07-Q38, AFR-07-Q42, AFR-07-Q47, AFR-07-Q113, AFR-07-Q119, AFR-07-Q120, AFR-07-Q132, AFR-07-Q150, AFR-07-Q156, AFR-07-Q181, AFR-07-Q186, AFR-07-Q188, AFR-07-Q206, AFR-07-Q222, AFR-07-Q227, AFR-07-Q231, AFR-07-Q239, AFR-07-Q247

**Rationale:** These questions emphasized numeric targets (5 minutes, 95%, 99%, 60-70%) rather than investigative configuration practices, or were overly generic. Kept in guidance documentation rather than core question library.

### Questions Moved to KSI-AFR-03 (Machine-Readable Data Sharing) - 8 total
AFR-07-Q36, AFR-07-Q40, AFR-07-Q83, AFR-07-Q104, AFR-07-Q105, AFR-07-Q221, AFR-07-Q223, AFR-07-Q224

**Rationale:** These questions focus on export interfaces, machine-readable evidence, and data sharing rather than the secure configurations themselves. Better aligned with AFR-03 discovery objectives.

### Questions Moved to KSI-AFR-05 (Significant Change Notifications) - 10 total
AFR-07-Q43, AFR-07-Q44, AFR-07-Q45, AFR-07-Q80, AFR-07-Q110, AFR-07-Q111, AFR-07-Q229, AFR-07-Q230, AFR-07-Q231, AFR-07-Q232

**Rationale:** These questions focus on notification behavior, latency, and alerting rather than whether configurations are secure by default or properly governed. Better aligned with AFR-05 discovery objectives.

### Questions Moved to KSI-AFR-09 (Continuous Validation) - 25 total
AFR-07-Q41, AFR-07-Q79, AFR-07-Q149, AFR-07-Q150, AFR-07-Q151, AFR-07-Q152, AFR-07-Q153, AFR-07-Q154, AFR-07-Q155, AFR-07-Q160, AFR-07-Q161, AFR-07-Q210, AFR-07-Q212, AFR-07-Q225, AFR-07-Q226, AFR-07-Q227, AFR-07-Q228, AFR-07-Q233, AFR-07-Q234, AFR-07-Q235, AFR-07-Q236, AFR-07-Q237, AFR-07-Q238, AFR-07-Q239, AFR-07-Q240

**Rationale:** These questions focus on real-time compliance checking, continuous validation, and control effectiveness testing rather than configuration baseline establishment and governance. Better aligned with AFR-09 discovery objectives.

---

**End of Document**
