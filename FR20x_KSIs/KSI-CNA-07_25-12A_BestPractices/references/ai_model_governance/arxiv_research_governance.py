#!/usr/bin/env python3
"""
ArXiv Research Script: AI Model Governance & Compliance Frameworks
Focus: NIST AI RMF, ISO 42001, ML Model Lifecycle Management

Research Areas:
1. NIST AI RMF operationalization in production systems
2. ML model registry and lineage governance approaches
3. Model drift detection and compliance monitoring
4. AI compliance automation frameworks
5. Training data provenance and model supply chain security
"""

import arxiv
import time
import os
from pathlib import Path
from datetime import datetime, timedelta, timezone
import json
from typing import List, Dict

# Configuration
TARGET_DIR = Path(
    "/Users/tamnguyen/Documents/GitHub/ksi_watch/KSI-CNA-07_25-12A_BestPractices/"
    "references/ai_model_governance"
)
MIN_PAGES = 7
TARGET_PAPERS = 45
DOWNLOAD_DELAY = 3
DATE_CUTOFF = datetime(2024, 1, 1, tzinfo=timezone.utc)  # Prioritize 2024-2025 papers

# Research queries targeting AI model governance
SEARCH_QUERIES = [
    {
        "query": (
            "all:(NIST AI RMF) AND "
            "all:(implementation OR operationalization OR deployment) AND "
            "all:(cloud OR production OR system)"
        ),
        "category": "nist_ai_rmf",
        "max_results": 15,
    },
    {
        "query": (
            "all:(ISO 42001 OR AI management system) AND "
            "all:(governance OR compliance OR model management)"
        ),
        "category": "iso_42001_governance",
        "max_results": 10,
    },
    {
        "query": (
            "all:(machine learning model registry OR ML model registry) AND "
            "all:(governance OR lineage OR versioning OR tracking)"
        ),
        "category": "model_registry_governance",
        "max_results": 10,
    },
    {
        "query": (
            "all:(model drift OR concept drift) AND "
            "all:(monitoring OR detection OR retraining) AND "
            "all:(governance OR compliance OR management)"
        ),
        "category": "model_drift_governance",
        "max_results": 10,
    },
    {
        "query": (
            "all:(AI compliance automation OR automated compliance) AND "
            "all:(regulatory OR framework OR NIST OR governance)"
        ),
        "category": "compliance_automation",
        "max_results": 10,
    },
    {
        "query": (
            "all:(training data lineage OR data provenance) AND "
            "all:(AI governance OR model governance OR traceability)"
        ),
        "category": "data_provenance",
        "max_results": 10,
    },
    {
        "query": (
            "all:(model risk management OR AI risk management) AND "
            "all:(governance OR framework OR cloud OR deployment)"
        ),
        "category": "model_risk_management",
        "max_results": 10,
    },
    {
        "query": (
            "all:(MLOps governance OR ML lifecycle governance) AND "
            "all:(compliance OR monitoring OR model management)"
        ),
        "category": "mlops_governance",
        "max_results": 10,
    },
    {
        "query": (
            "all:(AI model supply chain OR ML supply chain) AND "
            "all:(security OR governance OR provenance OR risk)"
        ),
        "category": "model_supply_chain",
        "max_results": 10,
    },
    {
        "query": (
            "all:(responsible AI OR trustworthy AI) AND "
            "all:(governance framework OR compliance OR operationalization) AND "
            "all:(production OR deployment)"
        ),
        "category": "responsible_ai_governance",
        "max_results": 10,
    },
]


