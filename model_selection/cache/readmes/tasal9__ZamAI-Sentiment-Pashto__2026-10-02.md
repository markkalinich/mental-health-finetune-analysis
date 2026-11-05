---
license: "apache-2.0"
pipeline_tag: "text-classification"
library_name: transformers
language:
  - ps
  - en
datasets:
  - tasal9/ZamAI_Pashto_Dataset
metrics:
  - accuracy
  - f1
  - precision
  - recall
tags:
  - pashto
  - "text-classification"
  - "sentiment-analysis"
  - zamai
  - "language:ps"
  - "language:en"
  - "region:us"
widget:
  - text: >-
      سلام دې وي! تاسو څنګه یاست؟
    example_title: Pashto Greeting
  - text: >-
      دا ډیر خراب خبره ده
    example_title: Negative Sentiment
  - text: >-
      Hello, how can I help you today?
    example_title: English Greeting
---

# ZamAI Sentiment Pashto

**Task:** text-classification  
**Languages:** ps, en  
**Training dataset(s):** tasal9/ZamAI_Pashto_Dataset  

## Overview

This model is part of the **ZamAI** Pashto language AI collection. It is fine-tuned/adapted for **text-classification** in Pashto and related languages.

## Intended uses & limitations

- Use for research, prototyping, and production assistance in Pashto NLP.
- Evaluate outputs carefully before deploying in high-stakes applications.
- May reflect biases present in the pre-training or fine-tuning data.

## How to use

```python
from transformers import pipeline

classifier = pipeline("text-classification", model="tasal9/ZamAI-Sentiment-Pashto")
print(classifier("دا ډیره ښه خبره ده"))
```

## Training data

The model was trained or fine-tuned on: [tasal9/ZamAI_Pashto_Dataset](https://huggingface.co/tasal9/ZamAI_Pashto_Dataset).

## Evaluation

| Metric | Value | Description |
|--------|-------|-------------|
| accuracy | *TBD* | Add measured value |
| f1 | *TBD* | Add measured value |
| precision | *TBD* | Add measured value |
| recall | *TBD* | Add measured value |

> Update this table with your measured results and link to the evaluation script/notebook.

## Citation

```bibtex
@misc{zamai_pashto,
  title = {{ZamAI Sentiment Pashto}},
  author = {ZamAI / Yaqoob Tasal},
  year = {2024},
  howpublished = {\url{https://huggingface.co/tasal9/ZamAI-Sentiment-Pashto}}
}
```

## License

This model is released under the **"apache-2.0"** license.
