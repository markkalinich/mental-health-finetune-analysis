---
library_name: transformers
license: apache-2.0
tags:
- text-classification
- sentiment-analysis
- imdb
- bert
model-index:
- name: imdb-bert-student-0-4798
  results:
  - task:
      type: text-classification
      name: Sentiment Analysis
    dataset:
      name: IMDB
      type: imdb
    metrics:
    - name: accuracy
      type: accuracy
      value: 0.9246
    - name: f1
      type: f1
      value: 0.9246
---

# imdb-bert-student-0-4798

**Checkpoint:** `student_predistill_best_0.4798`  
**Tokenizer source:** `student_merged_0.4656`

Evaluated on IMDB test: accuracy/F1 ≈ **0.9246**.
