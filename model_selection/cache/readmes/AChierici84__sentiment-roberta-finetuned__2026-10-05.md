---
library_name: transformers
tags:
- sentiment
- reputation
- X
- tweets
- customer
- satisfaction
datasets:
- SemEvalWorkshop/sem_eval_2014_task_1
- AChierici84/sentiment-roberta-finetuned
language:
- en
metrics:
- accuracy
- f1
base_model:
- cardiffnlp/twitter-roberta-base-sentiment-latest
pipeline_tag: text-classification
---

# Sentiment Roberta finetuned for company reputation analysis

This is a RoBERTa-base model trained on SamEval datasets and fine-tuned with customer tweets. 
The main task is sentiment analysis with the TweetEval benchmark.
The original model can de found [here](https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment-latest)
This model is suitable for English. 
**Labels**: 
* 0 > Negative;
* 1 > Neutral;
* 2 > Positive

## Example Pipeline

 ```
from transformers import pipeline
sentiment_task = pipeline("sentiment-analysis", model=model_path, tokenizer=model_path)
sentiment_task("Delivery is late!")
 ```
Output format: Json 

 ```
[{'label': 'Negative', 'score': 0.99836}]
 ```

Test application [here](https://huggingface.co/spaces/AChierici84/companyReputation).


## Model Details

### Model Description

This model is generated to evaluate costumer satisfaction and company reputation.  

- **Developed by:** Anna Chierici
- **Language(s) (NLP):** English
- **Finetuned from model [optional]:** [cardiffnlp/twitter-roberta-base-sentiment-latest](https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment-latest)


## Training Details

### Training Data

SemEval dataset and tweet sent to @AmazonHelp account

### Training Procedure

#### Training Hyperparameters

The following training strategies were implemented:

  * validated at the end of each era
  * checkpoint saving
  * initial learning rate equal to 2e-5
  * training/validation batch size of 16
  * number of epochs 3
  * regularization with weight reduction
  * evaluation of the best model at the end of training
  * additional metrics accuracy and F1