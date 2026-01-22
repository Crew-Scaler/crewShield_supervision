# Metrics Extraction Guide for Issue #15 Research Papers

**Purpose:** Systematic extraction of quantified performance metrics from 45 credential security defense papers

**Target Directory:** `/Users/tamnguyen/Documents/GitHub/ksi_watch/KSI-IAM-02_25-12A_PasswordlessAuthentication/references/credential_security_defense`

---

## Critical Metrics to Extract

### 1. Detection Performance Metrics

#### Accuracy Metrics
- [ ] **True Positive Rate (TPR) / Recall / Sensitivity**
  - Format: X.XX% or 0.XXX
  - Context: Detection of actual credential compromises/anomalies

- [ ] **False Positive Rate (FPR)**
  - Format: X.XX% or 0.XXX
  - Context: Normal behavior incorrectly flagged as anomalous

- [ ] **True Negative Rate (TNR) / Specificity**
  - Format: X.XX% or 0.XXX
  - Context: Normal behavior correctly identified

- [ ] **False Negative Rate (FNR) / Miss Rate**
  - Format: X.XX% or 0.XXX
  - Context: Actual attacks/compromises missed

- [ ] **Precision / Positive Predictive Value (PPV)**
  - Format: X.XX% or 0.XXX
  - Context: Proportion of flagged cases that are actual attacks

- [ ] **F1 Score / F-Measure**
  - Format: 0.XXX
  - Context: Harmonic mean of precision and recall

- [ ] **Accuracy**
  - Format: X.XX% or 0.XXX
  - Context: Overall correct classifications (TP+TN)/(Total)

- [ ] **AUC-ROC (Area Under Curve - Receiver Operating Characteristic)**
  - Format: 0.XXX
  - Context: Overall model performance across thresholds

#### Behavioral Biometrics Specific
- [ ] **Equal Error Rate (EER)**
  - Format: X.XX%
  - Context: Point where FAR = FRR
  - Lower is better

- [ ] **False Acceptance Rate (FAR)**
  - Format: X.XX%
  - Context: Unauthorized users incorrectly authenticated

- [ ] **False Rejection Rate (FRR)**
  - Format: X.XX%
  - Context: Legitimate users incorrectly rejected

---

### 2. Timing and Latency Metrics

- [ ] **Detection Latency / Time to Detect**
  - Format: XXX ms/seconds/minutes
  - Context: Time from anomaly occurrence to detection alert

- [ ] **Mean Time to Detect (MTTD)**
  - Format: XXX seconds/minutes/hours
  - Context: Average time to detect compromise/anomaly

- [ ] **Mean Time to Respond (MTTR)**
  - Format: XXX seconds/minutes/hours
  - Context: Time from detection to mitigation action

- [ ] **Processing Time per Sample/Request**
  - Format: XXX ms/microseconds
  - Context: Time to analyze single authentication event

- [ ] **Training Time**
  - Format: XXX minutes/hours
  - Context: Time to train ML model

- [ ] **Inference Time**
  - Format: XXX ms
  - Context: Time to make prediction on new data

---

### 3. Scalability and Performance Metrics

- [ ] **Throughput**
  - Format: XXX events/second, requests/second
  - Context: Maximum processing rate

- [ ] **Concurrent Users Supported**
  - Format: XXX,XXX users
  - Context: Number of simultaneous users monitored

- [ ] **Data Volume**
  - Format: XXX GB/TB per day
  - Context: Log/event data processed

- [ ] **CPU Utilization**
  - Format: XX%
  - Context: Processor usage during operation

- [ ] **Memory Usage**
  - Format: XXX MB/GB
  - Context: RAM requirements

- [ ] **Network Bandwidth**
  - Format: XXX Mbps/Gbps
  - Context: Network traffic for monitoring

- [ ] **Storage Requirements**
  - Format: XXX GB/TB
  - Context: Disk space for logs/models

---

### 4. Dataset and Experimental Setup

- [ ] **Dataset Name**
  - Example: CERT Insider Threat, KDD Cup 99, UNSW-NB15

- [ ] **Dataset Size**
  - Format: XXX,XXX samples/events

- [ ] **Attack/Anomaly Percentage**
  - Format: X.XX%
  - Context: Class imbalance ratio

- [ ] **Training/Test Split**
  - Format: XX/XX%

- [ ] **Cross-Validation Folds**
  - Format: X-fold

- [ ] **Baseline Comparisons**
  - List of compared methods and their performance

---

### 5. Deployment and Operational Metrics

- [ ] **Deployment Complexity**
  - Scale: Low/Medium/High
  - Description: Installation and configuration effort

- [ ] **Integration Requirements**
  - List: APIs, protocols, dependencies

