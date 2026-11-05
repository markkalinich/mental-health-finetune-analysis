---
library_name: transformers
base_model: nvidia/NVIDIA-Nemotron-3-Nano-4B-BF16
tags:
  - safety
  - content-moderation
  - nemotron
  - rai
  - responsible-ai
  - dora
  - dpo
license: apache-2.0
---

# RAI Safety Classifier M3 — Nemotron 3 Nano 4B (Merged)

Enterprise content safety classifier achieving **0.150% Block Rate** and **100% Precision** (0 false positives) across 13 risk categories.

## Performance

### v14 Hello (5,835 benign enterprise queries)

| Template | Block Rate (FPR) | False Positives |
|----------|-----------------|-----------------|
| **VerdictReason** | **0.150%** (9 / 5,835) | 9 |
| CategoryOnly | 0.550% (32 / 5,835) | 32 |

### v200+ Balanced (2,061 samples: 1,061 violations + 1,000 benign)

| Template | Precision | Recall | F1 | FP |
|----------|-----------|--------|-----|-----|
| **VerdictReason** | **1.0000** (0 FP) | 0.1621 (172/1061) | 0.2790 | **0** |
| CategoryOnly | 0.9881 | 0.2347 | 0.3791 | 3 |

### Original v200 (2,000 samples: 1,000 violations + 1,000 benign)

| Template | Precision | Recall | F1 | FP |
|----------|-----------|--------|-----|-----|
| **VerdictReason** | **1.0000** (0 FP) | 0.1710 (171/1000) | 0.2924 | **0** |
| CategoryOnly | 0.9880 | 0.2470 | 0.3954 | 3 |

## Training Recipe

**3-stage pipeline on Nemotron 3 Nano 4B:**

### Stage 1: DoRA SFT (L4 base)
- **Architecture**: DoRA LoRA (r=36, alpha=72, all target modules)
- **Data**: ~21K rows from 12 source files:
  - Base: v1.6.0 (9,657) + v1.6b (604) + v1.6c (2,000×2) + v1.6d (1,660) + v1.6e (2,000) + v1.6e2 (2,000)
  - FP-correction: v1_6e7_FPonly (1,005) + v1_6g_fpfix (300) + v1_6h_ip_fix (100) + v1_6i_edu_style_fix (170) + v1_6j_pers_tag_fix (80)
- **Hyperparameters**: 1 epoch, lr=1e-4, batch=4, GA=16, cosine warmup, bf16

### Stage 2: Recall-boosting DPO (2 epochs)
- **Data**: 500 preference pairs — violation label as "chosen", "none" as "rejected"
- **Hyperparameters**: beta=0.1, lr=5e-7, 2 epochs, batch=2, GA=8

### Key Data Innovations
- `v1_6i_edu_style_fix.jsonl` (170 rows): Fixes FPs on educational-about-harm queries and style/tone instructions
- `v1_6j_pers_tag_fix.jsonl` (80 rows): Fixes FPs triggered by `[PERS-XXXX]` synthetic metadata tags in queries
- `v1_6k_recall_boost_dpo.jsonl` (500 rows): DPO pairs teaching the model to correctly flag violations instead of defaulting to "none"

## Quick Start

### Serving with vLLM

```bash
python -m vllm.entrypoints.openai.api_server \
  --model tzchen07/rai-n3-nano-4b-safety-m3-fullfix-recall \
  --served-model-name rai-classifier \
  --port 8180 \
  --max-model-len 8192 \
  --gpu-memory-utilization 0.85 \
  --trust-remote-code \
  --dtype bfloat16
```

**Note**: Requires `mamba-ssm` package (hybrid Mamba-Transformer architecture).

### Inference with Stop Token

When using the **VerdictReason** template, set `stop=["Reason:"]` to extract only the verdict and skip reason generation. This is recommended for production use:

