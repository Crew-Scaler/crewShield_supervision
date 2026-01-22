#!/usr/bin/env python3
"""
ArXiv DDoS Infrastructure Research Script v2 for Issue #11
Fixed version with direct PDF downloads
"""

import arxiv
import time
import os
import requests
from pathlib import Path
from typing import List, Dict, Tuple
import json
from datetime import datetime
import re

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

# Simplified, focused search queries for DDoS infrastructure
SEARCH_QUERIES = [
    {
        'name': 'ddos_mitigation',
        'query': 'abs:DDoS AND (mitigation OR defense OR protection) AND (infrastructure OR architecture OR system)',
        'description': 'DDoS mitigation infrastructure'
    },
    {
        'name': 'edge_cdn_security',
        'query': 'abs:(edge OR CDN OR anycast) AND (DDoS OR attack OR security)',
        'description': 'Edge computing and CDN security'
    },
    {
        'name': 'cloud_security',
        'query': 'abs:(cloud OR microservice OR serverless) AND (DDoS OR attack OR resilience)',
        'description': 'Cloud-native security'
    },
    {
        'name': 'network_defense',
        'query': 'abs:(network OR traffic) AND (defense OR filtering OR scrubbing) AND (attack OR DDoS)',
        'description': 'Network defense systems'
    },
    {
        'name': 'distributed_defense',
        'query': 'abs:distributed AND (defense OR mitigation OR resilience) AND (attack OR security)',
        'description': 'Distributed defense mechanisms'
    }
]


def safe_filename(s: str) -> str:
    """Create safe filename from string"""
    s = re.sub(r'[^\w\s-]', '', s)
    s = re.sub(r'[-\s]+', '_', s)
    return s[:100]


def estimate_pages(result) -> int:
    """Estimate number of pages from result metadata"""
    if hasattr(result, 'comment') and result.comment:
        comment = result.comment.lower()
        if 'pages' in comment or 'page' in comment:
            try:
                # Extract number before 'page' or 'pages'
                match = re.search(r'(\d+)\s*pages?', comment, re.IGNORECASE)
                if match:
                    return int(match.group(1))
            except:
                pass
    return 10  # Conservative estimate


def has_us_affiliation(result) -> bool:
    """Check if paper has US institution affiliation"""
    text = str(result.authors) + ' ' + (result.comment or '')
    text = text.lower()
    return any(inst.lower() in text for inst in US_INSTITUTIONS)


def calculate_relevance_score(result, query_name: str) -> float:
    """Calculate relevance score for prioritization"""
    score = 0.0

    # Recency bonus
    year = result.published.year
    if year == 2025:
        score += 10.0
    elif year == 2024:
        score += 5.0
    else:
        return 0.0  # Skip older papers

    # US institution bonus
    if has_us_affiliation(result):
        score += 3.0

    # DDoS-specific keywords in title
    title_lower = result.title.lower()
    ddos_keywords = ['ddos', 'denial of service', 'dos attack']
    if any(kw in title_lower for kw in ddos_keywords):
        score += 5.0

    # Infrastructure keywords
    infra_keywords = [
        'infrastructure', 'architecture', 'system', 'defense',
        'mitigation', 'protection', 'security', 'resilience',
        'cloud', 'edge', 'cdn', 'distributed', 'network'
    ]
    score += sum(1.0 for kw in infra_keywords if kw in title_lower)

    # Abstract keywords
    abstract_lower = result.summary.lower()
    if 'ddos' in abstract_lower:
        score += 2.0
    if 'infrastructure' in abstract_lower or 'architecture' in abstract_lower:
        score += 1.5

    return score


def download_pdf_direct(pdf_url: str, filepath: Path) -> bool:
    """Download PDF using direct HTTP request"""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        }
        response = requests.get(pdf_url, headers=headers, timeout=30, stream=True)
        response.raise_for_status()

        with open(filepath, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)

        # Verify file is not empty
        if filepath.stat().st_size < 1000:
            print(f"    Warning: Downloaded file is very small ({filepath.stat().st_size} bytes)")
            return False

        return True
    except Exception as e:
        print(f"    Download error: {e}")
        return False


