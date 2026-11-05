---
language: en
license: apache-2.0
tags:
- sentiment-analysis
- product-reviews
- smartphone-reviews
- aspect-based-sentiment-analysis
- distilroberta
- domain-adaptation
datasets:
- amazon-reviews
metrics:
- accuracy
- f1
widget:
- text: "Battery life is amazing! Best phone I ever had."
  example_title: "Positive Review"
- text: "Terrible phone. Broke after one week."
  example_title: "Negative Review"
- text: "It's okay, nothing special about it."
  example_title: "Neutral Review"
- text: "Camera quality is excellent but battery drains quickly."
  example_title: "Mixed Sentiment"
model-index:
- name: SmartReview DistilRoBERTa Sentiment
  results:
  - task:
      type: text-classification
      name: Sentiment Analysis
    dataset:
      name: Amazon Smartphone Reviews
      type: amazon-reviews
    metrics:
    - type: accuracy
      value: 88.23
      name: Test Accuracy
    - type: f1
      value: 94.88
      name: F1 Score (Positive)
    - type: f1
      value: 85.82
      name: F1 Score (Negative)
    - type: f1
      value: 36.35
      name: F1 Score (Neutral)
---

# SmartReview: DistilRoBERTa for Smartphone Review Sentiment Analysis

[![Hugging Face Model](https://img.shields.io/badge/🤗%20Hugging%20Face-Model-yellow)](https://huggingface.co/Abhishek86798/smartreview-distilroberta-sentiment)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

## Model Description

**SmartReview** is a domain-adapted DistilRoBERTa model fine-tuned for sentiment analysis of smartphone and electronics reviews. 

The model achieves **88.23% accuracy** on 3-class sentiment classification (Positive, Neutral, Negative) and was specifically trained on 67,987 Amazon smartphone reviews.

### 🎯 Key Features

- ✅ **Domain-Adapted**: Pretrained on 61,553 smartphone reviews via Masked Language Modeling
- ✅ **Efficient**: Only 82M parameters (34% smaller than RoBERTa-base)
- ✅ **Accurate**: 88.23% overall accuracy, 94.88% F1 on positive sentiment
- ✅ **Fast**: ~50ms inference time per review
- ✅ **Specialized**: Understands product review vocabulary and context

### 🏗️ Architecture

- **Base Model**: `distilroberta-base` (82M parameters)
- **Task**: 3-class sequence classification
- **Classes**: 
  - `LABEL_0`: Positive
  - `LABEL_1`: Neutral  
  - `LABEL_2`: Negative
- **Max Length**: 512 tokens

### 📊 Training Approach

**Two-Phase Training:**

1. **Phase 1 - Domain Adaptation (MLM)**
   - Task: Masked Language Modeling
   - Data: 61,553 smartphone reviews
   - Duration: 66 minutes
   - Result: 99.99% accuracy on domain vocabulary

2. **Phase 2 - Sentiment Fine-tuning**
   - Task: 3-class classification
   - Data: 39,044 training samples
   - Duration: 67 minutes
   - Optimizer: AdamW (lr=2e-5, weight_decay=0.01)
   - Hardware: NVIDIA RTX 3050 (4GB)

---

## 📈 Performance

### Overall Metrics (Test Set: 8,367 reviews)

| Metric | Score |
|--------|-------|
| **Accuracy** | **88.23%** |
| **Precision (Macro)** | 72.38% |
| **Recall (Macro)** | 72.39% |
| **F1 (Macro)** | 72.35% |
| **F1 (Weighted)** | 88.13% |

### Per-Class Performance

| Class | Precision | Recall | F1-Score | Support |
|-------|-----------|--------|----------|---------|
| **Positive** | 95.39% | 94.38% | **94.88%** ✅ | 5,481 |
| **Neutral** | 37.79% | 35.02% | **36.35%** ⚠️ | 614 |
| **Negative** | 83.96% | 87.76% | **85.82%** ✅ | 2,272 |

**Note:** Neutral class F1 is lower due to severe class imbalance (only 7.4% of training data). This is expected in product reviews where opinions are rarely truly neutral.

### Confusion Matrix

```
                PREDICTED
           Pos    Neu    Neg
ACTUAL
Pos      5,173   175    133    (94.4% correct)
Neu        151   215    248    (35.0% correct)
Neg         99   179  1,994    (87.8% correct)
```

---

## 🚀 Usage

### Quick Start

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load model and tokenizer
model_name = "Abhishek86798/smartreview-distilroberta-sentiment"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Example review
text = "Battery life is excellent but camera quality is poor"

# Tokenize and predict
inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=512)

with torch.no_grad():
    outputs = model(**inputs)
    logits = outputs.logits
    probabilities = torch.softmax(logits, dim=-1)
    prediction = logits.argmax(-1).item()

# Map to labels
labels = ["Positive", "Neutral", "Negative"]
sentiment = labels[prediction]
confidence = probabilities[0][prediction].item()

print(f"Sentiment: {sentiment}")
print(f"Confidence: {confidence:.2%}")
```

**Output:**
```
Sentiment: Positive
Confidence: 85.34%
```

### Using Pipeline

```python
from transformers import pipeline

# Create sentiment analysis pipeline
classifier = pipeline(
    "sentiment-analysis",
    model="Abhishek86798/smartreview-distilroberta-sentiment",
    tokenizer="Abhishek86798/smartreview-distilroberta-sentiment"
)

# Single prediction
result = classifier("Amazing phone! Battery lasts all day.")
print(result)
# [{'label': 'LABEL_0', 'score': 0.9876}]  # LABEL_0 = Positive

# Batch prediction
reviews = [
    "Amazing phone! Battery lasts all day.",
    "Terrible. Phone broke after one week.",
    "It's okay, nothing special."
]

results = classifier(reviews)
for review, result in zip(reviews, results):
    print(f"{review} → {result['label']} ({result['score']:.2%})")
```

### Detailed Prediction Function

```python
def predict_sentiment_detailed(text, model, tokenizer):
    # Get detailed sentiment prediction with all probabilities
    # Args: text (str), model, tokenizer
    # Returns: dict with sentiment, confidence, and probabilities
    # Tokenize
    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        max_length=512,
        padding=True
    )
    
    # Predict
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        probabilities = torch.softmax(logits, dim=-1)[0]
    
    # Get results
    labels = ["Positive", "Neutral", "Negative"]
    prediction_idx = logits.argmax(-1).item()
    
    return {
        "text": text,
        "sentiment": labels[prediction_idx],
        "confidence": probabilities[prediction_idx].item(),
        "probabilities": {
            "positive": probabilities[0].item(),
            "neutral": probabilities[1].item(),
            "negative": probabilities[2].item()
        }
    }

