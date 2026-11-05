---
language:
  - fr
license: mit
library_name: transformers
pipeline_tag: text-classification
tags:
  - text-classification
  - financial-sentiment-analysis
  - sentiment-analysis
  - camembert
base_model: camembert-base
datasets:
  - financial_phrasebank
metrics:
  - f1
  - accuracy
  - precision
  - recall
widget:
  - text: "Le chiffre d'affaires net a augmenté de 30 % pour atteindre 36 millions d'euros."
    example_title: "Example 1"
  - text: "Coup d'envoi du vendredi fou. Liste des promotions en magasin."
    example_title: "Example 2"
  - text: "Les actions de CDPROJEKT ont enregistré la plus forte baisse parmi les entreprises cotées au WSE."
    example_title: "Example 3"
model-index:
  - name: finance-sentiment-fr-base
    results:
      - task:
          type: text-classification
          name: Financial Sentiment Analysis
        dataset:
          name: Financial PhraseBank (translated to French)
          type: financial_phrasebank
        metrics:
          - type: f1
            value: 0.963
            name: F1 (macro)
          - type: precision
            value: 0.959
            name: Precision (macro)
          - type: recall
            value: 0.967
            name: Recall (macro)
          - type: accuracy
            value: 0.971
            name: Accuracy
---


# Finance Sentiment FR (base)

Finance Sentiment FR (base) is a model based on [camembert-base](https://huggingface.co/camembert-base) for analyzing sentiment of French financial news. It was trained on the translated version of [Financial PhraseBank](https://www.researchgate.net/publication/251231107_Good_Debt_or_Bad_Debt_Detecting_Semantic_Orientations_in_Economic_Texts) by Malo et al. (2014) for 10 epochs on single RTX3090 gpu. 

The model will give you a three labels: positive, negative and neutral.

## How to use

You can use this model directly with a pipeline for sentiment-analysis:

```python
from transformers import pipeline

nlp = pipeline("sentiment-analysis", model="bardsai/finance-sentiment-fr-base")
nlp("Le chiffre d'affaires net a augmenté de 30 % pour atteindre 36 millions d'euros.")
```
```bash
[{'label': 'positive', 'score': 0.9987998807375955}]
```

## Performance
| Metric | Value |
| --- | ----------- |
| f1 macro | 0.963 |
| precision macro | 0.959 |
| recall macro | 0.967 |
| accuracy | 0.971 |
| samples per second | 140.8 |

(The performance was evaluated on RTX 3090 gpu)

## Changelog
- 2023-09-18: Initial release

## License

This model is released under the **[MIT License](https://opensource.org/licenses/MIT)**, inherited from the base model [camembert-base](https://huggingface.co/camembert-base) (MIT).

Attribution: CamemBERT — Inria, Facebook AI Research; Finance Sentiment FR (base) — bards.ai.

## About bards.ai

At bards.ai, we focus on providing machine learning expertise and skills to our partners, particularly in the areas of nlp, machine vision and time series analysis. Our team is located in Wroclaw, Poland. Please visit our website for more information: [bards.ai](https://bards.ai/)

Let us know if you use our model :). Also, if you need any help, feel free to contact us at info@bards.ai
