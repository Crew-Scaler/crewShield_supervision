#!/usr/bin/env python3
"""
Paper Analysis Script: Extract validation data for AI agent security claims

Key Validation Targets:
1. 45:1 machine-to-human identity ratio claim
2. Agent lateral movement detection latency (15 min vs 6 months)
3. Multi-agent authorization complexity (5-10x increase)
4. Prompt injection attack success rates (>80%)
"""

import json
import re
from pathlib import Path
from typing import Dict, List, Tuple
import PyPDF2

BASE_DIR = Path("/Users/tamnguyen/Documents/GitHub/ksi_watch/KSI-CNA-07_25-12A_BestPractices/references/ai_agent_security")

# Keywords for each validation target
VALIDATION_KEYWORDS = {
    "identity_ratio": [
        r"machine.*human.*ratio",
        r"service account.*(\d+).*human",
        r"(\d+):1.*identity",
        r"credential.*explosion",
        r"(\d+)x.*service accounts",
        r"workload.*identity.*scale"
    ],
    "lateral_movement": [
        r"lateral movement.*(\d+).*minutes?",
        r"lateral movement.*(\d+).*hours?",
        r"lateral movement.*(\d+).*days?",
        r"detection.*latency.*(\d+)",
        r"dwell time.*(\d+)",
        r"mean.*time.*detect.*(\d+)"
    ],
    "authorization_complexity": [
        r"authorization.*complexity.*(\d+)x",
        r"(\d+)x.*increase.*authorization",
        r"multi-agent.*(\d+).*policies",
        r"RBAC.*scale.*(\d+)",
        r"permission.*management.*(\d+)%"
    ],
    "prompt_injection": [
        r"prompt injection.*(\d+)%.*success",
        r"attack.*success.*rate.*(\d+)%",
        r"(\d+)%.*vulnerable.*prompt",
        r"injection.*bypass.*(\d+)%"
    ]
}