class ArxivGovernanceResearcher:
    """Research assistant for AI model governance papers"""

    def __init__(self):
        self.downloaded_papers = []
        self.metadata = []
        self.papers_by_category = {}
        self.client = arxiv.Client()

    def estimate_pages(self, result) -> int:
        """Estimate page count from paper metadata"""
        # Most papers are 8-15 pages, use summary length as proxy
        summary_length = len(result.summary)
        if summary_length < 800:
            return 5
        elif summary_length < 1500:
            return 8
        elif summary_length < 2500:
            return 12
        else:
            return 15

    def is_relevant_paper(self, result) -> tuple[bool, str]:
        """
        Check if paper is relevant for AI model governance research
        Returns: (is_relevant, reason)
        """
        title_lower = result.title.lower()
        summary_lower = result.summary.lower()
        combined = title_lower + " " + summary_lower

        # High relevance keywords for AI model governance
        governance_terms = [
            "governance",
            "compliance",
            "nist",
            "iso 42001",
            "regulatory",
            "risk management",
            "model registry",
            "model lifecycle",
            "mlops",
        ]

        model_management_terms = [
            "model drift",
            "model monitoring",
            "model versioning",
            "model lineage",
            "model tracking",
            "model deployment",
            "model validation",
        ]

        compliance_terms = [
            "ai rmf",
            "ai risk management",
            "responsible ai",
            "trustworthy ai",
            "ai audit",
            "ai transparency",
            "explainable ai governance",
        ]

        data_governance_terms = [
            "data provenance",
            "data lineage",
            "training data",
            "data governance",
            "supply chain security",
        ]

        # Check for high-value combinations
        governance_count = sum(
            1 for term in governance_terms if term in combined
        )
        model_mgmt_count = sum(
            1 for term in model_management_terms if term in combined
        )
        compliance_count = sum(
            1 for term in compliance_terms if term in combined
        )
        data_gov_count = sum(
            1 for term in data_governance_terms if term in combined
        )

        total_matches = (
            governance_count + model_mgmt_count +
            compliance_count + data_gov_count
        )

        # Priority criteria
        if "nist" in combined and "ai rmf" in combined:
            return (True, "NIST AI RMF implementation paper")

        if "iso 42001" in combined:
            return (True, "ISO 42001 AI management system paper")

        if model_mgmt_count >= 2 and governance_count >= 1:
            return (True, "Strong model lifecycle governance focus")

        if compliance_count >= 2:
            return (True, "Strong AI compliance framework focus")

        if total_matches >= 3:
            return (True, f"Multiple relevant terms ({total_matches} matches)")

        # Exclude pure theory or unrelated papers
        exclude_terms = [
            "quantum computing",
            "drug discovery",
            "medical imaging only",
            "purely theoretical",
            "mathematics proof",
        ]

        if any(term in combined for term in exclude_terms):
            return (False, "Not relevant to enterprise AI governance")

        if total_matches >= 1:
            return (True, "Moderate relevance to AI governance")

        return (False, "Insufficient governance focus")

    def search_and_download(self, query_config: Dict) -> List[Dict]:
        """Search ArXiv and download relevant papers"""
        query = query_config["query"]
        category = query_config["category"]
        max_results = query_config["max_results"]

        print(f"\n{'='*80}")
        print(f"Searching: {category}")
        print(f"Query: {query}")
        print(f"{'='*80}\n")

        search = arxiv.Search(
            query=query,
            max_results=max_results * 3,  # Get more to filter
            sort_by=arxiv.SortCriterion.SubmittedDate,
            sort_order=arxiv.SortOrder.Descending,
        )

        category_papers = []
        papers_found = 0

        try:
            for result in self.client.results(search):
                # Check date relevance (prioritize 2024-2025)
                if result.published < DATE_CUTOFF:
                    continue

                # Check relevance
                is_relevant, reason = self.is_relevant_paper(result)
                if not is_relevant:
                    print(f"  ⊘ Skipping: {result.title[:60]}... - {reason}")
                    continue

                # Estimate pages
                estimated_pages = self.estimate_pages(result)
                if estimated_pages < MIN_PAGES:
                    print(
                        f"  ⊘ Too short ({estimated_pages}p): "
                        f"{result.title[:50]}..."
                    )
                    continue

                papers_found += 1
                print(f"\n  ✓ Relevant ({reason})")
                print(f"    Title: {result.title}")
                print(f"    Published: {result.published.strftime('%Y-%m-%d')}")
                print(f"    Est. pages: {estimated_pages}")
                print(f"    Categories: {', '.join(result.categories)}")

                # Download paper
                filename = f"{category}_{result.get_short_id()}.pdf"
                filepath = TARGET_DIR / filename

                try:
                    print(f"    Downloading to: {filename}")
                    result.download_pdf(dirpath=str(TARGET_DIR), filename=filename)

                    paper_metadata = {
                        "arxiv_id": result.get_short_id(),
                        "title": result.title,
                        "authors": [author.name for author in result.authors],
                        "published": result.published.strftime("%Y-%m-%d"),
                        "updated": result.updated.strftime("%Y-%m-%d"),
                        "categories": result.categories,
                        "primary_category": result.primary_category,
                        "summary": result.summary,
                        "pdf_url": result.pdf_url,
                        "estimated_pages": estimated_pages,
                        "category": category,
                        "relevance_reason": reason,
                        "downloaded_file": filename,
                    }

                    category_papers.append(paper_metadata)
                    self.downloaded_papers.append(paper_metadata)
                    self.metadata.append(paper_metadata)

                    print(f"    ✓ Downloaded successfully!")
                    time.sleep(DOWNLOAD_DELAY)

                except Exception as e:
                    print(f"    ✗ Download failed: {e}")

                if papers_found >= max_results:
                    break

            print(f"\n  Category summary: {papers_found} papers downloaded")

        except Exception as e:
            print(f"\n  ✗ Search failed for {category}: {e}")

        return category_papers

    def run_research(self):
        """Execute full research pipeline"""
        print("\n" + "=" * 80)
        print("ArXiv Research: AI Model Governance & Compliance Frameworks")
        print("=" * 80)
        print(f"Target directory: {TARGET_DIR}")
        print(f"Target papers: {TARGET_PAPERS}")
        print(f"Minimum pages: {MIN_PAGES}")
        print(f"Date cutoff: {DATE_CUTOFF.strftime('%Y-%m-%d')}")
        print("=" * 80)

        start_time = time.time()

        # Execute searches
        for query_config in SEARCH_QUERIES:
            category_papers = self.search_and_download(query_config)
            self.papers_by_category[query_config["category"]] = category_papers

            total_downloaded = len(self.downloaded_papers)
            print(f"\n  Progress: {total_downloaded}/{TARGET_PAPERS} papers")

            if total_downloaded >= TARGET_PAPERS:
                print(f"\n  ✓ Target of {TARGET_PAPERS} papers reached!")
                break

        elapsed_time = time.time() - start_time

        # Generate research summary
        self.generate_summary(elapsed_time)

        return self.metadata

    def generate_summary(self, elapsed_time: float):
        """Generate research summary and save metadata"""
        print("\n" + "=" * 80)
        print("RESEARCH SUMMARY")
        print("=" * 80)

        total_papers = len(self.downloaded_papers)
        print(f"\nTotal papers downloaded: {total_papers}")
        print(f"Time elapsed: {elapsed_time/60:.2f} minutes")
        print(f"\nPapers by category:")

        for category, papers in self.papers_by_category.items():
            if papers:
                print(f"  • {category}: {len(papers)} papers")

        # Save metadata
        metadata_file = TARGET_DIR / "research_metadata.json"
        with open(metadata_file, "w", encoding="utf-8") as f:
            json.dump(
                {
                    "research_date": datetime.now().isoformat(),
                    "total_papers": total_papers,
                    "target_papers": TARGET_PAPERS,
                    "elapsed_time_minutes": elapsed_time / 60,
                    "papers_by_category": {
                        cat: len(papers)
                        for cat, papers in self.papers_by_category.items()
                    },
                    "papers": self.metadata,
                },
                f,
                indent=2,
            )

        print(f"\nMetadata saved to: {metadata_file}")

        # Generate categorized summary
        self.generate_categorized_summary()

    def generate_categorized_summary(self):
        """Generate detailed categorized summary"""
        summary_file = TARGET_DIR / "research_summary.md"

        with open(summary_file, "w", encoding="utf-8") as f:
            f.write("# AI Model Governance & Compliance Frameworks Research\n\n")
            f.write(f"**Research Date:** {datetime.now().strftime('%Y-%m-%d')}\n")
            f.write(f"**Total Papers:** {len(self.downloaded_papers)}\n\n")

            f.write("## Research Focus Areas\n\n")
            f.write("1. NIST AI RMF operationalization in production systems\n")
            f.write("2. ML model registry and lineage governance approaches\n")
            f.write("3. Model drift detection and compliance monitoring\n")
            f.write("4. AI compliance automation frameworks\n")
            f.write("5. Training data provenance and model supply chain security\n\n")

            f.write("## Papers by Category\n\n")

            for category, papers in self.papers_by_category.items():
                if not papers:
                    continue

                f.write(f"### {category.replace('_', ' ').title()}\n\n")
                f.write(f"**Count:** {len(papers)} papers\n\n")

                for paper in papers:
                    f.write(f"#### {paper['title']}\n\n")
                    f.write(f"- **ArXiv ID:** {paper['arxiv_id']}\n")
                    f.write(f"- **Published:** {paper['published']}\n")
                    f.write(
                        f"- **Authors:** {', '.join(paper['authors'][:3])}"
                    )
                    if len(paper['authors']) > 3:
                        f.write(f" et al. ({len(paper['authors'])} total)")
                    f.write("\n")
                    f.write(f"- **Categories:** {', '.join(paper['categories'])}\n")
                    f.write(f"- **Est. Pages:** {paper['estimated_pages']}\n")
                    f.write(f"- **Relevance:** {paper['relevance_reason']}\n")
                    f.write(f"- **File:** `{paper['downloaded_file']}`\n")
                    f.write(f"- **URL:** {paper['pdf_url']}\n\n")
                    f.write("**Abstract:**\n")
                    f.write(f"> {paper['summary'][:300]}...\n\n")
                    f.write("---\n\n")

        print(f"Summary saved to: {summary_file}")


def main():
    """Main execution function"""
    researcher = ArxivGovernanceResearcher()
    researcher.run_research()


if __name__ == "__main__":
    main()
