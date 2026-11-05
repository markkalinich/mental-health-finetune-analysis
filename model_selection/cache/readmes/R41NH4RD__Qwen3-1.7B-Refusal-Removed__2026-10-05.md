---
license: mit
base_model: Qwen/Qwen3-1.7B
tags:
  - qwen3
  - refusal-removal
  - activation-ablation
  - model-editing
language:
  - zh
  - en
pipeline_tag: text-generation
---

# Qwen3-1.7B Refusal Removed

基于 [Qwen/Qwen3-1.7B](https://huggingface.co/Qwen/Qwen3-1.7B)，通过激活消融（Activation Ablation）技术移除拒绝行为的编辑版本。

## 模型说明

本模型是使用 [LLM-Refusal-Remover](https://github.com/Glimmer114514/LLM-Refusal-Remover) 工具对 Qwen3-1.7B 进行"脑手术"后的产物。通过识别模型内部的"拒绝方向"（refusal direction），利用正交投影从指定 Transformer 层的 MLP `down_proj` 权重中剔除该方向，从而改变模型对敏感输入的响应模式。

> ⚠️ **免责声明**：本模型仅用于学术研究和技术探索。编辑后的模型可能产生不可预期的输出，请谨慎使用，并遵守相关法律法规。

## 手术参数

| 参数 | 值 |
|------|-----|
| 基础模型 | Qwen/Qwen3-1.7B |
| 手术层范围 | 8-18（共 11 层） |
| 消融系数（ablation-scale） | 1.0（完全消融） |
| 数据类型 | float16 |
| 有害提示词数量 | 53 条（中英双语，覆盖 9 大类别） |
| 无害提示词数量 | 38 条（中英双语） |

## 模型架构

| 属性 | 值 |
|------|-----|
| 模型类型 | Qwen3ForCausalLM |
| 隐藏层大小 | 2048 |
| 注意力头数 | 16 |
| KV 头数 | 8 |
| 层数 | 28 |
| 中间层大小 | 6144 |
| 词表大小 | 151936 |
| 最大位置编码 | 40960 |
| 激活函数 | SiLU |

## 使用方法

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "R41NH4RD/Qwen3-1.7B-Refusal-Removed"

tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype="auto",
    trust_remote_code=True,
    device_map="auto"
)
model.eval()

messages = [{"role": "user", "content": "你的问题"}]
prompt = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True,
    enable_thinking=False,
)
inputs = tokenizer([prompt], return_tensors="pt").to(model.device)

with torch.inference_mode():
    output = model.generate(
        **inputs,
        max_new_tokens=512,
        do_sample=True,
        temperature=0.7,
        top_p=0.8,
        pad_token_id=tokenizer.eos_token_id,
    )

response = tokenizer.decode(output[0, inputs["input_ids"].shape[1]:], skip_special_tokens=True)
print(response)
```

## 工具与项目

- 🔧 **手术工具**：[LLM-Refusal-Remover (GitHub)](https://github.com/Glimmer114514/LLM-Refusal-Remover)
- 📖 **使用文档**：项目 README 中包含完整的使用说明、原理介绍和参数配置指南

## 许可证

本模型采用 [MIT License](LICENSE) 开源许可。基础模型 Qwen3-1.7B 遵循其原始许可证。
