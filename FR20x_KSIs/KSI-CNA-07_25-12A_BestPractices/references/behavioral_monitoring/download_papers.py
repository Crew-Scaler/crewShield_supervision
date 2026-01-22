#!/usr/bin/env python3
"""
ArXiv Paper Downloader for AI-Driven Resource Governance Research
Downloads papers on configuration drift, behavioral anomaly detection, and AI security
"""

import os
import time
import urllib.request
import urllib.error
from typing import List, Dict
from pathlib import Path

# High-quality papers identified from searches (2024-2025)
PAPERS_TO_DOWNLOAD = [
    # Configuration Drift Detection
    {
        "id": "2410.09190",
        "title": "Time_to_Retrain_Detecting_Concept_Drifts_in_Machine_Learning_Systems",
        "category": "drift_detection",
        "priority": "high"
    },
    {
        "id": "2510.20211",
        "title": "Automated_Cloud_Infrastructure-as-Code_Reconciliation_with_AI_Agents",
        "category": "drift_remediation",
        "priority": "high"
    },
    {
        "id": "2508.00042",
        "title": "Towards_Reliable_AI_in_6G_Detecting_Concept_Drift_in_Wireless_Network",
        "category": "drift_detection",
        "priority": "medium"
    },
    {
        "id": "2505.24149",
        "title": "RCCDA_Adaptive_Model_Updates_Concept_Drift_Constrained_Resources",
        "category": "drift_detection",
        "priority": "high"
    },
    {
        "id": "2404.18673",
        "title": "Open-Source_Drift_Detection_Tools_in_Action_Two_Use_Cases",
        "category": "drift_detection",
        "priority": "high"
    },
    {
        "id": "2406.17813",
        "title": "Unsupervised_Concept_Drift_Detection_Deep_Learning_Real-time",
        "category": "drift_detection",
        "priority": "high"
    },
    {
        "id": "2108.05319",
        "title": "Machine_Learning_Model_Drift_Detection_Via_Weak_Data_Slices",
        "category": "drift_detection",
        "priority": "medium"
    },

    # Infrastructure and Remediation
    {
        "id": "2507.07416",
        "title": "Securing_Critical_Infrastructure_AI_Era_Automated_Security_Framework",
        "category": "infrastructure_security",
        "priority": "high"
    },
    {
        "id": "2404.19452",
        "title": "Sustainably_Monitor_ML_Systems_Accuracy_Energy_Efficiency_Tradeoffs",
        "category": "monitoring",
        "priority": "high"
    },
    {
        "id": "2411.16591",
        "title": "Adversarial_Attacks_for_Drift_Detection",
        "category": "adversarial",
        "priority": "high"
    },

    # Behavioral Anomaly Detection
    {
        "id": "2503.13195",
        "title": "Deep_Learning_Advancements_in_Anomaly_Detection_Comprehensive_Survey",
        "category": "anomaly_detection",
        "priority": "high"
    },
    {
        "id": "2411.09047",
        "title": "Anomaly_Detection_Large-Scale_Cloud_Systems_Industry_Case_Dataset",
        "category": "cloud_anomaly",
        "priority": "high"
    },
    {
        "id": "2509.14294",
        "title": "Monitoring_Machine_Learning_Systems_Multivocal_Literature_Review",
        "category": "ml_monitoring",
        "priority": "high"
    },
    {
        "id": "2507.15676",
        "title": "Agentic_AI_Autonomous_Anomaly_Management_Complex_Systems",
        "category": "agentic_ai",
        "priority": "high"
    },
    {
        "id": "2512.03101",
        "title": "ALARM_Automated_MLLM_Anomaly_Detection_Uncertainty_Quantification",
        "category": "anomaly_detection",
        "priority": "high"
    },
    {
        "id": "2501.11430",
        "title": "Survey_on_Diffusion_Models_for_Anomaly_Detection",
        "category": "anomaly_detection",
        "priority": "high"
    },
    {
        "id": "2511.17119",
        "title": "Modeling_Anomaly_Detection_in_Cloud_Services_Analysis",
        "category": "cloud_anomaly",
        "priority": "medium"
    },
    {
        "id": "2408.03335",
        "title": "Explainable_AI_Intrusion_Detection_Industry_5.0_Overview",
        "category": "intrusion_detection",
        "priority": "medium"
    },

    # Behavioral Baseline Poisoning and Adversarial
    {
        "id": "2503.09302",
        "title": "Behavioral_Baseline_Adversarial_Attacks_Survey",
        "category": "adversarial",
        "priority": "high"
    },
    {
        "id": "2503.22759",
        "title": "Data_Poisoning_in_Deep_Learning_Survey",
        "category": "poisoning",
        "priority": "high"
    },
    {
        "id": "2401.08984",
        "title": "GAN-based_Data_Poisoning_Framework_Anomaly_Detection_Federated_Learning",
        "category": "poisoning",
        "priority": "high"
    },
    {
        "id": "2207.08486",
        "title": "Using_Anomaly_Detection_Detect_Poisoning_Attacks_Federated_Learning",
        "category": "poisoning_defense",
        "priority": "high"
    },

    # AI Resource Behavioral Profiling
    {
        "id": "2505.03945",
        "title": "AI-Driven_Security_Cloud_Computing_Threat_Detection_Automated_Response",
        "category": "cloud_security",
        "priority": "high"
    },
    {
        "id": "2506.07407",
        "title": "Multi-Cloud_Resource_Monitoring_Behavioral_Analysis",
        "category": "resource_monitoring",
        "priority": "high"
    },
    {
        "id": "2506.05001",
        "title": "Focus-Enhanced_Attack_Detection_Security_Monitoring",
        "category": "attack_detection",
        "priority": "high"
    },
    {
        "id": "2508.10043",
        "title": "Securing_Agentic_AI_Threat_Modeling_Risk_Analysis_Network_Monitoring",
        "category": "agentic_security",
        "priority": "high"
    },
    {
        "id": "2506.23296",
        "title": "Securing_AI_Systems_Guide_Known_Attacks_Impacts",
        "category": "ai_security",
        "priority": "high"
    },
    {
        "id": "2411.09200",
        "title": "Advancing_Software_Security_Cloud_Platforms_AI_Anomaly_Detection",
        "category": "cloud_security",
        "priority": "medium"
    },
    {
        "id": "2504.19154",
        "title": "Comparative_Analysis_AI-Driven_Security_DevSecOps_Challenges_Solutions",
        "category": "devsecops",
        "priority": "medium"
    },

    # False Positive Reduction
    {
        "id": "2209.13965",
        "title": "Anomaly_Detection_Optimization_Big_Data_Deep_Learning_False-Positive",
        "category": "false_positive",
        "priority": "high"
    },
    {
        "id": "2509.01375",
        "title": "Anomaly_Detection_Network_Flows_Unsupervised_Online_Machine_Learning",
        "category": "network_anomaly",
        "priority": "high"
    },
    {
        "id": "2211.05244",
        "title": "Deep_Learning_Time_Series_Anomaly_Detection_Survey",
        "category": "time_series",
        "priority": "high"
    },

    # Configuration Drift Remediation and Governance
    {
        "id": "2511.07585",
        "title": "LLM_Output_Drift_Cross-Provider_Validation_Mitigation_Financial_Workflows",
        "category": "llm_drift",
        "priority": "high"
    },
    {
        "id": "2510.04073",
        "title": "Moral_Anchor_System_Predictive_Framework_AI_Value_Alignment_Drift_Prevention",
        "category": "value_alignment",
        "priority": "medium"
    },
    {
        "id": "2506.17442",
        "title": "Keeping_Medical_AI_Healthy_Trustworthy_Detection_Correction_Degradation",
        "category": "medical_ai",
        "priority": "medium"
    },

    # Real-time Behavioral Monitoring and Observability
    {
        "id": "2506.06366",
        "title": "AI_Agent_Behavioral_Science_Systematic_Framework",
        "category": "agent_behavior",
        "priority": "high"
    },
    {
        "id": "2509.06733",
        "title": "Reinforcement_Learning_Foundations_Deep_Research_Systems_Survey",
        "category": "reinforcement_learning",
        "priority": "medium"
    },
    {
        "id": "2506.22355",
        "title": "Embodied_AI_Agents_Modeling_the_World",
        "category": "embodied_ai",
        "priority": "medium"
    },
    {
        "id": "2506.02064",
        "title": "Measurement_Imbalance_Agentic_AI_Evaluation_Industry_Productivity",
        "category": "ai_evaluation",
        "priority": "medium"
    },

    # Additional High-Value Papers
    {
        "id": "2302.02452",
        "title": "Performance_Analysis_Machine_Learning_Centered_Systems",
        "category": "ml_performance",
        "priority": "medium"
    },
]


