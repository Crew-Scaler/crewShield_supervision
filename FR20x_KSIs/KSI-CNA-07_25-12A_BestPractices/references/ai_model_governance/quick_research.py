#!/usr/bin/env python3
"""
Quick ArXiv Research: AI Model Governance
Focused search for 35-45 high-quality papers
"""

import arxiv
import time
from pathlib import Path
from datetime import datetime, timezone
import json

TARGET_DIR = Path("/Users/tamnguyen/Documents/GitHub/ksi_watch/KSI-CNA-07_25-12A_BestPractices/references/ai_model_governance")
MIN_PAGES = 7
TARGET_PAPERS = 40
DELAY = 3

# Focused queries for high-quality governance papers
QUERIES = [
    ("AI governance framework production deployment", "ai_governance", 8),
    ("model lifecycle management MLOps compliance", "model_lifecycle", 8),
    ("model drift monitoring governance", "model_drift", 6),
    ("AI compliance automation regulatory", "compliance_automation", 6),
    ("model registry versioning lineage", "model_registry", 6),
    ("responsible AI trustworthy framework", "responsible_ai", 6),
]

def estimate_pages(summary):
    """Estimate pages from summary length"""
    length = len(summary)
    if length < 800: return 5
    elif length < 1500: return 8
    elif length < 2500: return 12
    else: return 15

def is_relevant(title, summary):
    """Check relevance for governance research"""
    text = (title + " " + summary).lower()

    # High-value keywords
    keywords = [
        "governance", "compliance", "model lifecycle", "mlops",
        "model drift", "model monitoring", "model registry",
        "regulatory", "risk management", "responsible ai",
        "trustworthy ai", "model versioning", "lineage"
    ]

    count = sum(1 for k in keywords if k in text)
    return count >= 2

def download_papers():
    """Execute research and download papers"""
    print(f"\n{'='*80}")
    print("AI Model Governance Research - Quick Focused Search")
    print(f"{'='*80}\n")

    papers = []
    total = 0
    client = arxiv.Client()

    for query, category, max_results in QUERIES:
        if total >= TARGET_PAPERS:
            break

        print(f"\nSearching: {category} (target: {max_results})")
        print(f"Query: {query}\n")

        search = arxiv.Search(
            query=query,
            max_results=max_results * 3,
            sort_by=arxiv.SortCriterion.SubmittedDate,
            sort_order=arxiv.SortOrder.Descending
        )

        found = 0
        try:
            for result in client.results(search):
                # Filter by date (2024+)
                if result.published.year < 2024:
                    continue

                # Check relevance
                if not is_relevant(result.title, result.summary):
                    continue

                # Check page estimate
                pages = estimate_pages(result.summary)
                if pages < MIN_PAGES:
                    continue

                # Download
                filename = f"{category}_{result.get_short_id()}.pdf"
                filepath = TARGET_DIR / filename

                try:
                    print(f"  ✓ {result.title[:70]}...")
                    print(f"    Published: {result.published.strftime('%Y-%m-%d')}, Pages: ~{pages}")

                    result.download_pdf(dirpath=str(TARGET_DIR), filename=filename)

                    papers.append({
                        "arxiv_id": result.get_short_id(),
                        "title": result.title,
                        "authors": [a.name for a in result.authors],
                        "published": result.published.strftime("%Y-%m-%d"),
                        "categories": result.categories,
                        "summary": result.summary,
                        "pdf_url": result.pdf_url,
                        "estimated_pages": pages,
                        "category": category,
                        "file": filename
                    })

                    found += 1
                    total += 1
                    print(f"    Downloaded! Total: {total}/{TARGET_PAPERS}\n")

                    time.sleep(DELAY)

                    if found >= max_results or total >= TARGET_PAPERS:
                        break

                except Exception as e:
                    print(f"    ✗ Download failed: {e}\n")

        except Exception as e:
            print(f"  ✗ Search error: {e}\n")

        print(f"  Category complete: {found} papers")

    # Save metadata
    metadata = {
        "research_date": datetime.now().isoformat(),
        "total_papers": len(papers),
        "papers": papers
    }

    with open(TARGET_DIR / "metadata.json", "w") as f:
        json.dump(metadata, f, indent=2)

    print(f"\n{'='*80}")
    print(f"COMPLETE: Downloaded {len(papers)} papers")
    print(f"Metadata: metadata.json")
    print(f"{'='*80}\n")

    return papers

if __name__ == "__main__":
    download_papers()
