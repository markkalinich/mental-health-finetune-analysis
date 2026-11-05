---
license: apache-2.0
language:
- ar
pipeline_tag: text-classification
datasets:
- labr
widget:
- text: من أفضل الكتب التي قرأتها في هذا العام
  example_title: Positive
- text: الكتاب سيء، لا أنصح أحد بقراءته أبدا
  example_title: Negative
- text: لا يمكنك الجزم بشيء حول هذا الكتاب
  example_title: Neutral
metrics:
- precision
- recall
- f1
library_name: transformers
tags:
- code
- sentiment analysis
- sentiment-analysis
---

# Introduction
This model predicts the sentiment of a text if it is Positive, Neutral, or Negative.
This model is a finetune version of [UBC-NLP/MARBERTv2](https://huggingface.co/UBC-NLP/MARBERTv2) on [labr](https://huggingface.co/datasets/labr).

# Data
The data used is [labr](https://huggingface.co/datasets/labr), an Arabic book reviews dataset.
The sentiment is obtained from the number of stars given by each review.

| Nubmer of stars | Sentiment |
|-----------------|-----------|
| 1-2             | Negative  |
| 3               | Neutral   |
| 4-5             | Positive  |

# Training
Using the Arabic Pre-Trained [MARBERTv2](https://huggingface.co/UBC-NLP/MARBERTv2) as a base, we finetuned the model for a classification task.
For 3 epochs, the training has been done using huggingface trainer on Google Colab.
This is a POC experiment, so the training hyper-parameters were not optimized.

# Evaluation
Using the test set from [labr](https://huggingface.co/datasets/labr), and the same preprocessing steps, the model was evaluated.
Please note the for the following results, we obtained the macro average.
| Metric | Score |
|-----------------|-----------|
| Precision      | 0.663  |
| Recall            | 0.662   |
| F1             | 0.66  |

# Using the model
To use the model in your code, follow huggingface instructions, or 
```python
from transformers import pipeline

pipe = pipeline("text-classification", model="AbdallahNasir/book-review-sentiment-classification")
result = pipe("من أفضل الكتب التي قرأتها في هذا العام")
print(result)
```

# Training code
Following this code, you will get the same results I got. You can run it in Google Colab. Please use a GPU runtime to finish the training quickly.

```python
# Notebook only:
!pip install transformers[torch] datasets

# Download and load the data
import datasets
dataset = datasets.load_dataset("labr")

# Transform the ratings into Sentiment
POSITIVE = "Positive"
NEUTRAL = "Neutral"
NEGATIVE = "Negative"
rate_to_sentiment = {0: NEGATIVE, 1: NEGATIVE, 2: NEUTRAL, 3: POSITIVE, 4: POSITIVE}
dataset = dataset.map(lambda example: {"sentiment": rate_to_sentiment[example["label"]]}, remove_columns=["label"])
dataset = dataset.rename_column("sentiment", "label")
class_names = [POSITIVE, NEUTRAL, NEGATIVE]  
num_classes = len(class_names)
dataset = dataset.cast_column('label', datasets.ClassLabel(num_classes=num_classes, names=class_names))

# Download and load the pre-trained model and tokenizer
from transformers import AutoModelForSequenceClassification, AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained("UBC-NLP/MARBERTv2")
model = AutoModelForSequenceClassification.from_pretrained("UBC-NLP/MARBERTv2", num_labels=3)

# Tokenize data for training
def tokenize_function(examples):
  return tokenizer(examples["text"],  truncation=True, return_length=True,return_attention_mask=True, max_length=512)
tokenized_datasets = dataset.map(tokenize_function, batched=False, num_proc=16)

# Define data collator, useful for training and batching.
from transformers import DataCollatorWithPadding
data_collator = DataCollatorWithPadding(tokenizer=tokenizer)

# Defining training args
from transformers import TrainingArguments, Trainer
training_args = TrainingArguments("test-trainer", evaluation_strategy="epoch")

from transformers import Trainer
trainer = Trainer(
    model,
    training_args,
    train_dataset=tokenized_datasets["train"],
    eval_dataset=tokenized_datasets["test"],
    data_collator=data_collator,
    tokenizer=tokenizer,
)

# Train and save
trainer.train()
trainer.save_model("final_output")
```

##### Keywords
* sentiment analysis
* arabic
* book reviews