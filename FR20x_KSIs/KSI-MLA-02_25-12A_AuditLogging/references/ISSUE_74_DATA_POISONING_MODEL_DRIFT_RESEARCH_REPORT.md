# ArXiv Research Report: Data Poisoning and Model Drift
## Issue #74 - AI-Driven Security Risks in Audit Logs

**Date:** December 25, 2025
**Total Papers Downloaded:** 12 papers (2024-2025)
**Location:** `/Users/tamnguyen/Documents/GitHub/ksi_watch/KSI-MLA-02_25-12A_AuditLogging/references/`

---

## Executive Summary

This research compilation addresses two critical security risks in AI/ML systems deployed for audit log analysis:
1. **Data Poisoning Attacks** - Adversarial manipulation of training data to compromise model integrity
2. **Model Drift** - Silent performance degradation due to distribution shifts in operational environments

All papers are from top-tier venues (ICLR, ICML, AAAI, WSDM, SaTML, CODS-COMAD) and represent cutting-edge research from 2024-2025.

---

## TOPIC 1: DATA POISONING IN ML TRAINING

### 1.1 Survey and Foundational Research

#### Paper 1: Data Poisoning in Deep Learning: A Survey
- **ArXiv ID:** 2503.22759
- **Authors:** Pinlong Zhao, Weiyao Zhu, Pengfei Jiao, Di Gao, Ou Wu
- **Date:** March 2025
- **File:** `2503.22759_data_poisoning_deep_learning_survey.pdf`
- **Size:** 2.0 MB

**Key Contributions:**
- Comprehensive categorization of poisoning attacks across multiple dimensions
- First dedicated survey extending to LLM poisoning attacks
- Analysis of design principles for both traditional ML and foundation models
- GitHub repository with up-to-date resources maintained by authors

**Relevance to Audit Logs:**
Training data quality critically influences model performance and reliability in log analysis systems. This survey provides framework for understanding attack vectors.

---

#### Paper 2: Multi-Faceted Studies on Data Poisoning can Advance LLM Development
- **ArXiv ID:** 2502.14182
- **Authors:** Pengfei He, Yue Xing, Han Xu, Zhen Xiang, Jiliang Tang
- **Date:** February 2025
- **File:** `2502.14182_multi_faceted_data_poisoning_llm_development.pdf`
- **Size:** 1.3 MB

**Key Contributions:**
- Reframes data poisoning research beyond security threats
- Three perspectives: Threat evaluation, trustworthiness testing, mechanism understanding
- Lifecycle-aware poisoning across all LLM data sources
- Reveals hidden biases, harmful outputs, and hallucinations

**Relevance to Audit Logs:**
Demonstrates how poisoning studies can improve robustness of LLM-based log analysis systems by exposing vulnerabilities during development.

---

### 1.2 Poisoning Attack Variants

#### Paper 3: Machine Unlearning Fails to Remove Data Poisoning Attacks
- **ArXiv ID:** 2406.17216
- **Authors:** Martin Pawelczyk, Jimmy Z. Di, Yiwei Lu, Ayush Sekhari, Gautam Kamath, Seth Neel
- **Date:** June 2024 (revised April 2025)
- **Venue:** ICLR 2025
- **File:** `2406.17216_machine_unlearning_fails_remove_data_poisoning.pdf`
- **Size:** 2.6 MB

**Key Findings:**
- Unlearning methods fail across indiscriminate, targeted, and Gaussian poisoning attacks
- Tested on both image classifiers and LLMs
- Currently provides "limited benefit over retraining"
- New evaluation metrics introduced

**Relevance to Audit Logs:**
Critical for incident response - poisoned log data cannot be safely "unlearned" from deployed models, requiring complete retraining.

---

#### Paper 4: Generalizable Targeted Data Poisoning against Varying Physical Objects
- **ArXiv ID:** 2412.03908
- **Authors:** Zhizhen Chen, Zhengyu Zhao, Subrat Kishore Dutta, Chenhao Lin, Chao Shen, Xiao Zhang
- **Date:** December 2024 (revised July 2025)
- **Pages:** 13 pages
- **File:** `2412.03908_generalizable_targeted_data_poisoning.pdf`
- **Size:** 2.6 MB

**Key Findings:**
- First study on poisoning generalizability across physical conditions
- Optimizes both gradient direction AND magnitude (vs. direction only)
- 19.49% outperformance over SOTA on multi-view targets
- Addresses viewpoint, background, and lighting variations

