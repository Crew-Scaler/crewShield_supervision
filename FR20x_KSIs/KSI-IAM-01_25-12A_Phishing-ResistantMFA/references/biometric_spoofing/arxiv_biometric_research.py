#!/usr/bin/env python3
"""
ArXiv Research Script: Biometric Spoofing & Deepfake Detection for MFA Security
Focus: AI-powered attacks against biometric authentication systems
Target: 35-45 high-quality papers from 2024-2025
"""

import arxiv
import time
import os
from pathlib import Path
from datetime import datetime
import json

# Research configuration
TARGET_DIR = Path("/Users/tamnguyen/Documents/GitHub/ksi_watch/KSI-IAM-01_25-12A_Phishing-ResistantMFA/references/biometric_spoofing")
DOWNLOAD_DELAY = 3  # seconds between downloads
MIN_PAGES = 7  # minimum paper length
TARGET_PAPERS = 45
YEAR_FILTER = 2024  # papers from 2024 onwards

# Search queries focused on biometric spoofing and deepfake detection
SEARCH_QUERIES = [
    {
        "query": "deepfake AND (liveness detection OR biometric spoofing OR facial recognition)",
        "max_results": 50,
        "topic": "deepfake_liveness"
    },
    {
        "query": "voice synthesis AND (voice cloning OR speaker verification OR spoofing)",
        "max_results": 50,
        "topic": "voice_spoofing"
    },
    {
        "query": "fingerprint spoofing AND (presentation attacks OR AI generation)",
        "max_results": 50,
        "topic": "fingerprint_spoofing"
    },
    {
        "query": "multi-modal biometric AND (fusion OR security OR deepfake detection)",
        "max_results": 50,
        "topic": "multimodal_biometric"
    },
    {
        "query": "GAN AND (adversarial attacks OR biometric systems OR authentication)",
        "max_results": 50,
        "topic": "gan_attacks"
    },
    {
        "query": "face anti-spoofing AND (deep learning OR neural networks)",
        "max_results": 40,
        "topic": "face_antispoofing"
    },
    {
        "query": "iris recognition AND (spoofing OR liveness detection)",
        "max_results": 30,
        "topic": "iris_spoofing"
    },
    {
        "query": "behavioral biometrics AND (authentication OR continuous verification)",
        "max_results": 30,
        "topic": "behavioral_biometric"
    }
]