```python
from openai import OpenAI

client = OpenAI(base_url="http://localhost:8180/v1", api_key="unused")

resp = client.chat.completions.create(
    model="rai-classifier",
    messages=[
        {"role": "system", "content": "<v3.1 safety policy>"},
        {"role": "user", "content": query},
    ],
    max_tokens=50,
    temperature=0.0,
    stop=["Reason:"],
    extra_body={"chat_template_kwargs": {"enable_thinking": False}},
)

verdict = resp.choices[0].message.content.strip()
# Returns e.g. "Verdict: none" or "Verdict: Violence/Harassment"
```

**Benefits of using `stop=["Reason:"]`**:
- **Faster inference**: Generates ~5-10 tokens instead of 200-400, significantly reducing latency
- **Cleaner output**: Avoids degenerate repetition observed in some reason text
- **Same accuracy**: The classification decision is fully determined before the reason is generated
- **Lower cost**: Reduces output token usage by ~95%

### Evaluation

```bash
# Run inference (enable_thinking=False is critical for N3)
python eval_n3_raw_v14_VR.py \
  --data v14_eval.jsonl \
  --prompt v3_1_VerdictReason.jinja \
  --out predictions.jsonl \
  --api-base http://localhost:8180/v1 \
  --model rai-classifier \
  --max-tokens 400 --concurrency 16

# CRITICAL: Sort by row_id before scoring (concurrent workers write out-of-order)
python score_aligned.py predictions.jsonl

# Score
python binary_metrics_v2.py predictions.jsonl.sorted --gt-source-jsonl v14_eval.jsonl
```

## Campaign Context

This model was produced during an extensive RAI training campaign (iter10-iter11, ~80+ experiments) exploring:
- **LoRA rank**: r=32-96 (r=35-36 optimal for N3)
- **DoRA vs standard LoRA**: DoRA gives ~2pp precision improvement
- **Data mix**: FP-correction data is critical; IP-fix, edu/style-fix, PERS-tag-fix each eliminated specific FP patterns
- **DPO**: FP-fix DPO helps precision; recall-boosting DPO (violation-chosen, none-rejected) helps recall
- **Templates**: VerdictReason gives higher recall + precision but higher Block%; CategoryOnly gives lower Block%

### Sibling Models from Same Campaign

| Model | Block% | P | R | FP | Recipe |
|-------|--------|------|------|-----|--------|
| **M3 (this)** | **0.150%** | **100%** | 17.1% | **0** | L4 + recall DPO 2ep |
| L7 | 0.220% | 100% | 22.5% | 0 | r=35 fullfix 1.5ep |
| K3 | 0.170% | 100% | 16.7% | 0 | r=35 fullfix |
| M5 | 0.210% | 99.51% | 19.2% | 1 | K3 + recall DPO |

*Metrics above use augmented v200+ (2,061 rows) with pure-benign v14 (5,835 rows).*

## Related Repos

- [rai-n3-nano-4b-safety-lora-r64-ipfix](https://huggingface.co/tzchen07/rai-n3-nano-4b-safety-lora-r64-ipfix) — iter10 LoRA adapter + all training/eval scripts
- [rai-n3-nano-4b-safety-merged-ipfix](https://huggingface.co/tzchen07/rai-n3-nano-4b-safety-merged-ipfix) — iter10 merged model

## Limitations

- **Moderate recall**: Catches ~17% of violations (VR template). Deliberate trade-off for zero false positives.
- **N3-specific**: Requires `mamba-ssm` package. Not compatible with standard Transformer-only vLLM builds.
- **Template-dependent**: Performance varies significantly between CategoryOnly and VerdictReason templates.

## Citation

```
@misc{rai-n3-safety-m3-2026,
  title={RAI Safety Classifier M3: Nemotron 3 Nano 4B},
  author={Tony Chen},
  year={2026},
  publisher={HuggingFace},
  url={https://huggingface.co/tzchen07/rai-n3-nano-4b-safety-m3-fullfix-recall}
}
```
