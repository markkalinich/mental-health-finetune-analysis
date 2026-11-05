---
tags:
- llama-3-8b
- sft
- medical
base_model:
- meta-llama/Meta-Llama-3-8B
license: cc-by-nc-nd-4.0
---

# JSL-MedLlama-3-8B-v1.0
[<img src="https://repository-images.githubusercontent.com/104670986/2e728700-ace4-11ea-9cfc-f3e060b25ddf">](http://www.johnsnowlabs.com)


This model is developed by [John Snow Labs](https://www.johnsnowlabs.com/).

This model is available under a [CC-BY-NC-ND](https://creativecommons.org/licenses/by-nc-nd/4.0/deed.en) license and must also conform to this [Acceptable Use Policy](https://huggingface.co/johnsnowlabs). If you need to license  this model for commercial use, please contact us at info@johnsnowlabs.com.



## 💻 Usage

```python
!pip install -qU transformers accelerate

from transformers import AutoTokenizer
import transformers
import torch

model = "johnsnowlabs/JSL-MedLlama-3-8B-v1.0"
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
|stem                           |N/A    |none  |     0|acc     |0.6217|±  |0.0057|
|                               |       |none  |     0|acc_norm|0.5847|±  |0.0066|
| - medmcqa                     |Yaml   |none  |     0|acc     |0.5563|±  |0.0077|
|                               |       |none  |     0|acc_norm|0.5563|±  |0.0077|
| - medqa_4options              |Yaml   |none  |     0|acc     |0.6779|±  |0.0131|
|                               |       |none  |     0|acc_norm|0.6779|±  |0.0131|
| - anatomy (mmlu)              |      0|none  |     0|acc     |0.6963|±  |0.0397|
| - clinical_knowledge (mmlu)   |      0|none  |     0|acc     |0.7509|±  |0.0266|
| - college_biology (mmlu)      |      0|none  |     0|acc     |0.7986|±  |0.0335|
| - college_medicine (mmlu)     |      0|none  |     0|acc     |0.6590|±  |0.0361|
| - medical_genetics (mmlu)     |      0|none  |     0|acc     |0.8500|±  |0.0359|
| - professional_medicine (mmlu)|      0|none  |     0|acc     |0.7868|±  |0.0249|
| - pubmedqa                    |      1|none  |     0|acc     |0.7380|±  |0.0197|

|Groups|Version|Filter|n-shot| Metric |Value |   |Stderr|
|------|-------|------|-----:|--------|-----:|---|-----:|
|stem  |N/A    |none  |     0|acc     |0.6217|±  |0.0057|
|      |       |none  |     0|acc_norm|0.5847|±  |0.0066|