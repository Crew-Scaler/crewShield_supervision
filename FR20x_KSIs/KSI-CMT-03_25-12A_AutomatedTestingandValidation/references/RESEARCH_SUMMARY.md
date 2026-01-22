# Supply Chain Testing and Security Validation Research Summary
## ArXiv Papers Collection (2024-2025)

**Research Focus**: Automated testing and validation for AI-era cloud service providers, specifically supply chain testing and security validation.

**Collection Date**: December 10, 2025  
**Total Papers Downloaded**: 32 papers  
**Time Period Coverage**: 2022-2025 (focus on 2024-2025)

---

## Research Categories and Key Findings

### 1. Supply Chain Security Testing (10 papers)

**Location**: `/Users/tamnguyen/Documents/GitHub/ksi_watch/KSI-CMT-03_25-12A_AutomatedTestingandValidation/references/supply_chain_security/`

#### Key Papers:

1. **SBOMproof_2024.pdf** (ArXiv 2510.05798)
   - Evaluates SBOM generation tools and compliance
   - Compares software tools and cloud services for SBOM generation and CVE scanning
   - Critical for validating alleged SBOM compliance

2. **SecVul_AutonomousVehicles_2024.pdf** (ArXiv 2509.16899)
   - SBOM analysis using Microsoft's sbom-tool
   - Vulnerability scanning with Grype
   - Emphasizes routine SBOM scanning and timely dependency updates
   - Focus on both direct and transitive dependencies

3. **SoK_SupplyChainSecurity_2024.pdf** (ArXiv 2406.10109)
   - Systematization of knowledge on software supply chain security
   - Establishes secure design properties: transparency, validity, and separation
   - Identifies four stages of supply chain attacks

4. **DevSecOps_SMEs_2025.pdf** (ArXiv 2503.22612)
   - 68% of SMEs have implemented DevSecOps
   - Key barriers: technical complexity (41%), resource constraints (35%), cultural resistance (38%)
   - Only 12% conduct security scans per commit (automation gap)

5. **AI_DevSecOps_2024.pdf** (ArXiv 2504.19154)
   - AI-driven security approaches in DevSecOps
   - Comparative analysis of challenges, solutions, and future directions
   - Integration of SAST, DAST, and SCA tools

6. **STRIDE_ThreatModeling_CICD_2025.pdf** (ArXiv 2506.06478)
   - STRIDE-based threat modeling for CI/CD pipelines
   - References SolarWinds SUNBURST compromise
   - Integrates with SLSA framework and NIST SSDF

7-10. **S3C2 Summit Reports** (ArXiv 2510.24920, 2505.10538, 2504.00924, 2405.08762)
   - Industry and government secure supply chain summits (2024-2025)
   - Key topics: SBOMs, compliance, malicious commits, build infrastructure, LLMs and security
   - NSF-backed initiative with major universities
   - Finding: Running SCA tools directly sometimes better than using SBOMs for detecting vulnerable dependencies

**Key Statistics from Supply Chain Research**:
- 64.96% of Maven releases impacted by vulnerabilities
- Transitive vulnerabilities nearly double the number of direct vulnerabilities
- 84% of codebases contain at least one known open source vulnerability
- 74% have high-risk vulnerabilities

---

### 2. Dependency Vulnerability Testing (4 papers)

**Location**: `/Users/tamnguyen/Documents/GitHub/ksi_watch/KSI-CMT-03_25-12A_AutomatedTestingandValidation/references/dependency_scanning/`

#### Key Papers:

1. **Maven_DependencyRisks_2025.pdf** (ArXiv 2503.22134)
   - Quantitative study of vulnerabilities in Maven ecosystem
   - 64.96% of Maven releases impacted by vulnerabilities
   - Transitive vulnerabilities nearly 2x direct vulnerabilities
   - Current tools often fail to address systemic nature of transitive vulnerabilities

2. **Maven_CVE_Lifecycle_2025.pdf** (ArXiv 2502.04621)
   - Analyzes 3,362 CVEs in Maven
   - Uncovers patterns in vulnerability mitigation
   - Identifies factors influencing at-risk packages
   - Vulnerabilities propagate through library imports

3. **Maven_IndependentArtifacts_2024.pdf** (ArXiv 2504.12261)
   - Independent artifacts had fewer vulnerabilities (60 CVEs vs. 179 CVEs)
   - Zero propagated vulnerabilities in independent artifacts
   - Suggests independent artifacts lower transitive vulnerability risks

