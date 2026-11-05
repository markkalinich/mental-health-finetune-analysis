---
library_name: transformers
tags:
- modernbert
- fill-mask
- multilingual
license: apache-2.0
base_model: jhu-clsp/mmBERT-small
---

# mmBERT-small

Transformers v5 compatible checkpoint of [jhu-clsp/mmBERT-small](https://huggingface.co/jhu-clsp/mmBERT-small).

| | |
|---|---|
| **Parameters** | 140M |
| **Hidden size** | 384 |
| **Layers** | 22 |
| **Attention heads** | 6 |
| **Max seq length** | 8,192 |
| **RoPE theta** | 160,000 (both global & local) |

## Usage (transformers v5)

```python
from transformers import ModernBertModel, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("datalama/mmBERT-small")
model = ModernBertModel.from_pretrained("datalama/mmBERT-small")

inputs = tokenizer("인공지능 기술은 빠르게 발전하고 있습니다.", return_tensors="pt")
outputs = model(**inputs)

# [CLS] embedding (384-dim)
cls_embedding = outputs.last_hidden_state[:, 0, :]
```

For masked language modeling:

```python
from transformers import ModernBertForMaskedLM, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("datalama/mmBERT-small")
model = ModernBertForMaskedLM.from_pretrained("datalama/mmBERT-small")

inputs = tokenizer("The capital of France is [MASK].", return_tensors="pt")
outputs = model(**inputs)
```

## Migration Details

This checkpoint was migrated from [jhu-clsp/mmBERT-small](https://huggingface.co/jhu-clsp/mmBERT-small) with the following changes:

**1. Weight format**: `pytorch_model.bin` → `model.safetensors`
- Tied weights (`model.embeddings.tok_embeddings.weight` ↔ `decoder.weight`) were cloned to separate tensors before saving
- All 138 tensors verified bitwise equal after conversion

**2. Config**: Added explicit `rope_parameters` for transformers v5
```json
{
  "global_rope_theta": 160000,
  "local_rope_theta": 160000,
  "rope_parameters": {
    "full_attention": {"rope_type": "default", "rope_theta": 160000.0},
    "sliding_attention": {"rope_type": "default", "rope_theta": 160000.0}
  }
}
```
The original flat fields (`global_rope_theta`, `local_rope_theta`) are preserved for backward compatibility.
In transformers v5, `ModernBertConfig` defaults `sliding_attention.rope_theta` to 10,000 — but mmBERT uses 160,000 for both, so explicit `rope_parameters` are required.

## Verification

Cross-environment verification was performed between transformers v4 (original) and v5 (this checkpoint):

| Check | Result |
|---|---|
| **RoPE config** | `rope_parameters` present, theta=160,000 for both attention types |
| **Weight integrity** | 138 tensors bitwise equal (jhu-clsp `.bin` vs datalama `.safetensors`) |
| **Inference output** | v4 vs v5 max diff across 4 multilingual sentences: **1.14e-05** |
| **Fine-tuning readiness** | Tokenizer roundtrip, forward+backward pass, gradient propagation — all OK |

## Credit

Original model by [JHU CLSP](https://huggingface.co/jhu-clsp). See the [original model card](https://huggingface.co/jhu-clsp/mmBERT-small) for training details and benchmarks.
