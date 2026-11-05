---
license: mit
datasets:
- abhinand/MedEmbed-training-triplets-v1
language:
- en
base_model:
- medicalai/ClinicalBERT
- google-bert/bert-base-uncased
pipeline_tag: question-answering
library_name: adapter-transformers
tags:
- ColBERT
- retrieval
- triplets-learning
- dense-retrieval
- medical
---


# Medical Dense Retriever (Fine-tuned on Triplets)

This is a fine-tuned [medicalai/ClinicalBERT](https://huggingface.co/medicalai/ClinicalBERT) model trained on medical question-answer triplets using the [`abhinand/MedEmbed-training-triplets-v1`](https://huggingface.co/datasets/abhinand/MedEmbed-training-triplets-v1) dataset.



## Dataset

- **Source**: `abhinand/MedEmbed-training-triplets-v1`
- Format: (query, positive passage, negative passage)
- Size: Subsampled to 1000 triplets for demonstration



## Model Architecture

- Based on: `ClinicalBERT` (or similar encoder)
- Uses ColBERT's **late interaction** (MaxSim)
- Trained with triplet loss

## Training Configuration

| Parameter           | Value              | Description |
|--------------------|--------------------|-------------|
| `base_model`        | `medicalai/ClinicalBERT` | Pretrained model used |
| `interaction`       | `colbert`          | Late interaction for dense retrieval |
| `embedding_dim`     | `128`              | Vector dimension per token |
| `similarity`        | `cosine`           | Scoring method |
| `doc_maxlen`        | `256`              | Max length of document input |
| `query_maxlen`      | `32`               | (From config or defaults) |
| `batch_size`        | `32` (global)      | Effective total batch size |
| `per_gpu_batch_size`| `16`               | Because `nranks = 2` |
| `accum_steps`       | `1`                | Gradient accumulation |
| `learning_rate`     | `5e-6`             | Optimizer learning rate |
| `max_steps`         | `500000`           | Training cutoff |
| `warmup_steps`      | `auto`             | Defaults to 10% of total steps |
| `use_ib_negatives`  | `True`             | In-batch negatives for training |
| `use_relu`          | `False`            | Disabled (default for ColBERT) |
| `nbits`             | `4`                | Index compression (Product Quantization) |
| `AMP`               | `True`             | Mixed precision training |
| `gpus`              | `2`                | Multi-GPU training |
| `nranks`            | `2`                | Distributed ranks (1 per GPU) |



## Intended Use

Dense retrieval for:
- Medical Q&A
- Biomedical semantic search
- Clinical decision support



## 🧪 How to Use

shabawak/ClinicalBERT-colbert-finetuned-ragatouille using RAGatouille

ClinicalBERT-colbert-finetuned-ragatouille operates using ColBERT + RAGatouille. To install it along with its dependencies, run:

``` python
pip install -U ragatouille
```

## Using Bio_Clinical_ColBERT-finetuned Without an Index

For in-memory searching, simply:

1. Load the model
2. Encode documents
3. Search using search_encoded_documents()


``` python
from ragatouille import RAGPretrainedModel
RAG = RAGPretrainedModel.from_pretrained("shabawak/ClinicalBERT-colbert-finetuned-ragatouille")

RAG.encode(['document_1', 'document_2', ...])
RAG.search_encoded_documents(query="your search query")
```
- New encode() calls append to the existing collection.
- Clear stored docs with RAG.clear_encoded_docs().

## Indexing Documents

ColBERT's late-interaction retrieval requires indexing first. This step is slow, but retrieval is fast.

``` python
from ragatouille import RAGPretrainedModel  

RAG = RAGPretrainedModel.from_pretrained("shabawak/ClinicalBERT-colbert-finetuned-ragatouille")  
documents = ['document_1', 'document_2', ...]  # Your documents  
RAG.index(name="My_first_index", collection=documents)  
```
- Index files are saved in .ragatouille/colbert/indexes/{index_name} by default.

## Searching an Index

After indexing, querying is straightforward. If reopening a session, load the index first:

``` python
RAG = RAGPretrainedModel.from_index(".ragatouille/colbert/indexes/My_first_index")  
results = RAG.search(query="What is the expected outcome for a patient diagnosed with D-2-hydroxyglutaric aciduria type I?",k=5)
```
- The results include content, relevance scores, rankings, and metadata (if provided).

``` python
[[{'content': 'In April 1984, Miyazaki opened his own office in Suginami Ward, naming it Nibariki.\n\n\n=== Studio Ghibli ===\n\n\n==== Early films (1985–1996) ====\nIn June 1985, Miyazaki, Takahata, Tokuma and Suzuki founded the animation production company Studio Ghibli, with funding from Tokuma Shoten. Studio Ghibli\'s first film, Laputa: Castle in the Sky (1986), employed the same production crew of Nausicaä. Miyazaki\'s designs for the film\'s setting were inspired by Greek architecture and "European urbanistic templates".',
   'score': 25.90448570251465,
   'rank': 1,
   'document_id': 'miyazaki',
   'document_metadata': {'entity': 'person', 'source': 'wikipedia'}},
  {'content': 'Hayao Miyazaki (宮崎 駿 or 宮﨑 駿, Miyazaki Hayao, Japanese: [mijaꜜzaki hajao]; born January 5, 1941) is a Japanese animator, filmmaker, and manga artist. A co-founder of Studio Ghibli, he has attained international acclaim as a masterful storyteller and creator of Japanese animated feature films, and is widely regarded as one of the most accomplished filmmakers in the history of animation.\nBorn in Tokyo City in the Empire of Japan, Miyazaki expressed interest in manga and animation from an early age, and he joined Toei Animation in 1963. During his early years at Toei Animation he worked as an in-between artist and later collaborated with director Isao Takahata.',
   'score': 25.572620391845703,
   'rank': 2,
   'document_id': 'miyazaki',
   'document_metadata': {'entity': 'person', 'source': 'wikipedia'}},
  {'content': 'Glen Keane said Miyazaki is a "huge influence" on Walt Disney Animation Studios and has been "part of our heritage" ever since The Rescuers Down Under (1990). The Disney Renaissance era was also prompted by competition with the development of Miyazaki\'s films. Artists from Pixar and Aardman Studios signed a tribute stating, "You\'re our inspiration, Miyazaki-san!"',
   'score': 24.84041976928711,
   'rank': 3,
   'document_id': 'miyazaki',
   'document_metadata': {'entity': 'person', 'source': 'wikipedia'}}]]

```