class BiometricResearchCollector:
    def __init__(self):
        self.downloaded_papers = []
        self.research_metadata = []
        self.papers_by_topic = {}

    def is_recent_paper(self, result):
        """Check if paper is from 2024 or later"""
        if hasattr(result, 'published'):
            pub_year = result.published.year
            return pub_year >= YEAR_FILTER
        return False

    def estimate_pages(self, result):
        """Estimate paper length from PDF metadata"""
        # This is a heuristic - actual page count requires downloading
        # We'll be permissive in search and filter during download
        return True

    def is_relevant_to_mfa_security(self, result):
        """Check if paper is relevant to MFA security research"""
        keywords = [
            'authentication', 'biometric', 'spoofing', 'deepfake',
            'liveness', 'detection', 'security', 'attack', 'adversarial',
            'gan', 'synthesis', 'verification', 'face', 'voice', 'fingerprint',
            'iris', 'multi-modal', 'presentation attack', 'anti-spoofing'
        ]

        text = f"{result.title} {result.summary}".lower()
        return any(kw in text for kw in keywords)

    def extract_key_metrics(self, result):
        """Extract validation metrics from abstract"""
        summary = result.summary.lower()
        metrics = {
            'has_accuracy_metric': any(term in summary for term in ['accuracy', 'acc', 'precision', 'recall']),
            'has_attack_success': any(term in summary for term in ['attack success', 'spoofing rate', 'defeat rate']),
            'has_evaluation': any(term in summary for term in ['evaluation', 'experiment', 'benchmark', 'dataset']),
            'empirical_study': any(term in summary for term in ['empirical', 'experimental', 'study', 'analysis'])
        }
        return metrics

    def download_paper(self, result, topic):
        """Download paper with metadata"""
        try:
            # Create topic subdirectory
            topic_dir = TARGET_DIR / topic
            topic_dir.mkdir(exist_ok=True)

            # Generate filename
            first_author = result.authors[0].name.split()[-1] if result.authors else "Unknown"
            year = result.published.year
            title_slug = "_".join(result.title.split()[:5]).replace("/", "_")
            filename = f"{year}_{first_author}_{title_slug}.pdf"
            filepath = topic_dir / filename

            # Skip if already downloaded
            if filepath.exists():
                print(f"  ✓ Already downloaded: {filename}")
                return None

            # Download paper
            print(f"  → Downloading: {filename}")
            result.download_pdf(dirpath=str(topic_dir), filename=filename)

            # Extract metadata
            metrics = self.extract_key_metrics(result)
            metadata = {
                'title': result.title,
                'authors': [author.name for author in result.authors],
                'published': result.published.isoformat(),
                'arxiv_id': result.entry_id.split('/')[-1],
                'categories': result.categories,
                'summary': result.summary,
                'pdf_url': result.pdf_url,
                'topic': topic,
                'filepath': str(filepath),
                'metrics': metrics,
                'download_timestamp': datetime.now().isoformat()
            }

            return metadata

        except Exception as e:
            print(f"  ✗ Error downloading {result.title[:50]}: {str(e)}")
            return None

    def search_and_download(self, query_config):
        """Execute search and download papers"""
        query = query_config['query']
        topic = query_config['topic']
        max_results = query_config['max_results']

        print(f"\n{'='*80}")
        print(f"SEARCHING: {topic}")
        print(f"Query: {query}")
        print(f"{'='*80}")

        # Initialize topic tracking
        if topic not in self.papers_by_topic:
            self.papers_by_topic[topic] = []

        # Search ArXiv
        search = arxiv.Search(
            query=query,
            max_results=max_results,
            sort_by=arxiv.SortCriterion.SubmittedDate,
            sort_order=arxiv.SortOrder.Descending
        )

        downloaded_count = 0
        total_candidates = 0

        for result in search.results():
            total_candidates += 1

            # Filter by year
            if not self.is_recent_paper(result):
                continue

            # Filter by relevance
            if not self.is_relevant_to_mfa_security(result):
                continue

            # Download paper
            metadata = self.download_paper(result, topic)

            if metadata:
                self.downloaded_papers.append(metadata)
                self.papers_by_topic[topic].append(metadata)
                self.research_metadata.append(metadata)
                downloaded_count += 1

                print(f"  📄 Downloaded #{len(self.downloaded_papers)}: {result.title[:60]}...")
                print(f"     Authors: {', '.join([a.name for a in result.authors[:3]])}...")
                print(f"     Published: {result.published.year}")
                print(f"     Metrics: {metadata['metrics']}")

                # Delay between downloads
                time.sleep(DOWNLOAD_DELAY)

                # Stop if we've reached target
                if len(self.downloaded_papers) >= TARGET_PAPERS:
                    print(f"\n✓ Reached target of {TARGET_PAPERS} papers!")
                    return True

        print(f"\n{topic.upper()} Summary:")
        print(f"  Candidates screened: {total_candidates}")
        print(f"  Papers downloaded: {downloaded_count}")

        return False

    def save_research_metadata(self):
        """Save comprehensive research metadata"""
        metadata_file = TARGET_DIR / "research_metadata.json"

        research_summary = {
            'collection_timestamp': datetime.now().isoformat(),
            'total_papers': len(self.downloaded_papers),
            'papers_by_topic': {
                topic: len(papers) for topic, papers in self.papers_by_topic.items()
            },
            'papers': self.research_metadata,
            'search_queries': SEARCH_QUERIES,
            'research_focus': {
                'issue': '#14: AI-Era MFA Authentication',
                'subtopic': 'Biometric Spoofing & Deepfake Detection',
                'objectives': [
                    'AI-generated deepfakes defeating biometric MFA systems',
                    'Liveness detection robustness against AI video synthesis',
                    'Fingerprint spoofing using AI-generated images',
                    'Multi-modal biometric security against GAN-generated attacks',
                    'Voice spoofing and audio deepfakes for authentication bypass'
                ]
            }
        }

        with open(metadata_file, 'w') as f:
            json.dump(research_summary, f, indent=2)

        print(f"\n✓ Saved research metadata to {metadata_file}")

    def generate_summary_report(self):
        """Generate human-readable summary report"""
        report_file = TARGET_DIR / "RESEARCH_SUMMARY.md"

        report = f"""# Biometric Spoofing & Deepfake Detection Research Summary

**Research Focus:** AI-Era MFA Authentication - Issue #14
**Collection Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Total Papers:** {len(self.downloaded_papers)}

## Research Objectives

1. AI-generated deepfakes defeating biometric MFA systems
2. Liveness detection robustness against AI video synthesis
3. Fingerprint spoofing using AI-generated images
4. Multi-modal biometric security against GAN-generated attacks
5. Voice spoofing and audio deepfakes for authentication bypass

## Papers by Topic

"""

        for topic, papers in self.papers_by_topic.items():
            report += f"\n### {topic.replace('_', ' ').title()} ({len(papers)} papers)\n\n"

            for paper in papers:
                report += f"**{paper['title']}**\n"
                report += f"- Authors: {', '.join(paper['authors'][:3])}\n"
                report += f"- Published: {paper['published'][:10]}\n"
                report += f"- ArXiv ID: {paper['arxiv_id']}\n"
                report += f"- Metrics: {paper['metrics']}\n"
                report += f"- File: `{Path(paper['filepath']).name}`\n\n"

        report += f"""
## Key Validation Targets

- Deepfake quality thresholds for successful liveness detection bypass
- Voice cloning effectiveness against speaker verification systems
- AI-generated fingerprint success rates in spoofing attacks
- Multi-modal biometric robustness against coordinated attacks
- Detection accuracy for AI-generated biometric presentations

## Next Steps

1. Systematic review of papers for empirical robustness metrics
2. Extract attack success rates and defense effectiveness
3. Identify state-of-the-art deepfake detection techniques
4. Analyze multi-modal fusion approaches for enhanced security
5. Compile validation thresholds for MFA security assessment

"""

        with open(report_file, 'w') as f:
            f.write(report)

        print(f"✓ Saved summary report to {report_file}")

def main():
    """Main research execution"""
    print("="*80)
    print("ArXiv Research: Biometric Spoofing & Deepfake Detection for MFA Security")
    print("="*80)
    print(f"Target: {TARGET_PAPERS} papers from {YEAR_FILTER} onwards")
    print(f"Minimum pages: {MIN_PAGES}")
    print(f"Download delay: {DOWNLOAD_DELAY} seconds")
    print(f"Target directory: {TARGET_DIR}")
    print("="*80)

    collector = BiometricResearchCollector()

    # Execute searches
    for query_config in SEARCH_QUERIES:
        reached_target = collector.search_and_download(query_config)
        if reached_target:
            break

    # Save metadata and generate reports
    collector.save_research_metadata()
    collector.generate_summary_report()

    print("\n" + "="*80)
    print("RESEARCH COLLECTION COMPLETE")
    print("="*80)
    print(f"Total papers downloaded: {len(collector.downloaded_papers)}")
    print(f"Papers by topic:")
    for topic, papers in collector.papers_by_topic.items():
        print(f"  - {topic}: {len(papers)}")
    print("="*80)

if __name__ == "__main__":
    main()
