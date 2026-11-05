---
license: apache-2.0
base_model: Qwen/Qwen3.5-2B
library_name: transformers
pipeline_tag: image-text-to-text
tags:
- fall-detection
- vision-language-model
- safety
- video-classification
---

# edge-fall-vlm-qwen3.5-2b — fall / danger detection VLM (quality-first variant)

A full fine-tune of **Qwen3.5-2B** (Qwen's native image-text-to-text architecture) that
detects human **falls, being down, and distress** from a short strip of consecutive video
frames. This is a sibling model to
[`edge-fall-vlm-2.2b`](https://huggingface.co/Luigi/edge-fall-vlm-2.2b) (SmolVLM2-2.2B),
chosen for **capability over edge-device footprint** — see the honest trade-off below.

Code & full write-up: **https://github.com/vieenrose/edge-fall-vlm**

## What it does
Input: a few consecutive frames (oldest→newest). Output: JSON, e.g.
`{"posture":"horizontal-on-floor","status":"down","confidence":0.9,"person_down":true,"n_people":1}`
where `status ∈ {down, distress, normal}` (3-class `down3` scheme).

## Why this model exists (honest story)
`edge-fall-vlm-2.2b` (SmolVLM2-2.2B) has strong recall on our in-the-wild benchmark, but a
real user-submitted clip (an elderly person falling from a bent/reaching position near a
chair, in a cluttered, low-light room) was missed by every variant of it we tried —
including three separate rounds of synthetic-data improvement (more fall-type coverage,
procedural occlusion, and real photo-textured occlusion + indoor HDRI lighting). None of
those closed the gap. Testing a **different base architecture** on the exact same clip did:
`Qwen3.5-2B`, fine-tuned with the *same* recipe/data as the SmolVLM2 model (no extra
synthetic enrichment), correctly detected the fall — the only model in the investigation
to do so, verified across multiple frame windows spanning the actual fall event.

## Results (OOPS in-the-wild benchmark, n=210 combined val+test — the real trade-off)
| Model | Accuracy | Recall (danger) | This specific hard real clip |
|---|---|---|---|
| edge-fall-vlm-2.2b (SmolVLM2) | 0.800 | **0.897** | Missed |
| **edge-fall-vlm-qwen3.5-2b (this model)** | **0.847** | 0.784 | **Detected** |

This is a genuine trade-off, not a strict improvement: SmolVLM2-2.2B has meaningfully
better recall on the general in-the-wild population (catches more everyday falls), while
this Qwen3.5-2B model has better overall accuracy/specificity and uniquely handled one
particularly hard case (elderly subject, furniture occlusion, patterned-fabric camouflage,
low light). Chosen here because **quality/capability on hard real cases was prioritized
over raw recall-rate optimization** for this deployment — if maximizing general recall is
the priority, `edge-fall-vlm-2.2b` may be the better choice; see that model's card.

## Training data & recipe
Same as `edge-fall-vlm-2.2b`, for a clean architecture comparison:
- **Synthetic:** 3D humans (Blender skin-mesh mannequin) rendered from many viewpoints and
  lens models incl. native fisheye, with exact labels; hard-negative normals
  (crouch/sit/kneel/bend).
- **Real negatives:** UR Fall Detection dataset clips (research-use), oversampled, to fix
  specificity.
- Full fine-tune (not LoRA), `down3` label scheme, balanced oversampling.

## Usage (transformers)
```python
from transformers import AutoModelForImageTextToText, AutoProcessor
import torch
proc = AutoProcessor.from_pretrained("Luigi/edge-fall-vlm-qwen3.5-2b", do_image_splitting=False,
                                     size={"shortest_edge": 64*64, "longest_edge": 384*384})
model = AutoModelForImageTextToText.from_pretrained("Luigi/edge-fall-vlm-qwen3.5-2b",
                                                    dtype=torch.bfloat16).to("cuda").eval()
prompt = ("You are a safety monitor. These are consecutive video frames (oldest first), "
          "possibly with more than one person. Report whether ANYONE has fallen, fainted, "
          "is lying immobile, or is in distress; else normal. Answer with JSON only.")
frames = [...]  # list of PIL images, ~6 frames spanning ~3.5s
msgs = [{"role":"user","content":[{"type":"image"} for _ in frames]+[{"type":"text","text":prompt}]}]
text = proc.apply_chat_template(msgs, tokenize=False, add_generation_prompt=True, enable_thinking=False)
batch = proc(text=[text], images=[frames], return_tensors="pt").to("cuda")
print(proc.batch_decode(model.generate(**batch, max_new_tokens=64, do_sample=False)[:, batch["input_ids"].shape[1]:], skip_special_tokens=True)[0])
```

**Important:** always pass `enable_thinking=False` to `apply_chat_template` — Qwen's chat
template defaults to injecting a `<think>` block, which without this flag causes the model
to ramble into open-ended reasoning instead of emitting the trained JSON format directly.

## Limitations (read before use)
- **Research prototype, NOT a medical or safety-certified device.**
- Lower recall than the SmolVLM2 sibling model on the general in-the-wild benchmark — see
  the trade-off table above. Pick the model that matches your priority (general recall vs.
  hard-case robustness).
- Still misses the fully-settled, heavily-occluded aftermath of the hard real clip that
  motivated this model — it catches the *dynamic fall event*, not every frame after.
- Validated on small test sets (60-210 clips).
- Not validated on elderly falls as a *systematic* category (the one hard clip is a single
  data point, not a validated subpopulation result).

## License
Apache-2.0 (inherits Qwen3.5). Evaluation datasets (URFD, OmniFall/OOPS) are not
redistributed; see their sources for terms.
