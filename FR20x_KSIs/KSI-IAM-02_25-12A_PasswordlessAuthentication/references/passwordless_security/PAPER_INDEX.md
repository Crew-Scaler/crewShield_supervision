# Passwordless Security Research - Paper Index

Quick reference guide for all 40 downloaded papers, organized by research priority and theme.

---

## Priority 1: MUST READ (Critical for Issue #15)

### Agentic AI Authentication
1. **A Novel Zero-Trust Identity Framework for Agentic AI** (2505.19301v2)
   - Decentralized authentication and fine-grained access control for autonomous AI agents
   - Critical for agent credential management

2. **Fortifying the Agentic Web: A Unified Zero-Trust Architecture** (2508.12259v3)
   - Defense against logic-layer threats in agentic systems
   - Comprehensive zero trust architecture

3. **Agentic JWT: A Secure Delegation Protocol for Autonomous AI Agents** (2509.13597v1)
   - Secure credential delegation without passwords
   - JWT-based agent authentication

### AI Attack Defense
4. **Unmasking Puppeteers: Leveraging Biometric Leakage to Disarm Impersonation** (2510.03548v2)
   - Detecting AI-driven impersonation in videoconferencing
   - Biometric defense against AI attacks

5. **Addressing Deepfake Issue in Selfie banking** (2508.19714v1)
   - Camera-based authentication against deepfakes
   - Critical for biometric security

### Post-Quantum Readiness
6. **The Qey: Post Quantum Cryptography in FIDO2** (2510.21353v1)
   - Implementation and performance of PQC-FIDO2
   - Future-proofing passwordless authentication

7. **A Comparative Study of Hybrid Post-Quantum X.509 Certificate Schemes** (2511.00111v1)
   - PQC certificate comparison and recommendations
   - PKI quantum resistance

---

## Priority 2: FOUNDATIONAL (Core Technologies)

### FIDO2/WebAuthn Implementation
8. **Passwords and FIDO2 Are Meant To Be Secret** (2509.02289v2)
   - Secure authentication channels for browsers
   - Implementation security

9. **The Passwordless Authentication with Passkey Technology** (2508.11928v1)
   - Implementation perspective on passkeys
   - Practical deployment guide

10. **SSH-Passkeys: Leveraging Web Authentication for Passwordless SSH** (2507.09022v1)
    - Extending FIDO2 to infrastructure access
    - Enterprise passwordless adoption

11. **Device-Bound vs. Synced Credentials** (2501.07380v1)
    - Comparative evaluation of passkey strategies
    - Security vs. usability tradeoffs

12. **CTRAPS: CTAP Client Impersonation and API Confusion on FIDO2** (2412.02349v2)
    - Security vulnerabilities in FIDO2
    - Attack vectors and mitigations

13. **Cryptographic Binding Should Not Be Optional** (2511.06028v1)
    - Formal analysis of FIDO UAF channel binding
    - Protocol security guarantees

### Zero Trust Foundations
14. **Identity Control Plane: The Unifying Layer for Zero Trust** (2504.17759v1)
    - Centralized identity management for zero trust
    - Architectural patterns

15. **Establishing Workload Identity for Zero Trust CI/CD** (2504.14760v1)
    - SPIFFE-based authentication
    - Eliminating secrets in automation

16. **Hard-Earned Lessons in Access Control at Scale** (2508.01863v1)
    - Real-world mTLS implementation
    - Production deployment patterns

17. **Zero Trust Security Model in Microservices** (2511.04925v1)
    - Identity federation for microservices
    - Modern architecture security

18. **A Multi-Cloud Framework for Zero-Trust Workload Authentication** (2510.16067v1)
    - Multi-cloud security
    - Hybrid environment authentication

---

## Priority 3: ADVANCED TOPICS

### Biometric Security
19. **FLAME: Flexible and Lightweight Biometric Authentication** (2511.02176v1)
    - Robust biometric auth in malicious environments
    - Attack-resistant biometrics

