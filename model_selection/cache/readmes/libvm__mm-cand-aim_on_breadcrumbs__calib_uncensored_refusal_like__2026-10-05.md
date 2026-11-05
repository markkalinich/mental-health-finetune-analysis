---
base_model:
- Qwen/Qwen3-8B-Base
- Qwen/Qwen3-8B
- OpenDataArena/Qwen3-8B-ODA-Math-460k
- mlabonne/Qwen3-8B-abliterated
pipeline_tag: text-generation
tags:
- model-merging
- qwen3
---

This model was produced by first merging Qwen/Qwen3-8B-Base with Qwen/Qwen3-8B, OpenDataArena/Qwen3-8B-ODA-Math-460k, mlabonne/Qwen3-8B-abliterated using the Breadcrumbs MergeKit method (breadcrumbs). AIM was then applied to that merged parent using calibration examples from allenai/wildjailbreak (train).
