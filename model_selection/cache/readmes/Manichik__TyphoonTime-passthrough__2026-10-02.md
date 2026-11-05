---
license: apache-2.0
tags:
- merge
- mergekit
- lazymergekit
- scb10x/typhoon-7b
- chargoddard/storytime-13b
---

# TyphoonTime-passthrough

TyphoonTime-passthrough is a merge of the following models using [mergekit](https://github.com/cg123/mergekit):
* [scb10x/typhoon-7b](https://huggingface.co/scb10x/typhoon-7b)
* [chargoddard/storytime-13b](https://huggingface.co/chargoddard/storytime-13b)

## 🧩 Configuration

\```yaml
slices:
  - sources:
    - model: scb10x/typhoon-7b
      layer_range: [0, 32]
  - sources:
    - model: chargoddard/storytime-13b
      layer_range: [24, 32]
merge_method: passthrough
dtype: bfloat16
\```