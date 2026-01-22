#!/usr/bin/env python3
"""
Expanded ArXiv Research: AI Agent Authentication & Service Account MFA
Target: Additional 15-25 papers to reach 35-45 total
Focus: Broader searches on related topics
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
CACHE_FILE = TARGET_DIR / "download_cache.json"

# Expanded research queries with broader scope
EXPANDED_QUERIES = [
    # Agent security and identity
    'abs:"agent" AND abs:"identity" AND abs:security AND abs:authentication',
    'abs:"multi-agent" AND abs:security AND abs:authentication',
    'abs:"agent system" AND abs:"access control" AND abs:security',
    'abs:"autonomous system" AND abs:security AND abs:identity',

    # API and service authentication
    'abs:"API authentication" AND abs:security AND abs:identity',
    'abs:"REST API" AND abs:authentication AND abs:"access control"',
    'abs:"microservice" AND abs:authentication AND abs:security',
    'abs:"service mesh" AND abs:security AND abs:authentication',

    # Cloud and distributed security
    'abs:"cloud security" AND abs:authentication AND abs:identity',
    'abs:"distributed system" AND abs:authentication AND abs:security',
    'abs:"container security" AND abs:authentication AND abs:identity',
    'abs:"Kubernetes" AND abs:security AND abs:authentication',

    # ML/AI security broader
    'abs:"machine learning security" AND abs:authentication',
    'abs:"AI security" AND abs:"identity" AND abs:authentication',
    'abs:"neural network" AND abs:security AND abs:authentication',
    'abs:"deep learning" AND abs:security AND abs:authentication',

    # Credential and secret management
    'abs:"credential" AND abs:"secret management" AND abs:security',
    'abs:"key management" AND abs:authentication AND abs:security',
    'abs:"secret" AND abs:security AND abs:"access control"',
    'abs:"password" AND abs:security AND abs:authentication AND abs:AI',

    # Zero trust and policy
    'abs:"zero trust" AND abs:authentication AND abs:security',
    'abs:"policy enforcement" AND abs:authentication AND abs:security',
    'abs:"attribute-based" AND abs:"access control" AND abs:security',
    'abs:"role-based" AND abs:"access control" AND abs:authentication',

    # Behavioral and anomaly
    'abs:"behavioral analysis" AND abs:authentication AND abs:security',
    'abs:"anomaly detection" AND abs:authentication AND abs:security',
    'abs:"user behavior" AND abs:authentication AND abs:security',
    'abs:"continuous authentication" AND abs:security',

    # Federated and decentralized
    'abs:"federated" AND abs:authentication AND abs:security',
    'abs:"decentralized" AND abs:authentication AND abs:security',
    'abs:"blockchain" AND abs:authentication AND abs:identity',
    'abs:"distributed ledger" AND abs:authentication AND abs:security',

    # Enterprise and deployment
    'abs:"enterprise security" AND abs:authentication AND abs:identity',
    'abs:"security architecture" AND abs:authentication AND abs:identity',
    'abs:"security framework" AND abs:authentication AND abs:identity',
    'abs:"security implementation" AND abs:authentication',

    # Specific protocols and standards
    'abs:"OIDC" AND abs:authentication AND abs:security',
    'abs:"OAuth2" AND abs:security AND abs:authentication',
    'abs:"SAML" AND abs:authentication AND abs:security',
    'abs:"JWT" AND abs:authentication AND abs:security',

    # Threat and attack vectors
    'abs:"privilege escalation" AND abs:authentication AND abs:security',
    'abs:"credential theft" AND abs:security AND abs:detection',
    'abs:"identity compromise" AND abs:security AND abs:detection',
    'abs:"authentication bypass" AND abs:security',

    # Bot and automation security
    'abs:"bot" AND abs:authentication AND abs:security',
    'abs:"automation" AND abs:security AND abs:authentication',
    'abs:"robotic process" AND abs:security AND abs:authentication',
    'abs:"automated workflow" AND abs:security AND abs:authentication',
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
    """Filter papers for relevance."""
    pub_date = result.published
    if pub_date.year < 2024:
        return False

    abstract_words = len(result.summary.split())
    if abstract_words < 100:
        return False

    text = (result.title + " " + result.summary).lower()

    # Broader key terms
    key_terms = [
        'authentication', 'identity', 'credential', 'security',
        'agent', 'service', 'access control', 'authorization',
        'ai', 'machine learning', 'autonomous', 'workload'
    ]

    matches = sum(1 for term in key_terms if term in text)
    return matches >= 2

def download_paper(result, downloaded_ids: Set[str]) -> bool:
    """Download a single paper if not already downloaded."""
    paper_id = result.entry_id.split('/')[-1]

    if paper_id in downloaded_ids:
        print(f"  [SKIP] Already downloaded: {paper_id}")
        return False

    safe_title = "".join(c if c.isalnum() or c in (' ', '-', '_') else '_' for c in result.title)
    safe_title = safe_title[:100]
    filename = f"{paper_id}_{safe_title}.pdf"
    filepath = TARGET_DIR / filename

    try:
        print(f"  [DOWNLOAD] {paper_id}: {result.title[:80]}...")
        print(f"    Published: {result.published.strftime('%Y-%m-%d')}")
        print(f"    Authors: {', '.join([a.name for a in result.authors[:3]])}...")

        result.download_pdf(filename=str(filepath))
        downloaded_ids.add(paper_id)
        time.sleep(3.5)
        return True

    except Exception as e:
        print(f"  [ERROR] Failed to download {paper_id}: {e}")
        return False

def search_and_download():
    """Execute expanded searches and download papers."""
    downloaded_ids = load_cache()

    # Load existing metadata
    metadata = []
    if CACHE_FILE.exists():
        try:
            with open(CACHE_FILE, 'r') as f:
                data = json.load(f)
                metadata = data.get('metadata', [])
        except:
            pass

    print(f"Expanded ArXiv research on AI Agent Authentication & Service Account MFA")
    print(f"Current collection: {len(downloaded_ids)} papers")
    print(f"Target: 35-45 papers total")
    print(f"Target directory: {TARGET_DIR}\n")

    target_papers = 45
    papers_downloaded_this_session = 0

    for query_idx, query in enumerate(EXPANDED_QUERIES, 1):
        if len(downloaded_ids) >= target_papers:
            print(f"\n[SUCCESS] Reached target of {target_papers} papers!")
            break

        print(f"\n{'='*80}")
        print(f"Query {query_idx}/{len(EXPANDED_QUERIES)}: {query[:80]}...")
        print(f"{'='*80}")

        try:
            search = arxiv.Search(
                query=query,
                max_results=30,
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

                        metadata.append({
                            'paper_id': result.entry_id.split('/')[-1],
                            'title': result.title,
                            'authors': [a.name for a in result.authors],
                            'published': result.published.isoformat(),
                            'abstract': result.summary[:500],
                            'categories': result.categories,
                            'query': query
                        })

                        save_cache(downloaded_ids, metadata)

            print(f"  Relevant papers in this query: {relevant_count}")
            print(f"  Total papers downloaded: {len(downloaded_ids)}/{target_papers}")

        except Exception as e:
            print(f"[ERROR] Query failed: {e}")
            continue

    print(f"\n{'='*80}")
    print(f"EXPANDED SEARCH COMPLETE")
    print(f"{'='*80}")
    print(f"Papers downloaded this session: {papers_downloaded_this_session}")
    print(f"Total papers in collection: {len(downloaded_ids)}")
    print(f"Target directory: {TARGET_DIR}")

if __name__ == "__main__":
    search_and_download()
