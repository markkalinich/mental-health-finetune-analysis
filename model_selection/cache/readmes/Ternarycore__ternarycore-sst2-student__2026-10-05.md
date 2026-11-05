---
license: apache-2.0
language:
  - en
library_name: transformers
pipeline_tag: text-generation
base_model: Qwen/Qwen3-0.6B
base_model_relation: finetune
tags:
  - ternary
  - bitnet
  - b1.58
  - 1.58-bit
  - quantization
  - knowledge-distillation
  - qwen3
  - fpga
  - reconfigurable-computing
  - multiplier-free
  - sst-2
  - sentiment-analysis
datasets:
  - stanfordnlp/sst2
metrics:
  - accuracy
widget:
  - text: "Review: a gorgeous, witty, seductive movie.\nSentiment:"
    example_title: Positive
  - text: "Review: dull, plodding and utterly joyless.\nSentiment:"
    example_title: Negative
model-index:
  - name: ternarycore-sst2-student
    results:
      - task:
          type: text-classification
          name: Sentiment Analysis
        dataset:
          type: sst2
          name: GLUE SST-2
        metrics:
          - type: accuracy
            value: 0.914
            name: Validation accuracy
---

# TernaryCore SST-2 Student (W1.58A8)

A **ternary-weight** transformer distilled from a full-precision teacher for binary
sentiment classification on **GLUE SST-2**. Every linear-projection weight is constrained
to balanced ternary **{-1, 0, +1}** (~1.58 bits/weight, absmean-scaled) and paired with
8-bit activations (**W1.58A8**), so each weight-activation product is `+x`, `-x`, or `0`
and the matrix multiplies reduce to conditional accumulation - **no hardware multiplier
required**.

