---
license: apache-2.0
base_model: LiquidAI/LFM2.5-VL-450M
tags:
  - satellite
  - triage
  - remote-sensing
  - vision-language-model
  - lfm2_vl
  - lora
  - fine-tuned
datasets:
  - xiang709/VRSBench
pipeline_tag: image-text-to-text
---

# LFM2.5-VL-450M — Satellite Image Triage

Fine-tuned [LFM2.5-VL-450M](https://huggingface.co/LiquidAI/LFM2.5-VL-450M) for on-board satellite image triage. Given a satellite image, the model outputs a JSON object with a description, priority level, reasoning, and categories — enabling autonomous downlink decisions.

Part of the **automatic-downlink** project for the [Liquid AI x DPhi Space "AI in Space" Hackathon](https://www.dphi.tech/challenges/ai-in-space-hackathon).

## Usage

```python
from transformers import AutoModelForImageTextToText, AutoProcessor
from PIL import Image
import torch

model = AutoModelForImageTextToText.from_pretrained(
    "marcelo-earth/LFM2.5-VL-450M-satellite-triage",
    dtype=torch.float16,
)
# Processor must be loaded from base model
processor = AutoProcessor.from_pretrained("LiquidAI/LFM2.5-VL-450M")

image = Image.open("satellite_image.png").convert("RGB")

conversation = [
    {"role": "system", "content": [{"type": "text", "text": "You are a satellite image triage system. Analyze the image and respond ONLY with a JSON object."}]},
    {"role": "user", "content": [
        {"type": "image", "image": image},
        {"type": "text", "text": "Triage this satellite image. Respond with JSON only."},
    ]},
]

inputs = processor.apply_chat_template(
    conversation, add_generation_prompt=True,
    return_tensors="pt", return_dict=True, tokenize=True,
)
output_ids = model.generate(**inputs, max_new_tokens=512, temperature=0.1, do_sample=True)
generated = output_ids[0, inputs["input_ids"].shape[1]:]
print(processor.decode(generated, skip_special_tokens=True))
```

**Output:**
```json
{"description": "Densely populated urban area with residential and commercial buildings and a small harbor", "priority": "MEDIUM", "reasoning": "Routine scene with identifiable features — standard downlink", "categories": ["urban", "infrastructure"]}
```

## Training

- **Base model:** LiquidAI/LFM2.5-VL-450M
- **Method:** LoRA SFT (rank 16, alpha 32) via [leap-finetune](https://github.com/LiquidAI/leap-finetune)
- **Data:** 20,264 caption-only samples from [VRSBench](https://huggingface.co/datasets/xiang709/VRSBench), converted to triage JSON format with heuristic priority labels
- **Training:** 2 epochs on Modal H100, lr=1e-4, batch size 4, vision encoder lr multiplier 0.1
- **Eval loss:** 0.83 (epoch 2)

### Data Pipeline

VRSBench contains 142K items across 3 task types. Only the 20,264 `[caption]` items were used — VQA and referring tasks were filtered out. Captions were converted to triage JSON with keyword-based priority assignment:

| Priority | Count | Example Keywords |
|----------|-------|-----------------|
| MEDIUM | 16,896 | urban, building, road, vehicle |
| LOW | 1,945 | desert, barren, sparse |
| SKIP | 1,277 | cloud, ocean, haze |
| HIGH | 142 | deforestation, construction |
| CRITICAL | 4 | fire, flood |

## Evaluation vs Base Model

Tested on 4 Sentinel-2 satellite images:

| Metric | Base Model | Fine-tuned |
|--------|-----------|------------|
| Valid JSON | 66% | **100%** |
| Correct priority | 33% | **100%** |
| Unique descriptions | 33% | **100%** |
| Correct schema | 33% | **100%** |

The base model copies few-shot examples verbatim and wraps output in markdown fences. The fine-tuned model produces image-specific descriptions with correct triage JSON schema.

## Limitations

- Trained on VRSBench (Google Earth imagery), not Sentinel-2 directly — some domain gap expected
- Priority labels are heuristic, not human-annotated
- Only 2 of 3 planned epochs completed (eval loss was still decreasing)
- 450M parameters limits description quality compared to larger VLMs
