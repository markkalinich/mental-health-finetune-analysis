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
- EuroBERT/EuroBERT-610m
pipeline_tag: token-classification
tags:
- medical
---

*It is recommended to use the [XMLR model](https://huggingface.co/UMCU/XLMR_MedicalNER_SYMPTOM_DISEASE_PROCEDURE). The EuroBERT610-model underperforms, perhaps due to the vocabulary being much smaller.*

EuroBERT610 finetuned on the [MultiClinAI](https://temu.bsc.es/MultiClinAI/) [dataset](https://zenodo.org/records/18508039), augmented with the MedMentions translations
by Seinen et al..

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
    "epoch": 10.0,
    "eval_f1_B-DISEASE": 0.6609121501463708,
    "eval_f1_B-PROCEDURE": 0.7025976743490868,
    "eval_f1_B-SYMPTOM": 0.6750720662729842,
    "eval_f1_I-DISEASE": 0.7290676206465515,
    "eval_f1_I-PROCEDURE": 0.7396409865757174,
    "eval_f1_I-SYMPTOM": 0.7087080185020255,
    "eval_f1_O": 0.9139559539210023,
    "eval_f1_macro": 0.732850638630534,
    "eval_f1_micro": 0.8490640262937905,
    "eval_loss": 0.9810428619384766,
    "eval_precision_B-DISEASE": 0.7650430706865974,
    "eval_precision_B-PROCEDURE": 0.7697900632102971,
    "eval_precision_B-SYMPTOM": 0.7951279008438819,
    "eval_precision_I-DISEASE": 0.8077520368073986,
    "eval_precision_I-PROCEDURE": 0.8174088616261684,
    "eval_precision_I-SYMPTOM": 0.7965427607325645,
    "eval_precision_O": 0.8832735742700346,
    "eval_precision_macro": 0.8049911811681346,
    "eval_precision_micro": 0.8589291744048624,
    "eval_rauc_macro": 0.8162681085728037,
    "eval_rauc_micro": 0.9077398009034963,
    "eval_recall_B-DISEASE": 0.581731926985503,
    "eval_recall_B-PROCEDURE": 0.6461936051466747,
    "eval_recall_B-SYMPTOM": 0.5865146136264163,
    "eval_recall_I-DISEASE": 0.6643520283666311,
    "eval_recall_I-PROCEDURE": 0.6753851748800748,
    "eval_recall_I-SYMPTOM": 0.6383204454200827,
    "eval_recall_O": 0.9468466801441315,
    "eval_recall_macro": 0.6770492106527877,
    "eval_recall_micro": 0.8394229154369482,
    "eval_roc_auc_B-DISEASE": 0.7889384157990017,
    "eval_roc_auc_B-PROCEDURE": 0.8212754585670854,
    "eval_roc_auc_B-SYMPTOM": 0.7916429087200422,
    "eval_roc_auc_I-DISEASE": 0.8227301639001992,
    "eval_roc_auc_I-PROCEDURE": 0.8304035430118684,
    "eval_roc_auc_I-SYMPTOM": 0.8082598876123175,
    "eval_roc_auc_O": 0.8506263823991114,
    "eval_runtime": 85.6925,
    "eval_samples_per_second": 180.763,
    "eval_steps_per_second": 22.604
}
```

The end-to-end span detection performanc will be about 0.1 lower, this depends greatly on your inference strategy, see e.g. the inference class in [CardioNER](https://github.com/DataTools4Heart/CardioNER) / [MedNER.nl](https://github.com/UPOD-datascience/MedNER.nl)

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
