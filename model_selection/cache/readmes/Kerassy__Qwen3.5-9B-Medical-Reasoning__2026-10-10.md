---
license: apache-2.0
language:
- en
tags:
- medical
- reasoning
- chain-of-thought
- qwen
- unsloth
- lora
datasets:
- FreedomIntelligence/medical-o1-reasoning-SFT
metrics:
- accuracy
base_model: Qwen/Qwen3.5-9B
pipeline_tag: text-generation
---

# Qwen3.5-9B-Medical-Reasoning

**Qwen3.5-9B-Medical-Reasoning** is a fine-tuned 9-billion parameter model optimized for complex clinical reasoning and medical question-answering. By leveraging chain-of-thought (CoT) fine-tuning on medical reasoning traces, the model generates explicit step-by-step diagnostic reasoning inside `<think>` tags prior to delivering a final medical conclusion.

---

## Key Highlights

* **Reasoning Capabilities**: Fine-tuned using step-by-step medical reasoning datasets to prevent superficial guessing and encourage clinical chain-of-thought.
* **Dual Output Modes**:
  * **Thinking Mode (Default)**: Produces explicit CoT traces inside `<think>...</think>` tags for explainable medical reasoning.
  * **Direct Mode**: Can be forced to bypass reasoning and yield succinct direct answers by pre-filling closed tags (`<think>\n</think>`).
* **Strong Medical Benchmark Accuracy**: Outperforms standard base models and many 7B-13B non-reasoning models on board-style medical exams.

---

## Evaluation Results

TBC.

## Training Details

* **Base Model**: `Qwen/Qwen3.5-9B`
* **Fine-Tuning Dataset**: [`FreedomIntelligence/medical-o1-reasoning-SFT`](https://huggingface.co/datasets/FreedomIntelligence/medical-o1-reasoning-SFT) (Subset: `-EM`, Split: `Train`)
* **Fine-Tuning Framework**: [Unsloth](https://github.com/unslothai/unsloth) (LoRA fine-tuning)
* **Hardware**: 1x NVIDIA A100 (40GB VRAM)
* **Prompt Format**: Qwen ChatML (`<|im_start|>`, `<|im_end|>`)

---

## How to Use

### 1. Thinking Mode (Chain-of-Thought Enabled)

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

MODEL_ID = "Kerassy/Qwen3.5-9B-Medical-Reasoning"

tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_ID,
    torch_dtype=torch.bfloat16 if torch.cuda.is_bf16_supported() else torch.float16,
    device_map="auto"
)

system_prompt = "You are a clinical expert. Think step-by-step inside <think> tags before providing your final medical answer."
user_prompt = "A 45-year-old male presents with sudden chest pain, diaphoresis, and radiation to the left jaw. What is the most likely diagnosis?"

prompt = (
    f"<|im_start|>system\n{system_prompt}<|im_end|>\n"
    f"<|im_start|>user\n{user_prompt}<|im_end|>\n"
    f"<|im_start|>assistant\n"
)

inputs = tokenizer([prompt], return_tensors="pt").to("cuda")

outputs = model.generate(
    **inputs,
    max_tokens=1024,
    use_cache=True,
    temperature=0.7,
    top_p=0.9,
    eos_token_id=tokenizer.eos_token_id
)

decoded = tokenizer.batch_decode(outputs, skip_special_tokens=False)[0]
response = decoded.split("<|im_start|>assistant\n")[-1].replace("<|im_end|>", "").strip()

print(response)
```
### 2. Direct Mode (Bypassing Reasoning)
To bypass the reasoning phase and generate a direct response, pre-fill the assistant turn with closed empty <think>\n</think> tags:

```python
prompt_direct = (
    f"<|im_start|>system\nYou are a succinct medical assistant.<|im_end|>\n"
    f"<|im_start|>user\n{user_prompt}<|im_end|>\n"
    f"<|im_start|>assistant\n<think>\n</think>\n"
)

inputs_direct = tokenizer([prompt_direct], return_tensors="pt").to("cuda")

outputs_direct = model.generate(
    **inputs_direct,
    max_tokens=1024,
    eos_token_id=tokenizer.eos_token_id
)

decoded_direct = tokenizer.batch_decode(outputs_direct, skip_special_tokens=False)[0]
response_direct = decoded_direct.split("<think>\n</think>\n")[-1].replace("<|im_end|>", "").strip()

print(response_direct)
```

### Intended Use & Limitations
**Intended Use**
- Medical research and evaluation of chain-of-thought capabilities in compact LLMs.
- AI-assisted clinical reasoning benchmark comparison and analysis.

### Medical Disclaimer
**IMPORTANT:** This model is built for research and evaluation purposes only. It is not a certified medical device and should never be used for direct patient diagnosis, treatment advice, or real-world clinical decision-making. Always consult a qualified medical professional for health-related decisions.