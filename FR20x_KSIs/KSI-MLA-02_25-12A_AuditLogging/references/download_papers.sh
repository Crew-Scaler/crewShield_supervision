#!/bin/bash
# Manual Download Helper Script for ArXiv Papers - Issue #74
# Note: ArXiv requires reCAPTCHA verification, so automated downloads may fail
# This script provides download commands you can run manually or use with a browser

OUTPUT_DIR="/Users/tamnguyen/Documents/GitHub/ksi_watch/KSI-MLA-02_25-12A_AuditLogging/references"

echo "======================================================================"
echo "ArXiv Paper Download Helper - Issue #74: Ops Audit Logs"
echo "======================================================================"
echo ""
echo "NOTE: ArXiv may require reCAPTCHA verification for PDF downloads."
echo "If automated downloads fail, please visit each URL in your browser."
echo ""
echo "Output directory: $OUTPUT_DIR"
echo ""

# Array of papers with metadata
declare -a papers=(
    "2509.03821|rethinking_tamper_evident_logging|Nitro: High-Performance Tamper-Evident Logging"
    "2505.17236|logstamping_blockchain_log_auditing|LogStamping: Blockchain-Based Log Auditing"
    "2504.07938|quantum_resistant_blockchain_audit|Quantum-Resistant File Transfer with Blockchain"
    "2412.12814|tamper_resistance_forensic_artifacts|Tamper Resistance of Digital Forensic Artifacts"
    "2512.09938|blockchain_audit_trail_settlement|Blockchain-Anchored Audit Trail Model"
    "2512.11065|immutable_explainability_ai|Immutable Explainability: Fuzzy Logic and Blockchain"
    "2504.10702|container_energy_observability_kubernetes|Container-Level Energy Observability in Kubernetes"
    "2509.04191|kubeguard_llm_kubernetes_hardening|KubeGuard: LLM-Assisted Kubernetes Hardening"
    "2509.02449|kubeintellect_llm_kubernetes_management|KubeIntellect: Modular LLM-Orchestrated Agent Framework"
    "2507.16109|kubernetes_resilience_chaos_engineering|Resilience Evaluation of Kubernetes via Chaos Engineering"
    "2401.09960|cloud_native_pattern_detection|Cloud-Native Pattern Detection Framework"
    "2505.06701|rulegenie_siem_optimization|RuleGenie: SIEM Detection Rule Set Optimization"
    "2508.17851|logging_continuous_auditing_ml|Logging Requirement for Continuous Auditing of ML"
    "2511.21901|ai_security_threat_taxonomy|Standardized Threat Taxonomy for AI Security"
    "2503.02065|explainable_ai_threat_intelligence|The Role of Explainable AI in Threat Intelligence"
)

successful=0
failed=0

# Function to download a paper
download_paper() {
    local arxiv_id="$1"
    local filename="$2"
    local description="$3"

    echo "----------------------------------------------------------------------"
    echo "[$((successful + failed + 1))/15] Downloading: $description"
    echo "ArXiv ID: $arxiv_id"
    echo "Filename: ${filename}.pdf"
    echo ""

    # Try download with curl
    curl -L -s -H "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 KHTML like Gecko Chrome/120.0.0.0 Safari/537.36" \
         -H "Accept: application/pdf,*/*" \
         -H "Accept-Language: en-US,en;q=0.9" \
         "https://arxiv.org/pdf/${arxiv_id}.pdf" \
         -o "${OUTPUT_DIR}/${arxiv_id}_${filename}.pdf"

    # Check file size
    if [ -f "${OUTPUT_DIR}/${arxiv_id}_${filename}.pdf" ]; then
        size=$(wc -c < "${OUTPUT_DIR}/${arxiv_id}_${filename}.pdf")
        if [ "$size" -gt 50000 ]; then
            echo "✅ SUCCESS - Downloaded $(numfmt --to=iec-i --suffix=B $size)"
            ((successful++))
        else
            echo "❌ FAILED - File too small ($size bytes, likely reCAPTCHA page)"
            echo "   Manual download required: https://arxiv.org/abs/${arxiv_id}"
            rm "${OUTPUT_DIR}/${arxiv_id}_${filename}.pdf"
            ((failed++))
        fi
    else
        echo "❌ FAILED - Download error"
        ((failed++))
    fi

    # Rate limiting - be nice to ArXiv servers
    sleep 4
}

# Download all papers
for paper in "${papers[@]}"; do
    IFS='|' read -r arxiv_id filename description <<< "$paper"
    download_paper "$arxiv_id" "$filename" "$description"
done

echo ""
echo "======================================================================"
echo "Download Summary"
echo "======================================================================"
echo "✅ Successful: $successful papers"
echo "❌ Failed: $failed papers"
echo ""

if [ "$failed" -gt 0 ]; then
    echo "MANUAL DOWNLOAD REQUIRED FOR FAILED PAPERS"
    echo "======================================================================"
    echo ""
    echo "If automated downloads failed (due to reCAPTCHA), please:"
    echo "1. Visit each paper's URL in your browser"
    echo "2. Complete any reCAPTCHA verification"
    echo "3. Download the PDF manually"
    echo "4. Save to: $OUTPUT_DIR"
    echo "5. Use naming: {arxiv_id}_{filename}.pdf"
    echo ""
    echo "Failed paper URLs:"
    for paper in "${papers[@]}"; do
        IFS='|' read -r arxiv_id filename description <<< "$paper"
        if [ ! -f "${OUTPUT_DIR}/${arxiv_id}_${filename}.pdf" ]; then
            echo "  - https://arxiv.org/abs/${arxiv_id} -> ${arxiv_id}_${filename}.pdf"
        fi
    done
    echo ""
    echo "Alternative: Use a browser extension like 'DownThemAll' or 'Bulk Download'"
    echo "to download all PDFs from the list above."
fi

echo ""
echo "For detailed paper information, see:"
echo "  - ARXIV_RESEARCH_REPORT_ISSUE74.md (detailed report)"
echo "  - PAPER_SUMMARY_ISSUE74.csv (tabular summary)"
echo ""
