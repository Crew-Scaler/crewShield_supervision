#!/usr/bin/env python3
"""
ArXiv Research Script for Issue #16: AI Agent Authentication
Focus: Delegation Chain Management & AI Agent Credential Lifecycle

Research Objectives:
1. Delegation scope expansion attacks specific to AI agents
2. Credential lifecycle automation for agent workloads at scale
3. Short-lived token management effectiveness for AI systems
4. Credential exposure patterns in AI-assisted development
"""

import arxiv
import time
import os
from datetime import datetime
from pathlib import Path
from typing import List, Dict
import json

# Target directory for downloads
TARGET_DIR = Path(__file__).parent
CACHE_FILE = TARGET_DIR / "research_cache.json"
SUMMARY_FILE = TARGET_DIR / "research_summary.md"

# Research parameters
MIN_PAGES = 7
TARGET_PAPERS = 40
DELAY_SECONDS = 3
START_YEAR = 2024


class ArxivResearcher:
    """Conducts targeted ArXiv research for AI agent authentication."""

    def __init__(self):
        self.downloaded_papers = []
        self.cache = self._load_cache()

    def _load_cache(self) -> Dict:
        """Load cache of previously downloaded papers."""
        if CACHE_FILE.exists():
            with open(CACHE_FILE, "r") as f:
                return json.load(f)
        return {"papers": [], "queries": {}}

    def _save_cache(self):
        """Save cache of downloaded papers."""
        with open(CACHE_FILE, "w") as f:
            json.dump(self.cache, f, indent=2)

    def _is_relevant_year(self, published: datetime) -> bool:
        """Check if paper is from 2024 or 2025."""
        return published.year >= START_YEAR

    def _estimate_pages(self, result) -> int:
        """Estimate page count from paper metadata."""
        # ArXiv doesn't provide page count directly
        # Use comment field if available, otherwise assume relevant
        if hasattr(result, "comment") and result.comment:
            import re

            match = re.search(r"(\d+)\s*pages?", result.comment.lower())
            if match:
                return int(match.group(1))
        # If no page info, assume it meets criteria (will verify after download)
        return 10

    def search_and_download(
        self, query: str, max_results: int = 50, query_name: str = ""
    ) -> List[Dict]:
        """
        Search ArXiv and download relevant papers.

        Args:
            query: Search query string
            max_results: Maximum results to retrieve
            query_name: Human-readable name for this query

        Returns:
            List of downloaded paper metadata
        """
        print(f"\n{'=' * 80}")
        print(f"QUERY: {query_name or query}")
        print(f"{'=' * 80}\n")

        # Check cache for this query
        if query in self.cache.get("queries", {}):
            cached_count = len(self.cache["queries"][query])
            print(f"Found {cached_count} cached results for this query")

        client = arxiv.Client()
        search = arxiv.Search(
            query=query,
            max_results=max_results,
            sort_by=arxiv.SortCriterion.SubmittedDate,
            sort_order=arxiv.SortOrder.Descending,
        )

        downloaded_this_query = []
        processed = 0

        for result in client.results(search):
            processed += 1

            # Skip if already downloaded
            if result.entry_id in [p["id"] for p in self.cache.get("papers", [])]:
                print(f"[CACHED] {result.title[:60]}...")
                continue

            # Check year
            if not self._is_relevant_year(result.published):
                print(
                    f"[SKIP-YEAR] {result.title[:60]}... "
                    f"({result.published.year})"
                )
                continue

            # Estimate pages
            pages = self._estimate_pages(result)
            if pages < MIN_PAGES:
                print(f"[SKIP-PAGES] {result.title[:60]}... (~{pages} pages)")
                continue

            # Download paper
            print(f"[DOWNLOADING] {result.title[:60]}...")
            try:
                filename = self._safe_filename(result)
                filepath = TARGET_DIR / filename

                result.download_pdf(dirpath=str(TARGET_DIR), filename=filename)

                paper_meta = {
                    "id": result.entry_id,
                    "title": result.title,
                    "authors": [a.name for a in result.authors],
                    "published": result.published.isoformat(),
                    "updated": result.updated.isoformat(),
                    "categories": result.categories,
                    "abstract": result.summary,
                    "filename": filename,
                    "query": query_name or query,
                    "estimated_pages": pages,
                }

                self.downloaded_papers.append(paper_meta)
                downloaded_this_query.append(paper_meta)

                # Update cache
                if "papers" not in self.cache:
                    self.cache["papers"] = []
                self.cache["papers"].append(paper_meta)

                if "queries" not in self.cache:
                    self.cache["queries"] = {}
                if query not in self.cache["queries"]:
                    self.cache["queries"][query] = []
                self.cache["queries"][query].append(result.entry_id)

                self._save_cache()

                print(
                    f"  -> Saved: {filename} ({result.published.year}, "
                    f"~{pages} pages)"
                )

                # Respect rate limits
                time.sleep(DELAY_SECONDS)

                # Check if we've hit target
                total_downloaded = len(self.cache.get("papers", []))
                if total_downloaded >= TARGET_PAPERS:
                    print(f"\n*** TARGET REACHED: {total_downloaded} papers ***\n")
                    return downloaded_this_query

            except Exception as e:
                print(f"  -> ERROR: {e}")
                continue

        print(f"\nProcessed {processed} results, downloaded {len(downloaded_this_query)} new papers")
        return downloaded_this_query

    def _safe_filename(self, result) -> str:
        """Generate safe filename for paper."""
        # Use ArXiv ID as base
        arxiv_id = result.entry_id.split("/")[-1].replace(".", "_")

        # Add first author
        first_author = result.authors[0].name.split()[-1] if result.authors else "Unknown"

        # Add year
        year = result.published.year

        return f"{arxiv_id}_{first_author}_{year}.pdf"

    def generate_summary(self):
        """Generate research summary markdown."""
        total_papers = len(self.cache.get("papers", []))

        summary = f"""# AI Agent Authentication Research Summary
## Delegation Chain Management & Credential Lifecycle

**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

**Total Papers Downloaded:** {total_papers}

---

## Research Objectives

1. **Delegation scope expansion attacks** specific to AI agents
2. **Credential lifecycle automation** for agent workloads at scale
3. **Short-lived token management** effectiveness for AI systems
4. **Credential exposure patterns** in AI-assisted development

---

## Download Statistics by Query

"""

        for query, paper_ids in self.cache.get("queries", {}).items():
            summary += f"\n### {query}\n"
            summary += f"- Papers found: {len(paper_ids)}\n"

        summary += "\n---\n\n## Downloaded Papers\n\n"

        # Group by year
        papers_by_year = {}
        for paper in self.cache.get("papers", []):
            year = paper["published"][:4]
            if year not in papers_by_year:
                papers_by_year[year] = []
            papers_by_year[year].append(paper)

        for year in sorted(papers_by_year.keys(), reverse=True):
            summary += f"\n### {year} ({len(papers_by_year[year])} papers)\n\n"
            for paper in papers_by_year[year]:
                summary += f"**{paper['title']}**\n"
                summary += f"- Authors: {', '.join(paper['authors'][:3])}"
                if len(paper['authors']) > 3:
                    summary += f" et al. ({len(paper['authors'])} total)"
                summary += "\n"
                summary += f"- Published: {paper['published'][:10]}\n"
                summary += f"- Categories: {', '.join(paper['categories'])}\n"
                summary += f"- Query: {paper['query']}\n"
                summary += f"- File: `{paper['filename']}`\n"
                summary += f"\n**Abstract:**\n{paper['abstract'][:300]}...\n\n"
                summary += "---\n\n"

        with open(SUMMARY_FILE, "w") as f:
            f.write(summary)

        print(f"\nSummary saved to: {SUMMARY_FILE}")


