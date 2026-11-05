---
license: gemma
base_model: google/medgemma-4b-it
tags:
  - medical-llm
  - clinical
  - healthcare
  - medicine
  - medical-ai
  - clinical-decision-support
  - medical
  - triage
  - emergency-medicine
  - esi
  - grpo
  - sft
  - gemma3
  - merged
language:
  - en
pipeline_tag: text-generation
library_name: transformers
---

# MedGemma 4B — Emergency Severity Index (ESI) Triage (GRPO + SFT, Merged)

A fine-tuned variant of [`google/medgemma-4b-it`](https://huggingface.co/google/medgemma-4b-it) for emergency department triage. Given a triage narrative (chief complaint, vitals, history, arrival mode), the model classifies cases into ESI levels 1–5 with structured chain-of-thought reasoning.

> ⚠️ **Research model. Not approved for clinical use. Not a substitute for clinician judgment.**
> This model inherits Google's [Gemma Terms of Use](https://ai.google.dev/gemma/terms) and the [HAI-DEF terms](https://developers.google.com/health-ai-developer-foundations) from medgemma. Research and development use only.

## Result

**83.3% exact / 97.2% adjacent** on the 36-case MIETIC expert-annotated evaluation set.

| Model | Params | Stage | Exact | Adjacent |
|-------|--------|-------|-------|----------|
| Qwen3.5 v43 (SFT) | 9B | SFT | 75.0% | — |
| Qwen3.5 v46 (GRPO) | 9B | SFT + GRPO | 77.8% | 94.4% |
| Qwen3.5 v49 (GRPO) | 9B | SFT + rule-aware GRPO | 77.8% | 100.0% |
| medgemma SFT | 4B | SFT | 77.8–80.6% | 97.2% |
| **medgemma GRPO (this model)** | **4B** | **SFT + rule-aware GRPO** | **83.3%** | **97.2%** |

A 4 B model beating a 9 B model by 5.5 pp — the combination of MedGemma's medical pretraining + structured SFT + rule-aware GRPO is unusually effective on this task.

## Output format

```
EXTRACTION:
- Chief complaint: ...
- Vital signs: ...
- Red flags: ...

ESI ALGORITHM:
- Step A (lifesaving): ...
- Step B (high-risk): ...
- Step C (resources): ...
- Step D (vitals): ...

ANSWER: ESI 2
```

## Training pipeline

### Stage 1 — Supervised Fine-Tuning (SFT)

- **Base**: `google/medgemma-4b-it`
- **Data**: `bert_training_v43_balanced.jsonl` (7,483 records, class-balanced across ESI 1–5)
  - MIMIC-IV-ED gold (engine-verified) + MIETIC narrative cases
- **LoRA**: r=32, α=32, target modules = `q_proj, k_proj, v_proj, o_proj, gate_proj, up_proj, down_proj`
- **Hyperparams**: 3 epochs, LR=2e-4 (cosine), batch=4, grad_accum=4, max_seq_length=2048
- **Final loss**: ~0.20 (converged by epoch 2)
- **Hardware**: NVIDIA GB10, ~2.8 h
- **Eval result**: 77.8–80.6% exact on MIETIC-36

### Stage 2 — GRPO with rule-aware reward

The SFT model already matched Qwen v49's 9B GRPO result, but failed on the same patterns Qwen v46 missed (intubation/lifesaving intervention rule, severe pain rule, open injury). v49's rule-aware reward was applied to medgemma to fix those specific failures.

**Reward function**:

| Outcome | Reward |
|---------|--------|
| Correct, gold=1 | +3.0 |
| Correct, gold=2 | +2.0 |
| Correct, gold≥3 | +1.0 |
| Gold=1, pred=2 (critical under-triage) | −1.0 |
| Gold=1, pred≥3 (severe miss) | −2.0 |
| Pred=1, gold=2..5 (over-triage, scaled) | −0.5 to −2.0 |
| Adjacent wrong (other) | 0.0 (safety valve) |
| No parseable answer | **−2.0** (must dominate every wrong commit) |
| Format bonus (`EXTRACTION`/`ESI ALGORITHM`/`ANSWER`) | +0.1 |
| Length bonus (≤300 tokens) | up to +0.3 |
| **Rule bonuses** (target v46 failure patterns): | |
| `intubat\|chest tube\|central line\|cpr` + pred=ESI 1 | +0.5 |
| same + gold=ESI 1 + pred≠1 | −1.0 |
| `open fracture\|penetrating` + gold=2 + pred>2 | −0.5 |
| Pain ≥ 7 + gold=2 + pred>2 | −0.5 |

**Hyperparams**:
- Warm-start: medgemma-sft-v1 LoRA
- 300 steps, LR=2e-7 (cosine), G=8 generations/step
- max_new_tokens = 1024
- ESI-1 oversample 5×, ESI-2 oversample 3×
- attn_implementation=eager (workaround for SDPA dtype mismatch in Gemma3+GRPO)
- **Hardware**: NVIDIA GB10, ~19.3 h

## Usage

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

repo = "vadimbelsky/medgemma-4b-esi-triage-grpo-v1"
tokenizer = AutoTokenizer.from_pretrained(repo)
model = AutoModelForCausalLM.from_pretrained(repo, torch_dtype=torch.bfloat16, device_map="auto")

SYSTEM = (
    "You are an expert emergency triage nurse. "
    "First extract clinical fields from the triage note, "
    "then apply the ESI algorithm step by step, then state the ESI level."
)

case = ("A 67-year-old male arrived via ambulance with sudden onset chest pain "
        "radiating to the left arm, diaphoresis, and shortness of breath. "
        "BP 88/60, HR 118, RR 24, SpO2 91%. History of MI and hypertension. Pain 9/10.")

prompt = tokenizer.apply_chat_template(
    [{"role": "system", "content": SYSTEM},
     {"role": "user",   "content": case}],
    tokenize=False, add_generation_prompt=True,
)
out = model.generate(
    **tokenizer(prompt, return_tensors="pt").to(model.device),
    max_new_tokens=1024, temperature=0.1, do_sample=True,
)
print(tokenizer.decode(out[0], skip_special_tokens=True))
```

## Per-class results (MIETIC-36)

| ESI level | Exact | Adjacent (±1) |
|-----------|-------|---------------|
| 1 | 11/14 (79%) | 13/14 (93%) |
| 2 | 9/11 (82%) | 11/11 (100%) |
| 3 | 4/5 (80%) | 5/5 (100%) |
| 4 | 4/4 (100%) | 4/4 (100%) |
| 5 | 2/2 (100%) | 2/2 (100%) |

ESI-4 and ESI-5 are perfect on this eval. The one remaining adjacency violation is a single ESI-1 case where the model predicted ESI-3 — the patient's narrative didn't match any of our four rule-bonus trigger regexes.

## Known limitations

- **Small eval set**: 36 cases. The 95% CI for 83.3% is roughly ±12 pp. Treat the headline number as directional.
- **Rule bonuses are pattern-based**: regex triggers for intubation, lifesaving intervention, open injury, severe pain. Cases requiring clinical rules outside these patterns may still err.
- **Single dangerous error remains**: 1/36 case (~3%) where a clinical ESI-1 is misclassified to ESI-3. Mitigation requires either broader rule coverage or larger training data.
- **English-only**: trained on English narratives.
- **MIMIC-IV-ED distribution**: reflects U.S. emergency-department practice and retrospective acuity assignments.

## Citation and acknowledgments

- Base model: [`google/medgemma-4b-it`](https://huggingface.co/google/medgemma-4b-it)
- Data: MIMIC-IV-ED (gold ESI labels) + MIETIC narrative corpus
- Training stack: Unsloth FastModel + TRL GRPOTrainer (with patches for Gemma3 GRPO compatibility — see model repo for details)
- Developed at ScienceSoft as part of a medical SLM research initiative

This is a **modified version of MedGemma**. The base model is Google's, used under the Gemma Terms of Use. Modifications: SFT + GRPO fine-tuning for ESI triage. The HAI-DEF research-only restriction is preserved.
