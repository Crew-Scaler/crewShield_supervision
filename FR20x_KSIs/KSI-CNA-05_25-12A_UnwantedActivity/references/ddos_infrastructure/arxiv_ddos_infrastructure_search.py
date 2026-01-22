#!/usr/bin/env python3
"""
ArXiv DDoS Infrastructure Research Script for Issue #11
Focuses on: Scrubbing centers, multi-Tbps capacity, layered defense,
cloud-native protection, hybrid models
"""

import arxiv
import time
import os
from pathlib import Path
from typing import List, Dict, Tuple
import json
from datetime import datetime

# Configuration
OUTPUT_DIR = Path("/Users/tamnguyen/Documents/GitHub/ksi_watch/KSI-CNA-05_25-12A_UnwantedActivity/references/ddos_infrastructure")
MIN_PAGES = 7
DELAY_BETWEEN_DOWNLOADS = 3
TARGET_PAPERS = 45

# US institutions to prioritize
US_INSTITUTIONS = [
    'MIT', 'Stanford', 'Berkeley', 'CMU', 'Princeton', 'Harvard',
    'Microsoft', 'Google', 'Amazon', 'Cloudflare', 'Akamai',
    'Georgia Tech', 'UIUC', 'University of Michigan', 'Cornell',
    'USC', 'UCLA', 'UCSD', 'Purdue', 'UW', 'UT Austin'
]

# Search queries for DDoS infrastructure research
SEARCH_QUERIES = [
    {
        'name': 'scrubbing_centers_mitigation',
        'query': 'abs:("scrubbing center" OR "traffic filtering" OR "DDoS mitigation") AND (infrastructure OR architecture OR distributed)',
        'description': 'Scrubbing centers and distributed mitigation'
    },
    {
        'name': 'edge_cdn_anycast',
        'query': 'abs:("edge computing" OR CDN OR anycast) AND (DDoS OR "network security" OR defense)',
        'description': 'Edge computing, CDN, and anycast routing'
    },
    {
        'name': 'layered_defense',
        'query': 'abs:("layered defense" OR "defense in depth") AND ("network security" OR DDoS)',
        'description': 'Layered defense architecture'
    },
    {
        'name': 'cloud_native_protection',
        'query': 'abs:("cloud native" OR microservices OR serverless) AND ("DDoS protection" OR security OR resilience)',
        'description': 'Cloud-native DDoS protection'
    },
    {
        'name': 'hybrid_defense',
        'query': 'abs:("hybrid defense" OR "multi-cloud" OR federated) AND (security OR DDoS OR infrastructure)',
        'description': 'Hybrid defense models'
    },
    # Additional targeted queries
    {
        'name': 'capacity_planning',
        'query': 'abs:(capacity OR scaling OR "multi-Tbps") AND (DDoS OR mitigation OR defense)',
        'description': 'Multi-Tbps capacity planning'
    },
    {
        'name': 'traffic_engineering',
        'query': 'abs:("traffic engineering" OR "load balancing" OR routing) AND (DDoS OR attack OR mitigation)',
        'description': 'Traffic engineering solutions'
    },
    {
        'name': 'distributed_systems_security',
        'query': 'abs:("distributed systems" OR "distributed architecture") AND (DDoS OR "attack mitigation" OR resilience)',
        'description': 'Distributed systems security'
    }
]


def estimate_pages(result) -> int:
    """Estimate number of pages from result metadata"""
    # Try to get page count from comment field
    if hasattr(result, 'comment') and result.comment:
        comment = result.comment.lower()
        if 'pages' in comment:
            try:
                parts = comment.split('pages')
                num_str = parts[0].strip().split()[-1]
                return int(num_str)
            except:
                pass
    # Fallback: assume 0.5 pages per KB
    return 10  # Default conservative estimate


def has_us_affiliation(result) -> bool:
    """Check if paper has US institution affiliation"""
    authors_str = ' '.join([str(author) for author in result.authors])
    comment_str = result.comment if hasattr(result, 'comment') and result.comment else ''
    combined = (authors_str + ' ' + comment_str).lower()

    return any(inst.lower() in combined for inst in US_INSTITUTIONS)


