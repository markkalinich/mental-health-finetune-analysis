---
library_name: transformers
base_model: google/gemma-4-E2B-it
tags:
  - safety
  - content-moderation
  - gemma
  - rai
  - responsible-ai
  - dora
license: apache-2.0
---

# RAI Safety Classifier — Gemma 4 E2B 5B (Merged)

Campaign-winning enterprise content safety classifier that **hits all three targets**: **0.050% Block Rate**, **100% Precision** (0 false positives), and **22.7% Recall** across 13 risk categories. The first model to achieve the triple target from a 130+ experiment training campaign.

## Performance

### v14 Hello (5,835 benign enterprise queries)

| Template | Block Rate (FPR) | False Positives |
|----------|-----------------|-----------------|
| **VerdictReason** | **0.050%** (3 / 5,896) | 3 |
| CategoryOnly | 0.390% (23 / 5,896) | 23 |

### v200 Balanced (2,000 samples: 1,000 violations + 1,000 benign)

| Template | Precision | Recall | F1 | FP |
|----------|-----------|--------|-----|-----|
| **VerdictReason** | **1.0000** (0 FP) | **0.2270** (227/1000) | 0.3702 | **0** |
| CategoryOnly | 0.9412 | 0.2560 | 0.4023 | 16 |

### Triple Target Achievement

| Target | Value | Status |
|--------|-------|--------|
| Block Rate <= 0.200% | **0.050%** | **HIT** |
| Precision >= 99.5% | **100%** | **HIT** |
| Recall >= 20% | **22.7%** | **HIT** |

## Training Recipe

**Single-stage DoRA SFT:**

- **Base model**: `google/gemma-4-E2B-it` (5.2B params, multimodal Transformer)
- **LoRA**: DoRA (Weight-Decomposed), r=64, alpha=128, all target modules
- **Epochs**: 1
- **Learning rate**: 1e-4, cosine with 5% warmup
- **Batch**: 4 per device, gradient accumulation 16 (effective batch 64)
- **Precision**: bf16
- **Target modules**: `q_proj`, `k_proj`, `v_proj`, `o_proj`, `gate_proj`, `up_proj`, `down_proj` (in `model.language_model.layers`)

### Training Data (19,576 rows from 11 files)

| Dataset | Rows | Purpose |
|---------|------|---------|
| v1.6.0_train.jsonl | 9,657 | Base safety classification (Aegis 2.0, HH-RLHF, Dolly, OASST1) |
| v1.6b_train.jsonl | 604 | Supplementary paraphrase/corrections |
| v1.6c_train.jsonl | 2,000 | Violation-heavy supplementary |
| v1.6d_train.jsonl | 1,660 | Balanced supplementary |
| v1.6e_train.jsonl | 2,000 | Violence/Harassment focused |
| v1.6e2_train.jsonl | 2,000 | Misinformation/Illegal/IP focused |
| v1_6e7_FPonly.jsonl | 1,005 | Real FP corrections (all benign) |
| v1_6g_fpfix.jsonl | 300 | Synthetic FP-fix (HR, jailbreak edu, software verbs) |
| v1_6h_ip_fix.jsonl | 100 | IP-specific FP correction (slides, orders, licenses) |
| v1_6i_edu_style_fix.jsonl | 170 | Educational-about-harm + style/tone FP fix |
| v1_6j_pers_tag_fix.jsonl | 80 | [PERS-XXXX] metadata tag FP fix |

### What Made It Work

Three factors combined to achieve the triple target:

1. **Learning rate 1e-4** (vs previous G4 default of 5e-6): The 20x increase allowed the LoRA adapter to actually override Gemma 4's pre-trained safety behavior and learn our 13-category policy
2. **DoRA** (Weight-Decomposed LoRA): Improved precision from 99.34% (standard LoRA) to 100% by decoupling weight magnitude and direction updates
3. **Fullfix training data**: 4 rounds of targeted FP-correction data (IP, educational, style, PERS-tag patterns) developed across 120+ experiments on Nemotron 3 Nano transferred perfectly to Gemma 4

## Quick Start

### Serving with vLLM

```bash
python -m vllm.entrypoints.openai.api_server \
  --model tzchen07/rai-gemma4-e2b-5b-safety-dora-r64-fullfix \
  --served-model-name rai-classifier \
  --port 8180 \
  --max-model-len 8192 \
  --gpu-memory-utilization 0.85 \
  --trust-remote-code \
  --dtype bfloat16
```

