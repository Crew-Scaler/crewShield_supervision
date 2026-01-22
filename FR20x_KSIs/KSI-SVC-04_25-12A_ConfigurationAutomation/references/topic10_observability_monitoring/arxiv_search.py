#!/usr/bin/env python3
"""
ArXiv paper search and download script for observability and behavioral monitoring.
Searches for papers on agent configuration monitoring with proper rate limiting.
"""

import requests
import json
import time
import os
import re
import urllib.parse
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any
import feedparser

# Configuration
BASE_URL = "http://export.arxiv.org/api/query?"
OUTPUT_DIR = Path("/Users/tamnguyen/Documents/GitHub/ksi_watch/KSI-SVC-04_25-12A_ConfigurationAutomation/references/topic10_observability_monitoring")
RATE_LIMIT_DELAY = 3.5  # seconds between requests
MAX_PAPERS_PER_QUERY = 100

# Search queries
QUERIES = [
    '(all:"distributed tracing") AND (all:agent OR all:autonomous) AND (all:configuration OR all:infrastructure) AND submittedDate:[202401010000 TO 202512312359]',
    '(all:"behavioral baseline") AND (all:agent OR all:configuration) AND (all:monitoring OR all:"anomaly detection") AND submittedDate:[202401010000 TO 202512312359]',
    '(all:"semantic drift") AND (all:configuration OR all:"intended outcome") AND (all:detection OR all:analysis) AND submittedDate:[202401010000 TO 202512312359]',
    'all:agent AND all:observability AND all:configuration AND submittedDate:[202401010000 TO 202512312359]',
    'all:"configuration monitoring" AND all:agent AND submittedDate:[202401010000 TO 202512312359]',
    'all:"behavioral monitoring" AND (all:agent OR all:autonomous) AND submittedDate:[202401010000 TO 202512312359]',
]

def sanitize_filename(text: str) -> str:
    """Convert text to filesystem-safe format."""
    text = text.lower()
    text = re.sub(r'[^a-z0-9_\-]', '_', text)
    text = re.sub(r'_+', '_', text)
    return text.strip('_')[:50]

def search_arxiv(query: str, start: int = 0, max_results: int = 50) -> List[Dict[str, Any]]:
    """Search ArXiv API with given query."""
    params = {
        'search_query': query,
        'start': start,
        'max_results': max_results,
        'sortBy': 'submittedDate',
        'sortOrder': 'descending'
    }

    url = BASE_URL + urllib.parse.urlencode(params)

    try:
        print(f"Fetching: {url[:100]}...")
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        feed = feedparser.parse(response.content)
        papers = []

        for entry in feed.entries:
            paper = {
                'arxiv_id': entry.id.split('/abs/')[-1],
                'title': entry.title,
                'authors': [author.name for author in entry.authors],
                'published': entry.published,
                'summary': entry.summary,
                'categories': entry.get('arxiv_primary_category', {}).get('term', 'Unknown'),
                'pdf_url': entry.id.replace('abs', 'pdf') + '.pdf',
                'abs_url': entry.id
            }
            papers.append(paper)

        return papers
    except Exception as e:
        print(f"Error searching ArXiv: {e}")
        return []

def download_pdf(pdf_url: str, filename: str) -> bool:
    """Download PDF from ArXiv."""
    try:
        print(f"Downloading: {filename}...")
        response = requests.get(pdf_url, timeout=30)
        response.raise_for_status()

        filepath = OUTPUT_DIR / filename
        with open(filepath, 'wb') as f:
            f.write(response.content)

        print(f"✓ Saved: {filename}")
        return True
    except Exception as e:
        print(f"✗ Failed to download {filename}: {e}")
        return False

def extract_year(published_date: str) -> int:
    """Extract year from ISO format date."""
    try:
        return int(published_date[:4])
    except:
        return 2024

def score_paper(paper: Dict[str, Any], query_num: int) -> float:
    """Score paper relevance (higher = more relevant)."""
    score = 0.0

    # Year preference (2025 > 2024)
    year = extract_year(paper['published'])
    if year == 2025:
        score += 100
    elif year == 2024:
        score += 50

    # Affiliation preference (heuristic from title/authors)
    top_institutions = ['stanford', 'mit', 'cmu', 'google', 'aws', 'meta', 'berkeley', 'caltech', 'harvard']
    author_str = ' '.join(paper['authors']).lower()
    for inst in top_institutions:
        if inst in author_str:
            score += 30
            break

    # Topic relevance
    title_lower = paper['title'].lower()
    summary_lower = paper['summary'].lower()
    full_text = title_lower + ' ' + summary_lower

    # Core topic keywords
    if 'agent' in full_text:
        score += 20
    if 'configuration' in full_text:
        score += 20
    if 'observability' in full_text or 'monitoring' in full_text:
        score += 25
    if 'behavioral' in full_text:
        score += 15
    if 'semantic' in full_text or 'drift' in full_text:
        score += 15
    if 'distributed' in full_text or 'tracing' in full_text:
        score += 15

    # Category relevance
    if paper['categories'] in ['cs.AI', 'cs.MA', 'cs.LG', 'cs.SE', 'cs.SY']:
        score += 10

    return score