4. **DependencyPractices_VulnMitigation_2023.pdf** (ArXiv 2310.07847)
   - Dependency practices for vulnerability mitigation
   - Comprehensive dataset using Neo4j database (Goblin framework)
   - Dataset dated August 30, 2024, with CVE mappings

**Critical Gap Identified**: Despite availability of detection tools, current approaches fail to address the systemic nature of transitive vulnerabilities, requiring comprehensive studies across entire dependency chains.

---

### 3. Container and Infrastructure Testing (5 papers)

**Location**: `/Users/tamnguyen/Documents/GitHub/ksi_watch/KSI-CMT-03_25-12A_AutomatedTestingandValidation/references/container_security/`

#### Key Papers:

1. **Kubernetes_NetworkMisconfig_2025.pdf** (ArXiv 2506.21134)
   - "Inside Job: Defending Kubernetes Clusters Against Network Misconfigurations"
   - References Microsoft's threat matrix for Kubernetes
   - Misconfigurations identified as major factor in Kubernetes security threats

2. **Kubernetes_SecurityLandscape_AI_2024.pdf** (ArXiv 2409.04647)
   - AI-driven insights from developer discussions
   - **Critical Finding**: Sys:All Loophole vulnerability in 2024
   - Allowed takeover of GKE clusters with any Google account
   - Active in 250,000+ production Kubernetes clusters

3. **TrustedContainers_ConfidentialComputing_2022.pdf** (ArXiv 2205.05747)
   - Trusted Container Extensions (TCX) architecture
   - Combines container agility with hardware-enforced TEE protection
   - Runtime memory encryption for secure execution

4. **ProofOfCloud_DataCenter_TEE_2024.pdf** (ArXiv 2510.12469)
   - Data center execution assurance for confidential VMs
   - First-boot attestation processes
   - Cryptographic verification of system components

5. **KubeFence_SecurityHardening_2024.pdf** (ArXiv 2504.11126)
   - Security hardening of Kubernetes attack surface
   - Comprehensive analysis of security controls
   - Defense mechanisms for production clusters

**Key Security Tools Identified**:
- Red Hat Advanced Cluster Security (StackRox)
- Sysdig Secure (Falco-based)
- Kubescape (Kubernetes-specific)

---

### 4. Secrets and Credential Scanning (4 papers)

**Location**: `/Users/tamnguyen/Documents/GitHub/ksi_watch/KSI-CMT-03_25-12A_AutomatedTestingandValidation/references/secrets_detection/`

#### Key Papers:

1. **HardCodedCredentials_LLM_2025.pdf** (ArXiv 2506.13090)
   - Detecting hard-coded credentials via LLMs
   - Addresses CWE-798 (18th most dangerous software weakness, 2023)
   - Detects 8 categories: passwords, generic secrets, private keys, predefined patterns, seeds/salts/nonces, generic tokens, authentication keys/tokens, others

2. **SecretBreach_SourceCode_LLM_2024.pdf** (ArXiv 2504.18784)
   - 10 million hardcoded secrets detected in 2022 (67% increase from 2021)
   - Compromised credentials responsible for 50% of cyberattacks (H1 2023)
   - **Alarming**: 1212x increase in leaked OpenAI API keys (GenAI-related)

3. **TalesFromGit_SecretsDetection_2023.pdf** (ArXiv 2307.00892)
   - PassFinder model using ensemble of two CNN models
   - Context Model and Password Model for password leakage detection
   - Automated detection in source code

4. **ComparativeStudy_SecretsTools_2023.pdf** (ArXiv 2307.00714)
   - Comparative study of software secrets reporting by detection tools
   - **Tool Performance**:
     - Precision: GitHub Secret Scanner (75%), Gitleaks (46%), Commercial X (25%)
     - Recall: Gitleaks (88%), SpectralOps (67%)
   - TruffleHog: detects 800+ secret types, verifies against actual APIs

**Critical Statistics**:
- Stolen credentials exploits: 40% of all hacking breaches (2024)
- 39+ million secrets detected on GitHub repositories (2024)

---

### 5. Model Provenance and Lineage Testing (9 papers)

**Location**: `/Users/tamnguyen/Documents/GitHub/ksi_watch/KSI-CMT-03_25-12A_AutomatedTestingandValidation/references/model_provenance/`