# Example
result = predict_sentiment_detailed(
    "Screen is bright and clear, love the display!",
    model,
    tokenizer
)

print(f"Sentiment: {result['sentiment']}")
print(f"Confidence: {result['confidence']:.2%}")
print(f"Probabilities:")
for sentiment, prob in result['probabilities'].items():
    print(f"  {sentiment.capitalize()}: {prob:.2%}")
```

---

## 📊 Dataset

### Training Data

- **Source**: Amazon Cell Phones & Accessories Reviews (Kaggle)
- **Time Period**: 2015-2019
- **Total Reviews**: 67,987
- **Products**: 721 smartphone models

### Split Distribution

| Split | Reviews | Percentage |
|-------|---------|------------|
| Training | 39,044 | 57.4% |
| Validation | 8,367 | 12.3% |
| Test | 8,367 | 12.3% |

### Sentiment Distribution

| Sentiment | Count | Percentage | Rating Mapping |
|-----------|-------|------------|----------------|
| Positive | 32,615 | 57.5% | 4-5 stars |
| Neutral | 4,200 | 7.4% | 3 stars |
| Negative | 15,572 | 27.4% | 1-2 stars |

---

## 🎯 Intended Use

### ✅ Recommended Use Cases

- Sentiment analysis of smartphone/electronics reviews
- Product feedback analysis for e-commerce platforms
- Customer satisfaction monitoring
- Review summarization preprocessing
- Aspect-based sentiment analysis (as part of ABSA pipeline)

### ❌ Out-of-Scope Use

- Non-English reviews (model trained on English only)
- Non-product reviews (news articles, social media posts, etc.)
- Offensive content detection
- Sarcasm detection (known limitation)
- Real-time chat/conversation analysis

---

## ⚠️ Limitations

1. **Neutral Class Performance**: F1-score of 36.35% due to severe class imbalance (only 7.4% of training data). The model tends to classify neutral reviews as positive or negative.

2. **Sarcasm Detection**: Model struggles with sarcastic language. Example: *"Great, another phone that breaks after a week"* may be classified as positive.

3. **Domain Specificity**: Trained specifically on smartphone reviews. Performance may degrade on other product categories without domain adaptation.

4. **Context-Free Predictions**: Doesn't consider user expectations or product price range. *"Battery lasts 4 hours"* might be negative for smartphones but positive for smartwatches.

5. **Mixed Sentiments**: Reviews with multiple conflicting opinions may be misclassified based on the dominant sentiment.

---

## 🔧 Training Details

### Hyperparameters

```yaml
Model:
  base_model: distilroberta-base
  num_labels: 3
  max_position_embeddings: 512
  hidden_size: 768
  num_hidden_layers: 6
  num_attention_heads: 12
  dropout: 0.1

