---
library_name: transformers
license: mit
base_model: agentlans/deberta-v3-xsmall-zyda-2
tags:
- generated_from_trainer
- sentiment-analysis
- twitter-sentiment
model-index:
- name: deberta-v3-xsmall-zyda-2-transformed-sentiment-new
  results: []
---

# DeBERTa-v3-XSmall Sentiment Analysis Model

## Model Overview

This model is a fine-tuned version of [agentlans/deberta-v3-xsmall-zyda-2](https://huggingface.co/agentlans/deberta-v3-xsmall-zyda-2) optimized for sentiment analysis on Twitter data. It achieves the following results on the evaluation set:

- Loss: 0.0656
- MSE: 0.0656

## Dataset

The model was trained on the [Twitter Sentiment Meta-Analysis Dataset](https://huggingface.co/datasets/agentlans/twitter-sentiment-meta-analysis).

### Dataset Description

This dataset contains sentiment analysis results for English tweets collected between September 2009 and January 2010. The tweets were processed and analyzed using 10 different sentiment classifiers, with the final sentiment score derived from principal component analysis (PCA).

- **Source**: Cheng-Caverlee-Lee Twitter Scrape (Sept 2009 - Jan 2010)
- **Size**: 138,690 tweets
- **Language**: English only (filtered using langdetect)

## Usage

Here's an example of how to use the model for sentiment prediction:

```python
import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer

# Load model and tokenizer
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model_name = "agentlans/deberta-v3-xsmall-zyda-2-sentiment"
model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=1).to(device)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Function to perform inference
def predict_score(text):
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True).to(device)
    with torch.no_grad():
        logits = model(**inputs).logits
    return logits.item()

# Example usage
input_text = "I accidentally the whole thing. Is that bad?"
score = predict_score(input_text)
print(f"Predicted score: {score}")
```

## Example Outputs

| Text | Sentiment |
|------|----------:|
| Nothing seems to go right, and I'm constantly frustrated. | -2.25 |
| Everything is falling apart, and I can't see any way out. | -2.02 |
| I feel completely overwhelmed by the challenges I face. | -1.62 |
| There are some minor improvements, but overall, things are still tough. | -0.81 |
| I can see a glimmer of hope amidst the difficulties I encounter. | 1.03 |
| Things are starting to look up, and I'm cautiously optimistic. | 2.06 |
| There are many good things happening, and I appreciate them. | 2.23 |
| I'm feeling more positive about my situation than I have in a while. | 2.39 |
| Every day brings new joy and possibilities; I feel truly blessed. | 2.54 |
| Life is full of opportunities, and I'm excited about the future. | 2.56 |

## Training Procedure

### Hyperparameters

- Learning rate: 5e-05
- Train batch size: 64
- Eval batch size: 8
- Seed: 42
- Optimizer: AdamW with betas=(0.9, 0.999) and epsilon=1e-08
- LR scheduler: Linear
- Number of epochs: 3.0

### Training Results

| Training Loss | Epoch | Step | Validation Loss | MSE    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 0.0792        | 1.0   | 2011 | 0.0871          | 0.0871 |
| 0.0541        | 2.0   | 4022 | 0.0691          | 0.0691 |
| 0.0411        | 3.0   | 6033 | 0.0656          | 0.0656 |

## Framework Versions

- Transformers: 4.46.3
- PyTorch: 2.5.1+cu124
- Datasets: 3.1.0
- Tokenizers: 0.20.3
