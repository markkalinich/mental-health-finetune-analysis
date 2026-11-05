---
language:
- en
base_model: google/gemma-3-4b-it
pipeline_tag: text-generation
library_name: transformers
tags:
- psychosis
- schizophrenia
- clinical-nlp
- mental-health
- gemma
- lora
---

## Model description

This model is one of two population-specific models created to study linguistic differences between healthy controls and patients with psychosis. The general idea of the project is to compare both models using perplexity and other language-based signals.
This is the Healthy model for simulating responses from healthy control participants in clinical interviews.

## Training data

The model was trained on question-answer pairs extracted from the Discourse-UWO clinical interview dataset.

## Intended use

This model is intended for research in clinical NLP, language modeling, and psychosis-related speech analysis. It can also be used for experiments with population-specific text generation.

## Limitations

This model is for research purposes only and is not intended for diagnosis or clinical decision-making. The dataset is limited and imbalanced, so outputs may reflect dataset-specific biases.

## Citation

If you use this model, cite the associated thesis documentation:

```bibtex
@misc{cano2026population_modeling_psychosis,
  title={Towards Explainable AI for Psychosis Detection Through Clinical Language Modeling},
  author={Pablo Ramon Cano Ortiz},
  year={2026},
  note={Undergraduate thesis, Universidad Politecnica de Madrid}
}
```