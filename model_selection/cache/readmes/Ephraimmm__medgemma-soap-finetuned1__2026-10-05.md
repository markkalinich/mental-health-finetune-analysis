---
license: apache-2.0
base_model: unsloth/medgemma-4b-it-unsloth-bnb-4bit
tags:
- medical
- clinical-nlp
- healthcare
- text-generation-inference
- transformers
- unsloth
- gemma3
language:
- en
pipeline_tag: text-generation
---

# MedGemma SOAP Note Generation Model

## Overview

This model is a fine-tuned variant of **MedGemma** (Google's medical-domain Gemma 3 model family), adapted to draft clinical **SOAP notes** (Subjective, Objective, Assessment, Plan) from consultation text. It was built on top of `unsloth/medgemma-4b-it-unsloth-bnb-4bit`, a 4-bit quantized build of `google/medgemma-4b-it`, and fine-tuned with [Unsloth](https://github.com/unslothai/unsloth) and Hugging Face's TRL library. The goal is to help reduce the clinical documentation burden by structuring free-text encounter notes or transcripts into a standard SOAP format — as a research/portfolio project, not a deployed clinical tool.

## Training Details

The values below are as reported by the model author in the original repository card. No `trainer_state.json`, evaluation logs, or `adapter_config.json` are included in the repository, so these figures could not be independently re-derived from raw training artifacts — they are presented here as author-reported metadata rather than independently verified benchmarks.

| Setting | Value |
|---|---|
| Base model | `unsloth/medgemma-4b-it-unsloth-bnb-4bit` (Unsloth's 4-bit build of `google/medgemma-4b-it`) |
| Architecture | Gemma3ForConditionalGeneration (Gemma 3 text backbone + SigLIP vision encoder), confirmed in `config.json` |
| Framework | Unsloth + Hugging Face TRL |
| Fine-tuning method | 4-bit QLoRA |
| LoRA rank | 16 (author-reported) |
| LoRA alpha | 32 (author-reported) |
| Epochs | 3 (author-reported) |
| Effective batch size | 8 (author-reported) |
| Learning rate | 2e-4 (author-reported) |
| LR scheduler | Cosine (author-reported) |
| Final train loss | 0.8076 (author-reported) |
| Final eval loss | 1.0012 (author-reported) |
| License | Apache 2.0 |
| Language | English |

This repository hosts the **fully merged model weights** (`model-00001-of-00002.safetensors`, `model-00002-of-00002.safetensors`) rather than a standalone LoRA adapter — the QLoRA weights described above were merged back into the base model before upload.

## Intended Use

- Drafting SOAP-formatted clinical notes from consultation text/transcripts, as a starting point for a clinician to review and edit.
- Assisting with structuring unorganized clinical text into Subjective, Objective, Assessment, and Plan sections.
- Educational and portfolio demonstration of applying parameter-efficient fine-tuning (QLoRA via Unsloth) to a medical-domain LLM.

This is a **research/portfolio project** and has **not** been evaluated or certified as a medical device. It is not intended for direct use in patient care without human clinical oversight, further validation, and regulatory review.

## How to Use

The model uses the standard Gemma 3 chat template (`<start_of_turn>user ... <end_of_turn>`). Load it with `transformers` as follows:

```python
import torch
from transformers import AutoProcessor, AutoModelForImageTextToText

model_id = "Ephraimmm/medgemma-soap-finetuned1"

processor = AutoProcessor.from_pretrained(model_id)
model = AutoModelForImageTextToText.from_pretrained(
    model_id,
    torch_dtype=torch.bfloat16,
    device_map="auto",
)

messages = [
    {
        "role": "user",
        "content": [
            {"type": "text", "text": (
                "Convert the following clinical consultation notes into a SOAP note "
                "(Subjective, Objective, Assessment, Plan):\n\n"
                "Patient reports a 3-day history of sore throat and low-grade fever. "
                "Temp 37.9C, throat erythematous, no exudate. Rapid strep negative. "
                "Plan: supportive care, follow up if symptoms worsen."
            )}
        ],
    }
]

inputs = processor.apply_chat_template(
    messages,
    add_generation_prompt=True,
    tokenize=True,
    return_dict=True,
    return_tensors="pt",
).to(model.device)

with torch.inference_mode():
    output = model.generate(**inputs, max_new_tokens=512)

response = processor.decode(output[0][inputs["input_ids"].shape[-1]:], skip_special_tokens=True)
print(response)
```

Note: the base architecture (Gemma3ForConditionalGeneration) supports multimodal image+text input, but this fine-tune was trained and is intended for text-only SOAP note generation.

## Limitations

- **Not clinically validated.** No formal clinical accuracy, safety, or bias evaluation has been performed or is included in this repository. Any accuracy or quality figures beyond the training/eval loss values above should not be assumed.
- **Not a substitute for professional medical judgment.** Output must be reviewed and verified by a qualified clinician before any use in real patient documentation or care.
- **No independent training-run artifacts.** Since `trainer_state.json` and adapter configuration files are not present in this repository, the exact LoRA/training hyperparameters could not be independently confirmed beyond what the author documented.
- **Domain and demographic coverage unknown.** The fine-tuning dataset's size, sourcing, and representativeness are not documented in this repository, so generalization to arbitrary clinical specialties, populations, or documentation styles is unverified.
- **Hallucination risk.** As with any generative LLM, the model may produce plausible-sounding but incorrect or fabricated clinical content (e.g., inventing findings not present in the source text).
- Should **not** be used for real patient care, billing, or legal documentation without proper clinical validation, human review, and appropriate regulatory approval.

## Author

Developed by [Ephraimmm](https://huggingface.co/Ephraimmm)
