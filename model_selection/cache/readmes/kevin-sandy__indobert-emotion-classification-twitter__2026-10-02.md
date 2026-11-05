---
language:
- id

license: apache-2.0

tags:
- emotion-classification
- indobert
- indonesian-nlp
- text-classification
- twitter

library_name: transformers

pipeline_tag: text-classification

base_model:
- indobenchmark/indobert-base-p1

metrics:
- accuracy
- precision
- recall
- f1
---

# 🇮🇩 Indonesian Emotion Classification using IndoBERT
[![GitHub](https://img.shields.io/badge/GitHub-Repository-black?logo=github)](https://github.com/kevin-sandy/indobert-emotion-classification-twitter)
[![Hugging Face](https://img.shields.io/badge/HuggingFace-Model-yellow?logo=huggingface)](https://huggingface.co/kevin-sandy/indobert-emotion-classification-twitter)

Multiclass emotion classification for Indonesian text using **IndoBERT** and **Hugging Face Transformers**. This project was developed as part of the **NoLimit Indonesia Data Scientist Hiring Test**.

## Overview

The objective of this project is to classify Indonesian text into five emotion categories:

* 😡 Anger
* 😨 Fear
* 😊 Happy
* ❤️ Love
* 😢 Sadness

The model is fine-tuned from **IndoBERT Base P1** and evaluated using standard classification metrics including Accuracy, Precision, Recall, and F1 Score.

---

## Dataset

### Source

Indonesian Twitter Emotion Dataset:

https://www.kaggle.com/datasets/dennisherdi/indonesian-twitter-emotion

### Emotion Labels

| Label   | Description       |
| ------- | ----------------- |
| anger   | Anger emotion     |
| fear    | Fear or anxiety   |
| happy   | Happiness or joy  |
| love    | Affection or love |
| sadness | Sadness           |

### Data Split

| Split      | Percentage |
| ---------- | ---------- |
| Train      | 70%        |
| Validation | 15%        |
| Test       | 15%        |

---

## Project Structure

```text
.
├── dataset/
│   ├── emotion_dataset.csv
│   └── slang_dict.csv
│
├── models/
│   └── indobert-emotion-classification/
│       ├── config.json
│       ├── model.safetensors
│       ├── tokenizer.json
│       ├── tokenizer_config.json
│       └── training_args.bin
│
├── notebooks/
│   ├── emotion_classification.ipynb
│   └── word_dictionary.xlsx
│
├── results/
├── requirements.txt
└── README.md
```

---

## Workflow

![Project Workflow](flowchart.jpg)

---

## Methodology

### 1. Data Preprocessing

Several preprocessing techniques were applied to improve text quality before training:

* Lowercasing
* URL removal
* Mention removal
* Hashtag normalization
* Repeated character normalization
* Indonesian slang normalization
* Whitespace normalization

### Example

Input:

```text
GAKKK suka banget sama pelayanan ini!!!
```

Output:

```text
tidak suka banget sama pelayanan ini!!!
```

---

### 2. Tokenization

Tokenizer used:

```text
indobenchmark/indobert-base-p1
```

---

### 3. Model Fine-Tuning

Base model:

```text
indobenchmark/indobert-base-p1
```

Framework:

* PyTorch
* Hugging Face Transformers

Training configuration:

| Parameter         | Value    |
| ----------------- | -------- |
| Learning Rate     | 1e-5     |
| Batch Size        | 8        |
| Epochs            | 15       |
| Weight Decay      | 0.01     |
| Warmup Ratio      | 0.1      |
| FP16              | Enabled  |
| Evaluation Metric | Macro F1 |

---

## Results

### Test Performance

| Metric            | Score |
| ----------------- | ----- |
| Accuracy          | 0.74  |
| Macro Precision   | 0.76  |
| Macro Recall      | 0.75  |
| Macro F1 Score    | 0.75  |
| Weighted F1 Score | 0.74  |

### Key Findings

* IndoBERT achieved a Macro F1 Score of **0.75** on the test dataset.
* Text normalization helped improve model robustness against informal Indonesian social media language.
* The model performed well across all emotion categories with balanced precision and recall.
* Fear-related tweets remain the most challenging category due to semantic overlap with sadness and anxiety expressions.

---

## Example Predictions

| Text                             | Predicted Emotion |
| -------------------------------- | ----------------- |
| aku sangat senang hari ini       | happy             |
| aku kecewa dengan hasilnya       | sadness           |
| aku takut menghadapi ujian besok | fear              |
| aku sangat menyayanginya         | love              |
| aku marah dengan pelayanan ini   | anger             |

---

## Trained Model

The fine-tuned model is available in:

```text
models/indobert-emotion-classification/
```

The model directory contains:

* config.json
* model.safetensors
* tokenizer.json
* tokenizer_config.json
* training_args.bin

---

## Installation

Clone the repository:

```bash
git clone https://github.com/kevin-sandy/indobert-emotion-classification-twitter.git
cd indobert-emotion-classification-twitter
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Project

Launch Jupyter Notebook:

```bash
jupyter notebook
```

Open:

```text
notebooks/emotion_classification.ipynb
```

Run all cells sequentially to reproduce the complete workflow:

1. Data Loading
2. Exploratory Data Analysis (EDA)
3. Data Preprocessing
4. Label Encoding
5. Data Splitting
6. Tokenization
7. IndoBERT Fine-Tuning
8. Model Evaluation
9. Inference

---

## Inference

Load the trained model using Hugging Face Transformers:

```python
from transformers import pipeline

classifier = pipeline(
    task="text-classification",
    model="./models/indobert-emotion-classification"
)

classifier("aku sangat senang hari ini")
```

Example output:

```python
[
    {
        "label": "happy",
        "score": 0.95
    }
]
```

---

## Technologies

* Python
* PyTorch
* Hugging Face Transformers
* Scikit-learn
* Pandas
* NumPy
* Matplotlib
* Jupyter Notebook

---

## Author

**Kevin Sandy Dimpos Manurung**

Project submitted for the **Data Scientist Hiring Test**.