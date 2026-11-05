---
language:
- en
---

# Definition

[phi-2] for [P]ersonal [I]dentifiable [I]nformation with [B]anking [B]anking [I]nsurance Dataset

# How to use model

## Load model and tokenizer
```
import torch
from transformers import AutoModelForCausalLM, BitsAndBytesConfig, AutoTokenizer

torch.set_default_device("cuda")

model_name = "dcipheranalytics/phi-2-pii-bbi"

quantization_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_compute_dtype=torch.bfloat16,
        bnb_4bit_quant_type="nf4",
    )

model = AutoModelForCausalLM.from_pretrained(
    model_name,
    device_map="auto",
    # torch_dtype="auto",
    torch_dtype=torch.bfloat16,
    trust_remote_code=True,
    quantization_config=quantization_config,
)

tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
```

## Call generate method
```
def generate(msg: str, max_new_tokens = 300, temperature=0.3):
    chat_template = "<|im_start|>user\n{msg}<|im_end|><|im_start|>assistant\n"
    prompt = chat_template.format(msg=msg)

    with torch.no_grad():
        token_ids = tokenizer.encode(prompt, add_special_tokens=False, return_tensors="pt")
        output_ids = model.generate(
            token_ids.to(model.device),
            max_new_tokens=max_new_tokens,
            do_sample=True,
            temperature=temperature,
            pad_token_id=tokenizer.eos_token_id,
            eos_token_id=tokenizer.eos_token_id,
        )
        output = tokenizer.decode(output_ids[0][token_ids.size(1):-1]).strip()
        return output

instruction_template = "List the personally identifiable information in the given text below.\nText:########\n{text}\n########"
text_with_pii = "My passport number is 123456789."
generate(instruction_template.format(text=text_with_pii))
```


## Batch predictions
```
from transformers import TextGenerationPipeline

def get_prompt(text):
  instruction_template = "List the personally identifiable information in the given text below.\nText:########\n{text}\n########"
  msg = instruction_template.format(text=text)
  chat_template = "<|im_start|>user\n{msg}<|im_end|><|im_start|>assistant\n"
  prompt = chat_template.format(msg=msg)

  return prompt

generator = TextGenerationPipeline(
                     model=model,
                     tokenizer=tokenizer,
                     max_new_tokens=300,
                     do_sample=True,
                     temperature=0.3,
                     pad_token_id=tokenizer.eos_token_id,
                     eos_token_id=tokenizer.eos_token_id,
                     )

texts = ["My passport number is 123456789.",
         "My name is John Smith.",
]
prompts = list(map(get_prompt, texts))
outputs = generator(prompts, 
                  return_full_text=False, 
                  batch_size=2)
```

# Train Data

GPT4 generated customer service conversations. 
1. 100 unique banking topics, 8 examples per each,
2. New 100 banking topics, 4 examples per each,
3. 100 insurance topics, 4 examples per each.

# Evaluation Results

## Average
```
precision    0.836223
recall       0.781132
f1           0.801837
```

## Per topic:
![image/png](https://cdn-uploads.huggingface.co/production/uploads/63ea400bb1d9c4ef71ebb962/wUfwR-dmmyxF4pCYoebCX.png)

## On TAB test split:
```
precision    0.506118
recall       0.350976
f1           0.391614
```