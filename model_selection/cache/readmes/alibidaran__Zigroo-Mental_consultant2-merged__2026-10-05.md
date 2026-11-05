---
language:
- en
license: apache-2.0
base_model: unsloth/Qwen3-8B-unsloth-bnb-4bit
tags:
- mental-health
- therapy
- counseling
- qwen3
- lora
- sft
- dpo
- unsloth
- text-generation
- conversational
pipeline_tag: text-generation
datasets:
- vibhorag101/phr-mental-therapy-dataset-conversational-format-1024-tokens
- Ghani69/ACT_therapy_scripts
- jkhedri/psychology-dataset
- fadodr/mental_health_therapy
- arafatanam/Student-Mental-Health-Counseling-50K
---

# 🧠 Zigroo Mental Consultant 2 (Merged)

**`alibidaran/Zigroo-Mental_consultant2-merged`**

A fine-tuned large language model designed to provide empathetic, therapeutically-informed conversational support. Built on top of Qwen3-8B, this model was trained in two stages — Supervised Fine-Tuning (SFT) across five curated mental health datasets, followed by Direct Preference Optimization (DPO) to align responses toward reliable, compassionate, and therapeutically grounded outputs.

> ⚠️ **Disclaimer:** This model is intended for research and educational purposes only. It is **not** a substitute for professional mental health care, diagnosis, or treatment. If you or someone you know is in crisis, please contact a licensed mental health professional or a crisis helpline immediately.

---

## 🔍 Model Details

| Property | Value |
|---|---|
| **Base Model** | `unsloth/Qwen3-8B-unsloth-bnb-4bit` |
| **Model Type** | Causal Language Model (Merged LoRA) |
| **LoRA Rank** | 32 |
| **Training Stages** | SFT → DPO |
| **Language** | English |
| **License** | Apache 2.0 |

---

## 🏋️ Training Pipeline

### Stage 1 — Supervised Fine-Tuning (SFT)

The model was fine-tuned using a LoRA adapter (rank = 32) on five mental health and therapy datasets covering a wide range of therapeutic modalities:

| Dataset | Description |
|---|---|
| [`vibhorag101/phr-mental-therapy-dataset-conversational-format-1024-tokens`](https://huggingface.co/datasets/vibhorag101/phr-mental-therapy-dataset-conversational-format-1024-tokens) | Conversational mental therapy dialogues formatted to 1024 tokens |
| [`Ghani69/ACT_therapy_scripts`](https://huggingface.co/datasets/Ghani69/ACT_therapy_scripts) | Acceptance and Commitment Therapy (ACT) scripts |
| [`to-be/annomi-motivational-interviewing-therapy-conversations`](https://huggingface.co/datasets/to-be/annomi-motivational-interviewing-therapy-conversations) | Motivational interviewing therapy conversations |
| [`fadodr/mental_health_therapy`](https://huggingface.co/datasets/fadodr/mental_health_therapy) | General mental health therapy dialogues |
| [`arafatanam/Student-Mental-Health-Counseling-50K`](https://huggingface.co/datasets/arafatanam/Student-Mental-Health-Counseling-50K) | 50K student mental health counseling conversations |

### Stage 2 — Direct Preference Optimization (DPO)

Following SFT, the model underwent DPO training to align its outputs with preferred therapeutic response styles, improving reliability, empathy, and safety of generated responses.

| Dataset | Description |
|---|---|
| [`jkhedri/psychology-dataset`](https://huggingface.co/datasets/jkhedri/psychology-dataset) | Psychology-grounded preference pairs for DPO alignment |

---

## 🚀 Usage

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_id = "alibidaran/Zigroo-Mental_consultant2-merged"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.bfloat16,
    device_map="auto"
)

prompt = "I've been feeling very anxious lately and I don't know how to cope."

messages = [
    {"role": "user", "content": prompt}
]

text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
inputs = tokenizer(text, return_tensors="pt").to(model.device)

with torch.no_grad():
    outputs = model.generate(
        **inputs,
        max_new_tokens=512,
        do_sample=True,
        temperature=0.7,
        top_p=0.9,
    )

response = tokenizer.decode(outputs[0][inputs["input_ids"].shape[-1]:], skip_special_tokens=True)
print(response)
```

### 4-bit Quantized Inference (recommended for limited VRAM)

```python
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
import torch

model_id = "alibidaran/Zigroo-Mental_consultant2-merged"

bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16
)

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    quantization_config=bnb_config,
    device_map="auto"
)
```

---

## ⚙️ LoRA Configuration

This model was trained with a LoRA adapter and the weights have been merged into the base model for ease of deployment. The key LoRA hyperparameters used during training:

- **Rank (r):** 32
- **Base model:** Qwen3-8B (via Unsloth 4-bit quantized variant)
- **Merged:** ✅ LoRA weights fully merged into base model

---

## 🎯 Intended Use

- Research into LLM-based therapeutic conversational agents
- Prototyping mental health support chatbots
- Studying multi-stage fine-tuning pipelines (SFT + DPO) for sensitive domains
- Educational exploration of therapeutic dialogue generation

## ❌ Out-of-Scope Use

- Clinical diagnosis or treatment decisions
- Crisis intervention without human oversight
- Replacement of licensed therapists or psychiatrists
- Any deployment involving vulnerable populations without professional supervision

---

## ⚠️ Ethical Considerations & Safety

Mental health is a sensitive domain. Please be aware of the following:

- **Not a therapist.** This model does not possess clinical judgment and should never be used as a standalone mental health service.
- **Hallucinations.** Like all LLMs, this model can generate plausible-sounding but incorrect or harmful content.
- **Bias.** Training datasets may reflect biases in how mental health topics are framed; outputs should be reviewed critically.
- **Crisis situations.** This model is not equipped to handle acute crisis situations. Always redirect users in crisis to emergency services or licensed professionals.


*Built with ❤️ using [Unsloth](https://github.com/unslothai/unsloth) and [TRL](https://github.com/huggingface/trl).*