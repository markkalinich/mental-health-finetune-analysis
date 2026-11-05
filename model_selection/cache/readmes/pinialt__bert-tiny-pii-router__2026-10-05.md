---
language: en
license: apache-2.0
base_model: google/bert_uncased_L-4_H-256_A-4
tags:
- pii
- privacy
- routing
- text-classification
- knowledge-distillation
- tinybert
- traffic-control
datasets:
- ai4privacy/pii-masking-65k
metrics:
- f1
library_name: transformers
pipeline_tag: text-classification
model-index:
- name: bert-tiny-pii-router
  results:
  - task:
      type: text-classification
      name: PII Routing
    dataset:
      name: ai4privacy/pii-masking-65k
      type: ai4privacy/pii-masking-65k
    metrics:
    - name: F1
      type: f1
      value: 0.96
---

# bert-tiny-pii-router: The Semantic Gatekeeper

> *In the era of massive LLMs, sometimes the smartest solution is the smallest one.*

This is a **42MB Traffic Controller** designed for high-performance NLP pipelines. Instead of blindly running heavy extraction models (NER, Regex, Address Parsers) on every user query, this model acts as a "Gatekeeper" to predict *which* entities are present before extraction begins.

It was distilled from an **XLM-RoBERTa** teacher into a **TinyBERT** student, achieving a **9.1x speedup** while retaining 96% of the teacher's accuracy.

## The Problem: The "Blind Pipeline"
Traditional PII extraction pipelines are wasteful. They run every specialist model on every input:
* **Regex** is fast but generates false positives (e.g., confusing dates `12/05/2024` for IP addresses).
* **NER** models are accurate but heavy and slow.
* **LLMs** are perfect extractors but expensive, high-latency, and overkill for simple tasks.

## The Solution: The Router Pattern
Instead of a linear pipeline, we use a **Multi-Label Classifier** at the very front. It reads the text once and outputs a probability vector indicating which specialized engines are needed.

**Example Decision:**
```json
Input: "Schedule a meeting with John in London on Friday"
Output: {
  "NER": 0.99,      // -> Trigger Name Extractor
  "ADDRESS": 0.98,  // -> Trigger Geocoder
  "TEMPORAL": 0.95, // -> Trigger Date Parser
  "REGEX": 0.01     // -> Skip Regex Engine (Save Compute)
}

```

## Tag Purification: Solving Class Overlap

A major challenge in training this router was **Class Overlap**. Standard models struggle with ambiguous definitions.

> **The Ambiguity:**
> * **Is a Date a Regex?** A date like `12/05/2024` fits a regex pattern. But semantically, it belongs to the **TEMPORAL** engine, not the REGEX scanner.
> * **Is a State a Name?** "California" is technically a Named Entity (NER). But for routing purposes, it must be sent to the Geocoder (**ADDRESS**), not the Person/Org extractor.
> 
> 

To fix this, the training data underwent a **Tag Purification** layer. We mapped 38 granular tags into 4 distinct "Routing Engines" to enforce strict semantic boundaries:

| Source Tag | Action | Destination Engine (Label) |
| --- | --- | --- |
| **DATE / TIME** | **Removed** from Regex | `TEMPORAL` |
| **CITY / STATE / ZIP** | **Removed** from NER | `ADDRESS` |
| **IP / EMAIL / IBAN** | **Kept** in Regex | `REGEX` |
| **PERSON / ORG** | **Kept** in NER | `NER` |

## Student vs. Teacher (Distillation Results)

The model was trained using **Knowledge Distillation**. The student (`TinyBERT`) was forced to mimic the "soft targets" (thought process) of the teacher (`XLM-RoBERTa`), not just the final labels.

**Hardware:** Apple M4 Max
**Speedup:** 9.1x

| Model | Parameters | Size | Throughput | F1 Retention |
| --- | --- | --- | --- | --- |
| **Teacher** (XLM-R) | 278M | ~1 GB | ~360 samples/sec | 100% (Baseline) |
| **Student** (TinyBERT) | **11M** | **42 MB** | **~3,300 samples/sec** | **96%** |

## Evaluation Results

The model shows strong separation between the routing categories, with minimal confusion between semantically distinct classes (e.g., Address vs. Regex).

![Confusion Matrix](confusion_matrix.png)

## Usage

This model outputs **Multi-Label Probabilities** for the 4 engines. We recommend a threshold of **0.5** to trigger a route.

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model_name = "pinialt/bert-tiny-pii-router"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

def route_query(text, threshold=0.5):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=128)
    
    with torch.no_grad():
        logits = model(**inputs).logits
    
    # Sigmoid for multi-label (independent probabilities)
    probs = torch.sigmoid(logits)[0]
    
    # Map IDs to Labels
    active_routes = [
        model.config.id2label[i] 
        for i, score in enumerate(probs) 
        if score > threshold
    ]
    
    if not active_routes:
        return "⚡ Direct to LLM (No PII)"
        
    return f"🚦 Route to Engines: {', '.join(active_routes)}"

# === EXAMPLES ===
# 1. Complex Multi-Entity Request
print(route_query("Schedule a meeting with John in London on Friday"))
# Output: 🚦 Route to Engines: NER, ADDRESS, TEMPORAL

# 2. Pure Address
print(route_query("Ship to 123 Main St, New York, NY"))
# Output: 🚦 Route to Engines: ADDRESS

```

## Training & Distillation Details

* **Teacher Model:** `xlm-roberta-base`
* **Student Model:** `google/bert_uncased_L-4_H-256_A-4`
* **Dataset:** `ai4privacy/pii-masking-65k` (Filtered & Purified)
* **Loss Function:** 


## License

This project is licensed under the **Apache License 2.0**.
Finetuned on Google's bert_uncased_L-4_H-256_A-4 model
```
@article{turc2019,
  title={Well-Read Students Learn Better: On the Importance of Pre-training Compact Models},
  author={Turc, Iulia and Chang, Ming-Wei and Lee, Kenton and Toutanova, Kristina},
  journal={arXiv preprint arXiv:1908.08962v2 },
  year={2019}
}
```


## Links

* **Dataset:** [ai4privacy/pii-masking-65k](https://huggingface.co/datasets/ai4privacy/pii-masking-65k)
* **Training Code:** [pinialt/pii-router](https://www.google.com/search?q=https://github.com/pinialt/pii-router)