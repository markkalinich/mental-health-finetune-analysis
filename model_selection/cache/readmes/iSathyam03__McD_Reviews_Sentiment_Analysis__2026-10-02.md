---
library_name: transformers
tags:
- sentiment-analysis
- McDonals-Review
- Food
- NLP
license: mit
language:
- en
metrics:
- accuracy
- f1
base_model:
- microsoft/deberta-v3-small
pipeline_tag: text-classification
---

# Sentiment Analysis with Fine-Tuned DeBERTa

This repository contains a fine-tuned [DeBERTa](https://huggingface.co/microsoft/deberta) model for sentiment analysis using the McDonald's review dataset from Kaggle. The model has been fine-tuned to classify customer sentiments as positive, negative, or neutral.

## Model Details
- **Base Model:** `microsoft/deberta-v3-base`
- **Task:** Sentiment Analysis
- **Dataset:** McDonald's review dataset (Kaggle)
- **Framework:** Hugging Face Transformers, PyTorch
- **Fine-Tuning Approach:**
  - Tokenized using DeBERTa tokenizer
  - Trained with cross-entropy loss
  - Optimized using AdamW
  - Learning rate scheduler applied

## Dataset
The dataset consists of customer reviews from McDonald's, labeled with sentiment categories:
- `0`: Negative
- `1`: Neutral
- `2`: Positive

## Training Hyperparameters
- **Batch Size:** 16
- **Epochs:** 3
- **Learning Rate:** 2e-5
- **Optimizer:** AdamW
- **Scheduler:** Cosine learning rate decay with warmup (10% warmup ratio)
- **Weight Decay:** 0.01
- **Evaluation Strategy:** Epoch-based
- **Save Strategy:** Best model saved at the end
- **Mixed Precision Training:** Enabled (fp16)
- **Gradient Accumulation Steps:** 2
- **Logging Steps:** 50

## How to Use the Model
To load and use the model for inference:

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model_name = "iSathyam03/McD_Reviews_Sentiment_Analysis"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

def predict_sentiment(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
    logits = outputs.logits
    prediction = torch.argmax(logits, dim=1).item()
    sentiment_labels = {0: "Negative", 1: "Neutral", 2: "Positive"}
    return sentiment_labels[prediction]

# Example
text = "The fries were amazing but the burger was stale."
print(predict_sentiment(text))
```

## Evaluation
* The model was evaluated using accuracy, F1-score, and confusion matrix.
* Performance metrics suggest that the fine-tuned DeBERTa model achieves high accuracy on customer sentiment classification.

## Deployment
You can deploy this model using Hugging Face's Inference API or via Streamlit/Gradio for an interactive UI.

## Citation
If you use this model, please cite this repository and the original DeBERTa paper:
```
@article{he2020deberta,
  title={DeBERTa: Decoding-enhanced BERT with Disentangled Attention},
  author={He, Pengcheng and Liu, Xiaodong and Gao, Jianfeng and Chen, Weizhu},
  journal={arXiv preprint arXiv:2006.03654},
  year={2020}
}
```

