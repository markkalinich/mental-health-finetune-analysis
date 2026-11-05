---
language: "en"
tags:
- bert
- medical
- clinical
thumbnail: "https://core.app.datexis.com/static/paper.png"
---

# CORe Model - BioBERT + Clinical Outcome Pre-Training

## Model description

The CORe (_Clinical Outcome Representations_) model is introduced in the paper [Clinical Outcome Predictions from Admission Notes using Self-Supervised Knowledge Integration](https://www.aclweb.org/anthology/2021.eacl-main.75.pdf).
It is based on BioBERT and further pre-trained on clinical notes, disease descriptions and medical articles with a specialised _Clinical Outcome Pre-Training_ objective.

#### How to use CORe

You can load the model via the transformers library:
```
from transformers import AutoTokenizer, AutoModel
tokenizer = AutoTokenizer.from_pretrained("bvanaken/CORe-clinical-outcome-biobert-v1")
model = AutoModel.from_pretrained("bvanaken/CORe-clinical-outcome-biobert-v1")
```
From there, you can fine-tune it on clinical tasks that benefit from patient outcome knowledge.

### Pre-Training Data

The model is based on [BioBERT](https://huggingface.co/dmis-lab/biobert-v1.1) pre-trained on PubMed data.
The _Clinical Outcome Pre-Training_ included discharge summaries from the MIMIC III training set (specified [here](https://github.com/bvanaken/clinical-outcome-prediction/blob/master/tasks/mimic_train.csv)), medical transcriptions from [MTSamples](https://mtsamples.com/) and clinical notes from the i2b2 challenges 2006-2012. It  further includes ~10k case reports from PubMed Central (PMC), disease articles from Wikipedia and article sections from the [MedQuAd](https://github.com/abachaa/MedQuAD) dataset extracted from NIH websites.

### More Information

For all the details about CORe and contact info, please visit [CORe.app.datexis.com](http://core.app.datexis.com/).

### Cite

```bibtex
@inproceedings{vanaken21,
  author    = {Betty van Aken and
               Jens-Michalis Papaioannou and
               Manuel Mayrdorfer and
               Klemens Budde and
               Felix A. Gers and
               Alexander Löser},
  title     = {Clinical Outcome Prediction from Admission Notes using Self-Supervised
               Knowledge Integration},
  booktitle = {Proceedings of the 16th Conference of the European Chapter of the
               Association for Computational Linguistics: Main Volume, {EACL} 2021,
               Online, April 19 - 23, 2021},
  publisher = {Association for Computational Linguistics},
  year      = {2021},
}
```