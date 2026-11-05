---
library_name: transformers
datasets:
- nvidia/Aegis-AI-Content-Safety-Dataset-1.0
---

# Model Card for AC/MiniLM-L12-H384-uncased_Nvidia-Aegis-AI-Safety

<!-- Provide a quick summary of what the model is/does. -->
A microsoft/MiniLM-L12-H384-uncased model fine-tuned on the nvidia/Aegis-AI-Content-Safety-Dataset-1.0 dataset. A total of 3099 examples are in the training set. 

This is a multi-label text classifier that has 14 categories:
- "0": "Controlled/Regulated Substances"
- "1": "Criminal Planning/Confessions"
- "2": "Deception/Fraud"
- "3": "Guns and Illegal Weapons"
- "4": "Harassment"
- "5": "Hate/Identity Hate"
- "6": "Needs Caution"
- "7": "PII/Privacy"
- "8": "Profanity"
- "9": "Sexual"
- "10": "Sexual (minor)"
- "11": "Suicide and Self Harm"
- "12": "Threat"
- "13": "Violence"

## How to Get Started with the Model

```py
from accelerate import Accelerator
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import numpy as np
import torch

accelerator = Accelerator()
device = accelerator.device

def load_model(model_path, accelerator_device=None):
    model = AutoModelForSequenceClassification.from_pretrained(
        model_path, 
        problem_type="multi_label_classification", 
    )

    if accelerator_device:
        model.to(accelerator_device)
    
    tokenizer = AutoTokenizer.from_pretrained(model_path)

    return model, tokenizer

def predict(model, tokenizer, text, accelerator_device=None, threshold=0.5):
    if accelerator_device:
        inputs = tokenizer([text], return_tensors="pt").to(accelerator_device)
    else:
        inputs = tokenizer([text], return_tensors="pt")
        
    outputs = model(**inputs)
    probs = torch.nn.Sigmoid()((outputs.logits.squeeze().cpu()))
    predictions = np.zeros(probs.shape)
    predictions[np.where(probs >= threshold)] = 1
    return [model.config.id2label[idx] for idx, label in enumerate(predictions) if label == 1.0]

# USING CPU
hf_model, tokenizer = load_model("AC/MiniLM-L12-H384-uncased_Nvidia-Aegis-AI-Safety")
predict(hf_model, tokenizer, "How to make a bomb?")

# USING GPU
hf_model, tokenizer = load_model("AC/MiniLM-L12-H384-uncased_Nvidia-Aegis-AI-Safety", device)
predict(hf_model, tokenizer, "How to make a bomb?", device)
```

## Evaluation
Evaluation is conducted on the test set in nvidia/Aegis-AI-Content-Safety-Dataset-1.0 dataset. A total of 359 examples are in the test set. 

For AI safety use case, having false negatives (text was actually toxic but model predicted it as safe) is worse than having false positives (text was actually safe but model predicted it as unsafe)

Precision: Out of all text predicted as toxic, how many were actually toxic?
Recall: Out of all text that were actually toxic, how many were predicted toxic?

As we want to reduce false negatives, we will focus on recall.  

| Metric      | Value |
| :----------- | :----------- |
| accuracy      | 0.9514524472741743       |
| f1   | 0.5325670498084292        |
| precision   | 0.668269230769        |
| recall   | 0.442675159235668        |
| TP   | 4643        |
| TN   | 139        |
| FP   | 69        |
| FN   | 175        |


## Finetuning
```
from accelerate import Accelerator
from datasets import load_dataset, Dataset, DatasetDict
from datetime import datetime
from transformers import AutoModelForSequenceClassification, AutoTokenizer, TrainingArguments, Trainer, EvalPrediction, DataCollatorWithPadding
from sklearn.metrics import f1_score, roc_auc_score, accuracy_score, coverage_error

import numpy as np
import torch
import os
import pandas as pd
import evaluate

accelerator = Accelerator()
device = accelerator.device

def load_model(model_path, accelerator_device):
    model = AutoModelForSequenceClassification.from_pretrained(
        model_path, 
        problem_type="multi_label_classification", 
        num_labels=len(all_labels),
        id2label=id2label,
        label2id=label2id
    )

    model.to(accelerator_device)
    
    tokenizer = AutoTokenizer.from_pretrained(model_path)

    return model, tokenizer

def predict(model, tokenizer, text, threshold=0.5):
    inputs = tokenizer([text], return_tensors="pt").to(device)
    outputs = model(**inputs)
    probs = torch.nn.Sigmoid()((outputs.logits.squeeze().cpu()))
    predictions = np.zeros(probs.shape)
    predictions[np.where(probs >= threshold)] = 1
    return [id2label[idx] for idx, label in enumerate(predictions) if label == 1.0]

def tokenize_text(examples):
    final_labels = np.zeros(len(all_labels))
    for idx, label in enumerate(all_labels):
        final_labels[idx] = examples[label]
        
    examples["labels"] = final_labels
    return tokenizer(examples["text"], truncation=True, max_length=512)


### Data Preprocessing

all_labels = [
    'Controlled/Regulated Substances',
    'Criminal Planning/Confessions',
    'Deception/Fraud',
    'Guns and Illegal Weapons',
    'Harassment',
    'Hate/Identity Hate',
    'Needs Caution',
    'PII/Privacy',
    'Profanity',
    'Sexual',
    'Sexual (minor)',
    'Suicide and Self Harm',
    'Threat',
    'Violence'
]

id2label = {idx:label for idx, label in enumerate(all_labels)}
label2id = {label:idx for idx, label in enumerate(all_labels)}

base_model, tokenizer = load_model("microsoft/MiniLM-L12-H384-uncased", device)

train_df = pd.read_csv("nvidia_train.csv")
test_df = pd.read_csv("nvidia_test.csv")

dataset = DatasetDict({
    'train': Dataset.from_pandas(train_df),
    'test': Dataset.from_pandas(test_df)}
)

preprocessed_dataset = dataset.map(tokenize_text)


### Metrics for multi-label classification

clf_metrics = evaluate.combine(["accuracy", "f1", "precision", "recall"])

def sigmoid(x):
   return 1/(1 + np.exp(-x))

def compute_metrics(eval_pred):
   predictions, labels = eval_pred
   predictions = sigmoid(predictions)
   predictions = (predictions > 0.5).astype(int).reshape(-1)
   return clf_metrics.compute(predictions=predictions, references=labels.astype(int).reshape(-1))


### Finetuning

data_collator = DataCollatorWithPadding(tokenizer=tokenizer)

output_dir = f'./minilm_finetuned/minilm-{datetime.now().strftime("%d-%m-%Y_%H-%M")}' # Output directory where the training checkpoints will be stored

final_output_dir = './minilm_finetuned' # Best model from trainer will be saved here

training_args = TrainingArguments(
    output_dir=output_dir,
    learning_rate=2e-5,
    per_device_train_batch_size=3,
    per_device_eval_batch_size=3,
    num_train_epochs=20,
    weight_decay=0.01,
    fp16=True,
    evaluation_strategy="epoch",
    save_strategy="epoch",
    save_total_limit=2,
    load_best_model_at_end=True,
)

trainer = Trainer(
    model=base_model,
    args=training_args,
    train_dataset=preprocessed_dataset["train"],
    eval_dataset=preprocessed_dataset["test"],
    tokenizer=tokenizer,
    data_collator=data_collator,
    compute_metrics=compute_metrics,
)

trainer.train()

print("Saving model...")
trainer.save_model(final_output_dir)


### Evaluate model
base_model, tokenizer = load_model(final_output_dir, device)
predict(base_model, tokenizer, "How to make a bomb?")
```