---
base_model:
- microsoft/phi-4
library_name: peft
---
# Model Card for XM-phi

## Model Details

### Model Description

XM-phi-medical 是一款先进的医学诊断助手，结合了最新的自然语言处理技术和医学知识库，旨在辅助医生进行疾病诊断、病症分析以及治疗建议。

该模型可以解析患者病史、实验室检查结果以及影像学报告，提供基于循证医学的参考意见，帮助医疗工作者提升诊断效率和准确性。

其核心价值观是“精准、可靠、以患者为中心”，始终遵循医学伦理与行业法规，助力医疗行业智能化升级。

- **开发者:** 重庆埃克斯曼得信息技术有限公司
- **版本:** 1.0
- **发布日期:** 2025-03-15
- **模型类型:** 医学诊断辅助模型
- **支持语言:** 中文（主要）、英文（部分支持）
- **基于模型:** Microsoft/Phi-4

## Uses

### 直接用途

- 支持多种医学领域（内科、外科、儿科、皮肤科等）的疾病诊断辅助。
- 解析医学文本，如病历、检查报告、影像学描述等，并提供初步诊断建议。
- 根据症状、病史和体征，提供可能的疾病列表及其鉴别诊断依据。
- 提供基于最新医学文献的治疗方案推荐，支持个性化医疗建议。
- 具备医学知识问答能力，可解答常见疾病相关问题。
- 可用于医学研究、医学教育及智能医疗系统的集成应用。

### 下游用途

- 医学影像分析与辅助诊断。
- 电子病历分析与结构化处理。
- 医疗聊天机器人开发。
- 医学研究与数据挖掘。

### 禁止用途

- 该模型仅作为医学辅助工具，不能代替医生的专业判断。
- 不能用于紧急医疗情况的处理，遇到急性病症或危及生命的情况，用户应立即就医。
- 不能提供非法医疗建议或处方药推荐。
- 需遵守数据隐私法规（如 HIPAA、GDPR），不能存储或泄露患者隐私数据。

## 偏见、风险和限制

- 诊断结果基于已有医学文献和数据库，可能存在更新滞后或信息偏差。
- 不能代替专业医生的判断，用户在使用时应结合专业意见。
- 可能存在误诊风险，需谨慎参考。

### 建议

- 用户（包括医生和患者）在使用模型时，需结合专业医学知识进行判断。
- 模型应定期更新医学知识库，以提高准确性。

## 如何开始使用该模型

```python
from peft import PeftModel
from transformers import AutoModelForCausalLM

base_model = AutoModelForCausalLM.from_pretrained("unsloth/Phi-4")
model = PeftModel.from_pretrained(base_model, "xmindai/xmindai_trans")

input_text = "患者出现持续性头痛并伴有恶心，可能的原因是什么？"
inputs = tokenizer(input_text, return_tensors="pt")
outputs = model.generate(**inputs)
print(tokenizer.decode(outputs[0]))
```

## 训练细节

### 训练数据
[FreedomIntelligence/Medical-R1-Distill-Data-Chinese · Datasets at Hugging Face](https://huggingface.co/datasets/FreedomIntelligence/Medical-R1-Distill-Data-Chinese)
- 训练数据来源于公开的医学文献、病例数据库、医学问答数据等。
- 数据经过清理和预处理，以确保质量和一致性。

### 训练过程

#### 预处理

- 数据清洗，去除噪音数据。
- 归一化处理，提高模型泛化能力。

#### 训练超参数

- **训练精度:** bf16 mixed precision

## 评估

### 测试数据、因素与指标

#### 测试数据

- 使用医学诊断标准数据集进行测试。

#### 评估因素

- 诊断准确率
- 召回率
- 误诊率

#### 评估指标

- F1-score
- Precision
- Recall

## 环境影响

- **碳排放:** 可使用 [Machine Learning Impact calculator](https://mlco2.github.io/impact#compute) 估算。

## 技术规格

### 模型架构与目标

- 基于 transformer 结构，适用于医学文本理解和问答。

### 计算基础设施

#### 软件

- **框架版本:**
    - PEFT 0.14.0
    - Transformers 4.x

## 模型卡作者

- 重庆埃克斯曼得信息技术有限公司研发组