#!/usr/bin/env bash
# Record of the 14 Oct 2026 medical GPU run. It reads outputs/cross-grouping/2026-10-14/final_models.csv, rewritten on 15 and 16 Oct, so its pin of 29 no longer matches and a rerun stops.
# The 29 medical fine-tunes that share a family, version, and size cell with a
# mental-health fine-tune in outputs/cross-grouping/2026-10-14/final_models.csv.
# One local RTX. Load one model, run every benchmark below, then SIGTERM the
# server. Do not SIGKILL. Ignores SIGHUP so a closed shell does not stop it.
# Exits if a vLLM server is already running. Does not stop that server.
#
# Benchmarks, study prompts, temperature 0:
#   suicidal ideation yes/no   data/prompts/suicide_ideation_yesno_v1.txt          450  max_tokens 256
#   suicidal ideation JSON     data/prompts/system_suicide_detection_v2.txt        450  max_tokens 256
#   C-SSRS                     data/prompts/cssrs_severity_v1.txt                  500  max_tokens 256
#   CBT-Bench qa, cd, pc, fc   orchestration/run_cbt_bench.py                      220, 146, 184, 112  max_tokens 2048
#   AnnoMI therapist, client, session                                            4882, 4817, 133  max_tokens 256
#   MentalHealthBench         1,215 items, one sample                             max_tokens 2048
#
# Cache identity for the sentence tasks and MentalHealthBench: --model-size is
# the weights directory name, --model-version is 20261007. Qwen 3 and Qwen 3.5
# send enable_thinking false, including when only config.json model_type says so.
set -uo pipefail
trap '' HUP

MH_ROOT=/home/mkalinich/main
# ONLY_HF is the pretrained-model queue. That queue stays off this GPU until
# the chat-template check is finished. Remove the hold file to let it run.
if [[ -n "${ONLY_HF:-}" && -f "$MH_ROOT/replies/hold-pretrain-gpu" ]]; then
  echo "Pretrained GPU generation is held ($MH_ROOT/replies/hold-pretrain-gpu)."
  exit 0
fi
SI_PY="$MH_ROOT/.venv/bin/python"
VLLM_PY=/home/mkalinich/phone-data-video-extraction/.venv-vllm/bin/python
VLLM_ROOT=/home/mkalinich/phone-data-video-extraction
BENCH=/home/mkalinich/local_benchmarks
PORT=8000
BASE_URL="http://127.0.0.1:${PORT}/v1"
LIMIT="${LIMIT:-0}"
MAX_CONCURRENT=128
# ONLY_HF is a comma-separated list of models to serve instead of the 29.
# Used for parents that have no results yet. Those results go under
# replies/medical-parents so the 29-model cohort file is left as it is.
if [[ -n "${ONLY_HF:-}" ]]; then
  OUT_NAME=medical-parents
else
  OUT_NAME=medical-30
fi
FINAL="$MH_ROOT/outputs/cross-grouping/2026-10-14/final_models.csv"
REPAIRS="$MH_ROOT/config/serving_repairs.csv"
MHB_DATA="$BENCH/mentalhealthbench/mentalhealthbench/mentalhealthbench_eval.jsonl"
OUT="$MH_ROOT/replies/${OUT_NAME}"
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

