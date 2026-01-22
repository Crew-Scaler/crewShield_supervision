#!/usr/bin/env python3
"""
Supplemental research for specific governance topics
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
DELAY = 3

# Specific governance-focused searches
SEARCHES = [
    ("model drift detection", 3),
    ("model versioning", 3),
    ("AI risk management", 3),
]

def main():
    """Supplement with governance-specific papers"""
    print("\n" + "="*80)
    print("Supplemental Governance Research")
    print("="*80 + "\n")

    # Load existing metadata
    try:
        with open(TARGET_DIR / "research_results.json") as f:
            data = json.load(f)
            papers = data.get("papers", [])
            existing_ids = {p["id"] for p in papers}
    except:
        papers = []
        existing_ids = set()

    client = arxiv.Client()
    new_papers = 0

    for query, count in SEARCHES:
        print(f"\nSearching: {query} (need {count})")

        search = arxiv.Search(
            query=query,
            max_results=count * 3,
            sort_by=arxiv.SortCriterion.SubmittedDate,
            sort_order=arxiv.SortOrder.Descending
        )

        found = 0
        for r in client.results(search):
            if r.get_short_id() in existing_ids:
                continue

            if r.published.year < 2024:
                continue

            filename = f"{query.replace(' ', '_')}_{r.get_short_id()}.pdf"

            try:
                print(f"  ✓ {r.title[:65]}...")

                r.download_pdf(dirpath=str(TARGET_DIR), filename=filename)

                papers.append({
                    "id": r.get_short_id(),
                    "title": r.title,
                    "authors": [a.name for a in r.authors][:5],
                    "date": r.published.strftime("%Y-%m-%d"),
                    "categories": r.categories,
                    "summary": r.summary,
                    "url": r.pdf_url,
                    "file": filename
                })

                existing_ids.add(r.get_short_id())
                found += 1
                new_papers += 1
                print(f"    New total: {len(papers)}\n")

                time.sleep(DELAY)

                if found >= count:
                    break

            except Exception as e:
                print(f"    Failed: {e}\n")

    # Update metadata
    data = {
        "date": datetime.now().isoformat(),
        "total": len(papers),
        "papers": papers
    }

    with open(TARGET_DIR / "research_results.json", "w") as f:
        json.dump(data, f, indent=2)

    print("="*80)
    print(f"Added {new_papers} papers. Total: {len(papers)}")
    print("="*80 + "\n")

if __name__ == "__main__":
    main()
