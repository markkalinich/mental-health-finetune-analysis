---
base_model: minishlab/potion-base-8m
datasets:
- Intel/polite-guard
library_name: model2vec
license: mit
model_name: enguard/tiny-guard-8m-en-general-politeness-binary-intel
tags:
- static-embeddings
- text-classification
- model2vec
---

# enguard/tiny-guard-8m-en-general-politeness-binary-intel

This model is a fine-tuned Model2Vec classifier based on [minishlab/potion-base-8m](https://huggingface.co/minishlab/potion-base-8m) for the general-politeness-binary found in the [Intel/polite-guard](https://huggingface.co/datasets/Intel/polite-guard) dataset.



## Installation

```bash
pip install model2vec[inference]
```

## Usage

```python
from model2vec.inference import StaticModelPipeline

model = StaticModelPipeline.from_pretrained(
  "enguard/tiny-guard-8m-en-general-politeness-binary-intel"
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
| Classifies | general-politeness-binary |
| Base Model | [minishlab/potion-base-8m](https://huggingface.co/minishlab/potion-base-8m) |
| Precision | 0.9828 |
| Recall | 0.9905 |
| F1 | 0.9866 |

### Confusion Matrix

| True \ Predicted | FAIL | PASS |
| --- | --- | --- |
| **FAIL** | 2508 | 24 |
| **PASS** | 44 | 7624 |

<details>
<summary><b>Full metrics (JSON)</b></summary>

```json
{
  "FAIL": {
    "precision": 0.9827586206896551,
    "recall": 0.990521327014218,
    "f1-score": 0.9866247049567269,
    "support": 2532.0
  },
  "PASS": {
    "precision": 0.9968619246861925,
    "recall": 0.9942618675013041,
    "f1-score": 0.9955601984852442,
    "support": 7668.0
  },
  "accuracy": 0.9933333333333333,
  "macro avg": {
    "precision": 0.9898102726879239,
    "recall": 0.992391597257761,
    "f1-score": 0.9910924517209856,
    "support": 10200.0
  },
  "weighted avg": {
    "precision": 0.9933609868705815,
    "recall": 0.9933333333333333,
    "f1-score": 0.9933420936211065,
    "support": 10200.0
  }
}
```
</details>


<details>
<summary><b>Sample Predictions</b></summary>

| Text | True Label | Predicted Label |
|------|------------|-----------------|
| I appreciate your interest in our vegetarian options. I can provide you with a list of our current dishes that cater to your dietary preferences. | PASS | PASS |
| I understand you're concerned about the ski lessons, and I'll look into the options for rescheduling. | PASS | PASS |
| Our technical skills course will cover the essential topics in data analysis, including data visualization and statistical modeling. The course materials will be available on our learning platform. | PASS | PASS |
| Our buffet hours are from 11 AM to 9 PM. Please note that we have a limited selection of options available during the lunch break. | PASS | PASS |
| I'll look into your policy details and see what options are available to you. | PASS | PASS |
| I appreciate your interest in our vegetarian options. I can provide you with a list of our current dishes that cater to your dietary preferences. | PASS | PASS |
</details>


<details>
<summary><b>Prediction Speed Benchmarks</b></summary>

| Dataset Size | Time (seconds) | Predictions/Second |
|--------------|----------------|---------------------|
| 1 | 0.0002 | 5461.33 |
| 1000 | 0.0603 | 16570.29 |
| 10000 | 0.6861 | 14575.2 |
</details>


## Other model variants

Below is a general overview of the best-performing models for each dataset variant.

| Classifies | Model | Precision | Recall | F1 |
| --- | --- | --- | --- | --- |
| general-politeness-binary | [enguard/tiny-guard-2m-en-general-politeness-binary-intel](https://huggingface.co/enguard/tiny-guard-2m-en-general-politeness-binary-intel) | 0.9843 | 0.9889 | 0.9866 |
| general-politeness-multiclass | [enguard/tiny-guard-2m-en-general-politeness-multiclass-intel](https://huggingface.co/enguard/tiny-guard-2m-en-general-politeness-multiclass-intel) | 0.9875 | 0.9704 | 0.9789 |
| general-politeness-binary | [enguard/tiny-guard-4m-en-general-politeness-binary-intel](https://huggingface.co/enguard/tiny-guard-4m-en-general-politeness-binary-intel) | 0.9831 | 0.9878 | 0.9854 |
| general-politeness-multiclass | [enguard/tiny-guard-4m-en-general-politeness-multiclass-intel](https://huggingface.co/enguard/tiny-guard-4m-en-general-politeness-multiclass-intel) | 0.9896 | 0.9783 | 0.9839 |
| general-politeness-binary | [enguard/tiny-guard-8m-en-general-politeness-binary-intel](https://huggingface.co/enguard/tiny-guard-8m-en-general-politeness-binary-intel) | 0.9828 | 0.9905 | 0.9866 |
| general-politeness-multiclass | [enguard/tiny-guard-8m-en-general-politeness-multiclass-intel](https://huggingface.co/enguard/tiny-guard-8m-en-general-politeness-multiclass-intel) | 0.9873 | 0.9795 | 0.9833 |
| general-politeness-binary | [enguard/small-guard-32m-en-general-politeness-binary-intel](https://huggingface.co/enguard/small-guard-32m-en-general-politeness-binary-intel) | 0.9858 | 0.9889 | 0.9874 |
| general-politeness-multiclass | [enguard/small-guard-32m-en-general-politeness-multiclass-intel](https://huggingface.co/enguard/small-guard-32m-en-general-politeness-multiclass-intel) | 0.9897 | 0.9862 | 0.9879 |
| general-politeness-binary | [enguard/medium-guard-128m-xx-general-politeness-binary-intel](https://huggingface.co/enguard/medium-guard-128m-xx-general-politeness-binary-intel) | 0.9831 | 0.9901 | 0.9866 |
| general-politeness-multiclass | [enguard/medium-guard-128m-xx-general-politeness-multiclass-intel](https://huggingface.co/enguard/medium-guard-128m-xx-general-politeness-multiclass-intel) | 0.9881 | 0.9870 | 0.9876 |

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