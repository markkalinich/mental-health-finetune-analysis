---
license: mit
datasets:
- astromis/presuicidal_signals
language:
- ru
metrics:
- f1
library_name: transformers
pipeline_tag: text-classification
tags:
- russian
- suicide
---

# Presuicidal RuBERT base

The fine-tuned [ruBert](https://huggingface.co/ai-forever/ruBert-base) on the presuicidal dataset. Aims to help the psychologists to find text with useful information about person's suicide behavior.

The model has two categories:
* category 1 - the texts with useful information about person's suicidal behavior such as attempts and facts of rape, problems with parents, the fact of being in a psychiatric hospital, facts of self-harm, etc. Also, this category includes messages containing a display of subjective negative attitude towards oneself and others, including a desire to die, a feeling of pressure from the past, self-hatred, aggressiveness, rage directed at oneself or others.
* category 0 - normal texts that don't contain abovementioned information.

# How to use

```python
import torch

tokenizer = AutoTokenizer.from_pretrained("astromis/presuisidal_rubert")
model = BertForSequenceClassification.from_pretrained("astromis/presuisidal_rubert")
model.eval()

text = ["мне так плохо я хочу умереть", "вчера была на сходке с друзьями было оч клево"]

tokenized_text = tokenizer(text, padding="max_length", truncation=True, max_length=512, return_tensors="pt")

with torch.no_grad():
prediction = model(**tokenized_text).logits
print(prediction.argmax(dim=1).numpy())
# >>> [1, 0]
```

# Training procedure

## Data preprocessing

Before training, the text was transformed in the next way:
* removed all emojis. In the dataset, they are marked as `<emoji>emoja_name</emoji>`;
* the punctuation was removed;
* text was lowered;
* all enters was swapped to spaces;
* all several spaces were collapsed.

As the dataset is heavily imbalanced, the train part of normal texts was randomly downsampled to have only 22% samples out of source volume.

## Training

The training was done with `Trainier` class that have next parameters:
```
TrainingArguments(evaluation_strategy="epoch",
per_device_train_batch_size=16,
per_device_eval_batch_size=32,
learning_rate=1e-5,
num_train_epochs=5,
weight_decay=1e-3,
load_best_model_at_end=True,
save_strategy="epoch")
```

# Metrics

| F1-micro | F1-macro | F1-weighted |
|----------|----------|-------------|
| 0.811926 | 0.726722 | 0.831000 |

# Citation

```bibxtex
@article {Buyanov2022TheDF,
title={The dataset for presuicidal signals detection in text and its analysis},
author={Igor Buyanov and Ilya Sochenkov},
journal={Computational Linguistics and Intellectual Technologies},
year={2022},
month={June},
number={21},
pages={81--92},
url={https://api.semanticscholar.org/CorpusID:253195162},
}
```