def main():
    """Main search and download function."""
    print("=" * 80)
    print("ArXiv Paper Search: Observability and Behavioral Monitoring")
    print("=" * 80)

    all_papers = {}  # arxiv_id -> paper

    # Execute searches
    for i, query in enumerate(QUERIES, 1):
        print(f"\n[Query {i}/{len(QUERIES)}]")
        print(f"Query: {query[:80]}...")

        papers = search_arxiv(query, max_results=MAX_PAPERS_PER_QUERY)
        print(f"Found {len(papers)} papers")

        for paper in papers:
            arxiv_id = paper['arxiv_id']
            if arxiv_id not in all_papers:
                all_papers[arxiv_id] = paper
                all_papers[arxiv_id]['query_matches'] = [i]
            else:
                all_papers[arxiv_id]['query_matches'].append(i)

        time.sleep(RATE_LIMIT_DELAY)

    # Score and sort papers
    print(f"\n[Processing] Total unique papers found: {len(all_papers)}")

    scored_papers = []
    for arxiv_id, paper in all_papers.items():
        paper['score'] = score_paper(paper, 1)
        scored_papers.append(paper)

    scored_papers.sort(key=lambda x: (-x['score'], -extract_year(x['published']), x['arxiv_id']))

    # Separate into top 10 and archived
    top_papers = scored_papers[:10]
    archived_papers = scored_papers[10:]

    print(f"\n[Results]")
    print(f"Total papers: {len(scored_papers)}")
    print(f"Top 10 (to download): {len(top_papers)}")
    print(f"Archived (low relevance): {len(archived_papers)}")

    # Download top papers
    print(f"\n[Downloading Top 10 Papers]")
    downloaded_papers = []

    for i, paper in enumerate(top_papers, 1):
        arxiv_id = paper['arxiv_id']
        year = extract_year(paper['published'])
        title_slug = sanitize_filename(paper['title'])
        filename = f"{year}_{arxiv_id.replace('/', '_')}_{title_slug}.pdf"

        print(f"\n{i}. {paper['title'][:60]}...")
        print(f"   ArXiv: {arxiv_id} | Year: {year} | Score: {paper['score']:.1f}")

        if download_pdf(paper['pdf_url'], filename):
            paper['local_filename'] = filename
            paper['download_status'] = 'downloaded'
            downloaded_papers.append(paper)
        else:
            paper['download_status'] = 'failed'

        if i < len(top_papers):
            time.sleep(RATE_LIMIT_DELAY)

    # Archive low relevance papers
    print(f"\n[Archiving {len(archived_papers)} Low-Relevance Papers]")
    archived_metadata = {
        'total_archived': len(archived_papers),
        'papers': []
    }

    for paper in archived_papers:
        archived_metadata['papers'].append({
            'arxiv_id': paper['arxiv_id'],
            'title': paper['title'],
            'year': extract_year(paper['published']),
            'score': paper['score'],
            'authors': paper['authors'][:3],
            'categories': paper['categories'],
            'reason_archived': 'Lower relevance score'
        })

    # Save metadata
    print("\n[Saving Metadata]")

    metadata = {
        'search_date': datetime.now().isoformat(),
        'search_queries': QUERIES,
        'total_papers_found': len(scored_papers),
        'downloaded_papers': len(downloaded_papers),
        'archived_papers': len(archived_papers),
        'downloaded': [
            {
                'arxiv_id': p['arxiv_id'],
                'title': p['title'],
                'year': extract_year(p['published']),
                'score': p['score'],
                'authors': p['authors'],
                'categories': p['categories'],
                'local_filename': p.get('local_filename'),
                'summary': p['summary'][:500] + ('...' if len(p['summary']) > 500 else '')
            }
            for p in downloaded_papers
        ],
        'archived': archived_metadata['papers']
    }

    metadata_path = OUTPUT_DIR / 'metadata.json'
    with open(metadata_path, 'w') as f:
        json.dump(metadata, f, indent=2)

    print(f"✓ Metadata saved to {metadata_path}")

    return downloaded_papers, archived_papers

if __name__ == '__main__':
    downloaded, archived = main()
    print("\n" + "=" * 80)
    print(f"FINAL SUMMARY: Downloaded {len(downloaded)} papers, Archived {len(archived)} papers")
    print("=" * 80)
