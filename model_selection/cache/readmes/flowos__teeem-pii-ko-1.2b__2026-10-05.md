---
license: other
license_name: exaone-ai-license
license_link: https://huggingface.co/LGAI-EXAONE/EXAONE-4.0-1.2B/blob/main/LICENSE
language:
- ko
base_model: LGAI-EXAONE/EXAONE-4.0-1.2B
tags:
- pii
- privacy
- korean
- ner
- token-classification
- exaone
- lora
- Teeem
pipeline_tag: text-generation
library_name: transformers
---

# Teeem-pii-ko-1.2b

> **Korean enterprise PII detection** — fine-tuned EXAONE 4.0 1.2B with a regex layer in front for structured types. Built and used in production by [Teeem.ai.kr](https://Teeem.ai.kr).

**Final score on the 230-prompt eval (hybrid pipeline):**

| Metric    | Value |
|-----------|-------|
| Precision | **0.928** |
| Recall    | **0.931** |
| **F1**    | **0.930** |
| Pass rate | **0.800** |

9 of 12 PII types are at **F1 = 1.000** in the hybrid pipeline.

## What this is

A two-stage Korean PII detection system designed to be **dropped in front of an LLM** so you can mask sensitive data before it leaves your perimeter and unmask it on the way back:

```
user text  →  [regex layer]  →  [EXAONE LoRA]  →  merge  →  masked text  →  upstream LLM
                                                                  ↓
                                                              mappings
                                                                  ↓
upstream response  ←  unmask  ←  [reverse mappings]
```

The split is deliberate. **Structured PII is a regex problem** — phone numbers, RRNs, business registration numbers, account numbers, emails, cards. The ML model is reserved for what regex cannot do reliably: Korean person names, free-form addresses, and organization names. This is the same architecture used by AWS Comprehend, GCP DLP, and Microsoft Presidio.

## Per-type performance (hybrid, 230-prompt eval)

| Type             | P     | R     | F1    | Source |
|------------------|-------|-------|-------|--------|
| ACCOUNT          | 1.000 | 1.000 | 1.000 | regex  |
| BRN              | 1.000 | 1.000 | 1.000 | regex  |
| EMAIL            | 1.000 | 1.000 | 1.000 | regex  |
| HEALTH_INSURANCE | 1.000 | 1.000 | 1.000 | regex  |
| LICENSE          | 1.000 | 1.000 | 1.000 | regex  |
| PASSPORT         | 1.000 | 1.000 | 1.000 | regex  |
| PHONE            | 1.000 | 1.000 | 1.000 | regex  |
| RRN              | 1.000 | 1.000 | 1.000 | regex  |
| CARD             | 0.882 | 1.000 | 0.938 | regex  |
| NAME             | 0.899 | 0.973 | 0.934 | ML     |
| ORGANIZATION     | 0.885 | 0.857 | 0.871 | ML     |
| ADDRESS          | 0.719 | 0.622 | 0.667 | ML     |

ADDRESS is the weakest type — it's the only category where the model has to do free-form span identification with no structural anchor. Future iterations should target it with a dedicated address gazetteer or a separate ADDRESS-only adapter.

## Repo contents

```
Teeem-pii-ko-1.2b/
├── config.json              # EXAONE 4.0 1.2B config
├── generation_config.json
├── model.safetensors        # 2.4 GB merged weights (LoRA folded in)
├── tokenizer.json
├── tokenizer_config.json
├── chat_template.jinja      # EXAONE 4 chat template
├── regex_layer.py           # Python regex layer (for hybrid pipeline)
├── hybrid_pipeline.py       # Reference Python implementation
├── patterns_typescript/     # TS regex patterns (Teeem gateway version)
└── README.md
```

## Quick start (Python, hybrid pipeline)

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
from regex_layer import detect_regex, merge_with_ml
import json, re

MODEL = "FlowOS2026/Teeem-pii-ko-1.2b"
tok = AutoTokenizer.from_pretrained(MODEL, trust_remote_code=True)
mdl = AutoModelForCausalLM.from_pretrained(MODEL, trust_remote_code=True, torch_dtype="auto", device_map="auto")

SYSTEM = ("You are a Korean PII detection model. Return a JSON array of detected PII "
          "entities with type, value, start, end. Types: NAME, PHONE, ADDRESS, RRN, "
          "CARD, BRN, PASSPORT, LICENSE, HEALTH_INSURANCE, ACCOUNT, ORGANIZATION, EMAIL.")

def detect_pii(text: str):
    # 1. Regex first (deterministic, high precision)
    regex_hits = detect_regex(text)

    # 2. ML for the unstructured types
    prompt = f"[|system|]{SYSTEM}[|endofturn|][|user|]{text}[|endofturn|][|assistant|]"
    inputs = tok(prompt, return_tensors="pt").to(mdl.device)
    out = mdl.generate(**inputs, max_new_tokens=512, temperature=0, do_sample=False)
    raw = tok.decode(out[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True)
    ml_hits = []
    m = re.search(r"\[[\s\S]*\]", raw)
    if m:
        try:
            ml_hits = json.loads(m.group(0))
        except Exception:
            pass

    # 3. Merge — regex priority on structured types, drop hallucinated types
    return merge_with_ml(regex_hits, ml_hits)

print(detect_pii("홍길동 고객님 010-1234-5678 카카오뱅크 3333-12-3456789"))
```

## Quick start (vLLM serving)

```bash
# vLLM 0.6+ supports EXAONE 4.0 natively
pip install "vllm>=0.6.0"

vllm serve FlowOS2026/Teeem-pii-ko-1.2b \
    --port 8091 \
    --max-model-len 8192 \
    --served-model-name exaone-pii \
    --trust-remote-code

# Then call /v1/completions or /v1/chat/completions
```

For the **production gateway** (with the regex layer wired in front, mask/unmask, session-scoped mappings, optional AES-256-GCM encryption), use the Teeem PII Gateway: `packages/pii-gateway/` in the [Teeem](https://Teeem.ai.kr) monorepo. The TypeScript regex implementation is mirrored here in `patterns_typescript/`.

## Self-hosted deployment recipe

The reference deployment runs on AWS ECS with a g4dn.2xlarge GPU host. You can replicate this anywhere with a 16+ GB GPU.

**Container layout (two-container task):**

1. `exaone-vllm` — vLLM 0.6+ serving the model on `localhost:8091`
2. `gateway-proxy` — Node.js process running the regex layer + EXAONE client + mask/unmask pipeline, listening on `:8090`, forwarding to upstream LLM

**Cold-start time:** ~3-4 minutes (most of which is downloading the 2.4 GB safetensors). Use a persistent volume / cache directory if you spin the service up and down often.

**Spin up / spin down (ECS example):**

```bash
REGION=ap-northeast-2
CLUSTER=Teeem-platform
SERVICE=Teeem-pii-gateway

# Spin up
aws ecs update-service --region $REGION --cluster $CLUSTER \
    --service $SERVICE --desired-count 1
# Also scale the EC2 capacity provider ASG up
aws autoscaling update-auto-scaling-group --region $REGION \
    --auto-scaling-group-name Teeem-pii-gateway-asg \
    --min-size 1 --desired-capacity 1

# Spin down
aws ecs update-service --region $REGION --cluster $CLUSTER \
    --service $SERVICE --desired-count 0
aws autoscaling update-auto-scaling-group --region $REGION \
    --auto-scaling-group-name Teeem-pii-gateway-asg \
    --min-size 0 --desired-capacity 0

# Force a redeploy (after updating the model weights)
aws ecs update-service --region $REGION --cluster $CLUSTER \
    --service $SERVICE --force-new-deployment
```

## Training

**Base model:** `LGAI-EXAONE/EXAONE-4.0-1.2B`
**Method:** LoRA (PEFT) — `r=32`, `alpha=64`
**Target modules:** `q_proj, k_proj, v_proj, o_proj, gate_proj, up_proj, down_proj`
**Hardware:** AWS `g6e.xlarge` (NVIDIA L40S 48 GB), bf16
**Optimizer:** `adamw_torch_fused`, lr `8e-5`, batch 4 × grad_accum 2
**Steps per iteration:** 400
**Total iterations:** 14

Each iteration: generate fresh augmentation (`generate_aug.py`) → train on aug + replay buffer → merge LoRA → eval → analyze failures → adjust templates → repeat.

The full training data, replay buffer, scripts, and per-iteration metrics live in the project's S3 bucket — they are **not** in this HF repo because they contain templated synthetic Korean PII.

## Iteration history (highlights)

| Iter | F1 (orig 30) | F1 (230) | Notes |
|------|--------------|----------|-------|
| baseline (raw EXAONE) | ~0.50 | — | No fine-tuning, hallucinates types |
| iter 5  | 0.84 | — | r=16 LoRA, ACCOUNT stuck at 0/3 |
| iter 6  | 0.86 | — | r=32 + MLP targets, ACCOUNT 1/3 |
| iter 7  | 0.87 | — | 3/3 on orig 30 — first ACCOUNT win |
| iter 8  | — | 0.84 | Expanded bank vocab, ACCOUNT 27/37 |
| iter 11 | — | 0.845 | L40S bf16, batch 32 — over-eager EMAIL |
| iter 12 | — | 0.69 | Disaster: trained from raw HF base, regression on fundamentals |
| iter 13 | 0.93 | 0.85 (raw) / 0.926 (hybrid) | Clean reset; **regex layer added** |
| **iter 14** | **0.969** | **0.930 (hybrid)** | ADDRESS-focused refinement; final |

## The "stuck ACCOUNT" story

For five iterations, ACCOUNT recall sat at 0/3 on the original 30-prompt eval. We thought it was a vocabulary problem, then a regex-vs-NN problem, then a context problem. None of those explained it. The actual cause was **LoRA capacity** — `r=16` with attention-only target modules wasn't enough to learn the digit-pattern → ACCOUNT mapping for novel bank names. Bumping to `r=32` and adding the MLP target modules (`gate_proj, up_proj, down_proj`) unlocked it in one iteration.

The lesson: when a single PII type is stuck while everything else trains fine, **don't add more training data** — first check whether your adapter has enough capacity to represent the pattern at all.

## The "regex breakthrough"

After iter 11, the model was plateauing around F1 ≈ 0.87 on the 230-prompt eval. Each iteration overfit a slightly different bank vocabulary or phone format. We wired in a regex layer purely as a defensive measure — and ACCOUNT recall jumped from 0.703 (26/37) to **1.000 (37/37)** in a single rescore, with **zero false positives**. EMAIL went from 34/42 to 42/42 the same way.

The lesson: this is a **hybrid problem**, not an ML problem. The structured types didn't need a smarter model; they needed to not be the model's responsibility.

## License

This model is a fine-tune of `LGAI-EXAONE/EXAONE-4.0-1.2B` and inherits the **EXAONE AI License**. Read it carefully before using commercially: https://huggingface.co/LGAI-EXAONE/EXAONE-4.0-1.2B/blob/main/LICENSE

The Teeem additions (regex layer, training scripts, gateway code) are released under the same license to keep the package self-consistent.

## Citation

```
@misc{Teeem_pii_ko_1.2b_2026,
    title  = {Teeem-pii-ko-1.2b: Korean Enterprise PII Detection via Hybrid Regex + Fine-tuned EXAONE 4.0},
    author = {Teeem / FlowOS},
    year   = {2026},
    url    = {https://huggingface.co/FlowOS2026/Teeem-pii-ko-1.2b}
}
```

## Maintainer

[Teeem.ai.kr](https://Teeem.ai.kr) — Korean enterprise AI agent platform by FlowOS.
