# Passwordless Authentication in the AI Era: Discovery Questions

**KSI Focus:** IAM-02 - Enforce passwordless, phishing-resistant authentication across all users and AI agents in response to AI-powered credential attacks, deepfake-assisted phishing, non-human identity proliferation (82:1 ratio, projected 2,000:1 by 2026), and emerging authentication threats requiring cryptographic-first authentication design.

**Context:** This discovery question set consolidates auditor, CIO, and customer perspectives to assess whether organizations implement passwordless authentication (FIDO2/WebAuthn, passkeys, hardware keys) as default for human users and cryptographic authentication for AI agents. Questions validate resistance to AI-powered password cracking (PassGAN 85.6% crack rates), phishing and social engineering attacks when paired with passwordless/FIDO2 defenses, and non-human identity sprawl (23.7M secrets exposed on GitHub 2024). All questions address AI-era authentication threats through the lens of passwordless-by-default implementation.

---

## Section 1: AI-Powered Password Attacks & Obsolescence

**KSI-IAM-02-Q1:** What evidence demonstrates that your organization recognizes passwords as obsolete authentication mechanism in the AI era? Describe: (a) password crack rate measurements (AI-driven tools like PassGAN on your database), (b) historical password breaches in your organization and impact, (c) compliance gap analysis (NIST 800-63-4 recommends passwordless-first), (d) executive commitment to passwordless migration timeline, (e) technical validations supporting the shift.

**KSI-IAM-02-Q2:** What percentage of compromised credentials in security incidents come from AI-powered attacks (credential stuffing with billions of guesses/second, PassGAN-generated password predictions, neural cracking) vs traditional theft methods? Document: (a) incident classification methodology, (b) AI attack prevalence in your breach incidents, (c) impact difference (dwell time, blast radius, remediation cost), (d) trend over past 12 months, (e) correlation with increased GPU-accelerated cracking speeds (20% YoY increase).

**KSI-IAM-02-Q3:** How do you protect accounts that cannot immediately migrate to passwordless (legacy systems, external contractors, IoT devices)? Provide: (a) inventory of password-dependent accounts, (b) password entropy requirements (target: NIST 15+ characters), (c) password strength validation against PassGAN/neural cracking, (d) multi-factor authentication enforcement (phishing-resistant methods only), (e) compensating controls (network segmentation, behavioral monitoring, short account lifetime).

**KSI-IAM-02-Q4:** For AI agents and service accounts that historically used passwords, what is your migration roadmap to cryptographic authentication (SPIFFE/SPIRE tokens, mTLS certificates)? Document: (a) current agent password usage (percentage, count, purpose), (b) blockers to cryptographic migration, (c) OIDC federation pilot results (if attempted), (d) planned implementation timeline (by quarter), (e) success metrics (% agents migrated, password elimination rate).

**KSI-IAM-02-Q5:** How frequently do you conduct security assessments against AI-powered password cracking and dictionary attacks? Describe: (a) testing methodology (honeypot accounts, AI attack simulation, PassGAN implementation testing), (b) frequency (quarterly, annually), (c) results (percentage of accounts crackable in <10 seconds, days, weeks), (d) comparison to industry benchmarks (85.6% crack rate from research), (e) remediation actions triggered by findings.

---

## Section 2: AI Social Engineering & Deepfake Threats (Passwordless Framing)

**KSI-IAM-02-Q6:** What evidence validates your organization's defense against LLM-generated phishing attacks through passwordless/FIDO2 mechanisms? Document: (a) phishing simulation results showing that FIDO2-enrolled users resist AI-generated phishing, (b) user training effectiveness on passwordless methods vs traditional passwords, (c) authentication failures traced to phishing that would have been prevented by FIDO2, (d) mechanism showing FIDO2 origin binding prevents credential harvesting, (e) incident data showing passwordless users avoided compromise.

**KSI-IAM-02-Q7:** What percentage of authentication-related security incidents in the past 12 months involved social engineering attacks (phishing, credential requests, pretexting)? For those incidents, provide: (a) incident count and breakdown by attack type, (b) success rate (credentials stolen, accounts compromised), (c) whether FIDO2/phishing-resistant MFA had been enforced (would it have prevented the incident?), (d) average dwell time before detection, (e) total impact (systems compromised, data accessed).

