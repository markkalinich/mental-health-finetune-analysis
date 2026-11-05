---
tags:
  - mteb
  - sentence-transformers
  - transformers
  - embedding
  - bidirectional
  - multilingual
pipeline_tag: sentence-similarity
license: apache-2.0
base_model: BidirLM/BidirLM-1.7B-Base
language:
  - multilingual
  - af
  - am
  - ar
  - az
  - be
  - bg
  - bn
  - bs
  - ca
  - ceb
  - cs
  - cy
  - da
  - de
  - el
  - en
  - es
  - et
  - eu
  - fa
  - fi
  - fr
  - ga
  - gl
  - gu
  - ha
  - he
  - hi
  - hr
  - ht
  - hu
  - hy
  - id
  - ig
  - is
  - it
  - ja
  - jv
  - ka
  - kk
  - kn
  - ko
  - ky
  - lt
  - lv
  - mg
  - mk
  - ml
  - mr
  - ms
  - mt
  - my
  - nb
  - ne
  - nl
  - nso
  - ny
  - pa
  - pl
  - ps
  - pt
  - ro
  - ru
  - sd
  - si
  - sk
  - sl
  - sn
  - so
  - sq
  - sr
  - su
  - sv
  - sw
  - ta
  - te
  - th
  - tl
  - tr
  - uk
  - ur
  - vi
  - wo
  - xh
  - yo
  - zh
  - zu
---

# BidirLM-1.7B

BidirLM is a family of 5 frontier bidirectional encoders, including an omnimodal variant at 2.5B, adapted from causal decoder LLMs. Contrary to contrastive-only models, BidirLM relies on a prior masking phase (MNTP) that enables state-of-the-art results on task-specific fine-tuning (NER, classification, NLI) while achieving frontier performance on embedding benchmarks (MTEB) against open-source alternatives.

![Multilingual model performance by size on XTREME-Benchmark Augmented and MTEB Multilingual V2](final_results.png)

> *From the paper. MTEB(Multilingual, v2) below matches the paper; the LongEmbed table reports additional long-context results.*

| Model | Base LLM | Parameters | Embedding Dim | Max Tokens | MTEB Multi. V2 (Mean Task) |
|---|---|---|---|---|---|
| BidirLM-270M | Gemma3-270M | 268M | 640 | 512 | 56.3 |
| BidirLM-0.6B | Qwen3-0.6B | 596M | 1024 | 512 | 60.0 |
| BidirLM-1B | Gemma3-1B | 1001M | 1152 | 512 | 62.7 |
| **BidirLM-1.7B** | **Qwen3-1.7B** | **1721M** | **2048** | **512** (\*) | **63.1** |
| BidirLM-Omni-2.5B | Qwen3-1.7B | 2.5B | 2048 | 512 | 63.1 |

(\*) Evaluated at `max_seq_length=512`, matching the paper. The architecture supports much longer context (see the LongEmbed table below); on the MTEB leaderboard the shared LEMBPasskeyRetrieval task is scored at long context, making the leaderboard MTEB(Multilingual, v2) ~0.4 higher than this table.

## LongEmbed (Long-Context Retrieval)

