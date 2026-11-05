---
library_name: transformers
tags:
- medical
- icd-10
- classification
- biogpt
- clinical-notes
- healthcare
- multi-label
- pytorch
- medical-coding
- discharge-summaries
- clinical-nlp
license: mit
base_model: microsoft/biogpt
pipeline_tag: text-classification
---

# BioGPT for ICD-10 Medical Code Classification

<!-- Advanced BioGPT model fine-tuned for automated ICD-10 medical code classification from clinical discharge summaries -->

This model is a fine-tuned version of microsoft/biogpt specifically designed for automated ICD-10 medical code classification from clinical discharge summaries. The model incorporates advanced attention mechanisms and architectural enhancements for medical text understanding.

## Model Details

### Model Description

<!-- Enhanced BioGPT with cross-attention, hierarchical attention, and medical-specific optimizations -->

This model extends the BioGPT architecture with several medical-specific enhancements including cross-attention between clinical text and ICD code descriptions, hierarchical attention for understanding medical taxonomy, and enhanced classification heads for multi-label prediction.

- **Developed by:** Medhat Ramadan.
- **Shared by [optional]:** Medhat Ramadan.
- **Model type:** Multi-label Text Classification (Medical)
- **Language(s) (NLP):** English (Clinical Text)
- **License:** MIT
- **Finetuned from model [optional]:** microsoft/biogpt

### Model Sources [optional]

<!-- Basic links for the model -->

- **Repository:** https://huggingface.co/Medhatvv/biogpt_icd10_enhanced
<!-- - **Paper [optional]:** [Research paper in preparation]
- **Demo [optional]:** [Available in model repository] -->

## Uses

<!-- Model is intended for research and educational purposes in medical coding automation -->

### Direct Use

<!-- For automated ICD-10 code prediction from discharge summaries -->

This model can be used directly for automated ICD-10 code prediction from clinical discharge summaries. It processes medical text and outputs probability scores for 50 most frequent ICD-10 codes. Intended for research, educational purposes, and as a supportive tool for medical coding professionals.

### Downstream Use [optional]

<!-- Can be fine-tuned for other medical classification tasks or integrated into clinical workflows -->

The model can be fine-tuned for other medical classification tasks, integrated into clinical decision support systems, or used as a component in larger healthcare AI pipelines. It may also serve as a starting point for domain-specific medical coding applications.

### Out-of-Scope Use

<!-- Not for primary medical decision making or replacing professional medical coders -->

This model should NOT be used as the sole basis for medical billing, clinical decision-making, or patient care. It is not intended to replace professional medical coders or clinical judgment. The model should not be used on non-English text or non-clinical documents.

## Bias, Risks, and Limitations

<!-- Technical and sociotechnical limitations of the model -->

The model may exhibit biases present in the MIMIC-IV training dataset, including demographic, institutional, or temporal biases. It is limited to 50 most frequent ICD-10 codes and optimized specifically for discharge summaries. Performance may degrade on other clinical note types or different patient populations.

### Recommendations

<!-- Recommendations for responsible use -->

Users should validate model predictions with professional medical coding expertise. Regular evaluation for bias across different patient demographics is recommended. The model should be used as a supportive tool only, with human oversight for all clinical and billing decisions. Ensure proper data anonymization before processing patient information.

## How to Get Started with the Model

Use the code below to get started with the model.

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load model and tokenizer
model_name = "Medhatvv/biogpt_icd10_enhanced"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Example discharge summary
text = """
CHIEF COMPLAINT: Chest pain and shortness of breath.
HISTORY: 65-year-old male with hypertension and diabetes presents with acute chest pain...
"""

# Predict ICD codes
inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=1024)
with torch.no_grad():
    outputs = model(**inputs)
    predictions = torch.sigmoid(outputs.logits)

# Get codes above threshold
threshold = 0.40
predicted_codes = []
for i, score in enumerate(predictions[0]):
    if score > threshold:
        predicted_codes.append((i, score.item()))
