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
  - uganda-clinical-guidelines
  - bf16
  - safetensors
base_model: google/medgemma-1.5-4b-it
pipeline_tag: text-generation
---

# v2.1 Instruct MedGemma (SFT-only)

A clinical decision-support model fine-tuned from [MedGemma 1.5 4B-IT](https://huggingface.co/google/medgemma-1.5-4b-it) on the Uganda Clinical Guidelines 2023. Conservative SFT-only checkpoint with perfect refusal compliance.

For the primary production model (SFT + DPO, best overall performance), see [Crane MedGemma 1.5 IT](https://huggingface.co/CraneAILabs/crane-medgemma-1.5-it).

> **This model is a clinical thinking aid. It does not provide diagnoses, prescriptions, or automated clinical decisions.**

## Intended Use

**Primary use case**: Assist frontline health workers (clinical officers, nurses) at Health Centre II–IV facilities in Uganda with clinical triage reasoning — differential diagnosis, danger sign identification, investigation ordering, referral criteria, and special population considerations.

**Output formats**: The model can emit structured triage assessments in three formats (XML, positional array, prose) based on the system prompt. The production app uses compact XML packets for low-latency on-device inference.

**Deployment target**: On-device inference on Android via quantized GGUF. This bf16 checkpoint is the full-precision reference and was used as the base for the DPO-aligned [Crane MedGemma 1.5 IT](https://huggingface.co/CraneAILabs/crane-medgemma-1.5-it).

### In-Scope

- Differential diagnosis reasoning for conditions in the Uganda Clinical Guidelines
- Danger sign identification and referral triage
- Investigation recommendations
- Special population considerations (pediatric, pregnancy, HIV)
- Refusal of out-of-scope queries (treatment, dosing)

### Out-of-Scope

- **Treatment and dosing recommendations** — the model is trained to refuse these queries and redirect to the facility's Uganda Clinical Guidelines
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
| **Training method** | QLoRA SFT (Supervised Fine-Tuning) |
| **Training data** | 11,991 decision-support Q&A pairs derived from Uganda Clinical Guidelines 2023, followed by instruction-following SFT on format-switching data |
| **Scope** | Decision-support only — treatment and dosing categories removed by design |

### Training Approach

The model was fine-tuned in two stages:

1. **Decision-support SFT**: QLoRA fine-tuning on 11,991 Q&A pairs covering 7 clinical categories (differential diagnosis, diagnosis, referral, investigation, danger signs, special populations, refusal). Treatment and dosing categories were excluded after evaluation showed a capacity ceiling on factual drug recall at this parameter scale.

2. **Instruction-following SFT**: Continued fine-tuning to teach format-switching — the model emits XML, array, or prose triage packets depending on the system prompt.

### What the Model Refuses

The model is trained to refuse treatment and dosing questions with: *"Treatment and dosing recommendations are outside the scope of this tool. Please refer to your facility's Uganda Clinical Guidelines."*

This is a deliberate safety boundary. Drug name confusion at the 4B parameter scale made treatment responses unreliable, so the scope was narrowed to decision-support where the model performs well.

## Evaluation

Evaluated across three benchmarks using Gemini as an automated evaluator in constrained comparison mode.

### Ship Gate Analysis

| Gate | Target | Result |
|------|--------|--------|
| Prose content quality (210 samples) | >= 3.43/5 | 3.39 |
| XML parse rate | >= 95% | 98.2% |
| Array parse rate | >= 95% | 92.2% |
| Prose parse rate | >= 95% | 100% |
| XML content quality (held-out) | >= 3.43/5 | 3.03 |
| Refusal compliance (prose) | >= 4.5/5 | 5.00 |

**5 of 12 ship gates passed.** Content quality on held-out conditions caps at ~3.0/5 — a parameter capacity ceiling, not a training procedure failure. Retrieval-augmented generation (RAG) is expected to close this gap.

### Strengths

- **Perfect refusal compliance**: 5.00/5 on prose refusal — never leaks treatment or dosing content
- **Strong differential diagnosis**: 4.38/5 on diagnosis questions
- **High XML parse rate**: 98.2% valid structured output
- **Reasoning over recall**: "Why" questions score 5.0/5; the model reasons well about clinical logic

### Known Limitations

- **4B parameter capacity ceiling**: Held-out content quality caps at ~3.0/5. The model has limited factual recall for conditions it hasn't seen extensively in training.
- **Treatment and dosing excluded**: By design. The model refuses these queries.
- **Special populations weakness**: 1.11/5 — the source guidelines have limited population-specific detail for many conditions.
- **Array parse rate**: 92.2% (below 95% gate). XML and prose formats are more reliable.
- **Single-turn only**: No conversational follow-up capability.

## How to Use

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

model_id = "CraneAILabs/v2.1-instruct-medgemma-bf16"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype="bfloat16", device_map="auto")

messages = [
    {"role": "system", "content": "You are a clinical decision-support tool based on the Uganda Clinical Guidelines. Provide structured triage assessments. Do not provide treatment or dosing recommendations."},
    {"role": "user", "content": "A 4-year-old presents with fever 39.5C for 3 days, neck stiffness, and photophobia. What should I consider?"}
]

inputs = tokenizer.apply_chat_template(messages, return_tensors="pt", add_generation_prompt=True).to(model.device)
outputs = model.generate(inputs, max_new_tokens=512, temperature=0.3)
print(tokenizer.decode(outputs[0][inputs.shape[-1]:], skip_special_tokens=True))
```

## Ethical Considerations

- **Not a replacement for clinical judgment.** All outputs are advisory. The clinician makes all decisions.
- **No patient data** was used in training. All training data is derived from published government clinical guidelines.
- **Offline-first deployment** — no patient data leaves the device.
- **Scope boundaries are safety boundaries.** The refusal of treatment/dosing queries is a deliberate design choice to prevent harm from drug name confusion at this model scale.

## Citation

If you use this model, please cite:

```
@misc{crane-medgemma-v21-2026,
  title={v2.1 Instruct MedGemma: SFT-Only Clinical Decision-Support for Uganda Clinical Guidelines},
  author={Crane AI Labs},
  year={2026},
  publisher={Hugging Face},
  url={https://huggingface.co/CraneAILabs/v2.1-instruct-medgemma-bf16}
}
```

## License

This model is subject to the [MedGemma Terms of Use](https://huggingface.co/google/medgemma-1.5-4b-it). Additional fine-tuning artifacts are proprietary to Crane AI Labs.
