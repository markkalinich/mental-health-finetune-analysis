---
base_model: unsloth/Phi-3-mini-4k-instruct-bnb-4bit
datasets:
- medalpaca/medical_meadow_medqa
language:
- en
metrics:
- rouge
library_name: transformers
pipeline_tag: question-answering
license: apache-2.0
tags:
- medical-qa
- qlora
- peft
- unsloth
- trl
- transformers
new_version: merged-16bit
model-index:
- name: phi_medical_qa_finetune_16bit
  results:
  - task:
      type: question-answering
    dataset:
      type: medalpaca/medical_meadow_medqa
      name: Medical Meadow MedQA
    metrics:
    - type: rouge1
      value: 0.6212
    - type: rouge2
      value: 0.5815
    - type: rougeL
      value: 0.6195
---

# phi_medical_qa_finetune_16bit

A 16-bit merged medical question-answering model fine-tuned with QLoRA on the Medical Meadow MedQA dataset.

- **Developed by:** A-Kishore
- **Base model:** `unsloth/Phi-3-mini-4k-instruct-bnb-4bit`
- **License:** Apache-2.0
- **Task:** Medical question answering
- **Training approach:** QLoRA with PEFT adapters, merged into a 16-bit checkpoint for inference

## Model details

This checkpoint was trained to answer medical QA prompts in an instruction-following format. The training workflow uses the `unsloth` stack together with `transformers`, `peft`, `trl`, `bitsandbytes`, and `datasets`.

The dataset used in the notebook is `medalpaca/medical_meadow_medqa`, and the examples are formatted into a system/user/assistant prompt structure for supervised finetuning.

## Intended use

This model is intended for educational and research purposes, and for prototyping medical QA assistants. It should not be used as a substitute for clinical judgment, diagnosis, or treatment recommendations.

## Evaluation results

Evaluation was run on 1,018 examples with ROUGE metrics.

| Metric  |  Score |
| ------- | -----: |
| ROUGE-1 | 0.6212 |
| ROUGE-2 | 0.5815 |
| ROUGE-L | 0.6195 |

## Example usage

```python
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

model_id = "A-Kishore/phi_medical_qa_finetune_16bit"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id)

pipe = pipeline("question-answering", model=model, tokenizer=tokenizer)

prompt = "You are a medical AI. Answer the question clearly and concisely.\n\nQuestion: What is the most likely diagnosis for a patient with fever, rash, and migratory arthritis?"
print(pipe(prompt, max_new_tokens=128, do_sample=False)[0]["generated_text"])
```

## Limitations

The model can produce incorrect or overconfident answers, especially for ambiguous or poorly specified prompts. Review outputs carefully, and do not rely on this model for real-world medical decisions without qualified human oversight.