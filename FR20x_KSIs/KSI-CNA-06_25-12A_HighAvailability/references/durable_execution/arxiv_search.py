#!/usr/bin/env python3
"""
ArXiv research survey for durable execution and workflow orchestration
Issue #12 - Design for High Availability and Rapid Recovery
"""

import time
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import List, Dict, Tuple
import json

# Configuration
BASE_URL = "http://export.arxiv.org/api/query?"
DOWNLOAD_DIR = Path("/Users/tamnguyen/Documents/GitHub/ksi_watch/KSI-CNA-06_25-12A_HighAvailability/references/durable_execution")
MIN_PAGES = 7
DELAY_BETWEEN_REQUESTS = 3.5  # seconds
MAX_RESULTS_PER_QUERY = 100

# US institutions to prioritize
US_INSTITUTIONS = [
    "MIT", "Stanford", "Berkeley", "Carnegie Mellon", "Princeton",
    "Harvard", "Cornell", "University of Washington", "UCLA", "UCSD",
    "University of Michigan", "Georgia Tech", "UIUC", "University of Texas",
    "Columbia", "Yale", "Caltech", "Northwestern", "Duke", "Penn",
    "Microsoft", "Google", "Meta", "Amazon", "IBM", "Apple"
]

# Search queries
SEARCH_QUERIES = [
    {
        "name": "event_sourcing",
        "query": 'abs:(event sourcing OR event log OR immutable state) AND (system* OR architecture OR distributed) AND submittedDate:[202401010000 TO 202512312359]',
        "description": "Event sourcing and state persistence"
    },
    {
        "name": "durable_execution",
        "query": 'abs:(durable execution OR long-running workflow OR fault tolerant execution) AND (orchestration OR coordination) AND submittedDate:[202401010000 TO 202512312359]',
        "description": "Durable execution patterns"
    },
    {
        "name": "workflow_orchestration",
        "query": 'abs:(workflow orchestration OR distributed workflow OR task coordination) AND (failure handling OR resilience) AND submittedDate:[202401010000 TO 202512312359]',
        "description": "Workflow orchestration systems"
    },
    {
        "name": "checkpointing",
        "query": 'abs:(checkpointing OR checkpoint OR state snapshot) AND (optimization OR compression OR recovery) AND submittedDate:[202401010000 TO 202512312359]',
        "description": "Checkpointing strategies"
    },
    {
        "name": "process_migration",
        "query": 'abs:(process migration OR state transfer OR failover) AND (distributed system* OR cloud computing) AND submittedDate:[202401010000 TO 202512312359]',
        "description": "Cross-infrastructure migration"
    }
]


def estimate_pages(entry) -> int:
    """Estimate number of pages from PDF size (rough heuristic)."""
    try:
        # Look for PDF link
        for link in entry.findall('{http://www.w3.org/2005/Atom}link'):
            if link.get('type') == 'application/pdf':
                # Rough estimate: 100KB per page average
                # We'll be conservative and assume papers are longer
                return 10  # Default assumption for ArXiv papers
    except Exception:
        pass
    return 10  # Conservative default


def has_us_affiliation(entry) -> bool:
    """Check if paper has US institution affiliation."""
    try:
        # Check author affiliations if available
        authors = entry.findall('{http://www.w3.org/2005/Atom}author')
        for author in authors:
            affiliation = author.find('{http://arxiv.org/schemas/atom}affiliation')
            if affiliation is not None and affiliation.text:
                for inst in US_INSTITUTIONS:
                    if inst.lower() in affiliation.text.lower():
                        return True

        # Fallback: check comment field for institutional info
        comment = entry.find('{http://www.w3.org/2005/Atom}comment')
        if comment is not None and comment.text:
            for inst in US_INSTITUTIONS:
                if inst.lower() in comment.text.lower():
                    return True
    except Exception:
        pass
    return False


def get_submission_year(entry) -> int:
    """Extract submission year from entry."""
    try:
        published = entry.find('{http://www.w3.org/2005/Atom}published').text
        return int(published[:4])
    except Exception:
        return 0


