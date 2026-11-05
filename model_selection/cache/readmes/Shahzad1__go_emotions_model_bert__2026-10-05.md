---
library_name: transformers
tags:
- go-emotions
- text-classification
- emotion-detection
- distilbert
- pytorch
- nlp
---

# Model Card for GoEmotions Model BERT

This model is a fine-tuned **DistilBERT** model for emotion detection using the **simplified GoEmotions** dataset provided by Google.

It is capable of classifying English text into multiple emotions from the GoEmotions label set.

---

## Model Details

### Model Description

This is a fine-tuned `distilbert-base-uncased` model on the simplified version of the GoEmotions dataset for multi-label emotion classification.

- **Developed by:** Shahzad Sohail
- **Funded by [optional]:** Self-funded
- **Shared by [optional]:** Shahzad Sohail
- **Model type:** DistilBERT (fine-tuned for multi-label classification)
- **Language(s) (NLP):** English
- **License:** Apache 2.0
- **Finetuned from model [optional]:** distilbert-base-uncased

### Model Sources

- **Repository:** [Optional: Add link if you have a GitHub repository]
- **Dataset:** https://huggingface.co/datasets/google-research-datasets/go_emotions
- **Demo [optional]:** [Add Gradio/Hugging Face Space if applicable]

---

## Uses

### Direct Use

This model can be directly used for:
- Emotion classification in social media comments
- Sentiment analysis with fine-grained emotions
- Enhancing chatbot emotional understanding
- Social listening and brand monitoring

### Downstream Use [optional]

The model can be further fine-tuned for specialized domains such as healthcare, education, or customer support.

### Out-of-Scope Use

- Not suitable for clinical or psychological diagnosis.
- Not designed for non-English text.
- Should not be used in critical decision-making without human oversight.

---

## Bias, Risks, and Limitations

The model inherits biases from the GoEmotions dataset:
- May underperform on non-standard English, slang, or low-resource dialects.
- May misclassify ambiguous or sarcastic text.
- Model's emotion predictions should be verified in sensitive contexts.

### Recommendations

- Use the model with awareness of its biases and limitations.
- Apply additional human review in high-stakes or sensitive applications.

---

## How to Get Started with the Model

You can load and use the model with the Hugging Face `transformers` pipeline:
```python
from transformers import pipeline

classifier = pipeline("text-classification", model="Shahzad1/go_emotions_model_bert", top_k=None)

text = "I am feeling very happy today!"
results = classifier(text)
print(results)
