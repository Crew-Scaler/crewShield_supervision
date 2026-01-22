#!/usr/bin/env python3
"""
ArXiv Research Script: AI Agent Security & Identity Governance
Target: 35-45 papers on agent security, authorization, and cloud-native governance
"""

import arxiv
import time
import os
from pathlib import Path
from datetime import datetime, timedelta
from typing import List, Dict, Tuple
import json

# Base directory for research
BASE_DIR = Path("/Users/tamnguyen/Documents/GitHub/ksi_watch/KSI-CNA-07_25-12A_BestPractices/references/ai_agent_security")

# Research categories and their target directories
RESEARCH_CATEGORIES = {
    "agent_identity_governance": "agent_identity_governance",
    "service_account_management": "service_account_management",
    "multi_agent_security": "multi_agent_security",
    "lateral_movement_prevention": "lateral_movement_prevention",
    "rbac_frameworks": "rbac_frameworks",
    "prompt_injection_security": "prompt_injection_security",
    "behavioral_baselines": "behavioral_baselines"
}

# Search queries mapped to categories
SEARCH_QUERIES = {
    "agent_identity_governance": [
        "AI agent identity governance authorization cloud",
        "agentic AI security identity management",
        "autonomous agent authentication authorization",
        "AI agent credential management cloud-native"
    ],
    "service_account_management": [
        "service account explosion machine identity AI",
        "workload identity AI ML pipeline governance",
        "machine-to-human identity ratio cloud",
        "service account proliferation AI systems"
    ],
    "multi_agent_security": [
        "multi-agent system security authorization",
        "multi-agent privilege escalation",
        "collaborative AI agent security",
        "distributed agent system security"
    ],
    "lateral_movement_prevention": [
        "AI agent lateral movement detection",
        "authorization bypass agentic AI",
        "agent permission escalation prevention",
        "AI system privilege boundary enforcement"
    ],
    "rbac_frameworks": [
        "RBAC AI agents dynamic authorization",
        "role-based access control multi-agent",
        "attribute-based access control AI cloud",
        "scalable authorization AI orchestration"
    ],
    "prompt_injection_security": [
        "prompt injection AI governance security",
        "indirect prompt injection attack",
        "LLM security governance frameworks",
        "AI agent prompt attack mitigation"
    ],
    "behavioral_baselines": [
        "behavioral baseline AI agent anomaly",
        "AI agent monitoring anomaly detection",
        "agent behavior analysis security",
        "runtime AI agent security monitoring"
    ]
}

# Minimum paper quality criteria
MIN_PAGE_COUNT = 7
TARGET_PAPERS_PER_CATEGORY = 6
DOWNLOAD_DELAY = 3.5  # seconds between downloads

# Date filter: prioritize 2024-2025 papers
# Make timezone-aware for comparison with ArXiv dates
from datetime import timezone
CUTOFF_DATE = datetime(2023, 6, 1, tzinfo=timezone.utc)  # Accept papers from June 2023 onwards


