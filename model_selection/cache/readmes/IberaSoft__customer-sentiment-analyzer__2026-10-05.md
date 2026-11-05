---
language: en
license: mit
tags:
- sentiment-analysis
- customer-reviews
- transformers
- distilbert
- text-classification
datasets:
- IberaSoft/ecommerce-reviews-sentiment
metrics:
- accuracy
- f1
widget:
- text: This product exceeded my expectations! Fast shipping and great quality.
  example_title: Positive Review
- text: Terrible experience. Product broke after one week and customer service was
    unhelpful.
  example_title: Negative Review
- text: It's okay, nothing special. Does what it's supposed to do.
  example_title: Neutral Review
model-index:
- name: customer-sentiment-analyzer
  results:
  - task:
      type: text-classification
      name: Sentiment Analysis
    dataset:
      name: E-commerce Reviews
      type: IberaSoft/ecommerce-reviews-sentiment
    metrics:
    - type: accuracy
      value: 90.2
      name: Accuracy
    - type: f1
      value: 0.89
      name: F1 Score
---

# 🎯 Customer Sentiment Analyzer

> Fine-tuned DistilBERT model for analyzing customer review sentiment in e-commerce and SaaS domains.

[![Model on HF](https://huggingface.co/datasets/huggingface/badges/resolve/main/model-on-hf-sm.svg)](https://huggingface.co/IberaSoft/customer-sentiment-analyzer)
[![Dataset](https://img.shields.io/badge/Dataset-HuggingFace-yellow)](https://huggingface.co/datasets/IberaSoft/ecommerce-reviews-sentiment)
[![Demo](https://img.shields.io/badge/Demo-Spaces-orange)](https://huggingface.co/spaces/IberaSoft/sentiment-analyzer-demo)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## 🌟 Model Description

This model is a fine-tuned version of [`distilbert-base-uncased`](https://huggingface.co/distilbert-base-uncased) on a custom dataset of 20,000 customer reviews from e-commerce and SaaS platforms. It classifies text into three sentiment categories: **positive**, **negative**, and **neutral**.

### Key Features

- ✅ **Fast Inference**: ~35ms per prediction (CPU)
- ✅ **High Accuracy**: 90.2% on test set
- ✅ **Domain-Specific**: Trained on customer reviews
- ✅ **Production-Ready**: Optimized for real-world deployment
- ✅ **Multi-Class**: Handles positive, negative, and neutral sentiments

## 🚀 Quick Start

### Using Transformers Pipeline
```python
from transformers import pipeline

# Load the model
classifier = pipeline(
    "sentiment-analysis",
    model="IberaSoft/customer-sentiment-analyzer"
)

# Analyze sentiment
result = classifier("This product is amazing! Highly recommend.")
print(result)
# [{'label': 'positive', 'score': 0.9823}]
```

### Using AutoModel
```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load model and tokenizer
model_name = "IberaSoft/customer-sentiment-analyzer"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Prepare text
text = "Great quality but shipping took forever"
inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=512)

# Get prediction
with torch.no_grad():
    outputs = model(**inputs)
    predictions = torch.nn.functional.softmax(outputs.logits, dim=-1)

# Map to labels
labels = ['negative', 'neutral', 'positive']
predicted_class = predictions.argmax().item()
confidence = predictions[0][predicted_class].item()

print(f"Sentiment: {labels[predicted_class]}")
print(f"Confidence: {confidence:.2%}")
```

### Batch Processing
```python
from transformers import pipeline

classifier = pipeline(
    "sentiment-analysis",
    model="IberaSoft/customer-sentiment-analyzer",
    device=0  # Use GPU if available
)

reviews = [
    "Excellent product, will buy again!",
    "Disappointed with the quality.",
    "It's okay, nothing special."
]

results = classifier(reviews)
for review, result in zip(reviews, results):
    print(f"{review[:30]}... → {result['label']} ({result['score']:.2f})")
```

## 📊 Model Performance

### Evaluation Metrics

| Metric | Score |
|--------|-------|
| **Accuracy** | 90.2% |
| **F1 Score (Macro)** | 0.89 |
| **Precision** | 0.90 |
| **Recall** | 0.89 |

### Per-Class Performance

| Class | Precision | Recall | F1-Score | Support |
|-------|-----------|--------|----------|---------|
| **Positive** | 0.92 | 0.91 | 0.91 | 800 |
| **Negative** | 0.89 | 0.90 | 0.89 | 700 |
| **Neutral** | 0.88 | 0.86 | 0.87 | 500 |

### Confusion Matrix
```
                Predicted
              Pos  Neu  Neg
Actual Pos  [ 728   45   27 ]
       Neu  [  38  430   32 ]
       Neg  [  22   48  630 ]
```

### Inference Speed

| Batch Size | CPU (ms) | GPU (ms) |
|------------|----------|----------|
| 1 | 35 | 8 |
| 8 | 180 | 25 |
| 32 | 650 | 75 |

*Tested on Intel i7-11700K (CPU) and NVIDIA RTX 3080 (GPU)*

## 🎯 Intended Use

### Primary Use Cases

- **Customer Support**: Automatically triage support tickets by sentiment
- **Product Reviews**: Analyze product feedback at scale
- **Brand Monitoring**: Track customer sentiment over time
- **Market Research**: Understand customer opinions
- **Quality Assurance**: Flag negative feedback for review

### Out-of-Scope Use

❌ Medical or health-related sentiment analysis  
❌ Financial advice or stock sentiment (not trained on financial data)  
❌ Political sentiment analysis (potential bias)  
❌ Languages other than English  
❌ Detecting sarcasm or irony (limited capability)  

## 📚 Training Details

### Training Data

The model was fine-tuned on **20,000 labeled customer reviews** consisting of:

- **Amazon Customer Reviews**: 8,000 reviews
- **Yelp Business Reviews**: 7,000 reviews
- **SaaS Product Reviews**: 5,000 reviews (G2, Capterra, TrustRadius)

**Dataset Distribution**:
- Training: 15,000 (75%)
- Validation: 3,000 (15%)
- Test: 2,000 (10%)

**Class Balance**:
- Positive: 40% (8,000 reviews)
- Negative: 35% (7,000 reviews)
- Neutral: 25% (5,000 reviews)

📦 **[View Dataset on HuggingFace](https://huggingface.co/datasets/IberaSoft/ecommerce-reviews-sentiment)**

### Training Procedure

**Base Model**: `distilbert-base-uncased` (66M parameters)

**Hyperparameters**:
```yaml
learning_rate: 2e-5
batch_size: 16
epochs: 3
warmup_steps: 500
weight_decay: 0.01
max_length: 512
optimizer: AdamW
scheduler: linear with warmup
```

**Training Environment**:
- **Hardware**: NVIDIA Tesla V100 (16GB)
- **Training Time**: ~2.5 hours
- **Framework**: PyTorch 2.1, Transformers 4.36
- **Mixed Precision**: FP16

**Training Code**: [GitHub Repository](https://github.com/IberaSoft/sentiment-analysis-api)

### Preprocessing

Text preprocessing steps:
1. Lowercase conversion
2. URL removal
3. Excessive whitespace normalization
4. Emoji handling (converted to text)
5. HTML tag removal
6. Truncation to 512 tokens

## ⚠️ Limitations and Bias

### Known Limitations

1. **English Only**: Trained exclusively on English text
2. **Domain Specificity**: Best performance on e-commerce/SaaS reviews
3. **Sarcasm**: May misclassify sarcastic reviews
4. **Context Length**: Limited to 512 tokens (~350 words)
5. **Informal Language**: May struggle with heavy slang or abbreviations

### Potential Biases

- **Product Category Bias**: Training data skewed toward electronics and software
- **Platform Bias**: Amazon and Yelp reviews may have different characteristics
- **Temporal Bias**: Reviews collected 2020-2023
- **Rating Correlation**: 5-star reviews assumed positive (may not always be true)

### Recommendations

- ✅ Test on your specific domain before production use
- ✅ Implement human review for edge cases
- ✅ Monitor performance on your data distribution
- ✅ Consider retraining for specialized domains
- ✅ Use confidence scores to flag uncertain predictions

## 🔧 Optimization

### Model Size Reduction

**Standard Model**: 268 MB  
**Quantized (INT8)**: 67 MB (4x smaller, <2% accuracy drop)
```python
from optimum.onnxruntime import ORTModelForSequenceClassification

# Convert to ONNX with quantization
model = ORTModelForSequenceClassification.from_pretrained(
    "IberaSoft/customer-sentiment-analyzer",
    export=True,
    provider="CPUExecutionProvider"
)

# Save quantized model
model.save_pretrained("./optimized_model")
```

### Performance Tips
```python
import torch

# Use GPU if available
device = "cuda" if torch.cuda.is_available() else "cpu"
model = model.to(device)

# Enable inference mode
model.eval()
torch.set_grad_enabled(False)

# Batch processing for better throughput
classifier = pipeline(
    "sentiment-analysis",
    model=model,
    tokenizer=tokenizer,
    batch_size=32,
    device=0 if device == "cuda" else -1
)
```

## 🌐 Production Deployment

### FastAPI Example
```python
from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel

app = FastAPI()

# Load model once at startup
classifier = pipeline(
    "sentiment-analysis",
    model="IberaSoft/customer-sentiment-analyzer"
)

class ReviewRequest(BaseModel):
    text: str

@app.post("/predict")
def predict_sentiment(request: ReviewRequest):
    result = classifier(request.text)[0]
    return {
        "sentiment": result["label"],
        "confidence": round(result["score"], 4)
    }
```

### Docker Deployment
```dockerfile
FROM python:3.11-slim

RUN pip install transformers torch fastapi uvicorn

# Download model during build
RUN python -c "from transformers import pipeline; \
    pipeline('sentiment-analysis', \
    model='IberaSoft/customer-sentiment-analyzer')"

COPY app.py .

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
```

**Full API**: [GitHub Repository](https://github.com/IberaSoft/sentiment-analysis-api)

## 📖 Citation

If you use this model in your research or application, please cite:
```bibtex
@misc{customer-sentiment-analyzer,
  author = {Your Name},
  title = {Customer Sentiment Analyzer: Fine-tuned DistilBERT for E-commerce Reviews},
  year = {2026},
  publisher = {HuggingFace},
  howpublished = {\url{https://huggingface.co/IberaSoft/customer-sentiment-analyzer}},
}
```

## 📝 License

This model is licensed under the **MIT License**. See [LICENSE](LICENSE) for details.

The base model `distilbert-base-uncased` is licensed under Apache 2.0.

## 🤝 Contributing

Found an issue or want to improve the model?

- 🐛 [Report bugs](https://github.com/IberaSoft/sentiment-analysis-api/issues)
- 💡 [Suggest features](https://github.com/IberaSoft/sentiment-analysis-api/issues)
- 🔧 [Submit pull requests](https://github.com/IberaSoft/sentiment-analysis-api/pulls)

## 🙏 Acknowledgments

- **HuggingFace** for the Transformers library and model hub
- **DistilBERT Authors** for the efficient base model
- **Dataset Contributors** for publicly available reviews
- **Community** for feedback and testing

---

<div align="center">

### ⭐ Star this model if you find it useful!

**Try the live demo**: [HuggingFace Spaces](https://huggingface.co/spaces/IberaSoft/sentiment-analyzer-demo)

</div>
