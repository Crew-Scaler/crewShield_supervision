# Cluster 1: Agentic AI Systems & Vulnerability Management
## Paper Download Index

**Generated:** January 5, 2026
**Total Papers:** 16
**All papers published 2024-2026**
**Average Relevance Score:** 8.6/10

---

## Quick Download Links

All papers are directly available from ArXiv at these URLs:

### Tier 1 - Critical Papers (9-10/10 Relevance)

| ArXiv ID | Title | Pages | Published | Relevance | PDF URL |
|----------|-------|-------|-----------|-----------|---------|
| 2601.00205 | Understanding Security Risks of AI Agents' Dependency Updates | 5 | 2026-01 | 10/10 | [PDF](https://arxiv.org/pdf/2601.00205) |
| 2512.23480 | Agentic AI for Autonomous Defense in Software Supply Chain Security | 10 | 2025-12 | 9/10 | [PDF](https://arxiv.org/pdf/2512.23480) |
| 2510.23883 | Agentic AI Security: Threats, Defenses, Evaluation, and Open Challenges | ? | 2025-10 | 9/10 | [PDF](https://arxiv.org/pdf/2510.23883) |
| 2510.06445 | A Survey on Agentic Security: Applications, Threats and Defenses | ? | 2025-10 | 9/10 | [PDF](https://arxiv.org/pdf/2510.06445) |
| 2506.04133 | TRiSM for Agentic AI: Trust, Risk, and Security Management | ? | 2025-06 | 9/10 | [PDF](https://arxiv.org/pdf/2506.04133) |
| 2508.10043 | Securing Agentic AI: Threat Modeling and Risk Analysis | ? | 2025-08 | 9/10 | [PDF](https://arxiv.org/pdf/2508.10043) |
| 2511.21990 | A Safety and Security Framework for Real-World Agentic Systems | ? | 2025-11 | 9/10 | [PDF](https://arxiv.org/pdf/2511.21990) |
| 2410.21218 | Lifting the Veil on LLM Supply Chain Composition, Risks, Mitigations | 26 | 2024-10 | 9/10 | [PDF](https://arxiv.org/pdf/2410.21218) |
| 2503.12188 | Multi-Agent Systems Execute Arbitrary Malicious Code | 33 | 2025-03 | 9/10 | [PDF](https://arxiv.org/pdf/2503.12188) |

### Tier 2 - Strong Supporting Papers (8/10 Relevance)

| ArXiv ID | Title | Pages | Published | Relevance | PDF URL |
|----------|-------|-------|-----------|-----------|---------|
| 2508.16481 | Benchmarking the Robustness of Agentic Systems to Adversarially-Induced Harms | 54 | 2025-08 | 8/10 | [PDF](https://arxiv.org/pdf/2508.16481) |
| 2504.19956 | Securing Agentic AI: Comprehensive Threat Model and Mitigation Framework | 12 | 2025-04 | 8/10 | [PDF](https://arxiv.org/pdf/2504.19956) |
| 2510.00317 | MAVUL: Multi-Agent Vulnerability Detection | ? | 2025-09 | 8/10 | [PDF](https://arxiv.org/pdf/2510.00317) |
| 2505.12786 | Forewarned is Forearmed: LLM Agents in Autonomous Cyberattacks | ? | 2025-05 | 8/10 | [PDF](https://arxiv.org/pdf/2505.12786) |
| 2512.18043 | Securing Agentic AI Systems: A Multilayer Security Framework | 6 | 2025-12 | 8/10 | [PDF](https://arxiv.org/pdf/2512.18043) |
| 2502.07049 | LLMs in Software Security: Vulnerability Detection Techniques Survey | 33 | 2025-02 | 8/10 | [PDF](https://arxiv.org/pdf/2502.07049) |

### Tier 3 - Foundational Paper (7/10 Relevance)

| ArXiv ID | Title | Pages | Published | Relevance | PDF URL |
|----------|-------|-------|-----------|-----------|---------|
| 2411.10184 | Agentic LLMs in Supply Chain: Autonomous Multi-Agent Consensus | ? | 2024-11 | 7/10 | [PDF](https://arxiv.org/pdf/2411.10184) |

---

## ArXiv Direct Access

### Abstract Pages (with full metadata)
All papers have abstract pages on ArXiv:
- Replace `/pdf/` with `/abs/` in the URL above
- Example: `https://arxiv.org/abs/2601.00205`

### HTML Versions (Experimental)
Many papers available in HTML at:
- `https://arxiv.org/html/{arxiv_id}v{version}`
- Example: `https://arxiv.org/html/2601.00205v1`

### Source Code
LaTeX source available at:
- `https://arxiv.org/src/{arxiv_id}`

---

## Bulk Download Instructions

### Using wget (Linux/macOS)
```bash
cd /Users/tamnguyen/Documents/GitHub/ksi_watch/KSI-TPR-04_25-12A_SupplyChainRiskMonitoring/references/cluster_1_agentic_systems

# Download all papers
for arxiv in 2601.00205 2512.23480 2510.23883 2510.06445 2506.04133 2508.10043 2511.21990 2410.21218 2503.12188 2508.16481 2504.19956 2510.00317 2505.12786 2512.18043 2502.07049 2411.10184; do
  wget https://arxiv.org/pdf/$arxiv -O ${arxiv}.pdf
  sleep 3  # Respect ArXiv rate limits
done
```

### Using curl (Universal)
```bash
cd /Users/tamnguyen/Documents/GitHub/ksi_watch/KSI-TPR-04_25-12A_SupplyChainRiskMonitoring/references/cluster_1_agentic_systems

for arxiv in 2601.00205 2512.23480 2510.23883 2510.06445 2506.04133 2508.10043 2511.21990 2410.21218 2503.12188 2508.16481 2504.19956 2510.00317 2505.12786 2512.18043 2502.07049 2411.10184; do
  curl -L https://arxiv.org/pdf/$arxiv -o ${arxiv}.pdf
  sleep 3
done
```

### Using Python
```python
import urllib.request
import time

arxiv_ids = [
    "2601.00205", "2512.23480", "2510.23883", "2510.06445", "2506.04133",
    "2508.10043", "2511.21990", "2410.21218", "2503.12188", "2508.16481",
    "2504.19956", "2510.00317", "2505.12786", "2512.18043", "2502.07049", "2411.10184"
]

for arxiv_id in arxiv_ids:
    pdf_url = f"https://arxiv.org/pdf/{arxiv_id}"
    urllib.request.urlretrieve(pdf_url, f"{arxiv_id}.pdf")
    time.sleep(3.5)
```

---

## Search Strategy Used

The following ArXiv search queries were executed:

1. `autonomous agents software supply chain vulnerability`
2. `AI agents dependency management security`
3. `agentic systems vulnerability monitoring`
4. `agent-based vulnerability detection`
5. `LLM agents software composition`
6. `autonomous agents third-party risks`

**Search Results:** 50+ papers evaluated
**Papers Accepted:** 16 papers (32% acceptance rate)

---

## Selection Criteria Applied

Papers were selected based on:

- **Publication Date:** 2024-2026 (prioritize 2025)
- **Minimum Length:** Most papers 6+ pages (range 5-54 pages)
- **Abstract Keywords:** Must mention BOTH agent/autonomous AND security/vulnerability
- **Relevance Score:** 7+/10 minimum
- **Quality Threshold:** Only papers with clear research contributions

---

## Metadata Tracking

Complete metadata available in: `cluster_1_metadata.csv`

Columns:
- `arxiv_id`: Paper identifier on ArXiv
- `title`: Full paper title
- `authors`: Author list
- `publish_date`: Publication date (YYYY-MM-DD)
- `page_count`: Number of pages (where available)
- `first_author_affiliation`: Organization (where available)
- `relevance_score`: 7-10 scale for topic relevance
- `abstract_summary`: 100-word abstract summary

---

## Key Research Findings Summary

### Most Critical Paper
**2601.00205: Understanding Security Risks of AI Agents' Dependency Updates**
- Only paper with empirical analysis of agent-induced vulnerabilities
- 117,062 dependency changes analyzed
- AI agents introduce 2.46% vulnerable versions vs. 1.64% human rate
- Demonstrates 98-unit net vulnerability increase from agent work

### Most Comprehensive Framework
**2506.04133: TRiSM for Agentic AI**
- Extended framework for trust, risk, security management
- Component Synergy Score metric for evaluating agent coordination
- Covers explainability, operations, security, privacy, governance

### Most Practical Defense
**2511.21990: A Safety and Security Framework (NVIDIA)**
- Validated on real NVIDIA AI-Q system
- Releases 10,000+ attack/defense execution traces
- Operational risk taxonomy for enterprise deployment

### Most Comprehensive Threat Model
**2508.10043: MAESTRO Seven-Layer Framework**
- Practical threat modeling for network monitoring agents
- Demonstrates DoS and memory corruption attacks
- Defense-in-depth recommendations

---

## Citation Recommendations

### For Dependency Management Vulnerabilities
```bibtex
@article{singla2026understanding,
  title={Understanding Security Risks of AI Agents' Dependency Updates},
  author={Singla, Tanmay and Çakar, Berk and Amusuo, Paschal C. and Davis, James C.},
  year={2026},
  journal={arXiv},
  eprint={2601.00205}
}
```

### For Comprehensive Survey
```bibtex
@article{shahriar2025survey,
  title={A Survey on Agentic Security: Applications, Threats and Defenses},
  author={Shahriar, Asif and Rahman, Md Nafiu and Ahmed, Sadif and others},
  year={2025},
  journal={arXiv},
  eprint={2510.06445}
}
```

---

## ArXiv Submission Notes

All papers are preprints on ArXiv with the following status:
- May be under review at conferences/journals
- Some have multiple versions (v1, v2, etc.)
- Stable URLs for PDFs and abstracts

To cite: Include both ArXiv ID and persistent URL
- Example: https://arxiv.org/abs/2601.00205
- Cite as: arXiv:2601.00205

---

## Related Resources

### Companion Materials
- Most papers include GitHub repositories for code/data
- Check abstract page for repository links
- Some datasets are openly available (e.g., BAD-ACTS, NVIDIA AI-Q traces)

### Follow-up Research
- Check papers' "Related Work" sections for prior context
- Newer papers often cite and build on 2024 foundational work
- 2025 papers represent state-of-art as of January 2026

---

## File Organization

Suggested local organization:
```
cluster_1_agentic_systems/
  ├── RESEARCH_SUMMARY.md          # This overview document
  ├── DOWNLOAD_INDEX.md             # Download instructions
  ├── cluster_1_metadata.csv        # Complete metadata table
  ├── {arxiv_id}_{title}.pdf        # Individual papers (16 total)
  └── README.md                     # Usage guide
```

---

**Research compiled by:** Claude Code (AnthropicAI)
**Date:** January 5, 2026
**Search method:** Systematic ArXiv API queries + validation
**Total papers in collection:** 16
**Estimated total PDF size:** ~200-300 MB (depending on resolution)
