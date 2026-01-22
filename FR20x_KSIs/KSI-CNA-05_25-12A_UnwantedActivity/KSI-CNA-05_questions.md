# Unwanted Activity (DoS/DDoS) Detection & Mitigation: Discovery Questions

**KSI Focus:** CNA-05 - Detect and mitigate unwanted activity including denial-of-service (DoS) attacks powered by AI, adaptive botnets, and multi-vector coordinated campaigns. Implement behavioral analytics, anomaly detection, real-time response automation, multi-Tbps scrubbing infrastructure, and economic DoS (Denial of Wallet) protection to maintain availability during sophisticated attacks.

**Context:** This discovery question set consolidates auditor, CIO, and customer perspectives to assess whether organizations effectively defend against AI-powered DoS attacks through infrastructure capacity, detection speed, mitigation automation, AI-driven behavioral analytics, adversarial robustness testing, and economic denial protection. Questions focus on sub-10s detection latency, sub-60s mitigation, always-on protection architecture, multi-vector attack coordination, and DoW detection and prevention.

---

## Section 1: AI-Powered Attack Capability Assessment

**KSI-CNA-05-Q1:** What AI-powered attack methodologies have you detected in past 12 months? Document: (a) adaptive attacks using reinforcement learning to adjust tactics mid-attack, (b) behavioral mimicry attacks generating traffic that replicates human patterns (typing cadence, mouse movement), (c) multi-vector coordinated attacks (L3 flood + L7 API abuse simultaneously), (d) evasion techniques (attacks staying below static rate-limit thresholds). Provide examples of detected AI-driven botnets with evidence of learning/adaptation.

**KSI-CNA-05-Q2:** Can your detection systems distinguish AI-generated attack traffic from legitimate user traffic when attackers use behavioral mimicry? Describe detection methodology: (a) What behavioral signals identify human vs. bot traffic? (b) What is false negative rate (legitimate AI-generated traffic misclassified as attack)? (c) Provide examples of detected behavioral mimicry attacks with detection accuracy metrics.

**KSI-CNA-05-Q3:** For multi-vector attacks (simultaneous L3 volumetric + L4 protocol + L7 application-layer attacks), how do you detect and correlate across layers? Document: (a) Detection method for each vector type independently, (b) Correlation logic connecting simultaneous vectors, (c) Latency to detect multi-vector coordination, (d) Examples from past 12 months with detection timelines.

---

## Section 2: Anomaly Detection & Real-Time Intrusion Identification

**KSI-CNA-05-Q4:** Describe your anomaly detection architecture for DoS/DDoS: (a) What is your baseline methodology (per-customer, per-endpoint, dynamic adaptation)? (b) How frequently is baseline refreshed (daily, hourly, continuous)? (c) What is your false positive rate on legitimate traffic spikes (flash crowds, marketing campaigns)? (d) Can you detect low-and-slow attacks that stay below volumetric thresholds?

**KSI-CNA-05-Q5:** What machine learning models do you use for anomaly detection? Document: (a) Model types (CNN, LSTM, Autoencoder, Graph Neural Networks, Transformer)? (b) What features are analyzed (packet size, header patterns, request rate, geographic origin, behavioral signals)? (c) How often are models retrained (weekly, monthly, quarterly)? (d) What datasets inform training (UNSW-NB15, CIC-IDS, custom captures)?

**KSI-CNA-05-Q6:** What is your detection speed for novel attack patterns with no prior training data? Provide: (a) P50/P95/P99 detection latency for zero-day attacks from attack start to alert, (b) Comparison to known attack detection latency, (c) Examples of zero-day attacks detected in past 12 months, (d) Methodology for handling unsupervised anomalies vs. supervised attacks.

**KSI-CNA-05-Q7:** How do you monitor for model drift in production? Describe: (a) Drift detection procedures and alerting, (b) Impact if model accuracy degrades in production (happens undetected?), (c) Retraining trigger (manual, automated), (d) Historical trend: has detection accuracy remained stable or degraded over past 12 months?

---

## Section 3: DDoS Detection & Mitigation Infrastructure

**KSI-CNA-05-Q8:** What is your sub-10-second detection SLA for DDoS attacks? Provide: (a) Total scrubbing infrastructure capacity (Tbps), (b) Geographic distribution (number of edge locations, regions), (c) P50/P95/P99 detection latency from attack start to first alert for past 12 months, (d) Percentage of attacks exceeding 10s detection SLA, (e) Root cause analysis for detection failures/delays.

