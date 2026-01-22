#!/usr/bin/env python3
"""
ArXiv Paper Downloader for AI-Powered MFA Attack Research
Downloads papers related to AI phishing, voice cloning, deepfakes, and AitM attacks
"""

import time
import urllib.request
import urllib.error
from pathlib import Path
from typing import List, Dict
import json

# Target directory
TARGET_DIR = Path("/Users/tamnguyen/Documents/GitHub/ksi_watch/KSI-IAM-01_25-12A_Phishing-ResistantMFA/references/ai_powered_attacks")

# ArXiv paper IDs identified from searches
PAPERS = [
    # AI-Generated Phishing & LLM Social Engineering
    {"id": "2412.00586", "title": "LLM_Automated_Spear_Phishing_Human_Validation", "category": "phishing"},
    {"id": "2411.13874", "title": "Next_Generation_Phishing_LLM_Agents", "category": "phishing"},
    {"id": "2511.11759", "title": "Jailbreak_AI_Phishing_Elderly_Victims", "category": "phishing"},
    {"id": "2402.18093", "title": "ChatSpamDetector_LLM_Phishing_Detection", "category": "phishing"},
    {"id": "2507.07406", "title": "Evolution_Phishing_Detection_AI_Comparative", "category": "phishing"},
    {"id": "2510.11915", "title": "Robust_Detection_LLM_Generated_Adversarial_Phishing", "category": "phishing"},
    {"id": "2511.21448", "title": "Labeled_Email_Dataset_Phishing_Spam_Detection", "category": "phishing"},

    # Voice Cloning & MFA Bypass
    {"id": "2505.12332", "title": "VoiceCloak_Defense_Framework_Voice_Cloning", "category": "voice"},
    {"id": "2507.02606", "title": "DeAntiFake_Protective_Perturbations_Voice_Cloning", "category": "voice"},
    {"id": "2505.00579", "title": "Voice_Cloning_Comprehensive_Survey", "category": "voice"},
    {"id": "2402.18085", "title": "Pitch_AI_Tagging_Deepfake_Audio_Calls", "category": "voice"},
    {"id": "2410.20742", "title": "Mitigating_Unauthorized_Speech_Synthesis", "category": "voice"},
    {"id": "2312.01479", "title": "OpenVoice_Versatile_Voice_Cloning", "category": "voice"},
    {"id": "2504.09839", "title": "SafeSpeech_Universal_Voice_Protection", "category": "voice"},

    # Deepfake & Liveness Detection
    {"id": "2508.19714", "title": "Deepfake_Selfie_Banking_Camera_Authentication", "category": "deepfake"},
    {"id": "2506.06825", "title": "Identity_Deepfake_Biometric_Authentication_Threats", "category": "deepfake"},
    {"id": "2508.09094", "title": "Deep_Learning_Robust_Facial_Liveness_Detection", "category": "deepfake"},
    {"id": "2507.22469", "title": "Visual_Language_Models_Deepfake_Detectors", "category": "deepfake"},
    {"id": "2412.20833", "title": "Global_Multimedia_Deepfake_Detection_Challenge", "category": "deepfake"},
    {"id": "2208.05401", "title": "Benchmarking_Face_Spoofing_Forgery_Detection", "category": "deepfake"},
    {"id": "2507.21905", "title": "Evaluating_Deepfake_Detectors_Wild", "category": "deepfake"},
    {"id": "2508.06248", "title": "Deepfake_Detection_Generalizes_Benchmarks", "category": "deepfake"},
    {"id": "2509.18461", "title": "Zero_Shot_Visual_Deepfake_Detection", "category": "deepfake"},

    # Phishing-Resistant Authentication & FIDO2
    {"id": "2308.08096", "title": "Passwordless_FIDO2_Enterprise_Usability", "category": "auth"},
    {"id": "2308.02973", "title": "Security_Usability_Analysis_Local_Attacks_FIDO2", "category": "auth"},
    {"id": "2206.13358", "title": "FIDO2_Two_Displays_Protection", "category": "auth"},
    {"id": "2402.12864", "title": "Novel_Protocol_Captive_Portals_FIDO2", "category": "auth"},
    {"id": "2412.03277", "title": "EAP_FIDO_Network_Authentication", "category": "auth"},
    {"id": "2205.08071", "title": "Timing_Attacks_FIDO_Authenticator_Privacy", "category": "auth"},
]

# Additional papers to search for (will add more through API search)
SEARCH_QUERIES = [
    "AI phishing conversion rate effectiveness measurement",
    "LLM social engineering email generation GPT-4 Claude",
    "voice synthesis vishing authentication bypass",
    "deepfake facial recognition spoofing attack",
    "adversary middle MFA token stealing session hijacking",
    "behavioral biometrics AI evasion attack",
    "multi-modal deepfake attack voice face",
    "phishing-as-a-service EvilGinx AitM detection",
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
    print(f"ArXiv AI-Powered MFA Attack Research Downloader")
    print(f"Target Directory: {TARGET_DIR}")
    print(f"Papers to download: {len(PAPERS)}\n")

    TARGET_DIR.mkdir(parents=True, exist_ok=True)

    successful = 0
    failed = 0
    skipped = 0

    for idx, paper in enumerate(PAPERS, 1):
        print(f"\n[{idx}/{len(PAPERS)}] Processing: {paper['title']}")

        result = download_paper(paper['id'], paper['title'], paper['category'])

        if result:
            successful += 1
        else:
            failed += 1

        # Delay between downloads (3+ seconds as requested)
        if idx < len(PAPERS):
            delay = 3.5
            print(f"   Waiting {delay}s before next download...")
            time.sleep(delay)

    # Summary
    print(f"\n{'='*60}")
    print(f"Download Summary:")
    print(f"  Successful: {successful}")
    print(f"  Failed: {failed}")
    print(f"  Total: {len(PAPERS)}")
    print(f"{'='*60}")

    # Create download log
    log_data = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "total_papers": len(PAPERS),
        "successful": successful,
        "failed": failed,
        "papers": PAPERS
    }

    log_path = TARGET_DIR / "download_log.json"
    with open(log_path, 'w') as f:
        json.dump(log_data, f, indent=2)

    print(f"\nDownload log saved to: {log_path}")


if __name__ == "__main__":
    main()
