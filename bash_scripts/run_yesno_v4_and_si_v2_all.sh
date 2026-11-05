#!/usr/bin/env bash
# Record of the 17 Oct 2026 draft-prompt run (C-SSRS v4). The study prompts are synthetic SI v2 and C-SSRS yes/no v5 (docs/yesno-decision-review.md).
# Full heatmap cohort (75 models) on both approved prompts.
#   synthetic SI v2  -> replies/si-yesno-v2/     450 sentences
#   C-SSRS yes/no v4 -> replies/cssrs-yesno-v4/  500 users
# Skips a model that already has a complete file for that prompt.
# Waits for bash_scripts/run_si_yesno_v2_pilot.sh to exit. Does not stop
# a vLLM server that is already generating.
# One local RTX. Load one model, run one task, then SIGTERM the server.
# Do not SIGKILL. Ignores SIGHUP.
set -uo pipefail
trap '' HUP

MH_ROOT=/home/mkalinich/main
SI_PY="$MH_ROOT/.venv/bin/python"
VLLM_PY=/home/mkalinich/phone-data-video-extraction/.venv-vllm/bin/python
VLLM_ROOT=/home/mkalinich/phone-data-video-extraction
PORT=8000
BASE_URL="http://127.0.0.1:${PORT}/v1"
MAX_CONCURRENT=128
REPAIRS="$MH_ROOT/config/serving_repairs.csv"
SI_PROMPT="$MH_ROOT/data/prompts/suicide_ideation_yesno_v2.txt"
SI_PREFIX=$(tr -d '\n' < "$MH_ROOT/data/prompts/suicide_ideation_yesno_v2_prefix.txt")
SI_SUFFIX=$(tr -d '\n' < "$MH_ROOT/data/prompts/suicide_ideation_yesno_v2_suffix.txt")
SI_INPUT="$MH_ROOT/data/inputs/finalized_input_data/SI_finalized_sentences.csv"
SI_OUT="$MH_ROOT/replies/si-yesno-v2"
CSSRS_PROMPT="$MH_ROOT/data/prompts/cssrs_yesno_v4.txt"
CSSRS_PREFIX=$(tr -d '\n' < "$MH_ROOT/data/prompts/cssrs_yesno_v4_prefix.txt")
CSSRS_SUFFIX=$(tr -d '\n' < "$MH_ROOT/data/prompts/cssrs_yesno_v4_suffix.txt")
CSSRS_OUT="$MH_ROOT/replies/cssrs-yesno-v4"
STAMP=$(date +%Y%m%d_%H%M%S)
RUN_DIR="$MH_ROOT/replies/yesno-full-rtx-${STAMP}"
mkdir -p "$RUN_DIR"
printf 'hf_id\tstatus\tdetail\n' > "$RUN_DIR/status.tsv"
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

echo "Waiting for the six-model synthetic-SI pilot to exit. This script will not stop it."
while pgrep -f 'run_si_yesno_v2_pilot.sh' >/dev/null; do
  echo "$(date -Is) pilot still running"
  sleep 30
done
echo "$(date -Is) pilot script is gone"
for _ in $(seq 1 40); do
  if ! pgrep -f 'vllm.entrypoints.openai.api_server' >/dev/null; then
    break
  fi
  echo "$(date -Is) waiting for the pilot vLLM to exit"
  sleep 5
done
if pgrep -f 'vllm.entrypoints.openai.api_server' >/dev/null; then
  echo "A vLLM server is still running after the pilot. Not starting another, and not sending SIGKILL."
  exit 1
fi

