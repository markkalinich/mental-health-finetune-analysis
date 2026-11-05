<!-- doc-verbosity: public-ready -->

# Manual-removal rows a later rule made unnecessary

A row in `manual_removals.csv` may only name a model that reaches manual review. When a rule change cuts a reviewed model at an earlier step, its row is moved here with its wording, so the person's decision is kept and the funnel does not stop on a stale row. (The 6 October removals of the same kind are in git history and `unapproved-removals.md`.)

| Moved on | Model | Category | Reason as written | Why the row is no longer needed |
|---|---|---|---|---|
| 2026-10-09 | `ozertuu/TherapyZ-Llama-3-8B` | not an English-language model | parent ytu-ce-cosmos/Turkish-Llama-8b-DPO-v0.1 descends from a Llama 3 8B continued pre-training on Turkish text; the model is trained for Turkish, our benchmarks are English (decided by Mark Kalinich, 6 Oct) | The parent registry (9 Oct) classes `ytu-ce-cosmos/Turkish-Llama-8b-DPO-v0.1` as a fine-tune of an instruct model, so the model now stops at step 3 (`parent_finetune`). |
