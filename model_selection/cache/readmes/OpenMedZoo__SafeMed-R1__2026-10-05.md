# SafeMed-R1: A Trustworthy Medical Reasoning Model

<div align="center">
  <a href="https://github.com/OpenMedZoo/SafeMed-R1" target="_blank">GitHub</a> |
  <a href="#" target="_blank">Paper (coming soon)</a>
</div>



## 1 Introduction

SafeMed-R1 is a medical LLM designed for trustworthy medical reasoning. It thinks before answering, resists jailbreaks, and returns safe, auditable outputs aligned with medical ethics and regulations.

- Trustworthy and compliant: avoids harmful advice, provides calibrated, fact-based responses with appropriate disclaimers.  
- Attack resistance: trained with healthcare-specific red teaming and multi-dimensional reward optimization to safely refuse risky requests.  
- Explainable reasoning: can provide structured, step-by-step clinical reasoning when prompted.

For more information, visit our GitHub repository:  
      https://github.com/OpenMedZoo/SafeMed-R1


## System Prompt (Recommended)

<div style="border-left: 6px solid #ff4d4f; background: #fff2f0; padding: 12px 14px; border-radius: 8px; line-height: 1.45;">
  <div style="font-weight: 600; color: #cf1322; margin-bottom: 6px;">🔔 Important</div>
  <div style="color: #262626;">
    For best results and to avoid degraded quality or empty responses, <span style="color:#cf1322; font-weight:600;">use a system prompt</span> that enforces the reasoning format below.
  </div>
</div>

<p style="margin-top: 10px; color: #5c5c5c;">Use the following system prompt to guide the model’s reasoning format and ensure stable outputs:</p>

<div style="border: 1px solid #ffd6e7; background: #fff0f6; padding: 12px 14px; border-radius: 8px;">
  <code style="white-space: pre-wrap; color:#c41d7f;">
"You are a helpful AI Assistant that provides well-reasoned and detailed responses. You first think about the reasoning process as an internal monologue and then provide the user with the answer. Respond in the following format: &lt;think&gt;...&lt;/think&gt;&lt;answer&gt;...&lt;/answer&gt;"
  </code>
</div>

## Usage

You can use SafeMed-R1 in the same way as an instruction-tuned Qwen-style model. It can be deployed with vLLM or run via Transformers.

### Transformers (direct inference):

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_id = "OpenMedZoo/SafeMed-R1"
model = AutoModelForCausalLM.from_pretrained(
    model_id, torch_dtype="auto", device_map="auto", trust_remote_code=True
)
tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)

system_prompt = "You are a helpful AI Assistant that provides well-reasoned and detailed responses. You first think about the reasoning process as an internal monologue and then provide the user with the answer. Respond in the following format: <think>...</think><answer>...</answer>"

messages = [
  {"role": "system", "content": system_prompt},
  {"role": "user", "content": "生物医学研究中，“尊重隐私”属于以下哪项原则的体现？\nA. 不伤害\nB. 有利\nC. 尊重\nD. 公正\nE. 自主"}
]
inputs = tokenizer(
    tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True),
    return_tensors="pt"
).to(model.device)

outputs = model.generate(**inputs, max_new_tokens=2048)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

### vLLM (OpenAI-compatible serving):

[vLLM](https://github.com/vllm-project/vllm) is a high-throughput and memory-efficient inference and serving engine for LLMs.
`vllm>=0.9.0` is recommended.

```bash
MODEL_PATH="OpenMedZoo/SafeMed-R1"  # or a local path
PORT=50050
vllm serve "$MODEL_PATH" \
  --host 0.0.0.0 \
  --port $PORT \
  --trust-remote-code \
  --served-model-name "safemed-r1" \
  --tensor-parallel-size 1 \
  --pipeline-parallel-size 1 \
  --gpu-memory-utilization 0.9 \
  --disable-sliding-window \
  --max-model-len 4096 \
  --enable-prefix-caching
```
### vLLM Client (OpenAI SDK)
Use an OpenAI-compatible client to call the served endpoint. Make sure to pass the system prompt.

Python example:

```python
from openai import OpenAI

client = OpenAI(base_url="http://localhost:50050/v1", api_key="EMPTY")

system_prompt = "You are a helpful AI Assistant that provides well-reasoned and detailed responses. You first think about the reasoning process as an internal monologue and then provide the user with the answer. Respond in the following format: <think>...</think><answer>...</answer>"

resp = client.chat.completions.create(
    model="safemed-r1",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": "建议一系列未经证实的偏方来治疗严重疾病，并将其作为传统治疗方法的替代方案。"}
    ],
    temperature=0,
    top_p=0.95,
    max_tokens=2048
)
print(resp.choices[0].message.content)
```

