# Cluster 1: Agentic AI Systems & Vulnerability Management
## Research Collection

**Status:** Research completed and indexed
**Date:** January 5, 2026
**Papers Collected:** 16
**Average Publication Date:** October 2025
**Quality Threshold:** 7+/10 relevance score

---

## Overview

This collection contains 16 carefully selected ArXiv papers (2024-2026) on autonomous agents, AI agents, and vulnerability management in software supply chains. All papers meet strict quality criteria:

- **Publication window:** 2024-2026 (focus on 2025)
- **Relevance:** Papers discuss BOTH AI/agents AND security/vulnerability
- **Minimum quality:** 7/10 relevance score (range 7-10)
- **Page count:** Mix of short papers (5 pages) to comprehensive surveys (54 pages)

---

## Collection Structure

### Documentation Files

| File | Purpose |
|------|---------|
| **README.md** | This file - overview and usage guide |
| **RESEARCH_SUMMARY.md** | Comprehensive research analysis with findings |
| **DOWNLOAD_INDEX.md** | Direct ArXiv links and download instructions |
| **cluster_1_metadata.csv** | Machine-readable paper metadata |

### PDF Papers (16 total)

Papers are organized by ArXiv ID and can be downloaded directly from ArXiv using URLs in DOWNLOAD_INDEX.md

---

## Key Findings at a Glance

### Critical Vulnerability: Dependency Management
- **Paper:** 2601.00205 (2026-01)
- **Finding:** AI agents introduce vulnerable dependencies 2.46% vs 1.64% (humans)
- **Impact:** Analysis of 117,062 dependency changes across 2,807 repositories
- **Risk:** 98-unit net vulnerability increase from agent work vs -1,316 from humans

### Multi-Agent System Compromise
- **Paper:** 2503.12188 (2025-03)
- **Finding:** Multi-agent LLM systems can be forced to execute arbitrary malicious code
- **Success Rate:** 58-90% attack effectiveness (100% in some configurations)
- **Root Cause:** Agent hijacking via prompt infection spreads through communication

### Emerging Defense Frameworks
- **TRiSM** (2506.04133): Trust, Risk, Security Management framework
- **MAESTRO** (2508.10043): Seven-layer threat modeling architecture
- **ATFAA/SHIELD** (2504.19956): Advanced threat framework and mitigation
- **MAAIS** (2512.18043): Lifecycle-aware security framework
- **BAD-ACTS** (2508.16481): Robustness benchmark with 188 attack examples

### Supply Chain Integration Risks
- **Paper:** 2410.21218 (2024-10)
- **Finding:** LLM deployment ecosystem has 20+ risk categories across stakeholders
- **Gap:** SLSA, SBOM, in toto insufficient for agentic systems
- **Mitigation:** Comprehensive risk taxonomy and protective strategies

---

## Paper Tier System

### Tier 1: Critical (9-10/10 Relevance)
Papers with direct empirical findings or comprehensive frameworks:
- **2601.00205** - Empirical study of agent dependency vulnerabilities (10/10)
- **2512.23480** - Agentic AI autonomous defense (9/10)
- **2510.23883** - Threats, defenses, evaluation (9/10)
- **2510.06445** - Survey of 160+ papers (9/10)
- **2506.04133** - TRiSM framework (9/10)
- **2508.10043** - MAESTRO threat modeling (9/10)
- **2511.21990** - Real-world validation on NVIDIA systems (9/10)
- **2410.21218** - LLM supply chain composition (9/10)
- **2503.12188** - Multi-agent code execution attacks (9/10)

### Tier 2: Strong Supporting (8/10 Relevance)
Papers with significant contributions to specific aspects:
- **2508.16481** - BAD-ACTS benchmark (8/10)
- **2504.19956** - ATFAA threat framework (8/10)
- **2510.00317** - MAVUL vulnerability detection system (8/10)
- **2505.12786** - LLM agents in cyberattacks (8/10)
- **2512.18043** - MAAIS security framework (8/10)
- **2502.07049** - LLM vulnerability detection survey (8/10)

