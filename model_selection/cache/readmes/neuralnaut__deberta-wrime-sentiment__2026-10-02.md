---
language: ja
license: mit
tags:
  - text-classification
  - sentiment-analysis
  - japanese
  - wrime
  - deberta-v3
datasets:
  - shunk031/wrime
metrics:
  - rmse
  - mae
  - pearson
base_model: ku-nlp/deberta-v3-base-japanese
model-index:
  - name: deberta-wrime-sentiment
    results:
      - task:
          type: text-classification
          name: Sentiment Analysis (Regression)
        dataset:
          name: WRIME v2
          type: shunk031/wrime
          config: ver2
          split: test
        metrics:
          - type: rmse
            value: 0.9224
            name: RMSE (original scale -2 to +2)
          - type: mae
            value: 0.7254
            name: MAE (original scale -2 to +2)
          - type: pearson
            value: 0.6787
            name: Pearson Correlation
          - type: accuracy
            value: 0.6876
            name: Sign Accuracy (3-class)
---

# DeBERTa v3 for Japanese Sentiment Analysis (WRIME - Sentiment Polarity)

日本語の感情極性分析のための DeBERTa v3 モデル

このモデルは[ku-nlp/deberta-v3-base-japanese](https://huggingface.co/ku-nlp/deberta-v3-base-japanese)を[WRIME v2 データセット](https://huggingface.co/datasets/shunk031/wrime)の主観データ（writer）でファインチューニングしたものです。

## 🔄 重要：正規化について

**このモデルは正規化された値を出力します**

- **モデル出力**: -1.0 ~ +1.0 の連続値（正規化済み）
- **元のスケール**: -2 ~ +2 の連続値
- **デノーマライズ方法**: `prediction_original = prediction_normalized * 2.0`

```python
# 推論後、必ずデノーマライズしてください
prediction = outputs.logits.cpu().numpy()[0][0]  # -1.0~+1.0
prediction_original = prediction * 2.0            # -2~+2に変換
prediction_original = np.clip(prediction_original, -2.0, 2.0)
```

## Model Description

感情極性を**-2（強いネガティブ）から +2（強いポジティブ）の連続値**で予測する回帰モデルです。

- **ベースモデル**: [ku-nlp/deberta-v3-base-japanese](https://huggingface.co/ku-nlp/deberta-v3-base-japanese)
- **言語**: 日本語 (Japanese)
- **ライセンス**: MIT
- **タスク**: 感情極性分析（回帰）
- **データ**: WRIME v2（主観データのみ）

### Label Configuration

```json
{
  "id2label": {
    "0": "sentiment_polarity"
  },
  "problem_type": "regression"
}
```

### スコア範囲の解釈

| スコア範囲  | ラベル         | 例                                       |
| ----------- | -------------- | ---------------------------------------- |
| -2.0 ~ -1.5 | 強いネガティブ | "最悪の気分だ..."                        |
| -1.5 ~ -0.5 | ネガティブ     | "悲しいニュースを聞いて落ち込んでいます" |
| -0.5 ~ +0.5 | 中立           | "普通の一日だった"                       |
| +0.5 ~ +1.5 | ポジティブ     | "今日は良い天気だね"                     |
| +1.5 ~ +2.0 | 強いポジティブ | "最高に幸せ！！！"                       |

## How to Use

### インストール

```bash
pip install transformers torch
```

### 基本的な使い方

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import numpy as np

# モデルとトークナイザのロード
model_name = "neuralnaut/deberta-wrime-sentiment"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# 推論
text = "今日はとても楽しい一日でした！"
inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=128)

model.eval()
with torch.no_grad():
    outputs = model(**inputs)
    prediction = outputs.logits.cpu().numpy()[0][0]

# ⚠️ 重要：デノーマライズ (-1~+1 → -2~+2)
prediction = prediction * 2.0
prediction = np.clip(prediction, -2.0, 2.0)

# ラベル付け
if prediction <= -1.5:
    label = "強いネガティブ"
elif prediction < -0.5:
    label = "ネガティブ"
elif prediction <= 0.5:
    label = "中立"
elif prediction < 1.5:
    label = "ポジティブ"
else:
    label = "強いポジティブ"

print(f"テキスト: {text}")
print(f"感情極性: {prediction:+.2f} ({label})")
```

### 出力例

```
テキスト: 今日はとても楽しい一日でした！
感情極性: +1.67 (強いポジティブ)
```

### 視覚化例

```python
def visualize_sentiment(text, score):
    """感情極性を視覚化"""
    if score <= -1.5:
        label = "強いネガティブ"
    elif score < -0.5:
        label = "ネガティブ"
    elif score <= 0.5:
        label = "中立"
    elif score < 1.5:
        label = "ポジティブ"
    else:
        label = "強いポジティブ"

    print(f"\nテキスト: {text}")
    print(f"感情極性: {score:+.2f} ({label})")

    # バーで視覚化
    bar_position = int((score + 2) * 10)
    bar_position = max(0, min(40, bar_position))

    print("\n[-2]────────────────[0]────────────────[+2]")
    print(" " * bar_position + "▼")

# 使用例
text = "最高に幸せ！！！"
inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=128)
with torch.no_grad():
    outputs = model(**inputs)
    prediction = outputs.logits.cpu().numpy()[0][0] * 2.0
    prediction = np.clip(prediction, -2.0, 2.0)
