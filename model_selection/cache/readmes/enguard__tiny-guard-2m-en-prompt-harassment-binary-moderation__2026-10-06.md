---
base_model: minishlab/potion-base-2m
datasets:
- enguard/multi-lingual-prompt-moderation
library_name: model2vec
license: mit
model_name: enguard/tiny-guard-2m-en-prompt-harassment-binary-moderation
tags:
- static-embeddings
- text-classification
- model2vec
---

# enguard/tiny-guard-2m-en-prompt-harassment-binary-moderation

This model is a fine-tuned Model2Vec classifier based on [minishlab/potion-base-2m](https://huggingface.co/minishlab/potion-base-2m) for the prompt-harassment-binary found in the [enguard/multi-lingual-prompt-moderation](https://huggingface.co/datasets/enguard/multi-lingual-prompt-moderation) dataset.



## Installation

```bash
pip install model2vec[inference]
```

## Usage

```python
from model2vec.inference import StaticModelPipeline

model = StaticModelPipeline.from_pretrained(
  "enguard/tiny-guard-2m-en-prompt-harassment-binary-moderation"
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
| Classifies | prompt-harassment-binary |
| Base Model | [minishlab/potion-base-2m](https://huggingface.co/minishlab/potion-base-2m) |
| Precision | 0.8788 |
| Recall | 0.7180 |
| F1 | 0.7903 |

### Confusion Matrix

| True \ Predicted | FAIL | PASS |
| --- | --- | --- |
| **FAIL** | 1421 | 563 |
| **PASS** | 196 | 1788 |

<details>
<summary><b>Full metrics (JSON)</b></summary>

```json
{
  "FAIL": {
    "precision": 0.8787878787878788,
    "recall": 0.7180394138453765,
    "f1-score": 0.7903225806451613,
    "support": 1979.0
  },
  "PASS": {
    "precision": 0.7605150214592274,
    "recall": 0.9004065040650406,
    "f1-score": 0.8245695672405771,
    "support": 1968.0
  },
  "accuracy": 0.8089688370914618,
  "macro avg": {
    "precision": 0.8196514501235531,
    "recall": 0.8092229589552086,
    "f1-score": 0.8074460739428692,
    "support": 3947.0
  },
  "weighted avg": {
    "precision": 0.8198162590202613,
    "recall": 0.8089688370914618,
    "f1-score": 0.8073983520208335,
    "support": 3947.0
  }
}
```
</details>


<details>
<summary><b>Sample Predictions</b></summary>

| Text | True Label | Predicted Label |
|------|------------|-----------------|
| you don't have much experience with european gypsies, do you? <br><br>Touch one, and they spawn cousins all around you like an RPG boss. | FAIL | FAIL |
| 良い、悪天候時butthole! | FAIL | FAIL |
| I know what you are thinking....but where will he build the fire for the smoke signals? | PASS | PASS |
| Not really even an "unnatural" disaster.  Oil comes from the earth, water comes from the earth.  Its inevitable that they will find each other.   | PASS | PASS |
| You don't even know what you were quoting, do you? You just saw it on the internet somewhere and decided to parrot it here on reddit for karma. <br><br>Nicely done, I'll give you a C for effort, but you should try harder next time.<br><br> | FAIL | FAIL |
| you don't have much experience with european gypsies, do you? <br><br>Touch one, and they spawn cousins all around you like an RPG boss. | FAIL | FAIL |
</details>


<details>
<summary><b>Prediction Speed Benchmarks</b></summary>

| Dataset Size | Time (seconds) | Predictions/Second |
|--------------|----------------|---------------------|
| 1 | 0.0002 | 4928.68 |
| 1000 | 0.0504 | 19859.39 |
| 3968 | 0.2013 | 19709.62 |
</details>


## Other model variants

Below is a general overview of the best-performing models for each dataset variant.

| Classifies | Model | Precision | Recall | F1 |
| --- | --- | --- | --- | --- |
| prompt-harassment-binary | [enguard/tiny-guard-2m-en-prompt-harassment-binary-moderation](https://huggingface.co/enguard/tiny-guard-2m-en-prompt-harassment-binary-moderation) | 0.8788 | 0.7180 | 0.7903 |
| prompt-harmfulness-binary | [enguard/tiny-guard-2m-en-prompt-harmfulness-binary-moderation](https://huggingface.co/enguard/tiny-guard-2m-en-prompt-harmfulness-binary-moderation) | 0.8543 | 0.7256 | 0.7847 |
| prompt-harmfulness-multilabel | [enguard/tiny-guard-2m-en-prompt-harmfulness-multilabel-moderation](https://huggingface.co/enguard/tiny-guard-2m-en-prompt-harmfulness-multilabel-moderation) | 0.7687 | 0.5006 | 0.6064 |
| prompt-hate-speech-binary | [enguard/tiny-guard-2m-en-prompt-hate-speech-binary-moderation](https://huggingface.co/enguard/tiny-guard-2m-en-prompt-hate-speech-binary-moderation) | 0.9141 | 0.7269 | 0.8098 |
| prompt-self-harm-binary | [enguard/tiny-guard-2m-en-prompt-self-harm-binary-moderation](https://huggingface.co/enguard/tiny-guard-2m-en-prompt-self-harm-binary-moderation) | 0.8929 | 0.7143 | 0.7937 |
| prompt-sexual-content-binary | [enguard/tiny-guard-2m-en-prompt-sexual-content-binary-moderation](https://huggingface.co/enguard/tiny-guard-2m-en-prompt-sexual-content-binary-moderation) | 0.9256 | 0.8141 | 0.8663 |
| prompt-violence-binary | [enguard/tiny-guard-2m-en-prompt-violence-binary-moderation](https://huggingface.co/enguard/tiny-guard-2m-en-prompt-violence-binary-moderation) | 0.9017 | 0.7645 | 0.8275 |
| prompt-harassment-binary | [enguard/tiny-guard-4m-en-prompt-harassment-binary-moderation](https://huggingface.co/enguard/tiny-guard-4m-en-prompt-harassment-binary-moderation) | 0.8895 | 0.7160 | 0.7934 |
| prompt-harmfulness-binary | [enguard/tiny-guard-4m-en-prompt-harmfulness-binary-moderation](https://huggingface.co/enguard/tiny-guard-4m-en-prompt-harmfulness-binary-moderation) | 0.8565 | 0.7540 | 0.8020 |
| prompt-harmfulness-multilabel | [enguard/tiny-guard-4m-en-prompt-harmfulness-multilabel-moderation](https://huggingface.co/enguard/tiny-guard-4m-en-prompt-harmfulness-multilabel-moderation) | 0.7924 | 0.5663 | 0.6606 |
| prompt-hate-speech-binary | [enguard/tiny-guard-4m-en-prompt-hate-speech-binary-moderation](https://huggingface.co/enguard/tiny-guard-4m-en-prompt-hate-speech-binary-moderation) | 0.9198 | 0.7831 | 0.8460 |
| prompt-self-harm-binary | [enguard/tiny-guard-4m-en-prompt-self-harm-binary-moderation](https://huggingface.co/enguard/tiny-guard-4m-en-prompt-self-harm-binary-moderation) | 0.9062 | 0.8286 | 0.8657 |
| prompt-sexual-content-binary | [enguard/tiny-guard-4m-en-prompt-sexual-content-binary-moderation](https://huggingface.co/enguard/tiny-guard-4m-en-prompt-sexual-content-binary-moderation) | 0.9371 | 0.8468 | 0.8897 |
| prompt-violence-binary | [enguard/tiny-guard-4m-en-prompt-violence-binary-moderation](https://huggingface.co/enguard/tiny-guard-4m-en-prompt-violence-binary-moderation) | 0.8851 | 0.8370 | 0.8603 |
| prompt-harassment-binary | [enguard/tiny-guard-8m-en-prompt-harassment-binary-moderation](https://huggingface.co/enguard/tiny-guard-8m-en-prompt-harassment-binary-moderation) | 0.8895 | 0.7767 | 0.8292 |
| prompt-harmfulness-binary | [enguard/tiny-guard-8m-en-prompt-harmfulness-binary-moderation](https://huggingface.co/enguard/tiny-guard-8m-en-prompt-harmfulness-binary-moderation) | 0.8627 | 0.7912 | 0.8254 |
| prompt-harmfulness-multilabel | [enguard/tiny-guard-8m-en-prompt-harmfulness-multilabel-moderation](https://huggingface.co/enguard/tiny-guard-8m-en-prompt-harmfulness-multilabel-moderation) | 0.7902 | 0.5926 | 0.6773 |
| prompt-hate-speech-binary | [enguard/tiny-guard-8m-en-prompt-hate-speech-binary-moderation](https://huggingface.co/enguard/tiny-guard-8m-en-prompt-hate-speech-binary-moderation) | 0.9152 | 0.8233 | 0.8668 |
| prompt-self-harm-binary | [enguard/tiny-guard-8m-en-prompt-self-harm-binary-moderation](https://huggingface.co/enguard/tiny-guard-8m-en-prompt-self-harm-binary-moderation) | 0.9667 | 0.8286 | 0.8923 |
| prompt-sexual-content-binary | [enguard/tiny-guard-8m-en-prompt-sexual-content-binary-moderation](https://huggingface.co/enguard/tiny-guard-8m-en-prompt-sexual-content-binary-moderation) | 0.9382 | 0.8881 | 0.9125 |
| prompt-violence-binary | [enguard/tiny-guard-8m-en-prompt-violence-binary-moderation](https://huggingface.co/enguard/tiny-guard-8m-en-prompt-violence-binary-moderation) | 0.9042 | 0.8551 | 0.8790 |
| prompt-harassment-binary | [enguard/small-guard-32m-en-prompt-harassment-binary-moderation](https://huggingface.co/enguard/small-guard-32m-en-prompt-harassment-binary-moderation) | 0.8809 | 0.7964 | 0.8365 |
| prompt-harmfulness-binary | [enguard/small-guard-32m-en-prompt-harmfulness-binary-moderation](https://huggingface.co/enguard/small-guard-32m-en-prompt-harmfulness-binary-moderation) | 0.8548 | 0.8239 | 0.8391 |
| prompt-harmfulness-multilabel | [enguard/small-guard-32m-en-prompt-harmfulness-multilabel-moderation](https://huggingface.co/enguard/small-guard-32m-en-prompt-harmfulness-multilabel-moderation) | 0.8065 | 0.6494 | 0.7195 |
| prompt-hate-speech-binary | [enguard/small-guard-32m-en-prompt-hate-speech-binary-moderation](https://huggingface.co/enguard/small-guard-32m-en-prompt-hate-speech-binary-moderation) | 0.9207 | 0.8394 | 0.8782 |
| prompt-self-harm-binary | [enguard/small-guard-32m-en-prompt-self-harm-binary-moderation](https://huggingface.co/enguard/small-guard-32m-en-prompt-self-harm-binary-moderation) | 0.9333 | 0.8000 | 0.8615 |
| prompt-sexual-content-binary | [enguard/small-guard-32m-en-prompt-sexual-content-binary-moderation](https://huggingface.co/enguard/small-guard-32m-en-prompt-sexual-content-binary-moderation) | 0.9328 | 0.8847 | 0.9081 |
| prompt-violence-binary | [enguard/small-guard-32m-en-prompt-violence-binary-moderation](https://huggingface.co/enguard/small-guard-32m-en-prompt-violence-binary-moderation) | 0.9077 | 0.8913 | 0.8995 |
| prompt-harassment-binary | [enguard/medium-guard-128m-xx-prompt-harassment-binary-moderation](https://huggingface.co/enguard/medium-guard-128m-xx-prompt-harassment-binary-moderation) | 0.8660 | 0.8034 | 0.8336 |
| prompt-harmfulness-binary | [enguard/medium-guard-128m-xx-prompt-harmfulness-binary-moderation](https://huggingface.co/enguard/medium-guard-128m-xx-prompt-harmfulness-binary-moderation) | 0.8457 | 0.8074 | 0.8261 |
| prompt-harmfulness-multilabel | [enguard/medium-guard-128m-xx-prompt-harmfulness-multilabel-moderation](https://huggingface.co/enguard/medium-guard-128m-xx-prompt-harmfulness-multilabel-moderation) | 0.7795 | 0.6516 | 0.7098 |
| prompt-hate-speech-binary | [enguard/medium-guard-128m-xx-prompt-hate-speech-binary-moderation](https://huggingface.co/enguard/medium-guard-128m-xx-prompt-hate-speech-binary-moderation) | 0.8826 | 0.8153 | 0.8476 |
| prompt-self-harm-binary | [enguard/medium-guard-128m-xx-prompt-self-harm-binary-moderation](https://huggingface.co/enguard/medium-guard-128m-xx-prompt-self-harm-binary-moderation) | 0.9375 | 0.8571 | 0.8955 |
| prompt-sexual-content-binary | [enguard/medium-guard-128m-xx-prompt-sexual-content-binary-moderation](https://huggingface.co/enguard/medium-guard-128m-xx-prompt-sexual-content-binary-moderation) | 0.9153 | 0.8744 | 0.8944 |
| prompt-violence-binary | [enguard/medium-guard-128m-xx-prompt-violence-binary-moderation](https://huggingface.co/enguard/medium-guard-128m-xx-prompt-violence-binary-moderation) | 0.8821 | 0.8406 | 0.8609 |

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