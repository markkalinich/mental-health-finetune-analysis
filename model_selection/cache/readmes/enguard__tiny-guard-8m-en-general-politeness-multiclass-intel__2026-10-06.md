---
base_model: minishlab/potion-base-8m
datasets:
- Intel/polite-guard
library_name: model2vec
license: mit
model_name: enguard/tiny-guard-8m-en-general-politeness-multiclass-intel
tags:
- static-embeddings
- text-classification
- model2vec
---

# enguard/tiny-guard-8m-en-general-politeness-multiclass-intel

This model is a fine-tuned Model2Vec classifier based on [minishlab/potion-base-8m](https://huggingface.co/minishlab/potion-base-8m) for the general-politeness-multiclass found in the [Intel/polite-guard](https://huggingface.co/datasets/Intel/polite-guard) dataset.



## Installation

```bash
pip install model2vec[inference]
```

## Usage

```python
from model2vec.inference import StaticModelPipeline

model = StaticModelPipeline.from_pretrained(
  "enguard/tiny-guard-8m-en-general-politeness-multiclass-intel"
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
| Classifies | general-politeness-multiclass |
| Base Model | [minishlab/potion-base-8m](https://huggingface.co/minishlab/potion-base-8m) |
| Precision | 0.9873 |
| Recall | 0.9795 |
| F1 | 0.9833 |

### Confusion Matrix

| True \ Predicted | impolite | neutral | polite | somewhat polite |
| --- | --- | --- | --- | --- |
| **impolite** | 2480 | 30 | 2 | 20 |
| **neutral** | 14 | 2273 | 67 | 199 |
| **polite** | 3 | 80 | 2205 | 279 |
| **somewhat polite** | 15 | 182 | 206 | 2145 |

<details>
<summary><b>Full metrics (JSON)</b></summary>

```json
{
  "impolite": {
    "precision": 0.9872611464968153,
    "recall": 0.9794628751974723,
    "f1-score": 0.9833465503568596,
    "support": 2532.0
  },
  "neutral": {
    "precision": 0.8861598440545809,
    "recall": 0.890325107716412,
    "f1-score": 0.8882375928096913,
    "support": 2553.0
  },
  "polite": {
    "precision": 0.8891129032258065,
    "recall": 0.8589793533307363,
    "f1-score": 0.8737864077669902,
    "support": 2567.0
  },
  "somewhat polite": {
    "precision": 0.811577752553916,
    "recall": 0.8418367346938775,
    "f1-score": 0.826430360238875,
    "support": 2548.0
  },
  "accuracy": 0.8924509803921569,
  "macro avg": {
    "precision": 0.8935279115827797,
    "recall": 0.8926510177346245,
    "f1-score": 0.8929502277931041,
    "support": 10200.0
  },
  "weighted avg": {
    "precision": 0.8933690432244417,
    "recall": 0.8924509803921569,
    "f1-score": 0.8927704222130615,
    "support": 10200.0
  }
}
```
</details>


<details>
<summary><b>Sample Predictions</b></summary>

| Text | True Label | Predicted Label |
|------|------------|-----------------|
| I appreciate your interest in our vegetarian options. I can provide you with a list of our current dishes that cater to your dietary preferences. | somewhat polite | somewhat polite |
| I understand you're concerned about the ski lessons, and I'll look into the options for rescheduling. | somewhat polite | somewhat polite |
| Our technical skills course will cover the essential topics in data analysis, including data visualization and statistical modeling. The course materials will be available on our learning platform. | neutral | neutral |
| Our buffet hours are from 11 AM to 9 PM. Please note that we have a limited selection of options available during the lunch break. | neutral | neutral |
| I'll look into your policy details and see what options are available to you. | somewhat polite | somewhat polite |
| I appreciate your interest in our vegetarian options. I can provide you with a list of our current dishes that cater to your dietary preferences. | somewhat polite | somewhat polite |
</details>


<details>
<summary><b>Prediction Speed Benchmarks</b></summary>

| Dataset Size | Time (seconds) | Predictions/Second |
|--------------|----------------|---------------------|
| 1 | 0.001 | 1001.74 |
| 1000 | 0.0772 | 12952.54 |
| 10000 | 0.8414 | 11885.5 |
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