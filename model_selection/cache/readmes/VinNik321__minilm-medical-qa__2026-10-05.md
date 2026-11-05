
---
library_name: sentence-transformers
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- autotrain
base_model: sentence-transformers/all-MiniLM-L6-v2
widget:
- source_sentence: 'search_query: i love autotrain'
  sentences:
  - 'search_query: huggingface auto train'
  - 'search_query: hugging face auto train'
  - 'search_query: i love autotrain'
pipeline_tag: sentence-similarity
---

# Model Trained Using AutoTrain

- Problem type: Sentence Transformers

## Validation Metrics
loss: 0.2922568619251251

runtime: 9.0068

samples_per_second: 11.547

steps_per_second: 0.777

: 3.0

## Usage

### Direct Usage (Sentence Transformers)

First install the Sentence Transformers library:

```bash
pip install -U sentence-transformers
```

Then you can load this model and run inference.
```python
from sentence_transformers import SentenceTransformer

# Download from the Hugging Face Hub
model = SentenceTransformer("sentence_transformers_model_id")
# Run inference
sentences = [
    'search_query: autotrain',
    'search_query: auto train',
    'search_query: i love autotrain',
]
embeddings = model.encode(sentences)
print(embeddings.shape)

# Get the similarity scores for the embeddings
similarities = model.similarity(embeddings, embeddings)
print(similarities.shape)
```
