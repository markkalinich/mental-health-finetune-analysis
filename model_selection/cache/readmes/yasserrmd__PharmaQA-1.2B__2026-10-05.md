---
base_model:
- unsloth/LFM2-1.2B
- LiquidAI/LFM2-1.2B
tags:
- text-generation-inference
- transformers
- unsloth
- lfm2
license: apache-2.0
language:
- en
---


### PharmaQA-1.2B 

<img src="banner.png" width="800" />

**PharmaQA‑1.2B** is a merged, instruction-tuned pharmacology and pharmacy domain language model based on **Liquid AI LFM2-1.2B**. It was fine-tuned using the [MIRIAD-4.4M](https://huggingface.co/datasets/miriad/miriad-4.4M) dataset for research and educational Q\&A in pharmacology, therapeutics, and drug mechanisms. This model is **not intended for clinical or diagnostic use**.

---

### 🧪 Model Details

| Property           | Value                                                                                         |
| ------------------ | --------------------------------------------------------------------------------------------- |
| Base Model         | Liquid AI `LFM2-1.2B`                                                                         |
| Fine-tuning Method | LoRA using [Unsloth](https://github.com/unslothai/unsloth)                                    |
| Parameters Trained | \~9M (0.78% of total)                                                                         |
| Dataset Used       | [MIRIAD-4.4M](https://huggingface.co/datasets/miriad/miriad-4.4M) (subset of 50,000 examples) |
| Epochs             | 1                                                                                             |
| Final Format       | **Merged** (LoRA + base)                                                                      |
| Model Size         | 1.2 Billion                                                                                   |
| License            | **ODC-BY v1.0** dataset license, non-commercial educational use only                          |
| Author             | [Mohamed Yasser](https://huggingface.co/yasserrmd)                                            |

---

### ⚠️ Disclaimer

This model is **not intended for medical diagnosis, treatment planning, or patient care**.
It was trained on synthetic Q\&A pairs from peer-reviewed literature via MIRIAD and is for **educational and academic research only**.

MIRIAD includes a **cautionary note** that aligns with OpenAI’s usage policies:

> *Do not use this dataset or models trained on it for actual medical diagnosis, decision-making, or any application involving real-world patients.*

---

### Example Usage

```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, TextStreamer

model_name = "yasserrmd/PharmaQA-1.2B"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto")
model.eval()

# Example pharmacy-related question
question = "What is the mechanism of action of metformin?"

# Format as chat message
messages = [{"role": "user", "content": f"Q: {question} A:"}]

# Tokenize with chat template
inputs = tokenizer.apply_chat_template(
    messages,
    add_generation_prompt=True,
    return_tensors="pt",
    tokenize=True,
    return_dict=True,
).to(model.device)

# Clean input if necessary
if "token_type_ids" in inputs:
    del inputs["token_type_ids"]

# Generate the answer
with torch.no_grad():
    output_ids = model.generate(
        **inputs,
        max_new_tokens=128,
        temperature=0.3,
        min_p=0.15,
        repetition_penalty=1.05
    )

# Decode the response
response = tokenizer.decode(output_ids[0], skip_special_tokens=True).strip()
answer = response.split("A:")[-1].strip()

print("💊 Question:", question)
print("🧠 Answer:", answer)
```

---

### Performance Insights

From manual analysis of 50 unseen pharmacology questions:

* ✅ No hallucinations observed
* ✅ High alignment with biomedical terms (e.g., *dihydrofolate reductase*, *QT prolongation*)
* ✅ Long-form answers are clinically descriptive and accurate for education
* ⚠️ Short answers are concise but can lack therapeutic context

---

### License

* Model: Educational and research use only
* Dataset: [MIRIAD](https://huggingface.co/datasets/miriad/miriad-4.4M) (ODC-BY v1.0)

---

### Acknowledgements

* MIRIAD Team (for the dataset)
* [Unsloth](https://github.com/unslothai/unsloth) team (for fast & efficient LoRA)
* Hugging Face + Liquid AI for open model access

---

Let me know if you'd like a Markdown file for this (`README.md`) or want help preparing the Hugging Face push commands.


[<img src="https://raw.githubusercontent.com/unslothai/unsloth/main/images/unsloth%20made%20with%20love.png" width="200"/>](https://github.com/unslothai/unsloth)