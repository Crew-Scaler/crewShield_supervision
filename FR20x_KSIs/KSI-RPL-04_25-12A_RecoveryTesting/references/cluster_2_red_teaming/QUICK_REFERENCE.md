# Cluster 2: Quick Reference Guide

## Top 5 Must-Read Papers for Recovery Systems

### 1. 2509.21947v2 - Active Attacks: Red-teaming LLMs via Adaptive Environments (10/10)
- **Pages**: 21 | **Date**: 2025-09-26 | **Authors**: Bengio et al.
- **Why**: Adaptive adversarial environments directly applicable to testing recovery mechanisms under dynamic attacks
- **Key Contribution**: Framework for generating adaptive attacks that evolve based on system response
- **For Recovery**: Test recovery robustness against continuously evolving attack patterns

### 2. 2411.14133v3 - GASP: Efficient Black-Box Generation of Adversarial Suffixes (10/10)
- **Pages**: 46 | **Date**: 2024-11-21 | **Authors**: Basani, Zhang
- **Why**: Most comprehensive jailbreak framework; black-box approach applicable to recovery system attacks
- **Key Contribution**: 40-70% attack success rate; transferable across model families
- **For Recovery**: Use GASP techniques to test recovery-targeted adversarial inputs

### 3. 2502.14847v2 - Red-Teaming LLM Multi-Agent Systems via Communication Attacks (9/10)
- **Pages**: 21 | **Date**: 2025-02-20 | **Authors**: He et al.
- **Why**: Multi-agent attacks mirror distributed recovery system vulnerabilities
- **Key Contribution**: 70%+ system compromise rate via compromised agent communication
- **For Recovery**: Test inter-agent recovery coordination under message injection attacks

### 4. 2512.20986v1 - AegisAgent: Autonomous Defense Against Prompt Injection (8/10)
- **Pages**: 16 | **Date**: 2025-12-24 | **Authors**: Wang et al.
- **Why**: Defense framework showing recovery patterns for prompt injection
- **Key Contribution**: Real-time detection and autonomous response mechanisms
- **For Recovery**: Implement similar autonomous recovery trigger and state validation

### 5. 2512.23128v1 - TRAP: Task-Redirecting Agent Persuasion Benchmark (6/10)
- **Pages**: 17 | **Date**: 2025-12-29 | **Authors**: Korgul et al.
- **Why**: Agent task redirection attacks applicable to recovery system goal manipulation
- **Key Contribution**: Benchmark for evaluating agent goal alignment under adversarial inputs
- **For Recovery**: Test recovery task completion reliability against goal redirection attacks

---

## Attack Vectors Quick Reference

### Critical for Recovery Testing

| Vector | Paper | Severity | Metric |
|--------|-------|----------|--------|
| Adversarial Suffixes | GASP (2411.14133v3) | HIGH | 40-70% success rate |
| Communication Hijacking | Multi-Agent (2502.14847v2) | CRITICAL | 70%+ compromise |
| Task Redirection | TRAP (2512.23128v1) | HIGH | Goal manipulation |
| Prompt Injection | Multiple | HIGH | >85% detection miss rate |
| Memory Poisoning | AgentPoison (2407.12784v1) | CRITICAL | Long-term effects |
| Multimodal Attacks | Arondight (2407.15050v1) | MEDIUM | 60% VLM success |
| Code-Mixed Attacks | Hinglish (2505.14226v3) | MEDIUM | Multilingual bypass |

---

## Defense Patterns Quick Reference

### Detection-Based Defenses
- **Classifier-Based**: >85% accuracy on prompt injection (2512.12583v1)
- **Anomaly Detection**: Monitor for task deviation, state corruption
- **Real-Time Monitoring**: <100ms latency requirement (AegisAgent)

### Prevention-Based Defenses
- **Input Sanitization**: Filter against known attack patterns
- **Task Validation**: Verify recovery tasks pre-execution
- **State Constraints**: Bounded input processing

### Recovery-Based Defenses
- **Autonomous Response**: Trigger recovery on attack detection (AegisAgent pattern)
- **State Validation**: >95% accuracy requirements
- **Rollback Mechanisms**: Mean Time to Recovery <2 minutes

---

## Paper Organization by Use Case

### Attackers Perspective (Understanding Threats)
1. Read GASP (2411.14133v3) - How to generate attacks
2. Read Arondight (2407.15050v1) - Multimodal attack techniques
3. Read Multi-Agent (2502.14847v2) - System-level exploitation
4. Read Active Attacks (2509.21947v2) - Adaptive attack strategies

### Defenders Perspective (Building Defenses)
1. Read AegisAgent (2512.20986v1) - Defense architecture
2. Read Prompt Injection Detection (2512.12583v1) - Detection techniques
3. Read Defense Innovations (2512.16307v1) - Latest best practices
4. Read Trustworthy AI (2512.23557v1) - Framework validation

### Recovery Engineers (System Design)
1. Read Active Attacks (2509.21947v2) - Threat model
2. Read Multi-Agent (2502.14847v2) - Distributed recovery challenges
3. Read TRAP (2512.23128v1) - Recovery task validation
4. Read AegisAgent (2512.20986v1) - Autonomous recovery patterns

