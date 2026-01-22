#!/usr/bin/env python3
"""
ArXiv paper searcher for Cluster 7: Ransomware Recovery & Backup Integrity Testing
Searches for papers on ransomware resilience, backup integrity, and recovery validation.
"""

import feedparser
import csv
import time
import os
from datetime import datetime
from typing import List, Dict, Any
from pathlib import Path
import urllib.request
import urllib.error
import urllib.parse

# Configuration
OUTPUT_DIR = "/Users/tamnguyen/Documents/GitHub/ksi_watch/KSI-RPL-04_25-12A_RecoveryTesting/references/cluster_7_ransomware_recovery"
CSV_OUTPUT = "/Users/tamnguyen/Documents/GitHub/ksi_watch/KSI-RPL-04_25-12A_RecoveryTesting/references/cluster_7_metadata.csv"
RATE_LIMIT = 3.0  # seconds between requests (to respect ArXiv rate limits)
MAX_PAPERS_PER_QUERY = 50
YEAR_FILTER = "2024-2025"

# Search queries focused on ransomware recovery and backup integrity
SEARCH_QUERIES = [
    'ransomware recovery',
    'ransomware backup',
    'backup integrity malware',
    'backup contamination',
    'ransomware resilience',
    'ransomware testing',
    'malware persistence',
    'immutable backup',
    'backup security',
    'ransomware detection recovery',
]

def search_arxiv(query: str, max_results: int = MAX_PAPERS_PER_QUERY) -> List[Dict[str, Any]]:
    """
    Search ArXiv for papers matching the query.
    Returns list of paper metadata.
    """
    base_url = "http://export.arxiv.org/api/query?"
    params = {
        'search_query': query,
        'start': 0,
        'max_results': max_results,
        'sortBy': 'submittedDate',
        'sortOrder': 'descending',
    }

    # Build query string
    query_str = '&'.join([f"{k}={urllib.parse.quote(str(v))}" for k, v in params.items()])
    url = base_url + query_str

    print(f"Searching: {query[:60]}...")

    try:
        feed = feedparser.parse(url)
        papers = []

        for entry in feed.entries:
            # Extract metadata
            arxiv_id = entry.id.split('/abs/')[-1]
            title = entry.title
            authors = [author.name for author in entry.authors]
            published = entry.published

            # Extract page count from summary or estimate
            summary = entry.summary.replace('\n', ' ')

            # Try to get page count from summary
            pages = estimate_pages(summary)

            # Filter: only papers from 2024-2025 and at least 7 pages
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
        print(f"Error searching ArXiv: {e}")
        return []

