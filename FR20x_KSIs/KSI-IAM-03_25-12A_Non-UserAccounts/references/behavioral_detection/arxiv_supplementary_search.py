#!/usr/bin/env python3
"""
Supplementary ArXiv Search: Targeted queries for specific research gaps
Focus on: agent authentication, behavioral profiling, adversarial ML, continuous monitoring
"""

import arxiv
import time
import os
from typing import List, Dict
from datetime import datetime
from pathlib import Path
import json

# Target directory
TARGET_DIR = Path("/Users/tamnguyen/Documents/GitHub/ksi_watch/KSI-IAM-03_25-12A_Non-UserAccounts/references/behavioral_detection")
CACHE_FILE = TARGET_DIR / "search_cache.json"
METADATA_FILE = TARGET_DIR / "papers_metadata.json"

# Download delay
DOWNLOAD_DELAY = 3.5

# Supplementary search queries - more targeted
SUPPLEMENTARY_QUERIES = [
    # Agent authentication and identity
    {
        "query": '(abs:"agent authentication" OR abs:"service account" OR abs:"machine identity") AND (abs:"security" OR abs:"behavioral" OR abs:"monitoring") AND (abs:"machine learning" OR abs:"detection")',
        "category": "agent_authentication",
        "max_results": 50
    },
    # Behavioral profiling and fingerprinting
    {
        "query": '(abs:"behavioral profiling" OR abs:"behavioral fingerprint" OR abs:"behavior fingerprint") AND (abs:"machine learning" OR abs:"detection" OR abs:"classification") AND (abs:"security" OR abs:"authentication")',
        "category": "behavioral_profiling",
        "max_results": 50
    },
    # Continuous monitoring and verification
    {
        "query": '(abs:"continuous monitoring" OR abs:"continuous verification") AND (abs:"behavioral" OR abs:"behaviour") AND (abs:"anomaly" OR abs:"detection") AND (abs:"security" OR abs:"authentication")',
        "category": "continuous_monitoring",
        "max_results": 50
    },
    # Adversarial machine learning for security
    {
        "query": '(abs:"adversarial machine learning" OR abs:"adversarial robustness") AND (abs:"anomaly detection" OR abs:"behavioral detection") AND (abs:"security" OR abs:"defense")',
        "category": "adversarial_ml_security",
        "max_results": 50
    },
    # Time series anomaly for behavioral data
    {
        "query": '(abs:"time series anomaly" OR abs:"sequential anomaly") AND (abs:"behavioral" OR abs:"behaviour") AND (abs:"machine learning" OR abs:"deep learning") AND (abs:"detection" OR abs:"monitoring")',
        "category": "timeseries_behavioral",
        "max_results": 50
    },
    # Data poisoning and backdoor attacks
    {
        "query": '(abs:"data poisoning" OR abs:"backdoor attack") AND (abs:"anomaly detection" OR abs:"detection system") AND (abs:"defense" OR abs:"mitigation" OR abs:"robustness")',
        "category": "poisoning_backdoor",
        "max_results": 50
    },
    # Zero-day and novel attack detection
    {
        "query": '(abs:"zero-day" OR abs:"novel attack" OR abs:"unknown attack") AND (abs:"behavioral" OR abs:"behaviour" OR abs:"anomaly") AND (abs:"detection" OR abs:"machine learning")',
        "category": "zeroday_behavioral",
        "max_results": 50
    },
    # Adaptive security and dynamic baselines
    {
        "query": '(abs:"adaptive security" OR abs:"dynamic baseline" OR abs:"adaptive baseline") AND (abs:"behavioral" OR abs:"behaviour") AND (abs:"detection" OR abs:"monitoring" OR abs:"authentication")',
        "category": "adaptive_baseline",
        "max_results": 50
    }
]

def load_cache() -> Dict:
    """Load cached search results"""
    if CACHE_FILE.exists():
        with open(CACHE_FILE, 'r') as f:
            return json.load(f)
    return {"downloaded_papers": [], "search_history": []}

def save_cache(cache: Dict):
    """Save search cache"""
    with open(CACHE_FILE, 'w') as f:
        json.dump(cache, f, indent=2)

def load_existing_metadata() -> Dict:
    """Load existing metadata"""
    if METADATA_FILE.exists():
        with open(METADATA_FILE, 'r') as f:
            return json.load(f)
    return {"papers": []}

def is_recent_paper(published: datetime, cutoff_year: int = 2024) -> bool:
    """Check if paper is from 2024 or later"""
    return published.year >= cutoff_year

def is_substantial_paper(result: arxiv.Result) -> bool:
    """Check if paper is substantial"""
    abstract_words = len(result.summary.split())
    author_count = len(result.authors)
    return abstract_words > 150 or author_count >= 3