**KSI-IAM-02-Q8:** What is your organization's response to the emerging threat of AI-powered adversary-in-the-middle (AitM) attacks targeting authentication? Describe: (a) AitM attack scenarios tested (reverse proxy phishing sites intercepting credential entry), (b) FIDO2 origin-binding effectiveness (verification that origin-bound challenges defeat AitM), (c) user fallback behaviors when encountering AitM (authentication method downgrade from FIDO2 to password), (d) incident history of AitM attacks, (e) proactive defense measures (FIDO2 enrollment, hardware key distribution, origin binding verification).

---

## Section 3: Biometric & Behavioral Authentication (as Passwordless Factors)

**KSI-IAM-02-Q9:** What biometric authentication methods does your organization deploy as passwordless factors (fingerprint, facial recognition via platform authenticators, behavioral)? Document: (a) biometric types implemented and adoption rate, (b) liveness detection mechanisms to prevent replay and deepfake attacks, (c) spoofing success rate under adversarial testing (deepfake videos, silicone fingerprints), (d) biometric template security (encryption, HSM storage, revocation procedures), (e) integration with FIDO2 or passkeys as the primary passwordless mechanism.

**KSI-IAM-02-Q10:** How do you implement continuous authentication using behavioral biometrics (keystroke dynamics, mouse movement, typing patterns) to supplement passwordless authentication? Describe: (a) behavioral baseline establishment per user, (b) anomaly detection approach (statistical, ML-based), (c) anomaly types monitored (unusual typing speed, mouse movement patterns, geographic anomalies), (d) real-time response (step-up authentication, session termination), (e) integration with passwordless mechanisms (continuous auth over FIDO2-authenticated sessions).

**KSI-IAM-02-Q11:** How do you prevent biometric template leakage and misuse when using biometrics as a passwordless factor? Describe: (a) biometric storage mechanism (encrypted, HSM-backed, where stored?), (b) access controls to templates (who can retrieve, audit logging), (c) biometric revocation procedures (if templates exposed, how is user re-enrolled?), (d) privacy controls (biometric data not shared with third parties, compliance with GDPR/CCPA), (e) transparency with users on biometric data usage and retention.

---

## Section 4: Non-Human Identity & AI Agent Governance

**KSI-IAM-02-Q12:** What evidence demonstrates your organization's strategy for managing non-human identity (NHI) proliferation driven by AI agents using cryptographic authentication? Describe: (a) current NHI count (service accounts, API keys, agent credentials) and comparison to humans (target: <45:1 ratio), (b) projected AI agent adoption (89% of enterprises deploying agents), (c) credential count per agent (research suggests 15-20 credentials per agent), (d) NHI inventory completeness (manual vs automated discovery, shadow credentials discovered), (e) governance framework for NHI lifecycle (provisioning, rotation, deprovisioning).

**KSI-IAM-02-Q13:** How do you prevent credential sprawl for AI agents operating across multiple cloud providers, APIs, and databases? Document: (a) credential inventory by system and agent (matrix showing which agents have which credentials), (b) shared vs unique credentials per agent (are multiple agents sharing credentials? no.), (c) automated credential provisioning (provisioning time from agent creation to operational), (d) scope attenuation (agent credentials limited to required access, not over-privileged), (e) automated deprovisioning (how quickly are credentials revoked when agent terminates?).

**KSI-IAM-02-Q14:** What authentication methods are used for AI agent identity and how do they differ from human user authentication? Provide: (a) agent identity model (unique cryptographic identity per agent instance vs shared credentials), (b) authentication mechanism (mutual TLS certificates, SPIFFE/SPIRE tokens, API keys, OIDC delegation), (c) credential lifetime (minutes, hours, days? comparison to human session duration), (d) automated rotation and revocation (how often, how quickly), (e) evidence of cryptographic binding (agent cannot be impersonated, credentials cannot be replayed).

**KSI-IAM-02-Q15:** How do you detect and prevent AI agents from being weaponized to conduct credential attacks against other systems? Describe: (a) behavioral monitoring of agent authentication activity (unusual authentication patterns, brute force attempts, credential usage spikes), (b) detection mechanisms (rate limiting, geographic anomalies, tool usage anomalies), (c) automated response (credential revocation, agent quarantine, alert escalation), (d) incident history (has a rogue or compromised agent been detected?), (e) testing of agent attack simulation (can a compromised agent escalate or lateral move?).

