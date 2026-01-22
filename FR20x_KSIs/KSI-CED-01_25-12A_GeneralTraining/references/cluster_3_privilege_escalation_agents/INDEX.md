# Cluster 3 - Master Index & Navigation Guide

**Location**: `/Users/tamnguyen/Documents/GitHub/ksi_watch/KSI-CED-01_25-12A_GeneralTraining/references/cluster_3_privilege_escalation_agents/`

**Collection Size**: 60 KB of documentation + 20 papers
**Paper Count**: 20 peer-reviewed papers
**Documentation**: 5,890 words across 4 guides
**Date Created**: January 6, 2026

---

## File Navigation Guide

### Start Here (First 5 Minutes)
1. **INDEX.md** ← You are here
2. **QUICK_START.md** (8.9 KB) - Role-based reading guide
   - Quick problem statement
   - Key metrics you need to know
   - 30-day implementation plan
   - Common questions checklist
   - Cheat sheet for executives

### For Comprehensive Understanding (30-60 Minutes)
3. **README.md** (19 KB) - Complete research analysis
   - Executive summary
   - Key findings with evidence
   - Authorization models & frameworks
   - Threat taxonomy
   - Quantitative metrics
   - Implementation recommendations
   - Research gaps

### For Paper Access (Reference)
4. **PAPER_INDEX.md** (9.7 KB) - All 20 papers listed
   - Organized by relevance score (10, 9, 8, 7)
   - Direct arXiv links for each paper
   - Author affiliations
   - Key findings summary
   - Access methods (direct/bulk/browser)
   - Citation formats
   - Top 5 must-read papers

### For Data Analysis (Sorting/Filtering)
5. **cluster_3_metadata.csv** (4.6 KB) - Paper metadata
   - 20 rows of paper data
   - Columns: arxiv_id, title, authors, date, pages, affiliation, score, focus, findings
   - Sortable by relevance, year, focus area
   - Import to Excel/database for analysis

### For Project Management
6. **COLLECTION_SUMMARY.txt** (7.6 KB) - Completion report
   - Research methodology
   - Selection criteria met
   - Key findings summary
   - Paper distribution statistics
   - Implementation timeline
   - Next steps

---

## Reading Paths by Role

### Security Team (1-2 Hours)
**Goal**: Understand the vulnerability and fix options
1. QUICK_START.md → "For Security Teams" section (5 min)
2. Download 3 papers from QUICK_START (Security Teams) (90 min reading)
3. README.md → Authorization Models section (15 min)

**Key Takeaway**: "Agents can escalate privileges through multi-step attacks. Need runtime monitoring + identity framework."

### Solutions Architect (1.5-2 Hours)
**Goal**: Design authorization infrastructure
1. QUICK_START.md → "For Architects" section (5 min)
2. Download 3 papers from QUICK_START (Architects) (90 min reading)
3. README.md → Deployment Architecture section (15 min)

**Key Takeaway**: "Choose between zero-trust (complex), AAC (dynamic), or SAGA (cryptographic) based on existing architecture."

### Compliance/Governance (1-1.5 Hours)
**Goal**: Understand governance requirements and regulations
1. QUICK_START.md → "For Compliance/Governance" (5 min)
2. Download 3 papers from QUICK_START (Compliance) (60 min reading)
3. README.md → Critical Research Gaps section (10 min)

**Key Takeaway**: "63% of breached orgs lack AI governance. Need to establish agent authorization policies and audit requirements."

### Researcher (3+ Hours)
**Goal**: Deep dive into threat models and solutions
1. README.md → Complete document (45 min)
2. PAPER_INDEX.md → All 20 papers (reference) (20 min)
3. Download all 20 papers, start with score 10/9 papers (120+ min reading)
4. cluster_3_metadata.csv → Use for analysis/categorization (30 min)

**Key Takeaway**: "Emerging field with 17/20 papers from 2025. Major gaps in cross-domain authorization and automated detection."

---

## Quick Fact Sheet

### The Vulnerability
- **Name**: Privilege Escalation via Multi-Step Agent Operations
- **Root Cause**: Static authorization policies can't detect chained operations
- **Success Rate**: 73.5-96% depending on architecture
- **Affected**: 82.4% of multi-agent systems

### The Impact
- Credential theft
- Data exfiltration  
- Supply chain compromise
- System-level access
- Account takeover

### The Solution Domains
1. **Identity**: DIDs, VCs, agent authentication
2. **Authorization**: Hierarchical, context-aware, dynamic
3. **Monitoring**: Runtime drift detection, goal-conditioned
4. **Tokens**: Cryptographic, revocable, fine-grained
5. **Framework**: Governance model for agent ecosystems

### The Timeline
- Immediate (0-30 days): Audit, establish logging
- Short-term (1-3 months): Hierarchical permissions, authentication
- Medium-term (3-6 months): Zero-trust or AAC implementation
- Long-term (6-12 months): Full infrastructure overhaul

---

## Key Findings at a Glance

