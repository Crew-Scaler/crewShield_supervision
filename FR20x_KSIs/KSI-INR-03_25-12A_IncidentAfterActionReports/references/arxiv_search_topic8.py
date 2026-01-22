#!/usr/bin/env python3
"""
ArXiv Paper Search for Topic 8: Automated Cloud Remediation & Governance
Issue #76 - Ops Lessons Learned: AI-Driven Transformation & CSP Implications
"""

import arxiv
import time
import json
from datetime import datetime
from pathlib import Path

# Search keywords for Topic 8
SEARCH_QUERIES = [
    "cloud remediation AND (automated OR autonomous)",
    "cloud misconfiguration AND detection",
    "infrastructure as code AND (security OR governance)",
    "cloud configuration AND (automation OR drift)",
    "kubernetes AND (security OR misconfiguration)",
    "cloud compliance AND automation",
    "DevOps AND (governance OR security automation)",
    "cloud infrastructure AND (AI OR machine learning OR autonomous)",
]

# Additional focused queries
ADDITIONAL_QUERIES = [
    "serverless AND (security OR governance)",
    "container security AND automation",
    "cloud policy enforcement",
    "infrastructure automation AND security",
    "cloud resource management AND AI",
]

# US Universities and Companies to prioritize
PRIORITY_AFFILIATIONS = [
    'MIT', 'Stanford', 'Berkeley', 'CMU', 'Princeton', 'Harvard',
    'Google', 'Microsoft', 'Amazon', 'Meta', 'IBM', 'OpenAI',
    'Anthropic', 'DeepMind', 'NVIDIA'
]

def search_arxiv(query, max_results=20):
    """Search ArXiv with rate limiting"""
    print(f"\n[SEARCH] Query: '{query}'")

    client = arxiv.Client()
    search = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.SubmittedDate,
        sort_order=arxiv.SortOrder.Descending
    )

    results = []
    for result in client.results(search):
        results.append(result)

    print(f"[FOUND] {len(results)} papers")
    time.sleep(3)  # Respect ArXiv rate limits
    return results

def is_recent_paper(paper, start_year=2024):
    """Check if paper is from 2024-2025"""
    pub_date = paper.published
    return pub_date.year >= start_year

def has_priority_affiliation(paper):
    """Check if first author has priority affiliation"""
    if not paper.authors:
        return False

    first_author = str(paper.authors[0])
    # This is heuristic since ArXiv doesn't always include affiliation
    # We'll check the comment field and author string
    comment = paper.comment or ""

    for affiliation in PRIORITY_AFFILIATIONS:
        if affiliation.lower() in first_author.lower() or affiliation.lower() in comment.lower():
            return True
    return False

def estimate_pages(paper):
    """Estimate page count from comment field"""
    comment = paper.comment or ""

    # Look for explicit page mentions
    if 'pages' in comment.lower():
        import re
        match = re.search(r'(\d+)\s*pages?', comment, re.IGNORECASE)
        if match:
            return int(match.group(1))

    # Default: assume most CS papers are >7 pages
    return 15  # Conservative estimate

def is_relevant_topic(paper):
    """Check if paper is relevant to cloud remediation/governance"""
    text = f"{paper.title} {paper.summary}".lower()

    # Must have cloud-related terms
    cloud_terms = ['cloud', 'infrastructure', 'kubernetes', 'containeriz', 'aws', 'azure', 'gcp']
    has_cloud = any(term in text for term in cloud_terms)

    # Must have automation/governance terms
    automation_terms = [
        'remediation', 'auto-remediation', 'misconfiguration',
        'governance', 'compliance', 'automation', 'autonomous',
        'agent', 'policy', 'configuration', 'infrastructure-as-code',
        'iac', 'drift', 'security automation'
    ]
    has_automation = any(term in text for term in automation_terms)

    # Should have some AI/ML component
    ai_terms = ['ai', 'machine learning', 'ml', 'neural', 'deep learning', 'llm', 'language model']
    has_ai = any(term in text for term in ai_terms)

    # Penalize purely theoretical papers
    theoretical_terms = ['survey', 'taxonomy', 'ontology', 'framework comparison']
    is_theoretical = any(term in text for term in theoretical_terms)

    return has_cloud and has_automation and (has_ai or not is_theoretical)

def main():
    """Main search and filtering logic"""
    all_papers = {}

    # Search with all queries
    all_queries = SEARCH_QUERIES + ADDITIONAL_QUERIES

    for query in all_queries:
        papers = search_arxiv(query, max_results=30)

        for paper in papers:
            # Deduplicate by ArXiv ID
            arxiv_id = paper.entry_id.split('/abs/')[-1]

            if arxiv_id not in all_papers:
                all_papers[arxiv_id] = {
                    'arxiv_id': arxiv_id,
                    'title': paper.title,
                    'authors': [str(a) for a in paper.authors],
                    'published': paper.published.strftime('%Y-%m-%d'),
                    'summary': paper.summary,
                    'pdf_url': paper.pdf_url,
                    'categories': paper.categories,
                    'comment': paper.comment or '',
                    'is_recent': is_recent_paper(paper),
                    'has_priority': has_priority_affiliation(paper),
                    'estimated_pages': estimate_pages(paper),
                    'is_relevant': is_relevant_topic(paper),
                }

    print(f"\n[TOTAL] Found {len(all_papers)} unique papers")

    # Filter papers
    filtered_papers = []
    for arxiv_id, info in all_papers.items():
        if (info['is_recent'] and
            info['estimated_pages'] >= 7 and
            info['is_relevant']):
            filtered_papers.append(info)

    print(f"[FILTERED] {len(filtered_papers)} papers meet criteria (2024-2025, >7 pages, relevant)")

    # Sort by priority affiliation first, then by date
    filtered_papers.sort(
        key=lambda x: (not x['has_priority'], x['published']),
        reverse=False
    )

    # Take top 10
    top_papers = filtered_papers[:10]

    print(f"\n[SELECTED] Top {len(top_papers)} papers for download:")
    for i, paper in enumerate(top_papers, 1):
        priority_mark = "⭐" if paper['has_priority'] else "  "
        print(f"{i}. {priority_mark} [{paper['arxiv_id']}] {paper['title'][:80]}...")
        print(f"   Authors: {paper['authors'][0]} et al.")
        print(f"   Published: {paper['published']}")

    # Save results to JSON
    output_file = Path(__file__).parent / 'topic8_papers.json'
    with open(output_file, 'w') as f:
        json.dump(top_papers, f, indent=2)

    print(f"\n[SAVED] Results saved to {output_file}")

    return top_papers

if __name__ == '__main__':
    papers = main()
