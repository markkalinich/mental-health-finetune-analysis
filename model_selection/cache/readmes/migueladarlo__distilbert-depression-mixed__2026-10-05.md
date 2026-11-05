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
- name: distilbert-depression-mixed
  results: []
---

# distilbert-depression-mixed

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) trained on CLPsych 2015 and a scraped dataset, and evaluated on a scraped dataset from Twitter to detect potential users in Twitter for depression.
It achieves the following results on the evaluation set:
- Evaluation Loss: 0.71
- Accuracy: 0.63
- F1: 0.59
- Precision: 0.66
- Recall: 0.53
- AUC: 0.63


## Intended uses & limitations

Feed a corpus of tweets to the model to generate label if input is indicative of a depressed user or not. Label 1 is depressed, Label 0 is not depressed.

Limitation: All token sequences longer than 512 are automatically truncated. Also, training and test data may be contaminated with mislabeled users.

### How to use

You can use this model directly with a pipeline for sentiment analysis:

```python
>>> from transformers import DistilBertTokenizerFast, AutoTokenizer
>>> tokenizer = AutoTokenizer.from_pretrained('distilbert-base-uncased')
>>> from transformers import DistilBertForSequenceClassification
>>> model = DistilBertForSequenceClassification.from_pretrained(r"distilbert-depression-mixed")
>>> from transformers import pipeline
>>> classifier = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)
>>> tokenizer_kwargs = {'padding':True,'truncation':True,'max_length':512}
>>> result=classifier('pain peko',**tokenizer_kwargs) #For truncation to apply in the pipeline
>>> #Should note that the string passed as the input can be a corpus of tweets concatenated together into one document.


[{'label': 'LABEL_1', 'score': 0.5048992037773132}]
```

Otherwise, download the files and specify within the pipeline the path to the folder that contains the config.json, pytorch_model.bin, and training_args.bin

## Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 4.19e-05
- train_batch_size: 16
- eval_batch_size: 16
- weight_decay: 0.06
- num_epochs: 5.0

## Training results


| Epoch | Training Loss | Validation Loss | Accuracy |    F1    | Precision |  Recall  |    AUC   |
|:-----:|:-------------:|:---------------:|:--------:|:--------:|:---------:|:--------:|:--------:|
| 1.0   | 0.68          | 0.66            | 0.61     | 0.54     | 0.60      | 0.50     | 0.60     |
| 2.0   | 0.65          | 0.65            | 0.63     | 0.49     | 0.70      | 0.37     | 0.62     |
| 3.0   | 0.53          | 0.63            | 0.66     | 0.58     | 0.69      | 0.50     | 0.65     |
| 4.0   | 0.39          | 0.66            | 0.67     | 0.61     | 0.69      | 0.54     | 0.67     |
| 5.0   | 0.27          | 0.72            | 0.65     | 0.61     | 0.63      | 0.60     | 0.64     |