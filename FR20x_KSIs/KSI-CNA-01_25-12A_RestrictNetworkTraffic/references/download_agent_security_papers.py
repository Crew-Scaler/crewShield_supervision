#!/usr/bin/env python3
"""
Download ArXiv papers on AI Agent Security & Authorization
Target: 15-40 papers from 2024-2025
"""

import os
import time
import urllib.request
from pathlib import Path

# Target directory
OUTPUT_DIR = Path("/Users/tamnguyen/Documents/GitHub/ksi_watch/KSI-CNA-01_25-12A_RestrictNetworkTraffic/references/agent_security")

# ArXiv paper IDs extracted from search results
PAPERS = [
    # Core Security Papers
    ("2406.08689", "Security_of_AI_Agents.pdf"),
    ("2510.23883", "Agentic_AI_Security_Threats_Defenses_Evaluation.pdf"),
    ("2507.20526", "Security_Challenges_AI_Agent_Deployment.pdf"),
    ("2505.02077", "Open_Challenges_Multi_Agent_Security.pdf"),
    ("2506.04133", "TRiSM_Agentic_AI_Trust_Risk_Security.pdf"),
    ("2505.13076", "Hidden_Dangers_Browsing_AI_Agents.pdf"),
    ("2506.08837", "Design_Patterns_Securing_LLM_Agents_Prompt_Injection.pdf"),
    ("2510.06445", "Survey_Agentic_Security_Applications_Threats_Defenses.pdf"),
    ("2406.02630", "AI_Agents_Under_Threat_Survey.pdf"),

    # Isolation & Sandboxing
    ("2509.07764", "AgentSentinel_Real_Time_Security_Defense_Framework.pdf"),
    ("2503.17332", "CVE_Bench_AI_Agents_Exploit_Vulnerabilities.pdf"),
    ("2505.23847", "Seven_Security_Challenges_Cross_Domain_Multi_Agent.pdf"),
    ("2510.05244", "Indirect_Prompt_Injections_Firewalls.pdf"),

    # Autonomous Agent Security & Monitoring
    ("2505.12786", "LLM_Agents_Autonomous_Cyberattacks_Survey.pdf"),
    ("2511.16709", "AutoBackdoor_Automating_Backdoor_Attacks_LLM_Agents.pdf"),
    ("2503.02780", "Quantitative_Resilience_Modeling_Autonomous_Cyber_Defense.pdf"),
    ("2508.20307", "Operational_Cybersecurity_Supply_Chain_Threat_AI_Systems.pdf"),
    ("2508.10043", "Securing_Agentic_AI_Threat_Modeling_Network_Monitoring.pdf"),
    ("2510.09462", "Adaptive_Attacks_Trusted_Monitors_AI_Control.pdf"),
    ("2502.02649", "Fully_Autonomous_AI_Agents_Should_Not_Be_Developed.pdf"),

    # Anomaly Detection & Behavior Monitoring
    ("2503.13195", "Deep_Learning_Anomaly_Detection_Survey.pdf"),
    ("2507.15676", "Agentic_AI_Autonomous_Anomaly_Management.pdf"),
    ("2505.24201", "SentinelAgent_Graph_Based_Anomaly_Detection.pdf"),
    ("2505.08807", "Security_Internet_of_Agents_Attacks_Countermeasures.pdf"),
    ("2502.13256", "Survey_Anomaly_Detection_Cyber_Physical_Systems.pdf"),
    ("2505.12594", "Multi_Agent_Framework_Anomaly_Detection.pdf"),

    # Access Control & Permissions
    ("2509.22256", "Secure_Efficient_Access_Control_Computer_Use_Agents.pdf"),
    ("2510.26212", "AgentSentry_Task_Centric_Access_Control.pdf"),
    ("2510.11108", "Vision_Access_Control_LLM_Agent_Systems.pdf"),
    ("2501.17070", "Contextual_Agent_Security_Policy_Every_Purpose.pdf"),
    ("2504.21030", "Model_Context_Protocol_Multi_Agent_Systems.pdf"),
    ("2508.03858", "MI9_Runtime_Governance_Framework_Agentic_AI.pdf"),
    ("2501.09674", "Authenticated_Delegation_Authorized_AI_Agents.pdf"),

    # Additional Security Research
    ("2507.06323", "Bridging_AI_Software_Security_Vulnerability.pdf"),
]

def download_paper(arxiv_id: str, filename: str) -> bool:
    """Download a paper from ArXiv"""
    url = f"https://arxiv.org/pdf/{arxiv_id}.pdf"
    output_path = OUTPUT_DIR / filename

    if output_path.exists():
        print(f"✓ Already exists: {filename}")
        return True

    try:
        print(f"Downloading {arxiv_id}: {filename}...")
        urllib.request.urlretrieve(url, output_path)
        print(f"✓ Downloaded: {filename}")
        time.sleep(2)  # Polite delay between requests
        return True
    except Exception as e:
        print(f"✗ Failed {arxiv_id}: {e}")
        return False

def main():
    """Download all papers"""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    print(f"Downloading {len(PAPERS)} AI Agent Security papers to {OUTPUT_DIR}\n")

    successful = 0
    failed = 0

    for arxiv_id, filename in PAPERS:
        if download_paper(arxiv_id, filename):
            successful += 1
        else:
            failed += 1

    print(f"\n{'='*60}")
    print(f"Download Complete!")
    print(f"Successful: {successful}/{len(PAPERS)}")
    print(f"Failed: {failed}/{len(PAPERS)}")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()
