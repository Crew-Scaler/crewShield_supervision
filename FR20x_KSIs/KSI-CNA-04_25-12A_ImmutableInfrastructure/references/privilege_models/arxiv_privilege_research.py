#!/usr/bin/env python3
"""
ArXiv Research Script for AI Privilege Models and Least-Privilege Enforcement
Issue #10 - Design: Immutable Infrastructure
"""

import arxiv
import time
from pathlib import Path
from typing import List, Dict
import json
from datetime import datetime

# Target directory
DOWNLOAD_DIR = Path("/Users/tamnguyen/Documents/GitHub/ksi_watch/KSI-CNA-04_25-12A_ImmutableInfrastructure/references/privilege_models")
DOWNLOAD_DIR.mkdir(parents=True, exist_ok=True)

# Minimum page threshold
MIN_PAGES = 7

# Search queries with 2024-2025 focus
SEARCH_QUERIES = [
    {
        "name": "workload_identity_access_control",
        "query": 'abs:("workload identity" OR "machine identity" OR "agent identity") AND ("access control" OR RBAC OR authorization)',
        "max_results": 50
    },
    {
        "name": "least_privilege_ai",
        "query": 'abs:("least privilege" OR "privilege escalation" OR "just-in-time access") AND (AI OR agent* OR autonomous)',
        "max_results": 50
    },
    {
        "name": "policy_as_code_ai",
        "query": 'abs:("policy as code" OR "admission control") AND (AI OR "machine learning" OR agent*) AND (security OR authorization)',
        "max_results": 50
    },
    {
        "name": "non_human_identity",
        "query": 'abs:("non-human identity" OR "service account") AND (security OR authentication) AND (cloud OR kubernetes)',
        "max_results": 50
    },
    {
        "name": "rbac_ai_agents",
        "query": 'abs:(RBAC OR "attribute based access control" OR ABAC) AND (AI OR autonomous OR agent*)',
        "max_results": 50
    }
]

def estimate_pages(paper) -> int:
    """Estimate number of pages from paper metadata"""
    # Try to get from comment field
    if hasattr(paper, 'comment') and paper.comment:
        comment = paper.comment.lower()
        if 'pages' in comment or 'page' in comment:
            # Extract number before 'page' or 'pages'
            import re
            match = re.search(r'(\d+)\s*pages?', comment)
            if match:
                return int(match.group(1))
    # Default estimate - usually papers are 10+ pages
    return 10

def is_recent_paper(paper, start_year=2024) -> bool:
    """Check if paper is from 2024 or later"""
    if hasattr(paper, 'published'):
        return paper.published.year >= start_year
    return False

def download_paper(paper, query_name: str, downloaded_ids: set) -> Dict:
    """Download a single paper with metadata"""
    paper_id = paper.entry_id.split('/')[-1]

    # Skip if already downloaded
    if paper_id in downloaded_ids:
        print(f"  ⏭️  Skipping duplicate: {paper_id}")
        return None

    # Estimate pages
    estimated_pages = estimate_pages(paper)

    # Check page requirement
    if estimated_pages < MIN_PAGES:
        print(f"  ⏭️  Skipping (too short): {paper.title[:60]}... ({estimated_pages} pages)")
        return None

    # Check if recent
    year = paper.published.year if hasattr(paper, 'published') else 0
    is_2025 = year == 2025
    is_2024 = year == 2024

    if not (is_2025 or is_2024):
        print(f"  ⏭️  Skipping (not 2024-2025): {paper.title[:60]}... ({year})")
        return None

    # Download
    filename = f"{query_name}_{paper_id}.pdf"
    filepath = DOWNLOAD_DIR / filename

    try:
        print(f"  ⬇️  Downloading: {paper.title[:60]}... ({year}, ~{estimated_pages}p)")
        paper.download_pdf(filename=str(filepath))
        downloaded_ids.add(paper_id)

        # Respectful delay
        time.sleep(3)

        return {
            "id": paper_id,
            "title": paper.title,
            "authors": [author.name for author in paper.authors],
            "published": paper.published.isoformat() if hasattr(paper, 'published') else None,
            "year": year,
            "categories": paper.categories if hasattr(paper, 'categories') else [],
            "abstract": paper.summary,
            "estimated_pages": estimated_pages,
            "filename": filename,
            "query": query_name,
            "url": paper.entry_id
        }
    except Exception as e:
        print(f"  ❌ Error downloading {paper_id}: {e}")
        return None

