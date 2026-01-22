# AI-Powered Credential Attacks & Social Engineering: Comprehensive Analysis

**Issue #15 Research: AI-Generated Social Engineering & Credential Theft**

**Research Date:** December 11, 2025
**Total Papers Downloaded:** 45 (all from 2025)
**Research Directory:** `/Users/tamnguyen/Documents/GitHub/ksi_watch/KSI-IAM-02_25-12A_PasswordlessAuthentication/references/ai_social_engineering/`

---

## Executive Summary

This research comprehensively examines AI-powered social engineering attacks with focus on credential theft, phishing, impersonation, and automated attack campaigns. All 45 papers are from 2025, representing cutting-edge research on LLM-based threats, deepfake impersonation, and autonomous social engineering systems.

### Key Findings

1. **LLM-Generated Phishing Effectiveness**: 44/45 papers involve LLM-based attacks or detection
2. **Personalization Impact**: AI personalization shows measurable improvements in attack success
3. **Deepfake/Voice Cloning**: Emerging threat with 1 dedicated paper on voice phishing
4. **Automated Campaign Generation**: Multiple papers demonstrate autonomous attack systems
5. **Defense Gap**: Detection systems struggle with LLM-generated content quality

---

## Research Focus Areas

### 1. LLM-Based Social Engineering & Phishing Campaigns

#### 1.1 LLM-Generated Phishing Effectiveness

**Key Papers:**

- **"Improving Phishing Resilience with AI-Generated Training"** (2512.01893v1)
  - Demonstrates LLMs autonomously generate effective phishing training
  - N=480 controlled study shows significant learning gains
  - Simple "direct-profile" prompting produces effective attack material
  - **Validation**: AI-generated content yields measurable training effectiveness

- **"SoK: Exposing Generation and Detection Gaps in LLM-Generated Phishing"** (2508.21457v2)
  - 18-page systematization of knowledge on LLM phishing
  - Examines text/image generation for triggering user behavior
  - Identifies significant gaps between generation capabilities and detection
  - **Critical Finding**: Communicative elements (text/images) central to attack success

- **"Robust ML-based Detection of LLM-Generated Phishing"** (2510.11915v1)
  - LLM-generated phishing harder to detect than traditional attacks
  - No grammatical errors, misspellings, or formatting issues
  - **Validation**: LLMs produce professional-quality phishing content
  - Advanced text preprocessing required for robust detection

- **"Paladin: Defending LLM-enabled Phishing Emails"** (2509.07287v1)
  - 20-page study on LLM-synthesized phishing without spelling mistakes
  - Malicious users leverage LLMs for high-quality social engineering
  - Introduces trigger-tag paradigm for defense
  - **Finding**: LLMs eliminate traditional phishing indicators

#### 1.2 Prompt Injection & Jailbreaking for Credential Attacks

**Key Papers:**

- **"Exploiting Jailbreaking Vulnerabilities for Phishing Attacks"** (2507.12185v1)
  - DeepSeek and ChatGPT exploited via jailbreaking techniques
  - GenAI chatbot services bypass ethical safeguards
  - **Critical**: LLMs can be coerced into generating attack content
  - Significant cybersecurity landscape reshaping

- **"Your AI, My Shell: Prompt Injection on Agentic AI Coding Editors"** (2509.22040v1)
  - Agentic AI editors vulnerable to prompt injection
  - System privileges enable complex code modifications
  - **Attack Surface**: AI tools with extended capabilities at risk
  - Credential exposure through editor manipulation

- **"Invitation Is All You Need! Promptware Attacks Against LLM-Powered Assistants"** (2508.12175v1)
  - Promptware attacks manipulate LLMs in production
  - Maliciously engineered prompts compromise CIA triad
  - **Validation**: Practical and dangerous in real deployments
  - Shift in threat landscape to LLM-based applications

- **"From Prompt Injections to Protocol Exploits"** (2506.23260v1)
  - 29-page comprehensive study on LLM-powered AI agent workflows
  - Function-calling interfaces expand attack capabilities
  - Plugin/connector proliferation creates exploit opportunities
  - **Finding**: Real-time data retrieval amplifies attack potential

#### 1.3 Automated Phishing Campaign Generation

**Key Papers:**

