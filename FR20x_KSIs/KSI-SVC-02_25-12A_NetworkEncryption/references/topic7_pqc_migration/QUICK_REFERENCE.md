# Topic 7: PQC Migration - Quick Reference Guide

## Collection Overview
- **Location**: `/Users/tamnguyen/Documents/GitHub/ksi_watch/KSI-SVC-02_25-12A_NetworkEncryption/references/topic7_pqc_migration/`
- **Total PDFs**: 35 papers (15 highly relevant)
- **Top Papers**: 10 ranked papers in consolidated JSON
- **Total Size**: ~275 MB
- **Coverage**: 2024-2025, emphasis on 2025 papers

## Start Here - 3 Essential Files

### 1. **topic7_pqc_migration_top10_consolidated.json** ⭐⭐⭐
**The definitive ranked list of 10 most relevant papers**
- Ranked by relevance score (22.0 - 10.0)
- Includes: ArXiv ID, title, authors, year, focus area, key metrics
- JSON format for easy parsing

### 2. **README.md**
**Comprehensive guide with analysis**
- Executive summary
- Detailed paper descriptions (Rank 1-10)
- Key metrics summary table
- Algorithm recommendations by use case
- Deployment timeline
- Open research challenges

### 3. **COLLECTION_SUMMARY.txt**
**Collection statistics and metadata**
- Paper statistics
- Key metrics extracted
- Query results breakdown
- Deployment recommendations
- How to use this collection

---

## Top 10 Papers (Quick Summary)

| Rank | Score | ArXiv | Year | Title | Key Metric |
|------|-------|-------|------|-------|-----------|
| 1 | 22.0 | 2510.10436v1 | 2025 | PQC Survey | Comprehensive review |
| 2 | 20.0 | 2509.01701v2 | 2025 | AmphiKey | 0.15ms handshake (server) |
| 3 | 20.0 | 2507.17074v1 | 2025 | 5G Analysis | ML-KEM best for 5G |
| 4 | 12.0 | 2506.19943v1 | 2025 | DNS Security | Fragmentation risks |
| 5 | 11.0 | 2404.13544v2 | 2024 | ML-KEM Opt | 1.64x speedup (AVX-512) |
| 6 | 14.0 | 2502.17202v1 | 2025 | QKD+TLS | Production deployment |
| 7 | 11.0 | 2405.09264v1 | 2024 | QUIC Analysis | 10-20% overhead |
| 8 | 10.0 | 2503.17830v3 | 2025 | Fingerprinting | 100% accuracy attacks |
| 9 | 16.0 | 2512.12904v1 | 2025 | OptHQC | 55% speedup |
| 10 | 16.0 | 2512.13333v1 | 2025 | Blockchain SOK | Migration strategies |

---

## Key Metrics at a Glance

### Handshake Latency
- **Best case (optimized)**: 0.15 ms
- **Average case**: 0.41-4.8 ms
- **Typical overhead**: 10-15%

### Performance Gains
- **ML-KEM AVX-512**: 1.64x faster than AVX2
- **Batch key gen**: 3.5-4.9x acceleration
- **HQC optimization**: 55% speedup
- **Packet protection**: 10-20% overhead

### Algorithm Performance (for different use cases)

**Best for TLS/HTTPS**:
- KEM: ML-KEM-768 (NIST standard)
- Signature: ML-DSA-65

**Best for 5G/Mobile**:
- KEM: ML-KEM (low latency)
- Signature: ML-DSA (best balance)

**Best for DNS**:
- KEM: ML-KEM or Falcon
- Reason: Message size critical

**Best for QUIC/HTTP3**:
- KEM: ML-KEM, Kyber
- Signature: Dilithium, Falcon

**Best for IoT/Embedded**:
- KEM: ML-KEM (resource-efficient)
- Signature: Falcon (balanced)

---

## Which Paper To Read For...?

| Need | Paper | Rank |
|------|-------|------|
| Foundation/Overview | Survey (2510.10436v1) | 1 |
| Real deployment metrics | AmphiKey (2509.01701v2) | 2 |
| 5G/Mobile strategy | 5G Analysis (2507.17074v1) | 3 |
| Internet infrastructure | DNS Security (2506.19943v1) | 4 |
| Implementation optimization | ML-KEM Opt (2404.13544v2) | 5 |
| QKD integration | QKD+TLS (2502.17202v1) | 6 |
| Modern protocols | QUIC (2405.09264v1) | 7 |
| Security threats | Fingerprinting (2503.17830v3) | 8 |
| Code-based alternative | OptHQC (2512.12904v1) | 9 |
| Blockchain/Crypto | Disruption (2512.13333v1) | 10 |

---

## Critical Findings

### Handshake Performance
- ML-KEM/ML-DSA: 10-15% increase over classical
- SPHINCS+: Significant increase (avoid if latency-critical)
- Kyber/Dilithium: Good balance

### Certificate Sizes
- ML-DSA signatures: ~2544 bytes (vs 64 bytes for ECDSA)
- ML-KEM public keys: ~1184 bytes (vs 65 bytes for X25519)
- Overall growth: 2-4x larger

### Implementation Fingerprinting Risks
- Classical vs PQC: 98-100% detection accuracy
- Specific algorithm: 86-97% accuracy
- Mitigation: Constant-time implementations

