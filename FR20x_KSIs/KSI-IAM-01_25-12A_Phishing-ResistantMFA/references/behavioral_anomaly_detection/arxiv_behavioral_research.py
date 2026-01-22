#!/usr/bin/env python3
"""
ArXiv Research Script: ML-Based Behavioral Anomaly Detection for Authentication
Focus: Authentication security, behavioral biometrics, adaptive MFA, model robustness
"""

import arxiv
import time
import os
from pathlib import Path
from typing import List, Dict, Set
import json
from datetime import datetime

class BehavioralAuthenticationResearcher:
    def __init__(self, output_dir: str):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.downloaded_papers = set()
        self.metadata_file = self.output_dir / "research_metadata.json"
        self.metadata = []
        self.min_pages = 7
        self.target_papers = 45
        self.download_delay = 3

    def search_and_download(self, query: str, category: str, max_results: int = 100):
        """Search ArXiv and download relevant papers"""
        print(f"\n{'='*80}")
        print(f"Searching: {query}")
        print(f"Category: {category}")
        print(f"{'='*80}\n")

        search = arxiv.Search(
            query=query,
            max_results=max_results,
            sort_by=arxiv.SortCriterion.SubmittedDate,
            sort_order=arxiv.SortOrder.Descending
        )

        downloaded_count = 0
        for result in search.results():
            if len(self.downloaded_papers) >= self.target_papers:
                print(f"\n✓ Target of {self.target_papers} papers reached!")
                return

            # Filter for recent papers (2024-2025)
            pub_year = result.published.year
            if pub_year < 2024:
                continue

            # Check if already downloaded
            paper_id = result.entry_id.split('/')[-1]
            if paper_id in self.downloaded_papers:
                continue

            # Quality filters
            title_lower = result.title.lower()
            abstract_lower = result.summary.lower()

            # Relevance scoring
            relevance_keywords = {
                'authentication': 3,
                'behavioral': 3,
                'anomaly detection': 3,
                'biometric': 2,
                'mfa': 2,
                'multi-factor': 2,
                'continuous authentication': 3,
                'risk-based': 2,
                'adaptive': 2,
                'machine learning': 2,
                'deep learning': 2,
                'neural network': 1,
                'model drift': 3,
                'concept drift': 3,
                'adversarial': 2,
                'attack': 1,
                'evasion': 2,
                'poisoning': 2,
                'baseline': 1,
                'account takeover': 3,
                'credential': 2,
                'zero trust': 2,
                'user behavior': 2,
                'keystroke': 2,
                'mouse dynamics': 2,
                'touch dynamics': 2,
                'gait': 1,
                'false positive': 2,
                'false negative': 2,
                'precision': 1,
                'recall': 1,
                'f1-score': 1,
                'auc-roc': 1,
                'lstm': 1,
                'transformer': 1,
                'autoencoder': 1,
                'isolation forest': 1,
                'one-class': 1,
                'unsupervised': 1,
                'semi-supervised': 1
            }

            relevance_score = 0
            for keyword, weight in relevance_keywords.items():
                if keyword in title_lower:
                    relevance_score += weight * 2
                if keyword in abstract_lower:
                    relevance_score += weight

            # Minimum relevance threshold
            if relevance_score < 5:
                continue

            # Download paper
            try:
                pdf_filename = f"{paper_id.replace('/', '_')}_{pub_year}.pdf"
                pdf_path = self.output_dir / pdf_filename

                print(f"\n📄 Downloading: {result.title}")
                print(f"   Authors: {', '.join([a.name for a in result.authors[:3]])}...")
                print(f"   Published: {result.published.strftime('%Y-%m-%d')}")
                print(f"   Relevance Score: {relevance_score}")
                print(f"   ArXiv ID: {paper_id}")

                result.download_pdf(filename=str(pdf_path))

                # Check file size (proxy for page count)
                file_size_mb = pdf_path.stat().st_size / (1024 * 1024)
                if file_size_mb < 0.3:  # ~7 pages minimum
                    print(f"   ⚠️  File too small ({file_size_mb:.2f} MB), skipping...")
                    pdf_path.unlink()
                    continue

                print(f"   ✓ Downloaded: {pdf_filename} ({file_size_mb:.2f} MB)")

                # Store metadata
                metadata = {
                    'arxiv_id': paper_id,
                    'title': result.title,
                    'authors': [a.name for a in result.authors],
                    'published': result.published.strftime('%Y-%m-%d'),
                    'updated': result.updated.strftime('%Y-%m-%d'),
                    'category': category,
                    'query': query,
                    'relevance_score': relevance_score,
                    'file_size_mb': file_size_mb,
                    'pdf_url': result.pdf_url,
                    'abstract': result.summary[:500] + '...',
                    'primary_category': result.primary_category,
                    'categories': result.categories,
                    'downloaded_at': datetime.now().isoformat()
                }

                self.metadata.append(metadata)
                self.downloaded_papers.add(paper_id)
                downloaded_count += 1

                # Save metadata after each download
                self._save_metadata()

                # Respectful delay
                time.sleep(self.download_delay)

            except Exception as e:
                print(f"   ✗ Error downloading: {e}")
                continue

        print(f"\n✓ Downloaded {downloaded_count} papers in this search")

    def _save_metadata(self):
        """Save metadata to JSON file"""
        with open(self.metadata_file, 'w') as f:
            json.dump({
                'total_papers': len(self.metadata),
                'last_updated': datetime.now().isoformat(),
                'papers': self.metadata
            }, f, indent=2)

    def execute_research_plan(self):
        """Execute comprehensive research strategy"""

        print("\n" + "="*80)
        print("ArXiv Research: ML-Based Behavioral Anomaly Detection for Authentication")
        print("Target: 35-45 high-quality papers (2024-2025)")
        print("="*80 + "\n")

        # Research queries with categories
        research_queries = [
            # Core behavioral authentication & ML
            (
                'ti:behavioral AND (ti:authentication OR ti:biometric) AND '
                '(abs:anomaly OR abs:"machine learning" OR abs:"deep learning")',
                'behavioral_ml_authentication'
            ),
            (
                'abs:"behavioral anomaly detection" AND abs:authentication AND '
                '(abs:"machine learning" OR abs:"neural network")',
                'behavioral_anomaly_ml'
            ),
            (
                'ti:"continuous authentication" AND (abs:behavioral OR abs:biometric) AND '
                '(abs:"machine learning" OR abs:lstm OR abs:transformer)',
                'continuous_auth_ml'
            ),

            # Risk-based & adaptive MFA
            (
                '(ti:"risk-based authentication" OR ti:"adaptive MFA") AND '
                '(abs:behavioral OR abs:"anomaly detection" OR abs:"machine learning")',
                'risk_based_adaptive'
            ),
            (
                'abs:"adaptive authentication" AND abs:behavioral AND '
                '(abs:"risk score" OR abs:"risk assessment" OR abs:ml)',
                'adaptive_risk_ml'
            ),
            (
                'ti:MFA OR ti:"multi-factor authentication" AND '
                'abs:"machine learning" AND (abs:behavioral OR abs:adaptive)',
                'mfa_ml_behavioral'
            ),

            # Behavioral biometrics
            (
                '(abs:"keystroke dynamics" OR abs:"mouse dynamics" OR abs:"touch dynamics") AND '
                '(abs:"machine learning" OR abs:"deep learning" OR abs:lstm)',
                'behavioral_biometrics_ml'
            ),
            (
                'ti:"behavioral biometrics" AND (abs:authentication OR abs:verification) AND '
                'abs:"machine learning"',
                'biometric_auth_ml'
            ),
            (
                'abs:"user behavior" AND abs:authentication AND '
                '(abs:"anomaly detection" OR abs:"outlier detection") AND abs:ml',
                'user_behavior_anomaly'
            ),

            # Model drift & robustness
            (
                '(abs:"model drift" OR abs:"concept drift") AND '
                '(abs:authentication OR abs:behavioral OR abs:biometric)',
                'model_drift_auth'
            ),
            (
                'abs:"concept drift" AND abs:"anomaly detection" AND '
                '(abs:security OR abs:authentication OR abs:behavioral)',
                'concept_drift_anomaly'
            ),
            (
                '(ti:"data drift" OR abs:"distribution drift") AND '
                '(abs:"machine learning" OR abs:"deep learning") AND abs:security',
                'data_drift_security'
            ),

            # Adversarial attacks & evasion
            (
                'abs:"adversarial attack" AND (abs:authentication OR abs:biometric OR abs:behavioral) AND '
                'abs:"machine learning"',
                'adversarial_auth_ml'
            ),
            (
                '(abs:"evasion attack" OR abs:"poisoning attack") AND '
                '(abs:authentication OR abs:"anomaly detection") AND abs:behavioral',
                'evasion_poisoning_behavioral'
            ),
            (
                'abs:"adversarial robustness" AND '
                '(abs:"behavioral biometrics" OR abs:"behavioral authentication")',
                'adversarial_robustness'
            ),

            # Account takeover & credential compromise
            (
                'abs:"account takeover" AND (abs:"anomaly detection" OR abs:"machine learning") AND '
                '(abs:behavioral OR abs:detection)',
                'account_takeover_detection'
            ),
            (
                'abs:"credential compromise" AND abs:detection AND '
                '(abs:behavioral OR abs:"machine learning" OR abs:anomaly)',
                'credential_compromise_ml'
            ),
            (
                '(abs:"compromised credentials" OR abs:"stolen credentials") AND '
                'abs:"anomaly detection" AND abs:behavioral',
                'compromised_creds_behavioral'
            ),

            # Zero Trust & modern approaches
            (
                'abs:"zero trust" AND abs:authentication AND '
                '(abs:behavioral OR abs:"machine learning" OR abs:adaptive)',
                'zero_trust_behavioral'
            ),
            (
                'ti:"zero trust" AND (abs:"continuous authentication" OR abs:"risk-based") AND '
                'abs:ml',
                'zero_trust_continuous'
            ),

            # Specific ML architectures
            (
                '(abs:autoencoder OR abs:"isolation forest" OR abs:"one-class SVM") AND '
                'abs:"anomaly detection" AND (abs:authentication OR abs:security)',
                'ml_architectures_anomaly'
            ),
            (
                '(abs:lstm OR abs:gru OR abs:transformer) AND abs:behavioral AND '
                '(abs:authentication OR abs:biometric OR abs:security)',
                'deep_learning_behavioral'
            ),

            # Performance metrics & evaluation
            (
                'abs:authentication AND abs:"anomaly detection" AND '
                '(abs:"false positive" OR abs:"false alarm" OR abs:"precision recall")',
                'auth_anomaly_metrics'
            ),
            (
                'abs:"behavioral authentication" AND '
                '(abs:evaluation OR abs:benchmark OR abs:performance) AND abs:ml',
                'behavioral_evaluation'
            ),
        ]

        # Execute searches
        for query, category in research_queries:
            if len(self.downloaded_papers) >= self.target_papers:
                break
            self.search_and_download(query, category, max_results=100)

        # Final report
        self._generate_final_report()

    def _generate_final_report(self):
        """Generate comprehensive research report"""
        print("\n" + "="*80)
        print("RESEARCH COMPLETE - FINAL REPORT")
        print("="*80 + "\n")

        print(f"📊 Total Papers Downloaded: {len(self.downloaded_papers)}")
        print(f"📁 Output Directory: {self.output_dir}")
        print(f"📋 Metadata File: {self.metadata_file}")

        # Category breakdown
        category_counts = {}
        year_counts = {}

        for paper in self.metadata:
            cat = paper['category']
            category_counts[cat] = category_counts.get(cat, 0) + 1

            year = paper['published'][:4]
            year_counts[year] = year_counts.get(year, 0) + 1

        print("\n📚 Papers by Category:")
        for cat, count in sorted(category_counts.items(), key=lambda x: x[1], reverse=True)[:10]:
            print(f"   {cat}: {count}")

        print("\n📅 Papers by Year:")
        for year, count in sorted(year_counts.items(), reverse=True):
            print(f"   {year}: {count}")

        # Top papers by relevance
        print("\n⭐ Top 10 Papers by Relevance Score:")
        sorted_papers = sorted(self.metadata, key=lambda x: x['relevance_score'], reverse=True)
        for i, paper in enumerate(sorted_papers[:10], 1):
            print(f"\n{i}. {paper['title']}")
            print(f"   Score: {paper['relevance_score']} | {paper['published']} | {paper['arxiv_id']}")
            print(f"   Category: {paper['category']}")

        print("\n" + "="*80)
        print("✓ Research phase complete!")
        print("="*80 + "\n")


if __name__ == "__main__":
    output_directory = "/Users/tamnguyen/Documents/GitHub/ksi_watch/KSI-IAM-01_25-12A_Phishing-ResistantMFA/references/behavioral_anomaly_detection"

    researcher = BehavioralAuthenticationResearcher(output_directory)
    researcher.execute_research_plan()
