---
language:
  - pl
license: apache-2.0
library_name: transformers
pipeline_tag: text-classification
tags:
  - text-classification
  - financial-sentiment-analysis
  - sentiment-analysis
  - distiluse
base_model: sentence-transformers/distiluse-base-multilingual-cased-v1
datasets:
  - financial_phrasebank
metrics:
  - f1
  - accuracy
  - precision
  - recall
widget:
  - text: "Sprzedaż netto wzrosła o 30% do 36 mln EUR."
    example_title: "Example 1"
  - text: "Rusza Black Friday. Lista promocji w sklepach."
    example_title: "Example 2"
  - text: "Akcje CDPROJEKT zanotowały największy spadek wśród spółek notowanych na GPW."
    example_title: "Example 3"
model-index:
  - name: finance-sentiment-pl-fast
    results:
      - task:
          type: text-classification
          name: Financial Sentiment Analysis
        dataset:
          name: Financial PhraseBank (translated to Polish)
          type: financial_phrasebank
        metrics:
          - type: f1
            value: 0.933
            name: F1 (macro)
          - type: precision
            value: 0.950
            name: Precision (macro)
          - type: recall
            value: 0.918
            name: Recall (macro)
          - type: accuracy
            value: 0.944
            name: Accuracy
---


# Finance Sentiment PL (fast)

Finance Sentiment PL (fast) is a [distiluse](https://huggingface.co/sentence-transformers/distiluse-base-multilingual-cased-v1)-based model for analyzing sentiment of Polish financial news. It was trained on the translated version of [Financial PhraseBank](https://www.researchgate.net/publication/251231107_Good_Debt_or_Bad_Debt_Detecting_Semantic_Orientations_in_Economic_Texts) by Malo et al. (2014) for 10 epochs on single RTX3090 gpu. 

The model will give you a three labels: positive, negative and neutral.

## How to use

You can use this model directly with a pipeline for sentiment-analysis:

```python
from transformers import pipeline

nlp = pipeline("sentiment-analysis", model="bardsai/finance-sentiment-pl-fast")
nlp("Sprzedaż netto wzrosła o 30% do 36 mln EUR.")
```
```bash
[{'label': 'positive', 'score': 0.9999998807907104}]
```

## Performance
| Metric | Value |
| --- | ----------- |
| f1 macro | 0.933 |
| precision macro | 0.950 |
| recall macro | 0.918 |
| accuracy | 0.944 |
| samples per second | 268.1 |

(The performance was evaluated on RTX 3090 gpu)

## Changelog
- 2022-12-01: Rename the model to finance-sentiment-pl-base
- 2022-11-15: Initial release

## License

This model is released under the **[Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0)**, inherited from the base model [sentence-transformers/distiluse-base-multilingual-cased-v1](https://huggingface.co/sentence-transformers/distiluse-base-multilingual-cased-v1) (Apache 2.0).

Attribution: distiluse-base-multilingual-cased-v1 — Sentence-Transformers (UKP Lab); Finance Sentiment PL (fast) — bards.ai.

## About bards.ai

At bards.ai, we focus on providing machine learning expertise and skills to our partners, particularly in the areas of nlp, machine vision and time series analysis. Our team is located in Wroclaw, Poland. Please visit our website for more information: [bards.ai](https://bards.ai/)

Let us know if you use our model :). Also, if you need any help, feel free to contact us at info@bards.ai
