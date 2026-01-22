# AI-Driven Cryptographic Resource Integrity: Discovery Questions

**KSI-SVC-05** - Resource Integrity with AI-Driven Cryptographic Verification and Behavioral Detection

**Research Foundation:** 45 papers synthesized across 8 research clusters addressing model tampering, prompt injection, supply chain poisoning, reproducible builds, GPU acceleration, hardware attestation, continuous monitoring, and model provenance.

**Question Set Version:** 1.1 (Refined per Issue #46)
**Generated:** 2026-01-08
**Refined:** 2026-01-13

---

## SECTION 1: AI MODEL TAMPERING & CRYPTOGRAPHIC EVASION DETECTION (Q01-Q05)

**KSI-SVC-05-Q01:** How does the organization detect weight-level model tampering when backdoors can be injected with <1% performance degradation, making corruption invisible to standard testing?

**KSI-SVC-05-Q02:** What behavioral testing methodology validates that cryptographically signed artifacts and their deployed behavior match, using signed test suites and golden traces as cryptographic evidence of expected model behavior?

**KSI-SVC-05-Q03:** For cryptographically undetectable backdoors using indistinguishability obfuscation (making detection theoretically impossible), what defense-in-depth layering prevents deployment of compromised models?

**KSI-SVC-05-Q04:** When architectural backdoors exist at compiler-level or quantization-based trigger injection creates post-training compromise, what verification mechanisms detect these attack vectors?

**KSI-SVC-05-Q05:** How does the organization distinguish between legitimate model optimization (quantization, pruning) and malicious weight-level surgical attacks that bypass integrity verification?

---

## SECTION 2: PROMPT INJECTION & AGENT INTEGRITY BYPASS (Q06-Q10)

**KSI-SVC-05-Q06:** How do prompt/agent defenses prevent bypass of cryptographic integrity mechanisms (e.g., agents tricking signing services, altering signed artifacts, bypassing attestation)? What mechanisms prevent injection-driven alteration of cryptographically secured models or configurations?

**KSI-SVC-05-Q07:** For multi-modal prompt injection attacks, what cryptographic validation ensures that injected instructions cannot alter signed model artifacts or bypass cryptographic verification of agent decisions?

**KSI-SVC-05-Q08:** What mechanisms prevent agents from using protocol-level exploits to circumvent cryptographic integrity verification or to bypass attestation validation of model signatures?

**KSI-SVC-05-Q09:** When agents can be compromised to issue fraudulent signatures or bypass verification, what isolated verification systems ensure integrity checks execute outside agent control?

**KSI-SVC-05-Q10:** What happens if an agent detects integrity violations but is compromised to suppress alerts—how does the system detect silent integrity check failures?

---

## SECTION 3: SUPPLY CHAIN POISONING & DEPENDENCY INTEGRITY (Q11-Q15)

**KSI-SVC-05-Q11:** How does the organization ensure signing and notarization of model artifacts and dependencies? What verification processes confirm that only signed, approved dependencies are incorporated during model training and deployment?

**KSI-SVC-05-Q12:** What cryptographic mechanisms verify the integrity of AI frameworks and libraries throughout their lifecycle? How is notarization of framework versions and signed model artifacts maintained to prevent dependency substitution attacks?

**KSI-SVC-05-Q13:** For pickle serialization exploiting 22 loading paths and 133 gadget chains (~100% scanner bypass), what multi-layer defense detects pickle-based supply chain attacks?

**KSI-SVC-05-Q14:** What cryptographic enforcement ensures that only signed training datasets and approved data sources are automatically incorporated during model training? How is training data integrity verified and signed to prevent poisoned data from contaminating models?

**KSI-SVC-05-Q15:** What SBOM/AI BOM standards (SPDX 3.0, CycloneDX) provide sufficient supply chain visibility, and how is SBOM generation protected against insider manipulation?

---

## SECTION 4: REPRODUCIBLE BUILDS & THIRD-PARTY VERIFICATION (Q16-Q20)

**KSI-SVC-05-Q16:** For reproducible builds achieving 69-91% success rate (Nix 709K packages), what attestable build infrastructure enables third-party independent verification?

**KSI-SVC-05-Q17:** When deterministic compilation requires <1% modification overhead, why aren't reproducible builds mandatory for all AI artifacts to enable source-to-binary verification?

**KSI-SVC-05-Q18:** What TEE-based attestable builds (42-second startup, 14% overhead for LLVM/Clang) establish proof-of-compilation preventing source repository compromise from affecting binaries?

**KSI-SVC-05-Q19:** How does the organization establish rebuilderd infrastructure enabling independent verification that published artifacts match claimed source code?

**KSI-SVC-05-Q20:** What cryptographically verifiable documentation (signed build manifests and attestable build recipes) ensures reproducible builds remain trustworthy? How are environment dependencies and build outputs signed to prevent them from becoming supply chain attack vectors?

---

## SECTION 5: GPU-ACCELERATED VERIFICATION & POST-QUANTUM CRYPTOGRAPHY (Q21-Q25)

**KSI-SVC-05-Q21:** For GPU-accelerated verification achieving 400-5,915× speedup for cryptographic operations, how are terabyte-scale AI models verified within acceptable latency windows?

**KSI-SVC-05-Q22:** When GPU elliptic curve cryptography and zero-knowledge proofs reduce verification overhead, what integration enables practical deployment for billion-scale LLM attestation?

**KSI-SVC-05-Q23:** What crypto-agility strategy maintains integrity verification effectiveness as algorithms evolve? How do key rotation, algorithm agility, dual-signing, and migration plans for artifact-signing enable seamless transitions between cryptographic algorithms without service disruption?

**KSI-SVC-05-Q24:** How will the organization preserve verifiable model history and artifact integrity once current cryptographic algorithms weaken? What mechanisms (hash-anchoring, multi-algorithm signing, time-stamping services) establish long-term integrity assurance beyond algorithm lifetime?

**KSI-SVC-05-Q25:** What mechanisms maintain cryptographic strength of integrity verification across algorithm transitions? How does the organization plan for maintaining artifact signatures, audit logs, and provenance records when cryptographic standards evolve or quantum computing advances?

---

## SECTION 6: HARDWARE ATTESTATION & TRUSTED EXECUTION (Q26-Q30)

**KSI-SVC-05-Q26:** For TPM 2.0 measured boot with Platform Configuration Register chaining, how does the organization ensure TPM compromise (physical attacks, firmware exploitation) doesn't enable signature falsification?

**KSI-SVC-05-Q27:** When remote attestation prevents replay attacks via nonce protection, what continuous re-attestation frequency validates device state without excessive overhead?

**KSI-SVC-05-Q28:** For Trusted Execution Environment isolation executed at hardware level, what prevents CPU-GPU mismatch attacks where GPU-direct memory access bypasses CPU integrity checks?

**KSI-SVC-05-Q29:** How does the organization prevent attestation staleness—point-in-time snapshots provide no protection against post-attestation compromise when verification latency exceeds attack speed?

**KSI-SVC-05-Q30:** When confidential computing integrates GPU memory encryption with CPU attestation, what validates that cryptographic operations remain secure throughout the attestation chain?

---

## SECTION 7: RUNTIME INTEGRITY DETECTION & CRYPTOGRAPHIC BASELINE MONITORING (Q31, Q33, Q35)

**KSI-SVC-05-Q31:** How does eBPF kernel-level monitoring detect divergence between deployed model behavior and cryptographically attested baselines? What mechanisms alert on unauthorized changes to signed artifacts or configuration drifts from baseline signatures?

**KSI-SVC-05-Q33:** How does the organization distinguish between legitimate, authorized model parameter changes (with signed change manifests) and unauthorized tampering? What cryptographic mechanisms enforce signed change authorization for model updates?

**KSI-SVC-05-Q35:** What post-deployment behavioral monitoring validates model inference consistency against cryptographically attested expected behavior? How does monitoring detect divergence from behavior baselines verified by digital signatures or integrity proofs?

---

## SECTION 8: MODEL PROVENANCE & TRANSPARENCY LOG INTEGRITY (Q36-Q40)

**KSI-SVC-05-Q36:** For Sigstore/Rekor transparency logs tracking model signing events and transformations, what prevents Rekor operator compromise from issuing unauthorized certificates?

**KSI-SVC-05-Q37:** How does C2PA-based model attestations maintain integrity when OIDC identity providers or transparency log operators are compromised?

**KSI-SVC-05-Q38:** When transparency logs require active monitoring (passive observation is insufficient), what detection mechanisms identify STH (Signed Tree Head) window vulnerabilities?

**KSI-SVC-05-Q39:** How does the organization enable third-party verification of model history and forensic reconstruction of modification timeline using transparent audit logs?

**KSI-SVC-05-Q40:** What organizational vision exists for cryptographic integrity evolution 2025-2027: from post-deployment point-in-time verification toward continuous real-time behavioral integrity assurance?

---

## RESEARCH CLUSTERS SUPPORTING THESE QUESTIONS

**Cluster 1:** AI-Driven Cryptographic Evasion (6 papers) - Undetectable backdoors, weight-level manipulation, <1% degradation, architectural backdoors

**Cluster 2:** Prompt Injection & Agent Integrity (4 papers) - 100% evasion rates, multi-modal attacks, 50%+ bypass rates, protocol exploits

**Cluster 3:** Supply Chain Security (8 papers) - 76% vulnerable LLM projects, 56+ month lag, AI BOM standards, dependency poisoning

**Cluster 4:** Reproducible Builds (7 papers) - 69-91% success, deterministic compilation, third-party verification, TEE-based attestation

**Cluster 5:** GPU Acceleration & Post-Quantum (7 papers) - 400-5,915× speedup, NIST algorithms, quantum threat timeline

**Cluster 6:** Hardware Attestation (5 papers) - TPM 2.0, PCR chaining, TEE isolation, confidential computing

**Cluster 7:** Continuous Monitoring (3 papers) - eBPF (94% precision), behavioral baselining, drift detection, quantum gradient descent

**Cluster 8:** Model Provenance (3 papers) - Sigstore/Rekor, C2PA attestations, transparency logs, forensic reconstruction

---

**Document Purpose:** Enable organizations to comprehensively evaluate AI model cryptographic integrity verification with exclusive focus on cryptographic resource validation, supply chain resilience, and runtime integrity detection against attested baselines.
