---
language: zh
license: apache-2.0
base_model: Qwen/Qwen2.5-1.5B-Instruct
tags:
- depression
- geriatric
- clinical-narrative
- lora
- chinese
---

# Geriatric Depression Clinical Narrative Model

Fine-tuned qwen2.5:1.5b for generating Chinese clinical narratives assessing depression risk in older adults.

## Model Details

- **Base Model**: Qwen/Qwen2.5-1.5B-Instruct
- **Fine-tuning Method**: LoRA (r=8, alpha=16)
- **Training Data**: 1,200 balanced samples from CHARLS (China Health and Retirement Longitudinal Study)
- **Task**: Generate clinical narratives explaining depression risk based on 15 patient features

## Input Features

| Feature | Description |
|---------|-------------|
| age | Age |
| female | Gender (0=Male, 1=Female) |
| education_years | Years of education |
| married | Marital status (0=Unmarried, 1=Married) |
| has_diabetes | Diabetes |
| has_hypertension | Hypertension |
| has_heart_disease | Heart disease |
| has_stroke | Stroke history |
| has_lung_disease | Lung disease |
| adl_total | ADL limitation count (0-6) |
| iadl_total | IADL limitation count (0-6) |
| cognition_total | Cognitive score (0-21) |
| grip_strength | Grip strength (kg) |
| fall_history | Fall history |
| drink_now | Current drinking |

## Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("your-username/geriatric-depression-llm")
tokenizer = AutoTokenizer.from_pretrained("your-username/geriatric-depression-llm")

system_prompt = "你是一位临床医生，请根据患者健康档案判断抑郁风险。回答必须以'该患者抑郁风险较高'或'该患者抑郁风险较低'开头。"
profile = "年龄72岁，女性，独居，患有糖尿病和高血压，ADL受限2项，认知得分8/21，握力18kg，生活满意度2。"

messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": f"请评估以下患者的抑郁风险：\n\n{profile}"},
]
text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
inputs = tokenizer(text, return_tensors="pt")
outputs = model.generate(**inputs, max_new_tokens=400, do_sample=True, temperature=0.3)
print(tokenizer.decode(outputs[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True))
```

## Performance

Evaluated on 200 real CHARLS patients:
- Accuracy: 63.5%
- Specificity: 98.0%
- PPV: 93.5%

## Citation

If you use this model, please cite:

```
[Paper title TBD]
[Authors TBD]
```

## License

Apache 2.0
