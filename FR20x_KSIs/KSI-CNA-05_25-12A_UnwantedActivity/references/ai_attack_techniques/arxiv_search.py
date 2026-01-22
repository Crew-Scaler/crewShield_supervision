#!/usr/bin/env python3
"""
ArXiv paper search and download for AI-powered DDoS attack techniques research.
Issue #11 - DoS Protection Design
"""

import time
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import List, Dict, Tuple
import json
import re

# ArXiv API endpoint
ARXIV_API = "http://export.arxiv.org/api/query"

# Target directory
TARGET_DIR = Path("/Users/tamnguyen/Documents/GitHub/ksi_watch/KSI-CNA-05_25-12A_UnwantedActivity/references/ai_attack_techniques")

# Priority institutions (US universities and companies)
PRIORITY_INSTITUTIONS = [
    "MIT", "Stanford", "Berkeley", "CMU", "Princeton", "Harvard",
    "Google", "Microsoft", "Meta", "Amazon", "IBM", "OpenAI",
    "Georgia Tech", "UIUC", "Cornell", "Yale", "Caltech",
    "Northwestern", "Duke", "Brown", "Columbia"
]


def search_arxiv(query: str, max_results: int = 100) -> List[Dict]:
    """Search ArXiv with a specific query."""
    params = {
        "search_query": query,
        "start": 0,
        "max_results": max_results,
        "sortBy": "submittedDate",
        "sortOrder": "descending"
    }

    url = f"{ARXIV_API}?{urllib.parse.urlencode(params)}"
    print(f"\nSearching ArXiv: {query[:80]}...")

    try:
        with urllib.request.urlopen(url) as response:
            xml_data = response.read()

        # Parse XML response
        root = ET.fromstring(xml_data)
        ns = {'atom': 'http://www.w3.org/2005/Atom'}

        papers = []
        for entry in root.findall('atom:entry', ns):
            paper = {
                'id': entry.find('atom:id', ns).text,
                'title': entry.find('atom:title', ns).text.strip().replace('\n', ' '),
                'summary': entry.find('atom:summary', ns).text.strip(),
                'published': entry.find('atom:published', ns).text,
                'updated': entry.find('atom:updated', ns).text,
                'authors': [author.find('atom:name', ns).text for author in entry.findall('atom:author', ns)],
                'pdf_url': None,
                'arxiv_id': None
            }

            # Get PDF link
            for link in entry.findall('atom:link', ns):
                if link.get('type') == 'application/pdf':
                    paper['pdf_url'] = link.get('href')

            # Extract ArXiv ID
            arxiv_id = paper['id'].split('/abs/')[-1]
            paper['arxiv_id'] = arxiv_id

            # Get affiliation from summary if available
            paper['affiliation'] = ''

            papers.append(paper)

        print(f"Found {len(papers)} papers")
        return papers

    except Exception as e:
        print(f"Error searching ArXiv: {e}")
        return []


def calculate_priority_score(paper: Dict) -> int:
    """Calculate priority score based on publication date and institution."""
    score = 0

    # Year scoring (2025 = 100, 2024 = 50)
    year = int(paper['published'][:4])
    if year == 2025:
        score += 100
    elif year == 2024:
        score += 50

    # Institution scoring
    text_to_check = f"{paper['title']} {paper['summary']} {' '.join(paper['authors'])}"
    for institution in PRIORITY_INSTITUTIONS:
        if institution.lower() in text_to_check.lower():
            score += 25
            break

    return score


def estimate_page_count(summary: str, title: str) -> int:
    """Estimate page count based on summary length and content."""
    # This is a rough heuristic - ArXiv API doesn't provide page count
    # We'll assume papers with detailed summaries are longer
    summary_length = len(summary)

    # Heuristic: longer summaries usually mean longer papers
    if summary_length > 2000:
        return 15  # Likely a substantial paper
    elif summary_length > 1500:
        return 12
    elif summary_length > 1000:
        return 10
    elif summary_length > 500:
        return 8
    else:
        return 6


def download_paper(paper: Dict, delay: int = 3) -> bool:
    """Download a paper PDF with delay."""
    if not paper['pdf_url']:
        print(f"  No PDF URL for {paper['arxiv_id']}")
        return False

    # Create safe filename
    safe_title = re.sub(r'[^\w\s-]', '', paper['title'][:80])
    safe_title = re.sub(r'[-\s]+', '_', safe_title)
    filename = f"{paper['arxiv_id']}_{safe_title}.pdf"
    filepath = TARGET_DIR / filename

    # Skip if already downloaded
    if filepath.exists():
        print(f"  Already downloaded: {filename}")
        return True

    try:
        print(f"  Downloading: {filename}")
        urllib.request.urlretrieve(paper['pdf_url'], filepath)
        time.sleep(delay)  # Respect ArXiv rate limits
        return True
    except Exception as e:
        print(f"  Error downloading {paper['arxiv_id']}: {e}")
        return False


