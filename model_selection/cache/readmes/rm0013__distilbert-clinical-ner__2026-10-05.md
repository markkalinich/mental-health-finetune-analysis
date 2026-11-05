---
license: apache-2.0
language:
- en
base_model:
- distilbert/distilbert-base-uncased
tags:
- medical
- NER
---

## Model Description

`distilbert-clinical-ner` is a fine-tuned DistilBERT model for **biomedical and clinical NER tasks**.  
It is trained to identify and classify entities such as **diseases, medications, lab values, procedures, and other biomedical concepts** in text.  

This model is intended for **research and learning purposes** 

---

## Intended Use

- Extract biomedical entities from clinical notes, research papers, or other health-related texts.  
- Educational purposes: experiment with NER pipelines, token classification, and fine-tuning pre-trained transformers.  

---

## Not Intended For

- Production-level clinical decision making.  
- Use in real-world medical diagnosis or treatment recommendations.  

---

## Metrics

The model was evaluated on a biomedical NER dataset (BioMedical NER, MACCROBAT) using standard token-level metrics:

| Metric    | Score |
|-----------|-------|
| Accuracy  | 0.65  |
| Precision | 0.65  |
| Recall    | 0.65  |
| F1-score  | 0.65  |

> These metrics reflect experimental performance and are intended for learning and demonstration purposes.

---

## Citation

If you use this model for research or portfolio demonstrations, you can cite:

```
@misc{rakesh-mohan-2025-distilbertclinicalner,
title={distilbert-clinical-ner: A Biomedical NER Model},
author={Rakesh Mohan},
year={2025},
howpublished={\url{https://huggingface.co/rm0013/distilbert-clinical-ner}}
}

```

---