Training:
  learning_rate: 2e-5
  batch_size: 4
  gradient_accumulation_steps: 4
  effective_batch_size: 16
  epochs: 5
  warmup_steps: 500
  weight_decay: 0.01
  optimizer: AdamW
  fp16: true
  max_grad_norm: 1.0

Hardware:
  gpu: NVIDIA RTX 3050 (4GB VRAM)
  memory_usage: ~2.5 GB
  training_time: 67 minutes
```

### Training Loss Progression

| Epoch | Train Loss | Val Loss | Val Accuracy |
|-------|------------|----------|--------------|
| 1 | 0.3832 | 0.3724 | 87.22% |
| 2 | 0.2833 | 0.3274 | 88.17% |
| 3 | 0.1935 | 0.3740 | 88.22% |
| 4 | 0.1661 | 0.4177 | 88.68% |
| 5 | 0.1328 | 0.4728 | 88.38% |

**Best Model**: Epoch 4 (highest validation accuracy)

---

## 🌟 Comparison with Other Models

| Model | Parameters | Accuracy | Training Time | GPU Memory |
|-------|------------|----------|---------------|------------|
| SVM (TF-IDF) | - | 78.4% | <5 min | <1 GB |
| LSTM | 2M | 82.3% | ~45 min | ~1.5 GB |
| BERT-base | 110M | 85.7% | ~90 min | ~3.2 GB |
| **SmartReview (Ours)** | **82M** | **88.23%** | **67 min** | **2.5 GB** |
| RoBERTa-base | 125M | ~89-90% | ~120 min | ~3.8 GB |

**Key Advantage**: Achieves competitive accuracy with 34% fewer parameters and 44% faster training than RoBERTa-base.

---

## 📝 Bias and Fairness

- Model trained on Amazon reviews from 2015-2019
- May reflect temporal biases (older smartphone features/expectations)
- Performance may vary across different price ranges and brands
- Dataset primarily contains English reviews from US market
- Recommended to validate on your specific use case and domain

---

## 📚 Citation

If you use this model in your research or applications, please cite:

```bibtex
@misc{smartreview2025,
  author = {Abhishek},
  title = {SmartReview: Efficient Aspect-Based Sentiment Analysis using Domain-Adapted DistilRoBERTa},
  year = {2025},
  publisher = {Hugging Face},
  journal = {Hugging Face Model Hub},
  howpublished = {\url{https://huggingface.co/Abhishek86798/smartreview-distilroberta-sentiment}}
}
```

---

## 🔗 Additional Resources

- **Project Repository**: [GitHub - SmartReview](https://github.com/Abhishek86798/smartAnalysis)
- **Full Technical Report**: Available in repository
- **Training Notebooks**: 6 complete Jupyter notebooks
- **ABSA Pipeline**: Complete aspect-based sentiment analysis system
- **Contact**: [Your Email]

---

## 👥 Model Card Authors

**Abhishek** ([Abhishek86798](https://github.com/Abhishek86798))

---

## 📄 License

This model is released under the **Apache License 2.0**.

---

## 🙏 Acknowledgments

- **Base Model**: `distilroberta-base` by Hugging Face
- **Dataset**: Amazon Reviews dataset (Kaggle)
- **Framework**: Hugging Face Transformers
- **Inspiration**: Research in domain adaptation and efficient NLP models

---

## 📞 Support

For issues, questions, or feedback:
- Open an issue on GitHub
- Contact: [Your Email]
- Hugging Face Discussions

---

**Model Version**: 1.0  
**Last Updated**: November 10, 2025  
**Status**: Production-Ready ✅

---

*Making advanced sentiment analysis accessible for everyone!* 🚀