def search_and_collect(query_dict: Dict) -> List[Tuple[arxiv.Result, float]]:
    """Search ArXiv and collect results with relevance scores"""
    print(f"\n{'='*80}")
    print(f"Searching: {query_dict['description']}")
    print(f"{'='*80}")

    search = arxiv.Search(
        query=query_dict['query'],
        max_results=50,
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
        if estimated_pages < MIN_PAGES:
            continue

        # Calculate relevance score
        score = calculate_relevance_score(result, query_dict['name'])
        if score < 5.0:  # Minimum threshold
            continue

        results_with_scores.append((result, score))
        print(f"  ✓ [{result.published.year}] Score: {score:.1f}: {result.title[:70]}...")

    results_with_scores.sort(key=lambda x: x[1], reverse=True)
    print(f"\nFound {len(results_with_scores)} relevant papers")
    return results_with_scores


def download_paper(result: arxiv.Result, score: float, category: str) -> bool:
    """Download a single paper with metadata"""
    try:
        # Create safe filename
        first_author = str(result.authors[0]).split()[-1] if result.authors else 'Unknown'
        year = result.published.year
        title_clean = safe_filename(result.title)

        filename = f"{year}_{first_author}_{title_clean}.pdf"
        filepath = OUTPUT_DIR / filename

        # Skip if already downloaded
        if filepath.exists() and filepath.stat().st_size > 10000:
            print(f"  ⊙ Already exists: {filename}")
            return True

        # Download PDF
        print(f"  ↓ Downloading: {filename}")
        pdf_url = result.pdf_url

        if download_pdf_direct(pdf_url, filepath):
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

            print(f"    ✓ Success ({filepath.stat().st_size / 1024:.1f} KB)")
            time.sleep(DELAY_BETWEEN_DOWNLOADS)
            return True
        else:
            if filepath.exists():
                filepath.unlink()
            return False

    except Exception as e:
        print(f"  ✗ Error: {e}")
        return False


def main():
    """Main research execution"""
    print(f"\n{'#'*80}")
    print("# ArXiv DDoS Infrastructure Research - Issue #11 (v2)")
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
        time.sleep(2)

    # Remove duplicates
    unique_results = {}
    for result, score, category in all_results:
        arxiv_id = result.entry_id.split('/')[-1]
        if arxiv_id not in unique_results or score > unique_results[arxiv_id][1]:
            unique_results[arxiv_id] = (result, score, category)

    # Sort by score
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
        print(f"\n[{i}/{len(sorted_results)}] Score: {score:.1f} | Year: {result.published.year}")
        print(f"Title: {result.title}")

        if download_paper(result, score, category):
            downloaded += 1
        else:
            failed += 1

    # Generate summary
    print(f"\n{'#'*80}")
    print("# RESEARCH SUMMARY")
    print(f"{'#'*80}\n")
    print(f"Total papers downloaded: {downloaded}")
    print(f"Failed downloads: {failed}")

    # Category breakdown
    category_counts = {}
    for result, _, category in sorted_results[:downloaded]:
        category_counts[category] = category_counts.get(category, 0) + 1

    print("\nPapers by category:")
    for category, count in sorted(category_counts.items(), key=lambda x: x[1], reverse=True):
        print(f"  {category:30s}: {count:2d} papers")

    # Year breakdown
    year_counts = {}
    for result, _, _ in sorted_results[:downloaded]:
        year = result.published.year
        year_counts[year] = year_counts.get(year, 0) + 1

    print("\nPapers by year:")
    for year in sorted(year_counts.keys(), reverse=True):
        print(f"  {year}: {year_counts[year]} papers")

    # US affiliation
    us_papers = sum(1 for result, _, _ in sorted_results[:downloaded]
                   if has_us_affiliation(result))
    print(f"\nUS institution papers: {us_papers}/{downloaded}")

    # Save summary
    summary_file = OUTPUT_DIR / f"research_summary_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    summary = {
        'timestamp': datetime.now().isoformat(),
        'total_downloaded': downloaded,
        'total_failed': failed,
        'category_breakdown': category_counts,
        'year_breakdown': year_counts,
        'us_affiliation_count': us_papers
    }

    with open(summary_file, 'w') as f:
        json.dump(summary, f, indent=2)

    print(f"\nSummary saved to: {summary_file}")
    print(f"\n{'#'*80}\n")


if __name__ == '__main__':
    main()
