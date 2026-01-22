# Archived Papers - Lower Relevance for Topic 5

**Topic:** Agent-to-Agent Mutual TLS with Real-Time Certificate Revocation
**Issue:** #68 Topic 5
**Archive Date:** 2025-12-25
**Total Archived Papers:** 42

## Archive Criteria

Papers archived here are relevant to the broader topic of TLS, PKI, and certificate management but have lower direct relevance to the specific requirements:
- Agent-to-agent mutual TLS authentication
- Real-time certificate revocation mechanisms (OCSP, CRL)
- Performance and scalability in production deployments

Papers ranked 11-52 are cataloged below with basic metadata. Full details available in `metadata.json`.

---

## Post-Quantum Cryptography & PKI (10 papers)

These papers focus on integrating post-quantum cryptography into TLS and PKI systems:

1. **2504.12062** - A Scalable Framework for Post-Quantum Authentication in Public Key Infrastructures (2025)
2. **2408.02179** - X.509 Information Security Certification Based on Post-Quantum Cryptography (2024)
3. **2511.00111** - A Comparative Study of Hybrid Post-Quantum Cryptographic X.509 Certificate Schemes (2025)
4. **2404.13544** - Faster Post-Quantum TLS 1.3 Based on ML-KEM: Implementation and Assessment (2024)
5. **2510.10436** - Post-Quantum Cryptography and Quantum-Safe Security: A Comprehensive Survey (2024)
6. **2401.17538** - Post-Quantum Cryptography for Internet of Things: A Survey (2024)
7. **2311.18674** - LiteQSign: Lightweight and Quantum-Safe Signatures for Heterogeneous IoT (2025)
8. **2409.13937** - Lightweight and Resilient Signatures for Cloud-Assisted Embedded IoT Systems (2024)

**Archive Reason:** While important for future-proofing, post-quantum cryptography integration is not the primary focus of current mTLS revocation requirements.

---

## Certificate Transparency & Revocation Theory (8 papers)

These papers address certificate transparency, revocation paradigms, and theoretical foundations:

9. **2203.02280** - Postcertificates for Revocation Transparency (2022)
10. **1704.04937** - Certificate Transparency with Enhancements and Short Proofs (2017)
11. **2405.05206** - Anomaly Detection in Certificate Transparency Logs (2024)
12. **2102.04288** - Revocation Statuses on the Internet (2021)
13. **2208.03951** - One-Time Certificates for Reliable and Secure Document Signing (2022)
14. **2503.22010** - Towards Privacy-Preserving Revocation of Verifiable Credentials (2025)
15. **cs/9909012** - Certificate Revocation Paradigms (1999)
16. **1705.06903** - Optimized Certificate Revocation List Distribution for Secure V2X Communications (2017)

**Archive Reason:** These focus on certificate transparency logging, theoretical revocation paradigms, or specialized use cases (V2X, document signing) rather than real-time service-to-service revocation.

---

## Blockchain-Based PKI & Decentralized Identity (7 papers)

Papers exploring blockchain and distributed ledger approaches to PKI:

17. **2407.04536** - Blockchain-based PKI within a Corporate Organization (2024)
18. **1806.03914** - CertLedger: A New PKI Model with Certificate Transparency Based on Blockchain (2018)
19. **2012.15351** - A Decentralized Dynamic PKI based on Blockchain (2020)
20. **2207.09127** - Smart Contract Assisted Blockchain based PKI System (2022)
21. **2402.02455** - A Survey on Decentralized Identifiers and Verifiable Credentials (2025)
22. **2503.15964** - Are We There Yet? A Study of Decentralized Identity Applications (2025)
23. **2207.02207** - None Shall Pass: A blockchain-based federated identity management system (2022)

**Archive Reason:** Blockchain-based approaches introduce latency incompatible with real-time revocation requirements. Relevant for research but not immediate implementation.

---

## Zero Trust Architecture & Service Mesh (5 papers)

Papers on zero trust, service mesh security, and network segmentation:

24. **2503.11659** - Zero Trust Architecture: A Systematic Literature Review (2025)
25. **2411.12162** - Microsegmented Cloud Network Architecture for Zero Trust (2024)
26. **2210.12610** - Partially Trusting the Service Mesh Control Plane (2022)
27. **2502.10281** - TrustZero - open, verifiable and scalable zero-trust (2025)
28. **2212.14422** - Security, Privacy and Challenges in Microservices Architecture (2022)

**Archive Reason:** Broader architectural patterns; useful context but not specifically addressing mTLS performance or revocation mechanisms.

---

## IoT & Lightweight Authentication (4 papers)

Papers focusing on constrained device authentication:

29. **2410.12190** - LPUF-AuthNet: Lightweight PUF-Based IoT Authentication (2024)
30. **2405.13146** - A lightweight PUF-based authentication protocol (2024)
31. **1902.04255** - Communication-efficient Certificate Revocation for IoT (2019)

**Archive Reason:** Focus on resource-constrained devices and PUF-based authentication rather than mTLS between full-capability agents.

---

## Federated Identity & API Security (6 papers)

Papers on federated authentication and API gateway security:

32. **2512.01832** - Privacy-Preserving Information-Sharing Protocol for Federated Authentication (2025)
33. **2405.03955** - IPFed: Identity protected federated learning for user authentication (2024)
34. **2505.19301** - Zero-Trust Identity Framework for Agentic AI (2025)
35. **2506.11950** - Secure API-Driven Research Automation (2025)
36. **2411.13441** - API Design for Interoperability and Security of IoT (2024)
37. **2408.03960** - Microservice Vulnerability Analysis (2024)

**Archive Reason:** Focus on federated identity patterns and API security rather than direct mTLS certificate revocation.

---

## Edge Computing & Network Security (2 papers)

Papers examining edge computing security challenges:

38. **2404.09681** - Dissecting Open Edge Computing Platforms: Security Risks (2024)
39. **2409.17670** - A Comprehensive Review of TLSNotary Protocol (2024)

**Archive Reason:** Edge computing presents unique challenges, but papers focus on broader security issues rather than mTLS revocation specifics.

---

## Certificate Centralization & Digital Sovereignty (2 papers)

Papers on geopolitical aspects of PKI:

40. **2504.16897** - Assessing SSL/TLS Certificate Centralization (2025)
41. **1901.11520** - Formal Security Analysis of OpenID Financial-grade API (2019)

**Archive Reason:** Important for understanding CA centralization risks, but not directly applicable to technical mTLS implementation.

---

## Performance & Optimization (2 papers)

Papers on RPKI and other certificate system optimizations:

42. **2507.01465** - Pruning the Tree: Rethinking RPKI Architecture (2025)

**Archive Reason:** RPKI-specific optimizations not directly transferable to mTLS agent authentication.

---

## Research Value

All archived papers provide valuable context for understanding:
- Evolution of PKI and certificate management
- Emerging alternatives to traditional CA-based systems
- Performance trade-offs in different deployment scenarios
- Security considerations across various use cases

For implementation of agent-to-agent mTLS with real-time revocation, prioritize the **TOP 10 papers** in the main directory.

---

## Access Information

- **Metadata:** All papers cataloged in `../metadata.json`
- **Download Status:** PDFs not downloaded to save storage; URLs provided in metadata
- **Priority Papers:** See main directory for downloaded TOP 10 papers
- **Search Date:** 2025-12-25
- **Total Papers Evaluated:** 52
