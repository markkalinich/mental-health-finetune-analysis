---
title: README
emoji: 🏃
colorFrom: gray
colorTo: purple
sdk: static
pinned: false
license: mit
tags:
- oxford-legacy
---

# Model Description
TinyClinicalBERT is a distilled version of the [BioClinicalBERT](https://huggingface.co/emilyalsentzer/Bio_ClinicalBERT) which is distilled for 3 epochs using a total batch size of 192 on the MIMIC-III notes dataset.

# Distillation Procedure
This model uses a unique distillation method called ‘transformer-layer distillation’ which is applied on each layer of the student to align the attention maps and the hidden states of the student with those of the teacher.

# Architecture and Initialisation
This model uses 4 hidden layers with a hidden dimension size and an embedding size of 768 resulting in a total of 15M parameters. Due to the model's small hidden dimension size, it uses random initialisation.

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