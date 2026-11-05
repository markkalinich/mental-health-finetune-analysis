---
language:
- en
license: apache-2.0
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- dense
- generated_from_trainer
- dataset_size:7869
- loss:MatryoshkaLoss
- loss:MultipleNegativesRankingLoss
base_model: nomic-ai/nomic-embed-text-v1.5
widget:
- source_sentence: Visual Stimulation Through Video Therapy to Enhance Lower Limb
    Motor Recovery After Stroke Use of Intensive Visual Stimulation Through Video
    Therapy to Enhance Lower Limb Motor Recovery After Stroke (SIVIMI). A Single-Center
    Pilot Study Using a Single-Case Experimental Design (SCED)
  sentences:
  - What is the condition affecting the children participating in this trial?
  - What is the focus of this clinical trial?
  - What is the focus of this clinical trial?
- source_sentence: 'The main objectives of this trial are:


    To assess the mass balance (total recovery of \[14C\]-radioactivity) in urine,
    faeces, and expired air after a single subcutaneous dose of BI 3034701 (C-14)
    in healthy male trial participants.'
  sentences:
  - What age groups are eligible for this clinical trial?
  - What is the disease status for patients eligible for this trial?
  - Who are the participants in this trial?
- source_sentence: This is a multicenter, randomized, phase III non-inferiority trial
    in women aged 40 years or older with clinically node-negative (cN0), pathologically
    pT1 (≤2 cm), grade 1-2, lymphovascular invasion (LVI)-negative invasive breast
    cancer treated with breast-conserving surgery (BCS) in whom sentinel lymph node
    biopsy (SLNB) was omitted (pNx). Eligible patients are randomized 1:1 to partial
    breast irradiation (PBI) or whole breast irradiation (WBI). The primary aim is
    to determine whether PBI is non-inferior to WBI with respect to the 5-year recurrence-free
    survival (RFS) rate. Secondary aims include comparison of axillary recurrence,
    overall survival, locoregional recurrence, treatment-related toxicity, and quality
    of life between arms.
  sentences:
  - What is being compared in terms of recurrence-free survival in this trial?
  - Who are the patients involved in this study?
  - Who are the patients being studied in this clinical trial, those with essential
    hypertension and primary hypercholesterolemia?
- source_sentence: 'The aim of this observational cohort study is to characterise
    use of eplontersen in patients with prior liver transplant or with pre-existing
    severe hepatic impairment, as well as to assess long-term safety among all new
    users of eplontersen; all are areas of missing information


    Primary objectives are:


    1. To describe demographic and clinical characteristics of patients at eplontersen
    initiation, including the prevalence of prior liver transplant (overall and by
    reason for liver transplant), and the prevalence of severe hepatic impairment;
    and to describe patients in these subgroups (prior liver transplant, severe hepatic
    impairment).

    2. To describe long-term safety in patients who initiate eplontersen treatment,
    including onset of new clinical events, abnormal laboratory values and serious
    adverse events.'
  sentences:
  - What is the focus of this clinical trial?
  - What clinical tests are used to assess patients in this trial?
  - What is being studied in this observational cohort study?
- source_sentence: '* 0-12 months of age. (Must be less than 1 year of life for the
    pulse oximeter portion of the study) Weight greater than 2 Kg at time of study

    * Admitted to an intensive care unit. (Not applicable for outpatient cohort)

    * Arterial line in place as standard of care (Not applicable for outpatient cohort)

    * Informed consent provided by parent or LAR.


    '
  sentences:
  - What is the focus of this clinical trial?
  - Are patients with ASA physical status IV excluded from participating in this study?
  - What age group is targeted for this clinical trial?
