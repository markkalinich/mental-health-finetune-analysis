---
language: ja
license: mit
tags:
  - japanese
  - text-classification
  - binary-classification
  - risk-analysis
  - bert
datasets:
  - custom
metrics:
  - accuracy
model-index:
  - name: Japanese Risk Classifier (リスク分類モデル)
    results:
      - task:
          type: text-classification
          name: Text Classification
        dataset:
          name: Custom CSV (train.csv)
          type: custom
        metrics:
          - name: Accuracy
            type: accuracy
            value: 0.XX  # 任意で精度を記載できます（例：0.91）
---

# Japanese Risk Classifier - リスクあり／なし 二値分類モデル

このモデルは、日本語の医療で使われる会話文を対象に「ハイリスクあり」「ハイリスクなし」を二値で分類するためにファインチューニングされたBERTベースモデルです。  
医療・介護・健康関連の文脈などにおける**状態・兆候・症状のリスク分類**を想定しています。

## 📌 ベースモデル

- モデル名：[`llm-book/bert-base-japanese-v3-marc_ja`](https://huggingface.co/llm-book/bert-base-japanese-v3-marc_ja)
- モデルタイプ：BERT（日本語事前学習済み）

## 🧪 学習設定

| 項目                     | 設定値                 |
|--------------------------|------------------------|
| 学習エポック数           | 6                      |
| バッチサイズ             | 8                      |
| 学習率                   | 2e-5                   |
| トークナイザー           | `AutoTokenizer`        |
| トークン長               | `padding="max_length"` |

使用データ：CSVファイル `train.csv` に含まれる以下の形式  
```csv
text,label
"夜1時頃トイレに行った時寒気と足の震えが強くて…",リスクあり
```

## 🧠 ラベル定義

- `リスクなし` → 0
- `リスクあり` → 1

## 🛠 使用方法

### 推論（Inference）

```python
from transformers import pipeline

classifier = pipeline("text-classification", model="ユーザー名/モデル名", tokenizer="ユーザー名/モデル名")
result = classifier("夜1時頃トイレに行った時寒気と足の震えが強くて…")
print(result)
```

出力例：
```json
[{'label': 'リスクあり', 'score': 0.982}]
```

### 推論速度
ローカル環境（Windows）での実測：

```
⏱ 推論時間: 約2.00秒
```

## 💾 保存済みファイル構成

```
./risk_classifier/
├── config.json
├── pytorch_model.bin
├── tokenizer_config.json
├── tokenizer.json（または vocab.txt 等）
├── special_tokens_map.json
└── README.md
```

## 📄 ライセンス

MIT License

## 📄 Framework versions
transformers	4.41.1（最新版でOK）	Hugging Face ライブラリの本体

fugashi	1.3.0〜1.5.1	日本語形態素解析（MeCab wrapper）

unidic-lite	1.0.8 以降	軽量辞書（fugashi用）

torch	2.0〜2.2（互換性重視）	PyTorch：モデルの実行基盤

---

## 📬 お問い合わせ

本モデルに関する質問・改善提案は Issue や Pull Request にてご連絡ください。
