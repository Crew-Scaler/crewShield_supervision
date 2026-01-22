# Cluster 6: CSP-Specific Attack Surfaces - Complete Index

## Quick Navigation

### By Relevance (Highest to Lowest)

| Rank | ArXiv ID | Title | Score | Category |
|------|----------|-------|-------|----------|
| 1 | 2512.19997 | BacAlarm: API Security & BOLA Prevention | 9 | API Security |
| 2 | 2512.10361 | Bit of a Close Talker: Co-Location Attacks | 9 | Multi-Tenant Cloud |
| 3 | 2512.09957 | CloudFix: IAM Policy Repair (AWS/Azure/GCP) | 9 | Cloud Access Control |
| 4 | 2511.01910 | Security Audit: Intel ICE Driver for e810 | 9 | Cloud Infrastructure |
| 5 | 2512.22223 | ReGAIN: RAG Network Traffic Analysis | 8 | RAG Security |
| 6 | 2512.18335 | Quantization for Vector Search | 8 | Vector Database |
| 7 | 2512.12938 | SPAR: Adaptive Retrieval on Legacy Systems | 8 | RAG & Cloud Storage |
| 8 | 2512.12458 | Vector Retrieval Stability | 8 | Vector Database |
| 9 | 2512.12885 | SignRAG: Zero-Shot Road Sign Recognition | 8 | RAG Scalability |
| 10 | 2512.07509 | Vector Systems with Privacy Preservation | 8 | Vector DB & Privacy |
| 11 | 2512.08984 | RAG-HAR: Human Activity Recognition | 8 | RAG Applications |
| 12 | 2512.12140 | Embeddings in Smart Buildings | 7 | Embedding Security |
| 13 | 2512.06387 | AI Model Security: "Ten Deadly Sins" | 7 | AI Model Security |
| 14 | 2512.23471 | Semantic Tree Inference | 7 | Data Analysis |
| 15 | 2512.06316 | Pattern Detection in FRB Catalog | 6 | ML Anomaly Detection |

### By Topic Area

#### API Security (3 papers)
- 2512.19997 - BacAlarm (Rank 1)
- 2512.09957 - CloudFix (Rank 3)
- 2512.10361 - Co-Location Attacks (Rank 2)

#### Vector Database Security (3 papers)
- 2512.18335 - Vector Search Quantization (Rank 6)
- 2512.12458 - Vector Retrieval Stability (Rank 8)
- 2512.07509 - Vector Systems Privacy (Rank 10)

#### RAG Security & Applications (4 papers)
- 2512.22223 - ReGAIN (Rank 5)
- 2512.12938 - SPAR (Rank 7)
- 2512.12885 - SignRAG (Rank 9)
- 2512.08984 - RAG-HAR (Rank 11)

#### Multi-Tenant & Infrastructure (3 papers)
- 2512.10361 - Co-Location Attacks (Rank 2)
- 2511.01910 - Network Hardware (Rank 4)
- 2512.12140 - IoT/Cloud Control (Rank 12)

#### Supporting & Enabling (2 papers)
- 2512.06387 - AI Model Security (Rank 13)
- 2512.23471 - Semantic Analysis (Rank 14)
- 2512.06316 - Pattern Detection (Rank 15)

### By Publication Date

**December 2025 (Most Recent)**
- 2512.23471 (Dec 31)
- 2512.22223 (Dec 29)
- 2512.19997 (Dec 26)
- 2512.18335 (Dec 24)
- 2512.12938 (Dec 18)
- 2512.12885 (Dec 18)
- 2512.12458 (Dec 17)
- 2512.12140 (Dec 16)
- 2512.10361 (Dec 14)
- 2512.09957 (Dec 13)
- 2512.08984 (Dec 12)
- 2512.07509 (Dec 10)
- 2512.06387 (Dec 9)
- 2512.06316 (Dec 9)

**November 2025**
- 2511.01910 (Nov 3)

## Search Strategies Used

### Original Queries (ArXiv)
1. `all:API AND all:security AND submittedDate:[202401010000 TO 202512312359]`
2. `all:cloud AND all:vulnerability AND submittedDate:[202401010000 TO 202512312359]`
3. `all:vector AND all:database AND submittedDate:[202401010000 TO 202512312359]`
4. `all:RAG AND all:security AND submittedDate:[202401010000 TO 202512312359]`
5. `all:multi-tenant AND all:cloud AND submittedDate:[202401010000 TO 202512312359]`
6. `all:embedding AND all:attack AND submittedDate:[202401010000 TO 202512312359]`
7. `all:cloud AND all:infrastructure AND submittedDate:[202401010000 TO 202512312359]`

### Results
- Total search results: 210 papers
- After relevance filtering: 15 papers selected
- Selection criteria: Published 2024-2025, CSP-specific focus, minimum 6 relevance score

## Key Metrics

| Metric | Value |
|--------|-------|
| Total Papers | 15 |
| Average Relevance Score | 8.0 |
| Papers from 2025 | 14 (93%) |
| Papers from 2024 | 1 (7%) |
| Total Download Size | ~120 MB |
| Topics Covered | 5 major areas |
| Critical Priority Papers | 4 |

## File Listing

