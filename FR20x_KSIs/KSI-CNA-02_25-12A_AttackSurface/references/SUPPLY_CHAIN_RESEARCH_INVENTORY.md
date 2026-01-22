# Supply Chain Attack Surface Minimization Research Papers
## Comprehensive Inventory - December 2025

**Research Focus**: Supply chain security frameworks, dependency management, container integrity, CI/CD pipeline security, and AI model supply chain security for AI-era cloud service providers.

**Total Papers Downloaded**: 58 papers (2024-2025)

---

## 1. Supply Chain Security Frameworks (15 papers)

### Core SBOM and Provenance
1. **2412.05138_supply_chain_insecurity_sbom.pdf** - December 2024
   - *Supply Chain Insecurity: The Lack of Integrity Protection in SBOM Solutions*
   - Systematic investigation of trust in SBOM outputs; reveals manipulation vulnerabilities

2. **2506.03507_sbom_systematic_review.pdf** - June 2025
   - *Software Bill of Materials in Software Supply Chain Security: A Systematic Literature Review*
   - Synthesizes 40 peer-reviewed studies on SBOM applications

3. **2510.05798_sbomproof.pdf** - October 2025
   - *SBOMproof: Beyond Alleged SBOM Compliance for Supply Chain Security*
   - Addresses SBOM compliance verification challenges

### SLSA Framework and Attestation
4. **2409.05014_slsa_deployment_challenges.pdf** - September 2024
   - *Analyzing Challenges in Deployment of the SLSA Framework*
   - Qualitative study of 1,523 SLSA-related GitHub issues

5. **2406.10109_sok_supply_chain_secure_design.pdf** - June 2024
   - *SoK: Analysis of Software Supply Chain Security by Establishing Secure Design Properties*
   - Attack trees and secure design patterns framework

6. **2405.14993_sok_defense_supply_chain.pdf** - May 2024
   - *SoK: A Defense-Oriented Evaluation of Software Supply Chain Security*
   - Defense framework with explicit attack-to-objective mapping

### Industry and Academic Summits
7. **2505.10538_s3c2_summit_2024.pdf** - May 2025
   - *S3C2 Summit 2024-09: Industry Secure Supply Chain Summit*
   - NSF-backed summit practical challenges discussion

8. **2510.24920_s3c2_summit_2025.pdf** - October 2025
   - *S3C2 Summit 2025-03: Industry Secure Supply Chain Summit*
   - Latest SBOM implementation challenges

### Specialized Supply Chain Security
9. **2509.16899_autonomous_vehicles_supply_chain.pdf** - September 2025
   - *Security Vulnerabilities in Software Supply Chain for Autonomous Vehicles*
   - 107 attack vectors across contribution, build, and distribution stages

10. **2509.08083_supply_chain_task_adoption.pdf** - September 2025
    - *Establishing a Baseline of Software Supply Chain Security Task Adoption*
    - Empirical baseline of organizational adoption patterns

11. **2406.13166_ml_supply_chain_security.pdf** - June 2024
    - *Enhancing Supply Chain Security with Automated Machine Learning*
    - ML-based security enhancement approaches

### Reproducible and Hermetic Builds
12. **2504.21679_reproducible_builds_java.pdf** - April 2025
    - *Causes and Canonicalization of Unreproducible Builds in Java*
    - Root causes taxonomy of unreproducibility

13. **2510.00730_maven_lockfile.pdf** - October 2025
    - *Maven-Lockfile: High Integrity Rebuild of Past Java Releases*
    - Lockfiles for reproducible and transparent builds

14. **2402.00424_reproducibility_build_environments.pdf** - February 2024
    - *Reproducibility of Build Environments through Space and Time*
    - Hermetic and sandboxed build environments

### Social Engineering and Human Factors
15. **2402.18401_devphish_social_engineering.pdf** - February 2024
    - *DevPhish: Exploring Social Engineering in Software Supply Chain Attacks*
    - Developer-targeted social engineering vectors

---

## 2. Container and Artifact Integrity (7 papers)

### Container Security Foundations
1. **2506.02043_docker_security.pdf** - May 2025
   - *Docker under Siege: Securing Containers in the Modern Era*
   - Comprehensive Docker security challenges examination

2. **2409.04647_kubernetes_security_landscape.pdf** - September 2024
   - *The Kubernetes Security Landscape: AI-Driven Insights from Developer Discussions*
   - Analysis of Sys:All Loophole affecting 250,000+ clusters