def calculate_relevance_score(result, query_name: str) -> float:
    """Calculate relevance score for prioritization"""
    score = 0.0

    # Recency bonus (2025 papers get highest priority)
    year = result.published.year
    if year == 2025:
        score += 10.0
    elif year == 2024:
        score += 5.0

    # US institution bonus
    if has_us_affiliation(result):
        score += 3.0

    # Keywords in title (strong relevance)
    title_lower = result.title.lower()
    high_value_keywords = [
        'ddos', 'mitigation', 'scrubbing', 'anycast', 'cdn',
        'infrastructure', 'defense', 'protection', 'resilience',
        'cloud', 'edge', 'distributed', 'architecture'
    ]
    score += sum(2.0 for kw in high_value_keywords if kw in title_lower)

    # Query-specific bonuses
    query_keywords = {
        'scrubbing_centers_mitigation': ['scrubbing', 'filtering', 'mitigation'],
        'edge_cdn_anycast': ['edge', 'cdn', 'anycast'],
        'layered_defense': ['layered', 'layer', 'defense in depth'],
        'cloud_native_protection': ['cloud', 'microservice', 'serverless'],
        'hybrid_defense': ['hybrid', 'multi-cloud', 'federated'],
        'capacity_planning': ['capacity', 'scaling', 'tbps'],
        'traffic_engineering': ['traffic', 'routing', 'load balancing']
    }

    if query_name in query_keywords:
        abstract_lower = result.summary.lower()
        score += sum(1.5 for kw in query_keywords[query_name]
                    if kw in abstract_lower)

    return score


def search_and_collect(query_dict: Dict) -> List[Tuple[arxiv.Result, float]]:
    """Search ArXiv and collect results with relevance scores"""
    print(f"\n{'='*80}")
    print(f"Searching: {query_dict['description']}")
    print(f"Query: {query_dict['query']}")
    print(f"{'='*80}")

    search = arxiv.Search(
        query=query_dict['query'],
        max_results=100,
        sort_by=arxiv.SortCriterion.SubmittedDate,
        sort_order=arxiv.SortOrder.Descending
    )

    results_with_scores = []

    for result in search.results():
        # Filter by date (2024-2025)
        if result.published.year < 2024:
            continue

        # Estimate pages
        estimated_pages = estimate_pages(result)

        # Skip short papers
        if estimated_pages < MIN_PAGES:
            print(f"  ⊗ Skipping (too short): {result.title[:60]}... "
                  f"(~{estimated_pages} pages)")
            continue

        # Calculate relevance score
        score = calculate_relevance_score(result, query_dict['name'])

        results_with_scores.append((result, score))

        print(f"  ✓ Found [{result.published.year}] Score: {score:.1f} "
              f"(~{estimated_pages}p): {result.title[:70]}...")

        if has_us_affiliation(result):
            print(f"    [US Institution]")

    # Sort by relevance score
    results_with_scores.sort(key=lambda x: x[1], reverse=True)

    print(f"\nTotal relevant papers found: {len(results_with_scores)}")
    return results_with_scores


def download_paper(result: arxiv.Result, score: float, category: str) -> bool:
    """Download a single paper with metadata"""
    try:
        # Create safe filename
        first_author = str(result.authors[0]).split()[-1] if result.authors else 'Unknown'
        year = result.published.year
        title_clean = ''.join(c for c in result.title if c.isalnum() or c in ' -_')[:50]
        title_clean = title_clean.strip().replace(' ', '_')

        filename = f"{year}_{first_author}_{title_clean}.pdf"
        filepath = OUTPUT_DIR / category / filename

        # Create category subdirectory
        (OUTPUT_DIR / category).mkdir(exist_ok=True)

        # Skip if already downloaded
        if filepath.exists():
            print(f"  ⊙ Already exists: {filename}")
            return True

        # Download with delay
        print(f"  ↓ Downloading: {filename}")
        result.download_pdf(str(filepath))

        # Save metadata
        metadata = {
            'title': result.title,
            'authors': [str(a) for a in result.authors],
            'published': result.published.isoformat(),
            'arxiv_id': result.entry_id.split('/')[-1],
            'abstract': result.summary,
            'categories': result.categories,
            'relevance_score': score,
            'query_category': category,
            'us_affiliation': has_us_affiliation(result),
            'pdf_url': result.pdf_url,
            'downloaded': datetime.now().isoformat()
        }

        metadata_file = filepath.with_suffix('.json')
        with open(metadata_file, 'w') as f:
            json.dump(metadata, f, indent=2)

        time.sleep(DELAY_BETWEEN_DOWNLOADS)
        return True

    except Exception as e:
        print(f"  ✗ Error downloading: {e}")
        return False


