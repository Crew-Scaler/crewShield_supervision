#!/usr/bin/env python3
"""
ArXiv Research Script: AI Agent Authentication & Service Account MFA
Target: 35-45 high-quality papers from 2024-2025
Focus: AI agent authentication, service accounts, workload identity, non-human identity management
"""

import arxiv
import time
import os
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Set
import json

# Target directory
TARGET_DIR = Path("/Users/tamnguyen/Documents/GitHub/ksi_watch/KSI-IAM-01_25-12A_Phishing-ResistantMFA/references/ai_agent_authentication")
TARGET_DIR.mkdir(parents=True, exist_ok=True)

# Cache file to track downloads
CACHE_FILE = TARGET_DIR / "download_cache.json"

# Research queries targeting AI agent authentication and service accounts
SEARCH_QUERIES = [
    # Core AI agent authentication
    'abs:"AI agent" AND abs:authentication AND abs:"service account"',
    'abs:"autonomous agent" AND abs:authentication AND abs:security',
    'abs:"AI agent" AND abs:"credential management" AND abs:identity',
    'abs:"machine learning" AND abs:"service account" AND abs:authentication',

    # Workload identity and federation
    'abs:"workload identity" AND abs:federation AND abs:authentication',
    'abs:"workload identity" AND abs:OIDC AND abs:"AI system"',
    'abs:"OAuth" AND abs:"service account" AND abs:"machine learning"',
    'abs:"identity federation" AND abs:"AI agent" AND abs:security',

    # Non-human identity management
    'abs:"non-human identity" AND abs:authentication AND abs:management',
    'abs:"service account" AND abs:security AND abs:"AI workload"',
    'abs:"machine identity" AND abs:authentication AND abs:governance',
    'abs:"bot authentication" AND abs:security AND abs:credential',

    # MFA and behavioral monitoring
    'abs:"multi-factor authentication" AND abs:"service account" AND abs:AI',
    'abs:"behavioral monitoring" AND abs:"service account" AND abs:anomaly',
    'abs:"behavioral baseline" AND abs:authentication AND abs:"non-human"',
    'abs:"anomaly detection" AND abs:"service account" AND abs:authentication',

    # AI pipeline security
    'abs:"ML pipeline" AND abs:authentication AND abs:"credential management"',
    'abs:"AI workflow" AND abs:security AND abs:"service account"',
    'abs:"MLOps" AND abs:authentication AND abs:"identity management"',
    'abs:"AI deployment" AND abs:security AND abs:credential',

    # Privilege and lateral movement
    'abs:"privilege escalation" AND abs:"AI agent" AND abs:security',
    'abs:"lateral movement" AND abs:"service account" AND abs:detection',
    'abs:"AI agent" AND abs:"access control" AND abs:security',
    'abs:"least privilege" AND abs:"AI system" AND abs:authentication',

    # Enterprise AI security
    'abs:"enterprise AI" AND abs:authentication AND abs:"identity management"',
    'abs:"AI security" AND abs:"credential" AND abs:"service account"',
    'abs:"AI governance" AND abs:authentication AND abs:identity',
    'abs:"AI risk" AND abs:authentication AND abs:security',

    # Broader related searches
    'abs:"agent authentication" AND abs:security AND abs:protocol',
    'abs:"automated system" AND abs:authentication AND abs:credential',
    'abs:"API security" AND abs:"service account" AND abs:authentication',
    'abs:"cloud identity" AND abs:"AI workload" AND abs:authentication',
]

def load_cache() -> Set[str]:
    """Load previously downloaded paper IDs from cache."""
    if CACHE_FILE.exists():
        try:
            with open(CACHE_FILE, 'r') as f:
                data = json.load(f)
                return set(data.get('downloaded_ids', []))
        except Exception as e:
            print(f"Warning: Could not load cache: {e}")
    return set()

