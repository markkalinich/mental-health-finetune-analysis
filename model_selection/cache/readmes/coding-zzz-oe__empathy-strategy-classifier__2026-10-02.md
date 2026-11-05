---
language: en
tags:
- text-classification
- emotional-support
- empathy
- mental-health
license: mit
datasets:
- esconv
library_name: transformers
---

# Emotional Support Strategy Classifier

This model is a fine-tuned RoBERTa-base model for classifying emotional support conversation strategies.

## Model Description

- **Base Model**: roberta-base
- **Task**: Multi-class text classification
- **Training Data**: ESConv (Emotional Support Conversation) dataset
- **Number of Labels**: 8

## Labels

The model classifies text into 8 emotional support strategies:

0. Affirmation and Reassurance
1. Information
2. Others
3. Providing Suggestions
4. Question
5. Reflection of feelings
6. Restatement or Paraphrasing
7. Self-disclosure

## Usage

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load model and tokenizer
model_name = "RyanDDD/empathy-strategy-classifier"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Example prediction
text = "I understand how you feel. It's completely normal to feel this way."
inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=512)
outputs = model(**inputs)
predictions = torch.nn.functional.softmax(outputs.logits, dim=-1)
predicted_class = torch.argmax(predictions, dim=-1).item()

print(f"Predicted strategy: {model.config.id2label[predicted_class]}")
```

## Training

Fine-tuned on the ESConv dataset using the Hugging Face Transformers library.

## Citation

If you use this model, please cite the ESConv dataset:

```bibtex
@inproceedings{liu2021towards,
  title={Towards Emotional Support Dialog Systems},
  author={Liu, Siyang and Zheng, Chujie and Demasi, Orianna and Sabour, Sahand and Li, Yu and Yu, Zhou and Jiang, Yong and Huang, Minlie},
  booktitle={Proceedings of ACL},
  year={2021}
}
```