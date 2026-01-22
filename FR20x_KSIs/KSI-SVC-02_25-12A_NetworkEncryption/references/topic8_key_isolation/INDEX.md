# Topic 8: Cryptographic Key Isolation Failures - Research Files Index

## Overview
This directory contains the complete ArXiv research collection on cryptographic key isolation failures in agent execution, covering 2024-2025 papers with focus on key management, memory disclosure, side-channel attacks, and trusted execution environments.

**Research Date:** December 24, 2025
**Total Papers Downloaded:** 30+
**Unique Papers Identified:** 150+
**Top Papers Selected:** 10

---

## Key Files

### 1. Consolidated Top 10 Papers
- **File:** `topic8_consolidated_top10_papers.json`
- **Contents:** Ranked list of 10 most relevant papers with scores, abstracts, and key topics
- **Format:** JSON with structured metadata
- **Use:** Primary reference for paper quality and relevance

### 2. Research Summary
- **File:** `RESEARCH_SUMMARY.md`
- **Contents:**
  - Executive summary of key findings
  - Detailed analysis of top 10 papers
  - Research landscape analysis
  - Threat model evolution
  - Recommendations for implementation
  - Research gaps and future directions
- **Length:** ~16 KB (comprehensive analysis)
- **Use:** Strategic reference for understanding the field

### 3. Per-Query Results
Query results are stored in separate JSON files showing all papers returned per search query:

| File | Query Focus | Papers Found |
|------|-------------|--------------|
| `topic8_query1_papers.json` | Key isolation/management in agents | 1 |
| `topic8_query3_papers.json` | Key management/reuse (broad) | 10 |
| `topic8_query4_papers.json` | Memory disclosure & side-channels | 10 |
| `topic8_query5_papers.json` | Confidential computing & attestation | 10 |

---

## Top 10 Papers by Relevance

### Rank 1: Future-Proofing Cloud Security Against Quantum Attacks
- **ArXiv ID:** 2509.15653v2
- **PDF:** `2509.15653v2_Future-Proofing_Cloud_Security_Against_Quantum_Attacks_Risk_Transition_and_Mitigation_Strategies.pdf`
- **Authors:** Yaser Baseri, Abdelhakim Hafid, Arash Habibi Lashkari
- **Score:** 20.0
- **Key Metrics:** PQC transition strategies, cloud stack analysis, cryptographic agility
- **Relevance:** Quantum threats to key isolation and cryptographic systems

### Rank 2: Thermal-Aware 3D Design for Side-Channel Information Leakage
- **ArXiv ID:** 2508.02816v1
- **PDF:** `2508.02816v1_Thermal-Aware_3D_Design_for_Side-Channel_Information_Leakage.pdf`
- **Authors:** Dylan Stow, Russell Barnes, Eren Kurshan, Yuan Xie
- **Score:** 20.0
- **Key Metrics:** SVF < 0.05, STSF < 0.59, microarchitectural defense
- **Relevance:** Side-channel extraction of encryption keys from thermal emanations

### Rank 3: An Improved ChaCha Algorithm Based on Quantum Random Number
- **ArXiv ID:** 2507.18157v1
- **PDF:** `2507.18157v1_An_Improved_ChaCha_Algorithm_Based_on_Quantum_Random_Number.pdf`
- **Authors:** Chao Liu, Shuai Zhao, Chenhao Jia
- **Score:** 20.0
- **Key Metrics:** NIST randomness compliance, differential attack resistance
- **Relevance:** Cryptographic strengthening against key reuse and timing attacks

### Rank 4: Securing Open RAN - Cryptographic Challenges for 5G
- **ArXiv ID:** 2506.09418v1
- **PDF:** `2506.09418v1_Securing_Open_RAN_A_Survey_of_Cryptographic_Challenges_and_Emerging_Solutions_for_5G.pdf`
- **Authors:** Ryan Barker, Fatemeh Afghah
- **Score:** 20.0
- **Key Metrics:** Cipher bidding-down attacks, dynamic selection, zero-trust
- **Relevance:** Key management in disaggregated distributed systems

### Rank 5: On Immutable Memory Systems for Artificial Agents
- **ArXiv ID:** 2506.13246v1
- **PDF:** `2506.13246v1_On_Immutable_Memory_Systems_for_Artificial_Agents_A_Blockchain-Indexed_Automata-Theoretic_Framework_.pdf`
- **Authors:** Craig Steven Wright
- **Score:** 20.0
- **Key Metrics:** ECDH key derivation, formal verification, non-repudiation
- **Relevance:** Direct focus on key isolation in multi-agent execution environments

