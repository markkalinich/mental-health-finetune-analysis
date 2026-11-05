---
license: apache-2.0
library_name: sentence-transformers
pipeline_tag: sentence-similarity
language:
- es
base_model:
- BSC-LT/MrBERT-es
tags:
- biomedical
- spanish
- bi-encoder
- sentence-transformers
- embeddings
- retrieval
---

# ALIA MrBERT Spanish Biomedical Embeddings Model

This repository contains **ALIA MrBERT Spanish Biomedical Embeddings**, a Spanish biomedical domain bi-encoder model for semantic similarity and information retrieval tasks. It is built upon [MrBERT-es](https://huggingface.co/BSC-LT/MrBERT-es), a bilingual (Spanish-English) foundational language model based on the ModernBERT architecture, and fine-tuned on domain-specific biomedical data using a Curriculum Learning strategy.

> [!WARNING]
> **DISCLAIMER:** This model is a domain-specific proof-of-concept designed to demonstrate retrieval capabilities in the Spanish biomedical domain.
> While optimized for this domain, results should be verified against official clinical sources and expert judgment. The model may fail in out-of-domain or adversarial inputs.

---

## Model Details

### Model Lineage

```
ModernBERT (architecture)
       ↓
  MrBERT-es (BSC-LT)
  Bilingual ES/EN encoder
  150M parameters
       ↓
  ALIA-MrBERT-es-biomedical-embeddings (SINAI)
  Biomedical domain fine-tuning
  Curriculum Learning + Hard Negatives
```

### Key Features

- 🔍 **Domain**: Spanish biomedical and healthcare texts
- 📐 **Architecture**: ModernBERT with Mean Pooling (bi-encoder)
- 📏 **Long context**: up to 8,192 tokens
- 🎓 **Training strategy**: Curriculum Learning (easy → medium → hard)
- ⚙️ **Negative mining**: Positive-Aware Hard Negative Mining (NVIDIA approach)

### Architecture

This model uses the same base architecture as [MrBERT-es](https://huggingface.co/BSC-LT/MrBERT-es), extended with a Mean Pooling layer for sentence-level embeddings:

|                              |               |
|------------------------------|:--------------|
| **Base Architecture**        | ModernBERT    |
| **Total Parameters**         | ~150M         |
| **Hidden size**              | 768           |
| **Intermediate size**        | 1,152         |
| **Attention heads**          | 12            |
| **Hidden layers**            | 22            |
| **Context length**           | 8,192 tokens  |
| **Vocabulary size**          | 51,200        |
| **Precision**                | bfloat16      |
| **Positional encoding**      | RoPE          |
| **Activation function**      | GeLU          |
| **Attention type**           | Mixed (global every 3 layers + sliding window) |
| **Pooling strategy**         | Mean Pooling  |

---

## Training

### Training Strategy: Curriculum Learning

The model was fine-tuned using a two-phase **Curriculum Learning** strategy and progressively increasing the difficulty of training examples thanks to [SINAI/ALIA-es-biomedical-triplets/train](https://huggingface.co/datasets/SINAI/ALIA-es-biomedical-triplets/viewer/hard-negatives/train):

| Phase | Epochs | Negative Type | Difficulty Progression |
|-------|:------:|:-------------:|:----------------------:|
| **Phase 1** | 8 | Random negatives | Easy → Medium → Hard |
| **Phase 2** | 4 | Hard negatives (mined) | Easy → Medium → Hard |
| **Total** | **12** | — | — |

**Phase 1 - Contrastive Learning with Random Negatives:**
Training uses triplets `{query, relevant_doc, [irrelevant_docs]}` with in-batch negatives. Examples are sorted by difficulty across 4 sub-phases (2 epochs each).

**Phase 2 - Advanced Refinement with Hard Negatives:**
Refinement using mined hard negatives with **Positive-Aware Mining** (NVIDIA approach) to avoid false negatives. A candidate is only considered a negative if:
```
score < score_positive - margin   (margin = 0.05)
```

### Hyperparameter Optimization

Before training, hyperparameter search was conducted using **[Optuna](https://optuna.org/)**  (20 trials, subsets of 5,000 examples):
- **Sampler**: TPESampler (Tree-structured Parzen Estimator)
- **Pruner**: MedianPruner
- **Storage**: SQLite for trial persistence

| Hyperparameter | Search Space |
|----------------|:------------:|
| Learning Rate | [1×10⁻⁶, 5×10⁻⁵] (log-uniform) |
| Warmup Ratio | [0.05, 0.2] |
| Weight Decay | [0.0, 0.1] |
| Mini Batch Size | {1, 4, 8, 12} |

### Final Training Hyperparameters

| Hyperparameter | Value | Description |
|----------------|:-----:|:------------|
| **Learning Rate** | 5×10⁻⁵ | Nominal learning rate |
| **Batch Size** | 128 | Global batch size |
| **Cache Mini-Batch** | 4 | For CachedMultipleNegativesRankingLoss |
| **Warmup Ratio** | 0.1595 | Linear LR warmup at start of each phase |
| **Weight Decay** | 0.02143 | L2 regularization |
| **Optimizer** | AdamW | Standard HuggingFace Trainer optimizer |
| **Precision** | bf16 | Bfloat16 for Ampere+ architectures |
| **Max Sequence Length** | 8,192 | Maximum tokens processed |

### Loss Function

- **CachedMultipleNegativesRankingLoss**: Enables training with large batches without VRAM overflow, by recalculating embeddings in smaller sub-batches (cache size: 4).

### Training Framework

| Component | Details |
|-----------|---------|
| **Library** | `sentence-transformers` |
| **Distributed** | DDP (Distributed Data Parallel) via `torchrun` |
| **Memory optimization** | Gradient Checkpointing |
| **Logging** | WandB (offline mode) |

---

## Intended Use

### Direct Use

This model is designed for semantic similarity and information retrieval tasks in the **Spanish biomedical domain**. Primary use cases include:
- **Semantic search**: Finding relevant biomedical documents from a query
- **RAG pipelines**: Retrieving biomedical context for grounded question answering
- **Biomedical document clustering**: Grouping similar biomedical texts by semantic content
- **Duplicate detection**: Identifying semantically similar biomedical passages

### Out-of-Scope Use

- General-domain retrieval (model is specialized for biomedical Spanish)
- Cross-lingual retrieval beyond Spanish
- Use as a generative model (this is an encoder-only model)
- Clinical decision support without human expert validation

---

## How to Use

### With `sentence-transformers`

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("SINAI/ALIA-MrBERT-es-biomedical-embeddings")

queries = ["¿Cuáles son los síntomas principales de la insuficiencia cardíaca?"]
documents = [
    "La insuficiencia cardíaca puede causar disnea, fatiga y edema periférico...",
    "El tratamiento inicial incluye control de la presión arterial y ajuste farmacológico...",
]

query_embeddings = model.encode(queries, prompt_name="query")
doc_embeddings = model.encode(documents)

scores = model.similarity(query_embeddings, doc_embeddings)
print(scores)
```

### With `transformers` (manual)

```python
import torch
from transformers import AutoTokenizer, AutoModel

model_name = "SINAI/ALIA-MrBERT-es-biomedical-embeddings"
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
model = AutoModel.from_pretrained(model_name, trust_remote_code=True)

def mean_pooling(model_output, attention_mask):
    token_embeddings = model_output[0]
    input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
    return torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(input_mask_expanded.sum(1), min=1e-9)

texts = ["¿Qué recomendaciones existen para el manejo de la hipertensión arterial?"]
encoded = tokenizer(texts, padding=True, truncation=True, return_tensors="pt")

with torch.no_grad():
    outputs = model(**encoded)

embeddings = mean_pooling(outputs, encoded["attention_mask"])
print(embeddings.shape)  # (1, 768)
```

---

## Evaluation

The model was evaluated using the [MTEB](https://huggingface.co/mteb) (Massive Text Embedding Benchmark) framework, adapted for the legal domain. The main reported metric is **NDCG@10** (Normalized Discounted Cumulative Gain at k=10), which is the standard metric used in retrieval leaderboards and aligns with the metric reported in the MrBERT family.

An additional evaluation was made thanks to [ragas](https://github.com/vibrantlabsai/ragas) evaluation framework and [MiniMaxAI/MiniMax-M2.5](https://huggingface.co/MiniMaxAI/MiniMax-M2.5) language model. These metrics are calculated by averaging on each pair puntuation from particular subsets of some of the following datasets.

### Evaluation Datasets

| Dataset | Category | Description |
|---------|----------|-------------|
| **QA** | Retrieval | Spanish subset of the MIRACL dataset in MTEB format ([jinaai/miracl-es](https://huggingface.co/datasets/jinaai/miracl-es)) |
| **STS** | STS | Combination of three Spanish STS datasets: PAWS-X ([google-research-datasets/paws-x](https://huggingface.co/datasets/google-research-datasets/paws-x)), STS22 ([mteb/sts22-crosslingual-sts](https://huggingface.co/datasets/mteb/sts22-crosslingual-sts)), and SemRel2024 ([SemRel/SemRel2024](https://huggingface.co/datasets/SemRel/SemRel2024)) |
| **CoWeSe** | Retrieval | Generated open-ended questions from the [CoWeSe](https://arxiv.org/abs/2109.07765) corpus ([chrisnb1/cowese-qa-dataset](https://huggingface.co/datasets/chrisnb1/cowese-qa-dataset)) |
| **AbSanitas** | Retrieval | Spanish biomedical information retrieval dataset built from biomedical texts collected from official academic repositories and open-access sources ([BSC-LT/AbSanitas](https://huggingface.co/datasets/BSC-LT/AbSanitas)) |
| **pairs1.5k** | Retrieval | Subset of 1.5K biomedical evaluation pairs (query + passage) located in [SINAI/ALIA-es-biomedical-triplets/test](https://huggingface.co/datasets/SINAI/ALIA-es-biomedical-triplets/viewer/evaluation/test). |
| **pairs3645** | Retrieval | Subset of 3,645 biomedical evaluation pairs (query + passage) located in [SINAI/ALIA-es-biomedical-triplets/test](https://huggingface.co/datasets/SINAI/ALIA-es-biomedical-triplets/viewer/evaluation/test). |

### Results (NDCG@10)

| Model | QA | STS | CoWeSe | AbSanitas | pairs1.5k | pairs3645 |
|-------|:------------:|:-------------:|:--------:|:--------:|:------------:|:-------------:|
| [BAAI/bge-m3](https://huggingface.co/BAAI/bge-m3) | 0.9839 | 0.4629 | 0.7974 | 0.7613 | 0.9775 | 0.9840 |
| [Qwen/Qwen3-Embedding-0.6B](https://huggingface.co/Qwen/Qwen3-Embedding-0.6B) | **0.9869**| **0.5033** | **0.8807** | **0.8165** | **0.9921** | 0.9962 |
| [sentence-transformers/paraphrase-multilingual-mpnet-base-v2](https://huggingface.co/sentence-transformers/paraphrase-multilingual-mpnet-base-v2) | 0.9419 | 0.4632 | 0.7262 | 0.4870 | 0.7871 | 0.8212 |
| **ALIA-MrBERT-es-biomedical-embeddings (ours)** | 0.9666 | 0.4932 | 0.8551 | 0.8124 | 0.9877 | **0.9966** |

[BAAI/bge-m3](https://huggingface.co/BAAI/bge-m3) and [Qwen/Qwen3-Embedding-0.6B](https://huggingface.co/Qwen/Qwen3-Embedding-0.6B) are SOTA models with a size x4 larger than ours. Yet, our model shows comparable results.

### Results (ragas)

#### Subset: `triplets_queries1724_contexts3645 (pairs3645)`

| Model | [Context Precision](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/context_precision/#context-precision_1) (avg) | [Context Utilization](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/context_precision/#context-utilization) (avg) | [Context Relevance](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/nvidia_metrics/#context-relevance) (avg) |
| :--- | :---: | :---: | :---: |
| [Qwen/Qwen3-Embedding-0.6B](https://huggingface.co/Qwen/Qwen3-Embedding-0.6B) | 0.9577 | 0.9582 | 0.9098 |
| **ALIA-MrBERT-es-biomedical-embeddings (ours)** | **0.9588** | **0.9589** | **0.9102** |

#### Subset: `cowese_queries661_contexts551`

| Model | [Context Relevance](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/nvidia_metrics/#context-relevance) (avg) |
| :--- | :---: |
| [**Qwen/Qwen3-Embedding-0.6B**](https://huggingface.co/Qwen/Qwen3-Embedding-0.6B) | **0.4231** |
| ALIA-MrBERT-es-biomedical-embeddings (ours) | 0.3932 |

#### Subset: `absanitas_queries800_contexts25192`

| Model | [Context Relevance](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/nvidia_metrics/#context-relevance) (avg) |
| :--- | :---: |
| [**Qwen/Qwen3-Embedding-0.6B**](https://huggingface.co/Qwen/Qwen3-Embedding-0.6B) | **0.9228** |
| ALIA-MrBERT-es-biomedical-embeddings (ours) | 0.9156 |

> **Note:** Each evaluation subset is named following the pattern `{dataset}_queries{N}_contexts{M}`, where `N` is the number of queries evaluated against `M` contexts taken from the datasets.

---

## Limitations and Biases

### Known Limitations

- **Domain specificity**: The model is optimized for Spanish biomedical texts. Performance may degrade on general-domain or other specialized texts.
- **Language**: Although MrBERT-es supports Spanish and English, this fine-tuned model focuses on Spanish biomedical content.
- **Clinical accuracy**: Semantic similarity does not guarantee medical correctness. Retrieved documents should be verified by qualified healthcare professionals.
- **Context length**: Despite supporting up to 8,192 tokens, very long documents may still require chunking strategies for optimal retrieval performance.

### Biases

- The model may reflect biases present in the biomedical corpora used for training.
- It may underperform on subdomains underrepresented in the source data.

---

## Additional Information

### License
[Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0)

### Citation

If you use this model in your research, please cite:

```bibtex
@misc{ALIA-MrBERT-es-biomedical-embeddings,
  title        = {ALIA MrBERT Spanish Biomedical Embeddings Model},
  author       = {SINAI Research Group, Universidad de Jaén},
  year         = {2026},
  publisher    = {HuggingFace},
  howpublished = {\url{https://huggingface.co/SINAI/ALIA-MrBERT-es-biomedical-embeddings}}
}
```

Please also cite the base model:

```bibtex
@misc{tamayo2026mrbertmodernmultilingualencoders,
      title={MrBERT: Modern Multilingual Encoders via Vocabulary, Domain, and Dimensional Adaptation}, 
      author={Daniel Tamayo and Iñaki Lacunza and Paula Rivera-Hidalgo and Severino Da Dalt and Javier Aula-Blasco and Aitor Gonzalez-Agirre and Marta Villegas},
      year={2026},
      eprint={2602.21379},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2602.21379}, 
}
```

### Funding
This work is funded by the Ministerio para la Transformación Digital y de la Función Pública - Funded by EU – NextGenerationEU within the framework of the project [ALIA](https://alia.gob.es).

### Acknowledgments
This dataset has been generated thanks to [CEATIC](https://www.ujaen.es/centros/ceatic/) (
Centro de Estudios Avanzados en Tecnologías de la Información y de la Comunicación) – [UJA](http://www.ujaen.es/) (Universidad de Jaén) which provided the needed computational resources on its clusters.

---

**Contact:** [ALIA Project](https://www.alia.gob.es/) - [SINAI Research Group](https://sinai.ujaen.es) - [Universidad de Jaén](https://www.ujaen.es/)

**More Information:** [SINAI Research Group](https://sinai.ujaen.es) | [ALIA-UJA Project](https://github.com/sinai-uja/ALIA-UJA)