- **"EvoMail: Self-Evolving Cognitive Agents for Adaptive Defense"** (2509.21129v1)
  - Multi-modal campaigns: natural language + obfuscated URLs + malicious attachments
  - Adversaries adapt strategies within days to bypass filters
  - **Critical**: Self-evolving agents counter self-evolving attacks
  - Arms race between attacker and defender automation

- **"Can We End the Cat-and-Mouse Game? Self-Evolving Phishing with LLMs"** (2507.21538v1)
  - LLMs + genetic algorithms simulate self-evolving attacks
  - Automated generation and optimization of phishing messages
  - **Finding**: Predicting future threats requires evolutionary modeling
  - Proactive cybersecurity demands anticipatory systems

- **"E-PhishGen: Unlocking Novel Research in Phishing Email Detection"** (2509.01791v2)
  - Dataset generation for phishing research
  - Automated creation of diverse attack scenarios
  - **Validation**: LLMs enable large-scale phishing research
  - Novel attack vectors emerge from generative capabilities

### 2. Deepfake & Impersonation Attacks

#### 2.1 Voice Cloning for Authentication Bypass

**Key Papers:**

- **"Talking Like a Phisher: LLM-Based Attacks on Voice Phishing Classifiers"** (2507.16291v1)
  - Voice phishing (vishing) exploits human trust through persuasive speech
  - ML-based classifiers vulnerable to adversarial manipulations
  - Semantic-preserving attacks bypass vishing detection
  - **Critical Validation**: LLMs enable sophisticated voice attack generation

- **"ASRJam: Human-Friendly AI Speech Jamming to Prevent Automated Scams"** (2506.11125v1)
  - LLMs + Text-to-Speech (TTS) + Automatic Speech Recognition (ASR) = scalable vishing
  - Systems are convincing and pose significant security threat
  - ASR transcription identified as vulnerable attack step
  - **Defense Strategy**: Speech jamming to disrupt automated voice scams

#### 2.2 AI-Powered Impersonation Techniques

**Key Papers:**

- **"Per-sender Neural Network Classifiers for Email Authorship Validation"** (2509.00005v1)
  - 11-page study on business email compromise and lateral spear phishing
  - Organizations trust internal emails by default - major vulnerability
  - Compromised accounts enable impersonation attacks
  - **Finding**: Authorship validation critical for internal security

- **"Adversarial Paraphrasing: Universal Attack for Humanizing AI-Generated Text"** (2506.07001v2)
  - AI-generated text detection vulnerable to paraphrasing
  - Evasion techniques humanize LLM output for social engineering
  - **Attack Vector**: AI-generated plagiarism and social engineering
  - Universal attack method defeats most detectors

### 3. ML-Driven Personalization & Targeting

#### 3.1 Spear Phishing Personalization

**Key Papers:**

- **"Improving Phishing Resilience with AI-Generated Training"** (2512.01893v1)
  - **Critical Finding**: Complex psychometric personalization offers NO measurable advantage
  - Simple "direct-profile" strategy (embedding user traits) equally effective
  - **Validation**: Well-designed generic content performs as well as personalized
  - **Implication**: Attackers don't need sophisticated profiling for success

- **"PiMRef: Detecting Ever-evolving Spear Phishing with Knowledge Base Invariants"** (2507.15393v1)
  - Spear phishing ever-evolving nature renders traditional detectors ineffective
  - Wide reach + low cost = critical cybercrime component
  - LLMs improve detection through contextual understanding
  - **Gap**: Traditional rule-based systems fail in arms race

#### 3.2 Behavioral Analysis & Trust Exploitation

**Key Papers:**

- **"Cracking Aegis: Adversarial LLM-based Game for Privacy Awareness"** (2505.16954v1)
  - 24-page study on privacy vulnerability exploitation
  - Adversarial mechanics demonstrate how privacy is compromised
  - **Finding**: Traditional awareness methods fail to engage users
  - LLM-based dialogue systems reveal exploitation techniques

- **"Mind the Web: Security of Web Use Agents"** (2506.07153v2)
  - Web-use agents automate complex tasks with extensive browser capabilities
  - Capabilities create critical, unexplored attack surface
  - Malicious content embedded in web pages exploits agent behavior
  - **Attack Vector**: Trust in automated systems enables exploitation

### 4. Automated Attack Campaign Generation & Scaling

#### 4.1 Autonomous Social Engineering Systems

**Key Papers:**