def execute_search(query_config: Dict, downloaded_ids: set, total_downloaded: int, target: int = 45) -> List[Dict]:
    """Execute a single ArXiv search query"""
    print(f"\n{'='*80}")
    print(f"Query: {query_config['name']}")
    print(f"{'='*80}")
    print(f"Search: {query_config['query']}")
    print(f"Max Results: {query_config['max_results']}")

    papers_metadata = []

    # Create search
    search = arxiv.Search(
        query=query_config['query'],
        max_results=query_config['max_results'],
        sort_by=arxiv.SortCriterion.SubmittedDate,
        sort_order=arxiv.SortOrder.Descending
    )

    # Execute search
    results = list(search.results())
    print(f"\nFound {len(results)} papers total")

    # Sort: 2025 first, then 2024
    results_2025 = [r for r in results if hasattr(r, 'published') and r.published.year == 2025]
    results_2024 = [r for r in results if hasattr(r, 'published') and r.published.year == 2024]
    results_older = [r for r in results if hasattr(r, 'published') and r.published.year < 2024]

    print(f"  2025 papers: {len(results_2025)}")
    print(f"  2024 papers: {len(results_2024)}")
    print(f"  Older papers: {len(results_older)}")

    sorted_results = results_2025 + results_2024 + results_older

    # Download papers
    for paper in sorted_results:
        if total_downloaded >= target:
            print(f"\n✅ Reached target of {target} papers. Stopping.")
            break

        metadata = download_paper(paper, query_config['name'], downloaded_ids)
        if metadata:
            papers_metadata.append(metadata)
            total_downloaded += 1
            print(f"  📊 Progress: {total_downloaded}/{target} papers")

    return papers_metadata, total_downloaded

