---
license: apache-2.0
language:
  - ar
  - en
tags:
  - medical
  - arabic
  - healthcare
  - qwen
  - lora-merged
---

# Qwen2.5-1.5B-Medical (Merged)

نموذج دردشة طبي أولي باللغة العربية مبني على **Qwen/Qwen2.5-1.5B-Instruct** بعد دمج LoRA fine-tuned على بيانات أعراض وأمراض طبية.

### الاستخدام الأساسي

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_name = "Mahmoud7Dev/qwen2.5-1.5b-medical-merged"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float16,
    device_map="auto"
)

messages = [
    {"role": "system", "content": "أنت مساعد طبي أولي. رد بالعربية فقط. لا تعطِ علاجًا ولا تشخيصًا نهائيًا."},
    {"role": "user", "content": "الأعراض: صداع شديد، غثيان، حساسية للضوء"}
]

text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
inputs = tokenizer([text], return_tensors="pt").to(model.device)

outputs = model.generate(**inputs, max_new_tokens=300, temperature=0.7)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))