---
language:
- hi
- en
license: mit
library_name: transformers
tags:
- emotion-classification
- xlm-roberta
- hindi
- multi-label
datasets:
- google-research-datasets/go_emotions
metrics:
- accuracy
- f1
- precision
- recall
base_model:
- FacebookAI/xlm-roberta-base
pipeline_tag: text-classification
---

# XLM-Emotion-Hi (Hindi Emotion Classifier)

This model is a fine-tuned version of [XLM-RoBERTa base](https://huggingface.co/facebook/xlm-roberta-base) for multi-label emotion classification on Hindi text. It is specifically optimized to detect 28 different emotion categories (including 'neutral') based on the GoEmotions dataset structure.

## Model Description

- **Developed by:** samarthruckstar
- **Model type:** XLM-RoBERTa Sequence Classification
- **Language(s):** Hindi (hi), English (en)
- **License:** MIT
- **Finetuned from model:** FacebookAI/xlm-roberta-base

## Intended Uses & Limitations

### Intended Use
The model is designed for analyzing the emotional content of Hindi text, such as song lyrics, social media posts, and reviews. It is particularly useful for the "Sarcastic Music Analyzer" project to categorize the vibe of a song.

### Limitations
- The model may struggle with complex sarcasm or very short, ambiguous phrases.
- Performance is best on modern conversational Hindi.

## Performance (Evaluation on Hindi Validation Set)

Evaluated on a subset (500 samples) of the GoEmotions Hindi Validation dataset:

- **Accuracy (Subset):** 36.00%
- **F1 Score (Micro):** 0.4790
- **F1 Score (Macro):** 0.2717
- **Precision (Micro):** 0.6964
- **Recall (Micro):** 0.3651

*Note: Accuracy refers to Subset Accuracy (exact match), which is a strict metric for multi-label classification.*

## Label Mapping

The model outputs scores for the following 28 labels:
0: admiration, 1: amusement, 2: anger, 3: annoyance, 4: approval, 5: caring, 6: confusion, 7: curiosity, 8: desire, 9: disappointment, 10: disapproval, 11: disgust, 12: embarrassment, 13: excitement, 14: fear, 15: gratitude, 16: grief, 17: joy, 18: love, 19: nervousness, 20: optimism, 21: pride, 22: realization, 23: relief, 24: remorse, 25: sadness, 26: surprise, 27: neutral

## How to use

```python
from transformers import pipeline

pipe = pipeline("text-classification", model="samarthruckstar/xlm_hindi_english_emoClss", top_k=None)

text = "क्या यह न्यू ऑरलियन्स में है ?? मुझे वास्तव मे डर लग रहा है"
results = pipe(text)
print(results)
```

## Training procedure

The model was fine-tuned using the GoEmotions dataset translated into Hindi, employing a multi-label classification objective with BCE loss.