---
language: en
license: apache-2.0
tags:
  - text-classification
  - emotion
  - distilbert
  - sentiment
datasets:
  - emotion
metrics:
  - accuracy
  - f1
pipeline_tag: text-classification
base_model: distilbert-base-uncased
model-index:
  - name: my-emotion-model
    results:
      - task:
          type: text-classification
          name: Emotion Classification
        dataset:
          name: emotion
          type: emotion
          split: test
        metrics:
          - type: accuracy
            value: 0.921
          - type: f1
            value: 0.922
---

# DistilBERT fine-tuned on the Emotion dataset

本模型在 [`emotion`](https://huggingface.co/datasets/emotion) 数据集上对
`distilbert-base-uncased` 进行了微调，用于英文文本的六类情感分类：
**sadness, joy, love, anger, fear, surprise**。

## 评测结果

| 指标 | 测试集 | 验证集 |
| --- | --- | --- |
| accuracy | 0.921 | 0.944 |
| weighted-F1 | 0.922 | 0.944 |
| macro-F1 | 0.874 | 0.921 |

测试集（test split，未参与训练/调参）各类别 F1：sadness 0.961 / joy 0.944 / anger 0.923 / love 0.832 / fear 0.872 / surprise 0.709。其中最稀有的 surprise（仅 66 条）表现最弱。

## 训练设置

- base model: `distilbert-base-uncased`
- learning rate: `5e-5`（由学习率扫描确定，`1e-3` 会发散、`2e-5` 略低）
- epochs: 2，batch size: 64，weight decay: 0.01
- seed: 42（结果可复现）

## 用法

```python
from transformers import pipeline

clf = pipeline("text-classification",
               model="Mickey-yy/my-emotion-model")
clf("I love this so much!")
# [{'label': 'joy', 'score': 0.99...}]
```

## 局限性

模型主要依赖表层情感词汇，对**反讽、否定、混合情感及表情符号/网络口语等分布外输入**鲁棒性有限
（例如 “I do not feel happy” 可能仍被判为 joy）。在稀有类别（love/surprise）上的表现也相对较弱。
