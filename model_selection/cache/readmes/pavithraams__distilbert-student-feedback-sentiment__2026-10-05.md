---
library_name: transformers
base_model: distilbert-base-uncased
pipeline_tag: text-classification
tags: [sentiment-analysis, fine-tuned, distilbert, education]
---
# DistilBERT fine-tuned on student course feedback (Open Elective Project)

`distilbert-base-uncased` fine-tuned to classify student course feedback as **negative / neutral / positive**.

- Dataset: our own student feedback dataset (240 sentences; train 168 / validation 36 / test 36)
- Hyperparameter search: learning rate [5e-05] x batch size [16], 4 epochs, best epoch by validation macro F1
- Best hyperparameters: {'learning_rate': 5e-05, 'batch_size': 16}

## Results (test set)
| Model | Accuracy | Macro F1 |
|---|---|---|
| A. DistilBERT, not fine-tuned | 22.22% | 0.166 |
| B. TF-IDF + LogReg (tuned) | 33.33% | 0.320 |
| C. Frozen DistilBERT + LogReg | 80.56% | 0.806 |
| D. Fine-tuned DistilBERT | 83.33% | 0.832 |

## Usage
```python
from transformers import pipeline
clf = pipeline("text-classification", model="pavithraams/distilbert-student-feedback-sentiment")
print(clf("The labs were really helpful and the teacher explained everything clearly."))
```

## Limitations
Small dataset (240 sentences), so test scores have high variance. Trained on short, English, course-related feedback only.
