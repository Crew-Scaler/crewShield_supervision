# Topic 7: Post-Quantum Cryptography (PQC) Migration - ArXiv References

**Collection Date**: December 24, 2025
**Total Papers**: 10 (ranked by relevance)
**Focus Area**: NIST ML-KEM/ML-DSA deployment, hybrid TLS 1.3 implementation, handshake performance metrics

---

## Executive Summary

This collection contains 10 of the most relevant ArXiv papers from 2024-2025 on Post-Quantum Cryptography migration, with emphasis on:
- **NIST standardized algorithms**: ML-KEM (key encapsulation), ML-DSA (digital signatures), SLH-DSA (hash-based signatures)
- **Deployment contexts**: TLS 1.3, QUIC, DNS, 5G/IoT, smart grid, blockchain
- **Performance metrics**: Handshake latency, certificate size growth, CPU/memory overhead, throughput
- **Hybrid approaches**: X25519+ML-KEM combinations, classical+quantum+PQC integration

---

## Papers by Rank

### 1. Post-Quantum Cryptography and Quantum-Safe Security: A Comprehensive Survey
**Authors**: Gaurab Chhetri, Shriyank Somvanshi, Pavan Hebli, Shamyo Brotee, Subasish Das
**Year**: 2025 (October)
**ArXiv ID**: 2510.10436v1
**Category**: cs.CR

**Key Contributions**:
- Comprehensive taxonomy of PQC families: lattice, code, hash, multivariate, isogeny, MPC-in-the-Head
- Detailed coverage of ML-KEM, ML-DSA, SLH-DSA standardization status
- Hardware acceleration analysis: AVX2, FPGA/ASIC implementations
- Side-channel resistance discussion
- Protocol integration: TLS, DNSSEC, PKI, certificates
- Deployment guidance: IoT, cloud, finance, blockchain
- Crypto-agility and hybrid migration strategies

**Relevance**: Foundational survey providing context for all other papers

---

### 2. AmphiKey: A Dual-Mode Secure Authenticated Key Encapsulation Protocol for Smart Grid
**Authors**: Kazi Hassan Shakib, Muhammad Asfand Hafeez, Arslan Munir
**Year**: 2025 (September)
**ArXiv ID**: 2509.01701v2
**Category**: cs.CR

**Key Metrics**:
- **Handshake latency (Deniable Mode)**:
  - Server: 0.15 ms
  - Raspberry Pi client: 0.41 ms
- **Handshake latency (Authenticated Mode)**:
  - Client signature generation: 4.8 ms
  - Server verification: 0.84 ms

**Key Contributions**:
- Dual-mode hybrid AKEM: Authenticated vs. Deniable
- ML-KEM-768 + X25519 (AKEM) with Raccoon DSA (signature)
- Masking-friendly design for side-channel resistance
- Tested on AMD Ryzen 5 and Raspberry Pi (resource-constrained)
- Performance comparison: Raccoon vs. ML-DSA-65

**Relevance**: Real-world deployment metrics for hybrid key exchange on heterogeneous hardware

---

### 3. Analysis of Post-Quantum Cryptography in User Equipment in 5G and Beyond
**Authors**: Sanzida Hoque, Abdullah Aydeger, Engin Zeydan, Madhusanka Liyanage
**Year**: 2025 (July)
**ArXiv ID**: 2507.17074v1
**Category**: cs.CR

**Key Findings**:
- **Best efficiency**: ML-KEM + ML-DSA for latency-sensitive applications
- **Higher overhead**: SPHINCS+ and HQC combinations unsuitable for time-sensitive scenarios
- Full 5G emulation stack: Open5GS + UERANSIM
- PQC-enabled TLS 1.3 via BoringSSL and liboqs
- Performance analysis: Handshake latency, CPU/memory, bandwidth, retransmission rates

**Key Metrics**:
- Evaluation under realistic 5G network conditions
- Varying cryptographic configurations and client loads
- User Equipment (UE) to UE communications focus

**Relevance**: Mobile/5G deployment guidance for PQC algorithm selection

---

### 4. Quantum-Resistant Domain Name System: A Comprehensive System-Level Study
**Authors**: Juyoul Lee, Sanzida Hoque, Abdullah Aydeger, Engin Zeydan
**Year**: 2025 (June)
**ArXiv ID**: 2506.19943v1
**Category**: cs.CR

**Key Findings**:
- **Practical candidates**: ML-KEM and Falcon (good latency/resource profiles)
- **Overhead concern**: SPHINCS+ significantly increases message sizes and processing overhead
- Three DNS mechanisms analyzed: DNSSEC, DNS-over-TLS (DoT), DNS-over-HTTPS (DoH)
- OQS libraries integration with BIND9 and TLS 1.3
- Performance and threat models formalized