def main():
    """Execute targeted ArXiv research."""
    researcher = ArxivResearcher()

    # Define research queries
    queries = [
        # Query 1: Delegation chain + privilege escalation
        {
            "query": (
                "(delegation chain OR privilege escalation OR scope boundaries) AND "
                "(AI agent OR autonomous agent OR LLM agent) AND "
                "(authentication OR authorization OR security)"
            ),
            "name": "Delegation Chain & Privilege Escalation",
            "max_results": 50,
        },
        # Query 2: Credential lifecycle automation
        {
            "query": (
                "(credential lifecycle OR credential management OR credential provisioning) AND "
                "(AI agent OR autonomous system OR agent automation) AND "
                "(cloud OR kubernetes OR infrastructure)"
            ),
            "name": "Credential Lifecycle Automation",
            "max_results": 50,
        },
        # Query 3: Short-lived tokens
        {
            "query": (
                "(short-lived token OR temporary credential OR ephemeral credential) AND "
                "(AI workload OR agent authentication OR autonomous agent) AND "
                "(cloud OR security)"
            ),
            "name": "Short-Lived Token Management",
            "max_results": 50,
        },
        # Query 4: Credential exposure in AI development
        {
            "query": (
                "(credential exposure OR secret leak OR secrets management) AND "
                "(AI code assistant OR copilot OR LLM development OR AI-assisted) AND "
                "(security OR vulnerability)"
            ),
            "name": "Credential Exposure in AI-Assisted Development",
            "max_results": 50,
        },
        # Query 5: Zero standing privilege
        {
            "query": (
                "(zero standing privilege OR just-in-time OR JIT access) AND "
                "(AI agent OR autonomous system OR agent credential) AND "
                "(cloud OR infrastructure OR security)"
            ),
            "name": "Zero Standing Privilege Architecture",
            "max_results": 50,
        },
        # Query 6: Agent credential rotation
        {
            "query": (
                "(credential rotation OR key rotation OR secret rotation) AND "
                "(AI agent OR agent lifecycle OR autonomous agent) AND "
                "(automation OR orchestration OR security)"
            ),
            "name": "Agent Credential Rotation & Lifecycle",
            "max_results": 50,
        },
        # Query 7: Workload identity federation
        {
            "query": (
                "(workload identity OR federated identity OR identity federation) AND "
                "(AI agent OR agent authentication OR token management) AND "
                "(cloud OR kubernetes OR service account)"
            ),
            "name": "Workload Identity & Token Management",
            "max_results": 50,
        },
        # Query 8: OAuth delegation attacks
        {
            "query": (
                "(OAuth OR OIDC OR token delegation) AND "
                "(scope expansion OR privilege escalation OR security vulnerability) AND "
                "(AI OR agent OR automated)"
            ),
            "name": "OAuth Delegation & Scope Attacks",
            "max_results": 40,
        },
        # Query 9: Service account security
        {
            "query": (
                "(service account OR machine identity OR non-human identity) AND "
                "(AI agent OR autonomous agent OR LLM) AND "
                "(security OR authentication OR credential management)"
            ),
            "name": "Service Account Security for AI Agents",
            "max_results": 40,
        },
        # Query 10: Production security incidents
        {
            "query": (
                "(security incident OR credential compromise OR breach) AND "
                "(AI system OR agent OR automation) AND "
                "(cloud OR production OR infrastructure)"
            ),
            "name": "Production Security Incidents",
            "max_results": 40,
        },
    ]

    # Execute searches
    for i, q in enumerate(queries, 1):
        print(f"\n\n{'#' * 80}")
        print(f"# SEARCH {i}/{len(queries)}: {q['name']}")
        print(f"{'#' * 80}\n")

        researcher.search_and_download(
            query=q["query"], max_results=q["max_results"], query_name=q["name"]
        )

        # Check if target reached
        total = len(researcher.cache.get("papers", []))
        if total >= TARGET_PAPERS:
            print(f"\n*** TARGET PAPERS REACHED: {total}/{TARGET_PAPERS} ***")
            break

        # Brief pause between queries
        if i < len(queries):
            print(f"\nPausing 5 seconds before next query...")
            time.sleep(5)

    # Generate summary
    print("\n\n" + "=" * 80)
    print("GENERATING RESEARCH SUMMARY")
    print("=" * 80 + "\n")

    researcher.generate_summary()

    total_downloaded = len(researcher.cache.get("papers", []))
    print(f"\n*** RESEARCH COMPLETE ***")
    print(f"Total papers downloaded: {total_downloaded}")
    print(f"Target: {TARGET_PAPERS}")
    print(f"Directory: {TARGET_DIR}")


if __name__ == "__main__":
    main()
