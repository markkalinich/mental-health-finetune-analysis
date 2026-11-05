---
license: gpl-3.0
language:
- ro
- cs
- en
- it
- es
- nl
- sv
metrics:
- f1
- recall
- precision
base_model:
- FacebookAI/xlm-roberta-large
pipeline_tag: token-classification
tags:
- medical
---


XLM-RoBERTa large, finetuned on the [MultiClinAI](https://temu.bsc.es/MultiClinAI/) [dataset](https://zenodo.org/records/18508039), using the [following](https://github.com/UPOD-datascience/MedNER.nl) library.
We approximately aligned the mono-label documents to create a multilabel corpus using the approach from [Jonker and Matos](https://aclanthology.org/2026.smm4h-1.8/). 

* Type: multilabel (class weighted BCE loss)
  * DISEASE
  * PROCEDURE
  * SYMPTOM
* Head: 3x768 layered dense neural networks with 10% dropout
* Chunking: Span-centered
* Context window: 128 tokens


Token-accuracy: 
```json
{
  "eval_f1_B-DISEASE": {
    "mean": 0.893,
    "median": 0.893,
  },
  "eval_f1_B-PROCEDURE": {
    "mean": 0.873,
    "median": 0.873,
  },
  "eval_f1_B-SYMPTOM": {
    "mean": 0.877,
    "median": 0.877,
  },
  "eval_f1_I-DISEASE": {
    "mean": 0.919,
    "median": 0.919,
  },
  "eval_f1_I-PROCEDURE": {
    "mean": 0.91,
    "median": 0.91,
  },
  "eval_f1_I-SYMPTOM": {
    "mean": 0.898,
    "median": 0.898,
  },
  "eval_f1_O": {
    "mean": 0.954,
    "median": 0.954,
  },
  "eval_f1_macro": {
    "mean": 0.903,
    "median": 0.903,
  },
  "eval_f1_micro": {
    "mean": 0.932,
    "median": 0.932,
  },
  "eval_loss": {
    "mean": 0.092,
    "median": 0.092,
  },
  "eval_precision_B-DISEASE": {
    "mean": 0.897,
    "median": 0.897,
  },
  "eval_precision_B-PROCEDURE": {
    "mean": 0.874,
    "median": 0.874,
  },
  "eval_precision_B-SYMPTOM": {
    "mean": 0.879,
    "median": 0.879,
  },
  "eval_precision_I-DISEASE": {
    "mean": 0.917,
    "median": 0.917,
  },
  "eval_precision_I-PROCEDURE": {
    "mean": 0.916,
    "median": 0.916,
  },
  "eval_precision_I-SYMPTOM": {
    "mean": 0.899,
    "median": 0.899,
  },
  "eval_precision_O": {
    "mean": 0.954,
    "median": 0.954,
  },
  "eval_precision_macro": {
    "mean": 0.905,
    "median": 0.905,
  },
  "eval_precision_micro": {
    "mean": 0.933,
    "median": 0.933,
  },
  "eval_rauc_macro": {
    "mean": 0.943,
    "median": 0.943,
  },
  "eval_rauc_micro": {
    "mean": 0.96,
    "median": 0.96,
  },
  "eval_recall_B-DISEASE": {
    "mean": 0.889,
    "median": 0.889,
  },
  "eval_recall_B-PROCEDURE": {
    "mean": 0.873,
    "median": 0.873,
  },
  "eval_recall_B-SYMPTOM": {
    "mean": 0.876,
    "median": 0.876,
  },
  "eval_recall_I-DISEASE": {
    "mean": 0.92,
    "median": 0.92,
  },
  "eval_recall_I-PROCEDURE": {
    "mean": 0.904,
    "median": 0.904,
  },
  "eval_recall_I-SYMPTOM": {
    "mean": 0.896,
    "median": 0.896,
  },
  "eval_recall_O": {
    "mean": 0.954,
    "median": 0.954,
  },
  "eval_recall_macro": {
    "mean": 0.902,
    "median": 0.902,
  },
  "eval_recall_micro": {
    "mean": 0.931,
    "median": 0.931,
  },
  "eval_roc_auc_B-DISEASE": {
    "mean": 0.943,
    "median": 0.943,
  },
  "eval_roc_auc_B-PROCEDURE": {
    "mean": 0.935,
    "median": 0.935,
  },
  "eval_roc_auc_B-SYMPTOM": {
    "mean": 0.936,
    "median": 0.936,
  },
  "eval_roc_auc_I-DISEASE": {
    "mean": 0.954,
    "median": 0.954,
  },
  "eval_roc_auc_I-PROCEDURE": {
    "mean": 0.947,
    "median": 0.947,
  },
  "eval_roc_auc_I-SYMPTOM": {
    "mean": 0.939,
    "median": 0.939,
  },
  "eval_roc_auc_O": {
    "mean": 0.944,
    "median": 0.944,
  },
  "eval_runtime": {
    "mean": 50.691,
    "median": 50.691,
  },
  "eval_samples_per_second": {
    "mean": 279.142,
    "median": 279.142,
  },
  "eval_steps_per_second": {
    "mean": 34.898,
    "median": 34.898,
  }
}
```

The end-to-end span detection performance, note this depends on your inference pipeline.
```json
{"strict":
 {"per_category": {"DISEASE": {"Precision": 0.74, "Recall": 0.69, "F1": 0.71},
                   "PROCEDURE": {"Precision": 0.71, "Recall": 0.67, "F1": 0.69},
                   "SYMPTOM": {"Precision": 0.67, "Recall": 0.65, "F1": 0.66}},
   "micro": {"Precision": 0.71, "Recall": 0.67, "F1": 0.69},
   "macro": {"Precision": 0.71, "Recall": 0.67, "F1": 0.69}},
"relaxed":
  {"per_category": {"DISEASE": {"Precision": 0.91, "Recall": 0.85, "F1": 0.88},
                    "PROCEDURE": {"Precision": 0.89, "Recall": 0.83, "F1": 0.86},
                    "SYMPTOM": {"Precision": 0.88, "Recall": 0.85, "F1": 0.86}},
   "micro": {"Precision": 0.89, "Recall": 0.84, "F1": 0.87},
   "macro": {"Precision": 0.89, "Recall": 0.84, "F1": 0.87}}
}
```

Also see: [Parallia](https://huggingface.co/Parallia).

If you use this model please cite
```python
@inproceedings{van2026dt4h,
  title={DT4H. nl at\# SMM4H-HeaRD 2026: Multilingual Clinical NER with multilingual and monolingual models},
  author={van Es, Bram},
  booktitle={Proceedings of the 11th Social Media Mining for Health Research and Applications (SMM4H-HeaRD 2026) Workshop and Shared Tasks},
  pages={82--87},
  year={2026}
}
```