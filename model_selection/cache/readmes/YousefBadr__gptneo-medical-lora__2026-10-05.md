---
library_name: transformers
tags:
- medical
- question-answering
- text-generation
- causal-lm
- lora
datasets:
- medalpaca/medical_meadow_medical_flashcards
language:
- en
metrics:
- perplexity
base_model:
- EleutherAI/gpt-neo-125M
pipeline_tag: text-generation
license: apache-2.0
---

# GPT-Neo Medical LoRA Fine-Tuned Model

## Model Overview

This model is a medical-domain fine-tuned version of **EleutherAI/gpt-neo-125M**, trained using **LoRA (Low-Rank Adaptation)** on the **Medical Meadow Medical Flashcards dataset**.

The model generates accurate, structured medical responses given a medical instruction and question.

Fine-tuning significantly improved performance compared to the base GPT-Neo model, reducing perplexity by **97.95%**.

This model was trained using parameter-efficient fine-tuning, allowing efficient adaptation with minimal computational cost.

Model link:  
https://huggingface.co/YousefBadr/gptneo-medical-lora

---

## Model Details

### Model Description

This is a causal language model fine-tuned for medical question answering using LoRA.

Expected prompt format:

```
Instruction: Answer this question truthfully
Question: <medical question>
Response:
```

The model generates structured medical explanations.

### Developed by

Yousef Badr

### Model Type

Causal Language Model (GPT-Neo architecture) fine-tuned using LoRA

### Language

English

### Base Model

EleutherAI/gpt-neo-125M  
https://huggingface.co/EleutherAI/gpt-neo-125M

### Fine-Tuning Method

Low-Rank Adaptation (LoRA)

LoRA enables efficient fine-tuning by training less than 1% of the total model parameters.

---

## Intended Uses

### Direct Use

- Medical question answering
- Medical knowledge generation
- Medical education tools
- AI research in domain adaptation

Example:

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

model = AutoModelForCausalLM.from_pretrained("YousefBadr/gptneo-medical-lora")
tokenizer = AutoTokenizer.from_pretrained("YousefBadr/gptneo-medical-lora")

prompt = """Instruction: Answer this question truthfully
Question: What causes diabetes?
Response:"""

inputs = tokenizer(prompt, return_tensors="pt")

outputs = model.generate(
    **inputs,
    max_length=200,
    temperature=0.7,
    top_p=0.9
)

print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

---

### Downstream Applications

- Medical chatbots
- Healthcare AI assistants
- Educational tools
- Domain-specific LLM research

---

### Out-of-Scope Use

This model is NOT intended for:

- Clinical diagnosis
- Medical decision-making
- Professional healthcare use

Always consult licensed medical professionals.

---

## Training Details

### Dataset

Medical Meadow Medical Flashcards  
https://huggingface.co/datasets/medalpaca/medical_meadow_medical_flashcards

Dataset size: ~34,000 samples

Format:

```
Instruction: Answer this question truthfully
Question: <medical question>
Response: <medical answer>
```

Split:

- Train: 90%
- Validation: 10%

---

### Training Method

- Base model frozen
- LoRA adapters trained
- LoRA weights merged into base model

This approach reduces training cost while maintaining high performance.

---

### Training Hyperparameters

| Parameter | Value |
|---------|------|
Base Model | GPT-Neo-125M |
LoRA Rank | 16 |
LoRA Alpha | 32 |
LoRA Dropout | 0.1 |
Batch Size | 8 |
Learning Rate | 2e-4 |
Optimizer | AdamW |
Precision | FP16 |
GPU | NVIDIA Tesla T4 |
Platform | Google Colab |

---

## Evaluation

### Metric

Perplexity was used as the primary evaluation metric.

Lower perplexity indicates better performance.

---

### Quantitative Results

Evaluation performed on validation dataset.

| Model | Loss | Perplexity |
|------|------|------------|
| Base GPT-Neo | 4.7494 | 115.51 |
| GPT-Neo + LoRA | 0.8638 | 2.37 |

Improvement:

Perplexity reduction: **97.95%**

This demonstrates significant improvement in medical language modeling performance.

---

### Qualitative Results

The fine-tuned model produces:

- More accurate medical explanations
- Improved terminology usage
- Better structured responses
- Reduced generic answers

Detailed comparison available in:

generation_comparison.csv

---

### Evaluation Files

Available files:

- model_performance_comparison.csv
- generation_comparison.csv

These files contain full quantitative and qualitative comparisons.

---

## Example

Input:

```
Instruction: Answer this question truthfully
Question: What causes asthma?
Response:
```

Output:

Asthma is a chronic inflammatory disease of the airways characterized by bronchial hyperresponsiveness, airflow obstruction, and inflammation.

---

## Architecture

GPT-Neo Transformer

- Layers: 12
- Hidden size: 768
- Attention heads: 12
- Parameters: 125M
- Objective: Causal Language Modeling

---

## Compute Infrastructure

Hardware:

- NVIDIA Tesla T4 GPU

Software:

- Transformers
- PEFT
- PyTorch
- Hugging Face Datasets

---

## Limitations

- May generate incorrect medical information
- Not suitable for clinical use
- Limited by dataset coverage

---

## Environmental Impact

Parameter-efficient LoRA significantly reduces compute cost compared to full fine-tuning.

Training performed on single GPU using Google Colab.

---

## Citation

```
Yousef Badr. GPT-Neo Medical LoRA Fine-Tuned Model. 2026.
```

---

## Author

Yousef Badr  
Machine Learning Engineer  

Hugging Face: https://huggingface.co/YousefBadr

---

## Acknowledgment

Special thanks to **Eng. Mahmoud Khorshid** for guidance and support.