#!/usr/bin/env python3
"""Download ArXiv papers using the arxiv package."""

import arxiv
import os
import time

papers = [
    ("2501.11638", "class_imbalance_anomaly_detection"),
    ("2503.13195", "deep_learning_anomaly_detection_survey"),
    ("2505.04204", "cyber_security_imbalanced_datasets"),
    ("2401.12262", "network_intrusion_detection_imbalanced"),
    ("2503.03022", "generative_active_adaptation_intrusion_detection"),
    ("2505.14027", "csagc_ids_intrusion_detection"),
    ("2409.10951", "fair_anomaly_detection_imbalanced"),
    ("2502.02337", "rule_attack_mapper_siem_llm"),
    ("2408.03335", "explainable_ai_intrusion_detection_industry"),
    ("2512.03462", "malicious_url_classification_deep_learning"),
    ("2510.26046", "bias_corrected_data_synthesis_imbalanced"),
    ("2401.00286", "autonomous_threat_hunting_ai"),
    ("2407.14945", "intrusion_detection_cnn_bilstm"),
    ("2512.07030", "zero_day_attack_detection_imbalanced"),
]

base_dir = "/Users/tamnguyen/Documents/GitHub/ksi_watch/KSI-MLA-02_25-12A_AuditLogging/references"

client = arxiv.Client()

for arxiv_id, short_name in papers:
    filename = f"{base_dir}/{arxiv_id}_{short_name}.pdf"

    # Skip if already exists and is larger than 100KB
    if os.path.exists(filename) and os.path.getsize(filename) > 100000:
        print(f"✓ {arxiv_id} already downloaded ({os.path.getsize(filename)//1024} KB)")
        continue

    print(f"Downloading {arxiv_id}...", end=" ", flush=True)

    try:
        search = arxiv.Search(id_list=[arxiv_id])
        paper = next(client.results(search))

        paper.download_pdf(dirpath=base_dir, filename=f"{arxiv_id}_{short_name}.pdf")

        if os.path.exists(filename):
            size_kb = os.path.getsize(filename) // 1024
            print(f"✓ ({size_kb} KB)")
        else:
            print(f"✗ File not created")

        time.sleep(3)  # Be nice to arXiv servers

    except Exception as e:
        print(f"✗ Error: {e}")
        time.sleep(5)

print(f"\nDownload complete!")
