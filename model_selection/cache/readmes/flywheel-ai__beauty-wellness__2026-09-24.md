---
license: apache-2.0
base_model: Qwen/Qwen3.6-35B-A3B
library_name: transformers
pipeline_tag: text-generation
tags:
  - flywheel
  - opspot
  - vertical-ai-employee
  - beauty-wellness
  - gguf
---

# Flywheel — beauty-wellness (35b-v1.1)

An open-source **vertical AI-employee** model from [Flywheel by OpSpot](https://opspot.ai),
fine-tuned (LoRA) from `Qwen/Qwen3.6-35B-A3B` (Apache-2.0) for the **beauty-wellness** domain.

Warm front-desk and operations assistant for salons, spas, and med-spas: booking and rescheduling, service-menu and pricing questions, retail recommendations, memberships and packages, and routine aftercare.

- **Base:** Qwen/Qwen3.6-35B-A3B  ·  **License:** Apache-2.0  ·  **Version:** 35b-v1.1
- **Formats:** safetensors (transformers / vLLM, ~65G) + `model-q4_k_m.gguf` (llama.cpp / Ollama, ~20G)

## Download (one command)

```bash
pip install -U huggingface_hub
hf download flywheel-ai/beauty-wellness                      # full repo (safetensors + GGUF)
hf download flywheel-ai/beauty-wellness model-q4_k_m.gguf    # just the GGUF
```

## Run

```bash
# llama.cpp
llama-server -m model-q4_k_m.gguf -ngl 999
# Ollama (pulls the GGUF straight from HF)
ollama run hf.co/flywheel-ai/beauty-wellness
# vLLM (serves the safetensors)
vllm serve flywheel-ai/beauty-wellness
```

## Guardrail

Not medical advice; anything touching a contraindication (pregnancy, skin reactions, prescription retinoids, allergies, post-procedure care) is deferred to a licensed dermatologist or physician.

## Provenance & honesty

v1.0 is trained on **synthetic seed data** authored by permissively-licensed local models
(Apache/MIT teachers only — never distilled from closed models). On general prompts it is
roughly on par with the base; the niche edge sharpens as **consented** real usage flows through
the OpSpot flywheel. Built on Qwen3.6 (Apache-2.0).
