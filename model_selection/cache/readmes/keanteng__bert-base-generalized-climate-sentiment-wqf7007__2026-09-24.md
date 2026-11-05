
---
language: en
license: agpl-3.0
datasets:
  - edqian/twitter-climate-change-sentiment-dataset
metrics:
  - accuracy
  - f1
  - precision
  - recall
base_model: bert-base-uncased
pipeline_tag: text-classification
tags:
  - text-classification
  - sentiment-analysis
  - climate-change
  - twitter
  - bert
---

# BERT Climate Sentiment Analysis Model

## Model Description
This model fine-tunes BERT (bert-base-uncased) to perform sentiment analysis on climate change-related tweets. It classifies tweets into four sentiment categories: anti-climate (negative), neutral, pro-climate (positive), and news.

## Model Details

- **Model Type:** Fine-tuned BERT (bert-base-uncased)
- **Version:** 1.0.0
- **Framework:** PyTorch & Transformers
- **Language:** English
- **License:** [AGPL-3.0](https://www.gnu.org/licenses/agpl-3.0.en.html)

## Training Data

This model was trained on the [Twitter Climate Change Sentiment Dataset](https://www.kaggle.com/datasets/edqian/twitter-climate-change-sentiment-dataset/data), which contains tweets related to climate change labeled with sentiment categories:

- **news**: Factual news about climate change (2)
- **pro**: Supporting action on climate change (1)
- **neutral**: Neutral stance on climate change (0)
- **anti**: Skeptical about climate change claims (-1)

The dataset was cleaned with the following steps:
            
|Features | Strategy |
|---------|----------|
| Hashtag | Kept |
| Mention | Generalized |
| RT Tag | Generalized |
| URL | Generalized |
| Stop Words | Kept |
| Special Characters | Removed |
            
## Training Procedure

- **Training Framework:** PyTorch with Transformers
- **Training Approach:** Fine-tuning the entire BERT model
- **Optimizer:** AdamW with learning rate 2e-5
- **Batch Size:** 64
- **Early Stopping:** Yes, with patience of 3 epochs
- **Hardware:** GPU acceleration (when available)

## Model Performance

- AUC-ROC
            
![AUC-ROC Curve](images/roc_curve.png)
            
- Training and Validation Loss

![Loss Curves](images/loss_curves_with_best_epoch.png)

## Limitations and Biases

- The model is trained on Twitter data, which may not generalize well to other text sources.
- Twitter data may contain inherent biases in how climate change is discussed.
- The model might struggle with complex or nuanced sentiment expressions.
- Sarcasm and figurative language may be misclassified.
- The model is only trained for English language content.

## Usage

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("google/bert-base-uncased")
model = AutoModelForSequenceClassification.from_pretrained("keanteng/bert-base-generalized-climate-sentiment-wqf7007")

# Prepare text
text = "Climate change is real and we need to act now!"
inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=128)

# Make prediction
with torch.no_grad():
    outputs = model(**inputs)
    predictions = torch.argmax(outputs.logits, dim=1)

# Map prediction to sentiment
sentiment_map = {-1: "anti", 0: "neutral", 1: "pro", 2: "news"}
predicted_sentiment = sentiment_map[predictions.item()]
print("Predicted sentiment: " + predicted_sentiment)
```

## Ethical Considerations

This model should be used responsibly for analyzing climate sentiment and should not be deployed in ways that might:
- Amplify misinformation about climate change
- Target or discriminate against specific groups
- Make critical decisions without human oversight

