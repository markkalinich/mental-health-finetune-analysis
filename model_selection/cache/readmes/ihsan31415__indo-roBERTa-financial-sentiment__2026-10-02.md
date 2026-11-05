---
tags:
- indonesian
- sentiment-analysis
- finance
- financial-sentiment
- indo-roberta
- transformers
- fine-tuned
- huggingface
- ihsg
- stock-market
- nlp
- indonesian-roberta-base-financial-sentiment-classifier
language:
- id
datasets:
- intanm/indonesian-financial-sentiment-analysis
metrics:
- accuracy
- f1
- precision
- recall
model-index:
- name: indo-roBERTa-financial-sentiment
  results:
  - task:
      type: text-classification
      name: Text Classification (Sentiment Analysis)
    dataset:
      name: indonesian-financial-sentiment
      type: intanm/indonesian-financial-sentiment-analysis
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.9749
    - name: F1
      type: f1
      value: 0.9749
    - name: Precision
      type: precision
      value: 0.9749
    - name: Recall
      type: recall
      value: 0.9749
license: mit
library_name: transformers
---



# 🇮🇩 IndoRoBERTa for Indonesian Financial Sentiment Classification

This is a fine-tuned version of [`w11wo/indonesian-roberta-base-sentiment-classifier`](https://huggingface.co/w11wo/indonesian-roberta-base-sentiment-classifier), specialized for **Indonesian financial news sentiment classification** since i cant find any financial sentiment models for indonesian market, i decided to make my self.

### 🧠 Model Summary

| Field             | Value                                                                 |
|------------------|-----------------------------------------------------------------------|
| **Model Name**    | `ihsan31415/indo-roBERTa-financial-sentiment`              |
| **Base Model**    | [`w11wo/indonesian-roberta-base-sentiment-classifier`](https://huggingface.co/w11wo/indonesian-roberta-base-sentiment-classifier) |
| **Language**      | Indonesian (`id`)                                                    |
| **Task**          | Sentiment Analysis (Financial)                                       |
| **Labels**        | `0`: Positive, `1`: Neutral, `2`: Negative *(⚠️ flipped label order)* |
| **Dataset**       | [`intanm/indonesian-financial-sentiment-analysis`](https://huggingface.co/datasets/intanm/indonesian-financial-sentiment-analysis) + synthetic and augmented samples |
| **Fine-tuned by** | [`ihsan31415`](https://huggingface.co/ihsan31415)                   |
| **Training Epochs** | 5 (Early stopping at epoch 5, best at epoch 3)                    |
| **Eval Accuracy** | `97.49%`                                                             |


---

## 🧠 Model Objective

This model classifies Indonesian financial news articles into:

* `0` → **Positive**
* `1` → **Neutral**
* `2` → **Negative**

⚠️ **Important: Label Mapping is Flipped**
This label order follows the base model's unexpected configuration. During training and evaluation, the dataset was relabeled accordingly.

> ⚠️ Always interpret model output using this mapping:
>
> * `0`: Positive
> * `1`: Neutral
> * `2`: Negative

---

## 📊 Dataset & Preprocessing Pipeline

### 🔹 Source Dataset

* [`intanm/indonesian-financial-sentiment-analysis`](https://huggingface.co/datasets/intanm/indonesian-financial-sentiment-analysis)
* Labeled financial news (imbalanced and limited)

### 📈 Data Augmentation & Balancing

#### 1. 🧪 Gemini Synthetic Generation

* Generated structured financial news samples using `gemini-2.0-flash-lite`
* Targeted generation for underrepresented classes

#### 2. ✍️ GPT-2 Prompt Completion

* Used [`indonesian-nlp/gpt2-medium-indonesian`](https://huggingface.co/indonesian-nlp/gpt2-medium-indonesian)
* Prompt templates varied and strictly separated between train/test sets

#### 3. 🧩 Roberta-Based Masked Augmentation

* Strategic masking/filling while protecting key financial terms
* Iterative masking to increase diversity and context coverage

#### 📊 Final Label Distribution

**Train Set**:

```
2 (Negative): 22906
1 (Neutral): 23374
0 (Positive): 23423
```

**Test Set**:

```
2 (Negative): 9817
1 (Neutral): 10018
0 (Positive): 10039
```

---

## 🏋️ Training Details

### 🔁 Label Flipping

> The base model uses **non-standard labels**:
>
> * `0`: Positive
> * `1`: Neutral
> * `2`: Negative
>
> Training data was relabeled accordingly.

### 🔧 TrainingArguments

```python
TrainingArguments(
    output_dir="./results-roberta",
    eval_strategy="epoch",
    save_strategy="epoch",
    logging_strategy="epoch",
    per_device_train_batch_size=256,
    per_device_eval_batch_size=256,
    num_train_epochs=15,
    learning_rate=2e-5,
    weight_decay=0.01,
    load_best_model_at_end=True,
    metric_for_best_model="accuracy",
    save_total_limit=4,
)
```

* Early stopping (`patience=2`)
* Training completed at **epoch 5**, best model from **epoch 3**

### 📊 Training Progress

| Epoch | Training Loss | Validation Loss | Accuracy   | Precision  | Recall     | F1 Score   |
|-------|----------------|------------------|------------|------------|------------|------------|
| 1     | 0.104500       | 0.085562         | 0.969402   | 0.969715   | 0.969402   | 0.969356   |
| 2     | 0.029100       | 0.088392         | 0.974859   | 0.974914   | 0.974859   | 0.974860   |
| 3     | 0.012700       | 0.102305         | 0.974926   | 0.974949   | 0.974926   | 0.974933   |
| 4     | 0.008900       | 0.125707         | 0.972816   | 0.972959   | 0.972816   | 0.972846   |
| 5     | 0.004400       | 0.157659         | 0.966690   | 0.966902   | 0.966690   | 0.966676   |


### ✅ Evaluation Results

```bash
eval_loss                 = 0.10230540484189987
eval_accuracy             = 0.9749255130394028
eval_precision            = 0.9749490510899772
eval_recall               = 0.9749255130394028
eval_f1                   = 0.9749326327197978
eval_runtime              = 71.9098
eval_samples_per_second   = 415.395
eval_steps_per_second     = 1.627
epoch                     = 5.0
```

---

## 🔎 Usage

#### Using Pipeline
```python
from transformers import pipeline

pretrained_name = "ihsan31415/indo-roBERTa-financial-sentiment"

nlp = pipeline(
    "sentiment-analysis",
    model=pretrained_name,
    tokenizer=pretrained_name
)

nlp("IHSG diprediksi melemah karena sentimen global negatif")
```
#### RAW
```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load model and tokenizer
model = AutoModelForSequenceClassification.from_pretrained("ihsan31415/indo-roBERTa-financial-sentiment")
tokenizer = AutoTokenizer.from_pretrained("ihsan31415/indo-roBERTa-financial-sentiment")

# Example input
text = "IHSG diprediksi melemah karena sentimen global negatif"
inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
outputs = model(**inputs)

# Get predicted class
predicted_label = torch.argmax(outputs.logits, dim=1).item()

# Interpret using flipped label mapping
label_map = {
    0: "Positive",
    1: "Neutral",
    2: "Negative"
}
print(f"Predicted sentiment: {label_map[predicted_label]}")
```

## Author

this indonesian RoBERTa base financial CLassifier was trained and evaluated by Khoirul Ihsan using Google colab GPU T4.

---

## 📌 Citation

```bibtex
@misc{khoirul_ihsan_2025,
  title        = {IndoRoBERTa for Indonesian Financial Sentiment Classification},
  author       = {Khoirul Ihsan},
  howpublished = {\url{https://huggingface.co/ihsan31415/indo-roBERTa-financial-sentiment}},
  year         = {2025},
  note         = {Fine-tuned from w11wo/indonesian-roberta-base-sentiment-classifier using augmented financial news data from intanm/indonesian-financial-sentiment-analysis and various synthetic generation methods (Gemini, GPT-2, Roberta masking).},
  publisher    = {Hugging Face}
}
```
---

## 📬 Contact

Created with love and tears by ihsan:\
[![HuggingFace](https://img.shields.io/badge/HuggingFace-orange?style=flat&logo=huggingface&logoColor=white)](https://huggingface.co/ihsan31415)
[![GitHub](https://img.shields.io/badge/GitHub-black?style=flat&logo=github&logoColor=white)](https://github.com/ihsan31415)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-blue?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/khoirul-ihsan-387115288/)\
For collaborations or questions, feel free to reach out via Hugging Face or GitHub.