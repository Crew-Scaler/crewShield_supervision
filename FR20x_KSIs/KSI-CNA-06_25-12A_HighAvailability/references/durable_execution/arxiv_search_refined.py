#!/usr/bin/env python3
"""
Refined ArXiv research survey for durable execution and workflow orchestration
Issue #12 - Design for High Availability and Rapid Recovery
Using more specific search terms and CS category filtering
"""

import time
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import List, Dict
import json
import re

# Configuration
BASE_URL = "http://export.arxiv.org/api/query?"
DOWNLOAD_DIR = Path("/Users/tamnguyen/Documents/GitHub/ksi_watch/KSI-CNA-06_25-12A_HighAvailability/references/durable_execution")
MIN_PAGES = 7
DELAY_BETWEEN_REQUESTS = 3.5
MAX_RESULTS_PER_QUERY = 200

# Relevant keywords for filtering
RELEVANT_KEYWORDS = [
    "workflow", "orchestration", "temporal", "state machine", "saga",
    "event sourcing", "cqrs", "durable", "execution", "checkpoint",
    "recovery", "fault tolerance", "distributed system", "microservice",
    "transaction", "compensation", "idempotent", "exactly-once",
    "state management", "event-driven", "process migration", "failover",
    "consensus", "raft", "paxos", "replication", "durability",
    "serverless", "function-as-a-service", "long-running", "resumable",
    "kubernetes", "container orchestration", "service mesh", "cloud native",
    "distributed transaction", "two-phase commit", "saga pattern"
]

# CS categories relevant to our research
RELEVANT_CATEGORIES = [
    "cs.DC",  # Distributed Computing
    "cs.SE",  # Software Engineering
    "cs.DB",  # Databases
    "cs.OS",  # Operating Systems
    "cs.NI",  # Networking
    "cs.PL"   # Programming Languages
]

# Refined search queries
SEARCH_QUERIES = [
    {
        "name": "temporal_workflow",
        "query": 'cat:cs.DC AND (all:temporal OR all:"workflow engine" OR all:"durable execution") AND submittedDate:[202401010000 TO 202512312359]',
        "description": "Temporal and workflow engines"
    },
    {
        "name": "saga_pattern",
        "query": 'cat:cs.DC AND (all:saga OR all:"distributed transaction" OR all:"compensation" OR all:"long-running transaction") AND submittedDate:[202401010000 TO 202512312359]',
        "description": "Saga patterns and distributed transactions"
    },
    {
        "name": "event_sourcing_cqrs",
        "query": 'cat:cs.SE AND (all:"event sourcing" OR all:cqrs OR all:"event store" OR all:"event log") AND submittedDate:[202401010000 TO 202512312359]',
        "description": "Event sourcing and CQRS"
    },
    {
        "name": "checkpoint_recovery",
        "query": 'cat:cs.DC AND (all:checkpoint OR all:"state snapshot" OR all:"incremental checkpoint") AND (all:recovery OR all:fault) AND submittedDate:[202401010000 TO 202512312359]',
        "description": "Checkpointing and recovery mechanisms"
    },
    {
        "name": "process_migration_failover",
        "query": 'cat:cs.DC AND (all:"process migration" OR all:failover OR all:"live migration" OR all:"state transfer") AND submittedDate:[202401010000 TO 202512312359]',
        "description": "Process migration and failover"
    },
    {
        "name": "serverless_orchestration",
        "query": 'cat:cs.DC AND (all:serverless OR all:faas OR all:"function orchestration") AND (all:workflow OR all:stateful) AND submittedDate:[202401010000 TO 202512312359]',
        "description": "Serverless workflow orchestration"
    },
    {
        "name": "container_orchestration",
        "query": 'cat:cs.DC AND (all:kubernetes OR all:"container orchestration" OR all:"service mesh") AND (all:stateful OR all:resilience) AND submittedDate:[202401010000 TO 202512312359]',
        "description": "Container orchestration systems"
    },
    {
        "name": "consensus_replication",
        "query": 'cat:cs.DC AND (all:raft OR all:paxos OR all:"state machine replication" OR all:"replicated log") AND submittedDate:[202401010000 TO 202512312359]',
        "description": "Consensus protocols and replication"
    },
    {
        "name": "distributed_workflow",
        "query": 'cat:cs.DC AND all:"distributed workflow" AND submittedDate:[202401010000 TO 202512312359]',
        "description": "Distributed workflow systems"
    },
    {
        "name": "fault_tolerant_execution",
        "query": 'cat:cs.DC AND (all:"fault tolerant" OR all:"fault tolerance") AND (all:execution OR all:computation) AND submittedDate:[202401010000 TO 202512312359]',
        "description": "Fault-tolerant execution systems"
    }
]


