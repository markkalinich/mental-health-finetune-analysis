---
license: apache-2.0
datasets:
- TheBlueScrubs/TheBlueScrubs-v1
language:
- en
metrics:
- accuracy
- r_squared
base_model:
- answerdotai/ModernBERT-base
pipeline_tag: text-classification
tags:
- medical
- biology
---

![image/png](https://cdn-uploads.huggingface.co/production/uploads/66eb0a4e55940cd564ad8e0a/usrRuzoZO6Rb79DYphdZG.png)

# ModernBERT Medical Precision & Factual Detail Regressor

The **ModernBERT Medical Precision & Factual Detail Regressor** is a transformer-based language model that predicts the *level of precision and factual detail* within medical or biological texts. Built upon the **ModernBERT** architecture, this model provides a continuous score (1–5) indicating how precise and factually detailed a given text is. These scores can help users filter, categorize, or prioritize documents based on their informational quality.

## Model Details

- **Model Name**: [TheBlueScrubs/ModernBERT-base-TBS-MedicalPrecision](https://huggingface.co/TheBlueScrubs/ModernBERT-base-TBS-MedicalPrecision)  
- **Developed by**: TheBlueScrubs  
- **Model Type**: Transformer-based language model (regression output)  
- **Language**: English  
- **License**: Apache-2.0  
- **Base Model**: [answerdotai/ModernBERT-base](https://huggingface.co/answerdotai/ModernBERT-base)

This model leverages ModernBERT’s **Rotary Positional Embeddings**, **local–global alternating attention**, and **Flash Attention**, providing extended context windows (up to 8,192 tokens) and fast, memory-efficient inference.

## Intended Uses & Limitations

### Intended Uses
- **Medical/Scientific Document Filtering**: Identify texts with high precision and factual detail to focus on reliable information sources.  
- **Data Curation**: Aid in building high-quality corpora by prioritizing documents that exhibit strong factual rigor.  

### Limitations
- **Domain Shift**: Primarily trained on medical and biological data. May not generalize well to non-medical text or highly specialized domains not covered in the dataset.  
- **Score Interpretation**: The raw regression output (1–5) requires clear thresholds or binning strategies, depending on the downstream application.

## How to Use

You can run inference using the Hugging Face Transformers library as follows:

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("TheBlueScrubs/ModernBERT-base-TBS-MedicalPrecision")
model = AutoModelForSequenceClassification.from_pretrained("TheBlueScrubs/ModernBERT-base-TBS-MedicalPrecision")

# Example text
text = "A recent randomized trial found that combining targeted therapy with immunotherapy improved survival rates for melanoma patients."

# Tokenize input
inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=4096)

# Get model predictions
outputs = model(**inputs)
predictions = outputs.logits

# The model outputs a single continuous score indicating the level of precision & factual detail
precision_score = predictions.item()
print(f"Precision & Factual Detail Score: {precision_score}")
```

## Training Data

A **balanced subset** of The Blue Scrubs dataset was prepared, each text featuring a *“Precision and Factual Detail”* label (1–5). Steps included:

- **Data Cleaning**: Removed rows with parsing errors, NaNs, or out-of-range values.  
- **Balancing**: Ensured a roughly even distribution of documents across lower and higher precision scores.  

## Training Procedure

### Preprocessing
- **Tokenizer**: ModernBERT tokenizer with a maximum sequence length of 4,096.  
- No additional filtering beyond standard data cleaning.

### Training Hyperparameters

- **Learning Rate**: `2e-5`  
- **Number of Epochs**: `5`  
- **Batch Size**: `16` (per device)  
- **Gradient Accumulation Steps**: `1`  
- **Optimizer**: AdamW  
- **Weight Decay**: `0.01`  
- **FP16 Training**: Enabled  
- **Total Training Steps**: ~5 epochs on the balanced set  

Training used multi-GPU distributed data parallelism, with frequent evaluations (1/5 epoch) based on the `mse` metric.

## Evaluation

### Testing Data

The final model was evaluated on an out-of-sample test set. This dataset contained medical documents not included in the training or validation splits.

### Metrics

- **Mean Squared Error (MSE)**: ~0.5671  
- **Accuracy** (with threshold ≤ 2.0 for “low precision” vs. > 2.0): 0.9630  
- **ROC Analysis**: Demonstrated robust classification capability with high True Positive Rates and low False Positive Rates.

![image/png](https://cdn-uploads.huggingface.co/production/uploads/66eb0a4e55940cd564ad8e0a/e0WXu-Oa0w78GS25NqOL1.png)

## Bias, Risks, and Limitations

- **Data Bias**: Underrepresented subfields or rare document types may impact performance.  
- **Misinterpretation**: A single numeric score is not a guarantee of clinical accuracy or evidence-based correctness.  
- **Domain Evolution**: Medical knowledge evolves quickly; periodic retraining or re-validation is recommended.

## Recommendations

- **Domain-Specific Adjustments**: Consider further fine-tuning if applying to highly specialized medical subdomains.  
- **Score Thresholding**: Set context-appropriate cutoffs or categories (e.g., “low,” “moderate,” “high” precision) based on your downstream needs.  
- **Continuous Monitoring**: Maintain up-to-date evaluations as new data or medical findings emerge.

## Citation

If you utilize this model in your research or applications, please cite it as follows:

```bibtex
@misc{thebluescrubs2025modernbert,
  author = {TheBlueScrubs},
  title = {ModernBERT Medical Precision & Factual Detail Regressor},
  year = {2025},
  publisher = {Hugging Face},
  url = {https://huggingface.co/TheBlueScrubs/ModernBERT-base-TBS-MedicalPrecision}
}
```

## Model Card Authors

- TheBlueScrubs Team