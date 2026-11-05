---
tags:
- transformers
- roberta
- sentiment-analysis
- hr
- employee-engagement
- classification
- fine-tuning
license: mit
pipeline_tag: text-classification
library_name: transformers
---

# Employee Sentiment Classifier — DistilRoBERTa (Fine-tuned)

This model is a fine-tuned version of [`j-hartmann/emotion-english-distilroberta-base`](https://huggingface.co/j-hartmann/emotion-english-distilroberta-base) on a custom HR feedback dataset containing employee survey responses.

It is designed to classify text responses into the following sentiment categories:

- **Disengaged**
- **Content**
- **Engaged**
- **At Risk of Leaving**

## Model Details

- **Base Model:** `distilroberta-base` (via j-hartmann's emotion model)
- **Fine-tuned on:** Employee survey feedback
- **Framework:** Hugging Face Transformers
- **Training:** Multi-class classification with W&B sweeps for hyperparameter tuning

## Labels

| Label | Description              |
|-------|--------------------------|
| 0     | Disengaged               |
| 1     | Content                  |
| 2     | Engaged                  |
| 3     | At Risk of Leaving       |

## Evaluation Metrics

Evaluated on a held-out test set of employee reviews:

- **Accuracy:** 91.75%
- **Macro F1 Score:** 91.69%
- **Eval Loss:** 0.380

> These metrics indicate strong generalization on multi-class sentiment prediction in real HR text data.


## 💡 Intended Use

This model is intended for analyzing internal employee sentiment from free-text responses, especially for HR and PeopleOps use cases (e.g. engagement surveys, exit feedback, etc.)

## 👩‍💻 Author

Fine-tuned and maintained by [@yaagni](https://github.com/yaagni-raolji)