# Top Papers: AI-Powered Credential Attacks

**Issue #15 Critical Research - Credential Theft Focus**

---

## Tier 1: Must-Read Papers (Direct Credential Theft)

### 1. LLM-Based Identification of Infostealer Infection Vectors (2507.23611v1)

**Why Critical:**
- **29 million stealer logs in 2024** - massive credential compromise scale
- Infostealers exfiltrate credentials, session cookies, sensitive data
- LLM-based screenshot analysis for automated detection
- Manual analysis unfeasible at scale

**Credential Theft Mechanism:**
- Automated credential harvesting from infected systems
- Session cookie theft enables account takeover without passwords
- Sensitive data exfiltration includes authentication tokens

**File:** `2507.23611v1.pdf`

---

### 2. MCP Safety Training: Falsely Benign MCP Exploits (2505.23634v1)

**Why Critical:**
- 27-page comprehensive study on credential theft via MCP
- Retrieval-based "falsely benign" attacks appear harmless
- Malicious system access and **credential theft explicitly mentioned**
- Attacks bypass security through seemingly benign interactions

**Credential Theft Mechanism:**
- MCP protocol exploited for unauthorized credential access
- Falsely benign requests hide malicious intent
- System access escalation leads to credential exfiltration

**File:** `2505.23634v1.pdf`

---

### 3. Per-sender Neural Network Classifiers for Email Authorship Validation (2509.00005v1)

**Why Critical:**
- **Business email compromise** - direct credential theft vector
- **Lateral spear phishing** from compromised accounts
- Organizations trust internal emails by default - exploited for credentials
- Compromised accounts impersonate trusted senders

**Credential Theft Mechanism:**
- Initial account compromise via phishing
- Lateral movement using compromised credentials
- Internal trust exploited for further credential harvesting
- Business email compromise targets financial/authentication systems

**File:** `2509.00005v1.pdf`

---

### 4. Constructing Labeled Email Dataset: LLM-Generated Phishing (2511.21448v1)

**Why Critical:**
- Explicitly annotates **credential theft** as phishing motivation
- Distinguishes human vs LLM-generated credential theft attempts
- Emotional appeal analysis: urgency, fear, authority
- LLMs craft highly deceptive credential-harvesting emails

**Credential Theft Mechanism:**
- Phishing emails specifically designed for credential theft
- LLM-generated content targets authentication information
- High-quality deceptive content bypasses user awareness

**File:** `2511.21448v1.pdf`

---

### 5. Invitation Is All You Need! Promptware Attacks on LLM Assistants (2508.12175v1)

**Why Critical:**
- LLM-powered assistants in production compromised via prompts
- Malicious prompts manipulate **CIA triad** (includes credentials)
- Practical and dangerous in real deployments
- Shift in threat landscape to LLM applications with credential access

**Credential Theft Mechanism:**
- Prompt injection causes LLM to reveal/exfiltrate credentials
- LLM assistants with system access manipulated
- Production environments with authentication systems at risk

**File:** `2508.12175v1.pdf`

---

## Tier 2: High-Priority Papers (Authentication Bypass)

### 6. Talking Like a Phisher: LLM-Based Voice Phishing Attacks (2507.16291v1)

**Why Critical:**
- Voice phishing (vishing) targets authentication systems
- LLMs generate adversarial voice attacks that preserve semantics
- ML-based vishing classifiers vulnerable to manipulation
- Human trust exploited through persuasive speech for credentials

**Authentication Bypass Mechanism:**
- Voice-based identity verification defeated
- Social engineering via phone for credential extraction
- Automated vishing at scale

**File:** `2507.16291v1.pdf`

---

### 7. ASRJam: Preventing Automated Phone Scams (2506.11125v1)

**Why Critical:**
- LLM + TTS + ASR = scalable, convincing vishing for credentials
- Automated voice phishing systems pose significant security threat
- ASR transcription step identified as attack surface
- Defense mechanism (speech jamming) proposed

**Authentication Bypass Mechanism:**
- Automated voice systems target credential disclosure
- Phone-based authentication bypassed via AI voice
- Scalable attacks enable mass credential harvesting

**File:** `2506.11125v1.pdf`

---

### 8. "Your AI, My Shell": Prompt Injection on Agentic AI Coding Editors (2509.22040v1)

