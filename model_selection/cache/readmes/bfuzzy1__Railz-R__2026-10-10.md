---
license: cc-by-4.0
base_model: Qwen/Qwen3-0.6B
tags:
  - content-moderation
  - safety
  - guardrail
  - policy-conditioned
  - reasoning
language:
  - en
---

# Railz-R — sub-1B policy-conditioned safety guard *with reasoning*

**Railz-R** is a 0.6B content-moderation guard that judges content against a **policy you supply at inference** — not a fixed taxonomy. Give it a list of prohibited categories; it emits the **violated category verbatim (or abstains)**, then a short **chain-of-thought** justifying the decision against *that* policy. Same content flips safe↔unsafe when the policy changes.

Built on Qwen3-0.6B. Trained with **mechanical supervision** (NVIDIA Aegis-2.0 labels) + published short reasoning traces (NVIDIA Nemotron Content-Safety-Reasoning, CC-BY-4.0, filtered to ground-truth-matched) + mechanical policy-check rationales. **No teacher model in the training loop.**

## Results (0.6B)

| metric | Railz-R | note |
|---|---|---|
| policy-flip (held-out contrast pairs) | **78%** | same content, policy toggled → verdict must flip |
| Aegis-2.0 test F1 (in-domain detection) | **76%** (P72/R81) | NVIDIA's primary in-domain metric; in the range of 8B guards |
| ToxicChat F1 (out-of-domain) | 28% | OOD generalization; see limitations |

## Prompt format (verdict-first, then reasoning)

```
<|im_start|>system
You are a content moderation system. The policy below lists PROHIBITED categories. Anything not listed is permitted.
First reason briefly inside <think></think>. Then, on a new line, state the violated category using the exact category text from the list, or exactly: no listed category applies

PROHIBITED:
- violence or physical harm
- hate speech or identity-based hatred
- controlled or regulated substances
<|im_end|>
<|im_start|>user
CONTENT TO MODERATE:
<content here><|im_end|>
<|im_start|>assistant
```

Model output:
```
Violated category: controlled or regulated substances
<think>
The request seeks synthesis instructions; the policy prohibits controlled or regulated substances and the content matches it, so it is a violation.
</think>
```
Parse the verdict from the line after `Violated category:`; strip the `<think>…</think>` block. Greedy decoding, ~120 max new tokens.

## Limitations
- **OOD gap**: trained on the Aegis distribution. On out-of-distribution benchmarks (ToxicChat) it under-flags novel phrasing. Strong sub-1B OOD requires teacher-distillation pipelines this model deliberately avoids.
- The CoT is a *post-hoc justification* of a verdict-first decision — useful for interpretability, not a guaranteed faithful causal trace.
- English; text-only.

## Sibling model
**Railz** (non-reasoning): same task, emits the verdict only (no CoT), higher policy-flip. Use Railz for throughput, Railz-R for interpretability.

## License
CC-BY-4.0 (inherits Aegis-2.0 / Nemotron data licensing).
