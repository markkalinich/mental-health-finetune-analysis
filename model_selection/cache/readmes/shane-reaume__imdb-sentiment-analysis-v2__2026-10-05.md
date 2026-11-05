---
language: en
license: mit
library_name: transformers
tags:
- sentiment-analysis
- text-classification
- pytorch
- distilbert
- imdb
datasets:
- imdb
metrics:
- accuracy
- f1
- precision
- recall
model-index:
- name: imdb-sentiment-analysis-v2
  results:
  - task:
      type: text-classification
      name: Text Classification
    dataset:
      name: IMDB
      type: imdb
      split: test
    metrics:
    - type: accuracy
      value: 86.5
      name: Accuracy
    - type: f1
      value: 0.8672
      name: F1 Score
---

# Sentiment Analysis Model v2.0

This is an improved version of the sentiment analysis model, fine-tuned with additional challenging examples to handle difficult cases like negation, sarcasm, and subtle expressions.

## Model Details

- **Model Type:** DistilBERT (fine-tuned)
- **Task:** Binary Sentiment Classification (Positive/Negative)
- **Training Data:** IMDB Movie Reviews Dataset
- **Language:** English
- **License:** MIT
- **Version:** 2.0

## Performance

| Metric | Value |
|--------|-------|
| Accuracy | 86.50% |
| F1 Score | 0.8672 |
| Precision | 84.21% |
| Recall | 89.47% |

## Training Details

The model was trained on the IMDB dataset augmented with challenging examples specifically designed to improve performance on difficult sentiment analysis cases.

### Training Hyperparameters

- Learning Rate: 2e-5
- Batch Size: 16 (effective batch size: 32 with gradient accumulation)
- Epochs: 3
- Optimizer: AdamW with weight decay
- Mixed Precision: FP16

## Usage

### Direct Use with Pipeline

```python
from transformers import pipeline

# Load the model
sentiment = pipeline("sentiment-analysis", model="shane-reaume/imdb-sentiment-analysis-v2")

# Analyze text
result = sentiment("I really enjoyed this movie!")
print(result)  # [{'label': 'POSITIVE', 'score': 0.9998}]

# Batch processing
texts = [
    "This movie was absolutely amazing, I loved every minute of it!",
    "The acting was terrible and the plot made no sense at all."
]
results = sentiment(texts)
for i, (text, result) in enumerate(zip(texts, results)):
    print(f"Text: {{text}}")
    print(f"Sentiment: {{result['label']}}, Score: {{result['score']:.4f}}")
```

### Loading Model Directly

```python
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch

# Load model and tokenizer
model_name = "shane-reaume/imdb-sentiment-analysis-v2"
model = AutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Prepare text
text = "I really enjoyed this movie!"
inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)

# Get prediction
with torch.no_grad():
    outputs = model(**inputs)
    
# Process outputs
probabilities = torch.nn.functional.softmax(outputs.logits, dim=-1)
prediction = torch.argmax(probabilities, dim=-1).item()
confidence = probabilities[0][prediction].item()

# Map prediction to label (0: negative, 1: positive)
sentiment_label = "POSITIVE" if prediction == 1 else "NEGATIVE"
print(f"Sentiment: {{sentiment_label}}, Confidence: {{confidence:.4f}}")
```

## Limitations

- The model is trained primarily on movie reviews and may not perform as well on other domains.
- The model may struggle with certain types of text:
  - Sarcasm and irony
  - Mixed sentiment expressions
  - Subtle negative expressions
  - Complex negations

## Citation

If you use this model in your research, please cite:

```
@misc{sentiment-analysis-model,
  author = {Your Name},
  title = {Sentiment Analysis Model based on DistilBERT},
  year = {2023},
  publisher = {Hugging Face},
  howpublished = {\url{https://huggingface.co/shane-reaume/imdb-sentiment-analysis-v2}}
}
```
