---
language: en
license: mit
tags:
- text-generation
- question-answering
- sentence-similarity
- text-classification
- need-ai
base_model: unitary/toxic-bert
pipeline_tag: text-classification
---

# NEED AI - Content Moderation

BERT model for detecting toxic and inappropriate content in user messages and reviews.

## Model Details

- **Base Model**: unitary/toxic-bert
- **Task**: Text Classification
- **Fine-tuned for**: NEED Service Marketplace Platform
- **Language**: English
- **License**: MIT

## Usage

```python
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
# or AutoModelForSequenceClassification for moderation
# or SentenceTransformer for semantic-search

model_name = "yogami9/need-content-moderation"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

# Example usage
input_text = "Your input here"
inputs = tokenizer(input_text, return_tensors="pt")
outputs = model.generate(**inputs)
result = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(result)
```

## Training Data

Trained on curated datasets specific to the NEED platform's service categories and user interactions.

## Limitations

- Optimized for English language
- Best performance on NEED platform-specific queries
- May require fine-tuning for other domains

## Contact

- **Organization**: NEED Service App
- **Email**: needserviceapp@gmail.com
- **GitHub**: https://github.com/Need-Service-App

## Related Models

All NEED AI models:
- [Category Recommendation](https://huggingface.co/yogami9/need-category-recommendation)
- [Chat Support](https://huggingface.co/yogami9/need-chat-support)
- [Service Description](https://huggingface.co/yogami9/need-service-description)
- [Semantic Search](https://huggingface.co/yogami9/need-semantic-search)
- [Content Moderation](https://huggingface.co/yogami9/need-content-moderation)
