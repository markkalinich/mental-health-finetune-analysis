---
language:
- en
license: apache-2.0
library_name: transformers
pipeline_tag: text-classification
base_model: bert-base-uncased
datasets:
- glue
- sst2
metrics:
- accuracy
tags:
- bert
- fine-tuning
- sentiment-analysis
- text-classification
- glue
- sst2
- pytorch
---

# UnMelow/422_zhuravlev — BERT (base uncased) fine-tuned on GLUE/SST-2

## Model summary
This repository contains a **BERT-base-uncased** model fine-tuned for **binary sentiment classification** on the **GLUE/SST-2** dataset.

- **Task:** sentiment analysis (binary classification)
- **Labels:** `negative (0)`, `positive (1)`
- **Base model:** `bert-base-uncased`
- **Library:** Transformers (`Trainer` API)

> Note: In the training notebook, the model was fine-tuned on a **small subset** (640 train / 640 validation) for demonstration purposes. For production use, fine-tune on the full dataset and validate thoroughly.

---

## Intended uses
### Supported
- Quick demos of sentiment classification on English sentences
- Educational examples of fine-tuning with `Trainer`
- Baseline experiments on SST-2-like sentiment data

### Not recommended
- High-stakes or safety-critical decisions (medical, legal, hiring, etc.)
- Domains significantly different from SST-2 (e.g., clinical notes, finance news) without further fine-tuning
- Non-English text (model and data are English-focused)

---

## Limitations and biases
- **Dataset bias:** SST-2 reflects movie review sentiment distribution and language patterns; performance may degrade on other domains.
- **Small fine-tuning subset:** if you trained on 640 samples, results are not representative of the full SST-2 benchmark.
- **Short-text behavior:** very short/ambiguous or sarcastic statements can be misclassified.
- **Offensive/toxic content:** the model may output confident predictions on harmful text; it does not provide safety filtering.

---

## Training data
Fine-tuning used the **GLUE** benchmark dataset configuration **SST-2** (Stanford Sentiment Treebank v2 as used in GLUE).

- **Dataset:** `glue`, config `sst2`
- **Text field:** `sentence`
- **Label field:** `label` (0/1)

In the provided Colab:
- `train`: selected `range(640)`
- `validation`: selected `range(640)`
- `test`: predictions generated without labels (GLUE test split)

---

## Training procedure
### Preprocessing
- Tokenizer: `AutoTokenizer.from_pretrained("bert-base-uncased")`
- Truncation enabled (`truncation=True`)
- Dynamic padding via `DataCollatorWithPadding`

### Hyperparameters (from Colab)
- **epochs:** 3
- **learning_rate:** 2e-5
- **batch_size:** 16 (per device)
- **weight_decay:** 0.01
- **evaluation:** each epoch
- **checkpointing:** each epoch
- **best model selection:** `accuracy` on validation
- **logging:** disabled (`report_to="none"`)

---

### Results (validation)
- **Accuracy:** `0.8625`
- **Loss:** `0.33919745683670044`

Optional (if you computed them):
- Confusion matrix screenshot or values
- Precision/recall/F1 per class

---

## How to use

### Transformers pipeline
```python
from transformers import pipeline

model_id = "UnMelow/422_zhuravlev"

clf = pipeline(
    "text-classification",
    model=model_id,
    tokenizer=model_id,
    return_all_scores=False
)

print(clf("This movie was surprisingly good!"))
print(clf("The plot was boring and predictable."))
