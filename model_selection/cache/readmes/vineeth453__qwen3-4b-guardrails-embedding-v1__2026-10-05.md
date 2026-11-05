---
language:
- en
license: apache-2.0
tags:
- sentence-transformers
- embeddings
- qwen3
- lora
- rag
- guardrails
- regulatory
- ai-governance
base_model: Qwen/Qwen3-Embedding-4B
pipeline_tag: sentence-similarity
model-index:
- name: qwen3-4b-guardrails-embedding-v1
  results:
  - task:
      type: information-retrieval
    metrics:
    - type: recall_at_1
      value: 0.9479
      name: Recall@1 (Val)
    - type: recall_at_1
      value: 0.9745
      name: Recall@1 (Test)
    - type: mrr
      value: 0.9732
      name: MRR (Val)
---

# Qwen3-4B Guardrails Embedding v1

Fine-tuned from [Qwen/Qwen3-Embedding-4B](https://huggingface.co/Qwen/Qwen3-Embedding-4B) for **regulatory document retrieval** as part of a Multi-Agent Debate (MAD) Guardrails system developed at SJSU.

This model serves as the retrieval backbone in a RAG pipeline that provides ground truth for agent debates on AI governance and regulatory compliance.

---

## Model Description

| Property | Value |
|---|---|
| Base model | Qwen/Qwen3-Embedding-4B |
| Architecture | Decoder-only (Qwen3), last-token pooling |
| Embedding dimension | 2560 |
| Max sequence length | 512 |
| Fine-tuning method | LoRA (r=16, alpha=32) merged into base |
| Pooling | Last token + L2 normalization |

---

## Training Details

| Parameter | Value |
|---|---|
| Training records | 13,572 synthetic query-chunk pairs |
| Data domain | AI regulatory documents |
| Documents covered | EU AI Act, NIST AI RMF GenAI Profile, NIS2, Cyber Resilience Act, DORA, NIST CSF 2.0, NIST SP 1270 |
| Query types | benign_sensitive, ambiguous, adversarial |
| Loss | MultipleNegativesRankingLoss |
| Hard negatives | 1 per example (mined from rank 6-50 via MiniLM) |
| Epochs | 3 |
| Batch size | 4 (effective 16 with grad accum=4) |
| Learning rate | 1e-4 with cosine decay |
| Warmup ratio | 0.1 |
| LoRA rank | 16 |
| LoRA alpha | 32 |
| LoRA dropout | 0.05 |
| LoRA targets | q_proj, k_proj, v_proj, o_proj, gate_proj, up_proj, down_proj |
| Hardware | NVIDIA A100 SXM4 40GB |
| Training time | ~2.5 hours |

---

## Evaluation Results

Evaluated on a 4-candidate reranking task (1 positive + 3 hard negatives) with 864 val / 864 test samples.

### Overall

| Split | recall@1 | recall@3 | MRR |
|---|---|---|---|
| Validation | 0.9479 | 1.0000 | 0.9732 |
| Test | 0.9745 | 1.0000 | 0.9869 |

### Per Query Type — Validation

| Query Type | recall@1 | recall@3 | MRR |
|---|---|---|---|
| benign_sensitive | 0.9479 | 1.0000 | 0.9734 |
| ambiguous | 0.9583 | 1.0000 | 0.9792 |
| adversarial | 0.9375 | 1.0000 | 0.9670 |

### Per Query Type — Test

| Query Type | recall@1 | recall@3 | MRR |
|---|---|---|---|
| benign_sensitive | 0.9826 | 1.0000 | 0.9913 |
| ambiguous | 0.9826 | 1.0000 | 0.9902 |
| adversarial | 0.9583 | 1.0000 | 0.9792 |

---

## Usage
```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "vineeth453/qwen3-4b-guardrails-embedding-v1",
    trust_remote_code=True
)
model.max_seq_length = 512

# Queries require the instruction prefix
QUERY_INSTRUCTION = (
    "Instruct: Retrieve relevant regulatory passage to answer the query\n"
    "Query: "
)

# Passages are encoded without any prefix
query   = QUERY_INSTRUCTION + "What are the documentation requirements for high-risk AI systems?"
chunks  = [
    "EU AI Act Article 11 requires providers of high-risk AI systems to draw up technical documentation...",
    "NIST AI RMF suggests organizations establish governance structures for AI risk management..."
]

query_emb  = model.encode([query],  normalize_embeddings=True)
chunk_emb  = model.encode(chunks,   normalize_embeddings=True)
scores     = query_emb @ chunk_emb.T
print(scores)
```

> **Important:** Always apply the instruction prefix to queries. Chunks/passages are encoded without any prefix. Consistency between fine-tuning and inference is critical for performance.

---

## Intended Use

- Retrieval in RAG pipelines for AI governance and regulatory compliance
- Ground truth retrieval for multi-agent debate (MAD) systems
- Semantic search over regulatory documents (EU AI Act, NIST frameworks, cybersecurity regulations)

## Out-of-Scope Use

- General-purpose semantic similarity (not optimized for non-regulatory domains)
- Generation tasks
- Classification without a retrieval head

---

## Roadmap

- [ ] Round 2 fine-tuning — r=32, all 3 hard negatives, MNR scale=15, LR=5e-5, 4 epochs
- [ ] Hard negative re-mining using this model as the miner
- [ ] Quantization (GGUF / AWQ) for faster inference
- [ ] Larger eval pool (10-20 candidates for production-realistic metrics)

---

## Project Context

This model is part of the **SJSU Guardrails Project** — a system for evaluating AI agent outputs against regulatory ground truth using Multi-Agent Debate (MAD) orchestration.

Pipeline: User query → RAG retrieval (this model) → Ground truth chunks → Agent debate → Guardrail verdict

---

## License

Apache 2.0 — same as base model.