class ArxivResearcher:
    def __init__(self):
        self.downloaded_papers = []
        self.metadata_log = []
        self.client = arxiv.Client()

    def estimate_page_count(self, result) -> int:
        """Estimate page count from PDF file size (rough heuristic)."""
        # Typical academic paper: ~100-200 KB per page
        # Use conservative estimate of 150 KB/page
        if hasattr(result, 'pdf_url'):
            # We'll download and check actual length later
            # For now, return high estimate to allow download
            return 15  # Optimistic default
        return 10

    def is_relevant_paper(self, result, keywords: List[str]) -> bool:
        """Check if paper is relevant based on title and abstract."""
        text = f"{result.title} {result.summary}".lower()

        # Must contain at least 2 keywords
        matches = sum(1 for kw in keywords if kw.lower() in text)
        return matches >= 2

    def search_and_download(
        self,
        category: str,
        queries: List[str],
        max_papers: int = TARGET_PAPERS_PER_CATEGORY
    ) -> List[Dict]:
        """Search ArXiv and download papers for a category."""
        category_dir = BASE_DIR / RESEARCH_CATEGORIES[category]
        category_dir.mkdir(parents=True, exist_ok=True)

        downloaded = []
        seen_titles = set()

        print(f"\n{'='*80}")
        print(f"Category: {category}")
        print(f"Target: {max_papers} papers")
        print(f"{'='*80}\n")

        for query in queries:
            if len(downloaded) >= max_papers:
                break

            print(f"Searching: {query}")

            try:
                search = arxiv.Search(
                    query=query,
                    max_results=20,
                    sort_by=arxiv.SortCriterion.SubmittedDate,
                    sort_order=arxiv.SortOrder.Descending
                )

                results = list(self.client.results(search))

                for result in results:
                    if len(downloaded) >= max_papers:
                        break

                    # Skip if already seen
                    if result.title in seen_titles:
                        continue

                    # Date filter
                    if result.published < CUTOFF_DATE:
                        continue

                    # Relevance check
                    keywords = query.split()[:5]  # Use first 5 words as keywords
                    if not self.is_relevant_paper(result, keywords):
                        continue

                    seen_titles.add(result.title)

                    # Download paper
                    safe_title = "".join(
                        c for c in result.title[:80]
                        if c.isalnum() or c in (' ', '-', '_')
                    ).strip().replace(' ', '_')

                    arxiv_id = result.entry_id.split('/')[-1]
                    filename = f"{arxiv_id}_{safe_title}.pdf"
                    filepath = category_dir / filename

                    try:
                        print(f"  Downloading: {result.title[:60]}...")
                        print(f"    ArXiv ID: {arxiv_id}")
                        print(f"    Published: {result.published.strftime('%Y-%m-%d')}")

                        result.download_pdf(dirpath=str(category_dir), filename=filename)

                        # Verify download
                        if filepath.exists():
                            file_size_mb = filepath.stat().st_size / (1024 * 1024)
                            estimated_pages = int(file_size_mb * 6.67)  # ~150KB per page

                            print(f"    Size: {file_size_mb:.2f} MB (~{estimated_pages} pages)")

                            metadata = {
                                "title": result.title,
                                "arxiv_id": arxiv_id,
                                "authors": [str(author) for author in result.authors],
                                "published": result.published.strftime('%Y-%m-%d'),
                                "category": category,
                                "query": query,
                                "file_path": str(filepath),
                                "file_size_mb": file_size_mb,
                                "estimated_pages": estimated_pages,
                                "summary": result.summary[:300] + "..."
                            }

                            downloaded.append(metadata)
                            self.metadata_log.append(metadata)
                            print(f"    ✓ Downloaded successfully\n")

                            time.sleep(DOWNLOAD_DELAY)
                        else:
                            print(f"    ✗ Download failed\n")

                    except Exception as e:
                        print(f"    ✗ Error downloading: {e}\n")
                        continue

                time.sleep(2)  # Delay between queries

            except Exception as e:
                print(f"  Error searching '{query}': {e}\n")
                continue

        print(f"Category '{category}' complete: {len(downloaded)}/{max_papers} papers\n")
        return downloaded

    def run_full_research(self):
        """Execute comprehensive research across all categories."""
        print("\n" + "="*80)
        print("ArXiv Research: AI Agent Security & Identity Governance")
        print("Target: 35-45 papers | Min 7 pages | 2023-2025 focus")
        print("="*80 + "\n")

        start_time = time.time()

        # Search each category
        for category, queries in SEARCH_QUERIES.items():
            self.search_and_download(category, queries)

        # Generate summary report
        self.generate_summary_report()

        elapsed = time.time() - start_time
        print(f"\n{'='*80}")
        print(f"Research Complete!")
        print(f"Total papers downloaded: {len(self.metadata_log)}")
        print(f"Time elapsed: {elapsed/60:.2f} minutes")
        print(f"{'='*80}\n")

    def generate_summary_report(self):
        """Generate comprehensive research summary."""
        report_path = BASE_DIR / "RESEARCH_SUMMARY.md"

        # Group papers by category
        by_category = {}
        for paper in self.metadata_log:
            cat = paper['category']
            if cat not in by_category:
                by_category[cat] = []
            by_category[cat].append(paper)

        # Generate markdown report
        report = []
        report.append("# ArXiv Research Summary: AI Agent Security & Identity Governance\n")
        report.append(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        report.append(f"**Total Papers:** {len(self.metadata_log)}\n")
        report.append(f"**Research Period:** 2023-2025\n\n")

        report.append("## Research Objectives\n")
        report.append("1. Validate AI agent credential explosion claims (45:1 ratio)\n")
        report.append("2. Research RBAC models for large-scale multi-agent deployments\n")
        report.append("3. Investigate lateral movement prevention in agentic AI\n")
        report.append("4. Find empirical data on agent security incidents\n\n")

        report.append("## Papers by Research Category\n\n")

        for category, papers in sorted(by_category.items()):
            report.append(f"### {category.replace('_', ' ').title()} ({len(papers)} papers)\n\n")

            for i, paper in enumerate(papers, 1):
                report.append(f"**{i}. {paper['title']}**\n")
                report.append(f"- ArXiv ID: {paper['arxiv_id']}\n")
                report.append(f"- Published: {paper['published']}\n")
                report.append(f"- Authors: {', '.join(paper['authors'][:3])}")
                if len(paper['authors']) > 3:
                    report.append(f" et al.")
                report.append(f"\n- File: `{Path(paper['file_path']).name}`\n")
                report.append(f"- Est. Pages: {paper['estimated_pages']}\n")
                report.append(f"- Summary: {paper['summary'][:200]}...\n\n")

        report.append("## Key Validation Targets\n\n")
        report.append("### 1. Machine-to-Human Identity Ratio (45:1 Claim)\n")
        report.append(f"- Papers addressing service account explosion: {len(by_category.get('service_account_management', []))}\n")
        report.append("- Status: Requires manual review of downloaded papers\n\n")

        report.append("### 2. Lateral Movement Detection Latency\n")
        report.append(f"- Papers on lateral movement prevention: {len(by_category.get('lateral_movement_prevention', []))}\n")
        report.append("- Status: Requires empirical data extraction\n\n")

        report.append("### 3. Multi-Agent Authorization Complexity\n")
        report.append(f"- Papers on multi-agent security: {len(by_category.get('multi_agent_security', []))}\n")
        report.append(f"- Papers on RBAC frameworks: {len(by_category.get('rbac_frameworks', []))}\n")
        report.append("- Status: Requires complexity analysis from papers\n\n")

        report.append("### 4. Prompt Injection Attack Success Rates\n")
        report.append(f"- Papers on prompt injection: {len(by_category.get('prompt_injection_security', []))}\n")
        report.append("- Status: Requires attack success rate extraction\n\n")

        report.append("## Production-Ready Frameworks Identified\n\n")
        report.append("*Requires manual review of downloaded papers for framework details*\n\n")

        report.append("## Next Steps\n\n")
        report.append("1. Manual review of high-impact papers (10+ pages, recent)\n")
        report.append("2. Extract quantitative validation data for claims\n")
        report.append("3. Identify production-ready frameworks and tools\n")
        report.append("4. Conduct gap analysis for agent identity governance\n")
        report.append("5. Synthesize findings into Issue #13 analysis\n\n")

        with open(report_path, 'w') as f:
            f.write(''.join(report))

        print(f"Summary report generated: {report_path}")

        # Also save JSON metadata
        json_path = BASE_DIR / "papers_metadata.json"
        with open(json_path, 'w') as f:
            json.dump(self.metadata_log, f, indent=2)
        print(f"Metadata JSON saved: {json_path}")


if __name__ == "__main__":
    researcher = ArxivResearcher()
    researcher.run_full_research()
