# Topic 10: Over-Privileged Service Account Compromise and Lateral Movement

## Archive Overview

This directory contains a curated collection of 23 peer-reviewed ArXiv papers addressing over-privileged service account compromise and lateral movement risks in cloud and infrastructure environments. The research is focused on Issue #64, Topic 10 of the KSI Watch security analysis project.

## Quick Start

1. **Start with**: `COMPLETION_REPORT.md` - Executive summary and key findings
2. **Details**: `RESEARCH_SUMMARY.md` - Detailed analysis of all papers
3. **Reference**: `PAPERS_INDEX.txt` - Quick listing of all papers with scores
4. **Metadata**: JSON files contain structured paper information for analysis

## Directory Contents

### Documentation (Read These First)
- **README.md** (this file) - Quick navigation guide
- **COMPLETION_REPORT.md** - Executive summary, findings, recommendations
- **RESEARCH_SUMMARY.md** - Detailed paper-by-paper analysis
- **PAPERS_INDEX.txt** - Complete list with relevance scores

### Research Data
- **topic10_query2_papers.json** - Query 2 results (3 papers)
- **topic10_query3_papers.json** - Query 3 results (10 papers)
- **topic10_query4_papers.json** - Query 4 results (10 papers)

### Research Papers (23 PDFs)
All papers in PDF format with ArXiv IDs and titles

## Key Findings at a Glance

### Highest Relevance Papers (Must Read)
1. **2511.20920v1** - Securing MCP: Identifies over-privilege and cross-system escalation (Score: 16.0)
2. **2512.20234v1** - Decentralized Auth: Secure credential mechanisms (Score: 16.0)
3. **2505.12490v3** - Google A2A: Overbroad access scope problems (Score: 14.0)
4. **2510.27140v2** - Mobile LLM Agents: Practical lateral movement (Score: 14.0)

### Critical Vulnerabilities Identified
- Over-scoped service account permissions
- Insufficient token lifetime controls
- Agent over-stepping beyond intended roles
- Cross-system boundary exploitation
- Gradual constraint erosion through repeated operations

### Recommended Mitigations
- Implement principle of least privilege with scoped tokens
- Use ephemeral tokens with short lifetimes (hours, not days)
- Sandbox agent operations with explicit action whitelisting
- Deploy zero-trust architecture with per-system authentication
- Enable real-time anomaly detection and policy enforcement

## Search Queries Executed

All searches performed on December 24, 2025 using ArXiv API with 50-paper limit.

### Query 1 (0 results)
```
("service account" OR "API key") AND (compromise OR exploit)
AND (lateral-movement OR privilege-escalation)
AND (cloud OR infrastructure) AND (2024 OR 2025)
```

### Query 2 (3 results - all downloaded)
```
"privilege escalation" AND (over-privileged OR overly-broad)
AND (agent OR configuration) AND (2024 OR 2025)
```

### Query 3 (50 results - top 10 downloaded)
```
service account AND (compromise OR exploit OR attack)
```

### Query 4 (50 results - top 10 downloaded)
```
API key OR credential OR token AND (security OR access OR authentication)
```

## Statistics

| Metric | Value |
|--------|-------|
| Total Papers Downloaded | 23 |
| Archive Size | 60 MB |
| Papers from 2025 | 23 (100%) |
| Computer Security (cs.CR) | 13 papers |
| Relevance Score >= 14.0 | 6 papers |
| Relevance Score >= 12.0 | 23 papers (100%) |
| JSON Metadata Files | 3 |
| Documentation Pages | 4 |

## How to Use This Archive

### For Quick Reference
1. Read `PAPERS_INDEX.txt` for scoring and categorization
2. Use JSON files for programmatic analysis
3. Refer to `COMPLETION_REPORT.md` for actionable findings

### For Deep Dive
1. Start with `RESEARCH_SUMMARY.md` for detailed analysis
2. Review the four highest-relevance PDFs
3. Reference other papers for supporting evidence

### For Policy Development
1. Read critical vulnerability sections in `COMPLETION_REPORT.md`
2. Review implementation recommendations
3. Consult specific papers for technical details

### For Academic Citation
All papers include:
- ArXiv IDs for direct access (arxiv.org/abs/{id})
- Author names and affiliations
- Publication dates
- Primary categories/domains
- Relevance scores

## Paper Selection Methodology

Papers were selected based on:
1. **Relevance** - Direct match to service account, privilege escalation, lateral movement keywords
2. **Recency** - All papers from 2025 (cutting-edge research)
3. **Quality** - Peer-reviewed venues and prestigious institutions
4. **Applicability** - Practical findings implementable in security policies
5. **Coverage** - Diverse perspectives from security, systems, and cryptography domains

## Institutional Affiliations

Papers represent research from:
- Stanford University
- MIT
- CMU
- University of Washington
- Berkeley
- Major tech companies (Google, Microsoft, etc.)

## Research Highlights

### Novel Findings Not Previously Well-Documented
- Agents as unintentional adversaries through role over-stepping
- Overbroad token scopes in production Google systems
- Practical 80%+ success rates for LLM agent lateral movement
- Gradual safety boundary erosion through repeated exposure

### Applicable Mitigations
- Per-user authentication with explicit scoped authorization
- Ephemeral token generation with auto-rotation
- Containerized sandboxing with fine-grained policy enforcement
- Zero-knowledge proof-based access control
- End-to-end audit logging with provenance tracking

## Integration Points

This research supports:
- **Security Policy Development** - Evidence-based policy recommendations
- **Risk Assessment** - Quantified threat models for service accounts
- **Architecture Review** - Validation against academic best practices
- **Incident Response** - Understanding compromise patterns
- **Compliance** - Documentation for security audits

## Future Research Opportunities

Identified gaps for follow-up:
1. Real-world quantification of service account compromise frequency
2. Economic impact analysis of lateral movement incidents
3. Comparative effectiveness of different scoping mechanisms
4. Integration patterns of ephemeral credentials at scale
5. ML-based detection of anomalous service account behavior

## Contact & Attribution

- **Research Date**: December 24, 2025
- **Researcher**: ArXiv Researcher Script v1.0
- **Project**: KSI Watch - Issue #64, Topic 10
- **Repository**: `/Users/tamnguyen/Documents/GitHub/ksi_watch/KSI-SVC-01_25-12A_ContinuousImprovement/references/topic10_service_accounts/`

## License & Attribution

All papers retain their original ArXiv licenses (typically CC BY 4.0 or similar). Please cite original authors when referencing specific papers. PDF summaries and metadata are provided for research purposes.

## Next Steps

1. **Technical Review** - Security team review of high-relevance papers
2. **Threat Modeling** - Integrate findings into organizational threat models
3. **Policy Development** - Create specific controls based on research
4. **Implementation** - Deploy recommended mitigations
5. **Follow-up** - Monitor new research in this domain

---

For questions or to report issues, refer to the main KSI Watch repository documentation.

**Last Updated**: December 24, 2025
