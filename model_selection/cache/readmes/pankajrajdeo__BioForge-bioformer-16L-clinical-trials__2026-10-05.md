---
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- generated_from_trainer
- dataset_size:3977498
- loss:CachedMultipleNegativesRankingLoss
widget:
- source_sentence: While the prevalence of smoking in the United States general population
    has declined over the past 50 years, there has been little to no decline among
    people with mental health conditions. Affective Disorders (ADs) are the most common
    mental health conditi
  sentences:
  - The purpose of this study is to evaluate safety, tolerability and efficacy of
    BZ371B in intubated patients with severe Acute Respiratory Distress Syndrome.
  - Cigarettes Per Day, Cigarettes per day will be assessed for use of cigarettes
    with different nicotine content., 16 weeks
  - 'RADIATION: CyberKnife Stereotactic Radiosurgery'
- source_sentence: A Study to Assess the Effect of a Normal vs. High Protein Diets
    in Carbohydrates Metabolism in Obese Subjects With Diabetes or Prediabetes
  sentences:
  - 'DIETARY_SUPPLEMENT: Weight Loss'
  - Parkinson's Disease
  - The objective of the study is to assess the effect of low-calorie diets with normal
    (18%) vs. high (35%) protein (mainly coming from animal source) composition on
    body weight and carbohydrates metabolism in overweight and obese subjects with
    pre-diabetes o
- source_sentence: In developed countries, stroke is the third leading cause of death
    and the leading cause of permanent disability. Systemic and endovascular thrombolytic
    treatments in acute cerebral ischemic stroke caused by occlusion of large caliber
    vessels are currently
  sentences:
  - Stroke|Endovascular Thrombectomy|Ischemic Stroke
  - D2 receptor occupancy, To determine whether additional D2 receptor occupancy can
    be accomplished with doses of 160 mg of lurasidone per day., Up to 6 weeks
  - headache frequency, headache days, 12 week
- source_sentence: Adjunctive Oral Hygiene Aids in Reducing Oral Hygiene Parameters
    Among Orthodontic Patients
  sentences:
  - Work of breathing
  - Gingival Bleeding|Dental Plaque Accumulation
  - Hemodialysis|Metabolic Syndrome X|Insulin Resistance
- source_sentence: Gaucher Disease
  sentences:
  - Pregnancy Complications|Gestational Diabetes|Obstetric Labor Complications|Neurodevelopmental
    Disorders|Childhood Obesity
  - Premenstrual Syndrome (PMS)
  - 'OTHER: Digital Engagement Application (GD App)|OTHER: No Intervention'
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
- name: SentenceTransformer
  results:
  - task:
      type: information-retrieval
      name: Information Retrieval
    dataset:
      name: ct pubmed clean eval
      type: ct-pubmed-clean-eval
    metrics:
    - type: cosine_accuracy@1
      value: 0.6569362716818584
      name: Cosine Accuracy@1
    - type: cosine_accuracy@3
      value: 0.7522402984500596
      name: Cosine Accuracy@3
    - type: cosine_accuracy@5
      value: 0.7922387600476904
      name: Cosine Accuracy@5
    - type: cosine_accuracy@10
      value: 0.8404676743202184
      name: Cosine Accuracy@10
    - type: cosine_precision@1
      value: 0.6569362716818584
      name: Cosine Precision@1
    - type: cosine_precision@3
      value: 0.28274553542812453
      name: Cosine Precision@3
    - type: cosine_precision@5
      value: 0.185777470097304
      name: Cosine Precision@5
    - type: cosine_precision@10
      value: 0.10339602322987579
      name: Cosine Precision@10
    - type: cosine_recall@1
      value: 0.5430221548255469
      name: Cosine Recall@1
    - type: cosine_recall@3
      value: 0.6531362790300814
      name: Cosine Recall@3
    - type: cosine_recall@5
      value: 0.6998681289242362
      name: Cosine Recall@5
    - type: cosine_recall@10
      value: 0.7595522516007772
      name: Cosine Recall@10
    - type: cosine_ndcg@10
      value: 0.6889243452744613
      name: Cosine Ndcg@10
    - type: cosine_mrr@10
      value: 0.7148324881277467
      name: Cosine Mrr@10
    - type: cosine_map@100
      value: 0.6491783814844273
      name: Cosine Map@100
---

# SentenceTransformer

