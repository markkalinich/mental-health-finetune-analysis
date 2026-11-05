---
language: en
license: apache-2.0
tags:
- biomedical
- rag
- hyde
- information-retrieval
- question-answering
- scifive
datasets:
- miriad
---

# SciFive HyDE Generator (Cardiology Fine Tuned)

## Model Description
This model is a fine-tuned version of **razent/SciFive-base-Pubmed_PMC** for **Hypothetical Document Generation (HyDE)** in biomedical Retrieval-Augmented Generation (RAG) systems.

The model generates domain-specific hypothetical documents from user queries to improve dense retrieval performance and reduce hallucinations.

## Training Data
- Dataset: MIRIAD medical QA dataset
- Specialties:
  - Cardiology
  - Cardiothoracic Surgery
  - Vascular Surgery
- ~15,000 question–answer pairs

## Training Objective
Sequence-to-sequence generation:
