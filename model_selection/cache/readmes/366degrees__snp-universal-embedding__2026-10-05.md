---
language: en
library_name: sentence-transformers
tags:
  - emotional-ai
  - reasoning-embedding
  - substrate-prism
  - cognitive-modeling
license: mit
pipeline_tag: feature-extraction
---

# 🧬 SNP-Universal-Embedding  
### *Foundational Step Toward Modeling Human Decision Conflict with the Substrate–Prism Neuron (SNP)*

The **SNP-Universal-Embedding** model represents a reasoning-centric embedding system derived from the **Substrate–Prism Neuron (SNP)** framework.  
Unlike conventional semantic models (OpenAI, SBERT, Cohere), this embedding learns to represent **reflective reasoning, emotional coherence**, and **decision conflict geometry** — the foundation for building **Emotional AI**.

---

## 🧠 Abstract

This model forms the *first operational layer* of the **Substrate–Prism Neuron (SNP)** architecture — an experimental AI neuron designed to model human **decision conflict**, **moral opposition**, and **emotional reasoning**.

While most embeddings capture only word-level semantics, SNP embeddings are trained using:
- **A/B Loss:** enforcing permutation invariance (concept consistency).
- **Mirror Loss:** encoding opposition and moral conflict.
- **Prism Logic:** aligning reasoning layers and emotional axes.

This allows SNP embeddings to simulate both **rational coherence** and **emotional reflection** — a key step toward **modeling emotional intelligence computationally**.

---

## 📊 Experimental Evaluation

The SNP model was benchmarked against five leading semantic models (OpenAI, Cohere, Google, SBERT).  
All were tested across three analytical dimensions: **reasoning divergence**, **semantic variance**, and **emotional coherence.**

### 🧩 Embedding Cosine Similarity Matrix
![Embedding Similarity Matrix](https://huggingface.co/366dEgrees/SNP-Universal-Embedding/blob/main/embedding_matrix.png)

---

### 🧭 PCA Projection — Reasoning Geometry
![PCA Projection](https://huggingface.co/366dEgrees/SNP-Universal-Embedding/blob/main/pca_projection.png)

SNP shows **distinct geometric separation**, indicating that its embedding space encodes **reasoning-based dimensions** rather than surface-level semantic proximity.

---

### 🧮 Centroid Distance & Variance
![Centroid Distance](https://huggingface.co/366dEgrees/SNP-Universal-Embedding/blob/main/centroid_variance.png)

| Metric | Meaning | SNP Result | Industry Avg |
|--------|----------|-------------|---------------|
| **Variance (σ²)** | Intra-cluster compactness | **800.63** | ~10,000 |
| **Centroid Distance (Δ)** | Reasoning space separation | **High (Distinct)** | Moderate |
| **RDI (Reasoning Divergence Index)** | Reasoning uniqueness + coherence | **0.04888** | 0.0044 |

---

### 🧭 Reasoning Spectrum — Divergence vs Coherence
![Reasoning Spectrum](https://huggingface.co/366dEgrees/SNP-Universal-Embedding/blob/main/reasoning_spectrum.png)

SNP exhibits a **10× higher RDI score**, representing far more structured divergence and emotional reasoning coherence.

---

### 🧬 Cognitive Geometry Radar
![Cognitive Geometry Radar](https://huggingface.co/366dEgrees/SNP-Universal-Embedding/blob/main/cognitive_radar.png)

SNP demonstrates a balance of **low variance (tight semantics)** and **high reasoning divergence**, indicating a unique dual encoding capability.

---

### 💓 Cognitive–Emotional Geometry Radar
![Cognitive Emotional Geometry Radar](https://huggingface.co/366dEgrees/SNP-Universal-Embedding/blob/main/emotional_radar.png)

This final radar integrates *Reasoning Divergence (RDI)*, *Semantic Tightness (1/σ²)*, and *Emotional Coherence (ΔAffect)* —  
showing that SNP uniquely aligns *rational and emotional embeddings*.

---

## ✅ Validation Tests Performed

### 🧩 Test 1 — Permutation Invariance (Conceptual Consistency)
- **Goal:** Check if “A doctor was offered a job” ≈ “A job was offered to a doctor.”  
- **Metric:** Intra-event cosine similarity.
- **Result:** SNP maintained >0.98 average similarity across permutations.
- **Conclusion:** SNP understands **concept identity** independent of syntax.

---

### ⚖️ Test 2 — Conflict Opposition (Mirror Logic Validation)
- **Goal:** Detect conceptual opposition (e.g., *“choosing to stay” vs “choosing to leave”*).  
- **Metric:** Triplet Satisfaction Rate — ensuring similarity(A,P) > similarity(A,N).  
- **Result:** SNP scored **91%**, while others averaged ~64%.  
- **Conclusion:** SNP correctly recognizes **moral and decisional polarity** — proof of Mirror Block logic.

---

### 🧠 Test 3 — Structural Retrieval (Prism Block Validation)
- **Goal:** Retrieve reasoning structures (e.g., all “Job Offer” conflicts).  
- **Metric:** Structural Match Rate (Top 5 Nearest Neighbors).  
- **Result:** SNP achieved **84% structural accuracy**, vs ~52% for SBERT/OpenAI.  
- **Conclusion:** SNP generalizes reasoning frames beyond topical similarity.

---

## 🧩 Example Usage
```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("366dEgrees/SNP-Universal-Embedding")

text = "She knows he cheats but stays anyway."
embedding = model.encode([text])
print(embedding.shape)

Citation

If you use this model, please cite:

@article{Ola2025PrismNeuron,
  title={SNP-Universal-Embedding: Foundational Step Toward Modeling Human Decision Conflict with the Substrate–Prism Neuron},
  author={Seun Ola},
  year={2025},
  journal={GitHub Preprint},
  url={https://github.com/PunchNFIT/prism-neuron},
  note={Supplementary analysis for the Substrate–Prism Neuron project}
}

Related Research

Main Paper: Modeling Human Decision Conflict with the Substrate–Prism Neuron (SNP)

Author: Seun Ola

Affiliation: 366 Degree FitTech & Sci Institute

Contact: info@366degreefitresearch.com

Summary

The SNP-Universal-Embedding is not a linguistic model — it is a cognitive model built on emotional and reflective logic.
This foundational work proves that reasoning and emotional alignment can be geometrically represented, forming the basis for next-generation Emotional AI.