pipeline_tag: sentence-similarity
library_name: sentence-transformers
metrics:
- cosine_accuracy@1
- cosine_accuracy@3
- cosine_accuracy@5
- cosine_accuracy@10
- cosine_precision@1
- cosine_precision@3
- cosine_precision@5
- cosine_precision@10
- cosine_recall@1
- cosine_recall@3
- cosine_recall@5
- cosine_recall@10
- cosine_ndcg@10
- cosine_mrr@10
- cosine_map@100
model-index:
- name: nomic-embed text-v1.5 Clinical-Trials Matryoshka
  results:
  - task:
      type: information-retrieval
      name: Information Retrieval
    dataset:
      name: dim 768
      type: dim_768
    metrics:
    - type: cosine_accuracy@1
      value: 0.28914285714285715
      name: Cosine Accuracy@1
    - type: cosine_accuracy@3
      value: 0.3702857142857143
      name: Cosine Accuracy@3
    - type: cosine_accuracy@5
      value: 0.3942857142857143
      name: Cosine Accuracy@5
    - type: cosine_accuracy@10
      value: 0.43314285714285716
      name: Cosine Accuracy@10
    - type: cosine_precision@1
      value: 0.28914285714285715
      name: Cosine Precision@1
    - type: cosine_precision@3
      value: 0.12342857142857143
      name: Cosine Precision@3
    - type: cosine_precision@5
      value: 0.07885714285714286
      name: Cosine Precision@5
    - type: cosine_precision@10
      value: 0.043314285714285715
      name: Cosine Precision@10
    - type: cosine_recall@1
      value: 0.28914285714285715
      name: Cosine Recall@1
    - type: cosine_recall@3
      value: 0.3702857142857143
      name: Cosine Recall@3
    - type: cosine_recall@5
      value: 0.3942857142857143
      name: Cosine Recall@5
    - type: cosine_recall@10
      value: 0.43314285714285716
      name: Cosine Recall@10
    - type: cosine_ndcg@10
      value: 0.3588066463064098
      name: Cosine Ndcg@10
    - type: cosine_mrr@10
      value: 0.3353814058956916
      name: Cosine Mrr@10
    - type: cosine_map@100
      value: 0.3406556945903613
      name: Cosine Map@100
  - task:
      type: information-retrieval
      name: Information Retrieval
    dataset:
      name: dim 512
      type: dim_512
    metrics:
    - type: cosine_accuracy@1
      value: 0.2834285714285714
      name: Cosine Accuracy@1
    - type: cosine_accuracy@3
      value: 0.3657142857142857
      name: Cosine Accuracy@3
    - type: cosine_accuracy@5
      value: 0.38971428571428574
      name: Cosine Accuracy@5
    - type: cosine_accuracy@10
      value: 0.42857142857142855
      name: Cosine Accuracy@10
    - type: cosine_precision@1
      value: 0.2834285714285714
      name: Cosine Precision@1
    - type: cosine_precision@3
      value: 0.12190476190476189
      name: Cosine Precision@3
    - type: cosine_precision@5
      value: 0.07794285714285713
      name: Cosine Precision@5
    - type: cosine_precision@10
      value: 0.04285714285714286
      name: Cosine Precision@10
    - type: cosine_recall@1
      value: 0.2834285714285714
      name: Cosine Recall@1
    - type: cosine_recall@3
      value: 0.3657142857142857
      name: Cosine Recall@3
    - type: cosine_recall@5
      value: 0.38971428571428574
      name: Cosine Recall@5
    - type: cosine_recall@10
      value: 0.42857142857142855
      name: Cosine Recall@10
    - type: cosine_ndcg@10
      value: 0.35497901761696793
      name: Cosine Ndcg@10
    - type: cosine_mrr@10
      value: 0.3315569160997733
      name: Cosine Mrr@10
    - type: cosine_map@100
      value: 0.3368151539451454
      name: Cosine Map@100
  - task:
      type: information-retrieval
      name: Information Retrieval
    dataset:
      name: dim 256
      type: dim_256
    metrics:
    - type: cosine_accuracy@1
      value: 0.2651428571428571
      name: Cosine Accuracy@1
    - type: cosine_accuracy@3
      value: 0.35314285714285715
      name: Cosine Accuracy@3
    - type: cosine_accuracy@5
      value: 0.3782857142857143
      name: Cosine Accuracy@5
    - type: cosine_accuracy@10
      value: 0.4217142857142857
      name: Cosine Accuracy@10
    - type: cosine_precision@1
      value: 0.2651428571428571
      name: Cosine Precision@1
    - type: cosine_precision@3
      value: 0.1177142857142857
      name: Cosine Precision@3
    - type: cosine_precision@5
      value: 0.07565714285714287
      name: Cosine Precision@5
    - type: cosine_precision@10
      value: 0.04217142857142857
      name: Cosine Precision@10
    - type: cosine_recall@1
      value: 0.2651428571428571
      name: Cosine Recall@1
    - type: cosine_recall@3
      value: 0.35314285714285715
      name: Cosine Recall@3
    - type: cosine_recall@5
      value: 0.3782857142857143
      name: Cosine Recall@5
    - type: cosine_recall@10
      value: 0.4217142857142857
      name: Cosine Recall@10
    - type: cosine_ndcg@10
      value: 0.34096687945458515
      name: Cosine Ndcg@10
    - type: cosine_mrr@10
      value: 0.3154303854875284
      name: Cosine Mrr@10
    - type: cosine_map@100
      value: 0.3207519101631984
      name: Cosine Map@100
  - task:
      type: information-retrieval
      name: Information Retrieval
    dataset:
      name: dim 128
      type: dim_128
    metrics:
    - type: cosine_accuracy@1
      value: 0.25142857142857145
      name: Cosine Accuracy@1
    - type: cosine_accuracy@3
      value: 0.336
      name: Cosine Accuracy@3
    - type: cosine_accuracy@5
      value: 0.37257142857142855
      name: Cosine Accuracy@5
    - type: cosine_accuracy@10
      value: 0.408
      name: Cosine Accuracy@10
    - type: cosine_precision@1
      value: 0.25142857142857145
      name: Cosine Precision@1
    - type: cosine_precision@3
      value: 0.112
      name: Cosine Precision@3
    - type: cosine_precision@5
      value: 0.07451428571428571
      name: Cosine Precision@5
    - type: cosine_precision@10
      value: 0.040799999999999996
      name: Cosine Precision@10
    - type: cosine_recall@1
      value: 0.25142857142857145
      name: Cosine Recall@1
    - type: cosine_recall@3
      value: 0.336
      name: Cosine Recall@3
    - type: cosine_recall@5
      value: 0.37257142857142855
      name: Cosine Recall@5
    - type: cosine_recall@10
      value: 0.408
      name: Cosine Recall@10
    - type: cosine_ndcg@10
      value: 0.32808986744195817
      name: Cosine Ndcg@10
    - type: cosine_mrr@10
      value: 0.3027133786848072
      name: Cosine Mrr@10
    - type: cosine_map@100
      value: 0.3074793364715046
      name: Cosine Map@100
  - task:
      type: information-retrieval
      name: Information Retrieval
    dataset:
      name: dim 64
      type: dim_64
    metrics:
    - type: cosine_accuracy@1
      value: 0.21828571428571428
      name: Cosine Accuracy@1
    - type: cosine_accuracy@3
      value: 0.2948571428571429
      name: Cosine Accuracy@3
    - type: cosine_accuracy@5
      value: 0.3222857142857143
      name: Cosine Accuracy@5
    - type: cosine_accuracy@10
      value: 0.3668571428571429
      name: Cosine Accuracy@10
    - type: cosine_precision@1
      value: 0.21828571428571428
      name: Cosine Precision@1
    - type: cosine_precision@3
      value: 0.09828571428571428
      name: Cosine Precision@3
    - type: cosine_precision@5
      value: 0.06445714285714287
      name: Cosine Precision@5
    - type: cosine_precision@10
      value: 0.03668571428571429
      name: Cosine Precision@10
    - type: cosine_recall@1
      value: 0.21828571428571428
      name: Cosine Recall@1
    - type: cosine_recall@3
      value: 0.2948571428571429
      name: Cosine Recall@3
    - type: cosine_recall@5
      value: 0.3222857142857143
      name: Cosine Recall@5
    - type: cosine_recall@10
      value: 0.3668571428571429
      name: Cosine Recall@10
    - type: cosine_ndcg@10
      value: 0.28779848319451573
      name: Cosine Ndcg@10
    - type: cosine_mrr@10
      value: 0.2631002267573696
      name: Cosine Mrr@10
    - type: cosine_map@100
      value: 0.2690894932872432
      name: Cosine Map@100
