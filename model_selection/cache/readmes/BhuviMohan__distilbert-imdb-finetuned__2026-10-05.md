---
language: en
library_name: transformers
pipeline_tag: text-classification
tags:
- sentiment-analysis
- imdb
- distilbert
- fine-tuned
---

# DistilBERT Fine-Tuned on IMDB Sentiment Dataset

This model is a fine-tuned version of **distilbert-base-uncased** on the IMDB movie
reviews dataset for binary sentiment classification (positive/negative).

## Model Details
- **Base model:** distilbert-base-uncased  
- **Dataset:** IMDB (25k train + 25k test reviews)  
- **Labels:**  
  - 0 → negative  
  - 1 → positive  

## How to Use

```python
from transformers import pipeline

clf = pipeline("text-classification", model="BhuviMohan/distilbert-imdb-finetuned")
print(clf("The movie was absolutely fantastic!"))

## Training Procedure

- Epochs: 1

- Batch size: 8

- Learning rate: 2e-5

- Optimizer: AdamW

- Hardware: CPU training (Windows)

- Results (Evaluation)

**Accuracy: ~1.0 (on 2k subset)**


Save the file.

---

# ✅ **STEP 5 — Upload model to Hugging Face Hub**

Make sure your token is created with **Write access**.

Then login (if not logged in):

```bash
huggingface-cli login
