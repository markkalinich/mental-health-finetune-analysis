#!/usr/bin/env bash
# MentalHealthBench, 1,215 items, temperature 0, for the three instruction-tuned
# parents that have no grade file. Each model is served, then its Luna grader
# starts in the background. The next model does not wait on Luna.
# SIGTERM only. Do not SIGKILL. Ignores SIGHUP so a closed shell does not stop it.
set -uo pipefail
trap '' HUP

MH_ROOT=/home/mkalinich/main
SI_PY="$MH_ROOT/.venv/bin/python"
VLLM_PY=/home/mkalinich/phone-data-video-extraction/.venv-vllm/bin/python
VLLM_ROOT=/home/mkalinich/phone-data-video-extraction
DATA=/home/mkalinich/local_benchmarks/mentalhealthbench/mentalhealthbench/mentalhealthbench_eval.jsonl
PORT=8000
BASE_URL="http://127.0.0.1:${PORT}/v1"
OUT="$MH_ROOT/replies/mentalhealthbench-1215-temp0"
STAMP=$(date +%Y%m%d_%H%M%S)
RUN_DIR="$OUT/instruction-parents-${STAMP}"
mkdir -p "$RUN_DIR"
printf 'hf_id\tstatus\tdetail\n' > "$RUN_DIR/status.tsv"
: > "$RUN_DIR/luna.pids"
echo "RUN_DIR=$RUN_DIR"
echo "DATA=$DATA"

export CUDA_HOME="$VLLM_ROOT/.venv-vllm/lib/python3.11/site-packages/nvidia/cu13"
export PATH="$CUDA_HOME/bin:$PATH"
export VLLM_USE_FLASHINFER_SAMPLER=0
export PYTHONUNBUFFERED=1

if pgrep -f '[v]llm.entrypoints.openai.api_server' >/dev/null; then
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

start_luna() {
  local hf_id="$1"
  local safe="$2"
  local log="$RUN_DIR/luna-${safe}.log"
  echo "$(date -Is) luna start $hf_id"
  (
    cd "$MH_ROOT" && "$SI_PY" -u -m orchestration.grade_mentalhealthbench \
      --generations "$OUT/$safe" \
      --judge-model gpt-5.6-luna \
      --reasoning-effort high \
      --grades-name grades-gpt-5.6-luna.jsonl
  ) > "$log" 2>&1 &
  echo "$! $hf_id" >> "$RUN_DIR/luna.pids"
  echo "luna pid $! log $log"
}

mapfile -t PLAN < <(
  "$SI_PY" - "$OUT" << 'PY'
import json, os, sys
from pathlib import Path
out_root = Path(sys.argv[1])
HF = Path("/home/mkalinich/hf_models")
order = [
    "google/gemma-3-270m-it",
    "meta-llama/Llama-3.2-1B-Instruct",
    "Qwen/Qwen3-4B-Instruct-2507",
]

def safe(hf):
    return hf.replace("/", "__")

def ready_bytes(hf):
    d = HF / safe(hf)
    if not d.is_dir() or not (d / "config.json").is_file():
        return None
    nbytes = 0
    saw = False
    for dirpath, dirnames, filenames in os.walk(d):
        dirnames[:] = [x for x in dirnames if x not in (".cache", ".git")]
        for fn in filenames:
            if fn.endswith(".incomplete"):
                return None
            if fn.endswith((".safetensors", ".bin", ".pth")) and "optimizer" not in fn:
                saw = True
                nbytes += (Path(dirpath) / fn).stat().st_size
    return nbytes if saw else None

def maxlen_of(hf, nbytes):
    cfg = json.loads((HF / safe(hf) / "config.json").read_text())
    n = cfg.get("max_position_embeddings")
    if not isinstance(n, int) and isinstance(cfg.get("text_config"), dict):
        n = cfg["text_config"].get("max_position_embeddings")
    if not isinstance(n, int):
        n = 8192
    cap = 12288 if nbytes > 45 * (1024 ** 3) else 32768
    return min(int(n), max(4096, min(int(n), cap)))

planned = []
for hf in order:
    summary = out_root / safe(hf) / "summary.json"
    if summary.is_file():
        s = json.loads(summary.read_text())
        if s.get("n_items") == 1215 and s.get("n_samples") == 1 and s.get("n_api_errors") == 0:
            print(f"skip {hf} already 1215", file=sys.stderr)
            continue
    nbytes = ready_bytes(hf)
    if nbytes is None:
        print(f"skip {hf} weights missing", file=sys.stderr)
        continue
    seqs = 8 if nbytes > 45 * (1024 ** 3) else 128
    family = "qwen" if "qwen" in hf.lower() else "other"
    planned.append((nbytes, hf, safe(hf), family, str(maxlen_of(hf, nbytes)), str(seqs)))
planned.sort(key=lambda r: (r[0], r[1].lower()))
for row in planned:
    print("|".join(row[1:]))
print(f"queue_models={len(planned)}", file=sys.stderr)
PY
)

if [[ ${#PLAN[@]} -eq 0 ]]; then
  echo "No models in the serve plan."
  exit 1
fi

for line in "${PLAN[@]}"; do
  IFS='|' read -r hf_id dirname family maxlen seqs <<<"$line"
  safe="$dirname"
  log="$RUN_DIR/${safe}.vllm.log"
  model_path="/home/mkalinich/hf_models/${dirname}"
  echo "---- serve $hf_id len=$maxlen seqs=$seqs ----"
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
    > "$log" 2>&1 &
  VLLM_PID=$!
  echo "vLLM pid $VLLM_PID log $log"
  if ! wait_ready "$hf_id"; then
    record "$hf_id" "fail" "vLLM did not become ready"
    stop_vllm || exit 1
    continue
  fi
  if (
    cd "$MH_ROOT" && "$SI_PY" -u -m orchestration.run_mentalhealthbench \
      --base-url "$BASE_URL" --model-name "$hf_id" --model-family "$family" \
      --model-size "$dirname" --model-version 20261007 \
      --data "$DATA" \
      --output-dir "$OUT/$safe" \
      --samples 1 \
      --temperature 0 \
      --max-tokens 2048 \
      --max-concurrent 128
  ); then
    record "$hf_id" "ok" "mhb 1215 exit 0"
    start_luna "$hf_id" "$safe"
  else
    record "$hf_id" "fail" "mhb exit $?"
  fi
  stop_vllm || exit 1
done

echo "RUN_DIR=$RUN_DIR"
echo "generation queue finished; luna pids are in $RUN_DIR/luna.pids"
