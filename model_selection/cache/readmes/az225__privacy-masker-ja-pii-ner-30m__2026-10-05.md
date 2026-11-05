---
language:
  - ja
license: apache-2.0
library_name: privacy-masker
pipeline_tag: token-classification
inference: false
base_model: cl-nagoya/ruri-v3-30m
base_model_relation: finetune
tags:
  - ner
  - pii
  - anonymization
  - de-identification
  - japanese
  - modernbert
  - character-level
  - privacy-masker
datasets:
  - stockmark/ner-wikipedia-dataset
  - nvidia/Nemotron-Personas-Japan
---

# privacy-masker 用 日本語 PII 検出モデル（文字単位 NER）

[privacy-masker](https://github.com/NishidaAzuharu/privacy-masker)（日本語テキストの個人情報を検出・仮名化・匿名化する Python ライブラリ、MIT）が
NER 検出器として使う学習済みモデルです。日本語テキストから、個人情報につながる固有表現 — **人名 PERSON・組織 ORG・地名 LOCATION・施設 FACILITY・住所 ADDRESS** — を
**文字単位**のスパンで検出します。ライブラリの使い方、評価の手順、精度の目安は privacy-masker の README を参照してください。

*The NER model used by [privacy-masker](https://github.com/NishidaAzuharu/privacy-masker), a Japanese PII de-identification library.
It returns character-level spans for PERSON / ORG / LOCATION / FACILITY / ADDRESS. Load it with privacy-masker's `CharHeadNerDetector`;
it is not a `transformers` token-classification model, so the Hub inference widget does not apply. Documentation is in Japanese.*

## 使い方

```bash
pip install 'privacy-masker[transformers]'
```

```python
from privacy_masker import PrivacyEngine, Policy
from privacy_masker.detectors import CharHeadNerDetector, HandleDetector, RegexDetector

ner = CharHeadNerDetector(model="az225/privacy-masker-ja-pii-ner-30m")   # 初回に Hub から取得してキャッシュ。revision="<commit>" で固定できます
engine = PrivacyEngine(
    detectors=[ner, RegexDetector.default_ja(), HandleDetector()],   # NER + 電話・メール等の正規表現 + ハンドル名
    policy=Policy.preset("llm_input"),                                # すべて <TYPE_001> 形式のトークンに
)
print(engine.transform("山田太郎さんは株式会社ABCに勤務しており、東京都新宿区に住んでいる。").text)
# <PERSON_001>さんは<ORG_001>に勤務しており、<LOCATION_001>に住んでいる。
```

`transformers` の `pipeline("token-classification")` や `AutoModelForTokenClassification` では使えません（`AutoModel` で読めるのは encoder だけです）。
検出結果だけが要るときは `engine.detect(text)`、偽名への置換や公知の実体を残すレベルの使い方はライブラリの README にあります。

## 仕様

| 項目 | 内容 |
|---|---|
| 用途 | privacy-masker の NER 検出器（`CharHeadNerDetector`）。Refiner（敬称・助詞の削除、種別語尾の取り込み）と Resolver（重複解決）はライブラリ側 |
| 対象 | 日本語。ラベルは PERSON・ORG・LOCATION・FACILITY・ADDRESS（文字単位の BIO、11 ラベル） |
| encoder | [`cl-nagoya/ruri-v3-30m`](https://huggingface.co/cl-nagoya/ruri-v3-30m)（ModernBERT、10 層・hidden 256、Apache-2.0。commit `24899e5de370b56d179604a007c0d727bf144504`）を全層 fine-tune |
| 文字ヘッド | サブワードの隠れ状態を文字に展開し、文字埋め込み・文字種・トークン内位置の特徴を足して、文字ごとに BIO ラベルを出す小さなヘッド（追加パラメータ 87,947） |
| 重み | 1 回の学習の複数エポックの単純平均 |
| 入力 | 400 字のチャンク（重なり 50 字、最大 512 トークン）。被覆されない文字や非有限の出力があれば例外で止まる（空結果を返さない） |
| 規約 | ADDRESS は番地あり、LOCATION は番地なし。敬称・肩書きはスパン外。電話・メール・郵便番号・日付は対象外（privacy-masker の正規表現が担当） |
| ファイル | `model.safetensors`（encoder）、`char_head.safetensors` + `char_head_config.json`（文字ヘッド）、`config.json`、`tokenizer.json`、`tokenizer_config.json`、`privacy_masker_model.json`（由来と SHA-256） |

## 学習データ

Wikipedia 由来の固有表現データ（[`stockmark/ner-wikipedia-dataset`](https://huggingface.co/datasets/stockmark/ner-wikipedia-dataset)、CC BY-SA 3.0）、
[UD Japanese GSD](https://github.com/megagonlabs/UD_Japanese-GSD) の学習・開発分割（CC BY-SA 4.0）、
LLM（[`Qwen/Qwen3.8-27B-FP8`](https://huggingface.co/Qwen/Qwen3.8-27B-FP8)、Apache-2.0）に書かせたテンプレートへ
[`nvidia/Nemotron-Personas-Japan`](https://huggingface.co/datasets/nvidia/Nemotron-Personas-Japan)（CC BY 4.0）の人名と日本郵便の郵便番号データから合成した値を差し込んだ文書、
および PII を含まない負例で学習しました。評価に使う文書の本文・表層は学習データから除外しています。学習データそのものは配布しません。

## 制限

- 検出漏れ・過剰検出は起こり得ます。人手レビューの併用を前提にし、導入前に自分の文書で評価してください（評価の手順と精度の目安は privacy-masker の README）。
- 個人情報保護法などの基準への適合を保証するものではありません。個人を特定・追跡する目的での利用は意図していません。

## ライセンスと帰属

- このリポジトリの重みと設定ファイル: **apache-2.0**
- encoder の元モデル `cl-nagoya/ruri-v3-30m`: Apache-2.0（その元の `sbintuitions/modernbert-ja-30m`: MIT）
- 学習データ: 上記の各ライセンス。文書・名前そのものは再配布していません。

## ファイルの SHA-256

| ファイル | バイト数 | SHA-256 |
|---|---:|---|
| `config.json` | 1,620 | `00d64f3a89db465a5b5b99b5a05c8cdef530698f45de52f921633dd825b26520` |
| `model.safetensors` | 146,828,152 | `bfa2ca18011e19a6433e1d4629d782b50d3f3fc611aad2c2fdedc169b5a06c0a` |
| `tokenizer.json` | 6,718,593 | `4609ae999e7493b0fa06aa904f230520b80ccc93eecdf33b8d5e1276808be1a5` |
| `tokenizer_config.json` | 641 | `63727b7709f506f417676e76109680de4cede16708c5ad14d9c790a8688631d7` |
| `char_head.safetensors` | 353,028 | `0e6846a813e7192d3d84bac998d82589bc91bdb6976a2ba77b8d604cee51b080` |
| `char_head_config.json` | 381 | `fd82a8e2b40bb2b5333b4fe795ce976ee51fa1528e45076152415dbb441651a9` |
