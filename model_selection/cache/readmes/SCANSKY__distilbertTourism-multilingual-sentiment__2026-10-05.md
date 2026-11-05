---
language:
- en
- ko
- zh
- ja
- es
- fr
- ru
- hi
base_model:
- distilbert/distilbert-base-multilingual-cased
pipeline_tag: text-classification
tags:
- tourism
- sentiment
- multilingual
---



---

# distilbertTourism-multilingual-sentiment

A fine-tuned DistilBERT model for performing sentiment analysis on tourism-related texts in multiple languages. This model is a key component of the thesis project **"Enhancing Tourist Destination Management through a Multilingual Web-Based Tourist Survey System with Machine Learning."** It is designed to analyze reviews, feedback, and other textual data to improve tourist feedback collection in Panglao.

## Overview

This model builds on the [distilbert-base-multilingual-cased](https://huggingface.co/distilbert/distilbert-base-multilingual-cased) architecture and has been fine-tuned on tourism-specific sentiment data. With support for eight languages, it provides a practical solution for multilingual sentiment classification in the tourism sector.

> **Thesis Context:**  
> As part of the thesis project, this model integrates with a comprehensive system that leverages advanced natural language processing techniques. In addition to this DistilBERT-based sentiment analyzer, the system utilizes BERTopic for topic modeling. The project aims to surpass the 70% accuracy benchmark set by the IPCR while addressing language barriers and inefficiencies inherent in traditional survey methods.

## Model Details

- **Task:** Text Classification (Sentiment Analysis)
- **Base Model:** [distilbert-base-multilingual-cased](https://huggingface.co/distilbert/distilbert-base-multilingual-cased)
- **Architecture:** DistilBERT
- **Parameters:** 135M
- **Tensor Format:** F32 (Safetensors)
- **Supported Languages:** 8 (Multilingual)
- **Training Data:** 160k synthetic tourism reviews
- **Performance:** Achieves over 95% confidence in sentiment classification for tourism-related texts.
- **Fine-tuning:** Adapted to the tourism domain (242 fine-tuning iterations/steps indicated)

## Usage

To integrate this model into your application, you can use the Hugging Face Transformers library. Below is an example in Python:

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# Define the model repository
model_name = "SCANSKY/distilbertTourism-multilingual-sentiment"

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Example input text (replace with your own tourism-related text)
text = "I had an amazing experience during my trip!"
inputs = tokenizer(text, return_tensors="pt")

# Perform inference
outputs = model(**inputs)
logits = outputs.logits

# You can further process the logits to get predicted sentiment labels.
```

### Installation

Ensure you have the required packages installed:

```bash
pip install transformers safetensors
```

## Limitations

- **Domain Specific:** This model is fine-tuned specifically for tourism sentiment analysis and may not perform optimally on texts from other domains.
- **Inference API:** Currently, the model does not support direct deployment to the Hugging Face Inference API since it lacks a library tag.

## Future Work

- **Dataset Expansion:** Incorporating additional data from more tourism sources could further improve performance.
- **Model Optimization:** Experimentation with different fine-tuning strategies or hyperparameters might yield even better sentiment classification accuracy.
- **API Integration:** Future updates may include support for direct inference API deployment.

## Acknowledgements

- This model is based on the robust [DistilBERT](https://huggingface.co/distilbert/distilbert-base-multilingual-cased) architecture.
- Special thanks to the Hugging Face community for providing the infrastructure that makes deploying and sharing models seamless.
- This work is part of the thesis project **"Enhancing Tourist Destination Management through a Multilingual Web-Based Tourist Survey System with Machine Learning."** The project also utilizes BERTopic for topic modeling, aiming to revolutionize the collection and analysis of tourist feedback by overcoming language barriers and improving upon traditional survey methods.
## Citation

```bibtex
@inproceedings{your_citation,
  title={Distilbert Sentiment for Multilingual Tourism Feedback},
  author={Paul Andre D. Tadiar},
  year={2025}
}
```
---

