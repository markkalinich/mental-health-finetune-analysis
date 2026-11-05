---
license: mit
language:
- zho
- eng
- fra
- spa
- por
- deu
- ita
- rus
- jpn
- kor
- vie
- tha
- ara
base_model:
- Qwen/Qwen2.5-7B-Instruct
tags:
- medical
---

## Model Details
This model has been LoRA‑fine‑tuned on Qwen2.5‑7B‑Instruct.
In the future, reinforcement learning training may be carried out based on this model, such as DPRO algorithm, etc.


### Base Model Sources [optional]

https://huggingface.co/Qwen/Qwen2.5-7B-Instruct

## How to Get Started with the Model
```python
from transformers import AutoModelForCausalLM, AutoTokenizer
model_name = "ggbaobao/medc_llm_based_on_qwen2.5"
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    device_map="auto",
    torch_dtype=torch.bfloat16 
)
tokenizer = AutoTokenizer.from_pretrained(model_name)
prompt = "猩红热多在发热后多久出现皮疹，请从以下选项中选择：12小时之内, 12～48小时, 60～72小时, 84～96小时, 大于96小时"
messages = [
    {"role": "system", "content": "You are Qwen, You are a helpful assistant."},    
    {"role": "user", "content": prompt},
]
text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True
)
model_inputs = tokenizer([text], return_tensors="pt").to(model.device)

generated_ids = model.generate(
    **model_inputs,
    max_new_tokens=512,
    do_sample=True
)  
generated_ids = [output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)]
response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]

print(response)
```
## Training Details
```python
lora_config = LoraConfig(
    r=16,              
    lora_alpha=32,    
    target_modules=["q_proj", "v_proj"],  
    lora_dropout=0.1 
)

training_args = TrainingArguments(
    output_dir="./results_final1",
    learning_rate=7e-5,
    per_device_train_batch_size=2,
    per_device_eval_batch_size=2,
    gradient_accumulation_steps=1,  # 梯度累积
    num_train_epochs=2,
    evaluation_strategy="steps",
    # evaluate_steps=1,
    save_strategy="steps",
    save_steps=10,
    logging_steps=10,
    logging_dir="./logs1",
    bf16=True,  # 混合精度训练
```
### Training Data

The training data comes from https://github.com/SupritYoung/Zhongjing
If you want to know more details about the above github project, you can also read their paper: 
Zhongjing: Enhancing the Chinese Medical Capabilities of Large Language Model through Expert Feedback and Real-world Multi-turn Dialogue

The data includes about one-seventh of the multi-round medical consultation data and six-sevenths of the single medical consultation data.

#### Hardware
vGPU-32GB * 6

#### Software
use peft and deepspeed
