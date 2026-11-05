---
language: tr
tags:
- sentiment-analysis
- turkish
- bert
- text-classification
license: apache-2.0
datasets:
- winvoker/turkish-sentiment-analysis-dataset
- WhiteAngelss/Turkce-Duygu-Analizi-Dataset
metrics:
- accuracy
- f1
- precision
- recall
---

# Turkish Sentiment Analysis Model

A fine-tuned BERT model for Turkish sentiment analysis, trained on a combined dataset of 439,384 labeled Turkish sentences.

## Model Details

- **Base Model:** `dbmdz/bert-base-turkish-cased`
- **Task:** Text Classification (Sentiment Analysis)
- **Language:** Turkish
- **Labels:** positive, negative, neutral

## Training Data

The model was trained on a combination of two high-quality Turkish sentiment datasets:
- `winvoker/turkish-sentiment-analysis-dataset` (440,641 samples)
- `WhiteAngelss/Turkce-Duygu-Analizi-Dataset` (440,641 samples)

After deduplication and preprocessing, the final training set consisted of:
- **Training:** 351,507 samples
- **Validation:** 43,938 samples
- **Test:** 43,939 samples

### Label Distribution

- **Positive:** 234,957 (53.5%)
- **Neutral:** 153,809 (35.0%)
- **Negative:** 50,618 (11.5%)

## Training

- **Epochs:** 3
- **Learning Rate:** 2e-5
- **Batch Size:** 16
- **Max Length:** 128
- **Optimizer:** AdamW

## Usage

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load model and tokenizer
model_name = "codealchemist01/turkish-sentiment-analysis"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Example text
text = "Bu ürün gerçekten harika!"

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

## Performance

Evaluation metrics on the test set (43,939 samples):

- **Accuracy:** 97.45%
- **Weighted F1:** 97.42%
- **Weighted Precision:** 97.41%
- **Weighted Recall:** 97.45%

### Per-Class Performance

| Class    | Precision | Recall | F1-Score | Support |
|----------|-----------|--------|----------|---------|
| Negative | 91.42%    | 86.69% | 88.99%   | 5,062   |
| Neutral  | 99.79%    | 99.96% | 99.87%   | 15,381  |
| Positive | 97.15%    | 98.12% | 97.63%   | 23,496  |

**Note:** Negative class has lower performance due to class imbalance (only 11.5% of the dataset). The model performs excellently on neutral and positive classes.

## Limitations

- The model may not perform well on very short texts (< 3 words)
- Performance may vary across different domains (social media, news, reviews)
- Class imbalance may affect performance on minority classes (negative)

## Citation

If you use this model, please cite:

```bibtex
@misc{turkish-sentiment-analysis,
  title={Turkish Sentiment Analysis Model},
  author={codealchemist01},
  year={2024},
  howpublished={\url{https://huggingface.co/codealchemist01/turkish-sentiment-analysis}}
}
```

## License

Apache 2.0