### Rank 6: Logic Encryption: This Time for Real
- **ArXiv ID:** 2512.00833v2
- **PDF:** `2512.00833v2_Logic_Encryption_This_Time_for_Real.pdf`
- **Authors:** Rupesh Raj Karn et al.
- **Score:** 18.0
- **Key Metrics:** Circuit-level obfuscation, side-channel protection
- **Relevance:** Hardware-level key isolation and anti-reverse engineering

### Rank 7: Automated Side-Channel Analysis of Cryptographic Protocols
- **ArXiv ID:** 2511.11385v2
- **PDF:** `2511.11385v2_Automated_Side-Channel_Analysis_of_Cryptographic_Protocol_Implementations.pdf`
- **Authors:** Faezeh Nasrabadi, Robert Künnemann, Hamed Nemati
- **Score:** 18.0
- **Key Metrics:** Binary-level analysis, leakage contract integration
- **Relevance:** Practical key extraction from real-world implementations

### Rank 8: EthVault - Secure FPGA-Based Ethereum Cold Wallet
- **ArXiv ID:** 2510.23847v2
- **PDF:** `2510.23847v2_EthVault_A_Secure_and_Resource-Conscious_FPGA-Based_Ethereum_Cold_Wallet.pdf`
- **Authors:** Joel Poncha Lemayian et al.
- **Score:** 18.0
- **Key Metrics:** Hardware key isolation, timing attack resistance
- **Relevance:** Practical key isolation in cryptocurrency systems

### Rank 9: FHE-SQL: Fully Homomorphic Encrypted Database
- **ArXiv ID:** 2510.15413v1
- **PDF:** `2510.15413v1_FHE-SQL_Fully_Homomorphic_Encrypted_SQL_Database.pdf`
- **Authors:** Po-Yu Tseng, Po-Chu Hsu, Shih-Wei Liao
- **Score:** 18.0
- **Key Metrics:** End-to-end encryption, Universal Composability
- **Relevance:** Key isolation without TEE dependency through homomorphic encryption

### Rank 10: FAARM - Firmware Attestation for Mali GPUs
- **ArXiv ID:** 2510.22566v1
- **PDF:** `2510.22566v1_FAARM_Firmware_Attestation_and_Authentication_Framework_for_Mali_GPUs.pdf`
- **Authors:** Md. Mehedi Hasan
- **Score:** 18.0
- **Key Metrics:** 1.34 ms attestation latency, TOCTOU prevention
- **Relevance:** Firmware-level threats to TEE key isolation

---

## Additional Papers Included

### Related Security Papers (20+ more PDFs available)

**Trusted Execution Environment Research:**
- AutoTEE: Automated Migration and Protection of Programs in TEEs (2502.13379v1)
- What You Trust Is Insecure: Developer Misuse of TEEs (2512.17363v1)
- Confidential Computing for Cloud Security (2511.04550v1)
- Securing Generative AI with Confidential Computing (2511.11836v1)
- TICAL: Trusted Compilation (2511.17070v2)

**Key Management & Cryptography:**
- Secure User-friendly Blockchain Modular Wallet (2506.17988v1)
- Modern Hardware Security: Attacks & Countermeasures (2501.04394v1)
- LURK-T: Limited Use of Remote Keys in TLS 1.3 (2506.12026v1)
- Lightweight Session-Key Rekeying for IoT (2511.02924v2)
- Wrangling Entropy: Multi-Factor Key Derivation (2509.05893v1)

**Hardware Security:**
- ShuffleV: Defense Against EM Side-Channel Attacks (2510.13111v1)
- Logic Encryption Protection (2512.00833v2)
- Thermal Side-Channel Defense (2508.02816v1)

**Emerging Platforms:**
- Optimistic TEE-Rollups for AI Inference (2512.20176v1)
- Persistent BitTorrent Trackers with Confidential Computing (2511.17260v2)
- SSH-Passkeys for Passwordless Authentication (2507.09022v1)

---

## Search Query Details

### Query 1: Key Isolation in Agent Execution
```
cat:cs.CR AND ("key isolation" OR "key management" OR "key leakage")
AND (agent OR container OR execution) AND (memory OR compromise) AND (2024 OR 2025)
```
**Results:** 1 paper (too specific for agent execution focus)

### Query 3: Key Management & Reuse (Broad)
```
cat:cs.CR AND ("key isolation" OR "key reuse" OR "key management") AND (2024 OR 2025)
```
**Results:** 49 papers | 10 selected (score >= 16.0)

### Query 4: Memory Disclosure & Side-Channels
```
cat:cs.CR AND ("memory disclosure" OR "memory leakage" OR "side channel")
AND (cryptographic OR encryption OR key) AND (2024 OR 2025)
```
**Results:** 50 papers | 10 selected (score >= 18.0)