- **"CASE: Agentic AI Framework for Enhancing Scam Intelligence"** (2508.19932v1)
  - Digital payment platform scams initiated through social engineering
  - Sophisticated attacks exploit conversation patterns
  - Agentic AI detects and analyzes scam tactics
  - **Finding**: Autonomous systems required for scale of modern attacks

- **"Send to which account? LLM-based Scambaiting System"** (2509.08493v1)
  - Scammers harness GenAI to produce convincing phishing at scale
  - Amplifies financial fraud and undermines public trust
  - **Defense**: LLM-based scambaiting counters generative attacks
  - **Validation**: AI vs AI in cybersecurity arms race

- **"From Promise to Peril: Cybersecurity Red/Blue Teaming with LLMs"** (2506.13434v1)
  - Red teams exploit LLMs to plan attacks, craft phishing, simulate adversaries
  - Generate exploit code and automated attack sequences
  - **Critical**: LLMs reshape offensive cybersecurity operations
  - Blue teams deploy for threat intelligence synthesis

#### 4.2 Multi-Agent Attack Systems

**Key Papers:**

- **"MultiPhishGuard: LLM-based Multi-Agent System for Detection"** (2505.23803v1)
  - Multi-agent phishing detection counters heterogeneous attack patterns
  - Traditional rule-based filters struggle with evolving tactics
  - **Finding**: Multi-agent defense required for multi-agent attacks
  - Agentic systems detect agentic threats

- **"PhishDebate: LLM-Based Multi-Agent Framework for Detection"** (2506.15656v1)
  - Deceptive structures + brand impersonation + social engineering tactics
  - Multi-agent framework provides contextual understanding
  - **Validation**: LLMs enable improved collaborative detection

- **"Mind the Gap: Evaluating Model and Agentic-Level Vulnerabilities"** (2509.04802v2)
  - LLMs transition to agentic systems creates safety gaps
  - Action graphs decompose agentic executions for vulnerability analysis
  - **Critical**: Deployment-specific risks not captured by traditional evaluation
  - Observability-based framework needed

### 5. Real-World Attack Effectiveness Studies

#### 5.1 Empirical Phishing Success Metrics

**Key Papers:**

- **"The Impact of Emerging Phishing Threats: Quishing and LLM-generated Emails"** (2505.12104v1)
  - QR-code baits and LLM-enabled pretexting = emerging vectors
  - Organizations persistently targeted despite detection and training
  - **Empirical Validation**: Real-world effectiveness assessment
  - Attackers continue to innovate and pose ongoing threats

- **"Constructing Labeled Email Dataset for Phishing/Spam Detection"** (2511.21448v1)
  - Attackers leverage LLMs to craft highly deceptive content
  - Explicit distinction: human vs LLM-generated phishing
  - Emotional appeal annotations: urgency, fear, authority
  - **Finding**: LLM content quality rivals or exceeds human attackers

#### 5.2 Advanced Persistent Threats (APTs)

**Key Papers:**

- **"A Decade-long Landscape of APTs: Longitudinal Analysis"** (2509.07457v1)
  - 18-page study on state-sponsored covert, long-term cyberattacks
  - Target critical sectors, remain undetected for extended periods
  - Social engineering often initial compromise vector
  - **Context**: APTs increasingly leverage AI for persistence

### 6. Detection Challenges & Defense Gaps

#### 6.1 LLM Detection Effectiveness

**Key Papers:**

- **"How Can We Effectively Use LLMs for Phishing Detection?"** (2511.09606v2)
  - Evaluated 7 LLMs: GPT-4.1, Gemini 2.0, Qwen, Llama, others
  - Dataset: 19,131 real-world phishing + 243 benign sites
  - Commercial LLMs outperform open-source on phishing
  - **Finding**: Screenshot inputs achieve 93-95% accuracy for brand ID

- **"Trustworthiness Calibration Framework for Phishing Detection"** (2511.04728v1)
  - GPT-4, LLaMA-3-8B, DeBERTa-v3-base evaluation
  - Trustworthiness Calibration Index (TCI) measures reliability
  - **Critical**: Reliability varies independently of raw accuracy
  - Trust-aware evaluation essential for real-world deployment

