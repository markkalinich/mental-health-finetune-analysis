---
language:
  - zh
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
  - text: "净销售额增长30%，达到3600万欧元。"
    example_title: "Example 1"
  - text: "黑色星期五拉开帷幕。店内促销活动列表。"
    example_title: "Example 2"
  - text: "CDPROJEKT股价在WSE上市公司中跌幅最大。"
    example_title: "Example 3"
model-index:
  - name: finance-sentiment-zh-fast
    results:
      - task:
          type: text-classification
          name: Financial Sentiment Analysis
        dataset:
          name: Financial PhraseBank (translated to Chinese)
          type: financial_phrasebank
        metrics:
          - type: f1
            value: 0.953
            name: F1 (macro)
          - type: precision
            value: 0.959
            name: Precision (macro)
          - type: recall
            value: 0.949
            name: Recall (macro)
          - type: accuracy
            value: 0.961
            name: Accuracy
---


# Finance Sentiment ZH (fast)

Finance Sentiment ZH (fast) is a [distiluse](https://huggingface.co/sentence-transformers/distiluse-base-multilingual-cased-v1)-based model for analyzing sentiment of Chinese financial news. It was trained on the translated version of [Financial PhraseBank](https://www.researchgate.net/publication/251231107_Good_Debt_or_Bad_Debt_Detecting_Semantic_Orientations_in_Economic_Texts) by Malo et al. (2014) for 10 epochs on single RTX3090 gpu. 

The model will give you a three labels: positive, negative and neutral.

## How to use

You can use this model directly with a pipeline for sentiment-analysis:

```python
from transformers import pipeline

nlp = pipeline("sentiment-analysis", model="bardsai/finance-sentiment-zh-fast")
nlp("净销售额增长30%，达到3600万欧元。")
```
```bash
[{'label': 'positive', 'score': 0.9996095299720764}]
```

## Performance
| Metric | Value |
| --- | ----------- |
| f1 macro | 0.953 |
| precision macro | 0.959 |
| recall macro | 0.949 |
| accuracy | 0.961 |
| samples per second | 264.6 |

(The performance was evaluated on RTX 3090 gpu)

## Changelog
- 2023-07-12: Initial release

## License

This model is released under the **[Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0)**, inherited from the base model [sentence-transformers/distiluse-base-multilingual-cased-v1](https://huggingface.co/sentence-transformers/distiluse-base-multilingual-cased-v1) (Apache 2.0).

Attribution: distiluse-base-multilingual-cased-v1 — Sentence-Transformers (UKP Lab); Finance Sentiment ZH (fast) — bards.ai.

## About bards.ai

At bards.ai, we focus on providing machine learning expertise and skills to our partners, particularly in the areas of nlp, machine vision and time series analysis. Our team is located in Wroclaw, Poland. Please visit our website for more information: [bards.ai](https://bards.ai/)

Let us know if you use our model :). Also, if you need any help, feel free to contact us at info@bards.ai