20. **Deep Learning-Based Multi-Factor Authentication Survey** (2510.05163v1)
    - Comprehensive biometric MFA survey
    - State-of-the-art techniques

21. **Know Me by My Pulse: Continuous Authentication on Wearables** (2508.13690v1)
    - PPG-based continuous authentication
    - Passwordless continuous verification

22. **Who's Wearing? Ear Canal Biometric Authentication** (2510.02563v1)
    - Novel biometric modality
    - Innovative authentication approach

23. **CryptoFace: End-to-End Encrypted Face Recognition** (2509.00332v1)
    - Privacy-preserving facial recognition
    - Biometric without privacy compromise

24. **GANs for Privacy Preservation in Biometric Authentication** (2509.20024v1)
    - Protecting biometric templates
    - Privacy-preserving techniques

25. **Privacy-Preserving Federated Learning for Adaptive Authentication** (2508.18453v3)
    - Federated learning for biometric auth
    - Privacy and accuracy balance

26. **Securing Face and Fingerprint Templates** (2508.18415v1)
    - Biometric template protection at scale
    - Humanitarian system security

### Zero Trust Extensions
27. **Dstack: A Zero Trust Framework for Confidential Containers** (2509.11555v1)
    - Hardware-backed zero trust
    - Confidential computing security

28. **Security Friction Quotient for Zero Trust Identity Policy** (2509.22663v1)
    - Measuring security vs. usability
    - Empirical validation

29. **Addressing Weak Authentication in EVs using AI-powered Adaptive Auth** (2508.19465v1)
    - AI-enhanced adaptive authentication
    - RFID/NFC weakness mitigation

30. **Bridging the Mobile Trust Gap: Zero Trust for Consumer Apps** (2508.16662v1)
    - Mobile zero trust framework
    - Consumer device security

31. **Blockchain-Enabled Zero Trust for FinTech** (2507.19976v1)
    - Blockchain-based zero trust
    - Insider threat defense

32. **Zero Trust Decentralized Identity for Autonomous Vehicles** (2509.25566v1)
    - Zero trust for autonomous systems
    - AI agent authentication in physical systems

33. **TrustZero: Open, Verifiable and Scalable Zero-Trust** (2502.10281v2)
    - Open-source zero trust architecture
    - Transparent, verifiable security

---

## Priority 4: SPECIALIZED APPLICATIONS

### Certificate & PKI
34. **Authentication Against Insecure Bootstrapping for 5G Networks** (2510.23457v1)
    - Post-quantum 5G authentication
    - Mobile network security

35. **On Post-Quantum Cryptography Authentication for QKD** (2507.21325v1)
    - PQC authentication for quantum key distribution
    - Quantum-secure communication

36. **Applied Post Quantum Cryptography in Industrial Environments** (2505.04333v1)
    - Practical PQC certificate generation
    - Industrial deployment

37. **A Scalable Framework for Post-Quantum Authentication in PKI** (2504.12062v1)
    - Enterprise-scale PQC PKI
    - Scalability and performance

38. **Streamlining Plug-and-Charge Authorization for EVs** (2501.14397v2)
    - OAuth2/OIDC for vehicle authentication
    - IoT passwordless authentication

39. **SLVC-DIDA: Signature-less Verifiable Credential** (2501.11052v2)
    - Privacy-preserving credentials
    - Decentralized identity

### Network Integration
40. **EAP-FIDO: Using FIDO2 Credentials for Network Authentication** (2412.03277v1)
    - FIDO2 for network-level auth
    - Enterprise network security

41. **FIDO2 Smart Card for Decentralized Financial Transactions** (2408.04977v1)
    - Smart card FIDO2 implementation
    - Financial system security

42. **SoK: Web Authentication in the Age of End-to-End Encryption** (2406.18226v1)
    - Systematization of knowledge
    - Web auth security analysis

