---
license: apache-2.0
language:
  - en
  - es
  - de
base_model: convaiinnovations/laya-multilingual
datasets:
  - tyqiangz/multilingual-sentiments
pipeline_tag: text-classification
library_name: laya
inference: false
tags:
  - decision-model
  - sentiment-analysis
  - multilingual
  - laya
  - experiment
  - data-scaling
metrics:
  - accuracy
  - ece
model-index:
  - name: laya-sentiment-multilingual-v2
    results:
      - task:
          type: text-classification
          name: Binary Sentiment Classification
        dataset:
          type: tyqiangz/multilingual-sentiments
          name: Multilingual Sentiments — full non-neutral test set (580 per language)
          split: test
        metrics:
          - type: accuracy
            value: 0.866
            name: Accuracy (n=1740)
            verified: false
          - type: ece
            value: 0.0465
            name: Expected Calibration Error, cross-fitted (n=1740)
            verified: false
---

# Laya Sentiment Multilingual v2 — data-scaling run (4,326 examples)

⚠️ **This is an experiment release, not an upgrade.** Same recipe as
[`Ramg77/laya-sentiment-multilingual`](https://huggingface.co/Ramg77/laya-sentiment-multilingual)
(v1) but trained on **4.8× the data**. It improves accuracy by less than one point on a
1,740-example test set and the difference is **not statistically significant** (McNemar
p = 0.46). It is published so the result can be checked, not because it should be used.
**Prefer v1 for anything real.**

## What was tested

The v1 model was trained on 900 examples while the source dataset is often described as
having 591k rows. That 591k figure is the dataset total across *all* languages: for EN/ES/DE
there are only 1,839 train + 324 validation rows per language. After removing the neutral
class, the EN/ES/DE pool is 1,442 examples per language.

v2 was trained on **4,326 examples** (1,442 per language) — a record-level superset of the 900
used by v1 — with the recipe deliberately unchanged: RLCD, LR 3e-5, batch 8, group size 4,
label smoothing 0.1, dropout 0.1, up to 15 epochs, early stopping with patience 4, and the same
checkpoint-selection criterion (best accuracy on the 300-example holdout). Seed 42.

## Results (paired, same examples)

| Subset | v1 (900) | **v2 (4,326)** | Difference | 95% CI | McNemar |
|---|---|---|---|---|---|
| Holdout 300 | 88.0% | 88.0% | +0.0 | [−0.038, +0.037] | 17/17, p = 1.0 |
| Clean 1,440 *(never used for selection)* | 85.6% | **86.3%** | +0.8 | [−0.011, +0.023] | 71/82, p = 0.42 |
| Full test 1,740 | 86.0% | **86.6%** | +0.6 | [−0.007, +0.021] | 88/99, p = 0.46 |

Per language on the full test set: EN 90.0%, DE 85.3%, ES 84.5%. Per class: positive 83.9%,
negative 89.3% — the extra data traded positive recall for negative recall.

## Training trajectory

| epoch | loss | train acc | holdout 300 | full test 1,740 | minutes |
|---|---|---|---|---|---|
| 1 | −0.0642 | 0.879 | 0.813 | 0.817 | 11.7 |
| **2** | −0.1413 | 0.963 | **0.880** | **0.866** | 23.1 |
| 3 | −0.2591 | 0.973 | 0.873 | 0.864 | 34.6 |
| 4 | −0.2996 | 0.972 | 0.870 | 0.857 | 46.1 |
| 5 | −0.3102 | 0.981 | 0.857 | 0.868 | 57.5 |
| 6 | −0.3370 | 0.975 | 0.867 | 0.856 | 69.0 |

The released checkpoint is **epoch 2**. Training accuracy keeps rising while validation falls:
the model memorised the training set.

## Why more data did not help

| | v1 | v2 |
|---|---|---|
| examples | 900 | 4,326 |
| batches per epoch (batch 8) | 113 | 541 |
| best epoch | 1 | 2 |
| optimizer steps at the best checkpoint | **113** | **~1,082** |

Same hyperparameters is not the same training: the best v2 checkpoint saw ~9.6× more gradient
steps at a constant learning rate of 3e-5. The bottleneck is the training recipe (constant LR,
the whole encoder trainable, no scheduler), not the volume of data.

## Calibration (worse than v1)

`calibration.json` fits T = 1.35 on the 300-example holdout (v1 needs only 0.9):

| | ECE @T=1 | ECE @ shipped T | ECE cross-fitted |
|---|---|---|---|
| Holdout 300 | 0.0600 | 0.0480 (T=1.35) | — |
| Full test 1,740 | 0.0756 | 0.0473 (T=1.35) | 0.0465 (T folds 1.45–1.5) |

The model is markedly **more confident and less calibrated** than v1 (which reports ECE 0.0338
at T=0.9 on the same 1,740 examples). Practical consequence: a confidence gate at 0.75 would
delegate only **1.8%** of cases with v2 versus **12.1%** with v1. An overconfident model
silently defeats a confidence threshold.

## Details

- Weights: `model.safetensors`, 643,835,524 bytes, sha256 `9f79ac8f9e518d210af4f6f51458d3562d8149935e63c9623831cf4d20fb8142`
- Base model: `convaiinnovations/laya-multilingual` (322M params, mmBERT-base)
- Task: binary sentiment via the `noul` primitive; neutral class removed
- Languages: EN, ES, DE only (Latin script)
- No CoreML conversion is provided for this checkpoint
- License: Apache 2.0

## Usage

```python
import laya

agent = laya.load("Ramg77/laya-sentiment-multilingual-v2")
result = agent.predict(
    "I love this product, it changed my life!",
    {"sentiment": {"type": "noul",
                   "instructions": "Does this text express positive sentiment?"}}
)
print(result["answers"]["sentiment"])
```

Set `USE_TF=0` if TensorFlow is installed in the same environment (abseil can deadlock Laya's
model initialisation).

## Reproduce

Everything is in the main repository, under `experiments/data-scaling/`:

- `train_v2.jsonl` — the 4,326-example training set
- `train_v2.py` — the training script (`python train_v2.py`, ~70 min on Apple Silicon MPS)
- `compare_v1_v2.py` — the paired comparison with McNemar and bootstrap intervals
- `results/train_v2_log.jsonl`, `results/compare_v1_v2.json` — raw logs

Evaluation uses `eval_sentiment.py` and `split/test_extended.jsonl` from the main repository.

## Limitations

- **Not better than v1.** Use v1 unless you specifically need to reproduce this experiment.
- **Worse calibrated** than v1 and more confident, which breaks confidence-based gating.
- Binary only; EN/ES/DE only; short social-media text; not validated on formal text.
- One seed only: this experiment rules out large effects, not differences under one point.
- Do not use for high-stakes decisions or for routing/escalation.

## Citation

```bibtex
@misc{laya-sentiment-multilingual-v2,
  author = {Ramg77},
  title = {Laya Sentiment Multilingual v2 — data-scaling run (4,326 examples)},
  year = {2026},
  publisher = {Hugging Face}
}
```

## Acknowledgments

- Laya by Nandha Kishor M and Convai Innovations — Apache 2.0.
- multilingual-sentiments by tyqiangz — Apache 2.0.