def download_paper(paper_id: str, filename: str, output_dir: Path) -> bool:
    """
    Download a paper from ArXiv

    Args:
        paper_id: ArXiv paper ID (e.g., "2410.09190")
        filename: Name to save the file as
        output_dir: Directory to save the paper

    Returns:
        True if successful, False otherwise
    """
    url = f"https://arxiv.org/pdf/{paper_id}.pdf"
    output_path = output_dir / f"{filename}.pdf"

    # Skip if already downloaded
    if output_path.exists():
        print(f"[SKIP] {filename} - Already exists")
        return True

    try:
        print(f"[DOWNLOADING] {paper_id} -> {filename}.pdf")

        # Set user agent to avoid blocking
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        }
        request = urllib.request.Request(url, headers=headers)

        with urllib.request.urlopen(request, timeout=30) as response:
            with open(output_path, 'wb') as out_file:
                out_file.write(response.read())

        print(f"[SUCCESS] {filename} - Downloaded successfully")
        return True

    except urllib.error.HTTPError as e:
        print(f"[ERROR] {filename} - HTTP Error {e.code}: {e.reason}")
        return False
    except urllib.error.URLError as e:
        print(f"[ERROR] {filename} - URL Error: {e.reason}")
        return False
    except Exception as e:
        print(f"[ERROR] {filename} - Unexpected error: {str(e)}")
        return False