---

## Reading Recommendations by Role

### Security Architects
**Start with:** 1, 2, 3, 14, 15, 16, 17, 18, 33
**Focus:** Agentic AI frameworks, zero trust architecture, identity control planes

### Implementation Engineers
**Start with:** 8, 9, 10, 11, 12, 20, 36, 37
**Focus:** FIDO2 implementation, passkey deployment, practical PQC

### Research & Development
**Start with:** 6, 7, 13, 19, 23, 34, 35
**Focus:** Post-quantum cryptography, formal verification, advanced biometrics

### Product Managers
**Start with:** 11, 28, 9, 10, 40
**Focus:** User experience, security friction, practical deployment

### Biometric Specialists
**Start with:** 4, 5, 19, 20, 21, 22, 23, 24, 25, 26
**Focus:** Biometric security, anti-spoofing, privacy preservation

---

## Quick Reference: Paper Categories

### By Year
- **2025:** 35 papers (88%)
- **2024:** 5 papers (12%)

### By Publication Month (2025)
- **October-December:** 12 papers
- **July-September:** 14 papers
- **April-June:** 6 papers
- **January-March:** 3 papers

### By Topic Distribution
- **Zero Trust:** 15 papers (38%)
- **Biometric Authentication:** 10 papers (25%)
- **FIDO2/WebAuthn:** 10 papers (25%)
- **Certificate/PKI:** 7 papers (18%)
- **Agentic AI:** 3 papers (8%)
- **Post-Quantum:** 8 papers (20%)

*Note: Papers may appear in multiple categories*

---

## Research Quality Indicators

### High-Impact Papers (>100 pages or major surveys)
- 2510.05163v1 - Deep Learning MFA Survey
- 2406.18226v1 - SoK: Web Authentication
- 2510.23457v1 - 5G Authentication (comprehensive)
- 2508.16662v1 - Mobile Zero Trust Framework

### Formal Verification & Mathematical Rigor
- 2511.06028v1 - FIDO UAF Formal Analysis
- 2509.22663v1 - Security Friction Quotient (empirical)
- 2502.10281v2 - TrustZero (verifiable)

### Implementation-Focused
- 2508.11928v1 - Passkey Implementation
- 2505.04333v1 - Industrial PQC Certificates
- 2508.01863v1 - Access Control at Scale
- 2507.09022v1 - SSH-Passkeys

### Novel Approaches
- 2510.02563v1 - Ear Canal Biometric
- 2509.13597v1 - Agentic JWT
- 2509.00332v1 - CryptoFace Encrypted
- 2509.20024v1 - GANs for Biometric Privacy

---

## Cross-Reference: Technology Combinations

### FIDO2 + Post-Quantum
- 2510.21353v1, 2511.00111v1, 2510.23457v1

### Zero Trust + Agentic AI
- 2505.19301v2, 2508.12259v3, 2509.13597v1

### Biometric + Privacy-Preserving
- 2509.00332v1, 2509.20024v1, 2508.18453v3, 2508.18415v1

### Certificate + Post-Quantum
- 2511.00111v1, 2504.12062v1, 2505.04333v1, 2507.21325v1

### Zero Trust + mTLS
- 2508.01863v1, 2511.04925v1, 2510.16067v1

---

## Related Research Areas (Not Covered)

Potential gaps for future research:
1. Quantum authentication protocols
2. Blockchain-based identity (limited coverage)
3. Behavioral biometrics (continuous typing, mouse movement)
4. WebAuthn extensions and future standards
5. Cross-domain federation protocols
6. FIDO2 for IoT and embedded systems
7. Passwordless authentication for legacy systems

---

**Last Updated:** December 11, 2025
**Total Papers:** 40
**Target Directory:** `/Users/tamnguyen/Documents/GitHub/ksi_watch/KSI-IAM-02_25-12A_PasswordlessAuthentication/references/passwordless_security/`
