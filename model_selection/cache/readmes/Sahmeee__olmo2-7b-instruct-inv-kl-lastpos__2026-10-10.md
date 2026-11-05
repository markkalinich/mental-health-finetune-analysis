---
license: apache-2.0
base_model: allenai/OLMo-2-1124-7B-Instruct
tags: [tokenization, robustness, safety, adversarial-tokenization]
---

# inv_kl_lastpos

Research checkpoint from a study of **tokenization (reader) invariance** and its
effect on robustness to adversarial re-tokenization. Fine-tuned from
`allenai/OLMo-2-1124-7B-Instruct`.

**These are research artifacts, not products.** Numbers below are measured on a
200-prompt AdvBench holdout that was excluded from training by construction.

## Measured

| metric | value |
| --- | --- |
| — | not yet measured |

`AdvTok ASR` is attack success rate under adversarial tokenization
(Geh et al., arXiv:2503.02174), Llama-Guard-3-8B judged, greedy decoding.
`XSTest over-refusal` is the refusal rate on *safe* prompts — the cost side.

## Training configuration

| field | value |
| --- | --- |
| `mode` | `prefix` | 
| `objective` | `kl_lastpos` | 
| `kl_direction` | `forward` | 
| `ce_weighting` | `uniform` | 
| `ema_beta` | `None` | 
| `harmful_mix` | `mixed` | 
| `harmful_fraction` | `0.286` | 
| `num_encodings` | `8` | 
| `cvar_quantile` | `0.25` | 
| `max_steps` | `700` | 
| `learning_rate` | `1e-05` | 
| `grad_accum` | `8` | 
| `seed` | `42` | 
| `reference_model` | `allenai/OLMo-2-1124-7B-Instruct` | 
| `max_new_tokens` | `128` | 
| `prefix_tokens` | `8` | 
| `stochastok_p` | `0.3` | 

## Parameter drift from base (training-happened guard)

| group | relative L2 |
| --- | --- |
| attn | 0.01020 |
| embed_tokens | 0.00053 |
| lm_head | 0.01036 |
| mlp | 0.01086 |
| norm | 0.00081 |

## Caveats

- Single seed. No claim of significance across seeds.
- Evaluated on English AdvBench/XSTest/Alpaca only.
- The safety numbers are for the *specific* attack studied; they do not imply
  robustness to other jailbreaks.
