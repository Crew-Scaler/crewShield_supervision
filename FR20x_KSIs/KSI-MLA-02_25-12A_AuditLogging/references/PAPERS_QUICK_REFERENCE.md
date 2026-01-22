# Quick Reference: Issue #74 ArXiv Papers

## Papers by Topic

### BIAS IN AI-DRIVEN LOG ANOMALY DETECTION (8 papers)

| ArXiv ID | Title | Date | Pages | Key Metric |
|----------|-------|------|-------|------------|
| 2501.11638 | Class Imbalance in Anomaly Detection | Jan 2025 | 30 | Optimal training imbalance ≠ 50% |
| 2503.13195 | Deep Learning Anomaly Detection Survey | Mar 2025 | 24 | 180+ studies reviewed |
| 2505.04204 | Cyber Security ML on Imbalanced Datasets | May 2025 | 13 | Imbalance techniques can hurt performance |
| 2503.03022 | NetGuard: Generative Active Adaptation | Mar 2025 | 13 | F1: 0.60→0.86, rare attacks 300x better |
| 2505.14027 | CSAGC-IDS: Dual-Module DL IDS | May 2025 | 20 | 91.09% accuracy (binary) |
| 2409.10951 | Fair Anomaly Detection for Imbalanced Groups | Sep 2024 | 19 | Fairness-aware contrastive learning |
| 2510.26046 | Bias-Corrected Data Synthesis | Oct 2025 | 41 | Corrects synthetic data bias |
| 2512.07030 | Zero-Day Attack Detection | Dec 2025 | 13 | XGBoost best for speed+accuracy |

### LOG INJECTION / DATA POISONING (4 papers)

| ArXiv ID | Title | Date | Pages | Key Metric |
|----------|-------|------|-------|------------|
| 2512.03462 | Malicious URL Classification | Nov 2025 | 14 | Real-time hybrid framework |
| 2401.00286 | Autonomous Threat Hunting | Dec 2023 | 79 | Comprehensive 79-page review |
| 2502.02337 | RAM: SIEM Rules to TTPs Mapper | Feb 2025 | 13 | LLM-based, GPT-4 best |
| 2407.14945 | CNN-BiLSTM Intrusion Detection | Jul 2024 | 6 | Chi-square feature selection |

### MULTI-TENANT SECURITY / SIEM (2 papers)

| ArXiv ID | Title | Date | Pages | Key Metric |
|----------|-------|------|-------|------------|
| 2503.02065 | XAI in AI-Driven SOCs | Mar 2025 | - | 248 survey + 24 interviews |
| 2408.03335 | XAI-based IDS for Industry 5.0 | Jul 2024 | 57 | Adversarial XIDS framework |

## Top Papers by Relevance

### MUST-READ (Highest Impact for Issue #74):

1. **2503.03022** - NetGuard (NYU) - Only US institution paper, quantified metrics
2. **2501.11638** - Class Imbalance - Theoretical framework for optimal sampling
3. **2505.04204** - Cyber Security ML - WARNING: Techniques can hurt performance
4. **2502.02337** - SIEM Rules Mapper - Direct SIEM application

### HIGH-VALUE (Strong Supporting Evidence):

5. **2503.13195** - DL Survey - Comprehensive overview
6. **2512.07030** - Zero-Day Detection - Realistic testing methodology
7. **2409.10951** - Fair Anomaly Detection - Fairness guarantees
8. **2408.03335** - Industry 5.0 XAI - Bias detection focus

### SUPPLEMENTARY (Additional Context):

9. **2510.26046** - Bias-Corrected Synthesis - Mathematical rigor
10. **2505.14027** - CSAGC-IDS - Interpretability with SHAP/LIME
11. **2401.00286** - Threat Hunting - Comprehensive review
12. **2503.02065** - SOC Analyst Study - Human factors
13. **2512.03462** - Malicious URLs - Injection vectors
14. **2407.14945** - IoT IDS - Resource constraints (6 pages only)

## Key Quantified Findings

### Detection Performance Impact:
- **Rare attack detection improvement:** 12.5x to 300x with proper imbalance handling
- **Overall F1-score improvement:** 0.60 → 0.86 (43% gain)
- **Specific attacks:**
  - Infiltration: 0.001 → 0.30
  - Web attacks: 0.04 → 0.50
  - FTP-BruteForce: 0.00 → 0.71

### Class Imbalance Ratios Studied:
- Common ratio: 1000:100 (10:1 majority:minority)
- Extreme cases: 1000:1 in some datasets
- Optimal training ratio: Problem-dependent, NOT 50:50

### Model Performance (NSL-KDD):
- 5-class classification: 84.55% accuracy
- Binary classification: 91.09% accuracy
- Cost-sensitive + attention: Best approach

## Coverage Gaps

### Topics with NO direct ArXiv papers (2024-2025):
1. Multi-tenant log isolation failures in CSP environments
2. Cross-tenant data leakage via shared logging infrastructure
3. Traditional log injection attacks (Log4Shell-style)
4. Log forging and audit trail corruption
5. Incident response creating mandatory cross-tenant visibility

### Why gaps exist:
- ArXiv focuses on algorithmic contributions > operational security
- Multi-tenant infrastructure security is proprietary/NDA-protected
- Traditional injection considered "solved" (input validation)
- Recent shift to LLM security (prompt injection) over log injection

### Recommended additional sources:
- IEEE Xplore: Multi-tenant cloud security
- ACM DL: SIEM papers (CCS, RAID, ACSAC)
- USENIX Security: System-level multi-tenancy
- OWASP: Log injection guidance
- NIST SP 800-92: Log management

## US Institution Coverage

Only 1 of 14 papers (7%) has first author from top US institution:
- **2503.03022** - University of Illinois Urbana-Champaign + NYU (US)

All other papers: International authorship (France, China, Morocco, Israel, etc.)

## File Locations

**Papers:** `/Users/tamnguyen/Documents/GitHub/ksi_watch/KSI-MLA-02_25-12A_AuditLogging/references/{arxiv_id}_{title}.pdf`

**Reports:**
- Full report: `ISSUE_74_ARXIV_PAPERS_REPORT.md`
- This quick reference: `PAPERS_QUICK_REFERENCE.md`
- Metadata: `metadata_report.txt`

**Total downloaded:** 14 papers, ~33.1 MB
