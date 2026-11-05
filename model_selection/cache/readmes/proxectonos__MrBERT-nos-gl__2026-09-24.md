---
license: apache-2.0
language:
- gl
- pt
base_model:
- BSC-LT/MrBERT
datasets:
- proxectonos/corpusnos
pipeline_tag: fill-mask
---
# MrBERT-nos-gl

MrBERT-nos-gl is a domain-adapted encoder model obtained by continued pre-training of [BSC-LT/MrBERT](https://huggingface.co/BSC-LT/MrBERT) on [CorpusNÓS](https://huggingface.co/datasets/proxectonos/corpusnos), a large-scale Galician corpus (~1.9B tokens). It inherits MrBERT's ModernBERT architecture — with efficient long-context modeling (up to 1,024 tokens) via RoPE and sliding-window attention — and extends its coverage of Galician and Portuguese, two closely related Iberian languages underrepresented in most multilingual encoders.

The model is designed as a general-purpose encoder suitable for fine-tuning on downstream tasks such as named entity recognition, part-of-speech tagging, text classification, semantic similarity, question answering, and cross-lingual retrieval. It is the foundation for the [MrBERT-nos-gl model collection](https://huggingface.co/collections/proxectonos/mrbert-nos-gl).

Developed as part of **Proxecto Nós**, an initiative to build language technology for the Galician language.

## Technical Description

MrBERT-nos-gl starts from the MrBERT base checkpoint and continues pre-training with a masked language modelling objective on a combined Galician and Portuguese corpus. The architecture is identical to the base model; only the training regime and data distribution differ.

### Model Architecture

| Description                    | Value                      |
|--------------------------------|----------------------------|
| Base Model                     | BSC-LT/MrBERT              |
| Model Parameters               | 308M                       |
| Tokenizer                      | SentencePiece (SPM)        |
| Vocabulary Size                | 256,000                    |
| Hidden Layers                  | 22                         |
| Hidden Size                    | 768                        |
| Intermediate Size (FFN)        | 1,152                      |
| Attention Heads                | 12 (head size: 64)         |
| Attention Type                 | RoPE (Rotary Positional Embedding) |
| Sliding Window Size            | 128 tokens                 |
| Global Attention Every N Layers| 3                          |
| FFN Layer                      | Gated Linear Unit (GLU)    |
| Normalization                  | Pre-norm LayerNorm (ε=1e-5)|
| Activation Function            | GeLU                       |
| Precision                      | bfloat16 (AMP)             |
| Context Length                 | 1,024 tokens               |
| Weight Initialisation          | Full Megatron               |

### Continued Pre-training Hyperparameters

| Hyperparameter                  | Value                                              |
|---------------------------------|----------------------------------------------------|
| Objective                       | Masked Language Modeling (MLM)                     |
| Train MLM Mask Probability      | 30%                                                |
| Eval MLM Mask Probability       | 15%                                                |
| Peak Learning Rate              | 1e-5                                               |
| LR Scheduler                    | Warmup–Stable–Decay (WSD)                          |
| Decay Budget                    | 0 tokens (no decay phase)                          |
| Final LR Factor (α_f)           | 0.0                                                |
| Optimizer                       | Decoupled StableAdamW                              |
| Optimizer β1 / β2               | 0.9 / 0.98                                         |
| Optimizer ε                     | 1e-6                                               |
| Weight Decay                    | 1e-5                                               |
| Bias & Norm Weight Decay        | Disabled (`filter_bias_norm_wd: true`)             |
| Global Batch Size               | 512 sequences                                      |
| Device Microbatch Size (train)  | 16 sequences                                       |
| Device Batch Size (eval)        | 32 sequences                                       |
| Training Budget                 | 300,000,000 tokens                                 |
| Sequence Packing                | Disabled                                           |
| Padding Strategy                | Unpadded (Flash Attention compatible)              |
| Count Padding Tokens in Budget  | No                                                 |
| Batch Size Warmup               | From microbatch size up over 30M tokens            |
| Attention Dropout               | 0.0 (train) / 0.1 (output projection)             |
| Seed                            | 17                                                 |

## Usage

This model is a **base encoder** intended for fine-tuning, not for direct text generation. Load it with the `fill-mask` pipeline for masked language modeling, or use it as a backbone for downstream task fine-tuning.

### Installation

```bash
pip install transformers torch
```

### Masked language modeling

```python
from transformers import pipeline

mlm = pipeline("fill-mask", model="proxectonos/MrBERT-nos-gl")

results = mlm("A lingua galega é unha das linguas [MASK] de Europa.")
for r in results:
    print(f"{r['token_str']:<20} {r['score']*100:.1f}%")
```

### Feature extraction / embeddings

```python
from transformers import AutoTokenizer, AutoModel
import torch

tokenizer = AutoTokenizer.from_pretrained("proxectonos/MrBERT-nos-gl")
model = AutoModel.from_pretrained("proxectonos/MrBERT-nos-gl")

inputs = tokenizer("A lingua galega é unha das linguas romances de Europa.", return_tensors="pt")
with torch.no_grad():
    outputs = model(**inputs)

# Mean-pool the last hidden state for a sentence embedding
embeddings = outputs.last_hidden_state.mean(dim=1)
```

## Acknowledgements

This work is funded by the Ministerio para la Transformación Digital y de la Función Pública - Funded by EU – NextGenerationEU within the framework of the project Desarrollo de Modelos ALIA. (Esta publicación del proyecto Desarrollo de Modelos ALIA está financiada por el Ministerio para la Transformación Digital y de la Función Pública y por el Plan de Recuperación, Transformación y Resiliencia – Financiado por la Unión Europea – NextGenerationEU)