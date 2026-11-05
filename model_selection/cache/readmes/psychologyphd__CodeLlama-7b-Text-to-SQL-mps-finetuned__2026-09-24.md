---
license: llama2
datasets:
- b-mc2/sql-create-context
language:
- en
base_model:
- codellama/CodeLlama-7b-hf
pipeline_tag: text-generation
library_name: peft
tags:
- text-to-sql
- code
- lora
- nlp
- mps
new_version: psychologyphd/CodeLlama-7b-Text-to-SQL-MPS-FineTuned-V4
---

# CodeLlama-7b Text-to-SQL (Fine-Tuned on Mac MPS)

## Model Description
This is a fine-tuned version of **CodeLlama-7b-hf** specifically optimized for **Text-to-SQL** tasks. 
Right now it is overfitting. 

It was trained on a **MacBook Pro M3** using **MPS (Metal Performance Shaders)** acceleration. The training process successfully demonstrates that LLM fine-tuning is feasible on Apple Silicon devices with the right configuration.

### Origin & Adaptation
This project is adapted from the **Microsoft "Generative AI for Beginners" Course (Chapter 18: Fine-tuning)**.
- Original Source: [Generative AI for Beginners](https://github.com/microsoft/generative-ai-for-beginners)
- **Modifications**: The original code was designed for NVIDIA GPUs (using `bitsandbytes` and CUDA). I heavily modified the training pipeline to support **macOS/MPS**, including:
    - Removing unsupported quantization.
    - Optimizing memory usage to prevent OOM on Mac.
    - Adjusting `device_map` and FP16/FP32 settings for Metal compatibility.
  - see setup_fine_tune_mps.ipynb

## How to Use
See how_to_use.ipynb. 
- It seems like on mps pipeline doesn't work properly(at least I have not figured out how to make it working properly). Just use model.generate.
- chat template is required as the original data doesn't contain the template, but model is fine tuned with this template. 

## Training Details
- **Hardware**: Mac M3 (MPS)
- **Base Model**: [codellama/CodeLlama-7b-hf](https://huggingface.co/codellama/CodeLlama-7b-hf)
- **Dataset**: [b-mc2/sql-create-context](https://huggingface.co/datasets/b-mc2/sql-create-context)
- **Technique**: LoRA (PEFT)