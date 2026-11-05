---
language:
- en
- zh
- pl
license: other
license_name: openmdw-1.1
license_link: LICENSE
library_name: sentence-transformers
pipeline_tag: sentence-similarity
tags:
- medical
- biomedical
- clustering
- retrieval
- embeddings
- mteb
- sentence-transformers
base_model: nvidia/Nemotron-3-Embed-8B-BF16
---

# nemotron-3-embed-8b-medical

An embedding model for biomedical and clinical text. It is built for searching the medical
literature, retrieving evidence for clinical and consumer health questions, checking scientific
claims against published work, powering RAG over clinical corpora, and organising large
collections of research by subject.

Mean(Task) 68.80 on MTEB(Medical, v1).

It is built on [nvidia/Nemotron-3-Embed-8B-BF16](https://huggingface.co/nvidia/Nemotron-3-Embed-8B-BF16),
already a strong biomedical retriever. The transformer weights are unchanged from it. What this
model adds is a **clustering head**, a low-rank projection fitted on external PubMed literature
and applied when clustering, worth +10.3 on MedrxivClusteringS2S.v2 and +8.2 on P2P.

## Results

MTEB(Medical, v1), `mteb` 2.18.6.

| Task | Score |
|---|---|
| PublicHealthQA | 90.88 |
| MedicalQARetrieval | 87.16 |
| TRECCOVID | 86.78 |
| TRECCOVID-PL | 85.17 |
| SciFact | 83.33 |
| SciFact-PL | 80.71 |
| CMedQAv2-reranking | 79.91 |
| CUREv1 | 66.92 |
| MedrxivClusteringP2P.v2 | 42.77 &nbsp;*(base 34.62)* |
| NFCorpus | 42.32 |
| MedrxivClusteringS2S.v2 | 41.96 &nbsp;*(base 31.65)* |
| CmedqaRetrieval | 37.64 |
| **Mean(Task)** | **68.80** |

Base figures are the same checkpoint without the head, under the same prompt.

## The clustering head

Embedding spaces are organised for general similarity, so k-means over raw medical embeddings
often groups papers by topic rather than by clinical subject. The head is fitted to correct
that. We grouped PubMed abstracts by clinical subject, 46k for the title head and 25k for the
title and abstract head, reduced the embedding space to 512 dimensions with PCA, then took the
discriminant directions in that reduced space. The PCA step is necessary: LDA at 4096 dimensions
fails on small-sample covariance estimation. The resulting basis is orthonormalised and applied
as a rank-51 projection returning 4096-dimensional vectors, so output shape is unchanged.

## Usage

Needs `transformers>=5.2.0` and `sentence-transformers>=5.4.1`, same as the base model.

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("minetta/nemotron-3-embed-8b-medical")

q = model.encode(["what causes myocarditis?"], prompt_name="query")
d = model.encode(["Myocarditis is an inflammation..."], prompt_name="document")
```

For clustering, apply the head:

```python
import numpy as np
from huggingface_hub import hf_hub_download

h = np.load(hf_hub_download("minetta/nemotron-3-embed-8b-medical",
                            "clustering_head/head_s2s.npz"))
mu, P = h["mu"].astype(np.float32), h["P"].astype(np.float32)

titles = ["Tocilizumab in severe COVID-19 pneumonia",
          "Hypertension prevalence among adults in rural Bangladesh"]
x = model.encode(titles, prompt_name="clustering").astype(np.float32)
z = ((x - mu) @ P.T) @ P
z /= np.maximum(np.linalg.norm(z, axis=1, keepdims=True), 1e-12)
```

`head_s2s.npz` for titles, `head_p2p.npz` for title+abstract. The projection returns
4096-dimensional vectors, so output dimensionality is unchanged.

## Zero-shot

100% zero-shot on MTEB(Medical, v1). No MTEB task dataset, or anything derived from one, was
used at any stage. The head is fitted on external PubMed literature; every document was checked
for n-gram overlap against all twelve evaluation corpora before use. The gate, the counts and
what it removed are in [CONTAMINATION.md](https://huggingface.co/minetta/nemotron-3-embed-8b-medical/blob/main/CONTAMINATION.md).

## Limitations

- The head is fitted for clinical subject categories and is not expected to transfer to
  unrelated taxonomies.
- `default_prompt_name` is `clustering`; pass `prompt_name="document"` when encoding passages.
- Chinese and Polish performance is inherited from the base model.
- Benchmark runs truncate at 4096 tokens, matching the base model's own MTEB configuration.
  The checkpoint accepts 32k, but long documents at large batch sizes will exhaust an 80GB card.
- Scores were produced with `mteb` 2.18.6.

## Acknowledgements

Thanks to NVIDIA for Nemotron-3-Embed-8B-BF16. It is a very capable base model and a
strong starting point for medical work.

---

Built by [minetta.ai](https://minetta.ai)