**KSI-CNA-05-Q9:** What is your sub-60-second mitigation SLA? Document: (a) Mitigation mechanisms for each attack type (L3 volumetric: scrubbing, rate limiting; L4: protocol validation; L7: WAF, behavioral blocking), (b) Automation percentage (fully automated 0-15s, semi-automated 15-30s, manual >30s), (c) P50/P95/P99 mitigation latency for past 12 months, (d) False positive rate (legitimate traffic blocked), (e) Mitigation effectiveness (percentage of attack volume reduced).

**KSI-CNA-05-Q10:** Is your DDoS protection always-on or on-demand? Explain: (a) Architecture (traffic continuously filtered vs. activated after detection), (b) If on-demand, activation time and blind window, (c) Latency impact on legitimate traffic if always-on, (d) SLA compliance: can you meet 99.9%+ uptime with current architecture?, (e) Largest attack mitigated to date (size, duration, attack type).

**KSI-CNA-05-Q11:** Describe your edge scrubbing deployment: (a) Number and geographic distribution of edge locations, (b) Technologies deployed at edge (eBPF/XDP, WAF, rate limiting, protocol validation), (c) Routing methodology to nearest edge (Anycast, DNS-based, BGP), (d) Latency from customer origin to nearest scrubbing edge (P50/P95), (e) Mitigation effectiveness at edge (percentage of attack volume blocked before regional/core infrastructure).

**KSI-CNA-05-Q12:** How do you ensure multi-layer defense coordination (L3/L4/L7)? Provide: (a) L3/L4 controls (ingress filtering/BCP 38, protocol validation, SYN cookies, amplification prevention), (b) L7 controls (WAF, HTTP flood protection, challenge-response, API rate limiting), (c) Multi-vector attack examples showing coordinated response across layers, (d) Correlation logic ensuring layers activate simultaneously, (e) Detection latency for multi-layer response.

---

## Section 4: Economic Denial-of-Service (DoW) Protection

**KSI-CNA-05-Q13:** Do you have real-time cost anomaly detection for Denial-of-Wallet (DoW) attacks? Describe: (a) Monitoring scope (per-customer, per-service, per-region cost tracking), (b) Anomaly detection methodology (what signals indicate DoW attack vs. legitimate spikes?), (c) Alert latency (how quickly detected after cost spike begins?), (d) Historical DoW incidents: any $10K+ cost anomalies in past 12 months? Detection latency?

**KSI-CNA-05-Q14:** What auto-scaling safeguards prevent DoW exploitation? Document: (a) Per-customer scaling caps (max scaling multiplier, time window), (b) Burst budgets with cost-based circuit breakers, (c) Can attackers trigger infinite scaling by generating sustained traffic?, (d) Cost-aware orchestration (Kubernetes, cloud platform integration), (e) Historical incidents: any auto-scaling exploitations detected?

**KSI-CNA-05-Q15:** How do you defend against expensive operation targeting (API cost amplification, ML inference exploitation, token multiplication)? Describe: (a) Identification of high-cost operations (inference APIs, data export, report generation), (b) Rate limiting on expensive operations, (c) Request batching and cost aggregation, (d) Detection of abnormal request patterns targeting expensive operations, (e) Examples of detected resource exhaustion attacks.

---

## Section 5: Deep Learning & Advanced ML Defense Systems

**KSI-CNA-05-Q16:** What adversarial robustness testing do you conduct on AI-powered defense models? Provide: (a) Testing methodology (evasion attacks via adversarial perturbations, poisoning attacks, model inversion, model extraction attacks), (b) Adversarial example generation methods and transferability testing (attacks trained on one model that work on yours), (c) Testing frequency (quarterly, annually, ad-hoc) and who conducts testing (internal red team, external security firm), (d) Recent red team report results showing evasion attack success/failure rates and percentage of adversarial examples successfully detected/blocked, (e) Remediation status for findings, (f) Defense mechanisms implemented against adversarial inputs.

**KSI-CNA-05-Q17:** What are your ML model performance metrics for DDoS detection? Provide current and historical (past 12 months): (a) Accuracy, Precision, Recall, F1-Score, (b) False Positive Rate, False Negative Rate, (c) Comparison: test dataset metrics vs. production metrics (large gap indicates overfitting/drift), (d) Trend analysis: has accuracy remained stable or degraded?, (e) Model performance benchmarks vs. industry standards.

---

## Section 6: Distributed & Federated Defense Architectures

**KSI-CNA-05-Q18:** Do you use federated learning for collaborative threat intelligence without data centralization? If yes, explain: (a) Architecture (how distributed threat data is shared), (b) Organizations involved in threat intelligence consortium, (c) Privacy-preserving techniques (differential privacy, secure multi-party computation), (d) Threat intelligence improvement from federated approach (detection accuracy lift vs. isolated model).