Mean nDCG@10 over the 6 [LongEmbed](https://huggingface.co/datasets/dwzhu/LongEmbed) retrieval tasks. Each model is reported at the context length (8k or 32k) that maximizes its average; the architecture supports the base model's full context.

| Model | LongEmbed (Mean nDCG@10) | Eval Context |
|---|---|---|
| BidirLM-270M | 71.8 | 32k |
| BidirLM-0.6B | 71.9 | 8k |
| BidirLM-1B | 76.4 | 32k |
| **BidirLM-1.7B** | **73.4** | **8k** |

> **Note:** Extending the evaluation context from 8k to 32k helped the Gemma-based models (270M, 1B) but not the Qwen-based models (0.6B, 1.7B), which scored best at 8k.

## Supported Tasks

**General embeddings** (via Sentence Transformers): retrieval, semantic similarity (STS), clustering, classification, pair classification, reranking, bitext mining, multilabel classification

**Downstream fine-tuning** (via Transformers): sequence classification (e.g. MNLI, XNLI, PAWS-X, MathShepherd), token classification (e.g. PAN-X, POS), information retrieval (e.g. MIRACL, CodeSearchNet), sequence regression (e.g. Seahorse)

## Usage

### Sentence Transformers

Use Sentence Transformers to compute embeddings for any text representation task.

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("BidirLM/BidirLM-1.7B-Embedding", trust_remote_code=True)

queries = [
    "What is the capital of France?",
    "How does photosynthesis work?",
]
documents = [
    "Paris is the capital and largest city of France, situated on the river Seine.",
    "Photosynthesis is the process by which plants convert sunlight, water, and CO2 into glucose and oxygen.",
]

query_embeddings = model.encode(queries)
document_embeddings = model.encode(documents)

similarities = model.similarity(query_embeddings, document_embeddings)
print(similarities)
```

### Fine-tuning for Downstream Tasks

BidirLM can be directly fine-tuned for downstream tasks:

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification, AutoModelForTokenClassification

tokenizer = AutoTokenizer.from_pretrained("BidirLM/BidirLM-1.7B-Embedding", trust_remote_code=True)

# Sequence classification (e.g., NLI: entailment, neutral, contradiction)
seq_model = AutoModelForSequenceClassification.from_pretrained(
    "BidirLM/BidirLM-1.7B-Embedding",
    trust_remote_code=True,
    num_labels=3,
)

# Token classification (e.g., NER)
tok_model = AutoModelForTokenClassification.from_pretrained(
    "BidirLM/BidirLM-1.7B-Embedding",
    trust_remote_code=True,
    num_labels=7,
)

# Fine-tune with HuggingFace Trainer
```

## Evaluation

Please follow the [mteb repository](https://github.com/embeddings-benchmark/mteb) on how to reproduce our scores. The evaluation prompts used for each task are also available at [mteb_v2_eval_prompts.json](mteb_v2_eval_prompts.json).

## Supported Languages

Multilingual support across over 119 languages, inherited from the Qwen3 base model and reinforced through contrastive training with 87 languages.

## Requirements

This model requires `trust_remote_code=True` as it uses a custom bidirectional architecture.

```
transformers>=5.0
sentence-transformers>=5.0.0
```

> **Note:** This model was trained with `transformers==4.57.6` (transformers 4.x). The version on `main` was patched to work with `transformers>=5.0`. For the original (pre-patch) version, which is compatible with `transformers>=4.57.6,<5.0.0`, use the `transformers-v4` branch:
> ```python
> from sentence_transformers import SentenceTransformer
> model = SentenceTransformer(
>     "BidirLM/BidirLM-1.7B-Embedding",
>     trust_remote_code=True,
>     revision="transformers-v4",
> )
> ```

## FAQ

### 1. What pooling strategy does this model use?

The model uses **mean pooling**. This is handled automatically when using Sentence Transformers.

### 2. Do I need `trust_remote_code=True`?

Yes. BidirLM uses a custom bidirectional architecture (`BidirLMModel`) that requires loading custom code from the repository.

### 3. Why are my reproduced results slightly different from those reported in the model card?

Different versions of `transformers` and `pytorch` could cause negligible but non-zero performance differences. This model should be used with `transformers>=5.0` (evaluated with `transformers==5.5.4` and `pytorch==2.6.0`).

### 4. What is the relationship between BidirLM-1.7B and BidirLM-1.7B-Base?

[BidirLM/BidirLM-1.7B-Base](https://huggingface.co/BidirLM/BidirLM-1.7B-Base) is the intermediate MNTP-adapted checkpoint (bidirectional pretraining stage). BidirLM-1.7B is the final contrastive fine-tuned version optimized for both sentence embeddings and downstream fine-tuning.

### 5. How is BidirLM different from other embedding models?

Most embedding models (BGE-M3, KaLM, EmbedGemma, Qwen3-Embedding) use contrastive-only training, which optimizes embeddings but sacrifices fine-tuning ability. BidirLM restores a prior MNTP phase, advancing the Pareto frontier on both MTEB and XTREME simultaneously.

## Citation

```bibtex
@misc{boizard2026bidirlmtextomnimodalbidirectional,
      title={BidirLM: From Text to Omnimodal Bidirectional Encoders by Adapting and Composing Causal LLMs}, 
      author={Nicolas Boizard and Théo Deschamps-Berger and Hippolyte Gisserot-Boukhlef and Céline Hudelot and Pierre Colombo},
      year={2026},
      eprint={2604.02045},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2604.02045}, 
}
```
