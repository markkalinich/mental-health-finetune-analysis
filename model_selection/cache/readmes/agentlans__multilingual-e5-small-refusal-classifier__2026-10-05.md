---
license: mit
base_model:
- agentlans/multilingual-e5-small-aligned-v2
language:
- en
- zh
- fr
- pt
- es
- ja
- tr
- ru
- ar
- ko
- th
- it
- de
- vi
- ms
- id
- fil
- hi
- pl
- cs
- nl
- km
- my
- fa
- gu
- ur
- te
- mr
- he
- bn
- ta
- uk
- bo
- kk
- mn
- ug
- yue
datasets:
- agentlans/refusal-classifier-data
pipeline_tag: text-classification
tags:
  - text-classification
  - multilingual
  - refusal-detection
  - alignment
  - conversation-analysis
  - fine-tuned-model
  - ethics
  - ai-safety
  - e5
  - transformer
  - huggingface
  - research
---

# Multilingual Refusal Classifier

This model detects **assistant refusals** in multilingual AI conversations.
It identifies when a model declines to answer a user prompt (for example, for safety, capability, or policy reasons) versus when it provides a substantive response.

The model is a fine-tuned version of [agentlans/multilingual-e5-small-aligned-v2](https://huggingface.co/agentlans/multilingual-e5-small-aligned-v2), 
trained on the [agentlans/refusal-classifier-data](https://huggingface.co/datasets/agentlans/refusal-classifier-data) dataset.

**Evaluation results:**
- **Loss:** 0.2665  
- **Accuracy:** 0.9153  
- **Training tokens:** 5,347,200  

## Usage

This classifier accepts input in conversation-like text formats using structured role tokens.  
For long texts, insert `<|...|>` as an ellipsis placeholder in the middle of omitted content.

**Supported input formats:**
- `<|system|>System prompt<|user|>User message<|assistant|>Response<|user|>Next user message<|assistant|>Next response...`
- `<|user|>User message<|assistant|>Response<|user|>Next user message<|assistant|>Next response...`

**Example:**

```python
from transformers import pipeline

classifier = pipeline(
    task="text-classification",
    model="agentlans/multilingual-e5-small-refusal-classifier"
)

text = (
    "<|user|>Mr. Loyd wants to fence his square-shaped land of 150 sqft each side. "
    "If a pole is laid every certain distance, he needs 30 poles. "
    "What is the distance between each pole in feet?"
    "<|assistant|>If Mr. Loyd's land is square-shaped and each side is 150 sqft, then<|...|>"
    "ce between poles ≈ 20.69 sqft\n\nTherefore, the distance between each pole is approximately 20.69 feet."
)

print(classifier(text))
# [{'label': 'Non-refusal', 'score': 0.9906}]
```

## Evaluation Results

The classifier was tested on ten examples translated from the [NousResearch/Minos-v1](https://huggingface.co/NousResearch/Minos-v1) model page.
Full examples are available in [Examples.md](Examples.md).

- 🚫 — The model predicted a **refusal to answer**.  
- ◯ — The model predicted a **valid response**.

| Example | English | French | Spanish | Chinese | Russian | Arabic |
|----------|:--------:|:-------:|:---------:|:---------:|:----------:|:--------:|
| 1        | 🚫 | 🚫 | 🚫 | 🚫 | 🚫 | 🚫 |
| 2        | 🚫 | 🚫 | 🚫 | 🚫 | 🚫 | 🚫 |
| 3        | 🚫 | 🚫 | 🚫 | 🚫 | 🚫 | 🚫 |
| 4        | 🚫 | 🚫 | 🚫 | 🚫 | 🚫 | 🚫 |
| 5        | 🚫 | 🚫 | 🚫 | 🚫 | 🚫 | 🚫 |
| 6        | ◯ | ◯ | ◯ | ◯ | ◯ | ◯ |
| 7        | ◯ | ◯ | ◯ | ◯ | ◯ | ◯ |
| 8        | ◯ | ◯ | ◯ | ◯ | ◯ | ◯ |
| 9        | ◯ | 🚫 | ◯ | ◯ | 🚫 | 🚫 |
| 10       | ◯ | ◯ | ◯ | ◯ | ◯ | ◯ |

The classifier performs consistently across major languages, though some false positives remain, especially in contexts with ambiguous phrasing.

## Limitations

- **Input length:** 512-token maximum  
- **False positives/negatives:** Occasionally similar to the Minos classifier  
- **Low-resource languages:** May yield inconsistent predictions  
- **Cultural variation:** Expressions of refusal differ linguistically, which can affect accuracy  

## Training Details

### Hyperparameters
- **Learning rate:** 5e-5  
- **Train batch size:** 8  
- **Eval batch size:** 8  
- **Seed:** 42  
- **Optimizer:** `ADAMW_TORCH_FUSED` (`betas=(0.9, 0.999)`, `epsilon=1e-8`)  
- **Scheduler:** Linear  
- **Epochs:** 5  

### Framework Versions
- Transformers 5.0.0.dev0  
- PyTorch 2.9.1+cu128  
- Datasets 4.4.1  
- Tokenizers 0.22.1  

## Intended Use

This model is designed for:
- Identifying **AI refusals** during conversation analysis.  
- Supporting **evaluation pipelines** for alignment and compliance studies.  
- Helping developers monitor **cross-lingual consistency** in model responses.  

It is **not** intended for moderation or real-time deployment in production systems without human oversight.
