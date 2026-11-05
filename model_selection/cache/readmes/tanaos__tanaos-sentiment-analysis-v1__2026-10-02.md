---
language: multilingual
license: mit
tags:
- text-classification
- sentiment-analysis
- nlp
- sentiment-classification
- small-model
- synthetic-data
- tanaos
- artifex
base_model:
- microsoft/Multilingual-MiniLM-L12-H384
datasets:
- tanaos/synthetic-sentiment-analysis-dataset-v1
library_name: transformers
---

<p align="center">
    <img src="https://raw.githubusercontent.com/tanaos/.github/master/assets/logo.png" width="250px" alt="Tanaos – Train task specific LLMs without training data, for offline NLP and Text Classification">
</p>

# tanaos-sentiment-analysis-v1: A small but performant sentiment analysis model

This model was created by Tanaos with the [Artifex Python library](https://github.com/tanaos/artifex).

This is a **sentiment analysis model** based on [microsoft/Multilingual-MiniLM-L12-H384](https://huggingface.co/microsoft/Multilingual-MiniLM-L12-H384) and fine-tuned on [a synthetic dataset](https://huggingface.co/datasets/tanaos/synthetic-sentiment-analysis-dataset-v1) to classify text as one of the following labels:
- `very_negative`
- `negative`
- `neutral`
- `positive`
- `very_positive`

`neutral` is the default label for text that is either factual or does not express a clear sentiment.

This model can be used to classify text belonging to any domain, including but not limited to:
- Product reviews
- Movie reviews
- Social media posts
- Customer feedback

## How to Use

Use this model through the [Artifex library](https://github.com/tanaos/artifex):

install Artifex with

```bash
pip install artifex
```

use the model with

```python
from artifex import Artifex

sentiment_analysis = Artifex().sentiment_analysis()

label = sentiment_analysis("While the battery life is average, the camera quality is good.")
print(label)

# >>> [{'label': 'neutral', 'score': 0.9254}]
```

## Model Description

- **Base model:** `microsoft/Multilingual-MiniLM-L12-H384`
- **Task:** Text classification (sentiment analysis)
- **Languages:** English
- **Fine-tuning data:** A synthetic, custom dataset of passages labeled with one of the following sentiments: `very_negative`, `negative`, `neutral`, `positive`, `very_positive`.

## Training Details

This model was trained using the [Artifex Python library](https://github.com/tanaos/artifex)

```bash
pip install artifex
```

by providing the following instructions and generating 10,000 synthetic training samples:

```python
from artifex import Artifex


sa = Artifex().sentiment_analysis()

sa.train(
    domain="general",
    num_samples=10000
)
```

## Intended Uses

This model is intended to:
- Classify sentiment in text from various domains, including product reviews, social media posts, customer feedback and more.
- Provide a lightweight alternative for sentiment analysis tasks.

Not intended for:
- Analyzing highly specialized or technical text without further fine-tuning.