3. **2504.07707_container_security_practitioners.pdf** - April 2025
   - *Managing Security Issues in Software Containers: From Practitioners' Perspective*
   - Practitioner perspectives on security management

### SLSA Implementation in Kubernetes
4. **2503.20079_argo_slsa_kubernetes.pdf** - March 2025
   - *ARGO-SLSA: Software Supply Chain Security in Argo Workflows*
   - Kubernetes-native controller for SLSA compliance

5. **2403.12980_containerization_multicloud.pdf** - March 2024
   - *Containerization in Multi-Cloud Environment*
   - Multi-cloud containerization strategies and challenges

### Runtime Integrity and Attestation
6. **2408.10200_sok_runtime_integrity.pdf** - August 2024
   - *SoK: Runtime Integrity* (IEEE S&P 2025)
   - CFI, CFA, secure boot, and remote attestation

7. **2506.23706_attestable_audits_tee.pdf** - June 2025
   - *Attestable Audits: Verifiable AI Safety Benchmarks Using Trusted Execution Environments*
   - AWS Nitro Enclaves for attestation pipelines

---

## 3. CI/CD Pipeline Security (14 papers)

### CI/CD Threat Analysis
1. **2401.17606_ambush_cicd_threats.pdf** - January 2024
   - *Ambush from All Sides: Understanding Security Threats in Open-Source Software CI/CD Pipelines*
   - Analysis of 320,000+ CI/CD pipeline-configured repos; 25% pass credentials

2. **2506.06478_stride_cicd_threat_modeling.pdf** - June 2025
   - *Enhancing Software Supply Chain Security through STRIDE-Based Threat Modelling of CI/CD Pipelines*
   - STRIDE framework application to CI/CD

3. **2511.01395_build_compromises_vulnerability.pdf** - November 2025
   - *Characterizing Build Compromises Through Vulnerability Disclosure Analysis*
   - Build infrastructure as second major attack vector

### Secrets Management and Credential Protection
4. **2506.13090_hardcoded_credentials_llm.pdf** - June 2025
   - *Detecting Hard-Coded Credentials in Software Repositories via LLMs*
   - Analysis of 100,000+ repositories for credential leakage

5. **2509.09036_secret_management_tools.pdf** - September 2025
   - *Extended Version: It Should Be Easy but... New Users' Experiences with Secret Management Tools*
   - Usability study of HashiCorp Vault and Infisical

6. **2504.18784_secret_breach_detection_llm.pdf** - April 2025
   - *Secret Breach Detection in Source Code with Large Language Models*
   - LLM-based secret detection to reduce false positives

### Static Analysis and Code Review
7. **2407.12241_sast_secure_code_review.pdf** - July 2024
   - *An Empirical Study of Static Analysis Tools for Secure Code Review*
   - Analysis of 319 vulnerabilities; SAST can flag 52% of VCCs

8. **2405.17238_iris_llm_static_analysis.pdf** - May 2024
   - *IRIS: LLM-Assisted Static Analysis for Detecting Security Vulnerabilities*
   - Neuro-symbolic approach for whole-repository reasoning

9. **2407.16235_sast_llm_comparison.pdf** - July 2024
   - *Comparison of Static Application Security Testing Tools and Large Language Models*
   - Repository-level vulnerability detection comparison

### Zero Trust Architecture
10. **2503.11659_zero_trust_systematic_review.pdf** - March 2025
    - *Zero Trust Architecture: A Systematic Literature Review*
    - 10 years of ZTA research (2016-2025) using PRISMA framework

11. **2502.10281_trustzero_framework.pdf** - February 2025
    - *TrustZero: Open, Verifiable and Scalable Zero-Trust*
    - Framework leveraging complexity as strength

12. **2508.15776_zero_trust_pharma_supply_chain.pdf** - August 2025
    - *Implementing Zero Trust Architecture in Pharmaceutical Supply Chain*
    - Continuous verification and least-privilege access

13. **2403.06388_zero_trust_power_grid.pdf** - March 2024
    - *A Zero Trust Framework for Realization and Defense Against GenAI Attacks in Power Grid*
    - Early detection of GenAI-driven attacks

14. **2502.03614_zero_trust_iot_aiml.pdf** - February 2025
    - *A Novel Zero-Touch, Zero-Trust, AI/ML Framework for IoT Network Security*
    - DDoS detection, mitigation, and prevention

