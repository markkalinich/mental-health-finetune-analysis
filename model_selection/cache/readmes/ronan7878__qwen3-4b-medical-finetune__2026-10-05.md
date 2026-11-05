---
base_model: Qwen/Qwen3-4B-Instruct-2507
library_name: transformers
license: apache-2.0
language:
- zh
tags:
- qwen3
- medical
- traditional-chinese-medicine
- western-medicine
- qlora
- lora-merged
- text-generation
---

# Qwen3-4B Medical Fine-tune

This is a merged fine-tuned model based on `Qwen/Qwen3-4B-Instruct-2507`.

## Intended Use

The model is designed for medical question-answering experiments with a focus on Traditional Chinese Medicine.

The intended training mix is:

- 80% Traditional Chinese Medicine data
- 20% western/general medical reasoning data

## Training Data

The training pipeline uses public datasets:

- `DigitalIntelligenceCenter-of-ICMM/Baize-TCM-Corpus-for-Large-Language-Models-V3`
- `FreedomIntelligence/medical-o1-reasoning-SFT`

Please review the original dataset licenses and terms before commercial use.

## Limitations

This model is a portfolio and research fine-tune. It is not a medical device and must not be used as a substitute for professional diagnosis or treatment.

It may:

- produce incorrect medical advice
- confuse Traditional Chinese Medicine and western medical concepts
- hallucinate prescriptions, herbs, dosages, contraindications, or diagnoses
- miss emergency warning signs

For real-world use, connect it to verified clinical guidelines and require professional review.

## Example

```text
User: 最近睡眠不好，舌苔厚腻，容易疲劳，可能是什么情况？
Assistant: 从中医角度看，舌苔厚腻和疲劳可能与湿困脾胃等因素有关，但仅凭这些信息不能诊断。建议结合饮食、二便、脉象和既往病史综合判断，并咨询专业医生。
```
