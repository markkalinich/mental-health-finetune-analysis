---
license: apache-2.0
language:
- ro
- en
- es
- fa
- hi
base_model: Qwen/Qwen3.5-4B
pipeline_tag: text-generation
tags:
- affective-state-identification
- masive
- emotion
- multilingual
- sft
---

# qwen3.5-4B-mixed

Qwen3.5-4B fine-tuned for multilingual **affective-state identification** (MASIVE-style masked affect expression filling) across Romanian, English, Spanish, Persian, and Hindi.

Given a passage with one or more `[MASK]` positions, the model outputs the distinct affective expressions that fill them, in order of first appearance, separated by spaces.

## Training data

5000 train / 1200 val / 5×1000 test rows, 1000 rows per language, scrambled and shuffled (seed 42). Sourced from:
- **ro**: sampled from `pipeline/data/benchmark_ro_asi_clean.jsonl` in the [Romanian_ASI](https://github.com/lolismek/Romanian_ASI) repo
- **en / es / fa**: sampled from the MASIVE dataset by the same pipeline
- **hi**: converted from Hindi affective-state samples via `scripts/convert_hindi_to_presentation_format.py`

Each row supplies a masked passage and a list of distinct affective expressions (single words or short idiomatic phrases) that fill those masks. Supervision target is `" ".join(labels)` — see the [training repo](https://github.com/lolismek/Romanian_ASI) `plans/sft_run_v1_qwen3.5-4b.md` for the full semantics.

## Training configuration

| | |
|---|---|
| Base model | `Qwen/Qwen3.5-4B` (post-trained, not Instruct) |
| Framework | HF `Trainer` + DeepSpeed ZeRO-3 + BF16 + SDPA |
| Hardware | 3 × A100-40GB |
| Batch | 2 × 2 grad-accum × 3 GPUs = 12 effective |
| Optimizer | AdamW, cosine, `lr=1e-5`, `warmup_ratio=0.03`, `max_grad_norm=1.0` |
| Epochs | 3 (1251 steps) |
| Best checkpoint | step 825 (best eval_loss 0.796), selected via `load_best_model_at_end=true` |
| Seed | 42 |

## Prompt format

Use the model's chat template with `enable_thinking=False`. System prompt:

> You are an affective-state identifier. Given a sentence with one or more [MASK] positions, output the distinct affective expressions that fill them, in order of first appearance, separated by a single space. Expressions may be single words or short idiomatic phrases. No explanation, no punctuation, no repeats.

### Minimal inference example

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

tok = AutoTokenizer.from_pretrained("alexjerpelea/qwen3.5-4B-mixed", trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    "alexjerpelea/qwen3.5-4B-mixed", torch_dtype=torch.bfloat16, trust_remote_code=True,
).cuda().eval()

SYSTEM = (
    "You are an affective-state identifier. Given a sentence with one or more "
    "[MASK] positions, output the distinct affective expressions that fill "
    "them, in order of first appearance, separated by a single space. "
    "Expressions may be single words or short idiomatic phrases. "
    "No explanation, no punctuation, no repeats."
)

user_text = "Eram [MASK] de vedenia ei."
messages = [
    {"role": "system", "content": SYSTEM},
    {"role": "user", "content": user_text},
]
prompt = tok.apply_chat_template(
    messages, tokenize=False, add_generation_prompt=True, enable_thinking=False,
)
ids = tok(prompt, return_tensors="pt").to("cuda")
out = model.generate(**ids, max_new_tokens=50, do_sample=False, num_beams=1,
                     pad_token_id=tok.eos_token_id)
print(tok.decode(out[0][ids["input_ids"].shape[1]:], skip_special_tokens=True).strip())
# → "uluita"
```

## Evaluation

Scored via **word-sequence set-match**: each gold label (single word or multi-word idiomatic phrase) must appear as a contiguous whitespace-token subsequence of the normalized model output. Evaluation used greedy decoding via `transformers` (`do_sample=False, num_beams=1`); top-k sampling via vLLM pending.

| language | n | set_acc@1 | sim@1 (mBERT) |
|---|---|---|---|
| ro | 1000 | **0.381** | 0.851 |
| en | 1000 | 0.147 | 0.848 |
| es | 1000 | 0.191 | 0.813 |
| fa | 1000 | **0.414** | 0.902 |
| hi | 1000 | 0.481 | 0.821 |
| **mean** | 5000 | **0.323** | 0.847 |

### Stratified by training-label frequency (set_acc@1 on test rows whose `labels[0]` appeared ≥ k times in training)

| lang | ≥1 | ≥5 | ≥10 | ≥20 | ≥50 |
|---|---|---|---|---|---|
| ro | 0.381 | 0.441 | 0.480 | 0.537 | **0.788** |
| en | 0.147 | 0.174 | 0.029 | — | — |
| es | 0.191 | 0.226 | 0.238 | 0.484 | — |
| fa | 0.414 | 0.604 | 0.743 | **0.853** | 0.853 |
| hi | 0.481 | 0.492 | 0.510 | 0.515 | 0.581 |

When gold labels were seen ≥20 times in training, accuracy on non-EN languages is in the 0.48–0.85 range. EN's flat label distribution (328 unique test labels across 1000 rows) prevents any single label from accumulating that density during training, which explains its lower headline number.

### Comparison to zero-shot baseline

For Romanian, the prior zero-shot reference from `Qwen/Qwen3.5-9B` on the same test split was **set_acc@1 = 0.22**. This SFT run with a smaller 4B model reaches **0.38** — a +17 pp improvement.

## Known limitations

- **Lexical-exact metric**: predictions like `"stupid"` vs gold `"foolish"`, or `"interesado"` vs gold `"interesada"` (Spanish gender), score 0 despite being semantically correct. `sim@1` (contextual mBERT similarity) is uniformly 0.81–0.90 across all five languages, indicating semantic agreement is much stronger than `set_acc@1` suggests.
- **Overfitting onset at step 850**: the model memorizes training in epoch 3. The released checkpoint is from step 825 (pre-overfit). A shorter 2-epoch run would likely generalize similarly.
- **Hindi label noise**: short Hindi stems (e.g., `डर` "fear") can substring-match loanwords (`किंडरगार्टेन` "kindergarten") during data conversion; a handful of HI training/test rows are affected.
- **FA phrase labels**: the model outputs full Persian idioms like `دلم تنگ شده` correctly when appropriate. Earlier eval pipelines that took only the first whitespace-token of the output under-score FA substantially — use word-sequence set-match or equivalent.

## Citation / Attribution

Base model: Qwen3.5-4B by Alibaba Cloud (Apache-2.0).
Fine-tuning: Alex Jerpelea, [Romanian_ASI](https://github.com/lolismek/Romanian_ASI) repo. See `reports/sft_qwen3.5-4b_v1_results.md` in the repo for the full training writeup and per-sample predictions.
