---
license: apache-2.0
base_model: InternScience/Agents-A1-4B
library_name: transformers
pipeline_tag: text-generation
tags:
- heretic
- uncensored
- decensored
- abliterated
- ara
- conversational
---

English version: [README_en.md](README_en.md)

# Agents-A1-4B-Heretic-ARA-Refusals7

## 概要

[InternScience/Agents-A1-4B](https://huggingface.co/InternScience/Agents-A1-4B) を [Heretic](https://github.com/p-e-w/heretic) v1.2.0 の [Arbitrary-Rank Ablation (ARA)](https://github.com/p-e-w/heretic/pull/211) 手法を用いて検閲解除したモデルです。

## 変換に関する注記

現時点では、そのままGGUF化すると読み込みエラーが発生するため、暫定的な回避策としてconfig.jsonの"mtp_num_hidden_layers"を0に変更しています。

## Abliteration パラメータ

| パラメータ | 値 |
| --- | --- |
| **start_layer_index** | 13 |
| **end_layer_index** | 25 |
| **preserve_good_behavior_weight** | 0.8630 |
| **steer_bad_behavior_weight** | 0.0001 |
| **overcorrect_relative_weight** | 1.1907 |
| **neighbor_count** | 15 |

## 性能

| 指標 | このモデル | 元のモデル ([InternScience/Agents-A1-4B](https://huggingface.co/InternScience/Agents-A1-4B)) |
| --- | --- | --- |
| **拒否率** | 7/100 | 85/100 |
| **KL発散** | 0.0030 | 0 *(定義上)* |

> 評価は [mlabonne/harmful_behaviors](https://huggingface.co/datasets/mlabonne/harmful_behaviors)（テスト 100 プロンプト）で拒否率を、[mlabonne/harmless_alpaca](https://huggingface.co/datasets/mlabonne/harmless_alpaca)（テスト 100 プロンプト）で KL 発散を計測しました。

## 注記

- このモデルは研究およびクリエイティブライティング目的を想定しています
- 拒否率の評価は英語プロンプトのみで実施しています。日本語プロンプトでの動作は異なる場合があります
- ベースモデル: [InternScience/Agents-A1-4B](https://huggingface.co/InternScience/Agents-A1-4B)
- Heretic: [p-e-w/heretic](https://github.com/p-e-w/heretic)
