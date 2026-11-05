
---
license: apache-2.0
base_model: distilbert-base-uncased
tags:
- generated_from_trainer
- sentiment-analysis
- movie-reviews
datasets:
- imdb
metrics:
- accuracy
model-index:
- name: malli_finetuned_model
  results:
  - task:
      type: text-classification
      name: Text Classification
    dataset:
      name: imdb
      type: imdb
    metrics:
    - type: accuracy
      value: 1.0000
---

# malli_finetuned_model

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the IMDB movie reviews dataset.
It achieves an accuracy of **100.0%** on the test set.

## Model Description

This is a sentiment analysis model specifically trained on movie reviews. It can classify text as either positive or negative sentiment.

## Intended Uses & Limitations

**Intended Uses:**
- Sentiment analysis of movie reviews
- General sentiment classification of English text
- Educational purposes and research

**Limitations:**
- Trained specifically on movie reviews, may not generalize well to other domains
- English language only
- Binary classification (positive/negative) - no neutral sentiment

## Training Procedure

### Training Data

The model was fine-tuned on the IMDB movie reviews dataset:
- Training samples: 2250
- Validation samples: 250  
- Test samples: 500

### Training Hyperparameters

- Learning rate: 2e-05
- Train batch size: 16
- Eval batch size: 16
- Number of epochs: 3
- Optimizer: AdamW
- Weight decay: 0.01

### Results

| Metric | Value |
|--------|-------|
| Accuracy | 1.0000 |

## Usage

```python
from transformers import pipeline

# Load the model
classifier = pipeline("text-classification", model="Mallikarjunareddy/malli_finetuned_model")

# Classify text
result = classifier("This movie was absolutely amazing!")
print(result)
# Output: [{'label': 'LABEL_1', 'score': 0.9998}]
# LABEL_0 = Negative, LABEL_1 = Positive
```

## Model Performance

The model shows strong performance on movie review sentiment analysis:
- **Test Accuracy: 100.0%**
- Baseline (random guessing): 50.0%
- Improvement: +50.0 percentage points

## Citation

```
@misc{malli_finetuned_model_2024,
  author = {Your Name},
  title = {malli_finetuned_model: Fine-tuned IMDB Sentiment Analysis},
  year = {2024},
  publisher = {Hugging Face},
  howpublished = {\url{https://huggingface.co/Mallikarjunareddy/malli_finetuned_model}}
}
```