#### Key Papers:

1. **ModelProvenanceTesting_LLM_2025.pdf** (ArXiv 2502.00706)
   - Framework for testing model provenance
   - Determines if one model is derived from another
   - Uses black-box access and statistical analysis
   - Critical for enforcing licensing terms and identifying derived models

2. **ProvenanceTracking_MLSystems_2025.pdf** (ArXiv 2507.01075)
   - Provenance tracking in large-scale ML systems
   - Logs deeper lineage information than MLFlow/Weights & Biases
   - Enables interpretation, analysis, and comparison of ML outputs
   - Tracks lineage of data, model updates, and system parameters

3. **Atlas_MLLifecycle_Provenance_2025.pdf** (ArXiv 2502.19567)
   - Framework for fully attestable ML pipelines
   - Addresses data poisoning and supply chain attacks
   - Leverages open specifications for provenance
   - Verifiable records of artifact authenticity and end-to-end lineage

4. **Blockchain_AI_Copyright_Provenance_2024.pdf** (ArXiv 2404.06077)
   - Blockchain for AI copyrights, provenance, and lineage
   - Facilitates data provenance throughout model retraining/fine-tuning
   - Maintains modelList and datasetList for tracking
   - DAG structure captures complete derivation history

5. **DataProvenance_AI_2024.pdf** (ArXiv 2404.12691)
   - Data authenticity, consent, and provenance for AI are all broken
   - Tools for tracing data origins increasingly relevant
   - **Crisis**: License omission rates >70%, error rates >50%
   - Study of 1,800+ text datasets reveals misattribution crisis

6. **MLSupplyChain_HuggingFace_2025.pdf** (ArXiv 2502.04484)
   - ML supply chain in Software 2.0 era
   - Empirical analysis of Hugging Face model and dataset documentation
   - Supply chain and licensing challenges
   - Hugging Face platform structured documentation analysis

7. **MLModels_SupplyChainProblem_2025.pdf** (ArXiv 2505.22778)
   - Open ML models contain significant supply-chain risks
   - Real attacks: model replacement with malware
   - Training using vulnerable frameworks or poisoned data
   - Restricted data usage violations

8. **SecureMLOps_Survey_2025.pdf** (ArXiv 2506.02032)
   - Surveying attacks, mitigation strategies, research challenges
   - MLOps market projected to grow 43% over next 5 years
   - Pressure to accelerate deployment results in insufficient security
   - **Example**: ShadowRay vulnerability (Sept 2023) - $1 billion data exfiltration

9. **EnhancingSupplyChain_AutoML_2024.pdf** (ArXiv 2406.13166)
   - Automated ML framework to enhance supply chain security
   - Detects fraudulent activities
   - Predicts maintenance needs
   - Forecasts material backorders

**Key Findings on ML Supply Chain**:
- ML/AI Bills of Materials (ML/AIBOMs) necessary to address different inputs, security concerns (model poisoning), and ethical considerations
- OWASP Machine Learning Security Top 10 2023 includes ML06:2023 AI Supply Chain Attacks
- Software supply chain in ML includes more elements than classic software

---

## Validation of Survey Claims

### Survey Claim 1: Supply Chain Vulnerabilities Are Widespread
**VALIDATED**: 
- 64.96% of Maven releases impacted by vulnerabilities
- 84% of codebases contain known open source vulnerabilities
- 74% have high-risk vulnerabilities
- Transitive vulnerabilities nearly 2x direct vulnerabilities

### Survey Claim 2: Automation Gaps Exist in Security Scanning
**VALIDATED**:
- Only 12% of organizations conduct security scans per commit
- Despite 73% leadership prioritization, automation gaps persist
- Current tools often fail to address systemic transitive vulnerabilities

### Survey Claim 3: Secrets and Credentials Are Major Attack Vectors
**VALIDATED**:
- 10 million hardcoded secrets detected in 2022 (67% increase)
- Compromised credentials: 50% of cyberattacks (H1 2023)
- 40% of all hacking breaches from stolen credentials (2024)
- 39+ million secrets on GitHub (2024)

### Survey Claim 4: Container Security Remains Challenging
**VALIDATED**:
- Sys:All Loophole affected 250,000+ production Kubernetes clusters
- Misconfigurations identified as major security threat
- Container security adoption remains low (34%) despite API security (63%) and SCA (62%) adoption

