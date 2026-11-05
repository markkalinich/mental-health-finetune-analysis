---
tags:
- sentence-transformers
- sentence-similarity
- loss:OnlineContrastiveLoss
base_model: Alibaba-NLP/gte-modernbert-base
pipeline_tag: sentence-similarity
library_name: sentence-transformers
metrics:
- cosine_accuracy
- cosine_precision
- cosine_recall
- cosine_f1
- cosine_ap
model-index:
- name: SentenceTransformer based on Alibaba-NLP/gte-modernbert-base
  results:
  - task:
      type: my-binary-classification
      name: My Binary Classification
    dataset:
      name: Medical
      type: unknown
    metrics:
    - type: cosine_accuracy
      value: 0.92
      name: Cosine Accuracy
    - type: cosine_f1
      value: 0.93
      name: Cosine F1
    - type: cosine_precision
      value: 0.92
      name: Cosine Precision
    - type: cosine_recall
      value: 0.93
      name: Cosine Recall
    - type: cosine_ap
      value: 0.97
      name: Cosine Ap
---

# Redis semantic caching embedding model based on Alibaba-NLP/gte-modernbert-base

This is a [sentence-transformers](https://www.SBERT.net) model finetuned from [Alibaba-NLP/gte-modernbert-base](https://huggingface.co/Alibaba-NLP/gte-modernbert-base) on the [Medical]( https://www.kaggle.com/datasets/thedevastator/medical-question-pair-classification/data) dataset. It maps sentences & paragraphs to a 768-dimensional dense vector space and can be used for semantic textual similarity for the purpose of semantic caching in the medical domain.

## Model Details

### Model Description
- **Model Type:** Sentence Transformer
- **Base model:** [Alibaba-NLP/gte-modernbert-base](https://huggingface.co/Alibaba-NLP/gte-modernbert-base) <!-- at revision bc02f0a92d1b6dd82108036f6cb4b7b423fb7434 -->
- **Maximum Sequence Length:** 8192 tokens
- **Output Dimensionality:** 768 dimensions
- **Similarity Function:** Cosine Similarity
- **Training Dataset:**
    - [Medical]( https://www.kaggle.com/datasets/thedevastator/medical-question-pair-classification/data)
<!-- - **Language:** Unknown -->
<!-- - **License:** Unknown -->

### Model Sources

- **Documentation:** [Sentence Transformers Documentation](https://sbert.net)
- **Repository:** [Sentence Transformers on GitHub](https://github.com/UKPLab/sentence-transformers)
- **Hugging Face:** [Sentence Transformers on Hugging Face](https://huggingface.co/models?library=sentence-transformers)

### Full Model Architecture

```
SentenceTransformer(
  (0): Transformer({'max_seq_length': 8192, 'do_lower_case': False}) with Transformer model: ModernBertModel
  (1): Pooling({'word_embedding_dimension': 768, 'pooling_mode_cls_token': True, 'pooling_mode_mean_tokens': False, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False, 'pooling_mode_weightedmean_tokens': False, 'pooling_mode_lasttoken': False, 'include_prompt': True})
)
```

## Usage

First install the Sentence Transformers library:

```bash
pip install -U sentence-transformers
```

Then you can load this model and run inference.
```python
from sentence_transformers import SentenceTransformer

# Download from the 🤗 Hub
model = SentenceTransformer("redis/langcache-embed-medical-v1")
# Run inference
sentences = [
    'Will the value of Indian rupee increase after the ban of 500 and 1000 rupee notes?',
    'What will be the implications of banning 500 and 1000 rupees currency notes on Indian economy?',
    "Are Danish Sait's prank calls fake?",
]
embeddings = model.encode(sentences)
print(embeddings.shape)
# [3, 768]

# Get the similarity scores for the embeddings
similarities = model.similarity(embeddings, embeddings)
print(similarities.shape)

```

#### Binary Classification


| Metric                    | Value     |
|:--------------------------|:----------|
| cosine_accuracy           |  0.92   |
| cosine_f1                 |  0.93   |
| cosine_precision          |  0.92   |
| cosine_recall             |  0.93   |
| **cosine_ap**             |  0.97   |


### Training Dataset

#### Medical

* Dataset: [Medical dataset]( https://www.kaggle.com/datasets/thedevastator/medical-question-pair-classification/data)
* Size: 2438 samples
* Columns: <code>question_1</code>, <code>question_2</code>, and <code>label</code>

### Evaluation Dataset

#### Medical

* Dataset: [Medical dataset]( https://www.kaggle.com/datasets/thedevastator/medical-question-pair-classification/data)
* Size: 610 samples
* Columns: <code>question_1</code>, <code>question_2</code>, and <code>label</code>

## Citation

### BibTeX

#### Redis Langcache-embed Models
```bibtex
@inproceedings{langcache-embed-v1,
    title = "Advancing Semantic Caching for LLMs with Domain-Specific Embeddings and Synthetic Data",
    author = "Gill, Cechmanek, Hutcherson, Rajamohan, Agarwal, Gulzar, Singh, Dion",
    month = "04",
    year = "2025",
    url = "https://arxiv.org/abs/2504.02268",
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
    url = "https://arxiv.org/abs/1908.10084",
}
```

<!--
