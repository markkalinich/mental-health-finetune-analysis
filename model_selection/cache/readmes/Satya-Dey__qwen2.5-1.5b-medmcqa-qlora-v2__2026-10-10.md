---
license: apache-2.0
base_model: Qwen/Qwen2.5-1.5B-Instruct
datasets:
- openlifescienceai/medmcqa
tags:
- medical
- question-answering
- qlora
language:
- en
---

# Qwen2.5-1.5B Fine-tuned on MedMCQA (v2)

## Model Description
Fine-tuned version of [Qwen2.5-1.5B-Instruct](https://huggingface.co/Qwen/Qwen2.5-1.5B-Instruct)
on the [MedMCQA](https://huggingface.co/datasets/openlifescienceai/medmcqa) dataset using QLoRA.
MedMCQA contains ~182k multiple-choice questions from AIIMS and NEET-PG Indian medical entrance
exams across 23 subjects. Only single-choice questions were used for training and evaluation.

## Training Details

| Parameter | Value |
|---|---|
| Method | QLoRA (4-bit nf4 + LoRA) |
| LoRA rank | 16 |
| LoRA alpha | 32 |
| Learning rate | 2e-4 (cosine schedule) |
| Epochs | 1 |
| Effective batch size | 16 |
| Best checkpoint | Step 5600 (selected by lowest eval loss) |
| Hardware | Google Colab A100 40GB |

## Evaluation

Evaluated on the full MedMCQA validation set (2,816 single-choice questions):

| | Accuracy |
|---|---|
| **This model** | **42.5%** |
| Base model (no fine-tune) | ~39% (estimated) |
| Random baseline | 25% |

### Subject-wise Accuracy

| Subject | Accuracy | Questions |
|---|---|---|
| Biochemistry | 60.7% | 122 |
| Pathology | 51.4% | 259 |
| Pharmacology | 49.2% | 179 |
| Pediatrics | 48.9% | 133 |
| Physiology | 46.6% | 133 |
| Microbiology | 45.9% | 74 |
| Medicine | 44.9% | 185 |
| Gynaecology & Obstetrics | 42.2% | 154 |
| Surgery | 41.4% | 249 |
| Dental | 37.0% | 845 |
| Anatomy | 35.4% | 147 |

Note: Dental accounts for 30% of the evaluation set and is the weakest subject,
reflecting limited dental knowledge in the base model's pre-training.

## Usage
```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model     = AutoModelForCausalLM.from_pretrained("Satya-Dey/qwen2.5-1.5b-medmcqa-qlora-v2")
tokenizer = AutoTokenizer.from_pretrained("Satya-Dey/qwen2.5-1.5b-medmcqa-qlora-v2")

prompt = (
    "### Question:\n"
    "Commonest site of aortic aneurysm?\n"
    "A) Ascending aorta  B) Arch of aorta  "
    "C) Descending thoracic aorta  D) Infrarenal abdominal aorta\n\n"
    "### Answer:\n"
)

inputs  = tokenizer(prompt, return_tensors="pt")
outputs = model.generate(**inputs, max_new_tokens=5, do_sample=False)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
