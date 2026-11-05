---
license: gemma
library_name: transformers
pipeline_tag: text-generation
tags:
- content-moderation
- safety
- function-calling
- gemma
base_model: google/functiongemma-270m-it
---

# SENTRY-270M — content-moderation gate (sweetpapa/sentry-270m-moderation-v3)

A 270M-parameter content-moderation classifier, distilled from a **Gemma-4 31B** teacher
onto the **FunctionGemma-270M** student. Given a piece of content it emits **exactly one
`moderate(...)` function call** — a category, a severity in [0.0, 1.0], and a policy
action — designed to run cheaply (CPU) as the **first-pass gate of a moderation cascade**,
escalating low-confidence cases to a larger judge.

## ⚠️ Serving — read this before you deploy

This model is **numerically fp16-sensitive** (Gemma-3-270M activations overflow fp16's
5-bit exponent range). That has a hard consequence:

- **Serve ONLY via a transformers-native path in fp32 or bf16.** On CPU use **fp32** (it is
  the exact reference AND ~7× faster than bf16, which CPUs emulate). bf16 is numerically
  identical to fp32 for this model and fine on GPU.
- **Do NOT serve via Ollama / llama.cpp / GGUF (any quant — F16, Q8_0, or even BF16-GGUF).**
  Measured directly: llama.cpp's kernels silently **under-flag borderline hate/self_harm**
  (~20 of 42 harmful items downgraded to `safe`) at every quant level. This is a 270M model
  — there is no resource problem for quantization to solve, and a quantized variant would
  put a silent safety failure under this model's name. **No quantized/GGUF artifacts are
  published, on purpose.**
- Reference inference code: [`scripts/moderate.py`](https://huggingface.co/sweetpapa/sentry-270m-moderation-v3) in the
  training repo (fp32, exactly the eval path).

## Output schema

```json
{"name": "moderate", "parameters": {
  "category": "safe | hate_harassment | dangerous_content | sexual_content | violence_gore | self_harm | spam_scam | pii_exposure",
  "severity": 0.0,
  "action":   "allow | flag | block | escalate"
}}
```

## Intended use & scope

- **Use:** a stateless first-pass moderation gate; pair it with a confidence threshold and
  escalate the uncertain slice to a stronger model. Calibrate the threshold to your risk
  tolerance (see the escalation curve in the eval).
- **Out of scope:** standalone high-stakes decisions without human/secondary review;
  CSAM/child-safety detection (explicitly excluded from training — handled by a separate
  Tier-0 hash gate).

## Evaluation (directional — scored against the 31B teacher's labels, not a human gold set)

| metric | value |
|---|---|
| format validity | 98.1% (greedy decoding) |
| high-severity recall (teacher sev ≥ 0.8) | 0.909 |
| calibration (ECE) | 0.071 |
| CPU latency | p50 ≈ 470 ms, p95 ≈ 525 ms per call (fp32, CPU; faster with int8) |
| recall — dangerous_content | 0.84 |
| recall — self_harm | 0.85 |
| recall — violence_gore | 0.58 |
| recall — hate_harassment | 0.54 |

These are teacher-scored and therefore **directional**; a human-verified gold set is the
pre-ship arbiter.

## Recommended generation config

Decode **greedily** and parse the call:

```python
model.generate(**inputs, max_new_tokens=48, do_sample=False)
```

Do NOT add `repetition_penalty` / `no_repeat_ngram_size` — they corrupt the JSON call's
required repetition (quotes, keys, enum names) and drop format validity from ~98% to ~9%.
On the rare unparseable output (~2%, a degenerate decode on hard inputs), **treat it as
`escalate`** — a malformed low-confidence result belongs with the larger judge, which is
exactly the cascade's job.

## Training

- **Teacher:** Gemma-4 31B (bf16), labeling via vLLM; each row gets one `moderate()` call.
- **Corpus:** ~33k rows balanced across the 8 categories (Aegis / BeaverTails / a
  self-harm set), child-safety rows dropped at ingest.
- **Student:** full fine-tune of FunctionGemma-270M with a **completion-only loss mask**
  (loss on the call tokens only) and **oversampling of thin toxic classes**.

## Limitations

- `hate_harassment` recall (~0.54) trails the other harmful classes — hard, contextual,
  and thinner in the teacher-labeled data.
- 270M capacity: **escalate low-confidence** rather than trust every call.
- Evaluated against teacher labels, not human gold.

## License

Governed by the [Gemma Terms of Use](https://ai.google.dev/gemma/terms). Trained on public
safety datasets (see their respective licenses).