def main():
    """Main research execution."""
    print("="*80)
    print("AI-POWERED DDoS ATTACK TECHNIQUES RESEARCH")
    print("Issue #11 - DoS Protection Design")
    print("="*80)

    # Search queries
    queries = [
        # Query 1: AI/ML DDoS and Botnets
        'abs:(AI OR "machine learning") AND (DDoS OR "denial of service" OR botnet) AND (attack* OR adversarial) AND submittedDate:[202401010000 TO 202512312359]',

        # Query 2: Adversarial/Adaptive Attacks
        'abs:("adversarial attack*" OR "adaptive attack*") AND (network OR infrastructure OR distributed) AND submittedDate:[202401010000 TO 202512312359]',

        # Query 3: Botnet AI/ML Coordination
        'abs:(botnet OR malware) AND (AI OR "machine learning" OR autonomous) AND (coordination OR orchestration) AND submittedDate:[202401010000 TO 202512312359]',

        # Query 4: Multi-vector Coordinated Attacks
        'abs:("multi-vector attack*" OR "coordinated attack*") AND (network OR DDoS OR infrastructure) AND submittedDate:[202401010000 TO 202512312359]',

        # Query 5: Resource Exhaustion and Cloud Attacks
        'abs:("resource exhaustion" OR "auto-scaling") AND (attack* OR exploit* OR abuse) AND (cloud OR serverless) AND submittedDate:[202401010000 TO 202512312359]'
    ]

    all_papers = {}

    # Execute searches
    for i, query in enumerate(queries, 1):
        print(f"\n{'='*80}")
        print(f"QUERY {i}/5")
        print(f"{'='*80}")
        papers = search_arxiv(query, max_results=50)

        # Deduplicate and add to collection
        for paper in papers:
            if paper['arxiv_id'] not in all_papers:
                # Estimate page count
                paper['estimated_pages'] = estimate_page_count(paper['summary'], paper['title'])
                paper['priority_score'] = calculate_priority_score(paper)
                all_papers[paper['arxiv_id']] = paper

        time.sleep(3)  # Rate limiting between queries

    print(f"\n{'='*80}")
    print(f"TOTAL UNIQUE PAPERS FOUND: {len(all_papers)}")
    print(f"{'='*80}")

    # Filter papers: >7 pages estimated
    filtered_papers = {
        pid: p for pid, p in all_papers.items()
        if p['estimated_pages'] > 7
    }

    print(f"\nPapers with >7 estimated pages: {len(filtered_papers)}")

    # Sort by priority score
    sorted_papers = sorted(
        filtered_papers.values(),
        key=lambda x: x['priority_score'],
        reverse=True
    )

    # Limit to target range (35-45 papers)
    target_papers = sorted_papers[:45]

    print(f"\n{'='*80}")
    print(f"DOWNLOADING TOP {len(target_papers)} PAPERS")
    print(f"{'='*80}")

    # Download papers
    downloaded = 0
    failed = 0

    for i, paper in enumerate(target_papers, 1):
        year = paper['published'][:4]
        print(f"\n[{i}/{len(target_papers)}] {year} - Priority: {paper['priority_score']}")
        print(f"  Title: {paper['title'][:80]}...")

        if download_paper(paper, delay=3):
            downloaded += 1
        else:
            failed += 1

    # Save metadata
    metadata = {
        'total_papers_found': len(all_papers),
        'papers_filtered': len(filtered_papers),
        'papers_downloaded': downloaded,
        'papers_failed': failed,
        'queries_executed': len(queries),
        'target_directory': str(TARGET_DIR),
        'papers': [
            {
                'arxiv_id': p['arxiv_id'],
                'title': p['title'],
                'year': p['published'][:4],
                'priority_score': p['priority_score'],
                'estimated_pages': p['estimated_pages'],
                'authors': p['authors'][:3]  # First 3 authors
            }
            for p in target_papers
        ]
    }

    metadata_file = TARGET_DIR / 'research_metadata.json'
    with open(metadata_file, 'w') as f:
        json.dump(metadata, f, indent=2)

    print(f"\n{'='*80}")
    print("RESEARCH SUMMARY")
    print(f"{'='*80}")
    print(f"Total papers found: {len(all_papers)}")
    print(f"Papers >7 pages: {len(filtered_papers)}")
    print(f"Papers downloaded: {downloaded}")
    print(f"Papers failed: {failed}")
    print(f"Metadata saved: {metadata_file}")
    print(f"\n2025 papers: {sum(1 for p in target_papers if p['published'].startswith('2025'))}")
    print(f"2024 papers: {sum(1 for p in target_papers if p['published'].startswith('2024'))}")
    print(f"\nTop 5 Papers by Priority:")
    for i, paper in enumerate(target_papers[:5], 1):
        print(f"{i}. [{paper['published'][:4]}] {paper['title'][:70]}...")
        print(f"   ArXiv ID: {paper['arxiv_id']} | Score: {paper['priority_score']}")


if __name__ == "__main__":
    main()
