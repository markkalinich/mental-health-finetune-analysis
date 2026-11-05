---
language: en
tags:
- emotion-classification
- bert
- lora
license: mit
---

# Emotion Classification Model

This model is a fine-tuned version of `bert-base-uncased` on the "dair-ai/emotion" dataset, using LoRA (Low-Rank Adaptation) for efficient fine-tuning.

label_list={"sadness", "joy", "love", "anger" ,"fear","surprise"}

## Model description

[Describe your model, its architecture, and the task it performs]

## Intended uses & limitations

[Describe what the model is intended for and any limitations]

## Training and evaluation data

The model was trained on the "dair-ai/emotion" dataset.

## Training procedure

[Describe your training procedure, hyperparameters, etc.]

## Eval results

[Include your evaluation results]

## How to use

Here's how you can use the model:

```python
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("ahmetyaylalioglu/text-emotion-classifier")
tokenizer = AutoTokenizer.from_pretrained("ahmetyaylalioglu/text-emotion-classifier")

text = "I am feeling very happy today!"
inputs = tokenizer(text, return_tensors="pt")
outputs = model(**inputs)
predictions = outputs.logits.argmax(-1)
print(model.config.id2label[predictions.item()])