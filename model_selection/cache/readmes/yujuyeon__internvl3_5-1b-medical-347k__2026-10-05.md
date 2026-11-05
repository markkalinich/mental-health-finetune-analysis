---
license: other
base_model: OpenGVLab/InternVL3_5-1B
language:
- ko
- en
pipeline_tag: image-text-to-text
library_name: transformers
tags:
- internvl
- mllm
- korean
- vision-language
---

# internvl3_5-1b-medical-347k

`OpenGVLab/InternVL3_5-1B` 를 한국어 멀티모달 데이터로 파인튜닝한 InternVL3.5 specialist.

| 항목 | 값 |
|---|---|
| Base model | [`OpenGVLab/InternVL3_5-1B`](https://huggingface.co/OpenGVLab/InternVL3_5-1B) |
| Method | — |
| Domain | 의료 347k |

## Hyperparameters
*별도 서버 학습 — 하이퍼파라미터 로그 미동봉.*

## Training Loss
*학습 loss 로그 미동봉 (별도 서버 학습).*

## Training Data
구성: **1개 서브셋** (한국어 specialist SFT)

| subset | repeat |
|---|---|
| `medical_347k` | 1 |

## Usage
```python
from transformers import AutoModel, AutoTokenizer
import torch
m = AutoModel.from_pretrained("yujuyeon/internvl3_5-1b-medical-347k", torch_dtype=torch.bfloat16,
                              trust_remote_code=True).eval().cuda()
tok = AutoTokenizer.from_pretrained("yujuyeon/internvl3_5-1b-medical-347k", trust_remote_code=True, use_fast=False)
```
