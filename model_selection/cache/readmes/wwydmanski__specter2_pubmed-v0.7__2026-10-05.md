---
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- generated_from_trainer
- dataset_size:57566
- loss:MultipleNegativesRankingLoss
base_model: allenai/specter2_base
widget:
- source_sentence: Cannabis evolution
  sentences:
  - 'The cannabis conundrum. '
  - 'Dawn and decline of the holy smoke. '
  - '[Computer-assisted system for interstitial hyperthermia]. '
- source_sentence: Lateral Ventricle AT/RT
  sentences:
  - 'Improved Assessment of Pathological Regurgitation in Patients with Prosthetic
    Heart Valves by Multiplane Transesophageal Echocardiography. '
  - '[Surgical anatomy of the lateral ventricles]. '
  - 'Lateral Ventricle Atypical Teratoid/Rhabdoid Tumor (AT/RT): Case Report and Review
    of Literature. '
- source_sentence: Parkinsonian motor fluctuations
  sentences:
  - 'Basic mechanisms of motor fluctuations. '
  - 'Nonmotor Fluctuations in Parkinson''s Disease. '
  - 'Sodium conductance in calcium channels of single smooth muscle cells of guinea-pig
    taenia caeci. '
- source_sentence: Phagocytic Assay
  sentences:
  - 'Assay for phagocytosis. '
  - 'Opsonophagocytic assay. '
  - 'Clinical evaluation of synthetic aperture sequential beamforming ultrasound in
    patients with liver tumors. '
- source_sentence: Content validity assessment
  sentences:
  - 'Content validity is naught. '
  - 'Male requires a higher median target effect-site concentration of propofol for
    I-gel placement when combined with dexmedetomidine. '
  - 'Establishing content-validity of a disease-specific health-related quality of
    life instrument for patients with chronic hypersensitivity pneumonitis. '
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
- name: SentenceTransformer based on allenai/specter2_base
  results:
  - task:
      type: information-retrieval
      name: Information Retrieval
    dataset:
      name: NanoNQ
      type: NanoNQ
    metrics:
    - type: cosine_accuracy@1
      value: 0.04
      name: Cosine Accuracy@1
    - type: cosine_accuracy@3
      value: 0.2
      name: Cosine Accuracy@3
    - type: cosine_accuracy@5
      value: 0.22
      name: Cosine Accuracy@5
    - type: cosine_accuracy@10
      value: 0.3
      name: Cosine Accuracy@10
    - type: cosine_precision@1
      value: 0.04
      name: Cosine Precision@1
    - type: cosine_precision@3
      value: 0.06666666666666667
      name: Cosine Precision@3
    - type: cosine_precision@5
      value: 0.044000000000000004
      name: Cosine Precision@5
    - type: cosine_precision@10
      value: 0.03
      name: Cosine Precision@10
    - type: cosine_recall@1
      value: 0.03
      name: Cosine Recall@1
    - type: cosine_recall@3
      value: 0.18
      name: Cosine Recall@3
    - type: cosine_recall@5
      value: 0.2
      name: Cosine Recall@5
    - type: cosine_recall@10
      value: 0.27
      name: Cosine Recall@10
    - type: cosine_ndcg@10
      value: 0.15735897323110787
      name: Cosine Ndcg@10
    - type: cosine_mrr@10
      value: 0.13194444444444445
      name: Cosine Mrr@10
    - type: cosine_map@100
      value: 0.13092350353731416
      name: Cosine Map@100
  - task:
      type: information-retrieval
      name: Information Retrieval
    dataset:
      name: NanoMSMARCO
      type: NanoMSMARCO
    metrics:
    - type: cosine_accuracy@1
      value: 0.2
      name: Cosine Accuracy@1
    - type: cosine_accuracy@3
      value: 0.36
      name: Cosine Accuracy@3
    - type: cosine_accuracy@5
      value: 0.42
      name: Cosine Accuracy@5
    - type: cosine_accuracy@10
      value: 0.52
      name: Cosine Accuracy@10
    - type: cosine_precision@1
      value: 0.2
      name: Cosine Precision@1
    - type: cosine_precision@3
      value: 0.12
      name: Cosine Precision@3
    - type: cosine_precision@5
      value: 0.084
      name: Cosine Precision@5
    - type: cosine_precision@10
      value: 0.052000000000000005
      name: Cosine Precision@10
    - type: cosine_recall@1
      value: 0.2
      name: Cosine Recall@1
    - type: cosine_recall@3
      value: 0.36
      name: Cosine Recall@3
    - type: cosine_recall@5
      value: 0.42
      name: Cosine Recall@5
    - type: cosine_recall@10
      value: 0.52
      name: Cosine Recall@10
    - type: cosine_ndcg@10
      value: 0.35375176104312445
      name: Cosine Ndcg@10
    - type: cosine_mrr@10
      value: 0.30138095238095236
      name: Cosine Mrr@10
    - type: cosine_map@100
      value: 0.31610409814616347
      name: Cosine Map@100
  - task:
      type: nano-beir
      name: Nano BEIR
    dataset:
      name: NanoBEIR mean
      type: NanoBEIR_mean
    metrics:
    - type: cosine_accuracy@1
      value: 0.12000000000000001
      name: Cosine Accuracy@1
    - type: cosine_accuracy@3
      value: 0.28
      name: Cosine Accuracy@3
    - type: cosine_accuracy@5
      value: 0.32
      name: Cosine Accuracy@5
    - type: cosine_accuracy@10
      value: 0.41000000000000003
      name: Cosine Accuracy@10
    - type: cosine_precision@1
      value: 0.12000000000000001
      name: Cosine Precision@1
    - type: cosine_precision@3
      value: 0.09333333333333332
      name: Cosine Precision@3
    - type: cosine_precision@5
      value: 0.064
      name: Cosine Precision@5
    - type: cosine_precision@10
      value: 0.041
      name: Cosine Precision@10
    - type: cosine_recall@1
      value: 0.115
      name: Cosine Recall@1
    - type: cosine_recall@3
      value: 0.27
      name: Cosine Recall@3
    - type: cosine_recall@5
      value: 0.31
      name: Cosine Recall@5
    - type: cosine_recall@10
      value: 0.395
      name: Cosine Recall@10
    - type: cosine_ndcg@10
      value: 0.25555536713711613
      name: Cosine Ndcg@10
    - type: cosine_mrr@10
      value: 0.21666269841269842
      name: Cosine Mrr@10
    - type: cosine_map@100
      value: 0.22351380084173883
      name: Cosine Map@100
