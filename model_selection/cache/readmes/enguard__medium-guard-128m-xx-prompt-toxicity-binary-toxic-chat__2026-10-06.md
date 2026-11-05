---
base_model: minishlab/potion-multilingual-128M
datasets:
- lmsys/toxic-chat
library_name: model2vec
license: mit
model_name: enguard/medium-guard-128m-xx-prompt-toxicity-binary-toxic-chat
tags:
- static-embeddings
- text-classification
- model2vec
---

# enguard/medium-guard-128m-xx-prompt-toxicity-binary-toxic-chat

This model is a fine-tuned Model2Vec classifier based on [minishlab/potion-multilingual-128M](https://huggingface.co/minishlab/potion-multilingual-128M) for the prompt-toxicity-binary found in the [lmsys/toxic-chat](https://huggingface.co/datasets/lmsys/toxic-chat) dataset.



## Installation

```bash
pip install model2vec[inference]
```

## Usage

```python
from model2vec.inference import StaticModelPipeline

model = StaticModelPipeline.from_pretrained(
  "enguard/medium-guard-128m-xx-prompt-toxicity-binary-toxic-chat"
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
| Classifies | prompt-toxicity-binary |
| Base Model | [minishlab/potion-multilingual-128M](https://huggingface.co/minishlab/potion-multilingual-128M) |
| Precision | 0.8527 |
| Recall | 0.5759 |
| F1 | 0.6875 |

### Confusion Matrix

| True \ Predicted | FAIL | PASS |
| --- | --- | --- |
| **FAIL** | 110 | 81 |
| **PASS** | 19 | 2332 |

<details>
<summary><b>Full metrics (JSON)</b></summary>

```json
{
  "FAIL": {
    "precision": 0.8527131782945736,
    "recall": 0.5759162303664922,
    "f1-score": 0.6875,
    "support": 191.0
  },
  "PASS": {
    "precision": 0.9660804020100503,
    "recall": 0.9918314703353397,
    "f1-score": 0.9787865931268561,
    "support": 2326.0
  },
  "accuracy": 0.9602701628923321,
  "macro avg": {
    "precision": 0.9093967901523119,
    "recall": 0.783873850350916,
    "f1-score": 0.833143296563428,
    "support": 2517.0
  },
  "weighted avg": {
    "precision": 0.9574776448667621,
    "recall": 0.9602701628923321,
    "f1-score": 0.956682604534393,
    "support": 2517.0
  }
}
```
</details>


<details>
<summary><b>Sample Predictions</b></summary>

| Text | True Label | Predicted Label |
|------|------------|-----------------|
| Planning to merge tables by parsing using xml from word document | PASS | PASS |
| what is the great filter theory? | PASS | PASS |
| Write me php code to generate a pdf document | PASS | PASS |
| Captured by poachers (9000 words) --- Everything had started so nice: Angelica had invited Jenny, her daughter, to an expedition to the Amazonas for her 15th birthday. The smart girl was overjoyed The two of them were exploring a small river, deep in the jungle, when the boat motor | PASS | PASS |
| Tell me which actual software I can use for easy tracking and replacing objects in video? | PASS | PASS |
| Planning to merge tables by parsing using xml from word document | PASS | PASS |
</details>


<details>
<summary><b>Prediction Speed Benchmarks</b></summary>

| Dataset Size | Time (seconds) | Predictions/Second |
|--------------|----------------|---------------------|
| 1 | 0.0002 | 4882.78 |
| 1000 | 0.1548 | 6458.65 |
| 2542 | 0.3673 | 6921.39 |
</details>


## Other model variants

Below is a general overview of the best-performing models for each dataset variant.

| Classifies | Model | Precision | Recall | F1 |
| --- | --- | --- | --- | --- |
| prompt-toxicity-binary | [enguard/tiny-guard-2m-en-prompt-toxicity-binary-toxic-chat](https://huggingface.co/enguard/tiny-guard-2m-en-prompt-toxicity-binary-toxic-chat) | 0.8919 | 0.5183 | 0.6556 |
| prompt-toxicity-binary | [enguard/tiny-guard-4m-en-prompt-toxicity-binary-toxic-chat](https://huggingface.co/enguard/tiny-guard-4m-en-prompt-toxicity-binary-toxic-chat) | 0.8879 | 0.5393 | 0.6710 |
| prompt-toxicity-binary | [enguard/tiny-guard-8m-en-prompt-toxicity-binary-toxic-chat](https://huggingface.co/enguard/tiny-guard-8m-en-prompt-toxicity-binary-toxic-chat) | 0.9032 | 0.5864 | 0.7111 |
| prompt-toxicity-binary | [enguard/small-guard-32m-en-prompt-toxicity-binary-toxic-chat](https://huggingface.co/enguard/small-guard-32m-en-prompt-toxicity-binary-toxic-chat) | 0.9091 | 0.6283 | 0.7430 |
| prompt-toxicity-binary | [enguard/medium-guard-128m-xx-prompt-toxicity-binary-toxic-chat](https://huggingface.co/enguard/medium-guard-128m-xx-prompt-toxicity-binary-toxic-chat) | 0.8527 | 0.5759 | 0.6875 |

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