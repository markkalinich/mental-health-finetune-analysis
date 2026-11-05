---
license: apache-2.0
datasets:
- Tuwhy/MIS_Train
base_model:
- Qwen/Qwen2-VL-7B-Instruct
pipeline_tag: image-text-to-text
tags:
- safety
- fine-tuning
- multi-image
- mllm
---

# Rethinking Bottlenecks in Safety Fine-Tuning of Vision Language Models
![motivation](./assets/motivation.png)
Our paper, code, data, models can be found at [MIS](https://dripnowhy.github.io/MIS/).

## Description
[Qwen2-VL-7B-Instruct](https://huggingface.co/Qwen/Qwen2-VL-7B-Instruct) model fine-tuned on [MIS training set](https://huggingface.co/datasets/Tuwhy/MIS_Train).

## MIRgae
![mirage](./assets/model_fig.png)
Here is example pipeline of [MIS training set](https://huggingface.co/datasets/Tuwhy/MIS_Train) and MIRage safety CoT label construction.

You can fine-tune Qwen2-VL series using [LlamaFactory](https://github.com/hiyouga/LLaMA-Factory).
