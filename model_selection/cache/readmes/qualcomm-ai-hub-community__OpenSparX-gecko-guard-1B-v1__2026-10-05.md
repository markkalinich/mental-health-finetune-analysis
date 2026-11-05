---
language:
- zh
- en
library_name: transformers
pipeline_tag: image-text-to-text
tags:
- multimodal
- internvl3
- vision-language-model
- guard
- sft
---

# OpenSparX-gecko-guard-1B-v1

## 简介 | Overview
这是一个面向 Guard 哨兵场景的多模态视觉语言模型，基于 `InternVL3-1B` 进行监督微调，支持输入单张图片和自然语言提示词，对画面中的人员行为、穿着特征和风险等级进行分析。

This is a multimodal vision-language model for Guard sentinel scenarios. It is fine-tuned from `InternVL3-1B` and supports one image plus a natural-language prompt to analyze human behavior, clothing cues, and scene risk level.

## 特性 | Highlights
- 多模态输入：支持图片加文本提示词联合输入。
- 哨兵场景优化：面向人员行为观察、风险提示和安防描述任务。
- 中英提示词均可：推荐中文提示词，但英文提示词也可用于测试和推理。
- 风险标签输出：可结合 `<|TAG|>` 风格输出做规则解析或下游集成。

- Multimodal input: accepts image plus text prompt together.
- Sentinel-oriented tuning: designed for behavior observation, risk prompting, and security-style scene description.
- Chinese and English prompts are both supported, while Chinese prompts are recommended for this release.
- Risk-tag output: can be integrated with parsers or downstream systems using `<|TAG|>`-style output.

## 适用场景 | Use Cases
- 哨兵模式下的陌生人靠近、徘徊、异常姿态观察。
- 对人员穿着、动作和场景状态进行文字描述。
- 输出风险等级，便于与告警、审核或后续业务规则联动。

- Stranger approach, loitering, and abnormal posture observation in sentinel scenarios.
- Natural-language description of clothing, actions, and scene status.
- Risk-level output for alerts, review workflows, or downstream business-rule integration.

## 输入输出格式 | Input And Output
推荐输入为单张图片和一段自然语言提示词，适合直接用于图片问答或风险分析任务。

Recommended input is one image and one natural-language task prompt, which fits image-question-answering or risk-analysis workflows.

```json
{
  "image": "/path/to/your/image.jpg",
  "prompt": "请分析图片中人员的异常行为与穿着特点，并给出风险等级。"
}
```

推荐输出通常包含两部分：
- 自然语言描述
- 风险标签，例如 `<|TAG|>高风险`

Typical output usually contains:
- A natural-language description
- A risk tag such as `<|TAG|>高风险`

## 示例提示词 | Example Prompts
### 中文哨兵风险分析

```text
你现在是一个优秀的汽车智能座舱助手,现在车辆开启了哨兵模式,请分析图片中人员的异常行为与穿着特点,并给出风险等级。
```

### English Sentinel Risk Analysis

```text
The vehicle is now in sentinel mode. Please analyze the person's behavior and clothing cues in the image, then provide the risk level.
```

### 强约束输出格式

```text
你现在是一个优秀的汽车智能座舱助手,现在车辆开启了哨兵模式,请分析图片中人员的异常行为与穿着特点,并给出风险等级。请严格输出“行为描述。穿着描述。<|TAG|>风险等级”。
```

### 示例输出

```text
画面中一名人员靠近车辆，身体前倾，疑似正在观察车窗或车门区域，存在可疑徘徊行为。该人员穿着深色上衣和长裤。<|TAG|>中风险
```

## Python 用法 | Python Usage
该模型包含自定义 `InternVLChatModel` 代码，加载时需要启用 `trust_remote_code=True`；推理时推荐使用 `AutoTokenizer` 和 `AutoModel`。

This model includes custom `InternVLChatModel` code, so loading requires `trust_remote_code=True`. For inference, use `AutoTokenizer` together with `AutoModel`.

```python
from pathlib import Path

import torch
from PIL import Image
from torchvision import transforms
from transformers import AutoModel, AutoTokenizer

repo_id = "qualcomm-ai-hub-community/OpenSparX-gecko-guard-1B-v1"
prompt = "请分析图片中人员的异常行为与穿着特点，并给出风险等级。"

transform = transforms.Compose(
    [
        transforms.Lambda(lambda img: img.convert("RGB")),
        transforms.Resize((448, 448), interpolation=transforms.InterpolationMode.BICUBIC),
        transforms.ToTensor(),
        transforms.Normalize(mean=(0.485, 0.456, 0.406), std=(0.229, 0.224, 0.225)),
    ]
)

tokenizer = AutoTokenizer.from_pretrained(
    repo_id,
    trust_remote_code=True,
    use_fast=False,
)
model = AutoModel.from_pretrained(
    repo_id,
    trust_remote_code=True,
    dtype=torch.bfloat16,
    low_cpu_mem_usage=False,
).eval().cuda()

image = Image.open(Path("/path/to/your/image.jpg"))
pixel_values = transform(image).unsqueeze(0).to(device="cuda", dtype=torch.bfloat16)

generation_config = {
    "max_new_tokens": 256,
    "do_sample": False,
    "temperature": 0.0,
}

response = model.chat(
    tokenizer=tokenizer,
    pixel_values=pixel_values,
    question=prompt,
    generation_config=generation_config,
    verbose=False,
)
print(response)
```

