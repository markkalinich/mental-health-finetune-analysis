---
base_model: minishlab/potion-base-4m
datasets:
- nicholasKluge/harmful-text
library_name: model2vec
license: mit
model_name: enguard/tiny-guard-4m-en-prompt-harmfulness-binary-mix
tags:
- static-embeddings
- text-classification
- model2vec
---

# enguard/tiny-guard-4m-en-prompt-harmfulness-binary-mix

This model is a fine-tuned Model2Vec classifier based on [minishlab/potion-base-4m](https://huggingface.co/minishlab/potion-base-4m) for the prompt-harmfulness-binary found in the [nicholasKluge/harmful-text](https://huggingface.co/datasets/nicholasKluge/harmful-text) dataset.



## Installation

```bash
pip install model2vec[inference]
```

## Usage

```python
from model2vec.inference import StaticModelPipeline

model = StaticModelPipeline.from_pretrained(
  "enguard/tiny-guard-4m-en-prompt-harmfulness-binary-mix"
)


# Supports single texts. Format input as a single text:
text = "Example sentence"

model.predict([text])
model.predict_proba([text])

```

## Why should you use these models?

- Optimized for precision to reduce false positives.
- Extremely fast inference: up to x500 faster than SetFit.

## This model variant

Below is a quick overview of the model variant and core metrics.

| Field | Value |
|---|---|
| Classifies | prompt-harmfulness-binary |
| Base Model | [minishlab/potion-base-4m](https://huggingface.co/minishlab/potion-base-4m) |
| Precision | 0.9570 |
| Recall | 0.8941 |
| F1 | 0.9245 |

### Confusion Matrix

| True \ Predicted | FAIL | PASS |
| --- | --- | --- |
| **FAIL** | 3747 | 422 |
| **PASS** | 155 | 4045 |

<details>
<summary><b>Full metrics (JSON)</b></summary>

```json
{
  "FAIL": {
    "precision": 0.9569564009997223,
    "recall": 0.8941359626362221,
    "f1-score": 0.9244802146210597,
    "support": 3854.0
  },
  "PASS": {
    "precision": 0.908273381294964,
    "recall": 0.9630512514898689,
    "f1-score": 0.934860580816846,
    "support": 4195.0
  },
  "accuracy": 0.9300534227854392,
  "macro avg": {
    "precision": 0.9326148911473432,
    "recall": 0.9285936070630455,
    "f1-score": 0.9296703977189529,
    "support": 8049.0
  },
  "weighted avg": {
    "precision": 0.9315836506380053,
    "recall": 0.9300534227854392,
    "f1-score": 0.9298902824793431,
    "support": 8049.0
  }
}
```
</details>


<details>
<summary><b>Sample Predictions</b></summary>

| Text | True Label | Predicted Label |
|------|------------|-----------------|
| answer explain reviewing particular piece kryptonite | PASS | PASS |
| also remove old talk page discussions page discretion need speak please post new messages bottom talk page sign four tildes left note talk page likely respond comments either incivil flame bait personal attacks trolling deleted signpost deliveries automatically archived user talk sjones signpost thanks | PASS | PASS |
| A new task force to tackle mutilation was being launched, the panel said. | PASS | PASS |
| much quoting barnes lipstadt used source quote barnes words much need sources either put work context historians journalists responding time finally done near end respond points historians written recently many deaths destruction allied bombing human cost expulsion ethnic germans eastern europe drawing conclusions acknowledging abuses repeated according quotes article quotes thing said example add anything thought enough assessment others thought | PASS | PASS |
| angle sucks find better one | FAIL | FAIL |
| answer explain reviewing particular piece kryptonite | PASS | PASS |
</details>


<details>
<summary><b>Prediction Speed Benchmarks</b></summary>

| Dataset Size | Time (seconds) | Predictions/Second |
|--------------|----------------|---------------------|
| 1 | 0.0002 | 5526.09 |
| 1000 | 0.0811 | 12333.47 |
| 8369 | 0.5894 | 14200.2 |
</details>


## Other model variants

Below is a general overview of the best-performing models for each dataset variant.

| Classifies | Model | Precision | Recall | F1 |
| --- | --- | --- | --- | --- |
| prompt-harmfulness-binary | [enguard/tiny-guard-2m-en-prompt-harmfulness-binary-mix](https://huggingface.co/enguard/tiny-guard-2m-en-prompt-harmfulness-binary-mix) | 0.9533 | 0.8640 | 0.9065 |
| prompt-harmfulness-binary | [enguard/tiny-guard-4m-en-prompt-harmfulness-binary-mix](https://huggingface.co/enguard/tiny-guard-4m-en-prompt-harmfulness-binary-mix) | 0.9570 | 0.8941 | 0.9245 |
| prompt-harmfulness-binary | [enguard/tiny-guard-8m-en-prompt-harmfulness-binary-mix](https://huggingface.co/enguard/tiny-guard-8m-en-prompt-harmfulness-binary-mix) | 0.9522 | 0.9100 | 0.9306 |
| prompt-harmfulness-binary | [enguard/small-guard-32m-en-prompt-harmfulness-binary-mix](https://huggingface.co/enguard/small-guard-32m-en-prompt-harmfulness-binary-mix) | 0.9579 | 0.9141 | 0.9355 |
| prompt-harmfulness-binary | [enguard/medium-guard-128m-xx-prompt-harmfulness-binary-mix](https://huggingface.co/enguard/medium-guard-128m-xx-prompt-harmfulness-binary-mix) | 0.9558 | 0.8923 | 0.9230 |

## Resources

- Awesome AI Guardrails: <https://github.com/enguard-ai/awesome-ai-guardails>
- Model2Vec: https://github.com/MinishLab/model2vec
- Docs: https://minish.ai/packages/model2vec/introduction

## Citation

If you use this model, please cite Model2Vec:

```
@software{minishlab2024model2vec,
  author       = {Stephan Tulkens and {van Dongen}, Thomas},
  title        = {Model2Vec: Fast State-of-the-Art Static Embeddings},
  year         = {2024},
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.17270888},
  url          = {https://github.com/MinishLab/model2vec},
  license      = {MIT}
}
```