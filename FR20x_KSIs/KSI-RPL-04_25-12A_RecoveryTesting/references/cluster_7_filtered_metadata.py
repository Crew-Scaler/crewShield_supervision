#!/usr/bin/env python3
"""
Filter and improve metadata for Cluster 7 papers.
Removes non-relevant papers and creates a refined dataset.
"""

import csv
from pathlib import Path

CSV_INPUT = "/Users/tamnguyen/Documents/GitHub/ksi_watch/KSI-RPL-04_25-12A_RecoveryTesting/references/cluster_7_metadata.csv"
CSV_OUTPUT = "/Users/tamnguyen/Documents/GitHub/ksi_watch/KSI-RPL-04_25-12A_RecoveryTesting/references/cluster_7_filtered_metadata.csv"

# Papers that are actually about ransomware recovery, backup integrity, or malware persistence
RELEVANT_ARXIV_IDS = {
    '2511.13517v1': 'Interpretable Ransomware Detection Using Hybrid LLMs',
    '2511.06429v1': 'Inside LockBit: Technical, Behavioral, and Financial Anatomy',
    '2511.01583v1': 'Federated Cyber Defense: Privacy-Preserving Ransomware Detection',
    '2510.21957v1': 'Low-Latency and Adaptive Ransomware Detection Using Contrastive Learning',
    '2510.15133v1': 'Intermittent File Encryption in Ransomware: Measurement, Modeling, Detection',
    '2512.21380v1': 'SENTINEL: Multi-Modal Early Detection Framework for Cyber Threats',
}

def main():
    """Filter papers to keep only ransomware-related ones."""
    with open(CSV_INPUT, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        papers = list(reader)

    # Filter for relevant papers
    filtered = [p for p in papers if p['arxiv_id'] in RELEVANT_ARXIV_IDS]

    print(f"Original papers: {len(papers)}")
    print(f"Filtered papers: {len(filtered)}")
    print(f"Removed: {len(papers) - len(filtered)}")

    # Update titles to be more accurate
    for paper in filtered:
        paper['title'] = RELEVANT_ARXIV_IDS.get(paper['arxiv_id'], paper['title'])
        paper['relevance'] = '9'  # High relevance for all

    # Save filtered metadata
    with open(CSV_OUTPUT, 'w', newline='', encoding='utf-8') as f:
        fieldnames = papers[0].keys()
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(filtered)

    print(f"\nFiltered metadata saved to: {CSV_OUTPUT}")

    # Print details
    print("\nRelevant Papers Found:")
    for i, paper in enumerate(filtered, 1):
        print(f"{i}. {paper['title']}")
        print(f"   ArXiv ID: {paper['arxiv_id']}")
        print(f"   Published: {paper['published'][:10]}")
        print(f"   Pages: {paper['pages']}")
        print()

if __name__ == '__main__':
    main()