### Query 5: Confidential Computing & Attestation
```
cat:cs.CR AND ("confidential computing" OR "Intel SGX" OR "AMD SEV" OR "attestation")
AND (key OR encryption OR cryptographic) AND (2024 OR 2025)
```
**Results:** 50 papers | 10 selected (score >= 16.0)

---

## Key Metrics from Top 10 Papers

### Key Isolation Effectiveness
| Paper | Solution | Key Isolation Mechanism | Metrics |
|-------|----------|------------------------|---------|
| Thermal-Aware 3D | Hardware | 3D integration + thermal masking | SVF < 0.05 |
| EthVault | Hardware | FPGA with unified timing | Timing-attack resilient |
| Immutable Memory | Software | ECDH + blockchain anchor | Formal proofs |
| FHE-SQL | Software | Homomorphic encryption | Universal Composability |
| LURK-T | TEE | SGX + remote attestation | TLS server compatible |
| FAARM | Hardware | Firmware attestation | 1.34 ms overhead |
| DSEKP* | Software | Per-session HKDF | 27% session latency, 10% per-packet |
| ChaCha Enhanced | Algorithm | Quantum random injection | NIST randomness |

*DSEKP from Query 3 results

### Threat Coverage by Paper
| Threat | Papers Addressing |
|--------|-------------------|
| Timing side-channels | EthVault, ChaCha Enhanced, SLIE |
| Thermal leakage | Thermal-Aware 3D |
| EM emanations | ShuffleV, Thermal-Aware 3D |
| Memory disclosure | Immutable Memory, FHE-SQL |
| Firmware attacks | FAARM, TICAL |
| Quantum threats | Future-Proofing Cloud |
| Developer misuse | What You Trust Is Insecure |
| Cipher selection | Open RAN Survey |

---

## How to Use This Collection

### For Architecture Design
1. Start with **Immutable Memory Systems** (ranks 5) for agent-focused isolation
2. Review **FAARM** (rank 10) for firmware threat model
3. Check **DSEKP** in Query 3 for session-based key rotation

### For Implementation
1. Read **EthVault** (rank 8) for hardware isolation patterns
2. Study **FHE-SQL** (rank 9) for encryption-preserving computation
3. Review **Logic Encryption** (rank 6) for circuit obfuscation

### For Threat Modeling
1. Start with **Future-Proofing Cloud** (rank 1) for quantum threats
2. Review **Thermal-Aware 3D** (rank 2) and **ShuffleV** for side-channels
3. Check **Automated Side-Channel Analysis** (rank 7) for formal methods

### For Developer Guidance
1. Review **What You Trust Is Insecure** for common misuse patterns
2. Check **TICAL** for supply chain threats
3. Study **SLIE** for secure cryptosystem design

---

## File Organization

```
topic8_key_isolation/
├── INDEX.md (this file)
├── RESEARCH_SUMMARY.md (comprehensive analysis)
├── topic8_consolidated_top10_papers.json (ranked list)
├── topic8_query[1,3-5]_papers.json (per-query results)
└── [30+ PDF files organized by ArXiv ID]
    ├── 2501-2509/ (2025-01 to 2025-09)
    ├── 2510/ (2025-10)
    ├── 2511/ (2025-11)
    ├── 2512/ (2025-12)
    └── [filename format: ARXIV_ID_TITLE.pdf]
```

---

## Citation Information

When referencing papers from this collection, use the following format:

**APA Format Example:**
Baseri, Y., Hafid, A., & Lashkari, A. H. (2025). Future-proofing cloud security against quantum attacks: Risk, transition, and mitigation strategies. arXiv preprint arXiv:2509.15653v2.

**BibTeX Example:**
```bibtex
@article{baseri2025quantum,
  title={Future-Proofing Cloud Security Against Quantum Attacks},
  author={Baseri, Yaser and Hafid, Abdelhakim and Lashkari, Arash Habibi},
  journal={arXiv preprint arXiv:2509.15653v2},
  year={2025}
}
```

---

## Research Completion Information

- **Search Execution Date:** December 24, 2025
- **Rate Limit Compliance:** 3.5+ seconds between ArXiv API requests
- **Download Success Rate:** 30/30 PDFs downloaded (100%)
- **Metadata Extraction:** All papers have complete metadata
- **Quality Assurance:** All papers are 2024-2025 publications from cs.CR category

**Total Disk Usage:** ~75 MB (PDFs)
**Metadata Size:** ~70 KB (JSON files)

---

## Questions or Updates?

For information about:
- **Paper relevance:** See `RESEARCH_SUMMARY.md` for analysis
- **Download links:** Check individual PDF filenames or JSON metadata
- **Research methodology:** See "Search Query Details" section above
- **Threat models:** See "Key Metrics from Top 10 Papers" section

---

**Index Created:** December 24, 2025
**Last Updated:** December 24, 2025
