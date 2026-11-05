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
datasets:
  - chcaa/fiction4sentiment
  - chcaa/Fiction4EmoBank
base_model: j-hartmann/sentiment-roberta-large-english-3-classes
pipeline_tag: text-classification
model-index:
  - name: sentiment-fiction
    results:
      - task:
          type: text-classification
          name: Sentiment Analysis
        metrics:
          - name: Spearman ρ (Hemingway test, vs. human)
            type: spearman_correlation
            value: 0.7138
          - name: Accuracy (Books test)
            type: accuracy
            value: 0.7819
          - name: Spearman ρ (EmoBank Fiction, vs. human)
            type: spearman_correlation
            value: 0.7538
---

# sentiment-fiction

A RoBERTa-large model finetuned for 3-class sentiment classification (negative / neutral / positive) on literary and fictional text. It is designed for sentence-level sentiment scoring of novels, short stories, and other narrative prose.

## Model description

This model is a finetuned version of [j-hartmann/sentiment-roberta-large-english-3-classes](https://huggingface.co/j-hartmann/sentiment-roberta-large-english-3-classes) (RoBERTa-large, 355M parameters). It was trained on a combined corpus of human-annotated fiction sentences from multiple sources, using class-weighted cross-entropy loss to handle label imbalance.

### Training data

Only human-annotated texts.

| Source | n (train) | Label type |
|--------|-----------|------------|
| Project Gutenberg and Wattpad excerpts | 6,646 | Nine emotions labels → binned to 3 classes |
| EmoBank Fiction (American National Corpus) | 2,164 | Continuous valence → binned to 3 classes |
| Fiction4 Hymns (translated from Danish) | 1,620 | Continuous valence → binned to 3 classes |
| Hemingway — *The Old Man and the Sea* | 1,554 | Continuous 1–10 valence → binned to 3 classes |
| Fiction4 Poetry (Plath) | 1,263 | Continuous valence → binned to 3 classes |
| Fiction4 Fairy Tales (Andersen, translated) | 617 | Continuous valence → binned to 3 classes |
| **Total** | **13,864** | |

Continuous valence scores were binned using the thresholds: ≤4 → negative, (4, 6] → neutral, >6 → positive on a 0–10 scale.

### Intended use

This model is intended for research on literary sentiment, narrative emotion arcs, and computational literary studies. It can be used for:

- Sentence-level sentiment classification of fiction and literary prose
- Generating continuous sentiment arcs by converting class probabilities to a valence score: `valence = p(positive) - p(negative)`
- Comparing sentiment patterns across genres, authors, or narrative structures

## Evaluation

All evaluation sets were held out from training. 
Continuous valence for correlation is computed as `p(positive) − p(negative)` from the model's softmax probabilities, yielding a score in approximately [−1, +1] rather than a discrete class label.
Spearman ρ is computed against continuous human valence annotations where available, or against ordinal 3-class labels.
Accuracy is computed on the 3-class prediction (argmax over negative/neutral/positive) against human valence binned with the same thresholds used for training (≤4 → negative, (4, 6] → neutral, >6 → positive).
Note that literary texts are heavily neutral-skewed, where always predicting "neutral" would do better. For this reason, the continuous valence correlation (Spearman ρ) is the more meaningful metric here.

| Eval set | n | Spearman ρ | Pearson r | Accuracy | Baseline (Syuzhet) |
|----------|---|-----------|-----------|----------|-------------------|
| Hemingway test | 187 | **0.714** | 0.729 | 0.845 | 0.307 |
| Book passages test | 839 | **0.754** | 0.759 | 0.782 | 0.578 |
| EmoBank Fiction | 271 | **0.754** | 0.785 | 0.804 | 0.517 |
| Fiction4 Poetry (Plath) | 158 | **0.723** | 0.768 | 0.791 | 0.473 |
| Fiction4 Fairy Tales (Andersen) | 78 | **0.674** | 0.743 | 0.705 | 0.611 |
| Fiction4 Hymns | 203 | **0.821** | 0.801 | 0.739 | 0.630 |

The Hemingway inter-annotator agreement (Spearman ρ between two human annotators) is 0.543, which the model substantially exceeds on the held-out test set.

The Syuzhet baseline is a dictionary-based method using the Syuzhet lexicon (Jockers, 2015).

### Comparison with base model (v2)

The base model (v2, not released) was finetuned only on Gutenberg and Wattpad passages + Hemingway (8,200 training sentences). This model (v3) adds EmoBank Fiction and Fiction4 subsets (13,864 training sentences).

| Eval set | v3 Spearman ρ | v2 Spearman ρ | Δ |
|----------|--------------|--------------|---|
| Hemingway test | **0.714** | 0.655 | +0.059 |
| EmoBank Fiction | **0.754** | 0.701 | +0.053 |
| Fiction4 Poetry | **0.723** | 0.652 | +0.070 |
| Fiction4 Hymns | **0.821** | 0.785 | +0.036 |
| Fiction4 Fairy Tales | 0.674 | **0.681** | −0.007 |
| Books test | 0.754 | **0.780** | −0.025 |

v3 improves on literary/fiction benchmarks with continuous human annotations. The slight drop on Books test (excerpts with ordinal labels) reflects a trade-off from the more diverse training mix.

### Sequential arc variant: sentiment-fiction-seq

A variant of this model, [fpianz/sentiment-fiction-seq](https://huggingface.co/fpianz/sentiment-fiction-seq), was trained on a modified split where complete sequential texts were held out from training to evaluate detrended sentiment arcs. The training data is slightly reduced (12,929 sentences) because all three Andersen fairy tales and a contiguous block of 400 Hemingway sentences were removed from training and reserved for sequential evaluation.

Detrending follows the nonlinear adaptive filtering method of Hu et al. (2021): the sentiment arc is integrated into a random walk, an adaptive polynomial filter extracts the global trend, and the residuals capture local narrative dynamics. Spearman ρ is computed between the detrended model arc and the detrended human annotation arc.

| Eval set | n | Raw Spearman ρ (Tr) | Raw Spearman ρ (Sy) | Detrended Spearman ρ (Tr) | Detrended Spearman ρ (Sy) |
|----------|---|-----------|-----------|-----------------|-----------------|
| Hemingway — *The Old Man and the Sea* | 400 | 0.712 | 0.465 | **0.781** | 0.335 |
| Andersen — *The Ugly Duckling* | 211 | 0.600 | 0.469 | **0.741** | 0.584 |
| Andersen — *The Little Mermaid* | 293 | 0.654 | 0.523 | **0.754** | 0.624 |
| Andersen — *The Shadow* | 267 | 0.734 | 0.456 | **0.796** | 0.657 |

Tr = Transformer, Sy = Syuzhet lexicon baseline. Detrended values use adaptive filter at window L/8. The Hemingway inter-annotator agreement is Spearman ρ = 0.613.

Detrending consistently improves the transformer's correlation with human annotations (+0.06 to +0.14), indicating that the model captures arc-level narrative dynamics beyond sentence-level sentiment. These results are limited to Andersen fairy tales (translated from Danish) and one Hemingway novella. Users working with other types of fictional text should validate on their own data to determine which model variant (`sentiment-fiction` or `sentiment-fiction-seq`) best fits their use case.

## Usage

```python
from transformers import pipeline

classifier = pipeline("text-classification", model="fpianz/sentiment-fiction")
result = classifier("The old man was thin and gaunt with deep wrinkles in the back of his neck.")
print(result)
# [{'label': 'negative', 'score': 0.82}]
```

For continuous sentiment arcs:

```python
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("fpianz/sentiment-fiction")
model = AutoModelForSequenceClassification.from_pretrained("fpianz/sentiment-fiction")

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
- **Loss:** Class-weighted cross-entropy (weights: negative=1.01, neutral=0.72, positive=1.60)
- **Epochs:** 5 (with early stopping, patience=3)
- **Learning rate:** 2e-5
- **Batch size:** 16
- **Max sequence length:** 512
- **Optimizer:** AdamW (weight decay=0.01, warmup ratio=0.1)
- **Precision:** FP16
- **Hardware:** NVIDIA A100 (University of Groningen Habrok HPC)

## Limitations

- Fiction4 Fairy Tales and Hymns are Google-translated from Danish (Feldkamp et al., 2024); translation artifacts may affect those evaluation scores.
- The 3-class label scheme (negative/neutral/positive) collapses the valence spectrum. The continuous valence conversion (`p(pos) - p(neg)`) provides finer granularity but is an approximation.
- Hemingway sentences constitute ~11% of training data. Evaluation on Hemingway test (held out) is uncontaminated, but the model may be biased toward Hemingway's style.

## References

- [Sentiment Below the Surface: Omissive and Evocative Strategies in Literature and Beyond](https://ceur-ws.org/Vol-3834/paper98.pdf) (Feldkamp et al., CHR 2024)
- [DENS: A Dataset for Multi-class Emotion Analysis](https://aclanthology.org/D19-1656/) (Liu et al., EMNLP-IJCNLP 2019)
- [Comparing Tools for Sentiment Analysis of Danish Literature from Hymns to Fairy Tales: Low-Resource Language and Domain Challenges](https://aclanthology.org/2024.wassa-1.15/) (Feldkamp et al., WASSA 2024)
- [Dynamic evolution of sentiments in *Never Let Me Go*: Insights from multifractal theory and its implications for literary analysis](https://doi.org/10.1093/llc/fqz092) (Hu et al., DSH 2021)

## Citation

*Paper under review — citation will be added upon publication.*