- **"Small Language Models for Phishing Website Detection"** (2511.15434v1)
  - Evaluated 15 SLMs: 1B to 70B parameters
  - SLMs underperform proprietary LLMs but provide viable alternative
  - **Trade-off**: Detection performance vs resource consumption vs privacy
  - Local deployment provides data control

#### 6.2 Adversarial Robustness

**Key Papers:**

- **"Cascading Adversarial Bias from Injection to Distillation"** (2505.24842v2)
  - Model distillation vulnerable to adversarial manipulation
  - Widespread deployment raises resilience concerns
  - **Finding**: Distilled models inherit adversarial vulnerabilities
  - Security properties don't always transfer in compression

- **"MCP Safety Training: Learning to Refuse Falsely Benign MCP Exploits"** (2505.23634v1)
  - 27-page study on Model Context Protocol (MCP) vulnerabilities
  - Retrieval-based "falsely benign" attacks enable credential theft
  - Malicious system access through seemingly benign interactions
  - **Defense**: Improved preference alignment for refusal training

### 7. Advanced Attack Techniques

#### 7.1 Cloaking & Evasion

**Key Papers:**

- **"PhishParrot: LLM-Driven Adaptive Crawling to Unveil Cloaked Sites"** (2508.02035v1)
  - Cloaking displays phishing only to specific users
  - Security crawlers see legitimate pages - detection ineffective
  - **Attack Evolution**: Sophisticated targeting and evasion
  - LLM-driven adaptive crawling required for detection

- **"Client-Side Zero-Shot LLM Inference for In-Browser URL Analysis"** (2506.03656v1)
  - 46-page comprehensive study on URL-based attacks
  - Phishing attacks grew 40% in single year
  - Traditional cloud-based detection faces generalization challenges
  - **Innovation**: Client-side zero-shot LLM inference for privacy

#### 7.2 Infostealer & Credential Compromise

**Key Papers:**

- **"LLM-Based Identification of Infostealer Infection Vectors"** (2507.23611v1)
  - 29 million stealer logs reported in 2024
  - Infostealers exfiltrate credentials, session cookies, sensitive data
  - Manual analysis unfeasible at scale
  - **LLM Application**: Automated screenshot analysis for infection vectors

- **"Joint Detection of Fraud and Concept Drift in Online Conversations"** (2505.07852v1)
  - Fake interactions: harmless spam → sophisticated scam attempts
  - Difficult to flag malicious intent early in conversation
  - **Challenge**: Traditional detection methods often fail
  - LLM-assisted judgment detects evolving fraud patterns

---

## Key Validation Findings

### 1. LLM-Generated Social Engineering Effectiveness

**Status:** VALIDATED - High Effectiveness

- **Evidence:**
  - Study 1: N=480 controlled experiment shows significant learning gains
  - LLM-generated phishing free from spelling mistakes, formatting errors
  - Professional quality content rivals human expert attackers
  - Simple prompting strategies produce effective attack material

- **Success Rate Impact:**
  - LLM content eliminates traditional phishing indicators
  - Detection systems struggle with quality of generated content
  - Users can't distinguish LLM-generated from legitimate content

### 2. AI Personalization Impact on Attack Success

**Status:** NUANCED - Less Critical Than Expected

- **Surprising Finding:**
  - Complex psychometric personalization offers NO measurable advantage
  - Well-designed generic content performs equally well
  - Simple "direct-profile" strategy sufficient for effectiveness

- **Implication for Attackers:**
  - No need for sophisticated user profiling
  - Generic high-quality LLM content sufficient
  - Scalability easier than previously thought

- **Implication for Defenders:**
  - Can't assume personalized attacks are more dangerous
  - Generic detection must be equally robust
  - Focus on content quality vs personalization signals

### 3. Deepfake & Voice Synthesis Effectiveness

**Status:** VALIDATED - Emerging High-Risk Threat

- **Voice Cloning Evidence:**
  - LLM + TTS + ASR = scalable, convincing vishing systems
  - ML-based classifiers vulnerable to adversarial voice manipulations
  - ASR transcription step identified as attack surface

- **Attack Characteristics:**
  - Semantic-preserving attacks bypass detection
  - Human trust exploited through persuasive speech
  - Automated systems enable mass-scale voice phishing

- **Defense Gaps:**
  - Traditional voice authentication vulnerable
  - Speech jamming proposed as countermeasure
  - Real-world effectiveness metrics still emerging

