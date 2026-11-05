---
license: mit
language:
- en
tags:
- sentiment-analysis
- imdb
- tinybert
datasets:
- jamander/Blockbuster
model_type: bert
base_model: prajjwal1/bert-tiny
fine_tuned_by: Jack Mander
---

## Project-Blockbuster

### Model Overview

- **Model Name**: Project-Blockbuster  
- **Model Type**: Sentiment Analysis  
- **Base Model**: TinyBERT (`prajjwal1/bert-tiny`)  
- **Fine-tuned by**: Jack Mander  

#### Description:
Project-Blockbuster is a sentiment analysis model fine-tuned on the IMDB Dataset for classifying movie reviews as either "positive" or "negative." It uses the compact TinyBERT architecture to balance performance with computational efficiency, making it suitable for resource-constrained environments.

---

### Model Details

#### Model Architecture:
- **Base Model**: TinyBERT (`prajjwal1/bert-tiny`)  
- **Tokenizer**: AutoTokenizer from Hugging Face Transformers  
- **Training Framework**: Transformers, PEFT, and BitsAndBytes libraries  

#### Training Data:
- The model was fine-tuned using the IMDB Dataset, which contains 50,000 labeled movie reviews.  
- The data was split into training (80%) and test (20%) sets using stratified sampling to maintain label balance.  
- Tokenization was applied with a maximum sequence length of 512 tokens.  

#### Hyperparameters:
- **Learning Rate**: 3e-5  
- **Epochs**: 3  
- **Batch Size**: 16 (with gradient accumulation steps of 2)  
- **Optimizer**: AdamW  
- **Scheduler**: Linear learning rate decay  

---

### Training Procedure

#### Environment:
- The model was trained on a Tesla T4 GPU in Google Colab using mixed precision (FP16) for efficiency.

#### Data Preparation:
1. The IMDB Dataset was preprocessed into training and test sets with stratified sampling.  
2. Text data was tokenized using TinyBERT's tokenizer with truncation and padding.

#### Model Training:
- Fine-tuning was performed using parameter-efficient fine-tuning (PEFT) via LoRA (Low-Rank Adaptation).  
- TinyBERT was quantized to 4-bit precision with the BitsAndBytes library for faster and more memory-efficient training.

---

### Evaluation Metrics

The model achieved the following performance on the IMDB test set:

| **Metric**     | **Score** |
|-----------------|-----------|
| **Accuracy**    | 85%       |
| **Precision**   | 87%       |
| **Recall**      | 83%       |
| **F1-Score**    | 85%       |

---

### Example Predictions

#### Input:
"I absolutely loved this movie. The characters were so well-developed!"

#### Prediction:
**Positive**

#### Input:
"This was one of the worst films I’ve ever seen. I wouldn’t recommend it to anyone."

#### Prediction:
**Negative**

---

### Limitations and Biases
- **Task-Specific**: The model is fine-tuned for movie review sentiment analysis and may not generalize well to other domains or datasets.
- **Data Bias**: Any biases present in the IMDB Dataset, such as overrepresentation of certain styles or phrases, may be reflected in the model's predictions.
- **Resource Constraints**: While TinyBERT is efficient, its smaller size means it may miss subtle nuances in complex reviews compared to larger models like BERT-base.

---

### Acknowledgments
This project was completed to explore the effectiveness of parameter-efficient fine-tuning (PEFT) for compact transformer architectures. Thanks to the Hugging Face and Transformers community for their tools and resources.

---

### Usage

  To use this model, follow these steps:

  1. **Log in to Hugging Face**:
     ```bash
     huggingface-cli login
     ```

  2. **Load the model**:
     ```python
     from transformers import AutoTokenizer, AutoModelForSequenceClassification

     tokenizer = AutoTokenizer.from_pretrained("jamander/Project-Blockbuster")
     model = AutoModelForSequenceClassification.from_pretrained("jamander/Project-Blockbuster")
     ```

  3. **Tokenize and predict**:
     ```python
     inputs = tokenizer("I loved the movie!", return_tensors="pt", padding=True, truncation=True)
     outputs = model(**inputs)
     prediction = torch.argmax(outputs.logits, dim=-1)
     print("Prediction:", "Positive" if prediction == 1 else "Negative")