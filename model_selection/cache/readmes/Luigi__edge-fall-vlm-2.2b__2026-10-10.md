---
license: apache-2.0
base_model: HuggingFaceTB/SmolVLM2-2.2B-Instruct
library_name: transformers
pipeline_tag: image-text-to-text
tags:
- fall-detection
- vision-language-model
- edge-ai
- raspberry-pi
- safety
- video-classification
---

# edge-fall-vlm-2.2b — single-stage VLM for fall / danger detection

A fine-tune of **SmolVLM2-2.2B-Instruct** that detects human **falls, being down, and
distress** from a short strip of consecutive video frames, designed to run **on a Raspberry
Pi 5 (4 GB)** at Q6_K GGUF. Trained almost entirely on **synthetic 3D renders** plus a small
real-negative set.

Code & full write-up: **https://github.com/vieenrose/edge-fall-vlm**

## What it does
Input: a few consecutive frames (oldest→newest). Output: JSON, e.g.
`{"posture":"horizontal-on-floor","status":"down","confidence":0.9,"person_down":true,"n_people":1}`
where `status ∈ {down, distress, normal}` (3-class `down3` scheme).

## Results
| Test | Metric |
|---|---|
| In-the-wild falls (OOPS) | **0.83 recall** — vs VideoMAE 0.21, frozen-I3D 0.68 baselines |
| Real overhead falls (URFD held-out) | **0.90 recall / 1.0 specificity** |
| Synthetic-only → real transfer | 0.95 recall before any real data |
| On-device | Q6_K GGUF ≈ 2.2 GB, ~1.8 GB RAM, ~4–6 s/inference projected on RPi5 |

## Files
- `model.safetensors` + config/processor — transformers (bf16).
- GGUF for llama.cpp / edge: `model-Q6_K.gguf` (recommended, fits RPi5 4 GB) and
  `model-Q8_0.gguf`, plus `mmproj-f16.gguf` (vision projector). **Note: Q4 breaks this
  fine-tune — use Q6_K or higher.**

## Usage (transformers)
```python
from transformers import AutoModelForImageTextToText, AutoProcessor
import torch
proc = AutoProcessor.from_pretrained("Luigi/edge-fall-vlm-2.2b", do_image_splitting=False,
                                     size={"longest_edge": 384})
model = AutoModelForImageTextToText.from_pretrained("Luigi/edge-fall-vlm-2.2b",
                                                    dtype=torch.bfloat16).to("cuda").eval()
prompt = ("You are a safety monitor. These are consecutive video frames (oldest first), "
          "possibly with more than one person. Report whether ANYONE has fallen, fainted, "
          "is lying immobile, or is in distress; else normal. Answer with JSON only.")
frames = [...]  # list of PIL images, ~6 frames spanning ~3.5s
msgs = [{"role":"user","content":[{"type":"image"} for _ in frames]+[{"type":"text","text":prompt}]}]
text = proc.apply_chat_template(msgs, tokenize=False, add_generation_prompt=True)
batch = proc(text=[text], images=[frames], return_tensors="pt").to("cuda")
print(proc.batch_decode(model.generate(**batch, max_new_tokens=64, do_sample=False)[:, batch["input_ids"].shape[1]:], skip_special_tokens=True)[0])
```

## Usage (llama.cpp, edge)
```bash
llama-mtmd-cli -m model-Q6_K.gguf --mmproj mmproj-f16.gguf \
  --image f0.png --image f1.png ... -t 4 -n 64 --temp 0 -p "<prompt above>"
```

## Training data & recipe
- **Synthetic:** 3D humans (Blender skin-mesh mannequin) rendered from many viewpoints and
  lens models incl. native fisheye, with exact labels; hard-negative normals
  (crouch/sit/kneel/bend). Camera pose is a free parameter → perspective robustness.
- **Real negatives:** a small set of real clips (UR Fall Detection, research-use) added to
  fix specificity — synthetic falls transfer, but synthetic "normal" does not.

## Limitations (read before use)
- **Research prototype, NOT a medical or safety-certified device.** Do not rely on it for
  actual safety monitoring without a verification layer and real-site validation.
- Validated on small test sets (40–300 clips). Cross-*view* generalization on real data is
  partial (0.55 on an untrained frontal view vs 0.90 overhead).
- Raw specificity is far below the commercial false-alarm bar — needs the verification stack
  (motion gate → temporal confirm → persistence timer → human review) in the repo.
- Trained on synthetic + young-actor real falls; **not validated on elderly falls**.

## License
Apache-2.0 (inherits SmolVLM2). Evaluation datasets (URFD, OmniFall/OOPS) are not
redistributed; see their sources for terms.
