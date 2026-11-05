#!/usr/bin/env bash
# Pilot suicide_ideation_yesno_v2 on six models. 450 sentences each.
# Three low one-word parse rates, then three that already parse every sentence.
# The sentence sits between the prefix and the decision line.
# Does not write replies/si_vllm/ or replies/medical-30/.
# One local RTX. Load one model, run the 450 sentences, then SIGTERM the server.
# Do not SIGKILL. Ignores SIGHUP. Exits if a vLLM server is already running.
set -uo pipefail
trap '' HUP

MH_ROOT=/home/mkalinich/main
SI_PY="$MH_ROOT/.venv/bin/python"
VLLM_PY=/home/mkalinich/phone-data-video-extraction/.venv-vllm/bin/python
VLLM_ROOT=/home/mkalinich/phone-data-video-extraction
PORT=8000
BASE_URL="http://127.0.0.1:${PORT}/v1"
MAX_CONCURRENT=128
PROMPT="$MH_ROOT/data/prompts/suicide_ideation_yesno_v2.txt"
PREFIX=$(tr -d '\n' < "$MH_ROOT/data/prompts/suicide_ideation_yesno_v2_prefix.txt")
SUFFIX=$(tr -d '\n' < "$MH_ROOT/data/prompts/suicide_ideation_yesno_v2_suffix.txt")
INPUT="$MH_ROOT/data/inputs/finalized_input_data/SI_finalized_sentences.csv"
OUT="$MH_ROOT/replies/si-yesno-v2"
STAMP=$(date +%Y%m%d_%H%M%S)
RUN_DIR="$OUT/rtx-${STAMP}"
mkdir -p "$RUN_DIR"
printf 'hf_id\tstatus\tdetail\n' > "$RUN_DIR/status.tsv"
echo "RUN_DIR=$RUN_DIR"

export CUDA_HOME="$VLLM_ROOT/.venv-vllm/lib/python3.11/site-packages/nvidia/cu13"
export PATH="$CUDA_HOME/bin:$PATH"
export VLLM_USE_FLASHINFER_SAMPLER=0
export PYTHONUNBUFFERED=1

if pgrep -f 'vllm.entrypoints.openai.api_server' >/dev/null; then
  echo "A vLLM server is already running. This script will not stop it."
  exit 1
fi

VLLM_PID=""

record() {
  printf '%s\t%s\t%s\n' "$1" "$2" "$3" >> "$RUN_DIR/status.tsv"
  echo "$(date -Is) $2 $1 $3"
}

stop_vllm() {
  if [[ -z "${VLLM_PID}" ]]; then
    return 0
  fi
  if ! kill -0 "$VLLM_PID" 2>/dev/null; then
    VLLM_PID=""
    return 0
  fi
  echo "SIGTERM vLLM pid $VLLM_PID"
  kill -TERM "$VLLM_PID" || true
  local _
  for _ in $(seq 1 40); do
    if ! kill -0 "$VLLM_PID" 2>/dev/null; then
      echo "vLLM parent exited"
      VLLM_PID=""
      return 0
    fi
    sleep 3
  done
  echo "ERROR: vLLM pid $VLLM_PID still alive after SIGTERM. Not sending SIGKILL."
  return 1
}

trap 'stop_vllm || true' EXIT
trap '' HUP

wait_ready() {
  local name="$1"
  local _
  for _ in $(seq 1 240); do
    if ! kill -0 "$VLLM_PID" 2>/dev/null; then
      echo "vLLM process exited before ready"
      return 1
    fi
    if curl -sf "http://127.0.0.1:${PORT}/v1/models" | grep -F "$name" >/dev/null; then
      return 0
    fi
    sleep 5
  done
  echo "vLLM did not become ready"
  return 1
}

# hf_id|dirname|family|maxlen|seqs|tokenizer_dir
# tokenizer_dir is empty except SQPsych, which has no tokenizer files of its own.
LLAMA3_TOK="/home/mkalinich/hf_models/meta-llama__Meta-Llama-3-8B-Instruct"
PLAN=(
  "dzur658/smollm2-mentalhealth-360m-V2|dzur658__smollm2-mentalhealth-360m-V2|other|8192|128|"
  "Wothmag07/counseLLM|Wothmag07__counseLLM|other|32768|128|"
  "AIMH/SQPsychLLM-8b-gemma-no_questionnaire|AIMH__SQPsychLLM-8b-gemma-no_questionnaire|other|8192|128|${LLAMA3_TOK}"
  "google/gemma-3-1b-it|google__gemma-3-1b-it|other|32768|128|"
  "Qwen/Qwen3-1.7B|Qwen__Qwen3-1.7B|qwen|32768|128|"
  "Qwen/Qwen2.5-7B-Instruct|Qwen__Qwen2.5-7B-Instruct|qwen|32768|128|"
)

for line in "${PLAN[@]}"; do
  IFS='|' read -r hf_id dirname family maxlen seqs tokenizer_dir <<<"$line"
  summary="$OUT/${dirname}/suicidal_ideation_summary.json"
  if [[ -f "$summary" ]] && grep -q 'suicide_ideation_yesno_v2' "$summary"; then
    record "$hf_id" "skip" "v2 summary already present"
    continue
  fi
  log="$RUN_DIR/${dirname}.vllm.log"
  model_path="/home/mkalinich/hf_models/${dirname}"
  tok_args=()
  if [[ -n "$tokenizer_dir" ]]; then
    tok_args=(--tokenizer "$tokenizer_dir")
  fi
  echo "---- serve $hf_id len=$maxlen seqs=$seqs ----"
  "$VLLM_PY" -m vllm.entrypoints.openai.api_server \
    --model "$model_path" \
    --served-model-name "$hf_id" \
    --host 127.0.0.1 \
    --port "$PORT" \
    "${tok_args[@]}" \
    --max-model-len "$maxlen" \
    --max-num-seqs "$seqs" \
    --gpu-memory-utilization 0.90 \
    --generation-config vllm \
    --enforce-eager \
    > "$log" 2>&1 &
  VLLM_PID=$!
  echo "vLLM pid $VLLM_PID log $log"
  if ! wait_ready "$hf_id"; then
    record "$hf_id" "fail" "vLLM did not become ready"
    stop_vllm || exit 1
    continue
  fi
  if (
    cd "$MH_ROOT" && "$SI_PY" -u -m orchestration.run_experiment \
      --experiment-name "si_v2_${dirname}" \
      --model-family "$family" \
      --model-size "$dirname" \
      --model-version 20261017v2 \
      --model-name "$hf_id" \
      --prompt-name suicide_ideation_yesno_v2 \
      --input "$INPUT" \
      --system "$PROMPT" \
      --user-prefix "$PREFIX" \
      --user-suffix "$SUFFIX" \
      --base-url "$BASE_URL" \
      --base-dir "$MH_ROOT" \
      --temperature 0 \
      --max-tokens 256 \
      --max-concurrent "$MAX_CONCURRENT" \
      --output-summary "$summary"
  ); then
    record "$hf_id" "ok" "450 exit 0"
  else
    record "$hf_id" "fail" "run exit $?"
  fi
  stop_vllm || exit 1
done

echo "RUN_DIR=$RUN_DIR"
