---
library_name: transformers
tags: ['sentiment-analysis', 'distilbert', 'imdb']
---

# Model Card for DistilBERT IMDb Sentiment Analysis

## Model Details

### Model Description

This DistilBERT model has been fine-tuned for sentiment analysis on the IMDb dataset. It is designed to be lightweight and efficient, making it suitable for deployment on low-end PCs and machines. The model can accurately classify movie reviews as positive or negative.

- **Developed by:** Saif jabri
- **Model type:** DistilBERT for Sequence Classification
- **Language(s) (NLP):** English
- **License:** Apache-2.0
- **Finetuned from model:** [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased)

### Model Sources

- **Repository:** [Link to your repository on Hugging Face](https://huggingface.co/saiffff/distilbert-imdb-sentiment)
- **Demo:** [Link to demo if available]

## Uses

### Direct Use

This model can be used directly for sentiment analysis on English text data, particularly movie reviews.

### Downstream Use

The model can be fine-tuned further for other sentiment analysis tasks or integrated into larger applications requiring sentiment classification.

### Out-of-Scope Use

This model is not suitable for non-English text or tasks unrelated to sentiment analysis.

## Bias, Risks, and Limitations

While the model performs well on the IMDb dataset, it may have biases related to the data it was trained on. It might not generalize well to other domains or nuanced sentiment contexts.

### Recommendations

Users should be aware of the model's limitations and biases. Testing the model on a variety of inputs is recommended to understand its behavior and performance across different scenarios.

## How to Get Started with the Model

Use the code below to get started with the model:

```python
from transformers import pipeline

classifier = pipeline("sentiment-analysis", model="saiffff/distilbert-imdb-sentiment")
result = classifier("This movie was fantastic! I loved every moment of it.")
print(result)
