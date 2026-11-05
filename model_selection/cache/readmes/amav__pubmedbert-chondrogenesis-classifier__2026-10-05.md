---
base_model: microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext
tags:
  - biomedical-nlp
  - gene-regulation
  - chondrogenesis
  - text-classification
  - active-learning
  - pubmedbert
pipeline_tag: text-classification
---

# PubMedBERT Chondrogenesis Regulator Classifier

A fine-tuned [PubMedBERT](https://huggingface.co/microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext) model that classifies whether a gene mentioned in a biomedical sentence is a **regulator of chondrogenesis** (cartilage development). Trained via an active learning loop on curator-annotated PubMed sentences.

This model was developed as part of a pipeline for large-scale literature mining to discover novel candidate regulators of chondrogenesis, combining NLP-based extraction with downstream graph-based machine learning on multi-omics data.

## Model description

- **Base model:** PubMedBERT (abstract + full-text pretraining)
- **Task:** Binary sentence-level classification
- **Classification target:** The gene, not the sentence
- **Training strategy:** Active learning with 6 iterations (150 seed sentences + 100 sentences/iteration), 2 curators annotating, class-weighted loss, and class-weighted acquisition (uncertainty/diversity/random criteria reweighted to surface more positive examples)
- **Stopping criterion:** Validation dataset AUC-ROC ≥ 0.9

## Intended use

Given a sentence mentioning a gene in a biomedical text, predict whether that mention supports the gene being a regulator of chondrogenesis. Intended for large-scale screening of PubMed abstracts to surface candidate regulators for downstream validation (e.g. GO enrichment analysis, graph-based multi-omics modeling), not for standalone clinical or biological ground-truth decisions.

## Training data

Sentences sampled from PubMed abstracts, annotated by 2 curators across 6 active learning iterations. Class imbalance (regulator vs. non-regulator) was addressed both at the model level (class-weighted loss) and the acquisition level (class-weighted sampling on top of uncertainty/diversity/random criteria).

## Performance

**Production model** (train+validation training set, held-out set):
- AUC-ROC: 0.93
- F1: 0.67
- Precision: 0.69
- Recall: 0.66

## Limitations

Decision threshold was not calibrated; evaluated at the default 0.5 cutoff

## Citation

If you use this model, please check the [project Github] (https://github.com/ChondroTextomics/ALRegulatorDiscovery/) for paper citation.