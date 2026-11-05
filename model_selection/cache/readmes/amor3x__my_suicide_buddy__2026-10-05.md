---
language: en
license: mit
tags:
  - text-classification
  - distilbert
  - huggingface
pipeline_tag: text-classification
---

# My Suicide Buddy 💬

This is a fine-tuned `DistilBERT` model for binary text classification (e.g., suicide risk detection or sentiment analysis).

## Labels
- `0`: NEGATIVE
- `1`: POSITIVE

## Example usage

```python
from transformers import pipeline

classifier = pipeline("text-classification", model="your-username/my_suicide_buddy")
<!-- classifier("I feel hopeless and alone.") -->
