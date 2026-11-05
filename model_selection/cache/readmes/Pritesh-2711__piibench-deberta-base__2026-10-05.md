---
license: other
library_name: transformers
pipeline_tag: token-classification
base_model: microsoft/deberta-v3-base
datasets:
- Pritesh-2711/pii-bench
metrics:
- f1
tags:
- pii-detection
- token-classification
- named-entity-recognition
- deberta
- piibench
---

# PIIBench Direct Fine-Tuned DeBERTa

This is the final selected PIIBench model: a standard DeBERTa-v3-base token
classifier trained directly on the prepared multi-source PII benchmark splits.
It outperformed the source-conditioned hierarchical comparison model on the
complete held-out experiment test split.

## Paper

This model is released with the paper:

**Fine-Tuning Over Architectural Complexity: Broad-Coverage PII Detection on PIIBench with DeBERTa**  
arXiv: https://arxiv.org/abs/2605.25816  
Hugging Face Papers: https://huggingface.co/papers/2605.25816

This repository corresponds to the direct fine-tuned DeBERTa model reported as the final selected model in the paper.

## Results

The reported evaluation uses the later prepared PIIBench experiment variant
with `82` retained entity types and a held-out test split of `100,002` records.
It is not the earlier `48`-type Hub dataset release.

| Held-Out Evaluation | Records | F1 | Precision | Recall |
|---|---:|---:|---:|---:|
| Corrected heldout subset | 5,000 | 0.6476 | 0.6300 | 0.6662 |
| Complete experiment test split | 100,002 | 0.6455 | 0.6277 | 0.6645 |

Full-test SHA-256:
`65f8edc86399ba3f9e4ba44591d4583f9271f5d1df20e30a913305049559df77`

## Usage

This is a standard Transformers token-classification model:

```python
from transformers import pipeline

pipe = pipeline(
    "token-classification",
    model="Pritesh-2711/piibench-deberta-base",
    aggregation_strategy="simple",
)
print(pipe("Contact me at jane@example.com."))
```

## Related Resources

- Dataset: [Pritesh-2711/pii-bench](https://huggingface.co/datasets/Pritesh-2711/pii-bench)
- Source-conditioned hierarchical comparison model: [Pritesh-2711/piibench-deberta-sch](https://huggingface.co/Pritesh-2711/piibench-deberta-sch)
