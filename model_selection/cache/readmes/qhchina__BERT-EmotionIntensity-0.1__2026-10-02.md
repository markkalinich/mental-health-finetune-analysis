---
library_name: transformers
language: zh
tags:
- emotion-detection
- sequence-classification
license: apache-2.0
widget:
- text: "我们昨天去了爬山，走了很多路。"
  example_title: "neutral"
- text: "这本书很一般，没有特别好的地方。"
  example_title: "weak"
- text: "我非常喜欢这个产品，强烈推荐！"
  example_title: "strong"
---

# BERT Emotion Detection Model

This model is fine-tuned for detecting strong and weak emotions in Chinese text using BERT.

## Model Description

The model is based on `bert-base-chinese` and fine-tuned for sequence classification with two labels: `weak` (0) and `strong` (1) emotion. The model was trained for one epoch using a dataset of ~125k comments from Douban, a Chinese social networking service, and achieved 87.9% accuracy on a held-out test set (10k comments). The comments were at least 200-character long; those with 1 or 5 stars were labeled "strong," those with 3 stars "weak."

## Usage

Here’s how you can use this model with the Transformers library:

```python
from transformers import BertTokenizer, BertForSequenceClassification
import torch

model_name = "qhchina/BERT-EmotionIntensity-0.1"
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertForSequenceClassification.from_pretrained(model_name)

sentence = "到达华侨居住的地区，疯狂地捣毁华侨的商店，洗劫华侨的财物，野蛮地殴打华侨，破坏华侨的车辆和看到的一切东西。他们对华侨大抢、大烧、大杀。种种暴行，简直同当年希特勒法西斯匪徒对待犹太人，和今天南非种族主义者对待非洲人，一模一样。"

inputs = tokenizer(sentence, return_tensors="pt")

outputs = model(**inputs)
logits = outputs.logits

# Get the probability of the "strong emotion" class
probability_strong_emotion = torch.nn.functional.softmax(logits, dim=-1)[0][1].item()

print(f"Sentence: {sentence}")
print(f"Probability of strong emotion: {probability_strong_emotion}")
