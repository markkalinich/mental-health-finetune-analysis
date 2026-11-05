---
pipeline_tag: sentence-similarity
tags:
- sentence-transformers
- feature-extraction
- sentence-similarity
- transformers
- biomedical
- hpo
- phenotype
- rare-disease
- clinical-nlp
- contrastive-learning
- pubmed
- ijcai
base_model: NeuML/pubmedbert-base-embeddings
language: en
library_name: sentence-transformers
license: mit
datasets:
- custom
metrics:
- pearsonr
- spearmanr
- recall
- mrr
---

# HPO-PubMedBERT — Structure-Aware Biomedical Embeddings

This is a **neuro-symbolic alignment model** that fine-tunes PubMedBERT to bridge the semantic gap between Human Phenotype Ontology (HPO) concepts and clinical literature. It was developed as part of the paper *"Structure-Aware Contrastive Learning for Biomedical Embeddings: Bridging the Gap between HPO and Clinical Literature"* (IJCAI-ECAI 2026).

The model maps biomedical sentences & phenotype descriptions to a 768-dimensional dense vector space optimized for **phenotype similarity** — two embeddings are close when their associated HPO terms are clinically related (share disease annotations), not merely taxonomically adjacent.

Compared to the base PubMedBERT, this model achieves:

- **+9%** Spearman ρ on HPO semantic similarity
- **+99%** Recall@1 on GSC+ gene-disease retrieval
- **4× improvement** in Top-1 accuracy on real-world Phenopacket patient retrieval

---

## Model Description

- **Base Model:** [NeuML/pubmedbert-base-embeddings](https://huggingface.co/NeuML/pubmedbert-base-embeddings)
- **Language:** English (biomedical domain)
- **Maximum Sequence Length:** 256 tokens
- **Output Dimensionality:** 768
- **Pooling:** Mean token embeddings (attention-weighted)
- **Similarity Function:** Cosine similarity
- **Training Data:** 270K sentence pairs from PubMed abstracts mentioning HPO terms, supervised by Disease-Overlap (RBP) similarity scores
- **Loss Function:** [AnglE Loss](https://arxiv.org/abs/2309.12871) (angle-optimized, avoids gradient saturation)
- **Training Strategy:** Discriminative layer-wise learning rates, bottom 6 encoder layers frozen

---

## Usage

### Sentence-Transformers (recommended)

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("Mellandd/hpo_pubmedbert-rbp-angle")
embeddings = model.encode([
    "Abnormality of the nervous system",
    "Seizures and neurodevelopmental delay"
])

# Compute cosine similarity
from sentence_transformers import util
similarity = util.cos_sim(embeddings[0], embeddings[1])
```

### Hugging Face Transformers

```python
from transformers import AutoTokenizer, AutoModel
import torch

def mean_pooling(output, mask):
    embeddings = output[0]
    mask = mask.unsqueeze(-1).expand(embeddings.size()).float()
    return torch.sum(embeddings * mask, 1) / torch.clamp(mask.sum(1), min=1e-9)

tokenizer = AutoTokenizer.from_pretrained("Mellandd/hpo_pubmedbert-rbp-angle")
model = AutoModel.from_pretrained("Mellandd/hpo_pubmedbert-rbp-angle")

sentences = ["Abnormality of the nervous system", "Seizures and neurodevelopmental delay"]
inputs = tokenizer(sentences, padding=True, truncation=True, return_tensors="pt")

with torch.no_grad():
    output = model(**inputs)

embeddings = mean_pooling(output, inputs["attention_mask"])
```

---

## Evaluation Results

### HPO Semantic Textual Similarity (STS)

Pearson and Spearman correlation between model cosine similarity and ground-truth Disease-Overlap (RBP) scores on held-out HPO term pairs:

| Model                  | Spearman ρ | Pearson r |
| ---------------------- | :--------: | :-------: |
| Base PubMedBERT        | 0.770      | 0.889     |
| **This model**         | **0.839**  | **0.939** |

### GSC+ — Mention-to-HPO Linking (228 annotated abstracts, 1,933 annotations)

| Model           | Recall@1 | Recall@5 | MRR   |
| --------------- | :------: | :------: | :---: |
| Base PubMedBERT | 0.131    | 0.290    | 0.209 |
| **This model**  | **0.261**| **0.452**| **0.320** |

### Real-World Phenopacket Patient Retrieval (6,556 clinical cases)

Matching patients by embedding their phenotype profiles:

| Model           | Top-1   | Top-5   | MRR    |
| --------------- | :-----: | :-----: | :----: |
| Base PubMedBERT | 0.042   | 0.114   | 0.110  |
| **This model**  | **0.175**| **0.341**| **0.265** |

---

## Training

### Dataset

Sentence pairs were generated from PubMed abstracts mentioning Human Phenotype Ontology (HPO) terms, with quality filtering including negation detection, enumeration removal, and dynamic context windows (±25 words). Training pairs were formed via **Anchor-Based Hard Sampling**:

- **33% Positive:** different sentences for the same phenotype
- **33% Hard Negative:** terms with moderate RBP similarity (0.3–0.7) — siblings/cousins sharing some diseases
- **33% Random Negative:** low-similarity terms for global structure preservation

Ground-truth similarity scores use the **Disease-Overlap (Relative Best Pair)** metric, which measures shared disease annotations between phenotype terms — capturing clinical co-occurrence rather than mere taxonomic proximity.

### Hyperparameters

| Parameter          | Value                              |
| ------------------ | ---------------------------------- |
| Loss function      | AnglE Loss                         |
| Epochs             | 4                                  |
| Batch size         | 64                                 |
| Evaluation batch   | 256                                |
| Frozen layers      | 6 (embeddings + layers 0-5)        |
| Max learning rate  | 7.87 × 10⁻⁵                        |
| Min learning rate  | 1.00 × 10⁻⁶                        |
| Weight decay       | 0.05                               |
| Warmup ratio       | 6%                                 |
| Max gradient norm  | 1.0                                |
| Optimizer          | AdamW (β₁=0.9, β₂=0.999, ε=1e-6)  |
| Mixed precision    | AMP (CUDA)                         |
| Seed               | 13                                 |

### Discriminative Layer-wise Learning Rates

Bottom 6 layers frozen, top 6 unfrozen with linearly increasing learning rates:

| Layer            | LR        | Parameters |
| ---------------- | :-------: | :--------: |
| encoder.layer.0-5| frozen    | —          |
| encoder.layer.6  | 1.00e-6   | 7.09M      |
| encoder.layer.7  | 1.65e-5   | 7.09M      |
| encoder.layer.8  | 3.21e-5   | 7.09M      |
| encoder.layer.9  | 4.76e-5   | 7.09M      |
| encoder.layer.10 | 6.32e-5   | 7.09M      |
| encoder.layer.11 | 7.87e-5   | 7.09M      |
| pooler           | 7.87e-5   | 0.59M      |

---

## Full Model Architecture

```
SentenceTransformer(
  (0): Transformer({'max_seq_length': 256, 'do_lower_case': False}) with Transformer model: BertModel
  (1): Pooling({'word_embedding_dimension': 768, 'pooling_mode_mean_tokens': True})
)
```

---

## Intended Use

This model is designed for **biomedical phenotype representation and retrieval** tasks:

- Semantic similarity between phenotype descriptions
- Patient-to-disease matching (embedding disease phenotype profiles and querying with patient phenotypes)
- Mention-to-HPO concept normalization
- Document-level phenotype indexing and retrieval

It is **not** intended for general-domain sentence similarity. The model specializes in clinical/biomedical phenotype vocabulary from the HPO.

---

## Limitations and Biases

- **Domain-specific:** Trained exclusively on PubMed biomedical literature and HPO terminology. Performance degrades on general-domain text.
- **Language:** English only.
- **HPO coverage:** Performance correlates with the number of training sentences available per HPO term; rare phenotypes with limited literature mentions may have weaker representations.
- **Sequence length:** Truncated at 256 tokens, suitable for sentences and short paragraphs but not full-length articles.

---

## Citation

TBD - Will update when the IJCAI-ECAI 2026 proceedings are online.
Preprint: [Here](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/AI4H271.pdf)

---

## Dependencies

- [sentence-transformers](https://www.SBERT.net) ≥ 5.1.0
- [transformers](https://github.com/huggingface/transformers) ≥ 4.57.0
- PyTorch ≥ 2.0

## Environment Versions

| Library              | Version |
| -------------------- | :-----: |
| sentence-transformers| 5.1.2   |
| transformers         | 4.57.1  |
| PyTorch              | 2.9.1   |
