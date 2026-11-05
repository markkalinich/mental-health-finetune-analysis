---
language:
- ar
license: apache-2.0
library_name: transformers
pipeline_tag: text-classification
tags:
- arabic
- algerian-darija
- sentiment-analysis
- dziribert
- text-classification
- nlp
- transformers
---

# Sentiment Darija 24 BERT

A fine-tuned version of **DziriBERT** for three-class sentiment classification of Algerian Darija text.

The model classifies text into:

- **Negative**
- **Neutral**
- **Positive**

## Model Details

- **Base model:** `alger-ia/dziribert`
- **Model name:** `sent-darija-24-bert`
- **Task:** Algerian Darija sentiment classification
- **Number of classes:** 3
- **Author:** Imen Ourraidji
- **Affiliation:** University of 8 May 1945 , Guelma, Algeria

## Intended Use

This model is intended for research and experimentation in:

- Algerian Darija sentiment analysis
- Arabic dialect NLP
- Sentiment classification
- Transformer-based NLP
- Social media and user-generated text analysis

It can be used as a research baseline or as a component in applications involving sentiment analysis of Algerian Darija text.

## Labels

| ID | Label |
|---:|---|
| 0 | Negative |
| 1 | Neutral |
| 2 | Positive |

## Training

The model was fine-tuned using a three-class Algerian Darija sentiment dataset.

### Training configuration

- Maximum sequence length: **128**
- Batch size: **64**
- Learning rate: **1.5e-5**
- Weight decay: **0.01**
- Number of epochs: **5**
- FP16 training: **Yes**
- Early stopping patience: **1**
- Model selection metric: **Weighted F1**
- Random seed: **42**

### Data augmentation

Data augmentation was applied to the training data only.

The augmentation pipeline included:

- Darija synonym replacement
- Franco/Arabizi spelling variation
- Light word-order variation

The validation and test sets were kept unchanged for evaluation.

## Evaluation

The model was evaluated on a held-out test set of **4,461 samples**.

### Reported results

The results reported in the accompanying research manuscript are:

| Metric | Score |
|---|---:|
| Accuracy | **83.17%** |
| Weighted F1 | **0.8332** |


## Research Context

This model is part of a research project on:

**Error-Analysis-Guided Data Augmentation for Three-Class Algerian Darija Sentiment Classification Using Transformer Models**

The research investigates the use of error analysis and targeted data augmentation to improve sentiment classification for Algerian Darija.

The project compares transformer-based models including:

- DziriBERT
- MARBERT
- BERT-Large-Arabic

DziriBERT was selected as the final model based on the reported evaluation results.

## 🔗 Project Resources

- 📂 **GitHub Research Repository:** https://github.com/ImenOrj/algerian-darija-sentiment-analysis
- 📄 **Research Manuscript:** Available in the GitHub repository

## Limitations

Algerian Darija is highly variable and may contain:

- Arabic script
- Latin script
- Arabizi
- French words
- Code-switching
- Informal spelling
- Regional vocabulary

The model may therefore perform less reliably on text that differs substantially from the training data.

The Neutral class is particularly challenging because some comments may contain mixed or ambiguous sentiment.

This model should be considered a research model rather than a production-ready sentiment-analysis system.

## Ethical Considerations

Sentiment predictions are probabilistic and should not be interpreted as objective judgments about users or individuals.

The model should not be used as the sole basis for high-impact decisions about people.

## Citation

If you use this model in your research, please cite the accompanying research manuscript.