---

# SentenceTransformer based on allenai/specter2_base

This is a [sentence-transformers](https://www.SBERT.net) model finetuned from [allenai/specter2_base](https://huggingface.co/allenai/specter2_base) on the json dataset. It maps sentences & paragraphs to a 768-dimensional dense vector space and can be used for semantic textual similarity, semantic search, paraphrase mining, text classification, clustering, and more.

## Model Details

### Model Description
- **Model Type:** Sentence Transformer
- **Base model:** [allenai/specter2_base](https://huggingface.co/allenai/specter2_base) <!-- at revision 3447645e1def9117997203454fa4495937bfbd83 -->
- **Maximum Sequence Length:** 512 tokens
- **Output Dimensionality:** 768 dimensions
- **Similarity Function:** Cosine Similarity
- **Training Dataset:**
    - json
<!-- - **Language:** Unknown -->
<!-- - **License:** Unknown -->

### Model Sources

- **Documentation:** [Sentence Transformers Documentation](https://sbert.net)
- **Repository:** [Sentence Transformers on GitHub](https://github.com/UKPLab/sentence-transformers)
- **Hugging Face:** [Sentence Transformers on Hugging Face](https://huggingface.co/models?library=sentence-transformers)

### Full Model Architecture

```
SentenceTransformer(
  (0): Transformer({'max_seq_length': 512, 'do_lower_case': False}) with Transformer model: PeftModelForFeatureExtraction 
  (1): Pooling({'word_embedding_dimension': 768, 'pooling_mode_cls_token': False, 'pooling_mode_mean_tokens': True, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False, 'pooling_mode_weightedmean_tokens': False, 'pooling_mode_lasttoken': False, 'include_prompt': True})
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
model = SentenceTransformer("sentence_transformers_model_id")
# Run inference
sentences = [
    'Content validity assessment',
    'Establishing content-validity of a disease-specific health-related quality of life instrument for patients with chronic hypersensitivity pneumonitis. ',
    'Content validity is naught. ',
]
embeddings = model.encode(sentences)
print(embeddings.shape)
# [3, 768]

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

* Datasets: `NanoNQ` and `NanoMSMARCO`
* Evaluated with [<code>InformationRetrievalEvaluator</code>](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#sentence_transformers.evaluation.InformationRetrievalEvaluator)

| Metric              | NanoNQ     | NanoMSMARCO |
|:--------------------|:-----------|:------------|
| cosine_accuracy@1   | 0.04       | 0.2         |
| cosine_accuracy@3   | 0.2        | 0.36        |
| cosine_accuracy@5   | 0.22       | 0.42        |
| cosine_accuracy@10  | 0.3        | 0.52        |
| cosine_precision@1  | 0.04       | 0.2         |
| cosine_precision@3  | 0.0667     | 0.12        |
| cosine_precision@5  | 0.044      | 0.084       |
| cosine_precision@10 | 0.03       | 0.052       |
| cosine_recall@1     | 0.03       | 0.2         |
| cosine_recall@3     | 0.18       | 0.36        |
| cosine_recall@5     | 0.2        | 0.42        |
| cosine_recall@10    | 0.27       | 0.52        |
| **cosine_ndcg@10**  | **0.1574** | **0.3538**  |
| cosine_mrr@10       | 0.1319     | 0.3014      |
| cosine_map@100      | 0.1309     | 0.3161      |

#### Nano BEIR

* Dataset: `NanoBEIR_mean`
* Evaluated with [<code>NanoBEIREvaluator</code>](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#sentence_transformers.evaluation.NanoBEIREvaluator)

| Metric              | Value      |
|:--------------------|:-----------|
| cosine_accuracy@1   | 0.12       |
| cosine_accuracy@3   | 0.28       |
| cosine_accuracy@5   | 0.32       |
| cosine_accuracy@10  | 0.41       |
| cosine_precision@1  | 0.12       |
| cosine_precision@3  | 0.0933     |
| cosine_precision@5  | 0.064      |
| cosine_precision@10 | 0.041      |
| cosine_recall@1     | 0.115      |
| cosine_recall@3     | 0.27       |
| cosine_recall@5     | 0.31       |
| cosine_recall@10    | 0.395      |
| **cosine_ndcg@10**  | **0.2556** |
| cosine_mrr@10       | 0.2167     |
| cosine_map@100      | 0.2235     |

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
* Size: 57,566 training samples
* Columns: <code>anchor</code>, <code>positive</code>, and <code>negative</code>
* Approximate statistics based on the first 1000 samples:
  |         | anchor                                                                          | positive                                                                          | negative                                                                         |
  |:--------|:--------------------------------------------------------------------------------|:----------------------------------------------------------------------------------|:---------------------------------------------------------------------------------|
  | type    | string                                                                          | string                                                                            | string                                                                           |
  | details | <ul><li>min: 3 tokens</li><li>mean: 7.4 tokens</li><li>max: 27 tokens</li></ul> | <ul><li>min: 4 tokens</li><li>mean: 19.98 tokens</li><li>max: 78 tokens</li></ul> | <ul><li>min: 4 tokens</li><li>mean: 12.3 tokens</li><li>max: 46 tokens</li></ul> |
* Samples:
  | anchor                                                            | positive                                                                                                           | negative                                                                                                           |
  |:------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------|
  | <code>neutron camera autofocus</code>                             | <code>The autofocusing system of the IMAT neutron camera. </code>                                                  | <code>Robust autofocusing in microscopy. </code>                                                                   |
  | <code>Melanophore-stimulating hormone-melatonin antagonism</code> | <code>Melanophore-stimulating hormone-melatonin antagonism in relation to colour change in Xenopus laevis. </code> | <code>Melanin-concentrating hormone, melanocortin receptors and regulation of luteinizing hormone release. </code> |
  | <code>Healthcare Reform Criticism</code>                          | <code>Experts critique doctors' ideas for reforming health care. </code>                                           | <code>Healthcare reform? </code>                                                                                   |
* Loss: [<code>MultipleNegativesRankingLoss</code>](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#multiplenegativesrankingloss) with these parameters:
  ```json
  {
      "scale": 20.0,
      "similarity_fct": "cos_sim"
  }
  ```

### Training Hyperparameters
#### Non-Default Hyperparameters

- `eval_strategy`: steps
- `per_device_train_batch_size`: 64
- `gradient_accumulation_steps`: 8
- `learning_rate`: 3e-05
- `weight_decay`: 0.01
- `num_train_epochs`: 1
- `lr_scheduler_type`: cosine_with_restarts
- `warmup_ratio`: 0.1
- `bf16`: True
- `batch_sampler`: no_duplicates

#### All Hyperparameters
<details><summary>Click to expand</summary>

- `overwrite_output_dir`: False
- `do_predict`: False
- `eval_strategy`: steps
- `prediction_loss_only`: True
- `per_device_train_batch_size`: 64
- `per_device_eval_batch_size`: 8
- `per_gpu_train_batch_size`: None
- `per_gpu_eval_batch_size`: None
- `gradient_accumulation_steps`: 8
- `eval_accumulation_steps`: None
- `torch_empty_cache_steps`: None
- `learning_rate`: 3e-05
- `weight_decay`: 0.01
- `adam_beta1`: 0.9
- `adam_beta2`: 0.999
- `adam_epsilon`: 1e-08
- `max_grad_norm`: 1.0
- `num_train_epochs`: 1
- `max_steps`: -1
- `lr_scheduler_type`: cosine_with_restarts
- `lr_scheduler_kwargs`: {}
- `warmup_ratio`: 0.1
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
- `dataloader_num_workers`: 0
- `dataloader_prefetch_factor`: None
- `past_index`: -1
- `disable_tqdm`: False
- `remove_unused_columns`: True
- `label_names`: None
- `load_best_model_at_end`: False
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
- `gradient_checkpointing`: False
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
- `dispatch_batches`: None
- `split_batches`: None
- `include_tokens_per_second`: False
- `include_num_input_tokens_seen`: False
- `neftune_noise_alpha`: None
- `optim_target_modules`: None
- `batch_eval_metrics`: False
- `eval_on_start`: False
- `use_liger_kernel`: False
- `eval_use_gather_object`: False
- `average_tokens_across_devices`: False
- `prompts`: None
- `batch_sampler`: no_duplicates
- `multi_dataset_batch_sampler`: proportional

</details>

### Training Logs
<details><summary>Click to expand</summary>

| Epoch  | Step | Training Loss | NanoNQ_cosine_ndcg@10 | NanoMSMARCO_cosine_ndcg@10 | NanoBEIR_mean_cosine_ndcg@10 |
|:------:|:----:|:-------------:|:---------------------:|:--------------------------:|:----------------------------:|
| 0      | 0    | -             | 0.0633                | 0.2640                     | 0.1636                       |
| 0.0089 | 1    | 22.3889       | -                     | -                          | -                            |
| 0.0178 | 2    | 22.1875       | -                     | -                          | -                            |
| 0.0267 | 3    | 21.4657       | -                     | -                          | -                            |
| 0.0356 | 4    | 21.7306       | -                     | -                          | -                            |
| 0.0444 | 5    | 21.3965       | -                     | -                          | -                            |
| 0.0533 | 6    | 21.5539       | -                     | -                          | -                            |
| 0.0622 | 7    | 21.5853       | -                     | -                          | -                            |
| 0.0711 | 8    | 21.6282       | -                     | -                          | -                            |
| 0.08   | 9    | 21.2169       | -                     | -                          | -                            |
| 0.0889 | 10   | 21.1228       | -                     | -                          | -                            |
| 0.0978 | 11   | 20.7026       | -                     | -                          | -                            |
| 0.1067 | 12   | 21.2562       | -                     | -                          | -                            |
| 0.1156 | 13   | 21.1227       | -                     | -                          | -                            |
| 0.1244 | 14   | 20.6465       | -                     | -                          | -                            |
| 0.1333 | 15   | 20.5888       | -                     | -                          | -                            |
| 0.1422 | 16   | 20.2334       | -                     | -                          | -                            |
| 0.1511 | 17   | 20.6545       | -                     | -                          | -                            |
| 0.16   | 18   | 20.2517       | -                     | -                          | -                            |
| 0.1689 | 19   | 19.6825       | -                     | -                          | -                            |
| 0.1778 | 20   | 19.9251       | -                     | -                          | -                            |
| 0.1867 | 21   | 19.6937       | -                     | -                          | -                            |
| 0.1956 | 22   | 19.2779       | -                     | -                          | -                            |
| 0.2044 | 23   | 19.2927       | -                     | -                          | -                            |
| 0.2133 | 24   | 19.2895       | -                     | -                          | -                            |
| 0.2222 | 25   | 18.9854       | 0.1085                | 0.2978                     | 0.2032                       |
| 0.2311 | 26   | 18.5096       | -                     | -                          | -                            |
| 0.24   | 27   | 18.3789       | -                     | -                          | -                            |
| 0.2489 | 28   | 18.2159       | -                     | -                          | -                            |
| 0.2578 | 29   | 17.8306       | -                     | -                          | -                            |
| 0.2667 | 30   | 17.5964       | -                     | -                          | -                            |
| 0.2756 | 31   | 17.2527       | -                     | -                          | -                            |
| 0.2844 | 32   | 17.2274       | -                     | -                          | -                            |
| 0.2933 | 33   | 17.557        | -                     | -                          | -                            |
| 0.3022 | 34   | 17.4682       | -                     | -                          | -                            |
| 0.3111 | 35   | 16.9115       | -                     | -                          | -                            |
| 0.32   | 36   | 16.9938       | -                     | -                          | -                            |
| 0.3289 | 37   | 16.1648       | -                     | -                          | -                            |
| 0.3378 | 38   | 16.2908       | -                     | -                          | -                            |
| 0.3467 | 39   | 16.7883       | -                     | -                          | -                            |
| 0.3556 | 40   | 16.5278       | -                     | -                          | -                            |
| 0.3644 | 41   | 15.4466       | -                     | -                          | -                            |
| 0.3733 | 42   | 15.3954       | -                     | -                          | -                            |
| 0.3822 | 43   | 16.1363       | -                     | -                          | -                            |
| 0.3911 | 44   | 14.8857       | -                     | -                          | -                            |
| 0.4    | 45   | 15.5596       | -                     | -                          | -                            |
| 0.4089 | 46   | 15.6978       | -                     | -                          | -                            |
| 0.4178 | 47   | 14.6959       | -                     | -                          | -                            |
| 0.4267 | 48   | 15.0677       | -                     | -                          | -                            |
| 0.4356 | 49   | 14.4375       | -                     | -                          | -                            |
| 0.4444 | 50   | 15.0901       | 0.1348                | 0.3290                     | 0.2319                       |
| 0.4533 | 51   | 13.813        | -                     | -                          | -                            |
| 0.4622 | 52   | 14.3135       | -                     | -                          | -                            |
| 0.4711 | 53   | 14.9517       | -                     | -                          | -                            |
| 0.48   | 54   | 14.0599       | -                     | -                          | -                            |
| 0.4889 | 55   | 13.8699       | -                     | -                          | -                            |
| 0.4978 | 56   | 14.6277       | -                     | -                          | -                            |
| 0.5067 | 57   | 13.3742       | -                     | -                          | -                            |
| 0.5156 | 58   | 13.7985       | -                     | -                          | -                            |
| 0.5244 | 59   | 13.2972       | -                     | -                          | -                            |
| 0.5333 | 60   | 12.9836       | -                     | -                          | -                            |
| 0.5422 | 61   | 13.2035       | -                     | -                          | -                            |
| 0.5511 | 62   | 13.399        | -                     | -                          | -                            |
| 0.56   | 63   | 12.8694       | -                     | -                          | -                            |
| 0.5689 | 64   | 12.9775       | -                     | -                          | -                            |
| 0.5778 | 65   | 13.5685       | -                     | -                          | -                            |
| 0.5867 | 66   | 12.5359       | -                     | -                          | -                            |
| 0.5956 | 67   | 12.7989       | -                     | -                          | -                            |
| 0.6044 | 68   | 12.2337       | -                     | -                          | -                            |
| 0.6133 | 69   | 12.9103       | -                     | -                          | -                            |
| 0.6222 | 70   | 12.6319       | -                     | -                          | -                            |
| 0.6311 | 71   | 12.3662       | -                     | -                          | -                            |
| 0.64   | 72   | 12.4788       | -                     | -                          | -                            |
| 0.6489 | 73   | 12.7665       | -                     | -                          | -                            |
| 0.6578 | 74   | 12.7189       | -                     | -                          | -                            |
| 0.6667 | 75   | 11.6918       | 0.1558                | 0.3619                     | 0.2588                       |
| 0.6756 | 76   | 12.0761       | -                     | -                          | -                            |
| 0.6844 | 77   | 12.0588       | -                     | -                          | -                            |
| 0.6933 | 78   | 12.1507       | -                     | -                          | -                            |
| 0.7022 | 79   | 11.7982       | -                     | -                          | -                            |
| 0.7111 | 80   | 12.6278       | -                     | -                          | -                            |
| 0.72   | 81   | 12.1629       | -                     | -                          | -                            |
| 0.7289 | 82   | 11.9421       | -                     | -                          | -                            |
| 0.7378 | 83   | 12.1184       | -                     | -                          | -                            |
| 0.7467 | 84   | 11.9142       | -                     | -                          | -                            |
| 0.7556 | 85   | 12.1162       | -                     | -                          | -                            |
| 0.7644 | 86   | 12.2741       | -                     | -                          | -                            |
| 0.7733 | 87   | 11.8835       | -                     | -                          | -                            |
| 0.7822 | 88   | 11.8583       | -                     | -                          | -                            |
| 0.7911 | 89   | 11.74         | -                     | -                          | -                            |
| 0.8    | 90   | 12.0793       | -                     | -                          | -                            |
| 0.8089 | 91   | 11.6838       | -                     | -                          | -                            |
| 0.8178 | 92   | 11.6922       | -                     | -                          | -                            |
| 0.8267 | 93   | 11.9418       | -                     | -                          | -                            |
| 0.8356 | 94   | 12.2899       | -                     | -                          | -                            |
| 0.8444 | 95   | 12.0957       | -                     | -                          | -                            |
| 0.8533 | 96   | 12.0643       | -                     | -                          | -                            |
| 0.8622 | 97   | 12.3496       | -                     | -                          | -                            |
| 0.8711 | 98   | 12.3521       | -                     | -                          | -                            |
| 0.88   | 99   | 11.7082       | -                     | -                          | -                            |
| 0.8889 | 100  | 11.6085       | 0.1574                | 0.3538                     | 0.2556                       |
| 0.8978 | 101  | 11.7018       | -                     | -                          | -                            |
| 0.9067 | 102  | 11.8227       | -                     | -                          | -                            |
| 0.9156 | 103  | 12.5774       | -                     | -                          | -                            |
| 0.9244 | 104  | 11.465        | -                     | -                          | -                            |
| 0.9333 | 105  | 11.303        | -                     | -                          | -                            |
| 0.9422 | 106  | 11.8521       | -                     | -                          | -                            |
| 0.9511 | 107  | 11.6083       | -                     | -                          | -                            |
| 0.96   | 108  | 12.3972       | -                     | -                          | -                            |
| 0.9689 | 109  | 11.6962       | -                     | -                          | -                            |
| 0.9778 | 110  | 11.1335       | -                     | -                          | -                            |
| 0.9867 | 111  | 12.1325       | -                     | -                          | -                            |
| 0.9956 | 112  | 11.7444       | -                     | -                          | -                            |

</details>

### Framework Versions
- Python: 3.12.3
- Sentence Transformers: 3.3.1
- Transformers: 4.49.0
- PyTorch: 2.5.1
- Accelerate: 1.2.1
- Datasets: 2.19.0
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

#### MultipleNegativesRankingLoss
```bibtex
@misc{henderson2017efficient,
    title={Efficient Natural Language Response Suggestion for Smart Reply},
    author={Matthew Henderson and Rami Al-Rfou and Brian Strope and Yun-hsuan Sung and Laszlo Lukacs and Ruiqi Guo and Sanjiv Kumar and Balint Miklos and Ray Kurzweil},
    year={2017},
    eprint={1705.00652},
    archivePrefix={arXiv},
    primaryClass={cs.CL}
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