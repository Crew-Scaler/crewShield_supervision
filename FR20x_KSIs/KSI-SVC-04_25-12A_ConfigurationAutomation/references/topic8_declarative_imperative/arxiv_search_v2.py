#!/usr/bin/env python3
"""
ArXiv Research Script for Issue #69 Topic 8 (Expanded Search):
Declarative-Imperative Convergence in Agent-Driven Configuration

Broader search queries to find 50-100 papers.
"""

import json
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Dict, List
from datetime import datetime
import re


class ArXivSearcher:
    """ArXiv search and download manager with rate limiting."""

    BASE_URL = "http://export.arxiv.org/api/query?"
    RATE_LIMIT_DELAY = 3.5  # seconds between requests

    def __init__(self, output_dir: str, archive_dir: str):
        self.output_dir = Path(output_dir)
        self.archive_dir = Path(archive_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.archive_dir.mkdir(parents=True, exist_ok=True)
        self.last_request_time = 0

    def rate_limit(self):
        """Enforce rate limiting between requests."""
        current_time = time.time()
        time_since_last = current_time - self.last_request_time
        if time_since_last < self.RATE_LIMIT_DELAY:
            time.sleep(self.RATE_LIMIT_DELAY - time_since_last)
        self.last_request_time = time.time()

    def search_arxiv(
        self, query: str, max_results: int = 100
    ) -> List[Dict]:
        """Search ArXiv and return paper metadata."""
        self.rate_limit()

        params = {
            'search_query': query,
            'start': 0,
            'max_results': max_results,
            'sortBy': 'submittedDate',
            'sortOrder': 'descending'
        }

        url = self.BASE_URL + urllib.parse.urlencode(params)
        print(f"Searching: {query[:120]}...")

        try:
            with urllib.request.urlopen(url, timeout=30) as response:
                data = response.read()
        except Exception as e:
            print(f"Error fetching results: {e}")
            return []

        # Parse XML response
        root = ET.fromstring(data)
        ns = {'atom': 'http://www.w3.org/2005/Atom'}

        papers = []
        for entry in root.findall('atom:entry', ns):
            paper = self._parse_entry(entry, ns)
            if paper:
                papers.append(paper)

        print(f"Found {len(papers)} papers")
        return papers

    def _parse_entry(self, entry, ns) -> Dict:
        """Parse individual ArXiv entry."""
        try:
            title = entry.find('atom:title', ns).text.strip()
            title = re.sub(r'\s+', ' ', title)

            summary = entry.find('atom:summary', ns).text.strip()
            summary = re.sub(r'\s+', ' ', summary)

            # Get authors
            authors = []
            for author in entry.findall('atom:author', ns):
                name = author.find('atom:name', ns)
                if name is not None:
                    authors.append(name.text.strip())

            # Get ArXiv ID and PDF link
            arxiv_id = entry.find('atom:id', ns).text.split('/')[-1]
            pdf_url = f"http://arxiv.org/pdf/{arxiv_id}.pdf"

            # Get publication date
            published = entry.find('atom:published', ns).text
            pub_year = published[:4]

            # Get categories
            categories = []
            for cat in entry.findall('atom:category', ns):
                term = cat.get('term')
                if term:
                    categories.append(term)

            # Get primary category
            primary_cat = entry.find('atom:primary_category', ns)
            primary_category = primary_cat.get('term') if primary_cat is not None else ''

            return {
                'arxiv_id': arxiv_id,
                'title': title,
                'authors': authors,
                'summary': summary,
                'published': published,
                'year': pub_year,
                'categories': categories,
                'primary_category': primary_category,
                'pdf_url': pdf_url,
                'relevance_score': 0.0
            }
        except Exception as e:
            print(f"Error parsing entry: {e}")
            return None

    def calculate_relevance(self, paper: Dict) -> float:
        """
        Calculate relevance score based on keywords and criteria.
        Priority: 2025 > 2024, US institutions, relevant keywords.
        """
        score = 0.0
        text = (paper['title'] + ' ' + paper['summary']).lower()

        # Year priority (most important)
        year = int(paper['year'])
        if year == 2025:
            score += 50.0
        elif year == 2024:
            score += 30.0
        elif year == 2023:
            score += 10.0
        elif year >= 2020:
            score += 5.0

        # Core concept keywords (high weight)
        core_keywords = {
            'declarative configuration': 20.0,
            'imperative workflow': 20.0,
            'declarative programming': 15.0,
            'imperative programming': 12.0,
            'idempotence': 18.0,
            'idempotent': 15.0,
            'agent-driven': 18.0,
            'autonomous agent': 15.0,
            'autonomous system': 12.0,
            'configuration management': 12.0,
            'orchestration': 10.0,
            'infrastructure as code': 15.0,
            'iac': 12.0,
        }

        for keyword, weight in core_keywords.items():
            if keyword in text:
                score += weight

        # Supporting keywords (medium weight)
        support_keywords = {
            'declarative': 5.0,
            'imperative': 5.0,
            'convergence': 8.0,
            'autonomous': 6.0,
            'policy-driven': 7.0,
            'state management': 7.0,
            'desired state': 8.0,
            'configuration drift': 8.0,
            'workflow automation': 6.0,
            'self-healing': 7.0,
            'self-managing': 7.0,
            'automated configuration': 7.0,
            'configuration automation': 7.0,
        }

        for keyword, weight in support_keywords.items():
            if keyword in text:
                score += weight

        # Related technologies (low weight)
        tech_keywords = {
            'kubernetes': 4.0,
            'ansible': 4.0,
            'terraform': 4.0,
            'puppet': 4.0,
            'chef': 4.0,
            'saltstack': 4.0,
            'gitops': 5.0,
            'devops': 3.0,
            'cloud native': 4.0,
            'containerization': 3.0,
        }

        for keyword, weight in tech_keywords.items():
            if keyword in text:
                score += weight

        # Agent/AI keywords
        agent_keywords = {
            'multi-agent': 7.0,
            'agent system': 6.0,
            'intelligent agent': 6.0,
            'software agent': 5.0,
            'agent-based': 5.0,
            'agentic': 8.0,
        }

        for keyword, weight in agent_keywords.items():
            if keyword in text:
                score += weight

        # Configuration/management keywords
        config_keywords = {
            'configuration': 3.0,
            'provisioning': 4.0,
            'deployment automation': 5.0,
            'system configuration': 5.0,
            'automated deployment': 4.0,
        }

        for keyword, weight in config_keywords.items():
            if keyword in text:
                score += weight

        # US institution bonus
        us_indicators = ['.edu', 'university', 'stanford', 'mit', 'berkeley',
                        'carnegie mellon', 'caltech', 'princeton', 'harvard',
                        'cornell', 'columbia', 'yale', 'georgia tech',
                        'university of', 'institute of technology']
        authors_text = ' '.join(paper['authors']).lower()
        for indicator in us_indicators:
            if indicator in authors_text or indicator in text:
                score += 5.0
                break

        # Computer Science category bonus
        cs_categories = ['cs.AI', 'cs.DC', 'cs.SE', 'cs.SY', 'cs.MA', 'cs.NI', 'cs.OS']
        for cat in cs_categories:
            if cat in paper['categories'] or cat == paper['primary_category']:
                score += 4.0
                break

        return round(score, 2)

    def download_pdf(self, paper: Dict, filepath: Path) -> bool:
        """Download PDF with rate limiting."""
        self.rate_limit()

        print(f"Downloading: {paper['title'][:80]}...")

        try:
            urllib.request.urlretrieve(paper['pdf_url'], filepath)
            print(f"  Saved to: {filepath.name}")
            return True
        except Exception as e:
            print(f"  Error downloading {paper['arxiv_id']}: {e}")
            return False

    def save_metadata(self, papers: List[Dict], filepath: Path):
        """Save paper metadata to JSON."""
        metadata = {
            'search_date': datetime.now().isoformat(),
            'total_papers': len(papers),
            'papers': papers
        }

        with open(filepath, 'w') as f:
            json.dump(metadata, f, indent=2)

        print(f"Metadata saved to: {filepath}")


def main():
    """Main execution function."""
    print("="*80)
    print("ArXiv Research: Declarative-Imperative Convergence (Issue #69 Topic 8)")
    print("EXPANDED SEARCH v2")
    print("="*80)

    output_dir = "/Users/tamnguyen/Documents/GitHub/ksi_watch/KSI-SVC-04_25-12A_ConfigurationAutomation/references/topic8_declarative_imperative"
    archive_dir = f"{output_dir}/_archived_low_relevance"

    searcher = ArXivSearcher(output_dir, archive_dir)

    # Broader search queries focused on individual concepts
    queries = [
        # Configuration management + agents
        'cat:cs.* AND (abs:"configuration management" OR abs:"infrastructure as code")',
        'cat:cs.* AND (abs:declarative OR abs:"declarative programming") AND submittedDate:[20230101 TO 20260101]',
        'cat:cs.* AND abs:idempotent AND submittedDate:[20230101 TO 20260101]',
        'cat:cs.* AND (abs:"autonomous agent" OR abs:"agent-driven" OR abs:"multi-agent")',
        'cat:cs.* AND abs:orchestration AND (abs:automation OR abs:autonomous)',
        'cat:cs.* AND abs:kubernetes AND (abs:configuration OR abs:automation)',
        'cat:cs.* AND (abs:ansible OR abs:terraform OR abs:puppet) AND submittedDate:[20230101 TO 20260101]',
        'cat:cs.* AND abs:"desired state" AND submittedDate:[20230101 TO 20260101]',
        'cat:cs.* AND abs:"policy-driven" AND (abs:configuration OR abs:automation)',
        'cat:cs.SE AND (abs:"workflow automation" OR abs:"automated deployment")',
        'cat:cs.* AND abs:gitops AND submittedDate:[20230101 TO 20260101]',
        'cat:cs.* AND abs:"self-healing" AND (abs:system OR abs:infrastructure)',
        'cat:cs.* AND (abs:"configuration drift" OR abs:"state management")',
        'cat:cs.AI AND abs:"agent system" AND submittedDate:[20230101 TO 20260101]',
        'cat:cs.* AND abs:imperative AND abs:declarative AND submittedDate:[20230101 TO 20260101]',
    ]

    # Collect all papers
    all_papers = []
    seen_ids = set()

    for i, query in enumerate(queries, 1):
        print(f"\n{'='*80}")
        print(f"Query {i}/{len(queries)}")
        print(f"{'='*80}")

        papers = searcher.search_arxiv(query, max_results=30)

        # Deduplicate
        for paper in papers:
            if paper['arxiv_id'] not in seen_ids:
                seen_ids.add(paper['arxiv_id'])
                all_papers.append(paper)

        print(f"Total unique papers so far: {len(all_papers)}")

        # Break if we have enough papers
        if len(all_papers) >= 100:
            print(f"\nReached target of 100+ papers, stopping search.")
            break

    print(f"\n{'='*80}")
    print(f"TOTAL UNIQUE PAPERS FOUND: {len(all_papers)}")
    print(f"{'='*80}")

    # Calculate relevance scores
    print("\nCalculating relevance scores...")
    for paper in all_papers:
        paper['relevance_score'] = searcher.calculate_relevance(paper)

    # Sort by relevance
    all_papers.sort(key=lambda x: x['relevance_score'], reverse=True)

    # Display top papers
    print("\n" + "="*80)
    print("TOP 10 PAPERS (to be downloaded)")
    print("="*80)

    for i, paper in enumerate(all_papers[:10], 1):
        print(f"\n{i}. [{paper['year']}] {paper['title']}")
        print(f"   Authors: {', '.join(paper['authors'][:3])}")
        if len(paper['authors']) > 3:
            print(f"            + {len(paper['authors']) - 3} more")
        print(f"   ArXiv ID: {paper['arxiv_id']}")
        print(f"   Relevance Score: {paper['relevance_score']}")
        print(f"   Categories: {', '.join(paper['categories'][:5])}")

    # Download top 10 papers
    print("\n" + "="*80)
    print("DOWNLOADING TOP 10 PAPERS")
    print("="*80)

    downloaded_count = 0
    for i, paper in enumerate(all_papers[:10], 1):
        filename = f"{i:02d}_{paper['arxiv_id'].replace('/', '_')}.pdf"
        filepath = Path(output_dir) / filename

        if searcher.download_pdf(paper, filepath):
            downloaded_count += 1
            paper['downloaded'] = True
            paper['download_path'] = str(filepath)
        else:
            paper['downloaded'] = False

    # Save metadata for top 10
    metadata_path = Path(output_dir) / "metadata.json"
    searcher.save_metadata(all_papers[:10], metadata_path)

    # Archive papers 11+
    if len(all_papers) > 10:
        print("\n" + "="*80)
        print(f"ARCHIVING PAPERS 11-{len(all_papers)}")
        print("="*80)

        archived_papers = all_papers[10:]
        archive_metadata_path = Path(archive_dir) / "archived_metadata.json"

        # Save archived metadata
        archive_data = {
            'search_date': datetime.now().isoformat(),
            'total_archived': len(archived_papers),
            'papers': archived_papers
        }

        with open(archive_metadata_path, 'w') as f:
            json.dump(archive_data, f, indent=2)

        print(f"Archived {len(archived_papers)} papers to metadata")
        print(f"Archive location: {archive_metadata_path}")

    # Generate summary report
    print("\n" + "="*80)
    print("SUMMARY REPORT")
    print("="*80)
    print(f"Total papers found: {len(all_papers)}")
    print(f"Papers downloaded (Top 10): {downloaded_count}")
    print(f"Papers archived (11+): {len(all_papers) - 10 if len(all_papers) > 10 else 0}")
    print(f"\nOutput directory: {output_dir}")
    print(f"Archive directory: {archive_dir}")

    # Key findings
    print("\n" + "="*80)
    print("KEY FINDINGS")
    print("="*80)

    year_dist = {}
    for paper in all_papers[:10]:
        year = paper['year']
        year_dist[year] = year_dist.get(year, 0) + 1

    print("\nYear distribution (Top 10):")
    for year in sorted(year_dist.keys(), reverse=True):
        print(f"  {year}: {year_dist[year]} papers")

    print("\nTop keywords in titles:")
    title_words = {}
    for paper in all_papers[:10]:
        words = paper['title'].lower().split()
        for word in words:
            word = word.strip(',:;.()[]{}')
            if len(word) > 4:
                title_words[word] = title_words.get(word, 0) + 1

    top_words = sorted(title_words.items(), key=lambda x: x[1], reverse=True)[:10]
    for word, count in top_words:
        print(f"  {word}: {count}")

    # Category distribution
    print("\nTop categories (Top 10):")
    cat_dist = {}
    for paper in all_papers[:10]:
        for cat in paper['categories']:
            cat_dist[cat] = cat_dist.get(cat, 0) + 1

    top_cats = sorted(cat_dist.items(), key=lambda x: x[1], reverse=True)[:10]
    for cat, count in top_cats:
        print(f"  {cat}: {count}")

    print("\n" + "="*80)
    print("RESEARCH COMPLETE")
    print("="*80)


if __name__ == "__main__":
    main()
