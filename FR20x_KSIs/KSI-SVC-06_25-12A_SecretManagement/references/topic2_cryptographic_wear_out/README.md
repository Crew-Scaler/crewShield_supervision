# Topic 2: Cryptographic Wear-Out and Continuous Key Rotation at Machine-Speed

## Quick Reference

**Research Date:** December 25, 2025
**Papers Downloaded:** 10
**Total Size:** ~8 MB
**Year Coverage:** 2024-2025 (prioritized 2025)
**US Institutions:** 4 papers (Meta, AWS, Cornell Tech, NIST)

## Files in This Directory

### Core Documents
- `RESEARCH_SUMMARY.md` - Comprehensive 19KB analysis with technical findings and FedRAMP recommendations
- `metadata.json` - Structured metadata for all 10 papers with abstracts, authors, institutions
- `README.md` - This file

### Downloaded Papers (10 Total)

#### US Institution Papers (4)
1. `01_DNDK_2025_Meta_Gueron_Ristenpart.pdf` - **Meta/Cornell Tech** - Production deployment
2. `02_BlockcipherKeyCommitment_2025_AWS_Kampanakis.pdf` - **AWS** - FIPS-compliant solution
3. `10_PracticalChallengesAESGCM_2024_NIST_Amazon_Kampanakis.pdf` - **AWS** - Real-world wear-out data

#### International Leading Research (6)
3. `03_TightMultiUserCCM_2025_Naito_Sasaki_Sugawara.pdf` - NIST Associate co-author
4. `04_MakingGCMGreatAgain_2025_KAIST_Chung.pdf` - EUROCRYPT 2025
5. `05_KIVR_CommittingAE_2025_Naito_Sasaki_Sugawara.pdf` - ACNS 2024, NIST Workshop
6. `06_OptimallySecureDAE_2025_EUROCRYPT_Chen.pdf` - EUROCRYPT 2025
7. `07_CollisionBasedAttacks_2024_Ericsson_Mattsson.pdf` - Security analysis
8. `08_ComprehensiveRobustnessGCM_2024_CTRSA_Inoue.pdf` - CT-RSA 2025
9. `09_FuzzyLogicDynamicKeyGen_2025_ArXiv_Bhand.pdf` - Dynamic key generation

## Key Findings at a Glance

### Cryptographic Wear-Out Limits
- **Standard AES-GCM:** 2^32 messages (~4.3 billion) or 64 GiB per key
- **AWS Cloud Scale:** 2^64 blocks encrypted every 2 weeks
- **High-Speed Networks (500Gbps):** 91-minute rekey frequency required
- **Security Degradation:** GCM with 96-bit IVs provides <97 bits (not 128)

### Production-Ready Solutions
1. **DNDK-GCM** (Meta 2025) - 1.02× overhead, 2^64 bytes/key, IETF draft standard
2. **KC-XAES-256-GCM** (AWS 2025) - FIPS-compliant, enhanced data bounds
3. **AWS KMS** (FedRAMP Authorized) - Derived key per request

### Recommended for FedRAMP
- **Immediate:** AWS KMS with automatic rotation (already FedRAMP authorized)
- **Near-term:** KC-XAES-256-GCM (FIPS-compliant, AWS production)
- **Future:** DNDK-GCM (pending FIPS validation)

## Search Methodology

### Queries Executed
1. "cryptographic wear-out" AND (key rotation OR AES-GCM) AND (machine learning OR high-volume) AND (2024 OR 2025)
2. "nonce collision" AND (GCM OR encryption) AND (security OR cryptanalysis) AND (2024 OR 2025)
3. "symmetric key rotation" AND (automated OR continuous) AND (KMS OR key management) AND (2024 OR 2025)

### Sources Searched
- IACR ePrint Archive (primary)
- ArXiv cs.CR (Cryptography and Security)
- NIST Workshops (Block Cipher Modes)
- ACM/IEEE Digital Libraries

### Selection Criteria
- Publication year (2025 > 2024)
- US institution affiliation (Meta, AWS, Cornell Tech, NIST)
- Direct relevance to wear-out/rotation/nonce management
- Practical deployment evidence
- Top-tier venues (EUROCRYPT, NIST, CT-RSA, SAC)

## Citations

### APA Format
See `metadata.json` for complete citation information for all 10 papers.

### BibTeX
Available upon request - extract from metadata.json

## Usage

### For FedRAMP Compliance Review
1. Read `RESEARCH_SUMMARY.md` → Section "Practical Implications for FedRAMP Compliance"
2. Focus on papers #1, #2, #10 (US institution, production-deployed)
3. Review "Deployment Considerations" → "Recommended Solutions for FedRAMP Systems"

### For Technical Implementation
1. Paper #1: DNDK-GCM technical specification
2. Paper #2: KC-XAES-256-GCM FIPS-compliant approach
3. Paper #10: Real-world AWS scale metrics

### For Security Analysis
1. Paper #7: Collision-based attack vectors and complexities
2. Paper #8: Robustness analysis under nonce misuse
3. Paper #4: Next-generation GCM variants (eGCM)

## Archive Directory
- `_archived_low_relevance/` - Reserved for papers ranked 11+ (none in this research - only 10 papers selected)

## Contact
For questions about this research, see Issue #68 Topic 2 in the ksi_watch repository.

---
**Last Updated:** December 25, 2025
**Total Papers:** 10 downloaded, 0 archived
**Research Status:** COMPLETE
