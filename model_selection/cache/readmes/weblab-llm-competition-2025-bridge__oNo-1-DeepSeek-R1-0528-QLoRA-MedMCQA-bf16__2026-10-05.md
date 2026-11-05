---

license: mit
base\_model: deepseek-ai/DeepSeek-R1-0528
organization: "oNo.1"
model\_name: oNo-1-DeepSeek-R1-0528-QLoRA-MedMCQA-bf16
library\_name: transformers
pipeline\_tag: text-generation
language:
  - ja
tags:
  - bf16
  - merged
  - instruction-tuning
  - medical-qa
  - deepseek
  - ono1
  - reasoning
  - japan
datasets:
  - oNo-1/MedMCQA
---

# oNo-1-DeepSeek-R1-0528-QLoRA-MedMCQA-bf16

## ドキュメント

* Notion ガイド: **[https://www.notion.so/257e14b94af5808687a1f39f4b84bd0e?source=copy\_link](https://www.notion.so/257e14b94af5808687a1f39f4b84bd0e?source=copy_link)**

> **サマリー** — DeepSeek-R1-0528 をベースに、oNo-1/MedMCQAのプライベートサブセットを用いた内部ポストトレーニングの成果物です。

---

## モデル詳細

* **ベースモデル**: `deepseek-ai/DeepSeek-R1-0528`（MIT）
* **パラメータ構成**: マージ済みフルモデル（追加アダプタ不要）
* **トークナイザ**: ベースモデル付属を使用

---

## データ

* **利用データ（private）**: `oNo-1/MedMCQA`
* **ライセンス**: Dataset 側は **Apache-2.0** 表記。ベース（MIT）との整合を確認のうえ再配布・商用可否を判断してください。

### プロンプト

* ベースの DeepSeek **チャットテンプレート**準拠。具体的な運用・プロンプト設計は **Notion** を参照してください。

---

## 学習サマリー

* **oNo.1** による **内部ポストトレーニング**の成果物です。
* 具体的なハイパーパラメータやレシピは **コンペ期間中は非公開**です。
* 最終モデルは **merged** でエクスポートされています。

---

## 推論

* 推論手順・推奨ランタイム の注意事項は **Notion** を参照してください：[https://www.notion.so/257e14b94af5808687a1f39f4b84bd0e?source=copy\_link](https://www.notion.so/257e14b94af5808687a1f39f4b84bd0e?source=copy_link)

---

## 安全性と責任ある利用

* **医療用途不可**。診断・治療・処方の代替には使用しないでください。
* エンドユーザー向け公開前に、**拒否ポリシー**／**検証付き検索**／**人手レビュー**の導入を推奨します。
* 幻覚・古い知識・バイアスに対して **レッドチーミング** を実施してください。

---

## バージョン管理と成果物

* 配布対象: **マージ済みモデル重み** と **tokenizer**。
* 付随する設定や学習ログはコンペ期間中は非公開です。

---

## ライセンス

* **Base model**: MIT（DeepSeek-R1-0528）
* **Dataset**: Apache-2.0（oNo-1/MedMCQA）
* **This model**: **MIT**

---

## 引用

* DeepSeek-R1: *DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning*（2025）, arXiv:2501.12948
* MedMCQA: Pal et al., *MedMCQA: A Large-scale Multi-Subject Multi-Choice Dataset for Medical domain Question Answering*, PMLR 174（2022）

---

## 謝辞

* DeepSeek チーム（ベースモデル／トークナイザ）
* Transformers / bitsandbytes / PEFT メンテナ
* データセット作成者およびレビュアのみなさま
