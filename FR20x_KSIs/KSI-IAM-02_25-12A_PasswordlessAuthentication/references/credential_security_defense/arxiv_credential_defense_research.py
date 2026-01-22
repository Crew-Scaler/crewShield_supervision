#!/usr/bin/env python3
"""
ArXiv Research Script: AI-Powered Credential Security Defense & Detection
Research Focus: ML-based anomaly detection, automated compromise detection,
behavioral analytics, and real-time credential monitoring systems.
"""

import arxiv
import time
import os
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Set
import json


class CredentialSecurityResearcher:
    """Research AI-powered credential security defense systems on ArXiv."""

    def __init__(self, output_dir: str):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.downloaded_papers: Set[str] = set()
        self.paper_metadata: List[Dict] = []
        self.min_pages = 7
        self.delay_between_downloads = 3
        self.target_papers = 45

    def search_papers(
        self,
        query: str,
        max_results: int = 15,
        sort_by: arxiv.SortCriterion = arxiv.SortCriterion.SubmittedDate
    ) -> List[arxiv.Result]:
        """Search ArXiv with a specific query."""
        print(f"\n{'='*80}")
        print(f"SEARCHING: {query}")
        print(f"{'='*80}")

        try:
            search = arxiv.Search(
                query=query,
                max_results=max_results,
                sort_by=sort_by,
                sort_order=arxiv.SortOrder.Descending
            )

            results = list(search.results())
            print(f"Found {len(results)} papers")
            return results

        except Exception as e:
            print(f"Search error: {e}")
            return []

    def estimate_pages(self, result: arxiv.Result) -> int:
        """Estimate page count from paper length indicators."""
        summary_words = len(result.summary.split())
        estimated_pages = max(8, summary_words // 150)
        return estimated_pages

    def is_relevant_paper(self, result: arxiv.Result) -> bool:
        """Check if paper is relevant to credential security defense."""
        title_lower = result.title.lower()
        summary_lower = result.summary.lower()

        # Core credential security topics
        credential_terms = [
            'credential', 'password', 'authentication', 'login',
            'access control', 'identity', 'oauth', 'sso'
        ]

        # Defense and detection focus
        defense_terms = [
            'anomaly detection', 'intrusion detection', 'threat detection',
            'compromise detection', 'behavioral analytics', 'monitoring',
            'prevention', 'defense', 'security', 'protection'
        ]

        # AI/ML methods
        ml_terms = [
            'machine learning', 'deep learning', 'neural network',
            'artificial intelligence', 'ai', 'ml', 'classification',
            'detection model', 'lstm', 'transformer', 'bert'
        ]

        # Check for credential terms
        has_credential = any(
            term in title_lower or term in summary_lower
            for term in credential_terms
        )

        # Check for defense/detection terms
        has_defense = any(
            term in title_lower or term in summary_lower
            for term in defense_terms
        )

        # Check for ML terms
        has_ml = any(
            term in title_lower or term in summary_lower
            for term in ml_terms
        )

        # Paper should have credential + (defense OR ml)
        return has_credential and (has_defense or has_ml)

    def download_paper(self, result: arxiv.Result) -> bool:
        """Download a paper if it meets criteria."""
        if result.entry_id in self.downloaded_papers:
            print(f"SKIP: Already downloaded - {result.title[:80]}")
            return False

        # Check relevance
        if not self.is_relevant_paper(result):
            print(f"SKIP: Not relevant - {result.title[:80]}")
            return False

        # Estimate pages
        estimated_pages = self.estimate_pages(result)
        if estimated_pages < self.min_pages:
            print(f"SKIP: Too short (~{estimated_pages} pages) - {result.title[:80]}")
            return False

        # Check publication date (prefer 2024-2025)
        pub_year = result.published.year
        is_recent = pub_year >= 2024

        try:
            # Create filename
            arxiv_id = result.entry_id.split('/')[-1]
            safe_title = "".join(
                c for c in result.title[:50]
                if c.isalnum() or c in (' ', '-', '_')
            ).strip().replace(' ', '_')
            filename = f"{arxiv_id}_{safe_title}.pdf"
            filepath = self.output_dir / filename

            # Download
            print(f"\n{'*'*80}")
            print(f"DOWNLOADING: {result.title}")
            print(f"ArXiv ID: {arxiv_id}")
            print(f"Published: {result.published.strftime('%Y-%m-%d')}")
            print(f"Authors: {', '.join(a.name for a in result.authors[:3])}")
            print(f"Estimated pages: {estimated_pages}")
            print(f"Recent (2024+): {is_recent}")
            print(f"File: {filename}")

            result.download_pdf(filename=str(filepath))

            # Store metadata
            metadata = {
                'arxiv_id': arxiv_id,
                'title': result.title,
                'authors': [a.name for a in result.authors],
                'published': result.published.strftime('%Y-%m-%d'),
                'updated': result.updated.strftime('%Y-%m-%d'),
                'categories': result.categories,
                'primary_category': result.primary_category,
                'summary': result.summary,
                'pdf_url': result.pdf_url,
                'estimated_pages': estimated_pages,
                'is_recent': is_recent,
                'filename': filename,
                'downloaded_at': datetime.now().isoformat()
            }
            self.paper_metadata.append(metadata)
            self.downloaded_papers.add(result.entry_id)

            print(f"SUCCESS: Downloaded {len(self.downloaded_papers)} papers")
            print(f"{'*'*80}\n")

            # Delay between downloads
            time.sleep(self.delay_between_downloads)
            return True

        except Exception as e:
            print(f"ERROR downloading {result.title}: {e}")
            return False

    def execute_research(self):
        """Execute comprehensive credential security defense research."""
        print("\n" + "="*80)
        print("ARXIV RESEARCH: AI-POWERED CREDENTIAL SECURITY DEFENSE & DETECTION")
        print("="*80)
        print(f"Target: {self.target_papers} papers (>7 pages)")
        print(f"Priority: 2024-2025 publications")
        print(f"Output: {self.output_dir}")
        print("="*80 + "\n")

        # Define search queries targeting credential security defense
        search_queries = [
            # Query 1: ML-based credential anomaly detection
            (
                'abs:"credential" AND '
                '(abs:"anomaly detection" OR abs:"behavioral analytics") AND '
                '(abs:"machine learning" OR abs:"deep learning")',
                15
            ),

            # Query 2: Automated credential compromise detection
            (
                'abs:"authentication" AND '
                '(abs:"compromise detection" OR abs:"intrusion detection") AND '
                '(abs:"automated" OR abs:"real-time")',
                15
            ),

            # Query 3: Behavioral analytics for authentication
            (
                'abs:"authentication" AND '
                'abs:"behavioral" AND '
                '(abs:"analytics" OR abs:"pattern") AND '
                'abs:"security"',
                15
            ),

            # Query 4: AI-powered credential theft prevention
            (
                '(abs:"credential theft" OR abs:"password attack") AND '
                '(abs:"prevention" OR abs:"defense") AND '
                '(abs:"AI" OR abs:"machine learning")',
                12
            ),

            # Query 5: Real-time credential monitoring
            (
                'abs:"credential" AND '
                'abs:"monitoring" AND '
                '(abs:"real-time" OR abs:"continuous") AND '
                '(abs:"detection" OR abs:"security")',
                12
            ),

            # Query 6: Insider threat detection via credentials
            (
                '(abs:"insider threat" OR abs:"insider attack") AND '
                'abs:"authentication" AND '
                '(abs:"detection" OR abs:"monitoring")',
                12
            ),

            # Query 7: Access pattern anomaly detection
            (
                'abs:"access control" AND '
                'abs:"anomaly detection" AND '
                '(abs:"machine learning" OR abs:"neural network")',
                12
            ),

            # Query 8: Login anomaly detection systems
            (
                'abs:"login" AND '
                'abs:"anomaly" AND '
                '(abs:"detection system" OR abs:"security system") AND '
                '(abs:"ML" OR abs:"AI")',
                10
            ),

            # Query 9: Identity theft detection
            (
                'abs:"identity theft" AND '
                'abs:"detection" AND '
                '(abs:"machine learning" OR abs:"behavioral")',
                10
            ),

            # Query 10: OAuth/SSO security monitoring
            (
                '(abs:"OAuth" OR abs:"SSO" OR abs:"single sign-on") AND '
                'abs:"security" AND '
                '(abs:"monitoring" OR abs:"detection")',
                10
            ),
        ]

        # Execute searches
        for query, max_results in search_queries:
            if len(self.downloaded_papers) >= self.target_papers:
                print(f"\nTarget reached: {len(self.downloaded_papers)} papers")
                break

            results = self.search_papers(query, max_results)

            for result in results:
                if len(self.downloaded_papers) >= self.target_papers:
                    break

                self.download_paper(result)

            # Brief pause between searches
            time.sleep(2)

        # Save metadata
        self.save_metadata()
        self.generate_summary()

    def save_metadata(self):
        """Save paper metadata to JSON file."""
        metadata_file = self.output_dir / "paper_metadata.json"
        with open(metadata_file, 'w', encoding='utf-8') as f:
            json.dump(self.paper_metadata, f, indent=2, ensure_ascii=False)
        print(f"\nMetadata saved to: {metadata_file}")

    def generate_summary(self):
        """Generate research summary report."""
        summary_file = self.output_dir / "RESEARCH_SUMMARY.md"

        # Count by category
        recent_papers = sum(1 for p in self.paper_metadata if p['is_recent'])

        # Categorize papers
        categories = {
            'Anomaly Detection': [],
            'Behavioral Analytics': [],
            'Compromise Detection': [],
            'Theft Prevention': [],
            'Real-time Monitoring': [],
            'Insider Threat': [],
            'Other': []
        }

        for paper in self.paper_metadata:
            title_lower = paper['title'].lower()
            summary_lower = paper['summary'].lower()

            categorized = False
            if 'anomaly' in title_lower or 'anomaly' in summary_lower:
                categories['Anomaly Detection'].append(paper)
                categorized = True
            if 'behavioral' in title_lower or 'behavioral' in summary_lower:
                categories['Behavioral Analytics'].append(paper)
                categorized = True
            if 'compromise' in title_lower or 'intrusion' in title_lower:
                categories['Compromise Detection'].append(paper)
                categorized = True
            if 'theft' in title_lower or 'prevention' in title_lower:
                categories['Theft Prevention'].append(paper)
                categorized = True
            if 'real-time' in title_lower or 'monitoring' in summary_lower:
                categories['Real-time Monitoring'].append(paper)
                categorized = True
            if 'insider' in title_lower or 'insider' in summary_lower:
                categories['Insider Threat'].append(paper)
                categorized = True
            if not categorized:
                categories['Other'].append(paper)

        with open(summary_file, 'w', encoding='utf-8') as f:
            f.write("# ArXiv Research Summary\n")
            f.write("## AI-Powered Credential Security Defense & Detection\n\n")
            f.write(f"**Research Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

            f.write("## Overview\n\n")
            f.write(f"- **Total Papers Downloaded:** {len(self.paper_metadata)}\n")
            f.write(f"- **Recent Papers (2024-2025):** {recent_papers}\n")
            f.write(f"- **Output Directory:** `{self.output_dir}`\n\n")

            f.write("## Research Focus Areas\n\n")
            f.write("1. ML-based credential usage anomaly detection\n")
            f.write("2. Automated credential compromise detection systems\n")
            f.write("3. Behavioral analytics for authentication security\n")
            f.write("4. AI-powered credential theft prevention and response\n")
            f.write("5. Real-time credential monitoring and protection systems\n")
            f.write("6. Machine learning for insider threat detection\n\n")

            f.write("## Papers by Category\n\n")
            for category, papers in categories.items():
                if papers:
                    f.write(f"### {category} ({len(papers)} papers)\n\n")
                    for paper in papers:
                        f.write(f"**{paper['title']}**\n")
                        f.write(f"- ArXiv ID: {paper['arxiv_id']}\n")
                        f.write(f"- Published: {paper['published']}\n")
                        f.write(f"- Authors: {', '.join(paper['authors'][:3])}")
                        if len(paper['authors']) > 3:
                            f.write(f" et al.")
                        f.write(f"\n- File: `{paper['filename']}`\n\n")

            f.write("## Key Validation Targets\n\n")
            f.write("- ML-based credential anomaly detection accuracy and effectiveness\n")
            f.write("- Automated compromise detection system performance metrics\n")
            f.write("- Behavioral analytics effectiveness for credential security\n")
            f.write("- AI-powered prevention system response times and accuracy\n")
            f.write("- Real-time monitoring system scalability and precision\n\n")

            f.write("## Next Steps\n\n")
            f.write("1. Review downloaded papers for production system implementations\n")
            f.write("2. Extract performance metrics and validation results\n")
            f.write("3. Identify best practices for credential security defense\n")
            f.write("4. Document quantified effectiveness studies\n")
            f.write("5. Analyze real-time monitoring system architectures\n\n")

        print(f"Summary report saved to: {summary_file}")

        # Print summary to console
        print("\n" + "="*80)
        print("RESEARCH COMPLETE")
        print("="*80)
        print(f"Total papers downloaded: {len(self.paper_metadata)}")
        print(f"Recent papers (2024-2025): {recent_papers}")
        print("\nPapers by category:")
        for category, papers in categories.items():
            if papers:
                print(f"  - {category}: {len(papers)}")
        print("="*80 + "\n")


def main():
    """Main execution function."""
    output_dir = "/Users/tamnguyen/Documents/GitHub/ksi_watch/KSI-IAM-02_25-12A_PasswordlessAuthentication/references/credential_security_defense"

    researcher = CredentialSecurityResearcher(output_dir)
    researcher.execute_research()


if __name__ == "__main__":
    main()
