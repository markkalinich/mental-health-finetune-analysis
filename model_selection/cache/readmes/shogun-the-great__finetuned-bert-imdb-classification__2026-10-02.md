---
library_name: transformers
tags:
  - text-classification
  - sentiment-analysis
  - distilbert
  - sequence-classification
  - huggingface
datasets:
  - imdb
---
# Model Card for Fine-tuned DistilBERT on IMDB for Sentiment Analysis

## Model Details

### Model Description
This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) for Sentiment Analysis using the [IMDB dataset](https://huggingface.co/datasets/stanfordnlp/imdb). The model classifies movie reviews as either positive or negative sentiment.

- **Developed by:** [shogun-the-great]
- **Model type:** Sequence Classification (Sentiment Analysis)
- **Language(s):** English
- **License:** Apache-2.0 (or specify your license)
- **Finetuned from model:** `distilbert-base-uncased`

### Model Sources
- **Dataset:** [imdb](https://huggingface.co/datasets/stanfordnlp/imdb)

## Uses

### Direct Use
This model can be directly used for sentiment analysis tasks on movie reviews and similar text content. Typical use cases include:
- Review sentiment classification
- Customer feedback analysis
- Social media sentiment monitoring
- Product review analysis

### Downstream Use
This model can be further fine-tuned for specific tasks requiring sentiment analysis in specific domains like product reviews, social media content, etc.

### Out-of-Scope Use
This model might not perform well for:
- Non-English text
- Text domains very different from movie reviews
- Fine-grained sentiment analysis (beyond binary positive/negative classification)

## Bias, Risks, and Limitations

### Bias
The model's predictions are influenced by the IMDB dataset used during fine-tuning. If the dataset contains biases related to certain movie genres, directors, or actors, they may be reflected in the predictions.

### Risks
- False positives/negatives: Incorrectly classified sentiment, especially for reviews with complex or nuanced opinions
- Limited generalization to non-entertainment domains
- Potential reinforcement of existing biases in movie review data

### Recommendations
- Regularly update the model with diverse data for better generalization
- Review and monitor predictions to ensure accuracy across different types of content
- Consider using this model as part of a larger system with human oversight for critical applications

## Training Details

### Training Data
The model was trained on the IMDB dataset, which contains 25,000 movie reviews for training and 25,000 for testing, with balanced positive and negative labels.

### Training Procedure
- **Preprocessing:** Text was tokenized using the DistilBERT tokenizer with maximum sequence length of 512 tokens
- **Training Hyperparameters:**
  - Learning rate: 2e-5
  - Batch size: 16
  - Number of epochs: 3
  - Weight decay: 0.01
  - Optimizer: AdamW
- **Evaluation Results:** Accuracy of approximately 92.5% on the test set

## How to Get Started with the Model

You can load the fine-tuned model directly from the Hugging Face Hub:

```python
from transformers import pipeline

# Load model directly
classifier = pipeline("sentiment-analysis", model="shogun-the-great/distilbert-imdb-finetuned")

# Example usage
texts = [
    "This movie was absolutely fantastic! I loved every minute of it.",
    "What a waste of time. The plot made no sense and the acting was terrible."
]

results = classifier(texts)
for text, result in zip(texts, results):
    sentiment = "positive" if result["label"] == "LABEL_1" else "negative"
    print(f"Text: {text}")
    print(f"Sentiment: {sentiment} (Score: {result['score']:.4f})")
    print()
```

Alternatively, you can load the model and tokenizer separately:

```python
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch

# Load model and tokenizer
model_name = "shogun-the-great/distilbert-imdb-finetuned"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Example usage
text = "This movie was absolutely fantastic! I loved every minute of it."
inputs = tokenizer(text, return_tensors="pt", truncation=True)
outputs = model(**inputs)
prediction = torch.nn.functional.softmax(outputs.logits, dim=-1)
sentiment = "positive" if prediction[0][1] > prediction[0][0] else "negative"
score = prediction[0][1].item() if sentiment == "positive" else prediction[0][0].item()
print(f"Sentiment: {sentiment} (Score: {score:.4f})")
```

## Model Architecture

DistilBERT with a sequence classification head:
- 6 layers
- 768 hidden dimension
- 12 attention heads
- 66M parameters total