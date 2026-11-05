---
license: apache-2.0
datasets:
- TheBlueScrubs/TheBlueScrubs-v1
language:
- en
metrics:
- accuracy
- r_squared
- mse
base_model:
- answerdotai/ModernBERT-base
pipeline_tag: text-classification
tags:
- medical
- biology
---

![image/png](https://cdn-uploads.huggingface.co/production/uploads/66eb0a4e55940cd564ad8e0a/usrRuzoZO6Rb79DYphdZG.png)

# ModernBERT Medical Relevance Classifier

The **ModernBERT Medical Relevance Classifier** is a transformer-based language model designed to evaluate the *scope of medical relevance* in biomedical texts. Built on top of the **ModernBERT** architecture, it predicts a continuous or near-continuous measure of how closely a text pertains to medical/biological content. This model is particularly suitable for identifying documents that are highly relevant to medical topics, aiding in tasks such as corpus filtering, data triaging, or domain-specific retrieval pipelines.

## Model Details

- **Developed by**: TheBlueScrubs  
- **Model Type**: Transformer-based language model (for regression/classification)  
- **Language**: English  
- **License**: Apache-2.0  
- **Base Model**: [answerdotai/ModernBERT-base](https://huggingface.co/answerdotai/ModernBERT-base)

ModernBERT adopts recent innovations such as **Rotary Positional Embeddings**, **local–global alternating attention**, and **Flash Attention**, which enable both **extended context windows** (up to 8,192 tokens) and more efficient inference.

## Intended Uses & Limitations

### Intended Uses
- **Biomedical Document Filtering**: Identifying which texts are more relevant to medical or biological research.  
- **Data Preprocessing**: Screening large corpora to retain only highly relevant medical content for subsequent tasks (e.g., entity extraction, summarization).

### Limitations
- **Domain Shift**: Trained primarily on biomedical texts, particularly those related to cancer and general medical literature. Relevance scores for out-of-domain texts (e.g., chemistry or physics) may be inaccurate.  
- **Score Interpretation**: The raw output can be a continuous score that may need thresholding or binarization based on your specific application.

## How to Use

Use the Hugging Face Transformers library to load and run this model:

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("TheBlueScrubs/ModernBERT-base-TBS-MedicalRelevance")
model = AutoModelForSequenceClassification.from_pretrained("TheBlueScrubs/ModernBERT-base-TBS-MedicalRelevance")

# Example text
text = "This study discusses the efficacy of a new monoclonal antibody for metastatic breast cancer."

# Tokenize input
inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=4096)

# Get model predictions
outputs = model(**inputs)
predictions = outputs.logits

# Interpret predictions (e.g., a continuous or near-continuous score)
relevance_score = predictions.item()
print(f"Relevance Score: {relevance_score}")
```

## Training Data

A **balanced subset** of The Blue Scrubs dataset was created to ensure coverage across different relevance levels. Each text entry is paired with a *“Scope of Medical Relevance”* score, which served as the regression target. The data preparation steps included:

- Scanning a large corpus of medical documents for valid rows (removing parse/NaN/out-of-range entries).
- Retaining rows with relevance scores spanning 1 (least relevant) to 5 (most relevant).
- Randomly sampling to balance coverage across low- and high-relevance texts.

## Training Procedure

### Preprocessing

- **Tokenizer**: ModernBERT tokenizer, max sequence length = 4,096.  
- **No Additional Filtering**: Data was considered reliable following the basic cleaning steps.

### Training Hyperparameters

- **Learning Rate**: `2e-5`  
- **Number of Epochs**: `3`  
- **Batch Size**: `16` (per device)  
- **Gradient Accumulation Steps**: `1`  
- **Optimizer**: AdamW  
- **Weight Decay**: `0.01`  
- **FP16 Training**: Enabled  
- **Total Training Steps**: ~3 epochs over the balanced set  

The above settings reflect a typical fine-tuning approach with the Hugging Face [Trainer API](https://huggingface.co/docs/transformers/main_classes/trainer). We utilized multiple GPUs in a distributed data-parallel configuration, adjusting for HPC constraints.

## Evaluation

### Testing Data

The final model was evaluated on an **out-of-sample test set** containing documents not seen during training or validation. This test set covers a variety of biomedical topics to ensure generalization.

### Metrics

- **Accuracy** (where applicable, after binarizing or thresholding scores)  
- **R-Squared (r²)**: Evaluates how well the predictions track the true variability in relevance  
- **Mean Squared Error (MSE)**: Quantifies the average squared difference between predicted and true relevance scores

### Results

- **MSE**: ~0.373 on the test set  
- **Accuracy**: 0.9573 

These results suggest that the model reliably assigns a *relevance score* consistent with the ground-truth annotations.

![image/png](https://cdn-uploads.huggingface.co/production/uploads/66eb0a4e55940cd564ad8e0a/seKwZG72NWxU5qYT_u7L2.png)

## Bias, Risks, and Limitations

- **Data Composition**: Certain subdomains may be underrepresented; the model may be less accurate for rare specialties.  
- **Overinterpretation**: A single numeric score does not ensure clinically rigorous validation. Always verify with domain experts.  
- **Shifting Standards**: Medical fields evolve quickly, so re-training or updating data may be necessary to maintain relevance accuracy.

## Recommendations

- **Domain-Specific Check**: If you specialize in a particular area (e.g., pediatrics), consider additional fine-tuning or custom calibration.  
- **Thresholding Strategy**: For binary classification (e.g., “Relevant” vs. “Not relevant”), select an optimal cutoff based on your dataset and tolerance for false positives/negatives.  
- **Continuous Monitoring**: Periodically evaluate new new data to ensure the model remains valid as medical literature grows.

## Citation

If you utilize this model in your research or applications, please cite it as follows:

```bibtex
@misc{thebluescrubs2025modernbert,
  author = {TheBlueScrubs},
  title = {ModernBERT Medical Relevance Classifier},
  year = {2025},
  publisher = {Hugging Face},
  url = {https://huggingface.co/TheBlueScrubs/ModernBERT-base-TBS-MedicalRelevance}
}
```

## Model Card Authors

- TheBlueScrubs Team

--- 