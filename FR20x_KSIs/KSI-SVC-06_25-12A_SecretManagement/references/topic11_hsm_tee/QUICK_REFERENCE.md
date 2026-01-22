# Quick Reference: Topic 11 HSM/TEE Papers

## Top 10 Papers - At a Glance

| # | Score | Year | Title | ArXiv ID | Key Focus |
|---|-------|------|-------|----------|-----------|
| 1 | 81.0 | 2025 | HSM and TPM Failures in Cloud | 2507.17655v2 | Real-world HSM/TPM failures, cloud security |
| 2 | 64.0 | 2025 | TEEs Threat Model & Deployment | 2506.14964v1 | CVM attestation, provider binding |
| 3 | 62.0 | 2025 | Trust Boundary Vulnerabilities | 2508.20962v1 | TEE container isolation, automated analysis |
| 4 | 57.0 | 2025 | Rollbaccine: Storage Rollback | 2505.04014v2 | Rollback attack resistance, disk consistency |
| 5 | 55.0 | 2025 | TensorShield | 2505.22735v1 | Selective TEE protection, memory optimization |
| 6 | 55.0 | 2025 | RaceTEE: Smart Contracts | 2503.09317v2 | TEE interoperability, blockchain integration |
| 7 | 55.0 | 2025 | TEE-based Key-Value Stores | 2501.03118v1 | KVS design patterns, performance optimization |
| 8 | 55.0 | 2024 | TEE Evolution: SGX/SEV/TDX | 2408.00443v1 | Performance comparison, technology selection |
| 9 | 54.0 | 2024 | Teamwork Makes TEE Work | 2402.08908v2 | Decentralized attestation, PUF-based RoT |
| 10 | 53.0 | 2024 | Energy-based Attacks on TEEs | 2405.15537v3 | Side-channel attacks, power management |

## Reading Priority by Use Case

### For Cloud HSM Architecture Design
**Start with:** Papers #1, #2, #7
- Paper #1: Real-world failure modes and defenses
- Paper #2: Multi-cloud attestation challenges
- Paper #7: Key-value store design patterns

### For TEE Technology Selection
**Start with:** Papers #8, #5, #4
- Paper #8: SGX vs SEV vs TDX comparison
- Paper #5: Memory-constrained optimization strategies
- Paper #4: Persistent storage requirements

### For Security Threat Modeling
**Start with:** Papers #3, #10, #9
- Paper #3: Container isolation vulnerabilities
- Paper #10: Energy-based side-channel attacks
- Paper #9: Decentralized trust assumptions

### For Blockchain/Distributed Systems
**Start with:** Papers #6, #9, #1
- Paper #6: Smart contract interoperability
- Paper #9: Decentralized remote attestation
- Paper #1: Distributed key management systems

## File Locations

```
/Users/tamnguyen/Documents/GitHub/ksi_watch/KSI-SVC-06_25-12A_SecretManagement/references/topic11_hsm_tee/
├── 2402.08908v2_Teamwork_Makes_TEE_Work_Open_and_Resilient_Remote_Attestation_on_Decentralized_Trust.pdf
├── 2405.15537v3_Do_Not_Trust_Power_Management_A_Survey_on_Internal_Energy_based_Attacks_Circumventing_Trusted_Execut.pdf
├── 2408.00443v1_An_Experimental_Evaluation_of_TEE_technology_Evolution_Benchmarking_Transparent_Approaches_based_on_.pdf
├── 2501.03118v1_TEE_based_Key_Value_Stores_a_Survey.pdf
├── 2503.09317v2_RaceTEE_Enabling_Interoperability_of_Confidential_Smart_Contracts.pdf
├── 2505.04014v2_Rollbaccine_Herd_Immunity_against_Storage_Rollback_Attacks_in_TEEs_Technical_Report.pdf
├── 2505.22735v1_TensorShield_Safeguarding_On_Device_Inference_by_Shielding_Critical_DNN_Tensors_with_TEE.pdf
├── 2506.14964v1_Narrowing_the_Gap_between_TEEs_Threat_Model_and_Deployment_Strategies.pdf
├── 2507.17655v2_HSM_and_TPM_Failures_in_Cloud_A_Real_World_Taxonomy_and_Emerging_Defenses.pdf
├── 2508.20962v1_Characterizing_Trust_Boundary_Vulnerabilities_in_TEE_Containers.pdf
├── metadata.json
├── RESEARCH_SUMMARY.md
├── QUICK_REFERENCE.md (this file)
└── _archived_low_relevance/
    └── archived_papers_metadata.json (59 papers)
```

## ArXiv Links (Direct Access)

1. https://arxiv.org/abs/2507.17655
2. https://arxiv.org/abs/2506.14964
3. https://arxiv.org/abs/2508.20962
4. https://arxiv.org/abs/2505.04014
5. https://arxiv.org/abs/2505.22735
6. https://arxiv.org/abs/2503.09317
7. https://arxiv.org/abs/2501.03118
8. https://arxiv.org/abs/2408.00443
9. https://arxiv.org/abs/2402.08908
10. https://arxiv.org/abs/2405.15537

## Key Concepts Covered

### Hardware Security
- HSM failure modes and recovery
- TPM integration
- PUF-based root of trust
- Hardware attestation

### TEE Technologies
- Intel SGX (process-based)
- AMD SEV (VM-based)
- Intel TDX (VM-based)
- ARM TrustZone
- TEE runtimes (Gramine, Occlum)

### Security Properties
- Confidentiality in use
- Integrity verification
- Remote attestation
- Rollback resistance
- Side-channel protection

### Attack Vectors
- Storage rollback attacks
- Energy-based side channels
- Trust boundary violations
- API compromise
- Iago attacks

### Design Patterns
- Selective protection
- Decentralized attestation
- Container isolation
- Key-value stores
- Persistent storage

## Research Statistics

- **Total Papers Evaluated:** 69
- **Download Rate:** 10/69 (14.5% top papers)
- **2024-2025 Papers:** 46/69 (67%)
- **Average Relevance Score:** 59.1/100
- **cs.CR (Crypto & Security):** 10/10 (100%)
- **Research Institutions:** Mixed US/international

## Next Steps Checklist

- [ ] Read Paper #1 (HSM failures) for cloud architecture insights
- [ ] Read Paper #7 (TEE KVS) for key storage design patterns
- [ ] Review Paper #8 (TEE comparison) for technology selection
- [ ] Study Paper #4 (Rollbaccine) for persistent storage requirements
- [ ] Analyze Papers #3 & #10 for threat modeling
- [ ] Extract specific design patterns from all 10 papers
- [ ] Map findings to agent key management requirements
- [ ] Identify gaps requiring additional research
- [ ] Draft HSM/TEE integration architecture proposal
- [ ] Develop proof-of-concept implementation plan

---

**Last Updated:** December 25, 2025
**Research ID:** Issue #68 Topic 11
