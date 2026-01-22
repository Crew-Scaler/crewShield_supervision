#!/usr/bin/env python3
"""
Simplified ArXiv paper search for Cluster 6: CSP-Specific Attack Surfaces
"""

import feedparser
import requests
import csv
import os
from datetime import datetime
from typing import List, Dict
import time
import urllib.parse

class ArXivSearcher:
    def __init__(self):
        self.base_url = "http://export.arxiv.org/api/query?"
        self.papers = []

    def search(self, query: str, max_results: int = 50) -> List[Dict]:
        """Search ArXiv for papers matching query"""
        params = {
            'search_query': query,
            'start': 0,
            'max_results': max_results,
            'sortBy': 'submittedDate',
            'sortOrder': 'descending'
        }

        url = self.base_url + urllib.parse.urlencode(params)
        print(f"Searching: {query}")

        try:
            response = requests.get(url, timeout=30)
            response.raise_for_status()
            feed = feedparser.parse(response.content)

            results = []
            for entry in feed.entries:
                paper = {
                    'arxiv_id': entry.id.split('/abs/')[-1],
                    'title': entry.title,
                    'authors': [author.name for author in entry.authors],
                    'published': entry.published,
                    'summary': entry.summary,
                    'pdf_url': entry.id.replace('abs', 'pdf') + '.pdf',
                    'categories': entry.tags[0]['term'] if entry.tags else 'N/A'
                }
                results.append(paper)

            print(f"Found {len(results)} papers\n")
            return results
        except Exception as e:
            print(f"Error searching: {e}\n")
            return []

    def download_pdf(self, paper: Dict, output_dir: str) -> bool:
        """Download PDF from ArXiv"""
        try:
            arxiv_id = paper['arxiv_id']
            filename = f"{arxiv_id.replace('/', '_')}.pdf"
            filepath = os.path.join(output_dir, filename)

            if os.path.exists(filepath):
                print(f"Already downloaded: {filename}")
                return True

            print(f"Downloading: {paper['title'][:60]}...")
            response = requests.get(paper['pdf_url'], timeout=60)
            response.raise_for_status()

            with open(filepath, 'wb') as f:
                f.write(response.content)

            print(f"Saved: {filename}\n")
            return True
        except Exception as e:
            print(f"Error downloading {paper['arxiv_id']}: {e}\n")
            return False

    def is_relevant(self, paper: Dict) -> bool:
        """Check if paper is relevant based on criteria"""
        # Check publication year
        try:
            pub_date = datetime.strptime(paper['published'][:10], '%Y-%m-%d')
            if pub_date.year < 2024:
                return False
        except:
            return False

        # Check for CSP/cloud specific keywords
        title_lower = paper['title'].lower()
        summary_lower = paper['summary'].lower()
        combined = title_lower + " " + summary_lower

        csp_keywords = [
            'cloud', 'api', 'aws', 'azure', 'gcp', 'csp',
            'vector', 'embedding', 'rag', 'retrieval',
            'tenant', 'infrastructure', 'vulnerability',
            'security', 'attack'
        ]

        keyword_matches = sum(1 for kw in csp_keywords if kw in combined)
        return keyword_matches >= 1

    def assign_relevance_score(self, paper: Dict) -> int:
        """Assign relevance score 1-10"""
        score = 5

        title_lower = paper['title'].lower()
        summary_lower = paper['summary'].lower()
        combined = title_lower + " " + summary_lower

        # Bonus for 2025 papers
        pub_date = datetime.strptime(paper['published'][:10], '%Y-%m-%d')
        if pub_date.year == 2025:
            score += 2

        # Bonus for specific keywords
        high_value_keywords = [
            'api security', 'cloud api', 'vector database',
            'rag security', 'cloud attack', 'multi-tenant',
            'aws', 'azure', 'google cloud'
        ]
        for keyword in high_value_keywords:
            if keyword in combined:
                score += 1

        return min(score, 10)

def main():
    output_dir = "/Users/tamnguyen/Documents/GitHub/ksi_watch/KSI-CED-01_25-12A_GeneralTraining/references/cluster_6_csp_attack_surfaces"

    searcher = ArXivSearcher()

    # Simplified search queries
    search_queries = [
        'all:API AND all:security AND submittedDate:[202401010000 TO 202512312359]',
        'all:cloud AND all:vulnerability AND submittedDate:[202401010000 TO 202512312359]',
        'all:vector AND all:database AND submittedDate:[202401010000 TO 202512312359]',
        'all:RAG AND all:security AND submittedDate:[202401010000 TO 202512312359]',
        'all:multi-tenant AND all:cloud AND submittedDate:[202401010000 TO 202512312359]',
        'all:embedding AND all:attack AND submittedDate:[202401010000 TO 202512312359]',
        'all:cloud AND all:infrastructure AND submittedDate:[202401010000 TO 202512312359]'
    ]

    all_papers = []

    # Search for papers
    for query in search_queries:
        results = searcher.search(query, max_results=30)

        for paper in results:
            if searcher.is_relevant(paper):
                paper['relevance_score'] = searcher.assign_relevance_score(paper)
                all_papers.append(paper)

        time.sleep(2)

    # Remove duplicates
    unique_papers = {}
    for paper in all_papers:
        if paper['arxiv_id'] not in unique_papers:
            unique_papers[paper['arxiv_id']] = paper

    all_papers = list(unique_papers.values())

    # Sort by relevance score and publication date
    all_papers.sort(key=lambda x: (-x['relevance_score'], -datetime.strptime(x['published'][:10], '%Y-%m-%d').timestamp()))

    # Cap at 15 papers
    selected_papers = all_papers[:15]

    print(f"\nSelected {len(selected_papers)} papers for download\n")
    print("Papers selected:")
    for i, paper in enumerate(selected_papers, 1):
        print(f"{i}. {paper['title'][:80]} ({paper['published'][:4]}, Score: {paper['relevance_score']})")

    print("\n")

    # Download PDFs
    for i, paper in enumerate(selected_papers, 1):
        print(f"[{i}/{len(selected_papers)}]")
        if searcher.download_pdf(paper, output_dir):
            paper['downloaded'] = True
        else:
            paper['downloaded'] = False
        time.sleep(1)

    # Save metadata
    metadata_file = os.path.join(output_dir, "cluster_6_metadata.csv")
    with open(metadata_file, 'w', newline='', encoding='utf-8') as f:
        fieldnames = [
            'arxiv_id', 'title', 'authors', 'published', 'relevance_score',
            'categories', 'downloaded'
        ]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for paper in selected_papers:
            writer.writerow({
                'arxiv_id': paper['arxiv_id'],
                'title': paper['title'][:120],
                'authors': '; '.join(paper['authors'][:3]),
                'published': paper['published'][:10],
                'relevance_score': paper['relevance_score'],
                'categories': paper['categories'],
                'downloaded': paper.get('downloaded', False)
            })

    print(f"\nMetadata saved to: {metadata_file}")
    print(f"Total papers selected: {len(selected_papers)}")

if __name__ == "__main__":
    main()
