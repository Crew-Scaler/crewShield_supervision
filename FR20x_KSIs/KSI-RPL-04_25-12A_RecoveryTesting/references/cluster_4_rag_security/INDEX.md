# Cluster 4: RAG Systems Security & Knowledge Base Integrity - Quick Index

## Files Overview

### Documentation Files

1. **README.md** (12 KB)
   - Comprehensive research summary
   - Attack techniques and defense mechanisms
   - Key findings and recommendations
   - Complete paper categorization

2. **DOWNLOAD_SUMMARY.txt** (13 KB)
   - Detailed download statistics
   - All 15 papers ranked by relevance score
   - Quantitative metrics from papers
   - Implementation recommendations

3. **cluster_4_metadata.csv** (6.1 KB)
   - Tabular format with 15 rows (papers)
   - 12 columns: rank, arxiv_id, title, authors, date, pages, score, pdf_filename, topic, attack_type, key_findings
   - Sortable and filterable
   - Suitable for Excel/Sheets

### Data Files

4. **papers.json** (8.9 KB)
   - Structured JSON format
   - Complete metadata for all 15 papers
   - Authors, abstracts, URLs included
   - Machine-readable format

### PDF Papers (15 Total, 61.6 MB)

Listed by Relevance Score (Highest to Lowest):

#### Tier 1: Highest Relevance (Score 45+)
- **2512.10998v1.pdf** - SCOUT: A Defense Against Data Poisoning (Score: 58)
- **2511.06212v1.pdf** - RAG-targeted Adversarial Attack (Score: 56)
- **2512.13207v2.pdf** - Evaluating Adversarial Attacks on FL (Score: 46)
- **2510.10008v1.pdf** - RIPRAG: Hack RAG QA Systems (Score: 45)
- **2512.21681v1.pdf** - Retriever Backdoors in RAG (Score: 45)

#### Tier 2: High Relevance (Score 35-44)
- **2511.01268v1.pdf** - Rescuing the Unpoisoned (Score: 40)
- **2511.11240v1.pdf** - HealSplit: Self-Healing Defense (Score: 38)
- **2511.09105v1.pdf** - Cost-Minimized Label-Flipping (Score: 38)
- **2512.19286v2.pdf** - GShield: Poison Defense in FL (Score: 38)
- **2511.15435v1.pdf** - HV-Attack: Multimodal RAG (Score: 35)
- **2512.16962v1.pdf** - MemoryGraft: Memory Poisoning (Score: 35)

#### Tier 3: Moderate Relevance (Score <35)
- **2512.23132v1.pdf** - Multi-Agent Threat Mitigation (Score: 28)
- **2512.22860v1.pdf** - Adaptive Trust Consensus (Score: 28)
- **2511.09392v4.pdf** - Potent but Stealthy Poisoning (Score: 26)
- **2512.23809v1.pdf** - Zero-Trust Agentic FL (Score: 20)

## Quick Start Guide

### For Researchers
1. Start with **README.md** for comprehensive overview
2. Review **cluster_4_metadata.csv** for quick paper comparison
3. Read highest-scored papers first:
   - SCOUT (2512.10998v1.pdf)
   - RAG-targeted Attack (2511.06212v1.pdf)
   - RIPRAG (2510.10008v1.pdf)

### For Security Teams
1. Focus on papers in Tier 1 & 2
2. Review DOWNLOAD_SUMMARY.txt for attack/defense mapping
3. Key papers to review:
   - Retriever Backdoors (2512.21681v1.pdf)
   - MemoryGraft (2512.16962v1.pdf)
   - SCOUT Defense (2512.10998v1.pdf)

### For Machine Learning Engineers
1. Review defense mechanisms in README.md
2. Focus on:
   - GShield (Byzantine-robust aggregation)
   - HealSplit (Adversarial distillation)
   - Rescuing the Unpoisoned (Detection methods)

## Research Topics Covered

### RAG Attacks (5 papers)
- Direct adversarial attacks on RAG systems
- Black-box attack techniques
- Retriever backdoor insertion
- Multimodal poisoning attacks
- Agent memory corruption

### Data Poisoning (4 papers)
- Training data poisoning
- Label-flipping attacks
- Cost-effective poisoning strategies
- Stealthy attack designs

### Defenses (4 papers)
- Statistical anomaly detection
- Byzantine-robust aggregation
- Adversarial distillation
- Multi-agent verification

### Distributed Systems (2 papers)
- Federated learning security
- Zero-trust architectures
- Blockchain-based integrity verification

## Key Statistics

- **Total Papers**: 15
- **Total Pages**: ~150-180 pages (average 10-12 pages per paper)
- **Coverage Period**: Oct 2024 - Jan 2025
- **Success Rate**: 100% download completion
- **Total Size**: 61.6 MB
- **Attack Categories**: 6 major types identified
- **Defense Mechanisms**: 6 main approaches identified

## Search Terms Used

The following ArXiv search terms were used to compile this cluster:

1. `cat:cs.AI AND (RAG OR "retrieval augmented")`
2. `cat:cs.AI AND ("poisoning attack" OR "data poisoning")`
3. `cat:cs.CL AND (RAG OR "retrieval augmented")`
4. `cat:cs.CL AND ("poisoning" OR "adversarial attack")`
5. `cat:cs.CR AND (RAG OR poisoning OR backdoor)`

Filters applied:
- Publication date: 2024-2025 only
- Minimum 7 pages per paper
- Explicit focus on RAG, knowledge bases, or data poisoning

## How to Use These Files

### Viewing PDFs
```bash
# Open individual paper
open "2512.10998v1.pdf"

# List all papers
ls -lh *.pdf

# Count papers
ls -1 *.pdf | wc -l
```

### Analyzing Metadata
```bash
# View CSV in terminal
cat cluster_4_metadata.csv

# View as JSON
cat papers.json | jq .

# Sort by relevance score
sort -t',' -k8 -rn cluster_4_metadata.csv | head -5
```

### Creating Custom Reports
All files are provided in open formats (PDF, CSV, JSON, TXT, MD) for easy analysis and reporting.

## Related Clusters

This cluster (Cluster 4) is part of a larger research effort on AI-Driven Transformation & CSP Implications:

- **Cluster 1**: Chaos Engineering & Cloud Infrastructure
- **Cluster 2**: [To be added]
- **Cluster 3**: [To be added]
- **Cluster 4**: RAG Systems Security & Knowledge Base Integrity (THIS)
- **Cluster 5+**: [Ongoing]

See parent directory for other clusters: `/KSI-RPL-04_25-12A_RecoveryTesting/references/`

## Metadata Dictionary

### CSV Column Descriptions

| Column | Type | Description |
|--------|------|-------------|
| rank | Integer | Paper ranking (1-15) by relevance |
| arxiv_id | String | ArXiv paper identifier (e.g., 2512.10998v1) |
| title | String | Full paper title |
| first_author | String | Primary/first author name |
| all_authors | String | Complete author list (comma-separated) |
| published_date | Date | Publication date (YYYY-MM-DD format) |
| pages | Integer | Estimated page count |
| relevance_score | Integer | Relevance to RAG security (1-50 scale) |
| pdf_filename | String | Local PDF filename |
| main_topic | String | Primary research topic |
| attack_type | String | Attack/defense mechanism category |
| key_findings | String | Summary of key findings (truncated) |

## Contact & Attribution

- **Compiled**: January 6, 2025
- **Source**: ArXiv (arxiv.org)
- **Method**: Systematic search with manual curation
- **Quality Assurance**: 100% download verification

---

Last Updated: 2025-01-06
Total Files: 19 (15 PDFs + 4 metadata/documentation files)
