---
library_name: transformers
datasets:
- shunk031/wrime
language:
- ja
base_model:
- tohoku-nlp/bert-base-japanese-v3
license: cc-by-nc-4.0
tags:
- sentiment-analysis
- wrime
---

# wrime-sentiment-analyzer

<!-- Provide a quick summary of what the model is/does. -->


## モデルについて

このモデルは、日本語の文章に対して −１ (ネガティブ) 〜 ＋１ (ポジティブ) の感情スコアを予測する回帰モデルです。

[tohoku-nlp/bert-base-japanese-v3](https://huggingface.co/cl-tohoku/bert-base-japanese-v3)をベースに、[WRIME v2](https://huggingface.co/datasets/shunk031/wrime) データセットの読者の平均感情スコア（avg_readers.sentiment） を用いてファインチューニングしています。


## 使用方法

```python
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model_id = "katsutaku/wrime-sentiment-analyzer"
tokenizer = AutoTokenizer.from_pretrained(model_id)
# trust_remote_code=True は必須．モデルが独自のクラス（TanhBertRegressor）を使用
model = AutoModelForSequenceClassification.from_pretrained(model_id, trust_remote_code=True)
model.to(device)
model.eval()

text = "とても助かりました、ありがとうございます！"

inputs = tokenizer(text, return_tensors="pt", 
                   truncation=True, 
                   max_length=512) 
inputs.to(device)

with torch.no_grad():
    outputs = model(**inputs)

score = outputs.logits.squeeze().item()
```