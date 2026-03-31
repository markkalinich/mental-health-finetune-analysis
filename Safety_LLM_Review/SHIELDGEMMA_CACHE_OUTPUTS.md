# ShieldGemma raw outputs (exploratory)

**Available assistant outputs (native format):** JSON objects with the **same keys the standard paper pipeline expects** from instruction-tuned models on each task — i.e. not `Safety:`/`Categories:` lines (that is Qwen/LLaMA Guard). After optional `` ```json `` fences:

| Task | Prompt | JSON fields (typical) |
|------|--------|------------------------|
| SI | `system_suicide_detection_v2` | `safety_type`, `counseling_request`, confidences |
| TR | `therapy_request_classifier_v3` | `safety_type` (usually `no_SI`), `therapy_request`, confidences |
| TE | `therapy_engagement_conversation_v2` | `therapy_engagement`, confidence (`safety_type` optional) |

Ingest **`cached_results.status`** is **`ok`** when that JSON passes `validate_and_coerce` (`utilities/schemas.py`). Counts below use **robust** parsing: strip a leading `` ```json `` line, then parse from first `{` to last `}` (needed for **2b** when the closing fence is missing).

**Source:** `cache/results.db`, `model_family = shieldgemma`.

**Registry:** `config/models_config.csv` — `2b`, `4b-it`, `9b`, `27b`. This doc: **27b**, **9b**, **2b** only (`4b-it` not summarized here).

**Reproducibility:** Regenerate field counts (and fenced/nonempty summaries) with:

```bash
# from repo root; use project venv per docs/DEVELOPMENT.md
.venv/bin/python utilities/query_guard_cache_outputs.py --db cache/results.db --family shieldgemma
```

---

## `shieldgemma-27b` (`shieldgemma-27b`)

| Task | Rows | `status` | Empty | Nonempty | Fenced | Bare | Robust JSON |
|------|-----:|----------|------:|----------:|-------:|-----:|------------:|
| SI | 900 | all `ok` | 0 | 900 | 709 | 191 | 900 |
| TR | 780 | all `ok` | 0 | 780 | 770 | 10 | 780 |
| TE | 420 | all `ok` | 0 | 420 | 414 | 6 | 420 |

### SI — `safety_type`

| value | count |
|------|------:|
| `clearly_neutral` | 151 |
| `active_si_plan_with_intent` | 148 |
| `passive_si` | 134 |
| `active_si_no_plan` | 117 |
| `clearly_sad` | 93 |
| `clearly_happy` | 86 |
| `clearly_angry` | 64 |
| `active_si_plan_no_intent` | 59 |
| `ambiguous_emotional` | 32 |
| `active_si_plan_with_intent_prep` | 16 |

### SI — `counseling_request`

| value | count |
|------|------:|
| `no_request` | 870 |
| `non_counseling_question` | 22 |
| `ambiguous_request` | 8 |

### TR — `safety_type`

| value | count |
|------|------:|
| `no_SI` | 780 |

### TR — `therapy_request`

| value | count |
|------|------:|
| `non_therapeutic_question` | 292 |
| `explicit_therapy_request` | 274 |
| `declarative` | 214 |

### TE — `therapy_engagement`

| value | count |
|------|------:|
| `non_therapeutic` | 186 |
| `simulated_therapy` | 118 |
| `ambiguous_engagement` | 116 |

---

## `shieldgemma-9b` (`shieldgemma-9b`)

| Task | Rows | `status` | Empty | Nonempty | Fenced | Bare | Robust JSON |
|------|-----:|----------|------:|----------:|-------:|-----:|------------:|
| SI | 900 | all `parse_fail` | 900 | 0 | 0 | 0 | 0 |
| TR | 780 | `parse_fail` 777, `ok` 3 | 777 | 3 | 0 | 3 | 3 |
| TE | 420 | `parse_fail` 186, `ok` 234 | 186 | 234 | 0 | 234 | 234 |

**SI:** No assistant text — no field counts.

### TR (nonempty **n=3**)

| field | value | count |
|-------|-------|------:|
| `safety_type` | `no_SI` | 3 |
| `therapy_request` | `non_therapeutic_question` | 3 |

### TE (nonempty **n=234**)

| value | count |
|------|------:|
| `ambiguous_engagement` | 131 |
| `simulated_therapy` | 81 |
| `non_therapeutic` | 22 |

**186** TE rows: empty assistant (`parse_fail`).

---

## `shieldgemma-2b` (`shieldgemma-2b`)

| Task | Rows | `status` | Empty | Nonempty | Fenced | Bare | Robust JSON |
|------|-----:|----------|------:|----------:|-------:|-----:|------------:|
| SI | 900 | `ok` 894, `parse_fail` 6 | 0 | 900 | 893 | 7 | 896 |
| TR | 780 | all `ok` | 0 | 780 | 652 | 128 | 780 |
| TE | 420 | all `ok` | 0 | 420 | 361 | 59 | 420 |

**Strict** balanced `` ```json `…` ``` `` parse matches **272** / **224** / **62** (SI/TR/TE); **4** SI rows have no `{…}` in `content`.

### SI — `safety_type` (robust **n=896**)

| value | count |
|------|------:|
| `active_si_plan_with_intent` | 330 |
| `clearly_neutral` | 157 |
| `clearly_sad` | 111 |
| `ambiguous_emotional` | 96 |
| `clearly_happy` | 90 |
| `passive_si` | 74 |
| `clearly_angry` | 24 |
| `active_si_no_plan` | 10 |
| `None` | 2 |
| `active_si_plan_no_intent` | 2 |

### SI — `counseling_request`

| value | count |
|------|------:|
| `no_request` | 818 |
| `clear_request` | 74 |
| `None` | 2 |
| `non_counseling_question` | 2 |

### TR — `safety_type`

| value | count |
|------|------:|
| `no_SI` | 780 |

### TR — `therapy_request`

| value | count |
|------|------:|
| `non_therapeutic_question` | 392 |
| `explicit_therapy_request` | 307 |
| `declarative` | 81 |

### TE — `therapy_engagement`

| value | count |
|------|------:|
| `simulated_therapy` | 174 |
| `non_therapeutic` | 159 |
| `ambiguous_engagement` | 87 |

---

## Cross-size (nonempty / total)

| | 27b | 9b | 2b |
|--|-----|-----|-----|
| SI | 900/900 | 0/900 | 900/900 |
| TR | 780/780 | 3/780 | 780/780 |
| TE | 420/420 | 234/420 | 420/420 |
