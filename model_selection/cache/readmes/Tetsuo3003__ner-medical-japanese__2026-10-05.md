---
language: ja
license: mit
datasets:
- custom
metrics:
- f1
- precision
- recall
model_name: ner-medical-japanese
base_model: tsmatz/xlm-roberta-ner-japanese
tags:
- ner
- japanese
- medical
- token-classification
---


# 🇯🇵 日本語 医療会話 NER モデル

このモデルは、日本語の医療会話文書に特化した固有表現抽出（NER）モデルです。  
`tsmatz/xlm-roberta-ner-japanese` をベースにファインチューニングを行い、医療分野での情報抽出や匿名化に役立つよう最適化しています。

---

## 📚 用途

- 医療会話文書からの固有表現抽出（名前、施設名、地名など）
- 匿名化処理
- 医療関連データの情報整理
- リスク分析、研究データ整理

---

## 🎯 対象ドメイン

- 患者との会話記録  
- 診療メモ、訪問看護記録  
- 医療施設における報告書やドキュメント  

---

## 🏷️ ラベル一覧

| ラベル  | 説明        |
|---------|-------------|
| PER     | 人名         |
| ORG     | 組織名       |
| ORG-P   | 組織の部門   |
| ORG-O   | 組織その他   |
| LOC     | 地名         |
| INS     | 施設名（病院・学校など）|
| PRD     | 製品名       |
| EVT     | イベント名   |
| O       | その他（非エンティティ） |

---

## 🚀 使用方法

```python
from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline

model = AutoModelForTokenClassification.from_pretrained("Tetsuo3003/ner-medical-japanese")
tokenizer = AutoTokenizer.from_pretrained("Tetsuo3003/ner-medical-japanese")
ner_pipeline = pipeline("ner", model=model, tokenizer=tokenizer, aggregation_strategy="simple")

text = "金丸先生が松本市にある石川クリニックに通院しました。"
results = ner_pipeline(text)
for entity in results:
    print(f"{entity['word']} → {entity['entity_group']} (score: {entity['score']:.2f})")
