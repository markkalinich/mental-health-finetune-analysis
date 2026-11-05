---
base_model: unsloth/Meta-Llama-3.1-8B-Instruct-bnb-4bit
language:
- en
license: llama3.1
library_name: transformers
tags:
- text-generation-inference
- transformers
- unsloth
- llama
- trl
- psychology
- counseling
---

# Osuda — a length-calibrated psychology assistant

**Built with Llama**

A QLoRA fine-tune of Llama 3.1 8B Instruct that answers like a counselor — short, warm,
and directive — instead of producing a numbered listicle.

The headline result is not accuracy. It is **style control**: the base model answered a
44-word reference with 193 words. After fine-tuning, 42.

- **Developed by:** David33706
- **Finetuned from:** `unsloth/Meta-Llama-3.1-8B-Instruct-bnb-4bit`
- **Training data:** [`samhog/psychology-10k`](https://huggingface.co/datasets/samhog/psychology-10k)
- **Code, evaluation pipeline and full write-up:** https://github.com/David33706/osuda

## Results

Held-out sample of 100 examples (`random_state=42`). Both models decoded identically
(`max_new_tokens=256`, `temperature=1.0`, `min_p=0.1`, `do_sample=True`) with no system prompt.

| Metric | Base Llama 3.1 8B | Osuda | Change |
|---|---|---|---|
| ROUGE-1 | 0.2316 | **0.4385** | +89% |
| ROUGE-2 | 0.0679 | **0.1820** | +168% |
| ROUGE-L | 0.1443 | **0.3133** | +117% |
| BERTScore F1 | 0.8587 | **0.9139** | +0.055 |
| Avg length (words) | 193.2 | **42.3** | reference: 43.6 |

## Training configuration

| Setting | Value |
|---|---|
| Method | QLoRA (4-bit NF4) via [Unsloth](https://github.com/unslothai/unsloth) |
| Rank `r` | 16 |
| `lora_alpha` | 16 |
| `lora_dropout` | 0 |
| `use_rslora` | true |
| Target modules | `q_proj`, `k_proj`, `v_proj`, `o_proj`, `gate_proj`, `up_proj`, `down_proj` |
| Max sequence length | 2048 |

Note `use_rslora=true` scales updates by `alpha/√r` rather than `alpha/r` — with
`alpha=16, r=16` that is an effective factor of 4.0, not 1.0.

## Limitations

Read these before citing the numbers.

- **ROUGE rewards length matching.** The base model wrote ~4.5× the reference length, which
  depresses its precision regardless of content quality. A large share of the ROUGE gain is
  length calibration, not new knowledge. BERTScore (+0.055) is the less length-sensitive
  signal and its gain is far more modest.
- **The baseline is unprompted.** Neither model received a system prompt, so this measures
  fine-tuning against a zero-shot default rather than a prompt-engineered baseline. A base
  model told "answer in 2–3 sentences as a counselor" would close much of this gap. That
  control has not been run.
- **Base responses are truncated** at `max_new_tokens=256`, so 193.2 words is a floor and the
  4.5× ratio is a lower bound.
- **n = 100, single run, no confidence intervals**, stochastic decoding with no generation
  seed. Treat differences as directional.
- **Not a clinical tool.** No safety, crisis-handling, or clinician evaluation was performed.
  Do not deploy to people in distress.

## License

This model is a derivative of Meta's Llama 3.1 and is licensed under the
[Llama 3.1 Community License](https://github.com/meta-llama/llama-models/blob/main/models/llama3_1/LICENSE),
included in this repository as `LICENSE`.

Llama 3.1 is licensed under the Llama 3.1 Community License, Copyright © Meta Platforms, Inc.
All Rights Reserved.

Use is additionally subject to the [Llama 3.1 Acceptable Use Policy](https://llama.meta.com/llama3_1/use-policy).
