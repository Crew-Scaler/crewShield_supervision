#!/usr/bin/env python3
"""
Research Analysis: AI Agent Behavioral Anomaly Detection
Analyze downloaded papers for key findings on:
1. Baseline construction methods for non-human behavior
2. Baseline poisoning attacks and defenses
3. Model drift rates (validating 2-5% monthly claim)
4. Context-aware authentication frameworks
"""

import json
from pathlib import Path
from typing import Dict, List, Tuple
from collections import Counter, defaultdict
import re

METADATA_FILE = Path("/Users/tamnguyen/Documents/GitHub/ksi_watch/KSI-IAM-03_25-12A_Non-UserAccounts/references/behavioral_detection/papers_metadata.json")
OUTPUT_FILE = Path("/Users/tamnguyen/Documents/GitHub/ksi_watch/KSI-IAM-03_25-12A_Non-UserAccounts/references/behavioral_detection/RESEARCH_ANALYSIS.md")

def load_metadata() -> Dict:
    """Load papers metadata"""
    with open(METADATA_FILE, 'r') as f:
        return json.load(f)

def analyze_baseline_construction(papers: List[Dict]) -> Dict:
    """Analyze papers for baseline construction methods"""
    baseline_papers = []
    methods = defaultdict(list)

    keywords = [
        "baseline construction", "baseline learning", "baseline establishment",
        "behavioral profile", "behavior profile", "profile construction",
        "behavioral baseline", "normal behavior", "baseline model"
    ]

    for paper in papers:
        text = (paper["title"] + " " + paper["abstract"]).lower()

        for keyword in keywords:
            if keyword in text:
                baseline_papers.append({
                    "title": paper["title"],
                    "paper_id": paper["paper_id"],
                    "published": paper["published"],
                    "relevance_score": paper["relevance_score"],
                    "matched_keyword": keyword,
                    "abstract": paper["abstract"][:500]
                })
                break

    return {
        "count": len(baseline_papers),
        "papers": baseline_papers
    }

def analyze_poisoning_attacks(papers: List[Dict]) -> Dict:
    """Analyze papers for baseline poisoning and adversarial attacks"""
    poisoning_papers = []
    attack_types = defaultdict(int)

    keywords = {
        "baseline poisoning": "baseline_poisoning",
        "data poisoning": "data_poisoning",
        "backdoor attack": "backdoor",
        "adversarial attack": "adversarial",
        "evasion attack": "evasion",
        "poisoning attack": "poisoning"
    }

    for paper in papers:
        text = (paper["title"] + " " + paper["abstract"]).lower()

        matched = []
        for keyword, attack_type in keywords.items():
            if keyword in text:
                matched.append(keyword)
                attack_types[attack_type] += 1

        if matched:
            poisoning_papers.append({
                "title": paper["title"],
                "paper_id": paper["paper_id"],
                "published": paper["published"],
                "relevance_score": paper["relevance_score"],
                "attack_types": matched,
                "has_defense": any(term in text for term in ["defense", "mitigation", "robust", "detection"]),
                "abstract": paper["abstract"][:500]
            })

    return {
        "count": len(poisoning_papers),
        "attack_types": dict(attack_types),
        "papers": poisoning_papers
    }

