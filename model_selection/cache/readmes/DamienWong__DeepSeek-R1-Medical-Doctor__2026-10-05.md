# DeepSeek-R1-Distill-Qwen-14B Merged Model

## 📌 模型简介

本模型基于 **DeepSeek-R1-Distill-Qwen-14B** 进行微调，并已合并 LoRA 适配器，形成独立可用的完整模型，适用于医学领域的问答和推理任务。

- 🔹 **基座模型**: [deepseek-ai/DeepSeek-R1-Distill-Qwen-14B](https://huggingface.co/models/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B)
- 🔹 **微调方法**: LoRA + 合并 (`merged_16bit`)
- 🔹 **适用场景**: 医学文本问答、医学知识增强
- 🔹 **模型格式**: `fp16`

---

## 📂 使用方法

### 🔄 直接加载模型

合并后的模型可以直接加载并进行推理，无需额外加载 LoRA 适配器。

```python
from unsloth import FastLanguageModel
from transformers import TextStreamer

merged_model = ""

max_seq_length = 1280
dtype = None
load_in_4bit = True

model, tokenizer = FastLanguageModel.from_pretrained(
    "Tierney/DeepSeek-Qwen-14B-R1-Medical-Doctor",
    max_seq_length=max_seq_length,
    dtype=dtype,
    load_in_4bit=load_in_4bit,
)
tokenizer.pad_token = "<|endoftext|>"
```

### 🚀 推理示例

```python
prompt_style = """以下是描述任务的说明，并附有提供进一步背景的输入。
请写一个恰当的回应，完成该任务。
在回答之前，请仔细思考问题，并创建一个逐步的思维链，以确保逻辑清晰且准确。

### 任务描述:
您是一位在临床推理、诊断和治疗计划方面具有高级知识的医学专家。
请回答以下医学问题。

### 问题:
{}

### 回答:
{}"""
question = f"患者姓名：{name}，年龄：{age}，医疗情况：{medical}，检查情况：{instra}，请根据这些信息给出诊断和建议。"
prompt = prompt_style.format(question, "")

input_text = "请问阿司匹林的主要适应症是什么？"
FastLanguageModel.for_inference(model)
inputs = tokenizer([prompt], return_tensors="pt").to("cuda")

text_streamer = TextStreamer(tokenizer)
outputs = model.generate(**inputs, streamer=text_streamer, max_new_tokens=1024)
answer = tokenizer.decode(outputs[0], skip_special_tokens=True).split("### 回答:")[-1].strip()

```

---

## 🏗️ 训练信息

- **训练环境**: RTX 4090, CUDA 12.6, WSL Ubuntu
- **训练框架**: `transformers` + `peft` + `unsloth`
- **训练参数**:
  - LoRA Rank: 16
  - Alpha: 32
  - Dropout: 0.05
  - Max Seq Length: 4096
- **合并方式**: `merged_16bit` (FP16 精度)

---

## 📜 许可证

本模型基于 **DeepSeek-R1-Distill-Qwen-14B**，请遵守其[官方许可证](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B)。

---

## 📞 联系方式

如果你有任何问题或建议，可以在讨论区留言，或者联系我！
