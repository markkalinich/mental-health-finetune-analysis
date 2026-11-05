---
base_model: distilbert-base-uncased
library_name: transformers
tags:
- distilbert
- sentiment-analysis
- singapore-banks
- text-classification
- fine-tuning
license: apache-2.0
language:
- en
metrics:
- accuracy
- precision
- recall
- f1
- mae
datasets:
- custom
---

# DistilBERT Full Fine-Tuned for Singapore Bank Review Classification

This model is a **fully fine-tuned** version of `distilbert-base-uncased` for 5-class star rating prediction (1-5 stars) on Singapore digital bank reviews. All ~67M parameters were updated during training.

## 🎯 Model Performance

| Metric | Score |
|--------|-------|
| **Test Accuracy** | 0.4130 |
| **Precision (Macro)** | 0.4461 |
| **Recall (Macro)** | 0.4130 |
| **F1-Score (Macro)** | 0.3268 |
| **MAE (Mean Absolute Error)** | 1.0217 stars |

## 🚀 Quick Start

### Loading the Model

```python
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch

# Load model and tokenizer
model = AutoModelForSequenceClassification.from_pretrained("ajiayi/bert-full-finetuned-singapore-digi-banks")
tokenizer = AutoTokenizer.from_pretrained("ajiayi/bert-full-finetuned-singapore-digi-banks")

# Make predictions
text = "Love this bank! Best interest rates in Singapore."
inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=128)
outputs = model(**inputs)
predicted_stars = outputs.logits.argmax(dim=1).item() + 1  # Convert 0-4 to 1-5
print(f"Predicted rating: {predicted_stars} stars")
```

## 📊 Model Details

### Model Architecture
- **Base Model**: `distilbert-base-uncased` (66M parameters)
- **Fine-tuning Method**: Full supervised fine-tuning (all parameters updated)
- **Task**: Multi-class text classification (5 classes)
- **Classes**: 1-star, 2-star, 3-star, 4-star, 5-star

### Model Size
- **Total Parameters**: 66,957,317
- **Model Size**: ~250MB
- **Training Time**: 1.99 minutes

## 🎓 Training Details

### Training Data
- **Domain**: Singapore digital bank reviews (GXS, Trust Bank, MariBank, etc.)
- **Training Samples**: 1,055
- **Validation Samples**: 225
- **Test Samples**: 230
- **Augmentation**: LLM-based data augmentation using Google Gemini

### Training Hyperparameters
- **Learning Rate**: 5e-05
- **Batch Size**: 8
- **Gradient Accumulation Steps**: 2
- **Epochs**: 3
- **Weight Decay**: 0.01
- **Warmup Ratio**: 0.1
- **Optimizer**: AdamW
- **Loss Function**: Cross-Entropy with class weights

### Training Infrastructure
- **Framework**: HuggingFace Transformers
- **Hardware**: Apple Silicon (MPS) / CPU
- **Mixed Precision**: FP16 (when GPU available)

## 🎯 Intended Use

### Primary Use Cases
- Sentiment analysis of Singapore bank reviews
- Star rating prediction for financial services
- Customer feedback classification
- Banking app review analysis

### Out-of-Scope Use
- Reviews for non-Singapore banks (model trained specifically on Singapore digital banks)
- Non-English reviews
- General sentiment analysis (domain-specific model)

## ⚖️ Limitations and Bias

### Known Limitations
- Trained on Singapore digital bank reviews only
- May not generalize well to traditional banks
- Performance may vary on very short or very long reviews
- English language only

### Potential Biases
- Data collected from Apple App Store only
- May reflect platform-specific sentiment patterns
- Class imbalance handled via weighted loss and augmentation

## 📈 Evaluation Results

The model was evaluated on a held-out test set with the following results:

- **Accuracy**: 41.30%
- **Average prediction error**: 1.02 stars

See confusion matrix and detailed per-class metrics in the training notebook.

## 🔧 How to Use

### For Inference

```python
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch

# Load model and tokenizer
model = AutoModelForSequenceClassification.from_pretrained("ajiayi/bert-full-finetuned-singapore-digi-banks")
tokenizer = AutoTokenizer.from_pretrained("ajiayi/bert-full-finetuned-singapore-digi-banks")

# Predict
def predict_rating(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=128)
    model.eval()
    with torch.no_grad():
        outputs = model(**inputs)
        prediction = outputs.logits.argmax(dim=1).item()
    return prediction + 1  # Convert 0-indexed to 1-5 stars

# Example
review = "Great banking app! Very user-friendly interface."
stars = predict_rating(review)
print(f"Predicted: {stars} stars")
```

## 📚 Citation

```bibtex
@misc{full-finetuned-singapore-banks,
  author = {Your Name},
  title = {Full Fine-Tuned DistilBERT for Singapore Bank Review Classification},
  year = {2025},
  publisher = {HuggingFace},
  howpublished = {\url{https://huggingface.co/ajiayi/bert-full-finetuned-singapore-digi-banks}}
}
```

## 📄 License

This model is released under the Apache 2.0 License.

## 🙏 Acknowledgments

- Base model: [DistilBERT](https://huggingface.co/distilbert-base-uncased) by HuggingFace
- Training framework: HuggingFace Transformers

---

**Generated**: 2025-10-12 00:17:45