def analyze_model_drift(papers: List[Dict]) -> Dict:
    """Analyze papers for model drift and degradation rates"""
    drift_papers = []
    drift_metrics = []

    keywords = [
        "model drift", "concept drift", "baseline drift", "drift detection",
        "degradation", "decay", "performance degradation"
    ]

    # Regex patterns for extracting numeric drift rates
    percentage_pattern = r'(\d+\.?\d*)\s*%\s*(?:drift|degradation|decay|drop)'
    monthly_pattern = r'(?:monthly|per month|month)'

    for paper in papers:
        text = (paper["title"] + " " + paper["abstract"]).lower()

        for keyword in keywords:
            if keyword in text:
                # Try to extract drift rates
                percentages = re.findall(percentage_pattern, text)
                has_monthly = monthly_pattern in text

                drift_papers.append({
                    "title": paper["title"],
                    "paper_id": paper["paper_id"],
                    "published": paper["published"],
                    "relevance_score": paper["relevance_score"],
                    "matched_keyword": keyword,
                    "extracted_rates": percentages if percentages else None,
                    "mentions_monthly": has_monthly,
                    "abstract": paper["abstract"][:500]
                })

                if percentages:
                    drift_metrics.extend([(float(p), paper["title"][:60]) for p in percentages])

                break

    return {
        "count": len(drift_papers),
        "papers": drift_papers,
        "extracted_metrics": drift_metrics
    }

def analyze_context_aware_auth(papers: List[Dict]) -> Dict:
    """Analyze papers for context-aware authentication"""
    context_papers = []

    keywords = [
        "context-aware authentication", "contextual authentication",
        "adaptive authentication", "context-aware", "contextual security",
        "adaptive security", "dynamic authentication"
    ]

    for paper in papers:
        text = (paper["title"] + " " + paper["abstract"]).lower()

        for keyword in keywords:
            if keyword in text:
                has_behavioral = any(term in text for term in ["behavioral", "behaviour", "behavior"])
                has_realtime = any(term in text for term in ["real-time", "runtime", "continuous"])

                context_papers.append({
                    "title": paper["title"],
                    "paper_id": paper["paper_id"],
                    "published": paper["published"],
                    "relevance_score": paper["relevance_score"],
                    "matched_keyword": keyword,
                    "has_behavioral": has_behavioral,
                    "has_realtime": has_realtime,
                    "abstract": paper["abstract"][:500]
                })
                break

    return {
        "count": len(context_papers),
        "papers": context_papers
    }

def analyze_agent_specific(papers: List[Dict]) -> Dict:
    """Analyze papers specifically about AI agents"""
    agent_papers = []

    keywords = [
        "ai agent", "autonomous agent", "intelligent agent",
        "multi-agent", "agent system", "agentic"
    ]

    for paper in papers:
        text = (paper["title"] + " " + paper["abstract"]).lower()

        for keyword in keywords:
            if keyword in text:
                has_authentication = any(term in text for term in ["authentication", "identity", "credential"])
                has_behavioral = any(term in text for term in ["behavioral", "behaviour", "behavior"])
                has_monitoring = any(term in text for term in ["monitoring", "detection", "surveillance"])

                agent_papers.append({
                    "title": paper["title"],
                    "paper_id": paper["paper_id"],
                    "published": paper["published"],
                    "relevance_score": paper["relevance_score"],
                    "matched_keyword": keyword,
                    "has_authentication": has_authentication,
                    "has_behavioral": has_behavioral,
                    "has_monitoring": has_monitoring,
                    "abstract": paper["abstract"][:500]
                })
                break

    return {
        "count": len(agent_papers),
        "papers": agent_papers
    }

def analyze_empirical_evidence(papers: List[Dict]) -> Dict:
    """Analyze papers for empirical evidence and deployments"""
    empirical_papers = []

    keywords = [
        "evaluation", "experiment", "empirical", "case study",
        "deployment", "production", "real-world", "implementation"
    ]

    metrics_keywords = [
        "accuracy", "precision", "recall", "f1", "f-measure",
        "false positive", "false negative", "tpr", "fpr",
        "detection rate", "performance"
    ]

    for paper in papers:
        text = (paper["title"] + " " + paper["abstract"]).lower()

        empirical_match = [k for k in keywords if k in text]
        metrics_match = [k for k in metrics_keywords if k in text]

        if empirical_match:
            empirical_papers.append({
                "title": paper["title"],
                "paper_id": paper["paper_id"],
                "published": paper["published"],
                "relevance_score": paper["relevance_score"],
                "empirical_indicators": empirical_match,
                "has_metrics": bool(metrics_match),
                "metrics_mentioned": metrics_match,
                "abstract": paper["abstract"][:500]
            })

    return {
        "count": len(empirical_papers),
        "papers": empirical_papers
    }