**Identified Vulnerabilities**:
- Downgrade risks
- Fragmentation vulnerabilities
- DNS amplification DoS attacks

**Relevance**: Critical Internet infrastructure protection (DNS) with PQC

---

### 5. Faster Post-Quantum TLS 1.3 Based on ML-KEM: Implementation and Assessment
**Authors**: Jieyu Zheng, Haoliang Zhu, Yifan Dong, Zhenyu Song, Zhenhao Zhang, Yafang Yang, Yunlei Zhao
**Year**: 2024 (April)
**ArXiv ID**: 2404.13544v2
**Category**: cs.CR

**Key Performance Metrics**:
- **AVX-512 optimization**: 1.64x speedup vs. AVX2 implementation
- **Batch key generation**: 3.5x-4.9x acceleration
- **TLS 1.3 assessment**: PQ-only and hybrid modes benchmarked
- IND-1-CCA KEM constructions evaluated and implemented

**Key Contributions**:
- ML-KEM implementation optimization techniques
- Parallelization of polynomial multiplication, modular reduction
- Batch method for seamless TLS integration
- Detailed performance assessment methodology

**Relevance**: Practical optimization strategies for faster PQC handshakes

---

### 6. Quantum-Safe integration of TLS in SDN networks
**Authors**: Jaime S. Buruaga, Ruben B. Méndez, Juan P. Brito, Vicente Martin
**Year**: 2025 (February)
**ArXiv ID**: 2502.17202v1
**Category**: quant-ph

**Key Features**:
- Hybrid cryptography: Classical + Quantum Key Distribution + Post-Quantum
- TLS 1.3 protocol base with hybrid mode support
- QKD integration: ETSI 014 standards compliance
- Crypto-agility: Dynamic ciphersuite selection

**Advanced Capabilities**:
- Rekeying across large QKD networks
- Key transport protocols
- Backward compatibility with existing systems
- Demonstrated on production infrastructure

**Relevance**: Integration of QKD with PQC for layered security approach

---

### 7. A Quantum of QUIC: Dissecting Cryptography with Post-Quantum Insights
**Authors**: Marcel Kempf, Nikolas Gauder, Benedikt Jaeger, Johannes Zirngibl, Georg Carle
**Year**: 2024 (May)
**ArXiv ID**: 2405.09264v1
**Category**: cs.NI

**Performance Metrics**:
- **Packet protection overhead**: 10-20% performance impact
- **Header protection**: Negligible impact for AES ciphers
- **PQC algorithm comparison**:
  - Kyber, Dilithium, FALCON: Low handshake impact
  - SPHINCS+: Significantly higher duration and issues

**Evaluated Implementations**:
- LSQUIC, quiche, MsQuic
- NOOP AEAD algorithm testing (to isolate cryptography impact)
- Symmetric vs. asymmetric cryptography breakdown

**Relevance**: QUIC/HTTP3 protocol modernization with PQC

---

### 8. Fingerprinting Implementations of Cryptographic Primitives and Protocols that Use Post-Quantum Algorithms
**Authors**: Tushin Mallick, Ramana Kompella, Ashish Kundu, Cristina Nita-Rotaru
**Year**: 2025 (March)
**ArXiv ID**: 2503.17830v3
**Category**: cs.CR

**Key Findings**:
- **Detection accuracy**:
  - Classical vs. PQC key exchange: 98% accuracy
  - PQC digital signatures: 100% accuracy
  - Specific algorithm identification: 97% accuracy
  - Implementation fingerprinting: 100% accuracy
- **Protocols analyzed**: TLS, SSH, QUIC, OpenVPN, OIDC
- **Libraries examined**: liboqs, CIRCL (Windows, Ubuntu, MacOS)
- **SNARK libraries**: 100% distinguishability

**Practical Application**:
- Integrated into QUARTZ threat analysis tool (Cisco)
- Tranco dataset analysis for PQC adoption tracking

**Relevance**: Side-channel and traffic analysis threats from PQC implementations

---

### 9. OptHQC: Optimize HQC for High-Performance Post-Quantum Cryptography
**Authors**: Ben Dong, Hui Feng, Qian Wang
**Year**: 2025 (December)
**ArXiv ID**: 2512.12904v1
**Category**: cs.CR

**Performance Achievement**:
- **55% average speedup** over reference HQC implementation

