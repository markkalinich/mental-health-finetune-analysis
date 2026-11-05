---
library_name: transformers
tags:
- emotions
license: openrail++
datasets:
- ukr-detect/ukr-emotions-binary
language:
- uk
metrics:
- accuracy
- f1
base_model:
- intfloat/multilingual-e5-large
pipeline_tag: text-classification
---

# EmoBench-UA: Emotions Detection in Ukrainian Texts

<img alt="EmoBench-UA" style="width: 75%; height: 75%" src="intro_logo.png">


## Model Details

We provide the first of its kind emotions detector in Ukrainian texts. We cover six basic emotions: Joy, Anger, Fear, Disgust, Surprise, Sadness -- and None. Any text can contain any amount of emotion -- only one, several, or none at all. The texts with None emotions are the ones where the labels per emotions classes are 0.

The base model [intfloat/multilingual-e5-large](https://huggingface.co/intfloat/multilingual-e5-large) was fine-tuned for multi-label emotions classification task on the train part of [ukr-emotions-binary](https://huggingface.co/datasets/ukr-detect/ukr-emotions-binary) dataset.

**Usage**: The model outputs 0 or 1 indicating the presence of the emotion in the text. Thus, this model can be used to detect any basic emotions presence or their absence in the Ukrainian texts.

## Evaluation Results

General classification report of our model on the test part of [ukr-emotions-binary](https://huggingface.co/datasets/ukr-detect/ukr-emotions-binary):

|              | precision | recall | f1-score |   support   |
|:------------:|:------:|----------|---------|------|
| Joy          | 0.69   | 0.78     | 0.73    | 368  |
| Fear         | 0.80   | 0.81     | 0.81    | 151  |
| Anger        | 0.41   | 0.25     | 0.31    | 99   |
| Sadness      | 0.67   | 0.71     | 0.69    | 298  |
| Disgust      | 0.63   | 0.24     | 0.35    | 79   |
| Surprise     | 0.52   | 0.72     | 0.60    | 175  |
| None         | 0.82   | 0.80     | 0.81    | 1108 |
| micro avg    | 0.73   | 0.74     | 0.73    | 2278 |
| macro avg    | 0.65   | 0.62     | 0.62    | 2278 |
| weighted avg | 0.73   | 0.74     | 0.73    | 2278 |
| samples avg  | 0.72   | 0.74     | 0.72    | 2278 

<img alt="EmoBench-UA" style="width: 35%; height: 35%" src="./confusion_matrix.png">

## How to Get Started with the Model

We provide the code to get started with the model:

```python
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# 1. Set up model & tokenizer (update model_name as needed)
model_name = "ukr-detect/emotions_classifier"  # Or path to local dir
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)
model.eval()  # For inference

# 2. Define thresholds (must match the order of model's id2label)
thresholds = {
    "Joy": 0.35,
    "Fear": 0.5,
    "Anger": 0.25,
    "Sadness": 0.5,
    "Disgust": 0.3,
    "Surprise": 0.25,
    "None": 0.35
}

# 3. Prepare a function for prediction
def predict_emotions(texts):
    # Tokenize
    enc = tokenizer(texts, padding=True, truncation=True, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**enc)
        logits = outputs.logits
        probs = torch.sigmoid(logits)
    
    # Get label mapping in correct order
    id2label = model.config.id2label
    label_order = [id2label[i] for i in range(len(id2label))]
    
    # Threshold and get predictions
    predictions = []
    for prob_row in probs:
        single_pred = [
            label for label, prob in zip(label_order, prob_row.tolist())
            if prob > thresholds[label]
        ]
        predictions.append(single_pred)
    return predictions

# 4. Example usage
texts = [
    "Я щойно отримав підвищення на роботі!",
    "Я хвилююся за майбутнє.",
    "я не буду заради тебе, Гані і Каті терпіти того пйоса",
    "Сьогодні нічого не сталося.",
    "всі чомусь плутають, а мені то дивно так )))",
    " ого, то зовсім не приємно(("
]

results = predict_emotions(texts)
for t, r in zip(texts, results):
    print(f"Text: {t}\nEmotions: {r}\n")

# Expected output

Text: Я щойно отримав підвищення на роботі!
Emotions: ['Joy', 'Surprise']

Text: Я хвилююся за майбутнє.
Emotions: ['Fear']

Text: я не буду заради тебе, Гані і Каті терпіти того пйоса
Emotions: ['Anger', 'Disgust']

Text: Сьогодні нічого не сталося.
Emotions: ['None']

Text:  всі чомусь плутають, а мені то дивно так )))
Emotions: ['Surprise']

Text:  ого, то зовсім не приємно((
Emotions: ['Sadness']
```

## Citation

If you would like to acknowledge our work, please, cite the following manuscript:

```
@inproceedings{dementieva-etal-2025-emobench,
    title = "{E}mo{B}ench-{UA}: A Benchmark Dataset for Emotion Detection in {U}krainian",
    author = "Dementieva, Daryna  and
      Babakov, Nikolay  and
      Fraser, Alexander",
    editor = "Christodoulopoulos, Christos  and
      Chakraborty, Tanmoy  and
      Rose, Carolyn  and
      Peng, Violet",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2025",
    month = nov,
    year = "2025",
    address = "Suzhou, China",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2025.findings-emnlp.107/",
    doi = "10.18653/v1/2025.findings-emnlp.107",
    pages = "2025--2048",
    ISBN = "979-8-89176-335-7",
    abstract = "While Ukrainian NLP has seen progress in many texts processing tasks, emotion classification remains an underexplored area with no publicly available benchmark to date. In this work, we introduce \textbf{EmoBench-UA}, the first annotated dataset for emotion detection in Ukrainian texts. Our annotation schema is adapted from the previous English-centric works on emotion detection (Mohammad et al., 2018; Mohammad, 2022) guidelines. The dataset was created through crowdsourcing using the Toloka.ai platform ensuring high-quality of the annotation process. Then, we evaluate a range of approaches on the collected dataset, starting from linguistic-based baselines, synthetic data translated from English, to large language models (LLMs). Our findings highlight the challenges of emotion classification in non-mainstream languages like Ukrainian and emphasize the need for further development of Ukrainian-specific models and training resources."
}
```

## Contacts

[Nikolay Babakov](https://huggingface.co/NiGuLa), [Daryna Dementieva](https://huggingface.co/dardem)