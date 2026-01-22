#!/bin/bash
#
# Quick Download Script for Cluster 1 Papers
# Agentic AI Systems & Vulnerability Management
#
# Usage:
#   chmod +x QUICK_DOWNLOAD.sh
#   ./QUICK_DOWNLOAD.sh
#
# This script downloads all 16 papers from ArXiv
# Respects ArXiv rate limits (3.5 second delay between requests)
#

TARGET_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$TARGET_DIR" || exit 1

echo "=========================================="
echo "Cluster 1 Paper Downloader"
echo "=========================================="
echo "Target directory: $TARGET_DIR"
echo ""

# Array of arxiv IDs
arxiv_ids=(
    "2601.00205"
    "2512.23480"
    "2510.23883"
    "2510.06445"
    "2506.04133"
    "2508.10043"
    "2511.21990"
    "2410.21218"
    "2503.12188"
    "2508.16481"
    "2504.19956"
    "2510.00317"
    "2505.12786"
    "2512.18043"
    "2502.07049"
    "2411.10184"
)

# Paper titles for naming
titles=(
    "AI_Agents_Dependency_Updates"
    "Agentic_AI_Autonomous_Defense"
    "Agentic_AI_Security_Threats"
    "Survey_Agentic_Security"
    "TRiSM_Agentic_AI"
    "Securing_Agentic_AI_Threat_Modeling"
    "Safety_Security_Framework_Agentic"
    "LLM_Supply_Chain_Risks"
    "Multi_Agent_Malicious_Code"
    "Benchmarking_Robustness_Agentic"
    "Securing_AI_Threat_Model"
    "MAVUL_Vulnerability_Detection"
    "LLM_Agents_Cyberattacks"
    "Securing_Agentic_Systems_Framework"
    "LLMs_Software_Security"
    "Agentic_LLMs_Supply_Chain"
)

successful=0
failed=0

echo "Starting downloads..."
echo "Note: Please be patient. ArXiv requests are rate-limited."
echo ""

# Download each paper
for i in "${!arxiv_ids[@]}"; do
    id="${arxiv_ids[$i]}"
    title="${titles[$i]}"
    filename="${id}_${title}.pdf"
    url="https://arxiv.org/pdf/${id}"

    echo -n "[$((i+1))/16] Downloading $id..."

    # Use curl with retry
    if curl -s -L -m 30 "$url" -o "$filename" 2>/dev/null; then
        size=$(ls -lh "$filename" 2>/dev/null | awk '{print $5}')
        echo " OK ($size)"
        ((successful++))
    else
        echo " FAILED"
        rm -f "$filename"
        ((failed++))
    fi

    # Rate limiting (respect ArXiv guidelines)
    sleep 3.5
done

echo ""
echo "=========================================="
echo "Download Summary"
echo "=========================================="
echo "Successful: $successful"
echo "Failed:     $failed"
echo "Total:      $((successful + failed))"
echo ""

# List downloaded files
echo "Downloaded files:"
ls -1 *.pdf 2>/dev/null | nl
echo ""

# Calculate total size
if [ $successful -gt 0 ]; then
    total_size=$(du -sh . | awk '{print $1}')
    echo "Total download size: $total_size"
fi

echo ""
echo "For more information, see:"
echo "  - README.md (overview)"
echo "  - RESEARCH_SUMMARY.md (detailed analysis)"
echo "  - cluster_1_metadata.csv (paper metadata)"
echo ""
