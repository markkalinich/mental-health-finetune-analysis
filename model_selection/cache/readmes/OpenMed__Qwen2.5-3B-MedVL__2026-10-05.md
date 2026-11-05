---
language:
- en
license: apache-2.0
base_model: Qwen/Qwen2.5-VL-3B-Instruct
tags:
  - medical
  - vqa
  - qwen2.5-vl
  - synthvision
pipeline_tag: visual-question-answering
---

# Qwen2.5-3B-MedVL

![SynthVision](synthvision_featured.png)

Qwen2.5-VL-3B-Instruct fine-tuned on ~200K medical VQA records from the SynthVision pipeline.


## Benchmark Results (Exact Match)

| Split | VQA-RAD | PathVQA | SLAKE | Avg EM |
|-------|---------|---------|-------|--------|
| Base (Qwen2.5-VL-3B-Instruct) | 0.5033 | 0.3038 | 0.5438 | 0.4503 |
| **Fine-tuned** | **0.5211** | **0.3468** | **0.6032** | **0.4903** |
| Delta | +3.5% | +14.2% | +10.9% | +8.9% |

## Usage

### Transformers

```python
from transformers import AutoProcessor, AutoModelForImageTextToText

model_id = "OpenMed/Qwen2.5-3B-MedVL"
processor = AutoProcessor.from_pretrained(model_id)
model = AutoModelForImageTextToText.from_pretrained(model_id, torch_dtype="auto", device_map="auto")

messages = [
    {
        "role": "user",
        "content": [
            {"type": "image", "url": "https://example.com/xray.jpg"},
            {"type": "text", "text": "What are the key findings in this chest X-ray?"},
        ],
    }
]

inputs = processor.apply_chat_template(messages, add_generation_prompt=True, tokenize=True, return_dict=True, return_tensors="pt").to(model.device)
output = model.generate(**inputs, max_new_tokens=512)
print(processor.decode(output[0][inputs["input_ids"].shape[-1]:], skip_special_tokens=True))
```

### vLLM

```python
from vllm import LLM, SamplingParams

llm = LLM(model="OpenMed/Qwen2.5-3B-MedVL", max_model_len=4096, limit_mm_per_prompt={"image": 1})

messages = [{"role": "user", "content": [
    {"type": "image_url", "image_url": {"url": "https://example.com/xray.jpg"}},
    {"type": "text", "text": "What are the key findings in this chest X-ray?"},
]}]

output = llm.chat(messages, SamplingParams(temperature=0, max_tokens=512))
print(output[0].outputs[0].text)
```

### SGLang

```bash
# Launch server
python -m sglang.launch_server --model-path OpenMed/Qwen2.5-3B-MedVL --chat-template qwen2-vl --port 8000
```

```python
from openai import OpenAI

client = OpenAI(base_url="http://localhost:8000/v1", api_key="EMPTY")
response = client.chat.completions.create(
    model="OpenMed/Qwen2.5-3B-MedVL",
    messages=[{"role": "user", "content": [
        {"type": "image_url", "image_url": {"url": "https://example.com/xray.jpg"}},
        {"type": "text", "text": "What are the key findings in this chest X-ray?"},
    ]}],
    max_tokens=512,
)
print(response.choices[0].message.content)
```

## Training Details

- **Base model**: [Qwen/Qwen2.5-VL-3B-Instruct](https://huggingface.co/Qwen/Qwen2.5-VL-3B-Instruct)
- **Data**: ~200K medical VQA records from the [SynthVision pipeline](https://huggingface.co/blog/OpenMed/synthvision)
- **Method**: LoRA (rank=32, alpha=32)
- **Target modules**: q_proj, v_proj, k_proj, o_proj
- **Learning rate**: 7e-5, cosine schedule
- **Steps**: 700
- **Weight decay**: 0.03
- **Hardware**: 4x NVIDIA A100 80GB (48 vCPU, 568 GB RAM) via [Hugging Face Jobs](https://huggingface.co/docs/hub/jobs)
- **Training time**: 1h 14m

## Links

- [SynthVision blog post](https://huggingface.co/blog/OpenMed/synthvision)
- [Source code](https://github.com/openmed-labs/synthvision)
- [All SynthVision artifacts](https://huggingface.co/collections/OpenMed/synthvision-69baac655b557943aa1babd3)
- [OpenMed on Hugging Face](https://huggingface.co/OpenMed)
