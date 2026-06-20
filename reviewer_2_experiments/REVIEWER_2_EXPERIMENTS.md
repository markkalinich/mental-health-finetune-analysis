# Reviewer #2 experiments — claims and evidence

Walkthrough of each rebuttal claim with the exact code and data that backs it.

**Scope:** 127 enabled models in `config/models_config.csv`; safety-model deep-dive on **9** models (4 ShieldGemma, 2 Llama Guard, 3 Qwen Guard).

---

## How to read a section

Each section has:

1. **Claim** — language we use (or intend to use) in the rebuttal / Methods.
2. **Evidence** — committed artifacts (paths below are under `reviewer_2_experiments/` unless noted).
3. **Code** — scripts or pipeline modules that produce or consume the evidence.
4. **Reproduce** — one-liner to regenerate (read-only where possible).

---

## Verify all claims (one-liner)

From the **repository root** (uses `.venv`; live checks need LM Studio index + HF network):

```bash
reviewer_2_experiments/bash_scripts/audit_all_claims.sh
```

Artifact-only (no live LM Studio / HF calls):

```bash
reviewer_2_experiments/bash_scripts/audit_all_claims.sh --skip-live
```

Equivalent:

```bash
.venv/bin/python reviewer_2_experiments/scripts/audit_all_claims.py
```

Checks: Claim 1–6 artifacts; four-model ShieldGemma break JSON; full guard pipeline via `cache/results.db`; Table S2 **14→10** Bonferroni diff (parse≥50%); Figure 3 **9→4** + pair-level sign check; Safety/Qwen TR+TE negative ΔF1. Live checks (override scan, HF template) run only without `--skip-live`.

---

## Prerequisites (reviewer machine)

| Requirement | Needed for | If missing |
|-------------|------------|------------|
| **`.venv`** at repo root | All Python scripts | `python -m venv .venv && pip install -r requirements.txt` |
| **`cache/results.db`** (~312 MB subset) | **Claim 5 only**; optional for Claim 3 generic (paper) arm | Symlink or copy from [`manuscript_paper_cache/results.db`](../manuscript_paper_cache/results.db); verify with [`manuscript_paper_cache/SHA256SUMS.txt`](../manuscript_paper_cache/SHA256SUMS.txt). **Not in git** (see [`manuscript_paper_cache/README.md`](../manuscript_paper_cache/README.md)). |
| **`data/inputs/model_results/all_models_all_tasks.csv`** | Claim 6 primary comparison | Committed in repo |
| **Network** | Claim 1 live Q8 template compare only | Use `--skip-live` (default for reviewers) |
| **LM Studio + 127-model index** | Live audit, optional break-test **re-runs** | Use `--skip-live`; inspect committed break-test JSON instead |
| **Local GGUF files** | Regenerating Claim 1 full SHA256 audit only | Inspect committed `all_models_gguf_sha256_audit.json` instead |

### What runs without `cache/results.db`

| Claim | Artifact-only verify (`--skip-live`) | Notes |
|-------|-----------------------------------|--------|
| **1** | Yes | Committed SHA256 + Q8 template JSON |
| **2** | Yes | Committed override scan + off-disk embedded-template extraction (127) |
| **3** | Partial | Break-test JSON + **patched-arm** caches under `reviewer_2_experiments/cache/` are in git; **generic (paper) F1 arm** needs main `cache/results.db` to recompute Figure R1 |
| **4** | Yes | Committed break-test JSON |
| **5** | **No** | Audit loads guard rows from `cache/results.db` |
| **6** | Yes | Committed parse≥50% cohort CSV/JSON + Table S2 + Figures S11–S12 |

**Recommended first command** (Claims 1, 2, 4, 6 without LM Studio or local GGUFs; **skip Claim 5** if no cache):

```bash
reviewer_2_experiments/bash_scripts/audit_all_claims.sh --skip-live
```

With `cache/results.db` present, the same command also verifies Claim 5.


## Claim 1 — GGUF provenance: 123 / 3 / 1

### Claim

