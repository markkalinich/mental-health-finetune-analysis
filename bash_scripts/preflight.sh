#!/bin/bash
#
# Preflight Validation for Safety Simulation Experiments
#
# This script validates that everything is ready to run experiments:
# - Virtual environment is active
# - Input files exist
# - LM Studio is running and queryable
# - Models are available in registry and LM Studio
#
# Usage:
#   ./preflight.sh INPUT_DATA PROMPT_FILE PROMPT_NAME [MODELS]
#   
#   Returns exit code 0 if ready to run, 1 if validation fails.
#   When successful, exports variables for run_experiments.sh to use.
#
# Can be run standalone to check readiness without running experiments.

set -e  # Exit on any error

# =============================================================================
# Virtual Environment Setup
# =============================================================================

activate_venv() {
    # Determine project root (parent of bash_scripts directory)
    SCRIPT_DIR_TEMP="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
    export PROJECT_ROOT="$(cd "${SCRIPT_DIR_TEMP}/.." && pwd)"
    
    if [[ -z "${VIRTUAL_ENV}" ]]; then
        VENV_PATH="${PROJECT_ROOT}/.venv"
        if [[ -f "${VENV_PATH}/bin/activate" ]]; then
            echo "🔧 Activating virtual environment..."
            source "${VENV_PATH}/bin/activate"
            echo "✓ Using Python: $(which python) (version $(python --version 2>&1 | cut -d' ' -f2))"
        else
            echo "❌ Error: Virtual environment not found at ${VENV_PATH}"
            echo "   Please create it with: python -m venv .venv && pip install -r requirements.txt"
            return 1
        fi
    else
        echo "✓ Already in virtual environment: ${VIRTUAL_ENV}"
    fi
    
    echo "✓ Project root: ${PROJECT_ROOT}"
}

run_python_module() {
    # Run Python module commands from project root to ensure imports work
    (cd "${PROJECT_ROOT}" && python -m "$@")
}

# =============================================================================
# Argument Parsing
# =============================================================================

usage() {
    echo "Usage: $0 [OPTIONS] INPUT_DATA PROMPT_FILE PROMPT_NAME"
    echo ""
    echo "Required Arguments:"
    echo "  INPUT_DATA   Path to input CSV file"
    echo "  PROMPT_FILE  Path to prompt text file"  
    echo "  PROMPT_NAME  Exact prompt name (see below)"
    echo ""
    echo "Options:"
    echo "  --models MODELS      Comma-separated list of family:size pairs to run"
    echo "                       If not provided, runs all enabled models from registry"
    echo "  --replicates N       Number of replicates per sample (default: 1)"
    echo ""
    echo "PROMPT_NAME should contain keywords to identify experiment type:"
    echo "  - 'suicide', 'si_', 'safety' → suicidal ideation"
    echo "  - 'engagement' → therapy engagement"
    echo "  - 'therapy', 'request', 'counseling' → therapy request"
    echo ""
    echo "Valid PROMPT_NAME examples:"
    echo "  system_suicide_detection_v2, therapy_request_classifier_v3,"
    echo "  system_therapy_engagement_v2, etc."
    echo ""
    echo "Examples:"
    echo "  # Run all enabled models"
    echo "  $0 data/inputs/finalized_input_data/SI_finalized_sentences.csv \\"
    echo "     data/prompts/system_suicide_detection_v2.txt \\"
    echo "     system_suicide_detection_v2"
    echo ""
    echo "  # Run specific models with 3 replicates"
    echo "  $0 --models \"gemma:270m-it,gemma:1b-it\" --replicates 3 \\"
    echo "     data/inputs/finalized_input_data/SI_finalized_sentences.csv \\"
    echo "     data/prompts/system_suicide_detection_v2.txt \\"
    echo "     system_suicide_detection_v2"
    exit 1
}

