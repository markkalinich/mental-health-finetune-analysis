---
language:
  - pl
license: apache-2.0
library_name: transformers
pipeline_tag: text-classification
tags:
  - text-classification
  - twitter
  - emotion
  - distiluse
base_model: sentence-transformers/distiluse-base-multilingual-cased-v1
datasets:
  - tweet_eval
metrics:
  - f1
  - accuracy
  - precision
  - recall
widget:
  - text: "Nigdy przegrana nie sprawiła mi takiej radości. Szczęście i Opatrzność mają znaczenie Gratuluje @pzpn_pl"
    example_title: "Example 1"
  - text: "Osoby z Ukrainy zapłacą za życie w centrach pomocy? Sprzeczne prawem UE, niehumanitarne, okrutne."
    example_title: "Example 2"
model-index:
  - name: twitter-emotion-pl-fast
    results:
      - task:
          type: text-classification
          name: Emotion Classification
        dataset:
          name: TweetEval (translated to Polish)
          type: tweet_eval
        metrics:
          - type: f1
            value: 0.692
            name: F1 (macro)
          - type: precision
            value: 0.700
            name: Precision (macro)
          - type: accuracy
            value: 0.737
            name: Accuracy
---


# Twitter emotion PL (fast)

Twitter emotion PL (fast) is a model based on [distiluse](https://huggingface.co/sentence-transformers/distiluse-base-multilingual-cased-v1) for analyzing emotion of Polish twitter posts. It was trained on the translated version of [TweetEval](https://www.researchgate.net/publication/347233661_TweetEval_Unified_Benchmark_and_Comparative_Evaluation_for_Tweet_Classification) by Barbieri et al., 2020 for 10 epochs on single RTX3090 gpu.

The model will give you a four labels: joy, optimism, sadness and anger.

## How to use

You can use this model directly with a pipeline for text classification:

```python
from transformers import pipeline

nlp = pipeline("text-classification", model="bardsai/twitter-emotion-pl-fast")
nlp("Nigdy przegrana nie sprawiła mi takiej radości. Szczęście i Opatrzność mają znaczenie Gratuluje @pzpn_pl")
```
```bash
[{'label': 'joy', 'score': 0.7068771123886108}]
```

## Performance
| Metric | Value |
| --- | ----------- |
| f1 macro | 0.692 |
| precision macro | 0.700 |
| recall macro | 0.687 |
| accuracy | 0.737 |
| samples per second | 255.2 |


(The performance was evaluated on RTX 3090 gpu)

## Changelog
- 2023-07-19: Initial release

## License

This model is released under the **[Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0)**, inherited from the base model [sentence-transformers/distiluse-base-multilingual-cased-v1](https://huggingface.co/sentence-transformers/distiluse-base-multilingual-cased-v1) (Apache 2.0).

Attribution: distiluse-base-multilingual-cased-v1 — Sentence-Transformers (UKP Lab); Twitter emotion PL (fast) — bards.ai.

## About bards.ai

At bards.ai, we focus on providing machine learning expertise and skills to our partners, particularly in the areas of nlp, machine vision and time series analysis. Our team is located in Wroclaw, Poland. Please visit our website for more information: [bards.ai](https://bards.ai/)

Let us know if you use our model :). Also, if you need any help, feel free to contact us at info@bards.ai
