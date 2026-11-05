---
library_name: transformers
license: mit
base_model: dbmdz/bert-base-turkish-cased
tags:
- generated_from_trainer
- sentiment
- turkish
metrics:
- accuracy
- precision
- recall
- f1
model-index:
- name: turkish-sentiment
  results: []
datasets:
- winvoker/turkish-sentiment-analysis-dataset
language:
- tr
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# turkish-sentiment

This model is a fine-tuned version of [dbmdz/bert-base-turkish-cased](https://huggingface.co/dbmdz/bert-base-turkish-cased) on winvoker/turkish-sentiment-analysis-dataset dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0880
- Accuracy: 0.9688
- F1 Macro: 0.9454
- F1 Weighted: 0.9685
- Precision: 0.9683
- Recall: 0.9688

## Model description

A BERT-based(dbmdz Turkish BERT) model fine-tuned on a large-scale Turkish sentiment analysis dataset. This model classifies Turkish text into three sentiment classes: Negative, Notr (Neutral), and Positive.


- Model type: BertForSequenceClassification
- Base model: dbmdz/bert-base-turkish-cased
- Language(s): Turkish

## Intended uses & limitations

- Turkish text classification tasks involving sentiment analysis.
- Suitable for social media data, product reviews, or general-purpose sentiment detection in Turkish.

## Usage

```python
# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("text-classification", model="kaixkhazaki/turkish-sentiment")


pipe("Kargo geç geldi ve ürün beklentimi pek karşılamadı.")
>> [{'label': 'Negative', 'score': 0.984860897064209}]

pipe("Yemek lezzetliydi ancak servis yavaş ve çalışanlar ilgisizdi, pek anlayamadım nasıl hissettiğimi.")
>> [{'label': 'Notr', 'score': 0.9881975054740906}]

pipe("Gerçekten müthiş bir deneyimdi, keşke hep burda kalabilsem.")
>> [{'label': 'Positive', 'score': 0.9942901134490967}]

```

## Training and evaluation data

Fine-tuned on a combined dataset with 440,679 training samples and 48,965 validation samples.

## Training procedure

Trained on using the entire dataset on a single gpu for apx. 25 mins(1600 steps).

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 3e-05
- train_batch_size: 64
- eval_batch_size: 128
- seed: 42
- optimizer: Use adamw_torch with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: cosine
- lr_scheduler_warmup_steps: 400
- training_steps: 1600

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Accuracy | F1 Macro | F1 Weighted | Precision | Recall |
|:-------------:|:------:|:----:|:---------------:|:--------:|:--------:|:-----------:|:---------:|:------:|
| 0.3538        | 0.0581 | 400  | 0.1162          | 0.9582   | 0.9243   | 0.9568      | 0.9572    | 0.9582 |
| 0.1131        | 0.1162 | 800  | 0.1034          | 0.9639   | 0.9369   | 0.9635      | 0.9633    | 0.9639 |
| 0.1026        | 0.1743 | 1200 | 0.0940          | 0.9649   | 0.9411   | 0.9652      | 0.9657    | 0.9649 |
| 0.0936        | 0.2324 | 1600 | 0.0880          | 0.9688   | 0.9454   | 0.9685      | 0.9683    | 0.9688 |


### Framework versions

- Transformers 4.48.0.dev0
- Pytorch 2.4.1+cu121
- Datasets 3.1.0
- Tokenizers 0.21.0

### Citation
```bibtex
@misc{turkish-sentiment,
  title={Turkish Sentiment Analysis using Turkish BERT},
  author={Fatih Demrici},
  year={2025},
  howpublished={\url{https://huggingface.co/kaixkhazaki/turkish-sentiment}},
}
```