### DNS Vulnerabilities
- Fragmentation with larger signatures
- UDP amplification attacks
- Downgrade attack risks

### Best Practices
1. Always use hybrid: Classical + PQC (forward secrecy + quantum safety)
2. Use hardware acceleration: AVX2 minimum, AVX-512 for high-throughput
3. Implement constant-time: Protect against timing attacks
4. Support crypto-agility: Multiple algorithm options
5. Plan migrations: Start non-critical → critical systems

---

## Timeline Recommendations

### 2025 (Now)
- [ ] Enable hybrid TLS 1.3 support
- [ ] Begin 5G rollout testing
- [ ] Update DNS infrastructure plans

### 2026
- [ ] Deploy on non-critical systems
- [ ] Hardware acceleration implementation
- [ ] PKI pipeline updates

### 2027-2029
- [ ] Migrate critical infrastructure
- [ ] Deprecate classical-only TLS
- [ ] Full interoperability testing

### 2030+
- [ ] Complete migration
- [ ] Legacy support phase-out
- [ ] Continued monitoring

---

## Deployment Checklist

### Immediate (Next 3 months)
- [ ] Review README.md and top 3 papers
- [ ] Extract handshake latency requirements
- [ ] Assess current TLS versions in use
- [ ] Plan hybrid TLS 1.3 rollout

### Short-term (Next 6 months)
- [ ] Test liboqs/BoringSSL integration
- [ ] Benchmark on target systems
- [ ] Develop crypto-agility policies
- [ ] Create migration playbook

### Medium-term (6-12 months)
- [ ] Pilot deployment (non-critical systems)
- [ ] Hardware acceleration evaluation
- [ ] PKI updates
- [ ] Team training

### Long-term (12+ months)
- [ ] Staged migration of critical systems
- [ ] Interoperability testing
- [ ] Performance monitoring
- [ ] Regular updates

---

## Common Questions Answered

**Q: What's the biggest challenge with PQC?**
A: Larger key/signature sizes (2-4x) leading to handshake expansion, DNS fragmentation, and certificate overhead.

**Q: Which algorithm is most ready for production?**
A: ML-KEM (NIST finalized 2024), with ML-DSA for signatures. Both have proven performance.

**Q: How much slower is PQC?**
A: Typically 10-15% handshake latency increase with optimized ML-KEM. Can optimize further with AVX-512 (1.64x).

**Q: Do we need to replace classical cryptography?**
A: No. Hybrid approach is recommended: keep classical for forward secrecy + add PQC for quantum safety.

**Q: When must we migrate?**
A: Start planning now (2025), pilot 2026, critical systems 2027-2029, full migration by 2030.

**Q: What about blockchain/cryptocurrency?**
A: Significant impacts on transaction sizes and throughput. See paper #10 (Disruption).

**Q: Are there side-channel risks?**
A: Yes, but mitigated with masking-friendly designs and constant-time implementations.

---

## Quick Links to PDFs

All PDFs are in the same directory. Access pattern: `[arxiv_id]_[title_truncated].pdf`

```
2510.10436v1_Post-Quantum_Cryptography_and_Quantum-Safe_Security_A_Comprehensive_Survey.pdf
2509.01701v2_AmphiKey_A_Dual-Mode_Secure_Authenticated_Key_Encapsulation_Protocol_for_Smart_Grid.pdf
2507.17074v1_Analysis_of_Post-Quantum_Cryptography_in_User_Equipment_in_5G_and_Beyond.pdf
2506.19943v1_Quantum-Resistant_Domain_Name_System_A_Comprehensive_System-Level_Study.pdf
2404.13544v2_Faster_Post-Quantum_TLS_13_Based_on_ML-KEM_Implementation_and_Assessment.pdf
2502.17202v1_Quantum-Safe_integration_of_TLS_in_SDN_networks.pdf
2405.09264v1_A_Quantum_of_QUIC_Dissecting_Cryptography_with_Post-Quantum_Insights.pdf
2503.17830v3_Fingerprinting_Implementations_of_Cryptographic_Primitives_and_Protocols_that_Use_Post-Quantum_Algor.pdf
2512.12904v1_OptHQC_Optimize_HQC_for_High-Performance_Post-Quantum_Cryptography.pdf
2512.13333v1_Quantum_Disruption_An_SOK_of_How_Post-Quantum_Attackers_Reshape_Blockchain_Security_and_Performance.pdf
```

---

## Resources

| Resource | Purpose |
|----------|---------|
| **topic7_pqc_migration_top10_consolidated.json** | Primary metadata (10 papers) |
| **README.md** | Detailed analysis and recommendations |
| **COLLECTION_SUMMARY.txt** | Full statistics and breakdown |
| **QUICK_REFERENCE.md** | This file - quick answers |

---

## Next Action Items

1. **This week**: Read top 3 papers (Survey, AmphiKey, 5G Analysis)
2. **This month**: Evaluate liboqs for your infrastructure
3. **This quarter**: Create PQC migration plan
4. **This year**: Implement hybrid TLS 1.3

---

*Last Updated: December 24, 2025*
*For Issue #65, Topic 7: Post-Quantum Cryptography Migration*
