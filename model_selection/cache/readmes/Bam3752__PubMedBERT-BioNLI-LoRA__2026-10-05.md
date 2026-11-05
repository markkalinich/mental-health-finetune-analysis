---
language: 
- en
tags:
- nli
- biomedical
- pubmed
- lora
- entailment
datasets:
- bioasq
- mednli
metrics:
- type: accuracy
  value: 0.9039
- type: f1
  value: 0.9036
- type: loss
  value: 0.2673
model-index:
- name: PubMedBERT BioNLI LoRA
  results:
  - task:
      type: natural-language-inference
      name: Natural Language Inference
    dataset:
      name: BioASQ + MedNLI
      type: bioasq-mednli
    metrics:
    - type: accuracy
      value: 0.9039
    - type: f1
      value: 0.9036
    - type: loss
      value: 0.2673
---

# PubMedBERT BioNLI LoRA

[![Model](https://img.shields.io/badge/Model-LoRA-green)](https://huggingface.co/Bam3752/PubMedBERT-BioNLI-LoRA)
[![Hugging Face](https://img.shields.io/badge/HF-Bam3752-blue)](https://huggingface.co/Bam3752)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**PubMedBERT BioNLI LoRA** is a biomedical **Natural Language Inference (NLI)** model fine-tuned with **LoRA adapters**.  
It classifies **entailment, contradiction, and neutrality** between biomedical text pairs, optimized for **chain-of-thought reasoning validation**.

---

## 📊 Training Details

- **Base model:** [pritamdeka/PubMedBERT-MNLI-MedNLI](https://huggingface.co/pritamdeka/PubMedBERT-MNLI-MedNLI)  
- **Fine-tuning datasets:** BioASQ + MedNLI  
- **Objective:** 3-class NLI (entailment / neutral / contradiction)  
- **Method:** LoRA parameter-efficient fine-tuning  
- **Hardware:** Apple MPS (Metal backend)  
- **Hyperparameters:**  
  - Epochs: 4  
  - Learning rate: 1e-5  
  - Batch size: 8  
  - Max length: 256  
  - Gradient accumulation: 2  
  - Warmup ratio: 0.1  
  - Label smoothing: 0.05  

---

## 📈 Results

| Metric      | Value   |
|-------------|---------|
| Accuracy    | **90.39%** |
| Macro F1    | **0.9036** |
| Eval Loss   | **0.2673** |

👉 Calibrated with isotonic regression (`calibration/isotonic.pkl`) for reliable probabilities.

---

## 🚀 Usage

### Transformers

```python
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("Bam3752/PubMedBERT-BioNLI-LoRA")
tokenizer = AutoTokenizer.from_pretrained("Bam3752/PubMedBERT-BioNLI-LoRA")

premise = "Aspirin reduces the risk of myocardial infarction."
hypothesis = "Aspirin prevents heart attacks."

inputs = tokenizer(premise, hypothesis, return_tensors="pt")
outputs = model(**inputs)

probs = outputs.logits.softmax(-1).detach().cpu().numpy()
print(probs)  # [neutral, contradiction, entailment]
