---
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- depression-detection
- mental-health
- clinical
- contrastive-learning
- generated_from_trainer
- dataset_size:21500
- loss:MultipleNegativesRankingLoss
base_model: sentence-transformers/all-mpnet-base-v2
language: en
license: apache-2.0
pipeline_tag: sentence-similarity
library_name: sentence-transformers
metrics:
- pearson_cosine
- spearman_cosine
model-index:
- name: BDI-batch (sentence-transformers/all-mpnet-base-v2)
  results:
  - task:
      type: semantic-similarity
      name: Depression Symptom Retrieval
    dataset:
      name: eRisk T1 2023-2024 (DepreSym)
      type: depression-symptom-annotations
      size: 21500 sentences
    metrics:
    - type: pearson_cosine
      value: 0.8687
      name: Pearson Cosine
    - type: spearman_cosine
      value: 0.8676
      name: Spearman Cosine
    - type: recall@100
      value: 0.372
      name: Recall@100 (eRisk 2023)
    - type: ndcg@10
      value: 0.947
      name: NDCG@10 (eRisk 2023)
    - type: ndcg@1000
      value: 0.817
      name: NDCG@1000 (eRisk 2023)
---

# BDI-batch: Fine-tuned Sentence Transformers for Depression Symptom Retrieval

## Model Description

**BDI-batch** is a specialized sentence transformer model fine-tuned using contrastive learning for the precise retrieval of sentences related to depression symptoms defined in the Beck Depression Inventory (BDI). This model builds upon `sentence-transformers/all-mpnet-base-v2` and has been optimized to distinguish between closely related depressive symptoms.

Unlike general-purpose sentence embeddings, BDI-batch is specifically designed to capture fine-grained semantic distinctions among the 21 symptoms defined in the BDI clinical questionnaire. The model was trained using a novel in-batch contrastive learning approach that leverages the structure of standardized clinical questionnaires to generate meaningful hard negatives automatically.

### Model Details

- **Architecture**: Dual-encoder (bi-encoder) sentence transformer
- **Base Model**: `sentence-transformers/all-mpnet-base-v2` (384 dimensions)
- **Training Approach**: In-batch contrastive learning with MultipleNegativesRankingLoss
- **Training Data**: DepreSym dataset (~21.5K annotated sentences from social media)
- **Training Framework**: Sentence Transformers
- **Authors**: Marcos Fernández-Pichel and David E. Losada (CiTIUS, USC, Spain)
- **Paper**: "BDI-batch: Leveraging Standardized Clinical Questionnaires for Contrastive Learning in Psychological Marker Retrieval" (Accepted at EMNLP 2025)

## Intended Use

This model is designed for **research and analysis** purposes in mental health informatics. Primary use cases include:

- **Sentence-level symptom retrieval**: Identifying social media posts or text excerpts that are relevant to specific BDI depression symptoms
- **Clinical interpretability**: Supporting computational approaches to depression detection with fine-grained symptom understanding
- **Psychological marker detection**: Retrieval of psychological indicators from user-generated text
- **Mental health monitoring**: As a support tool for researchers and mental health professionals working with social media data

### Not Intended For

- **Direct clinical diagnosis or screening** without expert oversight
- **Real-time monitoring or surveillance** of individuals
- **Automated mental health interventions** without human review
- **Any production healthcare system** without proper validation and regulatory compliance

## Performance

The model shows substantial improvements over baseline sentence embeddings and state-of-the-art retrieval models on two eRisk challenge datasets:

### eRisk T1 2023 Results
| Metric | all-mpnet-base-v2 | BDI-batch | Improvement |
|--------|-------------------|-----------|------------|
| R@100  | 0.291             | 0.372     | +27.8%     |
| NDCG@10| 0.834             | 0.947     | +13.5%     |
| NDCG@1000| 0.698            | 0.817     | +17.0%     |

### eRisk T1 2024 Results
| Metric | all-mpnet-base-v2 | BDI-batch | Improvement |
|--------|-------------------|-----------|------------|
| R@100  | 0.268             | 0.315     | +17.5%     |
| NDCG@10| 0.926             | 0.976     | +5.4%      |
| NDCG@1000| 0.805            | 0.948     | +17.8%     |

### Key Improvements by Symptom

