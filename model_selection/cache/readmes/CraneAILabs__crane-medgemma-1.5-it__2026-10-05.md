---
language:
  - en
license: other
license_name: medgemma-terms
license_link: https://huggingface.co/google/medgemma-1.5-4b-it
library_name: transformers
tags:
  - medical
  - clinical-decision-support
  - gemma3
  - dpo
  - uganda-clinical-guidelines
  - bf16
  - safetensors
base_model: google/medgemma-1.5-4b-it
pipeline_tag: text-generation
---

# Crane MedGemma 1.5 IT

A clinical decision-support model fine-tuned from [MedGemma 1.5 4B-IT](https://huggingface.co/google/medgemma-1.5-4b-it) on the Uganda Clinical Guidelines 2023, with Direct Preference Optimization (DPO) for improved format compliance and triage safety.

This is the **primary production checkpoint** — best overall performance across format compliance, triage safety, and clinical content quality. For the conservative SFT-only checkpoint, see [v2.1-instruct-medgemma-bf16](https://huggingface.co/CraneAILabs/v2.1-instruct-medgemma-bf16).

> **This model is a clinical thinking aid. It does not provide diagnoses, prescriptions, or automated clinical decisions.**

## Intended Use

**Primary use case**: Structured triage assessment for frontline health workers at Health Centre II–IV facilities in Uganda. Designed for the production Android app where compact XML output is parsed for clinical decision support at the point of care.

**Output formats**: XML, positional array, and prose — selected via system prompt. XML is the primary production format (~50% fewer tokens than prose, optimized for on-device latency).

**Deployment target**: On-device inference on Android via quantized GGUF. This bf16 checkpoint is the full-precision reference.

### In-Scope

- Structured triage assessments with triage level, condition, confidence, suggestions, next steps, and red flags
- Differential diagnosis reasoning for conditions in the Uganda Clinical Guidelines
- Danger sign identification and referral triage
- Investigation recommendations
- Format-switching between XML, array, and prose based on system prompt
- Refusal of out-of-scope queries (treatment, dosing)

### Out-of-Scope

- **Treatment and dosing recommendations** — the model refuses these queries by design
- Diagnostic conclusions or prescriptions
- Multi-turn conversations
- Languages other than English
- Conditions not covered by the Uganda Clinical Guidelines 2023

## Model Details

| | |
|---|---|
| **Base model** | `google/medgemma-1.5-4b-it` (Gemma 3 4B architecture) |
| **Parameters** | 4.3B |
| **Precision** | BF16 |
| **Training method** | QLoRA SFT + DPO (Direct Preference Optimization) |
| **Training data** | Decision-support Q&A pairs from UCG 2023 + format-switching instruction data + DPO preference pairs |
| **Scope** | Decision-support only — treatment and dosing excluded by design |

### Training Approach

This model was trained in three stages:

1. **Decision-support SFT**: QLoRA fine-tuning on clinical Q&A pairs covering 7 categories (differential diagnosis, diagnosis, referral, investigation, danger signs, special populations, refusal). Treatment and dosing were excluded after evaluation confirmed a capacity ceiling on factual drug recall at the 4B parameter scale.

2. **Instruction-following SFT**: Continued fine-tuning from the SFT checkpoint to teach format-switching — emitting XML, array, or prose triage packets depending on the system prompt.

3. **DPO alignment**: Preference optimization using a structured taxonomy of preference pairs targeting format compliance, refusal consistency, and triage safety. DPO was stacked on the conservative SFT checkpoint (v2.1) to preserve its strong clinical reasoning baseline.

### What the Model Refuses

The model refuses treatment and dosing questions across all output formats. This is a deliberate safety boundary — drug name confusion at the 4B parameter scale made treatment responses unreliable.

### Crane MedGemma 1.5 IT vs v2.1

| | v2.1 (SFT-only) | This model (SFT + DPO) |
|---|---|---|
| **Training** | SFT only | SFT + DPO |
| **Best for** | Prose Q&A, refusal compliance | XML triage packets, triage safety |
| **Prose refusal** | 5.00/5 (perfect) | 4.33/5 |
| **XML parse rate** | 98.2% | 99.4% |
| **Array parse rate** | 92.2% | 97.6% |
| **Triage safety** | 2.63/5 | 3.08/5 (best) |
| **Ship gates passed** | 5/12 | 6/12 |

## Evaluation

Evaluated across three benchmarks using Gemini as an automated evaluator.

### Ship Gate Analysis

| Gate | Target | Result |
|------|--------|--------|
| Prose content quality (210 samples) | >= 3.43/5 | 3.41 |
| XML parse rate | >= 95% | 99.4% |
| Array parse rate | >= 95% | 97.6% |
| Prose parse rate | >= 95% | 100% |
| XML content quality (held-out) | >= 3.43/5 | 3.02 |
| Triage safety (50 presentations) | — | 3.08 (best) |
| XML refusal | >= 4.5/5 | 4.45 |

**6 of 12 ship gates passed.** Held-out content quality caps at ~3.0/5 — a 4B parameter capacity ceiling. RAG is expected to close this gap.

### Strengths

- **Best triage safety**: 3.08/5 on clinical presentation prompts — highest across all checkpoints
- **Best format compliance**: 99.4% XML parse, 97.6% array parse
- **Strong XML refusal**: 4.45/5 — closest to the 4.5 gate target
- **DPO improved format without losing content**: Clinical quality maintained (3.41/5 prose) while format compliance increased

### Known Limitations

- **4B parameter capacity ceiling**: Held-out content quality caps at ~3.0/5. Factual recall for unseen conditions is limited at this parameter scale.
- **Treatment and dosing excluded**: By design. The model refuses these queries.
- **Refusal regression from DPO**: Prose refusal dropped from 5.00 (SFT) to 4.33 after DPO. The DPO preference data slightly loosened the refusal boundary.
- **Special populations weakness**: 1.22/5 — limited population-specific detail in the source guidelines.
- **Single-turn only**: No conversational follow-up capability.

## How to Use

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

model_id = "CraneAILabs/crane-medgemma-1.5-it"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype="bfloat16", device_map="auto")

# XML triage output
messages = [
    {"role": "system", "content": "Respond in XML: <r><t>level</t><c>condition</c><cf>confidence</cf><sg>action1|action2</sg><ns>follow-up1|follow-up2</ns><rf>danger1|danger2</rf></r>"},
    {"role": "user", "content": "A 28-year-old pregnant woman at 32 weeks presents with severe headache, blurred vision, and blood pressure 160/110."}
]

inputs = tokenizer.apply_chat_template(messages, return_tensors="pt", add_generation_prompt=True).to(model.device)
outputs = model.generate(inputs, max_new_tokens=512, temperature=0.3)
print(tokenizer.decode(outputs[0][inputs.shape[-1]:], skip_special_tokens=True))
```

## Ethical Considerations

- **Not a replacement for clinical judgment.** All outputs are advisory. The clinician makes all decisions.
- **No patient data** was used in training. All data derives from published government clinical guidelines.
- **Offline-first deployment** — no patient data leaves the device.
- **Scope boundaries are safety boundaries.** Treatment/dosing refusal prevents harm from drug name confusion at this model scale.

## Citation

If you use this model, please cite:

```
@misc{crane-medgemma-2026,
  title={Crane MedGemma 1.5 IT: Clinical Decision-Support for Uganda Clinical Guidelines},
  author={Crane AI Labs},
  year={2026},
  publisher={Hugging Face},
  url={https://huggingface.co/CraneAILabs/crane-medgemma-1.5-it}
}
```

## License

This model is subject to the [MedGemma Terms of Use](https://huggingface.co/google/medgemma-1.5-4b-it). Additional fine-tuning artifacts are proprietary to Crane AI Labs.
