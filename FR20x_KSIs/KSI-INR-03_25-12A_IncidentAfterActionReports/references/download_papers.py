#!/usr/bin/env python3
"""
Download ArXiv papers for Topic 8: Automated Cloud Remediation & Governance
"""

import json
import time
import requests
from pathlib import Path
from PyPDF2 import PdfReader
import re

def sanitize_filename(title, max_length=50):
    """Create a safe filename from title"""
    # Remove special characters
    safe_title = re.sub(r'[^\w\s-]', '', title)
    # Replace spaces with underscores
    safe_title = re.sub(r'[\s]+', '_', safe_title)
    # Truncate if too long
    if len(safe_title) > max_length:
        safe_title = safe_title[:max_length]
    return safe_title

def download_pdf(url, output_path):
    """Download PDF from URL"""
    print(f"  Downloading: {url}")
    response = requests.get(url, timeout=30)
    response.raise_for_status()

    with open(output_path, 'wb') as f:
        f.write(response.content)

    print(f"  Saved to: {output_path}")
    return True

def verify_pdf(pdf_path, min_pages=7):
    """Verify PDF is readable and has minimum pages"""
    try:
        reader = PdfReader(pdf_path)
        num_pages = len(reader.pages)
        print(f"  Verified: {num_pages} pages")

        if num_pages < min_pages:
            print(f"  WARNING: Only {num_pages} pages (minimum is {min_pages})")
            return False, num_pages

        return True, num_pages
    except Exception as e:
        print(f"  ERROR: Could not read PDF: {e}")
        return False, 0

def main():
    """Download all papers from topic8_papers.json"""
    # Load papers list
    papers_file = Path(__file__).parent / 'topic8_papers.json'
    with open(papers_file, 'r') as f:
        papers = json.load(f)

    print(f"[START] Downloading {len(papers)} papers...\n")

    output_dir = Path(__file__).parent
    download_results = []

    for i, paper in enumerate(papers, 1):
        print(f"[{i}/{len(papers)}] {paper['title']}")
        print(f"  ArXiv ID: {paper['arxiv_id']}")
        print(f"  Authors: {', '.join(paper['authors'][:3])}{'...' if len(paper['authors']) > 3 else ''}")
        print(f"  Published: {paper['published']}")

        # Create filename
        arxiv_id = paper['arxiv_id'].replace('v', '_v')  # 2501.06706v1 -> 2501.06706_v1
        safe_title = sanitize_filename(paper['title'], max_length=60)
        filename = f"{arxiv_id}_{safe_title}.pdf"
        output_path = output_dir / filename

        # Download
        try:
            success = download_pdf(paper['pdf_url'], output_path)
            if success:
                time.sleep(3)  # Respect ArXiv rate limits

                # Verify
                is_valid, num_pages = verify_pdf(output_path)

                download_results.append({
                    'arxiv_id': paper['arxiv_id'],
                    'title': paper['title'],
                    'filename': filename,
                    'pages': num_pages,
                    'valid': is_valid,
                    'published': paper['published'],
                    'authors': paper['authors'],
                    'summary': paper['summary'],
                    'categories': paper['categories']
                })
        except Exception as e:
            print(f"  ERROR: Failed to download: {e}")
            download_results.append({
                'arxiv_id': paper['arxiv_id'],
                'title': paper['title'],
                'filename': filename,
                'pages': 0,
                'valid': False,
                'error': str(e),
                'published': paper['published'],
                'authors': paper['authors'],
                'summary': paper['summary'],
                'categories': paper['categories']
            })

        print()

    # Save download results
    results_file = output_dir / 'download_results.json'
    with open(results_file, 'w') as f:
        json.dump(download_results, f, indent=2)

    print(f"[COMPLETE] Downloaded {len([r for r in download_results if r['valid']])} valid papers")
    print(f"[SAVED] Results saved to {results_file}")

    return download_results

if __name__ == '__main__':
    results = main()
