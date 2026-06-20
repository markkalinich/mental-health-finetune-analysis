#!/usr/bin/env bash
# Audit all REVIEWER_2_EXPERIMENTS.md claims (artifact + live checks).
# From repo root:
#   reviewer_2_experiments/bash_scripts/audit_all_claims.sh
# Artifact-only (no LM Studio index / HF network):
#   reviewer_2_experiments/bash_scripts/audit_all_claims.sh --skip-live
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
exec "$ROOT/.venv/bin/python" "$ROOT/reviewer_2_experiments/scripts/audit_all_claims.py" "$@"
