---
language:
  - ja
license: cc-by-sa-3.0
library_name: transformers
pipeline_tag: text-classification
tags:
  - text-classification
  - financial-sentiment-analysis
  - sentiment-analysis
base_model: cl-tohoku/bert-base-japanese
datasets:
  - financial_phrasebank
metrics:
  - f1
  - accuracy
  - precision
  - recall
widget:
  - text: "売上高は30%増の3,600万ユーロとなった。"
    example_title: "Example 1"
  - text: "ブラックフライデー開幕。店頭プロモーション一覧。"
    example_title: "Example 2"
  - text: "CDPROJEKT株はWSE上場企業の中で最大の下落を記録した。"
    example_title: "Example 3"
model-index:
  - name: finance-sentiment-ja-base
    results:
      - task:
          type: text-classification
          name: Financial Sentiment Analysis
        dataset:
          name: Financial PhraseBank (translated to Japanese)
          type: financial_phrasebank
        metrics:
          - type: f1
            value: 0.959
            name: F1 (macro)
          - type: precision
            value: 0.959
            name: Precision (macro)
          - type: recall
            value: 0.959
            name: Recall (macro)
          - type: accuracy
            value: 0.967
            name: Accuracy
---


# Finance Sentiment JA (base)

Finance Sentiment JA (base) is a model based on [bert-base-japanese](https://huggingface.co/cl-tohoku/bert-base-japanese) for analyzing sentiment of Japanese financial news. It was trained on the translated version of [Financial PhraseBank](https://www.researchgate.net/publication/251231107_Good_Debt_or_Bad_Debt_Detecting_Semantic_Orientations_in_Economic_Texts) by Malo et al. (2014) for 10 epochs on single RTX3090 gpu. 

The model will give you a three labels: positive, negative and neutral.

## How to use

You can use this model directly with a pipeline for sentiment-analysis:

```python
from transformers import pipeline

nlp = pipeline("sentiment-analysis", model="bardsai/finance-sentiment-ja-base")
nlp("売上高は30%増の3,600万ユーロとなった。")
```
```bash
[{'label': 'positive', 'score': 0.9987998807375955}]
```

## Performance
| Metric | Value |
| --- | ----------- |
| f1 macro | 0.959 |
| precision macro | 0.959 |
| recall macro | 0.959 |
| accuracy | 0.967 |
| samples per second | 134.9 |

(The performance was evaluated on RTX 3090 gpu)

## Changelog
- 2023-09-18: Initial release

## License

This model is released under the **[Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0)](https://creativecommons.org/licenses/by-sa/3.0/)** license, inherited from the base model [cl-tohoku/bert-base-japanese](https://huggingface.co/cl-tohoku/bert-base-japanese), which is distributed under CC BY-SA 3.0.

> **ShareAlike requirement:** because the base model is licensed under CC BY-SA, any further derivative of this model must also be distributed under the same license (CC BY-SA 3.0, or a [later compatible CC BY-SA version](https://creativecommons.org/share-your-work/licensing-considerations/compatible-licenses/)).
>
> The base model's pretraining data (Japanese Wikipedia, snapshot 2019-09-01) is itself distributed under CC BY-SA 4.0.

Attribution: bert-base-japanese — Tohoku University NLP Group; Finance Sentiment JA (base) — bards.ai.

## About bards.ai

At bards.ai, we focus on providing machine learning expertise and skills to our partners, particularly in the areas of nlp, machine vision and time series analysis. Our team is located in Wroclaw, Poland. Please visit our website for more information: [bards.ai](https://bards.ai/)

Let us know if you use our model :). Also, if you need any help, feel free to contact us at info@bards.ai
