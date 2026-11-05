---
license: mit
datasets:
- tyqiangz/multilingual-sentiments
- cardiffnlp/tweet_sentiment_multilingual
- mteb/tweet_sentiment_multilingual
- Sp1786/multiclass-sentiment-analysis-dataset
- stanfordnlp/sst2
- statmt/cc100
language:
- en
- de
- es
- fr
- ja
- zh
- id
- ar
- hi
- it
- ms
- pt
metrics:
- accuracy
- f1
base_model:
- microsoft/mdeberta-v3-base
tags:
- sentiment
---

# Model 

Multi-language sentiment classification model developed over the multi-language Microsoft [mDeBERTa-v3 base model](https://huggingface.co/microsoft/mdeberta-v3-base). 
This model where originally trained over CC100 multi-lingual dataset with more that 100+ languages. In this repo we provide fine-tuned model towards the multi-language sentiment analysis.
Model where trained on mulitple datasets with multiple languages with additional weights over class (sentiment categories: Negative, Positive, Neutral).
In order to train the model the following dataset where used:
 - tyqiangz/multilingual-sentiments
 - cardiffnlp/tweet_sentiment_multilingual
 - mteb/tweet_sentiment_multilingual
 - Sp1786/multiclass-sentiment-analysis-dataset
 - ABSC amazon review
 - SST2

# Model parameters

Defined training arguments:
```python
TrainingArguments(
        label_smoothing_factor=0.1,  # Add label smoothing
        evaluation_strategy="epoch",
        greater_is_better=True,
        # Adding weight decay
        weight_decay=0.02,
        num_train_epochs=10,
        learning_rate=5e-6,  # 1e-5,
        optim="adamw_torch",
        adam_beta1=0.9,
        adam_beta2=0.999,
        adam_epsilon=1e-6,
        max_grad_norm=0.5,  # 1.0, # clipping
        lr_scheduler_type='cosine',
        per_device_train_batch_size=48,
        per_device_eval_batch_size=48,
        gradient_accumulation_steps=1,
        gradient_checkpointing=True,
        warmup_ratio=0.1,
        fp16=False,
        logging_strategy="epoch",
        save_strategy="epoch",
        metric_for_best_model="f1",
        save_total_limit=3,
    )
```
Additionaly dropout where changed to:
```python
model.config.classifier_dropout = 0.3  # Set classifier dropout rate
model.config.hidden_dropout_prob = 0.2  # Add hidden layer dropout
model.config.attention_probs_dropout_prob = 0.2  # Add attention dropout
```

Also in order to improve model generalization we make custom compute loss with focal loss function and pre-computed class weights:
```python
def compute_loss(self, model, inputs, return_outputs=False, num_items_in_batch=None):
        labels = inputs.pop("labels")
        labels = labels.to(model.device)
        # forward pass
        outputs = model(**inputs)
        logits = outputs.logits.float()
        logits = logits.to(model.device)
        # compute custom loss
        loss = torch.nn.CrossEntropyLoss(weight=self.tensor_class_w, reduction='none')
        loss = loss.to(model.device)
        if self.tensor_class_w is not None:
            """In case of imbalance data compute focal loss"""
            loss = loss(logits.view(-1, self.model.config.num_labels), labels.view(-1))
            pt = torch.exp(-loss)
            loss = ((1-pt)**self.gamma*loss).mean()
        return (loss, outputs) if return_outputs else loss
```

# Usage

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
model = pipeline(task='sentiment-analysis', model='alexander-sh/mDeBERTa-v3-multi-sent', device='cuda')
model('Keep your face always toward the sunshine—and shadows will fall behind you.')
>>> [{'label': 'positive', 'score': 0.6478521227836609}]
model('I am not coming with you.')
>>> [{'label': 'neutral', 'score': 0.790919840335846}]
model("I am hating that my transformer model don't work properly.")
>>> [{'label': 'negative', 'score': 0.7474458813667297}]
```

# Evaluation and comparison with Vanilla and GPT-4o model:

| Dataset          | Model  | F1     | Accuracy |
|------------------|--------|--------|----------|
|                  | Vanilla| 0.0000 | 0.0000   |
| **sst2**         | Our    | 0.6161 | 0.9231   |
|                  | GPT-4  | 0.6113 | 0.8605   |
|---|---|---|---|
|                  | Vanilla| 0.2453 | 0.5820   |
| **sent-eng**     | Our    | 0.6289 | 0.6470   |
|                  | GPT-4  | 0.4611 | 0.5870   |
|---|---|---|---|
|                  | Vanilla| 0.0889 | 0.1538   |
| **sent-twi**     | Our    | 0.3368 | 0.3488   |
|                  | GPT-4  | 0.5049 | 0.5385   |
|---|---|---|---|
|                  | Vanilla| 0.0000 | 0.0000   |
| **mixed**        | Our    | 0.5644 | 0.7786   |
|                  | GPT-4  | 0.5336 | 0.6863   |
|---|---|---|---|
|                  | Vanilla| 0.1475 | 0.2842   |
| **absc-laptop**  | Our    | 0.5513 | 0.6682   |
|                  | GPT-4  | 0.6679 | 0.7642   |
|---|---|---|---|
|                  | Vanilla| 0.1045 | 0.1858   |
| **absc-rest**    | Our    | 0.6149 | 0.7726   |
|                  | GPT-4  | 0.7057 | 0.8385   |
|---|---|---|---|
|                  | Vanilla| 0.1455 | 0.2791   |
| **stanford**     | Our    | 0.8352 | 0.8353   |
|                  | GPT-4  | 0.8045 | 0.8032   |
|---|---|---|---|
|                  | Vanilla| 0.0000 | 0.0000   |
| **amazon-var**   | Our    | 0.6432 | 0.9647   |
|                  | GPT-4  | -----  | 0.9450   |

F1 score is measured with macro average computation parameter. 

# Source code
[GitHub Repository](https://github.com/alexdrk14/mDeBERTa-v3-multi-sent)