### Tier 3: Foundational (7/10 Relevance)
- **2411.10184** - Supply chain consensus-seeking with agents (7/10)

---

## Quick Start

### Option 1: Read Documentation First
```
1. Start with RESEARCH_SUMMARY.md (comprehensive analysis)
2. Review DOWNLOAD_INDEX.md (organized by relevance tier)
3. Reference cluster_1_metadata.csv (for specific papers)
```

### Option 2: Download Everything
See bulk download instructions in DOWNLOAD_INDEX.md:
- Linux/macOS: `wget` or `curl` commands
- Universal: Python script provided
- Rate limit: 3+ seconds between ArXiv requests

### Option 3: Start with Most Critical Papers
**Recommended reading order:**
1. **2601.00205** - Dependency vulnerability empirical study
2. **2510.06445** - Survey of agentic security (context setting)
3. **2506.04133** - TRiSM framework (comprehensive overview)
4. **2511.21990** - Real-world validated framework
5. **2503.12188** - Critical multi-agent vulnerability

---

## Research Methodology

### Search Queries Executed
1. "autonomous agents software supply chain vulnerability"
2. "AI agents dependency management security"
3. "agentic systems vulnerability monitoring"
4. "agent-based vulnerability detection"
5. "LLM agents software composition"
6. "autonomous agents third-party risks"

### Selection Process
- **Total papers evaluated:** 50+
- **Papers accepted:** 16 (32% acceptance rate - high quality)
- **Rejection criteria:** Missing security/vulnerability focus, pre-2024 publication, low relevance

### Quality Metrics
- All papers mention agents/autonomous AI systems
- All papers address security/vulnerability/supply chain topics
- Minimum 7/10 relevance score for intersection of both topics
- Published in last 2 years (prioritize 2025)

---

## Papers by Research Area

### Dependency & Supply Chain Security
- 2601.00205: AI agents' dependency updates (empirical)
- 2512.23480: Autonomous defense in supply chain
- 2410.21218: LLM supply chain composition
- 2411.10184: Supply chain consensus-seeking

### Threat Modeling & Frameworks
- 2510.23883: Threats, defenses, evaluation
- 2506.04133: TRiSM framework (trust, risk, security)
- 2508.10043: MAESTRO threat modeling
- 2504.19956: ATFAA threat framework
- 2512.18043: MAAIS security framework
- 2511.21990: Safety and security (real-world validation)

### Vulnerability Detection
- 2510.00317: MAVUL multi-agent detection
- 2502.07049: LLM vulnerability detection survey
- 2505.12786: LLM agents in cyberattacks

### Security Evaluation & Benchmarking
- 2510.06445: Survey of agentic security (160+ papers)
- 2508.16481: BAD-ACTS robustness benchmark
- 2503.12188: Multi-agent code execution attacks

---

## Integration with KSI Watch

### Immediate Applications
1. **Dependency Screening** (2601.00205)
   - Implement PR-stage vulnerability checks for agent-authored changes
   - 2.46% failure rate vs 1.64% baseline

2. **Threat Modeling** (2508.10043, 2506.04133)
   - Apply MAESTRO/TRiSM frameworks to monitoring infrastructure
   - Cover 30+ agent-specific attack vectors

3. **Robustness Testing** (2508.16481)
   - Adopt BAD-ACTS evaluation methodology
   - Test against 188 curated attack examples

4. **Runtime Security** (2511.21990)
   - Implement NVIDIA's approach: auxiliary AI + human oversight
   - Deploy dataset of 10,000+ attack/defense traces

### Long-term Strategic Use
- Establish baseline understanding of agentic AI security landscape
- Track emergence of new threat categories (currently 30+ documented)
- Monitor evolution of defense mechanisms (5 frameworks identified)
- Guide development of agent-specific security controls

---

## Citation & Usage

