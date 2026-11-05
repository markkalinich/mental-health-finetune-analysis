---
license: apache-2.0
base_model: convaiinnovations/laya
library_name: laya
pipeline_tag: text-classification
tags:
  - laya
  - financial-sentiment
  - fingpt
  - rlcd
  - finance
  - sentiment-analysis
  - 3-class
datasets:
  - shanaka95/fingpt-sentiment-3class
metrics:
  - accuracy
---

# Laya Fine-tuned for 3-Class Financial Sentiment

`convaiinnovations/laya` (421M, ModernBERT-large + decision head) fine-tuned with **RLCD** (Reinforcement Learning for Calibrated Decisions) for a single task: pick one of `positive`, `negative`, `neutral` from a financial text.

## Evaluation

Same 15,355-item stratified test split of [`shanaka95/fingpt-sentiment-3class`](https://huggingface.co/datasets/shanaka95/fingpt-sentiment-3class), same `choice` question schema, same `laya.Agent.predict()` call. Only `MODEL_ID` differs.

| | Zero-shot (`convaiinnovations/laya`) | **Fine-tuned (this model)** | Δ |
|---|---|---|---|
| **Overall accuracy** | 0.7024 (10,786 / 15,355) | **0.9486** (14,566 / 15,355) | **+0.2462 (+24.62 pp)** |
| F1 — positive | 0.694 | 0.952 | +0.258 |
| F1 — neutral | 0.696 | 0.949 | +0.253 |
| F1 — negative | 0.726 | 0.942 | +0.216 |
| Recall — positive | 0.584 | 0.954 | **+0.370** |
| Latency p50 | 38.6 ms | 36.6 ms | -2 ms |

The fine-tuning script never saw any of these test examples. Eval notebooks + the full reproduction repo: [github.com/shanaka95/laya-fintiment](https://github.com/shanaka95/laya-fintiment).

## Training

- **Base model:** [`convaiinnovations/laya`](https://huggingface.co/convaiinnovations/laya)
- **Dataset:** [`shanaka95/fingpt-sentiment-3class`](https://huggingface.co/datasets/shanaka95/fingpt-sentiment-3class) — train split (61,017 items after 400 held out for post-training calibration)
- **Objective:** RLCD with strictly proper scoring rules (log + spherical, `w_sph=0.75`; no RPS because all questions are `choice`). REINFORCE with group-mean baseline, `group_size=4` noisy forward passes per example.
- **Epochs:** 4 (7,624 optimizer steps, effective batch 32)
- **Hardware:** 1 × 12 GB GPU
- **Optimisation:** AdamW, cosine LR schedule, gradient checkpointing ON, `micro_batch=16`, `grad_accum=2`
- **Question schema used for every example:**
  ```python
  {
      "sentiment": {
          "type": "choice",
          "instructions": (
              "What is the financial sentiment of this text? "
              "Please choose exactly one answer from {positive, negative, neutral}. "
              "Answer only with the chosen label."
          ),
          "criteria": {
              "positive": "The text expresses a positive / bullish financial sentiment.",
              "negative": "The text expresses a negative / bearish financial sentiment.",
              "neutral":  "The text is neutral, factual, or has no clear positive or negative sentiment.",
          },
      }
  }
  ```
- **Final calibration temperatures** (choice / score / noul): `[5.013, 1.2, 1.2]`
- **Epoch avg loss:** 0.257 → 0.493 → 0.323 → **0.199**

Recipe adapted from the upstream [fine-tuning notebook](https://github.com/NandhaKishorM/laya/blob/main/notebooks/laya_finetune_typed_decisions_2xT4_kaggle.ipynb).

## Usage

```bash
pip install "laya>=0.1.6" "transformers>=4.48.0"
```

```python
import os
os.environ["USE_TF"] = "0"  # avoids an abseil/TF deadlock when loading transformers

import laya

agent = laya.Agent("shanaka95/laya-fintiment", device="cuda")

questions = {
    "sentiment": {
        "type": "choice",
        "instructions": (
            "What is the financial sentiment of this text? "
            "Please choose exactly one answer from {positive, negative, neutral}. "
            "Answer only with the chosen label."
        ),
        "criteria": {
            "positive": "The text expresses a positive / bullish financial sentiment.",
            "negative": "The text expresses a negative / bearish financial sentiment.",
            "neutral":  "The text is neutral, factual, or has no clear positive or negative sentiment.",
        },
    }
}

result = agent.predict("Apple reported record quarterly revenue, beating analyst estimates.", questions)
print(result["answers"]["sentiment"]["choice"])   # -> 'positive' (probability mass concentrated on it)
```

For batched inference or CPU use, pass `device="cpu"` or pre-build a `laya.Router`.

## Worked example

| Input | Base laya | This model |
|---|---|---|
| `"Asset Management One Co. has a bullish call on Treasuries. One for the long, long run https://t.co/8go8ZhMvdc"` | `positive` @ **0.5604** (also 0.3705 on neutral) | `positive` @ **0.9488** (decisive) |

## Files

| File | Notes |
|---|---|
| `model.safetensors` | 842 MB fine-tuned weights |
| `encoder/` | encoder sub-dir (downstream code may read it directly) |
| `tokenizer/` | tokenizer sub-dir |
| `rl_agent_config.json` | decision head + calibration config |

## Honest limits

- **3-class only.** Anything beyond `positive / negative / neutral` (intensity, topic, aspect) needs a different fine-tune or a `score` / `noul` question — both are still in the underlying checkpoint but were not trained here.
- **Out-of-distribution drift.** Trained on FinGPT-sentiment-train distribution (news/tweets). Earnings calls, analyst reports, regulatory filings will be OOD; expect calibration drift. Refit temperatures per your domain before trusting the probabilities (the upstream [fine-tuning notebook](https://github.com/NandhaKishorM/laya/blob/main/notebooks/laya_finetune_typed_decisions_2xT4_kaggle.ipynb) shows how).
- **No soft distribution comparison done.** Argmax accuracy is reported; soft ECE / Brier against gold distributions is not measured yet.

## Citation

Base model and training library: [Convai Innovations — Laya](https://github.com/NandhaKishorM/laya).

Dataset: derived from [FinGPT/fingpt-sentiment-train](https://huggingface.co/datasets/FinGPT/fingpt-sentiment-train), collapsed to 3 classes and uploaded as [`shanaka95/fingpt-sentiment-3class`](https://huggingface.co/datasets/shanaka95/fingpt-sentiment-3class).

Apache 2.0.