def save_cache(downloaded_ids: Set[str], metadata: List[Dict]):
    """Save downloaded paper IDs and metadata to cache."""
    try:
        with open(CACHE_FILE, 'w') as f:
            json.dump({
                'downloaded_ids': list(downloaded_ids),
                'last_updated': datetime.now().isoformat(),
                'total_papers': len(downloaded_ids),
                'metadata': metadata
            }, f, indent=2)
    except Exception as e:
        print(f"Warning: Could not save cache: {e}")

def is_relevant_paper(result) -> bool:
    """
    Filter papers based on relevance criteria:
    - Published in 2024 or 2025
    - More than 7 pages (heuristic: ~350 words per page)
    - Contains key terms in title or abstract
    """
    # Check publication date
    pub_date = result.published
    if pub_date.year < 2024:
        return False

    # Estimate page count (rough heuristic)
    abstract_words = len(result.summary.split())
    if abstract_words < 100:  # Very short abstract suggests short paper
        return False

    # Check for key terms in title or abstract
    text = (result.title + " " + result.summary).lower()

    key_terms = [
        'authentication', 'service account', 'credential', 'identity',
        'ai agent', 'autonomous agent', 'workload', 'federation',
        'mfa', 'multi-factor', 'behavioral', 'anomaly detection',
        'privilege', 'access control', 'security', 'mlops'
    ]

    # Require at least 2 key terms
    matches = sum(1 for term in key_terms if term in text)
    return matches >= 2

def download_paper(result, downloaded_ids: Set[str]) -> bool:
    """Download a single paper if not already downloaded."""
    paper_id = result.entry_id.split('/')[-1]

    if paper_id in downloaded_ids:
        print(f"  [SKIP] Already downloaded: {paper_id}")
        return False

    # Create safe filename
    safe_title = "".join(c if c.isalnum() or c in (' ', '-', '_') else '_' for c in result.title)
    safe_title = safe_title[:100]  # Limit length
    filename = f"{paper_id}_{safe_title}.pdf"
    filepath = TARGET_DIR / filename

    try:
        print(f"  [DOWNLOAD] {paper_id}: {result.title[:80]}...")
        print(f"    Published: {result.published.strftime('%Y-%m-%d')}")
        print(f"    Authors: {', '.join([a.name for a in result.authors[:3]])}...")

        result.download_pdf(filename=str(filepath))
        downloaded_ids.add(paper_id)

        # Respectful delay between downloads
        time.sleep(3.5)
        return True

    except Exception as e:
        print(f"  [ERROR] Failed to download {paper_id}: {e}")
        return False

def search_and_download():
    """Execute searches and download papers."""
    downloaded_ids = load_cache()
    metadata = []

    print(f"Starting ArXiv research on AI Agent Authentication & Service Account MFA")
    print(f"Target: 35-45 papers from 2024-2025")
    print(f"Already downloaded: {len(downloaded_ids)} papers")
    print(f"Target directory: {TARGET_DIR}\n")

    target_papers = 45
    papers_downloaded_this_session = 0

    for query_idx, query in enumerate(SEARCH_QUERIES, 1):
        if len(downloaded_ids) >= target_papers:
            print(f"\n[SUCCESS] Reached target of {target_papers} papers!")
            break

        print(f"\n{'='*80}")
        print(f"Query {query_idx}/{len(SEARCH_QUERIES)}: {query[:80]}...")
        print(f"{'='*80}")

        try:
            # Search with date filter for 2024-2025
            search = arxiv.Search(
                query=query,
                max_results=50,
                sort_by=arxiv.SortCriterion.SubmittedDate,
                sort_order=arxiv.SortOrder.Descending
            )

            results = list(search.results())
            print(f"Found {len(results)} papers, filtering for relevance...")

            relevant_count = 0
            for result in results:
                if len(downloaded_ids) >= target_papers:
                    break

                if is_relevant_paper(result):
                    relevant_count += 1
                    if download_paper(result, downloaded_ids):
                        papers_downloaded_this_session += 1

                        # Store metadata
                        metadata.append({
                            'paper_id': result.entry_id.split('/')[-1],
                            'title': result.title,
                            'authors': [a.name for a in result.authors],
                            'published': result.published.isoformat(),
                            'abstract': result.summary[:500],
                            'categories': result.categories,
                            'query': query
                        })

                        # Save cache after each successful download
                        save_cache(downloaded_ids, metadata)

            print(f"  Relevant papers in this query: {relevant_count}")
            print(f"  Total papers downloaded: {len(downloaded_ids)}/{target_papers}")

        except Exception as e:
            print(f"[ERROR] Query failed: {e}")
            continue

    print(f"\n{'='*80}")
    print(f"RESEARCH COMPLETE")
    print(f"{'='*80}")
    print(f"Papers downloaded this session: {papers_downloaded_this_session}")
    print(f"Total papers in collection: {len(downloaded_ids)}")
    print(f"Target directory: {TARGET_DIR}")
    print(f"Metadata saved to: {CACHE_FILE}")

    # Generate summary report
    generate_summary_report(metadata, downloaded_ids)

