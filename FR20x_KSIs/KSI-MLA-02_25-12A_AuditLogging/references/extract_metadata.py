#!/usr/bin/env python3
"""Extract metadata from downloaded ArXiv papers."""

import arxiv
import PyPDF2
import os
from datetime import datetime

papers_to_analyze = [
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

# US institutions to check for
us_institutions = [
    'MIT', 'Stanford', 'Berkeley', 'Harvard', 'Carnegie Mellon', 'Princeton',
    'Yale', 'Columbia', 'Cornell', 'CalTech', 'University of California',
    'Georgia Tech', 'University of Michigan', 'University of Texas',
    'University of Washington', 'Northwestern', 'Duke', 'Brown',
    'University of Pennsylvania', 'Johns Hopkins', 'NYU', 'USC', 'UCLA',
    'UIUC', 'Purdue', 'University of Maryland', 'UC San Diego', 'UC Santa Barbara'
]

print("=" * 80)
print("ARXIV PAPERS METADATA REPORT")
print("=" * 80)
print()

for arxiv_id, short_name in papers_to_analyze:
    filename = f"{base_dir}/{arxiv_id}_{short_name}.pdf"

    if not os.path.exists(filename):
        print(f"⚠ {arxiv_id}: PDF not found")
        continue

    try:
        # Get metadata from arXiv
        search = arxiv.Search(id_list=[arxiv_id])
        paper = next(client.results(search))

        # Get page count from PDF
        page_count = 0
        try:
            with open(filename, 'rb') as f:
                pdf_reader = PyPDF2.PdfReader(f)
                page_count = len(pdf_reader.pages)
        except:
            page_count = "Unknown"

        # Check for US institutions
        us_institution = False
        first_author_institution = "Unknown"
        for author in paper.authors:
            author_str = str(author)
            for inst in us_institutions:
                if inst.lower() in author_str.lower():
                    us_institution = True
                    if first_author_institution == "Unknown":
                        first_author_institution = inst
                    break

        # Format output
        print(f"ArXiv ID: {arxiv_id}")
        print(f"Title: {paper.title}")
        print(f"Authors: {', '.join([str(a) for a in paper.authors[:5]])}" +
              (f" (+{len(paper.authors)-5} more)" if len(paper.authors) > 5 else ""))
        print(f"Published: {paper.published.strftime('%Y-%m-%d')}")
        print(f"Updated: {paper.updated.strftime('%Y-%m-%d')}")
        print(f"Pages: {page_count}")
        print(f"US Institution: {'✓' if us_institution else '✗'} {first_author_institution if us_institution else ''}")
        print(f"Categories: {', '.join(paper.categories)}")
        print(f"Abstract: {paper.summary[:200]}...")
        print(f"PDF: {filename}")
        print("-" * 80)
        print()

    except Exception as e:
        print(f"✗ {arxiv_id}: Error - {e}")
        print("-" * 80)
        print()

print("=" * 80)
print("Report complete!")
print("=" * 80)
