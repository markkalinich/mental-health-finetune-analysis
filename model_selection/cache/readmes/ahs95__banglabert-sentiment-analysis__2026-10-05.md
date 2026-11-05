---
license: apache-2.0
datasets:
- SayedShaun/sentigold
language:
- bn
metrics:
- accuracy
- f1
base_model:
- csebuetnlp/banglabert
pipeline_tag: text-classification
tags:
- sentiment-analysis
- bengali
- bangla
- multilabel-classification
library_name: transformers
---

# BanglaBERT Fine-tuned for Bangla Sentiment Analysis

## Model Description

This model is a fine-tuned version of [`csebuetnlp/banglabert`](https://huggingface.co/csebuetnlp/banglabert) on the [SentiGOLD](https://arxiv.org/pdf/2306.06147) dataset for 5-class sentiment analysis in Bengali. It classifies text into:
1. 😠 Very Negative (SN)
2. 😞 Negative (WN)
3. 😐 Neutral (N)
4. 😊 Positive (WP)
5. 😍 Very Positive (SP)

**Key Features:**
- State-of-the-art Bangla language understanding
- Handles both formal and informal Bengali text
- Optimized for social media, reviews, and customer feedback
- Requires text normalization using [Bangla Normalizer](https://github.com/csebuetnlp/normalizer)

## Intended Uses & Limitations

### Primary Use
- Sentiment analysis of Bengali text
- Social media monitoring
- Customer feedback analysis
- Product review classification

### Limitations
- Performance may degrade on code-mixed text (Bengali-English)
- May struggle with sarcasm and highly contextual expressions
- Best for short to medium-length texts (up to 512 tokens)

## Training Data

The model was fine-tuned on **SentiGOLD**, the largest gold-standard Bangla sentiment analysis dataset:

| Feature                | Value         |
|------------------------|---------------|
| Total Samples          | 70,000        |
| Domains Covered        | 30+           |
| Source Diversity       | Social media, news, blogs, reviews |
| Class Distribution     | Balanced across 5 classes |
| Annotation Quality     | Fleiss' kappa = 0.88 |

## Training Procedure

### Hyperparameters

| Parameter | Value |
| --- | --- |
| Learning Rate | 2e-5 → 1.05e-6 |
| Batch Size | 48 |
| Epochs | 5 |
| Optimizer | AdamW |
| Scheduler | ReduceLROnPlateau |
| Weight Decay | 0.01 |
| Gradient Accumulation | 4 steps |
| Warmup Ratio | 5% |

### Techniques

* Class-weighted loss handling imbalance
* Early stopping (patience=3)
* Mixed precision (FP16) training
* Gradient checkpointing
* Text normalization using Bangla Normalizer

## Evaluation Results

### Validation Performance

| Epoch | F1 (Macro) | Accuracy | Very Neg F1 | Neg F1 | Neu F1 | Pos F1 | Very Pos F1 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.6334 | 0.6331 | 0.6789 | 0.5834 | 0.6407 | 0.5635 | 0.7004 |
| 5 | 0.6537 | 0.6551 | 0.7081 | 0.6157 | 0.6421 | 0.5789 | 0.7236 |

### Final Test Performance

| Metric | Score |
| --- | --- |
| Macro F1 | 0.6660 |
| Accuracy | 0.6671 |

## How to Use

### Direct Inference

```python
from transformers import pipeline
from normalizer import normalize

# Load model
classifier = pipeline(
    "text-classification", 
    model="ahs95/banglabert-sentiment-analysis",
    tokenizer="ahs95/banglabert-sentiment-analysis"
)

# Prepare text
text = "আপনার পণ্যটি অসাধারণ! আমি খুবই সন্তুষ্ট।"
normalized_text = normalize(text)  # Important for BanglaBERT

# Classify
result = classifier(normalized_text)
print(f"Sentiment: {result[0]['label']} (Confidence: {result[0]['score']:.2f})")
```

### Advanced Usage
```python

from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
from normalizer import normalize

# Load model and tokenizer
model_name = "ahs95/banglabert-sentiment-analysis"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Prepare inputs
texts = [
    "সেবা খুব খারাপ ছিল। আমি কখনো ফিরে আসব না।",
    "পণ্যটির গুণগত মান মোটামুটি ভাল"
]
normalized_texts = [normalize(t) for t in texts]

# Tokenize and predict
inputs = tokenizer(normalized_texts, padding=True, truncation=True, return_tensors="pt")
with torch.no_grad():
    outputs = model(**inputs)
    probabilities = torch.nn.functional.softmax(outputs.logits, dim=-1)

# Get predictions
sentiment_labels = ["Very Negative", "Negative", "Neutral", "Positive", "Very Positive"]
predictions = [sentiment_labels[p] for p in probabilities.argmax(dim=1)]

for text, pred in zip(texts, predictions):
    print(f"Text: {text}\nPredicted Sentiment: {pred}\n")
```

### Ethical Considerations
- **Bias:** While SentiGOLD reduces bias through synthetic data, real-world validation is recommended

- **Use Cases:** Suitable for:
  * Product feedback analysis
  * Social media monitoring
  * Market research
  
  - **Avoid:** Critical decision systems without human oversight

### Citation 
If you use this model, please cite:

```bibtex
@misc{banglabert-sentiment,
  author = {Arshadul Hoque},
  title = {Fine-tuned BanglaBERT for Bengali Sentiment Analysis},
  year = {2025},
  publisher = {Hugging Face},
  howpublished = {\url{https://huggingface.co/ahs95/banglabert-sentiment-analysis}}
}
```

### Contact
For questions and support: ahsbd95@gmail.com