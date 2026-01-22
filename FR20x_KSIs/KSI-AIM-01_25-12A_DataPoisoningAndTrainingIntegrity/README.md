# KSI-AIM-01: Data Poisoning & Training Integrity

## Overview

This KSI focuses on preventing, detecting, and remediating data poisoning attacks that corrupt AI training datasets. Data poisoning represents a critical supply-chain risk for AI systems, where attackers inject malicious data into training pipelines, degrading model accuracy silently (22-27% accuracy loss) while remaining undetected for months.

## Context

- **Threat**: Attackers poison training datasets through GitHub repositories, public datasets, and third-party data sources
- **Impact**: 22-27% accuracy degradation; 100% backdoor success at 2% poison ratio; undetected for months until incident discovery
- **Challenge**: Byzantine-resilient aggregation required for distributed training with compromised data sources
- **Defense**: Multi-stage validation, supplier assessment, continuous monitoring, class imbalance handling

## Key Questions

5 discovery questions address:
1. Data poisoning attack detection (threat model, detection mechanisms, attack types)
2. Training data provenance validation (source auditing, integrity checks, supplier assessment)
3. Byzantine-resilient aggregation for distributed training (tolerance thresholds, algorithms)
4. Implicit poisoning detection via malicious logs (crafted log detection, retraining validation)
5. Clean data validation and class balance management (43% F1 improvement with proper handling)

## Research Metrics

- **Accuracy Degradation**: 22-27% from poisoning (ensemble defenses restore 15-20%)
- **Detection Success**: 85.77% for baseline poisoning detection
- **Class Imbalance Impact**: 10x per-attack-type variance; 1000 benign vs. 10 attack examples
- **Retraining Efficiency**: 76.6% sample reduction possible with clean data validation

## Relationship to Other KSIs

- **KSI-MLA-02** (Audit Logging): Data poisoning questions moved here from MLA-02 to focus MLA-02 on logging architecture
- **KSI-AIM-02** (Model Drift): Complementary KSI addressing runtime model health and degradation
- **KSI-AIM-04** (Governance): Investment justification for data poisoning defenses

## File Structure

```
KSI-AIM-01_25-12A_DataPoisoningAndTrainingIntegrity/
├── KSI-AIM-01_questions.md      # 5 discovery questions
└── README.md                     # This file
```

## Created From

- **Source**: KSI-MLA-02 (Issue #35 scope refinement)
- **Extraction**: Questions Q16-Q20 from original 40-question set
- **Rationale**: Better domain alignment—data poisoning is training/ML pipeline robustness, not logging per se

## Next Steps

1. Add research papers supporting data poisoning defense mechanisms
2. Develop recommendations for Byzantine-resilient aggregation selection
3. Create compliance mapping (NIST AI RMF, EU AI Act)
4. Add case studies of detected and prevented poisoning attacks