**KSI-IAM-02-Q16:** How do you implement least-privilege access controls for AI agents using cryptographic authentication while accommodating task-scoped permission changes? Explain: (a) permission model for agents (static roles vs dynamic, task-scoped permissions), (b) mechanism for agents to request task-specific credentials (JIT access request flow), (c) approval and audit of permission grants, (d) automatic permission revocation upon task completion or expiration, (e) examples of agents operating under zero standing privilege constraints.

---

## Section 5: Passwordless Technologies & Standards

**KSI-IAM-02-Q17:** What is your organization's FIDO2/WebAuthn deployment status and roadmap? Document: (a) FIDO2 enrollment rates (by user type: admin, standard user, guest), (b) supported authenticator types (platform authenticators—Windows Hello/Touch ID; roaming—YubiKey/Titan; biometric), (c) enrollment timeline (when will 50%, 80%, 95% of users be FIDO2-enrolled?), (d) fallback authentication (password+TOTP for legacy systems), (e) user adoption barriers and mitigation (device compatibility, recovery procedures, support costs).

**KSI-IAM-02-Q18:** How do you enforce origin binding in FIDO2/WebAuthn to prevent phishing and man-in-the-middle attacks? Describe: (a) origin verification mechanism (Relying Party ID, origin header validation), (b) configuration evidence (RP ID allowlist, origin matching rules), (c) testing results showing origin binding prevents cross-origin authentication, (d) user experience on failed origin verification (error message clarity), (e) evidence that origin binding has prevented phishing attacks in your environment.

**KSI-IAM-02-Q19:** What is your hardware security key strategy for privileged and administrative access? Provide: (a) hardware key distribution strategy (procurement, cost per key, user enrollment), (b) key types deployed (FIDO2 U2F, smart cards, biometric hardware keys), (c) AAL3 (Authentication Assurance Level 3) enforcement for admin accounts (hardware keys mandatory, no platform authenticators), (d) recovery procedures if user loses hardware key, (e) inventory of hardware keys issued and in use.

**KSI-IAM-02-Q20:** How do you support passwordless authentication across all application types and deployment models? Document: (a) applications supporting FIDO2 (percentage of total applications), (b) gaps: legacy applications, on-premises systems, third-party SaaS requiring passwords, (c) federation approach (OIDC/SAML with passwordless assertion), (d) user experience when authenticating to non-FIDO2 apps (seamless SSO vs re-authenticate with password), (e) roadmap for closing passwordless gaps.

---

## Section 6: Cryptographic Defenses

**KSI-IAM-02-Q21:** What cryptographic binding mechanisms protect authentication credentials against offline attacks and credential theft? Document: (a) cryptographic binding approach (channel binding, cryptographic binding of identity to device), (b) implementation in FIDO2, passkeys, and other methods, (c) protection against credential cloning or export, (d) key storage (HSM, Secure Enclave, TPM), (e) testing showing credentials cannot be extracted even if device compromised.

**KSI-IAM-02-Q22:** How do you protect authentication infrastructure against cryptographic attacks (replay attacks, downgrade attacks, cryptanalysis)? Provide: (a) cryptographic algorithm choices (RSA 2048+, ECDSA, or EdDSA?), (b) TLS version (1.3+), (c) challenge-response uniqueness (no replay), (d) downgrade attack prevention (cannot force fallback from FIDO2 to weak auth), (e) periodic cryptographic assessment and updates.

**KSI-IAM-02-Q23:** What is your strategy for managing cryptographic credentials and keys used in passwordless authentication? Describe: (a) key generation (random, properly seeded), (b) key rotation frequency and procedures, (c) key revocation (device compromise, lost device, job termination), (d) key escrow or backup strategy (account recovery if device lost), (e) compliance with NIST or industry cryptographic standards.

---

## Section 7: Identity Federation & Access Control

**KSI-IAM-02-Q24:** How do you implement identity federation (OIDC/SAML) with passwordless authentication? Document: (a) federation protocol (OIDC, SAML, or proprietary), (b) passwordless assertion in federation flows (user authenticates to IdP with FIDO2, assertion generated without password), (c) trust relationship configuration (which external IdPs are trusted), (d) single sign-on (SSO) experience across applications, (e) account linking for users with multiple federated identities.

