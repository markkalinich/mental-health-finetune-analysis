---
library_name: transformers
license: mit
base_model: microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: biorecall-PubMedBERT-NLI
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# biorecall-PubMedBERT-NLI

This model is a fine-tuned version of [microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext](https://huggingface.co/microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext) on synthetic biomedical Natural Language Inference (NLI) dataset
available at [https://huggingface.co/datasets/sharraks97/PubMedQA-synthetic-nli] to classify whether a hypothesis sentence is entailed by, contradicted by, or neutral with respect to a biomedical context.
It achieves the following results on the evaluation set:
- Loss: 0.2108
- Accuracy: 0.9274
- F1 Macro: 0.9054

## Model description

- Base model: microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext  
- Task: Natural Language Inference (3-class classification)  
- Labels: entailment, neutral, contradiction  
- Architecture: cross-encoder classification model 

## Intended uses & limitations

This model can be used to:

- Verify generated biomedical answers against retrieved context  
- Detect hallucinated sentences  
- Score factual consistency in RAG pipelines  
- Support biomedical entailment research  

Example usage:

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

tokenizer = AutoTokenizer.from_pretrained("sharraks97/biorecall-PubMedBERT-NLI")
model = AutoModelForSequenceClassification.from_pretrained("sharraks97/biorecall-PubMedBERT-NLI")

premise = "Biomedical context text"
hypothesis = "Claim sentence"

inputs = tokenizer(premise, hypothesis, return_tensors="pt", truncation=True)
outputs = model(**inputs)
prediction = torch.argmax(outputs.logits, dim=-1)
```

## Training and evaluation

- Accuracy  
- Macro F1-score  

Best model checkpoint selected using validation Macro F1-score.

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 3e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 32
- optimizer: Use adamw_torch_fused with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 4

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1 Macro |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:--------:|
| 0.7412        | 1.0   | 79   | 0.3621          | 0.9078   | 0.8822   |
| 0.3472        | 2.0   | 158  | 0.3379          | 0.9218   | 0.8986   |
| 0.2476        | 3.0   | 237  | 0.2202          | 0.9078   | 0.8840   |
| 0.1514        | 4.0   | 316  | 0.2108          | 0.9274   | 0.9054   |


### Framework versions

- Transformers 4.57.1
- Pytorch 2.9.1+cu128
- Datasets 4.4.1
- Tokenizers 0.22.1

## Limitations

- Trained on synthetic data
- May not generalize beyond biomedical QA
- Sentence-level reasoning only
- Not intended for clinical use

## Author

Rakshit Sharma
Project: BioRecall (Reasoning Enabled and Contradiction Augmented LLM RAG)