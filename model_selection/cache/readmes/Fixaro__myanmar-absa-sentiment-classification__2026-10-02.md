---
language:
  - my
license: mit
tags:
  - text-classification
  - sentiment-analysis
  - aspect-based-sentiment-analysis
  - absa
  - burmese
  - xlm-roberta
  - sentence-pair
---

# Myanmar ABSA - Sentiment Classification Model (Stage 2)

An aspect-level sentiment classification model for Burmese product/service reviews. This is Stage 2 of a two-stage Aspect-Based Sentiment Analysis (ABSA) pipeline that predicts sentiment polarity given a review and an aspect category.

## Model Details

- **Base Model:** [xlm-roberta-base](https://huggingface.co/xlm-roberta-base)
- **Architecture:** XLM-RoBERTa for Sequence Classification
- **Problem Type:** Single-label classification (sentence-pair)
- **Language:** Burmese (Myanmar)
- **License:** MIT

## Sentiment Classes

The model predicts sentiment polarity for a given aspect:

- **0: negative** - Negative sentiment or dissatisfaction
- **1: neutral** - Neutral or factual statements
- **2: positive** - Positive sentiment or satisfaction

## Input Format

This model uses **sentence-pair classification**:
- **Text:** The review text
- **Text Pair:** The aspect category (one of 5 aspects)

### Supported Aspects

1. `product_quality`
2. `fulfillment_and_speed`
3. `price_and_value`
4. `staff_and_service`
5. `variety_and_availability`

## Training Data

- **Total Samples:** 5,247 aspect-level annotations
- **Data Split:** Stratified train/val/test split
  - Train: 4,197 samples
  - Validation: 525 samples
  - Test: 525 samples
- **Alignment:** Filtered to match Stage 1 aspect taxonomy
- **Label Distribution:**
  - Negative: 2,107 samples (40.2%)
  - Neutral: 406 samples (7.7%)
  - Positive: 2,734 samples (52.1%)

## Performance Metrics

Evaluated on the test set:

| Metric | Score |
|--------|-------|
| **F1 Macro** | 0.8671 |
| **F1 Micro** | 0.9124 |
| **F1 Weighted** | 0.9115 |

### Per-Class Performance

| Class | Precision | Recall | F1-Score |
|-------|-----------|--------|----------|
| **negative** | 0.92 | 0.92 | 0.92 |
| **neutral** | 0.81 | 0.71 | 0.75 |
| **positive** | 0.92 | 0.94 | 0.93 |

### Training Configuration

- **Learning Rate:** 2e-5
- **Batch Size:** 8 (with gradient accumulation steps = 4, effective batch size = 32)
- **Epochs:** 4
- **Max Sequence Length:** 128 tokens
- **Optimizer:** AdamW
- **Precision:** bfloat16

## Usage

### Basic Usage with Pipeline

```python
from transformers import pipeline

# Load the model
classifier = pipeline(
    "text-classification",
    model="Fixaro/myanmar-absa-sentiment-classification"
)

# Predict sentiment for a specific aspect
review = "ပစ္စည်းအရည်အသွေးက ကောင်းပါတယ်"
aspect = "product_quality"

result = classifier({
    "text": review,
    "text_pair": aspect.replace('_', ' ')  # Convert to readable format
})

print(f"Sentiment: {result[0]['label']}")
print(f"Confidence: {result[0]['score']:.4f}")
```

### Advanced Usage with Tokenizer

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load model and tokenizer
model_name = "Fixaro/myanmar-absa-sentiment-classification"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Prepare input (sentence pair)
review = "ဈေးလည်း သက်သာတယ်၊ ပို့တာလည်း မြန်တယ်"
aspect = "price_and_value"

inputs = tokenizer(
    review,
    aspect.replace('_', ' '),  # Convert to readable format
    return_tensors="pt",
    truncation=True,
    max_length=128,
    padding=True
)

# Get predictions
with torch.no_grad():
    outputs = model(**inputs)
    logits = outputs.logits
    probabilities = torch.softmax(logits, dim=-1)
    predicted_class = torch.argmax(probabilities, dim=-1).item()

# Map to sentiment label
sentiment_labels = {0: "negative", 1: "neutral", 2: "positive"}
predicted_sentiment = sentiment_labels[predicted_class]

print(f"Aspect: {aspect}")
print(f"Sentiment: {predicted_sentiment}")
print(f"Confidence: {probabilities[0][predicted_class]:.4f}")
```

### Complete ABSA Pipeline Example

```python
from transformers import pipeline

# Load both models
aspect_detector = pipeline(
    "text-classification",
    model="Fixaro/myanmar-absa-aspect-detection",
    return_all_scores=True,
    function_to_apply="sigmoid"
)

sentiment_classifier = pipeline(
    "text-classification",
    model="Fixaro/myanmar-absa-sentiment-classification"
)

# Analyze a review
review = "ပစ္စည်းက ကောင်းတယ်၊ ဒါပေမယ့် ပို့တာ နည်းနည်း ကြာတယ်"

# Stage 1: Detect aspects
aspect_scores = aspect_detector(review)[0]
detected_aspects = [
    result['label'] 
    for result in aspect_scores 
    if result['score'] > 0.5
]

# Stage 2: Classify sentiment for each aspect
results = []
for aspect in detected_aspects:
    sentiment_result = sentiment_classifier({
        "text": review,
        "text_pair": aspect.replace('_', ' ')
    })
    results.append({
        "aspect": aspect,
        "sentiment": sentiment_result[0]['label'],
        "confidence": sentiment_result[0]['score']
    })

# Display results
print(f"Review: {review}\n")
for result in results:
    print(f"Aspect: {result['aspect']}")
    print(f"Sentiment: {result['sentiment']} ({result['confidence']:.4f})\n")
```

## Model Architecture

```
XLM-RoBERTa Base (xlm-roberta-base)
├── Encoder: 12 transformer layers
├── Hidden size: 768
├── Attention heads: 12
└── Classification head: Linear(768, 3) with softmax activation
```

## Limitations and Biases

- **Aspect Dependency:** Performance depends on accurate aspect detection from Stage 1
- **Class Imbalance:** Neutral class has fewer samples (7.7%), leading to lower recall
- **Context Sensitivity:** May struggle with sarcastic or context-dependent sentiment
- **Aspect Specificity:** Requires explicit aspect input; cannot infer aspect from context
- **Domain Specificity:** Trained on product/service reviews; may not generalize to other domains

## Intended Use

This model is intended for:
- Aspect-level sentiment analysis in Burmese reviews
- Second stage of ABSA pipelines (after aspect detection)
- Fine-grained sentiment analysis
- Research and academic purposes
- Commercial applications with proper validation

## Citation

If you use this model in your research, please cite:

```bibtex
@software{myanmar_absa_sentiment_classification,
  title = {Myanmar ABSA: Sentiment Classification Model},
  author = {Fixaro},
  year = {2026},
  publisher = {Hugging Face},
  url = {https://huggingface.co/Fixaro/myanmar-absa-sentiment-classification}
}
```

## Related Models

- **Stage 1 Model:** [Fixaro/myanmar-absa-aspect-detection](https://huggingface.co/Fixaro/myanmar-absa-aspect-detection) - Multi-label aspect detection

## Contact

For questions or issues, please open an issue on the model repository.
