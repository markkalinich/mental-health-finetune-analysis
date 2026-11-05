---
license: apache-2.0
datasets:
- >-
  DigitalIntelligenceCenter-of-ICMM/Baize-TCM-Corpus-for-Large-Language-Models-V2
language:
- zh
base_model:
- Qwen/Qwen3-8B
pipeline_tag: question-answering
---
# 白泽中医药大语言模型 V3 - 16bit 
**Baize-Traditional-Chinese-Medicine-Large-Language-Model-V3-16bit**

🩺 **领域专用 | 中医药智能问答 **

> 🐉 “白泽”取自中国古代通晓万物的神兽，寓意“通晓中医，智启未来”。本模型致力于推动中医药知识的智能化传承。

---

## 📚 模型简介

**Baize-TCM-LLM-V2** 是一个专为**中医药领域**设计的大语言模型，基于通用大模型在 **10,578 条高质量中医问答语料** 上进行指令微调（Supervised Fine-Tuning）。

该模型适用于：
- 中医智能问答系统
- 中医药知识辅助诊断
- 医学生教学与考试辅助
- 低资源环境下的本地化部署

---

## 🏗️ 模型架构

| 项目 | 说明 |
|------|------|
| 基础模型 | Qwen3-8B
| 微调数据 | [Baize-TCM-Corpus-for-Large-Language-Models-V2](https://huggingface.co/datasets/your-username/baize-tcm-corpus-v2) |
| 参数量 | ~8B 
| 量化方式 | 未量化
| 量化工具 | 
| 上下文长度 | 2048 tokens |
| 训练方式 | LoRA 

---

## 🚀 快速使用（Inference）

### 方法 ：使用 `transformers` 加载（推荐）

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# 模型名称
model_name = "your-username/Baize-Traditional-Chinese-Medicine-Large-Language-Model-V2-16bit"

# 加载 tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)

# 加载模型，使用 float16（16-bit）半精度，不进行量化
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float16,      # 使用 float16
    device_map="auto",              # 自动分配 GPU 显存
    trust_remote_code=True          # 支持自定义模型代码
)

# 推理
prompt = "问题：气虚的主要症状有哪些？\n答案："
inputs = tokenizer(prompt, return_tensors="pt").to("cuda")

outputs = model.generate(
    **inputs,
    max_new_tokens=200,
    temperature=0.7,
    do_sample=True
)

print(tokenizer.decode(outputs[0], skip_special_tokens=True))