**KSI-CNA-05-Q19:** For multi-cloud or distributed CSP deployments, how do you ensure consistent DDoS protection policy across regions/clouds? Describe: (a) Policy abstraction layer enabling portable rules, (b) Consistency verification during policy distribution, (c) Latency impact of policy synchronization, (d) Examples of attack where coordinated response required across clouds.

---

## Section 7: DDoS-Specific SLA Accountability

**KSI-CNA-05-Q20:** Are DoS/DDoS attacks included in your uptime SLA commitment? Document: (a) Uptime SLA percentage (99.9%, 99.95%, 99.99%), (b) Whether DDoS events are explicitly included or excluded from SLA calculations, (c) If excluded, what is the recourse for customers impacted by DDoS?, (d) Evidence of SLA compliance for past 12 months for DDoS events (redacted customer examples).

---

## Section 8: Incident Response & Forensics

**KSI-CNA-05-Q21:** What is your incident detection-to-response SLA for critical DDoS incidents? Provide: (a) Definition of "critical" incident (attack size, duration, customer impact), (b) Detection-to-response time for past critical incidents (P50/P95), (c) Automated response triggers vs. human escalation points, (d) 24/7 SOC staffing for incident response, (e) Customer communication SLA (notification of attack, mitigation status updates).

**KSI-CNA-05-Q22:** How do you maintain immutable, tamper-proof audit trails for DDoS incidents? Describe: (a) What is logged (attack timestamps, detection logic, mitigation actions, customer interactions), (b) Audit log storage (location, retention duration), (c) Integrity verification (cryptographic hashing, blockchain, other methods), (d) Access controls on audit logs (who can read/delete?), (e) Forensic investigation capability: can you prove logs were not modified post-incident?

**KSI-CNA-05-Q23:** For attacks causing SLA violations or customer impact, what root cause analysis is conducted? Document: (a) RCA process and timeline, (b) Was it detection failure (attack not detected in time)?, (c) Was it mitigation failure (detected but not mitigated effectively)?, (d) Was it false positive (legitimate traffic blocked)?, (e) Corrective actions and timeline to prevent recurrence.

---

## Section 9: Continuous Improvement & Threat Evolution

**KSI-CNA-05-Q24:** How do you adapt defenses as attack sophistication evolves? Describe: (a) Monitoring of emerging attack techniques (botnet evolution, new evasion methods), (b) Threat intelligence feeds integrated (MITRE ATT&CK, vendor feeds, custom analysis), (c) Frequency of defense updates (weekly, monthly, as needed), (d) Testing of new defenses before production deployment via chaos engineering (fault injection testing, systematic injection of failures), (e) Frequency of chaos experiments (monthly, quarterly), (f) Failure scenarios tested (detection system failure, mitigation system failure, partial infrastructure outage), (g) Attack trend analysis: what new attack types emerged in past 6 months? How did you respond?, (h) Learning from chaos testing and improvements deployed.

---

## Section 10: Performance Benchmarking & Transparency

**KSI-CNA-05-Q25:** Can you provide historical attack data and performance metrics for past 12 months? Supply: (a) Count of DDoS attacks by type (L3 volumetric, L4 protocol, L7 application), (b) Distribution of attack sizes (small, medium, large, mega), (c) Percentage of attacks causing customer-visible impact, (d) P50/P95/P99 detection and mitigation latencies, (e) Redacted case studies of complex multi-vector attacks and response.

**KSI-CNA-05-Q26:** Do you publish real-time DDoS metrics and transparency reports? Describe: (a) Customer-accessible dashboards showing real-time attack metrics, (b) Historical attack data available for analysis, (c) Monthly transparency reports (if published), (d) Attack statistics by region, customer segment, attack type, (e) Comparative metrics vs. industry benchmarks (if available).

---

## Section 11: DDoS-Specific Threat Intelligence Integration

**KSI-CNA-05-Q27:** What DDoS-specific threat intelligence feeds and external data sources inform your detection systems? Document: (a) Threat intelligence sources (MITRE ATT&CK DDoS tactics, vendor feeds, ISACs, custom sensors), (b) Integration frequency (real-time, hourly, daily), (c) Validation of threat intelligence (how do you verify accuracy and reduce false signals?), (d) Feedback loop: do you contribute threat intelligence to external sources?, (e) Impact of threat intelligence on detection accuracy improvement vs. isolated model.

---

## Schema Reference

**Question ID Format:** KSI-[KSI-CODE]-Q##
Example: KSI-CNA-05-Q1

**All questions should be answered with:**
- Direct evidence (not claims)
- Quantifiable data where applicable
- Supporting documentation (architecture diagrams, policies, audit logs, test results)
- AI-specific examples where relevant
- Timeline/frequency information
- Comparison to research benchmarks when available

---

**Version:** 2.0 (Refined)
**Generated:** 2026-01-13
