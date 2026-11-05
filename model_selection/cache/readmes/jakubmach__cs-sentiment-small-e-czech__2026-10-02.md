---
language:
- cs
license: cc-by-4.0
tags:
- text-classification
- sentiment-analysis
- czech
- electra
datasets:
- fewshot-goes-multilingual/cs_csfd-movie-reviews
pipeline_tag: text-classification
---

# Czech Sentiment Classifier — Small-E-Czech v1 (Experiment 1)

Fine-tuned [Seznam/small-e-czech](https://huggingface.co/Seznam/small-e-czech) for 3-class Czech movie review sentiment.

**⚠️ This is experiment 1.** The improved model is [jakubmach/cs-sentiment-small-e-czech-v2](https://huggingface.co/jakubmach/cs-sentiment-small-e-czech-v2).

| Metric | This model (v1) | v2 (best) |
|--------|:---:|:---:|
| Accuracy | 60.8% | **67.7%** |
| F1 (macro) | 0.421 | **0.488** |
| F1 (weighted) | 0.542 | **0.619** |

Training: lr=5e-5, 3 epochs, 1,500 training samples.
