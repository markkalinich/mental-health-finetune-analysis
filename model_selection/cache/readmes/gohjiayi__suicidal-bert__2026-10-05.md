---
license: mit
language:
- en
base_model:
- google-bert/bert-base-uncased
pipeline_tag: text-classification
---
# Suicidal-BERT
This text classification model predicts whether a sequence of words are suicidal (1) or non-suicidal (0).

## Data
The model was trained on the [Suicide and Depression Dataset](https://www.kaggle.com/nikhileswarkomati/suicide-watch) obtained from Kaggle. The dataset was scraped from Reddit and consists of 232,074 rows equally distributed between 2 classes - suicide and non-suicide.

## Parameters
The model fine-tuning was conducted on 1 epoch, with batch size of 6, and learning rate of 0.00001. Due to limited computing resources and time, we were unable to scale up the number of epochs and batch size.

## Performance
The model has achieved the following results after fine-tuning on the aforementioned dataset:
- Accuracy: 0.9757
- Recall: 0.9669
- Precision: 0.9701
- F1 Score: 0.9685

## How to Use
Load the model via the transformers library:
```
from transformers import AutoTokenizer, AutoModel
tokenizer = AutoTokenizer.from_pretrained("gooohjy/suicidal-bert")
model = AutoModel.from_pretrained("gooohjy/suicidal-bert")
```

## Resources
For more resources, including the source code, please refer to the GitHub repository [gohjiayi/suicidal-text-detection](https://github.com/gohjiayi/suicidal-text-detection/).