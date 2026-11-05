---
license: cc-by-nc-sa-4.0
base_model: microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext
tags:
- text-classification
- medical-multimodal-data-curation
- medpmc
---

# MedPMC Initial Screening Model

This model is used in the **initial screening stage** of the MedPMC data curation pipeline. It is a text-based classifier that takes a figure caption and its inline reference text from a PubMed Central article as input and predicts whether the corresponding figure is likely to be a clinically relevant medical image for downstream multimodal data curation.

The model is initialized from [`microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext`](https://huggingface.co/microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext).

## Task

The model performs binary classification.

| Label | Meaning |
|---|---|
| 0 | Non-medical |
| 1 | Medical |

## Input format

This repository corresponds to the **caption only** version of the initial screening model. The input text should concatenate the figure caption and inline reference text using the following format:

```text
"Caption": {figure_caption}
```

## Quick start

```python
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

repo_id = "Yale-BIDS-Chen/medpmc-screening-pubmedbert-caption-only"

tokenizer = AutoTokenizer.from_pretrained(repo_id)
model = AutoModelForSequenceClassification.from_pretrained(repo_id)
model.eval()

caption = "Axial CT image showing a pulmonary nodule in the right upper lobe."

text = '"Caption": ' + caption

inputs = tokenizer(
    text,
    return_tensors="pt",
    truncation=True,
    padding=True,
    max_length=512,
)

with torch.no_grad():
    outputs = model(**inputs)
    probs = torch.softmax(outputs.logits, dim=-1)
    pred = torch.argmax(probs, dim=-1).item()

print("Prediction:", pred)
print("Probabilities:", probs.tolist())
```

## Model Performance

MedPMC includes multiple initial screening variants depending on the input text and model backbone.
The table below summarizes the performance of different screening models evaluated on the MedPMC validation set.

| Model | Input | Precision | Recall | F1 |
|---|---|---:|---:|---:|
| Keyword match | Caption + inline text; Keywords | 70.6 | 62.2 | 61.7 |
| [Bioformer-16L](https://huggingface.co/Yale-BIDS-Chen/medpmc-screening-bioformer-16l-caption-only) | Caption only | 92.2 | 92.3 | 92.2 |
| [Bioformer-16L](https://huggingface.co/Yale-BIDS-Chen/medpmc-screening-bioformer-16l-caption-reference) | Caption + inline text | 93.0 | 92.9 | 92.9 |
| [Bioformer-8L](https://huggingface.co/Yale-BIDS-Chen/medpmc-screening-bioformer-8l-caption-only) | Caption only | 92.3 | 92.3 | 92.3 |
| [Bioformer-8L](https://huggingface.co/Yale-BIDS-Chen/medpmc-screening-bioformer-8l-caption-reference) | Caption + inline text | 92.3 | 92.6 | 92.5 |
| [BioLinkBERT-base](https://huggingface.co/Yale-BIDS-Chen/medpmc-screening-biolinkbert-caption-only) | Caption only | 93.0 | 92.7 | 92.9 |
| [BioLinkBERT-base](https://huggingface.co/Yale-BIDS-Chen/medpmc-screening-biolinkbert-caption-reference) | Caption + inline text | 92.9 | 93.0 | 92.9 |
| **[PubMedBERT-fulltext](https://huggingface.co/Yale-BIDS-Chen/medpmc-screening-pubmedbert-caption-only)** ⭐ **(This model)** | **Caption only** | 92.7 | **93.1** | 92.9 |
| [PubMedBERT-fulltext](https://huggingface.co/Yale-BIDS-Chen/medpmc-screening-pubmedbert-caption-reference) | Caption + inline text | **93.3** | **93.1** | **93.2** |


## License

The model is released for non-commercial research use under CC BY-NC-SA 4.0.


## Citation

```bibtex
@article{kim2026medpmc,
  title={MedPMC: A Systematic Framework for Scaling High-Fidelity Medical Multimodal Data for Foundation Models},
  author={Kim, Hyunjae and Kim, Dain and Xiao, Pan and Applebaum, Serina S and Chung, Younjoon and Ai, Xuguang and Yin, Yu and Jiang, Roy and Du, Yuexi and Wei, Yawen and others},
  journal={arXiv preprint arXiv:2607.07673},
  year={2026}
}
```


## Questions?

For questions or feedback, please contact Hyunjae Kim at ```hyunjae.kim@yale.edu```.