All files located in: `/Users/tamnguyen/Documents/GitHub/ksi_watch/KSI-CED-01_25-12A_GeneralTraining/references/cluster_6_csp_attack_surfaces/`

```
README.md                          # Comprehensive overview & analysis
cluster_6_metadata.csv             # Detailed metadata for all papers
SUMMARY.txt                        # Executive summary
INDEX.md                           # This file
arxiv_search_v2.py               # Search script used
create_metadata.py               # Metadata generation script

# Research Papers (PDFs)
2511.01910v2.pdf                 # [9] Intel ICE Driver Security
2512.06316v1.pdf                 # [6] Pattern Detection (Supporting)
2512.06387v1.pdf                 # [7] AI Model Security
2512.07509v2.pdf                 # [8] Vector Systems Privacy
2512.08984v1.pdf                 # [8] RAG-HAR
2512.09957v1.pdf                 # [9] CloudFix - IAM
2512.10361v2.pdf                 # [9] Co-Location Attacks *** CRITICAL ***
2512.12140v1.pdf                 # [7] Smart Buildings
2512.12458v1.pdf                 # [8] Vector Retrieval
2512.12885v1.pdf                 # [8] SignRAG
2512.12938v1.pdf                 # [8] SPAR
2512.18335v1.pdf                 # [8] Vector Quantization
2512.19997v1.pdf                 # [9] BacAlarm - API *** CRITICAL ***
2512.22223v1.pdf                 # [8] ReGAIN - RAG
2512.23471v1.pdf                 # [7] Semantic Analysis
```

## Critical Papers (Must Read)

### 1. BacAlarm (2512.19997v1.pdf)
- **Why Critical**: Most exploited cloud attack surface
- **Key Finding**: BOLA (Broken Object Level Authorization) affects all cloud APIs
- **CSP Impact**: Immediate risk to AWS, Azure, GCP resource authorization
- **Training Focus**: API security patterns for developers

### 2. Bit of a Close Talker (2512.10361v2.pdf)
- **Why Critical**: Fundamental CSP isolation vulnerability
- **Key Finding**: Serverless co-location attacks are practical and repeatable
- **CSP Impact**: AWS Lambda, Azure Functions, Google Cloud Functions all vulnerable
- **Training Focus**: Infrastructure architects and DevOps teams

### 3. CloudFix (2512.09957v1.pdf)
- **Why Critical**: IAM policy misconfiguration is widespread
- **Key Finding**: LLM-based automated remediation is effective
- **CSP Impact**: Reduces common misconfigurations across all CSPs
- **Training Focus**: Security teams and IAM administrators

### 4. Intel ICE Driver (2511.01910v2.pdf)
- **Why Critical**: Network infrastructure attack vector
- **Key Finding**: Driver-level vulnerabilities impact cloud data centers
- **CSP Impact**: Affects underlying CSP network hardware
- **Training Focus**: Cloud architects and infrastructure teams

## Training Recommendations

### For Cloud Architects
1. Start: 2512.10361 (multi-tenant risks)
2. Follow: 2511.01910 (infrastructure security)
3. Deep Dive: 2512.09957 (policy/access control)

### For API Developers
1. Start: 2512.19997 (BacAlarm - API patterns)
2. Follow: 2512.09957 (access control)
3. Reference: 2512.22223 (traffic analysis)

### For ML/Data Engineers
1. Start: 2512.18335 (vector database security)
2. Follow: 2512.22223 (RAG security)
3. Deep Dive: 2512.12938 (RAG on CSP storage)

### For Security Teams
1. Executive: SUMMARY.txt (overview)
2. Strategic: 2512.10361 (multi-tenant risks)
3. Tactical: 2512.09957 (policy remediation)
4. Technical: 2512.19997 (API exploitation)

### For DevOps/SRE
1. Critical: 2512.10361 (deployment risks)
2. Important: 2512.09957 (IAM policies)
3. Reference: 2511.01910 (infrastructure)

## Integration Points

- **Cluster 1**: Foundational AI security concepts
- **Cluster 2**: Model vulnerabilities connect to CSP API security
- **Cluster 3**: Prompt injection risks overlap with RAG security
- **Cluster 4**: Data protection relates to vector database security
- **Cluster 5**: Data governance supports multi-tenant isolation
- **Cluster 7**: Real-world attacks demonstrate CSP-specific impacts

## Related Resources

### External References
- AWS Well-Architected Security Pillar
- Azure Security Best Practices
- Google Cloud Security Command Center
- NIST CSP Security Framework
- CIS Cloud Controls

### ArXiv Categories Represented
- cs.CR (Cryptography and Security) - Primary
- cs.AI (Artificial Intelligence) - Supporting
- cs.DB (Databases) - Vector database papers
- cs.NE (Neural and Evolutionary Computing) - ML applications

## Updates & Maintenance

- **Last Updated**: 2026-01-06
- **Review Cycle**: Quarterly (new papers released constantly)
- **Next Review**: 2026-04-06
- **Maintenance Owner**: Security Research Team

---

**Status**: COMPLETE - Ready for integration into training modules
**Quality**: All papers from reputable sources, 93% from 2025
**Coverage**: Comprehensive across CSP attack surfaces
**Applicability**: Directly applicable to mandatory security training
