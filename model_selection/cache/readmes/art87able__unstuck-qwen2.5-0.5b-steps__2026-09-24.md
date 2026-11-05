---
license: apache-2.0
base_model: Qwen/Qwen2.5-0.5B-Instruct
library_name: transformers
pipeline_tag: text-generation
tags:
  - unstuck
  - task-breakdown
  - adhd
  - lora
  - build-small-hackathon
  - small-models
language:
  - en
---

# Unstuck — Qwen2.5-0.5B fine-tuned for ADHD task breakdowns

A tiny (0.5B) instruct model fine-tuned to turn one overwhelming task into **tiny, timed, categorised steps** in the exact JSON schema used by [Unstuck](https://huggingface.co/spaces/build-small-hackathon/unstuck) (HF Build Small Hackathon, Backyard AI track).

It powers Unstuck's `UNSTUCK_BACKEND=finetuned` path — a fully local, serverless-free option that runs the same `generate(prompt) -> str` seam as the app's other backends.

## What it does

Given an overwhelming task, it returns only:

```json
{"steps":[{"text":"Open a trash bag and collect visible rubbish","category":"admin","est_minutes":5}, ...]}
```

- each step a single concrete action starting with an imperative verb,
- one category from `admin · creative · errand · deep-work`,
- a positive-integer minute estimate, **never above 25** (a hard app rule).

## How it was built

- **Base:** `Qwen/Qwen2.5-0.5B-Instruct`.
- **Data:** 130 schema-valid breakdowns **distilled** from a strong serverless model (`Qwen/Qwen3-30B-A3B-Instruct-2507` on Nebius Token Factory), each filtered through Unstuck's own validator so only on-contract examples survive. Purely synthetic — no user data.
- **Method:** LoRA (r=16, α=32, dropout 0.05; q/k/v/o projections), 3 epochs, lr 2e-4, merged into the base. Final train loss ≈ 0.21.
- **Compute:** a single **Modal** A10G GPU. Full pipeline (distill → train → verify): [`scripts/finetune/`](https://github.com/art87able/unstuck/tree/main/scripts/finetune).

## Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

tok = AutoTokenizer.from_pretrained("art87able/unstuck-qwen2.5-0.5b-steps")
model = AutoModelForCausalLM.from_pretrained("art87able/unstuck-qwen2.5-0.5b-steps")
# Feed it Unstuck's breakdown prompt (see unstuck.prompts.breakdown_prompt) and parse the JSON.
```

Or in the app: `UNSTUCK_BACKEND=finetuned python app.py`.

## Limitations

A 0.5B model specialised for one narrow JSON task — it is not a general chat model. Outputs should still be schema-validated (the app does one repair retry on failure). Estimates are starting points; Unstuck recalibrates them to *your* real timings client-side.

- **Source:** https://github.com/art87able/unstuck
- **Live app:** https://huggingface.co/spaces/build-small-hackathon/unstuck