- **123/127** local GGUF files are **fully bitwise identical** to HuggingFace (`local SHA256` = HF `x-linked-etag` from HEAD).
- **3/127** could not be full-file verified (Q8 quant unavailable on HF); for these, **embedded `tokenizer.chat_template` strings** from an **adjacent quant in the same HF repo** are **bitwise identical, SHA256 verified** (where a template exists).
- **1/127** we **cannot confirm** — HF repo no longer accessible (`therapist1-gemma3-12b-qvo`).

### Evidence

| Bucket | Count | Artifact |
|--------|------:|----------|
| Full file match | 123 | [`data/provenance/all_models_gguf_sha256_audit.json`](data/provenance/all_models_gguf_sha256_audit.json) — per-model `status: VERIFIED_match` |
| Template from adjacent quant | 3 | [`data/provenance/hf_template_compare/q8_vs_smaller_quant_template_compare.json`](data/provenance/hf_template_compare/q8_vs_smaller_quant_template_compare.json) |
| Unable to confirm | 1 | Same audit JSON — `therapist1-gemma3-12b-qvo` |

The three template-only models: `gemma-2-27b`, `klyang_mentallama-chat-13b`, `llama-3.1-8b-instruct-mental-health-classification`.

### Code

- [`scripts/run_gguf_sha256_audit.py`](scripts/run_gguf_sha256_audit.py) — hashes **entire local GGUF**; HF via HEAD `x-linked-etag` (no HF download).
- [`scripts/lm_studio_load_crosswalk.py`](scripts/lm_studio_load_crosswalk.py) — CSV `lm_studio_id` → LM Studio index key.

### Reproduce

**Verify (recommended for reviewers)** — inspect committed artifacts + live cross-checks; does not overwrite JSON:

```bash
reviewer_2_experiments/bash_scripts/audit_all_claims.sh
```

**Regenerate full GGUF audit (optional, slow)** — re-hashes all 127 local GGUF files and re-fetches HuggingFace HEAD `x-linked-etag` for each model. Requires every enabled model on disk under `~/.lmstudio/models/` and network access; typically **1–3+ hours** depending on disk and HF latency. Use when refreshing provenance, not for a first-pass review.

```bash
.venv/bin/python reviewer_2_experiments/scripts/run_gguf_sha256_audit.py --full
# → data/provenance/all_models_gguf_sha256_audit.json
```

**Regenerate Q8-orphan template compare only** (3 models, ~15 s, network):

```bash
.venv/bin/python reviewer_2_experiments/scripts/run_q8_orphan_template_compare.py \
  --compare-to reviewer_2_experiments/data/provenance/hf_template_compare/q8_vs_smaller_quant_template_compare.json
```

(No flags on `run_gguf_sha256_audit.py`: merge re-audit of five previously fixable skips only.)

---

## Claim 2 — Template provenance: 122 embedded/default, 5 overrides

### Claim

- **122/127** models ran with **publisher embedded** `tokenizer.chat_template` or LM Studio’s documented fallback when the GGUF has no template.
- **5/127** had a **Jinja override** installed in LM Studio because the embedded template could not render under our OpenAI-compatible `{system, user}` API.
- Which template applies per model is established from disk-level evidence plus LM Studio's documented precedence (installed override → GGUF-embedded `tokenizer.chat_template` → host default): the override scan (5 installed Jinja overrides), GGUF template-field presence (90 embedded vs 32 absent among the 122 non-override models), and break tests showing which embedded templates fail under the `{system, user}` API.

### The five overrides

| `lm_studio_id` | Why |
|----------------|-----|
| `shieldgemma-2b`, `shieldgemma-9b`, `shieldgemma-27b`, `shieldgemma-2-4b-it` | Embedded SG-1/SG-2 expects `guideline` or iterable multimodal `content` — breaks under string API (§ Claim 3) |
| `meta-llama_-_llama-guard-3-1b` | Embedded multimodal template; `selectattr` on string `content` → HTTP 400 (§ Claim 4) |

`llama-guard-3-8b` runs **embedded, no override**.

### Evidence

