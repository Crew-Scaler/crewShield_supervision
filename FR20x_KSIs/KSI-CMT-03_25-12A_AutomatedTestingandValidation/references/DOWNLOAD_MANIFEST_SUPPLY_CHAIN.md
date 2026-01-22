# Supply Chain Testing & Security Validation - Download Manifest

**Download Date**: December 10, 2025  
**Total Papers**: 32 papers  
**Total Size**: ~38MB (new papers only)  
**Repository**: /Users/tamnguyen/Documents/GitHub/ksi_watch/KSI-CMT-03_25-12A_AutomatedTestingandValidation/references/

---

## Download Summary by Category

### 1. Supply Chain Security Testing (10 papers)
| Filename | ArXiv ID | Size | Year |
|----------|----------|------|------|
| SBOMproof_2024.pdf | 2510.05798 | 818K | 2024 |
| SecVul_AutonomousVehicles_2024.pdf | 2509.16899 | 1.6M | 2024 |
| SoK_SupplyChainSecurity_2024.pdf | 2406.10109 | 641K | 2024 |
| DevSecOps_SMEs_2025.pdf | 2503.22612 | 326K | 2025 |
| AI_DevSecOps_2024.pdf | 2504.19154 | 1.8M | 2024 |
| STRIDE_ThreatModeling_CICD_2025.pdf | 2506.06478 | 1.5M | 2025 |
| S3C2_Industry_Summit_2025-03.pdf | 2510.24920 | 413K | 2025 |
| S3C2_Industry_Summit_2024-09.pdf | 2505.10538 | 431K | 2024 |
| S3C2_Government_Summit_2024-08.pdf | 2504.00924 | 421K | 2024 |
| S3C2_Industry_Summit_2024-03.pdf | 2405.08762 | 388K | 2024 |

**Subtotal**: 10 papers, ~8.3MB

### 2. Dependency Vulnerability Testing (4 papers)
| Filename | ArXiv ID | Size | Year |
|----------|----------|------|------|
| Maven_DependencyRisks_2025.pdf | 2503.22134 | 899K | 2025 |
| Maven_CVE_Lifecycle_2025.pdf | 2502.04621 | 236K | 2025 |
| Maven_IndependentArtifacts_2024.pdf | 2504.12261 | 156K | 2024 |
| DependencyPractices_VulnMitigation_2023.pdf | 2310.07847 | 716K | 2023 |

**Subtotal**: 4 papers, ~2MB

### 3. Container and Infrastructure Security (5 papers)
| Filename | ArXiv ID | Size | Year |
|----------|----------|------|------|
| Kubernetes_NetworkMisconfig_2025.pdf | 2506.21134 | 1.8M | 2025 |
| Kubernetes_SecurityLandscape_AI_2024.pdf | 2409.04647 | 632K | 2024 |
| TrustedContainers_ConfidentialComputing_2022.pdf | 2205.05747 | 331K | 2022 |
| ProofOfCloud_DataCenter_TEE_2024.pdf | 2510.12469 | 1.2M | 2024 |
| KubeFence_SecurityHardening_2024.pdf | 2504.11126 | 5.6M | 2024 |

**Subtotal**: 5 papers, ~9.5MB

### 4. Secrets and Credential Scanning (4 papers)
| Filename | ArXiv ID | Size | Year |
|----------|----------|------|------|
| HardCodedCredentials_LLM_2025.pdf | 2506.13090 | 1.2M | 2025 |
| SecretBreach_SourceCode_LLM_2024.pdf | 2504.18784 | 802K | 2024 |
| TalesFromGit_SecretsDetection_2023.pdf | 2307.00892 | 451K | 2023 |
| ComparativeStudy_SecretsTools_2023.pdf | 2307.00714 | 610K | 2023 |

**Subtotal**: 4 papers, ~3MB

### 5. Model Provenance and Lineage Testing (9 papers)
| Filename | ArXiv ID | Size | Year |
|----------|----------|------|------|
| ModelProvenanceTesting_LLM_2025.pdf | 2502.00706 | 2.3M | 2025 |
| ProvenanceTracking_MLSystems_2025.pdf | 2507.01075 | 1.0M | 2025 |
| Atlas_MLLifecycle_Provenance_2025.pdf | 2502.19567 | 2.6M | 2025 |
| Blockchain_AI_Copyright_Provenance_2024.pdf | 2404.06077 | 1.7M | 2024 |
| DataProvenance_AI_2024.pdf | 2404.12691 | 380K | 2024 |
| MLSupplyChain_HuggingFace_2025.pdf | 2502.04484 | 1.3M | 2025 |
| MLModels_SupplyChainProblem_2025.pdf | 2505.22778 | 560K | 2025 |
| SecureMLOps_Survey_2025.pdf | 2506.02032 | 908K | 2025 |
| EnhancingSupplyChain_AutoML_2024.pdf | 2406.13166 | 2.1M | 2024 |

**Subtotal**: 9 papers, ~12.8MB