### Evaluators (Metrics & Benchmarking)
1. Read Comprehensive Testing (2409.00551v1) - Full evaluation methodology
2. Read TRAP (2512.23128v1) - Benchmark design
3. Read Code-Switching (2406.15481v3) - Multilingual evaluation
4. Read Curiosity-driven (2402.19464v1) - Exploration-based testing

---

## Quantitative Metrics Summary

### Attack Success Rates
- **Adversarial Suffixes (GASP)**: 40-70% baseline
- **Prompt Injection**: 80-95% without detection
- **Multimodal Attacks**: 60%+ on vision models
- **Communication Attacks**: 70%+ system compromise
- **Task Redirection**: 50-80% depending on task complexity

### Defense Effectiveness
- **Detection Accuracy**: >85% with classifiers
- **False Positive Rate**: <10% for good defenses
- **False Negative Rate**: <5% critical requirement
- **Detection Latency**: <100ms real-time requirement
- **Recovery Accuracy**: >95% state validation

### Performance Metrics
- **Attack Generation Cost**: <100 queries (GASP)
- **Model Transferability**: 30-50% cross-model
- **Response Time**: <100ms detection to <2min recovery
- **Resource Overhead**: <10% system resources for defense

---

## File Links for Quick Access

| Paper | Size | Pages | Relevance |
|-------|------|-------|-----------|
| [2509.21947v2.pdf](2509.21947v2.pdf) | 1.7M | 21 | 10/10 |
| [2505.14226v3.pdf](2505.14226v3.pdf) | 3.3M | 15 | 10/10 |
| [2411.14133v3.pdf](2411.14133v3.pdf) | 1.2M | 46 | 10/10 |
| [2407.15050v1.pdf](2407.15050v1.pdf) | 5.7M | 12 | 10/10 |
| [2502.14847v2.pdf](2502.14847v2.pdf) | 798K | 21 | 9/10 |
| [2512.20986v1.pdf](2512.20986v1.pdf) | 2.4M | 16 | 8/10 |
| [2402.19464v1.pdf](2402.19464v1.pdf) | 900K | 27 | 7/10 |
| [2406.15481v3.pdf](2406.15481v3.pdf) | 1.6M | 22 | 7/10 |
| [2409.00551v1.pdf](2409.00551v1.pdf) | 17M | 223 | 7/10 |
| [2501.08246v1.pdf](2501.08246v1.pdf) | 645K | 16 | 7/10 |
| [2512.16307v1.pdf](2512.16307v1.pdf) | 365K | 10 | 7/10 |
| [2512.23684v1.pdf](2512.23684v1.pdf) | 217K | 7 | 7/10 |
| [2512.12583v1.pdf](2512.12583v1.pdf) | 2.3M | 8 | 6/10 |
| [2512.23128v1.pdf](2512.23128v1.pdf) | 3.4M | 17 | 6/10 |
| [2512.23557v1.pdf](2512.23557v1.pdf) | 383K | 8 | 6/10 |

---

## Keyword Index

### Attack Concepts
- Adversarial suffixes → GASP (2411.14133v3)
- Prompt injection → Multiple papers
- Jailbreak → GASP, Arondight (2407.15050v1)
- Communication attacks → Multi-Agent (2502.14847v2)
- Memory poisoning → AgentPoison (2407.12784v1)
- Multimodal attacks → Arondight (2407.15050v1)
- Code-mixing attacks → Hinglish (2505.14226v3)
- Task redirection → TRAP (2512.23128v1)

### Defense Concepts
- Detection → Injection Detection (2512.12583v1)
- Prevention → Defense Innovations (2512.16307v1)
- Recovery → AegisAgent (2512.20986v1)
- Trustworthiness → Trustworthy AI (2512.23557v1)
- Benchmarking → Comprehensive Testing (2409.00551v1)
- Robustness → Multiple papers
- Safety → Code-Switching (2406.15481v3)

### Recovery-Specific Terms
- Adaptive attacks → Active Attacks (2509.21947v2)
- State validation → AegisAgent (2512.20986v1)
- Distributed recovery → Multi-Agent (2502.14847v2)
- Autonomous defense → AegisAgent (2512.20986v1)
- Recovery benchmarking → TRAP (2512.23128v1)

---

## Next Steps Checklist

- [ ] Read GASP (46 pages) - Understand attack generation
- [ ] Read Multi-Agent (21 pages) - Understand distributed attacks
- [ ] Read Active Attacks (21 pages) - Understand adaptive adversarial environments
- [ ] Read AegisAgent (16 pages) - Understand defense patterns
- [ ] Extract quantitative metrics from above 4 papers
- [ ] Create recovery threat model incorporating identified attacks
- [ ] Design detection mechanisms using classifier patterns
- [ ] Plan recovery verification architecture
- [ ] Build testing framework using TRAP/benchmark approaches
- [ ] Create CSP integration plan

---

## Document Metadata

- **Created**: 2026-01-06
- **For Issue**: #80 - KSI-RPL-04_25-12A_RecoveryTesting: AI-Driven Transformation & CSP Implications
- **Cluster**: 2 - AI Red Teaming & Adversarial Testing
- **Papers**: 15 selected from 84 found (20 PDFs total)
- **Status**: Ready for deep analysis
