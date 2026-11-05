---
license: apache-2.0
language:
  - zh
pipeline_tag: text-generation
library_name: transformers
base_model: Qwen/Qwen3-4B
tags:
  - qwen3
  - chinese
  - instruction-tuned
  - traffic-accident
  - safetyraise
---

<!--
如果你的训练底座最终确认不是 Qwen/Qwen3-4B，请在发布前只改上面的 base_model。
-->

# SafetyRAISE-TS-Qwen3

SafetyRAISE-TS-Qwen3 是一个面向道路交通事故分析场景的中文专家模型，主要用于生成事故指导意见、辅助梳理事故事实、归纳责任分析要点，并为检索增强报告链路提供前置专家意见。

本模型服务于 SafetyRAISE 道路交通事故分析报告生成系统，定位是“事故分析辅助专家模型”，不是通用聊天模型。

相关资源：

- 开源应用：[QianYan-Art/SafetyRAISE-OS](https://github.com/QianYan-Art/SafetyRAISE-OS)
- 推理引擎：[QianYan-Art/SafetyRAISE-LMEngine](https://github.com/QianYan-Art/SafetyRAISE-LMEngine)
- 训练数据集：[suyuan37/TS-Dataset](https://huggingface.co/datasets/suyuan37/TS-Dataset)
- 数据集 Markdown 预览：[suyuan37/TS-Dataset-Markdown-Viewer](https://huggingface.co/spaces/suyuan37/TS-Dataset-Markdown-Viewer)

## 模型定位

本模型主要承担以下任务：

1. 根据事故图片、视频分析后的结构化信息生成专家指导意见
2. 提炼事故分析中需要进一步核实的关键点
3. 为后续知识检索和报告生成提供中间指导信息

本模型不直接替代人工事故认定，也不应被视为最终法律结论。

## 适用场景

适合：

1. 道路交通事故辅助分析
2. 事故责任分析前置梳理
3. 事故报告生成流程中的专家意见草稿生成

不适合：

1. 通用闲聊
2. 无交通事故上下文的开放式问答
3. 直接输出最终法律裁决结论

## 基座模型

当前发布配置按 `Qwen/Qwen3-4B` 标注。  
从导出目录中的 `config.json` 看，`hidden_size=2560`、`num_hidden_layers=36`，与公开的 `Qwen/Qwen3-4B` 配置一致。

## 输入与输出

典型输入包括：

1. 结构化事故字段
2. 事故过程描述
3. 车辆、道路、人员、违法行为等事实要素

典型输出包括：

1. 需要重点核实的事实点
2. 可供责任分析参考的专家指导意见
3. 面向后续知识检索的分析要点

## 推荐使用方式

建议把本模型作为 SafetyRAISE 工作流中的“专家意见生成”节点使用，而不是单独作为终裁模型使用。

如果你需要在本地或服务器部署，可以使用兼容 OpenAI Chat Completions 的推理服务承载本模型，再将服务地址接入 SafetyRAISE：

1. `EXPERT_LOCAL_MODEL`
2. `EXPERT_LOCAL_BASE_URL`

## Transformers 使用示例

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "suyuan37/SafetyRAISE-TS-Qwen3"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype="auto", device_map="auto")
```

## 仓库文件说明

本仓库当前按 Transformers 分片权重格式发布。普通用户不需要手动只下载某一个权重分片，推荐通过 `transformers`、`huggingface_hub` 或 `hf download` 下载完整仓库。

| 文件 | 说明 |
| --- | --- |
| `model-00001-of-00002.safetensors` | 模型权重分片 1 |
| `model-00002-of-00002.safetensors` | 模型权重分片 2 |
| `model.safetensors.index.json` | 分片权重索引，加载模型时需要 |
| `config.json` | 模型结构配置 |
| `generation_config.json` | 生成参数配置 |
| `tokenizer.json` | Tokenizer 主文件 |
| `tokenizer_config.json` | Tokenizer 配置 |
| `special_tokens_map.json` | 特殊 token 映射 |
| `added_tokens.json` | 额外 token |
| `vocab.json`、`merges.txt` | BPE 词表与合并规则 |
| `chat_template.jinja` | Chat template |
| `Modelfile` | Ollama / Modelfile 风格运行配置参考 |
| `README.md` | 模型卡片 |

完整下载示例：

```bash
hf download suyuan37/SafetyRAISE-TS-Qwen3 --local-dir SafetyRAISE-TS-Qwen3
```

训练数据集文件建议：

| 数据集文件 | 用途 | 建议 |
| --- | --- | --- |
| `ts-sft.parquet` | SFT 训练主文件 | 首选 |
| `ts-dpo.parquet` | DPO / 偏好优化主文件 | 首选 |
| `ts-sft.jsonl`、`ts-dpo.jsonl` | JSONL 兼容格式 | 需要行式 JSON 管线时使用 |
| `ts-sft.json`、`ts-dpo.json` | 原始 JSON 数组格式 | 归档与兼容用途 |

## 在 SafetyRAISE 中接入

如果你用 vLLM、LM Studio、SGLang 或其他兼容 OpenAI Chat Completions 的服务加载本模型，建议：

1. 模型名填 `suyuan37/SafetyRAISE-TS-Qwen3`，或填你服务端映射后的别名
2. 服务地址填到 `EXPERT_LOCAL_BASE_URL`
3. 在 SafetyRAISE 的 `workflow.yaml` 或环境变量中完成接入

## 限制说明

1. 模型输出会受到输入事实完整性影响
2. 对缺失事实、模糊表述和材料冲突较敏感
3. 不应脱离检索增强和人工复核单独使用

## 许可

本模型仓库使用 Apache-2.0 许可发布。  
使用时还应同时遵守基座模型及相关依赖的许可要求。
