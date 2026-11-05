---
base_model:
- Qwen/Qwen3.5-4B
library_name: transformers
license: apache-2.0
language:
- en
tags:
- qwen3.5
- ai-safety
- reasoning
- thinking
- alignment
- sft
- gguf
base_model_relation: finetune
pipeline_tag: text-generation
---

<div align="center">

# Qwen3.5-4B-Safety-Thinking

![QwenMerlin](https://cdn-uploads.huggingface.co/production/uploads/67329d3f69fded92d56ab41a/DWJ7JC09BHG3z1q-8-esc.jpeg)

**4B parameters  • 1M context possible • Safety reasoning**

[🤗 Model](https://huggingface.co/MerlinSafety/Qwen3.5-4B-Safety-Thinking) | [📖 arXiv in progress] 
</div>

## Model Overview

![qwen3.5_small_size_score](https://cdn-uploads.huggingface.co/production/uploads/67329d3f69fded92d56ab41a/uS3wACe_-wb_a72pvcJbk.png)

This model has been specifically optimized to excel in several key areas:
- **Structured Reasoning Quality:** Enhanced ability to break down complex problems and think step-by-step.
- **Instruction Adherence:** Superior capability to follow strict guidelines and constraints provided in prompts.
- **Safety-Aligned Behavior:** Designed to operate safely in practical assistant and autonomous agent workflows.
- **Robustness:** Increased resistance against common misalignment patterns and adversarial inputs.

It leverages a rigorous post-training stack that combines supervised reasoning tuning with alignment-oriented optimization, focusing heavily on reliable behavior in real-world applications.

## Training Approach

- **Base Model:** `Qwen/Qwen3.5-4B`
- **Methodology:** LoRA-based Supervised Fine-Tuning (SFT) resulting in a merged BF16 checkpoint.
- **Reasoning Architecture:** Native support and normalization for the `<think>...</think>` format to explicitly separate the reasoning process from the final output.
- **Optimization Focus:** Enhancing safety reasoning, maximizing controllability, and ensuring response consistency.

## Data

This model was trained on **Merlin Research private datasets** built from internal R&D pipelines for:
- reasoning reliability improvements,
- instruction-following robustness,
- safety behavior refinement,
- misalignment reduction in applied scenarios.
- Using Anthropic’s framework Bloom&Petri for for better behavioral alignment.

![petri](https://cdn-uploads.huggingface.co/production/uploads/67329d3f69fded92d56ab41a/zivmYaesiM-tq4rriU_1x.jpeg)
(https://www.anthropic.com/research/petri-open-source-auditing)

## Intended Use Cases

This model is particularly well-suited for:
- Building safety-oriented reasoning assistants and chatbots.
- Tasks requiring strict, constrained instruction-following.
- Experimentation in AI alignment, safety research, and robustness testing.
- Agentic workflows where predictable and safe autonomous behavior is required.

## GGUF Status

GGUF artifacts are currently **in active development** and validation.

At this stage, we recommend using the **BF16 Transformers checkpoint** for stable results.
Updated and fully validated GGUF builds will be published in future releases.

**For Ollama**

```bash
ollama create qwen35-safety-thinking-bf16 -f Modelfile
ollama run qwen35-safety-thinking-bf16
```

## Organization

Designed, developed, and maintained with ❤️ by **Merlin Research**.

## Citation

If you utilize this model in your research or applications, please cite it as follows:

```bibtex
@misc{qwen3.5-4b-safety-thinking,
  author = {Merlin Research},
  title = {Qwen3.5-4B-Safety-Thinking: A Reasoning and Safety Aligned Model},
  year = {2026},
  publisher = {Hugging Face},
  howpublished = {\url{https://huggingface.co/MerlinSafety/Qwen3.5-4B-Safety-Thinking}},
  note = {Base model: Qwen/Qwen3.5-4B}
}
```