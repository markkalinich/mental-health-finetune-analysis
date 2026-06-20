#!/usr/bin/env bash
# Launch detached provenance verification jobs (override scan + HF template compare).
# Reports land under reviewer_2_experiments/logs/verify_<timestamp>/.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
R2="$ROOT/reviewer_2_experiments"
PY="$ROOT/.venv/bin/python"
TS="$(date -u +%Y%m%dT%H%M%SZ)"
OUTDIR="$R2/logs/verify_${TS}"
mkdir -p "$OUTDIR"

COMMITTED_OVERRIDE="$R2/data/provenance/all_models_lmstudio_jinja_overrides.json"
COMMITTED_TEMPLATE="$R2/data/provenance/hf_template_compare/q8_vs_smaller_quant_template_compare.json"

echo "verify jobs -> $OUTDIR"

nohup "$PY" "$R2/scripts/run_lmstudio_jinja_override_scan.py" \
  --compare-to "$COMMITTED_OVERRIDE" \
  --report "$OUTDIR/override_scan_report.json" \
  > "$OUTDIR/override_scan.log" 2>&1 &
PID1=$!
echo "$PID1" > "$OUTDIR/override_scan.pid"

nohup "$PY" "$R2/scripts/run_q8_orphan_template_compare.py" \
  --compare-to "$COMMITTED_TEMPLATE" \
  --report "$OUTDIR/template_compare_report.json" \
  > "$OUTDIR/template_compare.log" 2>&1 &
PID2=$!
echo "$PID2" > "$OUTDIR/template_compare.pid"

cat > "$OUTDIR/README.txt" <<EOF
Detached provenance verification (${TS} UTC)

Jobs:
  override scan:     PID ${PID1}  log: override_scan.log     report: override_scan_report.json
  template compare:  PID ${PID2}  log: template_compare.log  report: template_compare_report.json

Tail logs:
  tail -f $OUTDIR/override_scan.log
  tail -f $OUTDIR/template_compare.log

Check exit / reports:
  wait ${PID1} && echo override OK || echo override FAIL
  wait ${PID2} && echo template OK || echo template FAIL
  jq .ok $OUTDIR/override_scan_report.json $OUTDIR/template_compare_report.json
EOF

echo "Started override scan PID $PID1"
echo "Started template compare PID $PID2"
echo "Monitor: $OUTDIR"
