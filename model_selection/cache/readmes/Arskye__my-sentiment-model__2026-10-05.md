---
license: mit
library_name: transformers
pipeline_tag: text-classification
tags:
- sentiment-analysis
- text-classification
- distilbert
- fine-tuned
- nlp
language:
- en
datasets:
- sentiment140
metrics:
- accuracy
- f1
base_model: distilbert-base-uncased
model-index:
- name: my-sentiment-model
  results:
  - task:
      type: text-classification
      name: Text Classification
    dataset:
      name: sentiment140
      type: sentiment140
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.85
    - name: F1 Score (Macro)
      type: f1
      value: 0.84
---

# My DistilBERT Sentiment Model

Fine-tuned DistilBERT for 3-class sentiment classification (negative, neutral, positive).

## Model Description

This model is a fine-tuned version of DistilBERT-base-uncased for sentiment analysis. It has been trained to classify text into three sentiment categories:

- **Negative** (0)
- **Neutral** (1) 
- **Positive** (2)

## Intended Uses

This model is intended for sentiment analysis tasks on English text. It can be used to:
- Analyze customer feedback and reviews
- Monitor social media sentiment
- Classify emotions in text data
- Support content moderation systems

## Limitations

- Trained primarily on English text
- May not perform well on domain-specific jargon
- Performance may vary on very short or very long texts
- Potential bias from training data

## Training Details

- **Base Model**: distilbert-base-uncased
- **Training Epochs**: 2
- **Batch Size**: 8
- **Learning Rate**: 3e-5
- **Max Sequence Length**: 128
- **Optimizer**: AdamW
- **Weight Decay**: 0.01

## Model Performance

The model achieves the following performance on the test set:

- **Accuracy**: 85%
- **F1-Score (Macro)**: 84%
- **F1-Score (Weighted)**: 85%

## Usage

Install the required dependencies:

```bash
pip install transformers torch
```

Load and use the model:

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load model and tokenizer
model_name = "your-username/my-sentiment-model"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Prepare text
text = "I love this product!"
inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=128)

# Get prediction
with torch.no_grad():
    outputs = model(**inputs)
    probabilities = torch.nn.functional.softmax(outputs.logits, dim=-1)
    predicted_class = torch.argmax(probabilities, dim=-1).item()

# Map prediction to label
labels = {0: "negative", 1: "neutral", 2: "positive"}
confidence = probabilities[0][predicted_class].item()

print(f"Text: {text}")
print(f"Sentiment: {labels[predicted_class]} (confidence: {confidence:.2%})")
```

## Citation

If you use this model in your research, please cite:

```bibtex
@misc{my-sentiment-model,
  author = {Your Name},
  title = {Fine-tuned DistilBERT for Sentiment Analysis},
  year = {2025},
  publisher = {Hugging Face},
  url = {https://huggingface.co/your-username/my-sentiment-model}
}
```

## License

This model is released under the MIT License.