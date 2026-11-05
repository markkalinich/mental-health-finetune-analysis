---
base_model: minishlab/potion-base-2m
datasets:
- lmsys/toxic-chat
library_name: model2vec
license: mit
model_name: enguard/tiny-guard-2m-en-prompt-toxicity-toxic-chat
tags:
- static-embeddings
- text-classification
- model2vec
---

# enguard/tiny-guard-2m-en-prompt-toxicity-toxic-chat

This model is a fine-tuned Model2Vec classifier based on [minishlab/potion-base-2m](https://huggingface.co/minishlab/potion-base-2m) for the prompt-toxicity found in the [lmsys/toxic-chat](https://huggingface.co/datasets/lmsys/toxic-chat) dataset.



## Installation

```bash
pip install model2vec[inference]
```

## Usage

```python
from model2vec.inference import StaticModelPipeline

model = StaticModelPipeline.from_pretrained(
  "enguard/tiny-guard-2m-en-prompt-toxicity-toxic-chat"
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
| Classifies | prompt-toxicity |
| Base Model | [minishlab/potion-base-2m](https://huggingface.co/minishlab/potion-base-2m) |
| Precision | 0.5820 |
| Precision | 0.5820 |
| Recall | 0.7801 |
| F1 | 0.6667 |

### Confusion Matrix

| | FAIL | PASS |
| --- | --- | --- |
| **FAIL** | 149 | 42 |
| **PASS** | 111 | 2240 |

<details>
<summary><b>Full metrics (JSON)</b></summary>

```json
{
  "FAIL": {
    "precision": 0.58203125,
    "recall": 0.7801047120418848,
    "f1-score": 0.6666666666666666,
    "support": 191.0
  },
  "PASS": {
    "precision": 0.9814241486068112,
    "recall": 0.9539982803095443,
    "f1-score": 0.9675168955744495,
    "support": 2326.0
  },
  "accuracy": 0.9408025427095749,
  "macro avg": {
    "precision": 0.7817276993034056,
    "recall": 0.8670514961757145,
    "f1-score": 0.817091781120558,
    "support": 2517.0
  },
  "weighted avg": {
    "precision": 0.9511166223319202,
    "recall": 0.9408025427095749,
    "f1-score": 0.944687180150776,
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
| 1 | 0.0002 | 4346.43 |
| 1000 | 0.0678 | 14749.51 |
| 2542 | 0.1606 | 15828.34 |
</details>


## Other model variants

Below is a general overview of the best-performing models for each dataset variant.

| Classifies | Model | Precision | Recall | F1 |
| --- | --- | --- | --- | --- |
| prompt-toxicity | [enguard/tiny-guard-2m-en-prompt-toxicity-toxic-chat](https://huggingface.co/enguard/tiny-guard-2m-en-prompt-toxicity-toxic-chat) | 0.5820 | 0.7801 | 0.6667 |
| prompt-toxicity | [enguard/tiny-guard-4m-en-prompt-toxicity-toxic-chat](https://huggingface.co/enguard/tiny-guard-4m-en-prompt-toxicity-toxic-chat) | 0.6549 | 0.7749 | 0.7098 |
| prompt-toxicity | [enguard/tiny-guard-8m-en-prompt-toxicity-toxic-chat](https://huggingface.co/enguard/tiny-guard-8m-en-prompt-toxicity-toxic-chat) | 0.6471 | 0.7487 | 0.6942 |
| prompt-toxicity | [enguard/small-guard-32m-en-prompt-toxicity-toxic-chat](https://huggingface.co/enguard/small-guard-32m-en-prompt-toxicity-toxic-chat) | 0.6852 | 0.7749 | 0.7273 |
| prompt-toxicity | [enguard/medium-guard-128m-xx-prompt-toxicity-toxic-chat](https://huggingface.co/enguard/medium-guard-128m-xx-prompt-toxicity-toxic-chat) | 0.6129 | 0.7958 | 0.6925 |

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