---
license: apache-2.0
language:
- en
base_model:
- google/gemma-3-12b-it
datasets:
- farbodtavakkoli/OTel-Safety
tags:
- telecom
- telecommunications
- gsma
- rag
- full-parameter-fine-tuning
- fine-tuned
pipeline_tag: text-generation
---

# OTel-LLM-12B-Safety

**OTel-LLM-12B-Safety** is a safety-tuned telecom language model full-parameter fine-tuned on OTel telecommunications data. It is part of the [OTel Family of Models](https://huggingface.co/collections/farbodtavakkoli/otel-llm), an open-source initiative to build reference AI resources for the global telecommunications sector.

The safety variants are auxiliary models trained to refuse when retrieved context is insufficient or off-topic.

## Community Use

As of June 23, 2026, the released OTel models had more than 18 million downloads, and the Open Telco AI project had received 157+ pieces of media coverage worldwide.

## Model Details

| Attribute | Value |
|---|---|
| Base model | [google/gemma-3-12b-it](https://huggingface.co/google/gemma-3-12b-it) |
| Parameters | 12B |
| OTel training dataset | [OTel-Safety](https://huggingface.co/datasets/farbodtavakkoli/OTel-Safety) |
| Dataset fields | `prompt`, `completion`, `abstention`, chunk-count metadata, token-count metadata |
| Training method | Full-parameter post-training / fine-tuning |
| Language | English |
| OTel release license | Apache 2.0 |

## Model Lineage

`google/gemma-3-12b-it` -> `OTel-Safety` full-parameter post-training -> `farbodtavakkoli/OTel-LLM-12B-Safety`

## OTel vs. Base Model

This model is an auxiliary safety-tuned variant trained for abstention behavior and is not part of the 30-model core baseline table. It should be evaluated with abstention-focused metrics for the target deployment, such as correct-abstention rate on insufficient-context examples and answer quality on sufficient-context examples.

## Evaluation Caveats

- This auxiliary safety model is not part of the 30-model core baseline table.
- Abstention quality depends on the retriever, reranker, context window, and prompt policy around the model.
- Evaluate both correct-abstention rate on insufficient-context examples and answer quality on sufficient-context examples before deployment.
- External benchmark transfer, multilingual performance, and per-subdomain performance should be evaluated separately for production settings.


## Training Data

The model was trained on telecom-focused data curated by 100+ domain experts. The raw corpus contained roughly 1.1M training points and was filtered to 326,767 higher-confidence examples.

| Source | Contributor |
|---|---|
| arXiv telecom papers, 3GPP standards, telecom Wikipedia, telecom Common Crawl | Yale University |
| GSMA Permanent Reference Documents, Discover portal | GSMA |
| IETF RFC series | NetoAI |
| Industry whitepapers | Khalifa University |
| O-RAN specifications (working groups 1, 2, 4, 5, 6, 7, 8, 9, 10) | University of Leeds |
| O-RAN documents across working groups | The University of Texas at Dallas |

Released datasets: [OTel-LLM](https://huggingface.co/datasets/farbodtavakkoli/OTel-LLM), [OTel-Embedding](https://huggingface.co/datasets/farbodtavakkoli/OTel-Embedding), [OTel-Reranker](https://huggingface.co/datasets/farbodtavakkoli/OTel-Reranker), and [OTel-Safety](https://huggingface.co/datasets/farbodtavakkoli/OTel-Safety).

The OTel datasets release derived QA/retrieval/reranking examples rather than the raw source documents.

Each released dataset includes a dataset card and Croissant metadata with Responsible AI fields for data limitations, biases, sensitive-information considerations, use cases, social impact, synthetic-data status, and provenance.

## Representative Training Row

`OTel-Safety` is schema-compatible with `OTel-LLM`, but focuses on cases where the retrieved context is insufficient or off-topic and the model should abstain.

```json
{
  "anchor": "How are SCP domains structured and grouped in the SCP trust domain solution?",
  "completion": "I do not have enough information based on the provided context to answer your question.",
  "abstention": true,
  "n_positive_chunks": 0,
  "n_negative_chunks": 5
}
```

## Intended Use

This model is intended for telecom RAG pipelines where the assistant should refuse to answer when retrieved context is missing, irrelevant, or insufficient. It can be used as an abstention-focused generation model or as a reference checkpoint for further safety tuning.

The model should be evaluated in the full target pipeline before deployment, because abstention quality depends on the retriever, reranker, context window, and refusal policy used around the model.

## Training Recipe

| Item | Value |
|---|---|
| Framework | ScalarLM |
| Optimizer | AdamW, 8-bit |
| Learning-rate schedule | Cosine decay with warmup |
| Weight decay | 0.01 |
| Warmup steps | 100 |
| Random seed | 42 |
| Maximum sequence length | 1500 tokens |
| Precision | BF16 |
| Attention | Flash Attention 2 |
| Distributed training | Fully Sharded Data Parallel |
| Gradient checkpointing | Enabled |
| Epochs | 3 for LLM/embedding models; 2 for rerankers |
| Compute | AMD MI300X/MI325X/MI355X and NVIDIA A100/H100 GPUs |

## Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_name = "farbodtavakkoli/OTel-LLM-12B-Safety"
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.bfloat16,
    device_map="auto",
    trust_remote_code=True,
)

prompt = """You are a precise telecom assistant in a RAG pipeline.
Use only the retrieved context to answer.

User Question
What is the purpose of the F1 interface in O-RAN?

Retrieved Contexts
CONTEXT 1
The F1 interface connects the O-RAN Distributed Unit (O-DU) to the O-RAN Central Unit (O-CU).

Answer:"""

inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
outputs = model.generate(**inputs, max_new_tokens=256)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

## Limitations and Responsible Use

- OTel models are domain-specific to telecommunications and should not be treated as general-purpose models.
- The current release is English-only and primarily text-centric.
- The reported OTel performance results use held-out OTel evaluation partitions and should not be interpreted as results from a fully independent external benchmark suite.
- Aggregate scores can hide subdomain variation; collaborator stress tests suggest O-RAN retrieval is comparatively strong, while academic-paper and GSMA PRD examples need further curation.
- Generated telecom content should be verified before operational, customer-facing, regulatory, safety, or network-configuration use.
- Users must comply with both the OTel release license and the upstream base-model license or terms.
- The model may over-abstain or under-abstain depending on retrieval quality and prompt format; tune and measure this behavior before production use.

## Related Models

- [OTel LLM Collection](https://huggingface.co/collections/farbodtavakkoli/otel-llm)
- [OTel Embedding Collection](https://huggingface.co/collections/farbodtavakkoli/otel-embedding)
- [OTel Reranker Collection](https://huggingface.co/collections/farbodtavakkoli/otel-reranker)

## Project Resources

- Project page: https://huggingface.co/farbodtavakkoli
- Code: https://github.com/farbodtavakkoli/OTel
- Media coverage list: https://github.com/farbodtavakkoli/OTel/blob/main/docs/media_coverage.md

## Citation

```bibtex
@misc{otel_models_2026,
  title  = {OTel: Open Telco AI Datasets, Benchmarks, and Models},
  author = {Tavakkoli, Farbod and others},
  year   = {2026},
  note   = {Open Telco (OTel) model release},
  url    = {https://huggingface.co/farbodtavakkoli}
}
```

## Contact

For technical questions, contact farbod.tavakkoli@att.com or farbodtavakoli@gmail.com.
