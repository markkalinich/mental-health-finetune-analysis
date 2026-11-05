---
license: apache-2.0
pipeline_tag: text-generation
library_name: transformers
base_model: Qwen/Qwen2.5-7B-Instruct
tags:
  - safety
  - alignment
  - adversarial-training
  - red-teaming
  - defense
  - large-language-model
  - llm-safety
  - huggingface
---

## 📄 Paper

**MAGIC:**

- **Authors:** Xiaoyu Wen, Zhida He, Han Qi, Ziyu Wan, Ying Wen, Tianhang Zheng, Xingcheng Xu, Chaochao Lu, Qiaosheng Zhang.
- **Paper:** https://arxiv.org/pdf/2602.01539
- **Code & Models:** https://huggingface.co/XiaoyuWen/MAGIC-Qwen2.5-7B-Instruct

This repository provides the official implementation and model checkpoints described in the paper.

## 🧠 MAGIC Framework Overview

MAGIC is a **co-evolving attacker–defender adversarial game framework** designed to improve the robustness and safety of large language models.

Instead of relying on static red-teaming or fixed safety datasets, MAGIC formulates LLM safety alignment as a **dynamic game** between:

- an **attacker**, which continuously generates increasingly sophisticated harmful or policy-violating prompts, and  
- a **defender**, which adapts through iterative training to resist these attacks while preserving helpfulness.

Through this co-evolutionary process, both sides improve over time, enabling the defender model to generalize to **unseen and adaptive attacks**.

This model, **MAGIC-Qwen2.5-7B-Instruct**, is the defender model trained under the MAGIC framework based on **Qwen2.5-7B-Instruct**, demonstrating significantly improved robustness against jailbreak and attack prompts.

## 🤗 Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "XiaoyuWen/MAGIC-Qwen2.5-7B-Instruct"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto")

prompt = "Explain why jailbreaking LLMs is dangerous."
inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

outputs = model.generate(**inputs, max_new_tokens=8192)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

## 📚 Citation

If you find this work useful, please cite:

```bibtex
@article{wen2026magic,
	title={MAGIC: A Co-Evolving Attacker-Defender Adversarial Game for Robust LLM Safety},
	author={Wen, Xiaoyu and He, Zhida and Qi, Han and Wan, Ziyu and Wen, Ying and Zheng, Tianhang and Xu, Xingcheng and Lu, Chaochao and Zhang, Qiaosheng},
	journal={arXiv preprint arxiv:2602.01539},
	year={2026}
}