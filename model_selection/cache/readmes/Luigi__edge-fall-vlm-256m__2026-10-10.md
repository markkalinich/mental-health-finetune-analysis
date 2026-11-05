---
license: apache-2.0
base_model: HuggingFaceTB/SmolVLM2-256M-Video-Instruct
library_name: transformers
pipeline_tag: image-text-to-text
tags: [fall-detection, vision-language-model, edge-ai, raspberry-pi, safety]
---

# edge-fall-vlm-256m — 256M fall / danger detector (size-comparison sibling)

A **SmolVLM2-256M-Video-Instruct** fine-tune for fall / person-down / distress detection, same recipe as
[edge-fall-vlm-2.2b](https://huggingface.co/Luigi/edge-fall-vlm-2.2b) but at **256M**.
Published mainly to show **how accuracy scales with VLM size**.

Code: https://github.com/vieenrose/edge-fall-vlm · Demo (pick a size):
https://huggingface.co/spaces/Luigi/edge-fall-vlm-demo

## Accuracy vs size (same recipe, same real test sets)
| Model | URFD (easy) recall/spec | **OOPS in-the-wild recall** |
|---|---|---|
| 256M | 1.0 / 1.0 | **0.13** |
| 500M | 1.0 / 1.0 | **0.31** |
| **2.2B (recommended)** | 0.90 / 1.0 | **0.83** |

**This 256M model saturates the easy in-distribution test but MISSES most real in-the-wild
falls** (recall 0.13). Smaller VLMs fit the training distribution but do not generalize to
novel real footage. **For the actual safety task, use the 2.2B.** This model is useful for
research / the fastest possible on-device path where recall is not safety-critical.

Files: transformers `model.safetensors` + `model-Q8_0.gguf` / `mmproj-f16.gguf`
(llama.cpp). Apache-2.0. Not a medical/safety device.