This is a [sentence-transformers](https://www.SBERT.net) model trained. It maps sentences & paragraphs to a 384-dimensional dense vector space and can be used for semantic textual similarity, semantic search, paraphrase mining, text classification, clustering, and more.

## Model Details

### Model Description
- **Model Type:** Sentence Transformer
<!-- - **Base model:** [Unknown](https://huggingface.co/unknown) -->
- **Maximum Sequence Length:** 256 tokens
- **Output Dimensionality:** 384 dimensions
- **Similarity Function:** Cosine Similarity
<!-- - **Training Dataset:** Unknown -->
<!-- - **Language:** Unknown -->
<!-- - **License:** Unknown -->

### Model Sources

- **Documentation:** [Sentence Transformers Documentation](https://sbert.net)
- **Repository:** [Sentence Transformers on GitHub](https://github.com/UKPLab/sentence-transformers)
- **Hugging Face:** [Sentence Transformers on Hugging Face](https://huggingface.co/models?library=sentence-transformers)

### Full Model Architecture

```
SentenceTransformer(
  (0): Transformer({'max_seq_length': 256, 'do_lower_case': False}) with Transformer model: BertModel 
  (1): Pooling({'word_embedding_dimension': 384, 'pooling_mode_cls_token': False, 'pooling_mode_mean_tokens': True, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False, 'pooling_mode_weightedmean_tokens': False, 'pooling_mode_lasttoken': False, 'include_prompt': True})
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
model = SentenceTransformer("pankajrajdeo/BioForge-bioformer-16L-clinical-trials")
# Run inference
sentences = [
    'Gaucher Disease',
    'OTHER: Digital Engagement Application (GD App)|OTHER: No Intervention',
    'Pregnancy Complications|Gestational Diabetes|Obstetric Labor Complications|Neurodevelopmental Disorders|Childhood Obesity',
]
embeddings = model.encode(sentences)
print(embeddings.shape)
# [3, 384]

# Get the similarity scores for the embeddings
similarities = model.similarity(embeddings, embeddings)
print(similarities.shape)
# [3, 3]
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

* Dataset: `ct-pubmed-clean-eval`
* Evaluated with [<code>InformationRetrievalEvaluator</code>](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#sentence_transformers.evaluation.InformationRetrievalEvaluator)

| Metric              | Value      |
|:--------------------|:-----------|
| cosine_accuracy@1   | 0.6569     |
| cosine_accuracy@3   | 0.7522     |
| cosine_accuracy@5   | 0.7922     |
| cosine_accuracy@10  | 0.8405     |
| cosine_precision@1  | 0.6569     |
| cosine_precision@3  | 0.2827     |
| cosine_precision@5  | 0.1858     |
| cosine_precision@10 | 0.1034     |
| cosine_recall@1     | 0.543      |
| cosine_recall@3     | 0.6531     |
| cosine_recall@5     | 0.6999     |
| cosine_recall@10    | 0.7596     |
| **cosine_ndcg@10**  | **0.6889** |
| cosine_mrr@10       | 0.7148     |
| cosine_map@100      | 0.6492     |

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

#### Unnamed Dataset

* Size: 3,977,498 training samples
* Columns: <code>anchor</code> and <code>positive</code>
* Approximate statistics based on the first 1000 samples:
  |         | anchor                                                                            | positive                                                                           |
  |:--------|:----------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------|
  | type    | string                                                                            | string                                                                             |
  | details | <ul><li>min: 3 tokens</li><li>mean: 31.98 tokens</li><li>max: 75 tokens</li></ul> | <ul><li>min: 3 tokens</li><li>mean: 30.28 tokens</li><li>max: 102 tokens</li></ul> |
* Samples:
  | anchor                                                                                                                                                                                                                                                                        | positive                                                                                                                                                                                                                                                                      |
  |:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | <code>Kinesiotape for Edema After Bilateral Total Knee Arthroplasty</code>                                                                                                                                                                                                    | <code>The purpose of this study is to determine if kinesiotaping for edema management will decrease post-operative edema in patients with bilateral total knee arthroplasty. The leg receiving kinesiotaping during inpatient rehabilitation may have decreased edema </code> |
  | <code>Kinesiotape for Edema After Bilateral Total Knee Arthroplasty</code>                                                                                                                                                                                                    | <code>Arthroplasty Complications|Arthroplasty, Replacement, Knee</code>                                                                                                                                                                                                       |
  | <code>The purpose of this study is to determine if kinesiotaping for edema management will decrease post-operative edema in patients with bilateral total knee arthroplasty. The leg receiving kinesiotaping during inpatient rehabilitation may have decreased edema </code> | <code>Change from baseline and during 1-2-day time intervals of circumferences of both knees and lower extremities, Bilateral circumferences, in centimeters, at the following points: 10 cm above the superior pole of the patella; middle of the knee joint; calf ci</code> |
* Loss: [<code>CachedMultipleNegativesRankingLoss</code>](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#cachedmultiplenegativesrankingloss) with these parameters:
  ```json
  {
      "scale": 20.0,
      "similarity_fct": "cos_sim"
  }
  ```

### Training Hyperparameters
#### Non-Default Hyperparameters

- `eval_strategy`: steps
- `per_device_train_batch_size`: 512
- `learning_rate`: 2e-05
- `lr_scheduler_type`: cosine
- `warmup_ratio`: 0.05
- `bf16`: True
- `dataloader_num_workers`: 16
- `load_best_model_at_end`: True
- `gradient_checkpointing`: True

#### All Hyperparameters
<details><summary>Click to expand</summary>

- `overwrite_output_dir`: False
- `do_predict`: False
- `eval_strategy`: steps
- `prediction_loss_only`: True
- `per_device_train_batch_size`: 512
- `per_device_eval_batch_size`: 8
- `per_gpu_train_batch_size`: None
- `per_gpu_eval_batch_size`: None
- `gradient_accumulation_steps`: 1
- `eval_accumulation_steps`: None
- `torch_empty_cache_steps`: None
- `learning_rate`: 2e-05
- `weight_decay`: 0.0
- `adam_beta1`: 0.9
- `adam_beta2`: 0.999
- `adam_epsilon`: 1e-08
- `max_grad_norm`: 1.0
- `num_train_epochs`: 3
- `max_steps`: -1
- `lr_scheduler_type`: cosine
- `lr_scheduler_kwargs`: {}
- `warmup_ratio`: 0.05
- `warmup_steps`: 0
- `log_level`: passive
- `log_level_replica`: warning
- `log_on_each_node`: True
- `logging_nan_inf_filter`: True
- `save_safetensors`: True
- `save_on_each_node`: False
- `save_only_model`: False
- `restore_callback_states_from_checkpoint`: False
- `no_cuda`: False
- `use_cpu`: False
- `use_mps_device`: False
- `seed`: 42
- `data_seed`: None
- `jit_mode_eval`: False
- `use_ipex`: False
- `bf16`: True
- `fp16`: False
- `fp16_opt_level`: O1
- `half_precision_backend`: auto
- `bf16_full_eval`: False
- `fp16_full_eval`: False
- `tf32`: None
- `local_rank`: 0
- `ddp_backend`: None
- `tpu_num_cores`: None
- `tpu_metrics_debug`: False
- `debug`: []
- `dataloader_drop_last`: False
- `dataloader_num_workers`: 16
- `dataloader_prefetch_factor`: None
- `past_index`: -1
- `disable_tqdm`: False
- `remove_unused_columns`: True
- `label_names`: None
- `load_best_model_at_end`: True
- `ignore_data_skip`: False
- `fsdp`: []
- `fsdp_min_num_params`: 0
- `fsdp_config`: {'min_num_params': 0, 'xla': False, 'xla_fsdp_v2': False, 'xla_fsdp_grad_ckpt': False}
- `fsdp_transformer_layer_cls_to_wrap`: None
- `accelerator_config`: {'split_batches': False, 'dispatch_batches': None, 'even_batches': True, 'use_seedable_sampler': True, 'non_blocking': False, 'gradient_accumulation_kwargs': None}
- `deepspeed`: None
- `label_smoothing_factor`: 0.0
- `optim`: adamw_torch
- `optim_args`: None
- `adafactor`: False
- `group_by_length`: False
- `length_column_name`: length
- `ddp_find_unused_parameters`: None
- `ddp_bucket_cap_mb`: None
- `ddp_broadcast_buffers`: False
- `dataloader_pin_memory`: True
- `dataloader_persistent_workers`: False
- `skip_memory_metrics`: True
- `use_legacy_prediction_loop`: False
- `push_to_hub`: False
- `resume_from_checkpoint`: None
- `hub_model_id`: None
- `hub_strategy`: every_save
- `hub_private_repo`: None
- `hub_always_push`: False
- `hub_revision`: None
- `gradient_checkpointing`: True
- `gradient_checkpointing_kwargs`: None
- `include_inputs_for_metrics`: False
- `include_for_metrics`: []
- `eval_do_concat_batches`: True
- `fp16_backend`: auto
- `push_to_hub_model_id`: None
- `push_to_hub_organization`: None
- `mp_parameters`: 
- `auto_find_batch_size`: False
- `full_determinism`: False
- `torchdynamo`: None
- `ray_scope`: last
- `ddp_timeout`: 1800
- `torch_compile`: False
- `torch_compile_backend`: None
- `torch_compile_mode`: None
- `include_tokens_per_second`: False
- `include_num_input_tokens_seen`: False
- `neftune_noise_alpha`: None
- `optim_target_modules`: None
- `batch_eval_metrics`: False
- `eval_on_start`: False
- `use_liger_kernel`: False
- `liger_kernel_config`: None
- `eval_use_gather_object`: False
- `average_tokens_across_devices`: False
- `prompts`: None
- `batch_sampler`: batch_sampler
- `multi_dataset_batch_sampler`: proportional

</details>

### Training Logs
<details><summary>Click to expand</summary>

| Epoch  | Step  | Training Loss | ct-pubmed-clean-eval_cosine_ndcg@10 |
|:------:|:-----:|:-------------:|:-----------------------------------:|
| 0.0129 | 100   | 2.2196        | -                                   |
| 0.0257 | 200   | 1.7937        | -                                   |
| 0.0386 | 300   | 1.5607        | -                                   |
| 0.0515 | 400   | 1.4738        | -                                   |
| 0.0644 | 500   | 1.4141        | -                                   |
| 0.0772 | 600   | 1.3807        | -                                   |
| 0.0901 | 700   | 1.3341        | -                                   |
| 0.1030 | 800   | 1.3077        | -                                   |
| 0.1158 | 900   | 1.3093        | -                                   |
| 0.1287 | 1000  | 1.2638        | -                                   |
| 0.1416 | 1100  | 1.2509        | -                                   |
| 0.1545 | 1200  | 1.2333        | -                                   |
| 0.1673 | 1300  | 1.2375        | -                                   |
| 0.1802 | 1400  | 1.2022        | -                                   |
| 0.1931 | 1500  | 1.1917        | -                                   |
| 0.2059 | 1600  | 1.1853        | -                                   |
| 0.2188 | 1700  | 1.1842        | -                                   |
| 0.2317 | 1800  | 1.1748        | -                                   |
| 0.2446 | 1900  | 1.1735        | -                                   |
| 0.2574 | 2000  | 1.1457        | -                                   |
| 0.2703 | 2100  | 1.1445        | -                                   |
| 0.2832 | 2200  | 1.1448        | -                                   |
| 0.2960 | 2300  | 1.1313        | -                                   |
| 0.3089 | 2400  | 1.1301        | -                                   |
| 0.3218 | 2500  | 1.1281        | -                                   |
| 0.3347 | 2600  | 1.1139        | -                                   |
| 0.3475 | 2700  | 1.1062        | -                                   |
| 0.3604 | 2800  | 1.0989        | -                                   |
| 0.3733 | 2900  | 1.1147        | -                                   |
| 0.3862 | 3000  | 1.106         | -                                   |
| 0.3990 | 3100  | 1.1074        | -                                   |
| 0.4119 | 3200  | 1.0853        | -                                   |
| 0.4248 | 3300  | 1.0918        | -                                   |
| 0.4376 | 3400  | 1.0857        | -                                   |
| 0.4505 | 3500  | 1.0774        | -                                   |
| 0.4634 | 3600  | 1.0744        | -                                   |
| 0.4763 | 3700  | 1.0799        | -                                   |
| 0.4891 | 3800  | 1.0791        | -                                   |
| 0.4999 | 3884  | -             | 0.6628                              |
| 0.5020 | 3900  | 1.077         | -                                   |
| 0.5149 | 4000  | 1.0531        | -                                   |
| 0.5277 | 4100  | 1.0449        | -                                   |
| 0.5406 | 4200  | 1.0544        | -                                   |
| 0.5535 | 4300  | 1.0496        | -                                   |
| 0.5664 | 4400  | 1.0508        | -                                   |
| 0.5792 | 4500  | 1.0649        | -                                   |
| 0.5921 | 4600  | 1.0633        | -                                   |
| 0.6050 | 4700  | 1.0576        | -                                   |
| 0.6178 | 4800  | 1.0398        | -                                   |
| 0.6307 | 4900  | 1.0311        | -                                   |
| 0.6436 | 5000  | 1.0558        | -                                   |
| 0.6565 | 5100  | 1.0355        | -                                   |
| 0.6693 | 5200  | 1.0221        | -                                   |
| 0.6822 | 5300  | 1.0188        | -                                   |
| 0.6951 | 5400  | 1.0266        | -                                   |
| 0.7079 | 5500  | 1.0254        | -                                   |
| 0.7208 | 5600  | 1.0229        | -                                   |
| 0.7337 | 5700  | 1.0199        | -                                   |
| 0.7466 | 5800  | 1.0187        | -                                   |
| 0.7594 | 5900  | 1.0143        | -                                   |
| 0.7723 | 6000  | 1.0241        | -                                   |
| 0.7852 | 6100  | 1.0174        | -                                   |
| 0.7980 | 6200  | 1.0069        | -                                   |
| 0.8109 | 6300  | 1.0008        | -                                   |
| 0.8238 | 6400  | 1.0083        | -                                   |
| 0.8367 | 6500  | 1.0047        | -                                   |
| 0.8495 | 6600  | 1.0134        | -                                   |
| 0.8624 | 6700  | 1.0021        | -                                   |
| 0.8753 | 6800  | 0.9956        | -                                   |
| 0.8881 | 6900  | 1.0           | -                                   |
| 0.9010 | 7000  | 1.0098        | -                                   |
| 0.9139 | 7100  | 0.9991        | -                                   |
| 0.9268 | 7200  | 1.0003        | -                                   |
| 0.9396 | 7300  | 0.965         | -                                   |
| 0.9525 | 7400  | 0.9992        | -                                   |
| 0.9654 | 7500  | 0.9889        | -                                   |
| 0.9782 | 7600  | 0.9961        | -                                   |
| 0.9911 | 7700  | 0.9912        | -                                   |
| 0.9999 | 7768  | -             | 0.6744                              |
| 1.0040 | 7800  | 0.9734        | -                                   |
| 1.0169 | 7900  | 0.9606        | -                                   |
| 1.0297 | 8000  | 0.9552        | -                                   |
| 1.0426 | 8100  | 0.953         | -                                   |
| 1.0555 | 8200  | 0.9701        | -                                   |
| 1.0683 | 8300  | 0.9603        | -                                   |
| 1.0812 | 8400  | 0.9448        | -                                   |
| 1.0941 | 8500  | 0.9332        | -                                   |
| 1.1070 | 8600  | 0.9427        | -                                   |
| 1.1198 | 8700  | 0.9512        | -                                   |
| 1.1327 | 8800  | 0.9441        | -                                   |
| 1.1456 | 8900  | 0.9509        | -                                   |
| 1.1585 | 9000  | 0.9568        | -                                   |
| 1.1713 | 9100  | 0.9473        | -                                   |
| 1.1842 | 9200  | 0.9434        | -                                   |
| 1.1971 | 9300  | 0.9329        | -                                   |
| 1.2099 | 9400  | 0.932         | -                                   |
| 1.2228 | 9500  | 0.9513        | -                                   |
| 1.2357 | 9600  | 0.9476        | -                                   |
| 1.2486 | 9700  | 0.933         | -                                   |
| 1.2614 | 9800  | 0.9243        | -                                   |
| 1.2743 | 9900  | 0.9422        | -                                   |
| 1.2872 | 10000 | 0.9249        | -                                   |
| 1.3000 | 10100 | 0.9297        | -                                   |
| 1.3129 | 10200 | 0.9285        | -                                   |
| 1.3258 | 10300 | 0.9364        | -                                   |
| 1.3387 | 10400 | 0.9339        | -                                   |
| 1.3515 | 10500 | 0.9395        | -                                   |
| 1.3644 | 10600 | 0.9365        | -                                   |
| 1.3773 | 10700 | 0.9223        | -                                   |
| 1.3901 | 10800 | 0.926         | -                                   |
| 1.4030 | 10900 | 0.925         | -                                   |
| 1.4159 | 11000 | 0.9373        | -                                   |
| 1.4288 | 11100 | 0.9304        | -                                   |
| 1.4416 | 11200 | 0.9251        | -                                   |
| 1.4545 | 11300 | 0.9315        | -                                   |
| 1.4674 | 11400 | 0.9301        | -                                   |
| 1.4802 | 11500 | 0.9292        | -                                   |
| 1.4931 | 11600 | 0.9187        | -                                   |
| 1.4998 | 11652 | -             | 0.6844                              |
| 1.5060 | 11700 | 0.9195        | -                                   |
| 1.5189 | 11800 | 0.9251        | -                                   |
| 1.5317 | 11900 | 0.9292        | -                                   |
| 1.5446 | 12000 | 0.913         | -                                   |
| 1.5575 | 12100 | 0.9262        | -                                   |
| 1.5703 | 12200 | 0.9199        | -                                   |
| 1.5832 | 12300 | 0.9216        | -                                   |
| 1.5961 | 12400 | 0.9307        | -                                   |
| 1.6090 | 12500 | 0.9257        | -                                   |
| 1.6218 | 12600 | 0.9242        | -                                   |
| 1.6347 | 12700 | 0.9225        | -                                   |
| 1.6476 | 12800 | 0.9155        | -                                   |
| 1.6604 | 12900 | 0.9175        | -                                   |
| 1.6733 | 13000 | 0.9114        | -                                   |
| 1.6862 | 13100 | 0.9201        | -                                   |
| 1.6991 | 13200 | 0.9233        | -                                   |
| 1.7119 | 13300 | 0.9129        | -                                   |
| 1.7248 | 13400 | 0.9192        | -                                   |
| 1.7377 | 13500 | 0.9042        | -                                   |
| 1.7505 | 13600 | 0.9048        | -                                   |
| 1.7634 | 13700 | 0.9116        | -                                   |
| 1.7763 | 13800 | 0.9119        | -                                   |
| 1.7892 | 13900 | 0.9095        | -                                   |
| 1.8020 | 14000 | 0.909         | -                                   |
| 1.8149 | 14100 | 0.9091        | -                                   |
| 1.8278 | 14200 | 0.902         | -                                   |
| 1.8406 | 14300 | 0.8988        | -                                   |
| 1.8535 | 14400 | 0.9025        | -                                   |
| 1.8664 | 14500 | 0.9031        | -                                   |
| 1.8793 | 14600 | 0.9221        | -                                   |
| 1.8921 | 14700 | 0.9022        | -                                   |
| 1.9050 | 14800 | 0.9081        | -                                   |
| 1.9179 | 14900 | 0.9051        | -                                   |
| 1.9308 | 15000 | 0.9006        | -                                   |
| 1.9436 | 15100 | 0.9158        | -                                   |
| 1.9565 | 15200 | 0.9077        | -                                   |
| 1.9694 | 15300 | 0.8976        | -                                   |
| 1.9822 | 15400 | 0.899         | -                                   |
| 1.9951 | 15500 | 0.9096        | -                                   |
| 1.9997 | 15536 | -             | 0.6843                              |
| 2.0080 | 15600 | 0.8844        | -                                   |
| 2.0209 | 15700 | 0.8738        | -                                   |
| 2.0337 | 15800 | 0.8896        | -                                   |
| 2.0466 | 15900 | 0.8892        | -                                   |
| 2.0595 | 16000 | 0.8805        | -                                   |
| 2.0723 | 16100 | 0.8732        | -                                   |
| 2.0852 | 16200 | 0.8821        | -                                   |
| 2.0981 | 16300 | 0.8903        | -                                   |
| 2.1110 | 16400 | 0.8901        | -                                   |
| 2.1238 | 16500 | 0.8844        | -                                   |
| 2.1367 | 16600 | 0.8887        | -                                   |
| 2.1496 | 16700 | 0.871         | -                                   |
| 2.1624 | 16800 | 0.8776        | -                                   |
| 2.1753 | 16900 | 0.8754        | -                                   |
| 2.1882 | 17000 | 0.8949        | -                                   |
| 2.2011 | 17100 | 0.8835        | -                                   |
| 2.2139 | 17200 | 0.8694        | -                                   |
| 2.2268 | 17300 | 0.8773        | -                                   |
| 2.2397 | 17400 | 0.8808        | -                                   |
| 2.2525 | 17500 | 0.8908        | -                                   |
| 2.2654 | 17600 | 0.8854        | -                                   |
| 2.2783 | 17700 | 0.8813        | -                                   |
| 2.2912 | 17800 | 0.8813        | -                                   |
| 2.3040 | 17900 | 0.8805        | -                                   |
| 2.3169 | 18000 | 0.8666        | -                                   |
| 2.3298 | 18100 | 0.8851        | -                                   |
| 2.3426 | 18200 | 0.8719        | -                                   |
| 2.3555 | 18300 | 0.8819        | -                                   |
| 2.3684 | 18400 | 0.8695        | -                                   |
| 2.3813 | 18500 | 0.8778        | -                                   |
| 2.3941 | 18600 | 0.8673        | -                                   |
| 2.4070 | 18700 | 0.8868        | -                                   |
| 2.4199 | 18800 | 0.886         | -                                   |
| 2.4327 | 18900 | 0.882         | -                                   |
| 2.4456 | 19000 | 0.8701        | -                                   |
| 2.4585 | 19100 | 0.874         | -                                   |
| 2.4714 | 19200 | 0.8681        | -                                   |
| 2.4842 | 19300 | 0.886         | -                                   |
| 2.4971 | 19400 | 0.882         | -                                   |
| 2.4997 | 19420 | -             | 0.6884                              |
| 2.5100 | 19500 | 0.8837        | -                                   |
| 2.5228 | 19600 | 0.8765        | -                                   |
| 2.5357 | 19700 | 0.8771        | -                                   |
| 2.5486 | 19800 | 0.8727        | -                                   |
| 2.5615 | 19900 | 0.8735        | -                                   |
| 2.5743 | 20000 | 0.8765        | -                                   |
| 2.5872 | 20100 | 0.8701        | -                                   |
| 2.6001 | 20200 | 0.8804        | -                                   |
| 2.6129 | 20300 | 0.8785        | -                                   |
| 2.6258 | 20400 | 0.8719        | -                                   |
| 2.6387 | 20500 | 0.8758        | -                                   |
| 2.6516 | 20600 | 0.8868        | -                                   |
| 2.6644 | 20700 | 0.8684        | -                                   |
| 2.6773 | 20800 | 0.8636        | -                                   |
| 2.6902 | 20900 | 0.8942        | -                                   |
| 2.7031 | 21000 | 0.8726        | -                                   |
| 2.7159 | 21100 | 0.8704        | -                                   |
| 2.7288 | 21200 | 0.8728        | -                                   |
| 2.7417 | 21300 | 0.8708        | -                                   |
| 2.7545 | 21400 | 0.8654        | -                                   |
| 2.7674 | 21500 | 0.8599        | -                                   |
| 2.7803 | 21600 | 0.8714        | -                                   |
| 2.7932 | 21700 | 0.8753        | -                                   |
| 2.8060 | 21800 | 0.8793        | -                                   |
| 2.8189 | 21900 | 0.8787        | -                                   |
| 2.8318 | 22000 | 0.8797        | -                                   |
| 2.8446 | 22100 | 0.876         | -                                   |
| 2.8575 | 22200 | 0.8732        | -                                   |
| 2.8704 | 22300 | 0.8687        | -                                   |
| 2.8833 | 22400 | 0.871         | -                                   |
| 2.8961 | 22500 | 0.8796        | -                                   |
| 2.9090 | 22600 | 0.8812        | -                                   |
| 2.9219 | 22700 | 0.8659        | -                                   |
| 2.9347 | 22800 | 0.8625        | -                                   |
| 2.9476 | 22900 | 0.8755        | -                                   |
| 2.9605 | 23000 | 0.8767        | -                                   |
| 2.9734 | 23100 | 0.8658        | -                                   |
| 2.9862 | 23200 | 0.8751        | -                                   |
| 2.9991 | 23300 | 0.8774        | -                                   |
| 2.9996 | 23304 | -             | 0.6889                              |

</details>

### Framework Versions
- Python: 3.11.11
- Sentence Transformers: 3.4.1
- Transformers: 4.53.2
- PyTorch: 2.6.0+cu124
- Accelerate: 1.5.2
- Datasets: 3.2.0
- Tokenizers: 0.21.0

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

#### CachedMultipleNegativesRankingLoss
```bibtex
@misc{gao2021scaling,
    title={Scaling Deep Contrastive Learning Batch Size under Memory Limited Setup},
    author={Luyu Gao and Yunyi Zhang and Jiawei Han and Jamie Callan},
    year={2021},
    eprint={2101.06983},
    archivePrefix={arXiv},
    primaryClass={cs.LG}
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