---

## 4. Dependency Vulnerability Management (14 papers)

### SBOM-based Vulnerability Management
1. **2511.20313_sbom_vulnerability_management.pdf** - December 2024
   - *A Reality Check on SBOM-based Vulnerability Management*
   - 97.5% false positive rate; proposes lock file usage

2. **2503.13998_sbom_vulnerability_description.pdf** - March 2025
   - *Augmenting Software Bills of Materials with Software Vulnerability Description*
   - GitHub study using osv-scanner

### Maven Ecosystem Studies
3. **2503.22134_maven_dependency_risks.pdf** - March 2025
   - *Decoding Dependency Risks: A Quantitative Study of Vulnerabilities in the Maven Ecosystem*
   - Transitive vulnerabilities have nearly double the impact

4. **2504.04175_maven_ripple_effect.pdf** - April 2025
   - *The Ripple Effect of Vulnerabilities in Maven Central*
   - Vulnerability propagation through dependency networks

5. **2502.04621_maven_cve_lifecycle.pdf** - February 2025
   - *Tracing Vulnerabilities in Maven: A Study of CVE Lifecycles and Dependency Networks*
   - Analysis of 3,362 CVEs in Maven

### Comprehensive Vulnerability Studies
6. **2512.03868_vulnerable_dependencies_impact.pdf** - December 2024
   - *A Comprehensive Study on the Impact of Vulnerable Dependencies on Open-Source Software*
   - 1k+ projects from GitHub (2013-2023) using VODA

7. **2506.01342_vulnerability_propagation.pdf** - June 2025
   - *Propagation-Based Vulnerability Impact Assessment for Software Supply Chains*
   - Vulnerability Propagation Scoring System (VPSS)

### Container Vulnerability Scanning
8. **2503.14388_vex_container_scanners.pdf** - March 2025
   - *Vexed by VEX tools: Consistency evaluation of container vulnerability scanners*
   - Low consistency among VEX-compliant scanners

### Vulnerable API and LLM Dependencies
9. **2409.02753_vulnerable_api_detection.pdf** - September 2024
   - *Does the Vulnerability Threaten Our Projects? Automated Vulnerable API Detection*
   - 90,749 vulnerable APIs from 362 libraries

10. **2508.21417_llm_vulnerable_dependencies.pdf** - August 2025
    - *An Empirical Study of Vulnerable Package Dependencies in LLM Repositories*
    - Security vulnerabilities in 52 LLM projects using Snyk.io

### Malicious Package Detection
11. **2309.02637_malicious_package_detection.pdf** - September 2023 (updated 2024)
    - *Killing Two Birds with One Stone: Malicious Package Detection in NPM and PyPI*
    - Cerebro detected 683 (PyPI) and 799 (NPM) new malicious packages

12. **2404.04991_malicious_packages_wild.pdf** - April 2024
    - *OSS Malicious Package Analysis in the Wild*
    - 23,730 malicious packages cataloged

13. **2412.05259_ml_malicious_pypi.pdf** - December 2024
    - *A Machine Learning-Based Approach For Detecting Malicious PyPI Packages*
    - ML-based PyPI malicious package detection

14. **2403.08334_donapi_npm_detector.pdf** - March 2024
    - *Donapi: Malicious NPM Packages Detector using Behavior Sequence Knowledge Mapping*
    - Behavior-based NPM malicious package detection

---

## 5. AI Model Supply Chain Security (8 papers)

### ML Provenance and Transparency
1. **2502.19567_atlas_ml_provenance.pdf** - February 2025
   - *Atlas: A Framework for ML Lifecycle Provenance & Transparency*
   - Fully attestable ML pipelines with verifiable records

2. **2505.22778_ml_supply_chain_problem.pdf** - May 2025
   - *Machine Learning Models Have a Supply Chain Problem*
   - Training data provenance and broader security issues

3. **2404.12736_llm_supply_chain_agenda.pdf** - April 2024
   - *Large Language Model Supply Chain: A Research Agenda*
   - Data poisoning as severe supply chain risk

### Data Poisoning and Model Integrity
4. **2503.09302_data_poisoning_detection.pdf** - March 2025
   - *Detecting and Preventing Data Poisoning Attacks on AI Models*
   - Methodologies leveraging data provenance

5. **2412.17614_llm_security_challenges.pdf** - December 2024
   - *Emerging Security Challenges of Large Language Models*
   - Supply chain attacks across ML lifecycle

