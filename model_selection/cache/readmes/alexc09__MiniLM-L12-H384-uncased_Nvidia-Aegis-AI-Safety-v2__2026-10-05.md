---
datasets:
- nvidia/Aegis-AI-Content-Safety-Dataset-1.0
library_name: transformers
language:
- en
metrics:
- accuracy
- f1
- confusion_matrix
---

# Model Card for AC/MiniLM-L12-H384-uncased_Nvidia-Aegis-AI-Safety-v2
A further finetuned model from AC/MiniLM-L12-H384-uncased_Nvidia-Aegis-AI-Safety.

[`AC/MiniLM-L12-H384-uncased_Nvidia-Aegis-AI-Safety`](https://huggingface.co/AC/MiniLM-L12-H384-uncased_Nvidia-Aegis-AI-Safety) is trained on 50 epochs, while [`AC/MiniLM-L12-H384-uncased_Nvidia-Aegis-AI-Safety-v2`](https://huggingface.co/AC/MiniLM-L12-H384-uncased_Nvidia-Aegis-AI-Safety-v2) is trained on 750 epochs.

## Evaluation
Evaluation is conducted on the test set in nvidia/Aegis-AI-Content-Safety-Dataset-1.0 dataset. A total of 359 examples are in the test set. 

For AI safety use case, having false negatives (text was actually toxic but model predicted it as safe) is worse than having false positives (text was actually safe but model predicted it as unsafe)

Precision: Out of all text predicted as toxic, how many were actually toxic?
Recall: Out of all text that were actually toxic, how many were predicted toxic?

As we want to reduce false negatives, we will focus on recall.  

| Metric      | MiniLM-L12-H384-uncased_Nvidia-Aegis-AI-Safety-v2 (This Version) | MiniLM-L12-H384-uncased_Nvidia-Aegis-AI-Safety (Original Version) |
| :----------- | :----------- | :----------- |
| accuracy      | 0.9532431356943891       | 0.9514524472741743 |
| f1   | 0.6153846153846154        | 0.5325670498084292 |
| precision   | 0.632996632996633        | 0.668269230769 |
| recall   | 0.5987261146496815        | 0.442675159235668 |
| TP   | 4603        | 4643 |
| TN   | 188        | 139 |
| FP   | 109        | 69 |
| FN   | 126        | 175 |