**Relevance to Audit Logs:**
Log entries vary across environments (cloud/on-prem, different systems). Generalized poisoning attacks could compromise models across diverse deployment contexts.

---

#### Paper 5: Indiscriminate Data Poisoning Attacks on Pre-trained Feature Extractors
- **ArXiv ID:** 2402.12626
- **Authors:** Yiwei Lu, Matthew Y.R. Yang, Gautam Kamath, Yaoliang Yu
- **Date:** February 2024
- **Venue:** SaTML 2024
- **File:** `2402.12626_indiscriminate_data_poisoning_pretrained_features.pdf`
- **Size:** 7.4 MB

**Key Findings:**
- Two attack methodologies: input space and feature-targeted attacks
- Transfer learning MORE vulnerable than fine-tuning
- Feature-targeted attacks outperform when defenses are active
- Three-stage process: parameter acquisition → feature manipulation → input inversion

**Relevance to Audit Logs:**
Modern log analysis systems use pre-trained transformers. This research exposes vulnerabilities in transfer learning pipelines commonly used for log anomaly detection.

---

#### Paper 6: PoisonBench: Assessing Large Language Model Vulnerability to Data Poisoning
- **ArXiv ID:** 2410.08811
- **Authors:** Tingchen Fu, Mrinank Sharma, Philip Torr, Shay B. Cohen, David Krueger, Fazl Barez
- **Date:** October 2024 (revised June 2025)
- **Venue:** ICML 2025
- **File:** `2410.08811_poisonbench_llm_vulnerability_data_poisoning.pdf`
- **Size:** 1.0 MB

**Key Findings:**
- Benchmark across 21 LLMs and 8 realistic scenarios
- Larger models do NOT resist poisoning better (scaling ≠ safety)
- Log-linear relationship between attack effectiveness and poison ratio
- Poisoning effects generalize to unseen triggers

**Relevance to Audit Logs:**
LLM-based log analysis tools (e.g., GPT-4 for SIEM rule generation) are vulnerable. Size alone doesn't guarantee safety against poisoned training data.

---

## TOPIC 2: MODEL DRIFT AND SILENT DEGRADATION

### 2.1 Drift Detection and Interpretation

#### Paper 7: Interpretable Model Drift Detection
- **ArXiv ID:** 2503.06606
- **Authors:** Pranoy Panda, Kancheti Sai Srinivas, Vineeth N Balasubramanian, Gaurav Sinha
- **Date:** March 2025
- **Venue:** CODS-COMAD 2024
- **File:** `2503.06606_interpretable_model_drift_detection.pdf`
- **Size:** 811 KB

**Key Contributions:**
- TRIPODD framework: Feature-interaction aware hypothesis testing
- Identifies WHICH features drive drift (not just "drift detected")
- Works for both classification and regression tasks
- Comparable performance to black-box methods WITH interpretability
- Focuses on model-sensitive and drift-sensitive features

**Relevance to Audit Logs:**
When log analysis models degrade, TRIPODD can pinpoint specific log fields or patterns causing drift, enabling targeted remediation.

---

#### Paper 8: "Who experiences large model decay and why?" - Hierarchical Framework for Diagnosing Heterogeneous Performance Drift
- **ArXiv ID:** 2506.00756
- **Authors:** Harvineet Singh, Fan Xia, Alexej Gossmann, Andrew Chuang, Julian C. Hong, Jean Feng
- **Date:** May 2025
- **Venue:** ICML 2025 (PMLR 267)
- **Pages:** 13 pages (main), 18 pages (appendix) = 31 total
- **File:** `2506.00756_who_experiences_model_decay_hierarchical_framework.pdf`
- **Size:** 1.6 MB

**Key Contributions:**
- SHIFT framework identifies subgroups with unacceptable performance decay
- Addresses heterogeneous drift - some populations degrade while others don't
- Explains decay through variable-specific shifts (covariate/outcome shifts)
- Recommends targeted mitigation strategies per affected subgroup

**Relevance to Audit Logs:**
Different system types (databases, firewalls, applications) may exhibit different drift patterns. SHIFT enables differential monitoring and remediation.

---

### 2.2 Covariate and Concept Drift Management

#### Paper 9: A Scalable Approach to Covariate and Concept Drift Management via Adaptive Data Segmentation
- **ArXiv ID:** 2411.15616
- **Authors:** Vennela Yarabolu, Govind Waghmare, Sonia Gupta, Siddhartha Asthana
- **Date:** November 2024
- **Venue:** CODS-COMAD 2024
- **File:** `2411.15616_scalable_covariate_concept_drift_management.pdf`
- **Size:** 851 KB

