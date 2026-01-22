# Topic 12 Supply Chain Security - Quick Index

## Quick Reference

**Research Complete**: December 25, 2025
**Papers Downloaded**: 10 (Primary)
**Papers Archived**: 5 (Secondary)
**Total Size**: ~16.2 MB
**Location**: `/Users/tamnguyen/Documents/GitHub/ksi_watch/KSI-SVC-04_25-12A_ConfigurationAutomation/references/topic12_supply_chain_templates/`

---

## Essential Documents

1. **RESEARCH_SUMMARY.md** - Start here for comprehensive findings
2. **COMPLETION_REPORT.md** - Verification and delivery details
3. **metadata.json** - Complete paper tracking (machine-readable)
4. **INDEX.md** - This file

---

## Top 3 Most Critical Papers

### 1. Characterizing Build Compromises (2511.01395) - 2025
- **Why**: First systematic taxonomy of build-specific attacks
- **Impact**: Shows 23.8% of supply chain attacks target build phase
- **For Topic**: Directly relevant to configuration template security
- **Key Finding**: Dependency confusion & build script injection most common

### 2. Wolves in Repository (2504.17473) - 2024
- **Why**: Detailed analysis of XZ Utils backdoor (CVE-2024-3094)
- **Impact**: Demonstrates process-level supply chain manipulation
- **For Topic**: Shows how configuration and processes weaponized over 2+ years
- **Key Finding**: Social engineering + CI/CD configuration as effective as code injection

### 3. Granite: GitHub Actions Permissions (2512.11602) - 2025
- **Why**: First step-level permission enforcement in CI/CD
- **Impact**: Can protect 52.7% of workflows from permission escalation
- **For Topic**: Directly addresses CI/CD configuration security
- **Key Finding**: 55% performance overhead acceptable for security gains

---

## Papers by Category

### Build System Security (3 papers)
- 2511.01395 - Build compromise taxonomy
- 2511.17070 - TICAL trusted compilation
- 2509.23970 - Binary diff for malware detection

### CI/CD Configuration Security (2 papers)
- 2512.11602 - Granite (GitHub Actions)
- 2504.14760 - Zero Trust workload identity

### Package/Dependency Security (3 papers)
- 2512.04338 - Robust malicious package detection
- 2512.12559 - Malicious logic taxonomy
- 2411.11017 - Linux distribution malware prevention [archived]

### Supply Chain Attack Case Studies (2 papers)
- 2511.00140 - ROS 2 supply chain exploitation
- 2504.17473 - XZ Utils detailed analysis

### Cross-Domain Applications (2 papers)
- 2509.16899 - AV supply chain vulnerabilities
- 2409.09368 - Model hub poisoning [archived]

---

## Key Statistics

### Year Distribution
- 2025: 7 papers (70%)
- 2024: 3 papers (30%)

### Paper Sizes
- Largest: 4.56 MB (ROS 2 attack)
- Smallest: 0.36 MB (Malicious logic)
- Average: 1.53 MB

### Institutions Represented
- TU Delft & Endor Labs (2 papers)
- MIT/CMU/Stanford affiliations (multiple)
- Google, Microsoft, Amazon (industry)
- NSF S3C2 Center (government)

---

## Main Findings

### Evolution of Attacks
1. **2024**: Code-focused, signature-based poisoning
2. **2025**: Process-focused, configuration manipulation, social engineering

### Attack Vectors Ranked by Prevalence
1. **Build Injection** (23.8% of documented attacks)
2. **Package Poisoning** (346 found in 37 days on PyPI)
3. **CI/CD Misconfiguration** (Permission issues in 52.7% of jobs)
4. **Dependency Chains** (Vulnerabilities persist >1 year average)

### Emerging Defenses
1. **Trusted Compilation** - Build pipeline integrity
2. **Granular Permission** - Step-level CI/CD control
3. **Behavioral Detection** - Multi-stage malware identification
4. **Workload Identity** - Non-human actor authentication

---

## How to Use These Papers

### For Security Architecture
Start with: 2504.14760 (SPIFFE) → 2512.11602 (Granite) → 2511.17070 (TICAL)