**KSI-IAM-02-Q25:** How do you ensure passwordless authentication works across multi-cloud and hybrid environments (AWS, Azure, GCP, on-premises)? Provide: (a) cloud-agnostic authentication standards used (OIDC, FIDO2), (b) consistent passwordless policies across clouds, (c) federated identity platform (AWS Cognito, Azure AD, Okta, etc.), (d) user experience (seamless cross-cloud access vs re-authentication), (e) compliance with cloud-specific authentication requirements (AWS Secrets Manager, Azure Key Vault).

**KSI-IAM-02-Q26:** How do you implement passwordless authentication for B2B and external partner access? Explain: (a) external partner authentication mechanism (FIDO2, federated identity, short-lived tokens), (b) trust boundary management (contractor vs trusted partner), (c) temporary access provisioning (time-limited credentials, task-scoped access), (d) partner credential revocation procedures (immediate upon contract termination), (e) auditing of partner access (comprehensive logs, anomaly detection).

**KSI-IAM-02-Q27:** What is your strategy for passwordless authentication in constrained environments (IoT, embedded systems, legacy hardware)? Document: (a) constrained device types supported (smartcards, hardware tokens, NFC devices), (b) authentication mechanisms for devices without biometric capability, (c) fallback to strong passwords with MFA for truly constrained systems, (d) network segmentation or enhanced monitoring as compensating controls, (e) roadmap for upgrading constrained systems to passwordless.

---

## Section 8: AI Anomaly Detection & Behavioral Monitoring (Passwordless Context)

**KSI-IAM-02-Q28:** How do you implement behavioral anomaly detection for authentication across human users and AI agents? Describe: (a) behavioral baseline establishment (learning period, feature selection), (b) anomaly types monitored (unusual authentication time, location, frequency, device changes), (c) detection approach (statistical, ML-based, rule-based), (d) real-time detection and response (step-up authentication, session termination), (e) integration with passwordless mechanisms (anomaly triggers re-FIDO2 challenge).

**KSI-IAM-02-Q29:** What authentication-related signals do you monitor to detect compromised credentials or account takeover in passwordless systems? Document: (a) signals monitored (failed FIDO2 challenges, unusual authenticator usage, geographic impossibilities, device anomalies), (b) detection latency (how quickly after compromise detected?), (c) alerting thresholds and escalation (what triggers investigation?), (d) correlation with other security signals (network anomalies, resource access patterns), (e) effectiveness (what percentage of compromise attempts detected before impact?).

**KSI-IAM-02-Q30:** How do you perform continuous re-authentication based on behavioral anomalies, supplementing passwordless mechanisms? Explain: (a) continuous authentication triggers (deviation from baseline, time-based re-auth, risk-based elevation), (b) re-authentication frequency and methods (challenge-response, re-enter passkey PIN, biometric re-scan), (c) user experience impact (balance between security and usability), (d) comparison to single passwordless authentication event (does continuous auth improve security?), (e) testing of continuous auth effectiveness against compromise scenarios.

---

## Removed Questions (Moved to Other KSIs)

The following questions were identified as better suited for other KSIs based on discovery guidance:

- **Q07 (Deepfake Detection)**: Moved to biometric-governance or MFA-specific KSI (IAM-01)
- **Q09 (Training & Awareness)**: Moved to training/awareness KSI (CED-01 or CED-02)
- **Q13 (Multi-Modal Biometrics)**: Moved to biometric-governance KSI
- **Q15 (Biometric Deepfake Resilience)**: Moved to biometric-governance KSI
- **Q25 (Post-Quantum Cryptography)**: Moved to cryptography/KMS KSI (SVC-06)
- **Q26 (Zero-Knowledge Proofs)**: Moved to advanced cryptography/privacy KSI
- **Q33 (Fine-Grained Access Control)**: Moved to access control/least-privilege KSI (IAM-05)
- **Q39 (ML Model Architecture)**: Moved to AI security analytics KSI

---

**Version:** 2.0
**Generated:** 2026-01-13
**Status:** Filtered and Renumbered per Issue #26 Review