### Backdoor and Trojan Attacks
6. **2507.12919_architectural_backdoors_survey.pdf** - July 2025
   - *Architectural Backdoors in Deep Learning: A Survey of Vulnerabilities*
   - Malicious logic embedded in computational graphs

7. **2509.07504_backdoor_attacks_cv_survey.pdf** - September 2025
   - *Backdoor Attacks and Defenses in Computer Vision Domain: A Survey*
   - Computer vision backdoor attack landscape

8. **2408.08920_trojan_attacks_survey.pdf** - August 2024
   - *A Survey of Trojan Attacks and Defenses to Deep Neural Networks*
   - Comprehensive trojan attack taxonomy

---

## Key Research Findings

### Critical Vulnerabilities Identified

1. **SBOM Limitations**
   - 97.5% false positive rate in vulnerability scanners
   - SBOMs only track direct dependencies, not transitive
   - Manipulation vulnerabilities in generation process

2. **CI/CD Security**
   - 25% of pipelines pass credentials to build systems
   - Average update lag: 11.04 months for script dependencies
   - 83.56% of script references are outdated

3. **Dependency Risks**
   - Transitive vulnerabilities have 2x impact vs. direct dependencies
   - 62.89% of releases impacted through transitive dependencies
   - Small applications can have thousands of transitive dependencies

4. **Container Security**
   - 250,000+ Kubernetes clusters affected by Sys:All Loophole (2024)
   - Low consistency among VEX container vulnerability scanners
   - Compromised registries enable malicious image injection

5. **AI Model Supply Chain**
   - Architectural backdoors persist through retraining
   - 352,000 suspicious issues flagged in 51,700 models
   - PyTorch, Hugging Face supply chain breaches in 2024

### Production-Ready Tools and Frameworks

1. **SLSA Framework** - Supply-chain Levels for Software Artifacts
2. **Sigstore** - Keyless signing with transparency logs
3. **GitHub Artifact Attestations** - Tamper-proof paper trails
4. **Cerebro** - Malicious package detection (NPM/PyPI)
5. **Atlas** - ML lifecycle provenance framework
6. **IRIS** - LLM-assisted static analysis
7. **TrustZero** - Scalable zero-trust framework

### Emerging Trends

1. **AI-Driven Security**
   - LLMs for credential detection and vulnerability analysis
   - AI agents creating new CI/CD security risks
   - ML-based malicious package detection

2. **Zero Trust Adoption**
   - 10 years of ZTA evolution (2016-2025)
   - Integration with supply chain security
   - Continuous verification replacing perimeter security

3. **Reproducible Builds**
   - Hermetic build environments
   - Lockfiles for transparent dependency tracking
   - XZ Utils backdoor validates reproducibility importance

4. **Supply Chain Attestation**
   - SLSA compliance becoming baseline
   - Cryptographic signing standard in CI/CD
   - Open standards (SPDX 3, SLSA 1.0) stabilization

---

## Research Methodology

**Search Strategy**: Systematic ArXiv searches for 2024-2025 papers
**Keywords**: SBOM, SLSA, CI/CD security, container integrity, dependency management, AI model supply chain, zero trust, reproducible builds
**Institutions**: NSF S3C2, GitHub, Microsoft, Google, academic security research groups
**Validation**: Cross-referenced with real-world incidents (CVE-2025-30066, GhostAction, tj-actions compromise)

---

## Download Statistics

- **Total Papers**: 58 papers
- **Date Range**: January 2024 - December 2025
- **Average Paper Size**: ~800 KB
- **Total Storage**: ~45 MB
- **Download Date**: December 10, 2025

---

## Next Steps for Integration

1. **Survey Paper Development**
   - Synthesize findings across 58 papers
   - Create comprehensive attack surface taxonomy
   - Develop mitigation strategy framework

2. **Production Tool Evaluation**
   - Test SLSA implementation (Sigstore, GitHub Attestations)
   - Evaluate Cerebro for malicious package detection
   - Deploy IRIS for static analysis

3. **Framework Implementation**
   - Integrate TrustZero principles
   - Implement Atlas for ML provenance
   - Deploy container signing with SLSA

4. **Policy Development**
   - SBOM generation requirements
   - Dependency update policies
   - Zero trust architecture guidelines

---

**Last Updated**: December 10, 2025
**Maintained By**: AI-Era Cloud Service Provider Security Research Team