| What | Artifact |
|------|----------|
| Override scan (127) | [`data/provenance/all_models_lmstudio_jinja_overrides.json`](data/provenance/all_models_lmstudio_jinja_overrides.json) |
| Off-disk embedded chat templates (127) | [`data/provenance/all_models_gguf_embedded_templates.json`](data/provenance/all_models_gguf_embedded_templates.json) |
| ShieldGemma embedded break tests (4) | [`data/break_tests/shieldgemma_embedded_template_break_test.json`](data/break_tests/shieldgemma_embedded_template_break_test.json) |

### Code

- [`scripts/run_lmstudio_jinja_override_scan.py`](scripts/run_lmstudio_jinja_override_scan.py) — scan LM Studio override JSON for all 127 models (uses [`scripts/lm_studio_load_crosswalk.py`](scripts/lm_studio_load_crosswalk.py)).
- [`scripts/dump_gguf_embedded_templates.py`](scripts/dump_gguf_embedded_templates.py) — extract each GGUF's embedded `tokenizer.chat_template` off-disk (base64 + SHA256) for all 127.

### Reproduce

**Verify (recommended)** — read-only; checks committed JSON + live LM Studio index (seconds):

```bash
.venv/bin/python reviewer_2_experiments/scripts/run_lmstudio_jinja_override_scan.py \
  --compare-to reviewer_2_experiments/data/provenance/all_models_lmstudio_jinja_overrides.json
```

Full audit also covers Claim 2 artifact counts:

```bash
reviewer_2_experiments/bash_scripts/audit_all_claims.sh --skip-live
```

**Regenerate override scan** (writes JSON; needs LM Studio index):

```bash
.venv/bin/python reviewer_2_experiments/scripts/run_lmstudio_jinja_override_scan.py \
  --output reviewer_2_experiments/data/provenance/all_models_lmstudio_jinja_overrides.json
```

**Regenerate off-disk embedded templates** (reads local GGUF files; no LM Studio):

```bash
.venv/bin/python reviewer_2_experiments/scripts/dump_gguf_embedded_templates.py
# → data/provenance/all_models_gguf_embedded_templates.json
```

---

## Safety-model embedded templates (9 models) — where they live

**Yes — all nine safety models’ embedded GGUF templates are stored**, with override text when present:

| Storage | Contents |
|---------|----------|
| **[`data/provenance/subtask1_embedded_templates.json`](data/provenance/subtask1_embedded_templates.json)** | **Canonical** — full `embedded_chat_template` string per model, local GGUF path, SHA256 match flag, override Y/N + override template text |
| [`data/templates/llama_guard_3_1b_templates/`](data/templates/llama_guard_3_1b_templates/) | Verbatim `.jinja` files for 1B embedded vs override (SHA256 in README) |
| [`data/templates/shieldgemma_sg1_patched_guideline.jinja`](data/templates/shieldgemma_sg1_patched_guideline.jinja) | Patched SG-1 template used in sensitivity (not embedded) |
| [`data/templates/shieldgemma_sg2_patched_multimodal.jinja`](data/templates/shieldgemma_sg2_patched_multimodal.jinja) | Patched SG-2 template for 2-4b-it sensitivity |

**Nine models in `subtask1_embedded_templates.json`:**

1. `shieldgemma-2b`, `shieldgemma-9b`, `shieldgemma-27b`, `shieldgemma-2-4b-it`
2. `meta-llama_-_llama-guard-3-1b`, `llama-guard-3-8b`
3. `qwen3guard-gen-0.6b`, `qwen3guard-gen-4b`, `qwen3guard-gen-8b`

**Not** stored for all 127 in subtask 1 (safety models only); the full off-disk embedded-template extraction for all 127 is in [`data/provenance/all_models_gguf_embedded_templates.json`](data/provenance/all_models_gguf_embedded_templates.json). Template provenance comes from that off-disk extraction + the override scan.

### Code

- [`scripts/run_chat_template_audit.py`](scripts/run_chat_template_audit.py) — subtask 1 writes `data/provenance/subtask1_embedded_templates.json`.

---

## Claim 3 — ShieldGemma: embedded breaks, sensitivity, retain generic override, Figure R1

### Claim

