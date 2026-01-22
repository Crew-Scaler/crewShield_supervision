# Phishing-Resistant MFA in the AI Era: Discovery Questions

**KSI Focus:** IAM-01 - Enforce phishing-resistant, multi-factor authentication across all user and non-human identity authentication, with specific emphasis on AI-powered attack resilience, AI agent authentication, behavioral anomaly detection, deepfake/biometric spoofing defense, and continuous authentication. Move beyond static MFA checkpoints to continuous, AI-aware, behavioral-driven verification.

**Context:** This discovery question set consolidates auditor, CIO, and customer perspectives to assess organizational readiness for AI-era multi-factor authentication through cryptographic proof (FIDO2/WebAuthn), behavioral verification (continuous auth + anomaly detection), non-human identity governance (zero-trust service accounts), attack detection and response (deepfake forensics, phishing detection at scale), and biometric robustness (liveness detection, anti-spoofing). Questions address quantified threats: AI-generated phishing achieves 11% conversion (6x traditional), voice cloning requires only 30-second samples, deepfake detection accuracy drops 45-50% on real-world data, AitM attacks compromise 79% of MFA bypass incidents even with MFA deployed.

---

## Section 1: FIDO2/WebAuthn & Phishing-Resistant Foundation

**KSI-IAM-01-Q01:** What percentage of your user authentication currently uses phishing-resistant MFA (FIDO2/WebAuthn/hardware keys) vs legacy methods (SMS/TOTP/push)? Provide: (a) enrollment rates by method and user population (admin, standard, privileged), (b) authenticator types (platform passkeys, roaming security keys), (c) default authentication path for each system, (d) enforcement policies by service/sensitivity level, (e) barriers to adoption and remediation plan.

**KSI-IAM-01-Q02:** How do you validate FIDO2 origin binding and prevent adversary-in-the-middle (AitM) downgrade attacks? Describe: (a) origin validation implementation and configuration, (b) AitM attack testing (phishing proxy attempts, downgrade to SMS/TOTP), (c) user experience when authenticating to phishing proxy (blocked? alerted?), (d) incident response for origin binding compromise, (e) penetration test or red team results showing attack prevention effectiveness.

**KSI-IAM-01-Q03:** How do you achieve NIST 800-63-4 AAL2/AAL3 (Authenticator Assurance Level) compliance? Document: (a) AAL2/AAL3 requirements for your organization, (b) authenticators used and their AAL ratings, (c) cryptographic strength verification, (d) authentication binding (cryptographically linking authenticator to credential), (e) audit evidence for compliance validation.

**KSI-IAM-01-Q04:** For high-value accounts (admin, finance, engineering), what is your mandatory authentication method? Explain: (a) hardware security keys vs platform passkeys vs biometric, (b) enforcement mechanism (technical requirement vs policy), (c) exception process and approval criteria, (d) adoption rate among high-value accounts, (e) security incident history: have high-value accounts using legacy MFA been compromised?

---

## Section 2: AI Agent Identity & Non-Human Authentication

**KSI-IAM-01-Q05:** How do you authenticate AI agents and service accounts in your environment? Describe: (a) authentication protocol used (A2A, OIDC-A, SPIFFE, mTLS, token-based), (b) credential type (long-lived secrets, short-lived tokens), (c) credential lifecycle management (issuance, rotation, revocation), (d) maximum credential lifetime (target: <1 hour for production agents), (e) audit trail of agent authentication attempts and failures.

**KSI-IAM-01-Q06:** What is your service account inventory and governance? Provide: (a) total number of service accounts in production, (b) distribution across systems/applications, (c) accounts with human access (shared credentials, anti-pattern), (d) orphaned accounts (no owner, dormant >90 days), (e) credential rotation status (target: 100% using short-lived tokens, <5% using static secrets).

