---
language:
- en
license: mit  # Example: apache-2.0 or any license from https://huggingface.co/docs/hub/model-repos#list-of-license-identifiers
tags:
- text  # Example: audio
- Twitter
datasets:
- CLPsych 2015  # Example: common_voice. Use dataset id from https://hf.co/datasets
metrics:
- accuracy, f1, precision, recall, AUC # Example: wer. Use metric id from https://hf.co/metrics

model-index:
- name: distilbert-depression-base
  results: []
---

# distilbert-depression-base

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) trained on CLPsych 2015 and evaluated on a scraped dataset from Twitter to detect potential users in Twitter for depression.
It achieves the following results on the evaluation set:
- Evaluation Loss: 0.64
- Accuracy: 0.65
- F1: 0.70
- Precision: 0.61
- Recall: 0.83
- AUC: 0.65


## Intended uses & limitations

Feed a corpus of tweets to the model to generate label if input is indicative of a depressed user or not. Label 1 is depressed, Label 0 is not depressed.

Limitation: All token sequences longer than 512 are automatically truncated. Also, training and test data may be contaminated with mislabeled users.

### How to use

You can use this model directly with a pipeline for sentiment analysis:

```python
>>> from transformers import DistilBertTokenizerFast, AutoTokenizer
>>> tokenizer = AutoTokenizer.from_pretrained('distilbert-base-uncased')
>>> from transformers import DistilBertForSequenceClassification
>>> model = DistilBertForSequenceClassification.from_pretrained(r"distilbert-depression-base")
>>> from transformers import pipeline
>>> classifier = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)
>>> tokenizer_kwargs = {'padding':True,'truncation':True,'max_length':512}
>>> result=classifier('pain peko',**tokenizer_kwargs) #For truncation to apply in the pipeline. 
>>> #Should note that the string passed as the input can be a corpus of tweets concatenated together into one document.

[{'label': 'LABEL_1', 'score': 0.5048992037773132}]
```

Otherwise, download the files and specify within the pipeline the path to the folder that contains the config.json, pytorch_model.bin, and training_args.bin

## Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 3.39e-05
- train_batch_size: 16
- eval_batch_size: 16
- weight_decay: 0.13
- num_epochs: 3.0

## Training results


| Epoch | Training Loss | Validation Loss | Accuracy |    F1    | Precision |  Recall  |    AUC   |
|:-----:|:-------------:|:---------------:|:--------:|:--------:|:---------:|:--------:|:--------:|
| 1.0   | 0.68          | 0.66            | 0.59     | 0.63     | 0.56      | 0.73     | 0.59     |
| 2.0   | 0.60          | 0.68            | 0.63     | 0.69     | 0.59      | 0.83     | 0.63     |
| 3.0   | 0.52          | 0.67            | 0.64     | 0.66     | 0.62      | 0.72     | 0.65     |