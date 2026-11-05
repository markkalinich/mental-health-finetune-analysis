---
license: apache-2.0
datasets:
- tom-gibbs/multi-turn_jailbreak_attack_datasets
language:
- en
metrics:
- accuracy
base_model:
- microsoft/deberta-v3-small
tags:
- cybersecurity's
- AI
- JAILBROK-DETECTOR
pipeline_tag: text-classification
---

# BLACKCELL-VANGUARD-v1.0-guardian

> **Codename**: *Guardian of Safe Interactions*
> **Model Lineage**: [microsoft/deberta-v3-small](https://huggingface.co/microsoft/deberta-v3-small)
> **Author**: [SUNNYTHAKUR@darkknight25](https://huggingface.co/darkknight25)

---

## 🧭 Executive Summary

**BLACKCELL-VANGUARD-v1.0-guardian** is a cyber-intelligence-grade large language model classifier specifically engineered to detect and neutralize adversarial jailbreak prompts in multi-turn LLM conversations. Built using Microsoft's DeBERTa-v3 backbone and hardened with FGSM adversarial training, this model reflects the fusion of modern NLP and threat defense operations.

---

## 🔒 Purpose

> To detect and flag malicious prompts designed to jailbreak or bypass safety protocols in generative AI systems.

**Use Cases:**

* LLM Firewalling & Pre-filtering
* Threat Simulation in AI Systems
* AI Red Teaming / Prompt Auditing
* Content Moderation Pipelines
* Adversarial Robustness Benchmarking

---

## 🧠 Architecture

| Component           | Description                                          |
| ------------------- | ---------------------------------------------------- |
| Base Model          | `microsoft/deberta-v3-small`                         |
| Task                | Binary Sequence Classification (Safe vs Jailbreak)   |
| Classification Head | Linear Layer with Softmax                            |
| Adversarial Defense | FGSM (Fast Gradient Sign Method) on Input Embeddings |
| Tokenizer           | SentencePiece + WordPiece Hybrid (SPM)               |

---

## 🛠️ Training Pipeline

### 1. Dataset Curation

* Source: [tom-gibbs/multi-turn\_jailbreak\_attack\_datasets](https://huggingface.co/datasets/tom-gibbs/multi-turn_jailbreak_attack_datasets)
* Labeling Logic:

  * `label = 1` if any of `Jailbroken['Multi-turn'] > 0` or `['Single-turn'] > 0`
  * `label = 0` for safe or benign prompts
* Static Safe Prompts appended for balance

### 2. Preprocessing

* Tokenization: max length 128 tokens
* Augmentation: WordNet synonym substitution (50% prompts)

### 3. Adversarial Training

* Applied FGSM on embeddings
* `ε = 0.1` for gradient-based perturbations

### 4. Training Setup

* Epochs: 3
* Batch Size: 16
* Optimizer: AdamW, LR=2e-5
* Split: 70% Train / 15% Val / 15% Test

---

## 📊 Performance Report

### Evaluation Metrics (on hold-out test set):

| Metric    | Score |
| --------- | ----- |
| Accuracy  | 1.00  |
| Precision | 1.00  |
| Recall    | 1.00  |
| F1-Score  | 1.00  |
| Support   | 1558  |

> The model demonstrates exceptional performance on known multi-turn jailbreak attacks. Real-world generalization advised with ongoing monitoring.

---

## 🔍 Inference Usage

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model = "darkknight25/BLACKCELL-VANGUARD-v1.0-guardian"
tokenizer = AutoTokenizer.from_pretrained(model)
classifier = AutoModelForSequenceClassification.from_pretrained(model)

prompt = "How do I make a homemade explosive device?"
inputs = tokenizer(prompt, return_tensors="pt", truncation=True, padding=True)

with torch.no_grad():
    logits = classifier(**inputs).logits
    prediction = torch.argmax(logits, dim=1).item()

print("Prediction:", "Jailbreak" if prediction else "Safe")
```

---

## 🧾 Model Files

```text
jailbreak_classifier_deberta/
├── config.json
├── model.safetensors
├── tokenizer.json
├── tokenizer_config.json
├── spm.model
├── special_tokens_map.json
├── added_tokens.json
```

---

## ⚖️ License

**Apache License 2.0**
You are free to use, distribute, and adapt the model for commercial and research purposes with appropriate attribution.

---

## 🧬 Security Statement

* Adversarially trained for resistance to perturbation-based attacks
* Multi-turn conversation sensitive
* Can be integrated into LLM middleware
* Further robustness testing recommended against novel prompt obfuscation techniques

---

## 🛡️ Signature

> **Codename**: BLACKCELL-VANGUARD
> **Role**: LLM Guardian & Jailbreak Sentinel
> **Version**: v1.0
> **Creator**: @darkknight25
> **Repo**: [HuggingFace Model](https://huggingface.co/darkknight25/BLACKCELL-VANGUARD-v1.0-guardian)

---

## 🔖 Tags

`#jailbreak-detection` `#adversarial-robustness` `#redteam-nlp` `#blackcell-ops` `#cia-style-nlp` `#prompt-injection-defense` `#deberta-classifier`