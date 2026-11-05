---
license: apache-2.0
datasets:
- stanfordnlp/imdb
language:
- en
metrics:
- accuracy
tags:
- sentiment-analysis
- distilbert
- lora
---
# distilbert-base-uncased-imdb-lora
This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert/distilbert-base-uncased) on the [IMDb dataset](https://huggingface.co/datasets/imdb) for sentiment analysis, using LoRA (Low-Rank Adaptation) for efficient fine-tuning.

## Model Details
- **Base Model**: distilbert-base-uncased
- **Task**: Sentiment Analysis (binary classification)
- **Dataset**: IMDb (50,000 movie reviews, 25,000 train, 25,000 test)
- **Labels**: 
  - `LABEL_0`: NEGATIVE
  - `LABEL_1`: POSITIVE
- **Fine-Tuning Method**: LoRA
- **LoRA Parameters**:
  - `r=8` (rank)
  - `lora_alpha=16`
  - `lora_dropout=0.05`
  - Target modules: `q_lin`, `v_lin`

## Performance
- **Validation Accuracy**: ~82.32% (at step 2100)
- **Test Accuracy**: 82.60% (on full 25,000 test samples)
- **Test Loss**: 0.6206
- **Inference Example**:
  - Input: "The movie is good"
  - Output: `LABEL_1` (POSITIVE, score: 0.5600)
  - Input: "The movie is bad"
  - Output: `LABEL_0` (NEGATIVE, score: 0.5388)

## How to Use
### Requirements
```bash
pip install transformers peft torch 
```
### Inference Example
```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification, TextClassificationPipeline
from peft import PeftModel, PeftConfig
import torch

# Load model and tokenizer
model_name = "MyselfRee/distilbert-base-uncased-imdb-lora"
config = PeftConfig.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained("distilbert/distilbert-base-uncased", num_labels=2)
model = PeftModel.from_pretrained(model, model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Create pipeline
classifier = TextClassificationPipeline(
    model=model,
    tokenizer=tokenizer,
    framework="pt",
    task="sentiment-analysis",
    device=0 if torch.cuda.is_available() else -1
)

# Test inference with label mapping
label_map = {"LABEL_0": "NEGATIVE", "LABEL_1": "POSITIVE"}
def map_labels(prediction):
    prediction[0]["label"] = label_map[prediction[0]["label"]]
    return prediction

print(map_labels(classifier("The movie is good")))  # Output: [{'label': 'POSITIVE', 'score': 0.5600}]
print(map_labels(classifier("The movie is bad")))   # Output: [{'label': 'NEGATIVE', 'score': 0.5388}]
```

### Notes
- Requires the `peft` library for LoRA weights.
- Use a GPU for faster inference (CPU is supported but slower).
- The model outputs `LABEL_0` (NEGATIVE) and `LABEL_1` (POSITIVE)—use the `map_labels` function in the inference example to display proper labels.

## Limitations
- Fine-tuned on IMDb reviews; may not generalize to other domains.
- Confidence scores (~0.56 for positive) are moderate; further tuning can improve them.
- Only supports binary classification (positive/negative).