**Note**: Requires vLLM >= 0.22.1 for Gemma 4 support. The merged model includes k_norm weight patching required for vLLM serving.

### Inference (Verified Input/Output Format)

**IMPORTANT**: `stop=["Reason:"]` is **required** for production use. Without it, the model degenerates into repeated Verdict/Reason loops.

```python
from openai import OpenAI

client = OpenAI(base_url="http://localhost:8180/v1", api_key="unused")

# Input format: system = v3.1 policy, user = {'request': '<query>'}
resp = client.chat.completions.create(
    model="rai-classifier",
    messages=[
        {"role": "system", "content": "<v3.1 safety policy>"},
        {"role": "user", "content": "{'request': 'How many story points did our team complete?'}"},
    ],
    max_tokens=50,
    temperature=0.0,
    stop=["Reason:"],  # REQUIRED — prevents degenerate repetition
)

verdict = resp.choices[0].message.content.strip()
# Returns: "Verdict: none" or "Verdict: Self-harm" etc.
```

**Verified output examples:**
```
Benign query  → "Verdict: none"               (finish_reason: stop)
Self-harm     → "Verdict: Self-harm"           (finish_reason: stop)
Hate speech   → "Verdict: Hate/Discrimination" (finish_reason: stop)
```

**Why `stop=["Reason:"]` is required:**
- Without it, the model repeats the Verdict/Reason pattern in a loop
- Subsequent iterations may flip correct violations to "none"
- The stop token cleanly extracts just the verdict line (~5 tokens vs 400)
- Classification accuracy is identical — the verdict is determined before the reason

## Campaign Context

This model was the breakthrough result from a 130+ experiment campaign across two model families:

### Nemotron 3 Nano 4B (120+ experiments, iter10-iter11)
- Best: L7 — B=0.220%, P=100%, R=22.5% (missed Block% by 0.02pp)
- Hit the Pareto frontier — every technique exhausted (DoRA, DPO, epoch tuning, adapter interpolation, logprob thresholding, prompt engineering)

### Gemma 4 E2B 5B (8 experiments, iter12)
- **G4-B (this model)** — B=0.050%, P=100%, R=22.7% — **ALL THREE TARGETS HIT**
- The larger model (5B vs 4B) + correct learning rate + DoRA broke through the wall

### Sibling G4 Models

| Model | DoRA | r | Block% | P | R | FP | Targets |
|-------|------|---|--------|------|------|-----|---------|
| **G4-B (this)** | **Yes** | **64** | **0.050%** | **100%** | **22.7%** | **0** | **ALL 3** |
| G4-C | Yes | 32 | 0.150% | 99.59% | 24.5% | 1 | ALL 3 |
| G4-D | No | 64 | 0.000% | 99.34% | 30.3% | 2 | B,R |
| G4-A | Yes | 32 | 0.140% | 98.25% | 22.5% | 4 | B,R |

## Related Repos

- [rai-n3-nano-4b-safety-l7-fullfix-15ep](https://huggingface.co/tzchen07/rai-n3-nano-4b-safety-l7-fullfix-15ep) — Best N3 model (B=0.220%, P=100%, R=22.5%)
- [rai-n3-nano-4b-safety-m3-fullfix-recall](https://huggingface.co/tzchen07/rai-n3-nano-4b-safety-m3-fullfix-recall) — N3 lowest Block Rate (0.150%)
- [rai-n3-nano-4b-safety-lora-r64-ipfix](https://huggingface.co/tzchen07/rai-n3-nano-4b-safety-lora-r64-ipfix) — All training/eval scripts and prompts

## Limitations

- **Moderate recall**: Catches 22.7% of violations. Trade-off for zero false positives.
- **Requires vLLM >= 0.22.1**: Older vLLM versions don't support Gemma 4.
- **k_norm patched**: The merged model includes injected k_norm weights required for vLLM. Do not re-merge from the adapter without applying k_norm patching.
- **Template-dependent**: VerdictReason gives best combined metrics; CategoryOnly gives lower recall but similar Block%.

## Citation

```
@misc{rai-g4-safety-2026,
  title={RAI Safety Classifier: Gemma 4 E2B 5B — Triple Target Achievement},
  author={Tony Chen},
  year={2026},
  publisher={HuggingFace},
  url={https://huggingface.co/tzchen07/rai-gemma4-e2b-5b-safety-dora-r64-fullfix}
}
```
