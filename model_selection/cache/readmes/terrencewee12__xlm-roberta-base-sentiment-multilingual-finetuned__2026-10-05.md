
---
language:
- en
- ms
- zh
tags:
- sentiment-analysis
- text-classification
- multilingual
license: apache-2.0
datasets:
- tyqiangz/multilingual-sentiments
metrics:
- accuracy
model-index:
- name: xlm-roberta-base-sentiment-multilingual-finetuned
  results:
  - task:
      type: text-classification
      name: Text Classification
    dataset:
      type: tyqiangz/multilingual-sentiments
      name: Multilingual Sentiments
    metrics:
    - type: accuracy
      value: 0.7528205128205128


Baseline Scores:
  Classification Report:
    Negative:
      Precision: 0.6153
      Recall: 0.8292
      F1-score: 0.7064
      Support: 1680
    Neutral:
      Precision: 0.5381
      Recall: 0.3035
      F1-score: 0.3881
      Support: 1443
    Positive:
      Precision: 0.7607
      Recall: 0.7803
      F1-score: 0.7704
      Support: 1752
  Metrics:
    Accuracy:
      Value: 0.6560
      Support: 4875
    Macro Avg:
      Value: 0.6380
      Support: 4875
    Weighted Avg:
      Value: 0.6447
      Support: 4875

Finetuned Scores:
  Classification Report:
    Negative:
      Precision: 0.7487
      Recall: 0.7875
      F1-score: 0.7676
      Support: 1680
    Neutral:
      Precision: 0.6775
      Recall: 0.6216
      F1-score: 0.6484
      Support: 1443
    Positive:
      Precision: 0.8128
      Recall: 0.8276
      F1-score: 0.8201
      Support: 1752
  Metrics:
    Accuracy:
      Value: 0.7528
      Support: 4875
    Macro Avg:
      Value: 0.7463
      Support: 4875
    Weighted Avg:
      Value: 0.7507
      Support: 4875
---

# xlm-roberta-base-sentiment-multilingual-finetuned

## Model description

This is a fine-tuned version of the [cardiffnlp/twitter-xlm-roberta-base-sentiment-multilingual](https://huggingface.co/cardiffnlp/twitter-xlm-roberta-base-sentiment-multilingual) model, trained on the [tyqiangz/multilingual-sentiments](https://huggingface.co/datasets/tyqiangz/multilingual-sentiments) dataset. It's designed for multilingual sentiment analysis in English, Malay, and Chinese.

## Intended uses & limitations

This model is intended for sentiment analysis tasks in English, Malay, and Chinese. It can classify text into three sentiment categories: positive, negative, and neutral.

## Training and evaluation data

The model was trained and evaluated on the [tyqiangz/multilingual-sentiments](https://huggingface.co/datasets/tyqiangz/multilingual-sentiments) dataset, which includes data in English, Malay, and Chinese.

## Training procedure

The model was fine-tuned using the Hugging Face Transformers library.

training_args = TrainingArguments(
    output_dir="./results",
    num_train_epochs=5,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=64,
    warmup_steps=500,
    weight_decay=0.01,
    logging_dir='./logs',
    logging_steps=10,
    evaluation_strategy="epoch",
    save_strategy="epoch",
    load_best_model_at_end=True,
)

## Evaluation results

'eval_accuracy': 0.7528205128205128, 'eval_f1': 0.7511924805177581, 'eval_precision': 0.7506612130427309, 'eval_recall': 0.7528205128205128


## Test Score : 

## Environmental impact

Carbon emissions can be estimated using the [Machine Learning Impact calculator](https://mlco2.github.io/impact#compute) presented in [Lacoste et al. (2019)](https://arxiv.org/abs/1910.09700).