def is_relevant(paper: Dict) -> bool:
    """Check if paper is relevant based on title and abstract."""
    text = (paper['title'] + " " + paper['summary']).lower()

    # Count keyword matches
    matches = sum(1 for keyword in RELEVANT_KEYWORDS if keyword in text)

    # Require at least 2 keyword matches for relevance
    return matches >= 2


def has_relevant_category(paper: Dict) -> bool:
    """Check if paper has a relevant category."""
    categories = paper.get('categories', '').split()
    return any(cat in RELEVANT_CATEGORIES for cat in categories)


def extract_paper_info(entry) -> Dict:
    """Extract paper information from ArXiv entry."""
    paper = {
        'id': entry.find('{http://www.w3.org/2005/Atom}id').text,
        'title': entry.find('{http://www.w3.org/2005/Atom}title').text.strip().replace('\n', ' '),
        'summary': entry.find('{http://www.w3.org/2005/Atom}summary').text.strip().replace('\n', ' '),
        'published': entry.find('{http://www.w3.org/2005/Atom}published').text,
        'updated': entry.find('{http://www.w3.org/2005/Atom}updated').text,
        'authors': [],
        'categories': '',
        'pdf_url': None,
        'year': 0
    }

    # Extract authors
    for author in entry.findall('{http://www.w3.org/2005/Atom}author'):
        name_elem = author.find('{http://www.w3.org/2005/Atom}name')
        if name_elem is not None:
            paper['authors'].append(name_elem.text)

    # Extract categories
    categories = entry.findall('{http://arxiv.org/schemas/atom}primary_category')
    if categories:
        paper['categories'] = categories[0].get('term', '')

    # Extract year
    try:
        paper['year'] = int(paper['published'][:4])
    except Exception:
        paper['year'] = 0

    # Find PDF link
    for link in entry.findall('{http://www.w3.org/2005/Atom}link'):
        if link.get('type') == 'application/pdf':
            paper['pdf_url'] = link.get('href')
            break

    return paper


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
    print(f"  Query URL: {url[:120]}...")

    try:
        with urllib.request.urlopen(url) as response:
            data = response.read()

        root = ET.fromstring(data)
        entries = root.findall('{http://www.w3.org/2005/Atom}entry')

        papers = []
        for entry in entries:
            paper = extract_paper_info(entry)
            papers.append(paper)

        return papers

    except Exception as e:
        print(f"  Error searching ArXiv: {e}")
        return []


def download_pdf(url: str, filename: Path) -> bool:
    """Download PDF from URL."""
    try:
        urllib.request.urlretrieve(url, filename)
        return True
    except Exception as e:
        print(f"    Error downloading: {e}")
        return False


