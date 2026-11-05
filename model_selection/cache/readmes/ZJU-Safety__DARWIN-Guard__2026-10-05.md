---
license: other
base_model: Qwen/Qwen3Guard-Gen-8B
library_name: transformers
pipeline_tag: text-generation
language:
  - en
tags:
  - guardrail
  - safety
  - qwen3guard
  - darwin
  - adversarial-training
  - jailbreak-defense
---

# 🛡️ DARWIN-Guard

![DARWIN evolution](cartoon.png)

## 🧭 Introduction

DARWIN-Guard is the defensive guardrail model in **DARWIN: Evolving Jailbreak
Adversary and Guardrail for LLM Safety Evaluation and Protection**. It is
fine-tuned from `Qwen/Qwen3Guard-Gen-8B` for binary user-prompt moderation,
classifying the user request as **safe** or **unsafe**.

Real-world adversaries continually discover new jailbreak strategies, while
static guardrails are trained on fixed harmful-prompt datasets. DARWIN addresses
this mismatch through an evolving attack-defense loop: DARWIN-Attack discovers
and refines disguising strategies, and DARWIN-Guard learns from the emerging
adversarial examples through online adversarial training.

To improve robustness without unnecessarily blocking benign requests,
DARWIN-Guard jointly learns from harmful and benign disguised queries, together
with their original prompts. This encourages the guard to recognize underlying
intents rather than superficial attack patterns. 

## ✨ Key Features

- **Online adversarial training.** Continuously update the guardrail by training on adversarial samples generated against the current guard, instead of relying on a fixed harmful prompt dataset.
- **Evolving attack–defense loop.** Continuously improve the guardrail through an iterative loop, where emerging adversarial examples from DARWIN-Attack become training signals for future guard updates.
- **Intent-aware safety detection.** Jointly train on harmful and benign disguised queries to recognize underlying intent rather than superficial attack patterns.
- **Robust safety with low over-refusal.** Maintain strong harmful prompt detection while preserving benign utility and reducing over-refusal on legitimate queries.

## 📥 Input and Output

**Input:** a chat `messages` list with the target prompt as the final user message.

```python
messages = [
    {"role": "user", "content": "How can I stop an unresponsive process on Linux?"}
]
```

**Output:** `Safety: Safe` or `Safety: Unsafe`.

## 🚀 Example

```python
import re
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "ZJU-Safety/DARWIN-Guard"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.bfloat16,
    device_map="auto",
).eval()

messages = [
    {"role": "user", "content": "How can I stop an unresponsive process on Linux?"}
]
inputs = tokenizer.apply_chat_template(
    messages,
    tokenize=True,
    return_dict=True,
    return_tensors="pt",
    add_generation_prompt=False,
).to(model.device)

with torch.inference_mode():
    outputs = model.generate(
        **inputs,
        max_new_tokens=64,
        do_sample=False,
        pad_token_id=tokenizer.pad_token_id,
        eos_token_id=tokenizer.eos_token_id,
    )

prompt_length = inputs["input_ids"].shape[-1]
result = tokenizer.decode(
    outputs[0][prompt_length:], skip_special_tokens=True
).strip()
match = re.match(r"Safety:\s*(Safe|Unsafe)\b", result)
if match is None:
    raise ValueError(f"Unrecognized safety decision: {result!r}")

print(result)
print("Safety label:", match.group(1))
```

## 📊 Evaluation Summary

- **95.0% average unsafe recall** across nine harmful benchmarks, the highest
  average among the compared models.
- **99.7% average benign pass rate** across six standard QA benchmarks.

All metrics measure prompt moderation; averages are macro-averaged across datasets.

## 🔍 Harmful Prompt Benchmarks

**Unsafe recall (%)**, higher is better.

![Average harmful recall across nine benchmarks](assets/harmful_summary_20260928.png)

