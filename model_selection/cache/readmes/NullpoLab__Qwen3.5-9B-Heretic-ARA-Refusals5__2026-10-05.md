---
library_name: transformers
license: apache-2.0
license_link: https://huggingface.co/Qwen/Qwen3.5-9B/blob/main/LICENSE
pipeline_tag: image-text-to-text
base_model:
  - Qwen/Qwen3.5-9B
tags:
  - heretic
  - uncensored
  - decensored
  - abliterated
  - ara
---

# Qwen3.5-9B-Heretic-ARA-Refusals5

## 概要

[Qwen/Qwen3.5-9B](https://huggingface.co/Qwen/Qwen3.5-9B) を [Heretic](https://github.com/p-e-w/heretic) v1.2.0 の [Arbitrary-Rank Ablation (ARA)](https://github.com/p-e-w/heretic/pull/211) 手法を用いて検閲解除したモデルです。

## Abliteration 手法

**ARA (Arbitrary-Rank Ablation)** は Heretic PR #211 で導入された新しい abliteration 手法です。従来の方向性アブリタレーションとは異なり、PyTorch フックを使用して各トランスフォーマーモジュールの入出力テンソルをキャプチャし、L-BFGS による直接的な行列最適化でモジュールを修正します。

最適化は以下の3つの競合する目標のバランスを取ります：
1. 「無害な」プロンプトに対する出力をできる限り変化させない
2. 「有害な」プロンプトに対する出力を「無害な」プロンプトの出力に近づける
3. 「有害な」プロンプトに対する出力を元の状態から遠ざける（より強いステアリングのための過補正）

## Abliteration パラメータ

| パラメータ | 値 |
| :-------- | :---: |
| **start_layer_index** | 8 |
| **end_layer_index** | 31 |
| **preserve_good_behavior_weight** | 0.9665 |
| **steer_bad_behavior_weight** | 0.0001 |
| **overcorrect_relative_weight** | 1.1582 |
| **neighbor_count** | 15 |

## 性能

| 指標 | このモデル | 元のモデル ([Qwen/Qwen3.5-9B](https://huggingface.co/Qwen/Qwen3.5-9B)) |
| --- | --- | --- |
| **拒否率** | 5/100 | 84/100 |
| **KL発散** | 0.0239| 0 *(定義上)* |

> 評価は [mlabonne/harmful_behaviors](https://huggingface.co/datasets/mlabonne/harmful_behaviors)（テスト 100 プロンプト）で拒否率を、[mlabonne/harmless_alpaca](https://huggingface.co/datasets/mlabonne/harmless_alpaca)（テスト 100 プロンプト）で KL 発散を計測しました。

## 注記

- このモデルは研究およびクリエイティブライティング目的を想定しています
- Heretic の ARA ブランチ（PR #211）は現在(2026年3月20日) Draft 状態でメインブランチにまだマージされていません
- 拒否率の評価は英語プロンプトのみで実施しています。日本語プロンプトでの動作は異なる場合があります
- ベースモデル: [Qwen/Qwen3.5-9B](https://huggingface.co/Qwen/Qwen3.5-9B)
- Heretic: [p-e-w/heretic](https://github.com/p-e-w/heretic)
