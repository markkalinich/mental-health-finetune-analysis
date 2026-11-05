---
language:
- en
- fr
- es
- pt
tags:
- falcon3
license: other
license_name: falcon-llm-license
license_link: https://falconllm.tii.ae/falcon-terms-and-conditions.html
library_name: transformers
---

<div align="center">
    <img src="https://huggingface.co/datasets/tiiuae/documentation-images/resolve/main/general/falco3-logo.png" alt="drawing" width="500"/>
</div>

# Falcon3-1B-Base

**Falcon3** family of Open Foundation Models is a set of pretrained and instruct LLMs ranging from 1B to 10B parameters.

This repository contains the **Falcon3-1B-Base**. It achieves strong results on reasoning, language understanding, instruction following, code and mathematics tasks.
Falcon3-1B-Base supports 4 languages (English, French, Spanish, Portuguese) and a context length of up to 4K.
It was pruned in terms of depth, width, number of heads, and embedding channels from a larger 3B Falcon model, and was efficiently trained on only 80 GT using a knowledge distillation objective.

⚠️ **This is a raw, pretrained model, which should be further finetuned using SFT, RLHF, continued pretraining, etc. for most use cases.** 

## Model Details
- Architecture
  - Transformer-based causal decoder-only architecture
  - 18 decoder blocks
  - Grouped Query Attention (GQA) for faster inference: 8 query heads and 4 key-value heads
  - Wider head dimension: 256
  - High RoPE value to support long context understanding: 1000042
  - Uses SwiGLU and RMSNorm
  - 4K context length
  - 131K vocab size
- Pruned and healed using larger Falcon models (3B and 7B respectively) on only 80 Gigatokens of datasets comprising of web, code, STEM, high quality and multilingual data using 256 H100 GPU chips
- Supports EN, FR, ES, PT
- Developed by [Technology Innovation Institute](https://www.tii.ae)
- License: TII Falcon-LLM License 2.0
- Model Release Date: December 2024


## Getting started

<details>
<summary> Click to expand </summary>

```python
import torch
from transformers import pipeline

pipe = pipeline(
    "text-generation", 
    model="tiiuae/Falcon3-1B-Base", 
    torch_dtype=torch.bfloat16, 
    device_map="auto"
)
response = pipe("Question: How many hours in one day? Answer: ")
print(response[0]['generated_text'])
```

</details>

<br>

## Benchmarks
We report in the following table our internal pipeline benchmarks.
 - We use [lm-evaluation harness](https://github.com/EleutherAI/lm-evaluation-harness).
 - We report **raw scores**.
 - We use same batch-size across all models.



<table border="1" style="width: 100%; text-align: center; border-collapse: collapse;">
    <colgroup>
        <col style="width: 10%;">
        <col style="width: 10%;">
        <col style="width: 7%;">
        <col style="width: 7%;">
        <col style="width: 7%;">
        <col style="background-color: rgba(80, 15, 213, 0.5); width: 7%;">
    </colgroup>
    <thead>
        <tr>
            <th>Category</th>
            <th>Benchmark</th>
            <th>Llama-3.2-1B</th>
            <th>Qwen2.5-1.5B</th>
            <th>SmolLM2-1.7B</th>
            <th>Falcon3-1B-Base</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan="3">General</td>
            <td>MMLU (5-shot)</td>
            <td>31.1</td>
            <td><b>61.0</b></td>
            <td>50.1</td>
            <td>42.5</td>
        </tr>
        <tr>
            <td>MMLU-PRO (5-shot)</td>
            <td>11.7</td>
            <td><b>28.4</b></td>
            <td>21.3</td>
            <td>16.1</td>
        </tr>
        <tr>
            <td>IFEval</td>
            <td>14.8</td>
            <td><b>26.0</b></td>
            <td>24.2</td>
            <td>25.2</td>
        </tr>
        <tr>
            <td rowspan="2">Math</td>
            <td>GSM8K (5-shot)</td>
            <td>6.6</td>
            <td><b>62.2</b></td>
            <td>31.0</td>
            <td>34.3</td>
        </tr>
        <tr>
            <td>MATH Lvl-5 (4-shot)</td>
            <td>0.2</td>
            <td><b>6.7</b></td>
            <td>1.4</td>
            <td>2.2</td>
        </tr>
        <tr>
            <td rowspan="4">Reasoning</td>
            <td>Arc Challenge (25-shot)</td>
            <td>40.2</td>
            <td><b>54.8</b></td>
            <td>54.1</td>
            <td>48.1</td>
        </tr>
        <tr>
            <td>GPQA (0-shot)</td>
            <td>24.2</td>
            <td>28.1</td>
            <td><b>28.9</b></td>
            <td>28.1</td>
        </tr>
        <tr>
            <td>MUSR (0-shot)</td>
            <td>34.5</td>
            <td>35.5</td>
            <td>34.7</td>
            <td><b>41.9</b></td>
        </tr>
        <tr>
            <td>BBH (3-shot)</td>
            <td>31.2</td>
            <td><b>41.1</b></td>
            <td>34.2</td>
            <td>36.0</td>
        </tr>
        <tr>
            <td rowspan="4">CommonSense Understanding</td>
            <td>PIQA (0-shot)</td>
            <td>74.5</td>
            <td>76.0</td>
            <td><b>77.5</b></td>
            <td>74.5</td>
        </tr>
        <tr>
            <td>SciQ (0-shot)</td>
            <td>88.5</td>
            <td><b>93.1</b></td>
            <td>90.8</td>
            <td>91.1</td>
        </tr>
        <tr>
            <td>Winogrande (0-shot)</td>
            <td>60.4</td>
            <td>63.0</td>
            <td><b>66.1</b></td>
            <td>61.2</td>
        </tr>
        <tr>
            <td>OpenbookQA (0-shot)</td>
            <td>37.4</td>
            <td>40.4</td>
            <td><b>44.0</b></td>
            <td>41.0</td>
        </tr>
    </tbody>
</table>

## Useful links
- View our [release blogpost](https://huggingface.co/blog/falcon3).
- Feel free to join [our discord server](https://discord.gg/fwXpMyGc) if you have any questions or to interact with our researchers and developers.

## Technical Report
Coming soon....

## Citation
If the Falcon3 family of models were helpful to your work, feel free to give us a cite.
 
```
@misc{Falcon3,
    title = {The Falcon 3 Family of Open Models},
    url = {https://huggingface.co/blog/falcon3},
    author = {Falcon-LLM Team},
    month = {December},
    year = {2024}
}
```