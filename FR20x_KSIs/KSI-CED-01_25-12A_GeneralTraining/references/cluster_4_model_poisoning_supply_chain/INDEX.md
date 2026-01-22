# Cluster 4 Research Index
## Model Poisoning & AI Supply Chain Integrity

**Location**: `/Users/tamnguyen/Documents/GitHub/ksi_watch/KSI-CED-01_25-12A_GeneralTraining/references/cluster_4_model_poisoning_supply_chain/`

---

## Documents in This Directory

### 1. **README.md** - Comprehensive Research Report
- Executive summary of cluster focus
- 20 papers organized by category
- Quantitative findings and threat analysis
- Research gaps and future directions
- CSP compliance recommendations
- **Start here for full context**

### 2. **QUICK_REFERENCE.md** - One-Page Guide
- What is model poisoning
- Key attack vectors explained
- Success rate metrics table
- Architecture-specific threats
- Reading priority guide
- Risk assessment checklist
- **Start here for quick understanding**

### 3. **cluster_4_metadata.csv** - Paper Database
- 20 papers with full metadata
- ArXiv ID, title, authors, date
- Category, relevance score
- Key findings summary
- Direct download URLs
- **Use for reference/spreadsheet view**

### 4. **PAPERS_LIST.txt** - Organized Bibliography
- 20 papers grouped by priority level
- Direct links to ArXiv abstract and PDF
- Key findings for each paper
- **Use for quick paper lookup**

### 5. **INDEX.md** - This File
- Directory guide and navigation

---

## Quick Start

### For Security Compliance Training
1. Read: QUICK_REFERENCE.md (15 min)
2. Review: README.md executive summary (15 min)
3. Check: Risk assessment for your org
4. Action: Implement suggested controls

### For Researchers
1. Read: README.md (full document, 30 min)
2. Sort: cluster_4_metadata.csv by your interest area
3. Identify: 3-5 papers in PAPERS_LIST.txt to read first
4. Download: Papers via arxiv.org links

### For Security Teams
1. Review: Architecture-specific sections in QUICK_REFERENCE.md
2. Check: Quantitative threat metrics table
3. Assess: Controls needed for your organization
4. Read: Landmark papers (2401.05566, 2501.17433, 2510.05159)

---

## Paper Statistics

| Metric | Value |
|--------|-------|
| Total Papers | 20 |
| Average Relevance | 8.3/10 |
| 2025 Papers | 10 (50%) |
| 2024 Papers | 8 (40%) |
| 2020-2023 Papers | 2 (10%) |
| Landmark Papers | 1 (Sleeper Agents) |
| High-Priority (9+) | 6 |

## Paper Categories

- **Fine-tuning Attacks**: 2 papers
- **Supply Chain Security**: 2 papers
- **Backdoor Attacks (Diffusion/Vision)**: 5 papers
- **Backdoor Attacks (Specialized)**: 3 papers
- **Backdoor Attacks (Multi-modal/TS)**: 2 papers
- **Model Poisoning (Federated)**: 1 paper
- **Deceptive Training & Detection**: 3 papers
- **Related Work**: 2 papers

---

## Key Findings Summary

### Highest Impact Threats
1. **Sleeper Agents (10/10)** - Deceptive backdoors persist through safety training
2. **Fine-tuning Attacks (9/10)** - Safety guardrails bypassable with <100 samples
3. **Diffusion Poisoning (9/10)** - >90% success with 10 carefully chosen samples
4. **Supply Chain Backdoors (9/10)** - AI agent supply chain has multiple attack vectors

### Quantitative Red Flags
- **100% attack success** on MoE with only 2% poisoning ratio
- **98% success** on vision-language models via semantic manipulation
- **92.5% detection accuracy** represents best-in-class (vs. many vulnerable systems)
- **94.3% detection rate** for federated learning with <1.2% false positives

### Architectural Vulnerabilities Ranked
1. **Mixture of Experts** - Easiest to poison (100% ASR at 2%)
2. **Vision-Language Models** - High success (98% at <5%)
3. **Diffusion Models** - Low sample requirements (90% at 10 samples)
4. **LLMs** - Deceptive backdoors escape all testing
5. **Federated Learning** - Multi-round poisoning breaks state-of-the-art

---

## ArXiv Access

All papers are freely available on ArXiv:

**Format**: https://arxiv.org/pdf/{ARXIV_ID}.pdf

**Example**: 
- Abstract: https://arxiv.org/abs/2401.05566
- PDF: https://arxiv.org/pdf/2401.05566.pdf

See PAPERS_LIST.txt for all 20 links.

---

## How to Use This Collection

### As Training Material
- Managers: Read QUICK_REFERENCE.md
- Engineers: Read README.md + select papers from metadata
- Security Team: Focus on threat metrics and detection sections

### As Research Reference
- Researchers: Use cluster_4_metadata.csv to find papers by topic
- Students: QUICK_REFERENCE.md provides context for any paper
- Authors: Identify gaps and opportunities from README.md sections

### As Compliance Documentation
- Auditors: README.md section on "CSP Compliance Recommendations"
- CISOs: QUICK_REFERENCE.md section on "Risk Assessment"
- Incident Responders: Attack vector descriptions for threat hunting

---

## Search Tips

### Find papers on specific topics:
- **Fine-tuning attacks**: Papers 2-3, 15-16
- **Supply chain**: Papers 4, 7, 16
- **Backdoors on LLMs**: Papers 1-3, 6, 11, 15
- **Diffusion models**: Papers 9, 10
- **Vision-language models**: Papers 14, 17
- **Detection methods**: Papers 15, 18
- **Federated learning**: Paper 6

### Find papers by threat severity:
- **Maximum risk (10/10)**: Paper 1
- **Critical (9/10)**: Papers 2-6
- **Important (8/10)**: Papers 7-16
- **Supporting (7/10)**: Papers 17-20

---

## Document Maintenance

**Created**: 2026-01-06
**Last Updated**: 2026-01-06
**Format Version**: 1.0
**Collection Method**: ArXiv search with WebSearch tool
**Methodology**: Keyword-based search for poisoning, backdoor, supply chain threats
**Quality Gate**: All papers published 2020-2025, emphasis on 2024-2025

---

## Issues & Updates

If you find:
- **Broken links**: Check if ArXiv paper moved or removed
- **Missing papers**: See cluster_4_metadata.csv for complete list
- **Need newer papers**: Re-run ArXiv search with current year
- **Questions on findings**: Refer to README.md analysis sections

---

## Related Clusters in Issue #81

- **Cluster 1**: Prompt Injection & LLM Jailbreaks
- **Cluster 2**: Data Poisoning Detection & Mitigation  
- **Cluster 3**: Multi-Agent Security Attacks
- **Cluster 5**: Model Extraction & IP Theft

---

## Navigation

```
Start Here (Pick One Path):
  
  Path A: Quick Training (30 min)
    → QUICK_REFERENCE.md
    → README.md (executive summary)
    → Skip rest

  Path B: Research Focus (2-3 hours)
    → README.md (full)
    → cluster_4_metadata.csv
    → Select and read 3-5 papers

  Path C: Security Audit (1-2 hours)
    → QUICK_REFERENCE.md
    → Risk assessment section
    → Implement controls checklist

  Path D: Deep Analysis (4+ hours)
    → README.md
    → All papers marked 8+ relevance
    → cluster_4_metadata.csv analysis
```

---

*For Issue #81: KSI-CED-01_25-12A_GeneralTraining*
*Cluster 4 Research Collection - Complete*
