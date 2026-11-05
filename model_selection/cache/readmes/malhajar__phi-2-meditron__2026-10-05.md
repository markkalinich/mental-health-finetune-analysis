---
language:
- en
tags:
- Medicine
datasets:
- epfl-llm/guidelines
license: ms-pl
base_model: microsoft/phi-2
---
# Model Card for Model ID

<!-- Provide a quick summary of what the model is/does. -->
phi-2-meditron is a finetuned version of [`epfl-llm/meditron-7b`](https://huggingface.co/epfl-llm/meditron-7b) using SFT Training on the Meditron Dataset.
This model can answer information about different excplicit ideas in medicine (see [`epfl-llm/meditron-7b`](https://huggingface.co/epfl-llm/meditron-7b) for more info)

### Model Description

- **Finetuned by:** [`Mohamad Alhajar`](https://www.linkedin.com/in/muhammet-alhajar/) 
- **Language(s) (NLP):** English
- **Finetuned from model:** [`microsoft/phi-2`](https://huggingface.co/microsoft/phi-2)

### Prompt Template
```
### Instruction:

<prompt> (without the <>)

### Response:
```


## How to Get Started with the Model

Use the code sample provided in the original post to interact with the model.
```python
from transformers import AutoTokenizer,AutoModelForCausalLM
 
model_id = "malhajar/phi-2-meditron"
model = AutoModelForCausalLM.from_pretrained(model_name_or_path,
                                             device_map="auto",
                                             torch_dtype=torch.float16,
                                              trust_remote_code= True,
                                             revision="main")

tokenizer = AutoTokenizer.from_pretrained(model_id)

question: "what is tract infection?"
# For generating a response
prompt = '''
### Instruction:
{question} 

### Response:'''
input_ids = tokenizer(prompt, return_tensors="pt").input_ids
output = model.generate(inputs=input_ids,max_new_tokens=512,pad_token_id=tokenizer.eos_token_id,top_k=50, do_sample=True,
        top_p=0.95)
response = tokenizer.decode(output[0])

print(response)
```