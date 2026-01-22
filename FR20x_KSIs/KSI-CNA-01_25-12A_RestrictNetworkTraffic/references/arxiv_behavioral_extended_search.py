#!/usr/bin/env python3
"""
Extended ArXiv Research Script: Behavioral Anomaly Detection
Broader search to reach 20-45 papers target
"""

import arxiv
import os
import time
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Tuple

# Configuration
OUTPUT_DIR = Path("/Users/tamnguyen/Documents/GitHub/ksi_watch/KSI-CNA-01_25-12A_RestrictNetworkTraffic/references/behavioral_detection")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

CACHE_FILE = OUTPUT_DIR / "search_cache.txt"
SUMMARY_FILE = Path("/Users/tamnguyen/Documents/GitHub/ksi_watch/KSI-CNA-01_25-12A_RestrictNetworkTraffic/references/behavioral_detection_SUMMARY.md")

# Load existing papers to avoid duplicates
existing_papers = set()
if CACHE_FILE.exists():
    with open(CACHE_FILE, 'r') as f:
        for line in f:
            arxiv_id = line.split('\t')[0]
            existing_papers.add(arxiv_id)

print(f"[INFO] Found {len(existing_papers)} existing papers")

# Broader search queries
EXTENDED_QUERIES = [
    # Anomaly detection in systems
    'abs:"anomaly detection" AND (abs:"user behavior" OR abs:"entity behavior")',
    'abs:"behavioral analysis" AND abs:"security" AND abs:"machine learning"',
    'abs:"behavior analysis" AND abs:"threat detection"',

    # Bot and automation detection
    'abs:"bot detection" AND abs:"behavioral"',
    'abs:"automated attack" AND abs:"detection"',
    'abs:"malicious behavior" AND abs:"detection" AND abs:"machine learning"',

    # Baseline and profiling
    'abs:"user profiling" AND abs:"anomaly detection"',
    'abs:"behavioral profiling" AND abs:"security"',
    'abs:"normal behavior" AND abs:"deviation detection"',

    # Drift and concept drift
    'abs:"concept drift" AND abs:"anomaly detection"',
    'abs:"distribution drift" AND abs:"detection"',
    'abs:"behavior change detection"',

    # Poisoning attacks
    'abs:"poisoning attack" AND abs:"detection"',
    'abs:"adversarial attack" AND abs:"anomaly detection"',
    'abs:"backdoor attack" AND abs:"behavioral"',

    # Insider threats
    'abs:"insider threat" AND abs:"detection" AND abs:"machine learning"',
    'abs:"malicious insider" AND abs:"behavioral"',
    'abs:"user anomaly" AND abs:"detection"',

    # System and network behavior
    'abs:"system behavior" AND abs:"anomaly detection"',
    'abs:"process behavior" AND abs:"anomaly"',
    'abs:"API behavior" AND abs:"anomaly detection"',

    # AI/ML security
    'abs:"AI security" AND abs:"behavioral"',
    'abs:"machine learning" AND abs:"behavior monitoring"',
    'abs:"deep learning" AND abs:"anomaly detection" AND abs:"behavioral"',

    # Time series and temporal
    'abs:"time series" AND abs:"anomaly detection" AND abs:"behavioral"',
    'abs:"temporal anomaly" AND abs:"behavioral"',
    'abs:"sequential behavior" AND abs:"anomaly"',

    # Access and authentication
    'abs:"authentication" AND abs:"anomaly detection" AND abs:"behavioral"',
    'abs:"access pattern" AND abs:"anomaly detection"',
    'abs:"credential abuse" AND abs:"detection"',

    # Zero trust and identity
    'abs:"zero trust" AND abs:"behavioral" AND abs:"detection"',
    'abs:"identity verification" AND abs:"behavioral"',
    'abs:"continuous authentication" AND abs:"behavioral"',
]

def search_arxiv(query: str, max_results: int = 100) -> List[arxiv.Result]:
    """Search ArXiv with query and return results."""
    print(f"\n[SEARCH] Query: {query[:100]}...")

    search = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.SubmittedDate,
        sort_order=arxiv.SortOrder.Descending
    )

    results = []
    for result in search.results():
        # Filter for 2024-2025 papers
        if result.published.year >= 2024:
            arxiv_id = result.entry_id.split('/')[-1]
            if arxiv_id not in existing_papers:
                results.append(result)

    print(f"[INFO] Found {len(results)} new papers from 2024-2025")
    return results

