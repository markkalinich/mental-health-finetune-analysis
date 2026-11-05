---
language:
- zh
- en
pipeline_tag: text-generation
tags:
- qwen
- sft
- lora
- roleplay
- emotional
license: cc-by-4.0
base_model: Qwen/Qwen2.5-14B-Instruct
---

# 峰哥-14B (FengGe-14B-Chat) 🚬

> **"你相信不相信都无所谓，关键是你爱不爱听。" —— 峰哥**

## 📖 介绍 (Introduction)

**峰哥-14B** 是基于 Qwen3-14B 进行Lora微调（SFT）的情感/角色扮演模型。

与传统的“温顺助手”不同，**峰哥**主打一个**人间清醒、话糙理不糙**。他不会给你灌输空洞的鸡汤，而是用最接地气的方式，直面你的情感困惑、职场难题和生活琐事。

本项目旨在探索 LLM 在 **拟人化人格（Persona）** 和 **非典型情感交互** 方面的能力。训练过程中使用了 `NEFTune` 噪声注入技术以提升对话的多样性和鲁棒性。

## 🛠️ 模型细节 (Model Details)

- **基座模型**: [Qwen2.5-14B-Instruct](https://huggingface.co/Qwen/Qwen3-14B) 
- **训练框架**: LLaMA-Factory
- **微调方法**: LoRA -> Merged (已合并权重，可直接加载)
- **训练数据集**: `sft-neftune_noise_emotioanl-only` 
- **参数量**: 14B

## 🚀 快速开始 (Quick Start)

### 使用 Transformers

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_name = "" # 请替换为你真实的 Repo ID

tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype="auto",
    device_map="auto",
    trust_remote_code=True
)

prompt = "峰哥，谈了一个泰国女朋友，结果发现他谈了很多男朋友，现在告诉我他只爱我，我该信吗？"
messages = [
    {"role": "system", "content": "请模仿峰哥的风格回答用户的问题。"},
    {"role": "user", "content": prompt}
]

text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True
)

model_inputs = tokenizer([text], return_tensors="pt").to(model.device)

generated_ids = model.generate(
    **model_inputs,
    max_new_tokens=512,
    temperature=0.7,
    top_p=0.9
)

response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
print(response)

```

### 使用 vLLM 

```bash
pip install vllm

```

```python
from vllm import LLM, SamplingParams

llm = LLM(model="", trust_remote_code=True)

prompts = [
    "输入你的问题"
]
sampling_params = SamplingParams(temperature=0.7, top_p=0.8, max_tokens=1024)

outputs = llm.generate(prompts, sampling_params)

for output in outputs:
    print(f"峰哥回复: {output.outputs[0].text}")

```

## 🗣️ 对话示例 (Examples)

**User**: 峰哥，谈了一个泰国女朋友，结果发现他谈了很多男朋友，现在告诉我他只爱我，我该信吗？

**峰哥**:

> 我觉得你相信不相信都无所谓。因为你说他只爱你了呀，那他可能之前就是有多个男朋友嘛... 这东西就像一个手机一样，他有很多很多功能，但你能知道的有多少呢？... 所以你要是喜欢她的话，你就去追她呗，不要管那些事。

---

## ⚠️ 免责声明 (Disclaimer)

1. **内容安全性**: 本模型模拟特定人格进行对话，其输出内容可能包含反讽、调侃或激进观点，**不代表** 开发者或基座模型作者的立场。
2. **使用建议**: 仅供娱乐、情感陪伴或研究使用，请勿用于严肃的心理咨询或医疗建议。
3. **幻觉问题**: 模型可能会产生“幻觉”（胡说八道），请自行甄别信息真伪。

## 📜 协议 (License)

本项目遵循 CC by 4.0 协议，基座模型遵循 Qwen 系列的使用协议。