It is trained with Microsoft’s **BitNet Distillation** recipe
([arXiv:2510.13998](https://arxiv.org/abs/2510.13998)): replace the linear layers with
BitLinear, insert SubLN normalization, warm up with quantization-aware training, then
distill from the teacher with logit (and attention-relation) losses. The task is framed
generatively (`"Review: ...\nSentiment:"` -> `" positive"` / `" negative"`) so the
deployment path is the same decoder-LM datapath the hardware runs.

This is the reproducible demonstrator workload for **TernaryCore**, an open-source
multiplier-free ternary MAC/dot/GEMM accelerator that runs on a low-cost Artix-7 FPGA,
and it is the exact checkpoint behind the accompanying manuscript’s on-hardware energy
measurements.

> **Version note.** This card documents a frozen release. Cite this specific revision /
> DOI (not `main`) - the accompanying measured numbers are pinned to this snapshot.

## Usage

The model adds SubLN layers that stock `Qwen3ForCausalLM` does not have, so it ships with
its own modeling code and needs `trust_remote_code=True`:

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

mid = "Ternarycore/ternarycore-sst2-student"
tok = AutoTokenizer.from_pretrained(mid, trust_remote_code=True)
m = AutoModelForCausalLM.from_pretrained(
    mid, trust_remote_code=True, dtype=torch.bfloat16).eval()

ids = tok("Review: a gorgeous, witty, seductive movie.\nSentiment:",
          return_tensors="pt")
with torch.no_grad():
    logits = m(**ids).logits[0, -1]
print(tok.decode(logits.argmax()))   # " positive"
```

The `safetensors` hold the ternary values **already multiplied by their per-layer absmean
scale**, stored as bf16. Inference is therefore ordinary bf16 matmul, numerically
identical to the ternary datapath, and every projection tensor contains exactly three
distinct values:

```python
import numpy as np
w = m.model.layers[0].self_attn.q_proj.weight.detach().float().numpy()
np.unique(w)        # [-0.02478, 0.0, 0.02478]
(w == 0).mean()     # 0.3151
```

The genuinely 1.58-bit artifact - 2 bits per weight as the accelerator consumes it - is
under `hardware/` (see below).

## Results

| Task | Teacher | Ternary student | % of teacher |
|------|---------|-----------------|--------------|
| SST-2 (sentiment) | 94.4% | **91.4%** | 96.8% |

(A sibling MNLI student reached 82.8% vs an 88.2% teacher. This checkpoint is the
**SST-2** student.)

## Model details

- **Teacher / skeleton:** [`Qwen/Qwen3-0.6B`](https://huggingface.co/Qwen/Qwen3-0.6B)
  (Apache-2.0, 596M params). The student inherits the teacher’s **dimensions**, so it fits
  the accelerator by construction. It is not architecturally identical:
  BitNet-Distillation inserts a SubLN (RMSNorm) before `o_proj` and `down_proj` in every
  block - 56 extra tensors - which is why the custom modeling code is required.
- **Architecture:** decoder transformer, grouped-query attention (`q_proj` 2048x1024,
  `k_proj`/`v_proj` 1024x1024, `o_proj` 1024x2048) with a SwiGLU MLP
  (`gate_proj`/`up_proj` 3072x1024, `down_proj` 1024x3072).
- **Depth:** 28 blocks -> **196 weight-layer GEMMs**.
- **Hidden size:** 1024 - **MLP intermediate:** 3072 - **head dim:** 128 - 16 attention
  heads, 8 KV heads - **vocab:** 151,936 - tied embeddings.
- **Weight precision:** balanced ternary {-1, 0, +1} via BitLinear (absmean scale applied
  once after accumulation); **activations INT8** -> W1.58A8.
- **Total parameters:** 596.2M. The ternary GEMMs hold **440,545,280 weights** and pack to
  **110.1 MB** in the accelerator’s 2-bit format; **31.4% are exact zeros** (each a `skip`
  on the MAC array - the model learned roughly the sparsity the BitNet papers report).
  Embeddings, the tied LM head, SubLN and the normalization layers are not ternary and run
  in the activation domain.
- **Task:** SST-2 binary sentiment (positive / negative), framed generatively.

## `hardware/` - the packed format the FPGA consumes

- `layers/` - 196 per-projection blobs, `addr = k * GROUPS + g`, **4 codes per byte,
  LSB-first**, code map `00 -> 0`, `01 -> +1`, `10 -> -1`. One 1024x1024 layer packs to
  exactly 262,144 bytes.
- `manifest.json` - per-layer shape, absmean scale, zero fraction and file path.
- `reference.npz` - the same 196 projections as **int8 ternary matrices** (-1/0/+1), for
  checking a packer or an FPGA readback element by element.
- `weights.bin` + `pages.json` - the whole model pre-sliced into 420 pages of 256 KB in the
  order the block executor walks them, so the board can DMA by page index.

The bf16 `safetensors` were reconstructed *from* `layers/` and verified against
`reference.npz`: 196/196 projections match exactly, and every zero fraction matches
`manifest.json`.

## Intended use

- Reproducing the TernaryCore silicon and energy results.
- A compact, honestly-sized ternary checkpoint for research on multiplier-free / sub-watt
  LLM inference on reconfigurable hardware.
- An educational reference for BitNet b1.58 W1.58A8 arithmetic and the BitNet-distillation
  workflow at fine-tuning scale.

**Out of scope:** a task-specific SST-2 classifier, not a general chat/instruction model.
Do not use for open-ended generation or as a safety-sensitive classifier without
independent validation.

## How the arithmetic maps to hardware

| Ternary property | Hardware image |
|------------------|----------------|
| weight = 0       | **skip** (no accumulation) |
| weight = +1 / -1 | **add / subtract** |
| no sign bit      | **no multiplier** |

On the TernaryCore array a projection runs at one element/clock (64 MACs/cycle, 12.7 GOPS
at 100 MHz) using **zero DSP slices**. On the deployed Artix-7 SoC (DDR3 + Ethernet
active) one forward pass of this model’s 196 weight-layer GEMMs was measured at **~310 mJ
/ ~88 ms** by inline current sensing - the weight-layer portion only (attention scores,
softmax, normalization, embeddings, and the head are activation-domain and excluded).

## Provenance, license and attribution

- **Model weights:** released under **Apache-2.0**, following the teacher.
- **Teacher:** [`Qwen/Qwen3-0.6B`](https://huggingface.co/Qwen/Qwen3-0.6B) (Apache-2.0) -
  attribution retained per that license. The student was distilled to ternary from this
  teacher; it is not a Qwen release and carries no Qwen endorsement.
- **Method:** Microsoft BitNet Distillation,
  [arXiv:2510.13998](https://arxiv.org/abs/2510.13998).
- **Data:** GLUE **SST-2** (Socher et al., 2013), research-permissive terms.
- **Accelerator RTL/tooling** (separate repo) is licensed **CERN-OHL-S v2**; this license
  note covers the *model weights*, which are Apache-2.0.

## Citation

The accelerator this model was built for:

```bibtex
@software{ternarycore,
  title   = {TernaryCore: Multiplier-Free Balanced Ternary GEMM Accelerator for BitNet
             b1.58 Inference},
  author  = {Oladapo, Ifedayo and Vasilev, Dmitrii and Mohammed, Abubakar},
  year    = {2026},
  doi     = {10.5281/zenodo.22837568},
  url     = {https://github.com/Ternarycore/ternarycore},
  license = {CERN-OHL-S-2.0}
}
```

A manuscript describing the design, silicon validation and same-fabric comparison is in
preparation; this card will be updated with its citation once it is available.

## Limitations

Ternary quantization and distillation shift decision boundaries versus the full-precision
teacher (SST-2 lands at 96.8% of teacher accuracy; the sibling MNLI student missed its bar
by about 1 point). Validate on your own split before relying on it. The model inherits
biases of its teacher and of the SST-2 training data, and is English- and sentiment-only.
