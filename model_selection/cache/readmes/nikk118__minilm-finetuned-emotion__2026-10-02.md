---
language: en
license: apache-2.0
base_model: microsoft/MiniLM-L12-H384-uncased
pipeline_tag: text-classification
tags:
- emotion-classification
- transformers
- pytorch
- huggingface
- nlp
- fine-tuned
datasets:
- dair-ai/emotion
---

# MiniLM Emotion Classification Model

This model is fine-tuned from **microsoft/MiniLM-L12-H384-uncased** to classify text into 6 emotion categories.

It can detect emotional tone from user text such as joy, sadness, anger, fear, love, and surprise.

---

## Model Details

- Base Model: microsoft/MiniLM-L12-H384-uncased  
- Model Type: Transformer Encoder  
- Framework: PyTorch  
- Task: Emotion Classification  
- Parameters: 33.4M  

---

## Supported Emotions

| Label ID | Emotion |
|--------|--------|
| 0 | sadness |
| 1 | joy |
| 2 | love |
| 3 | anger |
| 4 | fear |
| 5 | surprise |

---

## Example Usage

### Install dependencies

```bash
pip install transformers torch
```

### Run inference

```python
from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="nikk118/minilm-finetuned-emotion"
)

result = classifier("I am really excited about this project")

print(result)
```

Output:

```
[{'label': 'joy', 'score': 0.99}]
```

---

## Training Details

Dataset used:

https://huggingface.co/datasets/emotion

Training configuration:

- Epochs: 5
- Batch size: 64
- Learning rate: 2e-5
- Loss function: Weighted CrossEntropyLoss
- Optimizer: AdamW
- Framework: Hugging Face Trainer API

---

## Architecture

Model pipeline:

```
Input Text
   ↓
Tokenizer
   ↓
MiniLM Transformer (12 layers)
   ↓
CLS token embedding
   ↓
Linear classification layer
   ↓
Emotion prediction
```

---

## Intended Use

This model can be used for:

- Chatbots
- Sentiment analysis
- Emotion detection
- Customer feedback analysis
- Social media analysis
- NLP applications

---

## Limitations

- Trained only on English text
- Performance depends on input quality
- May not generalize perfectly to domain-specific text

---

## Author

Created by: Nikk118  
Hugging Face: https://huggingface.co/nikk118  

---

## Model Source

Base model:

https://huggingface.co/microsoft/MiniLM-L12-H384-uncased

Dataset:

https://huggingface.co/datasets/emotion