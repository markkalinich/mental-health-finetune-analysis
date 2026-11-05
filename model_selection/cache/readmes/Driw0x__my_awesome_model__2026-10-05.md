---
language:
- en
library_name: transformers
license: apache-2.0
base_model: distilbert/distilbert-base-uncased
datasets:
- stanfordnlp/imdb
pipeline_tag: text-classification
tags:
- generated_from_trainer
- distilbert
- sentiment-analysis
- text-classification
- fine-tuned
- huggingface-course
metrics:
- accuracy
---

# DistilBERT fine-tuned on IMDb for Sentiment Classification

## Model Description

This model is a fine-tuned version of `distilbert/distilbert-base-uncased` for binary sentiment classification.

It was fine-tuned on the IMDb movie review dataset to classify English reviews as either **positive** or **negative**.

The model was created as a practical exercise while following the Hugging Face LLM Course.

- **Developed by:** Driw0x
- **Model type:** DistilBERT
- **Language:** English
- **Base model:** `distilbert/distilbert-base-uncased`
- **Task:** Text classification / sentiment analysis
- **Number of labels:** 2

### Labels

| ID | Label |
|---:|---|
| 0 | NEGATIVE |
| 1 | POSITIVE |

## Training and Evaluation Data

The model was fine-tuned on the `stanfordnlp/imdb` dataset.

The dataset contains English movie reviews labeled as either positive or negative.

The training notebook uses:

- the `train` split for training;
- the `test` split for evaluation.

Because the IMDb test split is evaluated during training, it also participates in the model-development process and should not be considered a completely untouched final test set for this experiment.

## Preprocessing

The reviews are tokenized using the DistilBERT tokenizer:

```python
def preprocess_function(examples):
    return tokenizer(examples["text"], truncation=True)
```

The complete dataset is tokenized with:

```python
tokenized_imdb = imdb.map(
    preprocess_function,
    batched=True
)
```

Dynamic padding is applied with `DataCollatorWithPadding`.

## Training Procedure

The model was fine-tuned using the Hugging Face `Trainer` API.

### Training Hyperparameters

| Hyperparameter | Value |
|---|---:|
| Learning rate | `2e-5` |
| Train batch size | `16` |
| Evaluation batch size | `16` |
| Number of epochs | `2` |
| Weight decay | `0.01` |
| Seed | `42` |
| Evaluation strategy | `epoch` |
| Save strategy | `epoch` |
| LR scheduler | `linear` |
| Load best model at end | `True` |

The optimizer used during training was AdamW (`ADAMW_TORCH_FUSED`) with:

- `betas=(0.9, 0.999)`
- `epsilon=1e-8`

Accuracy was computed using the Hugging Face `evaluate` library.

## Training Results

| Epoch | Training Loss | Validation Loss | Accuracy |
|---:|---:|---:|---:|
| 1 | 0.220537 | **0.198028** | 0.923640 |
| 2 | **0.149095** | 0.232832 | **0.931080** |

The complete training run reported:

- **Training loss:** `0.205667`
- **Training steps:** `3126`
- **Epochs:** `2`

The final evaluation logged by the Trainer reached:

- **Validation loss:** `0.232832`
- **Accuracy:** `0.931080`

The first epoch obtained the lowest validation loss, while the second epoch obtained the highest accuracy.

## Usage

### Pipeline

```python
from transformers import pipeline

classifier = pipeline(
    "sentiment-analysis",
    model="Driw0x/my_awesome_model"
)

text = (
    "This was a masterpiece. Not completely faithful to the books, "
    "but enthralling from beginning to end."
)

print(classifier(text))
```

Example output from the training notebook:

```text
[{'label': 'POSITIVE', 'score': 0.9944}]
```

### Direct Inference

```python
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained(
    "Driw0x/my_awesome_model"
)

model = AutoModelForSequenceClassification.from_pretrained(
    "Driw0x/my_awesome_model"
)

text = "This movie was fantastic."

inputs = tokenizer(
    text,
    return_tensors="pt"
)

with torch.no_grad():
    logits = model(**inputs).logits

predicted_class_id = logits.argmax().item()

print(model.config.id2label[predicted_class_id])
```

## Intended Uses

This model is primarily intended for:

- educational demonstrations of Transformer fine-tuning;
- experimenting with the Hugging Face `Trainer`;
- binary sentiment classification;
- learning how to publish and reuse models on the Hugging Face Hub.

## Limitations

This model was fine-tuned specifically on IMDb movie reviews.

Important limitations include:

- performance may decrease on text from other domains;
- the model only predicts positive or negative sentiment;
- neutral or more nuanced sentiment is not represented;
- long inputs may be truncated;
- biases present in the base model or IMDb dataset may be inherited;
- the IMDb test split was used during training for evaluation.

This model was created as a course exercise and has not been validated for production or high-stakes applications.

## Framework Versions

- Transformers 5.17.0
- PyTorch 2.11.0+cu130
- Datasets 4.8.5
- Tokenizers 0.23.2

## Training Source

The complete training procedure is available in the following repository:

`Driw0x/hf-ai-courses`

Notebook:

`llm-course/1-transformer-models/notebooks/sequence_classification.ipynb`