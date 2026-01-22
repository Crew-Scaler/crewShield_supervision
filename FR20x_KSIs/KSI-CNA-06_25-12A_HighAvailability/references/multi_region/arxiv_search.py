#!/usr/bin/env python3
"""
ArXiv search and download for multi-region active-active architecture research.
Focuses on 2024-2025 papers with emphasis on US institutions.
"""

import arxiv
import time
import os
from pathlib import Path
from typing import List, Dict
import json
from datetime import datetime

# Target directory
TARGET_DIR = Path("/Users/tamnguyen/Documents/GitHub/ksi_watch/KSI-CNA-06_25-12A_HighAvailability/references/multi_region")

# US institutions to prioritize
US_INSTITUTIONS = [
    'MIT', 'Stanford', 'Berkeley', 'CMU', 'Princeton', 'Harvard', 'Yale',
    'Google', 'Microsoft', 'Amazon', 'Meta', 'IBM', 'Intel', 'NVIDIA',
    'University of Washington', 'University of Michigan', 'Cornell',
    'Caltech', 'Georgia Tech', 'UIUC', 'Columbia', 'NYU', 'USC'
]

# Search queries
SEARCH_QUERIES = {
    "multi_region_deployment": {
        "query": 'abs:(multi-region OR multi-zone OR geo-distributed) AND (active-active OR active-passive OR replication)',
        "category": "deployment_patterns",
        "max_results": 50
    },
    "data_consistency": {
        "query": 'abs:(eventual consistency OR strong consistency OR CRDT) AND (distributed system* OR replication)',
        "category": "consistency_models",
        "max_results": 50
    },
    "cross_region_replication": {
        "query": 'abs:(cross-region OR geo-replication OR global replication) AND (consensus OR conflict resolution)',
        "category": "replication",
        "max_results": 50
    },
    "global_traffic_routing": {
        "query": 'abs:(anycast OR geo-routing OR global load balancing) AND (traffic routing OR failover)',
        "category": "traffic_routing",
        "max_results": 50
    },
    "disaster_recovery": {
        "query": 'abs:(disaster recovery OR RTO OR RPO) AND (automated failover OR regional failover) AND (cloud OR distributed)',
        "category": "disaster_recovery",
        "max_results": 50
    }
}

def is_us_institution(authors_str: str) -> bool:
    """Check if any author is from a US institution."""
    for inst in US_INSTITUTIONS:
        if inst.lower() in authors_str.lower():
            return True
    return False

def get_year_from_date(date_str) -> int:
    """Extract year from datetime object or string."""
    if hasattr(date_str, 'year'):
        return date_str.year
    try:
        return int(str(date_str)[:4])
    except:
        return 0

def search_and_download(query_name: str, query_info: Dict) -> List[Dict]:
    """Search ArXiv and download relevant papers."""
    print(f"\n{'='*80}")
    print(f"Searching: {query_name}")
    print(f"Query: {query_info['query']}")
    print(f"{'='*80}\n")

    results = []
    client = arxiv.Client()

    search = arxiv.Search(
        query=query_info['query'],
        max_results=query_info['max_results'],
        sort_by=arxiv.SortCriterion.SubmittedDate,
        sort_order=arxiv.SortOrder.Descending
    )

    papers_downloaded = 0
    papers_skipped = 0

    for result in client.results(search):
        # Get publication year
        pub_year = get_year_from_date(result.published)

        # Filter: Only 2024-2025 papers
        if pub_year < 2024:
            papers_skipped += 1
            continue

        # Estimate page count (rough approximation: 500 words per page)
        # ArXiv doesn't provide page count directly, so we skip this filter for now
        # and rely on manual inspection

        # Check US institution
        authors_str = ', '.join([author.name for author in result.authors])
        is_us = is_us_institution(authors_str)

        paper_info = {
            'title': result.title,
            'arxiv_id': result.entry_id.split('/')[-1],
            'published': str(result.published),
            'year': pub_year,
            'authors': authors_str,
            'summary': result.summary[:500] + '...' if len(result.summary) > 500 else result.summary,
            'pdf_url': result.pdf_url,
            'category': query_info['category'],
            'query_name': query_name,
            'is_us_institution': is_us
        }

        # Download PDF
        filename = f"{query_info['category']}_{paper_info['arxiv_id'].replace('.', '_')}.pdf"
        filepath = TARGET_DIR / filename

        if not filepath.exists():
            try:
                print(f"Downloading: {result.title[:80]}...")
                print(f"  Year: {pub_year}, US Institution: {is_us}")
                result.download_pdf(dirpath=str(TARGET_DIR), filename=filename)
                papers_downloaded += 1
                results.append(paper_info)
                print(f"  ✓ Saved as {filename}")

                # Delay between downloads (3+ seconds as required)
                time.sleep(3.5)
            except Exception as e:
                print(f"  ✗ Error downloading: {e}")
                papers_skipped += 1
        else:
            print(f"Skipping (exists): {result.title[:80]}...")
            papers_skipped += 1
            results.append(paper_info)

    print(f"\n{query_name} Summary:")
    print(f"  Downloaded: {papers_downloaded}")
    print(f"  Skipped: {papers_skipped}")
    print(f"  Total results: {len(results)}")

    return results

def main():
    """Main execution function."""
    print("="*80)
    print("MULTI-REGION ACTIVE-ACTIVE ARCHITECTURE RESEARCH")
    print("ArXiv Search and Download - Issue #12")
    print("="*80)

    TARGET_DIR.mkdir(parents=True, exist_ok=True)

    all_results = []
    total_downloaded = 0

    # Execute searches
    for query_name, query_info in SEARCH_QUERIES.items():
        results = search_and_download(query_name, query_info)
        all_results.extend(results)
        time.sleep(5)  # Delay between different query sets

    # Sort results: 2025 first, then US institutions
    all_results.sort(key=lambda x: (-x['year'], -x['is_us_institution']))

    # Save metadata
    metadata_file = TARGET_DIR / "papers_metadata.json"
    with open(metadata_file, 'w') as f:
        json.dump({
            'search_date': str(datetime.now()),
            'total_papers': len(all_results),
            'papers_by_year': {
                '2025': len([p for p in all_results if p['year'] == 2025]),
                '2024': len([p for p in all_results if p['year'] == 2024])
            },
            'papers_by_category': {
                cat: len([p for p in all_results if p['category'] == cat])
                for cat in set(p['category'] for p in all_results)
            },
            'us_institution_count': len([p for p in all_results if p['is_us_institution']]),
            'papers': all_results
        }, f, indent=2)

    print(f"\n{'='*80}")
    print("RESEARCH SUMMARY")
    print(f"{'='*80}")
    print(f"Total papers collected: {len(all_results)}")
    print(f"  2025 papers: {len([p for p in all_results if p['year'] == 2025])}")
    print(f"  2024 papers: {len([p for p in all_results if p['year'] == 2024])}")
    print(f"  US institutions: {len([p for p in all_results if p['is_us_institution']])}")
    print(f"\nPapers by category:")
    for cat in set(p['category'] for p in all_results):
        count = len([p for p in all_results if p['category'] == cat])
        print(f"  {cat}: {count}")
    print(f"\nMetadata saved to: {metadata_file}")
    print(f"PDFs saved to: {TARGET_DIR}")
    print(f"{'='*80}\n")

if __name__ == "__main__":
    main()
