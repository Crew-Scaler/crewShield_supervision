# Quick Reference Guide: Topic 8 Papers
## Key Material Exfiltration Prevention During Rotation

---

## Top 10 Papers - Quick Access

### 1. HSM/TPM Cloud Failures (Score: 38.5) - **HIGHEST PRIORITY**
**File:** `01_2507.17655v2.pdf`
**Focus:** Hardware security module vulnerabilities, cloud threats, key management failures
**Why Read:** Most relevant to understanding real-world key exfiltration vectors in cloud environments

### 2. SSH-Passkeys (Score: 32.5) - **HIGH PRIORITY**
**File:** `02_2507.09022v1.pdf`
**Focus:** Key lifecycle management, attestation, passwordless authentication
**Why Read:** Practical key lifecycle and key material protection implementation

### 3. QLink Quantum-Safe (Score: 27.0)
**File:** `03_2512.18488v1.pdf`
**Focus:** Post-quantum cryptography, HSM integration, blockchain security
**Why Read:** Advanced HSM usage with quantum-safe considerations

### 4. Proof of Cloud (Score: 26.5)
**File:** `04_2510.12469v1.pdf`
**Focus:** TPM attestation, confidential VMs, trusted execution environments
**Why Read:** Attestation mechanisms for key security verification

### 5. Secure Device Framework (Score: 25.5)
**File:** `05_2501.13716v1.pdf`
**Focus:** End-to-end key management, hardware to application security
**Why Read:** Comprehensive key management framework across all layers

### 6. Multi-Factor Auth Survey (Score: 25.5)
**File:** `06_2510.05163v1.pdf`
**Focus:** TPM, secure enclaves, secure storage, biometric integration
**Why Read:** Secure storage mechanisms for credentials and keys

### 7. Key Derivation Functions (Score: 25.0) - **HIGH PRIORITY**
**File:** `07_2509.05893v1.pdf`
**Focus:** Cryptographic key derivation, entropy management, security analysis
**Why Read:** Deep cryptographic analysis of key generation and management security

### 8. Automotive Security (Score: 24.5)
**File:** `08_2506.13261v1.pdf`
**Focus:** Certificate lifecycle, authentication, long-term key management
**Why Read:** Key management for safety-critical, long-lived systems

### 9. Kyber Post-Quantum (Score: 24.5)
**File:** `09_2505.01782v1.pdf`
**Focus:** Post-quantum KEM, hardware implementation, TPM integration
**Why Read:** Hardware-level post-quantum key security

### 10. Quantum Key Distribution (Score: 24.0)
**File:** `10_2508.09735v1.pdf`
**Focus:** Secure key material transmission, QKD networks
**Why Read:** Physical-layer key distribution security

---

## Reading Priority by Topic

### For Key Exfiltration Prevention:
1. **Paper #1** - HSM/TPM Cloud Failures (real-world attack vectors)
2. **Paper #4** - Proof of Cloud (attestation/verification)
3. **Paper #2** - SSH-Passkeys (lifecycle security)

### For Key Rotation Security:
1. **Paper #2** - SSH-Passkeys (lifecycle management)
2. **Paper #7** - Key Derivation (entropy and rotation security)
3. **Paper #8** - Automotive Security (long-term rotation strategies)

### For Secure Deletion:
1. **Paper #1** - HSM/TPM Failures (deletion failures in cloud)
2. **Paper #6** - Multi-Factor Auth (secure storage and erasure)
3. **Paper #5** - Device Framework (hardware-level deletion)

### For Hardware Security:
1. **Paper #1** - HSM/TPM Cloud Failures
2. **Paper #3** - QLink (HSM integration)
3. **Paper #9** - Kyber FPGA (hardware crypto)

### For Post-Quantum Considerations:
1. **Paper #9** - Kyber Post-Quantum
2. **Paper #3** - QLink Quantum-Safe
3. **Paper #5** - Secure Device Framework

---

## Key Concepts by Paper

### Hardware Security Modules (HSM)
- Papers: #1 (comprehensive), #3 (integration)
- Total: 2 papers with deep HSM coverage

