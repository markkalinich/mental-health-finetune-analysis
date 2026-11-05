---
license: apache-2.0
library_name: sentence-transformers
pipeline_tag: text-classification
language:
- es
base_model:
- BSC-LT/MrBERT-es
tags:
- biomedical
- spanish
- cross-encoder
- reranker
- sentence-transformers
- retrieval
---

# ALIA MrBERT Spanish Biomedical Reranker Model

This repository contains **ALIA MrBERT Spanish Biomedical Reranker**, a Spanish biomedical domain cross-encoder (reranker) model for information retrieval and document ranking tasks. It is built upon [MrBERT-es](https://huggingface.co/BSC-LT/MrBERT-es), a bilingual (Spanish–English) foundational language model based on the ModernBERT architecture, and fine-tuned on domain-specific biomedical data using a Curriculum Learning strategy.

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
  ALIA-MrBERT-es-biomedical-reranker (SINAI)
  Biomedical domain fine-tuning
  Curriculum Learning + Hard Negatives
```

### Key Features

- 🔍 **Domain**: Spanish biomedical texts
- 📐 **Architecture**: ModernBERT Cross-Encoder (reranker)
- 📏 **Context length**: up to 8,192 tokens
- 🎓 **Training strategy**: Curriculum Learning (easy → medium → hard)
- ⚙️ **Negative mining**: Positive-Aware Hard Negative Mining

### Architecture

This model uses the same base architecture as [MrBERT-es](https://huggingface.co/BSC-LT/MrBERT-es), formatted as a Cross-Encoder for sentence pair classification:

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
| **Model Type**               | Cross-Encoder |

---

## Training

### Training Strategy: Curriculum Learning

The model was fine-tuned using a **Curriculum Learning** strategy, progressively increasing the difficulty of training examples. For this Cross-Encoder, the training focused on the most challenging examples: pairs that a Bi-Encoder might struggle to distinguish.

The dataset consists of text pairs incorporating hard negatives mined from the corpus [SINAI/ALIA-es-biomedical-triplets/train](https://huggingface.co/datasets/SINAI/ALIA-es-biomedical-triplets/viewer/hard-negatives). For the Cross-Encoder, the data is **flattened** into independent `{query, document, label}` pairs, where `label` is either `1.0` (relevant) or `0.0` (irrelevant).

**Refinement with Hard Negatives:**
Training uses mined hard negatives to force the model to distinguish fine-grained nuances. Examples are processed in order of increasing difficulty (easy → medium → hard) to improve convergence and generalization.

### Hyperparameter Optimization

Before training, hyperparameter search was conducted using **[Optuna](https://optuna.org/)** (20 trials) to maximize NDCG@10 (with fallback to MRR@10) on a control subset:
- **Sampler**: TPESampler (Tree-structured Parzen Estimator)
- **Pruner**: MedianPruner with an `OptunaPruningCallback` reporting NDCG@10
- **Evaluator**: `CrossEncoderRerankingEvaluator`

### Final Training Hyperparameters

| Hyperparameter | Value | Description |
|----------------|:-----:|:------------|
| **Learning Rate** | 4.8×10⁻⁵ | Nominal learning rate |
| **Batch Size** | 32 | Global batch size per device |
| **Gradient Accumulation** | 4 | Simulates larger effective batches |
| **Warmup Ratio** | 0.1345 | Linear LR warmup during the first 11% of steps |
| **Weight Decay** | 0.0416 | L2 regularization |
| **Optimizer** | AdamW | Standard HuggingFace Trainer optimizer |
| **Precision** | bf16 | Bfloat16 for supported architectures |
| **Max Sequence Length** | 8,192 | Maximum tokens processed for the concatenated (query, doc) pair |
| **Loss Function** | BinaryCrossEntropyLoss | Treats pairs as an independent binary classification problem |
| **Gradient Checkpointing**| Enabled | Memory optimization for long contexts (`use_reentrant=False`) |

### Training Framework

| Component | Details |
|-----------|---------|
| **Library** | PyTorch, `sentence-transformers`, HuggingFace `datasets` |
| **Distributed** | DDP (Distributed Data Parallel) via `torchrun` |
| **Memory optimization** | Gradient Checkpointing (`expandable_segments:True`) |
| **Logging** | WandB (via `report_to=wandb`) |

---

## Intended Use

### Direct Use

This model is designed for document reranking and semantic matching tasks in the **Spanish biomedical domain**. Primary use cases include:
- **RAG pipelines**: Reranking retrieved context chunks for language models
- **Search pipelines**: Improving initial retrieval (e.g. BM25 or Bi-encoder) by doing precise cross-encoding over the top-k results
- **Biomedical text matching**: Determining high-resolution entailment or relevance between queries and biomedical passages

### Out-of-Scope Use

- General-domain retrieval (the model is specialized for biomedical Spanish)
- Fast, large-scale search across millions of documents (use a Bi-encoder first, then rerank the top-k results with this Cross-encoder)
- Cross-lingual retrieval beyond Spanish

---

## How to Use

### With `sentence-transformers`

```python
from sentence_transformers import CrossEncoder

model = CrossEncoder("SINAI/ALIA-MrBERT-es-biomedical-reranker")

query = "¿Cuáles son los síntomas principales de la insuficiencia cardíaca?"
documents = [
    "La insuficiencia cardíaca puede causar disnea, fatiga y edema periférico...",
    "El tratamiento inicial incluye control de la presión arterial y ajuste farmacológico...",
    "El subsidio de incapacidad temporal requiere un certificado médico en vigor.",
]

# We want to score the query with each document
pairs = [[query, doc] for doc in documents]

scores = model.predict(pairs)
print(scores)
```

---

## Evaluation

The model was evaluated using the [MTEB](https://huggingface.co/mteb) (Massive Text Embedding Benchmark) framework, adapted for the biomedical domain. The main reported metric is **NDCG@10** (Normalized Discounted Cumulative Gain at k=10), which is the standard metric used in retrieval leaderboards and aligns with the metric reported in the MrBERT family.

### Evaluation Datasets

| Dataset | Category | Description |
|---------|----------|-------------|
| **miracl** | Reranking | Spanish subset of the MIRACL ([mteb/MIRACLReranking](https://huggingface.co/datasets/mteb/MIRACLReranking)) |
| **esci** | Reranking | ESCI dataset for Spanish language ([mteb/ESCIReranking](https://huggingface.co/datasets/mteb/ESCIReranking)) |
| **CoWeSe** | Retrieval | Generated open-ended questions from the [CoWeSe](https://arxiv.org/abs/2109.07765) corpus ([chrisnb1/cowese-qa-dataset](https://huggingface.co/datasets/chrisnb1/cowese-qa-dataset)) |
| **AbSanitas** | Retrieval | Spanish biomedical information retrieval dataset built from biomedical texts collected from official academic repositories and open-access sources ([BSC-LT/AbSanitas](https://huggingface.co/datasets/BSC-LT/AbSanitas)) |
| **pairs800** | Retrieval | Subset of 800 biomedical evaluation pairs (query + passage) derived from [SINAI/ALIA-es-biomedical-triplets/test](https://huggingface.co/datasets/SINAI/ALIA-es-biomedical-triplets/viewer/evaluation). |
| **pairs1.6k** | Retrieval | Subset of 1.6k biomedical evaluation pairs (query + passage) derived from [SINAI/ALIA-es-biomedical-triplets/test](https://huggingface.co/datasets/SINAI/ALIA-es-biomedical-triplets/viewer/evaluation). |

### Results

The following table reports the performance of the model compared to leading commercial/open-weight generalist models:

| Model | miracl | esci | CoWeSe | AbSanitas | pairs800 | pairs1.6k |
|-------|:------------:|:-------------:|:--------:|:--------:|:------------:|:-------------:|
| [BAAI/bge-reranker-v2-m3](https://huggingface.co/BAAI/bge-reranker-v2-m3) | **0.6777** | **0.8321** | 0.9598 | 0.9966 | 0.9989 | 0.9987 |
| [nvidia/llama-nemotron-rerank-1b-v2](https://huggingface.co/nvidia/llama-nemotron-rerank-1b-v2) | 0.6258 | 0.8004 | 0.8957 | 0.9938 | 0.9878 | 0.9875 |
| [tomaarsen/Qwen3-Reranker-0.6B-seq-cls](https://huggingface.co/tomaarsen/Qwen3-Reranker-0.6B-seq-cls) | 0.6724 | 0.8133 | 0.9223 | 0.9983 | 0.9969 | 0.9942 |
| **ALIA-MrBERT-es-biomedical-reranker (ours)** | 0.5509 | 0.8164 | **0.9625** | **0.9987**| **1** | **0.9992** |

*Note: The BGE reranker is a significantly larger scale model (billions of parameters), yet our domain-specific 150M parameter cross-encoder performs comparably or better on specialized biomedical Spanish datasets (e.g., CoWeSe, AbSanitas, pairs800, pairs1.6k).*

---

## Limitations and Biases

### Known Limitations

- **Domain specificity**: The model is highly optimized for Spanish biomedical texts. Its zero-shot capabilities on general domains are weaker compared to massive generalist rerankers.
- **Latency**: Being a cross-encoder, it can be computationally heavy to score many document-query pairs. Use it to rerank a maximum of typical 20-100 top documents fetched by a fast bi-encoder.
- **Clinical accuracy**: Semantic similarity does not guarantee clinical or medical correctness.

### Biases

- The model reflects biases present in Spanish biomedical literature, clinical records, and health-related corpora.

---

## Additional Information

### License
[Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0)

### Citation
If you use this model in your research, please cite:

```bibtex
@misc{ALIA-MrBERT-es-biomedical-reranker,
  title        = {ALIA MrBERT Spanish Biomedical Reranker Model},
  author       = {SINAI Research Group, Universidad de Jaén},
  year         = {2026},
  publisher    = {HuggingFace},
  howpublished = {\url{https://huggingface.co/SINAI/ALIA-MrBERT-es-biomedical-reranker}}
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
This dataset has been generated thanks to [CEATIC](https://www.ujaen.es/centros/ceatic/) (Centro de Estudios Avanzados en Tecnologías de la Información y de la Comunicación) – [UJA](http://www.ujaen.es/) (Universidad de Jaén) which provided the needed computational resources on its clusters.

---

**Contact:** [ALIA Project](https://www.alia.gob.es/) - [SINAI Research Group](https://sinai.ujaen.es) - [Universidad de Jaén](https://www.ujaen.es/)

**More Information:** [SINAI Research Group](https://sinai.ujaen.es) | [ALIA-UJA Project](https://github.com/sinai-uja/ALIA-UJA)