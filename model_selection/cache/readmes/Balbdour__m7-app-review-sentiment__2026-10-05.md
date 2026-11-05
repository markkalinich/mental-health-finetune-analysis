---
library_name: transformers
tags:
- text-classification
- sentiment-analysis
- distilbert
---
 
# Model Card for m7-app-review-sentiment
 
DistilBERT fine-tuned on the AARSynth app reviews dataset for 3-class sentiment classification (negative, neutral, positive).
 
## Model Details
 
### Model Description
 
- **Developed by:** Bashar Albdour
- **Funded by [optional]:** N/A
- **Shared by [optional]:** Bashar Albdour
- **Model type:** Text Classification
- **Language(s) (NLP):** English
- **License:** apache-2.0
- **Finetuned from model:** distilbert-base-uncased
### Model Sources [optional]
 
- **Repository:** https://huggingface.co/Balbdour/m7-app-review-sentiment
- **Paper [optional]:** N/A
- **Demo [optional]:** N/A
## Uses
 
### Direct Use
 
3-class sentiment classification (negative, neutral, positive) of app reviews in English.
 
### Downstream Use [optional]
 
Can be plugged into review analysis pipelines to automatically tag user feedback by sentiment.
 
### Out-of-Scope Use
 
Not suitable for languages other than English, or domains far from app reviews such as medical or legal text.
 
## Bias, Risks, and Limitations
 
The model was trained on reviews from 9 specific apps and may not generalize well to other app categories. Neutral sentiment is the hardest class to identify (F1=0.499), and the model tends to confuse neutral reviews with both negative and positive classes.
 
### Recommendations
 
Use with caution on short or mixed-sentiment reviews. Human review is recommended for borderline predictions.
 
## How to Get Started with the Model
 
Use the code below to get started with the model.
 
```python
from transformers import pipeline
classifier = pipeline("text-classification", model="Balbdour/m7-app-review-sentiment")
result = classifier("This app is great!")
print(result)
```
 
## Training Details
 
### Training Data
 
AARSynth app reviews dataset — 7,472 reviews across 9 apps with 3 sentiment classes (negative, neutral, positive), split 80/20 into 5,977 training and 1,495 test examples using seed=42.
 
### Training Procedure
 
#### Preprocessing
 
Text was tokenized using the `distilbert-base-uncased` tokenizer with truncation at max_length=128. Dynamic padding was applied at training time via `DataCollatorWithPadding`.
 
#### Training Hyperparameters
 
- **Training regime:** fp32
- Learning rate: 5e-5
- Epochs: 2
- Batch size: 8
- Max length: 128
- Seed: 42
#### Speeds, Sizes, Times
 
- Training time: ~31 minutes on CPU (no GPU)
- Checkpoint size: ~265 MB
## Evaluation
 
### Testing Data, Factors & Metrics
 
#### Testing Data
 
1,495 held-out app reviews from the same AARSynth dataset.
 
#### Factors
 
Evaluation is disaggregated by sentiment class: negative, neutral, positive.
 
#### Metrics
 
Accuracy, Macro-F1, and per-class F1, Precision, and Recall.
 
### Results
 
| Metric | Value |
|---|---|
| Accuracy | 0.6428 |
| Macro-F1 | 0.6412 |
 
| Class | F1 | Precision | Recall |
|---|---|---|---|
| Negative | 0.7101 | 0.7211 | 0.6994 |
| Neutral | 0.4990 | 0.4755 | 0.5248 |
| Positive | 0.7144 | 0.7380 | 0.6923 |
 
#### Summary
 
The model performs well on negative and positive classes but struggles with neutral sentiment, which is the most ambiguous class.
 
## Environmental Impact
 
- **Hardware Type:** CPU (no GPU)
- **Hours used:** ~0.5 hours
- **Cloud Provider:** None (local)
- **Compute Region:** N/A
- **Carbon Emitted:** Minimal
## Technical Specifications
 
### Model Architecture and Objective
 
DistilBERT with a sequence classification head (3 output labels). Fine-tuned end-to-end on app review sentiment.
 
### Compute Infrastructure
 
#### Hardware
 
Local CPU (no GPU accelerator)
 
#### Software
 
- transformers>=4.41,<5.0
- datasets>=2.14,<3.0
- torch>=2.0,<3.0
- scikit-learn>=1.3
## Model Card Authors
 
Bashar Albdour
 
## Model Card Contact
 
https://huggingface.co/Balbdour