def is_relevant(result: arxiv.Result) -> Tuple[bool, int]:
    """Check if paper is relevant to behavioral anomaly detection."""
    title_lower = result.title.lower()
    summary_lower = result.summary.lower()
    text = title_lower + " " + summary_lower

    score = 0

    # High priority keywords (3 points each)
    high_priority = [
        "behavioral anomaly",
        "behavior anomaly",
        "behavioral baseline",
        "behavior baseline",
        "baseline poisoning",
        "behavioral poisoning",
        "ai agent behavior",
        "service account",
        "non-human identity",
        "behavioral monitoring",
        "behavior profiling",
        "behavioral profiling",
        "insider threat",
    ]
    for keyword in high_priority:
        if keyword in text:
            score += 3

    # Medium priority keywords (2 points each)
    medium_priority = [
        "anomaly detection",
        "behavioral pattern",
        "behavior pattern",
        "drift detection",
        "behavioral drift",
        "concept drift",
        "false positive",
        "automated system",
        "autonomous agent",
        "bot detection",
        "lateral movement",
        "user behavior",
        "entity behavior",
        "malicious behavior",
        "behavior analysis",
        "behavioral analysis",
        "poisoning attack",
        "adversarial attack",
        "user anomaly",
        "access pattern",
    ]
    for keyword in medium_priority:
        if keyword in text:
            score += 2

    # Low priority keywords (1 point each)
    low_priority = [
        "machine learning",
        "deep learning",
        "neural network",
        "real-time",
        "production",
        "security",
        "threat detection",
        "time series",
        "temporal",
        "authentication",
        "zero trust",
    ]
    for keyword in low_priority:
        if keyword in text:
            score += 1

    # Negative keywords
    negative = [
        "medical",
        "healthcare",
        "clinical",
        "patient",
        "disease",
        "biological",
        "cattle",
        "animal",
        "livestock",
        "image classification",
        "video analysis",
        "image processing",
        "computer vision",
    ]
    for keyword in negative:
        if keyword in text:
            score -= 3

    # Require minimum score of 5 for relevance
    return (score >= 5, score)

def download_paper(result: arxiv.Result, output_dir: Path) -> bool:
    """Download paper PDF if not already downloaded."""
    safe_title = "".join(c for c in result.title if c.isalnum() or c in (' ', '-', '_')).strip()
    safe_title = safe_title[:100]

    arxiv_id = result.entry_id.split('/')[-1]
    filename = f"{arxiv_id}_{safe_title}.pdf"
    filepath = output_dir / filename

    if filepath.exists():
        print(f"[SKIP] Already downloaded: {filename}")
        return True

    try:
        print(f"[DOWNLOAD] {filename}")
        result.download_pdf(dirpath=str(output_dir), filename=filename)
        time.sleep(2)
        return True
    except Exception as e:
        print(f"[ERROR] Failed to download {filename}: {e}")
        return False

def main():
    """Main execution function."""
    print("="*80)
    print("Extended ArXiv Research: Behavioral Anomaly Detection")
    print("="*80)

    all_papers = {}

    # Execute searches
    for i, query in enumerate(EXTENDED_QUERIES, 1):
        print(f"\n[QUERY {i}/{len(EXTENDED_QUERIES)}]")
        try:
            results = search_arxiv(query, max_results=100)

            for result in results:
                arxiv_id = result.entry_id.split('/')[-1]

                is_rel, score = is_relevant(result)

                if is_rel:
                    if arxiv_id not in all_papers or score > all_papers[arxiv_id][1]:
                        all_papers[arxiv_id] = (result, score)
                        print(f"  [RELEVANT] Score={score}: {result.title[:80]}")

            time.sleep(3)

        except Exception as e:
            print(f"[ERROR] Query failed: {e}")
            continue

    # Sort papers by relevance score
    sorted_papers = sorted(all_papers.values(), key=lambda x: x[1], reverse=True)

    print(f"\n{'='*80}")
    print(f"New relevant papers found: {len(sorted_papers)}")
    print(f"Total papers (including existing): {len(sorted_papers) + len(existing_papers)}")
    print(f"{'='*80}")

    # Download papers
    downloaded = []
    target_count = min(50, len(sorted_papers))

    print(f"\n[INFO] Downloading {target_count} papers...")

    for i, (result, score) in enumerate(sorted_papers[:target_count], 1):
        print(f"\n[{i}/{target_count}] Score={score}")
        print(f"  Title: {result.title}")

        if download_paper(result, OUTPUT_DIR):
            downloaded.append((result, score))

    # Update cache
    with open(CACHE_FILE, 'a') as f:
        for result, score in downloaded:
            arxiv_id = result.entry_id.split('/')[-1]
            f.write(f"{arxiv_id}\t{score}\t{result.title}\n")

    print(f"\n[SUCCESS] Downloaded {len(downloaded)} new papers")
    print(f"[INFO] Total papers now: {len(downloaded) + len(existing_papers)}")

if __name__ == "__main__":
    main()
