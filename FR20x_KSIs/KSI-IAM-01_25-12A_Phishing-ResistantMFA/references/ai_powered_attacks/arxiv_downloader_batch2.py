#!/usr/bin/env python3
"""
ArXiv Paper Downloader - Batch 2
Additional papers for AI-Powered MFA Attack Research
"""

import time
import urllib.request
import urllib.error
from pathlib import Path
from typing import List, Dict
import json

# Target directory
TARGET_DIR = Path("/Users/tamnguyen/Documents/GitHub/ksi_watch/KSI-IAM-01_25-12A_Phishing-ResistantMFA/references/ai_powered_attacks")

# Additional papers identified from secondary searches
ADDITIONAL_PAPERS = [
    # Behavioral Biometrics & Continuous Authentication
    {"id": "2302.02740", "title": "AuthentiSense_Behavioral_Biometrics_Few_Shot", "category": "biometrics"},
    {"id": "2501.17866", "title": "Brainwave_Biometrics_Multi_Session_Evaluation", "category": "biometrics"},
    {"id": "2502.03682", "title": "Defense_Intimate_Partner_Infiltration", "category": "biometrics"},
    {"id": "2001.08578", "title": "Sensor_Continuous_Authentication_Behavioral_Survey", "category": "biometrics"},
    {"id": "2205.08371", "title": "User_Authentication_Behavioral_Biometrics_ML", "category": "biometrics"},
    {"id": "2501.09239", "title": "AI_Based_Identity_Fraud_Detection_Systematic_Review", "category": "biometrics"},

    # Multi-Modal Deepfake Attacks
    {"id": "2406.06965", "title": "Single_Modal_to_Multi_Modal_Deepfake_Detection", "category": "multimodal"},
    {"id": "2503.02857", "title": "Deepfake_Eval_2024_Multi_Modal_Benchmark", "category": "multimodal"},
    {"id": "2504.00454", "title": "FA3_CLIP_Frequency_Aware_Face_Attack_Detection", "category": "multimodal"},
    {"id": "2510.21004", "title": "Face_to_Voice_Deepfake_Attacks_Detection", "category": "multimodal"},
    {"id": "2410.03487", "title": "Multimodal_Framework_DeepFake_Detection", "category": "multimodal"},
    {"id": "2507.21157", "title": "Unmasking_Synthetic_Realities_Generative_AI", "category": "multimodal"},
    {"id": "2408.01532", "title": "Contextual_Cross_Modal_Audio_Visual_Deepfake", "category": "multimodal"},

    # Additional Phishing & Social Engineering
    {"id": "2404.17929", "title": "LLM_Enhanced_Social_Engineering_Attack_Generation", "category": "phishing"},
    {"id": "2501.00234", "title": "Adversarial_Examples_Against_Email_Spam_Filters", "category": "phishing"},

    # Advanced Authentication Bypass
    {"id": "2311.08479", "title": "WebAuthn_Security_Analysis_Practical_Attacks", "category": "auth"},
]


def download_paper(arxiv_id: str, filename: str, category: str) -> bool:
    """Download a paper from ArXiv with retry logic"""
    url = f"https://arxiv.org/pdf/{arxiv_id}.pdf"
    category_dir = TARGET_DIR / category
    category_dir.mkdir(parents=True, exist_ok=True)

    output_path = category_dir / f"{filename}.pdf"

    if output_path.exists():
        print(f"✓ Already exists: {filename}")
        return True

    try:
        print(f"⬇ Downloading {arxiv_id}: {filename}...")
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        }
        req = urllib.request.Request(url, headers=headers)

        with urllib.request.urlopen(req, timeout=30) as response:
            content = response.read()

        with open(output_path, 'wb') as f:
            f.write(content)

        print(f"✓ Downloaded: {filename} ({len(content)/1024:.1f} KB)")
        return True

    except urllib.error.HTTPError as e:
        print(f"✗ HTTP Error {e.code} for {arxiv_id}: {filename}")
        return False
    except Exception as e:
        print(f"✗ Error downloading {arxiv_id}: {str(e)}")
        return False


def main():
    """Main download orchestration"""
    print(f"ArXiv AI-Powered MFA Attack Research Downloader - Batch 2")
    print(f"Target Directory: {TARGET_DIR}")
    print(f"Additional papers to download: {len(ADDITIONAL_PAPERS)}\n")

    TARGET_DIR.mkdir(parents=True, exist_ok=True)

    successful = 0
    failed = 0

    for idx, paper in enumerate(ADDITIONAL_PAPERS, 1):
        print(f"\n[{idx}/{len(ADDITIONAL_PAPERS)}] Processing: {paper['title']}")

        result = download_paper(paper['id'], paper['title'], paper['category'])

        if result:
            successful += 1
        else:
            failed += 1

        # Delay between downloads (3+ seconds as requested)
        if idx < len(ADDITIONAL_PAPERS):
            delay = 3.5
            print(f"   Waiting {delay}s before next download...")
            time.sleep(delay)

    # Summary
    print(f"\n{'='*60}")
    print(f"Batch 2 Download Summary:")
    print(f"  Successful: {successful}")
    print(f"  Failed: {failed}")
    print(f"  Total: {len(ADDITIONAL_PAPERS)}")
    print(f"{'='*60}")

    # Update download log
    log_data = {
        "batch": 2,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "total_papers": len(ADDITIONAL_PAPERS),
        "successful": successful,
        "failed": failed,
        "papers": ADDITIONAL_PAPERS
    }

    log_path = TARGET_DIR / "download_log_batch2.json"
    with open(log_path, 'w') as f:
        json.dump(log_data, f, indent=2)

    print(f"\nBatch 2 download log saved to: {log_path}")


if __name__ == "__main__":
    main()
