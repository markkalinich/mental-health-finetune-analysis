---
language:
- en
license: apache-2.0
library_name: transformers
tags:
- medical
- unsloth
pipeline_tag: text-generation
---

# Model Card for Model ID

<!-- Provide a quick summary of what the model is/does. -->



## Model Details

### Model Description

<!-- Provide a longer summary of what this model is. -->
This model is fined tune based on Google's Gemma model for creating virtual doctor or medical Asistant. It can be used in medical and healthcare AI assitant apps 
and chatbots. 

- **Developed by:** [Ali Bidaran]
-


## Uses

<!-- Address questions around how the model is intended to be used, including the foreseeable users of the model and those affected by the model. -->

```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig, GemmaTokenizer

model_id = "alibidaran/Gemma2_Virtual_doctor"
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16
)


tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, quantization_config=bnb_config, device_map={"":0})

prompt = " Hi doctor, I feel a pain on my ankle, I walk hardly and with pain what do you recommend me?"
text=f"<s> ###Human: {prompt} ###Asistant: "
inputs=tokenizer(text,return_tensors='pt').to('cuda')
with torch.no_grad():
    outputs=model.generate(**inputs,max_new_tokens=200,do_sample=True,top_p=0.92,top_k=10,temperature=0.7)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))

```
## Training Parameters
        per_device_train_batch_size=1,
        gradient_accumulation_steps=8,
        warmup_steps=2,
        #max_steps=200,
       
        num_train_epochs=1,
        learning_rate=2e-4,
        fp16=True,
        logging_steps=100,
        output_dir="outputs",
        optim="paged_adamw_8bit",
        save_steps=500,
        ddp_find_unused_parameters=False // for training on multiple GPU




