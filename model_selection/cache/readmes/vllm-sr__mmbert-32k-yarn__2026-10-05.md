---
license: mit
language:
- multilingual
- en
- de
- fr
- es
- zh
- ja
- ru
- ar
- ko
- pt
library_name: transformers
tags:
- modernbert
- mlm
- long-context
- rope
- yarn
- multilingual
- fill-mask
- semantic-router
- mixture-of-models
datasets:
- cc100
base_model: jhu-clsp/mmBERT-base
pipeline_tag: fill-mask
model-index:
- name: mmbert-32k-yarn
  results:
  - task:
      type: fill-mask
      name: Masked Language Modeling
    metrics:
    - name: MLM Accuracy (English)
      type: accuracy
      value: 1.0
    - name: MLM Accuracy (Multilingual)
      type: accuracy
      value: 1.0
    - name: Distance Retrieval (≤2048)
      type: accuracy
      value: 1.0
    - name: Perplexity (32K context)
      type: perplexity
      value: 1.0003
---

# mmBERT-32K-YaRN

**Modern Multilingual BERT with 32K context length** - Extended from 8K to 32K tokens using YaRN RoPE scaling.

This model extends [jhu-clsp/mmBERT-base](https://huggingface.co/jhu-clsp/mmBERT-base) (Modern Multilingual BERT supporting 1800+ languages) from 8,192 to **32,768** maximum context length using [YaRN](https://arxiv.org/abs/2309.00071) (Yet another RoPE extensioN) scaling method.

## Model Description

| Property | Value |
|----------|-------|
| **Base Model** | [jhu-clsp/mmBERT-base](https://huggingface.co/jhu-clsp/mmBERT-base) |
| **Architecture** | ModernBERT (RoPE + Flash Attention 2) |
| **Parameters** | 307M |
| **Max Context** | 32,768 tokens (extended from 8,192) |
| **Languages** | 1800+ languages |
| **Vocab Size** | 256,000 (Gemma 2 tokenizer) |
| **Scaling Method** | YaRN RoPE (4x extension) |

## Intended Use

This model is designed for:
- **Long-document understanding** in any of 1800+ languages
- **Semantic routing** for LLM request classification
- **Document classification** with extended context
- **Information retrieval** from long texts
- **Multilingual NLP tasks** requiring long context

Part of the [vLLM Semantic Router](https://huggingface.co/vllm-sr) Mixture-of-Models (MoM) family.

## Evaluation Results

### Distance-Based Retrieval (Key Metric for Long-Context)

| Distance (tokens) | Top-1 Accuracy | Top-5 Accuracy |
|-------------------|----------------|----------------|
| 64 | 100% | 100% |
| 128 | 100% | 100% |
| 256 | 100% | 100% |
| 512 | 100% | 100% |
| 1024 | 100% | 100% |
| 2048 | 100% | 100% |
| 4096 | 0% | 0% |
| 8192 | 0% | 0% |

**Summary**: Perfect retrieval up to 2048 tokens. Long-range capability improved from baseline ~33% to **50%** (averaged across all distances ≥1024).

### Multilingual MLM Accuracy

| Language | Correct |
|----------|---------|
| English (en) | ✅ |
| German (de) | ✅ |
| French (fr) | ✅ |
| Spanish (es) | ✅ |
| Chinese (zh) | ✅ |
| Japanese (ja) | ✅ |
| Russian (ru) | ✅ |
| Arabic (ar) | ✅ |
| Korean (ko) | ✅ |
| Portuguese (pt) | ✅ |

**Overall**: 100% (10/10 languages tested)

### Perplexity by Context Length

| Context Length | Loss | Perplexity |
|----------------|------|------------|
| 512 | 0.0110 | 1.01 |
| 1024 | 0.0082 | 1.01 |
| 2048 | 0.0065 | 1.01 |
| 4096 | 0.0036 | 1.00 |
| 8192 | 0.0014 | 1.00 |
| 16384 | 0.0014 | 1.00 |
| 24576 | 0.0014 | 1.00 |
| **32768** | **0.0003** | **1.00** |

### Position-wise Accuracy (16K context)

| Position Range | Accuracy |
|----------------|----------|
| 0-2048 | 100% |
| 2048-4096 | 100% |
| 4096-6144 | 100% |
| 6144-8192 | 100% |
| 8192-10240 | 100% |
| 10240-12288 | 100% |
| 12288-14336 | 100% |
| 14336-16384 | 100% |

## Training Details

### Training Configuration

```yaml
base_model: jhu-clsp/mmBERT-base
rope_scaling_type: yarn
original_max_position_embeddings: 8192
target_max_position_embeddings: 32768
scaling_factor: 4.0
yarn_beta_fast: 32.0
yarn_beta_slow: 1.0

# Training hyperparameters
learning_rate: 1e-5
batch_size: 1 (effective: 16 with gradient accumulation)
gradient_accumulation_steps: 16
num_epochs: 1
warmup_steps: 100
lr_scheduler: constant_with_warmup
mlm_probability: 0.3
bf16: true
```

### Training Data

- **Dataset**: CC-100 (Common Crawl) multilingual corpus
- **Samples**: 30,774 sequences
- **Sequence Length**: 32,768 tokens each
- **Total Tokens**: ~1B tokens

### Hardware

- **GPU**: AMD Instinct MI300X (192GB VRAM)
- **Training Time**: ~6.5 hours
- **Framework**: PyTorch 2.3 + ROCm 6.2

## Usage

### Basic Usage

```python
from transformers import AutoModelForMaskedLM, AutoTokenizer

model = AutoModelForMaskedLM.from_pretrained("vllm-sr/mmbert-32k-yarn")
tokenizer = AutoTokenizer.from_pretrained("vllm-sr/mmbert-32k-yarn")

# Multilingual MLM example
text = "The capital of France is <mask>."
inputs = tokenizer(text, return_tensors="pt")
outputs = model(**inputs)

mask_idx = (inputs["input_ids"] == tokenizer.mask_token_id).nonzero()[0, 1]
logits = outputs.logits[0, mask_idx]
top5 = tokenizer.decode(logits.topk(5).indices)
print(top5)  # ['Paris', 'Strasbourg', 'Nice', 'Brussels', 'Lyon']
```

### Long Context Usage (32K tokens)

```python
# Process long documents (up to 32K tokens)
long_document = "..." * 30000  # Your long text in any of 1800+ languages
inputs = tokenizer(
    long_document, 
    return_tensors="pt", 
    max_length=32768, 
    truncation=True
)
outputs = model(**inputs)
```

### Feature Extraction

```python
import torch

# Get embeddings for downstream tasks
with torch.no_grad():
    outputs = model(**inputs, output_hidden_states=True)
    # Use last hidden state or pooled output
    embeddings = outputs.hidden_states[-1].mean(dim=1)  # Mean pooling
```

## ONNX Runtime Usage

An ONNX export is available for high-performance inference with ONNX Runtime.

### Python

```python
import onnxruntime as ort
from transformers import AutoTokenizer
import numpy as np

# Load tokenizer and ONNX model
tokenizer = AutoTokenizer.from_pretrained("vllm-sr/mmbert-32k-yarn")
sess = ort.InferenceSession(
    "onnx/model.onnx",  # or download from HF
    providers=['ROCmExecutionProvider', 'CUDAExecutionProvider', 'CPUExecutionProvider']
)

# Inference
text = "What is the weather like today?"
inputs = tokenizer(text, return_tensors="np", padding=True)
outputs = sess.run(None, {
    'input_ids': inputs['input_ids'].astype(np.int64),
    'attention_mask': inputs['attention_mask'].astype(np.int64)
})
embeddings = outputs[0].mean(axis=1)  # Mean pooling
```

### Rust (ort-binding)

```rust
use onnx_semantic_router::MmBertEmbeddingModel;

let model = MmBertEmbeddingModel::load("./mmbert-32k-yarn-onnx", false)?;
let embeddings = model.embed("What is the weather?")?;
```

### Latency Benchmarks (AMD MI300X)

| Backend | Single Text | Batch(4)/text |
|---------|-------------|---------------|
| CPU | 10.1ms | 6.8ms |
| ROCm GPU | **4.7ms** | **1.2ms** |

## Limitations

- **Long-range retrieval**: While the model handles 32K context, retrieval accuracy drops significantly beyond 2048 tokens distance
- **Training data**: Trained on CC-100 which may have biases from web crawl data
- **Compute requirements**: Full 32K context requires significant GPU memory (~180GB for batch size 1)

## Citation

```bibtex
@misc{mmbert-32k-yarn,
  title={mmBERT-32K-YaRN: Extended Context Modern Multilingual BERT},
  author={vLLM Semantic Router Team},
  year={2026},
  publisher={Hugging Face},
  url={https://huggingface.co/vllm-sr/mmbert-32k-yarn}
}
```

## References

- [mmBERT](https://huggingface.co/jhu-clsp/mmBERT-base) - Modern Multilingual BERT (1800+ languages)
- [ModernBERT](https://huggingface.co/answerdotai/ModernBERT-base) - Base architecture
- [YaRN](https://arxiv.org/abs/2309.00071) - Yet another RoPE extensioN method
- [vLLM Semantic Router](https://huggingface.co/vllm-sr) - Mixture-of-Models routing

## License

MIT License (same as mmBERT base model)
