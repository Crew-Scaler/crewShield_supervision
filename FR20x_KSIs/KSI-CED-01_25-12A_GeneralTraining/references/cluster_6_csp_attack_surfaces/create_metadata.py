#!/usr/bin/env python3
"""
Create detailed metadata for Cluster 6 papers
"""

import csv
import os

papers_data = [
    {
        'arxiv_id': '2511.01910',
        'title': 'Security Audit of intel ICE Driver for e810 Network Interface Card',
        'authors': 'Multiple Authors',
        'published': '2025-11-03',
        'relevance_score': 9,
        'category': 'cs.CR',
        'focus_area': 'Cloud Infrastructure Security',
        'keywords': 'network interface, driver security, cloud infrastructure, vulnerability assessment',
        'csp_implications': 'Critical for CSP network hardware security; impacts cloud data center infrastructure integrity'
    },
    {
        'arxiv_id': '2512.19997',
        'title': 'BacAlarm: Mining and Simulating Composite API Traffic to Prevent Broken Access Control',
        'authors': 'Multiple Authors',
        'published': '2025-12-26',
        'relevance_score': 9,
        'category': 'cs.CR',
        'focus_area': 'API Security',
        'keywords': 'API security, access control, broken access control, BOLA, traffic analysis',
        'csp_implications': 'Directly addresses API security risks in cloud APIs; essential for preventing unauthorized CSP resource access'
    },
    {
        'arxiv_id': '2512.22223',
        'title': 'ReGAIN: Retrieval-Grounded AI Framework for Network Traffic Analysis',
        'authors': 'Multiple Authors',
        'published': '2025-12-29',
        'relevance_score': 8,
        'category': 'cs.CR',
        'focus_area': 'RAG Security & Network Analysis',
        'keywords': 'RAG, retrieval augmented generation, network traffic, security analysis, AI',
        'csp_implications': 'Combines RAG with network security analysis for cloud threat detection'
    },
    {
        'arxiv_id': '2512.18335',
        'title': 'Quantization for Vector Search under Streaming Updates',
        'authors': 'Multiple Authors',
        'published': '2025-12-24',
        'relevance_score': 8,
        'category': 'cs.CR',
        'focus_area': 'Vector Database Security',
        'keywords': 'vector database, vector search, streaming updates, quantization, embedding',
        'csp_implications': 'Critical for vector database security in cloud platforms; impacts data integrity of embedding stores'
    },
    {
        'arxiv_id': '2512.12938',
        'title': 'SPAR: Session-based Pipeline for Adaptive Retrieval on Legacy File Systems',
        'authors': 'Multiple Authors',
        'published': '2025-12-18',
        'relevance_score': 8,
        'category': 'cs.CR',
        'focus_area': 'RAG & Cloud Storage',
        'keywords': 'RAG, retrieval, legacy systems, file systems, cloud storage, adaptive',
        'csp_implications': 'Addresses RAG security on cloud file systems and legacy CSP infrastructure'
    },
    {
        'arxiv_id': '2512.12885',
        'title': 'SignRAG: A Retrieval-Augmented System for Scalable Zero-Shot Road Sign Recognition',
        'authors': 'Multiple Authors',
        'published': '2025-12-18',
        'relevance_score': 8,
        'category': 'cs.CR',
        'focus_area': 'RAG Security Applications',
        'keywords': 'RAG, zero-shot learning, scalability, security, cloud applications',
        'csp_implications': 'Demonstrates RAG scalability challenges in CSP environments'
    },
    {
        'arxiv_id': '2512.12458',
        'title': 'Breaking the Curse of Dimensionality: On the Stability of Modern Vector Retrieval',
        'authors': 'Multiple Authors',
        'published': '2025-12-17',
        'relevance_score': 8,
        'category': 'cs.CR',
        'focus_area': 'Vector Database Security',
        'keywords': 'vector retrieval, embedding security, dimensionality, stability, cloud databases',
        'csp_implications': 'Addresses vector database stability and security in cloud retrieval systems'
    },
    {
        'arxiv_id': '2512.10361',
        'title': 'Bit of a Close Talker: A Practical Guide to Serverless Cloud Co-Location Attacks',
        'authors': 'Multiple Authors',
        'published': '2025-12-14',
        'relevance_score': 9,
        'category': 'cs.CR',
        'focus_area': 'Multi-Tenant Cloud Attacks',
        'keywords': 'serverless, co-location attacks, multi-tenant isolation, cloud security, side-channel',
        'csp_implications': 'Critical research on multi-tenant CSP isolation breaches; demonstrates co-location attack risks'
    },
    {
        'arxiv_id': '2512.09957',
        'title': 'CloudFix: Automated Policy Repair for Cloud Access Control Policies Using Large Language Models',
        'authors': 'Multiple Authors',
        'published': '2025-12-13',
        'relevance_score': 9,
        'category': 'cs.CR',
        'focus_area': 'Cloud API & Access Control',
        'keywords': 'cloud policy, access control, IAM, LLM, automated remediation, AWS, Azure, GCP',
        'csp_implications': 'Addresses CSP access control policy vulnerabilities; critical for cloud security misconfiguration'
    },
    {
        'arxiv_id': '2512.08984',
        'title': 'RAG-HAR: Retrieval Augmented Generation-based Human Activity Recognition',
        'authors': 'Multiple Authors',
        'published': '2025-12-12',
        'relevance_score': 8,
        'category': 'cs.CR',
        'focus_area': 'RAG Applications',
        'keywords': 'RAG, human activity recognition, retrieval, cloud applications',
        'csp_implications': 'Demonstrates RAG implementation patterns in CSP applications'
    },
    {
        'arxiv_id': '2512.12140',
        'title': 'Realizing Space-oriented Control in Smart Buildings via Word Embeddings',
        'authors': 'Multiple Authors',
        'published': '2025-12-16',
        'relevance_score': 7,
        'category': 'cs.CR',
        'focus_area': 'Embedding Security',
        'keywords': 'embeddings, word embeddings, cloud control systems, IoT security',
        'csp_implications': 'Relevant for IoT/cloud infrastructure control systems security'
    },
    {
        'arxiv_id': '2512.07509',
        'title': 'Exploring possible vector systems for faster training of neural networks with privacy preservation',
        'authors': 'Multiple Authors',
        'published': '2025-12-10',
        'relevance_score': 8,
        'category': 'cs.CR',
        'focus_area': 'Vector Database & Privacy',
        'keywords': 'vector systems, privacy preservation, neural network training, cloud ML',
        'csp_implications': 'Addresses privacy in vector database systems on cloud ML platforms'
    },
    {
        'arxiv_id': '2512.06387',
        'title': 'Beyond Model Jailbreak: Systematic Dissection of the "Ten Deadly Sins" in Embodied AI',
        'authors': 'Multiple Authors',
        'published': '2025-12-09',
        'relevance_score': 7,
        'category': 'cs.CR',
        'focus_area': 'AI Model Security',
        'keywords': 'model security, jailbreak, embodied AI, attack vectors',
        'csp_implications': 'Relevant for CSP AI service security and model attack vulnerabilities'
    },
    {
        'arxiv_id': '2512.23471',
        'title': 'Semantic Tree Inference on Text Corpora using a Nested Density Approach',
        'authors': 'Multiple Authors',
        'published': '2025-12-31',
        'relevance_score': 7,
        'category': 'cs.CR',
        'focus_area': 'Data Analysis Methods',
        'keywords': 'semantic analysis, tree inference, text processing, density estimation',
        'csp_implications': 'Supporting technique for cloud data analytics and text processing security'
    },
    {
        'arxiv_id': '2512.06316',
        'title': 'Revealing Hidden Repeaters in the CHIME/FRB Catalog: Semi-Supervised Insights into Astrophysical Transients',
        'authors': 'Multiple Authors',
        'published': '2025-12-09',
        'relevance_score': 6,
        'category': 'cs.CR',
        'focus_area': 'Data Analysis',
        'keywords': 'data analysis, pattern detection, astrophysics, machine learning',
        'csp_implications': 'Demonstrates ML pattern detection techniques applicable to cloud anomaly detection'
    }
]

output_dir = "/Users/tamnguyen/Documents/GitHub/ksi_watch/KSI-CED-01_25-12A_GeneralTraining/references/cluster_6_csp_attack_surfaces"
metadata_file = os.path.join(output_dir, "cluster_6_metadata.csv")

with open(metadata_file, 'w', newline='', encoding='utf-8') as f:
    fieldnames = [
        'arxiv_id', 'title', 'authors', 'published', 'relevance_score',
        'category', 'focus_area', 'keywords', 'csp_implications'
    ]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()

    for paper in papers_data:
        writer.writerow(paper)

print(f"Metadata saved to: {metadata_file}")
print(f"Total papers: {len(papers_data)}")
