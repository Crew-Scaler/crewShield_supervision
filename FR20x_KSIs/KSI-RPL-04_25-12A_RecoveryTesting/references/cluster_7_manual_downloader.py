#!/usr/bin/env python3
"""
Manual PDF downloader for ArXiv papers - alternative method.
Uses requests library with proper session handling and retries.
"""

import requests
import time
import csv
from pathlib import Path
from typing import List, Dict, Any
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter

OUTPUT_DIR = "/Users/tamnguyen/Documents/GitHub/ksi_watch/KSI-RPL-04_25-12A_RecoveryTesting/references/cluster_7_ransomware_recovery"
CSV_INPUT = "/Users/tamnguyen/Documents/GitHub/ksi_watch/KSI-RPL-04_25-12A_RecoveryTesting/references/cluster_7_metadata.csv"

def create_session_with_retries():
    """Create a requests session with retry strategy."""
    session = requests.Session()

    # Setup retries
    retry_strategy = Retry(
        total=5,
        backoff_factor=2,
        status_forcelist=[403, 429, 500, 502, 503, 504],
        allowed_methods=["GET", "HEAD"]
    )

    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("http://", adapter)
    session.mount("https://", adapter)

    # Set headers
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': 'application/pdf, */*',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1'
    })

    return session

def download_pdf_requests(pdf_url: str, arxiv_id: str, session: requests.Session) -> bool:
    """Download PDF using requests library."""
    filename = Path(OUTPUT_DIR) / f"{arxiv_id.replace('/', '_')}.pdf"

    if filename.exists():
        print(f"  Already exists: {arxiv_id}")
        return True

    try:
        print(f"  Downloading: {arxiv_id}", end=" ", flush=True)

        # Try HTTPS first, then HTTP
        for url in [pdf_url.replace('http://', 'https://'), pdf_url]:
            try:
                response = session.get(url, timeout=60, stream=True)
                response.raise_for_status()

                if response.status_code == 200:
                    with open(filename, 'wb') as f:
                        for chunk in response.iter_content(chunk_size=8192):
                            if chunk:
                                f.write(chunk)

                    print("OK")
                    time.sleep(2)  # Rate limiting
                    return True

            except Exception:
                continue

        print(f"FAILED (All attempts failed)")
        if filename.exists():
            filename.unlink()
        return False

    except Exception as e:
        print(f"FAILED ({type(e).__name__})")
        if filename.exists():
            filename.unlink()
        return False

def main():
    """Download PDFs from metadata CSV."""
    print("=" * 70)
    print("ArXiv PDF Downloader - Alternative Method (requests library)")
    print("=" * 70)

    # Read metadata
    papers = []
    with open(CSV_INPUT, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        papers = list(reader)

    print(f"Found {len(papers)} papers to download\n")

    # Create session with retries
    session = create_session_with_retries()

    downloaded_count = 0
    for i, paper in enumerate(papers, 1):
        print(f"[{i}/{len(papers)}]", end=" ")
        if download_pdf_requests(paper['pdf_url'], paper['arxiv_id'], session):
            downloaded_count += 1

    session.close()

    print(f"\n\nDownload complete: {downloaded_count}/{len(papers)} PDFs downloaded")
    print(f"Output directory: {OUTPUT_DIR}")

if __name__ == '__main__':
    main()
