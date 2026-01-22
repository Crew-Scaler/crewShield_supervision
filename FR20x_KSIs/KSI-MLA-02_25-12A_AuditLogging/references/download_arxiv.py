#!/usr/bin/env python3
"""Download ArXiv papers using requests library."""

import requests
import time
import sys

papers = [
    ("2501.11638", "class_imbalance_anomaly_detection"),
    ("2503.13195", "deep_learning_anomaly_detection_survey"),
    ("2505.04204", "cyber_security_imbalanced_datasets"),
    ("2401.12262", "network_intrusion_detection_imbalanced"),
    ("2503.03022", "generative_active_adaptation_intrusion_detection"),
    ("2505.14027", "csagc_ids_intrusion_detection"),
    ("2409.10951", "fair_anomaly_detection_imbalanced"),
    ("2502.02337", "rule_attack_mapper_siem_llm"),
    ("2503.02065", "explainable_ai_threat_intelligence"),
    ("2408.03335", "explainable_ai_intrusion_detection_industry"),
    ("2512.03462", "malicious_url_classification_deep_learning"),
    ("2510.26046", "bias_corrected_data_synthesis_imbalanced"),
    ("2401.00286", "autonomous_threat_hunting_ai"),
    ("2407.14945", "intrusion_detection_cnn_bilstm"),
    ("2512.07030", "zero_day_attack_detection_imbalanced"),
]

base_dir = "/Users/tamnguyen/Documents/GitHub/ksi_watch/KSI-MLA-02_25-12A_AuditLogging/references"

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
}

for arxiv_id, short_name in papers:
    filename = f"{base_dir}/{arxiv_id}_{short_name}.pdf"
    url = f"https://arxiv.org/pdf/{arxiv_id}.pdf"

    print(f"Downloading {arxiv_id}...", end=" ", flush=True)

    try:
        response = requests.get(url, headers=headers, timeout=30, allow_redirects=True)

        if response.status_code == 200 and len(response.content) > 10000:
            with open(filename, 'wb') as f:
                f.write(response.content)
            print(f"✓ ({len(response.content)//1024} KB)")
        else:
            print(f"✗ (status {response.status_code}, size {len(response.content)})")

        time.sleep(1)  # Be nice to arXiv servers

    except Exception as e:
        print(f"✗ Error: {e}")

print(f"\nDownload complete!")
