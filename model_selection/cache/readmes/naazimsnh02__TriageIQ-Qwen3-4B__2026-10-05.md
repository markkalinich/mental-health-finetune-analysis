---
license: apache-2.0
base_model: Qwen/Qwen3-4B-Instruct-2507
library_name: transformers
pipeline_tag: text-generation
language:
- en
tags:
- itsm
- service-desk
- ticket-triage
- structured-output
- json
- lora
- qwen3
- rocm
- amd-mi300x
---

# TriageIQ — Qwen3-4B Incident Triage

**TriageIQ** turns a free-text IT support complaint into a single structured,
schema-valid JSON incident record. It is the fast-path model behind the
TriageIQ predictive complaint-triage & SLA-aware routing engine, fine-tuned on
the **AMD Instinct MI300X**.

This is `Qwen/Qwen3-4B-Instruct-2507` with a bf16 LoRA fine-tune **merged into
the base weights** — load it like any standard causal LM; no PEFT required at
inference time.

## What it does

Given a complaint, the model emits **exactly** this JSON object and nothing else:

```json
{
  "summary": "One-line normalized incident title",
  "category": "Software | Hardware | Network | Access",
  "urgency": 1,
  "impact": 1,
  "assignment_group": "IT Support | Network Ops",
  "suggested_first_action": "Concrete first remediation step",
  "confidence": 0.0
}
```

- `urgency` / `impact`: integers `1 = High, 2 = Medium, 3 = Low`.
- `confidence`: float in `[0.0, 1.0]`.

> **Design note — priority and SLA are *not* model outputs.** Priority (P1–P5)
> and the SLA target are computed deterministically downstream from
> `(impact, urgency)` via the ITSM matrix, and the dynamic SLA-breach-risk is a
> separate explainable engine. The model is deliberately kept to the perception
> step (text → structured record) so the business logic stays auditable.

## Intended use

- Automated first-pass triage of IT service-desk tickets into structured records.
- Feeding a deterministic routing / SLA engine that consumes the JSON contract.
- Demo / research within the TriageIQ project (AMD Hackathon — Customer Complaint
  Classification & Routing Engine track).

**Not intended for** medical, legal, or safety-critical decisions, or as the sole
authority for ticket prioritization without the downstream deterministic engine.

## Usage

The model was trained with a fixed system prompt; use it verbatim for best results.

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "naazimsnh02/TriageIQ-Qwen3-4B"
tok = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype=torch.bfloat16, device_map="auto")

SYSTEM_PROMPT = (
    "You are TriageIQ, an IT service-desk triage assistant. Convert the user's "
    "complaint into a single JSON object with EXACTLY these keys: summary, "
    "category, urgency, impact, assignment_group, suggested_first_action, "
    "confidence. "
    "category is one of [Software, Hardware, Network, Access]. "
    "assignment_group is one of [IT Support, Network Ops]. "
    "urgency and impact are integers 1=High, 2=Medium, 3=Low. "
    "confidence is a float 0.0-1.0. "
    "Do NOT include priority or SLA — those are computed elsewhere. "
    "Output ONLY the JSON object, no prose, no code fences."
)

complaint = "My laptop won't connect to the office Wi-Fi since this morning and I have a client call in 20 minutes."
messages = [
    {"role": "system", "content": SYSTEM_PROMPT},
    {"role": "user", "content": complaint},
]
prompt = tok.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
inputs = tok(prompt, return_tensors="pt").to(model.device)
out = model.generate(**inputs, max_new_tokens=256, do_sample=False)
print(tok.decode(out[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True))
```

Serving with vLLM (ROCm or CUDA):

```bash
vllm serve naazimsnh02/TriageIQ-Qwen3-4B
```

## Evaluation

Held-out validation set of **75** complaints, greedy decoding, scored with the
project's `TriageRecord` schema validator (the same contract enforced in
production). Field metrics are computed over schema-valid outputs.

| Metric | Base (Qwen3-4B-Instruct) | **TriageIQ (fine-tuned)** |
|---|---|---|
| Schema-valid rate | 100.0% | **100.0%** |
| Category accuracy | 86.7% | **97.3%** (+10.7) |
| Assignment-group agreement | 90.7% | **96.0%** (+5.3) |
| Impact agreement | 100.0% | **100.0%** |
| Urgency agreement | 65.3% | 61.3% |

The fine-tune's headline gain is **category accuracy (+10.7 pts)** and routing
accuracy (**assignment-group +5.3 pts**) while preserving a 100% schema-valid
rate. Urgency — the most subjective field — moves within label noise (a few
cases on 75); it is also the field whose downstream effect is bounded by the
deterministic priority matrix rather than the model alone.

## Training

| | |
|---|---|
| Base model | `Qwen/Qwen3-4B-Instruct-2507` |
| Method | LoRA (merged), **bf16** — no 4-bit / QLoRA |
| LoRA config | `r=32, alpha=64, dropout=0.05`, targets: `q,k,v,o,gate,up,down` proj |
| Objective | Causal LM, **completion-only loss** (prompt masked) |
| Epochs / seq len | 3 / 1024 |
| Optimizer / LR | AdamW, `2e-4`, cosine schedule, 3% warmup, effective batch 16 |
| Framework | TRL `SFTTrainer` + PEFT + Transformers |
| Hardware | **AMD Instinct MI300X** (gfx942, 192 GB), ROCm, PyTorch 2.8 |

bf16 LoRA was chosen deliberately: on ROCm, bitsandbytes ≤ 0.49.2 has a 4-bit
decode NaN bug, and the MI300X's 192 GB removes any need for quantization on a
4B model — one card co-hosts the fine-tuned model and the live streaming
pipeline without quantization juggling.

## Training data

~432 synthetic English IT complaints (357 train / 75 validation). Built from the
~100 unique realistic descriptions in
[`6StringNinja/synthetic-servicenow-incidents`](https://huggingface.co/datasets/6StringNinja/synthetic-servicenow-incidents)
used **as seeds only** (the raw set has independently shuffled fields and is not
trained on directly). Seeds were relabeled coherently against a fixed ITSM rubric
by a `Qwen2.5-32B-Instruct` teacher and paraphrase-augmented for phrasing/persona
diversity, with an 85/15 split stratified by category and de-leaked at the seed
level. Labels never include priority or SLA.

## Limitations & biases

- Trained on synthetic, English-only, single-paragraph complaints; behavior on
  long threads, multi-language, or out-of-distribution domains is unverified.
- Two assignment groups (`IT Support`, `Network Ops`) and four categories only —
  it will coerce inputs into this taxonomy.
- `urgency` is subjective and the weakest field; downstream the deterministic
  priority matrix bounds its impact.
- Confidence is a learned self-report, not a calibrated probability.
- For robustness the production pipeline validates every output against the
  schema and falls back to a deterministic rule tagger on invalid JSON — do the
  same when integrating.

## License

Apache-2.0, inherited from the `Qwen/Qwen3-4B-Instruct-2507` base model.