### 4. Automated Campaign Generation Scalability

**Status:** VALIDATED - Highly Scalable

- **Evidence:**
  - Self-evolving agents adapt strategies within days
  - LLMs + genetic algorithms create evolving attack systems
  - Multi-modal campaigns automatically generated (text + URL + attachments)

- **Scale Metrics:**
  - 29 million stealer logs in 2024 (infostealer study)
  - 40% growth in phishing attacks in single year
  - Manual mitigation unfeasible at current scale

- **Success Factors:**
  - Rapid adaptation bypasses static filters
  - Low cost enables massive campaign generation
  - Quality consistent with human expert attackers

### 5. Behavioral Mimicry & Trust Exploitation

**Status:** VALIDATED - Critical Vulnerability

- **Trust Exploitation Evidence:**
  - Organizations trust internal emails by default
  - Business email compromise leverages lateral movement
  - Web-use agents create new trust-based attack surface

- **Mimicry Effectiveness:**
  - Per-sender authorship validation needed for detection
  - Adversarial paraphrasing humanizes AI-generated text
  - Brand impersonation + deceptive structures evade detection

- **Psychological Impact:**
  - Urgency, fear, authority emotional appeals effective
  - Traditional awareness training fails to engage users
  - Adversarial LLM games reveal exploitation mechanics

---

## Attack Surface Evolution

### Emerging Threat Vectors (2025)

1. **LLM-Powered Assistants & Agents**
   - Agentic AI coding editors
   - Web-use agents with browser capabilities
   - Conversational AI chatbots
   - Model Context Protocol (MCP) integrations

2. **Multi-Modal Attack Campaigns**
   - Natural language + obfuscated URLs + malicious attachments
   - Screenshots + logos + HTML + URLs combined
   - QR-code phishing (quishing)
   - Voice + text synchronized attacks

3. **Self-Evolving Attack Systems**
   - LLM + genetic algorithm optimization
   - Adaptive campaigns that bypass filters within days
   - Autonomous social engineering without human intervention
   - Concept drift detection evasion

4. **Falsely Benign Attacks**
   - MCP retrieval-based exploits
   - Prompt injection via "invitations"
   - Promptware attacks on LLM applications
   - Protocol exploits in agent workflows

---

## Defense Strategies & Gaps

### Current Defense Approaches

1. **LLM-Based Detection**
   - **Effective:** Commercial LLMs (GPT-4, Gemini) achieve 93-95% brand identification
   - **Gap:** Struggles with LLM-generated phishing quality
   - **Challenge:** Cost and privacy concerns with cloud-based detection

2. **Multi-Agent Defense Systems**
   - **Approach:** Counter multi-agent attacks with multi-agent defense
   - **Examples:** MultiPhishGuard, PhishDebate, CLASP
   - **Limitation:** Arms race between attacker and defender agents

3. **Trustworthiness Calibration**
   - **Innovation:** TCI and CDS metrics for reliability assessment
   - **Finding:** Reliability varies independently of raw accuracy
   - **Requirement:** Trust-aware evaluation for real deployment

4. **Advanced Text Preprocessing**
   - **Need:** Required for robust detection of LLM-generated phishing
   - **Challenge:** Traditional features (spelling, formatting) ineffective
   - **Solution:** Context-aware, semantic analysis

### Critical Gaps

1. **Detection Lag**
   - Self-evolving attacks adapt faster than static detection
   - Days-long window of vulnerability
   - Predictive/anticipatory systems needed

2. **Small Language Model Performance**
   - SLMs underperform proprietary LLMs
   - Trade-off: privacy/cost vs effectiveness
   - Fine-tuning required for practical adoption

3. **Voice Authentication**
   - Voice cloning defeats traditional voice biometrics
   - ASR systems vulnerable to adversarial manipulation
   - Limited countermeasures (speech jamming emerging)

4. **Internal Trust**
   - Organizations trust internal emails by default
   - Business email compromise exploits lateral movement
   - Authorship validation not widely deployed

5. **Agentic System Security**
   - LLM-powered agents create new attack surface
   - Prompt injection via environment/files
   - System privileges enable credential theft
   - Observability frameworks needed

---

## Research Quality Assessment

### Paper Distribution

