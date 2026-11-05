---
library_name: transformers
tags:
- classification
- sentiment
license: mit
language:
- en
metrics:
- accuracy
base_model:
- google-bert/bert-base-uncased
pipeline_tag: text-classification
---

# Model Card for MESSItom/BERT-review-sentiment-analysis

This model is fine-tuned from BERT to perform sentiment analysis on a custom dataset containing student reviews about campus events or amenities. The objective is to classify the sentiments (positive, negative, neutral) while maintaining high performance metrics like accuracy.

## Model Details

### Model Description

This is the model card of a 🤗 transformers model that has been pushed on the Hub. This model card has been automatically generated.

- **Developed by:** Messy Tom Binoy
- **Funded by:** No funding, self-funded
- **Shared by:** Messy Tom Binoy
- **Model type:** BERT
- **Language(s) (NLP):** English
- **License:** MIT
- **Finetuned from model:** google-bert/bert-base-uncased

### Model Sources

- **Repository:** [GitHub Repository](https://github.com/messi10tom/Fine-Tuning-BERT-for-Sentiment-Analysis/tree/main)
- **Demo:** [GitHub Demo](https://github.com/messi10tom/Fine-Tuning-BERT-for-Sentiment-Analysis/tree/main)

## Uses

### Direct Use

The model can be used directly for sentiment classification of student reviews about campus events or amenities.

### Downstream Use

The model can be fine-tuned further for other sentiment analysis tasks or integrated into larger applications for sentiment classification.

### Out-of-Scope Use

The model is not suitable for tasks outside sentiment analysis, such as language translation or text generation.

## Bias, Risks, and Limitations

The model may inherit biases from the pre-trained BERT model and the custom dataset used for fine-tuning. It may not perform well on reviews that are significantly different from the training data.

### Recommendations

Users should be aware of the potential biases and limitations of the model. It is recommended to evaluate the model on a diverse set of reviews to understand its performance and limitations.

## How to Get Started with the Model

Use the code below to get started with the model:

```python
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model_id = "MESSItom/BERT-review-sentiment-analysis"

model = AutoModelForSequenceClassification.from_pretrained(model_id)
tokenizer = AutoTokenizer.from_pretrained(model_id)

def predict_sentiment(text):
    inputs = tokenizer(text, return_tensors='pt', padding=True, truncation=True, max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
    logits = outputs.logits
    predicted_class = torch.argmax(logits, dim=-1).item()
    class_names = ['positive', 'neutral', 'negative']
    sentiment = class_names[predicted_class]
    return sentiment