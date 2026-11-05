---
language: en
tags:
- sentiment-analysis
- text-classification
- roberta
- imdb
- pytorch
- transformers
datasets:
- imdb
metrics:
- accuracy
- f1
model-index:
- name: nkadoor/sentiment-classifier-roberta
  results:
  - task:
      type: text-classification
      name: Text Classification
    dataset:
      name: imdb
      type: imdb
    metrics:
    - type: accuracy
      value: 0.9590
    - type: f1
      value: 0.9791
---

# Fine-tuned Sentiment Classification Model

This model is a fine-tuned version of [roberta-base](https://huggingface.co/roberta-base) for sentiment analysis on movie reviews.

## Model Details

- **Model type:** Text Classification (Sentiment Analysis)
- **Base model:** roberta-base
- **Language:** English
- **Task:** Binary sentiment classification (positive/negative)
- **Training dataset:** IMDB Movie Reviews Dataset
- **Training samples:** 5000 samples
- **Validation samples:** 1000 samples
- **Test samples:** 1000 samples

## Performance

| Metric | Value |
|--------|-------|
| Test Accuracy | 0.9590 |
| Test F1 Score | 0.9791 |
| Test Precision | 1.0000 |
| Test Recall | 0.9590 |

## Training Details

| Parameter | Value |
|-----------|-------|
| Training epochs | 3 |
| Batch size | 16 |
| Learning rate | 5e-05 |
| Warmup steps | 500 |
| Weight decay | 0.01 |
| Max sequence length | 512 |

## Usage

### Quick Start

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

# Using pipeline (recommended for quick inference)
classifier = pipeline("sentiment-analysis", 
                     model="nkadoor/sentiment-classifier-roberta",
                     tokenizer="nkadoor/sentiment-classifier-roberta")

result = classifier("This movie was amazing!")
print(result)  # [{'label': 'POSITIVE', 'score': 0.99}]
```

### Manual Usage

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("nkadoor/sentiment-classifier-roberta")
model = AutoModelForSequenceClassification.from_pretrained("nkadoor/sentiment-classifier-roberta")

def predict_sentiment(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)
    
    with torch.no_grad():
        outputs = model(**inputs)
        predictions = torch.nn.functional.softmax(outputs.logits, dim=-1)
        predicted_class = torch.argmax(predictions, dim=-1).item()
        confidence = predictions[0][predicted_class].item()
    
    sentiment = "positive" if predicted_class == 1 else "negative"
    return sentiment, confidence

# Example usage
text = "This movie was absolutely fantastic!"
sentiment, confidence = predict_sentiment(text)
print(f"Sentiment: {sentiment} (Confidence: {confidence:.4f})")
```

## Dataset

The model was trained on the [IMDB Movie Reviews Dataset](https://huggingface.co/datasets/imdb), which contains movie reviews labeled as positive or negative sentiment. The dataset consists of:

- 25,000 training reviews
- 25,000 test reviews
- Balanced distribution of positive and negative sentiments

## Intended Use

This model is intended for sentiment analysis of English movie reviews or similar text. It can be used to:

- Analyze sentiment in movie reviews
- Classify text as positive or negative
- Build sentiment analysis applications
- Research in sentiment analysis

## Limitations

- Trained specifically on movie reviews, may not generalize well to other domains
- Limited to English language
- Binary classification only (positive/negative)
- May reflect biases present in the training data

## Citation

If you use this model, please cite:

```bibtex
@misc{sentiment-classifier-roberta,
  title={Fine-tuned RoBERTa for Sentiment Analysis},
  author={Narayana Kadoor},
  year={2025},
  url={https://huggingface.co/nkadoor/sentiment-classifier-roberta}
}
```

## Training Logs

Final training metrics:
- Final training loss: N/A
- Best validation F1: 0.9791
- Total training time: 3.0 epochs completed

---

*Model trained using Transformers library by Hugging Face*