class PaperAnalyzer:
    def __init__(self):
        self.papers_metadata = self.load_metadata()
        self.validation_findings = {
            "identity_ratio": [],
            "lateral_movement": [],
            "authorization_complexity": [],
            "prompt_injection": []
        }

    def load_metadata(self) -> List[Dict]:
        """Load papers metadata JSON."""
        json_path = BASE_DIR / "papers_metadata.json"
        if json_path.exists():
            with open(json_path, 'r') as f:
                return json.load(f)
        return []

    def extract_text_from_pdf(self, pdf_path: Path, max_pages: int = 20) -> str:
        """Extract text from PDF (first N pages for efficiency)."""
        try:
            text = []
            with open(pdf_path, 'rb') as f:
                reader = PyPDF2.PdfReader(f)
                num_pages = min(len(reader.pages), max_pages)

                for i in range(num_pages):
                    page = reader.pages[i]
                    text.append(page.extract_text())

            return ' '.join(text)
        except Exception as e:
            print(f"Error extracting text from {pdf_path}: {e}")
            return ""

    def search_validation_data(self, text: str, paper_title: str) -> Dict:
        """Search for validation data in paper text."""
        findings = {}

        for category, patterns in VALIDATION_KEYWORDS.items():
            matches = []
            for pattern in patterns:
                found = re.finditer(pattern, text, re.IGNORECASE)
                for match in found:
                    context_start = max(0, match.start() - 100)
                    context_end = min(len(text), match.end() + 100)
                    context = text[context_start:context_end]

                    matches.append({
                        "pattern": pattern,
                        "match": match.group(0),
                        "context": context.replace('\n', ' '),
                        "paper": paper_title
                    })

            if matches:
                findings[category] = matches

        return findings

    def analyze_all_papers(self):
        """Analyze all downloaded papers for validation data."""
        print("\n" + "="*80)
        print("Analyzing Papers for Validation Data")
        print("="*80 + "\n")

        if not self.papers_metadata:
            print("No metadata found. Scanning directory for PDFs...")
            pdf_files = list(BASE_DIR.rglob("*.pdf"))
            print(f"Found {len(pdf_files)} PDF files\n")

            for pdf_path in pdf_files:
                self.analyze_single_paper_direct(pdf_path)
        else:
            for paper in self.papers_metadata:
                pdf_path = Path(paper['file_path'])
                if pdf_path.exists():
                    self.analyze_single_paper(paper)

        self.generate_validation_report()

    def analyze_single_paper_direct(self, pdf_path: Path):
        """Analyze single paper directly from PDF path."""
        print(f"Analyzing: {pdf_path.name[:60]}...")

        text = self.extract_text_from_pdf(pdf_path)
        if not text:
            print("  Could not extract text\n")
            return

        findings = self.search_validation_data(text, pdf_path.name)

        for category, matches in findings.items():
            self.validation_findings[category].extend(matches)
            print(f"  Found {len(matches)} {category} data points")

        if not findings:
            print("  No validation data found")
        print()

    def analyze_single_paper(self, paper: Dict):
        """Analyze single paper from metadata."""
        print(f"Analyzing: {paper['title'][:60]}...")

        pdf_path = Path(paper['file_path'])
        text = self.extract_text_from_pdf(pdf_path)

        if not text:
            print("  Could not extract text\n")
            return

        findings = self.search_validation_data(text, paper['title'])

        for category, matches in findings.items():
            self.validation_findings[category].extend(matches)
            print(f"  Found {len(matches)} {category} data points")

        if not findings:
            print("  No validation data found")
        print()

    def generate_validation_report(self):
        """Generate comprehensive validation report."""
        report_path = BASE_DIR / "VALIDATION_FINDINGS.md"

        report = []
        report.append("# Validation Findings: AI Agent Security Claims\n\n")
        report.append(f"**Analysis Date:** {Path().resolve()}\n\n")

        # Summary section
        report.append("## Executive Summary\n\n")
        total_findings = sum(len(v) for v in self.validation_findings.values())
        report.append(f"**Total Validation Data Points Found:** {total_findings}\n\n")

        for category, findings in self.validation_findings.items():
            report.append(f"- **{category.replace('_', ' ').title()}:** {len(findings)} findings\n")
        report.append("\n")

        # Detailed findings by category
        report.append("## Detailed Findings\n\n")

        # 1. Identity Ratio
        report.append("### 1. Machine-to-Human Identity Ratio (Target: 45:1)\n\n")
        if self.validation_findings['identity_ratio']:
            report.append(f"**Status:** {len(self.validation_findings['identity_ratio'])} relevant data points found\n\n")
            for i, finding in enumerate(self.validation_findings['identity_ratio'][:10], 1):
                report.append(f"**Finding {i}:**\n")
                report.append(f"- Paper: {finding['paper'][:70]}\n")
                report.append(f"- Match: `{finding['match']}`\n")
                report.append(f"- Context: ...{finding['context']}...\n\n")
        else:
            report.append("**Status:** No direct validation data found in analyzed papers\n")
            report.append("**Recommendation:** May need industry reports or cloud provider data\n\n")

        # 2. Lateral Movement Detection
        report.append("### 2. Lateral Movement Detection Latency (Target: 15 min vs 6 months)\n\n")
        if self.validation_findings['lateral_movement']:
            report.append(f"**Status:** {len(self.validation_findings['lateral_movement'])} relevant data points found\n\n")
            for i, finding in enumerate(self.validation_findings['lateral_movement'][:10], 1):
                report.append(f"**Finding {i}:**\n")
                report.append(f"- Paper: {finding['paper'][:70]}\n")
                report.append(f"- Match: `{finding['match']}`\n")
                report.append(f"- Context: ...{finding['context']}...\n\n")
        else:
            report.append("**Status:** No direct validation data found in analyzed papers\n")
            report.append("**Recommendation:** Check cybersecurity incident reports (Verizon DBIR, etc.)\n\n")

        # 3. Authorization Complexity
        report.append("### 3. Multi-Agent Authorization Complexity (Target: 5-10x increase)\n\n")
        if self.validation_findings['authorization_complexity']:
            report.append(f"**Status:** {len(self.validation_findings['authorization_complexity'])} relevant data points found\n\n")
            for i, finding in enumerate(self.validation_findings['authorization_complexity'][:10], 1):
                report.append(f"**Finding {i}:**\n")
                report.append(f"- Paper: {finding['paper'][:70]}\n")
                report.append(f"- Match: `{finding['match']}`\n")
                report.append(f"- Context: ...{finding['context']}...\n\n")
        else:
            report.append("**Status:** No direct validation data found in analyzed papers\n")
            report.append("**Recommendation:** May need case studies from cloud-native organizations\n\n")

        # 4. Prompt Injection
        report.append("### 4. Prompt Injection Attack Success Rates (Target: >80%)\n\n")
        if self.validation_findings['prompt_injection']:
            report.append(f"**Status:** {len(self.validation_findings['prompt_injection'])} relevant data points found\n\n")
            for i, finding in enumerate(self.validation_findings['prompt_injection'][:10], 1):
                report.append(f"**Finding {i}:**\n")
                report.append(f"- Paper: {finding['paper'][:70]}\n")
                report.append(f"- Match: `{finding['match']}`\n")
                report.append(f"- Context: ...{finding['context']}...\n\n")
        else:
            report.append("**Status:** No direct validation data found in analyzed papers\n")
            report.append("**Recommendation:** Check OWASP LLM Top 10 and red team reports\n\n")

        # Conclusions and next steps
        report.append("## Conclusions\n\n")
        report.append("### Validation Status Summary\n\n")

        validated = sum(1 for v in self.validation_findings.values() if len(v) > 0)
        report.append(f"- Claims with supporting evidence: {validated}/4\n")
        report.append(f"- Claims requiring additional sources: {4 - validated}/4\n\n")

        report.append("### Recommended Next Steps\n\n")
        report.append("1. **Identity Ratio Claims:** Search cloud provider whitepapers (AWS, GCP, Azure)\n")
        report.append("2. **Lateral Movement Data:** Review Mandiant, CrowdStrike threat reports\n")
        report.append("3. **Authorization Complexity:** Analyze Kubernetes RBAC case studies\n")
        report.append("4. **Prompt Injection Rates:** Check OWASP AI Security Project data\n")
        report.append("5. **Production Frameworks:** Extract framework recommendations from papers\n\n")

        with open(report_path, 'w') as f:
            f.write(''.join(report))

        print(f"\nValidation report generated: {report_path}")

        # Also save JSON
        json_path = BASE_DIR / "validation_findings.json"
        with open(json_path, 'w') as f:
            json.dump(self.validation_findings, f, indent=2)
        print(f"Findings JSON saved: {json_path}")


if __name__ == "__main__":
    analyzer = PaperAnalyzer()
    analyzer.analyze_all_papers()
