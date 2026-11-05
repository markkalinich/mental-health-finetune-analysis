---
license: agpl-3.0
language:
- en
base_model:
- cambridgeltl/SapBERT-from-PubMedBERT-fulltext
pipeline_tag: feature-extraction
datasets:
- FiscaAI/icd10cm-multilabel-prompt
metrics:
- name: f1 macro
  type: f1
  value: 0.75
- name: recall micro
  type: recall
  value: 0.85
- name: precision micro
  type: precision
  value: 0.74
- name: subset accuracy
  type: set accuracy
  value: 0.4
library_name: transformers
tags:
- icd10
- healthcare
- medical
---

We finetuned the SapBERT encoder model on the synthetic ICD10 set by [FiscaAI](https://huggingface.co/FiscaAI).

We trimmed the ICD10 codes to ```X##```, i.e. we trimmed the dot, and then kept only the ICD10 codes that had more than 1000 occurrences, after which we kept the texts that had at least 
one of the remaining ICD10 codes, this resulted in close to 950 ICD10 codes uses as labels for the finetuning with about 700.000 samples.

We use multilabel finetuning with a head of 3 dense layers, with 10% dropout and GELU activation.

We used class weighting with log smoothing.

TLDR;
* ICD10 trimmed after dot, A10.42 -> A10
* minimum_token_count 16
* minimum_label_count 1000
* sequence_length 256
* log-smoothed class weights
* 3 dense layers, 10% dropout, GELU
* 10 epochs
* batch size 16
* max learning rate 2e-5
* repeated linear warmup (10.000 steps) + cosine decay (50.000 steps) 

When you load this model for feature extraction or classification use 

```python
from transformers import AutoModelForSequenceClassification

model = AutoModelForSequenceClassification.from_pretrained(
    "UMCU/ICD10_classifier_base_English",
    trust_remote_code=True,
)
tokenizer = AutoTokenizer.from_pretrained("UMCU/ICD10_classifier_base_English")
model.eval()

inputs = tokenizer(
    text,
    return_tensors="pt",
    truncation=True,
)

with torch.no_grad():
    features = model(**inputs).logits

```

An approach could be 

```python

def get_feature_vector(text):
    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
    )

    with torch.no_grad():
        features = model(**inputs).logits

    return features.flatten()

def reform(features, how='softmax'):
    if how == 'softmax':
        return torch.nn.functional.softmax(features)
    elif how == 'gumbel':
        return torch.nn.functional.gumbel_softmax(features)
    elif how == 'normalize':
        return torch.nn.functional.normalize(features.reshape(1,-1))

feature_vector = reform(get_feature_vector(text))
```

or with multiple texts

```python

def get_feature_vectors_with_stride(
    texts,
    stride=16,
    max_context_length=128,
    reformer=None
):
    """
    Extract one feature vector per document.

    Long documents are split into overlapping windows.
    Logits from all windows belonging to the same document are averaged.

    Returns:
        Tensor [n_documents, n_features]
    """

    inputs = tokenizer(
        texts,
        return_tensors="pt",
        truncation=True,
        max_length=max_context_length,
        stride=stride,
        return_overflowing_tokens=True,
        padding=True,
    )

    # Maps each generated chunk back to its original document.
    sample_mapping = inputs.pop("overflow_to_sample_mapping")

    inputs = {
        key: value.to(device)
        for key, value in inputs.items()
    }

    with torch.no_grad():
        logits = model(**inputs).logits

    # logits:
    # [n_chunks, n_features]

    sample_mapping = sample_mapping.to(logits.device)

    features = []

    for sample_idx in range(len(texts)):
        mask = sample_mapping == sample_idx

        # Mean over all windows belonging to this document.
        if reformer is None:
            document_features = logits[mask].mean(dim=0)
        else:
            document_features = reform(logits[mask].mean(dim=0).flatten(), how=reformer)

        features.append(document_features)

    return torch.stack(features).cpu()
```



The 
* macro f1 score is 0.75
* micro f1 score is 0.8
* micro precision is 0.74
* micro recall is 0.86
* subset accuracy is 0.4

We suggest to use it primarily for feature extraction or for use as an *explainable* embedder. 
