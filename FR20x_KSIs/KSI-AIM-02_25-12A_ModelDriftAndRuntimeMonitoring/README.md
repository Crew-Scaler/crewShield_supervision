# KSI-AIM-02: Model Drift & Runtime Monitoring

## Overview

This KSI focuses on detecting and mitigating model degradation in production AI systems. Concept drift, where model accuracy degrades silently over time, represents a critical operational risk: 91% of production ML systems degrade undetectably, with 2-3% accuracy loss occurring before SLO violations become apparent.

## Context

- **Threat**: Silent model degradation in production; 91% of systems degrade undetectably
- **Impact**: Advanced threats (APT) exploit degraded detection (45% vs. 99% common threats); undetected degradation spans weeks/months
- **Challenge**: Distinguish natural drift (legitimate infrastructure changes) from adversarial drift (attacker evasion)
- **Defense**: Interpretable drift detection (TRIPODD-style), per-attack-type metrics, rapid baseline establishment in ephemeral environments

## Key Questions

4 discovery questions address:
1. Baseline degradation monitoring (MTTD <24 hours, detection mechanisms, research validation)
2. Concept drift vs. adversarial drift distinction (drift attribution, explainability, differential response)
3. Baseline poisoning prevention during learning phase (ensemble voting, outlier filtering, baseline versioning)
4. MTTD metrics and measurement (detection latency, research comparison to industry baseline)

## Research Metrics

- **Degradation Rate**: 91% of ML systems degrade undetectably
- **Detection Timeline**: 2-3% accuracy loss before apparent SLO violation; undetected for weeks/months
- **Target MTTD**: <24 hours for drift detection
- **Drift Detection Success**: 85.77% with explainability (TRIPODD-style)
- **Attack Detection Variance**: 10x per-attack-type (APT 45% vs. brute-force 99%)

## Relationship to Other KSIs

- **KSI-MLA-02** (Audit Logging): Baseline monitoring in container/ephemeral environments overlaps (MLA-02-Q20); remaining drift questions moved here
- **KSI-AIM-01** (Data Poisoning): Complementary—baseline poisoning during learning phase is a specific attack variant
- **KSI-AIM-04** (Governance): Investment justification for drift detection infrastructure

## File Structure

```
KSI-AIM-02_25-12A_ModelDriftAndRuntimeMonitoring/
├── KSI-AIM-02_questions.md      # 4 discovery questions
└── README.md                     # This file
```

## Created From

- **Source**: KSI-MLA-02 (Issue #35 scope refinement)
- **Extraction**: Questions Q21-Q23, Q25 from original 40-question set; Q24 retained in MLA-02 due to container logging coupling
- **Rationale**: Model drift is runtime ML health monitoring, not audit logging implementation

## Next Steps

1. Add research papers on explainable drift detection (TRIPODD framework)
2. Develop per-attack-type detection metrics and SLO definitions
3. Create implementation guidance for rapid baseline establishment in Kubernetes
4. Add case studies of detected drift and successful remediation
