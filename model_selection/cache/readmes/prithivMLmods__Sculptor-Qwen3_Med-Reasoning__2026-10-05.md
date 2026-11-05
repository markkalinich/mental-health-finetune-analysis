---
license: apache-2.0
datasets:
- FreedomIntelligence/medical-o1-reasoning-SFT
- UCSC-VLAA/MedReason
base_model:
- Qwen/Qwen3-1.7B
language:
- en
pipeline_tag: text-generation
library_name: transformers
tags:
- text-generation-inference
- moe
- medical
- biology
- trl
---

![Add a heading.png](https://cdn-uploads.huggingface.co/production/uploads/65bb837dbfb878f46c77de4c/wq6VfaFU623sx351YhRdQ.png)

# Sculptor-Qwen3\_Med-Reasoning

> **Sculptor-Qwen3\_Med-Reasoning** is a fine-tuned variant of the **Qwen3-4B** architecture, trained specifically on the **Med Reason Dataset** to maximize **accurate medical and clinical reasoning**. This model excels at structured diagnostic logic, symptom analysis, and treatment planning, while maintaining lightweight performance, making it ideal for healthcare, medical education, and clinical support applications.

> [!note]
[!GGUF] : https://huggingface.co/prithivMLmods/Sculptor-Qwen3_Med-Reasoning-Q4_K_M-GGUF
 
## Key Features

1. **Precision Medical Reasoning with Med Reason Dataset**
   Tailored for clinical reasoning, medical question answering, and evidence-based analysis, powered by the specialized Med Reason fine-tuning.

2. **Lightweight Clinical Code Understanding**
   Capable of interpreting and generating medical-related code (e.g., for health data analysis in Python or R), optimized for concise, logic-oriented scripts.

3. **Structured Output Formatting**
   Produces well-organized responses in Markdown, JSON, LaTeX, and tabular formats suitable for electronic health records, research documentation, and structured reporting.

4. **Instruction-Following Accuracy**
   Tuned for consistent multi-step instruction adherence in clinical cases and decision-making workflows, enhancing reliability for educational and medical use.

5. **Multilingual Medical Capabilities**
   Supports clinical reasoning and documentation in over 20 languages, enabling accessibility for global healthcare professionals.

6. **Efficient 4B Architecture**
   Based on Qwen3-4B, offering a balanced tradeoff between inference speed and domain-specific accuracy—suitable for deployment on mid-tier GPUs or cloud-based systems.

## Quickstart with Transformers

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "prithivMLmods/Sculptor-Qwen3_Med-Reasoning"

model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype="auto",
    device_map="auto"
)
tokenizer = AutoTokenizer.from_pretrained(model_name)

prompt = "A 45-year-old male presents with chest pain and shortness of breath. List possible diagnoses and explain the reasoning."

messages = [
    {"role": "system", "content": "You are a clinical reasoning assistant trained on the Med Reason Dataset."},
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

## Intended Use

* Clinical reasoning and diagnosis support
* Medical question answering and tutoring
* Structured documentation and case analysis
* JSON/Markdown/tabular medical summaries
* Education tools for healthcare professionals
* Multilingual medical documentation and Q\&A

## Limitations

* Not designed for open-domain creative generation
* Limited context length compared to larger LLMs
* Sensitive to ambiguous or poorly formatted inputs
* May produce errors in complex or adversarial medical prompts

## References

1. [Qwen2.5 Technical Report](https://arxiv.org/pdf/2412.15115)
2. [YaRN: Context Window Extension for LLMs](https://arxiv.org/pdf/2309.00071) 