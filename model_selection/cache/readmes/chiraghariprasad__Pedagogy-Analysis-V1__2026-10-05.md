---
license: mit
language:
- en
library_name: transformers
pipeline_tag: text-classification
tags:
- sentiment-analysis
- aspect-based-sentiment-analysis
- education
- student-feedback
- teacher-evaluation
- pedagogy
---
# Pedagogy-Analysis-V1

A fine-tuned BERT model for pedagogical analysis of educational text.

## Model Details

- Architecture: BERT
- Framework: Hugging Face Transformers
- License: MIT
- Task: Text Classification

## Usage

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification

model_id = "chiraghariprasad/Pedagogy-Analysis-V1"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForSequenceClassification.from_pretrained(model_id)

text = "The instructor explained the concept clearly."

inputs = tokenizer(text, return_tensors="pt", truncation=True)
outputs = model(**inputs)

print(outputs.logits)