### Trusted Platform Modules (TPM)
- Papers: #1 (failures), #4 (attestation), #6 (MFA), #9 (PQC)
- Total: 4 papers with TPM focus

### Key Lifecycle
- Papers: #2 (complete lifecycle), #8 (long-term)
- Total: 2 papers with lifecycle emphasis

### Attestation & Verification
- Papers: #2 (passkey attestation), #4 (cloud attestation)
- Total: 2 papers on attestation

### Post-Quantum Cryptography
- Papers: #3 (QKD+PQC), #5 (PQC framework), #9 (Kyber implementation)
- Total: 3 papers with PQC content

---

## FedRAMP Control Mapping

### SC-12 (Cryptographic Key Establishment and Management)
**Primary Papers:** #1, #2, #3, #5, #7
**Read Order:** #7 → #2 → #1

### SC-13 (Cryptographic Protection)
**Primary Papers:** #3, #5, #9
**Read Order:** #9 → #3 → #5

### SC-28 (Protection of Information at Rest)
**Primary Papers:** #1, #4, #6
**Read Order:** #1 → #6 → #4

### AU-9 (Protection of Audit Information)
**Primary Papers:** #2, #4
**Read Order:** #4 → #2

---

## Recommended Reading Sequence

### Week 1: Foundation (Papers 1, 2, 7)
1. **Paper #1** - Understand real-world failures
2. **Paper #7** - Learn cryptographic fundamentals
3. **Paper #2** - Study practical lifecycle implementation

### Week 2: Hardware & Verification (Papers 4, 5, 6)
4. **Paper #4** - TPM-based attestation
5. **Paper #5** - Comprehensive framework
6. **Paper #6** - Secure storage mechanisms

### Week 3: Advanced Topics (Papers 3, 8, 9, 10)
7. **Paper #9** - Post-quantum hardware
8. **Paper #3** - Quantum-safe integration
9. **Paper #8** - Long-term management
10. **Paper #10** - Secure distribution

---

## Critical Sections to Focus On

### In Paper #1 (HSM/TPM Failures):
- Section on API exploitation
- Cloud-specific attack vectors
- Mitigation strategies
- Key exfiltration techniques

### In Paper #2 (SSH-Passkeys):
- Key lifecycle management section
- Attestation protocol details
- Key material protection mechanisms
- Credential rotation procedures

### In Paper #7 (Key Derivation):
- Entropy state transitions
- Multi-factor key derivation
- Security analysis methodology
- Vulnerability patterns

### In Paper #4 (Proof of Cloud):
- TPM attestation protocols
- Certificate verification
- Remote attestation chains
- Trust establishment

---

## Search Terms for In-Paper Navigation

Use these terms when searching within PDFs:

### Key Management Terms:
- "key rotation"
- "key deletion"
- "key lifecycle"
- "key material"
- "key exfiltration"

### Hardware Security Terms:
- "HSM"
- "TPM"
- "secure enclave"
- "hardware security"
- "root of trust"

### Verification Terms:
- "attestation"
- "verification"
- "audit"
- "validation"
- "integrity"

### Security Control Terms:
- "access control"
- "authentication"
- "authorization"
- "confidentiality"
- "secure deletion"

---

## Additional Resources

### Metadata File:
`metadata.json` - Full paper details, abstracts, and relevance scoring

### Archived Papers:
`_archived_low_relevance/archived_papers.json` - 506 additional papers for deeper research

### Research Summary:
`RESEARCH_SUMMARY.md` - Comprehensive analysis and findings

---

## Quick Stats

- **Total Storage:** ~9.8 MB (10 PDFs)
- **All Papers from:** 2025
- **Average Relevance Score:** 27.4
- **Highest Score:** 38.5 (Paper #1)
- **Lowest Score:** 24.0 (Paper #10)

- **US Institution Papers:** 7 out of 10
- **Papers with HSM content:** 3
- **Papers with TPM content:** 4
- **Papers with PQC content:** 3

---

**Last Updated:** December 25, 2025
**Status:** Research Complete - Ready for Review
