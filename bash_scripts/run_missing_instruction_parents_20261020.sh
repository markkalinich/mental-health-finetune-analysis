#!/usr/bin/env bash
# Instruction-tuned parents that have no locked-task files.
# One local RTX. Load one model, run the locked prompts, then SIGTERM the server.
#   suicide_ideation_yesno_v2     450   max_tokens 256
#   cssrs_yesno_v5                500   max_tokens 256
#   MentalHealthBench            1215   max_tokens 2048, temperature 0
# Luna starts after a finished MentalHealthBench file and does not hold the GPU.
# Skips a task that already has a complete file. Exits if a vLLM server is
# already running. Does not stop it. Do not SIGKILL. Ignores SIGHUP.
set -uo pipefail
trap '' HUP

MH_ROOT=/home/mkalinich/main
SI_PY="$MH_ROOT/.venv/bin/python"
VLLM_PY=/home/mkalinich/phone-data-video-extraction/.venv-vllm/bin/python
VLLM_ROOT=/home/mkalinich/phone-data-video-extraction
PORT=8000
BASE_URL="http://127.0.0.1:${PORT}/v1"
MAX_CONCURRENT=128
VERSION=20261019med
REPAIRS="$MH_ROOT/config/serving_repairs.csv"
SI_PROMPT="$MH_ROOT/data/prompts/suicide_ideation_yesno_v2.txt"
SI_PREFIX=$(tr -d '\n' < "$MH_ROOT/data/prompts/suicide_ideation_yesno_v2_prefix.txt")
SI_SUFFIX=$(tr -d '\n' < "$MH_ROOT/data/prompts/suicide_ideation_yesno_v2_suffix.txt")
SI_INPUT="$MH_ROOT/data/inputs/finalized_input_data/SI_finalized_sentences.csv"
SI_OUT="$MH_ROOT/replies/si-yesno-v2"
CSSRS_PROMPT="$MH_ROOT/data/prompts/cssrs_yesno_v5.txt"
CSSRS_PREFIX=$(tr -d '\n' < "$MH_ROOT/data/prompts/cssrs_yesno_v5_prefix.txt")
CSSRS_SUFFIX=$(tr -d '\n' < "$MH_ROOT/data/prompts/cssrs_yesno_v5_suffix.txt")
CSSRS_OUT="$MH_ROOT/replies/cssrs-yesno-v5"
MHB_DATA=/home/mkalinich/local_benchmarks/mentalhealthbench/mentalhealthbench/mentalhealthbench_eval.jsonl
MHB_OUT="$MH_ROOT/replies/mentalhealthbench-1215-temp0"
STAMP=$(date +%Y%m%d_%H%M%S)
RUN_DIR="$MH_ROOT/replies/missing-instruction-parents-${STAMP}"
mkdir -p "$RUN_DIR"
printf 'hf_id\tstatus\tdetail\n' > "$RUN_DIR/status.tsv"
: > "$RUN_DIR/luna.pids"
echo "RUN_DIR=$RUN_DIR"

export CUDA_HOME="$VLLM_ROOT/.venv-vllm/lib/python3.11/site-packages/nvidia/cu13"
export PATH="$CUDA_HOME/bin:$PATH"
export VLLM_USE_FLASHINFER_SAMPLER=0
export PYTHONUNBUFFERED=1

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

start_luna() {
  local hf_id="$1"
  local safe="$2"
  local log="$RUN_DIR/luna-${safe}.log"
  echo "$(date -Is) luna start $hf_id"
  (
    cd "$MH_ROOT" && "$SI_PY" -u -m orchestration.grade_mentalhealthbench \
      --generations "$MHB_OUT/$safe" \
      --judge-model gpt-5.6-luna \
      --reasoning-effort high \
      --grades-name grades-gpt-5.6-luna.jsonl
  ) > "$log" 2>&1 &
  echo "$! $hf_id" >> "$RUN_DIR/luna.pids"
  echo "luna pid $! log $log"
}

if pgrep -f '[v]llm.entrypoints.openai.api_server' >/dev/null; then
  echo "A vLLM server is already running. This script will not stop it."
  exit 1
fi

