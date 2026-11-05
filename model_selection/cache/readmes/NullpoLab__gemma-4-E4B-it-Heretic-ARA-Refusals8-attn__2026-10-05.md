---
library_name: transformers
license: apache-2.0
license_link: https://ai.google.dev/gemma/docs/gemma_4_license
pipeline_tag: image-text-to-text
base_model:
  - google/gemma-4-E4B-it
tags:
  - heretic
  - uncensored
  - decensored
  - abliterated
  - ara
---

# gemma-4-E4B-it-Heretic-ARA-Refusals8-attn

## 概要

[google/gemma-4-E4B-it](https://huggingface.co/google/gemma-4-E4B-it) を [Heretic](https://github.com/p-e-w/heretic) v1.2.0 の [Arbitrary-Rank Ablation (ARA)](https://github.com/p-e-w/heretic/pull/211) 手法を用いて検閲解除したモデルです。

## Abliteration 手法

**ARA (Arbitrary-Rank Ablation)** は Heretic PR #211 で導入された新しい abliteration 手法です。従来の方向性アブリタレーションとは異なり、PyTorch フックを使用して各トランスフォーマーモジュールの入出力テンソルをキャプチャし、L-BFGS による直接的な行列最適化でモジュールを修正します。

最適化は以下の3つの競合する目標のバランスを取ります：
1. 「無害な」プロンプトに対する出力をできる限り変化させない
2. 「有害な」プロンプトに対する出力を「無害な」プロンプトの出力に近づける
3. 「有害な」プロンプトに対する出力を元の状態から遠ざける（より強いステアリングのための過補正）

`target_components = ["attn.o_proj"]` を設定し、アテンション出力プロジェクション層のみをabliterationの対象としています。

## Abliteration パラメータ

| パラメータ | 値 |
| :-------- | :---: |
| **start_layer_index** | 17 |
| **end_layer_index** | 42 |
| **preserve_good_behavior_weight** | 0.9217 |
| **steer_bad_behavior_weight** | 0.0010 |
| **overcorrect_relative_weight** | 0.7196 |
| **neighbor_count** | 15 |

## 性能

| 指標 | このモデル | 元のモデル ([google/gemma-4-E4B-it](https://huggingface.co/google/gemma-4-E4B-it)) |
| --- | --- | --- |
| **拒否率** | 8/100 | 99/100 |
| **KL発散** | 0.0151 | 0 *(定義上)* |

> 評価は [mlabonne/harmful_behaviors](https://huggingface.co/datasets/mlabonne/harmful_behaviors)（テスト 100 プロンプト）で拒否率を、[mlabonne/harmless_alpaca](https://huggingface.co/datasets/mlabonne/harmless_alpaca)（テスト 100 プロンプト）で KL 発散を計測しました。

## 注記

- このモデルは研究およびクリエイティブライティング目的を想定しています
- Heretic の ARA ブランチ（PR #211）は現在(2026年4月4日) Draft 状態でメインブランチにまだマージされていません（使用コミット: `3b70fe5`）
- 拒否率の評価は英語プロンプトのみで実施しています。日本語プロンプトでの動作は異なる場合があります
- ベースモデル: [google/gemma-4-E4B-it](https://huggingface.co/google/gemma-4-E4B-it)
- Heretic: [p-e-w/heretic](https://github.com/p-e-w/heretic)