**Why Critical:**
- Agentic AI editors have **system privileges**
- Complex code modifications enable credential exposure
- Prompt injection via files/environment
- Developer credentials at risk in coding environments

**Credential Theft Mechanism:**
- System privileges allow credential file access
- Git credentials, API keys in development environments
- Editor capabilities manipulated to exfiltrate secrets

**File:** `2509.22040v1.pdf`

---

### 9. From Prompt Injections to Protocol Exploits (2506.23260v1)

**Why Critical:**
- 29-page study on LLM-powered AI agent workflow vulnerabilities
- Function-calling interfaces expand **credential access** capabilities
- Real-time data retrieval includes authentication systems
- Plugin/connector proliferation creates credential exposure

**Credential Theft Mechanism:**
- Agent workflows access authentication APIs
- Protocol exploits reveal stored credentials
- Inter-agent communication leaks authentication tokens

**File:** `2506.23260v1.pdf`

---

### 10. Mind the Web: Security of Web Use Agents (2506.07153v2)

**Why Critical:**
- Web-use agents automate tasks with **extensive browser capabilities**
- Critical, previously unexplored attack surface
- Malicious content embedded in web pages exploits agents
- Browser automation includes form filling (credentials)

**Credential Theft Mechanism:**
- Agents manipulated to input credentials in phishing sites
- Browser capabilities include password manager access
- Automated form filling with authentication data

**File:** `2506.07153v2.pdf`

---

## Tier 3: Important Context Papers (Attack Effectiveness)

### 11. Improving Phishing Resilience with AI-Generated Training (2512.01893v1)

**Why Critical:**
- N=480 controlled study validates AI phishing effectiveness
- Simple prompting produces effective credential-harvesting content
- No need for complex personalization - scales credential attacks
- Organizations struggle with LLM-generated phishing quality

**Credential Attack Context:**
- Validates that AI-generated phishing works for credential theft
- Training effectiveness shows users fall for AI phishing
- Generic content sufficient - enables mass credential harvesting

**File:** `2512.01893v1.pdf`

---

### 12. Paladin: Defending LLM-enabled Phishing Emails (2509.07287v1)

**Why Critical:**
- 20-page study on LLM-synthesized phishing for credentials
- No spelling mistakes - eliminates traditional phishing indicators
- Malicious users leverage LLMs for credential-harvesting emails
- Defense mechanisms required specifically for LLM phishing

**Credential Attack Context:**
- High-quality credential phishing via LLMs
- Traditional detection fails against LLM-generated attacks
- Trigger-tag paradigm proposed for defense

**File:** `2509.07287v1.pdf`

---

### 13. SoK: Exposing Generation and Detection Gaps in LLM-Generated Phishing (2508.21457v2)

**Why Critical:**
- 18-page systematization of knowledge on LLM phishing
- Communicative elements (text/images) trigger credential disclosure
- Significant gaps between generation capabilities and detection
- Comprehensive overview of LLM credential attack landscape

**Credential Attack Context:**
- User behavior triggered for credential exfiltration
- URLs are part of credential-harvesting campaigns
- Detection gap enables successful credential theft

**File:** `2508.21457v2.pdf`

---

### 14. Exploiting Jailbreaking Vulnerabilities for Phishing Attacks (2507.12185v1)

**Why Critical:**
- DeepSeek and ChatGPT exploited for credential attack generation
- GenAI chatbots bypass ethical safeguards
- Jailbreaking enables automated credential phishing content
- Demonstrates how attackers obtain phishing tools

**Credential Attack Context:**
- LLMs coerced into generating credential-harvesting emails
- Jailbreaking lowers barrier for credential attack campaigns
- Ethical safeguards insufficient to prevent misuse

**File:** `2507.12185v1.pdf`

---

### 15. Robust ML-based Detection of LLM-Generated Phishing (2510.11915v1)

**Why Critical:**
- LLM-generated credential phishing harder to detect
- No grammatical errors, misspellings, formatting issues
- Advanced text preprocessing required for detection
- Validates LLM credential phishing quality threat

**Credential Attack Context:**
- Professional-quality credential phishing from LLMs
- Traditional indicators (poor grammar) absent
- Users can't distinguish LLM phishing from legitimate requests

