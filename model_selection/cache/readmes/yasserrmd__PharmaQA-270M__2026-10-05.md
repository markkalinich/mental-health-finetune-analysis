---
base_model: unsloth/gemma-3-270m-it
tags:
- text-generation-inference
- transformers
- unsloth
- gemma3_text
license: apache-2.0
language:
- en
---

### PharmaQA‑270M

<img src="banner.png" width="800"/>

**PharmaQA‑270M** is a compact, instruction-tuned language model for pharmacology and pharmacy domains. Based on **Gemma3 (270M parameters)**, it was fine-tuned using LoRA and merged into a single model checkpoint for easy deployment. This model is optimized for **educational and research use cases**, especially where compute constraints are present.

---

### Model Details

| Property           | Value                                                                                    |
| ------------------ | ---------------------------------------------------------------------------------------- |
| Base Model         | Google Gemma3 (270M parameters)                                                          |
| Fine-tuning Method | LoRA using [Unsloth](https://github.com/unslothai/unsloth)                               |
| Dataset Used       | 25,000 Q\&A pairs from [MIRIAD-4.4M](https://huggingface.co/datasets/miriad/miriad-4.4M) |
| Epochs             | 3                                                                                        |
| Final Format       | Merged (base + LoRA weights)                                                             |
| Model Size         | 270M                                                                                     |
| License            | ODC-BY v1.0 dataset license (non-commercial)                                             |
| Author             | [Mohamed Yasser](https://huggingface.co/yasserrmd)                                       |

---

### ⚠️ Caution & Intended Use

* **Do not use this model for real-world medical diagnosis, treatment, or care decisions.**
* The model was trained on MIRIAD Q\&A pairs generated via LLMs from biomedical literature.
* MIRIAD and this model must be used for **educational, research, and academic exploration only**.
* This model inherits all **OpenAI and ODC-BY v1.0** usage limitations associated with the dataset.

---

### Performance Summary

From evaluation on 50 unseen pharma questions:

| Metric                   | Value                                               |
| ------------------------ | --------------------------------------------------- |
| Average Answer Length    | 40.3 words                                          |
| Longest Answer           | 95 words                                            |
| Shortest Answer          | 12 words                                            |
| Empty / Short Responses  | 0                                                   |
| Clinical Accuracy        | ✅ Consistent terminology                            |
| Depth in Short Responses | ⚠️ Limited                                          |
| Best Use Case            | Lightweight educational deployment (MCQs, tutoring) |

---

### Sample Inference Code

```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

model_name = "yasserrmd/PharmaQA-270M"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto")
model.eval()

question = "What is the mechanism of action of metformin?"
messages = [{"role": "user", "content": f"Q: {question} A:"}]

inputs = tokenizer.apply_chat_template(
    messages,
    add_generation_prompt=True,
    return_tensors="pt",
    tokenize=True,
    return_dict=True
).to(model.device)

if "token_type_ids" in inputs:
    del inputs["token_type_ids"]

with torch.no_grad():
    outputs = model.generate(
        **inputs,
        max_new_tokens=128,
        temperature=0.7,
        top_p=0.95,
        repetition_penalty=1.05
    )

response = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()
answer = response.split("A:")[-1].strip()

print("💊 Question:", question)
print("🧠 Answer:", answer)
```

---

### License

* **Model**: Open for academic and non-commercial use
* **Dataset**: [MIRIAD-4.4M](https://huggingface.co/datasets/miriad/miriad-4.4M) under ODC-BY v1.0

---

### Acknowledgements

* MIRIAD creators for making the dataset openly accessible.
* [Unsloth](https://github.com/unslothai/unsloth) team for enabling fast LoRA tuning on small GPUs.
* Hugging Face and Google for Gemma3 base model.

---



[<img src="https://raw.githubusercontent.com/unslothai/unsloth/main/images/unsloth%20made%20with%20love.png" width="200"/>](https://github.com/unslothai/unsloth)