- [ ] **Maintenance Overhead**
  - Description: Model retraining frequency, rule updates

- [ ] **False Alarm Workload**
  - Format: XXX alerts/day requiring human review

- [ ] **Alert Fatigue Impact**
  - Description: Sustainability of false positive rate

---

## Priority Papers with Expected High-Value Metrics

### Tier 1: Must Extract (Recent + Quantified)

1. **IDU-Detector** (2411.06172v1)
   - Expected: TPR, FPR, F1, Detection latency, Baseline comparisons
   - Focus: Masquerader attack detection accuracy

2. **Lateral Movement Detection** (2411.10279v1)
   - Expected: Time-to-detect, Accuracy, Precision/Recall, Graph size scalability
   - Focus: Authentication log analysis performance

3. **Mouse Dynamics Optimization** (2504.21415v2)
   - Expected: EER, FAR, FRR, Data sufficiency thresholds, Accuracy-practicality trade-off
   - Focus: Behavioral authentication performance

4. **Machine Learning Security Policy** (2501.00085v2)
   - Expected: Policy analysis accuracy, Processing time, Scalability
   - Focus: Automated policy validation metrics

5. **In-Application Defense** (2412.07005v1)
   - Expected: Detection rate, FPR, Response time, Throughput
   - Focus: Real-time behavioral analysis

### Tier 2: High Value (Production Systems)

6. **ADSAGE** (2007.06985v1)
   - Expected: Fine-grained detection accuracy, Graph processing time

7. **Enterprise Isolation Forest** (1609.06676v1)
   - Expected: Enterprise-scale metrics, False alarm rates, Operational overhead

8. **Real-Time Mitigation IEC 61850** (2511.18748v1)
   - Expected: MTTD, MTTR, Critical infrastructure latency requirements

9. **Federated Learning IoT** (2211.05662v1)
   - Expected: Distributed system performance, Privacy metrics, Convergence time

10. **HRGCN Graph Anomaly** (2308.14340v1)
    - Expected: GNN accuracy, Graph size limits, Training/inference time

### Tier 3: Specialized Metrics (Behavioral Biometrics)

11. **Keystroke Dynamics Review** (2502.16177v1)
    - Expected: Comprehensive EER comparison across methods

12. **Eye-tracking VR** (2502.20359v1)
    - Expected: Long-term performance degradation metrics

13. **Touch-Based Contrastive Learning** (2504.17271v1)
    - Expected: Mobile authentication accuracy, Resource usage

14. **Agent-Based Keystroke** (2505.05015v1)
    - Expected: Free-text authentication performance

15. **BlowPrint Biometrics** (2507.04126v1)
    - Expected: Multi-factor authentication improvement metrics

---

## Extraction Methodology

### Step 1: Quick Scan
1. Search PDF for: "accuracy", "precision", "recall", "F1", "EER", "latency", "detection time"
2. Locate "Results", "Evaluation", "Experiments" sections
3. Identify tables and figures with performance data

### Step 2: Structured Extraction
1. Create spreadsheet with metrics as columns
2. Extract exact values with context
3. Note experimental conditions (dataset, setup)
4. Record baseline comparisons

### Step 3: Validation
1. Verify metric definitions match expected interpretations
2. Check for conflicting or unclear metrics
3. Note assumptions and limitations
4. Flag papers with missing critical metrics

### Step 4: Synthesis
1. Calculate metric ranges across papers
2. Identify best-performing approaches
3. Correlate metrics (e.g., accuracy vs. latency trade-offs)
4. Document implementation complexity vs. performance

---

## Metrics Template (JSON Format)

```json
{
  "paper_id": "2411.06172v1",
  "title": "IDU-Detector: A Synergistic Framework for Robust Masquerader Attack Detection",
  "metrics": {
    "detection_performance": {
      "accuracy": 0.XX,
      "precision": 0.XX,
      "recall": 0.XX,
      "f1_score": 0.XX,
      "fpr": 0.XX,
      "auc_roc": 0.XX
    },
    "timing": {
      "detection_latency_ms": XXX,
      "inference_time_ms": XXX,
      "training_time_hours": XXX
    },
    "scalability": {
      "throughput_events_per_sec": XXX,
      "concurrent_users": XXX,
      "memory_usage_gb": XXX
    },
    "dataset": {
      "name": "DATASET_NAME",
      "size": XXX,
      "attack_percentage": 0.XX,
      "train_test_split": "XX/XX"
    },
    "baselines": [
      {
        "method": "BASELINE_METHOD",
        "accuracy": 0.XX,
        "f1_score": 0.XX
      }
    ],
    "notes": "Additional context or caveats"
  }
}
```

---

## Expected Metric Ranges (From Preliminary Review)