- Forcing the **embedded** ShieldGemma Jinja under our `{system, user}` API **fails** (HTTP 400; `guideline` undefined or iterable-content error).
- We **substituted** the generic Gemma **LM-STUDIO-GEMMA** override so inference could run.
- **Sensitivity analysis:** re-ran models with **patched Google SG-1** (2b/9b/27b) and **patched SG-2** (2-4b-it), scoring Yes/No outputs; compared to paper runs under generic override.
- **Figure R1 (paired bars, generic vs patched F1 per model×task):** patching did **not** uniformly improve performance — **7 of 12** model×task comparisons were worse under the patched Google template (mean ΔF1 **−0.20**, median **−0.13**); we **retained** the generic override for all paper metrics.

### Evidence

| Step | Artifact |
|------|----------|
| Embedded breaks | [`data/break_tests/shieldgemma_embedded_template_break_test.json`](data/break_tests/shieldgemma_embedded_template_break_test.json) |
| SG-1 full patched run | [`cache/shieldgemma_sg1_patched/`](cache/shieldgemma_sg1_patched/) + [`results/shieldgemma/sg1_patched/`](results/shieldgemma/sg1_patched/) analysis JSON |
| SG-2 full patched run | [`cache/shieldgemma_24b_sg2/`](cache/shieldgemma_24b_sg2/) + [`results/shieldgemma/sg2_24b/`](results/shieldgemma/sg2_24b/) |
| **Figure R1** | [`results/shieldgemma/sg1_patched/figures/sg1_template_f1_paired_bars_by_task.png`](results/shieldgemma/sg1_patched/figures/sg1_template_f1_paired_bars_by_task.png) |
| Supporting figures | same `figures/` dir |
| Per-cell generic vs patched F1 | [`results/shieldgemma/sg1_patched/figures/sg1_template_f1_paired_bars_by_task.csv`](results/shieldgemma/sg1_patched/figures/sg1_template_f1_paired_bars_by_task.csv) |

### Code

| Step | Script |
|------|--------|
| Break test | [`scripts/run_embedded_template_break_test.py`](scripts/run_embedded_template_break_test.py) — **all four** ShieldGemma overrides (2b, 9b, 27b SG-1; 2-4b-it SG-2) |
| Patched SG-1 inference | [`scripts/run_shieldgemma_sg1_patched_sensitivity.py`](scripts/run_shieldgemma_sg1_patched_sensitivity.py) `--full` |
| Patched SG-2 inference | [`scripts/run_shieldgemma_24b_sg2_sensitivity.py`](scripts/run_shieldgemma_24b_sg2_sensitivity.py) `--full` |
| Compare generic vs patched F1 | [`scripts/analyze_sg1_patched_smoke_test.py`](scripts/analyze_sg1_patched_smoke_test.py) `--full --task all` |
| SG-2 analysis | [`scripts/analyze_shieldgemma_24b_sg2.py`](scripts/analyze_shieldgemma_24b_sg2.py) `--full --task all` |
| Figures (paired bars) | [`scripts/plot_sg1_template_delta_grid.py`](scripts/plot_sg1_template_delta_grid.py) |

**F1 arms:**

- **Generic (paper):** `cache/results.db` via `data_loader.load_experiment_results` — LM-STUDIO-GEMMA override.
- **Patched:** isolated caches under `cache/shieldgemma_sg1_patched/` and `cache/shieldgemma_24b_sg2/`.
- **Patched scoring:** Yes/No → task positive/negative (`analyze_sg1_patched_smoke_test.py`); **not** the same code path as guard re-parse in `data_loader.py`.

### Reproduce (read-only analysis + figures)

| **Live break test** (requires LM Studio on `localhost:1234`; overwrites `data/break_tests/shieldgemma_embedded_template_break_test.json`):

```bash
lms unload --all
.venv/bin/python reviewer_2_experiments/scripts/run_embedded_template_break_test.py
```

Expected per model: `baseline_generic_override` HTTP 200; `embedded_original_as_override` and `no_override_gguf_embedded` HTTP 400; `restore_match=True`.

**Verify without LM Studio:** `audit_all_claims.sh --skip-live` reads the committed break-test JSON (four models, HTTP outcomes, restore flags). Re-running the script is optional and requires LM Studio plus local GGUF/override files on the reviewer's machine.

