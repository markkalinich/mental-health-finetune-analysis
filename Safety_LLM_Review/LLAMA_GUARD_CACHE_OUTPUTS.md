# LLaMA Guard raw outputs (exploratory)

**Available assistant outputs (native format):** Plain text — either the single token **`safe`** (lowercase in cache), or **`unsafe`** on the first line with an optional **second line** giving a **taxonomy code** (`S1`, `S2`, `S6`, `S11`, … — Meta’s Llama Guard label scheme; meanings are defined in Meta’s docs, not repeated here). **Not** task JSON (`counseling_request` / `therapy_request` / `therapy_engagement`) like **ShieldGemma** / instruction models, and **not** `Safety:` / `Categories:` lines like **Qwen Guard**.

Ingest **`ok`** only if `extract_first_json_object` + `validate_and_coerce` (`utilities/schemas.py`) succeed — so these rows are **`parse_fail`** when the body is guard text.

**Source:** `cache/results.db`, `model_family = llama_guard`.

**Registry:** `llama_guard` — enabled sizes include **`8b`** (`llama-guard-3-8b`) and **`1b`**. This doc: **`8b` only** (largest enabled guard in the registry).

**Reproducibility:**

```bash
.venv/bin/python utilities/query_guard_cache_outputs.py --db cache/results.db --family llama_guard
```

---

## `llama_guard-8b` (`llama-guard-3-8b`)

### Overview

| Task | Rows | `cached_results.status` | Empty assistant | Nonempty | Distinct full `content` |
|------|-----:|-------------------------|-----------------|----------:|------------------------:|
| SI | 900 | all `parse_fail` | 0 | 900 | 5 |
| TR | 780 | all `parse_fail` | 0 | 780 | 3 |
| TE | 420 | all `parse_fail` | 0 | 420 | 2 |

### SI (`system_suicide_detection_v2`)

**First line**

| value | count |
|------|------:|
| `safe` | 623 |
| `unsafe` | 277 |

**Second line (only when first line is `unsafe`)**

| code | count |
|------|------:|
| `S11` | 269 |
| `S1` | 6 |
| `S2` | 1 |
| `safe` | 1 |

**Exact full `content` strings**

| `content` | count |
|-----------|------:|
| `safe` | 623 |
| `unsafe\nS11` | 269 |
| `unsafe\nS1` | 6 |
| `unsafe\nsafe` | 1 |
| `unsafe\nS2` | 1 |

### TR (`therapy_request_classifier_v3`)

**First line**

| value | count |
|------|------:|
| `safe` | 708 |
| `unsafe` | 72 |

**Second line (unsafe only)**

| code | count |
|------|------:|
| `S6` | 71 |
| `S11` | 1 |

**Exact full `content`**

| `content` | count |
|-----------|------:|
| `safe` | 708 |
| `unsafe\nS6` | 71 |
| `unsafe\nS11` | 1 |

### TE (`therapy_engagement_conversation_v2`)

**First line**

| value | count |
|------|------:|
| `safe` | 418 |
| `unsafe` | 2 |

**Second line (unsafe only)**

| code | count |
|------|------:|
| `S6` | 2 |

**Exact full `content`**

| `content` | count |
|-----------|------:|
| `safe` | 418 |
| `unsafe\nS6` | 2 |

---

## Cross-format note

| Family | SI/TR/TE native shape in cache |
|--------|--------------------------------|
| ShieldGemma | JSON with task fields |
| Qwen Guard | `Safety:` + `Categories:` |
| LLaMA Guard | `safe` or `unsafe` + optional `S*` line |
