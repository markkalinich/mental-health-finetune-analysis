---
license: other
license_name: gemma
license_link: https://ai.google.dev/gemma/terms
base_model: google/medgemma-1.5-4b-it
tags:
  - text-generation
  - conversational
  - medical
  - health-chat
  - gemma3
  - safetensors
  - fine-tuned
language:
  - en
pipeline_tag: text-generation
model_type: gemma3
---

# MedGemma Health Chat — Merged 16-bit

## Model Description

A 16-bit merged model fine-tuned from [google/medgemma-1.5-4b-it](https://huggingface.co/google/medgemma-1.5-4b-it) for multi-persona health chat conversations. The LoRA adapter has been merged into the base model weights, producing a standalone model that requires no separate adapter loading.

The model responds as one of six medical personas (primary care, internal medicine, clinical nutritionist, exercise specialist, integrated physician, chronic health specialist) with direct, clinically grounded guidance optimized for mobile display.

## Intended Use

- Health chat assistant for patient-facing applications
- Provides clinical guidance in a conversational format
- Designed for mobile-first display (no tables, concise prose)
- Each conversation assigns a persona based on topic relevance

**Not intended for:** diagnosing conditions, replacing professional medical care, or emergency triage. Always recommend professional care for emergencies.

## Personas

| Persona | Specialty |
|---|---|
| Primary Care | General practice, common conditions, preventive care |
| Internal Medicine | Complex adult medicine, multi-system disorders, chronic disease |
| Clinical Nutritionist | Dietary interventions, nutritional therapy, meal planning |
| Exercise Specialist | Therapeutic exercise, sports performance, rehabilitation |
| Best Doctor | Cross-specialty integration, OLDCARTS methodology, comprehensive care |
| Chronic Health | Chronic illness management, diagnostic mysteries, patient coaching |

Persona prompts are sourced from [BisonHealth-AI/Personas-Prompts](https://github.com/bisonbet/BisonHealth-AI/tree/main/Personas-Prompts).

## Training Data

- **Dataset:** [bisonnetworking/medgemma-health-chat-sft](https://huggingface.co/datasets/bisonnetworking/medgemma-health-chat-sft)
- **Training samples:** 49,500 conversations
- **Eval samples:** 500 conversations
- **Format:** ShareGPT/conversational JSONL with system (persona prompt) + user + assistant turns
- **Health context:** Simulated Apple Health data (vitals, labs, medications, conditions) injected into user messages

## Training Procedure

### LoRA Fine-Tuning

- **Rank (r):** 32
- **Alpha:** 64
- **Dropout:** 0
- **Target modules:** q_proj, k_proj, v_proj, o_proj, gate_proj, up_proj, down_proj
- **Trainable parameters:** 65,576,960 (1.50% of 4,365,656,432 total)
- **Base model loaded in:** 4-bit (NF4) quantization

### Training Hyperparameters

- **Epochs:** 2
- **Batch size:** 8 (per-device)
- **Gradient accumulation:** 1
- **Learning rate:** 2e-4 (cosine scheduler, warmup ratio 0.03)
- **Optimizer:** adamw_8bit
- **Weight decay:** 0.01
- **Max sequence length:** 2048
- **Precision:** bf16
- **Packing:** True (sequence concatenation for GPU efficiency)

### Training Results

- **Total steps:** 12,376
- **Final training loss:** 0.7981
- **Best eval loss:** 0.8779 (step 12,000)
- **Loss trajectory:** 1.40 (step 75) → 1.01 (step 700) → 0.94 (step 1100) → 0.80 (step 12,375)

### Merging

The LoRA adapter was merged into the base MedGemma 1.5 4B model in float16 precision using PEFT's `merge_and_unload()`. The merged model is distributed as two safetensors shards (~8.6GB total).

### Compute Infrastructure

- **Hardware:** NVIDIA H100 80GB (Modal serverless)
- **Training time:** ~3 hours
- **Software:** Unsloth 2025.7.8, Transformers 4.54.0, PEFT 0.16.0, TRL 0.19.1
- **Platform:** [Modal](https://modal.com)

## How to Use

### With Transformers

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_id = "bisonnetworking/medgemma-health-chat-merged"

model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.float16,
    device_map="auto",
    trust_remote_code=True,
)
tokenizer = AutoTokenizer.from_pretrained(model_id)

messages = [
    {
        "role": "system",
        "content": "You are a board-certified Primary Care Physician. Provide clinical guidance with professionalism and clarity. Use ONLY health data explicitly provided in user context. No tables. No AI disclaimers. Answer the specific question asked - no more, no less.",
    },
    {
        "role": "user",
        "content": "PATIENT CONTEXT: Age 52, Male. BP: 145/92 mmHg. Medications: Lisinopril 20mg daily. Conditions: Hypertension.\n\nMy blood pressure has been reading higher than usual the past week. Should I adjust my medication?",
    },
]

inputs = tokenizer.apply_chat_template(
    messages, return_tensors="pt", add_generation_prompt=True
).to(model.device)

outputs = model.generate(
    inputs,
    max_new_tokens=512,
    temperature=0.7,
    top_p=0.9,
    do_sample=True,
)
response = tokenizer.decode(outputs[0][inputs.shape[1]:], skip_special_tokens=True)
print(response)
```

### With vLLM

```python
from vllm import LLM, SamplingParams

llm = LLM(model="bisonnetworking/medgemma-health-chat-merged", dtype="float16")
sampling = SamplingParams(temperature=0.7, top_p=0.9, max_tokens=512)

messages = [
    {"role": "system", "content": "You are a board-certified Primary Care Physician..."},
    {"role": "user", "content": "I've had a sore throat for 3 days. What should I do?"},
]
prompt = llm.get_tokenizer().apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
outputs = llm.generate([prompt], sampling)
print(outputs[0].outputs[0].text)
```

### For MLX (Apple Silicon)

```bash
# Convert to MLX format
pip install mlx-lm
mlx_lm.convert --hf-path bisonnetworking/medgemma-health-chat-merged --mlx-path ./medgemma-health-chat-mlx
mlx_lm.generate --model ./medgemma-health-chat-mlx --prompt "I've had a sore throat for 3 days. What should I do?"
```

## Evaluation

300 test cases (50 per persona) across 6 categories:

| Category | Cases/Persona | What It Tests |
|---|---|---|
| Medical accuracy | 14 | Clinically correct information for persona's specialty |
| Persona adherence | 9 | Response style matches persona (direct, no AI disclaimers, concise) |
| Health context usage | 10 | References actual values from provided health data |
| Data integrity | 6 | Does not hallucinate data not in context |
| Safety | 6 | Recognizes emergencies, recommends 911/988/Poison Control |
| Formatting | 5 | No markdown tables, no AI disclaimers, mobile-friendly |

Test cases are in the [medgemma-health-chat](https://github.com/bisonbet/medgemma-health-chat) repository under `test_data/`.

## Limitations

- Fine-tuned on synthetic conversations — quality depends on the base model's medical knowledge
- Persona prompts enforce style but cannot guarantee clinical accuracy
- No tables in output (mobile constraint) — may reduce clarity for complex comparisons
- Not a substitute for professional medical advice
- MedGemma base model is gated — users need approved access to the original model
- No safety training beyond what's in the base model — additional RLHF/red-teaming recommended for production

## Ethical Considerations

- This model provides health information but is NOT a medical device
- Responses should not be used as sole basis for medical decisions
- Emergency situations should always be directed to 911 or local emergency services
- The model may reflect biases present in the training data
- Users should be clearly informed they are chatting with an AI, not a human physician

## LoRA Adapter

The original LoRA adapter (pre-merge) is available at [bisonnetworking/medgemma-health-chat-lora](https://huggingface.co/bisonnetworking/medgemma-health-chat-lora) for those who prefer to load it separately or further fine-tune.

## Model Card Contact

[bisonnetworking](https://huggingface.co/bisonnetworking)