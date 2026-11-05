---
library_name: transformers
tags: []
---

# Model Card for Model ID

<!-- Provide a quick summary of what the model is/does. -->
Sentiment Analysis Model to predict the label from a review given, the labels go from 1 star to 5 stars. 

## Model Details

### Model Description

<!-- Provide a longer summary of what this model is. -->

This is the model card of a 🤗 transformers model that has been pushed on the Hub. This model card has been automatically generated.

- **Language(s) (NLP):** Sentiment Analysis
- **Finetuned from model [optional]:** juliensimon/reviews-sentiment-analysis

### Model Sources [optional]

<!-- Provide the basic links for the model. -->

- **Repository:** https://github.com/ElizaClapa/LLM-Project-LHL.git

## Training Details

### Training Data

<!-- This should link to a Dataset Card, perhaps with a short stub of information on what the training data is all about as well as documentation related to data pre-processing or additional filtering. -->
The *YelpReviewFull* dataset consists of reviews from Yelp. It was constructed by Xiang Zhang (xiang.zhang@nyu.edu) from the Yelp Dataset Challenge 2015. 

It was first used as a text classification benchmark in the following paper:

Xiang Zhang, Junbo Zhao, Yann LeCun. *Character-level Convolutional Networks for Text Classification*. *Advances in Neural Information Processing Systems 28* (NIPS 2015).

The dataset can be found in this Hugging Face [link🔗](https://huggingface.co/datasets/Yelp/yelp_review_full).

#### Preprocessing [optional]

Preprocessing steps include removing punctuation, removing stopwords, lemmatizing and padding. 

#### Training Hyperparameters

## Evaluation

<!-- This section describes the evaluation protocols and provides the results. -->
The performance metrics of the Optimized model were Accuracy, Precission, Recall, and F1-Score.

```
Evaluation Results:
{'eval_loss': 0.773500382900238, 'eval_accuracy': 0.684, 'eval_f1': 0.6833543859772582, 'eval_runtime': 98.6782, 'eval_samples_per_second': 5.067, 'eval_steps_per_second': 0.638}
Classification Report:
              precision    recall  f1-score   support

      1 star       0.79      0.78      0.79       110
      2 star       0.64      0.69      0.66       112
     3 stars       0.70      0.67      0.69        92
     4 stars       0.62      0.56      0.59       100
     5 stars       0.66      0.71      0.68        86

    accuracy                           0.68       500
   macro avg       0.68      0.68      0.68       500
weighted avg       0.68      0.68      0.68       500
```


#### Metrics

<!-- These are the evaluation metrics being used, ideally with a description of why. -->
The Hyperparameters changed for the optimization of this model include the following: 

```
training_args = TrainingArguments(
    output_dir=repo_name,
    learning_rate=2e-5, 
    per_device_train_batch_size=8,  
    per_device_eval_batch_size=8,  
    num_train_epochs=3,
    weight_decay=0.1,
    eval_strategy="epoch",
    save_strategy="epoch",
    load_best_model_at_end=True,
    logging_dir='/content/drive/My Drive/Colab Notebooks/LLM Project GoogleColab/Logs_Full',
    logging_steps=10,
    push_to_hub=True,
    report_to="none"
)

optimized_trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_ds['train'],
    eval_dataset=tokenized_ds['test'],
    #train_dataset=small_train_dataset,
    #eval_dataset=small_eval_dataset,
    tokenizer=tokenizer,
    data_collator=data_collator,
    compute_metrics=compute_metrics,
    callbacks=[EarlyStoppingCallback(early_stopping_patience=1, early_stopping_threshold=0.001)]
)
```

The most important hyperparameter for this optimization was the **Learning Rate**, which had been modified from 5e-1 to 1e-1, and finally set to 2e-5 for the final optimization. A learning rate that's too high can cause the model to converge too quickly to a suboptimal solution, while too low a learning rate can result in slow convergence, resulting in long training times. A compromised between risk of suboptimal performance and training time was found with the final learning rate used (2e-5). 

Another hyperparameter changed was the number of training **Epochs**, which controls how many times the model sees the entire training dataset. Too few epochs may lead to underfitting, while too many can lead to overfitting. To avoid overfitting, a technique called **Early Stopping** was used. This technique is used to halt training when the model's performance on the validation set stops improving. This helps prevent overfitting by ensuring that the model does not continue training beyond the point where it is making significant progress.

Another important consideration was the **Weight Decay** hyperparameter, is it is useful for regularization to avoid overfitting. 

### Hyperparameters important for memory usage and speed

The following hyperparameters helped to avoid losing valuable model training progress due to the Colab Notebook disconecting from the hosted runtime due to inactivity or reaching the maximum RAM available: 
   
1. The **Per Device Evaluation Batch Size** directly affected the speed and memory usage during the evaluation.

2. The **Evaluation Strategy** was set to 'epoch' so the model would be evaluated on the validation set everytime one epoch was completed. 

3. The **Save Strategy** was set to 'epoch' so the models state would be saved with every completed epoch. 

Even if the notebook would disconnect, with the saved model's progress, the training could be restarted from that point. 

### Results
| <p style="text-align: center;">text</p> | <p style="text-align: center;">label</p>|<p style="text-align: center;">score</p>|
|:----------|:----------|:----------|
| This restaurant was the best ever, I really enjoyed the food there!   | 5 stars    | 0.967317    |
| I would recommend this to my family and friends!    | 4 stars     | 0.530670    |
| Not that big of a deal, I don't know what everyone is talking about.   | 3 stars     | 0.626009   |
| It was okay, not that bad, but also not extremely good   | 3 stars    | 0.492008    |
| This was the worst meal I've ever had!   | 1 star    | 0.990348   |
