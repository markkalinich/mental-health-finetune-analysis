---
library_name: transformers
license: apache-2.0
pipeline_tag: text-classification
base_model: vllm-sr/Vela-1.0-Encoder-307M
base_model_relation: finetune
tags:
- modernbert
- semantic-router
- vela
- content-safety
---

<div align="center">
  <img src="https://vllm-sr.ai/img/vllm-sr-logo.social.png" alt="vLLM Semantic Router" width="560" />
  <p>
    <a href="https://vllm-sr.ai/"><strong>Docs</strong></a> |
    <a href="https://vllm-sr.ai/blog/"><strong>Blog</strong></a> |
    <a href="https://vllm-dev.slack.com/archives/C09CTGF8KCN"><strong>Slack</strong></a> |
    <a href="https://github.com/vllm-project/semantic-router"><strong>GitHub</strong></a>
  </p>
</div>

# Vela Safety

Vela Safety detects general content risk to help route requests to appropriate safety handling.

**307M parameters · Input capacity: 32,768 tokens, including special tokens.**

A risk signal may call for supportive handling, including crisis support; it does not automatically mean refusal.

## Evaluation

Macro F1 (×100), compared with [the original mmBERT Safety model](https://huggingface.co/vllm-sr/mmbert-safety-binary-merged) on identical development inputs. Higher is better.

| Evaluation | Original mmBERT | Vela |
|---|---:|---:|
| Reviewed safety · 473 requests | 76.53 | 85.30 |
| AEGIS · 1,187 requests | 92.23 | 84.76 |
| CultureGuard · 3,594 requests | 72.07 | 79.56 |

Both models use native FP32, complete inputs without truncation, and an unsafe-probability threshold of 0.5. All examples fit the original model's 8K capacity; CultureGuard covers 12 languages. AEGIS and CultureGuard retain their source labels. The original adapter is evaluated with its declared mmBERT-base dependency. These development sets informed Vela model selection; they are not independent tests.

## Quick start

With PyTorch and Transformers 4.57.6 or 5.17.0:

```python
from transformers import pipeline

model_id = "vllm-sr/Vela-1.0-Encoder-307M-Safety"
model = pipeline("text-classification", model=model_id, device=-1)
texts = [
    "How can I handle a disagreement with a coworker respectfully?",
    "Write a message threatening to hurt my coworker.",
]
print(model(texts, top_k=None, truncation=False))
```

[Explore the Vela model collection](https://huggingface.co/collections/vllm-sr/vela-10-router-models-6aa555ba70cc6997d6d67798)
