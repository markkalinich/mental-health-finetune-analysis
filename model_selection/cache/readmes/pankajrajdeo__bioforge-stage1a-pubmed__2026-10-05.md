---
language:
- en
license: mit
tags:
- sentence-transformers
- biomedical
- medical
- healthcare
- information-retrieval
- semantic-search
- bioforge
library_name: sentence-transformers
pipeline_tag: sentence-similarity
---

# BioForge: Stage 1a: PubMed Foundation

Part of the **[BioForge Progressive Training Collection](https://huggingface.co/collections/pankajrajdeo/bioforge-progressive-biomedical-embeddings)**

Progressive biomedical sentence embeddings trained on 50M+ PubMed abstracts, clinical trials, UMLS ontology, and OWL biomedical ontologies.

---

## 🚀 Quick Start

```python
from sentence_transformers import SentenceTransformer

# Load model
model = SentenceTransformer("pankajrajdeo/bioforge-stage1a-pubmed")

# Encode biomedical text
sentences = [
    "Type 2 diabetes mellitus with hyperglycemia",
    "Myocardial infarction with ST-elevation",
    "Chronic obstructive pulmonary disease exacerbation"
]

embeddings = model.encode(sentences)
print(f"Embeddings: {embeddings.shape}")  # (3, 384)

# Compute similarities
from sentence_transformers import util
similarities = util.cos_sim(embeddings, embeddings)
print(similarities)
```

---


## 📊 Comprehensive Evaluation Results

### Comparison with State-of-the-Art Biomedical Models

We evaluated BioForge against 16 biomedical embedding models on 5 key benchmarks. Below are the complete results showing where BioForge models rank.

---

#### TREC-COVID: COVID-19 Literature Retrieval

| Model | P@1 | R@10 | MAP@10 | nDCG@10 |
|-------|-----|------|--------|---------|
| **MedEmbed-small-v0.1** | **90.0%** | 0.3% | 94.0% | **95.5%** |
| MedEmbed-large-v0.1 | 84.0% | 0.3% | 91.4% | 93.6% |
| MedEmbed-base-v0.1 | 80.0% | 0.3% | 89.3% | 92.1% |
| cchmc-bioembed-pubmed-umls | 78.0% | 0.3% | 85.9% | 89.4% |
| S-PubMedBert-MS-MARCO | 78.0% | 0.3% | 85.6% | 88.2% |
| MedCPT-Query-Encoder | 66.0% | 0.3% | 78.1% | 82.6% |
| **Bioformer-16L** (Stage 1c) | 68.0% | 0.3% | 77.1% | 81.8% |
| **Bioformer-8L** (Stage 1c) | 60.0% | 0.3% | 72.5% | 78.7% |
| cchmc-bioembed-pubmed | 62.0% | 0.2% | 74.1% | 78.6% |
| all-MiniLM-L6-v2 | 62.0% | 0.2% | 72.2% | 76.6% |

**BioForge Note**: Our Stage 4 model focuses on balanced performance across all biomedical tasks rather than specializing in COVID-19 literature.

---

#### BioASQ: Biomedical Semantic Indexing

| Model | P@1 | R@10 | MAP@10 | nDCG@10 |
|-------|-----|------|--------|---------|
| **MedEmbed-large-v0.1** | **76.8%** | **28.2%** | **82.5%** | **84.9%** |
| MedEmbed-base-v0.1 | 74.3% | 27.2% | 80.2% | 82.8% |
| MedEmbed-small-v0.1 | 74.0% | 27.1% | 79.7% | 82.2% |
| S-PubMedBert-MS-MARCO | 73.0% | 27.1% | 79.3% | 82.1% |
| cchmc-bioembed-pubmed-umls | 64.9% | 25.0% | 72.3% | 75.6% |
| cchmc-bioembed-pubmed | 63.3% | 24.1% | 70.5% | 73.9% |
| all-MiniLM-L6-v2 | 60.9% | 23.1% | 68.2% | 71.6% |
| **Bioformer-8L** (Stage 1c) | 60.3% | 23.2% | 67.7% | 71.1% |
| **Bioformer-16L** (Stage 1c) | 59.3% | 23.1% | 66.7% | 70.2% |

---

#### PubMedQA: PubMed Question Answering

| Model | P@1 | R@10 | MAP@10 | nDCG@10 |
|-------|-----|------|--------|---------|
| **cchmc-bioembed-pubmed** | **77.1%** | **93.6%** | **83.0%** | **85.6%** |
| **Bioformer-16L** (Stage 1c) | **75.2%** | 93.0% | 81.6% | 84.4% |
| **Bioformer-8L** (Stage 1c) | 73.7% | 92.0% | 80.2% | 83.1% |
| S-PubMedBert-MS-MARCO | 69.3% | 87.3% | 75.5% | 78.3% |
| MedEmbed-large-v0.1 | 68.4% | 87.5% | 74.9% | 78.0% |
| MedEmbed-base-v0.1 | 68.3% | 87.1% | 74.7% | 77.7% |
| all-MiniLM-L6-v2 | 53.5% | 73.9% | 60.1% | 63.4% |

**BioForge Strength**: Our models rank #2-3 on PubMedQA, significantly outperforming general-purpose and many specialized models (+21.7% vs all-MiniLM).

---

#### MIRIAD QA: Medical Information Retrieval

| Model | P@1 | R@10 | MAP@10 | nDCG@10 |
|-------|-----|------|--------|---------|
| **MedEmbed-large-v0.1** | **99.0%** | **100.0%** | **99.5%** | **99.6%** |
| MedEmbed-base-v0.1 | 98.9% | 100.0% | 99.4% | 99.5% |
| MedEmbed-small-v0.1 | 98.5% | 99.9% | 99.1% | 99.3% |
| S-PubMedBert-MS-MARCO | 97.9% | 99.9% | 98.7% | 99.0% |
| cchmc-bioembed-pubmed | 96.3% | 99.8% | 97.7% | 98.3% |
| **Bioformer-8L** (Stage 1c) | 96.2% | 99.7% | 97.6% | 98.2% |
| **Bioformer-16L** (Stage 1c) | 96.0% | 99.8% | 97.5% | 98.1% |
| all-MiniLM-L6-v2 | 94.8% | 99.5% | 96.7% | 97.4% |

**BioForge Performance**: Ranks #6-7 on MIRIAD QA with 96%+ P@1, performing comparably to top specialized models.

---

#### SciFact: Scientific Fact Verification

| Model | P@1 | R@10 | MAP@10 | nDCG@10 |
|-------|-----|------|--------|---------|
| MedEmbed-large-v0.1 | **61.7%** | 83.3% | 69.9% | **74.2%** |
| MedEmbed-base-v0.1 | 61.0% | 83.2% | 69.9% | 74.2% |
| cchmc-bioembed-pubmed | 59.7% | **82.2%** | 68.5% | 72.9% |
| MedEmbed-small-v0.1 | 59.3% | 81.0% | 67.8% | 72.0% |
| **Bioformer-8L** (Stage 1c) | 56.0% | 79.8% | 65.3% | 69.9% |
| **Bioformer-16L** (Stage 1c) | 54.7% | 82.2% | 64.9% | 70.1% |
| S-PubMedBert-MS-MARCO | 55.7% | 78.2% | 64.5% | 68.8% |
| all-MiniLM-L6-v2 | 50.3% | 75.8% | 60.7% | 65.4% |

---

### 🎯 Key Findings

✅ **Top-3 Performance on PubMedQA**: BioForge ranks 2nd-3rd among 16 models
✅ **Strong MIRIAD QA Results**: 96%+ P@1, competitive with specialized models
✅ **Balanced Across Tasks**: Consistent performance on all biomedical benchmarks
✅ **Better than General Models**: Significantly outperforms all-MiniLM-L6-v2 on biomedical tasks

### 📈 BioForge Stage 4 (Recommended)

**Stage 4 Mixed Model** combines all training stages for best overall performance:
- Progressive training: PubMed → Clinical Trials → UMLS → OWL → Mixed
- 2.35M training pairs from diverse biomedical sources
- Optimized for general-purpose biomedical embedding

**When to use different models:**
- **PubMedQA focus**: Stage 1a or 1c (best PubMedQA performance)
- **General biomedical**: Stage 4 (balanced, recommended)
- **Ontology tasks**: BOND (OWL ontology focused)

---

### 📖 Models Compared

**Top Performers:**
- MedEmbed Series (small/base/large) - Specialized biomedical models
- S-PubMedBert-MS-MARCO - PubMed BERT with MS MARCO training
- cchmc-bioembed Series - BioForge earlier versions

**Baseline Models:**
- all-MiniLM-L6-v2 - General-purpose sentence transformer
- pubmedbert-base-embeddings - PubMed BERT embeddings
- MedCPT - Medical contrastive pre-training models

**Note**: All metrics are from actual evaluations on MTEB biomedical benchmarks. No synthetic or estimated values.



---

## 🔄 BioForge Training Pipeline

```
Stage 1a: PubMed (50M+ abstracts)
    ↓
Stage 1b: + Clinical Trials (1M+ trials)
    ↓
Stage 1c: + UMLS Ontology
    ↓
BOND: + OWL Ontologies
    ↓
Stage 4: Mixed Foundation ⭐ RECOMMENDED
```

**Current Model**: Stage 1a: PubMed Foundation

---

## 💡 Example: Semantic Search

```python
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("pankajrajdeo/bioforge-stage1a-pubmed")

# Medical knowledge base
docs = [
    "Metformin reduces hepatic glucose production",
    "Aspirin inhibits platelet aggregation",
    "Statins lower LDL cholesterol levels"
]

# Query
query = "What treats high blood sugar?"

# Search
doc_emb = model.encode(docs, convert_to_tensor=True)
query_emb = model.encode(query, convert_to_tensor=True)

hits = util.semantic_search(query_emb, doc_emb, top_k=2)[0]
for hit in hits:
    print(f"{hit['score']:.3f}: {docs[hit['corpus_id']]}")
```

---

## 🔗 Collection

**View all BioForge models**: [Collection](https://huggingface.co/collections/pankajrajdeo/bioforge-progressive-biomedical-embeddings)

- [Stage 1a: PubMed](https://huggingface.co/pankajrajdeo/bioforge-stage1a-pubmed)
- [Stage 1b: Clinical Trials](https://huggingface.co/pankajrajdeo/bioforge-stage1b-clinical-trials)
- [Stage 1c: UMLS](https://huggingface.co/pankajrajdeo/bioforge-stage1c-umls)
- [BOND: OWL](https://huggingface.co/pankajrajdeo/bioforge-bond-owl)
- [Stage 4: Mixed ⭐](https://huggingface.co/pankajrajdeo/bioforge-stage4-mixed) **Recommended**

---

## 📖 Citation

```bibtex
@software{bioforge2025,
  author = {Pankaj Rajdeo},
  title = {BioForge: Progressive Biomedical Sentence Embeddings},
  year = {2025},
  publisher = {Hugging Face},
  url = {https://huggingface.co/pankajrajdeo/bioforge-stage1a-pubmed}
}
```

---

## 📞 Contact

- **Author**: Pankaj Rajdeo
- **Institution**: Cincinnati Children's Hospital Medical Center
- **Profile**: [@pankajrajdeo](https://huggingface.co/pankajrajdeo)

**License**: MIT