def main():
    """Execute all searches and download papers."""
    DOWNLOAD_DIR.mkdir(parents=True, exist_ok=True)

    all_papers = []
    query_stats = {}

    print("=" * 100)
    print("REFINED ArXiv Research Survey: Durable Execution and Workflow Orchestration")
    print("Issue #12 - Design for High Availability and Rapid Recovery")
    print("=" * 100)
    print()

    # Execute each search query
    for i, search_config in enumerate(SEARCH_QUERIES, 1):
        print(f"\n[Query {i}/{len(SEARCH_QUERIES)}] {search_config['description']}")
        print(f"Category: {search_config['name']}")
        print("-" * 100)

        papers = search_arxiv(search_config['query'])
        print(f"  Found: {len(papers)} papers")

        # Filter by relevance
        relevant_papers = [p for p in papers if is_relevant(p)]
        print(f"  Relevant: {len(relevant_papers)} papers (keyword matching)")

        # Add category tag
        for paper in relevant_papers:
            paper['category'] = search_config['name']

        all_papers.extend(relevant_papers)
        query_stats[search_config['name']] = {
            'total_found': len(papers),
            'relevant': len(relevant_papers),
            'description': search_config['description']
        }

        # Delay between queries
        if i < len(SEARCH_QUERIES):
            print(f"  Waiting {DELAY_BETWEEN_REQUESTS}s...")
            time.sleep(DELAY_BETWEEN_REQUESTS)

    print("\n" + "=" * 100)
    print("PROCESSING RESULTS")
    print("=" * 100)

    # Remove duplicates
    unique_papers = {}
    for paper in all_papers:
        paper_id = paper['id'].split('/')[-1]
        if paper_id not in unique_papers:
            unique_papers[paper_id] = paper
        else:
            # Merge categories if duplicate
            existing = unique_papers[paper_id]
            if 'categories_list' not in existing:
                existing['categories_list'] = [existing['category']]
            existing['categories_list'].append(paper['category'])

    papers_list = list(unique_papers.values())
    print(f"\nTotal unique relevant papers: {len(papers_list)}")

    # Statistics
    year_2025 = sum(1 for p in papers_list if p['year'] == 2025)
    year_2024 = sum(1 for p in papers_list if p['year'] == 2024)

    print(f"  2025 papers: {year_2025}")
    print(f"  2024 papers: {year_2024}")

    # Sort by year (2025 first, then 2024)
    papers_list.sort(key=lambda p: p['year'], reverse=True)

    # Target 35-45 papers
    target_count = min(45, len(papers_list))
    if len(papers_list) < 35:
        print(f"\nWARNING: Only {len(papers_list)} papers found (target: 35-45)")

    selected_papers = papers_list[:target_count]

    print(f"\nSelecting {len(selected_papers)} papers for download")
    print("=" * 100)

    # Download papers
    downloaded = 0
    failed = []

    for i, paper in enumerate(selected_papers, 1):
        paper_id = paper['id'].split('/')[-1]
        filename = DOWNLOAD_DIR / f"{paper['category']}_{paper_id.replace('/', '_')}.pdf"

        # Check if already downloaded
        if filename.exists():
            print(f"\n[{i}/{len(selected_papers)}] ALREADY EXISTS: {paper['title'][:70]}...")
            downloaded += 1
            continue

        print(f"\n[{i}/{len(selected_papers)}] {paper['title'][:70]}...")
        print(f"  Year: {paper['year']} | Category: {paper['category']}")
        print(f"  Authors: {', '.join(paper['authors'][:2])}{'...' if len(paper['authors']) > 2 else ''}")

        if paper['pdf_url']:
            if download_pdf(paper['pdf_url'], filename):
                downloaded += 1
                print(f"  Status: Downloaded")
            else:
                failed.append(paper)
                print(f"  Status: Failed")
        else:
            print(f"  Status: No PDF URL")
            failed.append(paper)

        # Delay between downloads
        if i < len(selected_papers):
            time.sleep(DELAY_BETWEEN_REQUESTS)

    # Save metadata
    metadata_file = DOWNLOAD_DIR / "paper_metadata_refined.json"
    metadata = {
        'query_stats': query_stats,
        'total_unique_papers': len(papers_list),
        'selected_papers': len(selected_papers),
        'successfully_downloaded': downloaded,
        'failed_downloads': len(failed),
        'year_2025': year_2025,
        'year_2024': year_2024,
        'papers': [
            {
                'id': p['id'],
                'title': p['title'],
                'authors': p['authors'],
                'year': p['year'],
                'category': p['category'],
                'categories': p['categories'],
                'pdf_url': p['pdf_url'],
                'summary': p['summary'][:500]
            }
            for p in selected_papers
        ]
    }

    with open(metadata_file, 'w') as f:
        json.dump(metadata, f, indent=2)

    # Save detailed report
    report_file = DOWNLOAD_DIR / "research_summary.md"
    with open(report_file, 'w') as f:
        f.write("# Durable Execution and Workflow Orchestration Research Survey\n\n")
        f.write("**Issue #12: Design for High Availability and Rapid Recovery**\n\n")
        f.write("## Search Strategy\n\n")
        f.write(f"Executed {len(SEARCH_QUERIES)} targeted queries on ArXiv focusing on:\n")
        for sq in SEARCH_QUERIES:
            f.write(f"- {sq['description']}\n")
        f.write("\n## Results Summary\n\n")
        f.write(f"- Total unique papers: {len(papers_list)}\n")
        f.write(f"- Papers downloaded: {downloaded}\n")
        f.write(f"- 2025 papers: {year_2025}\n")
        f.write(f"- 2024 papers: {year_2024}\n\n")
        f.write("## Query Results\n\n")
        for category, stats in query_stats.items():
            f.write(f"### {stats['description']}\n")
            f.write(f"- Total found: {stats['total_found']}\n")
            f.write(f"- Relevant: {stats['relevant']}\n\n")
        f.write("## Downloaded Papers\n\n")
        for i, paper in enumerate(selected_papers, 1):
            f.write(f"{i}. **{paper['title']}** ({paper['year']})\n")
            f.write(f"   - Authors: {', '.join(paper['authors'][:3])}\n")
            f.write(f"   - Category: {paper['category']}\n")
            f.write(f"   - ArXiv: {paper['id']}\n\n")

    # Final summary
    print("\n" + "=" * 100)
    print("FINAL SUMMARY")
    print("=" * 100)
    print(f"\nQuery Results:")
    for category, stats in query_stats.items():
        print(f"  {category}: {stats['relevant']}/{stats['total_found']} relevant papers")

    print(f"\nDownload Results:")
    print(f"  Total unique papers: {len(papers_list)}")
    print(f"  Papers selected: {len(selected_papers)}")
    print(f"  Successfully downloaded: {downloaded}")
    print(f"  Failed downloads: {len(failed)}")

    print(f"\nYear Distribution:")
    print(f"  2025: {year_2025} papers")
    print(f"  2024: {year_2024} papers")

    print(f"\nOutputs:")
    print(f"  Metadata: {metadata_file}")
    print(f"  Research summary: {report_file}")
    print(f"  PDFs: {DOWNLOAD_DIR}")
    print("\n" + "=" * 100)


if __name__ == "__main__":
    main()
