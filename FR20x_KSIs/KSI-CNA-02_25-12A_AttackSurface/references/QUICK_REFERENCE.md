# Supply Chain Attack Surface Minimization - Quick Reference

## Research Completed: December 10, 2025

### Download Summary
**Total Papers**: 58 cutting-edge research papers (2024-2025)
**Storage Location**: `/Users/tamnguyen/Documents/GitHub/ksi_watch/KSI-CNA-02_25-12A_AttackSurface/references/`

### Papers by Category

| Category | Count | Location |
|----------|-------|----------|
| Supply Chain Security Frameworks | 15 | `supply_chain_security/` |
| Container & Artifact Integrity | 7 | `container_integrity/` |
| CI/CD Pipeline Security | 14 | `cicd_security/` |
| Dependency Vulnerability Management | 14 | `dependency_management/` |
| AI Model Supply Chain Security | 8 | `model_supply_chain/` |

---

## Top 10 Must-Read Papers

### 1. Supply Chain Insecurity: SBOM Solutions (Dec 2024)
**File**: `supply_chain_security/2412.05138_supply_chain_insecurity_sbom.pdf`
**Key Finding**: Reveals 97.5% false positive rate in SBOM-based vulnerability scanners

### 2. Ambush from All Sides: CI/CD Threats (Jan 2024)
**File**: `cicd_security/2401.17606_ambush_cicd_threats.pdf`
**Key Finding**: 25% of 320,000+ CI/CD pipelines pass credentials insecurely

### 3. SLSA Deployment Challenges (Sep 2024)
**File**: `supply_chain_security/2409.05014_slsa_deployment_challenges.pdf`
**Key Finding**: Analysis of 1,523 GitHub issues reveals implementation barriers

### 4. Kubernetes Security Landscape (Sep 2024)
**File**: `container_integrity/2409.04647_kubernetes_security_landscape.pdf`
**Key Finding**: Sys:All Loophole affected 250,000+ production clusters

### 5. Malicious Package Detection (Updated 2024)
**File**: `dependency_management/2309.02637_malicious_package_detection.pdf`
**Key Finding**: Cerebro detected 1,482 new malicious packages in NPM/PyPI

### 6. Atlas: ML Provenance Framework (Feb 2025)
**File**: `model_supply_chain/2502.19567_atlas_ml_provenance.pdf`
**Key Finding**: Fully attestable ML pipelines with TEE integration

### 7. IRIS: LLM-Assisted Static Analysis (May 2024)
**File**: `cicd_security/2405.17238_iris_llm_static_analysis.pdf`
**Key Finding**: Neuro-symbolic approach for whole-repository vulnerability detection

### 8. Maven Dependency Risks (Mar 2025)
**File**: `dependency_management/2503.22134_maven_dependency_risks.pdf`
**Key Finding**: Transitive vulnerabilities have 2x impact vs. direct dependencies

### 9. Architectural Backdoors Survey (Jul 2025)
**File**: `model_supply_chain/2507.12919_architectural_backdoors_survey.pdf`
**Key Finding**: 352,000 suspicious issues in 51,700 AI models

### 10. Zero Trust Systematic Review (Mar 2025)
**File**: `cicd_security/2503.11659_zero_trust_systematic_review.pdf`
**Key Finding**: 10-year evolution of ZTA (2016-2025) with PRISMA framework

---

## Critical Statistics

### SBOM and Provenance
- **97.5%** false positive rate in vulnerability scanners
- **SBOMs miss 100%** of transitive dependencies in some tools
- **Manipulation vulnerabilities** found in all major SBOM generators

### CI/CD Pipeline Security
- **25%** of pipelines pass credentials to CI/CD systems
- **11.04 months** average update lag for dependencies
- **83.56%** of script references are outdated
- **CVE-2025-30066**: GitHub Actions compromise affected 23,000+ repos

### Dependency Management
- **62.89%** of releases impacted through transitive dependencies
- **23,730** malicious packages cataloged (NPM/PyPI)
- **742%** average annual increase in OSS supply chain attacks
- **2x impact** from transitive vs. direct vulnerabilities

### Container Security
- **250,000+** K8s clusters affected by Sys:All Loophole
- **Low consistency** among VEX container scanners
- **90%+** of organizations will run containers by 2026

### AI Model Supply Chain
- **352,000** suspicious model issues flagged
- **Architectural backdoors** persist through retraining
- **PyTorch** and **Hugging Face** breaches in 2024

---

## Production-Ready Tools Identified

### SLSA and Attestation
- **SLSA Framework** - Supply-chain Levels for Software Artifacts
- **Sigstore** - Keyless signing with transparency logs
- **GitHub Artifact Attestations** - Tamper-proof provenance