**File:** `2510.11915v1.pdf`

---

## Attack Scenario Mapping

### Scenario 1: Automated Credential Harvesting Campaign

**Attack Chain:**
1. Jailbreak LLM to generate credential phishing emails (2507.12185v1)
2. Create personalized or generic high-quality phishing (2512.01893v1)
3. Target users with emotional appeals for urgency (2511.21448v1)
4. Harvest credentials via phishing pages
5. Infostealers exfiltrate 29M+ credentials (2507.23611v1)

**Relevant Papers:** 2507.12185v1, 2512.01893v1, 2511.21448v1, 2507.23611v1

---

### Scenario 2: Business Email Compromise for Lateral Movement

**Attack Chain:**
1. Initial phishing compromises employee account (2511.21448v1)
2. Compromised account sends internal phishing (2509.00005v1)
3. Organizations trust internal emails by default
4. Lateral spear phishing harvests additional credentials
5. Escalate to financial/admin systems

**Relevant Papers:** 2511.21448v1, 2509.00005v1

---

### Scenario 3: Voice Phishing for Authentication Bypass

**Attack Chain:**
1. LLM + TTS generates convincing voice phishing (2506.11125v1)
2. Automated vishing calls target victims at scale
3. Social engineering extracts credentials via phone (2507.16291v1)
4. Voice-based authentication systems bypassed
5. Credentials used for account takeover

**Relevant Papers:** 2506.11125v1, 2507.16291v1

---

### Scenario 4: AI Agent Exploitation for Credential Theft

**Attack Chain:**
1. Prompt injection via environment/files (2509.22040v1)
2. Agentic AI editor accesses credential files with system privileges
3. Web-use agents manipulated to fill credentials in phishing (2506.07153v2)
4. LLM agent workflows leak authentication tokens (2506.23260v1)
5. MCP protocol exploited for credential exfiltration (2505.23634v1)

**Relevant Papers:** 2509.22040v1, 2506.07153v2, 2506.23260v1, 2505.23634v1

---

## Key Metrics & Statistics

### Scale of Threat
- **29 million stealer logs in 2024** (2507.23611v1)
- **40% growth in phishing attacks** in single year (2506.03656v1)
- **N=480 study validates AI phishing effectiveness** (2512.01893v1)
- **19,131 real-world phishing sites** analyzed (2511.09606v2)

### Effectiveness Metrics
- **93-95% brand identification accuracy** with commercial LLMs (2511.09606v2)
- **Professional quality** credential phishing - no grammar errors (2510.11915v1)
- **No measurable advantage** from complex personalization (2512.01893v1)
- **Generic content as effective** as personalized attacks (2512.01893v1)

### Attack Characteristics
- **Multi-modal campaigns:** text + URLs + attachments (2509.21129v1)
- **Self-evolving attacks** adapt within days (2507.21538v1)
- **Falsely benign attacks** hide credential theft intent (2505.23634v1)
- **Voice synthesis** enables scalable vishing (2506.11125v1)

---

## Credential-Specific Keywords in Papers

Papers explicitly mentioning credential theft/authentication attacks:

1. **"credential theft"** - 2511.21448v1, 2505.23634v1
2. **"credential compromise"** - multiple papers
3. **"password attack"** - query matched papers
4. **"authentication bypass"** - 2507.16291v1, 2506.11125v1
5. **"session cookie theft"** - 2507.23611v1
6. **"business email compromise"** - 2509.00005v1
7. **"infostealer"** - 2507.23611v1
8. **"lateral spear phishing"** - 2509.00005v1

---

## Research Gaps for Credential Attacks

### Areas Needing More Research:

1. **Multi-Factor Authentication Bypass**
   - Limited coverage of MFA-specific attacks
   - Need research on AI-powered MFA social engineering

2. **Password Reset Social Engineering**
   - Weak coverage of password reset flow attacks
   - AI-generated pretexts for account recovery

3. **Credential Stuffing with AI**
   - No papers on ML-optimized credential stuffing
   - AI pattern recognition for successful credential reuse

4. **Deepfake Video for Account Recovery**
   - Only voice cloning papers found
   - Video deepfakes for identity verification bypass

