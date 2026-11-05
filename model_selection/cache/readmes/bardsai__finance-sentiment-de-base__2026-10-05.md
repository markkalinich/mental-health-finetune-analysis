---
language:
  - de
license: mit
library_name: transformers
pipeline_tag: text-classification
tags:
  - text-classification
  - financial-sentiment-analysis
  - sentiment-analysis
base_model: google-bert/bert-base-german-cased
datasets:
  - financial_phrasebank
metrics:
  - f1
  - accuracy
  - precision
  - recall
widget:
  - text: "Der Nettoumsatz stieg um 30 % auf 36 Mio. EUR."
    example_title: "Example 1"
  - text: "Der schwarze Freitag beginnt. Liste der Werbeaktionen in den Geschäften."
    example_title: "Example 2"
  - text: "Die CDPROJEKT-Aktie verzeichnete den stärksten Rückgang unter den an der WSE notierten Unternehmen."
    example_title: "Example 3"
model-index:
  - name: finance-sentiment-de-base
    results:
      - task:
          type: text-classification
          name: Financial Sentiment Analysis
        dataset:
          name: Financial PhraseBank (translated to German)
          type: financial_phrasebank
        metrics:
          - type: f1
            value: 0.955
            name: F1 (macro)
          - type: precision
            value: 0.960
            name: Precision (macro)
          - type: recall
            value: 0.950
            name: Recall (macro)
          - type: accuracy
            value: 0.966
            name: Accuracy
---


# Finance Sentiment DE (base)

Finance Sentiment DE (base) is a model based on [bert-base-german-cased](https://huggingface.co/bert-base-german-cased) for analyzing sentiment of German financial news. It was trained on the translated version of [Financial PhraseBank](https://www.researchgate.net/publication/251231107_Good_Debt_or_Bad_Debt_Detecting_Semantic_Orientations_in_Economic_Texts) by Malo et al. (2014) for 10 epochs on single RTX3090 gpu. 

The model will give you a three labels: positive, negative and neutral.

## How to use

You can use this model directly with a pipeline for sentiment-analysis:

```python
from transformers import pipeline

nlp = pipeline("sentiment-analysis", model="bardsai/finance-sentiment-de-base")
nlp("Der Nettoumsatz stieg um 30 % auf 36 Mio. EUR.")
```
```bash
[{'label': 'positive', 'score': 0.9987998807375955}]
```

## Performance
| Metric | Value |
| --- | ----------- |
| f1 macro | 0.955 |
| precision macro | 0.960 |
| recall macro | 0.950 |
| accuracy | 0.966 |
| samples per second | 135.2 |

(The performance was evaluated on RTX 3090 gpu)

## Changelog
- 2023-09-18: Initial release

## License

This model is released under the **[MIT License](https://opensource.org/licenses/MIT)**, inherited from the base model [bert-base-german-cased](https://huggingface.co/bert-base-german-cased) (MIT).

Attribution: bert-base-german-cased — deepset; Finance Sentiment DE (base) — bards.ai.

## About bards.ai

At bards.ai, we focus on providing machine learning expertise and skills to our partners, particularly in the areas of nlp, machine vision and time series analysis. Our team is located in Wroclaw, Poland. Please visit our website for more information: [bards.ai](https://bards.ai/)

Let us know if you use our model :). Also, if you need any help, feel free to contact us at info@bards.ai