run_one() {
  local hf_id="$1" task="$2" family="$3" size="$4" version="$5"
  local safe="${hf_id//\//__}"
  case "$task" in
    suicidal_ideation)
      ( cd "$MH_ROOT" && "$SI_PY" -u -m orchestration.run_experiment \
        --experiment-name "si_${safe}" \
        --model-family "$family" --model-size "$size" --model-version "$version" \
        --model-name "$hf_id" \
        --prompt-name suicide_ideation_yesno_v1 \
        --input "$MH_ROOT/data/inputs/finalized_input_data/SI_finalized_sentences.csv" \
        --system "$MH_ROOT/data/prompts/suicide_ideation_yesno_v1.txt" \
        --base-url "$BASE_URL" --base-dir "$MH_ROOT" \
        --temperature 0 --max-tokens 256 \
        --max-concurrent "$MAX_CONCURRENT" --limit "$LIMIT" --retry-errors \
        --output-summary "$OUT/${safe}/suicidal_ideation_summary.json" )
      ;;
    suicidal_ideation_json)
      ( cd "$MH_ROOT" && "$SI_PY" -u -m orchestration.run_experiment \
        --experiment-name "si_json_${safe}" \
        --model-family "$family" --model-size "$size" --model-version "$version" \
        --model-name "$hf_id" \
        --prompt-name system_suicide_detection_v2 \
        --input "$MH_ROOT/data/inputs/finalized_input_data/SI_finalized_sentences.csv" \
        --system "$MH_ROOT/data/prompts/system_suicide_detection_v2.txt" \
        --base-url "$BASE_URL" --base-dir "$MH_ROOT" \
        --temperature 0 --max-tokens 256 \
        --max-concurrent "$MAX_CONCURRENT" --limit "$LIMIT" --retry-errors \
        --output-summary "$OUT/${safe}/suicidal_ideation_json_summary.json" )
      ;;
    cssrs)
      ( cd "$MH_ROOT" && "$SI_PY" -u -m orchestration.run_cssrs_bench \
        --input "$BENCH/reddit_cssrs/prepared/standard_user_level.csv" \
        --system "$MH_ROOT/data/prompts/cssrs_severity_v1.txt" \
        --base-url "$BASE_URL" --model-name "$hf_id" --model-family "$family" \
        --model-size "$size" --model-version "$version" \
        --output-dir "$MH_ROOT/replies/cssrs/${safe}" \
        --temperature 0 --max-tokens 256 \
        --max-concurrent "$MAX_CONCURRENT" --limit "$LIMIT" )
      ;;
    cbt_qa|cbt_cd|cbt_pc|cbt_fc)
      ( cd "$MH_ROOT" && "$SI_PY" -u -m orchestration.run_cbt_bench \
        --tasks "${task#cbt_}" \
        --data-dir "$BENCH/cbt_bench" \
        --base-url "$BASE_URL" --model-name "$hf_id" --model-family "$family" \
        --output-dir "$MH_ROOT/replies/cbt_bench/${safe}" \
        --temperature 0 --max-tokens 2048 \
        --max-concurrent "$MAX_CONCURRENT" \
        --allow-unscored-qa \
        --limit "$LIMIT" )
      ;;
    annomi_therapist)
      ( cd "$MH_ROOT" && "$SI_PY" -u -m orchestration.run_annomi_bench \
        --task therapist \
        --input "$BENCH/annomi/prepared/standard_therapist.csv" \
        --system "$MH_ROOT/data/prompts/annomi_therapist_behaviour_v1.txt" \
        --base-url "$BASE_URL" --model-name "$hf_id" --model-family "$family" \
        --output-dir "$MH_ROOT/replies/annomi/${safe}/therapist" \
        --temperature 0 --max-tokens 256 \
        --max-concurrent "$MAX_CONCURRENT" --limit "$LIMIT" )
      ;;
    annomi_client)
      ( cd "$MH_ROOT" && "$SI_PY" -u -m orchestration.run_annomi_bench \
        --task client \
        --input "$BENCH/annomi/prepared/standard_client.csv" \
        --system "$MH_ROOT/data/prompts/annomi_client_talk_v1.txt" \
        --base-url "$BASE_URL" --model-name "$hf_id" --model-family "$family" \
        --output-dir "$MH_ROOT/replies/annomi/${safe}/client" \
        --temperature 0 --max-tokens 256 \
        --max-concurrent "$MAX_CONCURRENT" --limit "$LIMIT" )
      ;;
    annomi_session)
      ( cd "$MH_ROOT" && "$SI_PY" -u -m orchestration.run_annomi_bench \
        --task session \
        --input "$BENCH/annomi/prepared/standard_session.csv" \
        --system "$MH_ROOT/data/prompts/annomi_session_quality_v1.txt" \
        --base-url "$BASE_URL" --model-name "$hf_id" --model-family "$family" \
        --output-dir "$MH_ROOT/replies/annomi/${safe}/session" \
        --temperature 0 --max-tokens 256 \
        --max-concurrent "$MAX_CONCURRENT" --limit "$LIMIT" )
      ;;
    mhb)
      ( cd "$MH_ROOT" && "$SI_PY" -u -m orchestration.run_mentalhealthbench \
        --base-url "$BASE_URL" --model-name "$hf_id" --model-family "$family" \
        --model-size "$size" --model-version "$version" \
        --data "$MHB_DATA" \
        --output-dir "$MH_ROOT/replies/mentalhealthbench-1215-temp0/${safe}" \
        --samples 1 --temperature 0 --max-tokens 2048 \
        --max-concurrent "$MAX_CONCURRENT" )
      ;;
    *)
      echo "unknown task $task" >&2
      return 1
      ;;
  esac
}