### For Threat Intelligence
Start with: 2504.17473 (XZ) → 2511.01395 (Taxonomy) → 2511.00140 (ROS)

### For Detection/Response
Start with: 2512.04338 (Detection) → 2512.12559 (Taxonomy) → 2509.23970 (Validation)

### For Policy/Governance
Start with: 2505.10538 (Industry Summit) → 2504.00924 (Gov Summit) → 2504.14760 (Standards)

---

## Research Methodology Notes

- **Source**: ArXiv Computer Security (cs.CR)
- **Timeframe**: 2024-2025 (prioritized 2025)
- **Total Searches**: 5 major queries + specialized variants
- **Total Papers Found**: 500+
- **Selection Ratio**: 10/500 (top 2%)
- **Rate Limiting**: Respected 3+ second delays per ArXiv policy

---

## Known Limitations & Gaps

### Topic-Specific Gaps
- **Terraform Security**: <1% of papers explicitly mention Terraform
- **Helm Security**: <1% explicitly mention Helm
- **IaC Poisoning**: Limited research on infrastructure code poisoning

### Temporal Gaps
- Most recent threats (late 2025) may not be published yet on ArXiv
- Some industry reports not in academic repositories

### Scope Gaps
- Configuration verification during deployment (runtime) - limited coverage
- Cross-cloud configuration security - not extensively studied
- Configuration drifting detection - emerging area

---

## Next Steps

### If You Need More Papers
1. Check _archived_low_relevance/ (5 papers with lower specificity)
2. Review metadata.json for additional paper details
3. Consider specialist databases (IEEE Xplore, ACM DL) for proprietary tools

### If You Need Implementation Guidance
1. Read RESEARCH_SUMMARY.md "Practical Applications" section
2. Review individual paper abstracts in metadata.json
3. Cross-reference with your infrastructure stack (Terraform, Kubernetes, etc.)

### If You Need Citation Information
1. Each filename contains ArXiv ID (YYMM.NNNNN format)
2. metadata.json includes DOI where available
3. RESEARCH_SUMMARY.md lists publication venues

---

## Contact/Updates

**Last Updated**: December 25, 2025
**Next Recommended Review**: March 2026 (new quarterly research)
**Archive Location**: `/Users/tamnguyen/Documents/GitHub/ksi_watch/KSI-SVC-04_25-12A_ConfigurationAutomation/references/topic12_supply_chain_templates/`

---

## Quick File Navigation

```
topic12_supply_chain_templates/
├── [START HERE] ➡ RESEARCH_SUMMARY.md (comprehensive analysis)
├── [VERIFY] ➡ COMPLETION_REPORT.md (delivery checklist)
├── [REFERENCE] ➡ INDEX.md (this file)
├── [DATA] ➡ metadata.json (structured data)
│
├── [PAPERS] Downloaded 10 Primary Papers:
│   ├── 2025_2511.01395_characterizing_build_compromises.pdf
│   ├── 2025_2511.00140_supply_chain_exploitation_ros.pdf
│   ├── 2025_2512.04338_robust_malicious_packages_detector.pdf
│   ├── 2025_2512.12559_unveiling_malicious_logic_python.pdf
│   ├── 2025_2512.11602_granite_github_actions_permissions.pdf
│   ├── 2025_2509.16899_supply_chain_autonomous_vehicles.pdf
│   ├── 2024_2504.17473_wolves_in_repository_xz_utils.pdf
│   ├── 2024_2504.14760_workload_identity_zero_trust_cicd.pdf
│   ├── 2024_2511.17070_tical_trusted_compilation.pdf
│   └── 2025_2509.23970_binary_diff_summarization_llm.pdf
│
└── _archived_low_relevance/ (5 Secondary Papers)
    ├── 2024_2411.11017_malware_prevention_linux_distributions.pdf
    ├── 2024_2409.09368_models_are_codes_malicious_code_poisoning.pdf
    ├── 2025_2505.21642_reproducible_builds_arch_linux.pdf
    ├── 2025_2505.10538_s3c2_summit_2024_09_industry_supply_chain.pdf
    └── 2025_2504.00924_s3c2_summit_2024_08_government_supply_chain.pdf
```

---

**Ready for Integration** ✓
