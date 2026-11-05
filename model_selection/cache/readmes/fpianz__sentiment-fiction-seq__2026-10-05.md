---
license: mit
language:
  - en
library_name: transformers
tags:
  - sentiment-analysis
  - literary-sentiment
  - roberta
  - text-classification
  - sentiment-arcs
datasets:
  - chcaa/fiction4sentiment
  - chcaa/Fiction4EmoBank
base_model: j-hartmann/sentiment-roberta-large-english-3-classes
pipeline_tag: text-classification
model-index:
  - name: sentiment-fiction-seq
    results:
      - task:
          type: text-classification
          name: Sentiment Analysis
        metrics:
          - name: Spearman ρ (Hemingway arc, detrended, vs. human)
            type: spearman_correlation
            value: 0.7812
          - name: Spearman ρ (Hemingway arc, raw, vs. human)
            type: spearman_correlation
            value: 0.7122
          - name: Spearman ρ (Ugly Duckling, detrended, vs. human)
            type: spearman_correlation
            value: 0.7414
---

# sentiment-fiction-seq

A RoBERTa-large model finetuned for 3-class sentiment classification (negative / neutral / positive) on literary and fictional text, with complete narrative sequences held out from training to enable evaluation of detrended sentiment arcs.

This is a variant of [fpianz/sentiment-fiction](https://huggingface.co/fpianz/sentiment-fiction). The two models share the same architecture, base model, and training procedure. They differ only in their training splits: this model excludes complete sequential texts (three Andersen fairy tales and the final section of Hemingway's *The Old Man and the Sea*) to allow uncontaminated evaluation of narrative arc dynamics. Users should validate both models on their own data to determine which best fits their use case.

## Model description

This model is a finetuned version of [j-hartmann/sentiment-roberta-large-english-3-classes](https://huggingface.co/j-hartmann/sentiment-roberta-large-english-3-classes) (RoBERTa-large, 355M parameters). It was trained on a combined corpus of human-annotated fiction sentences using class-weighted cross-entropy loss to handle label imbalance.

### Training data

Only human-annotated texts. Compared to `sentiment-fiction`, this model excludes all Andersen fairy tale sentences and 400 contiguous Hemingway sentences from training.

| Source | n (train) | Label type |
|--------|-----------|------------|
| Project Gutenberg and Wattpad excerpts | 6,646 | Nine emotions labels → binned to 3 classes |
| EmoBank Fiction (American National Corpus) | 2,164 | Continuous valence → binned to 3 classes |
| Fiction4 Hymns (translated from Danish) | 1,620 | Continuous valence → binned to 3 classes |
| Fiction4 Poetry (Plath) | 1,263 | Continuous valence → binned to 3 classes |
| Hemingway — *The Old Man and the Sea* (first 1,236 sentences) | 1,236 | Continuous 1–10 valence → binned to 3 classes |
| **Total** | **12,929** | |

Continuous valence scores were binned using the thresholds: ≤4 → negative, (4, 6] → neutral, >6 → positive on a 0–10 scale.

### Intended use

This model is intended for research on literary sentiment, narrative emotion arcs, and computational literary studies. It can be used for:

- Sentence-level sentiment classification of fiction and literary prose
- Generating continuous sentiment arcs by converting class probabilities to a valence score: `valence = p(positive) - p(negative)`
- Studying detrended sentiment dynamics in sequential narrative text

## Evaluation

### Sentence-level (raw) correlation

Spearman ρ between model-predicted continuous valence and human annotations, on sequential held-out texts.
Continuous valence for correlation is computed as `p(positive) − p(negative)` from the model's softmax probabilities, yielding a score in approximately [−1, +1] rather than a discrete class label.
Accuracy is computed on the 3-class prediction (argmax over negative/neutral/positive) against human valence binned with the same thresholds used for training (≤4 → negative, (4, 6] → neutral, >6 → positive).
Note that literary texts are heavily neutral-skewed, where always predicting "neutral" would do better. For this reason, the continuous valence correlation (Spearman ρ) is the more meaningful metric here.

| Eval set | n | Spearman ρ (Tr) | Spearman ρ (Sy) | Accuracy | Majority Baseline |
|----------|---|----------------|----------------|---------|---------|
| Hemingway — *The Old Man and the Sea* | 400 | **0.712** | 0.465 | 0.818 | 0.688 |
| Andersen — *The Ugly Duckling* | 211 | **0.600** | 0.469 | 0.668 | 0.692 |
| Andersen — *The Little Mermaid* | 293 | **0.654** | 0.523 | 0.614 | 0.474 |
| Andersen — *The Shadow* | 267 | **0.734** | 0.456 | 0.704 | 0.742 |

Tr = Transformer (this model), Sy = Syuzhet lexicon baseline (Jockers, 2015).

### Detrended arc correlation

Detrending follows Hu et al. (2021): the sentiment arc is integrated into a random walk, a nonlinear adaptive filter extracts the global trend, and the residuals capture local narrative dynamics. Spearman ρ is computed between the detrended model arc and the detrended human annotation arc, at window size L/8.

| Eval set | n | Raw Spearman ρ (Tr) | Detrended Spearman ρ (Tr) | Δ (Tr) | Raw Spearman ρ (Sy) |Detrended Spearman ρ (Sy) |
|----------|---|-----------|-----------------|---|-----|------------|
| Hemingway | 400 | 0.712 | **0.781** | +0.069 | 0.465 | 0.335 |
| *The Ugly Duckling* | 211 | 0.600 | **0.741** | +0.141 | 0.469 | 0.584 |
| *The Little Mermaid* | 293 | 0.654 | **0.754** | +0.100 | 0.523 | 0.624 |
| *The Shadow* | 267 | 0.734 | **0.796** | +0.062 | 0.456 | 0.657 |

Detrending consistently improves the transformer's correlation with human annotations, indicating that the model captures arc-level narrative dynamics beyond sentence-level sentiment. The Hemingway inter-annotator agreement (Spearman ρ between two human annotators) is 0.613 on this subset.

## Usage

```python
from transformers import pipeline

classifier = pipeline("text-classification", model="fpianz/sentiment-fiction-seq")
result = classifier("The old man was thin and gaunt with deep wrinkles in the back of his neck.")
print(result)
# [{'label': 'negative', 'score': 0.82}]
```

For continuous sentiment arcs:

```python
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("fpianz/sentiment-fiction-seq")
model = AutoModelForSequenceClassification.from_pretrained("fpianz/sentiment-fiction-seq")

def valence(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=512)
    with torch.no_grad():
        logits = model(**inputs).logits
    probs = torch.softmax(logits, dim=-1)[0]
    return (probs[2] - probs[0]).item()  # p(positive) - p(negative)

score = valence("He was an old man who fished alone in a skiff in the Gulf Stream.")
print(f"Valence: {score:.3f}")  # range approx [-1, +1]
```

## Training details

- **Base model:** j-hartmann/sentiment-roberta-large-english-3-classes
- **Architecture:** RoBERTa-large (355M parameters)
- **Loss:** Class-weighted cross-entropy (weights: negative=0.99, neutral=0.74, positive=1.56)
- **Epochs:** 5 (with early stopping, patience=3)
- **Learning rate:** 2e-5
- **Batch size:** 16
- **Max sequence length:** 512
- **Optimizer:** AdamW (weight decay=0.01, warmup ratio=0.1)
- **Precision:** FP16
- **Hardware:** NVIDIA A100 (University of Groningen Habrok HPC)

## Limitations

- The detrended arc evaluation is limited to three Andersen fairy tales (translated from Danish) and one section of a Hemingway novella. These results may not generalize to other genres, periods, or languages.
- Fiction4 texts are Google-translated from Danish (Feldkamp et al., 2024); translation artifacts may affect evaluation scores for the fairy tales.
- The 3-class label scheme (negative/neutral/positive) collapses the valence spectrum. The continuous valence conversion (`p(pos) - p(neg)`) provides finer granularity but is an approximation.
- This model has slightly less training data than `sentiment-fiction` (12,929 vs. 13,864 sentences). For sentence-level classification where arc evaluation is not needed, `sentiment-fiction` may be preferable.

## References

- [Sentiment Below the Surface: Omissive and Evocative Strategies in Literature and Beyond](https://ceur-ws.org/Vol-3834/paper98.pdf) (Feldkamp et al., CHR 2024)
- [DENS: A Dataset for Multi-class Emotion Analysis](https://aclanthology.org/D19-1656/) (Liu et al., EMNLP-IJCNLP 2019)
- [Comparing Tools for Sentiment Analysis of Danish Literature from Hymns to Fairy Tales: Low-Resource Language and Domain Challenges](https://aclanthology.org/2024.wassa-1.15/) (Feldkamp et al., WASSA 2024)
- [Dynamic evolution of sentiments in *Never Let Me Go*: Insights from multifractal theory and its implications for literary analysis](https://doi.org/10.1093/llc/fqz092) (Hu et al., DSH 2021)

## Citation

*Paper under review — citation will be added upon publication.*
