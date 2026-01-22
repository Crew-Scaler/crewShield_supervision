# Quick Reference: Issue #73 Research Papers
## AI-Driven Cryptographic Integrity Evasion and Model Tampering

**Total Papers:** 10 (236 pages)
**All papers:** 7+ pages ✓ | 2024-2025 ✓ | ArXiv only ✓

---

## By Research Priority (Read in this order)

### CRITICAL (Must Read First)

**1. Undetectable Backdoors in Obfuscated NNs** (2406.05660)
- 33 pages | June 2024
- Why: Cryptographic proof of undetectability, steganographic techniques
- Key: Indistinguishability obfuscation makes backdoors provably undetectable

**2. Prompt Injections to Protocol Exploits** (2506.23260)
- 36 pages | Dec 2025
- Why: 30+ attack techniques, cryptographic provenance tracking
- Key: 50%+ bypass rate for adaptive attacks, protocol-layer vulnerabilities

**3. Bypassing LLM Guardrails** (2504.11168)
- 14 pages | July 2025
- Why: 100% evasion success against Azure Prompt Shield, Meta Prompt Guard
- Key: Current detection systems fundamentally insufficient

**4. Behavior Backdoor for DL Models** (2412.01369)
- 12 pages | Dec 2024
- Why: Surgical weight-level attacks, quantization-based triggers
- Key: Post-processing becomes attack vector

---

### HIGH PRIORITY

**5. Architectural Backdoors Survey** (2507.12919)
- 35 pages | July 2025
- Why: Comprehensive survey, compiler-level attacks, supply chain
- Key: Detection gaps in architectural verification

**6. Cross-LLM Behavioral Backdoor Detection** (2511.19874)
- 10 pages | Nov 2025
- Why: Behavioral testing framework, cross-model detection
- Key: 43.5pp accuracy drop when transferring detectors

**7. Backdoor Attacks and Defenses in CV** (2509.07504)
- 22 pages | Sept 2025
- Why: Comprehensive attack taxonomy, defense evaluation
- Key: Input-aware triggers evade classical sanitization

---

### IMPORTANT (Defense Mechanisms)

**8. Securing AI Agents Against Prompt Injection** (2511.15759)
- 10 pages | Nov 2025
- Why: 847 test cases, combined defense approach
- Key: 73.2% → 8.7% attack success (still problematic)

**9. Indirect Prompt Injections** (2510.05244)
- 30 pages | Oct 2025
- Why: Multi-modal bypass (Braille), obfuscation techniques
- Key: Benchmark weaknesses, firewall limitations

**10. Securing AI Systems: Attacks & Impacts** (2506.23296)
- 34 pages | June 2025
- Why: 11 attack types, CIA triad mapping, implementation guide
- Key: Comprehensive taxonomy for understanding threats

---

## By Research Topic

### Weight-Level Tampering & Backdoor Injection
- **2406.05660** - Undetectable Backdoors (steganographic)
- **2412.01369** - Behavior Backdoor (quantization triggers)
- **2507.12919** - Architectural Backdoors (compiler-level)
- **2509.07504** - CV Attacks (dataset poisoning, model modification)

### Adversarial Evasion (65-100% Success Rate)
- **2504.11168** - Bypassing Guardrails (100% evasion)
- **2510.05244** - Indirect Injections (obfuscation bypass)
- **2506.23296** - Attack Taxonomy (comprehensive threats)

### Prompt Injection Bypassing Integrity Verification
- **2506.23260** - Protocol Exploits (50%+ adaptive bypass)
- **2511.15759** - Securing Agents (defense evaluation)
- **2510.05244** - Firewalls (alternative modality evasion)

### Behavioral Testing & Trigger Detection
- **2511.19874** - Cross-LLM Detection (behavioral framework)
- **2412.01369** - Behavior Backdoor (trigger detection)
- **2509.07504** - CV Survey (input-aware triggers)

### Surgical Precision Attacks
- **2406.05660** - Steganographic embedding
- **2412.01369** - Address-shared training
- **2507.12919** - Compiler-level precision

---

## Key Statistics Quick Reference

### Attack Success Rates
- **100%** evasion: Azure Prompt Shield, Meta Prompt Guard
- **50%+** bypass: Adaptive prompt injection
- **43.5pp** drop: Cross-model detector accuracy
- **8.7%** residual: Best combined defense still vulnerable

### Paper Metrics
- **70%** from 2025 (7 papers)
- **30%** from 2024 (3 papers)
- **23.6** pages average
- **236** total pages

### Institutions
- Top US: Yale, Northwestern, McGill
- Research: Google DeepMind, Mila, ServiceNow
- Industry: Microsoft, Meta (evaluation targets)

---

## Critical Findings Summary

### What Works (Attacks)
✓ Indistinguishability obfuscation (provably undetectable)
✓ Multi-modal encoding (Braille bypass)
✓ Adaptive prompt injection (50%+ success)
✓ Quantization-based triggers (surgical precision)
✓ Compiler-level injection (persistent backdoors)

### What Fails (Defenses)
✗ Cryptographic signatures alone (semantic vs syntactic)
✗ Single-model detectors (cross-model failure)
✗ Static verification (runtime-activated backdoors)
✗ Classical sanitization (input-aware threats)
✗ Pattern-based filters (obfuscation bypass)

### What Helps (Defenses)
⚠ Multi-stage verification (8.7% residual attacks)
⚠ Behavioral testing (model-specific)
⚠ Cryptographic provenance (not standardized)
⚠ Ensemble detection (improved but incomplete)

---

## File Locations

**Base Directory:**
```
/Users/tamnguyen/Documents/GitHub/ksi_watch/KSI-SVC-05_25-12A_ResourceIntegrity/references/
```

**Documentation:**
- `PAPER_INVENTORY.md` - Detailed paper descriptions
- `RESEARCH_SUMMARY.md` - Comprehensive findings analysis
- `QUICK_REFERENCE.md` - This file

**Papers:** All PDFs in same directory with format:
`{arxiv_id}_{title}.pdf`

---

## Next Steps for Issue #73

1. **Immediate:** Review critical papers (2406.05660, 2506.23260, 2504.11168)
2. **Analysis:** Extract cryptographic evasion techniques
3. **Synthesis:** Develop multi-layered defense framework
4. **Implementation:** Design integrity verification system
5. **Testing:** Validate against documented attack vectors

---

**Research Date:** December 25, 2025
**Status:** Complete ✓
**All Requirements Met:** Yes ✓
