#!/usr/bin/env python3
"""
ArXiv paper search and download for Cluster 6: CSP-Specific Attack Surfaces
"""

import feedparser
import requests
import csv
import os
from datetime import datetime
from typing import List, Dict, Optional
import time
import urllib.parse

class ArXivSearcher:
    def __init__(self, base_url: str = "http://export.arxiv.org/api/query?"):
        self.base_url = base_url
        self.papers = []
        self.downloaded = []

    def search(self, query: str, max_results: int = 50, start_year: int = 2024) -> List[Dict]:
        """Search ArXiv for papers matching query"""
        params = {
            'search_query': f'({query}) AND submittedDate:[{start_year}010100000000 TO 202512312359999]',
            'start': 0,
            'max_results': max_results,
            'sortBy': 'submittedDate',
            'sortOrder': 'descending'
        }

        url = self.base_url + urllib.parse.urlencode(params)
        print(f"Searching: {query}")
        print(f"URL: {url}\n")

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

    def extract_page_count(self, pdf_path: str) -> int:
        """Extract page count from PDF"""
        try:
            import PyPDF2
            with open(pdf_path, 'rb') as f:
                reader = PyPDF2.PdfReader(f)
                return len(reader.pages)
        except:
            # If PyPDF2 not available, try pdfplumber
            try:
                import pdfplumber
                with pdfplumber.open(pdf_path) as pdf:
                    return len(pdf.pages)
            except:
                return 0

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

    def is_relevant(self, paper: Dict, min_pages: int = 7) -> bool:
        """Check if paper is relevant based on criteria"""
        # Check publication year
        pub_date = datetime.strptime(paper['published'][:10], '%Y-%m-%d')
        if pub_date.year < 2024:
            return False

        # Check for CSP/cloud specific keywords
        title_lower = paper['title'].lower()
        summary_lower = paper['summary'].lower()
        combined = title_lower + " " + summary_lower

        csp_keywords = [
            'cloud', 'api', 'aws', 'azure', 'gcp', 'csp',
            'vector database', 'embedding', 'rag', 'retrieval',
            'multi-tenant', 'infrastructure', 'attack surface',
            'vulnerability', 'security', 'breach', 'threat'
        ]

        keyword_matches = sum(1 for kw in csp_keywords if kw in combined)
        return keyword_matches >= 2  # At least 2 relevant keywords

    def assign_relevance_score(self, paper: Dict, query_terms: List[str]) -> int:
        """Assign relevance score 1-10"""
        score = 5  # Base score

        title_lower = paper['title'].lower()
        summary_lower = paper['summary'].lower()
        combined = title_lower + " " + summary_lower

        # Bonus for 2025 papers
        pub_date = datetime.strptime(paper['published'][:10], '%Y-%m-%d')
        if pub_date.year == 2025:
            score += 1

        # Bonus for exact phrase matches
        for query_term in query_terms:
            if query_term.lower() in combined:
                score += 1

        # Bonus for AWS/Google/Azure affiliation
        authors_str = " ".join(paper.get('authors', []))
        if any(org in authors_str for org in ['AWS', 'Google', 'Azure', 'Microsoft']):
            score += 2

        return min(score, 10)

def main():
    output_dir = "/Users/tamnguyen/Documents/GitHub/ksi_watch/KSI-CED-01_25-12A_GeneralTraining/references/cluster_6_csp_attack_surfaces"

    searcher = ArXivSearcher()

    # Search queries for Cluster 6
    search_queries = [
        ('cat:cs.CR AND ("API security" OR "cloud API" OR "API attack")',
         ['API security', 'cloud API', 'attack']),
        ('cat:cs.CR AND ("vector database" OR "embedding database" OR "embedding security")',
         ['vector database', 'embedding', 'security']),
        ('cat:cs.CR AND ("RAG" OR "retrieval augmented generation" OR "LLM security")',
         ['RAG', 'retrieval', 'generation']),
        ('cat:cs.CR AND ("cloud infrastructure" OR "CSP attack" OR "cloud attack")',
         ['cloud', 'infrastructure', 'attack']),
        ('cat:cs.CR AND ("multi-tenant" OR "cloud isolation" OR "tenant isolation")',
         ['multi-tenant', 'cloud', 'isolation'])
    ]

    all_papers = []

    # Search for papers
    for query, query_terms in search_queries:
        results = searcher.search(query, max_results=50)

        for paper in results:
            if searcher.is_relevant(paper):
                paper['query_terms'] = query_terms
                paper['relevance_score'] = searcher.assign_relevance_score(paper, query_terms)
                all_papers.append(paper)

        time.sleep(2)  # Be respectful to ArXiv API

    # Remove duplicates
    unique_papers = {}
    for paper in all_papers:
        if paper['arxiv_id'] not in unique_papers:
            unique_papers[paper['arxiv_id']] = paper

    all_papers = list(unique_papers.values())

    # Sort by relevance score and publication date
    all_papers.sort(key=lambda x: (-x['relevance_score'], x['published']), reverse=True)

    # Cap at 15 papers
    selected_papers = all_papers[:15]

    print(f"\nSelected {len(selected_papers)} papers for download\n")

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
                'title': paper['title'][:100],
                'authors': '; '.join(paper['authors'][:3]),
                'published': paper['published'][:10],
                'relevance_score': paper['relevance_score'],
                'categories': paper['categories'],
                'downloaded': paper.get('downloaded', False)
            })

    print(f"\nMetadata saved to: {metadata_file}")
    print(f"Total papers: {len(selected_papers)}")

if __name__ == "__main__":
    main()
