---
license: apache-2.0
language:
- en
- zh
pipeline_tag: text-generation
library_name: transformers
tags:
- qwen2
- qwen2.5
- qwen2.5-72b
- causal-lm
- rlhf
- reinforcement-learning
- safetensors
base_model: Qwen/Qwen2.5-72B
---

# Innospark-72b-safety

## 所属项目

本模型是 [InnoSpark-Safety](https://github.com/ZeroLoss-Lab/InnoSpark-Safety) 教育场景大语言模型安全框架中的安全对齐底座模型。该框架围绕用户输入、模型生成与服务化调用三个环节，提供前置拦截、安全对齐、后置审核与 OpenAI 兼容 API 代理能力。

## 模型概述

本仓库包含一个基于 Qwen/Qwen2.5-72B、通过强化学习（RL）训练得到的安全对齐 72B 参数因果语言模型检查点。

| 属性 | 值 |
|-----------|-------|
| 架构 | Qwen2ForCausalLM |
| 基座模型 | Qwen/Qwen2.5-72B |
| 隐藏层维度 | 8192 |
| 层数 | 80 |
| 注意力头（GQA） | 64 query / 8 key-value |
| FFN 中间维度 | 29568 |
| 词表大小 | 152064 |
| 上下文长度 | 32768 |
| 滑动窗口 | 131072 |
| 权重类型 | bfloat16 |
| 格式 | Safetensors（31 个分片，约 145 GB） |

## 文件清单

- `config.json`、`generation_config.json`、`tokenizer_config.json`
- `tokenizer.json`、`vocab.json`、`merges.txt`、`added_tokens.json`、`special_tokens_map.json`
- `model.safetensors.index.json`
- `model-00001-of-00031.safetensors` ... `model-00031-of-00031.safetensors`
- `.gitattributes`


## 使用方法

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "ZeroLoss-Lab/Innospark-72b-safety"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype="auto",
    device_map="auto",
)

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello, what can you do?"},
]
text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
inputs = tokenizer([text], return_tensors="pt").to(model.device)
outputs = model.generate(**inputs, max_new_tokens=512)
response = tokenizer.batch_decode(outputs, skip_special_tokens=True)[0]
print(response)
```

## 生成配置

- Temperature: 0.7
- Top-p: 0.8
- Top-k: 20
- Repetition penalty: 1.05
- EOS token IDs: 151645, 151643

## 相关资源

- GitHub 仓库（完整安全框架）：https://github.com/ZeroLoss-Lab/InnoSpark-Safety
- 前置输入审核模型：[ZeroLoss-Lab/egs-bert-input-moderator](https://huggingface.co/ZeroLoss-Lab/egs-bert-input-moderator)
- 后置响应审核模型：[ZeroLoss-Lab/egs-bert-response-auditor](https://huggingface.co/ZeroLoss-Lab/egs-bert-response-auditor)

## 许可证

本模型采用 Apache-2.0 许可证发布。
