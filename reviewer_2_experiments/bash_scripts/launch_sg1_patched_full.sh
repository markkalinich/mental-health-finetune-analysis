#!/usr/bin/env bash
# Detached SG-1 patched sensitivity: SI+TR+TE × 2b/9b/27b full datasets.
set -euo pipefail
R2="$(cd "$(dirname "$0")/.." && pwd)"
ROOT="$(cd "$R2/.." && pwd)"
OUT="$R2/cache/shieldgemma_sg1_patched"
LOG="$R2/logs/shieldgemma_sg1_patched/full_run_$(date +%Y%m%d_%H%M%S).log"
PIDFILE="$OUT/full_run.pid"

mkdir -p "$R2/logs/shieldgemma_sg1_patched" "$OUT"

nohup "$ROOT/.venv/bin/python" -u "$R2/scripts/run_shieldgemma_sg1_patched_sensitivity.py" \
  --full \
  --task all \
  >>"$LOG" 2>&1 &

echo $! >"$PIDFILE"
echo "Started SG-1 patched full run (PID $(cat "$PIDFILE"))"
echo "Log: $LOG"
echo "Manifest: $OUT/run_manifest.json"
echo "Cache: $OUT/cache/results.db"
echo "Golden backups: $R2/data/template_backups/sg1_patched_sensitivity_backups/"