Top-performing symptoms (largest relative improvements):
- **Self-criticality**: ~45% improvement
- **Agitation**: ~40% improvement
- **Loss of Interest**: ~35% improvement
- **Tiredness or Fatigue**: ~30% improvement
- **Punishment Feelings**: ~25% improvement

The model particularly excels at disambiguating between closely related symptoms such as:
- "Sadness" vs. "Crying"
- "Self-dislike" vs. "Pessimism" vs. "Past Failure"
- "Changes in Sleeping Patterns" vs. "Loss of Interest in Sex"
- "Irritability" vs. "Agitation"

## How to Use

### Installation
```bash
pip install sentence-transformers
```

### Basic Usage
```python
from sentence_transformers import util
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('your-username/bdi-batch-all-mpnet-base-v2')

# BDI symptom queries
query = "I feel sad much of the time"  # Sadness symptom

# Sentences to rank
sentences = [
    "I feel so sad that I can't bear it",
    "I feel more irritable than usual",
    "I've been crying a lot lately",
    "I don't enjoy things like I used to"
]

# Encode
query_embedding = model.encode(query, convert_to_tensor=True)
sentence_embeddings = model.encode(sentences, convert_to_tensor=True)

# Compute similarity scores
similarity_scores = util.pytorch_cos_sim(query_embedding, sentence_embeddings)[0]

# Rank by similarity
ranked_results = sorted(
    zip(sentences, similarity_scores), 
    key=lambda x: x[1], 
    reverse=True
)

for sentence, score in ranked_results:
    print(f"{score:.4f} - {sentence}")
```

### Advanced Usage: Batch Processing
```python
# For processing multiple symptom queries
bdi_symptoms = {
    "Sadness": "I feel sad much of the time",
    "Crying": "I cry more than I used to",
    "Pessimism": "I do not expect things to work out for me",
    "Loss of Pleasure": "I don't enjoy things as much as I used to"
}

# Encode corpus
corpus = [
    "I'm always sad and can't find joy in anything",
    "Everything seems hopeless to me",
    "I cry at the smallest things now"
    # ... more sentences from social media corpus
]
corpus_embeddings = model.encode(corpus, convert_to_tensor=True)

# Retrieve relevant sentences per symptom
for symptom_name, symptom_query in bdi_symptoms.items():
    query_embedding = model.encode(symptom_query, convert_to_tensor=True)
    similarity_scores = util.pytorch_cos_sim(query_embedding, corpus_embeddings)[0]
    
    # Get top-k most similar sentences
    top_k_results = util.semantic_search(query_embedding, corpus_embeddings, top_k=10)
```

### Semantic Search
```python
from sentence_transformers import util

query = "I have been thinking about suicide"
corpus = ["Your corpus of sentences here..."]

# Encode query and corpus
query_embedding = model.encode(query, convert_to_tensor=True)
corpus_embeddings = model.encode(corpus, convert_to_tensor=True)

# Perform semantic search
results = util.semantic_search(query_embedding, corpus_embeddings, top_k=10)

# Print results
for result in results[0]:
    print(f"Score: {result['score']:.4f} - {corpus[result['corpus_id']]}")
```

## Training Details

### Contrastive Learning Approach

The model was fine-tuned using a novel **in-batch contrastive learning method** that leverages the structure of the Beck Depression Inventory:

1. **Hard Negative Generation**: Instead of random negatives, the method groups related BDI symptoms and creates contrastive batches containing the most semantically similar symptoms (k=10 symptoms per batch)

2. **Training Signal**: For each BDI symptom, two random responses from the questionnaire are sampled to create positive pairs. Other symptoms in the batch serve as hard negatives, forcing the model to learn fine-grained distinctions.

3. **Loss Function**: `MultipleNegativesRankingLoss` encourages pairs from the same symptom to be close while pushing apart different symptoms in the embedding space.

### Training Configuration
- **Base Model**: sentence-transformers/all-mpnet-base-v2
- **Batch Size**: 10 symptoms per batch
- **Number of Epochs**: 10
- **Learning Rate**: 5e-5
- **Warmup Steps**: 100
- **Hardware**: Single node with NVIDIA RTX 5090 GPU (32GB VRAM)
- **Training Dataset**: DepreSym (~21.5K sentences annotated for 21 BDI symptoms)

### Key Innovation: Clinical Grounding

