---
license: mit
datasets:
- stanfordnlp/imdb
language:
- en
metrics:
- accuracy
base_model:
- google-bert/bert-base-uncased
pipeline_tag: text-classification
library_name: transformers
tags:
- code
- sentiment-analysis
- bert
- imdb
- text-classification
- nlp
---
# BERT IMDb Sentiment Analysis Model

This repository contains a fine-tuned BERT model for sentiment analysis on IMDb movie reviews. The model classifies text as either **Positive** or **Negative** sentiment.
## Live Demo: https://huggingface.co/spaces/philipobiorah/bert-sentiment-analysis
## Model Details
- **Base Model**: `bert-base-uncased`
- **Dataset**: IMDb Movie Reviews
- **Task**: Sentiment Analysis (Binary Classification)
- **Fine-tuned on**: IMDb dataset
- **Labels**:
  - `0`: Negative
  - `1`: Positive
## Evaluation
| **Model**                         | **SST-2 Accuracy** | **Yelp Accuracy** | **Amazon Accuracy** | **IMDB Accuracy** |
|-----------------------------------|------------------|------------------|------------------|------------------|
| **philipobiorah/bert-imdb-model** | **0.89**         | **0.89**         | **0.89**         | **0.96**         |
| **DistilBERT-SST-2**              | **0.94**         | **0.85**         | **0.85**         | **0.89**         |
| **RoBERTa-Sentiment**             | **0.40**         | **0.42**         | **0.47**         | **0.79**         |
| **Logistic Regression**           | **0.83**         | **0.91**         | **0.86**         | **0.85**         |
| **Naive Bayes**                   | **0.77**         | **0.86**         | **0.84**         | **0.85**         |

## Usage
### **Load the Model in Python**
```python
from transformers import BertTokenizer, BertForSequenceClassification
import torch

model_name = "philipobiorah/bert-imdb-model"

# Load tokenizer and model
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
model = BertForSequenceClassification.from_pretrained(model_name)

# Define function for sentiment prediction with confidence score
def predict_sentiment(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)
    
    with torch.no_grad():
        logits = model(**inputs).logits
    
    # Convert logits to probabilities
    probabilities = torch.nn.functional.softmax(logits, dim=1)[0]
    
    # Get predicted class (0 = Negative, 1 = Positive)
    sentiment_idx = probabilities.argmax().item()
    confidence = probabilities[sentiment_idx].item() * 100  # Convert to percentage
    
    sentiment_label = "Positive" if sentiment_idx == 1 else "Negative"
    
    return {"sentiment": sentiment_label, "confidence": round(confidence, 2)}

# Test the model
result1 = predict_sentiment("This movie was absolutely fantastic!")
result2 = predict_sentiment("I really disliked this movie, it was terrible.")

print(f"Sentiment: {result1['sentiment']}, Confidence: {result1['confidence']}%")
print(f"Sentiment: {result2['sentiment']}, Confidence: {result2['confidence']}%")



from transformers import pipeline

pipe = pipeline("text-classification", model="philipobiorah/bert-imdb-model")

text_to_classify = "This movie was fantastic! I loved every minute of it."
result = pipe(text_to_classify)
print(result)

text_to_classify_2 = "The acting was terrible and the plot made no sense."
result_2 = pipe(text_to_classify_2)
print(result_2)