def main():
    """Main research execution"""
    print(f"\n{'#'*80}")
    print("# ArXiv DDoS Infrastructure Research - Issue #11")
    print(f"# Target: {TARGET_PAPERS} papers (2024-2025, >7 pages)")
    print(f"# Output: {OUTPUT_DIR}")
    print(f"{'#'*80}\n")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Collect all results
    all_results = []

    for query_dict in SEARCH_QUERIES:
        results = search_and_collect(query_dict)
        for result, score in results:
            all_results.append((result, score, query_dict['name']))
        time.sleep(2)  # Respectful delay between searches

    # Remove duplicates (same arxiv ID), keeping highest score
    unique_results = {}
    for result, score, category in all_results:
        arxiv_id = result.entry_id.split('/')[-1]
        if arxiv_id not in unique_results or score > unique_results[arxiv_id][1]:
            unique_results[arxiv_id] = (result, score, category)

    # Sort by score and take top papers
    sorted_results = sorted(unique_results.values(),
                          key=lambda x: x[1],
                          reverse=True)[:TARGET_PAPERS]

    print(f"\n{'='*80}")
    print(f"DOWNLOADING TOP {len(sorted_results)} PAPERS")
    print(f"{'='*80}\n")

    # Download papers
    downloaded = 0
    failed = 0

    for i, (result, score, category) in enumerate(sorted_results, 1):
        print(f"\n[{i}/{len(sorted_results)}] Score: {score:.1f} | "
              f"Year: {result.published.year} | Category: {category}")
        print(f"Title: {result.title}")

        if download_paper(result, score, category):
            downloaded += 1
        else:
            failed += 1

    # Generate summary report
    print(f"\n{'#'*80}")
    print("# RESEARCH SUMMARY")
    print(f"{'#'*80}\n")
    print(f"Total papers downloaded: {downloaded}")
    print(f"Failed downloads: {failed}")
    print(f"Output directory: {OUTPUT_DIR}")

    # Category breakdown
    category_counts = {}
    for _, _, category in sorted_results[:downloaded]:
        category_counts[category] = category_counts.get(category, 0) + 1

    print("\nPapers by category:")
    for category, count in sorted(category_counts.items(),
                                  key=lambda x: x[1],
                                  reverse=True):
        query_desc = next(q['description'] for q in SEARCH_QUERIES
                         if q['name'] == category)
        print(f"  {category:30s}: {count:2d} papers - {query_desc}")

    # Year breakdown
    year_counts = {}
    for result, _, _ in sorted_results[:downloaded]:
        year = result.published.year
        year_counts[year] = year_counts.get(year, 0) + 1

    print("\nPapers by year:")
    for year in sorted(year_counts.keys(), reverse=True):
        print(f"  {year}: {year_counts[year]} papers")

    # US affiliation count
    us_papers = sum(1 for result, _, _ in sorted_results[:downloaded]
                   if has_us_affiliation(result))
    print(f"\nPapers with US institution affiliation: {us_papers}/{downloaded}")

    # Save summary report
    summary_file = OUTPUT_DIR / f"research_summary_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    summary = {
        'timestamp': datetime.now().isoformat(),
        'total_downloaded': downloaded,
        'total_failed': failed,
        'target_papers': TARGET_PAPERS,
        'category_breakdown': category_counts,
        'year_breakdown': year_counts,
        'us_affiliation_count': us_papers,
        'search_queries': SEARCH_QUERIES
    }

    with open(summary_file, 'w') as f:
        json.dump(summary, f, indent=2)

    print(f"\nSummary saved to: {summary_file}")
    print(f"\n{'#'*80}\n")


if __name__ == '__main__':
    main()
