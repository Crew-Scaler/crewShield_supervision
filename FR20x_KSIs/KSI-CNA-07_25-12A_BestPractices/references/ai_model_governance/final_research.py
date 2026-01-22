#!/usr/bin/env python3
"""
ArXiv Research: AI Model Governance & Compliance
Final version with optimized search and filtering
"""

import arxiv
import time
from pathlib import Path
from datetime import datetime
import json

TARGET_DIR = Path(
    "/Users/tamnguyen/Documents/GitHub/ksi_watch/"
    "KSI-CNA-07_25-12A_BestPractices/references/ai_model_governance"
)
TARGET = 40
DELAY = 3

# Optimized search queries
SEARCHES = [
    ("AI governance", 10),
    ("MLOps", 8),
    ("model monitoring", 6),
    ("AI compliance", 6),
    ("responsible AI", 5),
    ("model lifecycle", 5),
]

def get_pages(summary):
    """Estimate page count"""
    l = len(summary)
    return 12 if l > 2000 else (8 if l > 1200 else 5)

def main():
    """Run research"""
    print("\n" + "="*80)
    print("AI Model Governance Research")
    print("="*80 + "\n")

    papers = []
    client = arxiv.Client()

    for query, count in SEARCHES:
        if len(papers) >= TARGET:
            break

        print(f"\nSearching: {query} (need {count})")

        search = arxiv.Search(
            query=query,
            max_results=count * 2,
            sort_by=arxiv.SortCriterion.SubmittedDate,
            sort_order=arxiv.SortOrder.Descending
        )

        found = 0
        for r in client.results(search):
            if r.published.year < 2024:
                continue

            pages = get_pages(r.summary)
            if pages < 7:
                continue

            filename = f"{query.replace(' ', '_')}_{r.get_short_id()}.pdf"

            try:
                print(f"  ✓ {r.title[:65]}...")
                print(f"    {r.published.strftime('%Y-%m-%d')}, ~{pages}p")

                r.download_pdf(dirpath=str(TARGET_DIR), filename=filename)

                papers.append({
                    "id": r.get_short_id(),
                    "title": r.title,
                    "authors": [a.name for a in r.authors][:5],
                    "date": r.published.strftime("%Y-%m-%d"),
                    "categories": r.categories,
                    "summary": r.summary,
                    "url": r.pdf_url,
                    "pages": pages,
                    "file": filename
                })

                found += 1
                print(f"    Total: {len(papers)}/{TARGET}\n")

                time.sleep(DELAY)

                if found >= count or len(papers) >= TARGET:
                    break

            except Exception as e:
                print(f"    Failed: {e}\n")

        print(f"Category: {found} papers\n")

    # Save metadata
    meta = {
        "date": datetime.now().isoformat(),
        "total": len(papers),
        "papers": papers
    }

    with open(TARGET_DIR / "research_results.json", "w") as f:
        json.dump(meta, f, indent=2)

    print("="*80)
    print(f"COMPLETE: {len(papers)} papers downloaded")
    print("="*80 + "\n")

if __name__ == "__main__":
    main()
