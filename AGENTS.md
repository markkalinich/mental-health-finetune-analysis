# Agent instructions (short)

Read this file **before** doing substantive work in this repo.

Before running Python in this repository:

1. **Use the project venv** — Activate `.venv` or invoke `.venv/bin/python` explicitly. Do not use an unqualified `python` unless you have verified `which python` points inside `.venv/`.
2. **Verify file equality with checksums** — Use `sha256sum` or `cmp`; do not infer identity from file size.
3. **Details** — See [`docs/DEVELOPMENT.md`](docs/DEVELOPMENT.md) (venv, integrity checks, Git workflow for private vs public remotes, planned data-flow refactor notes).
4. **Docs marked verbose** — Search: `rg 'doc-verbosity:' --glob '*.md'` — see [`docs/DOCUMENTATION_FLAGS.md`](docs/DOCUMENTATION_FLAGS.md). Files with `verbose-troubleshooting` should be trimmed before a public release.

## Strict data / validation (default for cache, registry, and QC)

When the user (or code) defines a **single source of truth** (e.g. `config/models_config.csv` vs `cache_keys`):

- **Canonical join:** `utilities/cache_qc_report.py` maps cache rows using **`(model_family, model_size, normalized model_version)`** → enabled `lm_studio_id` (same as `experiment_manager` / `MODEL_NAME_MAP`). **Label drift** is fixed only via **explicit, human-approved** rows in **`model_cache_crosswalk_approved.csv`** (`model_full_name` → `lm_studio_id`), not by guessing.
- **No alternate matching** unless the user explicitly asks for it — no substring heuristics on model names, no silent `(family, size)` fallback if the spec disallows it.
- **Fail loud:** on mismatch, **exit non-zero**, print a **clear error to stderr**, and list **all** offending values. Do not catch-and-continue or add “best effort” paths that hide inconsistency.
- **If the requirement is ambiguous, ask** — do not guess a fallback to make the script pass.
- **Definition of done:** the pipeline passes strict checks, or the agent stops and reports what must change on the data/config side.

`utilities/cache_qc_report.py` follows these rules; align the DB and CSV instead of weakening checks.
