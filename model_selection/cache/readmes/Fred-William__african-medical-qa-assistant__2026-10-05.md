---
language: en
library_name: sentence-transformers
license: cc-by-nc-sa-4.0
base_model: sentence-transformers/multi-qa-MiniLM-L6-cos-v1
pipeline_tag: sentence-similarity
---

# African Medical Question Answering Assistant

This repository holds the files that the African Medical Question Answering Assistant loads when it starts. The model
is multi-qa-MiniLM-L6-cos-v1 fine-tuned with the Multiple Negatives Ranking loss on 711 question and answer pairs from
the Short Answer Questions of AfriMed-QA v2.5. The file `assistant_config.json` holds the two confidence thresholds, and
`knowledge_base.csv` holds the 1,205 unique human-written answers that the assistant can return.

The model is intended for educational use only and does not provide medical advice, diagnosis or treatment. The source
code, notebooks and evaluation are available at https://github.com/Adossi-design/African-Medical-Question-Answering-Assistant.
