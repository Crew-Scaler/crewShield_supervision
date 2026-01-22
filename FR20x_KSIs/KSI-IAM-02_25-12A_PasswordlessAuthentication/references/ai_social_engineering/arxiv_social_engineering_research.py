#!/usr/bin/env python3
"""
ArXiv Research: AI-Powered Social Engineering & Credential Theft
Focus: LLM-based phishing, deepfakes, impersonation, and automated attacks
Target: 35-45 papers from 2024-2025
"""

import arxiv
import time
import os
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Set
import json


class SocialEngineeringResearcher:
    """Research AI-powered social engineering and credential theft."""

    def __init__(self, output_dir: str):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.papers_downloaded: Set[str] = set()
        self.metadata: List[Dict] = []
        self.min_pages = 7
        self.target_papers = 45
        self.download_delay = 3.5

        # Define targeted search queries
        self.search_queries = [
            # LLM-based social engineering and phishing
            '(abs:"large language model" OR abs:LLM OR abs:"generative AI") AND '
            '(abs:"social engineering" OR abs:phishing OR abs:"credential theft" OR abs:"password attack") AND '
            '(submittedDate:[20240101 TO 20251231])',

            # AI impersonation and deepfake attacks
            '(abs:deepfake OR abs:"deep fake" OR abs:impersonation OR abs:"voice cloning") AND '
            '(abs:"social engineering" OR abs:authentication OR abs:trust OR abs:"credential attack") AND '
            '(submittedDate:[20240101 TO 20251231])',

            # ML-driven personalization for attacks
            '(abs:"machine learning" OR abs:"artificial intelligence") AND '
            '(abs:personalization OR abs:targeting OR abs:"spear phishing") AND '
            '(abs:"social engineering" OR abs:"credential compromise") AND '
            '(submittedDate:[20240101 TO 20251231])',

            # Automated campaign generation
            '(abs:automated OR abs:autonomous OR abs:"generative AI") AND '
            '(abs:"attack campaign" OR abs:"phishing campaign" OR abs:"social engineering attack") AND '
            '(abs:credential OR abs:authentication) AND '
            '(submittedDate:[20240101 TO 20251231])',

            # Voice synthesis and behavioral mimicry
            '(abs:"voice synthesis" OR abs:"speech synthesis" OR abs:"voice clone") AND '
            '(abs:authentication OR abs:"social engineering" OR abs:impersonation) AND '
            '(submittedDate:[20240101 TO 20251231])',

            # Behavioral analysis and trust exploitation
            '(abs:"behavioral analysis" OR abs:"trust exploitation" OR abs:"psychological manipulation") AND '
            '(abs:"AI" OR abs:"machine learning") AND '
            '(abs:credential OR abs:authentication OR abs:"social engineering") AND '
            '(submittedDate:[20240101 TO 20251231])',

            # LLM jailbreaking and prompt injection (credential context)
            '(abs:"prompt injection" OR abs:jailbreak OR abs:"adversarial prompt") AND '
            '(abs:LLM OR abs:"large language model") AND '
            '(abs:credential OR abs:authentication OR abs:"social engineering") AND '
            '(submittedDate:[20240101 TO 20251231])',

            # AI-generated content for deception
            '(abs:"AI-generated" OR abs:"synthetic content" OR abs:"generative model") AND '
            '(abs:deception OR abs:manipulation OR abs:phishing) AND '
            '(abs:credential OR abs:authentication) AND '
            '(submittedDate:[20240101 TO 20251231])',

            # Adversarial AI in social contexts
            '(abs:"adversarial AI" OR abs:"adversarial machine learning") AND '
            '(abs:social OR abs:human OR abs:trust) AND '
            '(abs:authentication OR abs:credential OR abs:security) AND '
            '(submittedDate:[20240101 TO 20251231])',

            # Chatbot and conversational AI attacks
            '(abs:chatbot OR abs:"conversational AI" OR abs:"dialogue system") AND '
            '(abs:attack OR abs:manipulation OR abs:deception) AND '
            '(abs:credential OR abs:authentication OR abs:"social engineering") AND '
            '(submittedDate:[20240101 TO 20251231])',
        ]

    def estimate_pages(self, result) -> int:
        """Estimate number of pages from metadata."""
        # Try to get page count from comments or other fields
        if hasattr(result, 'comment') and result.comment:
            comment = result.comment.lower()
            if 'pages' in comment or 'page' in comment:
                import re
                match = re.search(r'(\d+)\s*pages?', comment)
                if match:
                    return int(match.group(1))

        # Fallback: estimate from abstract length and typical paper structure
        # Average paper has ~250 words per page
        if hasattr(result, 'summary'):
            abstract_words = len(result.summary.split())
            # Abstracts are typically 150-300 words for 8+ page papers
            if abstract_words > 200:
                return 10  # Likely a full paper
            elif abstract_words > 150:
                return 8
            else:
                return 6

        return 8  # Default estimate

    def is_relevant(self, result) -> bool:
        """Check if paper is relevant to AI social engineering research."""
        title_lower = result.title.lower()
        abstract_lower = result.summary.lower()
        combined = title_lower + " " + abstract_lower

        # Must have AI/ML component
        ai_terms = ['llm', 'large language model', 'gpt', 'ai', 'machine learning',
                   'deep learning', 'neural network', 'generative', 'transformer',
                   'deepfake', 'synthetic', 'chatbot', 'conversational ai']
        has_ai = any(term in combined for term in ai_terms)

        # Must have social engineering/credential component
        attack_terms = ['social engineering', 'phishing', 'credential', 'password',
                       'authentication', 'impersonation', 'deception', 'manipulation',
                       'trust', 'voice clone', 'deepfake', 'spear phishing',
                       'pretexting', 'baiting', 'quid pro quo']
        has_attack = any(term in combined for term in attack_terms)

        # Boost for highly relevant combinations
        high_relevance_terms = [
            'llm social engineering', 'ai phishing', 'deepfake authentication',
            'voice clone attack', 'automated phishing', 'ai impersonation',
            'generative social engineering', 'llm credential', 'chatbot attack',
            'synthetic voice', 'ai deception', 'prompt injection attack'
        ]
        has_high_relevance = any(term in combined for term in high_relevance_terms)

        # Exclude pure theory without security focus
        exclude_terms = ['medical', 'healthcare', 'drug discovery', 'biology',
                        'chemistry', 'astronomy', 'physics simulation']
        has_exclude = any(term in combined for term in exclude_terms)

        return (has_ai and has_attack) or has_high_relevance and not has_exclude

    def download_paper(self, result) -> bool:
        """Download paper if meets criteria."""
        if result.entry_id in self.papers_downloaded:
            return False

        # Check relevance
        if not self.is_relevant(result):
            print(f"  ⊘ Not relevant: {result.title[:80]}...")
            return False

        # Estimate pages
        estimated_pages = self.estimate_pages(result)
        if estimated_pages < self.min_pages:
            print(f"  ⊘ Too short ({estimated_pages} pages): {result.title[:60]}...")
            return False

        # Check year (prioritize 2025, then 2024)
        pub_year = result.published.year
        if pub_year < 2024:
            print(f"  ⊘ Too old ({pub_year}): {result.title[:70]}...")
            return False

        # Download
        try:
            filename = f"{result.entry_id.split('/')[-1]}.pdf"
            filepath = self.output_dir / filename

            if filepath.exists():
                print(f"  ⊙ Already exists: {result.title[:70]}...")
                self.papers_downloaded.add(result.entry_id)
                return True

            print(f"  ⬇ Downloading [{pub_year}] {estimated_pages}p: {result.title[:60]}...")
            result.download_pdf(dirpath=str(self.output_dir), filename=filename)

            # Save metadata
            self.metadata.append({
                'title': result.title,
                'authors': [author.name for author in result.authors],
                'published': result.published.isoformat(),
                'updated': result.updated.isoformat(),
                'arxiv_id': result.entry_id.split('/')[-1],
                'categories': result.categories,
                'abstract': result.summary,
                'pdf_url': result.pdf_url,
                'estimated_pages': estimated_pages,
                'filename': filename
            })

            self.papers_downloaded.add(result.entry_id)
            print(f"  ✓ Downloaded: {filename}")

            # Delay between downloads
            time.sleep(self.download_delay)
            return True

        except Exception as e:
            print(f"  ✗ Error downloading {result.title[:50]}: {e}")
            return False

    def search_and_download(self, query: str, max_results: int = 50) -> int:
        """Execute search and download relevant papers."""
        print(f"\n{'='*80}")
        print(f"Search Query: {query[:100]}...")
        print(f"{'='*80}")

        downloaded = 0
        try:
            search = arxiv.Search(
                query=query,
                max_results=max_results,
                sort_by=arxiv.SortCriterion.SubmittedDate,
                sort_order=arxiv.SortOrder.Descending
            )

            for result in search.results():
                if len(self.papers_downloaded) >= self.target_papers:
                    print(f"\n✓ Target reached: {self.target_papers} papers")
                    return downloaded

                if self.download_paper(result):
                    downloaded += 1
                    print(f"  Progress: {len(self.papers_downloaded)}/{self.target_papers}")

        except Exception as e:
            print(f"✗ Search error: {e}")

        return downloaded

    def execute_research(self):
        """Execute all searches and compile results."""
        print(f"\n{'#'*80}")
        print(f"# ArXiv Research: AI Social Engineering & Credential Theft")
        print(f"# Target: {self.target_papers} papers (2024-2025)")
        print(f"# Minimum pages: {self.min_pages}")
        print(f"# Output: {self.output_dir}")
        print(f"{'#'*80}\n")

        start_time = time.time()

        # Execute searches
        for i, query in enumerate(self.search_queries, 1):
            if len(self.papers_downloaded) >= self.target_papers:
                break

            print(f"\n[Query {i}/{len(self.search_queries)}]")
            self.search_and_download(query, max_results=60)

            # Brief pause between queries
            if i < len(self.search_queries):
                time.sleep(2)

        # Save metadata
        metadata_file = self.output_dir / 'research_metadata.json'
        with open(metadata_file, 'w') as f:
            json.dump({
                'research_date': datetime.now().isoformat(),
                'total_papers': len(self.papers_downloaded),
                'papers': self.metadata,
                'search_queries': self.search_queries
            }, f, indent=2)

        # Generate summary report
        self.generate_report()

        elapsed = time.time() - start_time
        print(f"\n{'='*80}")
        print(f"Research Complete!")
        print(f"Papers Downloaded: {len(self.papers_downloaded)}")
        print(f"Time Elapsed: {elapsed/60:.1f} minutes")
        print(f"Metadata: {metadata_file}")
        print(f"{'='*80}\n")

    def generate_report(self):
        """Generate research summary report."""
        report_file = self.output_dir / 'RESEARCH_SUMMARY.md'

        # Analyze papers by category
        year_2025 = sum(1 for p in self.metadata if p['published'].startswith('2025'))
        year_2024 = sum(1 for p in self.metadata if p['published'].startswith('2024'))

        # Categorize by topic
        llm_social = sum(1 for p in self.metadata
                        if any(term in p['title'].lower() + p['abstract'].lower()
                              for term in ['llm', 'language model', 'gpt']))

        deepfake = sum(1 for p in self.metadata
                      if any(term in p['title'].lower() + p['abstract'].lower()
                            for term in ['deepfake', 'voice clone', 'synthetic']))

        phishing = sum(1 for p in self.metadata
                      if any(term in p['title'].lower() + p['abstract'].lower()
                            for term in ['phishing', 'social engineering']))

        with open(report_file, 'w') as f:
            f.write("# AI-Powered Social Engineering & Credential Theft Research\n\n")
            f.write(f"**Research Date:** {datetime.now().strftime('%Y-%m-%d')}\n\n")
            f.write(f"**Total Papers:** {len(self.papers_downloaded)}\n\n")

            f.write("## Distribution by Year\n\n")
            f.write(f"- 2025: {year_2025} papers\n")
            f.write(f"- 2024: {year_2024} papers\n\n")

            f.write("## Distribution by Topic\n\n")
            f.write(f"- LLM/Language Models: {llm_social} papers\n")
            f.write(f"- Deepfakes/Synthetic Media: {deepfake} papers\n")
            f.write(f"- Phishing/Social Engineering: {phishing} papers\n\n")

            f.write("## Research Focus Areas\n\n")
            f.write("1. **LLM-Based Social Engineering**\n")
            f.write("   - LLM-generated phishing campaigns\n")
            f.write("   - Automated social engineering attacks\n")
            f.write("   - Prompt injection and jailbreaking\n\n")

            f.write("2. **Deepfake & Impersonation Attacks**\n")
            f.write("   - Voice cloning for authentication bypass\n")
            f.write("   - Video deepfakes for credential theft\n")
            f.write("   - AI-powered impersonation techniques\n\n")

            f.write("3. **Personalization & Targeting**\n")
            f.write("   - ML-driven spear phishing\n")
            f.write("   - Behavioral analysis for targeting\n")
            f.write("   - Trust exploitation using AI\n\n")

            f.write("4. **Automated Attack Campaigns**\n")
            f.write("   - Generative AI for attack scaling\n")
            f.write("   - Autonomous social engineering systems\n")
            f.write("   - Campaign optimization using ML\n\n")

            f.write("## Downloaded Papers\n\n")

            # Sort by year (2025 first) then title
            sorted_papers = sorted(self.metadata,
                                 key=lambda x: (x['published'], x['title']),
                                 reverse=True)

            for paper in sorted_papers:
                year = paper['published'][:4]
                f.write(f"### [{year}] {paper['title']}\n\n")
                f.write(f"**Authors:** {', '.join(paper['authors'][:3])}")
                if len(paper['authors']) > 3:
                    f.write(f" et al. ({len(paper['authors'])} total)")
                f.write(f"\n\n**ArXiv ID:** {paper['arxiv_id']}\n\n")
                f.write(f"**Categories:** {', '.join(paper['categories'])}\n\n")
                f.write(f"**Estimated Pages:** {paper['estimated_pages']}\n\n")
                f.write(f"**Abstract:** {paper['abstract'][:300]}...\n\n")
                f.write(f"**PDF:** {paper['filename']}\n\n")
                f.write("---\n\n")

        print(f"\n✓ Report generated: {report_file}")


if __name__ == "__main__":
    output_dir = "/Users/tamnguyen/Documents/GitHub/ksi_watch/KSI-IAM-02_25-12A_PasswordlessAuthentication/references/ai_social_engineering"

    researcher = SocialEngineeringResearcher(output_dir)
    researcher.execute_research()
