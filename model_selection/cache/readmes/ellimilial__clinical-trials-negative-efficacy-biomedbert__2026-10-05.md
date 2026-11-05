---
language: en
license: mit
pipeline_tag: text-classification
tags:
- clinical-trials
- biomedbert
- text-classification
- negative-efficacy
- opentargets
- clinical-trial-stop-reasons
---

# Negative Efficacy Classifier (BiomedBERT)

Base model: `microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext`

This model was fine-tuned to classify whether a clinical trial termination text indicates **negative efficacy / futility / unmet endpoint**.

## Labels
- `0` = not_negative_efficacy
- `1` = negative_efficacy

## Training data
Fine-tuned on the Open Targets dataset `opentargets/clinical_trial_stop_reasons`, introduced in Razuvayevskaya, O., Lopez, I., Dunham, I. et al. *Genetic factors associated with reasons for clinical trial stoppage*. *Nature Genetics* 56, 1862–1867 (2024). https://doi.org/10.1038/s41588-024-01854-z

## Inference note
A suggested operating threshold is stored in `inference_config.json`.

## Text normalisation used
```
def normalise_text(text):
    text = "" if pd.isna(text) else str(text)
    text = text.replace("&amp;", "&")
    text = re.sub(r"\s+", " ", text.strip().lower())
    return text
```
