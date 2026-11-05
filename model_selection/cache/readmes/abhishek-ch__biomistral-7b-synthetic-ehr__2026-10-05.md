---
language:
- en
- fr
- nl
- es
- it
- pl
- ro
- de
license: apache-2.0
library_name: transformers
tags:
- mergekit
- merge
- dare
- medical
- biology
- mlx
datasets:
- health_fact
base_model:
- BioMistral/BioMistral-7B
- mistralai/Mistral-7B-Instruct-v0.1
pipeline_tag: text-generation
---
# abhishek-ch/biomistral-7b-synthetic-ehr

![image/png](https://cdn-uploads.huggingface.co/production/uploads/6460910f455531c6be78b2dd/tGtYB0b3eS7A4zbqp1xz0.png)


This model was converted to MLX format from [`BioMistral/BioMistral-7B-DARE`]().
Refer to the [original model card](https://huggingface.co/BioMistral/BioMistral-7B-DARE) for more details on the model.


## Use with mlx

```bash
pip install mlx-lm
```

The model was LoRA fine-tuned on [health_facts](https://huggingface.co/datasets/health_fact) and 
Synthetic EHR dataset inspired by MIMIC-IV using the format below, for 1000 steps (~1M tokens) using mlx.

```python
def format_prompt(prompt:str, question: str) -> str:
    return """<s>[INST]
## Instructions
{}
## User Question
{}.
[/INST]</s> 
""".format(prompt, question)
```

Example For Synthetic EHR Diagnosis System Prompt
```
You are an expert in provide diagnosis summary based on clinical notes inspired by MIMIC-IV-Note dataset.
These notes encompass Chief Complaint along with Patient Summary & medical admission details.
```

Example for Healthfacts Check System Prompt
```
You are a Public Health AI Assistant. You can do the fact-checking of public health claims. \nEach answer labelled with true, false, unproven or mixture. \nPlease provide the reason behind the answer
```

## Loading the model using `mlx`

```python
from mlx_lm import generate, load
model, tokenizer = load("abhishek-ch/biomistral-7b-synthetic-ehr")
response = generate(
    fused_model,
    fused_tokenizer,
    prompt=format_prompt(prompt, question),
    verbose=True,  # Set to True to see the prompt and response
    temp=0.0,
    max_tokens=512,
)
```

## Loading the model using `transformers`

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
repo_id = "abhishek-ch/biomistral-7b-synthetic-ehr"
tokenizer = AutoTokenizer.from_pretrained(repo_id)
model = AutoModelForCausalLM.from_pretrained(repo_id)
model.to("mps")
input_text = format_prompt(system_prompt, question)
input_ids = tokenizer(input_text, return_tensors="pt").to("mps")
outputs = model.generate(
    **input_ids,
    max_new_tokens=512,
)
print(tokenizer.decode(outputs[0]))
```