**F1 sensitivity** (recomputed from cache DBs, not CSV):

```bash
.venv/bin/python reviewer_2_experiments/scripts/analyze_sg1_patched_smoke_test.py --full --task all
.venv/bin/python reviewer_2_experiments/scripts/analyze_shieldgemma_24b_sg2.py --full --task all
MPLBACKEND=Agg .venv/bin/python reviewer_2_experiments/scripts/plot_sg1_template_delta_grid.py
```

Generic arm loads from main `cache/results.db`; patched arms load from isolated caches under `reviewer_2_experiments/cache/`.

---

## Claim 4 — Llama Guard 3 1B override

### Claim

- Embedded 1B template expects **multimodal list `content`**; fails on our **string** API (HTTP **400**).
- We substituted a **text-only Guard-3-style** override (adapted from 8B embedded shape).
- `llama-guard-3-8b` ran **embedded** with **no** override in this study.

### Evidence

| Item | Path |
|------|------|
| Break test JSON | [`data/break_tests/llama_guard_3_1b_break_test.json`](data/break_tests/llama_guard_3_1b_break_test.json) |
| Template files + SHA256 | [`data/templates/llama_guard_3_1b_templates/`](data/templates/llama_guard_3_1b_templates/) |
| Embedded template in subtask1 | `subtask1_embedded_templates.json` → `meta-llama_-_llama-guard-3-1b` |
| 1B vs 1B-PT metrics | Main repo `data/inputs/model_results/all_models_all_tasks.csv` — `llama_guard` / `1b` vs `1b-pt` rows |

### Code

- [`scripts/run_llama_guard_1b_break_test.py`](scripts/run_llama_guard_1b_break_test.py) — backup override → three API modes → restore (SHA256 verified).

### Reproduce

**Live break test** (requires **LM Studio** on `localhost:1234`; re-runnable, overwrites JSON artifact):

```bash
lms unload --all
.venv/bin/python reviewer_2_experiments/scripts/run_llama_guard_1b_break_test.py
```

Expected: baseline HTTP 200 + `safe`/`unsafe`; embedded and no-override modes HTTP 400 with `selectattr` Jinja error; override file restored with matching SHA256.

**Verify without LM Studio:** same as Claim 3 — `--skip-live` audit checks committed JSON outcomes.

The `all_models_all_tasks.csv` row cited for 1B vs 1B-PT is **aggregated paper output** (derived from cache). The break test itself is a live LM Studio API check, not read from CSV.

---

## Claim 5 — Guard re-parse: Llama Guard and Qwen Guard mappings

