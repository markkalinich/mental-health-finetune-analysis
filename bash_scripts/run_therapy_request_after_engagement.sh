#!/bin/bash
#
# Automated Sequential Experiment Runner
# 
# This script waits for the current therapy engagement experiment to complete,
# then automatically starts the therapy request experiment.
#
# Usage:
#   ./run_therapy_request_after_engagement.sh
#

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"

echo "═══════════════════════════════════════════════════════════════════"
echo "  SEQUENTIAL EXPERIMENT RUNNER"
echo "═══════════════════════════════════════════════════════════════════"
echo ""
echo "This script will:"
echo "  1. Wait for therapy engagement experiment to complete"
echo "  2. Start therapy request experiment automatically"
echo ""
echo "Started: $(date)"
echo ""

# Find the therapy engagement process
echo "🔍 Looking for running therapy engagement experiment..."
ENGAGEMENT_PID=$(ps aux | grep "run_all_models.sh.*therapy_engagement" | grep -v grep | awk '{print $2}' | head -1)

if [ -z "$ENGAGEMENT_PID" ]; then
    echo "⚠️  No therapy engagement experiment is currently running."
    echo "   Starting therapy request experiment immediately..."
else
    echo "✓ Found therapy engagement experiment (PID: $ENGAGEMENT_PID)"
    echo ""
    echo "⏳ Waiting for therapy engagement to complete..."
    echo "   Checking every 30 seconds..."
    
    # Wait for process to complete
    while kill -0 $ENGAGEMENT_PID 2>/dev/null; do
        sleep 30
        echo "   Still running... ($(date +%H:%M:%S))"
    done
    
    echo ""
    echo "✓ Therapy engagement experiment completed at $(date)"
    echo ""
    
    # Give system a moment to settle
    echo "⏸️  Waiting 30 seconds before starting therapy request..."
    sleep 30
fi

echo ""
echo "═══════════════════════════════════════════════════════════════════"
echo "  STARTING THERAPY REQUEST EXPERIMENT"
echo "═══════════════════════════════════════════════════════════════════"
echo ""
echo "Started: $(date)"
echo ""

# Change to script directory and run therapy request experiment
cd "$SCRIPT_DIR"

./run_all_models.sh \
    ../data/inputs/finalized_input_data/therapy_request_finalized_sentences.csv \
    ../data/prompts/therapy_request_classifier_v3.txt \
    therapy_request_classifier_v3

EXIT_CODE=$?

echo ""
echo "═══════════════════════════════════════════════════════════════════"
echo "  THERAPY REQUEST EXPERIMENT COMPLETED"
echo "═══════════════════════════════════════════════════════════════════"
echo ""
echo "Finished: $(date)"
echo "Exit code: $EXIT_CODE"
echo ""

exit $EXIT_CODE
