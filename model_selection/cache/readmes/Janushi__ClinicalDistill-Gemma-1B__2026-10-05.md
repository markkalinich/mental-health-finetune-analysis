---
language:
- en
license: apache-2.0
base_model: google/gemma-3-1b-it
tags:
- clinical-nlp
- medical
- information-extraction
- lora
- peft
- fine-tuned

pipeline_tag: text-generation
---

# ClinicalDistill-Gemma-1B

Fine-tuned Gemma-3-1B for structured clinical symptom extraction 
from unstructured medical text. Distills GPT-4o clinical NLP 
capability into a small, deployable model.

## Model Description

- **Base model:** google/gemma-3-1b-it
- **Fine-tuning:** LoRA (r=16, alpha=32, q_proj + v_proj)
- **Task:** Clinical symptom extraction → structured JSON
- **Developed by:** Janushi Shastri
- **License:** Apache 2.0

## What It Does

Converts unstructured clinical text into structured JSON.

**Input:**
"been feeling off for a few days, chest feels weird and i get tired just walking around"

**Output:**
```json
{
  "symptoms": ["chest discomfort", "fatigue"],
  "duration": ["few days", "unspecified"],
  "severity": ["unspecified", "mild"],
  "urgent": true
}
```
**Input:**
"stomach's been acting up since yesterday, went to the bathroom like 4 times, feeling drained"

**Output:**
```json
{
  "symptoms": ["diarrhea", "fatigue"],
  "duration": ["since yesterday", "unspecified"],
  "severity": ["unspecified", "mild"],
  "urgent": false
}
```

## Performance

Evaluated on 35 held-out clinical examples:

| Metric | Score |
|---|---|
| Valid JSON rate | 100% |
| Symptom F1 | 0.781 |
| Urgent Accuracy | 85.7% |

## Cross-Model Benchmark

| Model | Method | F1 | Urgent Acc |
|---|---|---|---|
| **Gemma-3-1B** | **LoRA** | **0.781** | **85.7%** |
| Gemma-3-1B | QLoRA | 0.740 | 82.9% |
| LLaMA-3.2-1B | LoRA | 0.743 | 74.3% |
| LLaMA-3.2-1B | QLoRA | 0.767 | 74.3% |
| Qwen1.5-1.8B | LoRA | 0.707 | 74.3% |
| Qwen1.5-1.8B | QLoRA | 0.696 | 87.9% |

## How to Use

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_id = "YOUR_HF_USERNAME/ClinicalDistill-Gemma-1B"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.bfloat16,
    device_map="auto"
)

def extract_clinical(text):
    prompt = f"""<instruction>
Extract symptoms from the clinical note below. Reply with ONLY valid JSON.
Format: {{"symptoms": ["s1"], "duration": ["d1"], "severity": ["sev1"], "urgent": true/false}}
Use "unspecified" if unknown. urgent=true only for chest pain, breathing difficulty, stroke, severe bleeding.
</instruction>
<input>{text}</input>
<o>"""

    inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=200,
            temperature=0.1,
            do_sample=True,
            pad_token_id=tokenizer.eos_token_id
        )
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response.split("<o>")[-1].replace("</o>", "").strip()

print(extract_clinical("Patient has chest pain for 3 days and mild fever"))
```

## Training Details

- **Dataset:** 145 synthetic clinical examples (GPT-4o generated)
- **Domains:** Cardiac, respiratory, neurological, gastrointestinal
- **Epochs:** 7
- **Batch size:** 2 (gradient accumulation: 4)
- **Learning rate:** 2e-4
- **Hardware:** Google Colab T4 GPU
- **Training time:** ~8 minutes

## Intended Use

- Clinical NLP research
- Healthcare AI prototyping
- Resource-limited deployment (runs on single GPU)

## Limitations

- Trained on synthetic data — real clinical notes may differ
- English only
- Best suited for symptom extraction, not diagnosis

## Citation

```bibtex
@misc{shastri2026clinicaldistill,
  title={Benchmarking Small LLMs for Clinical Symptom Extraction 
         on Resource-Constrained Compute},
  author={Shastri, Janushi},
  year={2026}
}
```