# Qwen Guard raw outputs (exploratory)

**Available assistant outputs (native format):** Two lines of plain text — **`Safety:`** (`Safe` \| `Unsafe` \| `Controversial`) and **`Categories:`** (e.g. `None`, `Suicide & Self-Harm`, `Violent`, `Non-violent Illegal Acts`, `Jailbreak`, `PII` — whatever appears in **this** cache). **Not** the task JSON (`counseling_request` / `therapy_request` / `therapy_engagement`) that **ShieldGemma** and the **other instruction models** use for the same prompts.

Ingest **`ok`** only if `extract_first_json_object` + `validate_and_coerce` (`utilities/schemas.py`) succeed — so these rows are **`parse_fail`** even when nonempty.

**Source:** `cache/results.db`, `model_family = qwen_guard`.

**Registry:** `0.6b`, `4b`, `8b` in `config/models_config.csv`.

**Reproducibility:**

```bash
.venv/bin/python utilities/query_guard_cache_outputs.py --db cache/results.db --family qwen_guard
```

---

## `qwen_guard-8b` (`qwen3guard-gen-8b`)

| Task | Rows | `status` | Empty | Nonempty | `Safety: Safe` | `Safety: Unsafe` | `Safety: Controversial` | `Categories: None` | `Categories: Suicide & Self-Harm` | `Categories: Violent` | `Categories: Non-violent Illegal Acts` | `Categories: Jailbreak` | `Categories: PII` |
|------|-----:|----------|------:|----------:|---------------:|-----------------:|--------------------------:|---------------------:|----------------------------------:|----------------------:|---------------------------------------:|--------------------------:|--------------------:|
| SI | 900 | all `parse_fail` | 0 | 900 | 488 | 211 | 201 | 488 | 388 | 20 | 4 | 0 | 0 |
| TR | 780 | all `parse_fail` | 0 | 780 | 780 | 0 | 0 | 780 | 0 | 0 | 0 | 0 | 0 |
| TE | 420 | all `parse_fail` | 0 | 420 | 420 | 0 | 0 | 420 | 0 | 0 | 0 | 0 | 0 |

**SI joint (counts):** Safe+None 488; Controv.+S&SH 197; Unsafe+S&SH 191; Unsafe+Violent 16; Controv.+Violent 4; Unsafe+NV Illegal 4.

**TR / TE:** Only `Safe` + `Categories: None` on every row.

---

## `qwen_guard-4b` (`qwen3guard-gen-4b`)

| Task | Rows | `status` | Empty | Nonempty | `Safety: Safe` | `Safety: Unsafe` | `Safety: Controversial` | `Categories: None` | `Categories: Suicide & Self-Harm` | `Categories: Violent` | `Categories: Non-violent Illegal Acts` | `Categories: Jailbreak` | `Categories: PII` |
|------|-----:|----------|------:|----------:|---------------:|-----------------:|--------------------------:|---------------------:|----------------------------------:|----------------------:|---------------------------------------:|--------------------------:|--------------------:|
| SI | 900 | all `parse_fail` | 0 | 900 | 484 | 232 | 184 | 484 | 370 | 34 | 12 | 0 | 0 |
| TR | 780 | all `parse_fail` | 0 | 780 | 778 | 0 | 2 | 778 | 0 | 0 | 0 | 2 | 0 |
| TE | 420 | all `parse_fail` | 0 | 420 | 420 | 0 | 0 | 420 | 0 | 0 | 0 | 0 | 0 |

**SI joint:** Safe+None 484; Unsafe+S&SH 202; Controv.+S&SH 168; Unsafe+Violent 22; Controv.+Violent 12; Unsafe+NV Illegal 8; Controv.+NV Illegal 4.

**TR:** 778 `Safe`+`None`; 2 `Controv.`+`Jailbreak`. **TE:** all `Safe`+`None`.

---

## `qwen_guard-0.6b` (`qwen3guard-gen-0.6b`)

| Task | Rows | `status` | Empty | Nonempty | `Safety: Safe` | `Safety: Unsafe` | `Safety: Controversial` | `Categories: None` | `Categories: Suicide & Self-Harm` | `Categories: Violent` | `Categories: Non-violent Illegal Acts` | `Categories: Jailbreak` | `Categories: PII` |
|------|-----:|----------|------:|----------:|---------------:|-----------------:|--------------------------:|---------------------:|----------------------------------:|----------------------:|---------------------------------------:|--------------------------:|--------------------:|
| SI | 900 | all `parse_fail` | 0 | 900 | 186 | 158 | 556 | 186 | 312 | 2 | 0 | 397 | 3 |
| TR | 780 | all `parse_fail` | 0 | 780 | 770 | 0 | 10 | 770 | 0 | 0 | 0 | 10 | 0 |
| TE | 420 | all `parse_fail` | 0 | 420 | 419 | 0 | 1 | 419 | 0 | 0 | 0 | 1 | 0 |

**SI joint:** Controv.+Jailbreak 387; Safe+None 186; Controv.+S&SH 166; Unsafe+S&SH 146; Unsafe+Jailbreak 10; Controv.+PII 3; Unsafe+Violent 2.

**TR:** 770 `Safe`+`None`; 10 `Controv.`+`Jailbreak`. **TE:** 419 `Safe`+`None`; 1 `Controv.`+`Jailbreak`.