parse_arguments() {
    export MODELS_OVERRIDE=""
    export NUM_REPLICATES=1
    
    # Parse options first
    while [[ "$1" == --* ]]; do
        case "$1" in
            --models)
                if [ -z "$2" ] || [[ "$2" == --* ]]; then
                    echo "❌ Error: --models requires a value"
                    usage
                fi
                export MODELS_OVERRIDE="$2"
                shift 2
                ;;
            --replicates)
                if [ -z "$2" ] || [[ "$2" == --* ]]; then
                    echo "❌ Error: --replicates requires a number"
                    usage
                fi
                if ! [[ "$2" =~ ^[0-9]+$ ]]; then
                    echo "❌ Error: --replicates must be a positive integer, got: $2"
                    usage
                fi
                export NUM_REPLICATES="$2"
                shift 2
                ;;
            --help|-h)
                usage
                ;;
            *)
                echo "❌ Error: Unknown option: $1"
                usage
                ;;
        esac
    done
    
    # Now parse required positional arguments
    if [ $# -lt 3 ]; then
        echo "❌ Error: Missing required arguments"
        echo "   Got: $@"
        usage
    fi

    export INPUT_DATA="$1"
    export PROMPT_FILE="$2"
    export PROMPT_NAME="$3"
    
    # Check for extra positional arguments (catch old usage pattern)
    if [ $# -gt 3 ]; then
        echo "❌ Error: Too many positional arguments"
        echo "   Did you mean to use --models? Example:"
        echo "   $0 --models \"$4\" $1 $2 $3"
        usage
    fi
}

# =============================================================================
# File Validation
# =============================================================================

validate_input_files() {
    echo ""
    echo "📁 Validating input files..."
    
    if [[ ! -f "$INPUT_DATA" ]]; then
        echo "❌ Error: Input data file not found: $INPUT_DATA"
        return 1
    fi
    echo "  ✓ Input data: $INPUT_DATA"
    
    if [[ ! -f "$PROMPT_FILE" ]]; then
        echo "❌ Error: Prompt file not found: $PROMPT_FILE"
        return 1
    fi
    echo "  ✓ Prompt file: $PROMPT_FILE"
    
    # Count samples in input data
    local sample_count
    sample_count=$(tail -n +2 "$INPUT_DATA" | wc -l)
    echo "  ✓ Input samples: $sample_count"
    export INPUT_SAMPLE_COUNT=$sample_count
}

# =============================================================================
# Experiment Type Detection
# =============================================================================

detect_experiment_type() {
    echo ""
    echo "🔬 Validating experiment type..."
    
    # Use flexible pattern matching to infer experiment type (matches Python logic)
    local prompt_lower
    prompt_lower=$(echo "${PROMPT_NAME}" | tr '[:upper:]' '[:lower:]')
    
    if [[ "${prompt_lower}" == *"suicide"* ]] || [[ "${prompt_lower}" == *"si_"* ]] || [[ "${prompt_lower}" == *"safety"* ]]; then
        export EXPERIMENT_TYPE="suicidal_ideation"
        export ANALYSIS_NAME="suicidal_ideation_model_comparison"
        export SUFFIX="SI"
    elif [[ "${prompt_lower}" == *"engagement"* ]]; then
        export EXPERIMENT_TYPE="therapy_engagement"
        export ANALYSIS_NAME="therapy_engagement_model_comparison"
        export SUFFIX="tx_engagement"
    elif [[ "${prompt_lower}" == *"therapy"* ]] || [[ "${prompt_lower}" == *"request"* ]] || [[ "${prompt_lower}" == *"counseling"* ]]; then
        export EXPERIMENT_TYPE="therapy_request"
        export ANALYSIS_NAME="therapy_request_model_comparison"
        export SUFFIX="tx_request"
    else
        echo "❌ Error: Could not infer experiment type from prompt name '${PROMPT_NAME}'"
        echo ""
        echo "   PROMPT_NAME should contain one of these keywords:"
        echo "     - 'suicide', 'si_', or 'safety' for suicidal ideation experiments"
        echo "     - 'engagement' for therapy engagement experiments"
        echo "     - 'therapy', 'request', or 'counseling' for therapy request experiments"
        echo ""
        echo "   Examples of valid names:"
        echo "     - system_suicide_detection_v2"
        echo "     - therapy_request_classifier_v3"
        echo "     - system_therapy_engagement_v2"
        return 1
    fi
    
    echo "  ✓ Experiment type: $EXPERIMENT_TYPE (inferred from '${PROMPT_NAME}')"
}

# =============================================================================
# LM Studio Validation
# =============================================================================

check_lm_studio() {
    echo ""
    echo "🖥️  Checking LM Studio..."
    
    if ! run_python_module utilities.lms_manager --check --quiet 2>/dev/null; then
        echo "❌ Error: LM Studio is not running or not responding"
        echo "   Please start LM Studio and ensure the local server is enabled."
        return 1
    fi
    echo "  ✓ LM Studio is running"
}

check_lms_inventory() {
    echo ""
    echo "📋 Checking LM Studio model inventory..."
    
    # Query LM Studio directly for model list
    local lms_output
    if ! lms_output=$(lms ls --json 2>&1); then
        echo "❌ Error: Failed to query LM Studio model inventory"
        echo "   Command 'lms ls --json' failed"
        echo "   Is LM Studio running?"
        return 1
    fi
    
    # Count models
    local model_count
    model_count=$(echo "$lms_output" | python -c "import json, sys; print(len(json.load(sys.stdin)))" 2>/dev/null || echo "0")
    
    if [ "$model_count" -eq 0 ]; then
        echo "⚠️  Warning: No models found in LM Studio"
        echo "   Download models in LM Studio before running experiments"
    else
        echo "  ✓ Models available in LM Studio: $model_count"
    fi
}

# =============================================================================
# Model Registry Validation
# =============================================================================

validate_model_registry() {
    echo ""
    echo "📊 Checking model registry..."
    
    local stats
    stats=$(run_python_module config.models_registry --stats 2>/dev/null) || {
        echo "❌ Error: Could not read model registry"
        return 1
    }
    
    # Extract key stats
    local enabled_count
    enabled_count=$(echo "$stats" | grep "Enabled:" | awk '{print $2}')
    local family_count
    family_count=$(echo "$stats" | grep "Families:" | awk '{print $2}')
    
    echo "  ✓ Enabled models: $enabled_count"
    echo "  ✓ Model families: $family_count"
}

# =============================================================================
# Model Availability Validation
# =============================================================================

validate_models_available() {
    echo ""
    echo "🔍 Validating model availability..."
    
    local models_to_check
    local available_models
    local missing_count=0
    local found_count=0
    local total_count=0
    
    # Get available models from LM Studio
    available_models=$(lms ls 2>/dev/null | tail -n +4 | awk '{print $1}' || true)
    
    if [ -n "${MODELS_OVERRIDE}" ]; then
        # Check specific models
        echo "  Checking specified models: ${MODELS_OVERRIDE}"
        IFS=',' read -ra MODEL_ARRAY <<< "${MODELS_OVERRIDE}"
        
        for model_pair in "${MODEL_ARRAY[@]}"; do
            local family size spec lm_studio_id
            family="${model_pair%%:*}"
            size="${model_pair#*:}"
            total_count=$((total_count + 1))
            
            spec=$(run_python_module config.models_registry --family "${family}" --size "${size}" --get-spec 2>/dev/null) || {
                echo "    ❌ ${family}:${size} - not in registry"
                missing_count=$((missing_count + 1))
                continue
            }
            lm_studio_id="${spec#*|}"
            
            if echo "${available_models}" | grep -qF "${lm_studio_id}"; then
                echo "    ✓ ${family}:${size}"
                found_count=$((found_count + 1))
            else
                echo "    ❌ ${family}:${size} - not in LM Studio"
                missing_count=$((missing_count + 1))
            fi
        done
    else
        # Check ALL enabled models individually
        echo "  Checking all enabled models..."
        local families
        families=$(run_python_module config.models_registry --list-families 2>/dev/null)
        
        for family in ${families}; do
            local sizes
            sizes=$(run_python_module config.models_registry --family "${family}" --list-sizes 2>/dev/null)
            
            for size in ${sizes}; do
                total_count=$((total_count + 1))
                local spec lm_studio_id
                spec=$(run_python_module config.models_registry --family "${family}" --size "${size}" --get-spec 2>/dev/null) || continue
                lm_studio_id="${spec#*|}"
                
                if echo "${available_models}" | grep -qF "${lm_studio_id}"; then
                    found_count=$((found_count + 1))
                else
                    echo "    ❌ ${family}:${size} - not in LM Studio (${lm_studio_id})"
                    missing_count=$((missing_count + 1))
                fi
            done
        done
        
        echo "  ✓ ${found_count}/${total_count} models available in LM Studio"
    fi
    
    export MODELS_FOUND=$found_count
    export MODELS_MISSING=$missing_count
    export MODELS_TOTAL=$total_count
    
    if [ $missing_count -gt 0 ] && [ -n "${MODELS_OVERRIDE}" ]; then
        echo ""
        echo "⚠️  Some specified models are not available."
        echo "   They will be skipped during the experiment run."
    fi
}

# =============================================================================
# Cache Validation
# =============================================================================

validate_cache_status() {
    echo ""
    echo "📦 Checking cache status for all enabled models..."
    
    # Run batch cache checker
    local cache_output
    cache_output=$(run_python_module utilities.batch_cache_checker \
        --prompt-name "${PROMPT_NAME}" \
        --prompt-file "${PROMPT_FILE}" \
        --input-data "${INPUT_DATA}" \
        --num-replicates "${NUM_REPLICATES}" 2>&1)
    local cache_exit_code=$?
    
    # Parse output
    local complete_line
    complete_line=$(echo "${cache_output}" | grep "^COMPLETE:" | head -1)
    local incomplete_line
    incomplete_line=$(echo "${cache_output}" | grep "^INCOMPLETE:" | head -1)
    
    if [ -n "${complete_line}" ]; then
        echo "  ✓ ${complete_line}"
    fi
    
    if [ ${cache_exit_code} -eq 0 ]; then
        # All models fully cached
        echo "  ✓ All models fully cached - no inference required!"
        export CACHE_STATUS="complete"
        export INCOMPLETE_MODEL_COUNT=0
    elif [ ${cache_exit_code} -eq 1 ]; then
        # Some models incomplete
        echo "  ⚠ ${incomplete_line}"
        echo ""
        # Show the incomplete models list
        echo "${cache_output}" | grep -A 1000 "^Incomplete models:" | tail -n +2
        echo ""
        
        # Extract count from "INCOMPLETE: N models below 100%"
        local incomplete_count
        incomplete_count=$(echo "${incomplete_line}" | grep -oE '[0-9]+' | head -1)
        export CACHE_STATUS="incomplete"
        export INCOMPLETE_MODEL_COUNT="${incomplete_count:-0}"
    else
        # Error occurred
        echo "  ⚠ Could not check cache status (continuing anyway)"
        export CACHE_STATUS="unknown"
        export INCOMPLETE_MODEL_COUNT=-1
    fi
}

# =============================================================================
# Summary
# =============================================================================

print_summary() {
    echo ""
    echo "═══════════════════════════════════════════════════════════════════"
    echo "  PREFLIGHT SUMMARY"
    echo "═══════════════════════════════════════════════════════════════════"
    echo ""
    echo "  Experiment:     ${EXPERIMENT_TYPE}"
    echo "  Input samples:  ${INPUT_SAMPLE_COUNT}"
    echo "  Replicates:     ${NUM_REPLICATES}"
    
    if [ -n "${MODELS_OVERRIDE}" ]; then
        echo "  Models:         ${MODELS_FOUND} specified (${MODELS_MISSING} unavailable)"
    else
        local enabled_models
        enabled_models=$(run_python_module config.models_registry --stats 2>/dev/null | grep "Enabled:" | awk '{print $2}')
        echo "  Models:         ${enabled_models} enabled in registry"
    fi
    
    # Cache status
    if [ "${CACHE_STATUS}" = "complete" ]; then
        echo "  Cache:          ✅ All models fully cached (no inference needed)"
    elif [ "${CACHE_STATUS}" = "incomplete" ]; then
        echo "  Cache:          ⚠️  ${INCOMPLETE_MODEL_COUNT} models need inference"
    else
        echo "  Cache:          ❓ Status unknown"
    fi
    
    echo ""
    if [ "${CACHE_STATUS}" = "complete" ]; then
        echo "  ✅ PREFLIGHT PASSED - Ready to run (all from cache)"
    else
        echo "  ✅ PREFLIGHT PASSED - Ready to run experiments"
        if [ "${INCOMPLETE_MODEL_COUNT}" -gt 0 ]; then
            echo "  ⚠️  Note: ${INCOMPLETE_MODEL_COUNT} models require model loading for inference"
        fi
    fi
    echo ""
    echo "═══════════════════════════════════════════════════════════════════"
}

# =============================================================================
# Main Preflight Function
# =============================================================================

run_preflight() {
    echo "═══════════════════════════════════════════════════════════════════"
    echo "  PREFLIGHT VALIDATION"
    echo "═══════════════════════════════════════════════════════════════════"
    
    activate_venv || return 1
    parse_arguments "$@"
    validate_input_files || return 1
    detect_experiment_type
    check_lm_studio || return 1
    check_lms_inventory || return 1
    validate_model_registry || return 1
    validate_models_available
    validate_cache_status
    print_summary
    
    # Export timestamp for experiments
    export TIMESTAMP=$(date +%Y%m%d_%H%M%S)
    export SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
    
    return 0
}

# =============================================================================
# Entry Point
# =============================================================================

# Only run if executed directly (not sourced)
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    run_preflight "$@"
    exit $?
fi
