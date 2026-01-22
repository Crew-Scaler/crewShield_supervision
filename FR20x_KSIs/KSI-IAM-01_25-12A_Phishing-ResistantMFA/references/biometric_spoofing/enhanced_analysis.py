#!/usr/bin/env python3
"""
Enhanced Analysis: Biometric Spoofing & Deepfake Detection Research
Focus: Extract validation metrics, attack success rates, and MFA security insights
"""

import json
from pathlib import Path
from collections import defaultdict

# Load research metadata
METADATA_FILE = Path("/Users/tamnguyen/Documents/GitHub/ksi_watch/KSI-IAM-01_25-12A_Phishing-ResistantMFA/references/biometric_spoofing/research_metadata.json")

def analyze_research_collection():
    """Analyze collected papers for key insights"""

    with open(METADATA_FILE, 'r') as f:
        data = json.load(f)

    papers = data['papers']

    print("="*80)
    print("BIOMETRIC SPOOFING & DEEPFAKE DETECTION RESEARCH ANALYSIS")
    print("="*80)
    print(f"\nTotal Papers Collected: {len(papers)}")
    print(f"Collection Date: {data['collection_timestamp']}")

    # Categorize papers by research focus
    categories = {
        'audio_deepfake': [],
        'face_deepfake': [],
        'multimodal': [],
        'liveness_detection': [],
        'voice_spoofing': [],
        'general_detection': []
    }

    for paper in papers:
        title_lower = paper['title'].lower()
        summary_lower = paper['summary'].lower()
        text = f"{title_lower} {summary_lower}"

        if any(term in text for term in ['audio', 'voice', 'speaker', 'speech']):
            if 'multimodal' in text or 'audio-visual' in text:
                categories['multimodal'].append(paper)
            else:
                categories['audio_deepfake'].append(paper)

        if any(term in text for term in ['face', 'facial', 'visual']):
            if 'multimodal' in text or 'audio-visual' in text:
                if paper not in categories['multimodal']:
                    categories['multimodal'].append(paper)
            else:
                categories['face_deepfake'].append(paper)

        if 'liveness' in text:
            categories['liveness_detection'].append(paper)

        if 'voice' in text and ('cloning' in text or 'synthesis' in text or 'spoofing' in text):
            categories['voice_spoofing'].append(paper)

        if paper not in [p for cat in categories.values() for p in cat]:
            categories['general_detection'].append(paper)

    print("\n" + "="*80)
    print("RESEARCH CATEGORIZATION")
    print("="*80)

    for category, papers_list in categories.items():
        if papers_list:
            print(f"\n{category.replace('_', ' ').title()}: {len(papers_list)} papers")

    # Identify high-value papers for MFA security
    print("\n" + "="*80)
    print("HIGH-VALUE PAPERS FOR MFA SECURITY ASSESSMENT")
    print("="*80)

    high_value_papers = []
    for paper in papers:
        score = 0
        summary_lower = paper['summary'].lower()
        title_lower = paper['title'].lower()

        # Scoring criteria
        if paper['metrics']['has_accuracy_metric']:
            score += 2
        if paper['metrics']['has_evaluation']:
            score += 2
        if paper['metrics']['empirical_study']:
            score += 3

        # Keywords indicating direct MFA relevance
        mfa_keywords = [
            'authentication', 'biometric', 'spoofing', 'attack success',
            'liveness detection', 'presentation attack', 'verification',
            'security', 'robust', 'defeat', 'bypass'
        ]

        keyword_matches = sum(1 for kw in mfa_keywords if kw in summary_lower or kw in title_lower)
        score += keyword_matches

        if score >= 5:
            high_value_papers.append((score, paper))

    # Sort by score
    high_value_papers.sort(reverse=True, key=lambda x: x[0])

    print(f"\nIdentified {len(high_value_papers)} high-value papers (score >= 5):\n")

    for rank, (score, paper) in enumerate(high_value_papers[:20], 1):
        print(f"{rank}. [Score: {score}] {paper['title']}")
        print(f"   Authors: {', '.join(paper['authors'][:3])}")
        print(f"   Published: {paper['published'][:10]}")
        print(f"   Metrics: Accuracy={paper['metrics']['has_accuracy_metric']}, "
              f"Evaluation={paper['metrics']['has_evaluation']}, "
              f"Empirical={paper['metrics']['empirical_study']}")
        print(f"   File: {Path(paper['filepath']).name}")
        print()

    # Extract papers with specific attack/defense focus
    print("\n" + "="*80)
    print("PAPERS BY SPECIFIC MFA SECURITY FOCUS")
    print("="*80)

    focus_areas = {
        'Voice Authentication Attacks': ['voice', 'speaker', 'audio', 'speech'],
        'Face Liveness Detection': ['liveness', 'face anti-spoofing', 'presentation attack'],
        'Multi-Modal Biometric Fusion': ['multimodal', 'multi-modal', 'fusion'],
        'GAN-Based Attacks': ['gan', 'generative adversarial', 'synthesis'],
        'Deepfake Detection Methods': ['detection', 'classifier', 'detection method']
    }

    for focus, keywords in focus_areas.items():
        matching_papers = []
        for paper in papers:
            text = f"{paper['title'].lower()} {paper['summary'].lower()}"
            if any(kw in text for kw in keywords):
                matching_papers.append(paper)

        if matching_papers:
            print(f"\n{focus}: {len(matching_papers)} papers")
            for paper in matching_papers[:5]:
                print(f"  - {paper['title'][:70]}...")

    # Year distribution
    print("\n" + "="*80)
    print("TEMPORAL DISTRIBUTION")
    print("="*80)

    year_counts = defaultdict(int)
    for paper in papers:
        year = paper['published'][:4]
        year_counts[year] += 1

    print("\nPapers by publication year:")
    for year in sorted(year_counts.keys(), reverse=True):
        print(f"  {year}: {year_counts[year]} papers")

    # Generate priority reading list
    print("\n" + "="*80)
    print("RECOMMENDED PRIORITY READING LIST FOR MFA SECURITY")
    print("="*80)

    priority_list = []

    # Criteria for priority
    for paper in papers:
        text = f"{paper['title'].lower()} {paper['summary'].lower()}"

        # High priority keywords
        high_priority = any(term in text for term in [
            'authentication', 'liveness detection', 'spoofing attack',
            'voice cloning', 'presentation attack', 'biometric security'
        ])

        # Has empirical evaluation
        has_evaluation = paper['metrics']['has_evaluation'] and paper['metrics']['has_accuracy_metric']

        if high_priority and has_evaluation:
            priority_list.append(paper)

    print(f"\n{len(priority_list)} papers prioritized for detailed review:\n")

    for idx, paper in enumerate(priority_list[:15], 1):
        print(f"{idx}. {paper['title']}")
        print(f"   Focus: {identify_focus(paper)}")
        print(f"   Published: {paper['published'][:10]}")
        print(f"   File: {Path(paper['filepath']).name}\n")

    # Generate summary statistics
    print("\n" + "="*80)
    print("RESEARCH COLLECTION STATISTICS")
    print("="*80)

    stats = {
        'Total Papers': len(papers),
        'Papers with Accuracy Metrics': sum(1 for p in papers if p['metrics']['has_accuracy_metric']),
        'Papers with Evaluation': sum(1 for p in papers if p['metrics']['has_evaluation']),
        'Empirical Studies': sum(1 for p in papers if p['metrics']['empirical_study']),
        'Audio/Voice Focus': len(categories['audio_deepfake']) + len(categories['voice_spoofing']),
        'Face/Visual Focus': len(categories['face_deepfake']),
        'Multi-Modal Focus': len(categories['multimodal']),
        'Liveness Detection': len(categories['liveness_detection'])
    }

    print()
    for key, value in stats.items():
        print(f"  {key}: {value}")

    print("\n" + "="*80)
    print("KEY VALIDATION TARGETS FOR ISSUE #14")
    print("="*80)

    validation_targets = [
        "Deepfake quality thresholds for successful liveness detection bypass",
        "Voice cloning effectiveness against speaker verification systems",
        "AI-generated fingerprint success rates in spoofing attacks",
        "Multi-modal biometric robustness against coordinated attacks",
        "Detection accuracy for AI-generated biometric presentations"
    ]

    print("\nResearch objectives covered by collected papers:")
    for idx, target in enumerate(validation_targets, 1):
        print(f"{idx}. {target}")

    print("\n" + "="*80)

def identify_focus(paper):
    """Identify primary research focus of paper"""
    text = f"{paper['title'].lower()} {paper['summary'].lower()}"

    if 'audio' in text or 'voice' in text or 'speech' in text:
        return "Audio/Voice"
    elif 'face' in text or 'facial' in text:
        return "Face/Visual"
    elif 'multimodal' in text or 'multi-modal' in text:
        return "Multi-Modal"
    elif 'liveness' in text:
        return "Liveness Detection"
    else:
        return "General Detection"

if __name__ == "__main__":
    analyze_research_collection()