write_plan() {
  local mode="$1" out_root="$2" plan_file="$3"
  if ! (
    cd "$MH_ROOT" && "$SI_PY" - "$mode" "$REPAIRS" "$out_root" << 'PY'
import csv, json, os, sys
from pathlib import Path
mode, repairs_path, out_root = sys.argv[1:]
from orchestration.plot_parse_rates import canonical_weight_id, load_cohorts
from safety_labels.cohort import USABLE_IDS

HF = Path("/home/mkalinich/hf_models")
cohorts = load_cohorts()
usable = frozenset(USABLE_IDS)
kept = [row for row in cohorts["safety"] if row["hf_id"] in usable]
if len(kept) != 9:
    raise SystemExit(f"safety heatmap list is {len(kept)}, expected 9")
cohorts["safety"] = kept
ids = []
seen = set()
role = {}
for grouping, rows in cohorts.items():
    for row in rows:
        parent = canonical_weight_id(row["parent"])
        for hf, kind in ((parent, "parent"), (row["hf_id"], grouping)):
            if hf in seen:
                continue
            seen.add(hf)
            ids.append(hf)
            role[hf] = kind
counts = {}
for kind in role.values():
    counts[kind] = counts.get(kind, 0) + 1
if len(ids) != 75 or counts.get("mental-health") != 22 or counts.get("safety") != 9 or counts.get("medical") != 24 or counts.get("parent") != 20:
    raise SystemExit(f"heatmap cohort {len(ids)} {counts}, expected 75 with 20/22/9/24")
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

def done(hf):
    if mode == "si":
        path = Path(out_root) / safe(hf) / "suicidal_ideation_summary.json"
        if not path.is_file():
            return False
        data = json.loads(path.read_text())
        return (
            "suicide_ideation_yesno_v2" in data.get("experiment_id", "")
            and data.get("status") == "completed"
            and data.get("total_results") == 450
        )
    path = Path(out_root) / safe(hf) / "metrics.json"
    if not path.is_file():
        return False
    data = json.loads(path.read_text())
    metrics = data.get("metrics") or {}
    return (
        str(data.get("prompt", "")).endswith("cssrs_yesno_v4.txt")
        and metrics.get("n") == 500
        and bool(data.get("user_prefix"))
        and bool(data.get("user_suffix"))
    )

lines = ["hf_id\trole\tbytes"]
planned = []
for hf in ids:
    nbytes = ready_bytes(hf)
    lines.append("\t".join([hf, role[hf], "" if nbytes is None else str(nbytes)]))
    if nbytes is None:
        print(f"MISSING {hf}", file=sys.stderr)
        continue
    if done(hf):
        print(f"skip {hf} already complete", file=sys.stderr)
        continue
    src = repairs.get(hf, {}).get("tokenizer_from", "")
    tok = str(HF / safe(src)) if src else ""
    family = "qwen" if "qwen" in hf.lower() else "other"
    seqs = 8 if nbytes > 45 * (1024 ** 3) else 128
    planned.append((nbytes, hf, safe(hf), family, str(maxlen_of(hf, nbytes)), str(seqs), tok))
cohort = Path(out_root) / "cohort.tsv"
cohort.parent.mkdir(parents=True, exist_ok=True)
cohort.write_text("\n".join(lines) + "\n", encoding="utf-8")
if len(lines) - 1 != 75:
    raise SystemExit(f"cohort.tsv has {len(lines) - 1} models")
planned.sort(key=lambda row: (row[0], row[1].lower()))
for row in planned:
    print("|".join(row[1:]))
print(f"queue_models={len(planned)}", file=sys.stderr)
PY
  ) > "$plan_file"; then
    echo "Serve plan failed for $mode"
    return 1
  fi
}

serve_plan() {
  local mode="$1" plan_file="$2"
  mapfile -t PLAN < "$plan_file"
  if [[ ${#PLAN[@]} -eq 0 ]]; then
    echo "No models left for $mode"
    return 0
  fi
  local line hf_id dirname family maxlen seqs tokenizer_dir log model_path
  for line in "${PLAN[@]}"; do
    [[ -z "$line" ]] && continue
    IFS='|' read -r hf_id dirname family maxlen seqs tokenizer_dir <<<"$line"
    log="$RUN_DIR/${mode}-${dirname}.vllm.log"
    model_path="/home/mkalinich/hf_models/${dirname}"
    local tok_args=()
    if [[ -n "$tokenizer_dir" ]]; then
      if [[ ! -f "$tokenizer_dir/tokenizer_config.json" ]]; then
        record "$hf_id" "skip" "$mode repair tokenizer dir missing: $tokenizer_dir"
        continue
      fi
      tok_args=(--tokenizer "$tokenizer_dir")
      record "$hf_id" "repair" "$mode tokenizer_from=$(basename "$tokenizer_dir")"
    fi
    echo "---- $mode serve $hf_id len=$maxlen seqs=$seqs ----"
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
      record "$hf_id" "fail" "$mode vLLM did not become ready"
      stop_vllm || exit 1
      continue
    fi
    local ok=0
    if [[ "$mode" == "si" ]]; then
      if (
        cd "$MH_ROOT" && "$SI_PY" -u -m orchestration.run_experiment \
          --experiment-name "si_v2_${dirname}" \
          --model-family "$family" \
          --model-size "$dirname" \
          --model-version 20261017v2 \
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
        ok=1
      fi
    else
      if (
        cd "$MH_ROOT" && "$SI_PY" -u -m orchestration.run_cssrs_yesno \
          --base-url "$BASE_URL" \
          --model-name "$hf_id" \
          --model-family "$family" \
          --model-size "$dirname" \
          --model-version 20261017v4 \
          --system "$CSSRS_PROMPT" \
          --user-prefix "$CSSRS_PREFIX" \
          --user-suffix "$CSSRS_SUFFIX" \
          --output-dir "$CSSRS_OUT/${dirname}" \
          --temperature 0 \
          --max-tokens 256 \
          --max-concurrent "$MAX_CONCURRENT"
      ); then
        ok=1
      fi
    fi
    if [[ "$ok" -eq 1 ]]; then
      record "$hf_id" "ok" "$mode exit 0"
    else
      record "$hf_id" "fail" "$mode run exit $?"
    fi
    stop_vllm || exit 1
  done
}

SI_PLAN="$RUN_DIR/si-plan.txt"
CSSRS_PLAN="$RUN_DIR/cssrs-plan.txt"
write_plan si "$SI_OUT" "$SI_PLAN" || exit 1
echo "---- synthetic SI v2 ----"
serve_plan si "$SI_PLAN"
write_plan cssrs "$CSSRS_OUT" "$CSSRS_PLAN" || exit 1
echo "---- C-SSRS yes/no v4 ----"
serve_plan cssrs "$CSSRS_PLAN"
echo "RUN_DIR=$RUN_DIR"
echo "full queue finished"