```

## Training Details

### Training Data

<!-- MIMIC-IV discharge summaries with ICD-10 annotations -->

The model was trained on MIMIC-IV discharge summaries with expert ICD-10 annotations. The dataset included 95,537 documents from 53,156 unique patients after filtering for the top 50 most frequent ICD codes. Average document length was 1,420 words with 5.43 codes per document on average.

### Training Procedure

<!-- Technical training specifications -->

#### Preprocessing [optional]

Text was chunked into 1024-token segments with 124-token overlap. Documents were split at the patient level to prevent data leakage. ICD code embeddings were initialized and made learnable during training.

#### Training Hyperparameters

- **Training regime:** Mixed precision (fp16)
- **Learning rate:** 1e-5 with cosine annealing warm restarts
- **Batch size:** 10 per GPU, effective batch size 80 with gradient accumulation
- **Optimizer:** AdamW with weight decay 0.01
- **Epochs:** 31
- **Dropout:** 0.2
- **Gradient clipping:** 1.0
- **Early stopping patience:** 30 epochs

#### Speeds, Sizes, Times [optional]

<!-- Training infrastructure details -->

- **Training time:** ~12 hours on 8x RTX 5070 GPUs
- **Model size:** 1.6B+ parameters
- **Memory usage:** ~45GB GPU memory during training
- **Checkpoint size:** ~3.1GB

## Evaluation

<!-- Evaluation protocols and results -->

### Testing Data, Factors & Metrics

#### Testing Data

<!-- MIMIC-IV test split -->

Evaluation performed on held-out test set from MIMIC-IV with document-level splitting to ensure no patient overlap between train/test sets.

#### Factors

<!-- Evaluation disaggregated by medical factors -->

Evaluation considered performance across different ICD code categories, document lengths, and patient demographics where available.

#### Metrics

<!-- Multi-label classification metrics -->

Standard multi-label classification metrics including F1-micro, F1-macro, precision, recall, and Hamming loss. These metrics are appropriate for medical coding where multiple codes per document are expected.

### Results

Performance metrics on MIMIC-IV test set:
- **F1-Score (Micro):** 74.27%
- **F1-Score (Macro):** 67.91 
- **Precision (Micro):** 74.5%
- **Recall (Micro):** 73.52%
- **Hamming Loss:** 0.0547

#### Summary

The model achieves competitive performance on ICD-10 classification compared to other medical NLP models, with particular strength in handling long clinical documents through its enhanced attention mechanisms.

## Model Examination [optional]

<!-- Interpretability and attention analysis -->

The model includes attention visualization capabilities showing which text segments contribute most to specific ICD code predictions. Cross-attention mechanisms provide interpretable mappings between clinical text and medical codes.

## Environmental Impact

<!-- Carbon footprint and computational considerations -->

Carbon emissions can be estimated using the [Machine Learning Impact calculator](https://mlco2.github.io/impact#compute) presented in [Lacoste et al. (2019)](https://arxiv.org/abs/1910.09700).

- **Hardware Type:** 8x RTX 5070 GPUs
- **Hours used:** ~12 hours
- **Carbon Emitted:** [Estimated based on regional energy mix]

## Technical Specifications [optional]

### Model Architecture and Objective

Enhanced BioGPT with cross-attention between text and ICD embeddings, hierarchical attention for medical taxonomy understanding, attention-based pooling, and ensemble classification heads. Objective is multi-label classification with BCEWithLogitsLoss.

### Compute Infrastructure

#### Hardware

8x RTX 5070 GPUs with distributed data parallel training.

#### Software

PyTorch 2.0, HuggingFace Transformers, CUDA 12.8, mixed precision training with automatic mixed precision.

## Citation [optional]

<!-- Citation information -->

**BibTeX:**

```bibtex
@misc{biogpt-icd10-enhanced-2024,
  title={BioGPT for ICD-10 Medical Code Classification: Enhanced Architecture with Cross-Attention and Hierarchical Learning},
  author={Medhat Ramadan.},
  year={2024},
  howpublished={HuggingFace Model Hub},
  url={https://huggingface.co/Medhatvv/biogpt_icd10_enhanced},
  note={Fine-tuned on MIMIC-IV discharge summaries for automated medical coding}
}
```

**APA:**

Medhat Ramadan. (2024). BioGPT for ICD-10 Medical Code Classification: Enhanced Architecture with Cross-Attention and Hierarchical Learning. HuggingFace Model Hub. https://huggingface.co/Medhatvv/biogpt_icd10_enhanced

## Glossary [optional]

<!-- Medical and technical terms -->

- **ICD-10:** International Classification of Diseases, 10th Revision - standardized medical coding system
- **Discharge Summary:** Clinical document summarizing patient's hospital stay and treatment
- **Cross-Attention:** Attention mechanism between different input modalities (text and ICD codes)
- **MIMIC-IV:** Medical Information Mart for Intensive Care IV - clinical database

## More Information [optional]

For detailed usage examples, advanced configuration options, and integration guides, see the model repository documentation.

## Model Card Authors [optional]

Medhat Ramadan.

## Model Card Contact

For questions or issues, please contact through the HuggingFace model repository or open an issue in the associated GitHub repository.