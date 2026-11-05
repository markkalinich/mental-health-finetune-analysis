---
license: apache-2.0
base_model: distilbert-base-uncased-finetuned-sst-2-english
tags:
- text-classification
- sentiment-analysis
- transformers
- pytorch
datasets:
- sst2
language:
- en
pipeline_tag: text-classification
---

# Sentiment Classifier Demo 5729

## Model Description

This model is based on **distilbert-base-uncased-finetuned-sst-2-english** and performs **Sentiment analysis on English text (positive/negative classification)**.

This model was uploaded as part of a machine learning assignment demonstrating model deployment to Hugging Face Hub.

## Quick Start

```python
from transformers import pipeline

# Load the model
classifier = pipeline("sentiment-analysis", model="Divi15/sentiment-classifier-demo-5729")

# Make predictions
result = classifier("I love machine learning!")
print(result)
# Expected output: [{'label': 'POSITIVE', 'score': 0.9991}]
```

## Model Details

- **Model Type**: Text Classification
- **Base Model**: distilbert-base-uncased-finetuned-sst-2-english
- **Task**: Sentiment Analysis (Binary Classification)
- **Language**: English
- **License**: Apache 2.0

## Intended Use

This model is intended for:
- Educational purposes
- Sentiment analysis of English text
- Binary classification tasks (positive/negative sentiment)

## Training Data

- **Dataset**: Stanford Sentiment Treebank (SST-2)
- **Training Examples**: ~67K sentences
- **Classes**: 2 (positive, negative)

## Performance

- **Accuracy**: ~91-92% on SST-2 test set
- **F1 Score**: ~0.91-0.92

## Usage Examples

### Basic Usage
```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from transformers import pipeline

tokenizer = AutoTokenizer.from_pretrained("Divi15/sentiment-classifier-demo-5729")
model = AutoModelForSequenceClassification.from_pretrained("Divi15/sentiment-classifier-demo-5729")

classifier = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

# Test examples
examples = [
    "I absolutely love this!",
    "This is terrible.",
    "It's okay, nothing special."
]

for text in examples:
    result = classifier(text)
    print(f"Text: {text}")
    print(f"Result: {result}")
    print()
```

### Batch Processing
```python
texts = [
    "Great product, highly recommended!",
    "Poor quality, very disappointed.",
    "Average performance, could be better."
]

results = classifier(texts)
for text, result in zip(texts, results):
    print(f"{text} -> {result['label']} ({result['score']:.3f})")
```

## Limitations

- Trained primarily on movie reviews and may not generalize well to other domains
- Binary classification only (positive/negative)
- English language only
- May exhibit biases present in the training data

## Ethical Considerations

- This model should not be used to make decisions that significantly impact individuals
- Consider potential biases when applying to different demographic groups
- Sentiment analysis can be subjective and context-dependent

## Citation

```bibtex
@misc{sentiment_classifier_demo_5729_2024,
  title={Sentiment Classifier Demo 5729},
  author={Your Name},
  year={2024},
  publisher={Hugging Face},
  url={https://huggingface.co/Divi15/sentiment-classifier-demo-5729}
}
```

## Model Card Authors

This model card was created as part of an educational assignment on model deployment and sharing.

---

*Last updated: 2025-09-08*