5. **Passwordless Authentication Attacks**
   - Limited research on biometric spoofing with AI
   - Behavioral biometrics under AI mimicry

---

## Recommended Reading Order

### For Security Practitioners:

1. **Start Here:** 2507.23611v1 (29M stealer logs - scale of problem)
2. **Understand Attacks:** 2511.21448v1 (LLM-generated credential phishing)
3. **Internal Threats:** 2509.00005v1 (business email compromise)
4. **AI Agent Risks:** 2505.23634v1 (MCP credential theft)
5. **Voice Threats:** 2506.11125v1 (automated vishing)

### For Researchers:

1. **Systematization:** 2508.21457v2 (18-page SoK on LLM phishing)
2. **Comprehensive Study:** 2506.23260v1 (29-page agent workflow attacks)
3. **Empirical Validation:** 2512.01893v1 (N=480 controlled study)
4. **Detection Challenges:** 2510.11915v1 (LLM phishing detection)
5. **Emerging Vectors:** 2506.07153v2 (web-use agent security)

### For Red Teams:

1. **Jailbreaking:** 2507.12185v1 (bypass LLM safeguards)
2. **Prompt Injection:** 2509.22040v1 (agentic AI coding editors)
3. **Protocol Exploits:** 2506.23260v1 (LLM agent workflows)
4. **Automated Campaigns:** 2507.21538v1 (self-evolving phishing)
5. **Voice Attacks:** 2507.16291v1 (adversarial vishing)

---

## Defense Priority Matrix

### Immediate Threat (Deploy Now):

1. **LLM-Generated Phishing Detection** (2510.11915v1, 2511.04728v1)
   - Advanced text preprocessing for LLM content
   - Trustworthiness calibration frameworks
   - Commercial LLMs for detection (93-95% accuracy)

2. **Infostealer Detection** (2507.23611v1)
   - Automated screenshot analysis with LLMs
   - 29M logs require automated response
   - Scale makes manual analysis unfeasible

3. **Internal Email Validation** (2509.00005v1)
   - Per-sender authorship validation
   - Don't trust internal emails by default
   - Detect business email compromise early

### Medium-Term (6-12 Months):

1. **Voice Phishing Defenses** (2506.11125v1, 2507.16291v1)
   - ASR jamming for automated scam prevention
   - Adversarial-robust vishing detection
   - Voice authentication replacement

2. **AI Agent Security** (2509.22040v1, 2506.07153v2, 2506.23260v1)
   - Prompt injection detection for agentic systems
   - Sandbox agent capabilities
   - Protocol-level security for LLM workflows

3. **MCP Security** (2505.23634v1)
   - Preference alignment for refusing falsely benign attacks
   - MCP exploit detection
   - Credential access monitoring

### Long-Term Research (12+ Months):

1. **Self-Evolving Defense Systems** (2507.21538v1, 2509.21129v1)
   - Adaptive defenses for adaptive attacks
   - Genetic algorithm-based detection evolution
   - Predictive threat modeling

2. **Multi-Modal Defense** (2508.21457v2)
   - Text + image + URL combined analysis
   - Holistic phishing detection
   - Cross-modal inconsistency detection

3. **Zero-Trust for AI Systems**
   - Assume all AI agents potentially compromised
   - Continuous validation for LLM outputs
   - Credential-less authentication priority

---

## Conclusion

**Top 15 papers provide comprehensive coverage of AI-powered credential attack landscape:**

- **Direct credential theft mechanisms** in 5 Tier 1 papers
- **Authentication bypass techniques** in 5 Tier 2 papers
- **Attack effectiveness validation** in 5 Tier 3 papers

**Critical Findings:**
1. 29M stealer logs demonstrate massive credential compromise scale
2. LLM-generated phishing eliminates traditional detection indicators
3. Business email compromise exploits internal trust
4. AI agents create new credential theft attack surface
5. Voice cloning enables scalable authentication bypass

**Immediate Action Required:**
- Deploy LLM-based phishing detection (93-95% accuracy available)
- Implement internal email authorship validation
- Address infostealer threat at scale (29M logs)
- Secure AI agent systems against prompt injection
- Prepare voice authentication replacement strategies

**Research extends Issue #15 understanding with 45 papers validating critical threat severity for AI-powered credential attacks.**
