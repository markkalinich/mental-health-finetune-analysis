#!/usr/bin/env bash
# One reply on all 1,215 MentalHealthBench items for the mental-health
# kept fine-tunes and their instruction-tuned parents.
# Temperature 0, one sample, max 2048 tokens: the same settings as the
# 100-item runs, so those 100 replies are cache hits.
# howardbaik/gemma-4-E4B-it-mentalchat16k is not in kept.csv.
# SoufianeDahimi/child_trauma_gemma_finetune is. Its local config.json is bfloat16.
# SIGTERM only. Do not SIGKILL. Ignores SIGHUP so a closed shell does not stop it.
set -uo pipefail
trap '' HUP

MH_ROOT=/home/mkalinich/main
SI_PY="$MH_ROOT/.venv/bin/python"
VLLM_PY=/home/mkalinich/phone-data-video-extraction/.venv-vllm/bin/python
VLLM_ROOT=/home/mkalinich/phone-data-video-extraction
DATA=$(cd "$MH_ROOT" && "$SI_PY" -m config.datasets mentalhealthbench_eval) || exit 1
PORT=8000
BASE_URL="http://127.0.0.1:${PORT}/v1"
CURRENT=$(tr -d '[:space:]' < "$MH_ROOT/outputs/funnel/mental-health/CURRENT")
KEPT="$MH_ROOT/outputs/funnel/mental-health/${CURRENT}/kept.csv"
REPAIRS="$MH_ROOT/config/serving_repairs.csv"
OUT="$MH_ROOT/replies/mentalhealthbench-1215-temp0"
STAMP=$(date +%Y%m%d_%H%M%S)
RUN_DIR="$OUT/rtx-${STAMP}"
mkdir -p "$RUN_DIR"
printf 'hf_id\tstatus\tdetail\n' > "$RUN_DIR/status.tsv"
echo "RUN_DIR=$RUN_DIR"
echo "DATA=$DATA"

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

mapfile -t PLAN < <(
  "$SI_PY" - "$KEPT" "$REPAIRS" "$OUT" << 'PY'
import csv, json, os, sys
from pathlib import Path
kept_path, repairs_path, out_root = sys.argv[1:]
HF = Path("/home/mkalinich/hf_models")
skip = set()
rows = list(csv.DictReader(open(kept_path, newline="")))
order = []
seen = set()
for row in rows:
    for hf in (row["hf_id"], row["parent"]):
        if hf in seen or hf in skip:
            continue
        seen.add(hf)
        order.append(hf)
repairs = {}
if Path(repairs_path).is_file():
    repairs = {r["hf_id"]: r for r in csv.DictReader(open(repairs_path, newline=""))}

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
        n = 12288 if cfg.get("model_type") == "gemma3" else 8192
    cap = 12288 if nbytes > 45 * (1024 ** 3) else 32768
    return min(int(n), max(4096, min(int(n), cap)))

planned = []
for hf in order:
    summary = Path(out_root) / safe(hf) / "summary.json"
    if summary.is_file():
        s = json.loads(summary.read_text())
        if s.get("n_items") == 1215 and s.get("n_samples") == 1 and s.get("n_api_errors") == 0:
            print(f"skip {hf} already 1215", file=sys.stderr)
            continue
    nbytes = ready_bytes(hf)
    if nbytes is None:
        print(f"skip {hf} weights missing", file=sys.stderr)
        continue
    src = repairs.get(hf, {}).get("tokenizer_from", "")
    tok = str(HF / safe(src)) if src else ""
    seqs = 8 if nbytes > 45 * (1024 ** 3) else 128
    family = "qwen" if "qwen" in hf.lower() else "other"
    planned.append((nbytes, hf, safe(hf), family, str(maxlen_of(hf, nbytes)), str(seqs), tok))
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
  IFS='|' read -r hf_id dirname family maxlen seqs tokenizer_dir <<<"$line"
  safe="$dirname"
  log="$RUN_DIR/${safe}.vllm.log"
  model_path="/home/mkalinich/hf_models/${dirname}"
  tok_args=()
  if [[ -n "$tokenizer_dir" ]]; then
    if [[ ! -f "$tokenizer_dir/tokenizer_config.json" ]]; then
      record "$hf_id" "skip" "repair tokenizer dir missing: $tokenizer_dir"
      continue
    fi
    tok_args=(--tokenizer "$tokenizer_dir")
  fi
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
    "${tok_args[@]}" \
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
  else
    record "$hf_id" "fail" "mhb exit $?"
  fi
  stop_vllm || exit 1
done

echo "RUN_DIR=$RUN_DIR"
