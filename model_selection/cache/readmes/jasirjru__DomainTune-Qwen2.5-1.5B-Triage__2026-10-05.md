---
license: apache-2.0
base_model: Qwen/Qwen2.5-1.5B
tags:
- fine-tuned
- qlora
- ticket-triage
- structured-extraction
- json
pipeline_tag: text-generation
---

# DomainTune: Autonomous Ticket Triage LLM

DomainTune is an enterprise-grade fine-tuned model based on `Qwen/Qwen2.5-1.5B`. It is specifically optimized to read messy, unstructured software bug reports and support tickets and output strict, deterministic JSON triage decisions.

## 🎯 Model Capabilities
Given a raw support ticket or GitHub issue, DomainTune extracts:
- **`priority`**: `P1` (critical outage) | `P2` (high severity) | `P3` (normal) | `P4` (minor/cosmetic)
- **`category`**: `bug` | `feature_request` | `documentation` | `performance` | `security` | `infra`
- **`affected_component`**: The specific system or module impacted (e.g. `auth_service`, `payment_gateway`, `database`)
- **`sentiment`**: `neutral` | `frustrated` | `urgent` | `satisfied`
- **`resolution_required`**: `true` | `false`

## 🚀 Quickstart & Inference

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "jasirjru/DomainTune-Qwen2.5-1.5B-Triage"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.float16,
    device_map="auto"
)

# Example ticket
ticket = """Title: Production payment gateway timeout on checkout
Description: Customers in us-east are receiving HTTP 504 errors when processing Stripe payments. Multiple checkout failures recorded in Datadog."""

prompt = f"<|im_start|>system\nYou are a support ticket triage assistant. Output only valid JSON.<|im_end|>\n<|im_start|>user\n{ticket}<|im_end|>\n<|im_start|>assistant\n"

inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
with torch.no_grad():
    outputs = model.generate(**inputs, max_new_tokens=150, do_sample=False)

print(tokenizer.decode(outputs[0][inputs.input_ids.shape[1]:], skip_special_tokens=True))
