---
base_model: sentence-transformers/all-MiniLM-L6-v2
library_name: sentence-transformers
license: apache-2.0
language:
- en
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- medical
- healthcare
- fine-tuned
pipeline_tag: sentence-similarity
---

> **Evaluation notice (2026-10-01).** Training text came from a copyrighted medical encyclopedia; the training code and data splits are not available, so the reported Spearman 0.8039 / +18.31% cannot be reproduced and refers to an in-corpus similarity task. In zero-shot retrieval tests on BEIR SciFact, NFCorpus, TREC-COVID and a MedQuAD question-to-answer task, this model scores far below its base model all-MiniLM-L6-v2 (for example SciFact nDCG@10 0.249 vs 0.645), and its embeddings have a much lower effective rank (27.5 vs 138.5). **We do not recommend it for retrieval.** Not medical advice. Details and code: https://github.com/yogvidwankhede/HealthMate-AI/pull/2

# HealthMate-AI — all-MiniLM-L6-v2 Medical (Best-2 Ensemble)

A [sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) model fine-tuned on medical text for the **HealthMate-AI** project (a medical RAG chatbot). This checkpoint is the **ensemble (weight average) of the 2 best-performing cross-validation folds**.

Maps sentences and paragraphs to a 384-dimensional dense vector space for semantic search and retrieval over medical documents.

## Usage

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("yogvidwankhede/healthmate-minilm-l6-v2-medical-best2")
embeddings = model.encode([
    "What are the symptoms of type 2 diabetes?",
    "Metformin is a first-line medication for type 2 diabetes.",
])
print(embeddings.shape)  # (2, 384)
```

## Training

- Base model: all-MiniLM-L6-v2 (384-dim, 6-layer MiniLM)
- Fine-tuned with 3-fold cross-validation on medical corpus text extracted from medical reference books
- This model averages the weights of the 2 best folds selected by validation performance

## Intended use and limitations

Embedding/retrieval component of a medical RAG system. Research/educational use. **Not a substitute for professional medical advice.**