visualize_sentiment(text, prediction)
```

### 出力例

```
テキスト: 最高に幸せ！！！
感情極性: +1.79 (強いポジティブ)

[-2]────────────────[0]────────────────[+2]
                                     ▼
```

## Intended Uses

### 主な用途

- SNS 投稿、レビュー、コメントのポジ/ネガ判定
- カスタマーフィードバックの定量化
- ブランドモニタリング、評判分析
- コンテンツモデレーション

### 制限事項

- **主観データのみ**: 筆者の主観的な感情極性のみを予測（読者の感情は対象外）
- **ドメイン**: SNS 投稿風のカジュアルなテキストで最適化
- **長さ**: 最大 128 トークンまで
- **中立の判定**: 中立（0 付近）の判定精度が極端な感情より低い傾向

## Training Data

**WRIME v2 データセット**

- **出典**: [shunk031/wrime](https://huggingface.co/datasets/shunk031/wrime) (ver2)
- **使用データ**: 主観データ（writer）の感情極性のみ
- **スケール**: -2（強いネガティブ）～ +2（強いポジティブ）の連続値

| Split      | サンプル数 |
| ---------- | ---------- |
| Train      | 30,000     |
| Validation | 2,500      |
| Test       | 2,500      |

## Training Procedure

### ハイパーパラメータ

| パラメータ     | 値                                |
| -------------- | --------------------------------- |
| 学習率         | 1e-5                              |
| バッチサイズ   | 32 (16 × 2 gradient accumulation) |
| エポック数     | 7 (Early Stopping)                |
| Warmup Ratio   | 0.1                               |
| Weight Decay   | 0.01                              |
| 最大トークン長 | 128                               |
| 最適化手法     | AdamW                             |
| 精度           | FP16                              |

### データ正規化

- **学習時**: -2~+2 → -1~+1 に正規化
- **推論時**: -1~+1 → -2~+2 にデノーマライズが必要

## Evaluation Results

### テストセット性能 (WRIME v2 test split)

| 指標                                          | スコア     |
| --------------------------------------------- | ---------- |
| **RMSE** (-2 to +2 scale)                     | **0.9224** |
| **MAE** (-2 to +2 scale)                      | **0.7254** |
| **Pearson Correlation**                       | **0.6787** |
| **Sign Accuracy** (Positive/Negative/Neutral) | **68.76%** |
| **Within ±0.5 Accuracy**                      | **43.24%** |

## Comparison with 8-Emotions Model

同じ WRIME データセットを使った 2 つのモデルを提供しています：

| モデル                                                                             | タスク     | 出力                   | Pearson 相関 | 用途           |
| ---------------------------------------------------------------------------------- | ---------- | ---------------------- | ------------ | -------------- |
| [deberta-wrime-emotions](https://huggingface.co/neuralnaut/deberta-wrime-emotions) | 8 感情分析 | 8 次元ベクトル (0-3)   | 0.4720       | 複雑な感情分析 |
| **deberta-wrime-sentiment**                                                        | 感情極性   | 1 次元スカラー (-2~+2) | **0.6787**   | ポジ/ネガ判定  |

**使い分けの目安:**

- **感情極性モデル（このモデル）**: シンプルなポジ/ネガ判定、レビュー分析、SNS モニタリング
- **8 感情モデル**: 詳細な感情分析、メンタルヘルス、複雑な感情の可視化

## Limitations and Bias

- **主観データのみ**: 筆者の感情極性のみを予測
- **ドメインバイアス**: SNS 投稿のような短文に最適化
- **文化的バイアス**: 日本語話者の感情表現に特化
- **中立の精度**: 中立（0 付近）の判定が極端な感情より難しい
- **ポジティブバイアス**: やや楽観的な予測をする傾向（中立が+0.2 程度）
- **皮肉の検出**: 皮肉や反語的表現の検出が困難

## Citation

### このモデルの引用

```bibtex
@misc{neuralnaut2025deberta-wrime-sentiment,
  title = {DeBERTa v3 for Japanese Sentiment Analysis (WRIME - Sentiment Polarity)},
  author = {neuralnaut},
  year = {2025},
  publisher = {Hugging Face},
  howpublished = {\url{https://huggingface.co/neuralnaut/deberta-wrime-sentiment}},
}
```

### WRIME データセット

```bibtex
@inproceedings{kajiwara-etal-2021-wrime,
    title = "{WRIME}: A New Dataset for Emotional Intensity Estimation with Subjective and Objective Annotations",
    author = "Kajiwara, Tomoyuki and Chu, Chenhui and Takemura, Noriko and Nakashima, Yuta and Nagahara, Hajime",
    booktitle = "Proceedings of NAACL-HLT 2021",
    year = "2021",
    pages = "2095--2104",
}
```

### ベースモデル

```bibtex
@misc{ku-nlp-deberta-v3-base-japanese,
  title = {DeBERTa V3 base Japanese model},
  author = {Kyoto University NLP Lab},
  year = {2023},
  publisher = {Hugging Face},
  howpublished = {\url{https://huggingface.co/ku-nlp/deberta-v3-base-japanese}},
}
```
