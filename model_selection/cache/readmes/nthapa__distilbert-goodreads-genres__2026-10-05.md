---
library_name: transformers
tags:
  - text-classification
  - nlp
  - bert
  - distilbert
  - sentiment-analysis
---

# Model Card for distilbert-goodreads-genres

## Model Details

### Model Description

This model is a fine-tuned DistilBERT model for multi-class text classification. It predicts the genre of a book based on the textual content of Goodreads reviews. The supported genres include:

- poetry  
- children  
- comics & graphic  
- fantasy & paranormal  
- history & biography  
- mystery, thriller & crime  
- romance  
- young adult  

The model was fine-tuned using the Hugging Face `transformers` library on a subset of the UCSD Goodreads Book Graph dataset.

- **Developed by:** Nishant Thapa  
- **Shared by:** Nishant Thapa  
- **Model type:** Transformer-based sequence classification (DistilBERT)  
- **Language(s):** English  
- **License:** Apache-2.0  
- **Finetuned from model:** distilbert-base-cased  

### Model Sources

- **Repository:** https://github.com/nthapa000/ass3_hf_goodreads  
- **Base Model:** https://huggingface.co/distilbert-base-cased  
- **Dataset:** https://mengtingwan.github.io/data/goodreads.html  

---

## Uses

### Direct Use

The model can be used to classify a single Goodreads review or short text into one of the supported book genres.

Example:

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model_name = "nthapa/distilbert-goodreads-genres"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

text = "A beautiful coming-of-age story with magic and dragons."
inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
with torch.no_grad():
    outputs = model(**inputs)
pred = outputs.logits.argmax(dim=-1).item()
print(pred)