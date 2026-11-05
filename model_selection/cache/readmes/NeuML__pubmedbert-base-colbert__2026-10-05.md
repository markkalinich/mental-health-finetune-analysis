---
tags:
- ColBERT
- PyLate
- sentence-transformers
- sentence-similarity
- feature-extraction
- generated_from_trainer
- loss:Contrastive
base_model: microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext
pipeline_tag: sentence-similarity
library_name: PyLate
metrics:
- accuracy
model-index:
- name: PyLate model based on microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext
  results:
  - task:
      type: col-berttriplet
      name: Col BERTTriplet
    dataset:
      name: Unknown
      type: unknown
    metrics:
    - type: accuracy
      value: 0.9996359348297119
      name: Accuracy
language: en
license: apache-2.0
---

# PubMedBERT ColBERT

This is a [PyLate](https://github.com/lightonai/pylate) model finetuned from [microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext](https://huggingface.co/microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext). It maps sentences & paragraphs to sequences of 128-dimensional dense vectors and can be used for semantic textual similarity using the MaxSim operator.

## Usage (txtai)

This model can be used to build embeddings databases with [txtai](https://github.com/neuml/txtai) for semantic search and/or as a knowledge source for retrieval augmented generation (RAG).

_Note: txtai 9.0+ is required for late interaction model support_

```python
import txtai

embeddings = txtai.Embeddings(
  path="neuml/pubmedbert-base-colbert",
  content=True
)
embeddings.index(documents())

# Run a query
embeddings.search("query to run")
```

Late interaction models excel as reranker pipelines.

```python
from txtai.pipeline import Reranker, Similarity

similarity = Similarity(path="neuml/pubmedbert-base-colbert", lateencode=True)
ranker = Reranker(embeddings, similarity)
ranker("query to run")
```

## Usage (PyLate)

Alternatively, the model can be loaded with [PyLate](https://github.com/lightonai/pylate).

```python
from pylate import rank, models

queries = [
    "query A",
    "query B",
]

documents = [
    ["document A", "document B"],
    ["document 1", "document C", "document B"],
]

documents_ids = [
    [1, 2],
    [1, 3, 2],
]

model = models.ColBERT(
    model_name_or_path=pylate_model_id,
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

## Evaluation Results

Performance of this model compared to the top base models on the [MTEB leaderboard](https://huggingface.co/spaces/mteb/leaderboard) is shown below. A popular smaller model was also evaluated along with the most downloaded PubMed similarity model on the Hugging Face Hub.

The following datasets were used to evaluate model performance.

- [PubMed QA](https://huggingface.co/datasets/qiaojin/PubMedQA)
  - Subset: pqa_labeled, Split: train, Pair: (question, long_answer)
- [PubMed Subset](https://huggingface.co/datasets/awinml/pubmed_abstract_3_1k)
  - Split: test, Pair: (title, text)
- [PubMed Summary](https://huggingface.co/datasets/armanc/scientific_papers)
  - Subset: pubmed, Split: validation, Pair: (article, abstract)

Evaluation results are shown below. The [Pearson correlation coefficient](https://en.wikipedia.org/wiki/Pearson_correlation_coefficient) is used as the evaluation metric.

| Model                                                                         | PubMed QA | PubMed Subset | PubMed Summary | Average   |
| ----------------------------------------------------------------------------- | --------- | ------------- | -------------- | --------- | 
| [all-MiniLM-L6-v2](https://hf.co/sentence-transformers/all-MiniLM-L6-v2)           | 90.40     | 95.92         | 94.07          | 93.46     |
| [bge-base-en-v1.5](https://hf.co/BAAI/bge-base-en-v1.5)                            | 91.02     | 95.82         | 94.49          | 93.78     |
| [gte-base](https://hf.co/thenlper/gte-base)                                        | 92.97     | 96.90         | 96.24          | 95.37     |
| [**pubmedbert-base-colbert**](https://hf.co/neuml/pubmedbert-base-colbert)       | **93.94**     | **97.21**         | **95.27**          | **95.47**     |
| [**pubmedbert-base-colbert (MUVERA)**](https://hf.co/neuml/pubmedbert-base-colbert)       | **88.77**     | **93.51**         | **95.18**          | **92.49**     |
| [pubmedbert-base-embeddings](https://hf.co/neuml/pubmedbert-base-embeddings)       | 93.27     | 97.00         | 96.58          | 95.62     |
| [S-PubMedBert-MS-MARCO](https://hf.co/pritamdeka/S-PubMedBert-MS-MARCO)            | 90.86     | 93.68         | 93.54          | 92.69     |

While this isn't the highest scoring model, note how it is the best model for the first two datasets, which are retrieval datasets. ColBERT models can be better at picking up on query nuances given that vectors are not mean pooled together.

The model also performs well enough for [MUVERA encoding](https://arxiv.org/abs/2405.19504). The goal with MUVERA is "good enough" recall that picks up on the signal and is then paired with a reranker pipeline.

### Full Model Architecture

```
ColBERT(
  (0): Transformer({'max_seq_length': 512, 'do_lower_case': False}) with Transformer model: BertModel 
  (1): Dense({'in_features': 768, 'out_features': 128, 'bias': False, 'activation_function': 'torch.nn.modules.linear.Identity'})
)
```