Unlike synthetic hard negatives generated by LLMs, this method leverages **clinically validated questionnaires**:
- BDI questionnaire responses are designed by experts to be mutually informative
- 21 distinct but sometimes overlapping symptoms ensure meaningful hard negatives
- No labeled data required—pairs are generated automatically from the questionnaire structure

**Result**: The questionnaire-derived pairs significantly outperformed LLM-generated synthetic data (Table 3 in the paper)

## Limitations

### Dataset Limitations
- **Social Media Source**: Training data comes exclusively from social media users, which may not represent all demographics (biased toward younger, online-active populations)
- **Language**: Currently only supports English-language content
- **Geographic/Cultural Scope**: Data may reflect primarily Western contexts

### Model Limitations
- **Clinical Questionnaire Dependency**: The model is optimized for BDI-specific symptom definitions and may not transfer seamlessly to alternative depression assessment tools (PHQ-9, DASS-21, etc.)
- **Fine-grained Overlap**: Some symptoms remain inherently difficult to distinguish (e.g., "Self-dislike" from "Crying"), reflecting real clinical complexity
- **Not for Diagnosis**: Performance metrics measure retrieval accuracy, not clinical validity or diagnostic utility
- **Context Dependence**: Model relies on explicit first-person language to identify relevant sentences; implicit mentions of symptoms may be missed

### Ethical and Practical Constraints
- **Not a Diagnostic Tool**: This model should never be used as a standalone diagnostic instrument. It is intended for research and information retrieval only.
- **Requires Expert Oversight**: Any real-world application must include human review by qualified mental health professionals
- **Privacy Concerns**: Analyzing social media text for mental health signals raises contextual integrity issues; users may not expect their posts to be analyzed this way
- **Dual-Use Risk**: Techniques developed for mental health monitoring could be misused for surveillance or discriminatory profiling

## Benchmarks

### Comparison with Baselines
The model outperforms several well-established baselines:

| Model | R@100 | NDCG@10 | NDCG@1000 |
|-------|-------|---------|-----------|
| BM25 | 0.141 | 0.356 | 0.404 |
| BM25 + Cross-Encoder | 0.141 | 0.704 | 0.446 |
| ANCE | 0.274 | 0.802 | 0.664 |
| all-mpnet-base-v2 | 0.291 | 0.834 | 0.698 |
| Contriever | 0.273 | 0.761 | 0.686 |
| **BDI-batch (ours)** | **0.372** | **0.947** | **0.817** |

### Comparison with eRisk Participants
The model also outperforms specialized systems from the eRisk 2024 challenge:
- AP3CM (best precision): R@100=0.291
- NUS IDS (ensemble approach): R@100=0.294
- **BDI-batch**: R@100=0.315 (eRisk 2024 collection)

## Environmental Impact

Model inference is computationally efficient:
- **Embedding Size**: 384 dimensions (same as base model)
- **Inference Time**: Similar to all-mpnet-base-v2
- **Model Size**: ~438MB (same as base model)
- **GPU Memory Required**: ~2GB for standard batch processing

## Citation

If you use this model, please cite the following paper:

```bibtex
@article{fernandez2026bdi,
  title={BDI-batch: Leveraging Standardized Clinical Questionnaires for Contrastive Learning in Psychological Marker Retrieval},
  author={Fern{\'a}ndez-Pichel, Marcos and Losada, David E.},
  journal={Findings of the 2026 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
  year={2026},
  organization={Association for Computational Linguistics}
}
```

## Model Card Contact

- **Marcos Fernández-Pichel** (marcosfernandez.pichel@usc.es)
- **David E. Losada** (david.losada@usc.es)
- CiTIUS, Universidade de Santiago de Compostela, Spain

## License

This model is licensed under the Apache 2.0 License. The base model (all-mpnet-base-v2) is also distributed under Apache 2.0.


## Additional Resources

- **DepreSym Dataset**: Pérez et al. (2025) - Language Resources and Evaluation
- **eRisk Challenge**: https://erisk.clef.org
- **Beck Depression Inventory**: https://www.ismanet.org/doctoryourspirit/pdfs/Beck-Depression-Inventory-BDI.pdf
- **Sentence Transformers**: https://www.sbert.net

---

**Disclaimer**: This model is provided for research purposes only. It should not be used for clinical diagnosis, treatment recommendations, or real-time monitoring of individuals without proper validation, regulatory compliance, and expert oversight. The authors and their institutions are not responsible for misuse of this model or harm resulting from its application.