def main():
    """Main download function"""
    output_dir = Path("/Users/tamnguyen/Documents/GitHub/ksi_watch/KSI-CNA-07_25-12A_BestPractices/references/behavioral_monitoring")
    output_dir.mkdir(parents=True, exist_ok=True)

    print("="*80)
    print("ArXiv Paper Downloader for AI-Driven Resource Governance Research")
    print("="*80)
    print(f"\nTarget Directory: {output_dir}")
    print(f"Total Papers to Download: {len(PAPERS_TO_DOWNLOAD)}\n")

    # Group papers by priority
    high_priority = [p for p in PAPERS_TO_DOWNLOAD if p["priority"] == "high"]
    medium_priority = [p for p in PAPERS_TO_DOWNLOAD if p["priority"] == "medium"]

    print(f"High Priority Papers: {len(high_priority)}")
    print(f"Medium Priority Papers: {len(medium_priority)}\n")

    success_count = 0
    failure_count = 0

    # Download high priority papers first
    print("\n" + "="*80)
    print("DOWNLOADING HIGH PRIORITY PAPERS")
    print("="*80 + "\n")

    for i, paper in enumerate(high_priority, 1):
        print(f"\n[{i}/{len(high_priority)}] Category: {paper['category']}")

        if download_paper(paper["id"], paper["title"], output_dir):
            success_count += 1
        else:
            failure_count += 1

        # Delay between downloads (3+ seconds)
        if i < len(high_priority):
            time.sleep(3.5)

    # Download medium priority papers
    print("\n" + "="*80)
    print("DOWNLOADING MEDIUM PRIORITY PAPERS")
    print("="*80 + "\n")

    for i, paper in enumerate(medium_priority, 1):
        print(f"\n[{i}/{len(medium_priority)}] Category: {paper['category']}")

        if download_paper(paper["id"], paper["title"], output_dir):
            success_count += 1
        else:
            failure_count += 1

        # Delay between downloads
        if i < len(medium_priority):
            time.sleep(3.5)

    # Print summary
    print("\n" + "="*80)
    print("DOWNLOAD SUMMARY")
    print("="*80)
    print(f"\nTotal Papers: {len(PAPERS_TO_DOWNLOAD)}")
    print(f"Successfully Downloaded: {success_count}")
    print(f"Failed: {failure_count}")
    print(f"Success Rate: {(success_count/len(PAPERS_TO_DOWNLOAD)*100):.1f}%")

    # Category breakdown
    print("\n" + "-"*80)
    print("PAPERS BY CATEGORY")
    print("-"*80)

    categories = {}
    for paper in PAPERS_TO_DOWNLOAD:
        cat = paper["category"]
        if cat not in categories:
            categories[cat] = 0
        categories[cat] += 1

    for cat, count in sorted(categories.items()):
        print(f"{cat:30s}: {count:2d} papers")

    print("\n" + "="*80)
    print("DOWNLOAD COMPLETE")
    print("="*80 + "\n")


if __name__ == "__main__":
    main()
