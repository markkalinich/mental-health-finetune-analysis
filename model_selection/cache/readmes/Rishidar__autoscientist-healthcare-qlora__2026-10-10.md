---
language: en
tags:
  - autoscientist
  - adaption-labs
  - qlora
  - healthcare
  - fine-tuned
base_model: Qwen/Qwen2.5-0.5B-Instruct
datasets:
  - Rishidar/autoscientist-competition-datasets
---

# AutoScientist Competition — Healthcare Model

Fine-tuned from [Qwen/Qwen2.5-0.5B-Instruct](https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct) on
the [healthcare adapted dataset](https://huggingface.co/datasets/Rishidar/autoscientist-competition-datasets)
produced by [Adaption Labs](https://adaptionlabs.ai) AutoScientist Challenge.

## Training
- Method: QLoRA (4-bit NF4, r=32, alpha=64)
- Epochs: 3
- Learning rate: 0.0002
- Dataset quality: Grade A (Adaption Labs evaluation)

## Usage
```python
from transformers import AutoModelForCausalLM, AutoTokenizer
model = AutoModelForCausalLM.from_pretrained("Rishidar/autoscientist-healthcare-qlora")
tokenizer = AutoTokenizer.from_pretrained("Rishidar/autoscientist-healthcare-qlora")
```
