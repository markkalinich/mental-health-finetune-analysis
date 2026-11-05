---
license: apache-2.0
base_model: google/gemma-4-E2B
tags:
  - emotional-support
  - companion
  - on-device
  - conversational
library_name: transformers
pipeline_tag: text-generation
---

<p align="center">
  <img src="https://huggingface.co/spaces/Lythri/README/resolve/main/Banner_flat.png" width="600" alt="Lythri"/>
</p>

<p align="center">
  <a href="https://huggingface.co/Lythri">Hugging Face</a> |
  <a href="https://www.modelscope.cn/profile/Spike8086">ModelScope</a> |
  <a href="https://github.com/SPIKE8086">GitHub</a> |
  Technical Report (coming soon)
</p>

# Lythri

## Introduction

**Lythri** is a family of on-device language models built for emotional companionship. Instead of chasing math and coding scores, Lythri is trained to understand how people feel and to hold natural, multi-turn conversations, while staying small enough to run locally on a laptop or phone.

<p align="center">
  <img src="https://huggingface.co/spaces/Lythri/README/resolve/main/Lythri_Overview.png" width="800" alt="Lythri Overview"/>
</p>

| Model | Total Params | Active Params | Base Model | GGUF |
|---|---|---|---|---|
| [Lythri-7B-A4B](https://huggingface.co/Lythri/Lythri-7B-A4B) | 7.46B | 4.5B | Gemma 4 E4B | [Lythri-7B-A4B-GGUF](https://huggingface.co/Lythri/Lythri-7B-A4B-GGUF) |
| [Lythri-4B-A2B](https://huggingface.co/Lythri/Lythri-4B-A2B) | 4.63B | 2.3B | Gemma 4 E2B | [Lythri-4B-A2B-GGUF](https://huggingface.co/Lythri/Lythri-4B-A2B-GGUF) |

## Emotional Intelligence (Preliminary)

Zero-shot results.

| Model | GoEmotions (Macro F1) | EmoBench (Acc) | EQ-Bench (v2) |
|---|---|---|---|
| Gemma 4 E4B | 8.00 | 31.39 | 43.19 |
| **Lythri-7B-A4B** | **31.54** | **46.83** | **49.41** |

> **Note:** These are preliminary results from an internal evaluation that is not yet formal or complete, and they may differ slightly from the final numbers. For full details and authoritative results, including Lythri-4B-A2B, please refer to the technical report (coming soon).

## General Benchmarks

<table width="100%" style="display: table; width: 100%; border-collapse: collapse; text-align: center;">
  <thead>
    <tr style="border-bottom: 2px solid #338f65;">
      <th width="40%" style="text-align: left; padding: 10px 16px;">Benchmark</th>
      <th width="30%" style="color: #338f65; white-space: nowrap; padding: 10px 16px;">Lythri-4B-A2B</th>
      <th width="30%" style="background: rgba(51,143,101,0.12); color: #338f65; white-space: nowrap; padding: 10px 16px;">Lythri-7B-A4B</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background: rgba(51,143,101,0.06);">
      <td colspan="3" style="text-align: left; color: #338f65; font-weight: bold;">Knowledge</td>
    </tr>
    <tr><td style="text-align: left;">MMLU</td><td>55.23</td><td style="background: rgba(51,143,101,0.12); color: #338f65; font-weight: bold;">69.09</td></tr>
    <tr><td style="text-align: left;">MMLU-Pro</td><td>24.42</td><td style="background: rgba(51,143,101,0.12); color: #338f65; font-weight: bold;">38.17</td></tr>
    <tr><td style="text-align: left;">ARC-E</td><td>81.40</td><td style="background: rgba(51,143,101,0.12); color: #338f65; font-weight: bold;">83.42</td></tr>
    <tr><td style="text-align: left;">ARC-C</td><td>52.99</td><td style="background: rgba(51,143,101,0.12); color: #338f65; font-weight: bold;">60.58</td></tr>
    <tr style="background: rgba(51,143,101,0.06);">
      <td colspan="3" style="text-align: left; color: #338f65; font-weight: bold;">Reasoning</td>
    </tr>
    <tr><td style="text-align: left;">PIQA</td><td>79.49</td><td style="background: rgba(51,143,101,0.12); color: #338f65; font-weight: bold;">81.88</td></tr>
    <tr><td style="text-align: left;">HellaSwag</td><td>72.80</td><td style="background: rgba(51,143,101,0.12); color: #338f65; font-weight: bold;">78.29</td></tr>
    <tr><td style="text-align: left;">WinoGrande</td><td>68.43</td><td style="background: rgba(51,143,101,0.12); color: #338f65; font-weight: bold;">74.90</td></tr>
    <tr style="background: rgba(51,143,101,0.06);">
      <td colspan="3" style="text-align: left; color: #338f65; font-weight: bold;">General</td>
    </tr>
    <tr><td style="text-align: left;">CommonsenseQA</td><td>65.52</td><td style="background: rgba(51,143,101,0.12); color: #338f65; font-weight: bold;">77.07</td></tr>
    <tr><td style="text-align: left;">SocialIQA</td><td>49.80</td><td style="background: rgba(51,143,101,0.12); color: #338f65; font-weight: bold;">50.46</td></tr>
    <tr><td style="text-align: left;">TruthfulQA MC2</td><td>46.16</td><td style="background: rgba(51,143,101,0.12); color: #338f65; font-weight: bold;">49.66</td></tr>
    <tr style="background: rgba(51,143,101,0.06);">
      <td colspan="3" style="text-align: left; color: #338f65; font-weight: bold;">Science</td>
    </tr>
    <tr><td style="text-align: left;">OpenBookQA</td><td>41.00</td><td style="background: rgba(51,143,101,0.12); color: #338f65; font-weight: bold;">43.60</td></tr>
    <tr><td style="text-align: left;">GPQA Diamond</td><td>28.79</td><td style="background: rgba(51,143,101,0.12); color: #338f65; font-weight: bold;">27.78</td></tr>
    <tr style="background: rgba(51,143,101,0.06);">
      <td colspan="3" style="text-align: left; color: #338f65; font-weight: bold;">Math</td>
    </tr>
    <tr><td style="text-align: left;">GSM8K</td><td>28.81</td><td style="background: rgba(51,143,101,0.12); color: #338f65; font-weight: bold;">62.02</td></tr>
    <tr><td style="text-align: left;">MATH</td><td>3.62</td><td style="background: rgba(51,143,101,0.12); color: #338f65; font-weight: bold;">21.28</td></tr>
    <tr style="background: rgba(51,143,101,0.06);">
      <td colspan="3" style="text-align: left; color: #338f65; font-weight: bold;">Reading</td>
    </tr>
    <tr><td style="text-align: left;">BoolQ</td><td>73.15</td><td style="background: rgba(51,143,101,0.12); color: #338f65; font-weight: bold;">85.32</td></tr>
    <tr style="background: rgba(51,143,101,0.06);">
      <td colspan="3" style="text-align: left; color: #338f65; font-weight: bold;">Code / Instruction</td>
    </tr>
    <tr><td style="text-align: left;">HumanEval</td><td>28.66</td><td style="background: rgba(51,143,101,0.12); color: #338f65; font-weight: bold;">45.12</td></tr>
    <tr><td style="text-align: left;">IFEval</td><td>26.43</td><td style="background: rgba(51,143,101,0.12); color: #338f65; font-weight: bold;">31.05</td></tr>
  </tbody>
</table>

All benchmarks are evaluated with their official standard settings and in generative mode with chat template applied, reflecting real-world inference conditions. Think-tag outputs from model are stripped before answer extraction.
## Quickstart

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_path = "Lythri/Lythri-7B-A4B"  # or "Lythri/Lythri-4B-A2B"
tok = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(
    model_path, dtype=torch.bfloat16, device_map="auto"
)

messages = [{"role": "user", "content": "My friend just lost their job and seems really down. What should I say to them?"}]
chat = tok.apply_chat_template(messages, tokenize=False, add_generation_prompt=True) + "<think>"
inputs = tok(chat, return_tensors="pt").to(model.device)

with torch.inference_mode():
    out = model.generate(
        **inputs,
        max_new_tokens=2048,
        do_sample=False,
        eos_token_id=[1, 106],
    )

print(tok.decode(out[0][inputs.input_ids.shape[1]:], skip_special_tokens=True))
```

### Recommended Generation Config

```python
generation_config = {
    "temperature": 0.7,
    "top_p": 0.9,
    "top_k": 64,
    "max_new_tokens": 2048,
    "repetition_penalty": 1.05,
    "do_sample": True,
    "eos_token_id": [1, 106],
}

out = model.generate(**inputs, **generation_config)
```

## Compute

The full development of Lythri, including training and evaluation, used about 2,842 GPU hours on NVIDIA RTX 6000D GPUs.

## Limitations

- Lythri is optimized for conversation and emotional understanding, not for math, coding or complex reasoning.
- Lythri is not a substitute for professional mental health support. If you or someone you know is in crisis, please contact local emergency services or a crisis helpline.
- Like all language models, it can produce inaccurate or inappropriate content.

## License

Lythri is built on Gemma 4 and is released under the Apache License 2.0.

## Support

**The whole training process is self-funded. If you like our model, please click a free like — that means a lot to me as a student!**