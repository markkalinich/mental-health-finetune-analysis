---
language: en
license: apache-2.0
tags:
  - text-classification
  - reranking
  - cross-encoder
  - mental-health
  - rag
datasets:
  - nbertagnolli/counsel-chat
metrics:
  - ndcg
pipeline_tag: text-classification
---

# MindLens RAG Reranker (Cross-Encoder)

## Model Description
Cross-encoder fine-tuned from `cross-encoder/ms-marco-MiniLM-L-6-v2` (pre-trained on MS MARCO passage
ranking) on mental-health domain query-passage pairs to re-rank ChromaDB
retrieval results before passage injection into the Groq therapy-response
generator. This is Model 5 in the MindLens five-model NLP pipeline.

## How It Works in MindLens
1. User message arrives at the orchestrator
2. ChromaDB retrieves top-20 candidate passages by cosine similarity
3. This reranker scores each (user message, passage) pair jointly
4. Top-3 ranked passages are injected into Groq Llama 3.3 70B's system prompt
5. Groq generates the therapy response, grounded in the most relevant counselling text

## Training Data
Built from [`nbertagnolli/counsel-chat`](https://huggingface.co/datasets/nbertagnolli/counsel-chat)
using a three-tier pair construction strategy:
- **Tier 1 — Automatic positives**: (question, its own counsellor answer) → label 1
- **Tier 2 — Hard negatives**: (question, answer from a different topic) → label 0
- **Tier 3 — Groq-scored**: (question, same-topic different-answer) scored by
  Groq Llama-3.1-8B as LLM-as-judge (Zheng et al., 2023) → binary label

Training pairs: 3,832 | Val: 479 | Test: 480
Groq-scored ambiguous pairs: 0

## Evaluation Results (held-out test set)
| Metric | Score | Interpretation |
|---|---|---|
| NDCG@3 | 1.0000 | Ranking quality of top-3 results |
| MRR | 1.0000 | How quickly the first relevant passage is found |
| Precision@3 | 0.5833 | Fraction of top-3 results that are relevant |

## Usage
```python
from sentence_transformers import CrossEncoder

reranker = CrossEncoder("AmiruMallawarachchi/mindlens-rag-reranker")

query = "I feel completely hopeless and can't stop crying"
passages = [...]  # top-20 from ChromaDB

scores = reranker.predict([[query, p] for p in passages])
top3_indices = scores.argsort()[::-1][:3]
top3_passages = [passages[i] for i in top3_indices]
```

## Citation
Zheng, L. et al. (2023). Judging LLM-as-a-Judge with MT-Bench and
Chatbot Arena. NeurIPS 2023.
Nogueira, R. & Cho, K. (2019). Passage Re-ranking with BERT.