def calculate_relevance_score(result: arxiv.Result, category: str) -> float:
    """Calculate relevance score"""
    score = 0.0
    text = (result.title + " " + result.summary).lower()

    # High-value keywords for supplementary search
    core_keywords = {
        "agent authentication": 3.5,
        "service account": 3.0,
        "machine identity": 3.0,
        "behavioral profiling": 3.5,
        "behavioral fingerprint": 3.5,
        "continuous monitoring": 2.5,
        "continuous verification": 2.5,
        "adversarial machine learning": 2.5,
        "data poisoning": 3.0,
        "backdoor attack": 3.0,
        "zero-day": 2.5,
        "adaptive baseline": 3.0,
        "dynamic baseline": 2.5,
        "time series anomaly": 2.0
    }

    supporting_keywords = {
        "anomaly detection": 1.5,
        "behavioral detection": 2.0,
        "authentication": 1.5,
        "security": 1.0,
        "machine learning": 1.0,
        "deep learning": 1.0,
        "monitoring": 1.5,
        "detection": 1.0,
        "defense": 1.5,
        "robustness": 1.5,
        "mitigation": 1.5
    }

    empirical_keywords = {
        "evaluation": 1.0,
        "experiment": 1.0,
        "deployment": 1.5,
        "production": 1.5,
        "real-world": 2.0,
        "case study": 1.5,
        "empirical": 1.5,
        "accuracy": 1.0,
        "performance": 1.0
    }

    for keyword, weight in core_keywords.items():
        if keyword in text:
            score += weight

    for keyword, weight in supporting_keywords.items():
        if keyword in text:
            score += weight

    for keyword, weight in empirical_keywords.items():
        if keyword in text:
            score += weight

    return score

def search_and_download(query_config: Dict, cache: Dict, target_total: int = 45) -> List[Dict]:
    """Execute search query and download relevant papers"""
    query = query_config["query"]
    category = query_config["category"]
    max_results = query_config["max_results"]

    # Load existing metadata to check total count
    existing_metadata = load_existing_metadata()
    current_total = len(existing_metadata.get("papers", []))

    print(f"\n{'='*80}")
    print(f"Searching: {category}")
    print(f"Current total: {current_total} papers")
    print(f"Target: {target_total} papers")
    print(f"{'='*80}\n")

    if current_total >= target_total:
        print(f"✓ Target already reached ({current_total} papers)")
        return []

    search = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.SubmittedDate,
        sort_order=arxiv.SortOrder.Descending
    )

    papers_metadata = []
    downloaded_count = 0

    for result in search.results():
        # Check if we've reached target
        if current_total + downloaded_count >= target_total:
            print(f"\n✓ Target reached: {current_total + downloaded_count} total papers")
            break

        # Check if already downloaded
        paper_id = result.entry_id.split('/')[-1]
        if paper_id in cache["downloaded_papers"]:
            continue

        # Filter by year
        if not is_recent_paper(result.published, cutoff_year=2024):
            continue

        # Check if substantial
        if not is_substantial_paper(result):
            continue

        # Calculate relevance
        relevance = calculate_relevance_score(result, category)

        # Download if relevance is high enough
        if relevance >= 3.0:
            try:
                safe_title = "".join(c if c.isalnum() or c in (' ', '-', '_') else '_' for c in result.title)
                safe_title = safe_title[:100]
                filename = f"{paper_id.replace('/', '_')}_{safe_title}.pdf"
                filepath = TARGET_DIR / filename

                print(f"  ↓ Downloading [Relevance: {relevance:.1f}]: {result.title}")
                print(f"    Published: {result.published.strftime('%Y-%m-%d')}")

                result.download_pdf(dirpath=str(TARGET_DIR), filename=filename)

                metadata = {
                    "paper_id": paper_id,
                    "title": result.title,
                    "authors": [a.name for a in result.authors],
                    "published": result.published.strftime('%Y-%m-%d'),
                    "updated": result.updated.strftime('%Y-%m-%d'),
                    "categories": result.categories,
                    "primary_category": result.primary_category,
                    "abstract": result.summary,
                    "pdf_url": result.pdf_url,
                    "entry_id": result.entry_id,
                    "relevance_score": relevance,
                    "search_category": category,
                    "filename": filename,
                    "downloaded_at": datetime.now().isoformat()
                }
                papers_metadata.append(metadata)

                cache["downloaded_papers"].append(paper_id)
                downloaded_count += 1
                print(f"    ✓ Downloaded ({current_total + downloaded_count} total)\n")

                time.sleep(DOWNLOAD_DELAY)

            except Exception as e:
                print(f"    ✗ Error: {str(e)}\n")
                continue

    save_cache(cache)
    return papers_metadata

def main():
    """Main execution"""
    print("="*80)
    print("Supplementary ArXiv Search: Behavioral Detection for AI Agents")
    print("="*80)

    cache = load_cache()
    existing_metadata = load_existing_metadata()
    current_total = len(existing_metadata.get("papers", []))

    print(f"\nCurrent papers: {current_total}")
    print(f"Target: 35-45 papers")
    print(f"Need: {max(0, 35 - current_total)} to {max(0, 45 - current_total)} more papers")
    print("="*80)

    if current_total >= 45:
        print("\n✓ Target already reached!")
        return

    all_new_metadata = []

    for query_config in SUPPLEMENTARY_QUERIES:
        papers = search_and_download(query_config, cache, target_total=45)
        all_new_metadata.extend(papers)

        # Update metadata file incrementally
        existing_metadata["papers"].extend(papers)
        existing_metadata["total_papers"] = len(existing_metadata["papers"])
        with open(METADATA_FILE, 'w') as f:
            json.dump(existing_metadata, f, indent=2)

        if len(existing_metadata["papers"]) >= 45:
            break

        time.sleep(2)

    print("\n" + "="*80)
    print("SUPPLEMENTARY SEARCH COMPLETE")
    print("="*80)
    print(f"New papers downloaded: {len(all_new_metadata)}")
    print(f"Total papers: {len(existing_metadata['papers'])}")
    print("="*80)

if __name__ == "__main__":
    main()
