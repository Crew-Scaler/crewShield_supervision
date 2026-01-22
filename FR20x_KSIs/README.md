# Supervising AI Agent Crews with FedRAMP-20x Key Security Indicators

## Overview

The **KSIs (Key Security Indicators)** directory contains comprehensive documentation and research materials for FedRAMP 20x compliance, focusing on AI and AI Agent security, infrastructure security, and operational security requirements. This repository aggregates +60 Key Security Indicator folders with over 9,000 academic and technical reference papers organized by security domain and topic clusters.

## Folder Structure

Each KSI folder typically contains:

```
KSI-{PREFIX}-{NUMBER}_25-12A_{Description}/
├── README.md                    # KSI overview and references
├── KSI-{PREFIX}-{NUMBER}_questions.md    # Assessment questions (if available)
├── KSI-{PREFIX}-{NUMBER}_report.md       # Analysis and findings (if available)
├── references/                  # Research papers and materials
│   ├── cluster-a/              # Research cluster (organized by topic)
│   ├── cluster-b/
│   ├── cluster-c/
│   └── manifest.json           # Metadata for reference papers
└── changelogs/                 # Version history (if available)
```

## Reference Organization

Research materials are organized by topic clusters:

### **Common Cluster Patterns**
- **Model Security**: Model infrastructure, poisoning detection, drift monitoring, hallucinations
- **Authentication & Identity**: Auth mechanisms, credential security, biometric systems
- **Threat Detection**: Prompt injection, behavioral anomalies, attack patterns
- **Infrastructure**: Network encryption, zero-trust architecture, immutable systems
- **Compliance**: FedRAMP controls, audit logging, encryption standards
- **Supply Chain**: Vendor assessment, SBOM composition, dependency tracking

## Key Features

### Academic Research Integration
- **9,000+ peer-reviewed papers** from arXiv, IEEE, ACM, and other sources
- Papers curated by topic relevance to FedRAMP 20x requirements
- Automatic classification and clustering by security domain
- Comprehensive coverage of emerging AI security threats

### Analysis Documentation
- **Security Assessment Reports**: In-depth analysis of KSI compliance requirements
- **Threat Analysis**: Structured threat models and attack vectors
- **Implementation Guides**: Best practices and secure configuration recommendations
- **Completion Reports**: Progress tracking and milestone documentation

### Metadata Management
- `manifest.json` files track paper metadata (arXiv IDs, publication dates, relevance scores)
- Structured changelog tracking for version management
- Cross-references between related KSIs

## How to Use

### 1. **Browse a Specific KSI**
```bash
cd KSIs/KSI-AFR-01_25-12A_MinimumAssessmentScope/
cat README.md                    # Read KSI overview
cat KSI-AFR-01_report.md        # Read analysis report
cat KSI-AFR-01_questions.md     # Read assessment questions
```

### 2. **Explore Research Materials**
```bash
ls references/                   # View available research clusters
# Each cluster contains PDFs organized by research topic
```

### 3. **Access Compliance References**
- Official FedRAMP Specification: https://github.com/FedRAMP/docs
- NIST SP 800-53B: https://csrc.nist.gov/pubs/sp/800/53/b/upd1/final
- OMB Circular A-130: https://whitehouse.gov/wp-content/uploads/legacy_drupal_files/omb/circulars/A130/a130revised.pdf

## Research Coverage

### AI Security & Agentic Systems
- Prompt injection and jailbreak techniques
- Model poisoning and data integrity
- Behavioral monitoring and anomaly detection
- Multi-agent system coordination and security
- LLM hallucinations and reasoning safety
- etc.

### Operational Security
- Access control and least privilege
- Session management
- Suspicious activity detection
- Secret management and rotation
- Security metrics and KPIs
- etc.

## File Naming Conventions

- `KSI-{PREFIX}-{NUMBER}_{Description}/` - Main KSI folder
- `*_questions.md` - Assessment questions and compliance criteria
- `*_report.md` - Analysis findings and recommendations
- `cluster-{letter}_description/` - Research topic cluster
- `manifest.json` - Metadata index for papers

## Accessing FedRAMP Resources

- **FedRAMP Program**: https://fedramp.gov/
- **FedRAMP 20x Documentation**: https://fedramp.gov/docs/20x/
- **Official KSI JSON Specification**: https://github.com/FedRAMP/docs/blob/main/FRMR.KSI.key-security-indicators.json