### Package Security
- **Cerebro** - Unified malicious package detector (NPM/PyPI)
- **Donapi** - NPM behavior-based detection
- **VODA** - SCA tool for 1,000+ projects

### Static Analysis
- **IRIS** - LLM-assisted whole-repository analysis
- **CodeQL** - GitHub's semantic analysis engine
- **osv-scanner** - 25+ ecosystem vulnerability aggregation

### ML Security
- **Atlas** - ML lifecycle provenance framework
- **TrojAI** - NIST backdoor detection corpus
- **Guardian** - Protect AI's model scanner

### Zero Trust
- **TrustZero** - Scalable supply chain ZTA framework
- **OIDC** - Keyless authentication for CI/CD

---

## Real-World Incidents Validated

### 2024-2025 Major Supply Chain Attacks

1. **CVE-2025-30066** (Mar 2025)
   - tj-actions/changed-files GitHub Action compromise
   - Affected 23,000+ repositories
   - Exfiltrated CI/CD secrets to attacker endpoint

2. **GhostAction Campaign** (Sep 2025)
   - 327 GitHub accounts compromised
   - 3,325 secrets stolen from 817 repositories
   - PyPI, npm, DockerHub tokens targeted

3. **XZ Utils Backdoor** (2024)
   - Official tarballs contained backdoor absent in source
   - Validated importance of reproducible builds
   - Could have been prevented by build verification

4. **PyTorch Nightly Builds** (Dec 2022, still relevant)
   - Dependency hijack in build pipeline
   - Model supply chain vulnerability

5. **Hugging Face Models** (Feb 2024)
   - Malware-laced models discovered
   - 51,700 models flagged with suspicious issues

---

## Key Frameworks and Standards

### Supply Chain Security
- **SLSA** (Supply-chain Levels for Software Artifacts)
  - Level 1: Documentation
  - Level 2: Build provenance with verification
  - Level 3: Hardened builds with protection
  - Level 4: Highest level with comprehensive review

### SBOM Standards
- **SPDX 3.0** - ISO/IEC standard
- **CycloneDX** - OWASP standard
- **SWID** - ISO/IEC 19770-2

### Vulnerability Databases
- **OSV** - Open Source Vulnerabilities
- **NVD** - National Vulnerability Database
- **GHSA** - GitHub Security Advisories
- **Snyk.io** - Commercial vulnerability intelligence

---

## Emerging Trends

### AI-Driven Security (2024-2025)
- LLMs for credential detection (100,000+ repos analyzed)
- ML-based malicious package detection (23,730 packages)
- AI agents introducing new CI/CD risks (PromptPwnd)
- Neuro-symbolic approaches (IRIS framework)

### Zero Trust Evolution
- 10-year research evolution (2016-2025)
- Integration with supply chain security
- Continuous verification replacing perimeters
- Application to pharmaceutical, power grid, IoT

### Reproducible Builds
- Hermetic build environments standard
- Lockfiles for transparent tracking
- XZ Utils validates importance
- Java ecosystem focus

### Supply Chain Attestation
- SLSA compliance becoming baseline
- Cryptographic signing standard
- Open standards stabilization (SPDX 3, SLSA 1.0)
- GitHub Artifact Attestations GA

---

## Next Actions

### Immediate Priorities
1. ✅ Read top 10 must-read papers
2. ✅ Review SUPPLY_CHAIN_RESEARCH_INVENTORY.md for full details
3. ✅ Evaluate production tools for deployment
4. ✅ Develop comprehensive survey paper
5. ✅ Create attack surface taxonomy

### Tool Evaluation Queue
1. **SLSA Implementation** - Sigstore + GitHub Attestations
2. **Cerebro Deployment** - NPM/PyPI malicious package detection
3. **IRIS Integration** - LLM-assisted static analysis
4. **Atlas Testing** - ML provenance framework
5. **TrustZero Pilot** - Zero-trust supply chain

### Policy Development
1. **SBOM Requirements** - Generation and validation policies
2. **Dependency Management** - Update and scanning requirements
3. **Zero Trust Architecture** - Implementation guidelines
4. **Container Security** - Image signing and attestation
5. **AI Model Verification** - Provenance and integrity checks

---

## Contact and Resources

**Full Inventory**: `SUPPLY_CHAIN_RESEARCH_INVENTORY.md`
**Research Location**: `/Users/tamnguyen/Documents/GitHub/ksi_watch/KSI-CNA-02_25-12A_AttackSurface/references/`
**Last Updated**: December 10, 2025

---

## Sources

All research papers downloaded from ArXiv.org with full citations available in the comprehensive inventory document.

Key research institutions:
- NSF Secure Software Supply Chain Center (S3C2)
- GitHub Security Lab
- Microsoft Security Response Center
- Google Project Zero
- Academic security research groups worldwide

