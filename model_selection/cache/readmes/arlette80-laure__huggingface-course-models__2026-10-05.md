---
license: mit
language:
- en
library_name: transformers
pipeline_tag: text-classification
tags:
- beginner
- tutorial
- huggingface-course
- sentiment-analysis
---

# Hugging Face Course Models

Welcome to my first Hugging Face model repository.

This repository was created as part of my learning journey with the Hugging Face Transformers library.

## Purpose

The purpose of this repository is to learn how to:

- Create a Hugging Face model repository
- Understand Model Cards
- Save pretrained models
- Upload models to the Hugging Face Hub
- Share models with other users

## Model Information

This repository will contain models developed during my Hugging Face course.

Current focus:

- Text Classification
- Sentiment Analysis
- Tokenization
- Transformer Models

## Libraries

The models in this repository are built using:

- Transformers
- PyTorch
- Hugging Face Hub

## Example

```python
from transformers import pipeline

classifier = pipeline(
    "sentiment-analysis"
)

classifier("I love Hugging Face!")
```

Expected output

```text
POSITIVE
```

## Future Updates

This repository will gradually include:

- Fine-tuned models
- Model weights
- Tokenizers
- Training notebooks
- Example applications
- Documentation

## Author

Arlette Laure

Artificial Intelligence with Hugging Face Transformers Course

## License

MIT License