PLAN_FILE="$RUN_DIR/plan.txt"
if ! (
  cd "$MH_ROOT" && "$SI_PY" - "$REPAIRS" "$SI_OUT" "$CSSRS_OUT" "$MHB_OUT" << 'PY'
import csv, json, os, sys
from pathlib import Path
repairs_path, si_out, cssrs_out, mhb_out = sys.argv[1:]
HF = Path("/home/mkalinich/hf_models")
MODELS = [
    "Qwen/Qwen3-0.6B",
    "Qwen/Qwen2.5-3B-Instruct",
    "unsloth/DeepSeek-R1-Distill-Qwen-1.5B",
]
repairs = {}
if Path(repairs_path).is_file():
    repairs = {row["hf_id"]: row for row in csv.DictReader(open(repairs_path, newline=""))}

def safe(hf):
    return hf.replace("/", "__")

def ready_bytes(hf):
    directory = HF / safe(hf)
    if not directory.is_dir() or not (directory / "config.json").is_file():
        return None
    nbytes = 0
    saw = False
    for dirpath, dirnames, filenames in os.walk(directory, followlinks=True):
        dirnames[:] = [name for name in dirnames if name not in (".cache", ".git")]
        for name in filenames:
            if name.endswith(".incomplete"):
                return None
            if name.endswith((".safetensors", ".bin", ".pth")) and "optimizer" not in name and not name.startswith("adapter_"):
                saw = True
                nbytes += (Path(dirpath) / name).stat().st_size
    return nbytes if saw else None

def maxlen_of(hf, nbytes):
    cfg = json.loads((HF / safe(hf) / "config.json").read_text())
    n = cfg.get("max_position_embeddings")
    if not isinstance(n, int) and isinstance(cfg.get("text_config"), dict):
        n = cfg["text_config"].get("max_position_embeddings")
    if not isinstance(n, int):
        n = 12288 if cfg.get("model_type") == "gemma3" else 8192
    cap = 12288 if nbytes > 45 * (1024 ** 3) else 32768
    return min(int(n), max(4096, min(int(n), cap)))

def si_done(hf):
    path = Path(si_out) / safe(hf) / "suicidal_ideation_summary.json"
    if not path.is_file():
        return False
    data = json.loads(path.read_text())
    return (
        "suicide_ideation_yesno_v2" in data.get("experiment_id", "")
        and data.get("status") == "completed"
        and data.get("total_results") == 450
    )

def cssrs_done(hf):
    path = Path(cssrs_out) / safe(hf) / "metrics.json"
    if not path.is_file():
        return False
    data = json.loads(path.read_text())
    metrics = data.get("metrics") or {}
    return (
        str(data.get("prompt", "")).endswith("cssrs_yesno_v5.txt")
        and metrics.get("n") == 500
        and bool(data.get("user_prefix"))
        and bool(data.get("user_suffix"))
    )

def mhb_done(hf):
    path = Path(mhb_out) / safe(hf) / "summary.json"
    if not path.is_file():
        return False
    data = json.loads(path.read_text())
    return data.get("n_items") == 1215 and data.get("n_samples") == 1 and data.get("n_api_errors") == 0

planned = []
for hf in MODELS:
    nbytes = ready_bytes(hf)
    if nbytes is None:
        print(f"MISSING {hf}", file=sys.stderr)
        continue
    tasks = []
    if not si_done(hf):
        tasks.append("si")
    if not cssrs_done(hf):
        tasks.append("cssrs")
    if not mhb_done(hf):
        tasks.append("mhb")
    if not tasks:
        print(f"skip {hf} already complete", file=sys.stderr)
        continue
    src = repairs.get(hf, {}).get("tokenizer_from", "")
    tok = str(HF / safe(src)) if src else ""
    family = "qwen" if "qwen" in hf.lower() else "other"
    seqs = 8 if nbytes > 45 * (1024 ** 3) else 128
    planned.append((nbytes, hf, safe(hf), family, str(maxlen_of(hf, nbytes)), str(seqs), tok, ",".join(tasks)))
if not planned:
    raise SystemExit("no models left to run")
planned.sort(key=lambda row: (row[0], row[1].lower()))
for row in planned:
    print("|".join(row[1:]))
print(f"queue_models={len(planned)}", file=sys.stderr)
PY
) > "$PLAN_FILE"; then
  echo "Serve plan failed"
  exit 1
fi

