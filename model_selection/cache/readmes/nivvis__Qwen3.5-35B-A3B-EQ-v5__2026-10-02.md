---
library_name: transformers
license: apache-2.0
license_link: https://huggingface.co/Qwen/Qwen3.5-35B-A3B/blob/main/LICENSE
pipeline_tag: text-generation
base_model:
  - Qwen/Qwen3.5-35B-A3B
  - llmfan46/Qwen3.5-35B-A3B-heretic-v2
tags:
  - eq
  - emotional-intelligence
  - dpo
  - lora
  - heretic
  - uncensored
---

# Qwen3.5-35B-A3B-EQ-v5

A DPO fine-tune of [Qwen3.5-35B-A3B-heretic-v2](https://huggingface.co/llmfan46/Qwen3.5-35B-A3B-heretic-v2).

The tune optimized for two things:
- bringing warmth, emotional intelligence, general chat improvement to Qwen 3.5 series
- countering some negative tendencies of Heretic models (overwillingness to agree, be sycophantic, etc) without sacrificing derestriction

**This is still intended as a general use model** (agentic, coding, general chat). Tuning was lightly & with precision. More general benchmarks to follow.

## What this model does

This model is trained to be a better conversational partner in emotionally complex situations, while maintaining base model capabilities. It:

- **Validates without sycophancy** — empathizes with frustration without rubber-stamping bad behavior
- **Sets boundaries warmly** — names uncomfortable truths without lecturing
- **Sounds human** — conversational tone, not therapist-speak. better tone vs vanilla Qwen 3.5, e.g. ~~"It sounds like"~~

## Key specs

| | |
|---|---|
| **Base** | Qwen/Qwen3.5-35B-A3B |
| **Parent** | llmfan46/Qwen3.5-35B-A3B-heretic-v2 (decensored via MPOA+SOMA) |
| **Fine-tune** | DPO with LoRA (r=32, alpha=64) |
| **Training data** | DPO preference pairs with diverse, simulated (real-situation-based) generated dialogue |
| **Precision** | bf16 |

## EQ-Bench 3 results

Evaluated on [EQ-Bench 3](https://eqbench.com/) — 45 emotional intelligence scenarios.

### Leaderboard ranking (raw rubric score, Sonnet 3.7 judge)

Re-judged with claude-3.7-sonnet to match the official leaderboard methodology.
These are raw rubric scores, not the official ELO ranking — higher is higher but not
necessarily better (see [eqbench.com](https://eqbench.com) for normalized ELO).
This is the best apples-to-apples comparison available without submitting for ELO.
Rankings sourced from the [EQ-Bench 3 canonical leaderboard data](https://github.com/EQ-bench/eqbench3) (2026-03-19 snapshot).
Newer models (gpt-5.4, claude-sonnet-4-6, claude-opus-4-6) are judged with Opus on the
live leaderboard and are not yet in the official repo data with Sonnet scores.

| # | Model | Raw Score | Judge |
|---|-------|----------|-------|
| 1 | horizon-alpha | 202.3 | claude-3.7-sonnet |
| 2 | Kimi-K2-Instruct | 202.0 | claude-3.7-sonnet |
| 3 | gemini-2.5-pro-preview-06-05 | 200.5 | claude-3.7-sonnet |
| 4 | o3 | 199.0 | claude-3.7-sonnet |
| 5 | gpt-5 | 195.6 | claude-3.7-sonnet |
| 6 | GLM-4.5 | 195.0 | claude-3.7-sonnet |
| 7 | gemini-2.5-pro | 193.7 | claude-3.7-sonnet |
| **8** | **EQ-v5 (this model, 3B active)** | **193.6** | **claude-3.7-sonnet** |
| 9 | grok-4 | 192.8 | claude-3.7-sonnet |
| 10 | claude-opus-4 | 192.6 | claude-3.7-sonnet |
| 11 | gpt-oss-120b | 192.2 | claude-3.7-sonnet |
| 12 | claude-sonnet-4 | 191.6 | claude-3.7-sonnet |
| 13 | Qwen3-235B-A22B | 191.1 | claude-3.7-sonnet |

### Qwen family comparison (all claude-3.7-sonnet judge)

| Model | Params (active) | Raw Score | Notes |
|-------|----------------|----------|-------|
| EQ-v1 (35B MoE, first DPO) | 3B | 195.6 | |
| Qwen3.5-27B dense | 27B | 194.1 | |
| **EQ-v5 (this model)** | **3B** | **193.6** | |
| EQ-v2-ckpt600 | 3B | 191.1 | |
| Qwen3-235B-A22B | 22B | 191.1 | leaderboard |
| heretic-v2-27B base | 27B | 190.5 | |
| Qwen3.5-35B-A3B vanilla | 3B | 185.5 | our base model |
| Qwen3-8B | 8B | 181.8 | leaderboard |
| Qwen3-32B | 32B | 179.7 | leaderboard |
| Qwen3-30B-A3B | 3B | 166.3 | leaderboard |

> **Note on EQ-v1 and Qwen3.5-27B scores:** While EQ-v1 and the 27B dense model score
> slightly higher on raw rubric, we recommend EQ-v5 for real-world use. The earlier models
> and the 27B dense produce verbose, formulaic responses that score well on analytical
> dimensions but feel robotic in conversation. EQ-v5 speaks more naturally — less therapist,
> more human. The heretic-v2 base was specifically chosen because it preserves empathy and
> emotional range while being de-restricted, giving EQ-v5 a more authentic voice that
> the vanilla Qwen models lack.

### Version history

EQ-v5 is the fifth iteration of the EQ fine-tune series on the Qwen3.5-35B-A3B architecture.

Key improvements over previous versions:
- Less sycophantic (reduced blind validation)
- More humanlike and conversational tone
- Better pragmatic advice
- Small warmth trade-off for increased honesty

**Strengths:** Warmth, humanlike quality, low moralising. Competitive with frontier on insight and analytical.
**Gaps:** Assertiveness lags behind frontier — the model is still too agreeable in some scenarios.

## HumanEval+ (coding)

| Benchmark | pass@1 |
|-----------|--------|
| HumanEval (base) | **95.1%** |
| HumanEval+ (extended tests) | **88.4%** |

Thinking enabled, temperature=0.6, top_p=0.95. Scores from FP8 quantization.

## Training details

- **Method:** Standard DPO (sigmoid loss) with LoRA
- **Data:** DPO preference pairs covering emotional warmth, boundary-setting, and anti-sycophancy training. The heretic-v2 base is de-restricted, so targeted training was added to maintain appropriate pushback on moralising and overly agreeable behavior.
- **LoRA:** r=32, alpha=64, all attention + MLP projections
- **LR:** 2e-6 cosine, warmup 0.1, beta=0.3

## Serving

```bash
vllm serve nivvis/Qwen3.5-35B-A3B-EQ-v5 \
  --served-model-name Qwen3.5-35B-A3B-EQ-v5 \
  --max-model-len 32768 \
  --trust-remote-code \
  --dtype bfloat16 \
  --reasoning-parser qwen3
```

### Sampling recommendations

- **With thinking:** `temp=0.7, top_p=0.9, max_tokens=4096`
- **Without thinking:** `temp=0.7, top_p=0.8, max_tokens=2048`

To disable thinking mode:
```python
extra_body={"chat_template_kwargs": {"enable_thinking": False}}
```

## Lineage

```
Qwen/Qwen3.5-35B-A3B
  → llmfan46/Qwen3.5-35B-A3B-heretic-v2 (decensored)
    → nivvis/Qwen3.5-35B-A3B-EQ-v5 (this model — DPO for EQ)
```

## Limitations

- Assertiveness is below frontier — the model can be too agreeable in scenarios requiring pushback
- Best insights sometimes stay in thinking tokens and don't fully surface in the response
- Trained on English conversational data only
- Not a therapist — do not use for mental health advice

## License

Apache 2.0, following the base Qwen3.5 license.
