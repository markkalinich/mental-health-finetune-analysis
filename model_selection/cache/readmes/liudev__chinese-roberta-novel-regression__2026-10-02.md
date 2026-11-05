---
license: apache-2.0
language:
- zh
pipeline_tag: text-classification
tags:
- novel
- emotion
- regression
---
# Chinese-RoBERTa-WWM-Ext Novel Regressor
基于 [hfl/chinese-roberta-wwm-ext](https://huggingface.co/hfl/chinese-roberta-wwm-ext) 微调的文本回归模型，用于小说内容的情绪量化。
## 模型详情
- **Base Model:** hfl/chinese-roberta-wwm-ext
- **任务:** 回归分析 (Regression)
- **输入长度:** 512 tokens
## 如何使用
```python
from transformers import AutoModelForSequenceClassification, AutoTokenizer
model_name = "liudev/chinese-roberta-novel-regression"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)
text = "小明很生气，后果很严重"
inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=512)
outputs = model(**inputs)
# 获取回归分数
score = outputs.logits.item()
print(f"预测得分: {score}")
# 预测得分: -0.7371920347213745
```