def generate_markdown_report(data: Dict) -> str:
    """Generate comprehensive markdown report"""

    report = f"""# ArXiv Research Analysis: AI Agent Behavioral Anomaly Detection

**Research Date:** {data['metadata']['search_date'][:10]}
**Total Papers Analyzed:** {data['metadata']['total_papers']}
**Analysis Date:** {data['analysis_date']}

## Executive Summary

This analysis examines {data['metadata']['total_papers']} recent papers (2024-2025) on behavioral anomaly detection for AI agents, focusing on baseline construction, poisoning attacks, model drift, and context-aware authentication.

### Key Findings Summary

- **Baseline Construction Papers:** {data['baseline_construction']['count']} papers
- **Poisoning/Adversarial Attack Papers:** {data['poisoning_attacks']['count']} papers
- **Model Drift Papers:** {data['model_drift']['count']} papers
- **Context-Aware Authentication Papers:** {data['context_aware_auth']['count']} papers
- **AI Agent-Specific Papers:** {data['agent_specific']['count']} papers
- **Empirical Studies:** {data['empirical_evidence']['count']} papers

---

## 1. Baseline Construction for Non-Human Agent Behavior

**Papers Found:** {data['baseline_construction']['count']}

### Key Papers

"""

    # Baseline construction papers
    for i, paper in enumerate(data['baseline_construction']['papers'][:10], 1):
        report += f"""
#### {i}. {paper['title']}

- **Paper ID:** `{paper['paper_id']}`
- **Published:** {paper['published']}
- **Relevance Score:** {paper['relevance_score']:.1f}
- **Matched Keywords:** {paper['matched_keyword']}
- **ArXiv:** https://arxiv.org/abs/{paper['paper_id']}

**Abstract Preview:** {paper['abstract']}...

"""

    # Poisoning attacks
    report += f"""

---

## 2. Baseline Poisoning Attacks and Defenses

**Papers Found:** {data['poisoning_attacks']['count']}

### Attack Type Distribution

"""

    for attack_type, count in sorted(data['poisoning_attacks']['attack_types'].items(), key=lambda x: x[1], reverse=True):
        report += f"- **{attack_type}:** {count} papers\n"

    report += "\n### Key Papers\n"

    for i, paper in enumerate(data['poisoning_attacks']['papers'][:10], 1):
        defense_status = "✓ Includes defense/mitigation" if paper['has_defense'] else "✗ Attack-only"
        report += f"""
#### {i}. {paper['title']}

- **Paper ID:** `{paper['paper_id']}`
- **Published:** {paper['published']}
- **Relevance Score:** {paper['relevance_score']:.1f}
- **Attack Types:** {', '.join(paper['attack_types'])}
- **Defense Coverage:** {defense_status}
- **ArXiv:** https://arxiv.org/abs/{paper['paper_id']}

**Abstract Preview:** {paper['abstract']}...

"""

    # Model drift
    report += f"""

---

## 3. Model Drift Rates and Baseline Degradation

**Papers Found:** {data['model_drift']['count']}

### Validation of 2-5% Monthly Drift Claim

"""

    if data['model_drift']['extracted_metrics']:
        report += "**Extracted Drift Rates from Papers:**\n\n"
        for rate, title in data['model_drift']['extracted_metrics'][:15]:
            report += f"- **{rate}%** - {title}...\n"
    else:
        report += "*Note: Specific numeric drift rates were not explicitly stated in abstracts. Full paper review required for validation.*\n"

    report += "\n### Key Papers\n"

    for i, paper in enumerate(data['model_drift']['papers'][:12], 1):
        monthly_indicator = "✓ Mentions monthly intervals" if paper['mentions_monthly'] else ""
        rates = f"Extracted rates: {', '.join(paper['extracted_rates'])}%" if paper['extracted_rates'] else "No specific rates in abstract"

        report += f"""
#### {i}. {paper['title']}

- **Paper ID:** `{paper['paper_id']}`
- **Published:** {paper['published']}
- **Relevance Score:** {paper['relevance_score']:.1f}
- **Drift Metrics:** {rates}
- **{monthly_indicator}**
- **ArXiv:** https://arxiv.org/abs/{paper['paper_id']}

**Abstract Preview:** {paper['abstract']}...

"""

    # Context-aware authentication
    report += f"""

---

## 4. Context-Aware Authentication Frameworks

**Papers Found:** {data['context_aware_auth']['count']}

### Key Papers

"""

    for i, paper in enumerate(data['context_aware_auth']['papers'][:8], 1):
        behavioral = "✓ Behavioral" if paper['has_behavioral'] else "✗"
        realtime = "✓ Real-time" if paper['has_realtime'] else "✗"

        report += f"""
#### {i}. {paper['title']}

- **Paper ID:** `{paper['paper_id']}`
- **Published:** {paper['published']}
- **Relevance Score:** {paper['relevance_score']:.1f}
- **Matched Keyword:** {paper['matched_keyword']}
- **Features:** {behavioral} | {realtime}
- **ArXiv:** https://arxiv.org/abs/{paper['paper_id']}

**Abstract Preview:** {paper['abstract']}...

"""

    # AI Agent specific
    report += f"""

---

## 5. AI Agent-Specific Security Research

**Papers Found:** {data['agent_specific']['count']}

These papers specifically address AI agents, autonomous agents, or intelligent agent systems.

### Key Papers

"""

    for i, paper in enumerate(data['agent_specific']['papers'][:8], 1):
        auth = "✓" if paper['has_authentication'] else "✗"
        behav = "✓" if paper['has_behavioral'] else "✗"
        mon = "✓" if paper['has_monitoring'] else "✗"

        report += f"""
#### {i}. {paper['title']}

- **Paper ID:** `{paper['paper_id']}`
- **Published:** {paper['published']}
- **Relevance Score:** {paper['relevance_score']:.1f}
- **Agent Type:** {paper['matched_keyword']}
- **Coverage:** Authentication {auth} | Behavioral {behav} | Monitoring {mon}
- **ArXiv:** https://arxiv.org/abs/{paper['paper_id']}

**Abstract Preview:** {paper['abstract']}...

"""

    # Empirical evidence
    report += f"""

---

## 6. Empirical Evidence and Production Deployments

**Papers Found:** {data['empirical_evidence']['count']}

Papers with empirical evaluations, experiments, or real-world deployments.

### Top Papers with Measured Performance

"""

    empirical_with_metrics = [p for p in data['empirical_evidence']['papers'] if p['has_metrics']][:10]

    for i, paper in enumerate(empirical_with_metrics, 1):
        report += f"""
#### {i}. {paper['title']}

- **Paper ID:** `{paper['paper_id']}`
- **Published:** {paper['published']}
- **Relevance Score:** {paper['relevance_score']:.1f}
- **Empirical Indicators:** {', '.join(paper['empirical_indicators'])}
- **Metrics Mentioned:** {', '.join(paper['metrics_mentioned'])}
- **ArXiv:** https://arxiv.org/abs/{paper['paper_id']}

**Abstract Preview:** {paper['abstract']}...

"""

    # Category breakdown
    report += f"""

---

## 7. Research Categories Distribution

### Papers by Search Category

"""

    category_counts = Counter([p['search_category'] for p in data['metadata']['papers']])
    for category, count in sorted(category_counts.items(), key=lambda x: x[1], reverse=True):
        report += f"- **{category}:** {count} papers\n"

    # Year distribution
    report += "\n### Papers by Publication Year\n\n"
    year_counts = Counter([p['published'][:4] for p in data['metadata']['papers']])
    for year, count in sorted(year_counts.items(), reverse=True):
        report += f"- **{year}:** {count} papers\n"

    # Final recommendations
    report += """

---

## 8. Research Validation and Recommendations

### Baseline Construction Methods

The research corpus includes multiple approaches to behavioral baseline construction:
- Machine learning-based profiling
- Statistical baseline establishment
- Adaptive baseline learning
- Profile construction from historical data

**Recommendation:** Review papers focusing on "baseline construction" and "behavioral profiling" for specific methodologies applicable to non-human agents.

### Baseline Poisoning Attacks

"""

    if data['poisoning_attacks']['count'] > 0:
        report += f"""Found {data['poisoning_attacks']['count']} papers addressing poisoning and adversarial attacks on detection systems. Key attack vectors include:
"""
        for attack_type in data['poisoning_attacks']['attack_types'].keys():
            report += f"- {attack_type.replace('_', ' ').title()}\n"

        defense_papers = sum(1 for p in data['poisoning_attacks']['papers'] if p['has_defense'])
        report += f"\n**Defense Coverage:** {defense_papers}/{data['poisoning_attacks']['count']} papers include defense/mitigation strategies.\n"
    else:
        report += "Limited papers specifically on baseline poisoning attacks found. This remains a research gap.\n"

    report += """

### Model Drift Rate Validation (2-5% Monthly Claim)

"""

    if data['model_drift']['extracted_metrics']:
        report += f"""**Status:** PARTIAL VALIDATION
- Found {len(data['model_drift']['extracted_metrics'])} papers with extracted drift metrics
- Specific rates require full paper analysis to validate the 2-5% monthly claim
- Many papers address concept drift but don't specify monthly degradation rates in abstracts

**Recommendation:** Conduct detailed review of the {data['model_drift']['count']} drift-related papers to extract:
1. Specific monthly degradation percentages
2. Baseline model types affected
3. Domain-specific drift rates
4. Mitigation strategies
"""
    else:
        report += """**Status:** REQUIRES FULL PAPER REVIEW
- Abstracts don't contain specific numeric drift rates
- Papers address drift conceptually but need detailed analysis
- The 2-5% monthly claim requires validation from full paper content

**Recommendation:** Prioritize full-text analysis of model_drift_behavioral papers.
"""

    report += """

### Context-Aware Authentication

"""

    if data['context_aware_auth']['count'] > 0:
        behavioral_count = sum(1 for p in data['context_aware_auth']['papers'] if p.get('has_behavioral'))
        realtime_count = sum(1 for p in data['context_aware_auth']['papers'] if p.get('has_realtime'))

        report += f"""**Status:** EVIDENCE FOUND
- {data['context_aware_auth']['count']} papers on context-aware authentication
- {behavioral_count} include behavioral components
- {realtime_count} address real-time/continuous monitoring

**Recommendation:** These papers provide frameworks applicable to autonomous agent authentication.
"""
    else:
        report += "**Status:** LIMITED EVIDENCE - Research gap identified.\n"

    # Next steps
    report += """

---

## 9. Next Steps for Research Validation

### Priority 1: Detailed Paper Analysis
1. **Model Drift Papers (28 papers):** Extract specific drift rates, methodologies, and validation data
2. **Poisoning Attack Papers:** Analyze attack success rates and defense effectiveness
3. **Baseline Construction Papers:** Document ML approaches for non-human behavior profiling

### Priority 2: Evidence Extraction
- False positive/negative rates for behavioral anomaly detection
- Baseline construction time and data requirements
- Real-world deployment case studies
- Performance metrics for agent authentication systems

### Priority 3: Gap Analysis
- Identify areas lacking empirical evidence
- Note missing validation for specific claims
- Document need for additional research

### Priority 4: Synthesis
- Create evidence matrix for Issue #16 claims
- Map papers to specific architectural components
- Generate recommendations for implementation

---

## 10. Full Paper List

### All Downloaded Papers

"""

    for i, paper in enumerate(sorted(data['metadata']['papers'], key=lambda x: x['relevance_score'], reverse=True), 1):
        report += f"""
**{i}. {paper['title']}**
- Paper ID: `{paper['paper_id']}`
- Published: {paper['published']}
- Relevance: {paper['relevance_score']:.1f}
- Category: {paper['search_category']}
- ArXiv: https://arxiv.org/abs/{paper['paper_id']}
- File: `{paper['filename']}`

"""

    report += """

---

## Appendix: Search Queries Used

The following ArXiv search queries were executed:

1. Behavioral anomaly detection for AI agents
2. Baseline poisoning and adversarial attacks
3. Model drift in behavioral systems
4. Context-aware authentication
5. Baseline construction methods
6. Real-time behavioral monitoring
7. ML-based anomaly detection for agents
8. Adversarial attacks on behavioral detection
9. Non-human behavior characterization
10. Behavioral biometrics for authentication
11. Agent authentication and identity
12. Behavioral profiling and fingerprinting
13. Continuous monitoring and verification
14. Adversarial ML for security
15. Time series anomaly detection
16. Data poisoning and backdoor attacks
17. Zero-day detection
18. Adaptive security and dynamic baselines

---

*Analysis generated for Issue #16: AI Agent Authentication, Behavioral Analysis, and Secure Identity Management*
"""

    return report

