---
license: apache-2.0
base_model: Qwen/Qwen3-4B
tags: [clinical, agent, harbor, grpo, rl]
---
# Qwen3-4B — Clinical-Long-Bench SFT + GRPO (multi-gate reward, step 50)

GRPO (SkyRL) from the SFT checkpoint (`qwen3-4b-clinical-long-bench-sft`). Reward = (2·diagnosis + required_tools +
parameterised_actions + must_ask) / 5. 8 tasks × 8 rollouts per step, temperature 1.0, lr 1e-6 constant, no KL,
≤ 32 agent turns / 15 min per rollout, patient simulator and must-ask judge Claude Opus 4.6. Step 50 is the RL
checkpoint with the highest held-out `pass@1`.

## Task and harness
Clinician agent for **Clinical-Long-Bench**, a Harbor benchmark of 333 long-horizon clinical consultations with a
simulated patient and a clinical tool surface, scored by four gates (diagnosis, required tools, parameterised
actions, LLM-judged must-ask coverage; `pass@1` = all gates pass). The model acts through the Harbor **terminus-2**
agent: every reply is a JSON object (`analysis`, `plan`, `commands`, `task_complete`) whose shell commands call the
benchmark's `clinic` CLI (`clinic say`, `clinic call <tool> '<json>'`).

Split: 283 training tasks / 50 held-out test tasks (42 of the 50 test diagnoses never occur in training).

## Held-out results (50 test tasks; patient simulator and must-ask judge Claude Opus 4.6)

| model | diagnosis | required tools | must-ask | pass@1 |
|---|---|---|---|---|
| Qwen3-4B (zero-shot, 2 rollouts/task) | 0.26 | 0.03 | 0.40 | 0.00 |
| SFT (`qwen3-4b-clinical-long-bench-sft`, 2 rollouts/task) | 0.39 | 0.33 | 0.78 | 0.08 |
| SFT + GRPO, multi-gate reward, step 50 (`qwen3-4b-clinical-long-bench-grpo`, 1 rollout/task) | 0.48 | 0.36 | 0.71 | 0.12 |

With 50 tasks, differences below ~0.07 are within noise; the GRPO row is a single evaluation pass.

## Intended use
Research on long-horizon clinical agents and RL reward design. **Not a medical device; not for clinical use.**
Outputs can be wrong, incoherent or overconfident.

Base model: [Qwen/Qwen3-4B](https://huggingface.co/Qwen/Qwen3-4B) (Apache-2.0).

## Citation

If you use this model, please cite the KlinikeBench paper ([arXiv:2609.38480](https://arxiv.org/abs/2609.38480)):

```bibtex
@misc{fang2026klinikebench,
  title         = {KlinikeBench: Evaluating Language Models Beyond Diagnostic Accuracy},
  author        = {Fang, Xueting and Li, Zehui and Yang, Yang and Giovino, Camilla and Patel, Shubh K. and
                   Prajapati, Shailly and Subasri, Vallijah and Shan, Caihua},
  year          = {2026},
  eprint        = {2609.38480},
  archivePrefix = {arXiv},
  url           = {https://arxiv.org/abs/2609.38480}
}
```