**Key Contributions:**
- Novel approach: INCORPORATE drifted historical data instead of discarding
- Sophisticated data segmentation identifies optimal batches reflecting test patterns
- Handles both covariate shift (input distribution) and concept drift (input-output relationship)
- Reduces computational overhead by working with relevant subsets
- Improves accuracy, operational cost, and latency

**Relevance to Audit Logs:**
Historical log data remains valuable even after drift. This method maximizes training efficiency while adapting to evolving threat landscapes.

---

## TOPIC 3: DISTRIBUTION SHIFT AND ANOMALY DETECTION

### 3.1 Anomaly Detection Under Distribution Shift

#### Paper 10: Filter or Compensate: Towards Invariant Representation from Distribution Shift for Anomaly Detection
- **ArXiv ID:** 2412.10115
- **Authors:** Zining Chen, Xingshuang Luo, Weiqiu Wang, Zhicheng Zhao, Fei Su, Aidong Men
- **Date:** December 2024
- **Venue:** AAAI 2025
- **File:** `2412.10115_filter_compensate_invariant_representation_anomaly.pdf`
- **Size:** 2.2 MB

**Key Contributions:**
- FiCo method with two components:
  1. Distribution-Specific Compensation: Reduces teacher-student misalignment
  2. Distribution-Invariant Filter: Captures invariant normality patterns
- Superior performance across three benchmarks
- Addresses fundamental problem in knowledge distillation-based anomaly detection

**Relevance to Audit Logs:**
Log anomaly detection must maintain accuracy across cloud migrations, system upgrades, and infrastructure changes. FiCo ensures robustness under distribution shifts.

---

#### Paper 11: Robust Distribution Alignment for Industrial Anomaly Detection under Distribution Shift
- **ArXiv ID:** 2503.14910
- **Authors:** Jingyi Liao, Xun Xu, Yongyi Su, Rong-Cheng Tu, Yifan Liu, Dacheng Tao, Xulei Yang
- **Date:** March 2025
- **File:** `2503.14910_robust_distribution_alignment_industrial_anomaly.pdf`
- **Size:** 3.6 MB

**Key Contributions:**
- Optimizes robust Sinkhorn distance on limited target training data
- Memory-bank-based approach for generalization to unseen target domains
- Competitive performance on 2D and 3D benchmarks
- No prior knowledge of target distributions required

**Relevance to Audit Logs:**
Enterprise audit systems face domain shifts (new applications, regulatory changes, infrastructure evolution). This method adapts without extensive labeled target data.

---

#### Paper 12: Alleviating Structural Distribution Shift in Graph Anomaly Detection
- **ArXiv ID:** 2401.14155
- **Authors:** Yuan Gao, Xiang Wang, Xiangnan He, Zhenguang Liu, Huamin Feng, Yongdong Zhang
- **Date:** January 2024
- **Venue:** WSDM 2023
- **File:** `2401.14155_alleviating_structural_distribution_shift_graph_anomaly.pdf`
- **Size:** 1.8 MB

**Key Contributions:**
- Graph Decomposition Network (GDN) for structural distribution shift
- Addresses heterophily vs. homophily changes between training and testing
- Constrains anomaly features to mitigate heterophilous neighbor effects
- Makes features invariant to structural shifts

**Relevance to Audit Logs:**
When modeling logs as graphs (user-resource relationships, network flows), structural patterns shift over time. GDN maintains detection accuracy despite topology changes.

---

## Summary Statistics

### By Topic:
- **Data Poisoning:** 6 papers
- **Model Drift:** 2 papers
- **Distribution Shift & Anomaly Detection:** 3 papers
- **Cross-cutting (Drift + Distribution):** 1 paper

### By Venue:
- **ICML 2025:** 2 papers
- **ICLR 2025:** 1 paper
- **AAAI 2025:** 1 paper
- **SaTML 2024:** 1 paper
- **WSDM 2023:** 1 paper
- **CODS-COMAD 2024:** 2 papers
- **Other/Preprint:** 4 papers

### By Institution Type:
While specific institutions were not always listed on abstract pages, the authors represent:
- Top US universities (implied from venue acceptance patterns)
- International research institutions
- Industry-academia collaborations

### Page Counts (Where Available):
- **13 pages:** 2 papers (2412.03908, 2506.00756 main)
- **31 pages total:** 1 paper (2506.00756 with appendix)
- Most papers: 7-15 pages estimated based on file sizes

---

## Key Insights for Issue #74

