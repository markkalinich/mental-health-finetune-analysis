---
license: apache-2.0
tags:
- unsloth
- trl
- sft
datasets:
- Congliu/Chinese-DeepSeek-R1-Distill-data-110k
- Kedreamix/psychology-10k-Deepseek-R1-zh
---

# Model Card for DeepSeek-R1-Psychology-COT

## Model Description
Xinjing-LM 是一个专注于心理健康领域的智能助手，基于 Qwen 模型进行微调和优化，旨在理解复杂的心理学知识、生成高质量文本并支持多轮对话。通过数据蒸馏、指令微调和多轮对话构建等技术，Xinjing-LM 在心理健康场景中表现出色，能够为用户提供准确、流畅且逻辑严谨的心理学相关建议。

## 项目亮点

- **多源数据融合**：结合开源数据集与 AI 合成数据，确保模型在多样性和专业性上的平衡。
- **多轮对话构建**：通过情感类型和生活场景的组合生成对话数据，提升模型在实际应用中的交互能力。
- **高效微调策略**：采用全参数微调与 LoRA 技术相结合的方式，在保证性能的同时降低计算资源消耗。
- **数据蒸馏优化**：利用 DeepSeek R1 生成的高质量数据，进一步提升模型的推理效率和准确性。

## 数据集

我们使用了以下数据集进行模型训练和优化：

- **Chinese-Data-Distill-From-R1**：开源中文蒸馏数据集，涵盖数学、考试、STEM 和通用类型数据。
- **psychology-10k-sft**：包含 10,000 条心理学相关指令微调数据。
- **psychology-10k-sft-zh**：将 psychology-10k-sft 的英文数据翻译为中文。
- **心理健康-R1蒸馏中文数据集-10k**：利用 DeepSeek R1 生成的心理健康相关推理数据。
- **多轮对话数据集**：通过情感类型和生活场景组合生成的多轮对话数据。

## 模型选择与微调

1. 先用**Congliu/Chinese-DeepSeek-R1-Distill-data-110k**对 **Qwen2.5-7B-Instruct** 进行SFT，全量微调，使得模型具备强大的中文推理能力，**Mingsmilet/Qwen2.5-7B-R1-SFT**已经训练好模型。
2. 再对SFT后的模型使用**LoRA** 技术进行优化。微调后的模型在心理健康领域的表现显著提升，能够处理复杂的心理学场景和多轮对话。

## Usage

### Fine-tuning Code Example

Below is the code to fine-tune the model using the `unsloth` and `trl` libraries:

```python
# Modules for inference
import unsloth
from unsloth import FastLanguageModel
import torch # Import PyTorch
from trl import SFTTrainer # Trainer for supervised fine-tuning (SFT)
from unsloth import is_bfloat16_supported # Checks if the hardware supports bfloat16 precision
# Hugging Face modules
from transformers import TrainingArguments # Defines training hyperparameters
from datasets import load_dataset # Lets you load fine-tuning datasets

model_id = "cvGod/DeepSeek-R1-Psychology-COT"
model, tokenizer = FastLanguageModel.from_pretrained(
    model_name=model_id,
    max_seq_length=4096,
    dtype=None,
    load_in_4bit=True,
    
)

prompt_style = """以下是一项任务说明，并附带了更详细的背景信息。
请撰写一个满足完成请求的回复。
在回答之前，请仔细考虑问题，并创建一个逐步的思考链，以确保逻辑和准确的回答。

### Instruction:
你是一个专业的心里专家专家,请你根据以下问题回答。
### Question:
{}
### Response:
{}"""
EOS_TOKEN = tokenizer.eos_token

question = """我晚上难以入睡，我认为这是因为我对工作感到压力"""

# Load the inference model using FastLanguageModel (Unsloth optimizes for speed)
FastLanguageModel.for_inference(model)  # Unsloth has 2x faster inference!

# Tokenize the input question with a specific prompt format and move it to the GPU
inputs = tokenizer([prompt_style.format(question, "")], return_tensors="pt").to("cuda")

# Generate a response using LoRA fine-tuned model with specific parameters
outputs = model.generate(
    input_ids=inputs.input_ids,          # Tokenized input IDs
    attention_mask=inputs.attention_mask, # Attention mask for padding handling
    max_new_tokens=4096,                  # Maximum length for generated response
    use_cache=True,                        # Enable cache for efficient generation
)

# Decode the generated response from tokenized format to readable text
response = tokenizer.batch_decode(outputs)

# Extract and print only the model's response part after "### Response:"
print(response[0].split("### Response:")[1])