---

# nomic-embed text-v1.5 Clinical-Trials Matryoshka

This is a [sentence-transformers](https://www.SBERT.net) model finetuned from [nomic-ai/nomic-embed-text-v1.5](https://huggingface.co/nomic-ai/nomic-embed-text-v1.5) on the [Clinical_trials_anchor-positive-pairs_EmbeddingModel-data2](https://huggingface.co/datasets/vab46/Clinical_trials_anchor-positive-pairs_EmbeddingModel-data2) dataset. It maps sentences & paragraphs to a 768-dimensional dense vector space and can be used for semantic textual similarity, semantic search, paraphrase mining, classification, clustering, and more.

## Model Details

### Model Description
- **Model Type:** Sentence Transformer
- **Base model:** [nomic-ai/nomic-embed-text-v1.5](https://huggingface.co/nomic-ai/nomic-embed-text-v1.5) <!-- at revision e9b6763023c676ca8431644204f50c2b100d9aab -->
- **Maximum Sequence Length:** 8192 tokens
- **Output Dimensionality:** 768 dimensions
- **Similarity Function:** Cosine Similarity
- **Supported Modality:** Text
- **Training Dataset:** [Clinical_trials_anchor-positive-pairs_EmbeddingModel-data2](https://huggingface.co/datasets/vab46/Clinical_trials_anchor-positive-pairs_EmbeddingModel-data2)
- **Language:** en
- **License:** apache-2.0

### Model Sources

- **Documentation:** [Sentence Transformers Documentation](https://sbert.net)
- **Repository:** [Sentence Transformers on GitHub](https://github.com/huggingface/sentence-transformers)
- **Hugging Face:** [Sentence Transformers on Hugging Face](https://huggingface.co/models?library=sentence-transformers)

### Full Model Architecture

```
SentenceTransformer(
  (0): Transformer({'transformer_task': 'feature-extraction', 'modality_config': {'text': {'method': 'forward', 'method_output_name': 'last_hidden_state'}}, 'module_output_name': 'token_embeddings', 'architecture': 'NomicBertModel'})
  (1): Pooling({'embedding_dimension': 768, 'pooling_mode': 'mean', 'include_prompt': True})
)
```

## Usage

### Direct Usage (Sentence Transformers)

First install the Sentence Transformers library:

```bash
pip install -U sentence-transformers
```
Then you can load this model and run inference.
```python
from sentence_transformers import SentenceTransformer

# Download from the 🤗 Hub
model = SentenceTransformer("vab46/nomic-embed-text-v1.5_Clinical-Trials_Matryoshka2")
# Run inference
documents = [
    '* 0-12 months of age. (Must be less than 1 year of life for the pulse oximeter portion of the study) Weight greater than 2 Kg at time of study\n* Admitted to an intensive care unit. (Not applicable for outpatient cohort)\n* Arterial line in place as standard of care (Not applicable for outpatient cohort)\n* Informed consent provided by parent or LAR.\n\n',
]
queries = [
    'What age group is targeted for this clinical trial?',
    'What is the focus of this clinical trial?',
    'Are patients with ASA physical status IV excluded from participating in this study?',
]
query_embeddings = model.encode_query(queries)
document_embeddings = model.encode_document(documents)
print(query_embeddings.shape, document_embeddings.shape)
# [1, 768] [3, 768]

# Get the similarity scores for the embeddings
similarities = model.similarity(query_embeddings, document_embeddings)
print(similarities)
# tensor([[ 0.4220, -0.1157,  0.1650]])
```
<!--
### Direct Usage (Transformers)

<details><summary>Click to see the direct usage in Transformers</summary>

</details>
-->

<!--
### Downstream Usage (Sentence Transformers)

You can finetune this model on your own dataset.

<details><summary>Click to expand</summary>

</details>
-->

<!--
### Out-of-Scope Use

*List how the model may foreseeably be misused and address what users ought not to do with the model.*
-->

## Evaluation

### Metrics

#### Information Retrieval

* Dataset: `dim_768`, `dim_512`, `dim_256`, `dim_128`, `dim_64`
* Evaluated with [<code>InformationRetrievalEvaluator</code>](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#sentence_transformers.sentence_transformer.evaluation.InformationRetrievalEvaluator) with these parameters:


| Metric              | dim_756 | dim_512 | dim_256 | dim_128 | dim_64 |
| ------------------- | ------- | ------- | ------- | ------- | ------ |
| cosine_accuracy@1   | 0.2891  | 0.2834  | 0.2651  | 0.2514  | 0.2183 |
| cosine_accuracy@3   | 0.3703  | 0.3657  | 0.3531  | 0.336   | 0.2949 |
| cosine_accuracy@5   | 0.3943  | 0.3897  | 0.3783  | 0.3726  | 0.3223 |
| cosine_accuracy@10  | 0.4331  | 0.4286  | 0.4217  | 0.408   | 0.3669 |
| cosine_precision@1  | 0.2891  | 0.2834  | 0.2651  | 0.2514  | 0.2183 |
| cosine_precision@3  | 0.1234  | 0.1219  | 0.1177  | 0.112   | 0.0983 |
| cosine_precision@5  | 0.0789  | 0.0779  | 0.0757  | 0.0745  | 0.0645 |
| cosine_precision@10 | 0.0433  | 0.0429  | 0.0422  | 0.0408  | 0.0367 |
| cosine_recall@1     | 0.2891  | 0.2834  | 0.2651  | 0.2514  | 0.2183 |
| cosine_recall@3     | 0.3703  | 0.3657  | 0.3531  | 0.336   | 0.2949 |
| cosine_recall@5     | 0.3943  | 0.3897  | 0.3783  | 0.3726  | 0.3223 |
| cosine_recall@10    | 0.4331  | 0.4286  | 0.4217  | 0.408   | 0.3669 |
| cosine_ndcg@10      | 0.3588  | 0.355   | 0.341   | 0.3281  | 0.2878 |
| cosine_mrr@10       | 0.3354  | 0.3316  | 0.3154  | 0.3027  | 0.2631 |
| cosine_map@100      | 0.3407  | 0.3368  | 0.3208  | 0.3075  | 0.2691 |


#### Comparison with the baseline model performance on same data

|    | metric       | dimensions | base_value | ft_value | diff     | %change  |
| -- | ------------ | ---------- | ---------- | -------- | -------- | -------- |
| 0  | accuracy@1   | 768        | 0.169143   | 0.288    | 0.118857 | 70.27027 |
| 1  | accuracy@1   | 512        | 0.164571   | 0.282286 | 0.117714 | 71.52778 |
| 2  | accuracy@1   | 256        | 0.162286   | 0.266286 | 0.104    | 64.08451 |
| 3  | accuracy@1   | 128        | 0.139429   | 0.251429 | 0.112    | 80.32787 |
| 4  | accuracy@1   | 64         | 0.123429   | 0.218286 | 0.094857 | 76.85185 |
| 19 | accuracy@10  | 64         | 0.251429   | 0.368    | 0.116571 | 46.36364 |
| 18 | accuracy@10  | 128        | 0.290286   | 0.408    | 0.117714 | 40.55118 |
| 17 | accuracy@10  | 256        | 0.309714   | 0.421714 | 0.112    | 36.16236 |
| 15 | accuracy@10  | 768        | 0.318857   | 0.433143 | 0.114286 | 35.84229 |
| 16 | accuracy@10  | 512        | 0.310857   | 0.428571 | 0.117714 | 37.86765 |
| 5  | accuracy@3   | 768        | 0.261714   | 0.370286 | 0.108571 | 41.48472 |
| 9  | accuracy@3   | 64         | 0.182857   | 0.294857 | 0.112    | 61.25    |
| 6  | accuracy@3   | 512        | 0.251429   | 0.365714 | 0.114286 | 45.45455 |
| 7  | accuracy@3   | 256        | 0.244571   | 0.353143 | 0.108571 | 44.39252 |
| 8  | accuracy@3   | 128        | 0.219429   | 0.336    | 0.116571 | 53.125   |
| 10 | accuracy@5   | 768        | 0.273143   | 0.394286 | 0.121143 | 44.35146 |
| 13 | accuracy@5   | 128        | 0.259429   | 0.373714 | 0.114286 | 44.05286 |
| 12 | accuracy@5   | 256        | 0.268571   | 0.378286 | 0.109714 | 40.85106 |
| 11 | accuracy@5   | 512        | 0.272      | 0.389714 | 0.117714 | 43.27731 |
| 14 | accuracy@5   | 64         | 0.217143   | 0.322286 | 0.105143 | 48.42105 |
| 60 | map@100      | 768        | 0.223553   | 0.340056 | 0.116504 | 52.11472 |
| 64 | map@100      | 64         | 0.166605   | 0.269093 | 0.102488 | 61.51569 |
| 61 | map@100      | 512        | 0.219486   | 0.336243 | 0.116757 | 53.19588 |
| 62 | map@100      | 256        | 0.214226   | 0.321319 | 0.107093 | 49.99074 |
| 63 | map@100      | 128        | 0.193375   | 0.307525 | 0.11415  | 59.03051 |
| 69 | mrr@10       | 64         | 0.162      | 0.263235 | 0.101235 | 62.49115 |
| 68 | mrr@10       | 128        | 0.189027   | 0.302751 | 0.113725 | 60.16329 |
| 67 | mrr@10       | 256        | 0.209354   | 0.316002 | 0.106648 | 50.94157 |
| 66 | mrr@10       | 512        | 0.214169   | 0.330985 | 0.116816 | 54.54395 |
| 65 | mrr@10       | 768        | 0.218709   | 0.33481  | 0.116101 | 53.08479 |
| 71 | ndcg@10      | 512        | 0.237504   | 0.354557 | 0.117054 | 49.28502 |
| 72 | ndcg@10      | 256        | 0.23342    | 0.341389 | 0.107969 | 46.25535 |
| 70 | ndcg@10      | 768        | 0.242732   | 0.358385 | 0.115653 | 47.64648 |
| 73 | ndcg@10      | 128        | 0.213486   | 0.328125 | 0.114639 | 53.69842 |
| 74 | ndcg@10      | 64         | 0.183309   | 0.288149 | 0.10484  | 57.19309 |
| 40 | precision@1  | 768        | 0.169143   | 0.288    | 0.118857 | 70.27027 |
| 41 | precision@1  | 512        | 0.164571   | 0.282286 | 0.117714 | 71.52778 |
| 42 | precision@1  | 256        | 0.162286   | 0.266286 | 0.104    | 64.08451 |
| 43 | precision@1  | 128        | 0.139429   | 0.251429 | 0.112    | 80.32787 |
| 44 | precision@1  | 64         | 0.123429   | 0.218286 | 0.094857 | 76.85185 |
| 59 | precision@10 | 64         | 0.025143   | 0.0368   | 0.011657 | 46.36364 |
| 57 | precision@10 | 256        | 0.030971   | 0.042171 | 0.0112   | 36.16236 |
| 56 | precision@10 | 512        | 0.031086   | 0.042857 | 0.011771 | 37.86765 |
| 55 | precision@10 | 768        | 0.031886   | 0.043314 | 0.011429 | 35.84229 |
| 58 | precision@10 | 128        | 0.029029   | 0.0408   | 0.011771 | 40.55118 |
| 49 | precision@3  | 64         | 0.060952   | 0.098286 | 0.037333 | 61.25    |
| 48 | precision@3  | 128        | 0.073143   | 0.112    | 0.038857 | 53.125   |
| 47 | precision@3  | 256        | 0.081524   | 0.117714 | 0.03619  | 44.39252 |
| 45 | precision@3  | 768        | 0.087238   | 0.123429 | 0.03619  | 41.48472 |
| 46 | precision@3  | 512        | 0.08381    | 0.121905 | 0.038095 | 45.45455 |
| 50 | precision@5  | 768        | 0.054629   | 0.078857 | 0.024229 | 44.35146 |
| 51 | precision@5  | 512        | 0.0544     | 0.077943 | 0.023543 | 43.27731 |
| 52 | precision@5  | 256        | 0.053714   | 0.075657 | 0.021943 | 40.85106 |
| 53 | precision@5  | 128        | 0.051886   | 0.074743 | 0.022857 | 44.05286 |
| 54 | precision@5  | 64         | 0.043429   | 0.064457 | 0.021029 | 48.42105 |
| 23 | recall@1     | 128        | 0.139429   | 0.251429 | 0.112    | 80.32787 |
| 24 | recall@1     | 64         | 0.123429   | 0.218286 | 0.094857 | 76.85185 |
| 22 | recall@1     | 256        | 0.162286   | 0.266286 | 0.104    | 64.08451 |
| 21 | recall@1     | 512        | 0.164571   | 0.282286 | 0.117714 | 71.52778 |
| 20 | recall@1     | 768        | 0.169143   | 0.288    | 0.118857 | 70.27027 |
| 35 | recall@10    | 768        | 0.318857   | 0.433143 | 0.114286 | 35.84229 |
| 39 | recall@10    | 64         | 0.251429   | 0.368    | 0.116571 | 46.36364 |
| 38 | recall@10    | 128        | 0.290286   | 0.408    | 0.117714 | 40.55118 |
| 36 | recall@10    | 512        | 0.310857   | 0.428571 | 0.117714 | 37.86765 |
| 37 | recall@10    | 256        | 0.309714   | 0.421714 | 0.112    | 36.16236 |
| 29 | recall@3     | 64         | 0.182857   | 0.294857 | 0.112    | 61.25    |
| 28 | recall@3     | 128        | 0.219429   | 0.336    | 0.116571 | 53.125   |
| 27 | recall@3     | 256        | 0.244571   | 0.353143 | 0.108571 | 44.39252 |
| 26 | recall@3     | 512        | 0.251429   | 0.365714 | 0.114286 | 45.45455 |
| 25 | recall@3     | 768        | 0.261714   | 0.370286 | 0.108571 | 41.48472 |
| 31 | recall@5     | 512        | 0.272      | 0.389714 | 0.117714 | 43.27731 |
| 30 | recall@5     | 768        | 0.273143   | 0.394286 | 0.121143 | 44.35146 |
| 34 | recall@5     | 64         | 0.217143   | 0.322286 | 0.105143 | 48.42105 |
| 33 | recall@5     | 128        | 0.259429   | 0.373714 | 0.114286 | 44.05286 |
| 32 | recall@5     | 256        | 0.268571   | 0.378286 | 0.109714 | 40.85106 |
|    | AVERAGE      |            |            |          |          | 51.87574 |
|    | VARIANCE     |            |            |          |          | 159.257  |
|    | STD_DEV      |            |            |          |          | 12.61971 |

<!--
## Bias, Risks and Limitations

*What are the known or foreseeable issues stemming from this model? You could also flag here known failure cases or weaknesses of the model.*
-->

<!--
### Recommendations

*What are recommendations with respect to the foreseeable issues? For example, filtering explicit content.*
-->

## Training Details

### Training Dataset

#### json

* Dataset: json
* Size: 7,869 training samples
* Columns: <code>positive</code> and <code>anchor</code>
* Approximate statistics based on the first 100 samples:
  |          | positive                                                                              | anchor                                                                             |
  |:---------|:--------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------|
  | type     | string                                                                                | string                                                                             |
  | modality | text                                                                                  | text                                                                               |
  | details  | <ul><li>min: 11 tokens</li><li>mean: 132.52 tokens</li><li>max: 1135 tokens</li></ul> | <ul><li>min: 10 tokens</li><li>mean: 15.27 tokens</li><li>max: 34 tokens</li></ul> |
* Samples:
  | positive                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | anchor                                                                                       |
  |:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------|
  | <code>* \- Age 18 years or older<br>* Biopsy-proven primary IgA nephropathy or primary focal segmental glomerulosclerosis<br>* Stable kidney function with an estimated glomerular filtration rate greater than 30 mL/min/1.73 m²<br>* Availability of serum and urine samples for soluble CD163 measurement<br>* Availability of relevant demographic, clinical, laboratory, histopathologic, and follow-up data<br>* For the healthy control group: age- and sex-matched individuals without known chronic disease and with normal kidney function<br>* Written informed consent<br><br></code> | <code>What are the specific kidney diseases included in this clinical trial?</code>          |
  | <code>* Written informed consent obtained and documented by the participant's signature.<br>* Age ≥18 years at the time of consent.<br>* Clinically established or suspected diagnosis or recurrence of an oncologic or non-oncologic disease as defined in chapter 7.1 of study protocol.<br>* Availability of standard-of-care imaging (e.g., clinically established PET tracer or anatomical imaging such as CT/MRI) to allow comparative evaluation.<br><br></code>                                                                                                                           | <code>What type of cancer or non-cancerous condition are participants diagnosed with?</code> |
  | <code>* Patients aged 16 years or older at the time of debonding<br>* Treatment plan of extraction or non-extraction followed by straight wire appliances in the upper arch only or both arches<br>* Undergone expansion treatment in the upper arch causing an arch width increase of 3-10mm, either using a Quadhelix, expansion with archwires, or URA with midline screw<br>* Had pretreatment dental cast<br>* Had no chronic medical condition.<br><br></code>                                                                                                                              | <code>What is the minimum age requirement for patients in this clinical trial?</code>        |
* Loss: [<code>MatryoshkaLoss</code>](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#matryoshkaloss) with these parameters:
  ```json
  {
      "loss": "MultipleNegativesRankingLoss",
      "matryoshka_dims": [
          768,
          512,
          256,
          128,
          64
      ],
      "matryoshka_weights": [
          1,
          1,
          1,
          1,
          1
      ],
      "n_dims_per_step": -1
  }
  ```

### Training Hyperparameters
#### Non-Default Hyperparameters

- `num_train_epochs`: 4
- `learning_rate`: 2e-05
- `lr_scheduler_type`: cosine
- `warmup_steps`: 0.1
- `gradient_accumulation_steps`: 4
- `fp16`: True
- `per_device_eval_batch_size`: 32
- `load_best_model_at_end`: True
- `batch_sampler`: no_duplicates

#### All Hyperparameters
<details><summary>Click to expand</summary>

- `per_device_train_batch_size`: 8
- `num_train_epochs`: 4
- `max_steps`: -1
- `learning_rate`: 2e-05
- `lr_scheduler_type`: cosine
- `lr_scheduler_kwargs`: None
- `warmup_steps`: 0.1
- `optim`: adamw_torch_fused
- `optim_args`: None
- `weight_decay`: 0.0
- `adam_beta1`: 0.9
- `adam_beta2`: 0.999
- `adam_epsilon`: 1e-08
- `optim_target_modules`: None
- `gradient_accumulation_steps`: 4
- `average_tokens_across_devices`: True
- `max_grad_norm`: 1.0
- `label_smoothing_factor`: 0.0
- `bf16`: False
- `fp16`: True
- `bf16_full_eval`: False
- `fp16_full_eval`: False
- `tf32`: None
- `gradient_checkpointing`: False
- `gradient_checkpointing_kwargs`: None
- `torch_compile`: False
- `torch_compile_backend`: None
- `torch_compile_mode`: None
- `use_liger_kernel`: False
- `liger_kernel_config`: None
- `use_cache`: False
- `neftune_noise_alpha`: None
- `torch_empty_cache_steps`: None
- `auto_find_batch_size`: False
- `log_on_each_node`: True
- `logging_nan_inf_filter`: True
- `include_num_input_tokens_seen`: no
- `log_level`: passive
- `log_level_replica`: warning
- `disable_tqdm`: False
- `project`: huggingface
- `trackio_space_id`: None
- `trackio_bucket_id`: None
- `trackio_static_space_id`: None
- `per_device_eval_batch_size`: 32
- `prediction_loss_only`: True
- `eval_on_start`: False
- `eval_do_concat_batches`: True
- `eval_use_gather_object`: False
- `eval_accumulation_steps`: None
- `include_for_metrics`: []
- `batch_eval_metrics`: False
- `save_only_model`: False
- `save_on_each_node`: False
- `enable_jit_checkpoint`: False
- `push_to_hub`: False
- `hub_private_repo`: None
- `hub_model_id`: None
- `hub_strategy`: every_save
- `hub_always_push`: False
- `hub_revision`: None
- `load_best_model_at_end`: True
- `ignore_data_skip`: False
- `restore_callback_states_from_checkpoint`: False
- `full_determinism`: False
- `seed`: 42
- `data_seed`: None
- `use_cpu`: False
- `accelerator_config`: {'split_batches': False, 'dispatch_batches': None, 'even_batches': True, 'use_seedable_sampler': True, 'non_blocking': False, 'gradient_accumulation_kwargs': None}
- `parallelism_config`: None
- `dataloader_drop_last`: False
- `dataloader_num_workers`: 0
- `dataloader_pin_memory`: True
- `dataloader_persistent_workers`: False
- `dataloader_prefetch_factor`: None
- `dataloader_multiprocessing_context`: None
- `dataloader_in_order`: True
- `remove_unused_columns`: True
- `label_names`: None
- `train_sampling_strategy`: random
- `length_column_name`: length
- `ddp_find_unused_parameters`: None
- `ddp_bucket_cap_mb`: None
- `ddp_broadcast_buffers`: False
- `ddp_static_graph`: None
- `ddp_backend`: None
- `ddp_timeout`: 1800
- `fsdp`: None
- `fsdp_config`: None
- `deepspeed`: None
- `debug`: []
- `skip_memory_metrics`: True
- `do_predict`: False
- `resume_from_checkpoint`: None
- `local_rank`: -1
- `prompts`: None
- `batch_sampler`: no_duplicates
- `multi_dataset_batch_sampler`: proportional
- `router_mapping`: {}
- `learning_rate_mapping`: {}
- `warmup_ratio`: None

</details>

### Training Logs
<details><summary>Click to expand</summary>

| Epoch   | Step    | Training Loss | dim_768_cosine_ndcg@10 | dim_512_cosine_ndcg@10 | dim_256_cosine_ndcg@10 | dim_128_cosine_ndcg@10 | dim_64_cosine_ndcg@10 |
|:-------:|:-------:|:-------------:|:----------------------:|:----------------------:|:----------------------:|:----------------------:|:---------------------:|
| 0.0407  | 10      | 5.5717        | -                      | -                      | -                      | -                      | -                     |
| 0.0813  | 20      | 4.9373        | -                      | -                      | -                      | -                      | -                     |
| 0.1220  | 30      | 4.5507        | -                      | -                      | -                      | -                      | -                     |
| 0.1626  | 40      | 3.8079        | -                      | -                      | -                      | -                      | -                     |
| 0.2033  | 50      | 2.9460        | -                      | -                      | -                      | -                      | -                     |
| 0.2439  | 60      | 3.1437        | -                      | -                      | -                      | -                      | -                     |
| 0.2846  | 70      | 2.5972        | -                      | -                      | -                      | -                      | -                     |
| 0.3252  | 80      | 2.5577        | -                      | -                      | -                      | -                      | -                     |
| 0.3659  | 90      | 2.5690        | -                      | -                      | -                      | -                      | -                     |
| 0.4065  | 100     | 2.1669        | -                      | -                      | -                      | -                      | -                     |
| 0.4472  | 110     | 2.2879        | -                      | -                      | -                      | -                      | -                     |
| 0.4878  | 120     | 2.6614        | -                      | -                      | -                      | -                      | -                     |
| 0.5285  | 130     | 2.2336        | -                      | -                      | -                      | -                      | -                     |
| 0.5691  | 140     | 2.2764        | -                      | -                      | -                      | -                      | -                     |
| 0.6098  | 150     | 2.3098        | -                      | -                      | -                      | -                      | -                     |
| 0.6504  | 160     | 2.0261        | -                      | -                      | -                      | -                      | -                     |
| 0.6911  | 170     | 2.1120        | -                      | -                      | -                      | -                      | -                     |
| 0.7317  | 180     | 2.1823        | -                      | -                      | -                      | -                      | -                     |
| 0.7724  | 190     | 2.0571        | -                      | -                      | -                      | -                      | -                     |
| 0.8130  | 200     | 1.9998        | -                      | -                      | -                      | -                      | -                     |
| 0.8537  | 210     | 1.5755        | -                      | -                      | -                      | -                      | -                     |
| 0.8943  | 220     | 1.9850        | -                      | -                      | -                      | -                      | -                     |
| 0.9350  | 230     | 1.8681        | -                      | -                      | -                      | -                      | -                     |
| 0.9756  | 240     | 1.6443        | -                      | -                      | -                      | -                      | -                     |
| 1.0     | 246     | -             | 0.3390                 | 0.3358                 | 0.3218                 | 0.3063                 | 0.2723                |
| 1.0163  | 250     | 0.7610        | -                      | -                      | -                      | -                      | -                     |
| 1.0569  | 260     | 1.1679        | -                      | -                      | -                      | -                      | -                     |
| 1.0976  | 270     | 1.4650        | -                      | -                      | -                      | -                      | -                     |
| 1.1382  | 280     | 1.6955        | -                      | -                      | -                      | -                      | -                     |
| 1.1789  | 290     | 1.6553        | -                      | -                      | -                      | -                      | -                     |
| 1.2195  | 300     | 1.6029        | -                      | -                      | -                      | -                      | -                     |
| 1.2602  | 310     | 1.4699        | -                      | -                      | -                      | -                      | -                     |
| 1.3008  | 320     | 1.6808        | -                      | -                      | -                      | -                      | -                     |
| 1.3415  | 330     | 1.7057        | -                      | -                      | -                      | -                      | -                     |
| 1.3821  | 340     | 1.1027        | -                      | -                      | -                      | -                      | -                     |
| 1.4228  | 350     | 1.2826        | -                      | -                      | -                      | -                      | -                     |
| 1.4634  | 360     | 1.7582        | -                      | -                      | -                      | -                      | -                     |
| 1.5041  | 370     | 1.2342        | -                      | -                      | -                      | -                      | -                     |
| 1.5447  | 380     | 1.4462        | -                      | -                      | -                      | -                      | -                     |
| 1.5854  | 390     | 1.2926        | -                      | -                      | -                      | -                      | -                     |
| 1.6260  | 400     | 1.4036        | -                      | -                      | -                      | -                      | -                     |
| 1.6667  | 410     | 1.6060        | -                      | -                      | -                      | -                      | -                     |
| 1.7073  | 420     | 1.3300        | -                      | -                      | -                      | -                      | -                     |
| 1.7480  | 430     | 1.5389        | -                      | -                      | -                      | -                      | -                     |
| 1.7886  | 440     | 1.5757        | -                      | -                      | -                      | -                      | -                     |
| 1.8293  | 450     | 1.6651        | -                      | -                      | -                      | -                      | -                     |
| 1.8699  | 460     | 1.1993        | -                      | -                      | -                      | -                      | -                     |
| 1.9106  | 470     | 1.5296        | -                      | -                      | -                      | -                      | -                     |
| 1.9512  | 480     | 1.4255        | -                      | -                      | -                      | -                      | -                     |
| 1.9919  | 490     | 0.3873        | -                      | -                      | -                      | -                      | -                     |
| 2.0     | 492     | -             | 0.3547                 | 0.3516                 | 0.3373                 | 0.3165                 | 0.2827                |
| 2.0325  | 500     | 0.7046        | -                      | -                      | -                      | -                      | -                     |
| 2.0732  | 510     | 0.6703        | -                      | -                      | -                      | -                      | -                     |
| 2.1138  | 520     | 0.9343        | -                      | -                      | -                      | -                      | -                     |
| 2.1545  | 530     | 1.1007        | -                      | -                      | -                      | -                      | -                     |
| 2.1951  | 540     | 1.0442        | -                      | -                      | -                      | -                      | -                     |
| 2.2358  | 550     | 0.9432        | -                      | -                      | -                      | -                      | -                     |
| 2.2764  | 560     | 0.9315        | -                      | -                      | -                      | -                      | -                     |
| 2.3171  | 570     | 0.8180        | -                      | -                      | -                      | -                      | -                     |
| 2.3577  | 580     | 1.1383        | -                      | -                      | -                      | -                      | -                     |
| 2.3984  | 590     | 0.9215        | -                      | -                      | -                      | -                      | -                     |
| 2.4390  | 600     | 0.7907        | -                      | -                      | -                      | -                      | -                     |
| 2.4797  | 610     | 1.0829        | -                      | -                      | -                      | -                      | -                     |
| 2.5203  | 620     | 0.9923        | -                      | -                      | -                      | -                      | -                     |
| 2.5610  | 630     | 1.0240        | -                      | -                      | -                      | -                      | -                     |
| 2.6016  | 640     | 0.8502        | -                      | -                      | -                      | -                      | -                     |
| 2.6423  | 650     | 0.7081        | -                      | -                      | -                      | -                      | -                     |
| 2.6829  | 660     | 1.0104        | -                      | -                      | -                      | -                      | -                     |
| 2.7236  | 670     | 0.9618        | -                      | -                      | -                      | -                      | -                     |
| 2.7642  | 680     | 1.0599        | -                      | -                      | -                      | -                      | -                     |
| 2.8049  | 690     | 0.8671        | -                      | -                      | -                      | -                      | -                     |
| 2.8455  | 700     | 0.9581        | -                      | -                      | -                      | -                      | -                     |
| 2.8862  | 710     | 0.9968        | -                      | -                      | -                      | -                      | -                     |
| 2.9268  | 720     | 1.0256        | -                      | -                      | -                      | -                      | -                     |
| 2.9675  | 730     | 0.7552        | -                      | -                      | -                      | -                      | -                     |
| 3.0     | 738     | -             | 0.3559                 | 0.3547                 | 0.3395                 | 0.3269                 | 0.2862                |
| 3.0081  | 740     | 0.0859        | -                      | -                      | -                      | -                      | -                     |
| 3.0488  | 750     | 0.8926        | -                      | -                      | -                      | -                      | -                     |
| 3.0894  | 760     | 0.6620        | -                      | -                      | -                      | -                      | -                     |
| 3.1301  | 770     | 0.6895        | -                      | -                      | -                      | -                      | -                     |
| 3.1707  | 780     | 0.7186        | -                      | -                      | -                      | -                      | -                     |
| 3.2114  | 790     | 0.5966        | -                      | -                      | -                      | -                      | -                     |
| 3.2520  | 800     | 0.8555        | -                      | -                      | -                      | -                      | -                     |
| 3.2927  | 810     | 0.4267        | -                      | -                      | -                      | -                      | -                     |
| 3.3333  | 820     | 0.7140        | -                      | -                      | -                      | -                      | -                     |
| 3.3740  | 830     | 0.6585        | -                      | -                      | -                      | -                      | -                     |
| 3.4146  | 840     | 0.4519        | -                      | -                      | -                      | -                      | -                     |
| 3.4553  | 850     | 0.5665        | -                      | -                      | -                      | -                      | -                     |
| 3.4959  | 860     | 0.6698        | -                      | -                      | -                      | -                      | -                     |
| 3.5366  | 870     | 0.6609        | -                      | -                      | -                      | -                      | -                     |
| 3.5772  | 880     | 0.6900        | -                      | -                      | -                      | -                      | -                     |
| 3.6179  | 890     | 0.9147        | -                      | -                      | -                      | -                      | -                     |
| 3.6585  | 900     | 0.8602        | -                      | -                      | -                      | -                      | -                     |
| 3.6992  | 910     | 0.4820        | -                      | -                      | -                      | -                      | -                     |
| 3.7398  | 920     | 0.6155        | -                      | -                      | -                      | -                      | -                     |
| 3.7805  | 930     | 0.8543        | -                      | -                      | -                      | -                      | -                     |
| 3.8211  | 940     | 0.5862        | -                      | -                      | -                      | -                      | -                     |
| 3.8618  | 950     | 0.6409        | -                      | -                      | -                      | -                      | -                     |
| 3.9024  | 960     | 0.8298        | -                      | -                      | -                      | -                      | -                     |
| 3.9431  | 970     | 0.8156        | -                      | -                      | -                      | -                      | -                     |
| 3.9837  | 980     | 0.1714        | -                      | -                      | -                      | -                      | -                     |
| **4.0** | **984** | **-**         | **0.3588**             | **0.355**              | **0.341**              | **0.3281**             | **0.2878**            |

* The bold row denotes the saved checkpoint.
</details>

### Training Time
- **Training**: 26.0 minutes

### Framework Versions
- Python: 3.13.15
- Sentence Transformers: 5.7.0
- Transformers: 5.15.0
- PyTorch: 2.11.0+cu128
- Accelerate: 1.14.0
- Datasets: 4.0.0
- Tokenizers: 0.22.2

## Additional Resources

- [Training and Finetuning Embedding Models with Sentence Transformers](https://huggingface.co/blog/train-sentence-transformers): the end-to-end guide for training or finetuning Sentence Transformer models.
- [Introduction to Matryoshka Embedding Models](https://huggingface.co/blog/matryoshka): variable-size embeddings that can be truncated with minimal quality loss.
- [Binary and Scalar Embedding Quantization for Significantly Faster & Cheaper Retrieval](https://huggingface.co/blog/embedding-quantization): post-training compression of embedding vectors.
- [Multimodal Embedding & Reranker Models with Sentence Transformers](https://huggingface.co/blog/multimodal-sentence-transformers): use text, image, audio, and video models through the same API.
- [Training and Finetuning Multimodal Embedding & Reranker Models with Sentence Transformers](https://huggingface.co/blog/train-multimodal-sentence-transformers): train multimodal embedding models, with a Visual Document Retrieval walkthrough.

## Citation

### BibTeX

#### Sentence Transformers
```bibtex
@inproceedings{reimers-2019-sentence-bert,
    title = "Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks",
    author = "Reimers, Nils and Gurevych, Iryna",
    booktitle = "Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing",
    month = "11",
    year = "2019",
    publisher = "Association for Computational Linguistics",
    url = "https://arxiv.org/abs/1908.10084",
}
```

#### MatryoshkaLoss
```bibtex
@misc{kusupati2024matryoshka,
    title={Matryoshka Representation Learning},
    author={Aditya Kusupati and Gantavya Bhatt and Aniket Rege and Matthew Wallingford and Aditya Sinha and Vivek Ramanujan and William Howard-Snyder and Kaifeng Chen and Sham Kakade and Prateek Jain and Ali Farhadi},
    year={2024},
    eprint={2205.13147},
    archivePrefix={arXiv},
    primaryClass={cs.LG}
}
```

#### MultipleNegativesRankingLoss
```bibtex
@misc{oord2019representationlearningcontrastivepredictive,
      title={Representation Learning with Contrastive Predictive Coding},
      author={Aaron van den Oord and Yazhe Li and Oriol Vinyals},
      year={2019},
      eprint={1807.03748},
      archivePrefix={arXiv},
      primaryClass={cs.LG},
      url={https://arxiv.org/abs/1807.03748},
}
```

<!--
## Glossary

*Clearly define terms in order to be accessible across audiences.*
-->

<!--
## Model Card Authors

*Lists the people who create the model card, providing recognition and accountability for the detailed work that goes into its construction.*
-->

<!--
## Model Card Contact

*Provides a way for people who have updates to the Model Card, suggestions, or questions, to contact the Model Card authors.*
-->