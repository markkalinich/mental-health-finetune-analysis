---
pipeline_tag: sentence-similarity
tags:
- sentence-transformers
- feature-extraction
- sentence-similarity
- transformers
- embeddings
- static-embeddings
base_model:
  - NeuML/pubmedbert-base-embeddings
language: en
license: apache-2.0
---

# PubMedBERT Embeddings 8M

This is a distilled version of [PubMedBERT Embeddings](https://huggingface.co/NeuML/pubmedbert-base-embeddings) using the [Model2Vec](https://github.com/MinishLab/model2vec) library. It uses static embeddings, allowing text embeddings to be computed orders of magnitude faster on both GPU and CPU. It is designed for applications where computational resources are limited or where real-time performance is critical.

## Usage (txtai)

This model can be used to build embeddings databases with [txtai](https://github.com/neuml/txtai) for semantic search and/or as a knowledge source for retrieval augmented generation (RAG).

```python
import txtai

# Create embeddings
embeddings = txtai.Embeddings(
  path="neuml/pubmedbert-base-embeddings-8M",
  content=True,
)
embeddings.index(documents())

# Run a query
embeddings.search("query to run")
```

## Usage (Sentence-Transformers)

Alternatively, the model can be loaded with [sentence-transformers](https://www.SBERT.net).

```python
from sentence_transformers import SentenceTransformer
from sentence_transformers.models import StaticEmbedding

# Initialize a StaticEmbedding module
static = StaticEmbedding.from_model2vec("neuml/pubmedbert-base-embeddings-8M")
model = SentenceTransformer(modules=[static])

sentences = ["This is an example sentence", "Each sentence is converted"]
embeddings = model.encode(sentences)
print(embeddings)
```

## Usage (Model2Vec)

The model can also be used directly with Model2Vec.

```python
from model2vec import StaticModel

# Load a pretrained Model2Vec model
model = StaticModel.from_pretrained("neuml/pubmedbert-base-embeddings-8M")

# Compute text embeddings
sentences = ["This is an example sentence", "Each sentence is converted"]
embeddings = model.encode(sentences)
print(embeddings)
```

## Evaluation Results

The following compares performance of this model against the models previously compared with [PubMedBERT Embeddings](https://huggingface.co/NeuML/pubmedbert-base-embeddings#evaluation-results). The following datasets were used to evaluate model performance.

- [PubMed QA](https://huggingface.co/datasets/qiaojin/PubMedQA)
  - Subset: pqa_labeled, Split: train, Pair: (question, long_answer)
- [PubMed Subset](https://huggingface.co/datasets/awinml/pubmed_abstract_3_1k)
  - Split: test, Pair: (title, text)
- [PubMed Summary](https://huggingface.co/datasets/armanc/scientific_papers)
  - Subset: pubmed, Split: validation, Pair: (article, abstract)

The [Pearson correlation coefficient](https://en.wikipedia.org/wiki/Pearson_correlation_coefficient) is used as the evaluation metric.

| Model                                                                              | PubMed QA | PubMed Subset | PubMed Summary | Average   |
| ---------------------------------------------------------------------------------- | --------- | ------------- | -------------- | --------- |
| [all-MiniLM-L6-v2](https://hf.co/sentence-transformers/all-MiniLM-L6-v2)           | 90.40     | 95.92         | 94.07          | 93.46     |
| [bge-base-en-v1.5](https://hf.co/BAAI/bge-base-en-v1.5)                            | 91.02     | 95.82         | 94.49          | 93.78     |
| [gte-base](https://hf.co/thenlper/gte-base)                                        | 92.97     | 96.90         | 96.24          | 95.37     |
| [pubmedbert-base-embeddings-2M](https://hf.co/neuml/pubmedbert-base-embeddings-2M) | 88.62     | 93.08         | 93.24          | 91.65     |
| [**pubmedbert-base-embeddings-8M**](https://hf.co/neuml/pubmedbert-base-embeddings-8M) | **90.05**     | **94.29**         | **94.15**          | **92.83**     |
| [pubmedbert-base-embeddings](https://hf.co/neuml/pubmedbert-base-embeddings)       | 93.27     | 97.00         | 96.58          | 95.62     |
| [S-PubMedBert-MS-MARCO](https://hf.co/pritamdeka/S-PubMedBert-MS-MARCO)            | 90.86     | 93.68         | 93.54          | 92.69     |

As we can see, this model while not the top scoring model is certainly competitive.

## Runtime performance

As another test, let's see how long each model takes to index 120K article abstracts using the following code. All indexing is done with a RTX 3090 GPU. 

```python
from datasets import load_dataset
from tqdm import tqdm
from txtai import Embeddings

ds = load_dataset("ccdv/pubmed-summarization", split="train")

embeddings = Embeddings(path="path to model", content=True, backend="numpy")
embeddings.index(tqdm(ds["abstract"]))
```

| Model                                                                              | Params (M) | Index time (s) |
| ---------------------------------------------------------------------------------- | ---------- | -------------- |
| [all-MiniLM-L6-v2](https://hf.co/sentence-transformers/all-MiniLM-L6-v2)           | 22         | 117            |
| BM25                                                                               | -          | 18             |
| [bge-base-en-v1.5](https://hf.co/BAAI/bge-base-en-v1.5)                            | 109        | 518            |
| [gte-base](https://hf.co/thenlper/gte-base)                                        | 109        | 523            |
| [pubmedbert-base-embeddings-2M](https://hf.co/neuml/pubmedbert-base-embeddings-2M) | 2          | 17             |
| [**pubmedbert-base-embeddings-8M**](https://hf.co/neuml/pubmedbert-base-embeddings-8M) | **8**  | **18**         |
| [pubmedbert-base-embeddings](https://hf.co/neuml/pubmedbert-base-embeddings)       | 109        | 462            |
| [S-PubMedBert-MS-MARCO](https://hf.co/pritamdeka/S-PubMedBert-MS-MARCO)            | 109        | 465            |

Clearly a static model's main upside is speed. It's important to note that if storage savings is the only concern, then take a look at [PubMedBERT Embeddings Matryoshka](https://huggingface.co/NeuML/pubmedbert-base-embeddings-matryoshka). The 256 dimension model scores higher than this model, so does the 64 dimension model. The tradeoff is that the runtime performance is still as slow as the base model.

If runtime performance is the major concern, then a static model offers the best blend of accuracy and speed. Model2Vec models only need CPUs to run, no GPU required. Note how this model takes the same amount of time as building a BM25 index, which is normally an order of magnitude faster than vector models.

## Training

This model was trained using the [Tokenlearn](https://github.com/MinishLab/tokenlearn) library. First data was featurized with the following script.

```bash
python -m tokenlearn.featurize --model-name "neuml/pubmedbert-base-embeddings" --dataset-path "training-articles" --output-dir "features"
```

_Note that the same random sample of articles as [described here](https://medium.com/neuml/embeddings-for-medical-literature-74dae6abf5e0) are used for the dataset `training-articles`._

From there, the following training script builds the model. The final model is weighted using [BM25](https://en.wikipedia.org/wiki/Okapi_BM25) instead of the default SIF weighting method. 

```python
from pathlib import Path

import numpy as np

from model2vec import StaticModel
from more_itertools import batched
from sklearn.decomposition import PCA
from tokenlearn.train import collect_means_and_texts, train_model
from tqdm import tqdm
from txtai.scoring import ScoringFactory

def tokenweights():
  tokenizer = model.tokenizer

  # Tokenize into dataset
  dataset = []
  for t in tqdm(batched(texts, 1024)):
      encodings = tokenizer.encode_batch_fast(t, add_special_tokens=False)
      for e in encodings:
          dataset.append((None, e.ids, None))

  # Build scoring index
  scoring = ScoringFactory.create({"method": "bm25", "terms": True})
  scoring.index(dataset)

  # Calculate mean value of weights array per token
  tokens = np.zeros(tokenizer.get_vocab_size())
  for token in scoring.idf:
    tokens[token] = np.mean(scoring.terms.weights(token)[1])

  return tokens

# Collect paths for training data
paths = sorted(Path("features").glob("*.json"))
texts, vectors = collect_means_and_texts(paths)

# Train the model
model = train_model("neuml/pubmedbert-base-embeddings", texts, vectors)

# Weight the model
weights = tokenweights()

# Remove NaNs from embedding, if any
embedding = np.nan_to_num(model.embedding)

# Apply PCA
embedding = PCA(n_components=embedding.shape[1]).fit_transform(embedding)

# Apply weights
embedding *= weights[:, None]

# Update model embedding and normalize
model.embedding, model.normalize = embedding, True

# Save model
model.save_pretrained("output path")
```

The following table compares the accuracy results for each of the methods

| Model                                                | PubMed QA | PubMed Subset | PubMed Summary | Average   |
| -----------------------------------------------------| --------- | ------------- | -------------- | --------- |
| **pubmedbert-base-embeddings-8M-BM25**               | **90.05** | **94.29**     | **94.15**      | **92.83** |
| pubmedbert-base-embeddings-8M-M2V (No training)      | 69.84     | 70.77         | 71.30          | 70.64     |
| pubmedbert-base-embeddings-8M-SIF                    | 88.75     | 93.78         | 93.05          | 91.86     |

As we can see, the BM25 weighted model has the best results for the evaluated datasets

## Acknowledgement

This model is built on the great work from the [Minish Lab](https://github.com/MinishLab) team consisting of [Stephan Tulkens](https://github.com/stephantul) and [Thomas van Dongen](https://github.com/Pringled).

Read more at the following links.

- [Model2Vec](https://github.com/MinishLab/model2vec)
- [Tokenlearn](https://github.com/MinishLab/tokenlearn)
- [Minish Lab Blog](https://minishlab.github.io/)
