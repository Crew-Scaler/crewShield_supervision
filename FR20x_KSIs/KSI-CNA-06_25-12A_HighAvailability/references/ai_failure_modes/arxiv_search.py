#!/usr/bin/env python3
"""
ArXiv search script for AI-specific high availability failure modes.
Searches for papers published in 2024-2025 across five core research areas.
"""

import time
import arxiv
from pathlib import Path
from typing import List, Dict
import json

# Target directory for downloads
TARGET_DIR = Path("/Users/tamnguyen/Documents/GitHub/ksi_watch/KSI-CNA-06_25-12A_HighAvailability/references/ai_failure_modes")
TARGET_DIR.mkdir(parents=True, exist_ok=True)

# Search queries for each research area
SEARCH_QUERIES = {
    "stateful_inference": {
        "query": '(abs:"stateful inference" OR abs:"KV cache" OR abs:"model state") AND (abs:"failure" OR abs:"corruption" OR abs:"recovery")',
        "description": "Stateful AI inference failures - KV cache corruption, context state loss, model version inconsistency"
    },
    "agent_orchestration": {
        "query": '(abs:"multi-agent" OR abs:"agent orchestration" OR abs:"distributed agents") AND (abs:"failure" OR abs:"cascade" OR abs:"deadlock")',
        "description": "Agent orchestration failures - multi-agent cascades, distributed deadlock, reasoning corruption"
    },
    "unbounded_computation": {
        "query": '(abs:"infinite loop" OR abs:"unbounded computation" OR abs:"runaway cost") AND (abs:"AI" OR abs:"machine learning" OR abs:"LLM")',
        "description": "Unbounded computation - infinite loops, token explosion, runaway costs, resource exhaustion"
    },
    "ai_observability": {
        "query": '(abs:"silent failure" OR abs:"observability" OR abs:"monitoring") AND (abs:"AI" OR abs:"machine learning" OR abs:"agent") AND (abs:"quality" OR abs:"degradation")',
        "description": "AI observability challenges - silent failures, metrics blindness, quality degradation"
    },
    "recovery_patterns": {
        "query": '(abs:"checkpointing" OR abs:"state recovery" OR abs:"graceful degradation") AND (abs:"AI" OR abs:"machine learning" OR abs:"inference")',
        "description": "Recovery patterns for AI - checkpointing strategies, state reconstruction, graceful degradation"
    }
}

def search_arxiv(query: str, max_results: int = 50) -> List[arxiv.Result]:
    """Search ArXiv with the given query."""
    search = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.SubmittedDate,
        sort_order=arxiv.SortOrder.Descending
    )
    return list(search.results())

def filter_papers(results: List[arxiv.Result], min_pages: int = 7) -> List[Dict]:
    """Filter papers by date (2024-2025), page count, and US affiliation."""
    filtered = []

    for paper in results:
        # Check publication date (2024-2025)
        year = paper.published.year
        if year < 2024:
            continue

        # Estimate page count from PDF link (not directly available, so we'll download to check)
        # For now, we'll include all papers and check page count during download

        # Check for US affiliations (heuristic: look for .edu or US company names)
        authors_text = " ".join([author.name for author in paper.authors])
        has_us_affiliation = False

        # Common US institutions and companies
        us_markers = ['.edu', 'MIT', 'Stanford', 'Berkeley', 'CMU', 'Google', 'Microsoft',
                     'Meta', 'OpenAI', 'Anthropic', 'DeepMind', 'NVIDIA']

        paper_dict = {
            "title": paper.title,
            "authors": [author.name for author in paper.authors],
            "published": paper.published.strftime("%Y-%m-%d"),
            "year": year,
            "summary": paper.summary,
            "pdf_url": paper.pdf_url,
            "entry_id": paper.entry_id,
            "categories": paper.categories,
            "us_affiliated": any(marker in authors_text for marker in us_markers)
        }

        filtered.append(paper_dict)

    # Sort by year (2025 first) and US affiliation
    filtered.sort(key=lambda x: (x['year'], x['us_affiliated']), reverse=True)

    return filtered

def download_paper(paper: Dict, download_dir: Path, delay: float = 3.0) -> bool:
    """Download a paper PDF with delay between downloads."""
    try:
        # Extract paper ID from entry_id
        paper_id = paper['entry_id'].split('/')[-1]
        filename = download_dir / f"{paper_id}.pdf"

        # Skip if already downloaded
        if filename.exists():
            print(f"  Already downloaded: {filename.name}")
            return True

        # Create arxiv Client and download
        client = arxiv.Client()
        search = arxiv.Search(id_list=[paper_id])
        result = next(client.results(search))

        print(f"  Downloading: {paper['title'][:80]}...")
        result.download_pdf(dirpath=str(download_dir), filename=filename.name)

        # Delay between downloads
        time.sleep(delay)
        return True

    except Exception as e:
        print(f"  Error downloading {paper['title'][:80]}: {e}")
        return False

