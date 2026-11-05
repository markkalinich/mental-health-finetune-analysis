---
license: cc-by-nc-4.0
language:
- es
tags:
- simplification
- NER
---

This is a model for **complex word identification (CWI)** of Spanish medical texts, based on the 
[Medical mT5 large model](https://huggingface.co/HiTZ/Medical-mT5-large). 

The model was fine-tuned on a corpus of 225 texts for patients (162575 tokens) to identify **complex words** (**CW**).

**Results (test set)**

| Class |   Precision   |     Recall    |       F1      |    Accuracy   |
|:-----:|:-------------:|:-------------:|:-------------:|:-------------:|
|  CW   | 74.94 (±1.16) | 82.07 (±0.40) | 78.34 (±0.77) | 94.72 (±0.13) |

*Results are the average of 3 experimental rounds.

If you use this model or want to have more details about the experiments and the training details, take a look at our article:

```
@article{2025CWI,
  title={Complex Word Identification for Lexical Simplification in Spanish Texts for Patients},
  author={Ortega-Riba, Federico and Campillos-Llanos, Leonardo and Samy, Doaa},
  journal={Procesamiento del lenguaje natural},
  volume={74},
  year={2025}
}
```


