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

# PIIBench Source-Conditioned Hierarchical DeBERTa

This is the source-conditioned hierarchical comparison model trained for the
follow-up PIIBench experiments. It uses a DeBERTa-v3-base encoder, a coarse
entity classification head, and a fine BIO classification head conditioned on
the coarse distribution.

The simpler directly fine-tuned model was the final overall winner on the full
held-out experiment test split and is published separately as
[`Pritesh-2711/piibench-deberta-base`](https://huggingface.co/Pritesh-2711/piibench-deberta-base).

## Paper

This model is released with the paper:

**Fine-Tuning Over Architectural Complexity: Broad-Coverage PII Detection on PIIBench with DeBERTa**  
arXiv: https://arxiv.org/abs/2605.25816  
Hugging Face Papers: https://huggingface.co/papers/2605.25816

This repository corresponds to the source-conditioned hierarchical DeBERTa comparison model evaluated in the paper.

## Results

The reported evaluation uses the later prepared PIIBench experiment variant
with `82` retained entity types and a held-out test split of `100,002` records.
It is not the earlier `48`-type Hub dataset release.

| Held-Out Evaluation | Records | F1 | Precision | Recall |
|---|---:|---:|---:|---:|
| Corrected heldout subset | 5,000 | 0.5899 | 0.5565 | 0.6274 |
| Complete experiment test split | 100,002 | 0.5894 | 0.5560 | 0.6270 |

Full-test SHA-256:
`65f8edc86399ba3f9e4ba44591d4583f9271f5d1df20e30a913305049559df77`

## Usage

This model includes custom architecture code. Load it with
`trust_remote_code=True`.

It was trained with a prepended source token. For arbitrary input where the
source dataset is unknown, use the general source token:

```python
from transformers import AutoModelForTokenClassification, AutoTokenizer, pipeline

model_id = "Pritesh-2711/piibench-deberta-sch"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForTokenClassification.from_pretrained(
    model_id,
    trust_remote_code=True,
)

pipe = pipeline("token-classification", model=model, tokenizer=tokenizer)
result = pipe("[SRC=general] Contact me at jane@example.com.")
print(result)
```

Transformers may print an informational warning that custom model classes are
not in its built-in token-classification support list. The model is loaded
correctly when its class is `HierarchicalPIIModel`; the warning does not mean
that a standard DeBERTa classifier head has been substituted.

When evaluating known PIIBench source records, use their associated source
token, for example `[SRC=nvidia_nemotron]` or `[SRC=gretel_finance]`.

## Important Note

Calling:

```python
pipeline("token-classification", model="Pritesh-2711/piibench-deberta-sch")
```

without `trust_remote_code=True` does not instantiate the hierarchical head and
must not be used to reproduce the reported results.

## Related Resources

- Dataset: [Pritesh-2711/pii-bench](https://huggingface.co/datasets/Pritesh-2711/pii-bench)
- Direct fine-tuned final model: [Pritesh-2711/piibench-deberta-base](https://huggingface.co/Pritesh-2711/piibench-deberta-base)