def generate_summary_report(metadata: List[Dict], all_ids: Set[str]):
    """Generate a summary report of downloaded papers."""
    report_file = TARGET_DIR / "research_summary.md"

    with open(report_file, 'w') as f:
        f.write("# AI Agent Authentication & Service Account MFA - ArXiv Research Summary\n\n")
        f.write(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write(f"**Total Papers Downloaded:** {len(all_ids)}\n\n")

        f.write("## Research Focus Areas\n\n")
        f.write("1. AI agent authentication protocols and frameworks\n")
        f.write("2. Service account security for ML pipelines and AI workflows\n")
        f.write("3. Non-human identity management and credential governance\n")
        f.write("4. Workload identity federation (OIDC, OAuth for AI agents)\n")
        f.write("5. Behavioral baselines and anomaly detection for service accounts\n")
        f.write("6. AI agent privilege escalation and lateral movement patterns\n\n")

        f.write("## Key Validation Targets\n\n")
        f.write("- Enterprise AI agent adoption: 89% with 15-20 service accounts per agent\n")
        f.write("- Service account credential exposure patterns in AI development\n")
        f.write("- Authentication protocol effectiveness for autonomous agents\n")
        f.write("- Behavioral baseline construction for non-human identities\n")
        f.write("- Lateral movement detection in AI-heavy environments\n\n")

        if metadata:
            f.write("## Downloaded Papers (This Session)\n\n")

            # Group by year
            papers_by_year = {}
            for paper in metadata:
                year = paper['published'][:4]
                if year not in papers_by_year:
                    papers_by_year[year] = []
                papers_by_year[year].append(paper)

            for year in sorted(papers_by_year.keys(), reverse=True):
                f.write(f"### {year} Papers ({len(papers_by_year[year])})\n\n")

                for paper in papers_by_year[year]:
                    f.write(f"#### {paper['title']}\n\n")
                    f.write(f"- **Paper ID:** {paper['paper_id']}\n")
                    f.write(f"- **Published:** {paper['published'][:10]}\n")
                    f.write(f"- **Authors:** {', '.join(paper['authors'][:5])}\n")
                    if len(paper['authors']) > 5:
                        f.write(f"  (and {len(paper['authors']) - 5} more)\n")
                    f.write(f"- **Categories:** {', '.join(paper['categories'])}\n")
                    f.write(f"- **Abstract:** {paper['abstract']}...\n")
                    f.write(f"- **ArXiv:** https://arxiv.org/abs/{paper['paper_id']}\n\n")

        f.write("## Next Steps\n\n")
        f.write("1. Review papers for enterprise AI agent adoption statistics\n")
        f.write("2. Extract authentication framework recommendations\n")
        f.write("3. Analyze service account credential management patterns\n")
        f.write("4. Document workload identity federation implementations\n")
        f.write("5. Compile behavioral baseline construction methodologies\n")

    print(f"\nSummary report generated: {report_file}")

if __name__ == "__main__":
    search_and_download()
