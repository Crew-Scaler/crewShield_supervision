#!/usr/bin/env python3
"""
ArXiv Research Script: Behavioral Anomaly Detection for AI Agents and NHI
Focus: Service account monitoring, ML-based anomaly detection, baseline poisoning
Date Range: 2024-2025
Target: 20-45 papers
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

# Search queries targeting behavioral anomaly detection for AI systems
SEARCH_QUERIES = [
    # Core behavioral anomaly detection
    'abs:"behavioral anomaly detection" AND (abs:"AI agent" OR abs:"service account" OR abs:"automated system")',
    'abs:"anomaly detection" AND abs:"behavioral baseline" AND (abs:"machine learning" OR abs:"deep learning")',
    'abs:"behavioral monitoring" AND (abs:"non-human identity" OR abs:"service account" OR abs:"bot detection")',

    # Baseline establishment and drift
    'abs:"baseline establishment" AND abs:"anomaly detection" AND abs:"behavioral"',
    'abs:"behavioral drift detection" AND (abs:"machine learning" OR abs:"AI system")',
    'abs:"behavior profiling" AND abs:"anomaly detection" AND abs:"automated"',

    # Baseline poisoning and attacks
    'abs:"baseline poisoning" OR abs:"behavioral poisoning attack"',
    'abs:"data poisoning" AND abs:"anomaly detection" AND abs:"behavioral"',
    'abs:"adversarial attacks" AND abs:"behavioral detection"',

    # False positive reduction
    'abs:"false positive reduction" AND abs:"anomaly detection"',
    'abs:"anomaly detection" AND abs:"precision" AND abs:"behavioral"',

    # AI agent specific
    'abs:"AI agent" AND abs:"behavioral pattern" AND abs:"detection"',
    'abs:"autonomous agent" AND abs:"anomaly detection" AND abs:"behavioral"',
    'abs:"agent behavior" AND abs:"monitoring" AND abs:"security"',

    # NHI and service accounts
    'abs:"service account" AND abs:"behavioral" AND abs:"security"',
    'abs:"non-human entity" AND abs:"behavior" AND abs:"detection"',
    'abs:"bot behavior" AND abs:"detection" AND abs:"machine learning"',

    # Lateral movement and threat detection
    'abs:"lateral movement" AND abs:"detection" AND abs:"behavioral"',
    'abs:"insider threat" AND abs:"behavioral anomaly"',
    'abs:"privilege escalation" AND abs:"behavioral detection"',

    # Production systems
    'abs:"production system" AND abs:"anomaly detection" AND abs:"behavioral"',
    'abs:"real-time anomaly detection" AND abs:"behavioral"',
    'abs:"online anomaly detection" AND abs:"behavioral pattern"',
]

def search_arxiv(query: str, max_results: int = 50) -> List[arxiv.Result]:
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
            results.append(result)

    print(f"[INFO] Found {len(results)} papers from 2024-2025")
    return results

def is_relevant(result: arxiv.Result) -> Tuple[bool, int]:
    """
    Check if paper is relevant to behavioral anomaly detection for AI/NHI.
    Returns (is_relevant, relevance_score)
    """
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
        "nhi",
        "behavioral monitoring",
        "behavior profiling",
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
        "false positive",
        "automated system",
        "autonomous agent",
        "bot detection",
        "lateral movement",
        "insider threat",
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
    ]
    for keyword in low_priority:
        if keyword in text:
            score += 1

    # Negative keywords (reduce relevance)
    negative = [
        "medical",
        "healthcare",
        "clinical",
        "patient",
        "disease",
        "biological",
        "network traffic",  # Too specific to network layer
        "image",
        "video",
    ]
    for keyword in negative:
        if keyword in text:
            score -= 2

    # Require minimum score of 5 for relevance
    return (score >= 5, score)

def download_paper(result: arxiv.Result, output_dir: Path) -> bool:
    """Download paper PDF if not already downloaded."""
    # Create safe filename
    safe_title = "".join(c for c in result.title if c.isalnum() or c in (' ', '-', '_')).strip()
    safe_title = safe_title[:100]  # Limit length

    # Extract arXiv ID for filename
    arxiv_id = result.entry_id.split('/')[-1]
    filename = f"{arxiv_id}_{safe_title}.pdf"
    filepath = output_dir / filename

    if filepath.exists():
        print(f"[SKIP] Already downloaded: {filename}")
        return True

    try:
        print(f"[DOWNLOAD] {filename}")
        result.download_pdf(dirpath=str(output_dir), filename=filename)
        time.sleep(2)  # Rate limiting
        return True
    except Exception as e:
        print(f"[ERROR] Failed to download {filename}: {e}")
        return False

def main():
    """Main execution function."""
    print("="*80)
    print("ArXiv Research: Behavioral Anomaly Detection for AI Agents and NHI")
    print("="*80)

    all_papers = {}  # Dict to deduplicate: arxiv_id -> (result, score)

    # Execute searches
    for i, query in enumerate(SEARCH_QUERIES, 1):
        print(f"\n[QUERY {i}/{len(SEARCH_QUERIES)}]")
        try:
            results = search_arxiv(query, max_results=50)

            for result in results:
                arxiv_id = result.entry_id.split('/')[-1]

                # Check relevance
                is_rel, score = is_relevant(result)

                if is_rel:
                    # Keep paper with highest score if duplicate
                    if arxiv_id not in all_papers or score > all_papers[arxiv_id][1]:
                        all_papers[arxiv_id] = (result, score)
                        print(f"  [RELEVANT] Score={score}: {result.title[:80]}")

            time.sleep(3)  # Rate limiting between queries

        except Exception as e:
            print(f"[ERROR] Query failed: {e}")
            continue

    # Sort papers by relevance score
    sorted_papers = sorted(all_papers.values(), key=lambda x: x[1], reverse=True)

    print(f"\n{'='*80}")
    print(f"Total relevant papers found: {len(sorted_papers)}")
    print(f"{'='*80}")

    # Download top papers (target 20-45)
    target_count = min(45, len(sorted_papers))
    downloaded = []

    print(f"\n[INFO] Downloading top {target_count} papers...")

    for i, (result, score) in enumerate(sorted_papers[:target_count], 1):
        print(f"\n[{i}/{target_count}] Score={score}")
        print(f"  Title: {result.title}")
        print(f"  Published: {result.published.strftime('%Y-%m-%d')}")

        if download_paper(result, OUTPUT_DIR):
            downloaded.append((result, score))

    # Generate summary metadata
    print(f"\n[INFO] Generating summary file...")

    with open(SUMMARY_FILE, 'w') as f:
        f.write("# Behavioral Anomaly Detection for AI Agents and Non-Human Identities\n\n")
        f.write(f"**Research Date:** {datetime.now().strftime('%Y-%m-%d')}\n")
        f.write(f"**Papers Downloaded:** {len(downloaded)}\n")
        f.write(f"**Date Range:** 2024-2025\n\n")

        f.write("## Research Focus\n\n")
        f.write("- Service account and NHI behavioral monitoring\n")
        f.write("- ML-based anomaly detection for automated systems\n")
        f.write("- Behavioral baseline establishment and drift detection\n")
        f.write("- Baseline poisoning attacks and defense\n")
        f.write("- False positive reduction in high-velocity environments\n")
        f.write("- AI agent behavioral patterns\n\n")

        f.write("## Papers by Relevance Score\n\n")

        for i, (result, score) in enumerate(downloaded, 1):
            arxiv_id = result.entry_id.split('/')[-1]
            f.write(f"### {i}. {result.title}\n\n")
            f.write(f"- **ArXiv ID:** {arxiv_id}\n")
            f.write(f"- **Relevance Score:** {score}\n")
            f.write(f"- **Published:** {result.published.strftime('%Y-%m-%d')}\n")
            f.write(f"- **Authors:** {', '.join([a.name for a in result.authors[:3]])}")
            if len(result.authors) > 3:
                f.write(f" et al. ({len(result.authors)} total)")
            f.write("\n")
            f.write(f"- **URL:** {result.entry_id}\n")
            f.write(f"- **Categories:** {', '.join(result.categories)}\n\n")
            f.write(f"**Abstract:**\n{result.summary[:500]}...\n\n")
            f.write("---\n\n")

    print(f"\n[SUCCESS] Summary written to: {SUMMARY_FILE}")
    print(f"[SUCCESS] Downloaded {len(downloaded)} papers to: {OUTPUT_DIR}")

    # Save cache of downloaded papers
    with open(CACHE_FILE, 'w') as f:
        for result, score in downloaded:
            arxiv_id = result.entry_id.split('/')[-1]
            f.write(f"{arxiv_id}\t{score}\t{result.title}\n")

    print(f"\n{'='*80}")
    print("Research complete!")
    print(f"{'='*80}")

if __name__ == "__main__":
    main()
