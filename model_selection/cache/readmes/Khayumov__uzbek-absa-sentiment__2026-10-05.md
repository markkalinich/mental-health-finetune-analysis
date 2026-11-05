---
library_name: transformers
tags:
- sentiment-analysis
- aspect-based-sentiment-analysis
- text-classification
- uzbek
- nlp
---

# Uzbek Aspect-Based Sentiment Analysis (ABSA)

## Model Details

This is an advanced Natural Language Processing (NLP) model designed to extract granular, aspect-based sentiments from Uzbek text. Unlike traditional sentiment analysis, it is trained to understand complex sentences where multiple, sometimes contradictory, sentiments are expressed.

- **Developed by:** Komron Khayumov
- **Model type:** Fine-tuned Transformer for Sequence Classification
- **Language:** Uzbek (uz)
- **Finetuned from model:** `bert-base-multilingual-cased`

## Uses

### Direct Use
This model is highly valuable for businesses, e-commerce platforms, and customer service departments operating in the Uzbekistan market. It can be directly used to:
- Automate the categorization of customer feedback.
- Monitor brand reputation on social media.
- Analyze product reviews to identify specific strengths and weaknesses (Aspect-Based Analysis).

### Out-of-Scope Use
The model is not intended for generating text, translating languages, or making automated decisions that could legally or financially harm individuals based solely on sentiment scores.

## Bias, Risks, and Limitations

While the model achieves high accuracy on standard reviews, users should be aware of the following NLP limitations:
- **Sarcasm and Irony:** The model may struggle to accurately classify heavily sarcastic or ironic statements.
- **Street Slang:** Highly informal internet slang, abbreviations, or texts heavily mixed with Russian/English words might lower confidence scores.

## How to Get Started with the Model

You can easily integrate this model into your Python pipeline using the Hugging Face `transformers` library.

```python
from transformers import pipeline

# Load the fine-tuned model
classifier = pipeline("sentiment-analysis", model="Khayumov/uzbek-absa-sentiment")

# Test with a complex sentence
text = "Xizmat yaxshi, lekin avtoturargoh yo'q ekan."
result = classifier(text)

print(result)
# Output Guide:
# LABEL_0 = Negative (Salbiy)
# LABEL_1 = Positive (Ijobiy)
# LABEL_2 = Neutral (Neytral)