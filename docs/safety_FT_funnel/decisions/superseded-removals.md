<!-- doc-verbosity: public-ready -->

# Manual-removal rows a later rule made unnecessary (safety)

A row in `manual_removals.csv` may only name a model that reaches manual review. When a rule change cuts a reviewed model at an earlier step, its row is moved here with its wording, so the person's decision is kept and the funnel does not stop on a stale row. The mental-health counterpart is `docs/mental_health_FT_funnel/decisions/superseded-removals.md`.

| Moved on | Model | Category | Reason as written | Why the row is no longer needed |
|---|---|---|---|---|
| 2026-10-09 | `shibu-phys/arise-japanese-guardrail-gemma2b-lora` | Japanese-language model | parent google/gemma-2-2b-jpn-it is Google's Japanese instruction tune; the guardrail is trained for Japanese text, our benchmarks are English (decided by Mark Kalinich, 6 Oct) | The parent registry (9 Oct) classes `google/gemma-2-2b-jpn-it` as a fine-tune: Google's card says it is "a Gemma 2 2B model fine-tuned on Japanese text" from `google/gemma-2-2b-it`, an already-instruct release, which under Mark's definition (instruct → more tuning) is `finetune`. The model now stops at step 3 (`parent_finetune`). |
