---
language: zh
license: apache-2.0
library_name: transformers
pipeline_tag: text-classification
tags:
  - bert
  - chinese
  - sentiment-analysis
  - weibo
  - text-classification
datasets:
  - weibo_senti_100k
base_model: hfl/chinese-bert-wwm-ext
widget:
  - text: "今天天气真好，心情也很棒！"
    example_title: "正面样例"
  - text: "这个产品质量太差了，非常失望。"
    example_title: "负面样例"
  - text: "今天上午开会讨论了新项目的进度安排。"
    example_title: "中性样例"
---

# Weibo Sentiment ChineseBERT (三分类)

基于 [`hfl/chinese-bert-wwm-ext`](https://huggingface.co/hfl/chinese-bert-wwm-ext)
在微博情感数据集上微调的**三分类**情感分析模型 (negative / positive / neutral).

本模型为本科毕业设计《基于 Spark 的微博舆情分析系统》的配套模型.
完整项目代码: [MOST951/Graduation-Design](https://github.com/MOST951/Graduation-Design)

## 标签映射

| id | label    | 中文  |
|----|----------|------|
| 0  | negative | 负面  |
| 1  | positive | 正面  |
| 2  | neutral  | 中性  |

## 使用方式

### 方式 1: pipeline (最简单)

```python
from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="MOST951/weibo-sentiment-chinese-bert",
)
result = classifier("今天天气真好，心情也很棒！")
print(result)
# [{'label': 'positive', 'score': 0.98...}]
```

### 方式 2: AutoModel (可批量 + 可控)

```python
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("MOST951/weibo-sentiment-chinese-bert")
model = AutoModelForSequenceClassification.from_pretrained("MOST951/weibo-sentiment-chinese-bert")
model.eval()

texts = [
    "今天天气真好，心情也很棒！",
    "这个产品质量太差了，非常失望。",
    "今天上午开会讨论了新项目的进度安排。",
]

with torch.no_grad():
    enc = tokenizer(texts, padding=True, truncation=True, max_length=128, return_tensors="pt")
    logits = model(**enc).logits
    probs = torch.softmax(logits, dim=-1)
    preds = probs.argmax(dim=-1).tolist()

id2label = model.config.id2label
for text, pred, prob in zip(texts, preds, probs):
    print(f"{id2label[pred]:<10} ({prob[pred]:.4f})  {text}")
```

## 训练数据

- 数据集: [weibo_senti_100k](https://github.com/SophonPlus/ChineseNlpCorpus/tree/master/datasets/weibo_senti_100k)
- 规模: 10 万条微博, 按 8:1:1 划分训练/验证/测试
- 原始为二分类 (正 / 负), 通过规则补全中性样本构造三分类

## 评估结果 (测试集 10,000 条)

### 标准模式 (纯 BERT)

| 指标 | negative | positive | neutral | Macro |
|------|----------|----------|---------|-------|
| Precision | 0.8945 | 0.9233 | 0.8213 | 0.8797 |
| Recall    | 0.9103 | 0.8632 | 0.8602 | 0.8779 |
| F1        | 0.9023 | 0.8922 | 0.8403 | 0.8783 |

**总体准确率: 87.79%**

### 推理速度 (RTX 3050 Ti, batch_size=32)

| batch_size | 平均耗时 | 加速比 |
|-----------|---------|--------|
| 1         | 23.54 ms/条 | 1.00× |
| 32        | 7.38 ms/条  | **3.19×** |
| 64        | 7.75 ms/条  | 3.04× |

### 级联模式 (词典 + BERT 两阶段批量化)

- 平均耗时: **6.54 ms/条** (17% 样本被词典直出, 无需 BERT)
- Accuracy: 85.85%, Macro F1: 0.8594

## 训练超参

| 参数 | 值 |
|------|---|
| 基础模型 | hfl/chinese-bert-wwm-ext |
| max_length | 128 |
| batch_size | 32 |
| learning_rate | 2e-5 |
| epochs | 3 |
| optimizer | AdamW |
| warmup_ratio | 0.1 |
| 硬件 | NVIDIA RTX 3050 Ti (CUDA 11.8) |

## 许可证

Apache 2.0

## 引用

如果你在研究中使用了本模型, 请引用:

```bibtex
@misc{weibo-sentiment-chinese-bert-2026,
  title={基于 Spark 的微博舆情分析系统},
  author={senlou},
  year={2026},
  howpublished={\url{https://github.com/MOST951/Graduation-Design}}
}
```
