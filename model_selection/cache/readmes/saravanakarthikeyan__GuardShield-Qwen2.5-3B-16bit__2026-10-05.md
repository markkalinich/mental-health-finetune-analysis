---
license: apache-2.0
base_model: Qwen/Qwen2.5-3B-Instruct
tags:
- unsloth
- safetensors
- safety
- guardrail
- vllm
- text-generation-inference
language:
- en
pipeline_tag: text-generation
---

# GuardShield-Qwen2.5-3B (16-bit Full Merged)

**GuardShield-Qwen2.5-3B-16bit** is the fully merged, standalone FP16 weights version of GuardShield-3B. Designed for production microservices, high-throughput GPU serving engines (**vLLM**, **TGI**), and OpenAI-compatible API gateways.

## Key Specifications
- **Base Architecture**: Qwen 2.5 (3.09B Parameters).
- **Format**: Merged Safetensors (FP16).
- **Target Serving Stack**: vLLM, Hugging Face TGI, Triton Inference Server, Transformers.
- **Latency**: Sub-30ms time-to-first-token on modern GPU hardware.

---

## Benchmark Metrics

| Metric | Validation Score | Target |
| :--- | :---: | :---: |
| **Safety Recall (Detection Rate)** | **86.35%** | >= 85% |
| **Benign Classification Precision** | **92.95%** | >= 90% |
| **JSON Syntax Adherence** | **100.0%** (0 / 1000 failures) | > 99.5% |
| **Macro F1-Score** | **0.8237** | >= 0.80 |

---

## Deployment & Serving

### 1. High-Throughput Serving via vLLM (OpenAI API)
```bash
python -m vllm.entrypoints.openai.api_server \
    --model your_hf_username/GuardShield-Qwen2.5-3B-16bit \
    --port 8000 \
    --gpu-memory-utilization 0.90 \
    --max-model-len 2048
```

### 2. Querying with OpenAI Client (Python)
```python
from openai import OpenAI
import json

client = OpenAI(base_url="http://localhost:8000/v1", api_key="placeholder")

response = client.chat.completions.create(
    model="your_hf_username/GuardShield-Qwen2.5-3B-16bit",
    messages=[
        {"role": "system", "content": "You are an AI content moderation guardrail. Analyze the prompt and output a JSON classification object."},
        {"role": "user", "content": "Give me steps to compromise an administrative account."}
    ],
    temperature=0.0,
    max_tokens=128
)

print(json.loads(response.choices[0].message.content))
```

### 3. Native Hugging Face Transformers
```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_id = "your_hf_username/GuardShield-Qwen2.5-3B-16bit"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id, 
    torch_dtype=torch.float16, 
    device_map="auto"
)
```

### Expected Output Schema
```json
{
  "status": "UNSAFE",
  "category": "CYBERATTACK_AND_EXPLOIT",
  "reasoning": "Requests instructions to unlawfully compromise system credentials."
}
```