**KSI-IAM-01-Q07:** Do you implement zero-trust identity for AI agents with task-based access control (TBAC)? Document: (a) TBAC implementation (agents granted permissions for specific tasks, not roles), (b) examples of task-based policies (agent X can call API Y only between 09:00-17:00 UTC), (c) permission scoping (time-limited, resource-limited, action-limited), (d) least-privilege enforcement (agents denied all by default, explicit allow-list), (e) policy enforcement latency and audit evidence.

**KSI-IAM-01-Q08:** How do you prevent lateral movement if a single AI agent credential is compromised? Explain: (a) isolation mechanisms between agents, (b) permission blast radius if one agent is compromised (how many systems/resources affected?), (c) automated containment procedures (revoke credentials, kill sessions, block API calls), (d) MTTR for containing compromised agent, (e) examples from past 12 months: agents compromised and response effectiveness.

---

## Section 3: Behavioral Anomaly Detection & Continuous Authentication

**KSI-IAM-01-Q09:** What behavioral anomaly detection system monitors for account compromise in real-time? Describe: (a) modalities monitored (keystroke dynamics, mouse patterns, device fingerprinting, geolocation, timing patterns), (b) detection approach (statistical baseline vs ML-based), (c) accuracy metrics (true positive rate, false positive rate), (d) detection latency (target: <100ms for real-time detection), (e) example detections: account takeover/compromise detected within minutes of occurrence.

**KSI-IAM-01-Q10:** How do you establish and maintain behavioral baselines for both human users and AI agents? Document: (a) baseline establishment process (learning period, feature extraction), (b) how AI agent baselines differ from human baselines, (c) baseline drift handling (model retraining frequency), (d) false positive rates at different sensitivity levels, (e) procedures for resetting baselines (credential compromise, behavior change, new role).

**KSI-IAM-01-Q11:** What concept drift mitigation strategies prevent your behavioral detection models from degrading over time? Explain: (a) model retraining frequency (weekly, monthly, quarterly), (b) incremental learning vs full retraining, (c) techniques for handling data drift (distribution shift in user behavior), (d) adversarial robustness testing (can attackers evade detection by slowly drifting behavior?), (e) measured model performance degradation over 12 months (target: <5% annual accuracy loss).

**KSI-IAM-01-Q12:** How do you detect session hijacking and lateral movement post-authentication? Describe: (a) session behavior monitoring (is this the legitimate user or attacker?), (b) detection approach (token reuse, geographic impossibility, anomalous API calls), (c) detection timeliness (MTTD), (d) automated response (session termination, re-authentication, escalation), (e) evidence: session hijacking attempts detected and blocked.

---

## Section 4: AI-Powered Attack Resilience - Phishing

**KSI-IAM-01-Q13:** What evidence do you have of AI-powered phishing attacks against your organization? Document: (a) phishing attempts detected in past 12 months, (b) AI-generated emails identified (LLM-based content analysis), (c) conversion rates by attack type (traditional phishing vs AI-generated), (d) user population most vulnerable (target: <1% conversion rate with security training), (e) examples of AI-enhanced phishing techniques used against your organization.

**KSI-IAM-01-Q14:** How do you detect and prevent AI-generated phishing emails? Describe: (a) detection technology (header analysis, content fingerprinting, ML-based detection), (b) detection accuracy (% of AI phishing caught), (c) false positive rate on legitimate emails, (d) detection latency vs attack delivery speed, (e) security awareness training on AI-generated phishing indicators and techniques.

**KSI-IAM-01-Q15:** What is your email authentication and anti-spoofing posture (SPF, DKIM, DMARC)? Provide: (a) SPF, DKIM, DMARC deployment and enforcement, (b) email domain reputation monitoring, (c) vendor email integration testing (external email masquerading as internal), (d) phishing mailbox automation (detection and removal timeline), (e) user reporting mechanism and follow-up procedures for phishing.

---

## Section 5: AI-Powered Attack Resilience - Voice & Biometric Spoofing

**KSI-IAM-01-Q16:** What defenses do you have against AI voice cloning and vishing (voice phishing) attacks? Document: (a) voice-based authentication methods used (if any), (b) awareness of 30-second audio sample threat (sufficient for high-quality voice clones), (c) speaker verification robustness testing against synthetic voices, (d) detection of audio deepfakes, (e) response procedures if voice-based MFA is compromised.

