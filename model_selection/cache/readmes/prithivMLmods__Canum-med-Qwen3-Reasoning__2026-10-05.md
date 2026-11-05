---
license: apache-2.0
datasets:
- mteb/raw_medrxiv
language:
- en
- zh
base_model:
- prithivMLmods/Qwen3-1.7B-ft-bf16
pipeline_tag: text-generation
library_name: transformers
tags:
- trl
- text-generation-inference
- medical
- article
- biology
- med
---

![1.png](https://cdn-uploads.huggingface.co/production/uploads/65bb837dbfb878f46c77de4c/FFOM9ye5qFOr6Jpef_yyb.png)

# **Canum-med-Qwen3-Reasoning (Experimental)**

> **Canum-med-Qwen3-Reasoning** is an **experimental medical reasoning and advisory model** fine-tuned on **Qwen/Qwen3-1.7B** using the **MTEB/raw\_medrxiv** dataset.
> It is designed to support **clinical reasoning, biomedical understanding, and structured advisory outputs**, making it a useful tool for researchers, educators, and medical professionals in experimental workflows.

> \[!note]
> GGUF: [https://huggingface.co/prithivMLmods/Canum-med-Qwen3-Reasoning-GGUF](https://huggingface.co/prithivMLmods/Canum-med-Qwen3-Reasoning-GGUF)

---

## **Key Features**

1. **Medical Reasoning Focus**
   Fine-tuned on **MTEB/raw\_medrxiv**, enabling strong performance in **biomedical literature understanding**, diagnostic reasoning, and structured medical advisory tasks.

2. **Clinical Knowledge Extraction**
   Summarizes, interprets, and explains medical research papers, case studies, and treatment comparisons.

3. **Step-by-Step Advisory**
   Provides structured reasoning chains for **symptom analysis, medical explanations, and advisory workflows**.

4. **Evidence-Aware Responses**
   Optimized for scientific precision and evidence-driven output, suitable for **research assistance** and **medical tutoring**.

5. **Structured Output Mastery**
   Capable of producing results in **LaTeX**, **Markdown**, **JSON**, and **tabular formats**, supporting integration into research and healthcare informatics systems.

6. **Optimized for Mid-Scale Deployment**
   Balanced efficiency for **research clusters**, **academic labs**, and **edge deployments in healthcare AI prototypes**.

---

## **Quickstart with Transformers**

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "prithivMLmods/Canum-med-Qwen3-Reasoning"

model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype="auto",
    device_map="auto"
)
tokenizer = AutoTokenizer.from_pretrained(model_name)

prompt = "Summarize the findings of a study on the effectiveness of mRNA vaccines for COVID-19."

messages = [
    {"role": "system", "content": "You are a medical reasoning assistant that explains biomedical studies and provides structured clinical insights."},
    {"role": "user", "content": prompt}
]

text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True
)

model_inputs = tokenizer([text], return_tensors="pt").to(model.device)

generated_ids = model.generate(
    **model_inputs,
    max_new_tokens=512
)
generated_ids = [
    output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
]

response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
print(response)
```

---

## **Intended Use**

* **Medical research summarization** and literature review
* **Diagnostic reasoning assistance** for educational or research purposes
* **Clinical advisory explanations** in structured step-by-step format
* **Biomedical tutoring** for students and researchers
* **Integration into experimental healthcare AI pipelines**

## **Limitations**

* ⚠️ **Not a replacement for medical professionals** – should not be used for direct clinical decision-making
* Training limited to research text corpora – may not capture rare or real-world patient-specific contexts
* Context length limits restrict multi-document medical record analysis
* Optimized for reasoning and structure, not empathetic or conversational dialogue