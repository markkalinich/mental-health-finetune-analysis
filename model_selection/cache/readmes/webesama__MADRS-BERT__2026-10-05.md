---
license: cc-by-nc-4.0
language:
- de
base_model:
- google-bert/bert-base-german-cased
pipeline_tag: text-classification
tags:
- depression
- mental-health
- MADRS
- clinical
- interview
---


# MADRS-BERT

**MADRS-BERT** is a fine-tuned `bert-base-german-cased` model that predicts depression severity scores (0–6) across individual items of the [Montgomery-Åsberg Depression Rating Scale (MADRS)](https://en.wikipedia.org/wiki/MADRS). Each prediction is based on transcribed, structured clinician–patient interview segments.

- **Publication**: [https://www.nature.com/articles/s41746-025-01982-8#Sec8](https://www.nature.com/articles/s41746-025-01982-8#Sec8)
- **Example dataset**: [https://github.com/webersamantha/MADRS-BERT/data](https://github.com/webersamantha/MADRS-BERT/data)
- **Github Repo**: The code for data curation, finetuning and evaluation is shared in the following github repo: [https://github.com/webersamantha/MADRS-BERT](https://github.com/webersamantha/MADRS-BERT)

This model was developed to support standardized, scalable mental health assessments in both clinical and low-resource settings.


## Model Details

- **Base model**: `bert-base-german-cased`
- **Task**: Ordinal regression (scores 0–6)
- **Language**: German 
- **Input**: Text (dialogue segment grouped by MADRS topic)
- **Output**: Predicted score for each MADRS item (rounded integer 0–6)
- **Training data**: Mix of real and synthetic clinician–patient interviews (MADRS-structured)


## Intended Use

This model is intended for research and development use. It is not a certified medical device. The goal is to:
- Explore AI-assisted symptom severity assessment
- Enable structured evaluation of individual MADRS items
- Support clinicians or researchers working in psychiatry/mental health

---

## 🚀 How to Use

### Preprocess Data File:

Please organize your data equivalent to the example data (synthetic data) with columns: Subject, Speaker, Transcription, Topic, Score.

```python

import pandas as pd

def load_and_prepare_conversations(filepath):
    df = pd.read_excel(filepath)
    conversations = []

    for topic in df['Topic'].unique():
        topic_df = df[df['Topic'] == topic]
        if topic_df.empty: continue

        dialogue = "\n".join([
            f"{row['Speaker']}: {row['Transcription']}"
            for _, row in topic_df.iterrows()
            if pd.notnull(row['Transcription'])
        ])

        conversations.append((topic, dialogue))
    return conversations

```

### Load model and tokenizer:

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model_name = "webesama/MADRS-BERT"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)
model.eval().to("cuda" if torch.cuda.is_available() else "cpu")
```

### Predict on a full structured interview / Run inference:
Assume you have a conversation log like this:

```python
def predict_madrs_scores(conversations, tokenizer, model):
    device = model.device
    predictions = {}
    
    for topic, dialogue in conversations:
        inputs = tokenizer(dialogue, truncation=True, padding="max_length", max_length=512, return_tensors="pt").to(device)
        with torch.no_grad():
            score = torch.round(model(**inputs).logits).clamp(0, 6).item()
        predictions[topic] = score

    return predictions

file_path = "example_interview.xlsx"
conversations = load_and_prepare_conversations(file_path)
scores = predict_madrs_scores(conversations, tokenizer, model)
print(scores)

```

---

## Acknowledgements

Model trained and released by [Samantha Weber](https://github.com/webersamantha) within the framework of the [Multicast Project on predicting and treating suicidality](https://www.multicast.uzh.ch/en.html). Research conducted as part of efforts to improve AI-driven mental health tools. Thanks to all clinicians and collaborators who contributed to the annotated MADRS dataset.


## Evaluation

The model was evaluated on a held-out clinical validation set and achieved strong performance under both strict and flexible scoring criteria (±1 deviation tolerance). See publication for full metrics.


## Citation

If you use this model, please cite:
> Weber, S. et al. (2025). "Using a Fine-tuned Large Language Model for Symptom-based Depression Evaluation" (DOI: https://doi.org/10.1038/s41746-025-01982-8)