PLAN_FILE="$RUN_DIR/plan.txt"
if ! (
  cd "$MH_ROOT" && "$SI_PY" - "$FINAL" "$REPAIRS" "$OUT" "$MH_ROOT" << 'PY'
import csv, json, os, sys
from pathlib import Path
final_path, repairs_path, out_root, repo = sys.argv[1:]
HF = Path("/home/mkalinich/hf_models")
MHB = Path(repo) / "replies/mentalhealthbench-1215-temp0"
rows = list(csv.DictReader(open(final_path, newline="")))
cells = {}
for row in rows:
    cells.setdefault((row["family"], row["version"], row["size"]), []).append(row)
med = []
for group in cells.values():
    if any(r["grouping"] == "mental-health" for r in group):
        med.extend(r for r in group if r["grouping"] == "medical")
only = [x.strip() for x in os.environ.get("ONLY_HF", "").split(",") if x.strip()]
if only:
    by_id = {r["hf_id"]: r for r in rows}
    med = []
    for hf in only:
        src = by_id.get(hf)
        if src:
            med.append(src)
        else:
            med.append({"hf_id": hf, "parent": hf, "family": "", "version": "", "size": ""})
elif len(med) != 29:
    raise SystemExit(f"expected 29 medical models in a mental-health cell, found {len(med)}")
repairs = {}
if Path(repairs_path).is_file():
    repairs = {r["hf_id"]: r for r in csv.DictReader(open(repairs_path, newline=""))}

def safe(hf):
    return hf.replace("/", "__")

def load(path):
    if not path.is_file():
        return None
    return json.loads(path.read_text())

def si_done(path):
    data = load(path)
    return bool(data) and data.get("status") == "completed" and data.get("input_samples") == 450 and data.get("errors") == 0

def metrics_n(path, n):
    data = load(path)
    if not data:
        return False
    metrics = data.get("metrics") or {}
    return metrics.get("n") == n

def cbt_done(path, n):
    data = load(path)
    return bool(data) and data.get("n_items") == n and data.get("expected_n") == n

def mhb_done(hf):
    data = load(MHB / safe(hf) / "summary.json")
    return bool(data) and data.get("n_items") == 1215 and data.get("n_samples") == 1 and data.get("n_api_errors") == 0

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

CBT_N = {"cbt_qa": 220, "cbt_cd": 146, "cbt_pc": 184, "cbt_fc": 112}
ANNOMI_N = {"annomi_therapist": 4882, "annomi_client": 4817, "annomi_session": 133}
cohort_path = Path(out_root) / "cohort.tsv"
lines = ["hf_id\tparent\tfamily\tversion\tsize\tbytes"]
planned = []
for row in med:
    hf = row["hf_id"]
    nbytes = ready_bytes(hf)
    lines.append("\t".join([hf, row["parent"], row["family"], row["version"], row["size"], "" if nbytes is None else str(nbytes)]))
    if nbytes is None:
        print(f"skip {hf} weights missing", file=sys.stderr)
        continue
    length = maxlen_of(hf, nbytes)
    base = Path(out_root) / safe(hf)
    missing = []
    if not si_done(base / "suicidal_ideation_summary.json"):
        missing.append("suicidal_ideation")
    if not si_done(base / "suicidal_ideation_json_summary.json"):
        missing.append("suicidal_ideation_json")
    if not metrics_n(Path(repo) / "replies/cssrs" / safe(hf) / "metrics.json", 500):
        missing.append("cssrs")
    for task, n in CBT_N.items():
        key = task.replace("cbt_", "")
        if length < 4096:
            print(f"skip {hf} {task}: context {length} too short for CBT", file=sys.stderr)
            continue
        if not cbt_done(Path(repo) / "replies/cbt_bench" / safe(hf) / key / "metrics.json", n):
            missing.append(task)
    for task, n in ANNOMI_N.items():
        kind = task.replace("annomi_", "")
        if not metrics_n(Path(repo) / "replies/annomi" / safe(hf) / kind / "metrics.json", n):
            missing.append(task)
    if not mhb_done(hf):
        missing.append("mhb")
    if not missing:
        print(f"skip {hf} already complete", file=sys.stderr)
        continue
    src = repairs.get(hf, {}).get("tokenizer_from", "")
    tok = str(HF / safe(src)) if src else ""
    family = "qwen" if ("qwen" in hf.lower() or "qwen" in row["parent"].lower()) else "other"
    seqs = 8 if nbytes > 45 * (1024 ** 3) else 128
    planned.append((nbytes, hf, safe(hf), family, str(length), ",".join(missing), str(seqs), tok))
cohort_path.parent.mkdir(parents=True, exist_ok=True)
cohort_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
planned.sort(key=lambda r: (r[0], r[1].lower()))
for row in planned:
    print("|".join(row[1:]))
print(f"queue_models={len(planned)}", file=sys.stderr)
PY
) > "$PLAN_FILE"; then
  echo "Serve plan failed."
  exit 1
fi
mapfile -t PLAN < "$PLAN_FILE"

if [[ ${#PLAN[@]} -eq 0 ]]; then
  echo "No models in the serve plan."
  exit 0
fi

for line in "${PLAN[@]}"; do
  IFS='|' read -r hf_id dirname family maxlen tasks seqs tokenizer_dir <<<"$line"
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
    record "$hf_id" "repair" "tokenizer_from=$(basename "$tokenizer_dir")"
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
    "${tok_args[@]}" \
    > "$log" 2>&1 &
  VLLM_PID=$!
  echo "vLLM pid $VLLM_PID log $log"
  if ! wait_ready "$hf_id"; then
    record "$hf_id" "fail" "vLLM did not become ready"
    stop_vllm || exit 1
    continue
  fi
  IFS=',' read -r -a task_list <<<"$tasks"
  for task in "${task_list[@]}"; do
    if run_one "$hf_id" "$task" "$family" "$dirname" "20261007"; then
      record "$hf_id" "ok" "$task exit 0"
    else
      record "$hf_id" "fail" "$task exit $?"
    fi
    if ! kill -0 "$VLLM_PID" 2>/dev/null; then
      record "$hf_id" "fail" "vLLM exited during $task"
      VLLM_PID=""
      break
    fi
  done
  stop_vllm || exit 1
done

echo "RUN_DIR=$RUN_DIR"
