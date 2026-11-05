---
license: apache-2.0
language:
  - en
  - ja
library_name: transformers
pipeline_tag: image-text-to-text
base_model: mistral-community/pixtral-12b
tags:
  - construction-safety
  - hazard-detection
  - vision-language
  - lora
  - distillation
  - vllm
  - mistral
datasets:
  - keremberke/construction-safety-object-detection
  - Francesco/construction-safety-gsnvb
---

# Pixtral 12B — Construction Safety VQA

A fine-tuned [Pixtral 12B](https://huggingface.co/mistral-community/pixtral-12b) for **construction site hazard detection and classification**. Distilled from Qwen3.5-27B teacher annotations using LoRA, this model outputs structured JSON with bounding boxes, severity levels, and bilingual (EN/JP) descriptions.

Built for [**Mistral EvoBoard**](https://github.com/TakashiShibata/Mistral-Hackathon-2026) — an AI Safety Committee that runs multi-agent debates on construction site images.

## Key Results

| Metric | Base Pixtral 12B | Fine-tuned (this model) | Delta |
|--------|:-:|:-:|:-:|
| **Violation Recall** | 0.302 | **0.790** | **+48.8 pp** |
| **Violation Accuracy** | 0.600 | **0.920** | **+32.0 pp** |
| Helmet Recall | 0.771 | 0.804 | +3.3 pp |
| Detection Precision | 0.850 | 0.855 | +0.5 pp |

> Evaluated on 50 COCO-format hardhat detection test images. The model dramatically improves **violation recall** — the ability to detect missing PPE — which is the most safety-critical metric.

## Usage

### With vLLM (recommended)

```bash
vllm serve a1273352/pixtral-12b-construction-safety \
  --tensor-parallel-size 2 \
  --max-model-len 8192 \
  --port 8200
```

```python
from openai import OpenAI

client = OpenAI(base_url="http://localhost:8200/v1", api_key="dummy")

response = client.chat.completions.create(
    model="a1273352/pixtral-12b-construction-safety",
    messages=[{
        "role": "user",
        "content": [
            {"type": "image_url", "image_url": {"url": "https://example.com/site.jpg"}},
            {"type": "text", "text": VISION_PROMPT},  # see below
        ],
    }],
    max_tokens=4096,
    temperature=0.1,
)
```

### With Transformers

```python
from transformers import AutoProcessor, LlavaForConditionalGeneration
from PIL import Image

model = LlavaForConditionalGeneration.from_pretrained(
    "a1273352/pixtral-12b-construction-safety",
    torch_dtype="bfloat16",
    device_map="auto",
)
processor = AutoProcessor.from_pretrained("a1273352/pixtral-12b-construction-safety")

image = Image.open("construction_site.jpg")
inputs = processor(text=VISION_PROMPT, images=image, return_tensors="pt").to(model.device)
outputs = model.generate(**inputs, max_new_tokens=4096, temperature=0.1)
print(processor.decode(outputs[0], skip_special_tokens=True))
```

## Vision Prompt

The model was trained with this bilingual prompt (use it at inference for best results):

```
You are a construction safety vision system. Analyze the provided image of a construction site and identify ALL safety hazards.

For each hazard detected, provide:
1. type: Category — one of: fall_hazard, electrical_hazard, ppe_violation, equipment_hazard, public_safety, structural_hazard, cable_hazard, environmental_hazard
2. description: Bilingual description — English first, then Japanese in parentheses
3. confidence: 0.0–1.0
4. location: Bounding box as {x, y, width, height} in percentage of image (0–100)
5. severity: low / medium / high / critical

Also provide:
- site_type: "high_rise" | "road_construction" | "renovation" | "other"
- site_description: Bilingual description of the construction site
- environmental_conditions: weather, lighting, ground_condition

Return ONLY valid JSON.
```

## Output Format

```json
{
  "site_type": "high_rise",
  "site_description": "Multi-story building under construction with exposed steel framework (鉄骨フレームが露出した多層建築工事現場)",
  "hazards": [
    {
      "id": "H1",
      "type": "ppe_violation",
      "description": "Worker without hard hat near scaffolding (足場付近でヘルメット未着用の作業員)",
      "confidence": 0.92,
      "severity": "critical",
      "location": { "x": 35.2, "y": 42.1, "width": 8.5, "height": 15.3 }
    }
  ],
  "environmental_conditions": {
    "weather": "clear",
    "lighting": "daylight",
    "ground_condition": "dry"
  }
}
```

## Training Details

### Method

**Teacher Distillation with LoRA** — Qwen3.5-27B (served via vLLM) annotated ~950 construction site images with structured hazard JSON. The annotations were used to fine-tune Pixtral 12B via LoRA using MS-Swift + DeepSpeed ZeRO-2.

### Dataset

| | Count |
|--|:-:|
| Source images | 1,001 |
| Annotated images | 950 |
| Training samples | 2,520 (2 prompt variants per image) |
| Validation samples | 114 |

**Image sources:**
- [keremberke/construction-safety-object-detection](https://huggingface.co/datasets/keremberke/construction-safety-object-detection) (~398 images)
- [Francesco/construction-safety-gsnvb](https://huggingface.co/datasets/Francesco/construction-safety-gsnvb) (600 images)
- Internal reference images (37 images)

### Hyperparameters

| Parameter | Value |
|-----------|-------|
| LoRA rank | 8 |
| LoRA alpha | 32 |
| LoRA dropout | 0.05 |
| Target modules | all-linear |
| Learning rate | 1e-4 |
| ViT learning rate | 1e-5 |
| Aligner learning rate | 1e-5 |
| Epochs | 5 |
| Batch size | 1 (x4 grad accum x4 GPUs = effective 16) |
| Max sequence length | 4096 |
| Warmup ratio | 0.05 |
| Precision | bfloat16 |
| Optimizer | AdamW (DeepSpeed ZeRO-2) |

### Hardware

- 4x NVIDIA H200 (141 GB) for training
- 2x NVIDIA H200 for inference (vLLM, tensor parallel)

## Hazard Categories

| Type | Description |
|------|-------------|
| `fall_hazard` | Unguarded edges, missing guardrails, unsafe scaffolding |
| `ppe_violation` | Missing hard hat, no safety vest, absent goggles |
| `electrical_hazard` | Exposed wiring, unsafe power tool usage |
| `equipment_hazard` | Improperly secured machinery, crane risks |
| `structural_hazard` | Unstable structures, compromised load-bearing elements |
| `cable_hazard` | Tripping hazards from cables and hoses |
| `public_safety` | Risks to bystanders, inadequate barriers |
| `environmental_hazard` | Wet surfaces, poor lighting, extreme weather effects |

## Evaluation

Evaluated using W&B Weave with 4 custom scorers:

- **JsonValidityScorer** — JSON format compliance
- **HazardF1Scorer** — Hazard type detection F1
- **SeverityAccuracyScorer** — Severity classification accuracy
- **BBoxIoUScorer** — Bounding box IoU

The primary improvement is in **violation recall** (+48.8 pp), which is the most safety-critical metric — missing a PPE violation in a real construction site can lead to injuries or fatalities.

## Limitations

- Trained primarily on outdoor construction sites; indoor renovation scenes may have lower accuracy
- Bounding boxes are approximate (trained from VLM teacher, not manual annotation)
- Environmental condition detection (weather, lighting) is based on visual cues only
- Model inherits biases from the Pixtral 12B base and Qwen3.5-27B teacher

## Citation

```bibtex
@misc{evoboard2026,
  title={Mistral EvoBoard: AI Safety Committee for Construction},
  author={Takashi Shibata},
  year={2026},
  url={https://github.com/TakashiShibata/Mistral-Hackathon-2026}
}
```
