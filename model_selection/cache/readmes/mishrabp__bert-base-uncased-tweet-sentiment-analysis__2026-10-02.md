
---
library_name: transformers
tags: [sentiment-analysis, BERT, social-media, emotion-detection]
---

# BERT Tweet Sentiment Analysis

## Model Details

### Model Description
This model is a BERT-based transformer (`bert-base-uncased`) fine-tuned for sentiment analysis on tweets. It classifies text into six emotion categories: sadness, joy, love, anger, fear, and surprise. The model was trained with a custom classification head on tweet data to capture short-form, social media style text.

- **Developed by:** Bibhu Mishra
- **Model type:** Sequence Classification
- **Language(s) (NLP):** English
- **License:** MIT
- **Finetuned from model:** bert-base-uncased

### Model Sources
- **Repository:** [Hugging Face Model Hub](https://huggingface.co/mishrabp/bert-base-uncased-tweet-sentiment-analysis)

## Uses

### Direct Use
This model can be used to classify tweets or short text into emotions, useful for social listening, customer sentiment analysis, and marketing insights.

### Downstream Use
The model can be integrated into larger NLP pipelines, such as real-time social media monitoring dashboards, chatbots, or recommendation systems that require sentiment-aware behavior.

### Out-of-Scope Use
- Not suitable for clinical, medical, or diagnostic use.
- Performance may decrease on very long text, sarcasm, or highly domain-specific language.

## Bias, Risks, and Limitations
- Limited to English-language social media text.
- May misclassify sarcastic or context-heavy tweets.
- Emotions are simplified into six categories, which may not capture nuanced sentiment.

### Recommendations
Use this model for **exploratory sentiment analytics** and not for critical decisions. Always review predictions in the context of business requirements.

## How to Get Started with the Model

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

model_name = "mishrabp/bert-base-uncased-tweet-sentiment-analysis"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

classifier = pipeline("text-classification", model=model, tokenizer=tokenizer)

tweets = [
    "I love spending time with my friends!",
    "I feel so sad about the news today."
]

results = classifier(tweets)
print(results)
```

#### Output
```json
[
    {"label": "love", "score": 0.95},
    {"label": "sadness", "score": 0.88}
]

```

### Labels
```
| ID | Emotion  |
| -- | -------- |
| 0  | sadness  |
| 1  | joy      |
| 2  | love     |
| 3  | anger    |
| 4  | fear     |
| 5  | surprise |
```

### Inference URL
https://mishrabp-twitter-sentiment-analysis.hf.space/