def main():
    """Main analysis execution"""
    print("="*80)
    print("Analyzing Research Findings")
    print("="*80)

    # Load metadata
    metadata = load_metadata()
    papers = metadata['papers']

    print(f"\nTotal papers to analyze: {len(papers)}")
    print("\nExecuting analysis...")

    # Run all analyses
    print("  - Analyzing baseline construction methods...")
    baseline_analysis = analyze_baseline_construction(papers)

    print("  - Analyzing poisoning attacks...")
    poisoning_analysis = analyze_poisoning_attacks(papers)

    print("  - Analyzing model drift rates...")
    drift_analysis = analyze_model_drift(papers)

    print("  - Analyzing context-aware authentication...")
    context_analysis = analyze_context_aware_auth(papers)

    print("  - Analyzing agent-specific research...")
    agent_analysis = analyze_agent_specific(papers)

    print("  - Analyzing empirical evidence...")
    empirical_analysis = analyze_empirical_evidence(papers)

    # Compile results
    analysis_data = {
        "analysis_date": "2025-12-11",
        "metadata": metadata,
        "baseline_construction": baseline_analysis,
        "poisoning_attacks": poisoning_analysis,
        "model_drift": drift_analysis,
        "context_aware_auth": context_analysis,
        "agent_specific": agent_analysis,
        "empirical_evidence": empirical_analysis
    }

    # Generate report
    print("\nGenerating markdown report...")
    report = generate_markdown_report(analysis_data)

    # Save report
    with open(OUTPUT_FILE, 'w') as f:
        f.write(report)

    print(f"\n✓ Analysis complete!")
    print(f"✓ Report saved to: {OUTPUT_FILE}")

    # Summary statistics
    print("\n" + "="*80)
    print("ANALYSIS SUMMARY")
    print("="*80)
    print(f"Total papers analyzed: {len(papers)}")
    print(f"Baseline construction papers: {baseline_analysis['count']}")
    print(f"Poisoning attack papers: {poisoning_analysis['count']}")
    print(f"Model drift papers: {drift_analysis['count']}")
    print(f"Context-aware auth papers: {context_analysis['count']}")
    print(f"Agent-specific papers: {agent_analysis['count']}")
    print(f"Empirical studies: {empirical_analysis['count']}")
    print("="*80)

if __name__ == "__main__":
    main()
