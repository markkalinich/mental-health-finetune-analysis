---
language: zh
tags:
- sentiment-analysis
- chinese
- bert
- text-classification
license: apache-2.0
datasets:
- custom
metrics:
- accuracy
library_name: transformers
pipeline_tag: text-classification
---

# 中文情感分析模型 (Chinese Sentiment Analysis)

這是一個基於 BERT 的中文情感分析模型，可以對中文文本進行正面/負面情感分類。

## 模型描述

- **模型類型**: BertForSequenceClassification
- **基礎模型**: bert-base-chinese  
- **語言**: 中文 (Chinese)
- **任務**: 文本分類 (情感分析)
- **標籤**: 
  - `POSITIVE`: 正面情感
  - `NEGATIVE`: 負面情感

## 使用方法

### 快速開始

```python
from transformers import pipeline

# 載入模型
classifier = pipeline("text-classification", model="sk413025/my-awesome-model")

# 進行推理
result = classifier("這個產品真的很棒！")
print(result)
# 輸出: [{'label': 'POSITIVE', 'score': 0.xxx}]
```

### 批量處理

```python
texts = [
    "這個產品真的很棒！",
    "質量太差了，不推薦。",
    "還不錯，可以考慮購買。"
]

results = classifier(texts)
for text, result in zip(texts, results):
    print(f"文本: {text}")
    print(f"預測: {result['label']} (信心度: {result['score']:.4f})")
    print("-" * 50)
```

### 直接使用模型

```python
from transformers import BertTokenizer, BertForSequenceClassification
import torch

# 載入模型和 tokenizer
tokenizer = BertTokenizer.from_pretrained("sk413025/my-awesome-model")
model = BertForSequenceClassification.from_pretrained("sk413025/my-awesome-model")

# 準備輸入
text = "這個服務體驗很棒！"
inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)

# 推理
with torch.no_grad():
    outputs = model(**inputs)
    predictions = torch.nn.functional.softmax(outputs.logits, dim=-1)
    
# 獲取結果
predicted_class = predictions.argmax().item()
confidence = predictions.max().item()

labels = {0: "NEGATIVE", 1: "POSITIVE"}
print(f"預測: {labels[predicted_class]} (信心度: {confidence:.4f})")
```

## API 使用

你也可以使用 Hugging Face 的 Inference API：

```python
import requests

API_URL = "https://api-inference.huggingface.co/models/sk413025/my-awesome-model"
headers = {"Authorization": f"Bearer YOUR_HF_TOKEN"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

result = query({"inputs": "這個產品質量很好！"})
print(result)
```

## 限制與注意事項

1. **領域限制**: 模型可能在特定領域（如醫療、法律）表現不佳
2. **語言變體**: 主要針對簡體中文，繁體中文可能需要額外處理
3. **文本長度**: 建議輸入文本長度不超過 512 個字符
4. **微調建議**: 建議根據你的具體用例進行微調

## 授權

本模型基於 Apache 2.0 授權發布。
