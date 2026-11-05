---
title: README
emoji: 🏃
colorFrom: gray
colorTo: purple
sdk: static
pinned: false
tags:
- oxford-legacy
---

# Model Description
DistilClinicalBERT is a distilled version of the [BioClinicalBERT](https://huggingface.co/emilyalsentzer/Bio_ClinicalBERT) model which is distilled for 3 epochs using a total batch size of 192 on the MIMIC-III notes dataset. 

# Distillation Procedure
This model uses a simple distillation technique, which tries to align the output distribution of the student model with the output distribution of the teacher based on the MLM objective. In addition, it optionally uses another alignment loss for aligning the last hidden state of the student and teacher.

# Initialisation
Following [DistilBERT](https://huggingface.co/distilbert-base-uncased?text=The+goal+of+life+is+%5BMASK%5D.), we initialise the student model by taking weights from every other layer of the teacher.

# Architecture
In this model, the size of the hidden dimension and the embedding layer are both set to 768. The vocabulary size is 28996. The number of transformer layers is 6 and the expansion rate of the feed-forward layer is 4. Overall this model has around 65 million parameters.

# Citation
If you use this model, please consider citing the following paper:

```bibtex
@article{rohanian2023lightweight,
  title={Lightweight transformers for clinical natural language processing},
  author={Rohanian, Omid and Nouriborji, Mohammadmahdi and Jauncey, Hannah and Kouchaki, Samaneh and Nooralahzadeh, Farhad and Clifton, Lei and Merson, Laura and Clifton, David A and ISARIC Clinical Characterisation Group and others},
  journal={Natural Language Engineering},
  pages={1--28},
  year={2023},
  publisher={Cambridge University Press}
}
```

# Support
If this model helps your work, you can keep the project running with a one-off or monthly contribution:  
https://github.com/sponsors/nlpie-research