---
license: apache-2.0
datasets:
- BI55/MedText
language:
- en
metrics:
- accuracy
- f1
base_model:
- google-bert/bert-base-uncased
pipeline_tag: text-classification
library_name: transformers
tags:
- medical
- symptomchecker
- nlp
- healthcare
---
# AI-Powered Symptom Checker 🏥🤖  
This model predicts potential medical conditions based on user-reported symptoms. Built using **BERT** and fine-tuned on the **MedText dataset**, it helps users get preliminary symptom insights.  

## 🔍 Model Details  
- **Model Type:** Text Classification  
- **Base Model:** BERT (`bert-base-uncased`)  
- **Dataset:** MedText (1.4k medical cases)  
- **Metrics:** Accuracy: `96.5%`, F1-score: `95.1%`  
- **Intended Use:** Assist users in identifying possible conditions based on symptoms  
- **Limitations:** Not a replacement for professional medical diagnosis  

## 📖 Usage Example  
```python
from transformers import pipeline

model = pipeline("text-classification", model="Lech-Iyoko/bert-symptom-checker")
result = model("I have a severe headache and nausea.")
print(result)

## 📌 Limitations & Ethical Considerations
- This model should not be used for medical diagnosis. Always consult a healthcare professional.

## 📝 Training Hyperparameters
- Preprocessing: Lowercasing, tokenisation, stopword removal
- Training Framework: Hugging Face transformers
- Training Regime: fp32 (full precision training for stability)
- Batch Size: 16
- Learning Rate: 3e-5
- Epochs: 5
- Optimiser: AdamW
- Scheduler: Linear with warmup

## ⏱ Speeds, Sizes, Times
- Model Checkpoint Size: 4.5GB
- Training Duration: ~3-4 hours on Google Colab
- Throughput: 1200 samples per minute

## 🧪 Evaluation
- Testing Data, Factors & Metrics
- Testing Data
- Dataset: MedText (1.4k samples)
- Dataset Type: Medical symptom descriptions → condition prediction

## Splits:
- Train: 80% (1,120 cases)
- Test: 20% (280 cases)

## Metrics
- Accuracy: 96.5% (measures overall correctness)
- F1-Score: 95.1% (harmonic mean of precision & recall)
- Precision: 94.7% (correct condition predictions out of all predicted)
- Recall: 95.5% (correct condition predictions out of all actual)

## 📊 Results
- Metric	Score
- Accuracy	96.5%
- F1-Score	95.1%
- Precision	94.7%
- Recall	95.5%

## Summary
- Strengths: High recall ensures most conditions are correctly identified.
- Weaknesses: Model might struggle with rare conditions due to dataset limitations.

## ⚙️ Model Architecture & Objective
- Architecture: BERT (bert-base-uncased) fine-tuned for medical text classification.
- Objective: Predict potential conditions/outcomes based on patient symptom descriptions.

💻 Compute Infrastructure
Hardware
- Training: Google Colab (NVIDIA T4 GPU, 16GB RAM)
- Inference: Hugging Face Inference API (optimised for CPU/GPU use)

Software
- Python Version: 3.8
- Deep Learning Framework: PyTorch (transformers library)
- Tokeniser: BERT WordPiece Tokenizer
- Preprocessing Libraries: nltk, spacy, textacy


