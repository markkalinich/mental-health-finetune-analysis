---
language: en
license: mit
tags:
- sentiment-analysis
- distilbert
datasets:
- sst-2
---

# my-sentiment-model

此模型是基于DistilBERT架构的情感分析模型，在SST-2数据集上微调。

## 使用示例

```python
from transformers import pipeline

classifier = pipeline('sentiment-analysis', 
                      model='andy-value/my-sentiment-model')
result = classifier("Hugging Face is amazing!")
print(result)  # [{'label': 'POSITIVE', 'score': 0.9998}]
```