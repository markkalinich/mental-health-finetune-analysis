---
license: mit
base_model: Qwen/Qwen3-4B
datasets:
- yuhan-nlp/collabllm-medium-rl-grpo
language:
- en
library_name: transformers
tags:
- collabllm
- grpo
- verl
- multiturn
pipeline_tag: text-generation
---

# verl-GRPO CollabLLM medium — Qwen3-4B, step 100

`Qwen/Qwen3-4B` trained with GRPO on the CollabLLM **medium** document-writing task using the
[verl](https://github.com/verl-project/verl) CollabLLM recipe (no SFT warm start). This is a
merged HF checkpoint — load it directly, no adapter step.

**This checkpoint: **the checkpoint to report.** Best BLEU of any arm, and the only one significantly above base (t=+2.31).**

## Benchmark (medium, n=100)

Three roles, thinking **off** everywhere: `Qwen3-4B` assistant (this model),
`Qwen/Qwen3.5-9B` user simulator, `Qwen/Qwen3.5-27B` judge. Flags:
`--user_sim_prompt sim_gap_paper_lazy_full --assistant_max_tokens 4096 --max_new_turns 14`.

| condition | BLEU | interactivity | tokens (k) | MR |
|---|---|---|---|---|
| base `Qwen3-4B` (no proact) | 0.4491 | 0.831 | 2.935 | 0.9870 |
| GRPO step 50 | 0.4524 | 0.819 | 2.281 | 1.0433 |
| **GRPO step 100** | **0.4827** | 0.801 | 2.077 | 1.0761 |
| GRPO step 129 | 0.4825 | 0.744 | 1.944 | 1.0316 |
| proact prompting (no training) | 0.4669 | 0.825 | 1.678 | **1.1236** |
| **← this model (step 100)** | **0.4827** | **0.801** | **2.077** | **1.0761** |

## ⚠️ Read before quoting these numbers

1. **Training peaked at step 100 and then regressed.** Step 129 bought no BLEU and cost
   interactivity. **Never select a checkpoint on verl's `critic/rewards/mean`** — it rises through
   step 129, because the reward credits brevity directly while the benchmark judge penalises the
   interactivity that brevity costs.
2. **Prompting alone still wins on MR** (1.1236 for proact vs 1.0761 for step 100) and needs no
   training. Step 100 wins on **BLEU**. Say which metric you mean.
3. **Every arm's MR gain is dominated by the token term**, not document quality — so MR overstates
   quality improvements for all of them.
4. ⚠️ **35/100 train/eval prompt overlap with byte-identical reward targets.** Because the BLEU
   reward target *is* the test reference on those rows, this is label leakage through the reward.
   See the [dataset card](https://huggingface.co/datasets/yuhan-nlp/collabllm-medium-rl-grpo).

## Training setup

GRPO, `train_batch_size=16`, `rollout.n=8`, `lr=1e-6`, `kl_loss_coef=0.001` (low-var KL),
8 GPUs (FSDP, `world_size_8`), reward = `bleu_score` (+1) + `interactivity` (+1) +
`token_amount` (−0.1). Reference run: wandb `photon/verlxcollabllm/e1adivlo`, `val@0` = 1.0618.

Full setup, the self-contained docker image, and the two acceptance tests are documented in
`studynotes/new_cluster_onboarding.md` of the code repo.