### Detection Accuracy
- **State-of-the-Art:** 95-99% accuracy
- **Production Acceptable:** 90-95% accuracy
- **Research Baseline:** 80-90% accuracy

### False Positive Rate
- **Excellent:** <1% FPR
- **Good:** 1-5% FPR
- **Acceptable:** 5-10% FPR
- **High (operational burden):** >10% FPR

### Detection Latency
- **Real-time:** <100ms
- **Near real-time:** 100ms-1s
- **Interactive:** 1-10s
- **Batch:** >10s

### Behavioral Biometrics EER
- **Excellent:** <2% EER
- **Good:** 2-5% EER
- **Acceptable:** 5-10% EER
- **Weak:** >10% EER

---

## Common Metrics Tables to Look For

### Table Types Often Containing Key Metrics

1. **Comparison Tables**
   - "Comparison with state-of-the-art methods"
   - "Performance comparison"
   - "Results on benchmark datasets"

2. **Ablation Studies**
   - "Component contribution analysis"
   - "Feature importance"
   - "Architecture variations"

3. **Scalability Tables**
   - "Performance vs. dataset size"
   - "Time complexity analysis"
   - "Resource utilization"

4. **ROC Curves and Confusion Matrices**
   - Often in figures rather than tables
   - Extract TPR, FPR, precision, recall

---

## Red Flags and Limitations

### Watch Out For:

1. **Unrealistic Datasets**
   - Synthetic data only
   - Extremely imbalanced classes
   - Small sample sizes (<1,000 samples)

2. **Missing Baselines**
   - No comparison with existing methods
   - Only absolute metrics, no relative performance

3. **Incomplete Metrics**
   - Only accuracy reported (no precision/recall)
   - No timing or scalability data
   - Missing false positive rates

4. **Unclear Experimental Setup**
   - No train/test split specified
   - No cross-validation
   - Overfitting indicators (training acc >> test acc)

5. **Production Viability Issues**
   - Extremely long training times (>24 hours)
   - Massive resource requirements
   - Unrealistic latency assumptions

---

## Output Deliverables

After extraction, produce:

1. **Metrics Database** (JSON/CSV)
   - All extracted metrics in structured format
   - Paper ID, metric name, value, context

2. **Comparison Matrix** (Markdown Table)
   - Papers as rows
   - Key metrics as columns
   - Color-coded performance tiers

3. **Top Performers Summary**
   - Highest accuracy approaches
   - Lowest latency methods
   - Best accuracy/latency trade-off
   - Most scalable solutions

4. **Gaps Analysis**
   - Missing metrics across papers
   - Underexplored attack scenarios
   - Limited deployment studies

5. **Implementation Recommendations**
   - Recommended approaches for Issue #15
   - Metric targets for validation
   - Architecture patterns to adopt

---

## Timeline Estimate

- **Tier 1 Papers (5 papers):** 2-3 hours (detailed extraction)
- **Tier 2 Papers (5 papers):** 1.5-2 hours
- **Tier 3 Papers (5 papers):** 1.5-2 hours
- **Remaining Papers (30 papers):** 3-4 hours (quick scan)
- **Synthesis and Documentation:** 2-3 hours

**Total Estimated Time:** 10-14 hours

---

## Tools for Extraction

### Recommended Tools

1. **PDF Search:** Use PDF reader's search function for metric keywords
2. **Table Extraction:** Tools like Tabula, Camelot, or pdfplumber
3. **Spreadsheet:** Google Sheets or Excel for metrics database
4. **Automation:** Python script for batch text extraction from PDFs

### Sample Python Script Skeleton

```python
import PyPDF2
import re
import json

def extract_metrics(pdf_path):
    """Extract performance metrics from research paper PDF."""
    metrics = {
        "accuracy": [],
        "precision": [],
        "recall": [],
        "f1_score": [],
        "latency": []
    }

    # Open PDF and extract text
    # Search for metric patterns
    # Parse values and context
    # Return structured metrics

    return metrics
```

---

## Success Criteria

The metrics extraction is complete when:

1. ✅ All Tier 1 papers have complete metric profiles
2. ✅ At least 80% of papers have accuracy metrics
3. ✅ At least 60% of papers have timing/latency data
4. ✅ Comparison matrix enables clear ranking of approaches
5. ✅ Sufficient data to make implementation recommendations for Issue #15
6. ✅ Metric ranges established for validation targets

---

## Contact / Notes

- Papers with exceptionally high-quality metrics should be flagged for detailed review
- Papers with production deployment case studies are priority for operational metrics
- Note any papers that provide open-source implementations (GitHub links)
- Flag papers with reproducibility concerns (missing details, unclear methods)

---

**Next Action:** Begin with Tier 1 papers, focus on detection performance and timing metrics first, then expand to scalability and operational metrics.