## 社区 ONNX 资产 | Community ONNX Asset
除原始模型目录外，本仓库还提供一个可直接下载的 ONNX 资产包：

In addition to the original model directory, this repository also provides a downloadable ONNX asset package:

- `OpenSparX-gecko-guard-1B-v1-onnx-fp32.zip`

该压缩包适合以下场景：

- 需要直接下载 ONNX 部署资产，而不是完整训练后模型目录
- 需要复用已经通过 AI Hub 编译验证的 `model.onnx + model.data`
- 需要将模型文件、版本信息和最小推理配置一起分发

This zip asset is intended for the following scenarios:

- Direct download of ONNX deployment assets instead of the full training-style model directory
- Reuse of the `model.onnx + model.data` package that has already passed AI Hub compile validation
- Distribution of the model files together with version metadata and minimal inference configs

`OpenSparX-gecko-guard-1B-v1-onnx-fp32.zip` 解压后当前包含：

The current contents of `OpenSparX-gecko-guard-1B-v1-onnx-fp32.zip` are:

- `model.onnx`
- `model.data`
- `tool_versions.yaml`
- `tokenizer.json`
- `tokenizer_config.json`
- `special_tokens_map.json`
- `preprocessor_config.json`
- `config.json`

说明：

- 该 zip 适合直接下载和分发 ONNX 部署资产
- 原始模型目录仍适合需要 `trust_remote_code=True` 方式加载和继续研究的用户
- 当前 ONNX 资产为 `fp32` 版本，并已完成面向 `SA8295P ADP` 的 AI Hub 编译验证

Notes:

- This zip is intended for direct download and distribution of ONNX deployment assets
- The original model directory remains useful for users who need `trust_remote_code=True` loading or further research
- The current ONNX asset is an `fp32` release and has passed AI Hub compile validation targeting `SA8295P ADP`

## 文件说明 | File Overview
- `model.safetensors`：模型权重。
- `config.json`、`generation_config.json`：模型结构与生成配置。
- `tokenizer.json`、`tokenizer_config.json`、`special_tokens_map.json`、`added_tokens.json`、`merges.txt`、`vocab.json`：分词器相关文件。
- `preprocessor_config.json`：图像预处理配置。
- `chat_template.jinja`：对话模板。
- `configuration_internvl_chat.py`、`configuration_intern_vit.py`、`modeling_internvl_chat.py`、`modeling_intern_vit.py`、`conversation.py`：`InternVL` 自定义配置和模型定义，加载时必需。

- `model.safetensors`: model weights.
- `config.json` and `generation_config.json`: model architecture and generation configs.
- `tokenizer.json`, `tokenizer_config.json`, `special_tokens_map.json`, `added_tokens.json`, `merges.txt`, and `vocab.json`: tokenizer files.
- `preprocessor_config.json`: image preprocessing config.
- `chat_template.jinja`: chat template.
- `configuration_internvl_chat.py`, `configuration_intern_vit.py`, `modeling_internvl_chat.py`, `modeling_intern_vit.py`, and `conversation.py`: custom `InternVL` config and model definition files required for loading.

## 模型来源 | Model Provenance
该模型基于 `InternVL3-1B` 进行多模态监督微调，当前发布内容来自一次面向 Guard 哨兵场景的可用微调产物。训练目标是让模型根据图片输出人员行为、穿着描述以及风险等级标签。

This model is built on top of `InternVL3-1B` through multimodal supervised fine-tuning. The released artifact comes from a usable fine-tuning run for Guard sentinel scenarios, with the objective of generating behavior description, clothing description, and a risk-level tag from an input image.

## 资源需求 | Requirements
- 建议使用支持 CUDA 的 GPU 进行推理。
- 推荐显存 16 GB 及以上，具体占用会随分辨率、生成长度和精度设置变化。
- 常见推理精度可使用 `float16` 或 `bfloat16`。

- A CUDA-capable GPU is recommended for inference.
- 16 GB or more VRAM is recommended, and actual usage depends on image resolution, generation length, and dtype settings.
- Common inference dtypes are `float16` and `bfloat16`.

## 许可与致谢 | License And Acknowledgement
- 基于 `InternVL3-1B` 微调，请遵循上游模型及相关依赖的许可与使用约束。
- 模型仅用于研究、演示和评估用途，真实业务接入前请完成充分验证。

- This model is fine-tuned from `InternVL3-1B`; please follow the upstream model license and related dependency terms.
- The model is intended for research, demo, and evaluation use. Perform sufficient validation before production integration.

## 注意事项 | Notes
- 模型输出受光照、遮挡、拍摄角度和图像质量影响。
- 风险标签仅供研究、演示和流程联调用途，不应直接替代人工判断。
- 部署到真实安防或车端场景前，请补充误报漏报评估、回退策略和权限控制。

This model output is affected by lighting, occlusion, camera angle, and image quality.
Risk tags are intended for research, demo, and workflow integration only, and should not replace human judgment directly.
Before real deployment in security or in-vehicle scenarios, add false-positive and false-negative evaluation, fallback handling, and access control.
