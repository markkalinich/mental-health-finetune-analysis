---
library_name: transformers
license: apache-2.0
base_model: distilbert-base-uncased-finetuned-sst-2-english
tags:
  - sentiment-analysis
  - fine-tuned
  - transformers
  - generated_from_trainer
model-index:
  - name: best_distilbert_model
    results: []
---

# **best_distilbert_model**

## **Model Description**
This model is a fine-tuned version of [distilbert-base-uncased-finetuned-sst-2-english](https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english) on the [Pitchfork Album Reviews dataset](https://huggingface.co/datasets/statworx/pitchfork_album_reviews). The model is designed to classify sentiment in album reviews as **positive (1) or negative (0).**

---

## **Intended Uses & Limitations**
### ✅ **Intended Use**
- **Primary Task:** Sentiment analysis for album reviews.
- **Dataset:** Fine-tuned on **19,305 album reviews** (binary labels: **1 = Positive, 0 = Negative**).
- **Ideal for:** Music review sentiment analysis.

### ⚠️ **Limitations**
- May **not generalize well** to non-music-related reviews.
- Optimized for **binary sentiment classification**, not multi-class sentiment.

---

## **Training & Evaluation Data**
### **Dataset Details**
- **Dataset Source:** [Pitchfork Album Reviews](https://huggingface.co/datasets/statworx/pitchfork_album_reviews)  
- **Training Set Size:** 19,305 reviews  
- **Test Set Size:** 1,566 reviews  
- **Labels:** Binary classification (**0 = Negative, 1 = Positive**)  

### **Evaluation Metrics**
- **Best Test Accuracy:** **73.44%**  
- **Best Generalization Settings:**  
  - **Dropout:** `0.2`  
  - **Learning Rate:** `5e-5`  
  - **Batch Size:** `16`  
  - **Warmup Steps:** `500`  

---

## **Training Procedure**
### **Hyperparameters Used**
- **Learning Rate:** `5e-5`
- **Train Batch Size:** `16`
- **Eval Batch Size:** `16`
- **Epochs:** `2`
- **Weight Decay:** `0.01`
- **Dropout:** `0.2`
- **Optimizer:** AdamW `(betas=(0.9, 0.999), epsilon=1e-08)`
- **LR Scheduler:** `Linear`
- **Warmup Steps:** `500`

### **Framework Versions**
- **Transformers:** `4.48.3`
- **PyTorch:** `2.6.0+cu124`
- **Datasets:** `3.4.1`
- **Tokenizers:** `0.21.1`

---

## Performance Metrics  

- **Best Test Accuracy:** 73.44%  
- **Evaluation Metrics Used:** Accuracy  
- **Generalization Settings:**  
  - **Dropout:** 0.2  
  - **Learning Rate:** 5e-5  
  - **Batch Size:** 16  
  - **Warmup Steps:** 500  
