---
license: mit
base_model: FacebookAI/xlm-roberta-base
pipeline_tag: text-classification
language:
- my
tags:
- sentiment-analysis
- myanmar
- burmese
- roberta
library_name: transformers
metrics:
- accuracy
- f1
---

# MM Sentiment Intensity Model v1

This is a fine-tuned **XLM-RoBERTa** model for Myanmar sentiment analysis. It classifies text into 5 intensity levels, ranging from Very Negative to Very Positive.

## Model Description
The model was trained on a custom Myanmar dataset specifically curated for sentiment detection. It utilizes a custom syllable breaking preprocessing step to handle Myanmar Unicode text effectively.

- **Developed by:** [Thuta Sann]
- **Model Type:** Text Classification
- **Language:** Myanmar (Burmese)
- **Base Model:** `facebookai/xlm-roberta-base`

## Classification Labels
| Label | Sentiment | Emoji |
|---|---|---|
| LABEL_0 | Very Negative | 🔴 |
| LABEL_1 | Negative | 🟠 |
| LABEL_2 | Neutral | 🟡 |
| LABEL_3 | Positive | 🟢 |
| LABEL_4 | Very Positive | 🔵 |


## How to Use
To use this model, you must apply the **Syllable Breaking** logic before passing text to the model.

```python
import re
from transformers import pipeline

def myanmar_sylbreak(line):
    pat = re.compile(r"((?<!္)[က-အ](?![်္])|[a-zA-Z0-9ဣဤဥဦဧဩဪဿ၌၍၏၀-၉၊။!-/:-@[-`{-~\s])")
    return pat.sub(r" \1", line).strip()

classifier = pipeline("text-classification", model="thutasann/mm_sentiment_model_v1")

raw_text = "ဒီနေ့ ရာသီဥတု အရမ်းသာယာတယ်"
segmented_text = myanmar_sylbreak(raw_text)
result = classifier(segmented_text)
print(result)

```

## Training Data

This model was trained on the [Myanmar Sentiment Intensity Dataset v1](https://huggingface.co/datasets/thutasann/mm_sentiment_model_v1_data), which is based on research from the Myanmar NLP community.

## Acknowledgments

* Base model by FacebookAI (XLM-RoBERTa).
* Syllable breaking logic based on [sylbreak](https://github.com/ye-kyaw-thu/sylbreak).
* Dataset inspiration from [chuuhtetnaing/myanmar-text-segmentation-dataset](https://huggingface.co/datasets/chuuhtetnaing/myanmar-social-media-sentiment-analysis-dataset).