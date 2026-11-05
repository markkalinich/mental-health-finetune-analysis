---
library_name: transformers
license: apache-2.0
language:
  - en
tags:
  - mental-health
  - counseling
  - llama
  - qlora
  - dpo
  - sft
  - alignment
base_model: meta-llama/Llama-3.1-8B-Instruct
pipeline_tag: text-generation
---

# CounseLLM — Empathy-Aligned Conversational Support LLM

An empathy-aligned conversational support model fine-tuned from **Llama 3.1 8B Instruct** using a two-stage alignment pipeline: Supervised Fine-Tuning (SFT) on 36K counseling examples followed by Direct Preference Optimization (DPO) on ~2K preference-filtered pairs.

> **Disclaimer:** This is an AI research project and is **not a substitute for professional mental health care.** If you are in crisis, please contact the [988 Suicide & Crisis Lifeline](https://988lifeline.org/) (call or text 988) or your local emergency services.

## Model Details

- **Developed by:** [Gowtham Arulmozhii](https://github.com/wothmag07)
- **Model type:** Causal Language Model (text generation)
- **Language:** English
- **License:** Apache 2.0
- **Base model:** [meta-llama/Llama-3.1-8B-Instruct](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct)
- **Repository:** [GitHub](https://github.com/wothmag07/counseLLM)

## Training

### Two-Stage Alignment Pipeline

**Stage 1 — Supervised Fine-Tuning (SFT)**

| Parameter | Value |
|---|---|
| Method | QLoRA (4-bit NF4 + double quantization) |
| LoRA Rank / Alpha | 64 / 128 |
| Learning Rate | 2e-4 (cosine scheduler) |
| Epochs | 2 |
| Effective Batch Size | 16 |
| Training Data | 36K multi-source counseling examples |
| GPU | NVIDIA H100 80GB |
| Training Time | ~3 hours |

**Stage 2 — Direct Preference Optimization (DPO)**

| Parameter | Value |
|---|---|
| Method | QLoRA on SFT-merged base |
| LoRA Rank / Alpha | 16 / 32 |
| Beta (KL penalty) | 0.5 |
| Learning Rate | 1e-5 (cosine scheduler) |
| Epochs | 1 |
| Effective Batch Size | 8 |
| Training Data | ~2K preference-filtered pairs |
| GPU | NVIDIA H100 80GB |
| Training Time | ~30 minutes |

### Training Data

**SFT (36K examples from 5 sources)**

| Source | Examples | Type |
|---|---|---|
| [MentalChat16K](https://huggingface.co/datasets/ShenLab/MentalChat16K) | ~16K | Synthetic + clinical |
| [empathetic_dialogues](https://huggingface.co/datasets/Estwld/empathetic_dialogues_llm) | ~10K | Real human multi-turn |
| [Psych8k](https://huggingface.co/datasets/EmoCareAI/Psych8k) | ~8K | Real therapist transcripts |
| [counsel-chat](https://huggingface.co/datasets/nbertagnolli/counsel-chat) | ~940 | Real therapist Q&A |
| [ESConv](https://huggingface.co/datasets/thu-coai/esconv) | ~910 | Real human + strategy labels |

**DPO (~2K preference pairs)**

| Source | Pairs | Selection |
|---|---|---|
| [PsychoCounsel-Preference](https://huggingface.co/datasets/Psychotherapy-LLM/PsychoCounsel-Preference) | ~2K | Rating-gap filtered across 7 dimensions |

## Evaluation

### Automated Metrics

| Metric | Base | SFT | DPO |
|---|---|---|---|
| Perplexity | 4.18 | 3.64 | **3.13** |
| BERTScore F1 | 0.8598 | 0.8527 | 0.8492 |
| ROUGE-L F1 | 0.1065 | 0.0772 | 0.0790 |
| Distinct-1 | 0.273 | **0.331** | 0.262 |
| Distinct-2 | 0.658 | **0.807** | 0.712 |
| Avg Response Length | 98 | 119 | **198** |

### LLM-as-Judge (GPT-4o, 1-5 scale)

| Dimension | Base | SFT | DPO |
|---|---|---|---|
| Empathy | 4.40 | 3.48 | **4.88** |
| Safety | 4.28 | 3.84 | **4.60** |
| Relevance | 4.68 | 3.72 | **4.88** |
| Helpfulness | 4.04 | 3.04 | **4.48** |
| **Overall** | 4.35 | 3.52 | **4.71** |

Evaluated on 25 curated prompts across 18 mental health categories (anxiety, depression, grief, crisis, relationships, trauma, etc.).

## Available Checkpoints

This repo contains three artifacts:

| Path | Format | Size | Description |
|---|---|---|---|
| `/` (root) | Full merged model | ~16 GB | Ready-to-use Llama 3.1 8B + SFT + DPO merged |
| `sft/` | LoRA adapter | ~640 MB | Stage-1 SFT adapter (r=64, α=128) — load on top of base Llama 3.1 8B |
| `dpo/` | LoRA adapter | ~160 MB | Stage-2 DPO adapter (r=16, α=32) — load on top of SFT-merged base |

Load an adapter with PEFT:

```python
from peft import PeftModel
from transformers import AutoModelForCausalLM

base = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-3.1-8B-Instruct", torch_dtype="bfloat16", device_map="auto")
model = PeftModel.from_pretrained(base, "Wothmag07/counseLLM", subfolder="dpo")
```


## How to Use

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_id = "Wothmag07/counseLLM"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.bfloat16,
    device_map="auto",
)

messages = [
    {"role": "system", "content": "You are a mental health counselor providing supportive, empathetic guidance. Respond by first acknowledging the person's feelings, then explore their situation with open-ended questions. Use techniques like reflective listening, validation, and gentle reframing. Keep responses warm, conversational, and non-judgmental."},
    {"role": "user", "content": "I've been feeling really anxious about work lately and I can't sleep."},
]

input_ids = tokenizer.apply_chat_template(messages, return_tensors="pt").to(model.device)
outputs = model.generate(
    input_ids,
    max_new_tokens=512,
    temperature=0.7,
    top_p=0.9,
    repetition_penalty=1.1,
)
response = tokenizer.decode(outputs[0][input_ids.shape[1]:], skip_special_tokens=True)
print(response)
```

## Uses

### Intended Use

- Research and educational purposes in AI-assisted mental health support
- Studying alignment techniques (SFT + DPO) applied to sensitive domains
- Demonstrating empathy-aligned language model fine-tuning

### Out-of-Scope Use

- **Clinical deployment** — this model is not validated for clinical use
- **Crisis intervention** — should not be relied upon for suicide prevention or emergency situations
- **Replacement for therapy** — not a substitute for licensed mental health professionals

## Bias, Risks, and Limitations

- The model may reflect biases present in training data (both real and synthetic sources)
- Responses may sometimes be generic or miss nuances of specific cultural contexts
- The model may generate plausible-sounding but clinically inaccurate advice
- Training data is predominantly English and may not generalize to other languages
- Should not be deployed in production clinical settings without extensive safety review

## Environmental Impact

- **Hardware:** NVIDIA H100 80GB
- **Training Time:** ~3.5 hours total (SFT: 3h, DPO: 30min)
- **Cloud Provider:** [Modal](https://modal.com/)

## Tech Stack

| Component | Technology |
|---|---|
| Base Model | Meta Llama 3.1 8B Instruct |
| Training | HuggingFace TRL (SFTTrainer, DPOTrainer) |
| Quantization | QLoRA via bitsandbytes (4-bit NF4) |
| Adapters | PEFT (LoRA) |
| Infrastructure | Modal (H100 GPUs) |
| Experiment Tracking | Weights & Biases |
| Evaluation | BERTScore, ROUGE-L, GPT-4o Judge |

## Citation

```bibtex
@misc{counseLLM2026,
  author = {Gowtham Arulmozhii},
  title = {CounseLLM: Empathy-Aligned Conversational Support LLM},
  year = {2026},
  publisher = {HuggingFace},
  url = {https://huggingface.co/Wothmag07/counseLLM}
}
```

## Model Card Contact

- GitHub: [@wothmag07](https://github.com/wothmag07)