def estimate_pages(summary: str) -> int:
    """Estimate page count from summary or default to 10."""
    # Look for page count in summary
    import re
    match = re.search(r'(\d+)\s*pages?', summary, re.IGNORECASE)
    if match:
        return int(match.group(1))

    # Default estimate based on summary length
    words = len(summary.split())
    estimated_pages = max(7, words // 250)  # Rough estimate: ~250 words per page
    return estimated_pages

def download_pdf(pdf_url: str, arxiv_id: str) -> bool:
    """Download PDF from ArXiv using curl with advanced options."""
    filename = os.path.join(OUTPUT_DIR, f"{arxiv_id.replace('/', '_')}.pdf")

    if os.path.exists(filename):
        print(f"  Already exists: {arxiv_id}")
        return True

    try:
        print(f"  Downloading: {arxiv_id}", end=" ", flush=True)

        # Use curl with advanced options to bypass cloudflare
        import subprocess
        cmd = [
            'curl', '-L', '--compressed',
            '--max-time', '120',
            '--retry', '5',
            '--retry-delay', '3',
            '--retry-max-time', '300',
            '-H', 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            '-H', 'Accept: */*',
            '-H', 'Accept-Encoding: gzip, deflate',
            '--cookie', 'cookie.txt',
            '--cookie-jar', 'cookie.txt',
            '-b', 'cookie.txt',
            '-c', 'cookie.txt',
            '-o', filename,
            '-w', '\n%{http_code}',
            pdf_url
        ]

        result = subprocess.run(cmd, capture_output=True, text=True, timeout=350, cwd=OUTPUT_DIR)
        output_lines = result.stdout.strip().split('\n')
        http_code = output_lines[-1] if output_lines else '000'

        if result.returncode == 0 and http_code.isdigit() and int(http_code) == 200:
            print("OK")
            time.sleep(RATE_LIMIT)
            return True
        else:
            print(f"FAILED (HTTP {http_code}, return code {result.returncode})")
            if os.path.exists(filename):
                os.remove(filename)
            return False
    except subprocess.TimeoutExpired:
        print("FAILED (Timeout)")
        if os.path.exists(filename):
            os.remove(filename)
        return False
    except Exception as e:
        print(f"FAILED ({type(e).__name__}: {str(e)[:30]})")
        if os.path.exists(filename):
            os.remove(filename)
        return False

def calculate_relevance(paper: Dict[str, Any], query: str) -> int:
    """Calculate relevance score (1-10) based on title and summary."""
    score = 5  # Base score

    title_lower = paper['title'].lower()
    summary_lower = paper['summary'].lower()

    # Keywords for relevance
    high_relevance_words = [
        'ransomware', 'backup', 'recovery', 'malware', 'persistence',
        'integrity', 'immutable', 'contamination', 'validation', 'resilience'
    ]

    critical_keywords = ['ransomware', 'backup integrity', 'recovery']

    # Check critical keywords
    for keyword in critical_keywords:
        if keyword in title_lower:
            score += 2
        elif keyword in summary_lower:
            score += 1

    # Check other high relevance words
    for word in high_relevance_words:
        if word in title_lower:
            score += 1

    # Prefer recent papers
    if paper['year'] == '2025':
        score += 1

    return min(10, score)

def main():
    """Main search and download process."""
    print("=" * 70)
    print("ArXiv Paper Search: Cluster 7 - Ransomware Recovery & Backup Integrity")
    print("=" * 70)

    # Ensure output directory exists
    Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)

    all_papers = {}

    # Search using all queries
    for i, query in enumerate(SEARCH_QUERIES, 1):
        print(f"\n[{i}/{len(SEARCH_QUERIES)}] Executing search query...")
        papers = search_arxiv(query)

        for paper in papers:
            arxiv_id = paper['arxiv_id']
            if arxiv_id not in all_papers:
                all_papers[arxiv_id] = paper

        print(f"  Found {len(papers)} new papers")
        time.sleep(RATE_LIMIT * 2)  # Extra delay between queries

    # Calculate relevance for all papers
    print(f"\n\nProcessing {len(all_papers)} unique papers...")
    for paper in all_papers.values():
        paper['relevance'] = calculate_relevance(paper, ' '.join(SEARCH_QUERIES))

    # Sort by relevance and take top papers
    sorted_papers = sorted(all_papers.values(), key=lambda x: (-x['relevance'], -int(x['year'])))
    selected_papers = sorted_papers[:15]  # Top 15 papers

    print(f"Selected {len(selected_papers)} papers for download")

    # Download PDFs
    print("\nDownloading PDFs...")
    downloaded_count = 0
    for i, paper in enumerate(selected_papers, 1):
        print(f"[{i}/{len(selected_papers)}]", end=" ")
        if download_pdf(paper['pdf_url'], paper['arxiv_id']):
            downloaded_count += 1

    # Save metadata to CSV
    print(f"\nSaving metadata to {CSV_OUTPUT}...")
    save_metadata_csv(selected_papers)

    print("\n" + "=" * 70)
    print(f"Complete! Downloaded {downloaded_count}/{len(selected_papers)} papers")
    print(f"Output directory: {OUTPUT_DIR}")
    print(f"Metadata file: {CSV_OUTPUT}")
    print("=" * 70)

def save_metadata_csv(papers: List[Dict[str, Any]]):
    """Save paper metadata to CSV file."""
    with open(CSV_OUTPUT, 'w', newline='', encoding='utf-8') as f:
        fieldnames = [
            'arxiv_id', 'title', 'first_author', 'published', 'year',
            'pages', 'relevance', 'url', 'pdf_url', 'summary'
        ]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for paper in papers:
            writer.writerow({
                'arxiv_id': paper['arxiv_id'],
                'title': paper['title'],
                'first_author': paper['first_author'],
                'published': paper['published'],
                'year': paper['year'],
                'pages': paper['pages'],
                'relevance': paper['relevance'],
                'url': paper['url'],
                'pdf_url': paper['pdf_url'],
                'summary': paper['summary']
            })

if __name__ == '__main__':
    main()
