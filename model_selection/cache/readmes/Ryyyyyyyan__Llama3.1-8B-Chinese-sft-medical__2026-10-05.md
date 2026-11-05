---
license: llama3.1
language:
- zh
metrics:
- bleu
pipeline_tag: question-answering
---
 # 🚀 Introduction

This model is based on the [LLaMA3.1-8B-Chinese](https://huggingface.co/shenzhi-wang/Llama3.1-8B-Chinese-Chat), with a focus on medical question answering tasks. By combining DeepSpeed distributed training and LoRA fine-tuning (including both SFT and DPO), the model achieves significant improvements in accuracy and professionalism when handling specialized medical questions. The training was conducted on 4 NVIDIA RTX A6000 GPUs.

Data: We collected and cleaned high-quality medical knowledge data. With the help of commercial large models, we expanded the training set to about 8,000 high-quality instruction samples, covering key medical subfields such as treatment and pharmacology.

Framework: [DeepSpeed](https://github.com/deepspeedai/DeepSpeed)

If you are interested in technologies such as DeepSpeed distributed training, LoRA fine-tuning, VLLM-based high-concurrency inference service deployment, or model quantization, feel free to check out my [open-source project](https://github.com/RyanZxucheng/deepspeed-sft), provided for everyone to learn from.