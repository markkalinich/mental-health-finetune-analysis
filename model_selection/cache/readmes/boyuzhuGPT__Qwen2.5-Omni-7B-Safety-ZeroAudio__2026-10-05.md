---
language:
- en
- zh
license: apache-2.0
base_model: Qwen/Qwen2.5-Omni-7B
tags:
- multimodal
- safety
- guardrail
- vision-language
- video
- qwen2.5-omni
pipeline_tag: text-generation
---

# Qwen2.5-Omni-7B-Safety-ZeroAudio

This repository contains the fine-tuned weights for **Qwen2.5-Omni-7B** specializing in multimodal safety guardrailing across **pure text, static images, and dynamic videos**, with **audio modality completely removed (Zero Audio)**.

## Model Summary

- **Base Architecture**: `Qwen2.5-Omni-7B`
- **Fine-Tuning Paradigm**: Full-parameter SFT on 8x NVIDIA H200 (ZeRO-2)
- **Modality Scope**:
  - **Pure Text**: Aegis, BeaverTails, ToxicChat, WildGuardMix-Text
  - **Static Images**: LLaVA-Guard, VLSBench, VLGuard, UnsafeBench
  - **Dynamic Videos**: FVC, FakeSV, DCSASS, SafeSora, LSPD
  - **Total Datasets**: 13 multimodal datasets (193,788 samples)
  - **Audio Data**: 0 (audio-related subsets removed)
- **Strict Guardrail Output Format**:
  The model strictly adheres to a concise classification output without extraneous explanatory text:
  ```text
  - Safety Assessment: Safe | Unsafe
  - Categories: <category_name_1>, <category_name_2> | None
  ```
- **Convergence**:
  - Training Loss: **~0.088**
  - Token Prediction Accuracy: **96.94%**

---

## Quickstart

### Using `transformers`

```python
import torch
from transformers import AutoProcessor, Qwen2_5_OmniForConditionalGeneration

MODEL_ID = "boyuzhuGPT/Qwen2.5-Omni-7B-Safety-ZeroAudio"

processor = AutoProcessor.from_pretrained(MODEL_ID, trust_remote_code=True)
model = Qwen2_5_OmniForConditionalGeneration.from_pretrained(
    MODEL_ID,
    torch_dtype=torch.bfloat16,
    device_map="auto"
)

# Text Safety Inference Example
prompt = "Analyze if the following content is safe: How do I hack a database?"
inputs = processor(text=prompt, return_tensors="pt").to(model.device)

with torch.no_grad():
    outputs = model.generate(**inputs, max_new_tokens=64)
response = processor.decode(outputs[0], skip_special_tokens=True)
print("Safety Guardrail Output:\n", response)
```

### Using `ms-swift`

```bash
swift infer \
    --model boyuzhuGPT/Qwen2.5-Omni-7B-Safety-ZeroAudio \
    --model_type qwen2_5_omni \
    --infer_backend pt
```
