---
license: apache-2.0
tags:
- unsloth
- transformers
- pytorch
- medical
- chinese
- grpo
- text-generation
library_name: transformers
pipeline_tag: text-generation
language: zh
base_model: meta-llama/Llama-3.1-8B
datasets:
- FreedomIntelligence/medical-o1-reasoning-SFT
---

# Medical Model GRPO 16bit

这是一个使用GRPO（Generalized Relative Policy Optimization）技术微调的医学模型，专注于提供详细的医学分析和建议。模型基于Llama-3.1-8B，使用Unsloth的高效GRPO算法训练，能够生成格式化的医学推理和答案。

## 模型描述

本模型基于meta-llama/Llama-3.1-8B，使用Unsloth的GRPO技术进行微调，训练数据来自FreedomIntelligence/medical-o1-reasoning-SFT数据集。模型能够提供详细的医学推理过程和最终答案，输出格式为XML格式。

### 主要特点

- **医学专业性**：模型经过医学数据集的专门训练，能够提供专业的医学分析
- **推理能力增强**：通过GRPO技术增强模型的推理能力，生成更深入的分析
- **结构化输出**：使用`<reasoning>...</reasoning><answer>...</answer>`格式输出，便于解析
- **中文优化**：专为中文医学问答场景优化

## 使用方法

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# 加载模型和分词器
tokenizer = AutoTokenizer.from_pretrained("ZhangQiao123/medical-model-grpo-16bit")
model = AutoModelForCausalLM.from_pretrained(
    "ZhangQiao123/medical-model-grpo-16bit",
    torch_dtype=torch.float16,
    device_map="auto"
)

# 使用模型回答医学问题
def generate_medical_answer(question):
    system_prompt = "你是一个专业的医学AI助手，请根据问题提供详细的医学分析和建议。请先进行推理分析，然后给出最终答案。请使用<reasoning>标签包裹推理过程，使用<answer>标签包裹最终答案。"
    
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": question}
    ]
    
    # 尝试使用chat方法
    try:
        response = model.chat(tokenizer, messages)
        return response
    except AttributeError:
        # 如果没有chat方法，使用标准的generate方法
        prompt = f"{system_prompt}\n\n问题: {question}\n\n回答:"
        inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
        
        with torch.no_grad():
            outputs = model.generate(
                **inputs,
                max_new_tokens=2048,
                temperature=0.7,
                do_sample=True,
                top_p=0.9,
                repetition_penalty=1.1
            )
        
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        
        if "回答:" in response:
            response = response.split("回答:")[-1].strip()
        else:
            response = response[len(prompt):].strip()
        
        return response

# 测试模型
question = "高血压患者应该如何调整饮食？"
answer = generate_medical_answer(question)
print(f"问题: {question}")
print(f"回答: {answer}")
```

## Gradio界面示例

您还可以创建一个Gradio界面来更方便地使用模型：

```python
import gradio as gr
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# 加载模型和分词器
tokenizer = AutoTokenizer.from_pretrained("ZhangQiao123/medical-model-grpo-16bit")
model = AutoModelForCausalLM.from_pretrained(
    "ZhangQiao123/medical-model-grpo-16bit",
    torch_dtype=torch.float16,
    device_map="auto"
)

def generate_answer(question):
    system_prompt = "你是一个专业的医学AI助手，请根据问题提供详细的医学分析和建议。请先进行推理分析，然后给出最终答案。请使用<reasoning>标签包裹推理过程，使用<answer>标签包裹最终答案。"
    
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": question}
    ]
    
    try:
        response = model.chat(tokenizer, messages)
    except AttributeError:
        prompt = f"{system_prompt}\n\n问题: {question}\n\n回答:"
        inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
        
        with torch.no_grad():
            outputs = model.generate(
                **inputs,
                max_new_tokens=2048,
                temperature=0.7,
                do_sample=True,
                top_p=0.9,
                repetition_penalty=1.1
            )
        
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        
        if "回答:" in response:
            response = response.split("回答:")[-1].strip()
        else:
            response = response[len(prompt):].strip()
    
    # 格式化输出，使XML标签更易读
    response = response.replace("<reasoning>", "<b>推理过程：</b><br>")
    response = response.replace("</reasoning>", "<br><br>")
    response = response.replace("<answer>", "<b>最终答案：</b><br>")
    response = response.replace("</answer>", "")
    
    return response

# 创建Gradio界面
demo = gr.Interface(
    fn=generate_answer,
    inputs=gr.Textbox(lines=3, placeholder="请输入您的医学问题..."),
    outputs="html",
    title="医学AI助手",
    description="基于GRPO微调的医学模型，可以回答医学相关问题并提供详细的推理过程和答案。"
)

# 启动界面
demo.launch()
```

## 训练细节

- **训练方法**：GRPO（Generalized Relative Policy Optimization）
- **训练数据集**：FreedomIntelligence/medical-o1-reasoning-SFT
- **训练步数**：1000+
- **基础模型**：meta-llama/Llama-3.1-8B
- **训练环境**：Colab Pro+，40GB GPU RAM
- **LoRA配置**：
  - rank: 32
  - alpha: 16
  - dropout: 0.05
  - 目标模块: q_proj, k_proj, v_proj, o_proj, gate_proj, up_proj, down_proj

### 奖励函数

模型训练使用了以下奖励函数：

1. **medical_correctness_reward_func**：评估医学回答的正确性
2. **medical_terminology_reward_func**：评估医学术语的使用情况
3. **strict_format_reward_func**和**soft_format_reward_func**：检查输出格式是否符合XML规范
4. **xmlcount_reward_func**：计算XML标签的使用情况
5. **reasoning_depth_reward_func**：评估医学推理的深度和质量

## 输出格式

模型输出采用XML格式，包含推理过程和最终答案：

```
<reasoning>
详细的医学推理过程...
</reasoning>
<answer>
最终医学建议和答案...
</answer>
```

## 局限性

- 模型可能在极其专业的医学领域知识有限
- 不应将模型输出作为专业医疗建议的替代
- 对于罕见疾病或最新医学研究可能了解有限

## 引用

如果您使用了本模型，请引用：

```
@misc{ZhangQiao123_medical_model_grpo,
  author = {ZhangQiao123},
  title = {Medical Model GRPO 16bit},
  year = {2025},
  publisher = {Hugging Face},
  journal = {Hugging Face repository},
  howpublished = {\url{https://huggingface.co/ZhangQiao123/medical-model-grpo-16bit}},
}
```

## 许可证

本模型使用 Apache 2.0 许可证。