---

## Download Statistics

### By Year
- 2025: 13 papers (40.6%)
- 2024: 16 papers (50.0%)
- 2023: 2 papers (6.25%)
- 2022: 1 paper (3.1%)

### By Institution/Source
- ArXiv preprints: 32 papers
- NSF-backed (S3C2): 4 papers
- NIST-related: Multiple references

### By Research Area Focus
- DevSecOps/CI/CD: 8 papers
- Vulnerability Analysis: 7 papers
- ML/AI Security: 9 papers
- Container/Kubernetes: 5 papers
- Secrets Detection: 4 papers

---

## Download Method

All papers were downloaded using curl with the following protocol:
- 3-second delays between requests to respect server limits
- Direct PDF downloads from arxiv.org
- Verification of successful downloads
- Organization into topic-based subdirectories

Example command:
```bash
curl -L -o "filename.pdf" "https://arxiv.org/pdf/ARXIV_ID" && sleep 3
```

---

## File Organization

```
KSI-CMT-03_25-12A_AutomatedTestingandValidation/references/
├── supply_chain_security/       (10 papers)
├── dependency_scanning/         (4 papers)
├── container_security/          (5 papers)
├── secrets_detection/          (4 papers)
├── model_provenance/           (9 papers)
├── RESEARCH_SUMMARY.md         (Comprehensive analysis)
├── INDEX.md                    (Quick navigation)
├── SUPPLY_CHAIN_VALIDATION.md  (Survey validation)
└── DOWNLOAD_MANIFEST_SUPPLY_CHAIN.md (This file)
```

---

## Key Papers by Priority

### CRITICAL (Must Read Immediately)
1. SBOMproof_2024.pdf - SBOM compliance validation
2. Maven_DependencyRisks_2025.pdf - 65% vulnerability rate
3. SecretBreach_SourceCode_LLM_2024.pdf - 10M secrets, 67% increase
4. Kubernetes_SecurityLandscape_AI_2024.pdf - 250K clusters affected
5. ModelProvenanceTesting_LLM_2025.pdf - Model derivation testing

### HIGH PRIORITY
6. STRIDE_ThreatModeling_CICD_2025.pdf - CI/CD threat modeling
7. DevSecOps_SMEs_2025.pdf - 12% scan rate problem
8. SecureMLOps_Survey_2025.pdf - 43% market growth
9. Atlas_MLLifecycle_Provenance_2025.pdf - Attestable pipelines
10. Kubernetes_NetworkMisconfig_2025.pdf - Misconfiguration defense

---

## Research Coverage

### Topics Comprehensively Covered
- SBOM generation and compliance
- Dependency vulnerability analysis (Maven ecosystem)
- Secrets detection methodologies
- Kubernetes security landscape
- ML model provenance challenges

### Topics Partially Covered
- Container runtime security (TEE focus)
- Automated remediation approaches
- Supply chain risk quantification
- Zero-trust architectures

### Gaps Identified for Future Research
- Real-time supply chain monitoring tools
- Standardized ML/AIBOM formats
- Transitive dependency graph analysis
- GenAI-specific security controls
- Automated misconfiguration remediation

---

## Verification Checksums (Optional)

To verify download integrity, use:
```bash
md5 /path/to/paper.pdf
```

All papers downloaded directly from arxiv.org are considered authentic sources.

---

## Usage Recommendations

### For Survey Validation
- Start with RESEARCH_SUMMARY.md for comprehensive overview
- Use SUPPLY_CHAIN_VALIDATION.md for specific claim verification
- Reference INDEX.md for quick paper lookup

### For Technical Implementation
- Review S3C2 Summit reports for industry insights
- Study tool comparison papers for selection criteria
- Analyze methodology papers for implementation patterns

### For Academic Research
- Use as baseline for literature review
- Identify research gaps from summary documents
- Cross-reference ArXiv IDs for citation

---

## Related Resources

### NIST Publications
- SP 800-204D: Strategies for Integration of SSC Security in DevSecOps CI/CD Pipelines (February 2024)
- Available at: https://csrc.nist.gov/pubs/sp/800/204/d/final

### Industry Standards
- OWASP ML Security Top 10 (2023)
- SLSA Framework (supply chain levels)
- CycloneDX/SPDX SBOM formats

### Tools Referenced
- Microsoft sbom-tool, Grype, Gitleaks, TruffleHog
- Red Hat ACS, Sysdig Secure, Kubescape
- Atlas, MLFlow, Weights & Biases

---

## Update History

- **December 10, 2025**: Initial download of 32 papers
  - 10 supply chain security papers
  - 4 dependency scanning papers
  - 5 container security papers
  - 4 secrets detection papers
  - 9 model provenance papers

---

## Contact and Contributions

Repository maintained as part of ksi_watch project.

For questions or additions, refer to main repository documentation.

---

**Manifest Version**: 1.0  
**Last Updated**: December 10, 2025  
**Status**: COMPLETE