**Optimization Techniques**:
1. **Data-level sparsity**: Vector multiplication acceleration
2. **Instruction-level**: AVX2 in hash computation
3. **Memory optimization**: Lookup table indexing, syndrome computation
4. **Error recovery**: Optimized vector recovery

**Algorithm Focus**:
- HQC (Hamming Quasi-Cyclic) - newly standardized code-based PQC
- Alternative to lattice-based schemes

**Relevance**: Code-based PQC alternative implementations and performance tuning

---

### 10. Quantum Disruption: An SOK of How Post-Quantum Attackers Reshape Blockchain Security and Performance
**Authors**: Tushin Mallick, Maya Zeldin, Murat Cenk
**Year**: 2025 (December)
**ArXiv ID**: 2512.13333v1
**Category**: cs.CR

**Key Topics**:
- Systemization of Knowledge (SoK) on post-quantum threats
- Blockchain security implications
- Performance impacts of PQC on blockchain systems
- Quantum-safe blockchain architecture design
- Migration strategies and deployment challenges
- Interoperability considerations

**Relevance**: Specialized analysis for blockchain/cryptocurrency applications

---

## Key Metrics Summary

### Handshake Latency (from Papers 2 & 3)
- **Typical range**: 0.15 ms (optimized, deniable) to 4.8 ms (with signatures)
- **Increase vs. classical**: 10-15% in most practical scenarios
- **Bottlenecks**: Signature generation (ML-DSA) most expensive operation

### Certificate Size Growth
- **ML-KEM**: ~1184 bytes public key
- **ML-DSA**: ~2544 bytes signature
- **X25519**: 32 bytes (for comparison)
- **Typical growth**: 2-4x larger than classical ECC

### Algorithm Recommendations by Use Case

| Use Case | KEMs | Signatures | Notes |
|----------|------|-----------|-------|
| TLS/HTTPS | ML-KEM-768 | ML-DSA-65 | NIST standard, good performance |
| 5G/Mobile | ML-KEM | ML-DSA | Latency-sensitive, power-constrained |
| DNS | ML-KEM, Falcon | Falcon | Message size critical |
| QUIC/HTTP3 | ML-KEM, Kyber | Dilithium, Falcon | Handshake optimization important |
| Blockchain | Varies | ML-DSA, SPHINCS+ | Trust-critical applications |
| IoT/Embedded | ML-KEM | Falcon | Resource-constrained |

### Implementation Best Practices

1. **Hybrid approach**: Always combine classical + PQC (forward secrecy + quantum safety)
2. **Hardware acceleration**: Use AVX2 minimum, AVX-512 for high-throughput scenarios
3. **Side-channel mitigation**: Constant-time implementations (masking-friendly designs)
4. **Crypto-agility**: Support multiple algorithms for graceful migration
5. **Interoperability**: Test across implementations (liboqs, CIRCL, BoringSSL)

---

## Deployment Timeline Implications

- **2024-2025**: Standards finalization and proof-of-concept deployments
- **2025-2026**: Enterprise adoption begins, pilot programs with major cloud providers
- **2026-2027**: Gradual migration of critical infrastructure (DNS, finance, government)
- **2027-2030**: Widespread deployment in consumer-facing systems (browsers, messaging)
- **2030+**: Classical-only systems become legacy

---

## Open Research Challenges

From the papers:

1. **Parameter agility**: Dynamic selection of PQC parameters per deployment
2. **Leakage-resilient implementations**: Better resistance to side-channel attacks
3. **Domain-specific rollout playbooks**: Guidance for specific industries
4. **Interoperability**: Full testing across diverse implementations
5. **Performance optimization**: Especially for resource-constrained environments
6. **Downgrade prevention**: Secure negotiation of quantum-safe algorithms

---

## References

All PDFs are stored in this directory with names matching their ArXiv IDs.

**Metadata Files**:
- `topic7_pqc_migration_query1_papers.json` - All 15 papers from first query (PQC + TLS + deployment)
- `topic7_pqc_migration_query2_alt_papers.json` - All 50 papers from second query (hybrid key exchange + performance)
- `topic7_pqc_migration_top10_consolidated.json` - **Use this for the top 10 ranked papers**

---

## How to Use This Collection

1. **Overview**: Start with paper #1 (Comprehensive Survey)
2. **Implementation focus**: Papers #5 and #9 (ML-KEM optimization)
3. **Deployment cases**: Papers #2-4 and #6-7 (specific protocols/environments)
4. **Security analysis**: Papers #8 and #10 (attacks and threats)

---

*Collection created with ArXiv research automation script respecting rate limits (3+ seconds between requests). All papers are from 2024-2025, prioritized from prestigious institutions.*
