
---
license: apache-2.0
---

# 🧠 MedGEMMA Summarizer Model – CXR Clinical Reasoning → Impression

This model is a fine-tuned version of `google/medgemma-4b-it` trained to **summarise step-by-step radiological reasoning into concise radiology impressions**.

---

## 🩺 Use Case

Given a structured or natural language clinical reasoning (e.g., output from a vision-language reasoning model), this summarizer produces a **final radiological impression** suitable for downstream clinical applications.

---

## 📚 Training Data

This model was fine-tuned on 10k step-wise annotated samples from the [`Manusinhh/cxr-10k-reasoning-dataset`](https://huggingface.co/datasets/Manusinhh/cxr-10k-reasoning-dataset), derived from the MIMIC-CXR dataset.

Each sample includes:
- `reasoning`: Step-wise explanation of radiological features
- `impression`: Final concise report summary

---

## 🔍 Inference Example

```python
messages = [
    {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": f"Summarise the following clinical reasoning into a concise radiology impression:\n\n{reasoning_text}"
            }
        ]
    }
]

formatted_text = processor.apply_chat_template(
    messages, tokenize=False, add_generation_prompt=True
)

inputs = processor.tokenizer(formatted_text, return_tensors="pt").to(model.device)

with torch.no_grad():
    outputs = model.generate(**inputs, max_new_tokens=100)

generated_tokens = outputs[0][inputs["input_ids"].shape[1]:]
summary_output = processor.tokenizer.decode(generated_tokens, skip_special_tokens=True)
````

---


## 📘 Citation

Please cite the original MIMIC-CXR dataset authors:

> Johnson AE, Pollard TJ, Berkowitz SJ, et al. *MIMIC-CXR: A de-identified publicly available database of chest radiographs with free-text reports.* Scientific Data. 2019;6:317. [https://doi.org/10.1038/s41597-019-0322-0](https://doi.org/10.1038/s41597-019-0322-0)

```
