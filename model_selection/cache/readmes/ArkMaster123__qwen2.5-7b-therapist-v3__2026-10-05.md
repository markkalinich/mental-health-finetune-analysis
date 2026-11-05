---
language:
- en
license: apache-2.0
base_model:
- Qwen/Qwen2.5-7B-Instruct
pipeline_tag: text-generation
tags:
- mental-health
- counseling
- therapist
- lora-merged
---

# Qwen2.5-7B Therapist v3

A therapist-oriented model based on [Qwen/Qwen2.5-7B-Instruct](https://huggingface.co/Qwen/Qwen2.5-7B-Instruct), fine-tuned with LoRA on a curated counseling mixture and merged for direct inference.

## Base Model
- [Qwen/Qwen2.5-7B-Instruct](https://huggingface.co/Qwen/Qwen2.5-7B-Instruct)

## Training Data (with gratitude)
This v3 run was trained on a curated mix from the following public datasets:

- [Amod/mental_health_counseling_conversations](https://huggingface.co/datasets/Amod/mental_health_counseling_conversations)
- [nbertagnolli/counsel-chat](https://huggingface.co/datasets/nbertagnolli/counsel-chat)
- [IINOVAII/therapy-conversations-combined](https://huggingface.co/datasets/IINOVAII/therapy-conversations-combined)

Thank you to the dataset creators and contributors for making this work possible.

## Training Notes
- SFT LoRA adapter: `ArkMaster123/qwen2.5-7b-therapist-v3-sft-fast`
- Merged model: `ArkMaster123/qwen2.5-7b-therapist-v3`
- Fast training profile: 120 steps, packed sequences, bf16, H100 multi-GPU run.

## Intended Use
Supportive, empathetic conversational assistance for mental wellness contexts.

## Safety
- Not a substitute for licensed care.
- In crisis or immediate danger, contact local emergency services or a crisis hotline.
