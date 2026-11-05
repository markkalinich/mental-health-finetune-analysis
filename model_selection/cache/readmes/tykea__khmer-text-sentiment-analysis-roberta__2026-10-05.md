---
license: mit
language:
- km
base_model:
- FacebookAI/xlm-roberta-base
pipeline_tag: text-classification
library_name: transformers
tags:
- sentiment
---

**This is a fine-tuned version of the XLM-RoBERTa model for sentiment analysis to classify khmer texts into 2 categories; Postive and Negative.** 

**It can process texts up to 512 tokens and performs well on khmer text inputs.**

- **Task**: Sentiment analysis (binary classification).
- **Languages Supported**: Khmer.
- **Intended Use Cases**: 
  - Analyzing customer reviews.
  - Social media sentiment detection.
- **Limitations**: 
  - Performance may degrade on languages or domains not present in the training data.
  - Does not handle sarcasm or highly ambiguous inputs well.
  - 
The model was evaluated on a test set of 400 samples, achieving the following performance:

- **Test Accuracy**: 83.25%
- **Precision**: 83.55%
- **Recall**: 83.25%
- **F1 Score**: 83.25%

Confusion Matrix:
| Predicted\Actual | Negative | Positive |
|-------------------|----------|----------|
| **Negative**      | 166      | 42       |
| **Positive**      | 25       | 167      |
The model supports a maximum sequence length of 512 tokens.
## How to Use
```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("tykea/khmer-text-sentiment-analysis-roberta")
model = AutoModelForSequenceClassification.from_pretrained("tykea/khmer-text-sentiment-analysis-roberta")

text = "អគុណCADT"
inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=512)
outputs = model(**inputs)
predictions = outputs.logits.argmax(dim=1)
labels_mapping = {0: 'negative', 1: 'positive'}
print("Predicted Class:", labels_mapping[predictions.item()])