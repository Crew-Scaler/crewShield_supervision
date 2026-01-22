# CED-01: Training Questions

Training questions for general workforce on AI-specific security and awareness.

## Governance And Leadership

********************************************************************************

**CED-01-Q01** – Do you have documented evidence that training covers AI governance, model risk management, and AI-specific threat vectors as required by these frameworks?

**CED-01-Q02** – What percentage of your workforce receives training on compliance frameworks related to AI (vs. traditional security compliance training)?

**CED-01-Q03** – What percentage of your workforce receives ANY AI-specific security training today? What is the distribution by role?

**CED-01-Q04** – Do executives understand the difference between AI model risk assessment and traditional software risk assessment? Can they identify decision gates that should block AI project progression?

**CED-01-Q05** – Have you documented the role of management in creating security culture that makes employees confident refusing shadow AI (vs. perceiving low detection risk)?

**CED-01-Q06** – What percentage of AI project charters include security sign-off from CISO or security leadership before execution?


## Strategy, Scope, And Budgeting

********************************************************************************

**CED-01-Q07** – What is your documented annual training budget allocation for AI-specific security awareness and education across all workforce roles? How is this budget justified and tracked? What percentage of your security training budget is dedicated to AI-specific content vs. traditional secure coding and compliance training?

**CED-01-Q08** – What percentage of your workforce currently has access to or actively uses public AI tools (ChatGPT, Claude, Copilot, etc.)? How has AI tool adoption evolved over the past 12-24 months? What percentage of your development staff actively use AI-generated code in their daily work, and what proportion of deployed code originates from or is augmented by AI tools?

**CED-01-Q09** – If a material data loss incident occurred via shadow AI, what would be the regulatory notification timeline and estimated financial impact?

**CED-01-Q10** – Which regulatory frameworks apply to your organization (DORA, NIS2, NIST AI RMF, ISO 42001, EU AI Act, etc.)? What training requirements does each impose?

**CED-01-Q11** – What audit/compliance gaps exist today? Are regulators or auditors expecting AI-specific training content that you don't yet provide?


## Curriculum Content And Tailoring

********************************************************************************

**CED-01-Q12** – Do your current security training or acceptable-use policies address prompt injection risks or unusual AI behavior? What is the detection capability if a prompt injection occurs?

**CED-01-Q13** – What training do your teams receive about differentiating legitimate AI output anomalies from injected/poisoned output?

**CED-01-Q14** – How many AI models (foundation models, fine-tuned variants, custom models) are deployed in production today? For each, do you have documented source, training data provenance, and risk assessment?

**CED-01-Q15** – Have your training data curators or model evaluators received any security awareness training about supply chain poisoning, model theft, or malicious model versions?

**CED-01-Q16** – What is your current phishing click rate? How has it trended over the past 12-24 months? Are click rates increasing despite security awareness training?

