---
datasets:
- gretelai/symptom_to_diagnosis
language:
- en
- am
- ti
metrics:
- accuracy
base_model:
- FacebookAI/xlm-roberta-base
pipeline_tag: text-classification
library_name: transformers
tags:
- symptom-extraction
- NER
- Amharic
- Tigrinya
- AI4health
---
# Multilingual Symptom Extraction (English + Amharic)

## Model Description
This model is a fine-tuned **XLM-R-base model** for extracting symptoms from patient generated texts in **English and Amharic**. It was developed as part of an MSc thesis at the Technical University of Munich, aiming to support AI-powered symptom extraction platforms in multilingual healthcare settings.

The model performs **named entity recognition (NER)** to identify symptom mentions in unstructured texts using the BIO tagging scheme.
## Intended Uses & Limitations
**Intended uses:**
- Automatic symptom extraction from patient-generated texts in English and Amharic.
- Research in multilingual biomedical NLP.
- Integration into AI diagnostic platforms for low-resource languages.
- **Limitations:**
- Only trained on the datasets described in the thesis; performance on other domains may vary.
- Not validated for real-world clinical deployment without further testing and ethical approval.
- ## Training Data
- Unlabeled English, Amharic, and Tigrinya corpora collected from diverse sources for domain adaptation.
- A combination of publicly available datasets and synthetically generated data, and then labeled, was used for fine-tuning the model.
- Preprocessed with tokenization, normalization, and Docanno BIO tagging.

## Evaluation
- Metrics: Precision, Recall, F1-score for symptom extraction.
- Results and detailed evaluation are described in the MSc thesis:  
  **Negash Desalegn. (2025). *Bridging the Linguistic Gap in Healthcare: A Multilingual AI Approach for Symptom Extraction in Low-Resource Languages*. Technical University of Munich.**

