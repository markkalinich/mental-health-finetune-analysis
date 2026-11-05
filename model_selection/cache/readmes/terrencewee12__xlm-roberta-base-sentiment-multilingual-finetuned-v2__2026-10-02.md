
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
- scfengv/TVL_Sentiment_Analysis
- argilla/twitter-coronavirus
metrics:
- accuracy
model-index:
- name: xlm-roberta-base-sentiment-multilingual-finetuned
  results:
  - task:
      type: text-classification
      name: Text Classification
    metrics:
    - type: accuracy
      value: 0.8444
---
# xlm-roberta-base-sentiment-multilingual-finetuned

## Model description

This is a fine-tuned version of the [cardiffnlp/twitter-xlm-roberta-base-sentiment-multilingual](https://huggingface.co/cardiffnlp/twitter-xlm-roberta-base-sentiment-multilingual) model, trained on the [tyqiangz/multilingual-sentiments](https://huggingface.co/datasets/tyqiangz/multilingual-sentiments) dataset. It's designed for multilingual sentiment analysis in English, Malay, and Chinese.

## Intended uses & limitations

This model is intended for sentiment analysis tasks in English, Malay, and Chinese. It can classify text into three sentiment categories: positive, negative, and neutral.

## Training and evaluation data

The model was trained and evaluated on the [tyqiangz/multilingual-sentiments](https://huggingface.co/datasets/tyqiangz/multilingual-sentiments)[TVL_Sentiment_Analysis](https://huggingface.co/datasets/scfengv/TVL_Sentiment_Analysis) , [argilla/twitter-coronavirus](https://huggingface.co/datasets/argilla/twitter-coronavirus) datasets, which includes data in English, Malay, and Chinese.

## Training procedure

The model was fine-tuned using the Hugging Face Transformers library.

training_args = TrainingArguments(
    output_dir="./results",
    num_train_epochs=2,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=64,
    warmup_steps=500,
    weight_decay=0.01,
    logging_dir='./logs',
    logging_steps=10,
    evaluation_strategy="steps",
    save_strategy="steps",
    load_best_model_at_end=True,
)

## Evaluation results

Test results: {'eval_loss': 0.5881872177124023, 'eval_accuracy': 0.8443683409436834, 'eval_f1': 0.8438625655671501, 'eval_precision': 0.8438352235376211, 'eval_recall': 0.8443683409436834}

## Environmental impact

Carbon emissions can be estimated using the [Machine Learning Impact calculator](https://mlco2.github.io/impact#compute) presented in [Lacoste et al. (2019)](https://arxiv.org/abs/1910.09700).

