---
language:
  - es
license: cc-by-4.0
library_name: transformers
pipeline_tag: text-classification
tags:
  - text-classification
  - financial-sentiment-analysis
  - sentiment-analysis
  - beto
base_model: dccuchile/bert-base-spanish-wwm-cased
datasets:
  - financial_phrasebank
metrics:
  - f1
  - accuracy
  - precision
  - recall
widget:
  - text: "Las ventas netas aumentaron un 30%, hasta 36 millones de euros."
    example_title: "Example 1"
  - text: "Comienza el Black Friday. Lista de promociones en tienda."
    example_title: "Example 2"
  - text: "Las acciones de CDPROJEKT registraron la mayor caída entre las empresas cotizadas en la WSE."
    example_title: "Example 3"
model-index:
  - name: finance-sentiment-es-base
    results:
      - task:
          type: text-classification
          name: Financial Sentiment Analysis
        dataset:
          name: Financial PhraseBank (translated to Spanish)
          type: financial_phrasebank
        metrics:
          - type: f1
            value: 0.973
            name: F1 (macro)
          - type: precision
            value: 0.974
            name: Precision (macro)
          - type: recall
            value: 0.972
            name: Recall (macro)
          - type: accuracy
            value: 0.978
            name: Accuracy
---


# Finance Sentiment ES (base)

Finance Sentiment ES (base) is a model based on [bert-base-spanish-wwm-cased](https://huggingface.co/dccuchile/bert-base-spanish-wwm-cased) for analyzing sentiment of Spanish financial news. It was trained on the translated version of [Financial PhraseBank](https://www.researchgate.net/publication/251231107_Good_Debt_or_Bad_Debt_Detecting_Semantic_Orientations_in_Economic_Texts) by Malo et al. (2014) for 10 epochs on single RTX3090 gpu. 

The model will give you a three labels: positive, negative and neutral.

## How to use

You can use this model directly with a pipeline for sentiment-analysis:

```python
from transformers import pipeline

nlp = pipeline("sentiment-analysis", model="bardsai/finance-sentiment-es-base")
nlp("Las ventas netas aumentaron un 30%, hasta 36 millones de euros.")
```
```bash
[{'label': 'positive', 'score': 0.9987998807375955}]
```

## Performance
| Metric | Value |
| --- | ----------- |
| f1 macro | 0.973 |
| precision macro | 0.974 |
| recall macro | 0.972 |
| accuracy | 0.978 |
| samples per second | 135.1 |

(The performance was evaluated on RTX 3090 gpu)

## Changelog
- 2023-09-18: Initial release

## License

This model is released under the **[Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/)** license, inherited from the base model [dccuchile/bert-base-spanish-wwm-cased](https://huggingface.co/dccuchile/bert-base-spanish-wwm-cased) (BETO, CC BY 4.0).

> **Commercial use caveat (from the BETO authors):** *"The license CC BY 4.0 best describes our intentions for our work. However we are not sure that all the datasets used to train BETO have licenses compatible with CC BY 4.0 (specially for commercial use). Please use at your own discretion and verify that the licenses of the original text resources match your needs."* This caveat is passed through to this derivative model.

Attribution: BETO (bert-base-spanish-wwm-cased) — Cañete et al., Universidad de Chile; Finance Sentiment ES (base) — bards.ai.

## About bards.ai

At bards.ai, we focus on providing machine learning expertise and skills to our partners, particularly in the areas of nlp, machine vision and time series analysis. Our team is located in Wroclaw, Poland. Please visit our website for more information: [bards.ai](https://bards.ai/)

Let us know if you use our model :). Also, if you need any help, feel free to contact us at info@bards.ai
