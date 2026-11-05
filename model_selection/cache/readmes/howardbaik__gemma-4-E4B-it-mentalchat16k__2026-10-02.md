---
base_model: google/gemma-4-E4B-it
datasets:
  - ShenLab/MentalChat16K
language:
  - en
library_name: transformers
tags:
  - gemma4
  - mental-health
  - counseling
  - conversational
  - sft
pipeline_tag: image-text-to-text
---

# Gemma-4-E4B-it fine-tuned on MentalChat16K

A supervised fine-tune of **google/gemma-4-E4B-it** on the **MentalChat16K** dataset, intended for research on empathetic conversational behavior in small instruction-tuned models.


## Model Details

- **Developed by:** Howard Baik
- **Model type:** Causal language model (Gemma 4, E4B variant, instruction-tuned), fine-tuned with SFT
- **Language(s):** English
- **Finetuned from:** [`google/gemma-4-E4B-it`](https://huggingface.co/google/gemma-4-E4B-it)
- **Dataset:** [`ShenLab/MentalChat16K`](https://huggingface.co/datasets/ShenLab/MentalChat16K) — ~16K counselor-style conversational turns combining synthetic data and anonymized interview transcripts.

## Intended Uses

### Direct use
Research into lightweight empathetic dialogue agents, evaluation of counseling-style response quality in small LLMs, and as a baseline for further alignment or safety work.

### Out-of-scope use
- Clinical decision-making, diagnosis, or treatment.
- Crisis intervention or suicide/self-harm response.
- Any deployment to vulnerable users without human-in-the-loop review and independent safety evaluation.
- Legal, medical, or financial advice.

## Bias, Risks, and Limitations

- The MentalChat16K dataset is partly synthetic; response patterns may reflect GPT-family stylistic biases rather than evidence-based therapeutic practice.
- The model may produce confident-sounding but clinically incorrect guidance, miss safety-critical cues (e.g., suicidal ideation), or reinforce harmful framings.
- English-only; performance on other languages is not evaluated.
- Inherits any biases present in the Gemma 4 base model.

Users should assume the model is **not safety-aligned for mental-health deployment** and test extensively before any downstream use.

## How to Get Started

````python
from transformers import AutoProcessor, AutoModelForImageTextToText
import torch

model_id = "howardbaik/gemma-4-E4B-it-mentalchat16k"
processor = AutoProcessor.from_pretrained(model_id)
model = AutoModelForImageTextToText.from_pretrained(
    model_id, torch_dtype=torch.bfloat16, device_map="auto"
)

messages = [
    {"role": "user", "content": [{"type": "text", "text": "I've been feeling overwhelmed at work lately."}]},
]
inputs = processor.apply_chat_template(
    messages, add_generation_prompt=True, tokenize=True,
    return_dict=True, return_tensors="pt"
).to(model.device)

outputs = model.generate(**inputs, max_new_tokens=256)
print(processor.decode(outputs[0][inputs["input_ids"].shape[-1]:], skip_special_tokens=True))
````

## Training Details

### Training data

MentalChat16K (≈16K dialogues). Training and validation sets (70/30 split).

### Training procedure

- **Method:** Supervised fine-tuning (SFT)
- **Framework:** 🤗 TRL `SFTTrainer` with `SFTConfig`
- **Epochs:** 3
- **Per-device batch size:** 1 (train), 2 (eval)
- **Gradient accumulation steps:** 16 → **effective batch size: 16**
- **Gradient checkpointing:** enabled (`use_reentrant=False`)
- **Optimizer:** `adamw_torch_fused`
- **Learning rate:** 2e-5 (lowered for the larger model)
- **LR scheduler:** cosine
- **Warmup:** 5 steps (~3% of 183 total steps)
- **Max gradient norm:** 1.0
- **Precision:** bf16
- **Evaluation / save / logging strategy:** per epoch, keeping the 2 most recent checkpoints and loading the best model at end
- **Dataset handling:** custom collation (`skip_prepare_dataset=True`, `remove_unused_columns=False`)

### Compute

- **Hardware:** A100 GPU High RAM instance on Google Colab
- **Training time:** 6 hours


## Citation

If you use this model, please cite the base model and dataset:

````bibtex
@misc{gemma4,
  title  = {Gemma 4},
  author = {{Google DeepMind}},
  year   = {2026},
  url    = {https://huggingface.co/google/gemma-4-E4B-it}
}

@dataset{mentalchat16k,
  title  = {MentalChat16K},
  author = {Shen Lab},
  url    = {https://huggingface.co/datasets/ShenLab/MentalChat16K}
}
````

## Contact

Howard Baik — [https://huggingface.co/howardbaik](https://huggingface.co/howardbaik)