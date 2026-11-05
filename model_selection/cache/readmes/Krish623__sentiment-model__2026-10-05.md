---
library_name: transformers
pipeline_tag: text-classification
tags:
- sentiment-analysis
- bert
- goemotions
- nlp
---


# Model Card for Sentiment Analysis (Positive / Negative / Neutral)

## Model Details

### Model Description

This model is a fine-tuned BERT-based transformer model for **sentiment analysis**.  
It is trained using the GoEmotions dataset, where the original 27 emotion labels are **mapped into three categories**:

- Positive 😊  
- Negative 😡  
- Neutral 😐  

The model takes text input and predicts its overall sentiment.

- **Developed by:** Krish Agrawal 
- **Model type:** BERT (Transformer-based classification model)  
- **Language(s):** English  
- **License:** Apache 2.0  
- **Finetuned from model:** bert-base-uncased  

---

### Model Sources

- **Repository:** https://github.com/krishagrawal623/bert-goemotions-sentiment-model.git 
- **Dataset:** GoEmotions (Google Research)   

---

## Uses

### Direct Use

This model can be used for:
- Sentiment analysis (positive / negative / neutral)  
- Social media monitoring  
- Customer feedback analysis  
- Review classification  

Example:
- Input: "This product is amazing!"  
- Output: Positive  

---

### Downstream Use

- Chatbots 🤖  
- Business analytics dashboards  
- Customer support systems  
- Market research tools  

---

### Out-of-Scope Use

- Not suitable for:
  - Non-English text  
  - Detecting detailed emotions (like anger, joy, fear separately)  
  - Sarcasm or complex context  

---

## Bias, Risks, and Limitations

- Mapping 27 emotions → 3 classes may **lose detailed emotional information**  
- May misclassify:
  - Sarcasm  
  - Mixed sentiments  
- Dataset bias may affect predictions  

---

### Recommendations

- Use only for general sentiment analysis  
- Avoid using for sensitive or critical decisions  
- Fine-tune further for domain-specific tasks  

---

## How to Get Started with the Model

```python
from transformers import pipeline

classifier = pipeline("text-classification", model="your-username/your-model-name")

result = classifier("I am very happy today!")
print(result)
