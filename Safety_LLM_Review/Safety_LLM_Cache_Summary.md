# Safety LLM cache review — cross-family summary

Summaries of **`cache/results.db`** assistant text for **ShieldGemma**, **Qwen Guard**, **LLaMA Guard** (SI / TR / TE). Per-family tables: [`SHIELDGEMMA_CACHE_OUTPUTS.md`](SHIELDGEMMA_CACHE_OUTPUTS.md), [`QWEN_GUARD_CACHE_OUTPUTS.md`](QWEN_GUARD_CACHE_OUTPUTS.md), [`LLAMA_GUARD_CACHE_OUTPUTS.md`](LLAMA_GUARD_CACHE_OUTPUTS.md).

```bash
.venv/bin/python utilities/query_guard_cache_outputs.py --db cache/results.db --family all
```

---

## Output format

| Family | Format | Matches ingest JSON schema? |
|--------|--------|------------------------------|
| ShieldGemma | Task JSON + optional `` ```json `` | Yes |
| Qwen Guard | `Safety:` / `Categories:` lines | No |
| LLaMA Guard | `safe` or `unsafe` + optional `S*` line | No |

So Qwen/LLaMA rows are usually **`parse_fail`** at ingest even when the text is fine — the validator only looks for task JSON (§2).

---

## `cached_results.status` (set when each row is **written**)

1. `content` = assistant string from the API response.
2. `parsed_json` = first `{…}` in `content` (`utilities/schemas.py` → `extract_first_json_object`).
3. `parsed_result` = `validate_and_coerce(parsed_json)` — task fields + allowed enum values (`utilities/schemas.py`).
4. **`ok`** if `parsed_result` is not **`None`**; else **`parse_fail`**. **`api_error:…`** if LM Studio threw (`orchestration/run_experiment.py`).

**Meaning:** **`parse_fail`** = “no valid task JSON for this pipeline,” not “empty HTTP response.” Benchmark F1 from guards still needs **custom** parsing (`analysis/comparative_analysis/facet_plot_utils.py`), not this flag alone.

---

## Findings in this DB (short)

| Family | Note |
|--------|------|
| ShieldGemma 27b | Full JSON; all `ok`. |
| ShieldGemma 9b | Lots of empty `content` on SI/TR. |
| ShieldGemma 2b | Often missing closing fence — parse JSON with first `{`…last `}`. |
| Qwen 8b/4b | SI varies; TR/TE often only `Safe` / `None`. |
| Qwen 0.6b | Heavy `Jailbreak` / `Controversial`; `PII` on SI. |
| LLaMA Guard 8b | `safe` vs `unsafe`+codes; TR/TE often `S6` vs SI `S11`. |

---

## QC

**`utilities/cache_qc_report.py`:** registry + row counts — not whether guard labels match the benchmark. See [`docs/TODO_GUARD_REPARSING.md`](../docs/TODO_GUARD_REPARSING.md).
