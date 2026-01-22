#!/usr/bin/env python3
"""
ArXiv Research: AI Agent Behavioral Anomaly Detection & Authentication
Issue #16: Behavioral baseline construction, poisoning attacks, and context-aware auth

Research Focus:
- ML-based baseline construction for non-human agent behavior
- Behavioral baseline poisoning attacks
- Model drift in behavioral monitoring (2-5% monthly claim validation)
- Context-aware authentication frameworks
"""

import arxiv
import time
import os
from typing import List, Dict, Tuple
from datetime import datetime, timedelta
from pathlib import Path
import json

# Target directory
TARGET_DIR = Path("/Users/tamnguyen/Documents/GitHub/ksi_watch/KSI-IAM-03_25-12A_Non-UserAccounts/references/behavioral_detection")
CACHE_FILE = TARGET_DIR / "search_cache.json"
METADATA_FILE = TARGET_DIR / "papers_metadata.json"

# Download delay in seconds (3+ seconds between downloads)
DOWNLOAD_DELAY = 3.5

# Search queries targeting behavioral detection for AI agents
SEARCH_QUERIES = [
    # Core behavioral anomaly detection for AI agents
    {
        "query": '(abs:"behavioral anomaly detection" OR abs:"behaviour anomaly detection") AND (abs:"AI agent" OR abs:"autonomous agent" OR abs:"intelligent agent") AND (abs:"non-human" OR abs:"baseline" OR abs:"authentication")',
        "category": "behavioral_anomaly_core",
        "max_results": 80
    },
    # Baseline construction and poisoning
    {
        "query": '(abs:"baseline poisoning" OR abs:"baseline attack") AND (abs:"anomaly detection" OR abs:"behavioral" OR abs:"behaviour") AND (abs:"agent" OR abs:"autonomous")',
        "category": "baseline_poisoning",
        "max_results": 60
    },
    # Model drift in behavioral systems
    {
        "query": '(abs:"model drift" OR abs:"concept drift" OR abs:"baseline drift") AND (abs:"behavioral" OR abs:"behaviour") AND (abs:"monitoring" OR abs:"detection" OR abs:"authentication")',
        "category": "model_drift_behavioral",
        "max_results": 60
    },
    # Context-aware authentication for agents
    {
        "query": '(abs:"context-aware authentication" OR abs:"contextual authentication") AND (abs:"AI agent" OR abs:"autonomous agent" OR abs:"intelligent agent" OR abs:"behavioral")',
        "category": "context_aware_auth",
        "max_results": 60
    },
    # Agent behavior baseline construction
    {
        "query": '(abs:"behavior baseline" OR abs:"behaviour baseline" OR abs:"behavioral profile") AND (abs:"AI agent" OR abs:"autonomous system" OR abs:"machine learning") AND (abs:"construction" OR abs:"learning" OR abs:"establishment")',
        "category": "baseline_construction",
        "max_results": 60
    },
    # Real-time behavioral monitoring
    {
        "query": '(abs:"real-time" OR abs:"runtime") AND (abs:"behavioral monitoring" OR abs:"behaviour monitoring" OR abs:"behavioral verification") AND (abs:"AI agent" OR abs:"autonomous agent" OR abs:"authentication")',
        "category": "realtime_behavioral",
        "max_results": 60
    },
    # Anomaly detection with ML for agent security
    {
        "query": '(abs:"anomaly detection" OR abs:"outlier detection") AND (abs:"machine learning" OR abs:"deep learning") AND (abs:"AI agent" OR abs:"autonomous agent") AND (abs:"security" OR abs:"authentication")',
        "category": "ml_anomaly_agent_security",
        "max_results": 80
    },
    # Adversarial attacks on behavioral detection
    {
        "query": '(abs:"adversarial attack" OR abs:"evasion attack") AND (abs:"behavioral detection" OR abs:"behaviour detection" OR abs:"anomaly detection") AND (abs:"agent" OR abs:"autonomous")',
        "category": "adversarial_behavioral",
        "max_results": 60
    },
    # Non-human behavior characterization
    {
        "query": '(abs:"non-human behavior" OR abs:"bot behavior" OR abs:"automated behavior") AND (abs:"detection" OR abs:"characterization" OR abs:"modeling") AND (abs:"machine learning" OR abs:"baseline")',
        "category": "nonhuman_behavior",
        "max_results": 60
    },
    # Behavioral biometrics for authentication
    {
        "query": '(abs:"behavioral biometric" OR abs:"behavioral authentication") AND (abs:"continuous authentication" OR abs:"anomaly detection") AND (abs:"machine learning" OR abs:"AI")',
        "category": "behavioral_biometrics",
        "max_results": 60
    }
]

