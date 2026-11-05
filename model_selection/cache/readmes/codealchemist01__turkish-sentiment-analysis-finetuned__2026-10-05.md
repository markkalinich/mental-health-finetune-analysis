---
language: tr
tags:
- sentiment-analysis
- turkish
- bert
- text-classification
- fine-tuned
license: apache-2.0
base_model: codealchemist01/turkish-sentiment-analysis
datasets:
- winvoker/turkish-sentiment-analysis-dataset
- WhiteAngelss/Turkce-Duygu-Analizi-Dataset
- maydogan/Turkish_SentimentAnalysis_TRSAv1
- turkish-nlp-suite/MusteriYorumlari
- W4nkel/turkish-sentiment-dataset
metrics:
- accuracy
- f1
- precision
- recall
---

# Turkish Sentiment Analysis Model (Fine-tuned)

A fine-tuned version of the [codealchemist01/turkish-sentiment-analysis](https://huggingface.co/codealchemist01/turkish-sentiment-analysis) model, improved with additional balanced training data to enhance neutral and negative class performance.

## Model Details

- **Base Model:** [codealchemist01/turkish-sentiment-analysis](https://huggingface.co/codealchemist01/turkish-sentiment-analysis)
- **Task:** Text Classification (Sentiment Analysis)
- **Language:** Turkish
- **Labels:** positive, negative, neutral
- **Fine-tuning Type:** Continued fine-tuning on balanced dataset

## Training Data

This model was fine-tuned on a balanced combination of the original dataset and additional Turkish sentiment datasets:

### Original Dataset (from base model):
- `winvoker/turkish-sentiment-analysis-dataset` (440,641 samples)
- `WhiteAngelss/Turkce-Duygu-Analizi-Dataset` (440,641 samples)

### Additional Datasets for Fine-tuning:
- `maydogan/Turkish_SentimentAnalysis_TRSAv1` (150,000 samples)
- `turkish-nlp-suite/MusteriYorumlari` (73,920 samples)
- `W4nkel/turkish-sentiment-dataset` (4,800 samples)
- `mustfkeskin/turkish-movie-sentiment-analysis-dataset` (Kaggle, 83,227 samples)

### Final Balanced Dataset:
- **Total:** 556,888 samples
- **Positive:** 237,966 (42.7%)
- **Neutral:** 209,668 (37.6%)
- **Negative:** 109,254 (19.6%)

**Split Distribution:**
- **Training:** 445,510 samples
- **Validation:** 55,689 samples
- **Test:** 55,689 samples

## Training

### Fine-tuning Parameters:
- **Base Model:** codealchemist01/turkish-sentiment-analysis
- **Epochs:** 2
- **Learning Rate:** 1e-5 (lower than initial training for fine-tuning)
- **Batch Size:** 12 (per device)
- **Gradient Accumulation:** 2 (effective batch size: 24)
- **Max Length:** 128 tokens
- **Optimizer:** AdamW
- **Mixed Precision (FP16):** Enabled

## Performance

### Test Set Results (55,689 samples):

**Overall Metrics:**
- **Accuracy:** 91.96%
- **Weighted F1:** 91.93%
- **Weighted Precision:** 91.93%
- **Weighted Recall:** 91.96%

### Per-Class Performance:

| Class    | Precision | Recall | F1-Score | Support |
|----------|-----------|--------|----------|---------|
| Negative | 90.65%    | 86.79% | 88.68%   | 10,926  |
| Neutral  | 90.91%    | 90.24% | 90.57%   | 20,967  |
| Positive | 93.41%    | 95.84% | 94.61%   | 23,796  |

## Improvements Over Base Model

### Key Improvements:
1. **Neutral Class Performance:**
   - Better recognition of neutral expressions
   - Improved handling of ambiguous texts
   - Neutral F1-score: **90.57%** (improved from base model's test performance)

2. **Better Class Balance:**
   - More balanced dataset (reduced class imbalance)
   - Negative class improved with more training examples
   - Neutral class significantly enhanced

3. **General Performance:**
   - Maintained high accuracy (91.96%)
   - Improved F1-scores across all classes
   - Better generalization on diverse Turkish texts

### Test Results Comparison (15 sample test):
- **Base Model Accuracy:** 66.7% (10/15)
- **Fine-tuned Model Accuracy:** 86.7% (13/15)
- **Improvement:** +20.0%

### Per-Class Test Results:
- **Neutral:** 0% → 80% (+80.0% improvement)
- **Negative:** 100% → 80% (slight decrease, but more balanced)
- **Positive:** 100% → 100% (maintained)

## Usage

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load model and tokenizer
model_name = "codealchemist01/turkish-sentiment-analysis-finetuned"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Example text
text = "Bu ürün normal, beklediğim gibi. Özel bir şey yok."

# Tokenize
inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=128)

# Predict
with torch.no_grad():
    outputs = model(**inputs)
    predictions = torch.nn.functional.softmax(outputs.logits, dim=-1)
    predicted_label_id = predictions.argmax().item()

# Map to label
id2label = {0: "negative", 1: "neutral", 2: "positive"}
predicted_label = id2label[predicted_label_id]
confidence = predictions[0][predicted_label_id].item()

print(f"Label: {predicted_label}")
print(f"Confidence: {confidence:.4f}")
```

## Limitations

- The model may not perform well on very short texts (< 3 words)
- Performance may vary across different domains (social media, news, reviews)
- Some ambiguous neutral expressions may still be misclassified
- Negative class performance may vary on different text types

## Citation

If you use this model, please cite:

```bibtex
@misc{turkish-sentiment-analysis-finetuned,
  title={Turkish Sentiment Analysis Model (Fine-tuned)},
  author={codealchemist01},
  year={2024},
  base_model={codealchemist01/turkish-sentiment-analysis},
  howpublished={\url{https://huggingface.co/codealchemist01/turkish-sentiment-analysis-finetuned}}
}
```

## License

Apache 2.0

