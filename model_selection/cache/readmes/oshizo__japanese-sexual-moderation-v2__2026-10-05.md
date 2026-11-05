---
license: mit
language:
- ja
---

japanese-sexual-moderation-v2は、[studio-ousia/luke-japanese-large-lite](https://huggingface.co/studio-ousia/luke-japanese-large-lite)をファインチューニングしたモデルです。  
短文が性的かどうかをスコアリングします。

regressionで学習しており、出力するスコアはおおむね0-1の範囲を取りますが負の値や1を超える値が出る場合があります。
長い文章は学習しておらず、入力は改行単位で分割することを想定しています。

0.0-0.2: 全く性的ではない  
0.2-0.4: ほとんど性的な内容を含まない  
0.4-0.6: 性的な内容を含む可能性がある  
0.6-0.8: 性的な内容を含んでいる  
0.8-1.0: 非常に性的な内容である

## Usage

```python
import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model_id = "oshizo/japanese-sexual-moderation-v2"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForSequenceClassification.from_pretrained(
    model_id,
    problem_type="regression"
)

texts = [
    "富士山は日本で一番高い山です。",
    "こんなになるまで我慢してたんだ...大変だったね",
    "俺は倒れる京子に近づき、担ぎ上げようと太ももの下に腕を通す。",
]

with torch.no_grad():
    encoding = tokenizer(texts, padding=True, max_length=64, return_tensors="pt")
    scores = model(**encoding).logits

# tensor([[-0.0045],
#         [ 0.2954],
#         [ 0.4391]])

```