def load_cache() -> Dict:
    """Load cached search results to avoid re-downloading"""
    if CACHE_FILE.exists():
        with open(CACHE_FILE, 'r') as f:
            return json.load(f)
    return {"downloaded_papers": [], "search_history": []}

def save_cache(cache: Dict):
    """Save search cache"""
    with open(CACHE_FILE, 'w') as f:
        json.dump(cache, f, indent=2)

def is_recent_paper(published: datetime, cutoff_year: int = 2024) -> bool:
    """Check if paper is from 2024 or later"""
    return published.year >= cutoff_year

def is_substantial_paper(result: arxiv.Result) -> bool:
    """Check if paper is substantial (>7 pages estimated by abstract/content)"""
    # ArXiv doesn't provide page count directly, so we use heuristics:
    # - Check if it's a full paper (not abstract-only)
    # - Most papers >7 pages have substantial abstracts and author lists
    abstract_words = len(result.summary.split())
    author_count = len(result.authors)

    # Heuristic: papers with >150 word abstracts and multiple authors are likely substantial
    return abstract_words > 150 or author_count >= 3

def calculate_relevance_score(result: arxiv.Result, category: str) -> float:
    """
    Calculate relevance score based on keywords and research objectives
    Higher scores indicate better alignment with research goals
    """
    score = 0.0
    text = (result.title + " " + result.summary).lower()

    # Core relevance keywords (high weight)
    core_keywords = {
        "behavioral anomaly": 3.0,
        "behaviour anomaly": 3.0,
        "behavioral detection": 2.5,
        "ai agent": 2.5,
        "autonomous agent": 2.5,
        "baseline poisoning": 3.5,
        "baseline attack": 3.0,
        "model drift": 2.5,
        "concept drift": 2.0,
        "context-aware authentication": 3.0,
        "behavioral baseline": 2.5,
        "behavioral profile": 2.0,
        "non-human behavior": 2.5,
        "behavioral biometric": 2.0
    }

    # Supporting keywords (medium weight)
    supporting_keywords = {
        "authentication": 1.5,
        "anomaly detection": 1.5,
        "machine learning": 1.0,
        "deep learning": 1.0,
        "adversarial": 1.5,
        "poisoning attack": 2.0,
        "real-time": 1.5,
        "runtime": 1.5,
        "behavioral monitoring": 2.0,
        "baseline construction": 2.0,
        "false positive": 1.5,
        "false negative": 1.5
    }

    # Validation keywords (bonus for empirical work)
    empirical_keywords = {
        "evaluation": 1.0,
        "experiment": 1.0,
        "deployment": 1.5,
        "production": 1.5,
        "accuracy": 1.0,
        "performance": 1.0,
        "empirical": 1.5,
        "case study": 1.5,
        "real-world": 2.0
    }

    # Calculate scores
    for keyword, weight in core_keywords.items():
        if keyword in text:
            score += weight

    for keyword, weight in supporting_keywords.items():
        if keyword in text:
            score += weight

    for keyword, weight in empirical_keywords.items():
        if keyword in text:
            score += weight

    # Category-specific bonuses
    category_bonuses = {
        "baseline_poisoning": ["poison", "attack", "adversarial"],
        "model_drift_behavioral": ["drift", "degradation", "decay"],
        "context_aware_auth": ["context", "contextual", "adaptive"],
        "baseline_construction": ["baseline", "profile", "characterization"],
        "realtime_behavioral": ["real-time", "runtime", "continuous"]
    }

    if category in category_bonuses:
        for bonus_term in category_bonuses[category]:
            if bonus_term in text:
                score += 1.0

    return score

