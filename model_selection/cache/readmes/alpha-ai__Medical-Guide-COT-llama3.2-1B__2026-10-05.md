---
base_model: meta-llama/Llama-3.2-1B-Instruct
tags:
- text-generation-inference
- transformers
- unsloth
- llama
- gguf
- chain-of-thought
license: apache-2.0
language:
- en
---

<div align="center">
<img src="https://cdn-uploads.huggingface.co/production/uploads/669777597cb32718c20d97e9/4emWK_PB-RrifIbrCUjE8.png"
     alt="Title card" 
     style="width: 500px;
            height: auto;
            object-position: center top;">
</div>

**Website - https://www.alphaai.biz**

# Model Name: Medical-Guide-COT-llama3.2-1B

**Developed by:** Alpha AI

**License:** apache-2.0

**Finetuned from model:** meta-llama/Llama-3.2-1B-Instruct

**Formats available:** Float16 (safetensors + GGUF-f16), GGUF quantized (q4\_k\_m, q5\_k\_m, q8\_0)

## Overview

**Medical-Guide-COT-llama3.2-1B** is a lightweight yet powerful medical reasoning model designed to produce explicit **Chain of Thought (CoT)** reasoning with `<think>...</think>` tags for transparency and clarity. Built for interpretability and performance, this model excels in structured medical question answering.

* **Finetuning Objective:** Supervised fine-tuning (SFT) on medical QA datasets with enforced reasoning chains.
* **Instruction format:** Adheres to Llama 3.2 Instruct prompting standards.
* **Deployment flexibility:** Offers multiple GGUF quantized variants for local, edge, or efficient inference environments.

## Training Data

* **Public sources:** PubMedQA, MedMCQA, USMLE-type questions (filtered)
* **Proprietary augmentation:** Alpha AI's curated "Clinical-Cases-CoT" dataset with physician-authored reasoning chains
* **Sample size:** 42,000 examples (approx. 60% public / 40% private)
* **Token structure:**

  ```
  <think>
  Step-by-step clinical reasoning...
  </think>
  Final answer.
  ```

## Model Specifications

| Attribute      | Value                                     |
| -------------- | ----------------------------------------- |
| Base Model     | meta-llama/Llama-3.2-1B-Instruct          |
| Model Type     | Causal Language Model                     |
| Finetuned By   | Alpha AI                                  |
| Precision      | Float16, GGUF q4\_k\_m / q5\_k\_m / q8\_0 |
| Context Length | 8,192 tokens                              |
| Language       | English                                   |

## Intended Use

* **Medical Education:** Transparent QA for students (USMLE/PLAB prep)
* **Prototype Decision Support:** Clear reasoning steps before answers
* **Research on COT Safety:** Evaluation of model interpretability and hallucination control

## Example Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "alpha-ai/Medical-Guide-COT-llama3.2-1B"
model = AutoModelForCausalLM.from_pretrained(model_id, trust_remote_code=True)
tokenizer = AutoTokenizer.from_pretrained(model_id)

prompt = """### Question:
A 65-year-old male presents with sudden chest pain radiating to the back. Most likely diagnosis?
### Answer:
"""
inputs = tokenizer(prompt, return_tensors="pt")
outputs = model.generate(**inputs, max_new_tokens=512, temperature=0.7, top_p=0.9)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

**Expected Output Format:**

```text
<think>
Sudden tearing chest pain suggests aortic dissection.
Hypertension is a key risk factor. Location of pain supports Stanford Type A.
</think>
Acute aortic dissection (Stanford Type A)
```

## Limitations & Usage Warnings

* **Not a clinical diagnostic tool.** Use only for research or educational purposes.
* **Bias & Hallucination Risk.** Outputs must be validated by qualified professionals.
* **Sensitive Content.** Model not trained on PHI but care should be taken with input prompts.

## License

Distributed under the **Apache-2.0** license.

## Acknowledgments

Thanks to Meta AI for Llama-3.2, the creators of open medical QA datasets, and the Alpha AI medical advisory board for domain alignment and data verification.

**Website:** [https://www.alphaai.biz](https://www.alphaai.biz)
