---
tags:
- ColBERT
- PyLate
- sentence-transformers
- sentence-similarity
- feature-extraction
- multilingual
- code search
- arxiv:2607.27178
pipeline_tag: sentence-similarity
library_name: PyLate
license: apache-2.0
language:
- en
- fr
- de
- it
- es
- pt
- sv
- 'no'
- ar
- code
base_model:
- jhu-clsp/mmBERT-base
---

<div align="center">
<img src="https://cdn-uploads.huggingface.co/production/uploads/609bbe2f4932693ca2009d6a/D2x1Tlj0fMgn2Y9IwHlUx.png" alt="LightOn" width="512">

[![Website](https://img.shields.io/badge/LightOn-Website-blue?logo=google-chrome)](https://lighton.ai)
[![LinkedIn](https://img.shields.io/badge/LightOn-LinkedIn-0A66C2?logo=linkedin)](https://www.linkedin.com/company/lighton/)
[![X](https://img.shields.io/badge/@LightOnIO-X-black?logo=x)](https://x.com/LightOnIO)

  📚 [Collection](https://huggingface.co/collections/lightonai/mdenseon-and-mlateon) | 📝 [Multilingual Blog](https://huggingface.co/blog/lightonai/mdenseon-mlateon) | 📝 [English Blog](https://huggingface.co/blog/lightonai/denseon-lateon) | 📝 [Paper](https://arxiv.org/abs/2607.27178) 

</div>

<h1 align="center">mLateOn-unsupervised</h1>

<h3 align="center">State-of-the-Art Multilingual ColBERT Retrieval Model by LightOn</h3>

<p align="center">
<a href="https://huggingface.co/lightonai/mDenseOn">mDenseOn</a> |
<a href="https://huggingface.co/lightonai/mLateOn">mLateOn</a> |
<a href="https://huggingface.co/lightonai/DenseOn">DenseOn</a> |
<a href="https://huggingface.co/lightonai/LateOn">LateOn</a> |
<a href="https://github.com/lightonai/pylate">PyLate</a> |
<a href="https://github.com/lightonai/fast-plaid">FastPlaid</a>
</p>

> 🎯 **TL;DR**: The intermediate multilingual ColBERT checkpoint produced by **Stage 1 only** (unsupervised contrastive pre-training) of the [mLateOn](https://huggingface.co/lightonai/mLateOn) pipeline, trained on a multilingual dataset with **2.8B query–document pairs across nine languages** (including 25% cross-lingual pairs). Released as a **strong starting point for your own supervised fine-tuning, knowledge distillation, or downstream adaptation**.

## About the mDenseOn / mLateOn Family

With [DenseOn](https://huggingface.co/lightonai/DenseOn) and [LateOn](https://huggingface.co/lightonai/LateOn), we demonstrated that an open, carefully curated data recipe can match closed-data retrieval models on English. mDenseOn and mLateOn extend this recipe to multilingual, long-context, and code retrieval.

Rather than independently collecting multilingual corpora from scratch (which would be expensive, uneven across languages, and hard to curate at the same quality), we applied the **translate-train** approach: machine-translating our validated English data into eight target languages (French, German, Italian, Spanish, Portuguese, Swedish, Norwegian, and Arabic) and adding cross-lingual pairs for cross-lingual alignment.

For more information, please read our [multilingual models blog post](https://huggingface.co/blog/lightonai/mdenseon-mlateon), our [English models blog post](https://huggingface.co/blog/lightonai/denseon-lateon) and our [paper](https://arxiv.org/abs/2607.27178).
## mLateOn-unsupervised

mLateOn-unsupervised is the output of the **first stage** of the [mLateOn](https://huggingface.co/lightonai/mLateOn) training pipeline. It has been pre-trained on a large, filtered multilingual corpus of approximately **2.8B query–document pairs** across nine languages (including **25% cross-lingual pairs**) using in-batch contrastive learning, but has **not** yet been fine-tuned with mined hard negatives.

For most production use cases, you should use the **fully-trained [mLateOn](https://huggingface.co/lightonai/mLateOn)** instead. This unsupervised checkpoint is intended for:

- Researchers studying what each pipeline stage contributes in a multilingual setting
- Practitioners who want to fine-tune on their own domain-specific or language-specific data
- Distillation experiments where you want to start from a strong but un-aligned multilingual base
- Anyone running their own ablations on hard-negative mining strategies or translate-train recipes

## Related Checkpoints

| Model | Description | Link |
|:---|:---|:---|
| **mLateOn-unsupervised** *(this card)* | Multilingual late-interaction, pre-training only | [`lightonai/mLateOn-unsupervised`](https://huggingface.co/lightonai/mLateOn-unsupervised) |
| mLateOn | Multilingual late-interaction retriever *(recommended)* | [`lightonai/mLateOn`](https://huggingface.co/lightonai/mLateOn) |
| mDenseOn-unsupervised | Multilingual dense, pre-training only | [`lightonai/mDenseOn-unsupervised`](https://huggingface.co/lightonai/mDenseOn-unsupervised) |
| mDenseOn | Multilingual dense retriever | [`lightonai/mDenseOn`](https://huggingface.co/lightonai/mDenseOn) |
| LateOn-unsupervised | English-only late-interaction, pre-training only | [`lightonai/LateOn-unsupervised`](https://huggingface.co/lightonai/LateOn-unsupervised) |
| LateOn | English-only late-interaction retriever | [`lightonai/LateOn`](https://huggingface.co/lightonai/LateOn) |
| DenseOn-unsupervised | English-only dense, pre-training only | [`lightonai/DenseOn-unsupervised`](https://huggingface.co/lightonai/DenseOn-unsupervised) |
| DenseOn | English-only dense retriever | [`lightonai/DenseOn`](https://huggingface.co/lightonai/DenseOn) |

### Model Description
- **Model Type:** PyLate ColBERT model
- **Base model:** [mmBERT-base](https://huggingface.co/jhu-clsp/mmBERT-base)
- **Query/Document Length:** 8,192 tokens
- **Output Dimensionality:** 128 tokens
- **Similarity Function:** MaxSim
- **Languages:** English, French, German, Italian, Spanish, Portuguese, Swedish, Norwegian, Arabic
- **License:** Apache 2.0

### Model Sources

- **Documentation:** [PyLate Documentation](https://lightonai.github.io/pylate/)
- **Repository:** [PyLate on GitHub](https://github.com/lightonai/pylate)
- **Hugging Face:** [PyLate models on Hugging Face](https://huggingface.co/models?library=PyLate)

### Full Model Architecture

```
ColBERT(
  (0): Transformer({'max_seq_length': 8192, 'do_lower_case': False, 'architecture': 'ModernBertModel'})
  (1): Dense({'in_features': 768, 'out_features': 1536, 'bias': False, 'activation_function': 'torch.nn.modules.linear.Identity', 'use_residual': True})
  (2): Dense({'in_features': 1536, 'out_features': 768, 'bias': False, 'activation_function': 'torch.nn.modules.linear.Identity', 'use_residual': True})
  (3): Dense({'in_features': 768, 'out_features': 128, 'bias': False, 'activation_function': 'torch.nn.modules.linear.Identity', 'use_residual': False})
)
```

## Usage

First install the PyLate library:

```bash
pip install -U pylate
```

### Retrieval

Use this model with PyLate to index and retrieve documents. The index uses [FastPlaid](https://github.com/lightonai/fast-plaid) for efficient similarity search.

#### Indexing documents

Load the ColBERT model and initialize the PLAID index, then encode and index your documents:

```python
from pylate import indexes, models, retrieve

# Step 1: Load the ColBERT model
model = models.ColBERT(
    model_name_or_path="lightonai/mLateOn-unsupervised",
)

# Step 2: Initialize the PLAID index
index = indexes.PLAID(
    index_folder="pylate-index",
    index_name="index",
    override=True,  # This overwrites the existing index if any
)

# Step 3: Encode the documents (supports multilingual content)
documents_ids = ["1", "2", "3", "4"]
documents = [
    "Mars, known for its reddish appearance, is often referred to as the Red Planet.",
    "Mars, connu pour son apparence rougeâtre, est souvent appelé la planète rouge.",
    "Mars, bekannt für sein rötliches Erscheinungsbild, wird oft als der Rote Planet bezeichnet.",
    "Venus is often called Earth's twin because of its similar size and proximity.",
]

documents_embeddings = model.encode(
    documents,
    batch_size=32,
    is_query=False,  # Ensure that it is set to False to indicate that these are documents, not queries
    show_progress_bar=True,
)

# Step 4: Add document embeddings to the index by providing embeddings and corresponding ids
index.add_documents(
    documents_ids=documents_ids,
    documents_embeddings=documents_embeddings,
)
```

Note that you do not have to recreate the index and encode the documents every time. Once you have created an index and added the documents, you can re-use the index later by loading it:

```python
# To load an index, simply instantiate it with the correct folder/name and without overriding it
index = indexes.PLAID(
    index_folder="pylate-index",
    index_name="index",
)
```

#### Retrieving top-k documents for queries

Once the documents are indexed, you can retrieve the top-k most relevant documents for a given set of queries — including cross-lingual retrieval:

```python
# Step 1: Initialize the ColBERT retriever
retriever = retrieve.ColBERT(index=index)

# Step 2: Encode the queries (can be in any supported language)
queries_embeddings = model.encode(
    [
        "Quelle planète est connue comme la planète rouge ?",  # French query
        "Which planet is the Red Planet?",                      # English query
    ],
    batch_size=32,
    is_query=True,  # Ensure that it is set to True to indicate that these are queries
    show_progress_bar=True,
)

# Step 3: Retrieve top-k documents (returns matches across all languages)
scores = retriever.retrieve(
    queries_embeddings=queries_embeddings,
    k=10,  # Retrieve the top 10 matches for each query
)
```

### Reranking

If you only want to use the ColBERT model to perform reranking on top of your first-stage retrieval pipeline without building an index, you can simply use the rank function and pass the queries and documents to rerank:

```python
from pylate import rank, models

queries = [
    "Quelle planète est la planète rouge ?",
    "What is the largest planet in the solar system?",
]

documents = [
    ["Mars ist der Rote Planet.", "Venus ist der Zwilling der Erde."],
    ["Jupiter is the largest planet.", "Saturn is known for its rings.", "Mars is the Red Planet."],
]

documents_ids = [
    [1, 2],
    [1, 3, 2],
]

model = models.ColBERT(
    model_name_or_path="lightonai/mLateOn-unsupervised",
)

queries_embeddings = model.encode(
    queries,
    is_query=True,
)

documents_embeddings = model.encode(
    documents,
    is_query=False,
)

reranked_documents = rank.rerank(
    documents_ids=documents_ids,
    queries_embeddings=queries_embeddings,
    documents_embeddings=documents_embeddings,
)
```

### Framework Versions
- Python: 3.11.10
- Sentence Transformers: 5.1.1
- PyLate: 1.3.4
- Transformers: 4.57.5
- PyTorch: 2.9.0+cu128
- Accelerate: 1.12.0
- Datasets: 3.6.0
- Tokenizers: 0.22.1

## Citation

### BibTeX

#### mDenseOn and mLateOn

```bibtex
@misc{sourty2026denseonlateonfullyopen,
  title         = {DenseOn with the LateOn: Fully Open Dense and Late-Interaction Models for Multilingual, Long-Context, and Code Search},
  author        = {Raphaël Sourty and Antoine Chaffin and Paulo Roberto Moura Junior and Amélie Chatelain},
  year          = {2026},
  eprint        = {2607.27178},
  archivePrefix = {arXiv},
  primaryClass  = {cs.CL},
  url           = {https://arxiv.org/abs/2607.27178},
}
```

#### DenseOn and LateOn
```bibtex
@misc{sourty2026denseonlateon,
  title={DenseOn with the LateOn: Open State-of-the-Art Single and Multi-Vector Models},
  author={Sourty, Raphael and Chaffin, Antoine and Weller, Orion and Moura Junior, Paulo Roberto and Chatelain, Amelie},
  year={2026},
  howpublished={\url{https://huggingface.co/blog/lightonai/denseon-lateon}},
}
```

#### PyLate

```bibtex
@inproceedings{DBLP:conf/cikm/ChaffinS25,
  author       = {Antoine Chaffin and
                  Rapha{\"{e}}l Sourty},
  editor       = {Meeyoung Cha and
                  Chanyoung Park and
                  Noseong Park and
                  Carl Yang and
                  Senjuti Basu Roy and
                  Jessie Li and
                  Jaap Kamps and
                  Kijung Shin and
                  Bryan Hooi and
                  Lifang He},
  title        = {PyLate: Flexible Training and Retrieval for Late Interaction Models},
  booktitle    = {Proceedings of the 34th {ACM} International Conference on Information
                  and Knowledge Management, {CIKM} 2025, Seoul, Republic of Korea, November
                  10-14, 2025},
  pages        = {6334--6339},
  publisher    = {{ACM}},
  year         = {2025},
  url          = {https://github.com/lightonai/pylate},
  doi          = {10.1145/3746252.3761608},
}
```

#### Sentence Transformers

```bibtex
@inproceedings{reimers-2019-sentence-bert,
    title = "Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks",
    author = "Reimers, Nils and Gurevych, Iryna",
    booktitle = "Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing",
    month = "11",
    year = "2019",
    publisher = "Association for Computational Linguistics",
    url = "https://arxiv.org/abs/1908.10084"
}
```

## Acknowledgements

We thank Eugene Yang for his feedback on adapting our English study to multilinguality through translate-train. We again thank Xin Zhang, Zach Nussbaum, Tom Aarsen, Bo Wang, Eugene Yang, Benjamin Clavié, Nandan Thakur, Oskar Hallström and Iacopo Poli for their valuable contributions and feedback on the original English study. We thank Orion Weller for building the FineWeb-derived Common Crawl split as well as for his feedback and help. We are grateful to the teams behind Sentence Transformers, BEIR, and MIRACL, and to the open-source retrieval community, in particular the authors of Nomic Embed.

This work was granted access to the HPC resources of IDRIS under GENCI allocations AS011016449, A0181016214, and A0171015706 (Jean Zay supercomputer). We also acknowledge the Barcelona Supercomputing Center (BSC-CNS) for providing access to MareNostrum 5 under EuroHPC AI Factory Fast Lane project EHPC-AIF-2025FL01-445. This project is also supported by the OpenEuroLLM project, co-funded by the Digital Europe Programme under GA no. 101195233.