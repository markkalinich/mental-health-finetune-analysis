---
tags:
- llama-3-8b
- sft
- medical
language:
- en
- ar
base_model:
- meta-llama/Meta-Llama-3-8B
license: cc-by-nc-nd-4.0
datasets:
- lighteval/med_mcqa
- qiaojin/PubMedQA
- bigbio/med_qa
---

# MedLLaMA-3


This model is developed by Basel Anaya.


## 💻 Usage

```python
!pip install -qU transformers accelerate

from transformers import AutoTokenizer
import transformers
import torch

model = "Reverb/MedLLaMA-3"
messages = [{"role": "user", "content": "What is a large language model?"}]

tokenizer = AutoTokenizer.from_pretrained(model)
prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
pipeline = transformers.pipeline(
    "text-generation",
    model=model,
    torch_dtype=torch.float16,
    device_map="auto",
)

outputs = pipeline(prompt, max_new_tokens=256, do_sample=True, temperature=0.7, top_k=50, top_p=0.95)
print(outputs[0]["generated_text"])
```
## 🏆 Evaluation

|             Tasks             |Version|Filter|n-shot| Metric |Value |   |Stderr|
|-------------------------------|-------|------|-----:|--------|-----:|---|-----:|
|stem                           |N/A    |none  |     0|acc     |0.6466|±  |0.0056|
|                               |       |none  |     0|acc_norm|0.6124|±  |0.0066|
| - medmcqa                     |Yaml   |none  |     0|acc     |0.6118|±  |0.0075|
|                               |       |none  |     0|acc_norm|0.6118|±  |0.0075|
| - medqa_4options              |Yaml   |none  |     0|acc     |0.6143|±  |0.0136|
|                               |       |none  |     0|acc_norm|0.6143|±  |0.0136|
| - anatomy (mmlu)              |      0|none  |     0|acc     |0.7185|±  |0.0389|
| - clinical_knowledge (mmlu)   |      0|none  |     0|acc     |0.7811|±  |0.0254|
| - college_biology (mmlu)      |      0|none  |     0|acc     |0.8264|±  |0.0317|
| - college_medicine (mmlu)     |      0|none  |     0|acc     |0.7110|±  |0.0346|
| - medical_genetics (mmlu)     |      0|none  |     0|acc     |0.8300|±  |0.0378|
| - professional_medicine (mmlu)|      0|none  |     0|acc     |0.7868|±  |0.0249|
| - pubmedqa                    |      1|none  |     0|acc     |0.7420|±  |0.0196|

|Groups|Version|Filter|n-shot| Metric |Value |   |Stderr|
|------|-------|------|-----:|--------|-----:|---|-----:|
|stem  |N/A    |none  |     0|acc     |0.6466|±  |0.0056|
|      |       |none  |     0|acc_norm|0.6124|±  |0.0066|