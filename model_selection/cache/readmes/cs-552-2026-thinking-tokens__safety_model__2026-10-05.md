---
license: apache-2.0
base_model: Qwen/Qwen3-1.7B
tags:
  - safety
  - cs-552
  - epfl
language:
  - en
  - zh
---

# safety_model — CS-552 team `thinking-tokens`

LoRA SFT + DPO on `Qwen/Qwen3-1.7B`, targeting the safety benchmark.

## Training data
- **SFT MC (5,552)**: SafetyBench dev (en+zh, 70) + synthesized 2-option MC from
  BeaverTails 30k_train (2,482) and HH-RLHF harmless-base (3,000)
- **SFT free-form (4,000)**: BeaverTails 30k_train, `is_safe=True` responses
- **DPO pairs (16,000)**: PKU-SafeRLHF-30K (8k) + HH-RLHF harmless-base (4k) +
  BeaverTails-1dim-preference (4k)

All MC items end with `\boxed{<LETTER>}`; free-form items end with `\boxed{Safe}`.

## Training recipe (LoRA, A100 40G)
1. **SFT** — rank=16, lr=1e-4, 2 epochs, ~28 min, train_loss 1.19
2. **DPO** — on top of SFT, β=0.1 sigmoid loss, lr=5e-6, 1 epoch, ~1h35,
   train_loss 0.85, rewards/accuracies 0.625

## Local eval (greedy + n=8 sampling on vLLM)
| eval set                            | n   | pass@1 (greedy) | pass@1 (n=8) | pass@8 |
| ----------------------------------- | --- | --------------- | ------------ | ------ |
| `validation_samples/safety.jsonl`   | 10  | 70%             | 76.2%        | 80%    |
| SafetyBench dev (in-training)       | 70  | 71.4%           | —            | —      |
| BeaverTails 30k_test (held-out)     | 97  | 68.0%           | —            | —      |

## Known limitations
- **Unfairness/Bias regression** (~ -10pp on SafetyBench dev): DPO data is biased
  toward polite non-confrontational responses, reducing willingness to flag bias
- **Offensiveness blind spot** (40% both before/after): no training data trains
  the "is this text offensive?" judgment format
- **Chinese parity but no growth**: all DPO data is English

## Output contract
- Chat template forces `enable_thinking=false` (no `<think>` reasoning)
- Every answer ends in `\boxed{LETTER}` for MC or `\boxed{Safe}` for free-form
- Use `tokenizer.apply_chat_template(messages, add_generation_prompt=True)` —
  no extra kwargs needed