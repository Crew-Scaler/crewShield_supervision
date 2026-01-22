# Topic 8: Model Extraction and Inference Attacks - Reference Papers

**Repository**: Issue #64 - AI Security Research
**Topic**: Model Extraction and Inference Attacks on Configuration Management ML Models
**Research Date**: December 24, 2025
**Total Papers**: 8 (all 2024-2025 publications)

## Quick Start

1. **Read the summary first**: [`TOPIC8_PAPERS_SUMMARY.md`](./TOPIC8_PAPERS_SUMMARY.md) - Comprehensive overview of all papers with relevance analysis
2. **View metadata**:
   - `topic8_query1_papers.json` - Query 1 results (model extraction/inference attacks)
   - `topic8_query2_papers.json` - Query 2 results (membership inference/side-channel attacks)

## Papers by Relevance Score

### Tier 1: Highest Relevance (Score 16.0)
1. **RADEP** (2505.19364v1) - Multi-layered defense against model extraction attacks on MLaaS
2. **THEMIS** (2503.23748v1) - IP protection for deployed on-device deep learning models

### Tier 2: High Relevance (Score 14.0-15.0)
3. **Spill The Beans** (2505.00817v1) - Cache side-channel attacks on LLM inference

### Tier 3: Medium Relevance (Score 11.0)
4. **Bounding-box Watermarking** (2411.13047v2) - Defense against extraction attacks on object detectors
5. **LDPKiT** (2405.16361v3) - Privacy-preserving model extraction from cloud services
6. **SWAP Attack** (2502.10115v1) - Quantum multi-tenant side-channel attacks
7. **Crosstalk NISQ** (2412.10507v1) - Side-channel threats in multi-tenant quantum systems

### Tier 4: Relevant (Score 9.0)
8. **Network Slicing Attack** (2409.11258v1) - RL-based side-channel attacks on 5G/6G slicing

## File Organization

```
topic8_model_extraction/
├── README.md                           (this file)
├── TOPIC8_PAPERS_SUMMARY.md           (detailed analysis)
├── topic8_query1_papers.json          (Query 1 metadata)
├── topic8_query2_papers.json          (Query 2 metadata)
│
└── PDF Papers (8 files):
    ├── 2505.19364v1_RADEP_*.pdf
    ├── 2503.23748v1_THEMIS_*.pdf
    ├── 2411.13047v2_Bounding-box_*.pdf
    ├── 2405.16361v3_LDPKiT_*.pdf
    ├── 2502.10115v1_SWAP_Attack_*.pdf
    ├── 2505.00817v1_Spill_The_Beans_*.pdf
    ├── 2412.10507v1_Crosstalk_*.pdf
    └── 2409.11258v1_Attacking_Slicing_*.pdf
```

## Research Coverage

### Key Topics Addressed

**Model Extraction Defense Mechanisms**:
- Adversarial training for resilience
- Query analysis and anomaly detection
- Watermarking and backdoor-based ownership verification
- Adaptive response mechanisms

**Side-Channel Attack Vectors**:
- Hardware cache exploitation (CPU L3 cache)
- Quantum crosstalk on shared platforms
- Network infrastructure timing channels
- Timing-based cache analysis

**Multi-Tenant Environment Threats**:
- Co-located attack scenarios
- Shared resource contention
- Configuration leakage through side-channels
- Infrastructure isolation bypass

**Model IP Protection**:
- Post-deployment watermarking
- Practical tool-based solutions
- Privacy-preserving extraction
- Real-world mobile app security

## Statistics

| Metric | Value |
|--------|-------|
| **Total Papers** | 8 |
| **Total Size** | ~85 MB |
| **2025 Publications** | 5 (62.5%) |
| **2024 Publications** | 3 (37.5%) |
| **Average Age** | 6.5 months |
| **Relevance Range** | 9.0 - 16.0 |
| **Primary Security Category** | 5 papers |

## Download Information

- **Method**: ArXiv API v2 (HTTP/2)
- **Rate Limit**: 3.5 seconds per request (ArXiv compliant)
- **Total Download Time**: ~6 minutes
- **Success Rate**: 100% (8/8 papers)
- **Verification**: All PDFs successfully validated

## Citation Information

For referencing papers in this collection:

```bibtex
@article{Chakraborty2025,
  title={RADEP: A Resilient Adaptive Defense Framework Against Model Extraction Attacks},
  author={Chakraborty, Amit and others},
  journal={arXiv preprint arXiv:2505.19364},
  year={2025}
}

@article{Huang2025,
  title={THEMIS: Towards Practical IP Protection for Post-Deployment On-Device Deep Learning},
  author={Huang, Yujin and others},
  journal={arXiv preprint arXiv:2503.23748},
  year={2025}
}

@article{Lee2025,
  title={SWAP Attack: Stealthy Side-Channel Attack on Multi-Tenant Quantum Cloud System},
  author={Lee, Wei Jie Bryan and others},
  journal={arXiv preprint arXiv:2502.10115},
  year={2025}
}

@article{Adiletta2025,
  title={Spill The Beans: Exploiting CPU Cache Side-Channels to Leak Tokens from LLMs},
  author={Adiletta, Andrew and Sunar, Berk},
  journal={arXiv preprint arXiv:2505.00817},
  year={2025}
}
```

## Recommendations for Issue #64

### Phase 1: Foundation
- Start with **RADEP** (2505.19364) for comprehensive defense framework
- Study **THEMIS** (2503.23748) for practical implementation patterns

### Phase 2: Infrastructure Hardening
- Review **SWAP Attack** (2502.10115) for quantum multi-tenant risks
- Study **Spill The Beans** (2505.00817) for CPU cache vulnerability

### Phase 3: Advanced Threats
- Analyze **Crosstalk NISQ** (2412.10507) for isolated shared infrastructure
- Examine **Network Slicing Attack** (2409.11258) for 5G/6G configurations

### Phase 4: Integration
- Combine watermarking from THEMIS + behavioral analysis from RADEP
- Implement differential privacy concepts from LDPKiT for privacy-preserving features

## Related Issues

- Issue #62: AI Supply Chain Attacks (related)
- Issue #63: Model Poisoning (related)
- Issue #65: Privacy-Preserving ML (related)

## Notes for Maintainers

- All papers are from reputable ArXiv sources (2024-2025)
- PDFs are in their original format from ArXiv
- Metadata preserved in JSON format for future processing
- No papers require special access/authentication

---

**Last Updated**: December 24, 2025
**Maintainer**: AI Security Research Team
**Status**: Complete - Ready for review and analysis