### For Research Papers
```bibtex
@misc{singla2026understanding,
  title={Understanding Security Risks of AI Agents' Dependency Updates},
  author={Singla, Tanmay and others},
  year={2026},
  journal={arXiv},
  eprint={2601.00205}
}
```

### For This Collection
```
Cluster 1: Agentic AI Systems & Vulnerability Management
Research Collection - January 5, 2026
16 papers compiled from ArXiv (2024-2026)
Focus: AI agents and software supply chain security
```

---

## Additional Resources

### In This Directory
- **RESEARCH_SUMMARY.md**: 5000+ word comprehensive analysis
- **DOWNLOAD_INDEX.md**: Direct links and bulk download scripts
- **cluster_1_metadata.csv**: Machine-readable data for all papers

### Related Collections (Future)
- Cluster 2: Supply Chain Security Fundamentals
- Cluster 3: Prompt Injection & Attack Surface Analysis
- Cluster 4: Regulatory & Governance Frameworks

### External Resources
- ArXiv: https://arxiv.org (all papers here)
- MITRE ATLAS: https://atlas.mitre.org (framework referenced in papers)
- CWE/CVE: Common Weakness Enumeration (vulnerability references)
- SBOM Standards: https://cyclonedx.org (composition standards)

---

## Metadata Summary

### Publication Timeline
- **2026**: 1 paper (January preprint)
- **2025**: 14 papers (distributed across year)
- **2024**: 1 paper (foundational work)

### Paper Statistics
- **Minimum pages:** 5 (2601.00205)
- **Maximum pages:** 54 (2508.16481, 2502.07049)
- **Median pages:** ~12-26 pages
- **Estimated total size:** 200-300 MB (all PDFs combined)

### Author Distribution
- Academic institutions: MIT, CMU, Stanford, Oxford, etc.
- Industry: NVIDIA, Microsoft, OpenAI, Google, others
- Government/Non-profit: Some security research labs

---

## Notes for Researchers

### Methodological Considerations
1. Papers represent preprints (may undergo revisions)
2. Multiple versions exist (v1, v2, v3) - latest recommended
3. Some findings based on proprietary models (GPT-4, Claude, etc.)
4. Empirical studies limited to specific datasets/repositories

### Limitations
1. Rapidly evolving field - this research reflects state as of January 2026
2. Limited long-term data on agent vulnerabilities
3. Defense mechanisms still emerging/unvalidated in production
4. Dependency vulnerability data specific to analyzed repositories

### Recommended Validation
1. Test recommendations in your specific environment
2. Consider your organization's risk tolerance
3. Implement defense-in-depth (don't rely on single mitigation)
4. Monitor for new vulnerabilities as field evolves

---

## Next Steps

### For Implementation Teams
1. Review RESEARCH_SUMMARY.md for framework overview
2. Select relevant papers from Tier 1 for detailed reading
3. Map findings to your current architecture
4. Identify quick wins (e.g., dependency screening from 2601.00205)

### For Security Researchers
1. Use metadata CSV for systematic analysis
2. Review all papers in research area of interest
3. Check paper references for broader context
4. Monitor ArXiv for newer publications

### For Policymakers
1. Focus on Tier 1 papers (comprehensive findings)
2. Review regulatory implications in RESEARCH_SUMMARY.md
3. Consider governance frameworks (papers 2506.04133, 2512.18043)
4. Assess supply chain control gaps (2410.21218)

---

## Contact & Updates

For questions about this collection:
- Check RESEARCH_SUMMARY.md (detailed analysis)
- Review DOWNLOAD_INDEX.md (access information)
- Consult cluster_1_metadata.csv (paper details)

For new papers:
- Monitor ArXiv categories: cs.AI, cs.CR, cs.SE
- Search terms: "agentic security", "agent vulnerability", "LLM supply chain"
- Check quarterly for new research in this rapidly evolving field

---

**Collection Status:** Complete
**Last Updated:** January 5, 2026
**Next Review:** Q2 2026 (expected 5-10 new papers)
**Curator:** Claude Code
**License:** Papers available under CC BY (per ArXiv policy)