mapfile -t PLAN < "$PLAN_FILE"
if [[ ${#PLAN[@]} -eq 0 ]]; then
  echo "No models in the serve plan."
  exit 1
fi

for line in "${PLAN[@]}"; do
  [[ -z "$line" ]] && continue
  IFS='|' read -r hf_id dirname family maxlen seqs tokenizer_dir tasks <<<"$line"
  log="$RUN_DIR/${dirname}.vllm.log"
  model_path="/home/mkalinich/hf_models/${dirname}"
  extra_args=()
  tok_args=()
  if [[ -n "$tokenizer_dir" ]]; then
    if [[ ! -f "$tokenizer_dir/tokenizer_config.json" ]]; then
      record "$hf_id" "skip" "repair tokenizer dir missing: $tokenizer_dir"
      continue
    fi
    tok_args=(--tokenizer "$tokenizer_dir")
    record "$hf_id" "repair" "tokenizer_from=$(basename "$tokenizer_dir")"
    if [[ -f "$tokenizer_dir/chat_template.jinja" ]]; then
      tok_args+=(--chat-template "$tokenizer_dir/chat_template.jinja")
    fi
  fi
  echo "---- serve $hf_id len=$maxlen seqs=$seqs tasks=$tasks ----"
  "$VLLM_PY" -m vllm.entrypoints.openai.api_server \
    --model "$model_path" \
    --served-model-name "$hf_id" \
    --host 127.0.0.1 \
    --port "$PORT" \
    --max-model-len "$maxlen" \
    --max-num-seqs "$seqs" \
    --gpu-memory-utilization 0.90 \
    --generation-config vllm \
    --enforce-eager \
    "${extra_args[@]}" \
    "${tok_args[@]}" \
    > "$log" 2>&1 &
  VLLM_PID=$!
  echo "vLLM pid $VLLM_PID log $log"
  if ! wait_ready "$hf_id"; then
    record "$hf_id" "fail" "vLLM did not become ready"
    stop_vllm || exit 1
    continue
  fi
  if [[ "$tasks" == *si* ]]; then
    if (
      cd "$MH_ROOT" && "$SI_PY" -u -m orchestration.run_experiment \
        --experiment-name "si_v2_${dirname}" \
        --model-family "$family" \
        --model-size "$dirname" \
        --model-version "$VERSION" \
        --model-name "$hf_id" \
        --prompt-name suicide_ideation_yesno_v2 \
        --input "$SI_INPUT" \
        --system "$SI_PROMPT" \
        --user-prefix "$SI_PREFIX" \
        --user-suffix "$SI_SUFFIX" \
        --base-url "$BASE_URL" \
        --base-dir "$MH_ROOT" \
        --temperature 0 \
        --max-tokens 256 \
        --max-concurrent "$MAX_CONCURRENT" \
        --output-summary "$SI_OUT/${dirname}/suicidal_ideation_summary.json"
    ); then
      record "$hf_id" "ok" "si v2 exit 0"
    else
      record "$hf_id" "fail" "si v2 exit $?"
    fi
  fi
  if [[ "$tasks" == *cssrs* ]]; then
    if (
      cd "$MH_ROOT" && "$SI_PY" -u -m orchestration.run_cssrs_yesno \
        --base-url "$BASE_URL" \
        --model-name "$hf_id" \
        --model-family "$family" \
        --model-size "$dirname" \
        --model-version "$VERSION" \
        --system "$CSSRS_PROMPT" \
        --user-prefix "$CSSRS_PREFIX" \
        --user-suffix "$CSSRS_SUFFIX" \
        --output-dir "$CSSRS_OUT/${dirname}" \
        --temperature 0 \
        --max-tokens 256 \
        --max-concurrent "$MAX_CONCURRENT"
    ); then
      record "$hf_id" "ok" "cssrs v5 exit 0"
    else
      record "$hf_id" "fail" "cssrs v5 exit $?"
    fi
  fi
  if [[ "$tasks" == *mhb* ]]; then
    if (
      cd "$MH_ROOT" && "$SI_PY" -u -m orchestration.run_mentalhealthbench \
        --base-url "$BASE_URL" \
        --model-name "$hf_id" \
        --model-family "$family" \
        --model-size "$dirname" \
        --model-version "$VERSION" \
        --data "$MHB_DATA" \
        --output-dir "$MHB_OUT/${dirname}" \
        --samples 1 \
        --temperature 0 \
        --max-tokens 2048 \
        --max-concurrent 128
    ); then
      record "$hf_id" "ok" "mhb 1215 exit 0"
      start_luna "$hf_id" "$dirname"
    else
      record "$hf_id" "fail" "mhb exit $?"
    fi
  fi
  stop_vllm || exit 1
done

echo "RUN_DIR=$RUN_DIR"
echo "generation queue finished; luna pids are in $RUN_DIR/luna.pids"
