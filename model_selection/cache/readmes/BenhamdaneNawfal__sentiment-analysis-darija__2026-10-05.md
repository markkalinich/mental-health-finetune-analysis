---
language: ar
tags:
- sentiment-analysis
- darija
- arabic
license: apache-2.0
datasets:
- custom
metrics:
- accuracy
- precision
- recall
- f1
---


# Sentiment Analysis for Darija (Arabic Dialect)

This repository hosts a **Sentiment Analysis model for Darija** (Moroccan Arabic dialect), built using **BERT**. The model is fine-tuned to classify text into two categories: **positive** and **negative** sentiment. It is designed to facilitate sentiment analysis in applications involving Darija text data, such as social media analysis, customer feedback, or market research.

---

## Model Details

- **Base Model**: [SI2M-Lab/DarijaBERT](https://huggingface.co/SI2M-Lab/DarijaBERT)
- **Task**: Sentiment Classification (Binary)
- **Architecture**: BERT with a custom classification head and dropout regularization (0.3 dropout rate).
- **Fine-Tuning Data**: Dataset of labeled Darija text samples (positive and negative).
- **Max Sequence Length**: 128 tokens

---

## How to Use

### Load the Model and Tokenizer

To use this model for sentiment analysis, you can load it using the Transformers library:

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# Load the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("BenhamdaneNawfal/sentiment-analysis-darija")
model = AutoModelForSequenceClassification.from_pretrained("BenhamdaneNawfal/sentiment-analysis-darija")

# Example text
test_text = "هذا المنتج رائع جدا"

# Tokenize the text
inputs = tokenizer(test_text, return_tensors="pt", truncation=True, padding=True, max_length=128)

# Get model predictions
outputs = model(**inputs)
logits = outputs.logits
predicted_class = logits.argmax().item()

print(f"Predicted class: {predicted_class}")
```

### Output Classes
- **0**: Negative
- **1**: Positive

---

## Fine-Tuning Process

The model was fine-tuned using the following:

- **Dataset**: A dataset of Darija text labeled for sentiment.
- **Loss Function**: Cross-entropy loss for binary classification.
- **Optimizer**: AdamW with weight decay (0.01).
- **Learning Rate**: 5e-5 with linear warmup.
- **Batch Size**: 16 for training, 64 for evaluation.
- **Early Stopping**: Training stops if validation loss does not improve after 1 epoch.

---

## Evaluation Metrics

The model's performance was evaluated using the following metrics:

- **Accuracy**: 80%
- **Precision**: 0.81%
- **Recall**: 0.79%
- **F1-Score**: 0.80%
 
---

## Publishing on Hugging Face

The model and tokenizer were saved and uploaded to Hugging Face using the `huggingface_hub` library. To reproduce or fine-tune this model, follow these steps:

1. Save the model and tokenizer:
   ```python
   model.save_pretrained("darija-bert-model")
   tokenizer.save_pretrained("darija-bert-model")
   ```


---

## Future Work

- Expand the dataset to include more labeled examples from diverse sources.
- Fine-tune the model for multi-class sentiment analysis (e.g., neutral, positive, negative).
- Explore the use of data augmentation techniques for better generalization.

---

## Citation
If you use this model, please cite it as:

```
@misc{benhamdanenawfal2025darijabert,
  author = {Benhamdane Nawfal},
  title = {Sentiment Analysis for Darija (Arabic Dialect)},
  year = {2025},
  publisher = {Hugging Face},
  url = {https://huggingface.co/BenhamdaneNawfal/sentiment-analysis-darija}
}
```

---

## Contact
For any questions or issues, feel free to contact me at: [n.benhamdane2003@gmail.com].