**CED-01-Q17** – Do your developers and ML engineers have training on identifying suspicious model behavior post-deployment (outputs that don't match expected patterns)?

**CED-01-Q18** – What is your team's baseline understanding that attack evolution outpaces defense innovation? Is this reflected in your security culture and training messaging?

**CED-01-Q19** – Do your security teams receive training on emerging evasion techniques (code obfuscation bypassing LLM vulnerability detectors, adversarial examples against detection systems)?

**CED-01-Q20** – How frequently do you update security training content based on newly discovered attack techniques? Is there a formal process to integrate emerging threats?

**CED-01-Q21** – Do you deploy vector databases (Pinecone, Weaviate, Milvus) or RAG systems? Have you assessed poisoning risks in your vector stores or training data pipeline?

**CED-01-Q22** – Do your employees understand the permanence of data exposure via public AI training data incorporation? Are they aware this is an irreversible loss?

**CED-01-Q23** – Do product managers understand how feature decisions (e.g., "add AI content summary") introduce new attack surfaces? Are they trained to identify security implications?

**CED-01-Q24** – Can your SOC detect prompt injection attacks, model inference anomalies, or training data poisoning attempts? What is the detection latency?

**CED-01-Q25** – How long does it take from publication of new research (ArXiv, academic conferences) to your organization implementing training on that threat?

**CED-01-Q26** – What is your cadence for updating AI threat curriculum? Is it annual, quarterly, or event-driven?

**CED-01-Q27** – What metrics do you currently use to measure training effectiveness (click rates, reporting rates, assessment scores)? Do these metrics capture AI-specific threat resistance?

**CED-01-Q28** – Have you tried measuring behavioral change (e.g., decreased shadow AI adoption, increased incident reporting) following AI-specific training?

**CED-01-Q29** – What is your baseline for AI threat incidents today? How would you measure improvement post-training?

**CED-01-Q30** – How many autonomous AI agents (orchestration, code generation, infrastructure automation) operate in production today? Who authorizes what permissions they receive?

**CED-01-Q31** – Are agent permissions granted as discrete, time-limited actions, or as broad standing access (e.g., "can read all AWS S3 buckets")? What is the blast radius if a single agent is compromised?

**CED-01-Q32** – For multi-agent systems, do you enforce Byzantine-fault-tolerant authorization where agents cannot implicitly trust peer agents? Or do agents have transitive privilege (agent A can delegate agent B's permissions)?

**CED-01-Q33** – Have you conducted an authorization review of all deployed agents in the past 12 months? What percentage of agents would you classify as "over-privileged"?

**CED-01-Q34** – How many of your employees regularly upload documents (PDFs, images, CSVs) to AI tools or use AI tools to process incoming documents? What sensitivity levels of data are involved?

**CED-01-Q35** – Do you have visibility into the supply chain for third-party models (foundation models from OpenAI, Anthropic, Meta, etc.)? Do you assess supplier security practices?

**CED-01-Q36** – Have you tested AI-generated phishing in your simulated campaigns? What is the click differential between AI-generated vs. human-crafted phishing?

**CED-01-Q37** – In your voice communication channels (phone, video calls), have you educated employees about deepfake voice risks? What is their confidence level in voice-based authentication?

**CED-01-Q38** – For high-sensitivity communications (wire transfers, credential changes, system access grants), do you have out-of-band verification procedures that employees understand and follow?

**CED-01-Q39** – What is the escalation procedure if a developer notices unusual model behavior? How quickly can they trigger a security investigation?

**CED-01-Q40** – For safety-critical AI systems (those affecting customer data or security decisions), do you have monitoring for model drift or gradual behavioral changes?

**CED-01-Q41** – In serverless environments, have you assessed multi-tenant isolation risks specific to AI workloads (co-location attacks on shared GPU/infrastructure)?

**CED-01-Q42** – Do finance and procurement teams understand the security implications of model sourcing decisions? Are they trained to assess supplier risk?

**CED-01-Q43** – When AI projects are proposed, do managers ask about threat modeling, supply chain assessment, and model poisoning risks? Or are these skipped in favor of speed/cost?

**CED-01-Q44** – For a suspected model compromise incident, do you have forensic procedures to verify integrity? Can you restore to a known-good baseline?

**CED-01-Q45** – In a multi-agent system compromise, can your IR team trace the cascade of compromises and understand the blast radius?

**CED-01-Q46** – Have your incident responders been trained on AI-specific incident patterns, evidence collection, and containment strategies?

**CED-01-Q47** – Do you have a mechanism to rapidly disseminate information about newly discovered AI attack vectors to affected teams?

**CED-01-Q48** – Do your security teams participate in threat intelligence communities focused on AI security (e.g., NIST AI RMF community, vendor threat feeds)?


## Policies, Procedures, And Shadow Ai

********************************************************************************

**CED-01-Q49** – Have you detected instances where employees used shadow AI tools to process proprietary data, customer information, or code? What was the incident severity and remediation effort?

**CED-01-Q50** – What percentage of insider threat incidents involve AI tools (shadow AI, unauthorized model access, or credential exposure via AI scanning)?

**CED-01-Q51** – Have you conducted behavioral analysis to identify the decision points where employees choose to use shadow AI (time pressure, perceived productivity, low detection risk)? What drives this choice?

**CED-01-Q52** – Do your DLP controls adequately monitor AI tool usage, or do employees have unmonitored channels to exfiltrate data?

**CED-01-Q53** – For AI-specific threats (prompt injection, shadow AI usage, model anomaly detection), what would success look like? How would you measure it?


## Technical Roles: Developers And Administrators

********************************************************************************

**CED-01-Q54** – Have you established baseline behavior profiles for deployed models (expected output distributions, confidence levels, error rates)? Do developers understand these baselines?

**CED-01-Q55** – How many of your developers build or consume APIs that integrate with AI systems? Do they understand BOLA risks specific to AI endpoints (e.g., accessing other users' model inference results)?

**CED-01-Q56** – Map your organization by role (data scientists, engineers, architects, product managers, compliance, finance, legal). For each, identify AI security decisions they make.


## Exercises, Measurements, And Assurance

********************************************************************************

**CED-01-Q57** – What DLP/MDM controls currently monitor AI tool usage and data loss vectors? What is the detection latency (how quickly do we identify violations)?

**CED-01-Q58** – Have you experienced any prompt injection incidents (malicious instructions in documents affecting AI system behavior)? If not, have you tested your detection capability?

**CED-01-Q59** – What is your incident response capability if a deployed model is discovered to have been poisoned or contains a backdoor?

**CED-01-Q60** – Have you tested your security detection systems (SIEM, WAF, IDS, anomaly detection) against adversarial evasion attacks? What evasion success rates did you discover?



================================================================================
### Footer

**Schema References:**
- `guide_InvestigativeQuestions.md` - Guidelines for investigative question structure
- `schema_question_library.json` - Schema for global question library
- `schema_questions.json` - Schema for binding questions