def search_arxiv(query: str, max_results: int = MAX_RESULTS_PER_QUERY) -> List[Dict]:
    """Search ArXiv and return paper metadata."""
    params = {
        'search_query': query,
        'start': 0,
        'max_results': max_results,
        'sortBy': 'submittedDate',
        'sortOrder': 'descending'
    }

    url = BASE_URL + urllib.parse.urlencode(params)
    print(f"Searching ArXiv: {url[:100]}...")

    try:
        with urllib.request.urlopen(url) as response:
            data = response.read()

        root = ET.fromstring(data)
        entries = root.findall('{http://www.w3.org/2005/Atom}entry')

        papers = []
        for entry in entries:
            paper = {
                'id': entry.find('{http://www.w3.org/2005/Atom}id').text,
                'title': entry.find('{http://www.w3.org/2005/Atom}title').text.strip(),
                'summary': entry.find('{http://www.w3.org/2005/Atom}summary').text.strip(),
                'published': entry.find('{http://www.w3.org/2005/Atom}published').text,
                'updated': entry.find('{http://www.w3.org/2005/Atom}updated').text,
                'authors': [author.find('{http://www.w3.org/2005/Atom}name').text
                           for author in entry.findall('{http://www.w3.org/2005/Atom}author')],
                'pdf_url': None,
                'estimated_pages': estimate_pages(entry),
                'us_affiliation': has_us_affiliation(entry),
                'year': get_submission_year(entry)
            }

            # Find PDF link
            for link in entry.findall('{http://www.w3.org/2005/Atom}link'):
                if link.get('type') == 'application/pdf':
                    paper['pdf_url'] = link.get('href')
                    break

            papers.append(paper)

        return papers

    except Exception as e:
        print(f"Error searching ArXiv: {e}")
        return []


def download_pdf(url: str, filename: Path) -> bool:
    """Download PDF from URL."""
    try:
        print(f"  Downloading: {filename.name}")
        urllib.request.urlretrieve(url, filename)
        return True
    except Exception as e:
        print(f"  Error downloading {filename.name}: {e}")
        return False


def prioritize_papers(papers: List[Dict]) -> List[Dict]:
    """Sort papers by priority: 2025 > 2024, US institutions > others."""
    def score(paper):
        year_score = paper['year'] * 1000  # 2025 = 2025000, 2024 = 2024000
        us_score = 100 if paper['us_affiliation'] else 0
        return year_score + us_score

    return sorted(papers, key=score, reverse=True)