def main():
    """Main execution function"""
    print(f"ArXiv Research: AI Privilege Models & Least-Privilege Enforcement")
    print(f"Target Directory: {DOWNLOAD_DIR}")
    print(f"Target: 35-45 papers")
    print(f"Minimum Pages: {MIN_PAGES}")
    print(f"Focus: 2024-2025 papers\n")

    all_metadata = []
    downloaded_ids = set()
    total_downloaded = 0
    target_papers = 45

    # Execute each search query
    for query_config in SEARCH_QUERIES:
        if total_downloaded >= target_papers:
            print(f"\n✅ Reached target of {target_papers} papers. Stopping all queries.")
            break

        papers_metadata, total_downloaded = execute_search(
            query_config,
            downloaded_ids,
            total_downloaded,
            target_papers
        )
        all_metadata.extend(papers_metadata)

    # Save metadata
    metadata_file = DOWNLOAD_DIR / "papers_metadata.json"
    with open(metadata_file, 'w') as f:
        json.dump({
            "search_date": datetime.now().isoformat(),
            "total_papers": len(all_metadata),
            "papers": all_metadata,
            "queries": SEARCH_QUERIES
        }, f, indent=2)

    # Generate summary
    print(f"\n{'='*80}")
    print(f"RESEARCH SUMMARY")
    print(f"{'='*80}")
    print(f"Total Papers Downloaded: {len(all_metadata)}")
    print(f"Unique Papers: {len(downloaded_ids)}")

    # By year
    papers_2025 = [p for p in all_metadata if p.get('year') == 2025]
    papers_2024 = [p for p in all_metadata if p.get('year') == 2024]
    print(f"\nBy Year:")
    print(f"  2025: {len(papers_2025)}")
    print(f"  2024: {len(papers_2024)}")

    # By query
    print(f"\nBy Query:")
    for query_config in SEARCH_QUERIES:
        query_papers = [p for p in all_metadata if p.get('query') == query_config['name']]
        print(f"  {query_config['name']}: {len(query_papers)}")

    # Top categories
    from collections import Counter
    all_categories = []
    for paper in all_metadata:
        all_categories.extend(paper.get('categories', []))
    top_categories = Counter(all_categories).most_common(10)
    print(f"\nTop Categories:")
    for cat, count in top_categories:
        print(f"  {cat}: {count}")

    print(f"\nMetadata saved to: {metadata_file}")
    print(f"Papers saved to: {DOWNLOAD_DIR}")

    # Generate detailed summary report
    summary_file = DOWNLOAD_DIR / "research_summary.md"
    with open(summary_file, 'w') as f:
        f.write("# AI Privilege Models & Least-Privilege Enforcement Research\n\n")
        f.write(f"**Issue #10**: Design - Immutable Infrastructure\n\n")
        f.write(f"**Research Date**: {datetime.now().strftime('%Y-%m-%d')}\n\n")
        f.write(f"## Summary Statistics\n\n")
        f.write(f"- **Total Papers**: {len(all_metadata)}\n")
        f.write(f"- **2025 Papers**: {len(papers_2025)}\n")
        f.write(f"- **2024 Papers**: {len(papers_2024)}\n")
        f.write(f"- **Minimum Pages**: {MIN_PAGES}\n\n")

        f.write("## Search Queries Executed\n\n")
        for i, query_config in enumerate(SEARCH_QUERIES, 1):
            f.write(f"{i}. **{query_config['name']}**\n")
            f.write(f"   - Query: `{query_config['query']}`\n")
            query_papers = [p for p in all_metadata if p.get('query') == query_config['name']]
            f.write(f"   - Papers Found: {len(query_papers)}\n\n")

        f.write("## Papers by Year\n\n")
        f.write("### 2025 Papers\n\n")
        for paper in papers_2025:
            f.write(f"- **{paper['title']}**\n")
            f.write(f"  - Authors: {', '.join(paper['authors'][:3])}\n")
            f.write(f"  - Published: {paper['published']}\n")
            f.write(f"  - Categories: {', '.join(paper['categories'][:3])}\n")
            f.write(f"  - URL: {paper['url']}\n\n")

        f.write("### 2024 Papers\n\n")
        for paper in papers_2024:
            f.write(f"- **{paper['title']}**\n")
            f.write(f"  - Authors: {', '.join(paper['authors'][:3])}\n")
            f.write(f"  - Published: {paper['published']}\n")
            f.write(f"  - Categories: {', '.join(paper['categories'][:3])}\n")
            f.write(f"  - URL: {paper['url']}\n\n")

        f.write("## Top Research Categories\n\n")
        for cat, count in top_categories:
            f.write(f"- {cat}: {count} papers\n")

        f.write("\n## Key Research Areas Covered\n\n")
        f.write("1. **Agent Identity and Access Control**\n")
        f.write("   - Non-human identities\n")
        f.write("   - Workload identity management\n")
        f.write("   - RBAC for autonomous agents\n\n")

        f.write("2. **Just-in-Time (JIT) Access**\n")
        f.write("   - Dynamic permission assignment\n")
        f.write("   - Time-bound access for AI systems\n\n")

        f.write("3. **Privilege Escalation Prevention**\n")
        f.write("   - Privilege boundary enforcement\n")
        f.write("   - Least-privilege enforcement mechanisms\n\n")

        f.write("4. **Task-Centric Permissions**\n")
        f.write("   - Context-aware authorization\n")
        f.write("   - Fine-grained access control\n\n")

        f.write("5. **Policy-as-Code**\n")
        f.write("   - Admission control policies\n")
        f.write("   - Automated policy enforcement\n\n")

    print(f"Summary report saved to: {summary_file}")

if __name__ == "__main__":
    main()
