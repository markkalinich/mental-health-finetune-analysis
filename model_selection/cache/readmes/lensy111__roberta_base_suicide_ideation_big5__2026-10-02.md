---
license: mit
base_model:
- FacebookAI/roberta-base
pipeline_tag: text-classification
---

# Model Card: RoBERTa + Personality + NLI for Suicide Ideation Detection

## Model Overview

This model detects suicidal ideation in social media posts while reducing false positives from supportive, awareness, and preventive content.

It extends a standard transformer-based classifier by incorporating:
- Psycholinguistic signals (Big Five personality traits)
- Natural Language Inference (NLI) for intent refinement

The goal is to improve **intent-aware suicide ideation detection**, not just keyword-based classification.

---

## Model Details

- **Base Model:** RoBERTa  
- **Enhancements:**
  - Big Five personality traits (Neuroticism, Extraversion, Agreeableness)
  - NLI-based post-classification filtering
- **Input:** Social media text (Reddit-style posts)
- **Output:** Binary classification  
  - Suicidal Ideation  
  - Non-suicidal content  

---

## Intended Use

This model is designed for research in:

- Suicide ideation detection
- Mental health NLP systems
- False positive reduction in safety-critical classifiers
- Intent-aware text classification

**Not intended for clinical diagnosis or autonomous decision-making.**

---

## Key Contribution

Most existing datasets label suicide-related content uniformly, leading to misclassification of:

- Supportive posts  
- Awareness campaigns  
- Preventive discussions  

This model addresses that issue through:

- Personality-aware representation learning  
- NLI-based intent filtering to distinguish discussion vs personal ideation  

---

## Performance Summary

Evaluated on standard and supportive-content false positive benchmarks:

- **F1-score:** 0.94  
- **Accuracy:** 94%  
- **False Positive Rate (Supportive Content):** 14.61%

Notable improvement over baseline transformer models in reducing misclassification of non-ideation content.

---

## Live Demo

Try the interactive demo here:

👉 https://huggingface.co/spaces/lensy111/roberta_suicide_ideation_personality_nli

---


## Related Resources

- Dataset: https://huggingface.co/datasets/lensy111/relabelled-suicide-ideation  
- Github: https://github.com/sylen111/Suicide-Ideation-Detection-Project
- Live Demo: https://huggingface.co/spaces/lensy111/roberta_suicide_ideation_personality_nli  