**KSI-IAM-01-Q17:** What liveness detection and anti-spoofing mechanisms protect biometric authentication? Describe: (a) liveness detection approach (motion-based, texture-based, multimodal), (b) protection against common spoofing attacks (photos, videos, masks, 3D replicas), (c) real-world accuracy (target: >95% on live biometrics, >99% on spoofing attempts), (d) gap between lab accuracy and real-world performance, (e) testing against deepfake video attacks.

**KSI-IAM-01-Q18:** How do you validate deepfake detection for facial biometric authentication? Provide: (a) deepfake detection methodology (forensic analysis, frequency domain, neural networks), (b) detection accuracy on 2024-2025 deepfakes (lab vs real-world), (c) detection failure modes (which types of deepfakes bypass detection?), (d) testing methodology against state-of-the-art deepfake generators, (e) recovery procedure if deepfake biometric authentication succeeds.

**KSI-IAM-01-Q19:** What multimodal biometric authentication do you deploy (e.g., face + voice + gesture)? Explain: (a) modalities combined, (b) how multimodal fusion improves spoofing resistance, (c) resilience against cross-modal attacks (deepfake face with cloned voice), (d) UX-security trade-off (additional authentication steps), (e) deployment scope (high-security accounts only? enterprise-wide?).

---

## Section 6: Attack Detection & Response Capabilities

**KSI-IAM-01-Q20:** How do you detect MFA bypass attempts and attacks on authentication infrastructure? Describe: (a) attack signatures/indicators monitored (brute force, credential stuffing, AitM, downgrade), (b) detection approach (threshold-based, ML-based, threat intelligence), (c) detection latency, (d) automated response (account lockout, re-authentication challenge, escalation), (e) MTTR for containing authentication attacks.

**KSI-IAM-01-Q21:** What incident response playbooks exist for authentication-related breaches? Provide: (a) phishing incident response (detected compromise, user education, credential revocation), (b) credential theft response (password reset, session termination, MFA re-enrollment), (c) biometric spoofing response (disable biometric auth, re-enroll, investigation), (d) root cause analysis process, (e) examples from past 12 months and remediation timeline.

---

## Section 7: Non-Human Identity & Service Account Governance