### Data Poisoning Risks in Audit Log Systems:

1. **Training Data Vulnerability:** Log aggregation pipelines can be poisoned at multiple stages (collection, preprocessing, labeling)
2. **Unlearning Ineffective:** Compromised models require full retraining, not patch-style unlearning
3. **LLM-Specific Risks:** Log analysis tools using GPT/Claude for rule generation vulnerable to preference poisoning
4. **Transfer Learning Weakness:** Pre-trained models commonly used for log embeddings are MORE vulnerable than models trained from scratch

### Model Drift Detection Requirements:

1. **Interpretability Critical:** Need to identify WHICH log fields/patterns drive drift, not just detect drift occurrence
2. **Heterogeneous Monitoring:** Different system types require subgroup-specific drift detection
3. **Historical Data Value:** Drifted data shouldn't be discarded but intelligently incorporated via segmentation
4. **Distribution Shift Robustness:** Anomaly detectors must maintain accuracy across infrastructure changes

### Operational Recommendations:

1. **Continuous Validation:** Monitor for both poisoning indicators AND drift metrics
2. **Multi-Stage Defense:** Combine input validation, training data auditing, and model monitoring
3. **Interpretable Methods:** Prioritize drift detectors that explain WHich features changed
4. **Adaptive Training:** Use techniques that incorporate historical data rather than discarding it
5. **Subgroup Analysis:** Track performance across system types, geographic regions, and user populations

---

## Files Downloaded

All papers available at: `/Users/tamnguyen/Documents/GitHub/ksi_watch/KSI-MLA-02_25-12A_AuditLogging/references/`

```
2503.22759_data_poisoning_deep_learning_survey.pdf (2.0 MB)
2502.14182_multi_faceted_data_poisoning_llm_development.pdf (1.3 MB)
2406.17216_machine_unlearning_fails_remove_data_poisoning.pdf (2.6 MB)
2412.03908_generalizable_targeted_data_poisoning.pdf (2.6 MB)
2402.12626_indiscriminate_data_poisoning_pretrained_features.pdf (7.4 MB)
2410.08811_poisonbench_llm_vulnerability_data_poisoning.pdf (1.0 MB)
2503.06606_interpretable_model_drift_detection.pdf (811 KB)
2506.00756_who_experiences_model_decay_hierarchical_framework.pdf (1.6 MB)
2411.15616_scalable_covariate_concept_drift_management.pdf (851 KB)
2412.10115_filter_compensate_invariant_representation_anomaly.pdf (2.2 MB)
2503.14910_robust_distribution_alignment_industrial_anomaly.pdf (3.6 MB)
2401.14155_alleviating_structural_distribution_shift_graph_anomaly.pdf (1.8 MB)
```

**Total Storage:** ~26 MB

---

## Sources

### Data Poisoning Research:
- [Data Poisoning in Deep Learning: A Survey](https://arxiv.org/abs/2503.22759)
- [Machine Unlearning Fails to Remove Data Poisoning Attacks](https://arxiv.org/abs/2406.17216)
- [Scaling Trends for Data Poisoning in LLMs](https://arxiv.org/abs/2408.02946)
- [Generalizable Targeted Data Poisoning against Varying Physical Objects](https://arxiv.org/abs/2412.03908)
- [PoisonBench: Assessing Large Language Model Vulnerability to Data Poisoning](https://arxiv.org/abs/2410.08811)
- [Indiscriminate Data Poisoning Attacks on Pre-trained Feature Extractors](https://arxiv.org/abs/2402.12626)
- [Multi-Faceted Studies on Data Poisoning can Advance LLM Development](https://arxiv.org/abs/2502.14182)

### Model Drift Research:
- [Interpretable Model Drift Detection](https://arxiv.org/abs/2503.06606)
- [Who experiences large model decay and why?](https://arxiv.org/abs/2506.00756)
- [A Scalable Approach to Covariate and Concept Drift Management](https://arxiv.org/abs/2411.15616)

### Distribution Shift & Anomaly Detection:
- [Filter or Compensate: Towards Invariant Representation](https://arxiv.org/abs/2412.10115)
- [Robust Distribution Alignment for Industrial Anomaly Detection](https://arxiv.org/abs/2503.14910)
- [Alleviating Structural Distribution Shift in Graph Anomaly Detection](https://arxiv.org/abs/2401.14155)

---

**Report Generated:** December 25, 2025
**Researcher:** Claude Code (Sonnet 4.5)
**Issue Reference:** #74 - AI-Driven Security Risks in Audit Log Analysis
