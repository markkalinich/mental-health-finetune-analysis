---
pipeline_tag: text-ranking
language: fr
license: mit
datasets:
- unicamp-dl/mmarco
metrics:
- recall
tags:
- passage-reranking
library_name: sentence-transformers
base_model: cmarkea/distilcamembert-base
model-index:
- name: crossencoder-distilcamembert-mmarcoFR
  results:
  - task:
      type: text-classification
      name: Passage Reranking
    dataset:
      name: mMARCO-fr
      type: unicamp-dl/mmarco
      config: french
      split: validation
    metrics:
    - type: recall_at_500
      value: 96.15
      name: Recall@500
    - type: recall_at_100
      value: 84.39
      name: Recall@100
    - type: recall_at_10
      value: 56.33
      name: Recall@10
    - type: mrr_at_10
      value: 31.86
      name: MRR@10
---

# crossencoder-distilcamembert-mmarcoFR

This is a cross-encoder model for French. It performs cross-attention between a question-passage pair and outputs a relevance score. 
The model should be used as a reranker for semantic search: given a query and a set of potentially relevant passages retrieved by an efficient first-stage 
retrieval system (e.g., BM25 or a fine-tuned dense single-vector bi-encoder), encode each query-passage pair and sort the passages in a decreasing order of 
relevance according to the model's predicted scores.

## Usage

Here are some examples for using the model with [Sentence-Transformers](#using-sentence-transformers), [FlagEmbedding](#using-flagembedding), or [Huggingface Transformers](#using-huggingface-transformers).

#### Using Sentence-Transformers

Start by installing the [library](https://www.SBERT.net): `pip install -U sentence-transformers`. Then, you can use the model like this:

```python
from sentence_transformers import CrossEncoder

pairs = [('Question', 'Paragraphe 1'), ('Question', 'Paragraphe 2') , ('Question', 'Paragraphe 3')]

model = CrossEncoder('antoinelouis/crossencoder-distilcamembert-mmarcoFR')
scores = model.predict(pairs)
print(scores)
```

#### Using FlagEmbedding

Start by installing the [library](https://github.com/FlagOpen/FlagEmbedding/): `pip install -U FlagEmbedding`. Then, you can use the model like this:

```python
from FlagEmbedding import FlagReranker

pairs = [('Question', 'Paragraphe 1'), ('Question', 'Paragraphe 2') , ('Question', 'Paragraphe 3')]

reranker = FlagReranker('antoinelouis/crossencoder-distilcamembert-mmarcoFR')
scores = reranker.compute_score(pairs)
print(scores)
```

#### Using HuggingFace Transformers

Start by installing the [library](https://huggingface.co/docs/transformers): `pip install -U transformers`. Then, you can use the model like this:

```python
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

pairs = [('Question', 'Paragraphe 1'), ('Question', 'Paragraphe 2') , ('Question', 'Paragraphe 3')]

tokenizer = AutoTokenizer.from_pretrained('antoinelouis/crossencoder-distilcamembert-mmarcoFR')
model = AutoModelForSequenceClassification.from_pretrained('antoinelouis/crossencoder-distilcamembert-mmarcoFR')
model.eval()

with torch.no_grad():
    inputs = tokenizer(pairs, padding=True, truncation=True, return_tensors='pt', max_length=512)
    scores = model(**inputs, return_dict=True).logits.view(-1, ).float()
print(scores)
```

***

## Evaluation

The model is evaluated on the smaller development set of [mMARCO-fr](https://ir-datasets.com/mmarco.html#mmarco/v2/fr/), which consists of 6,980 queries for which 
an ensemble of 1000 passages containing the positive(s) and [ColBERTv2 hard negatives](https://huggingface.co/datasets/antoinelouis/msmarco-dev-small-negatives) need 
to be reranked. We report the mean reciprocal rank (MRR) and recall at various cut-offs (R@k). To see how it compares to other neural retrievers in French, check out 
the [*DécouvrIR*](https://huggingface.co/spaces/antoinelouis/decouvrir) leaderboard.

***

## Training

#### Data

We use the French training samples from the [mMARCO](https://huggingface.co/datasets/unicamp-dl/mmarco) dataset, a multilingual machine-translated version of MS MARCO
that contains 8.8M passages and 539K training queries. We do not use the BM25 negatives provided by the official dataset but instead sample harder negatives mined from 
12 distinct dense retrievers, using the [msmarco-hard-negatives](https://huggingface.co/datasets/sentence-transformers/msmarco-hard-negatives#msmarco-hard-negativesjsonlgz) 
distillation dataset. Eventually, we sample 2.6M training triplets of the form (query, passage, relevance) with a positive-to-negative ratio of 1 (i.e., 50% of the pairs are 
relevant and 50% are irrelevant).

#### Implementation

The model is initialized from the [cmarkea/distilcamembert-base](https://huggingface.co/cmarkea/distilcamembert-base) checkpoint and optimized via the binary cross-entropy loss 
(as in [monoBERT](https://doi.org/10.48550/arXiv.1910.14424)). It is fine-tuned on one 80GB NVIDIA H100 GPU for 20k steps using the AdamW optimizer 
with a batch size of 128 and a constant learning rate of 2e-5. We set the maximum sequence length of the concatenated question-passage pairs to 256 tokens. 
We use the sigmoid function to get scores between 0 and 1.

***

## Citation

```bibtex
@online{louis2024decouvrir,
	author    = 'Antoine Louis',
	title     = 'DécouvrIR: A Benchmark for Evaluating the Robustness of Information Retrieval Models in French',
	publisher = 'Hugging Face',
	month     = 'mar',
	year      = '2024',
	url       = 'https://huggingface.co/spaces/antoinelouis/decouvrir',
}
```
