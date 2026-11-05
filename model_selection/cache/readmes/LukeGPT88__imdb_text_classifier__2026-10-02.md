---
language: "en"
tags:
- distilbert
- sentiment
- positive
- negative 
- review
- imdb
---

# Fine-tuned DistilBERT-base-uncased for IMDB Classification

# Model Description 

DistilBERT is a transformer model that performs sentiment analysis. I fine-tuned the model on IMDB dataset with the purpose of classifying positive reviews from the bad ones. The model predicts these 2 classes. 

The model is a fine-tuned version of [DistilBERT](https://huggingface.co/docs/transformers/model_doc/distilbert).

It was fine-tuned on IMDB dataset [https://huggingface.co/datasets/imdb].

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on IMDB dataset.

It achieves the following results on the evaluation set:
- Loss: 0.2265
- Accuracy: 0.9312

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 2

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.2273        | 1.0   | 1563 | 0.2471          | 0.9122   |
| 0.1524        | 2.0   | 3126 | 0.2265          | 0.9312   |


### Framework versions

- Transformers 4.35.2
- Pytorch 2.1.0+cu121
- Datasets 2.17.0
- Tokenizers 0.15.1

# How to Use 

```python
from transformers import pipeline

classifier = pipeline("text-classification", model="LukeGPT88/imdb_text_classifier")
classifier("I see it and it was awesome.")
```

```python
Output:
[{'label': 'POSITIVE', 'score': 0.9958052635192871}]
```

# Contact

Please reach out to [luca.flammia@gmail.com](luca.flammia@gmail.com) if you have any questions or feedback.
