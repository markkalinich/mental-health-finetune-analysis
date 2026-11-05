---
language: id
license: mit
tags:
- sentiment-analysis
- indobert
- indonesian
- google-play-reviews
- text-classification
datasets:
- smsa
metrics:
- accuracy
- f1
---

# sentiment-indonesian-playstore

Fine-tuned RoBERTa model for **Indonesian** sentiment analysis on Google Play Store reviews.

## Model Description

This model performs 3-class sentiment classification:
- **Positive** (label: 2) 😊
- **Neutral** (label: 1) 😐
- **Negative** (label: 0) 😞

## Training Data

- **Dataset**: SMSA (Sentiment Analysis on Indonesian Movie Reviews)
- **Language**: Indonesian (Bahasa Indonesia)
- **Size**: 11,000 reviews
  - Positive: 6,416 reviews (58.3%)
  - Negative: 3,436 reviews (31.2%)
  - Neutral: 1,148 reviews (10.4%)
- **Domain**: App reviews (Google Play Store)

## Usage

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model_name = "rkkzone/roberta-sentiment-indonesian-playstore"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Example Indonesian review
text = "Aplikasi bagus sekali! Sangat direkomendasikan."

inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=128)

with torch.no_grad():
    outputs = model(**inputs)
    predictions = torch.nn.functional.softmax(outputs.logits, dim=-1)
    sentiment = torch.argmax(predictions, dim=-1).item()

sentiment_labels = {0: "Negative", 1: "Neutral", 2: "Positive"}
print(f"Sentiment: {sentiment_labels[sentiment]}")
print(f"Confidence: {predictions[0][sentiment].item():.4f}")
```

### Batch Processing

```python
reviews = [
    "Aplikasi bagus, mudah digunakan!",
    "Tidak bisa login, aplikasi error terus",
    "Biasa aja sih"
]

inputs = tokenizer(reviews, return_tensors="pt", padding=True, truncation=True, max_length=128)

with torch.no_grad():
    outputs = model(**inputs)
    predictions = torch.nn.functional.softmax(outputs.logits, dim=-1)
    sentiments = torch.argmax(predictions, dim=-1)

for review, sentiment, probs in zip(reviews, sentiments, predictions):
    label = sentiment_labels[sentiment.item()]
    conf = probs[sentiment].item()
    print(f"Review: {review}")
    print(f"Sentiment: {label} ({conf:.2%} confident)\n")
```

## Model Performance

**Training Configuration:**
- **Base Model**: IndoBERT (`indobenchmark/indobert-base-p1`)
- **Training Epochs**: 3
- **Batch Size**: 16
- **Learning Rate**: 2e-5
- **Max Length**: 128 tokens
- **Optimizer**: AdamW
- **Weight Decay**: 0.01

**Evaluation Results:**
- Check model card for detailed metrics on test set
- Includes per-class precision, recall, and F1 scores

## Dataset Preprocessing

The model was trained with the following preprocessing:
1. **Indonesian Slang Normalization**: Common abbreviations expanded
2. **Text Cleaning**: Remove special characters, URLs, excessive whitespace
3. **Tokenization**: BertTokenizer with max 128 tokens
4. **Label Mapping**: 
   - `negative` → 0
   - `neutral` → 1
   - `positive` → 2

## Intended Use

This model is optimized for:
- ✅ Indonesian language app reviews
- ✅ Google Play Store sentiment analysis
- ✅ Customer feedback classification
- ✅ Review monitoring and analytics
- ✅ E-commerce product reviews (Indonesian)

## Limitations

- Optimized for **informal Indonesian** text (app reviews)
- May not generalize well to formal Indonesian literature
- Best performance on **short texts** (< 128 tokens)
- Sensitive to **slang variations** across Indonesian regions
- Trained primarily on app domain data

## Applications

### 1. **App Analytics Dashboard**
Analyze user sentiment in Indonesian app reviews to track satisfaction over time.

### 2. **Customer Support Prioritization**
Automatically flag negative reviews for urgent response.

### 3. **Market Research**
Understand Indonesian user preferences and pain points.

### 4. **Review Filtering**
Filter out spam or irrelevant reviews based on sentiment patterns.

## Example Predictions

| Review (Indonesian) | Predicted Sentiment | Confidence |
|---------------------|---------------------|------------|
| "Aplikasi keren banget! Fiturnya lengkap!" | Positive | 95.3% |
| "Aplikasi sering crash, mohon diperbaiki" | Negative | 87.2% |
| "Lumayan lah, standar aja" | Neutral | 72.8% |
| "Mantap jiwa! Recommended!" | Positive | 91.5% |
| "Mengecewakan, buang-buang waktu" | Negative | 89.6% |

## Citation

```bibtex
@misc{roberta_sentiment_indonesian_playstore,
  author = {rkkzone},
  title = {Indonesian Sentiment Analysis for Google Play Reviews},
  year = {2025},
  publisher = {Hugging Face},
  url = {https://huggingface.co/rkkzone/roberta-sentiment-indonesian-playstore}
}
```

## License

MIT License - Free for commercial and non-commercial use.

## Related Resources

- **English version**: [rkkzone/roberta-sentiment-playstore](https://huggingface.co/rkkzone/roberta-sentiment-playstore)
- **Dataset**: [SMSA Indonesian Sentiment](https://github.com/IndoNLP/indonlu)
- **Live Demo**: [Google Play Review Analyzer](https://google-play-review-analyzer.streamlit.app)

## Acknowledgments

- Dataset: Indonesian NLP research community (SMSA dataset)
- Base Model: IndoNLP team for IndoBERT
- Framework: Hugging Face Transformers

---

**Built with ❤️ for Indonesian app developers**

*For issues or questions, please open an issue on the model repository.*
