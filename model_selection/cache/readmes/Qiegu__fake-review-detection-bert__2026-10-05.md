---
license: mit
tags:
- fake-review-detection
- bert
- text-classification
- nlp
- sentiment-analysis
---

# Fake Review Detection BERT Model

This is a fine-tuned BERT model for detecting fake product reviews on e-commerce platforms.

## Model Description

- **Model Type**: BERT-based text classifier
- **Task**: Binary classification (Real vs Fake reviews)
- **Training Data**: Product reviews from e-commerce platforms
- **Use Case**: Detecting artificially generated or manipulated product reviews

## Usage

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# Load model and tokenizer
model_name = "Qiegu/fake-review-detection-bert"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Classify a review
text = "This product is amazing! I love it so much!"
inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
outputs = model(**inputs)
prediction = outputs.logits.argmax(dim=1).item()

# 0 = Real review, 1 = Fake review
result = "Fake" if prediction == 1 else "Real"
print(f"Review classification: {result}")
```

## Model Performance

- **Accuracy**: Trained on diverse product review datasets
- **Use Case**: E-commerce review authenticity detection
- **Input**: Product review text
- **Output**: Binary classification (Real/Fake)

## Citation

If you use this model in your research, please cite:

```bibtex
@misc{fake-review-detection-bert,
  title={Fake Review Detection BERT Model},
  author={Your Name},
  year={2024},
  publisher={Hugging Face},
  url={https://huggingface.co/Qiegu/fake-review-detection-bert}
}
```
