---
language: en
license: mit
tags:
- text-classification
- emotion-detection
- chatbot
- nlp
- small-model
- synthetic-data
- tanaos
- artifex
base_model:
- microsoft/Multilingual-MiniLM-L12-H384
datasets:
- tanaos/synthetic-emotion-detection-dataset-v1
library_name: transformers
---

<p align="center">
    <img src="https://raw.githubusercontent.com/tanaos/.github/master/assets/logo.png" width="250px" alt="Tanaos – Train task specific LLMs without training data, for offline NLP and Text Classification">
</p>

# tanaos-emotion-detection-v1: A small but performant emotion detection model

This model was created by Tanaos with the [Artifex Python library](https://github.com/tanaos/artifex).

This is an **emotion detection model** based on [microsoft/Multilingual-MiniLM-L12-H384](https://huggingface.co/microsoft/Multilingual-MiniLM-L12-H384) and fine-tuned on [a synthetic dataset](https://huggingface.co/datasets/tanaos/synthetic-emotion-detection-dataset-v1) to classify the main emotion expressed in any text input into one of the following categories:

| Label | Description |
|---------|-------------|
| `joy` | Text that expresses happiness or positivity |
| `anger` | Text that expresses anger or frustration |
| `fear` | Text that expresses fear or anxiety |
| `sadness` | Text that expresses sadness or sorrow |
| `surprise` | Text that expresses surprise or shock |
| `disgust` | Text that expresses disgust or revulsion |
| `excitement` | Text that expresses excitement or enthusiasm |
| `neutral` | Text that either expresses a neutral or indifferent emotion, or that does not express any emotion at all on account of being purely factual or descriptive |

`neutral` is the default label for text that is either factual or does not express a clear emotion.

These categories were chosen to cover a wide range of common emotions in text, in order to create a versatile and general-purpose emotion detection model, applicable across various industries and use cases.

This model can be used to analyze customer feedback, social media posts, reviews, and other text data to gain insights into the emotional tone and sentiment expressed by users.

## How to Use

Use this model through the [Artifex library](https://github.com/tanaos/artifex):

install Artifex with

```bash
pip install artifex
```

use the model with

```python
from artifex import Artifex

emotion_detection = Artifex().emotion_detection()

print(emotion_detection("I can't wait for the concert tonight!"))

# >>> [{'label': 'excitement', 'score': 0.9941}]
```

## Model Description

- **Base model:** `microsoft/Multilingual-MiniLM-L12-H384`
- **Task:** Text classification (emotion detection)
- **Languages:** English
- **Fine-tuning data:** A synthetic, custom dataset of 10,000 utterances, each belonging to one of 12 different emotion categories.

## Training Details

This model was trained using the [Artifex Python library](https://github.com/tanaos/artifex)

```bash
pip install artifex
```

by providing the following instructions and generating 10,000 synthetic training samples:

```python
from artifex import Artifex

ed = Artifex().emotion_detection()

ed.train(
    domain="general",
    classes={
        "joy": "text that expresses happiness or positivity",
        "anger": "text that expresses anger or frustration",
        "fear": "text that expresses fear or anxiety",
        "sadness": "text that expresses sadness or sorrow",
        "surprise": "text that expresses surprise or shock",
        "disgust": "text that expresses disgust or revulsion",
        "excitement": "text that expresses excitement or enthusiasm",
        "neutral": "text that either expresses a neutral or indifferent emotion, or that does not express any emotion at all on account of being purely factual or descriptive."
    },
    num_samples=10000
)
```

## Intended Uses

This model is intended to:
- Classify the emotional tone of text inputs across multiple languages.
- Be used in applications such as customer feedback analysis, social media monitoring, and sentiment analysis.
- Serve as a lightweight alternative to larger models for emotion detection tasks.

Not intended for:
- Highly specialized domains where emotions differ significantly from the predefined categories.