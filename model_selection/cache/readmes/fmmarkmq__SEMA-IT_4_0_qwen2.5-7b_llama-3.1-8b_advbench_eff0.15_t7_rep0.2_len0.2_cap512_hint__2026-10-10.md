---
license: apache-2.0
base_model: Qwen/Qwen2.5-7B-Instruct
tags: [red-teaming, jailbreak, rl, grpo, safety, sema]
pipeline_tag: text-generation
---

# SEMA-IT_4_1_qwen2.5-7b_llama-3.1-8b_advbench_eff0.15_t7_rep0.2_len0.2_cap512_hint

SEMA-IT attacker (manifest experiment `opt_b_cap512`). Research / red-teaming use only.

- attacker: `Qwen/Qwen2.5-7B-Instruct`  | victim: `meta-llama/Llama-3.1-8B-Instruct`  | dataset: advbench
- interaction: dependent (multiturn_chat=True)
- max turns: 7
- reward weights: efficiency=-0.15, repetition=-0.2, length=-0.2
- trained on [verl](https://github.com/volcengine/verl) `recipe/sema`; paper arXiv 2602.06854.
