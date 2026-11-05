---
language:
- zh
- en
license: apache-2.0
tags:
- sentiment-analysis
- text-classification
- bert-tiny
- multilingual
- chinese
- english
widget:
- text: "这家餐厅的服务真是太棒了！"
  example_title: "正面中文"
- text: "The product quality is extremely poor."
  example_title: "负面英文"
- text: "Not bad, but I've had better."
  example_title: "隐晦负面"
---

# ZJB's BERT-Tiny Multilingual Sentiment Model (v2.0)

## 模型概述 / Model Overview
这是一个基于 **BERT-Tiny** 架构微调的双语（中文/英文）情感分析模型。该模型使用约5000条高质量的中英双语数据进行训练，能够以极高的准确率和置信度判断文本的情感倾向（正面/负面）。

This is a bilingual (Chinese/English) sentiment analysis model fine-tuned on the **BERT-Tiny** architecture. Trained on approximately 5000 high-quality bilingual data pairs, it can judge the emotional tendency (positive/negative) of text with high accuracy and confidence.

## 模型详情 / Model Details
- **模型类型 (Model Type):** BERT-Tiny (约4M参数 / ~4M Parameters)
- **微调者 (Fine-tuned by):** ZJB
- **基础模型 (Base Model):** `prajjwal1/bert-tiny`
- **训练数据 (Training Data):** ~5000 条自定义中英双语句子 / ~5000 custom bilingual sentences.
- **最大序列长度 (Max Sequence Length):** 64 tokens
- **输入格式 (Input Format):** 原始文本 / Raw text。
- **输出格式 (Output Format):** 标签 (`LABEL_1` 为正面, `LABEL_0` 为负面) 及置信度 / Label (`LABEL_1` for positive, `LABEL_0` for negative) with confidence score.

## 如何使用 / How to Use
您可以直接使用 `transformers` 库的 `pipeline` API：
You can use the `pipeline` API from the `transformers` library directly:

```python
from transformers import pipeline

classifier = pipeline("text-classification", model="zjb522/bert-tiny-zjb-sentiment-v2")
result = classifier("The atmosphere and service of this restaurant are top-notch!")
print(result)
# [{'label': 'LABEL_1', 'score': 0.9958407282829285}]