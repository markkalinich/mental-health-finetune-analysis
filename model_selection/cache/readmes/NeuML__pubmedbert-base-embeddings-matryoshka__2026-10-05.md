---
pipeline_tag: sentence-similarity
tags:
- sentence-transformers
- feature-extraction
- sentence-similarity
- transformers
language: en
license: apache-2.0
---

# PubMedBERT Embeddings Matryoshka

This is a version of [PubMedBERT Embeddings](https://huggingface.co/NeuML/pubmedbert-base-embeddings) with [Matryoshka Representation Learning](https://arxiv.org/abs/2205.13147) applied. This enables dynamic embeddings sizes of `64`, `128`, `256`, `384`, `512` and the full size of `768`. It's important to note while this method saves space, the same computational resources are used regardless of the dimension size.

Sentence Transformers 2.4 added support for Matryoshka Embeddings. More can be read in [this blog post](https://huggingface.co/blog/matryoshka). 

## Usage (txtai)

This model can be used to build embeddings databases with [txtai](https://github.com/neuml/txtai) for semantic search and/or as a knowledge source for retrieval augmented generation (RAG).

```python
import txtai

# New embeddings with requested dimensionality
embeddings = txtai.Embeddings(
  path="neuml/pubmedbert-base-embeddings-matryoshka",
  content=True,
  dimensionality=256
)
embeddings.index(documents())

# Run a query
embeddings.search("query to run")
```

## Usage (Sentence-Transformers)

Alternatively, the model can be loaded with [sentence-transformers](https://www.SBERT.net).

```python
from sentence_transformers import SentenceTransformer
sentences = ["This is an example sentence", "Each sentence is converted"]

model = SentenceTransformer("neuml/pubmedbert-base-embeddings-matryoshka")
embeddings = model.encode(sentences)

# Requested dimensionality
dimensionality = 256

print(embeddings[:, :dimensionality])
```

## Usage (Hugging Face Transformers)

The model can also be used directly with Transformers. 

```python
from transformers import AutoTokenizer, AutoModel
import torch

# Mean Pooling - Take attention mask into account for correct averaging
def meanpooling(output, mask):
    embeddings = output[0] # First element of model_output contains all token embeddings
    mask = mask.unsqueeze(-1).expand(embeddings.size()).float()
    return torch.sum(embeddings * mask, 1) / torch.clamp(mask.sum(1), min=1e-9)

# Sentences we want sentence embeddings for
sentences = ['This is an example sentence', 'Each sentence is converted']

# Load model from HuggingFace Hub
tokenizer = AutoTokenizer.from_pretrained("neuml/pubmedbert-base-embeddings-matryoshka")
model = AutoModel.from_pretrained("neuml/pubmedbert-base-embeddings-matryoshka")

# Tokenize sentences
inputs = tokenizer(sentences, padding=True, truncation=True, return_tensors='pt')

# Compute token embeddings
with torch.no_grad():
    output = model(**inputs)

# Perform pooling. In this case, mean pooling.
embeddings = meanpooling(output, inputs['attention_mask'])

# Requested dimensionality
dimensionality = 256

print("Sentence embeddings:")
print(embeddings[:, :dimensionality])
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

Evaluation results from the original model are shown below for reference. The [Pearson correlation coefficient](https://en.wikipedia.org/wiki/Pearson_correlation_coefficient) is used as the evaluation metric.

| Model                                                                         | PubMed QA | PubMed Subset | PubMed Summary | Average   |
| ----------------------------------------------------------------------------- | --------- | ------------- | -------------- | --------- | 
| [all-MiniLM-L6-v2](https://hf.co/sentence-transformers/all-MiniLM-L6-v2)           | 90.40     | 95.92         | 94.07          | 93.46     |
| [bge-base-en-v1.5](https://hf.co/BAAI/bge-base-en-v1.5)                            | 91.02     | 95.82         | 94.49          | 93.78     |
| [gte-base](https://hf.co/thenlper/gte-base)                                        | 92.97     | 96.90         | 96.24          | 95.37     |
| [**pubmedbert-base-embeddings**](https://hf.co/neuml/pubmedbert-base-embeddings) | **93.27** | **97.00**     | **96.58**      | **95.62** |
| [S-PubMedBert-MS-MARCO](https://hf.co/pritamdeka/S-PubMedBert-MS-MARCO)            | 90.86     | 93.68         | 93.54          | 92.69     |

See the table below for evaluation results per dimension for `pubmedbert-base-embeddings-matryoshka`.

| Model               | PubMed QA | PubMed Subset | PubMed Summary | Average   |
| --------------------| --------- | ------------- | -------------- | --------- | 
| Dimensions =  64    | 92.16     | 96.14         | 95.67          | 94.66     |
| Dimensions = 128    | 92.80     | 96.58         | 96.22          | 95.20     |
| Dimensions = 256    | 93.11     | 96.82         | 96.53          | 95.49     |
| Dimensions = 384    | 93.42     | 97.00         | 96.61          | 95.68     |
| Dimensions = 512    | 93.37     | 97.07         | 96.61          | 95.68     |
| **Dimensions = 768**    | **93.53**     | **97.13**         | **96.70**          | **95.79**     |

This model performs slightly better overall compared to the original model.

The bigger takeaway is how competitive it is at lower dimensions. For example, `Dimensions = 256` performs better than all the other models originally tested above. Even `Dimensions = 64` performs better than `all-MiniLM-L6-v2` and `bge-base-en-v1.5`.

## Training
The model was trained with the parameters:

**DataLoader**:

`torch.utils.data.dataloader.DataLoader` of length 20191 with parameters:
```
{'batch_size': 24, 'sampler': 'torch.utils.data.sampler.RandomSampler', 'batch_sampler': 'torch.utils.data.sampler.BatchSampler'}
```

**Loss**:

`sentence_transformers.losses.MatryoshkaLoss.MatryoshkaLoss` with parameters:
  ```
  {'loss': 'MultipleNegativesRankingLoss', 'matryoshka_dims': [768, 512, 384, 256, 128, 64], 'matryoshka_weights': [1, 1, 1, 1, 1, 1]}
  ```

Parameters of the fit()-Method:
```
{
    "epochs": 1,
    "evaluation_steps": 500,
    "evaluator": "sentence_transformers.evaluation.EmbeddingSimilarityEvaluator.EmbeddingSimilarityEvaluator",
    "max_grad_norm": 1,
    "optimizer_class": "<class 'torch.optim.adamw.AdamW'>",
    "optimizer_params": {
        "lr": 2e-05
    },
    "scheduler": "WarmupLinear",
    "steps_per_epoch": null,
    "warmup_steps": 10000,
    "weight_decay": 0.01
}
```

## Full Model Architecture
```
SentenceTransformer(
  (0): Transformer({'max_seq_length': 512, 'do_lower_case': False}) with Transformer model: BertModel 
  (1): Pooling({'word_embedding_dimension': 768, 'pooling_mode_cls_token': False, 'pooling_mode_mean_tokens': True, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False, 'pooling_mode_weightedmean_tokens': False, 'pooling_mode_lasttoken': False, 'include_prompt': True})
)
```