| Finding | Evidence | Impact |
|---------|----------|--------|
| IAM inadequate | 5 papers show traditional models fail | Need new authorization paradigm |
| Attack chains work | 3,250 scenarios tested, 91-96% success | Current defense insufficient |
| Over-privileging default | 38.5% safety score avg | Permission models don't exist |
| Peer-agent vulnerable | 82.4% exploitation rate | Multi-agent systems high-risk |
| No standards | 0 published standards | Organizations improvising solutions |

---

## Paper Organization

### By Relevance Score
- **Score 10** (Critical, 2 papers): Must read
  - 2510.25819 - Identity Management
  - 2505.19301 - Zero-Trust Identity

- **Score 9** (Essential, 7 papers): Should read
  - 2501.09674, 2501.10114, 2510.11108, 2510.23883, 2504.21034, 2512.11147, 2510.06445

- **Score 8** (Important, 7 papers): Could read
  - 2508.03858, 2510.22620, 2509.22040, 2511.21990, 2512.05951, 2507.06323, 2506.04133

- **Score 7** (Foundational, 4 papers): Reference
  - 2505.02077, 2512.00742, 2407.19354, 2510.25445

### By Focus Area
- **Authorization & Access Control** (40%): 8 papers
- **Privilege Escalation Attacks** (25%): 5 papers
- **Security Surveys** (25%): 5 papers
- **Infrastructure & Governance** (10%): 2 papers

### By Year
- **2025**: 17 papers (85%)
- **2024**: 2 papers (10%)
- **2022**: 1 paper (5%)

### By Institution
- **AWS/Salesforce/MIT**: Zero-Trust Identity
- **Northeastern**: SAGA Architecture
- **UC Davis**: Security Threats Survey
- **ETH Zurich/Lakera**: Backbone Security Benchmark
- **NVIDIA**: Enterprise Safety Framework
- **Centre for Governance of AI**: Infrastructure
- **Others**: 14 papers from academic institutions

---

## How to Use These Files

### Scenario 1: "I need to brief executives"
1. Read: QUICK_START.md (5 min)
2. Pull: Key metrics from this index
3. Extract: COLLECTION_SUMMARY.txt sections
4. Reference: README.md for detailed evidence

### Scenario 2: "I need to understand the threat"
1. Read: README.md (30 min)
2. Review: Threat taxonomy section
3. Examine: Quantitative metrics
4. Download: 2-3 papers from score 9 category

### Scenario 3: "I need to implement a fix"
1. Use: 30-day plan from QUICK_START.md
2. Reference: README.md → Implementation recommendations
3. Evaluate: 5 frameworks by category
4. Download: 1-2 papers matching your architecture

### Scenario 4: "I need to select papers for research"
1. Filter: cluster_3_metadata.csv by relevance/focus
2. Review: PAPER_INDEX.md for descriptions
3. Analyze: 20 papers across 4 focus areas
4. Download: Bulk script from PAPER_INDEX.md

### Scenario 5: "I'm new to agent security"
1. Start: QUICK_START.md complete (10 min)
2. Read: README.md sections (30 min)
3. Learn: Threat taxonomy (15 min)
4. Study: 3-4 papers from recommended list (120 min)

---

## Critical Numbers to Remember

- **73.5%** - Vulnerability rate in Function Calling
- **82.4%** - Peer-agent exploitation rate
- **91-96%** - Success rate for chained attacks
- **84%** - Prompt injection success in coding editors
- **63%** - Organizations without AI governance
- **38.5%** - Average agent safety score
- **3,250** - Attack scenarios tested
- **194,331** - Adversarial attacks in benchmark
- **31** - LLMs tested (all vulnerable)
- **70+** - MITRE ATT&CK techniques used
- **20** - Papers in this collection
- **17** - Papers from 2025
- **5** - Major authorization frameworks documented

---

## Access the Papers

All 20 papers are freely available on arXiv.org

**Quick Access**:
- Go to PAPER_INDEX.md
- Click any arXiv link (e.g., https://arxiv.org/abs/2510.25819)
- Click "PDF" to download

**Bulk Download**:
```bash
# Copy script from PAPER_INDEX.md
# Run in papers directory
# All 20 PDFs downloaded in ~5 minutes
```

**Direct URL Pattern**:
```
https://arxiv.org/abs/[ARXIV_ID]
https://arxiv.org/pdf/[ARXIV_ID]
```

---

## Next Steps

- [ ] Choose your role (Security/Architect/Governance/Research)
- [ ] Read appropriate section in QUICK_START.md
- [ ] Download recommended papers
- [ ] Schedule team briefing
- [ ] Begin 30-day implementation plan
- [ ] Monitor arXiv monthly for new research

---

## Questions?

This collection covers:
- What's the vulnerability? (Threat taxonomy)
- How bad is it? (Quantitative metrics)
- What can we do? (5 frameworks)
- How do we implement it? (30-day plan)
- Where's the research? (20 papers)

All answers are in these files. Start with your role.

---

*Cluster 3 - AI Agent Privilege Escalation & Authorization Risk*
*GitHub Issue #81 - KSI-CED-01_25-12A_GeneralTraining*
*January 6, 2026*
