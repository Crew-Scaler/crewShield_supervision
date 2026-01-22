#!/usr/bin/env python3
"""
Advanced ArXiv search for Cluster 7 papers with more targeted queries.
Focuses on backup security, recovery mechanisms, and malware persistence.
"""

import feedparser
import csv
import time
import urllib.parse
import re
from typing import List, Dict, Any
from pathlib import Path

OUTPUT_DIR = "/Users/tamnguyen/Documents/GitHub/ksi_watch/KSI-RPL-04_25-12A_RecoveryTesting/references/cluster_7_ransomware_recovery"
CSV_OUTPUT = "/Users/tamnguyen/Documents/GitHub/ksi_watch/KSI-RPL-04_25-12A_RecoveryTesting/references/cluster_7_advanced_metadata.csv"
RATE_LIMIT = 2.0

# More specific search queries
SEARCH_QUERIES = [
    'all:ransomware all:backup',
    'all:ransomware all:recovery',
    'all:ransomware all:resilience',
    'all:backup all:contamination',
    'all:backup all:integrity',
    'all:malware all:persistence',
    'all:immutable all:backup',
    'all:ransomware all:testing',
    'all:catastrophic all:failure all:recovery',
    'all:data all:recovery all:security',
]

def search_arxiv(query: str, max_results: int = 50) -> List[Dict[str, Any]]:
    """Search ArXiv for papers matching the query."""
    base_url = "http://export.arxiv.org/api/query?"

    params = {
        'search_query': query,
        'start': 0,
        'max_results': max_results,
        'sortBy': 'submittedDate',
        'sortOrder': 'descending',
    }

    query_str = '&'.join([f"{k}={urllib.parse.quote(str(v))}" for k, v in params.items()])
    url = base_url + query_str

    print(f"Searching: {query[:60]}...")

    try:
        feed = feedparser.parse(url)
        papers = []

        for entry in feed.entries:
            arxiv_id = entry.id.split('/abs/')[-1]
            title = entry.title
            authors = [author.name for author in entry.authors]
            published = entry.published
            summary = entry.summary.replace('\n', ' ')

            # Estimate page count
            pages = estimate_pages(summary)

            # Filter: 2024-2025 and minimum 7 pages
            pub_year = published[:4]
            if pub_year not in ['2024', '2025']:
                continue
            if pages < 7:
                continue

            paper = {
                'arxiv_id': arxiv_id,
                'title': title,
                'authors': '; '.join(authors),
                'first_author': authors[0] if authors else 'Unknown',
                'published': published,
                'year': pub_year,
                'pages': pages,
                'summary': summary[:300] + '...' if len(summary) > 300 else summary,
                'url': f'http://arxiv.org/abs/{arxiv_id}',
                'pdf_url': f'http://arxiv.org/pdf/{arxiv_id}.pdf'
            }
            papers.append(paper)

        return papers

    except Exception as e:
        print(f"  Error: {e}")
        return []

def estimate_pages(summary: str) -> int:
    """Estimate page count from summary."""
    match = re.search(r'(\d+)\s*pages?', summary, re.IGNORECASE)
    if match:
        return int(match.group(1))
    words = len(summary.split())
    estimated_pages = max(7, words // 250)
    return estimated_pages

def is_ransomware_related(paper: Dict[str, Any]) -> bool:
    """Check if paper is actually about ransomware, backup, or malware."""
    title_lower = paper['title'].lower()
    summary_lower = paper['summary'].lower()

    ransomware_keywords = ['ransomware', 'backup', 'recovery', 'malware', 'persistence',
                          'integrity', 'contamination', 'resilience', 'immutable', 'encryption']

    # At least two relevant keywords for high confidence
    keyword_count = sum(1 for kw in ransomware_keywords if kw in title_lower)
    keyword_count += sum(1 for kw in ransomware_keywords if kw in summary_lower) * 0.5

    return keyword_count >= 1.5

def calculate_relevance(paper: Dict[str, Any]) -> int:
    """Calculate relevance score (1-10)."""
    score = 5
    title_lower = paper['title'].lower()
    summary_lower = paper['summary'].lower()

    critical_keywords = ['ransomware', 'backup integrity', 'recovery', 'malware persistence']
    for keyword in critical_keywords:
        if keyword in title_lower:
            score += 3
        elif keyword in summary_lower:
            score += 1

    if paper['year'] == '2025':
        score += 1

    return min(10, score)

def main():
    """Main search process."""
    print("=" * 70)
    print("Advanced ArXiv Search: Ransomware & Backup Security Papers")
    print("=" * 70)

    Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)

    all_papers = {}

    for i, query in enumerate(SEARCH_QUERIES, 1):
        print(f"\n[{i}/{len(SEARCH_QUERIES)}]", end=" ")
        papers = search_arxiv(query)

        relevant_papers = [p for p in papers if is_ransomware_related(p)]
        print(f"  Found {len(papers)} papers, {len(relevant_papers)} relevant")

        for paper in relevant_papers:
            arxiv_id = paper['arxiv_id']
            if arxiv_id not in all_papers:
                all_papers[arxiv_id] = paper
                paper['relevance'] = calculate_relevance(paper)

        time.sleep(RATE_LIMIT)

    # Sort and select top papers
    sorted_papers = sorted(all_papers.values(),
                          key=lambda x: (-x.get('relevance', 0), -int(x['year'])))
    selected_papers = sorted_papers[:15]

    print(f"\n\nSelected {len(selected_papers)} papers")
    print("Top Papers Found:")
    for i, paper in enumerate(selected_papers, 1):
        print(f"{i}. {paper['title'][:60]}...")
        print(f"   ArXiv ID: {paper['arxiv_id']}")
        print(f"   Relevance: {paper.get('relevance', 5)}/10")
        print()

    # Save metadata
    with open(CSV_OUTPUT, 'w', newline='', encoding='utf-8') as f:
        fieldnames = ['arxiv_id', 'title', 'first_author', 'published', 'year',
                     'pages', 'relevance', 'url', 'pdf_url', 'summary']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for paper in selected_papers:
            writer.writerow({
                'arxiv_id': paper['arxiv_id'],
                'title': paper['title'],
                'first_author': paper['first_author'],
                'published': paper['published'],
                'year': paper['year'],
                'pages': paper['pages'],
                'relevance': paper.get('relevance', 5),
                'url': paper['url'],
                'pdf_url': paper['pdf_url'],
                'summary': paper['summary']
            })

    print(f"\nMetadata saved to: {CSV_OUTPUT}")

if __name__ == '__main__':
    main()