def search_and_download(query_config: Dict, cache: Dict, start_year: int = 2024) -> List[Dict]:
    """
    Execute search query and download relevant papers
    """
    query = query_config["query"]
    category = query_config["category"]
    max_results = query_config["max_results"]

    print(f"\n{'='*80}")
    print(f"Searching: {category}")
    print(f"Query: {query}")
    print(f"Max results: {max_results}")
    print(f"{'='*80}\n")

    search = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.SubmittedDate,
        sort_order=arxiv.SortOrder.Descending
    )

    papers_metadata = []
    downloaded_count = 0
    skipped_count = 0

    for result in search.results():
        # Check if already downloaded
        paper_id = result.entry_id.split('/')[-1]
        if paper_id in cache["downloaded_papers"]:
            skipped_count += 1
            continue

        # Filter by year
        if not is_recent_paper(result.published, cutoff_year=start_year):
            skipped_count += 1
            continue

        # Check if substantial
        if not is_substantial_paper(result):
            print(f"  ⊘ Skipping (likely short paper): {result.title[:60]}...")
            skipped_count += 1
            continue

        # Calculate relevance
        relevance = calculate_relevance_score(result, category)

        # Download if relevance score is high enough (threshold: 3.0)
        if relevance >= 3.0:
            try:
                # Create filename
                safe_title = "".join(c if c.isalnum() or c in (' ', '-', '_') else '_' for c in result.title)
                safe_title = safe_title[:100]  # Limit length
                filename = f"{paper_id.replace('/', '_')}_{safe_title}.pdf"
                filepath = TARGET_DIR / filename

                print(f"  ↓ Downloading [Relevance: {relevance:.1f}]: {result.title}")
                print(f"    Authors: {', '.join([a.name for a in result.authors[:3]])}{'...' if len(result.authors) > 3 else ''}")
                print(f"    Published: {result.published.strftime('%Y-%m-%d')}")
                print(f"    Categories: {', '.join(result.categories[:3])}")

                # Download paper
                result.download_pdf(dirpath=str(TARGET_DIR), filename=filename)

                # Store metadata
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

                # Update cache
                cache["downloaded_papers"].append(paper_id)

                downloaded_count += 1
                print(f"    ✓ Downloaded successfully ({downloaded_count} total)\n")

                # Delay between downloads
                time.sleep(DOWNLOAD_DELAY)

            except Exception as e:
                print(f"    ✗ Error downloading: {str(e)}\n")
                continue
        else:
            print(f"  ⊘ Low relevance [{relevance:.1f}]: {result.title[:60]}...")
            skipped_count += 1

    print(f"\n{category} Summary: Downloaded {downloaded_count}, Skipped {skipped_count}")

    # Save cache after each query
    save_cache(cache)

    return papers_metadata

def main():
    """Main execution function"""
    print("="*80)
    print("ArXiv Research: AI Agent Behavioral Anomaly Detection")
    print("Issue #16: Behavioral Authentication & Baseline Construction")
    print("="*80)
    print(f"\nTarget Directory: {TARGET_DIR}")
    print(f"Target: 35-45 high-quality papers (>7 pages, 2024-2025)")
    print(f"Download Delay: {DOWNLOAD_DELAY} seconds")
    print(f"\nResearch Objectives:")
    print("  1. ML-based baseline construction for non-human agent behavior")
    print("  2. Behavioral baseline poisoning attacks & defenses")
    print("  3. Model drift rates validation (2-5% monthly claim)")
    print("  4. Context-aware authentication frameworks")
    print("="*80)

    # Load cache
    cache = load_cache()
    print(f"\nCache loaded: {len(cache['downloaded_papers'])} papers already downloaded")

    # Execute all search queries
    all_metadata = []
    total_downloaded = 0

    start_time = time.time()

    for query_config in SEARCH_QUERIES:
        papers = search_and_download(query_config, cache, start_year=2024)
        all_metadata.extend(papers)
        total_downloaded += len(papers)

        # Check if we've reached target
        if total_downloaded >= 45:
            print(f"\n✓ Target reached: {total_downloaded} papers downloaded")
            break

        # Brief pause between query categories
        time.sleep(2)

    # Save comprehensive metadata
    with open(METADATA_FILE, 'w') as f:
        json.dump({
            "search_date": datetime.now().isoformat(),
            "total_papers": len(all_metadata),
            "papers": all_metadata,
            "search_queries": SEARCH_QUERIES
        }, f, indent=2)

    elapsed_time = time.time() - start_time

    # Final summary
    print("\n" + "="*80)
    print("DOWNLOAD COMPLETE")
    print("="*80)
    print(f"Total papers downloaded: {total_downloaded}")
    print(f"Metadata saved to: {METADATA_FILE}")
    print(f"Time elapsed: {elapsed_time/60:.1f} minutes")
    print(f"\nBreakdown by category:")

    category_counts = {}
    for paper in all_metadata:
        cat = paper["search_category"]
        category_counts[cat] = category_counts.get(cat, 0) + 1

    for cat, count in sorted(category_counts.items(), key=lambda x: x[1], reverse=True):
        print(f"  {cat}: {count} papers")

    print("\n" + "="*80)
    print("Next Steps:")
    print("  1. Review papers_metadata.json for paper details")
    print("  2. Analyze papers for baseline construction methods")
    print("  3. Validate baseline poisoning attack claims")
    print("  4. Extract model drift rate evidence")
    print("  5. Identify production deployment case studies")
    print("="*80)

if __name__ == "__main__":
    main()
