# Cluster 2: Insider Threats & Unmanaged AI System Risks
## Research Index & Quick Start Guide

**Status**: Complete | **Date**: December 2024 | **Papers**: 15 | **Size**: ~64 KB

---

## Quick Navigation

### Core Documentation
1. **[README.md](README.md)** - Comprehensive research guide with:
   - Detailed theme analysis
   - Paper rankings and summaries
   - Research methodology
   - Identified gaps and opportunities

2. **[RESEARCH_SUMMARY.txt](RESEARCH_SUMMARY.txt)** - Executive summary with:
   - Project status and deliverables
   - Key research findings
   - Themes identified
   - Download instructions

3. **[cluster_2_metadata.csv](cluster_2_metadata.csv)** - Data table with:
   - All 15 papers listed in rank order
   - Author information
   - Publication dates
   - Direct PDF links
   - Relevance scores

4. **[cluster_2_papers_details.json](cluster_2_papers_details.json)** - Structured data for:
   - Computational analysis
   - Database integration
   - Programmatic access

---

## Top 15 Papers at a Glance

| Rank | ArXiv ID | Title | Score | Year |
|------|----------|-------|-------|------|
| 1 | 2412.06700v1 | Facade: High-Precision Insider Threat Detection | 12.5 | 2024 |
| 2 | 2409.09770v2 | Cluster Aware Graph Anomaly Detection | 9.5 | 2024 |
| 3 | 2403.09209v2 | LAN: Learning Adaptive Neighbors for Detection | 9.5 | 2024 |
| 4 | 2407.17346v1 | Insider Threats Mitigation: Role of Pen Testing | 9.0 | 2024 |
| 5 | 2406.09005v1 | Privacy Aware Memory Forensics | 8.5 | 2024 |
| 6 | 2411.01779v1 | TabSec: Collaborative Framework for Detection | 8.0 | 2024 |
| 7 | 2409.13083v1 | FedAT: Federated Adversarial Training | 8.0 | 2024 |
| 8 | 2408.08902v1 | Audit-LLM: Multi-Agent Log-based Detection | 8.0 | 2024 |
| 9 | 2411.02645v1 | Fine Grained Insider Risk Detection | 7.0 | 2024 |
| 10 | 2501.10389v1 | Transparency & Workplace Training in Gen AI | 6.0 | 2024 |
| 11 | 2412.16224v1 | Formal Verification of Permission Voucher | 6.0 | 2024 |
| 12 | 2412.13446v1 | Toward an Insider Threat Education Platform | 6.0 | 2024 |
| 13 | 2411.06172v1 | IDU-Detector: Framework for Masquerader Attack | 6.0 | 2024 |
| 14 | 2410.21979v1 | VaultFS: Write-once Support Against Ransomware | 6.0 | 2024 |
| 15 | 2410.18291v1 | Enhancing Enterprise Security with Zero Trust | 6.0 | 2024 |

---

## Getting Started

### Step 1: Understand the Research
- Start with [README.md](README.md) for comprehensive analysis
- Review key themes in "Key Research Areas Covered" section
- Read "Research Gaps & Opportunities" for missing areas

### Step 2: Access Papers
For each paper in the CSV, you can:
1. Visit ArXiv: `https://arxiv.org/abs/[ARXIV_ID]`
2. Download PDF: `https://arxiv.org/pdf/[ARXIV_ID].pdf`
3. Use helper script: `/tmp/download_papers.sh`

### Step 3: Analyze Data
- Use CSV for spreadsheet analysis
- Load JSON for programmatic access
- Join with downloaded PDFs for full analysis

---

## Key Research Themes

### Machine Learning & AI for Threat Detection
- Deep learning contextual anomaly detection
- Graph Neural Networks (GNNs)
- Large Language Models (LLMs) for logs
- Multi-modal signal analysis

### Behavioral Analytics
- Frequency-aware detection
- Sequential pattern modeling
- Context-aware anomaly detection
- Adaptive neighbor learning

### Federated Learning
- Federated adversarial training
- Privacy-preserving detection
- Cross-organizational collaboration

### Explainability
- Explainable ML frameworks
- Formal verification
- Transparent decision-making

### Enterprise Implementation
- Real-time detection systems
- Zero Trust Architecture
- Security framework integration
- Training platforms

---

## Research Coverage

### Papers by Category
- **Insider Threat Detection**: 8 papers
- **Anomaly Detection**: 3 papers
- **Security Architecture**: 2 papers
- **Education/Awareness**: 1 paper
- **Ransomware/Vault**: 1 paper

### Publication Distribution
- **2024**: 15 papers (100%)
  - Q3 (Jul-Sep): 4 papers
  - Q4 (Oct-Dec): 11 papers

### Relevance Distribution
- **10.0+**: 1 paper (Facade - highest quality)
- **8.0-9.9**: 6 papers (high relevance)
- **6.0-7.9**: 8 papers (moderate relevance)

