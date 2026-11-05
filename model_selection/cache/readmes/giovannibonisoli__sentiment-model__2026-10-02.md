---
---
library_name: transformers
tags:
- sentiment-analysis
- twitter
- roberta
- text-classification
datasets:
- tweet_eval
---

# Sentiment Analysis Model

## Model Details

### Model Description

Fine-tuned RoBERTa model for sentiment analysis on tweets, trained on the TweetEval benchmark.

- **Developed by**: Your Name
- **Model type**: RoBERTa (Sequence Classification)
- **Language**: English
- **License**: MIT
- **Finetuned from**: cardiffnlp/twitter-roberta-base-sentiment-latest

### Model Sources

- **Repository**: [HuggingFace Hub](https://huggingface.co/your-username/your-repo)
- **Paper**: [TweetEval](https://arxiv.org/abs/2020.emnlp.main.85)

## Uses

### Direct Use

This model can be used for sentiment analysis on English tweets. It classifies text into three categories:
- negative
- neutral
- positive

### Out-of-Scope Use

- Non-English text
- Very long documents (>512 tokens)
- Non-tweet content (may have reduced accuracy)

## Bias, Risks, and Limitations

- Model trained on English tweets only
- May not generalize well to other domains
- Sentiment labels may not capture nuance in complex expressions
- Sarcasm and irony may be misclassified

### Recommendations

Users should be aware that this model is specifically trained on tweets and may not perform well on other types of text. For production use, consider fine-tuning on domain-specific data.

## How to Get Started with the Model

```python
from transformers import pipeline

classifier = pipeline("sentiment-analysis", model="giovannibonisoli/sentiment-model")
result = classifier("I love this!")
# [{'label': 'positive', 'score': 0.98}]
```

## Training Details

### Training Data

- **Dataset**: TweetEval (sentiment)
- **Train split**: 1000 samples (configurable via `TRAIN_SAMPLES` env var)
- **Validation split**: 1000 samples (configurable via `VALIDATION_SAMPLES` env var)

### Training Procedure

#### Preprocessing

- Tokenization with truncation at 512 tokens
- Padding to max_length
- Batched processing

#### Training Hyperparameters

- **Training regime**: fp16 mixed precision
- **Epochs**: 3 (configurable via `NUM_EPOCHS`)
- **Batch size**: 16
- **Optimizer**: AdamW (default)
- **Learning rate**: 2e-5 (transformers default)

### Training Configuration

```python
TrainingArguments(
    num_train_epochs=3,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=16,
    eval_strategy="epoch",
    save_strategy="epoch",
    load_best_model_at_end=True,
    metric_for_best_model="macro_f1",
    logging_steps=50
)
```

## Evaluation

### Testing Data

- **Dataset**: TweetEval (sentiment) - test split

### Metrics

- **Accuracy**: ~0.72
- **Macro F1**: ~0.72

### Results

Final metrics after training:
- Accuracy: {accuracy_value_from_CI}
- Macro F1: {f1_value_from_CI}

## Environmental Impact

- **Hardware Type**: GPU (GitHub Actions runner)
- **Hours used**: ~5 minutes
- **Cloud Provider**: GitHub Actions

## Technical Specifications

### Model Architecture and Objective

- Base model: RoBERTa-base
- Objective: Sequence Classification (3 classes)
- Max sequence length: 512 tokens
- Parameters: ~125M

### Compute Infrastructure

- Training: GitHub Actions (Ubuntu runner with GPU)
- Storage: HuggingFace Hub