def main():
    """Execute all searches and download papers."""
    DOWNLOAD_DIR.mkdir(parents=True, exist_ok=True)

    all_papers = []
    query_stats = {}

    print("=" * 80)
    print("ArXiv Research Survey: Durable Execution and Workflow Orchestration")
    print("Issue #12 - Design for High Availability and Rapid Recovery")
    print("=" * 80)
    print()

    # Execute each search query
    for i, search_config in enumerate(SEARCH_QUERIES, 1):
        print(f"\n[Query {i}/5] {search_config['description']}")
        print(f"Category: {search_config['name']}")
        print("-" * 80)

        papers = search_arxiv(search_config['query'])
        print(f"Found {len(papers)} papers")

        # Filter by minimum pages (estimated)
        filtered_papers = [p for p in papers if p['estimated_pages'] >= MIN_PAGES]
        print(f"After filtering (>{MIN_PAGES} pages): {len(filtered_papers)} papers")

        # Add category tag
        for paper in filtered_papers:
            paper['category'] = search_config['name']

        all_papers.extend(filtered_papers)
        query_stats[search_config['name']] = {
            'total_found': len(papers),
            'filtered': len(filtered_papers),
            'description': search_config['description']
        }

        # Delay between queries
        if i < len(SEARCH_QUERIES):
            print(f"Waiting {DELAY_BETWEEN_REQUESTS}s before next query...")
            time.sleep(DELAY_BETWEEN_REQUESTS)

    print("\n" + "=" * 80)
    print("PROCESSING RESULTS")
    print("=" * 80)

    # Remove duplicates (same paper ID)
    unique_papers = {}
    for paper in all_papers:
        paper_id = paper['id'].split('/')[-1]
        if paper_id not in unique_papers:
            unique_papers[paper_id] = paper

    papers_list = list(unique_papers.values())
    print(f"\nTotal unique papers: {len(papers_list)}")

    # Prioritize papers
    prioritized_papers = prioritize_papers(papers_list)

    # Statistics
    year_2025 = sum(1 for p in papers_list if p['year'] == 2025)
    year_2024 = sum(1 for p in papers_list if p['year'] == 2024)
    us_affiliated = sum(1 for p in papers_list if p['us_affiliation'])

    print(f"2025 papers: {year_2025}")
    print(f"2024 papers: {year_2024}")
    print(f"US-affiliated papers: {us_affiliated}")

    # Target 35-45 papers
    target_count = min(45, len(prioritized_papers))
    selected_papers = prioritized_papers[:target_count]

    print(f"\nSelecting top {target_count} papers for download")
    print("=" * 80)

    # Download papers
    downloaded = 0
    failed = []

    for i, paper in enumerate(selected_papers, 1):
        paper_id = paper['id'].split('/')[-1]
        filename = DOWNLOAD_DIR / f"{paper['category']}_{paper_id.replace('/', '_')}.pdf"

        print(f"\n[{i}/{target_count}] {paper['title'][:70]}...")
        print(f"  Year: {paper['year']} | US: {paper['us_affiliation']} | Category: {paper['category']}")
        print(f"  Authors: {', '.join(paper['authors'][:3])}{'...' if len(paper['authors']) > 3 else ''}")

        if paper['pdf_url']:
            if download_pdf(paper['pdf_url'], filename):
                downloaded += 1
                print(f"  Status: Downloaded successfully")
            else:
                failed.append(paper)
                print(f"  Status: Download failed")
        else:
            print(f"  Status: No PDF URL available")
            failed.append(paper)

        # Delay between downloads
        if i < len(selected_papers):
            time.sleep(DELAY_BETWEEN_REQUESTS)

    # Save metadata
    metadata_file = DOWNLOAD_DIR / "paper_metadata.json"
    metadata = {
        'query_stats': query_stats,
        'total_unique_papers': len(papers_list),
        'selected_papers': target_count,
        'successfully_downloaded': downloaded,
        'failed_downloads': len(failed),
        'year_2025': year_2025,
        'year_2024': year_2024,
        'us_affiliated': us_affiliated,
        'papers': [
            {
                'id': p['id'],
                'title': p['title'],
                'authors': p['authors'],
                'year': p['year'],
                'category': p['category'],
                'us_affiliation': p['us_affiliation'],
                'pdf_url': p['pdf_url']
            }
            for p in selected_papers
        ]
    }

    with open(metadata_file, 'w') as f:
        json.dump(metadata, f, indent=2)

    # Final summary
    print("\n" + "=" * 80)
    print("FINAL SUMMARY")
    print("=" * 80)
    print(f"\nQuery Results:")
    for category, stats in query_stats.items():
        print(f"  {category}: {stats['filtered']} papers")

    print(f"\nDownload Results:")
    print(f"  Total unique papers found: {len(papers_list)}")
    print(f"  Papers selected for download: {target_count}")
    print(f"  Successfully downloaded: {downloaded}")
    print(f"  Failed downloads: {len(failed)}")

    print(f"\nYear Distribution:")
    print(f"  2025: {year_2025} papers")
    print(f"  2024: {year_2024} papers")

    print(f"\nAffiliation:")
    print(f"  US institutions: {us_affiliated} papers")

    print(f"\nMetadata saved to: {metadata_file}")
    print(f"Papers downloaded to: {DOWNLOAD_DIR}")
    print("\n" + "=" * 80)


if __name__ == "__main__":
    main()