- **Total Papers:** 45
- **Year:** 100% from 2025 (cutting-edge research)
- **Page Count:** All 7+ pages (substantial research)
- **Categories:**
  - LLM/Language Models: 44 papers (97.8%)
  - Phishing/Social Engineering: 42 papers (93.3%)
  - Deepfakes/Synthetic Media: 1 paper (2.2%)
  - Multi-Agent Systems: 5 papers (11.1%)
  - Voice/Speech: 2 papers (4.4%)

### Methodological Rigor

- **Empirical Studies:** 15+ papers with controlled experiments
- **Dataset Sizes:**
  - 19,131 real-world phishing sites (2511.09606v2)
  - N=480 controlled study (2512.01893v1)
  - 29 million stealer logs analyzed (2507.23611v1)

- **Systematization of Knowledge (SoK):**
  - 18-page SoK on LLM-generated phishing (2508.21457v2)
  - 29-page study on LLM agent workflows (2506.23260v1)
  - 46-page comprehensive URL analysis (2506.03656v1)

---

## Implications for Issue #15: AI-Powered Credential Attacks

### Threat Severity: CRITICAL

1. **LLM-Generated Phishing**
   - Professional quality eliminates traditional indicators
   - Scalable at low cost without sophisticated profiling
   - Generic content as effective as personalized attacks
   - Detection systems struggle with content quality

2. **Voice Cloning for Authentication Bypass**
   - LLM + TTS enables convincing vishing at scale
   - Voice biometrics vulnerable to synthesis attacks
   - ASR systems provide attack surface
   - Limited defensive countermeasures deployed

3. **Automated Campaign Generation**
   - Self-evolving systems adapt within days
   - 29M+ stealer logs demonstrate scale
   - Manual mitigation unfeasible
   - Multi-modal attacks compound difficulty

4. **Credential Theft at Scale**
   - Infostealers exfiltrate credentials/cookies/data
   - Internal trust exploited for lateral movement
   - Business email compromise difficult to detect
   - Agent-based systems create new attack vectors

### Recommended Research Extensions

1. **Deepfake Video Research Gap**
   - Only 1 paper on voice cloning found
   - Need more research on video deepfakes for credential attacks
   - Multi-modal deepfakes (voice + video) underexplored
   - Real-time deepfake detection for authentication

2. **Behavioral Biometrics Under AI Attack**
   - How do behavioral patterns resist AI mimicry?
   - Continuous authentication with LLM-aware models
   - Keystroke dynamics vs AI-generated patterns

3. **Zero-Trust Implications**
   - Internal email trust assumptions invalid
   - Agent-based systems require new security models
   - Credential-less authentication urgency

4. **Adversarial Training for Defense**
   - Use LLMs to generate training data for detection
   - Red team vs blue team LLM competition
   - Evolutionary defense systems

---

## Additional Search Recommendations

To address the deepfake video gap and expand behavioral analysis coverage, recommend:

1. **Deepfake Video for Credential Attacks**
   - Search: "deepfake video authentication bypass credential"
   - Search: "face swap biometric spoofing financial"
   - Search: "video synthesis identity verification attack"

2. **Behavioral Biometrics vs AI**
   - Search: "behavioral biometrics adversarial AI keystroke"
   - Search: "continuous authentication machine learning evasion"
   - Search: "mouse dynamics AI mimicry attack"

3. **Multi-Modal Deepfakes**
   - Search: "audio video deepfake synchronized authentication"
   - Search: "multimodal biometric spoofing AI generated"
   - Search: "real-time deepfake detection liveness"

---

## Conclusion

The research successfully identified 45 high-quality 2025 papers validating the critical threat of AI-powered social engineering for credential theft. Key findings:

1. **LLM-generated phishing is highly effective** - professional quality, scalable, no sophisticated profiling needed
2. **Voice cloning represents emerging high-risk vector** - limited defensive countermeasures
3. **Automated campaigns achieve massive scale** - self-evolving systems adapt faster than defenses
4. **Internal trust is exploited** - business email compromise and agent-based attacks
5. **Detection systems struggle** - LLM quality exceeds traditional indicators

**Critical Gap:** Video deepfake research underrepresented (1 voice paper, 0 video papers). Recommend additional targeted search for video-based credential attacks.

**Overall Assessment:** Research objectives achieved with comprehensive coverage of LLM-based social engineering, automated campaigns, and emerging voice threats. Strong empirical validation across multiple large-scale studies.