**KSI-IAM-01-Q22:** Do you enforce MFA-equivalent controls on service account authentication? Document: (a) controls applied to service accounts (short-lived tokens, behavioral monitoring, IP restrictions), (b) whether traditional MFA is feasible for service accounts (multi-factor doesn't apply to machines), (c) equivalent security level vs human MFA (target: token lifetime <1 hour vs human MFA re-authentication), (d) compliance requirement exemptions (are service accounts exempt from MFA?), (e) risk assessment: service account compromise vs human account compromise.

**KSI-IAM-01-Q23:** How do you prevent service account credential leakage and misuse? Explain: (a) credential storage (vault, secrets manager, HSM), (b) access controls on credentials (who can view, rotate, revoke?), (c) audit logging of credential usage (which systems/APIs accessed), (d) detection of anomalous credential usage (unusual IP, unusual API calls), (e) incidents: leaked service account credentials and impact.

**KSI-IAM-01-Q24:** What automation exists for service account lifecycle management (provisioning, rotation, decommissioning)? Describe: (a) automated provisioning (agents created → credentials auto-generated and injected), (b) automated credential rotation (frequency and mechanism), (c) automated decommissioning (agent removed → credentials revoked), (d) manual vs automated percentage (target: >90% automated), (e) audit trail and compliance reporting for lifecycle events.

---

## Section 8: Federated Identity & Continuous Verification

**KSI-IAM-01-Q25:** How do you prevent credential federation attacks (SAML/OIDC federation compromise)? Describe: (a) federation protocol implementation (SAML, OIDC), (b) token validation and signature verification, (c) issuer validation (is token from trusted IDP?), (d) testing against federation attacks (token forgery, issuer impersonation), (e) compromise response: if federation is compromised, how do you invalidate federated sessions?

---

## Section 9: Emerging Threats & Adaptive Controls - AI-Specific Auth Threats

**KSI-IAM-01-Q26:** What adaptive/risk-based authentication do you deploy? Describe: (a) risk scoring factors (location, device, time, behavior, threat intelligence), (b) adaptive MFA triggers (when is additional authentication required?), (c) risk threshold calibration (minimize false positives while catching attacks), (d) user experience impact (friction vs security balance), (e) measured effectiveness: attacks bypassed due to miscalibration vs legitimate users blocked.

**KSI-IAM-01-Q27:** How do you address authentication attacks specific to AI agents and LLMs? Document: (a) prompt injection attacks on authentication systems, (b) model-based authentication (is it vulnerable to adversarial examples?), (c) agent authentication that cannot be delegated/compromised (cryptographic guarantees), (d) LLM-assisted phishing against your organization, (e) detection and mitigation of AI-specific authentication threats.

---

## Section 10: Compliance & Regulatory Alignment

**KSI-IAM-01-Q28:** What regulatory/compliance requirements drive your MFA strategy (NIST, FedRAMP, SOC 2, HIPAA)? Provide: (a) applicable compliance frameworks, (b) specific MFA requirements per framework, (c) evidence of compliance (audit reports, attestations), (d) compliance audit findings related to authentication, (e) timeline for addressing any non-conformance.

**KSI-IAM-01-Q29:** How do you document and demonstrate MFA controls for compliance auditors? Describe: (a) policy documentation showing MFA enforcement, (b) technical evidence (logs, configuration, access controls), (c) testing evidence (penetration tests, security assessments), (d) compliance reporting frequency and automation level, (e) audit findings and remediation timeline.

---

## Section 9: Monitoring & Observability

**KSI-IAM-01-Q30:** What observability gaps exist in your authentication and identity infrastructure? List: (a) authentication events not logged or inadequately logged, (b) blind spots in federated identity monitoring, (c) latency of identity event processing (from occurrence to detection), (d) identity data retention and archival, (e) compliance requirements driving retention (audit trails kept >7 years).

**KSI-IAM-01-Q31:** How do you detect identity-based lateral movement and privilege escalation? Describe: (a) detection of abnormal permission requests (sudden privileged access), (b) detection of token reuse across systems, (c) detection of role/group membership changes, (d) correlation across systems (user auth in system A, unusual access in system B), (e) examples: lateral movement detected and stopped before compromise spread.

---

## Section 11: Third-Party & Supply Chain Identity

**KSI-IAM-01-Q32:** How do you authenticate and authorize third-party identities (contractors, vendors, API consumers)? Document: (a) third-party identity vetting (background check, security review), (b) authentication mechanism (separate IDP? federated?), (c) authorization scoping (limited to necessary resources/APIs), (d) access monitoring and anomaly detection for third-party activity, (e) offboarding procedures and credential revocation.

**KSI-IAM-01-Q33:** What controls prevent supply chain compromise via identity systems? Explain: (a) vendor security requirements (must support MFA, short-lived creds), (b) monitoring of third-party API usage (quota, rate limits, anomalies), (c) incident response if third-party is compromised (revoke API keys, audit logs), (d) SLA enforcement with vendors on identity security, (e) examples from past 12 months: supply chain identity incidents and response.

---

## Section 12: Training & Awareness

**KSI-IAM-01-Q34:** What security awareness training addresses AI-era authentication threats? Describe: (a) phishing training (AI-generated emails, social engineering techniques), (b) biometric spoofing awareness (deepfakes, voice cloning), (c) MFA usage training (FIDO2, passwordless authentication), (d) password hygiene (for systems not yet supporting passwordless), (e) training frequency and measured effectiveness (phishing click rate, incident reduction).

---

**Version:** 1.0
**Generated:** 2026-01-08