**Requires cache:** Claim 5 verification needs the paper inference cache at **`cache/results.db`** (~313 MB; symlink or copy from [`manuscript_paper_cache/results.db`](../manuscript_paper_cache/results.db), not in git — see [Prerequisites](#prerequisites-reviewer-machine)). Without it, unit tests in the audit still run, but the full-pipeline check and worked examples below cannot be reproduced.

### Claim

- Guards output **plain-text moderation** (`safe`/`unsafe` or `Safety: Safe`/`Safety: Unsafe`), not task JSON.
- At inference, rows are `parse_fail` under JSON schema validation.
- At analysis, **Phase-2 re-parse** maps verdict → task **binary** label for metrics only.
- Applies to **`llama_guard` and `qwen_guard` families only** — not ShieldGemma.
- High parse after re-parse does **not** imply strong TR/TE sensitivity (guards often say “safe”).

### Code (paper pipeline)

[`analysis/model_performance/data_loader.py`](../analysis/model_performance/data_loader.py):

- `GUARD_FAMILIES = {"llama_guard", "qwen_guard"}`
- `_parse_guard_binary(raw_response)` — extract safe(0) / unsafe(1)
- `_reparse_guard_models(df, experiment_type)` — on `parse_fail` guard rows only
- `_GUARD_POSITIVE` / `_GUARD_NEGATIVE` — per-task field names and category values

**Per-task mapping (unsafe → positive, safe → negative):**

| Task | Prediction field | Positive (unsafe) | Negative (safe) |
|------|------------------|-------------------|-----------------|
| Suicidal ideation | `safety_type` | `passive_si` | `no_SI` |
| Therapy request | `therapy_request` | `explicit_therapy_request` | `declarative` |
| Therapy engagement | `therapy_engagement` | `simulated_therapy` | `non_therapeutic` |

### Parsing rules

**Llama Guard** (`_parse_guard_binary`):

- `content.lower() == "safe"` → 0  
- `content.lower().startswith("unsafe")` → 1  

**Qwen Guard:**

- First line starting with `Safety:` → `Safe` → 0, else → 1  

### Worked examples (from `cache/results.db`)

**Llama Guard 1B — therapy request (`therapy_request_classifier_v3`), safe:**

```
API content:  "\n\nsafe"
DB status:    parse_fail
_parse_guard_binary → 0 (safe)
Mapped field: therapy_request = declarative   # negative / non-request
```

**Llama Guard 1B — suicidal ideation (`system_suicide_detection_v2`), unsafe:**

```
API content:  "unsafe\nS11"
DB status:    parse_fail
_parse_guard_binary → 1 (unsafe)
Mapped field: safety_type = passive_si        # positive / SI class
```

**Qwen Guard 0.6B — therapy request (`therapy_request_classifier_v3`), safe:**

```
API content:  "Safety: Safe\nCategories: None"
DB status:    parse_fail
_parse_guard_binary → 0
Mapped field: therapy_request = declarative
```

**Qwen Guard 0.6B — suicidal ideation (`system_suicide_detection_v2`), unsafe:**

```
API content:  "Safety: Unsafe\nCategories: Suicide & Self-Harm"
DB status:    parse_fail
_parse_guard_binary → 1
Mapped field: safety_type = passive_si
```

After mapping, `status` becomes `ok` and `metrics_calculator` scores the row like any other model (binary F1 vs ground truth).

Empirical TR/TE pattern: Guard 1B **100% parse** after re-parse, **~0% TR/TE sensitivity** (guards overwhelmingly output “safe” on TR/TE prompts).

### Reproduce

Guard re-parse is in the paper pipeline ([`analysis/model_performance/data_loader.py`](../analysis/model_performance/data_loader.py)); there is no separate reviewer_2 runner. `_parse_guard_binary` takes a **full API JSON** `raw_response` string (not bare message text).

**Verify** (`audit_all_claims.py` runs unit cases, four DB examples, and **full `load_experiment_results` for all guard models × three tasks** from `cache/results.db`):

```bash
reviewer_2_experiments/bash_scripts/audit_all_claims.sh --skip-live
```

(Claim 5 checks are the `audit_claim5` block inside [`scripts/audit_all_claims.py`](scripts/audit_all_claims.py).)

---

## Claim 6 — Parse≥50% sensitivity: Table S2, Figure S11, Figure S12

### Claim

- Parse compliance is part of the evaluated capability; **Figure S10** (main repo) shows Δparse vs ΔF1 under fine-tuning.
- **Manuscript sensitivity:** per-task parse ≥ **50%** — keep row iff `parse_success_rate ≥ 0.50` **on that task** (SI **91**, TR **84**, TE **99**).
- Paired ΔF1: **150** pair–task cells (both pair members pass on that task) vs **234** full cohort.
- **Table S2** — multivariable F1, Bonferroni (compare to main Table 1).
- **Figure S11** — family×parameter F1 trends (compare to main Figure 2).
- **Figure S12** — paired ΔF1 facets (compare to main Figure 3).

### Evidence (manuscript primary — parse≥50%)

| Deliverable | Path |
|-------------|------|
| Filtered cohort | [`results/parse50pct_per_task/cohort/models_config_parse50pct_per_task.json`](results/parse50pct_per_task/cohort/models_config_parse50pct_per_task.json) |
| Filtered results (274 rows) | [`results/parse50pct_per_task/cohort/all_models_all_tasks_parse50pct_per_task.csv`](results/parse50pct_per_task/cohort/all_models_all_tasks_parse50pct_per_task.csv) |
| **Table S2** | [`results/parse50pct_per_task/table_1/multivariable_regression_f1_bonferroni_parse50pct_per_task.csv`](results/parse50pct_per_task/table_1/multivariable_regression_f1_bonferroni_parse50pct_per_task.csv) |
| **Table S2 vs Table 1 diff** | [`results/parse50pct_per_task/table_1/table_s2_vs_primary_bonferroni_diff.md`](results/parse50pct_per_task/table_1/table_s2_vs_primary_bonferroni_diff.md) (auto-generated by audit) |
| Paste layout | [`results/parse50pct_per_task/table_1/table_1_f1_bonferroni_paste_format.tsv`](results/parse50pct_per_task/table_1/table_1_f1_bonferroni_paste_format.tsv) |
| **Figure S11** | [`results/parse50pct_per_task/figure_2/fig2_f1_vs_params_overall_trend_parse50pct_per_task.png`](results/parse50pct_per_task/figure_2/fig2_f1_vs_params_overall_trend_parse50pct_per_task.png) |
| Fig 2 stats | `results/parse50pct_per_task/figure_2/fig2_regression_statistics.csv` |
| **Figure S12** | [`results/parse50pct_per_task/figure_3/delta_f1_facet_plot_parse50pct_per_task.png`](results/parse50pct_per_task/figure_3/delta_f1_facet_plot_parse50pct_per_task.png) |
| Fig 3 stats | `results/parse50pct_per_task/figure_3/delta_f1_facet_plot_parse50pct_per_task_stats.csv` |
| **Figure S10** (main) | Generator: [`results/revision_experiments/delta_parse_vs_delta_f1_scatter.png`](../results/revision_experiments/delta_parse_vs_delta_f1_scatter.png) via [`analysis/revision/delta_parse_vs_delta_f1_scatter.py`](../analysis/revision/delta_parse_vs_delta_f1_scatter.py); pipeline renames to `figure_s10_delta_parse_vs_delta_f1.png` |
| Main Table 1 (N=127) | [`results/statistics/table_1_f1_bonferroni_paste_format_primary_n127.tsv`](../results/statistics/table_1_f1_bonferroni_paste_format_primary_n127.tsv) |

### Code

```bash
.venv/bin/python reviewer_2_experiments/scripts/run_parse_filtered_outputs.py --target all
```

### Headline numbers (parse≥50% per-task filter)

- **Table S2:** **10** Bonferroni-sig F1 coefficients (vs **14** in primary Table 1). **Retained:** parameter size (SI/TR), versions 3 and 4 (all tasks), LLaMA family (TR). **Lost:** instruction-tuning (TR/TE), medical (TR), version 2 (TR/TE). **New:** safety-tuned (SI only).
- **Figure S11:** **7/9** family×task panels statistically significant (vs **6/9** primary); all six primary sig panels retained; LLaMA/SI newly significant.
- **Figure S12:** **0** pair-level ΔF1 sign inversions (150 filtered pairs vs 234 primary); facet sig cells **9→4**. No domain-specific fine-tuning gains; significant decrements for MH/Gemma/TR, Medical/Qwen/TE, Safety/Qwen TR+TE.
- **Safety / Qwen guards:** mean ΔF1 stays **strongly negative** on TR (~−0.91) and TE (~−0.80) in both primary and filtered cohorts.

`audit_all_claims.py` verifies parse≥50% cohort counts, recomputed stats vs committed CSVs, **0** pair-level sign inversions, and Safety/Qwen TR+TE negative ΔF1. Writes [`table_s2_vs_primary_bonferroni_diff.md`](results/parse50pct_per_task/table_1/table_s2_vs_primary_bonferroni_diff.md).

Supplement figure filenames in repo: `results/FINETUNE_PAPER_FIGURES/*/revision_figures/figure_s10_*.png`, `figure_s11_*parse50*.png`, `figure_s12_*parse50*.png`.

---

## Tooling note

Portions of the code, documentation, and rebuttal text in this folder were drafted with assistance from **Cursor** (AI-assisted IDE agent mode). The authors reviewed all outputs and take full responsibility for the analyses, claims, and conclusions presented here.