### Survey Claim 5: AI/ML Supply Chain Requires Special Attention
**VALIDATED**:
- Open ML models contain significant supply-chain risks
- Real attacks documented: model replacement, framework vulnerabilities, data poisoning
- License omission rates >70%, error rates >50% on dataset hosting sites
- MLOps market growing 43% with insufficient security attention
- 1212x increase in leaked OpenAI API keys

---

## Critical Production-Ready Tools and Frameworks Identified

### SBOM and SCA Tools:
- Microsoft sbom-tool
- Grype (vulnerability scanning)
- GitHub Secret Scanner
- Gitleaks
- TruffleHog (800+ secret types)

### Container Security:
- Red Hat Advanced Cluster Security (StackRox)
- Sysdig Secure (Falco-based)
- Kubescape
- CNCF Confidential Containers (CoCo)

### ML Provenance and Security:
- Atlas framework (attestable ML pipelines)
- Goblin framework (dependency analysis with Neo4j)
- MLFlow and Weights & Biases (lineage tracking)
- Hugging Face Data Provenance Initiative

### CI/CD Integration Standards:
- NIST SP 800-204D (DevSecOps CI/CD pipelines)
- SLSA framework (supply chain levels)
- STRIDE threat modeling
- OWASP ML Security Top 10

---

## Key Gaps Identified in Current Research and Practice

1. **Transitive Dependency Management**: Current tools fail to systematically address vulnerabilities across entire dependency chains.

2. **SBOM Consumption**: Practitioners lack clear ways to consume and act on generated/received SBOMs.

3. **ML/AI-Specific Standards**: Need for distinct ML/AIBOMs to address unique inputs, security concerns, and ethical considerations.

4. **Automated Provenance Tracking**: Limited tools for comprehensive ML model lineage and training data validation.

5. **Real-Time Threat Detection**: Gap between security tool deployment and effective automation (12% scan per commit).

6. **GenAI Secret Leaks**: Dramatic increase (1212x) in API key leaks requires specialized detection approaches.

7. **Kubernetes Misconfiguration**: Limited research explicitly addressing misconfigurations despite being identified as major threat factor.

---

## Regulatory and Compliance Landscape (2024-2025)

### U.S. Federal Requirements:
- OMB requires federal agencies to comply with SSDF
- SBOM usage reinforced

### European Union:
- Cyber Resilience Act (CRA) became law in 2024
- SBOMs as cornerstone of software security

### Industry Standards:
- NIST SP 800-204D (February 2024)
- S3C2 summits (NSF-backed, ongoing)
- OWASP ML Security Top 10 2023

---

## Research Methodology

### Search Strategy:
- Systematic ArXiv searches for 2024-2025 papers
- Focus on top institutions: Microsoft, Google, Meta, NIST
- Keywords: supply chain security, DevSecOps, CI/CD, container security, secrets detection, ML provenance

### Download Protocol:
- 32 papers downloaded with 3-second delays between requests
- Papers organized into 5 subdirectories by topic
- All papers verified for successful download

### Quality Criteria:
- Production-ready security testing tools and frameworks
- CI/CD integration capabilities
- Automated scanning capabilities
- Peer-reviewed or authoritative sources (ArXiv, NIST, ACM)

---

## Future Research Directions

Based on the collected papers, priority areas for future research include:

1. **Automated Transitive Dependency Analysis**: Tools that systematically trace and validate entire dependency chains
2. **ML Model Provenance Standards**: Standardized formats for ML/AIBOMs and verification protocols
3. **AI-Powered Secrets Detection**: LLM-based approaches for reducing false positives and detecting new secret patterns
4. **Kubernetes Security Automation**: Automated misconfiguration detection and remediation
5. **Real-Time Supply Chain Monitoring**: Continuous validation of supply chain integrity across development lifecycle
6. **GenAI-Specific Security Controls**: Specialized tools for API key management and LLM-related secrets

---

## References and Sources

All papers are sourced from ArXiv.org (https://arxiv.org) and are freely available under open access licenses.

Full bibliography with ArXiv IDs available in individual paper filenames.

---

**Report Generated**: December 10, 2025  
**Research Conducted By**: AI-assisted systematic literature review  
**Repository**: /Users/tamnguyen/Documents/GitHub/ksi_watch/KSI-CMT-03_25-12A_AutomatedTestingandValidation/references/