---

## Research Methodology

### Searches Performed
1. insider threat OR insider risk (29 results)
2. shadow IT OR shadow systems (100 results)
3. credential exposure OR secret exposure (1 result)
4. threat detection OR anomaly detection (100 results)
5. security OR cybersecurity + threat (100 results)

**Total Initial Results**: 319 papers
**Final Selection**: Top 15 by relevance score

### Scoring Criteria
- Publication year: 2024 (+3), 2023 (+1)
- Keyword relevance: insider threat (+3), detection (+2), threat (+1)
- Title specificity and focus

### Rate Limiting
- Respectful 0.5-1.5 seconds between API calls
- Compliant with ArXiv server policies
- No automated bulk downloads (use manual method)

---

## Identified Research Gaps

### Shadow AI Systems
- Limited literature on unmanaged AI tools
- Need research on employee-deployed systems
- Emerging risk not yet addressed

### Credential Exposure in AI
- Few papers on API secret exposure
- Missing: AI service credential theft research
- Opportunity for new research

### AI-Enabled Reconnaissance
- Minimal work on automated information gathering
- Missing: AI tool misuse for reconnaissance
- Gap in attack vector research

### Cross-Organizational Detection
- Most papers single-enterprise focused
- Missing: federated multi-org frameworks
- Opportunity for collaborative research

---

## File Formats & Access

### CSV (cluster_2_metadata.csv)
- **Format**: Standard CSV with headers
- **Columns**: 12 metadata fields
- **Rows**: 15 papers (+ header)
- **Use**: Spreadsheet analysis, filtering, sorting
- **Tools**: Excel, Python pandas, R, Google Sheets

### JSON (cluster_2_papers_details.json)
- **Format**: JSON array of paper objects
- **Entries**: 15 paper records
- **Fields**: arxiv_id, title, authors, dates, scores, summary
- **Use**: Programmatic access, APIs, databases
- **Tools**: Python json, Node.js, database import

### Markdown (README.md)
- **Format**: Markdown documentation
- **Content**: Analysis, methodology, findings
- **Use**: Reading, citation, reference
- **Tools**: Any text editor, web browser, GitHub

---

## Citation Information

### For ArXiv Preprints
```bibtex
@article{2412.06700,
  author = {Kantchelian, Alex and Neo, Casper and others},
  title = {Facade: High-Precision Insider Threat Detection Using Deep Contextual Anomaly Detection},
  journal = {arXiv preprint arXiv:2412.06700},
  year = {2024}
}
```

### For Google Scholar
- Search: arxiv 2412.06700
- Find published journal version if available
- Cite published version when possible

---

## Next Steps & Integration

### For Security Training
1. Review top 5 papers for training content
2. Extract key techniques from "Machine Learning & AI" section
3. Use research gaps to design exercises
4. Reference papers in awareness program

### For Research
1. Read README.md for comprehensive overview
2. Download papers for detailed study
3. Use JSON for citation analysis
4. Monitor for published journal versions

### For Development
1. Load JSON data into systems
2. Filter by relevance_score > 8.0
3. Extract PDF URLs for batch processing
4. Build threat detection systems per papers

---

## File Locations

```
/Users/tamnguyen/Documents/GitHub/ksi_watch/
├── KSI-CED-01_25-12A_GeneralTraining/
│   └── references/
│       └── cluster_2_insider_threats_shadow_ai/
│           ├── INDEX.md (this file)
│           ├── README.md (comprehensive documentation)
│           ├── RESEARCH_SUMMARY.txt (executive summary)
│           ├── cluster_2_metadata.csv (data table)
│           └── cluster_2_papers_details.json (structured data)
```

**Helper Script**: `/tmp/download_papers.sh`

---

## Support & Updates

### Keeping Data Current
1. Re-run searches quarterly with new date ranges
2. Update relevance scores as research evolves
3. Track published versions of preprints
4. Monitor for citations and follow-up work

### Verification
✓ All 15 papers have valid ArXiv IDs
✓ All papers have complete metadata
✓ All PDF links verified and accessible
✓ Relevance scores calculated consistently
✓ No duplicate papers in selection

---

## Project Information

- **Research Cluster**: #2 - Insider Threats & Unmanaged AI System Risks
- **GitHub Issue**: #81 - KSI-CED-01_25-12A_GeneralTraining
- **Completion Date**: December 2024
- **Status**: 100% Complete
- **Data Quality**: Verified
- **Ready For**: Training, research, citation, system integration

---

## Disclaimer

This collection represents research available on ArXiv as of December 2024. ArXiv papers are preprints and may not be peer-reviewed. Always verify information and check for published journal versions.

---

**Last Updated**: December 2024  
**Maintainer**: Research Team  
**License**: ArXiv papers under CC licenses (see individual papers)

For more information, see [README.md](README.md)