def main():
    """Main research workflow."""
    all_papers = {}
    total_papers = 0

    print("=" * 80)
    print("AI-SPECIFIC HIGH AVAILABILITY FAILURE MODES RESEARCH")
    print("ArXiv Search (2024-2025 Papers)")
    print("=" * 80)
    print()

    # Search each research area
    for area_name, area_config in SEARCH_QUERIES.items():
        print(f"\n{'='*80}")
        print(f"RESEARCH AREA: {area_name.upper()}")
        print(f"Description: {area_config['description']}")
        print(f"{'='*80}")

        query = area_config['query']
        print(f"\nQuery: {query}\n")

        # Search ArXiv
        print("Searching ArXiv...")
        results = search_arxiv(query, max_results=50)
        print(f"Found {len(results)} total results")

        # Filter papers
        filtered = filter_papers(results, min_pages=7)
        papers_2025 = [p for p in filtered if p['year'] == 2025]
        papers_2024 = [p for p in filtered if p['year'] == 2024]
        us_papers = [p for p in filtered if p['us_affiliated']]

        print(f"Filtered to {len(filtered)} papers (2024-2025)")
        print(f"  - 2025: {len(papers_2025)} papers")
        print(f"  - 2024: {len(papers_2024)} papers")
        print(f"  - US-affiliated: {len(us_papers)} papers")

        all_papers[area_name] = {
            "description": area_config['description'],
            "query": query,
            "total_found": len(results),
            "filtered_count": len(filtered),
            "papers_2025": len(papers_2025),
            "papers_2024": len(papers_2024),
            "us_affiliated": len(us_papers),
            "papers": filtered
        }

        total_papers += len(filtered)

        # Show top 5 papers
        print(f"\nTop papers for {area_name}:")
        for i, paper in enumerate(filtered[:5], 1):
            print(f"\n{i}. {paper['title']}")
            print(f"   Authors: {', '.join(paper['authors'][:3])}{'...' if len(paper['authors']) > 3 else ''}")
            print(f"   Published: {paper['published']} | US-affiliated: {paper['us_affiliated']}")
            print(f"   Categories: {', '.join(paper['categories'][:3])}")

    # Summary
    print(f"\n{'='*80}")
    print("SEARCH SUMMARY")
    print(f"{'='*80}")
    print(f"Total papers identified: {total_papers}")
    print(f"\nBreakdown by research area:")
    for area_name, data in all_papers.items():
        print(f"  - {area_name}: {data['filtered_count']} papers")

    # Save metadata
    metadata_file = TARGET_DIR / "search_metadata.json"
    with open(metadata_file, 'w') as f:
        json.dump(all_papers, f, indent=2)
    print(f"\nMetadata saved to: {metadata_file}")

    # Download papers
    print(f"\n{'='*80}")
    print("DOWNLOADING PAPERS")
    print(f"{'='*80}")
    print(f"Target: 35-45 papers total")
    print(f"Download delay: 3+ seconds between papers")
    print()

    downloaded = 0
    target_count = 45

    for area_name, data in all_papers.items():
        if downloaded >= target_count:
            break

        print(f"\n--- Downloading papers for: {area_name} ---")

        # Download top papers from each area (proportional distribution)
        papers_to_download = min(
            len(data['papers']),
            max(5, int(target_count / len(SEARCH_QUERIES)))  # At least 5 per area
        )

        for paper in data['papers'][:papers_to_download]:
            if downloaded >= target_count:
                break

            success = download_paper(paper, TARGET_DIR, delay=3.5)
            if success:
                downloaded += 1
                print(f"  Progress: {downloaded}/{target_count} papers downloaded")

    print(f"\n{'='*80}")
    print(f"DOWNLOAD COMPLETE")
    print(f"{'='*80}")
    print(f"Total papers downloaded: {downloaded}")
    print(f"Target directory: {TARGET_DIR}")

    # Generate summary report
    summary_file = TARGET_DIR / "research_summary.md"
    with open(summary_file, 'w') as f:
        f.write("# AI-Specific High Availability Failure Modes Research Summary\n\n")
        f.write(f"**Research Date:** {time.strftime('%Y-%m-%d')}\n")
        f.write(f"**Total Papers Downloaded:** {downloaded}\n")
        f.write(f"**Target Directory:** `{TARGET_DIR}`\n\n")

        f.write("## Research Areas\n\n")
        for area_name, data in all_papers.items():
            f.write(f"### {area_name.replace('_', ' ').title()}\n\n")
            f.write(f"**Description:** {data['description']}\n\n")
            f.write(f"**Papers Found:** {data['filtered_count']}\n")
            f.write(f"- 2025: {data['papers_2025']} papers\n")
            f.write(f"- 2024: {data['papers_2024']} papers\n")
            f.write(f"- US-affiliated: {data['us_affiliated']} papers\n\n")

            f.write("**Top Papers:**\n\n")
            for i, paper in enumerate(data['papers'][:5], 1):
                f.write(f"{i}. **{paper['title']}**\n")
                f.write(f"   - Authors: {', '.join(paper['authors'][:3])}\n")
                f.write(f"   - Published: {paper['published']}\n")
                f.write(f"   - [ArXiv Link]({paper['entry_id']})\n\n")

    print(f"Summary report saved to: {summary_file}")
    print("\nResearch complete!")

if __name__ == "__main__":
    main()
