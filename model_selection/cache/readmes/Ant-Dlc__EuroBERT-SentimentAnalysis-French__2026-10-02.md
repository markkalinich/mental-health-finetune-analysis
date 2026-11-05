---
license: cc-by-nc-4.0
language:
- fr
base_model:
- EuroBERT/EuroBERT-210m
library_name: transformers
pipeline_tag: text-classification
tags:
- sentiment 
- french
- eurobert
- classification
- text
- bert
---

# EuroBERT-Sentiment-Analysis-french

## Usage

```python
from transformers import pipeline

clf = pipeline(
    "text-classification",
    model="Ant-Dlc/EuroBERT-SenimentAnalysis-French",
    truncation=True,
    trust_remote_code=True,
    
)

clf("[text]")
```

## Model description
**EuroBERT-Sentiment-Analysis-french** is a sentiment analysis model for French verbatims answering to the question "Qualification équipement" from an IT satisfaction survey.  
It classifies a given text into three categories:  
- **NEGATIF**  (french for "negative")
- **NEUTRE**   (french for "neutral")
- **POSITIF**  (french for "positive")

The model is based on **EuroBERT (210M parameters)** and has been fine-tuned using **Hugging Face Transformers** and **PyTorch**.  

---

## Training data
The model was trained on approximately 50,000 verbatims from an IT satisfaction survey. Labels were generated using an LLM (Mistral Small 24B, see Ant-Dlc/LLMPrompt-SentimentAnalysis)

⚠️ Notes on the dataset:  
- The dataset is not perfectly balanced between classes.  
- Duplicates were kept when they appeared in the survey (e.g., common responses such as *"basique"* or *"RAS"*).  

---

## Evaluation
For evaluation, **500 verbatims were manually labeled** and compared with the model predictions.  

- To avoid data leakage, any test sample that also appeared in the training set was adjusted.  
  - Example: if the training set contained *10 times* the word "basique" and the test set contained *3 times* the same word, then *7 occurrences* were kept in the training set.
  - We made this choice because the presence of multiple occurrences of the same word reflects the nature of the problem we aim to solve.
    
The confusion matrix below summarizes the results :  

![Confusion Matrix](confusion_matrix.png)

## Observations

- About half of the errors are **subjective** (e.g., the word *"moyen"* classified as **NEUTRAL** instead of **NEGATIVE**).  
- The model sometimes **overweights local negatives** in mixed statements where the overall verdict is positive but followed by specific drawbacks (e.g., *"globalement c’est bien, mais …"*). These should be **POSITIVE** but are often predicted **NEGATIVE**.
- A few rare **misclassifications** occur (**POSITIVE** instead of **NEGATIVE**), but they represent only a small fraction of errors.  

Overall, performance is good and consistent with human judgment, though some ambiguity in labels remains.  