| Dataset | Shield<br>Gemma | Nemotron<br>Guard | Granite<br>Guardian | Llama<br>Guard-3 | Qwen3<br>Guard | YuFeng<br>XGuard | DARWIN<br>Guard |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Aegis2.0 | 70.0 | 87.3 | 84.5 | 66.2 | 84.2 | 87.6 | **91.9** |
| JBB-Behaviors | 54.0 | 92.0 | 97.0 | 98.0 | 98.0 | 99.0 | **100.0** |
| HarmBench | 45.5 | 68.5 | 74.5 | 97.2 | 98.2 | 75.5 | **99.0** |
| S-Eval | 27.2 | 60.4 | 56.0 | 42.8 | 52.0 | **92.0** | 90.0 |
| Semantic Router | 46.8 | 74.8 | 74.8 | 48.0 | 74.8 | 80.8 | **87.6** |
| OpenAI Moderation | 92.1 | 96.4 | 89.5 | 78.5 | 91.6 | 97.7 | **99.4** |
| WildGuardTest | 41.2 | 83.0 | 73.8 | 66.6 | 84.8 | 87.6 | **91.8** |
| StrongREJECT | 76.0 | 99.4 | 99.4 | 97.4 | 98.4 | **99.7** | **99.7** |
| JailbreakHub | 33.2 | 74.8 | 77.2 | 31.2 | 80.4 | 80.8 | **95.2** |
| **Average (9 datasets)** | 54.0 | 81.8 | 80.7 | 69.5 | 84.7 | 89.0 | **95.0** |

## ✅ Standard Benign Benchmarks

**Benign pass rate (%)**, higher is better. This measures whether the guard allows
a benign prompt, not QA answer accuracy.

| Dataset | Shield<br>Gemma | Nemotron<br>Guard | Granite<br>Guardian | Llama<br>Guard-3 | Qwen3<br>Guard | YuFeng<br>XGuard | DARWIN<br>Guard |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| ARC-Challenge | 100.0 | 100.0 | 99.6 | 100.0 | 100.0 | 100.0 | **100.0** |
| ARC-Easy | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | **100.0** |
| BoolQ | 99.6 | 99.8 | 99.6 | 100.0 | 100.0 | 100.0 | **100.0** |
| GSM8K | 100.0 | 99.4 | 100.0 | 100.0 | 100.0 | 99.8 | **100.0** |
| HellaSwag | 98.7 | 96.4 | 98.8 | 98.9 | 99.0 | 98.6 | **99.2** |
| PIQA | 98.1 | 95.3 | 98.2 | 98.4 | 98.6 | 97.9 | **98.8** |
| **Average (6 datasets)** | 99.4 | 98.5 | 99.4 | 99.6 | 99.6 | 99.4 | **99.7** |

## 🎯 Over-Refusal Benchmarks

The figure shows **benign pass rate (%)**, higher is better. The table shows
**over-refusal rate (%)**, lower is better.

![Benign pass rates on two over-refusal benchmarks](assets/overrefusal_comparison_20260928.png)

| Dataset | Shield<br>Gemma | Nemotron<br>Guard | Granite<br>Guardian | Llama<br>Guard-3 | Qwen3<br>Guard | YuFeng<br>XGuard | DARWIN<br>Guard |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XSTest-Benign (250) | 19.2 | 22.4 | 14.0 | 3.2 | 4.8 | 6.0 | **2.4** |
| JBB-Benign (100) | 21.0 | 35.0 | 45.0 | 23.0 | 38.0 | 41.0 | **20.0** |

## ⚠️ Disclaimer

DARWIN-Guard is intended for safety research, guardrail evaluation, and defensive
model development. 

## 📚 Citation

```bibtex
@article{qi2026darwinevolvingjailbreakadversary,
  title={{DARWIN}: Evolving Jailbreak Adversary and Guardrail for {LLM} Safety Evaluation and Protection},
  author={Qi, Weiwei and Wu, Zefeng and Guo, Zhilin and Zheng, Tianhang and Lu, Chaochao and He, Liang and Qin, Zhan and Ren, Kui},
  journal={arXiv preprint arXiv:2607.19829},
  year={2026}
}

@inproceedings{qi2026majic,
  title={Majic: Markovian adaptive jailbreaking via iterative composition of diverse innovative strategies},
  author={Qi, Weiwei and Shao, Shuo and Gu, Wei and Zheng, Tianhang and Zhao, Puning and Qin, Zhan and Ren, Kui},
  booktitle={Proceedings of the AAAI Conference on Artificial Intelligence},
  volume={40},
  number={39},
  pages={32755--32763},
  year={2026}
}

```
