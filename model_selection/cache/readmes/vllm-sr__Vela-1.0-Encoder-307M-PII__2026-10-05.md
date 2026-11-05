---
library_name: transformers
license: apache-2.0
pipeline_tag: token-classification
base_model: vllm-sr/Vela-1.0-Encoder-307M
base_model_relation: finetune
language:
- en
- zh
- es
- fr
- de
- ja
tags:
- modernbert
- semantic-router
- vela
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

# Vela PII

Vela PII finds sensitive entity spans for privacy-aware routing and redaction.

**307M parameters · Input capacity: 32,768 tokens, including special tokens.**

Outputs use 35 BIO labels across 17 entity types. The example returns spans with Unicode character offsets.

## Evaluation

Exact-span micro F1 (×100) on the same synthetic development sets, compared with [the original mmBERT32K PII model](https://huggingface.co/vllm-sr/mmbert32k-pii-detector-merged). Higher is better.

| Evaluation | Original mmBERT | Vela |
|---|---:|---:|
| Short inputs · 888 | 23.66 | **90.76** |
| Controlled 4K context · 30 | 0.44 | **89.03** |
| Controlled 8K context · 30 | 0.28 | **89.88** |
| Controlled 16K context · 30 | 0.36 | **89.73** |
| Controlled 32K context · 30 | 0.23 | **89.24** |

Synthetic examples cover six languages. Long inputs include sparse entities, densely packed repeated entities and negative examples; micro F1 weights each entity equally. Both models process complete inputs in FP32 with the same exact-span scorer. These development sets informed Vela selection; they are not an independent natural-document benchmark.

## Quick start

With PyTorch and Transformers 4.57.6 or 5.17.0:

```python
from transformers import pipeline

model_id = "vllm-sr/Vela-1.0-Encoder-307M-PII"
model = pipeline("token-classification", model=model_id, aggregation_strategy="simple", device=-1)
text = "Contact Mara Wells at mara.wells@example.com."
assert len(model.tokenizer.encode(text)) <= model.model.config.max_position_embeddings
print(model(text))
```

[Explore the Vela model collection](https://huggingface.co/collections/vllm-sr/vela-10-router-models-6aa555ba70cc6997d6d67798)
