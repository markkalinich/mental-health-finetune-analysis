---
tags:
- sentence-transformers
- sparse-encoder
- sparse
- splade
- generated_from_trainer
- loss:SpladeLoss
- loss:SparseMultipleNegativesRankingLoss
- loss:FlopsLoss
base_model: microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext
pipeline_tag: sentence-similarity
library_name: sentence-transformers
metrics:
- pearson_cosine
- spearman_cosine
- active_dims
- sparsity_ratio
model-index:
- name: SPLADE Sparse Encoder
  results:
  - task:
      type: semantic-similarity
      name: Semantic Similarity
    dataset:
      type: pubmed-similarity
      name: PubMed Similarity
    metrics:
    - type: pearson_cosine
      value: 0.9422980731390805
      name: Pearson Cosine
    - type: spearman_cosine
      value: 0.8870061609483617
      name: Spearman Cosine
    - type: active_dims
      value: 34.0018196105957
      name: Active Dims
    - type: sparsity_ratio
      value: 0.9988859897906233
      name: Sparsity Ratio
language: en
license: apache-2.0
---

# PubMedBERT SPLADE

This is a [SPLADE Sparse Encoder](https://www.sbert.net/docs/sparse_encoder/usage/usage.html) model finetuned from [PubMedBERT-base](https://huggingface.co/microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext) using [sentence-transformers](https://www.SBERT.net). It maps sentences & paragraphs to a 30522-dimensional sparse vector space and can be used for semantic search and sparse retrieval.

The training dataset was generated using a random sample of [PubMed](https://pubmed.ncbi.nlm.nih.gov/) title-abstract pairs along with similar title pairs.

PubMedBERT SPLADE produces higher quality sparse embeddings than generalized models for medical literature. Further fine-tuning for a medical subdomain will result in even better performance.

## Usage (txtai)

This model can be used to build embeddings databases with [txtai](https://github.com/neuml/txtai) for semantic search and/or as a knowledge source for retrieval augmented generation (RAG).

_Note: txtai 9.0+ is required for sparse vector scoring support_

```python
import txtai

embeddings = txtai.Embeddings(
  sparse="neuml/pubmedbert-base-splade",
  content=True
)
embeddings.index(documents())

# Run a query
embeddings.search("query to run")
```

## Usage (Sentence-Transformers)

Alternatively, the model can be loaded with [sentence-transformers](https://www.SBERT.net).

```python
from sentence_transformers import SparseEncoder
sentences = ["This is an example sentence", "Each sentence is converted"]

model = SparseEncoder("neuml/pubmedbert-base-splade")
embeddings = model.encode(sentences)
print(embeddings)
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
| [pubmedbert-base-embeddings](https://hf.co/neuml/pubmedbert-base-embeddings)       | 93.27     | 97.00         | 96.58          | 95.62     |
| [**pubmedbert-base-splade**](https://hf.co/neuml/pubmedbert-base-splade)       | **90.76**     | **96.20**         | **95.87**          | **94.28**     |
| [S-PubMedBert-MS-MARCO](https://hf.co/pritamdeka/S-PubMedBert-MS-MARCO)            | 90.86     | 93.68         | 93.54          | 92.69     |

While this model was't the highest scoring model using the Pearson metric, it does well when measured by [Spearman rank correlation coefficient](https://en.wikipedia.org/wiki/Spearman%27s_rank_correlation_coefficient).

| Model                                                                         | PubMed QA | PubMed Subset | PubMed Summary | Average   |
| ----------------------------------------------------------------------------- | --------- | ------------- | -------------- | --------- | 
| [all-MiniLM-L6-v2](https://hf.co/sentence-transformers/all-MiniLM-L6-v2)           | 85.77     | 86.52         | 86.32          | 86.20     |
| [bge-base-en-v1.5](https://hf.co/BAAI/bge-base-en-v1.5)                            | 85.71     | 86.58         | 86.35          | 86.21     |
| [gte-base](https://hf.co/thenlper/gte-base)                                        | 86.44     | 86.60        | 86.55          | 86.53     |
| [pubmedbert-base-embeddings](https://hf.co/neuml/pubmedbert-base-embeddings)       | 86.29     | 86.57         | 86.47          | 86.44     |
| [**pubmedbert-base-splade**](https://hf.co/neuml/pubmedbert-base-splade)        | **86.80** | **89.12**     | **88.60**      | **88.17** |
| [S-PubMedBert-MS-MARCO](https://hf.co/pritamdeka/S-PubMedBert-MS-MARCO)            | 85.71     | 86.37         | 86.13          | 86.07     |

This indicates that the SPLADE model may do a better job of calculating scores/rankings in the correct direction. 

### Full Model Architecture

```
SparseEncoder(
  (0): MLMTransformer({'max_seq_length': 512, 'do_lower_case': False, 'architecture': 'BertForMaskedLM'})
  (1): SpladePooling({'pooling_strategy': 'max', 'activation_function': 'relu', 'word_embedding_dimension': 30522})
)
```

## More Information

The training data for this model is the same as described in [this article](https://medium.com/neuml/embeddings-for-medical-literature-74dae6abf5e0). See [this article](https://huggingface.co/blog/train-sparse-encoder) for more on the training scripts.
