---
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- generated_from_trainer
- dataset_size:15182
- loss:MultipleNegativesRankingLoss
base_model: BAAI/bge-m3-retromae
widget:
- source_sentence: Carditis in pediatric patients following foreign serum administration
  sentences:
  - 'Four cases of carditis occurring in children and associated with the administration
    of a foreign serum. '
  - 'Understanding Positive Youth Development in Sport Through the Voices of Indigenous
    Youth. '
  - 'Pericarditis in children. '
- source_sentence: Concept Synthesis
  sentences:
  - 'Centeredness in Healthcare: A Concept Synthesis of Family-centered Care, Person-centered
    Care and Child-centered Care. '
  - 'The Power in Concept Mapping! '
  - 'Using propensity scores to estimate the cost-effectiveness of medical therapies. '
- source_sentence: Visual Pathway Mapping
  sentences:
  - 'The visual connection. '
  - 'The "tobacco issue". '
  - 'Elaboration of the Visual Pathways from the Study of War-Related Cranial Injuries:
    The Period from the Russo-Japanese War to World War I. '
- source_sentence: Cerebral Aneurysm Thrombosis
  sentences:
  - '[A case of spontaneous thrombosis of a cerebral arteriovenous aneurysm]. '
  - 'Cerebral Sinus Thrombosis. '
  - 'Good clinical practice (GCP) standards: clinical trials in India. An interview
    with Dr. Urmila Thatte, Head of Clinical Pharmacology, TN Medical College & BYL
    Nair Hospital. Interview by Viveka Roychowdhury. '
- source_sentence: Calcineurin inhibitor-sparing regimen
  sentences:
  - 'Belatacept-based immunosuppression: A calcineurin inhibitor-sparing regimen in
    heart transplant recipients. '
  - 'The Outcomes of Cemented Femoral Revisions for Periprosthetic Femoral Fractures
    in the Elderly: Comparison with Cementless Stems. '
  - 'Neurotoxicity of calcineurin inhibitors: impact and clinical management. '
pipeline_tag: sentence-similarity
library_name: sentence-transformers
metrics:
- cosine_accuracy
model-index:
- name: SentenceTransformer based on BAAI/bge-m3-retromae
  results:
  - task:
      type: triplet
      name: Triplet
    dataset:
      name: triplet dev
      type: triplet-dev
    metrics:
    - type: cosine_accuracy
      value: 0.723
      name: Cosine Accuracy
---

# SentenceTransformer based on BAAI/bge-m3-retromae

This is a [sentence-transformers](https://www.SBERT.net) model finetuned from [BAAI/bge-m3-retromae](https://huggingface.co/BAAI/bge-m3-retromae) on the json dataset. It maps sentences & paragraphs to a 1024-dimensional dense vector space and can be used for semantic textual similarity, semantic search, paraphrase mining, text classification, clustering, and more.

## Model Details

### Model Description
- **Model Type:** Sentence Transformer
- **Base model:** [BAAI/bge-m3-retromae](https://huggingface.co/BAAI/bge-m3-retromae) <!-- at revision 95c4f81ef8f7911dcac8e384532489c32c8dea64 -->
- **Maximum Sequence Length:** 8192 tokens
- **Output Dimensionality:** 1024 dimensions
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
  (0): Transformer({'max_seq_length': 8192, 'do_lower_case': False}) with Transformer model: PeftModelForFeatureExtraction 
  (1): Pooling({'word_embedding_dimension': 1024, 'pooling_mode_cls_token': False, 'pooling_mode_mean_tokens': True, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False, 'pooling_mode_weightedmean_tokens': False, 'pooling_mode_lasttoken': False, 'include_prompt': True})
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
    'Calcineurin inhibitor-sparing regimen',
    'Belatacept-based immunosuppression: A calcineurin inhibitor-sparing regimen in heart transplant recipients. ',
    'Neurotoxicity of calcineurin inhibitors: impact and clinical management. ',
]
embeddings = model.encode(sentences)
print(embeddings.shape)
# [3, 1024]

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

#### Triplet

* Dataset: `triplet-dev`
* Evaluated with [<code>TripletEvaluator</code>](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#sentence_transformers.evaluation.TripletEvaluator)

| Metric              | Value     |
|:--------------------|:----------|
| **cosine_accuracy** | **0.723** |

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
* Size: 15,182 training samples
* Columns: <code>anchor</code>, <code>positive</code>, and <code>negative</code>
* Approximate statistics based on the first 1000 samples:
  |         | anchor                                                                            | positive                                                                          | negative                                                                          |
  |:--------|:----------------------------------------------------------------------------------|:----------------------------------------------------------------------------------|:----------------------------------------------------------------------------------|
  | type    | string                                                                            | string                                                                            | string                                                                            |
  | details | <ul><li>min: 4 tokens</li><li>mean: 10.68 tokens</li><li>max: 49 tokens</li></ul> | <ul><li>min: 6 tokens</li><li>mean: 26.34 tokens</li><li>max: 79 tokens</li></ul> | <ul><li>min: 4 tokens</li><li>mean: 15.75 tokens</li><li>max: 66 tokens</li></ul> |
* Samples:
  | anchor                                      | positive                                                                                                                                       | negative                                                  |
  |:--------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------|
  | <code>Immunogenetic polymorphism</code>     | <code>Immunogenetic polymorphism and disease mechanisms in juvenile chronic arthritis. </code>                                                 | <code>Immunogenetic model. </code>                        |
  | <code>Alemtuzumab-induced pancolitis</code> | <code>Pancolitis a novel early complication of Alemtuzumab for MS treatment. </code>                                                           | <code>Alemtuzumab in lymphoproliferate disorders. </code> |
  | <code>Intermittent infectiousness</code>    | <code>Understanding the effects of intermittent shedding on the transmission of infectious diseases: example of salmonellosis in pigs. </code> | <code>Infectious behaviour. </code>                       |
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
- `per_device_train_batch_size`: 32
- `per_device_eval_batch_size`: 32
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
- `per_device_train_batch_size`: 32
- `per_device_eval_batch_size`: 32
- `per_gpu_train_batch_size`: None
- `per_gpu_eval_batch_size`: None
- `gradient_accumulation_steps`: 1
- `eval_accumulation_steps`: None
- `torch_empty_cache_steps`: None
- `learning_rate`: 5e-05
- `weight_decay`: 0.0
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
- `hub_private_repo`: False
- `hub_always_push`: False
- `gradient_checkpointing`: False
- `gradient_checkpointing_kwargs`: None
- `include_inputs_for_metrics`: False
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
- `eval_use_gather_object`: False
- `prompts`: None
- `batch_sampler`: no_duplicates
- `multi_dataset_batch_sampler`: proportional

</details>

### Training Logs
<details><summary>Click to expand</summary>

| Epoch  | Step | Training Loss | triplet-dev_cosine_accuracy |
|:------:|:----:|:-------------:|:---------------------------:|
| 0      | 0    | -             | 0.543                       |
| 0.0032 | 1    | 3.4406        | -                           |
| 0.0064 | 2    | 3.2403        | -                           |
| 0.0096 | 3    | 3.3734        | -                           |
| 0.0128 | 4    | 3.3858        | -                           |
| 0.0160 | 5    | 3.3195        | -                           |
| 0.0192 | 6    | 3.2708        | -                           |
| 0.0224 | 7    | 3.4507        | -                           |
| 0.0256 | 8    | 3.4782        | -                           |
| 0.0288 | 9    | 3.2926        | -                           |
| 0.0319 | 10   | 3.2744        | -                           |
| 0.0351 | 11   | 3.4455        | -                           |
| 0.0383 | 12   | 3.3225        | -                           |
| 0.0415 | 13   | 3.3568        | -                           |
| 0.0447 | 14   | 3.3349        | -                           |
| 0.0479 | 15   | 3.2672        | -                           |
| 0.0511 | 16   | 3.2584        | -                           |
| 0.0543 | 17   | 3.1607        | -                           |
| 0.0575 | 18   | 3.1793        | -                           |
| 0.0607 | 19   | 3.1924        | -                           |
| 0.0639 | 20   | 3.2913        | -                           |
| 0.0671 | 21   | 3.2028        | -                           |
| 0.0703 | 22   | 3.1448        | -                           |
| 0.0735 | 23   | 3.0991        | -                           |
| 0.0767 | 24   | 3.1371        | -                           |
| 0.0799 | 25   | 3.0089        | -                           |
| 0.0831 | 26   | 3.1232        | -                           |
| 0.0863 | 27   | 2.8794        | -                           |
| 0.0895 | 28   | 2.982         | -                           |
| 0.0927 | 29   | 3.231         | -                           |
| 0.0958 | 30   | 2.9288        | -                           |
| 0.0990 | 31   | 3.0117        | -                           |
| 0.1022 | 32   | 2.8717        | -                           |
| 0.1054 | 33   | 2.7002        | -                           |
| 0.1086 | 34   | 2.6395        | -                           |
| 0.1118 | 35   | 2.5087        | -                           |
| 0.1150 | 36   | 2.7469        | -                           |
| 0.1182 | 37   | 2.6306        | -                           |
| 0.1214 | 38   | 2.1149        | -                           |
| 0.1246 | 39   | 2.5591        | -                           |
| 0.1278 | 40   | 2.0133        | -                           |
| 0.1310 | 41   | 2.2863        | -                           |
| 0.1342 | 42   | 2.2592        | -                           |
| 0.1374 | 43   | 2.1261        | -                           |
| 0.1406 | 44   | 2.278         | -                           |
| 0.1438 | 45   | 1.7339        | -                           |
| 0.1470 | 46   | 1.8337        | -                           |
| 0.1502 | 47   | 1.5944        | -                           |
| 0.1534 | 48   | 2.0899        | -                           |
| 0.1565 | 49   | 1.509         | -                           |
| 0.1597 | 50   | 1.8651        | -                           |
| 0.1629 | 51   | 2.2858        | -                           |
| 0.1661 | 52   | 2.6881        | -                           |
| 0.1693 | 53   | 1.7877        | -                           |
| 0.1725 | 54   | 1.6374        | -                           |
| 0.1757 | 55   | 2.0763        | -                           |
| 0.1789 | 56   | 1.7672        | -                           |
| 0.1821 | 57   | 1.7913        | -                           |
| 0.1853 | 58   | 1.8524        | -                           |
| 0.1885 | 59   | 2.2614        | -                           |
| 0.1917 | 60   | 1.8058        | -                           |
| 0.1949 | 61   | 2.0403        | -                           |
| 0.1981 | 62   | 1.2697        | -                           |
| 0.2013 | 63   | 1.9523        | -                           |
| 0.2045 | 64   | 1.3965        | -                           |
| 0.2077 | 65   | 1.5501        | -                           |
| 0.2109 | 66   | 1.0785        | -                           |
| 0.2141 | 67   | 1.721         | -                           |
| 0.2173 | 68   | 1.9049        | -                           |
| 0.2204 | 69   | 1.4317        | -                           |
| 0.2236 | 70   | 1.905         | -                           |
| 0.2268 | 71   | 1.236         | -                           |
| 0.2300 | 72   | 1.7312        | -                           |
| 0.2332 | 73   | 0.9951        | -                           |
| 0.2364 | 74   | 1.5471        | -                           |
| 0.2396 | 75   | 1.1289        | -                           |
| 0.2428 | 76   | 1.7902        | -                           |
| 0.2460 | 77   | 1.2619        | -                           |
| 0.2492 | 78   | 1.0043        | -                           |
| 0.2524 | 79   | 1.7546        | -                           |
| 0.2556 | 80   | 1.8505        | -                           |
| 0.2588 | 81   | 1.7437        | -                           |
| 0.2620 | 82   | 1.2788        | -                           |
| 0.2652 | 83   | 1.438         | -                           |
| 0.2684 | 84   | 1.5399        | -                           |
| 0.2716 | 85   | 2.1841        | -                           |
| 0.2748 | 86   | 1.6834        | -                           |
| 0.2780 | 87   | 1.3842        | -                           |
| 0.2812 | 88   | 1.619         | -                           |
| 0.2843 | 89   | 1.2492        | -                           |
| 0.2875 | 90   | 1.3613        | -                           |
| 0.2907 | 91   | 1.2457        | -                           |
| 0.2939 | 92   | 1.2966        | -                           |
| 0.2971 | 93   | 1.3718        | -                           |
| 0.3003 | 94   | 1.3675        | -                           |
| 0.3035 | 95   | 2.1095        | -                           |
| 0.3067 | 96   | 1.6177        | -                           |
| 0.3099 | 97   | 1.3287        | -                           |
| 0.3131 | 98   | 1.9805        | -                           |
| 0.3163 | 99   | 1.3861        | -                           |
| 0.3195 | 100  | 1.8392        | 0.622                       |
| 0.3227 | 101  | 1.4698        | -                           |
| 0.3259 | 102  | 1.4499        | -                           |
| 0.3291 | 103  | 1.5338        | -                           |
| 0.3323 | 104  | 1.3867        | -                           |
| 0.3355 | 105  | 1.7414        | -                           |
| 0.3387 | 106  | 1.5203        | -                           |
| 0.3419 | 107  | 1.6059        | -                           |
| 0.3450 | 108  | 1.3799        | -                           |
| 0.3482 | 109  | 1.5004        | -                           |
| 0.3514 | 110  | 1.0175        | -                           |
| 0.3546 | 111  | 1.0399        | -                           |
| 0.3578 | 112  | 1.6369        | -                           |
| 0.3610 | 113  | 1.5692        | -                           |
| 0.3642 | 114  | 1.6808        | -                           |
| 0.3674 | 115  | 1.4315        | -                           |
| 0.3706 | 116  | 0.9854        | -                           |
| 0.3738 | 117  | 1.3637        | -                           |
| 0.3770 | 118  | 1.3986        | -                           |
| 0.3802 | 119  | 1.3848        | -                           |
| 0.3834 | 120  | 1.4436        | -                           |
| 0.3866 | 121  | 1.0704        | -                           |
| 0.3898 | 122  | 1.3788        | -                           |
| 0.3930 | 123  | 1.7131        | -                           |
| 0.3962 | 124  | 1.5013        | -                           |
| 0.3994 | 125  | 1.7377        | -                           |
| 0.4026 | 126  | 2.0296        | -                           |
| 0.4058 | 127  | 1.2643        | -                           |
| 0.4089 | 128  | 1.3647        | -                           |
| 0.4121 | 129  | 1.175         | -                           |
| 0.4153 | 130  | 1.0797        | -                           |
| 0.4185 | 131  | 1.5746        | -                           |
| 0.4217 | 132  | 1.0914        | -                           |
| 0.4249 | 133  | 1.6672        | -                           |
| 0.4281 | 134  | 1.2959        | -                           |
| 0.4313 | 135  | 1.5387        | -                           |
| 0.4345 | 136  | 1.2571        | -                           |
| 0.4377 | 137  | 1.42          | -                           |
| 0.4409 | 138  | 1.3452        | -                           |
| 0.4441 | 139  | 1.2238        | -                           |
| 0.4473 | 140  | 0.9963        | -                           |
| 0.4505 | 141  | 1.0326        | -                           |
| 0.4537 | 142  | 0.8793        | -                           |
| 0.4569 | 143  | 1.2197        | -                           |
| 0.4601 | 144  | 1.2992        | -                           |
| 0.4633 | 145  | 1.1456        | -                           |
| 0.4665 | 146  | 1.6002        | -                           |
| 0.4696 | 147  | 1.54          | -                           |
| 0.4728 | 148  | 1.2323        | -                           |
| 0.4760 | 149  | 1.0184        | -                           |
| 0.4792 | 150  | 1.2416        | -                           |
| 0.4824 | 151  | 1.1777        | -                           |
| 0.4856 | 152  | 1.0964        | -                           |
| 0.4888 | 153  | 1.0828        | -                           |
| 0.4920 | 154  | 1.3446        | -                           |
| 0.4952 | 155  | 0.9454        | -                           |
| 0.4984 | 156  | 0.7719        | -                           |
| 0.5016 | 157  | 1.003         | -                           |
| 0.5048 | 158  | 0.9863        | -                           |
| 0.5080 | 159  | 0.9672        | -                           |
| 0.5112 | 160  | 1.1432        | -                           |
| 0.5144 | 161  | 1.0377        | -                           |
| 0.5176 | 162  | 1.102         | -                           |
| 0.5208 | 163  | 0.9345        | -                           |
| 0.5240 | 164  | 0.9486        | -                           |
| 0.5272 | 165  | 1.5389        | -                           |
| 0.5304 | 166  | 1.8956        | -                           |
| 0.5335 | 167  | 1.0425        | -                           |
| 0.5367 | 168  | 1.5296        | -                           |
| 0.5399 | 169  | 0.9602        | -                           |
| 0.5431 | 170  | 0.9832        | -                           |
| 0.5463 | 171  | 1.0982        | -                           |
| 0.5495 | 172  | 1.6295        | -                           |
| 0.5527 | 173  | 1.3986        | -                           |
| 0.5559 | 174  | 1.1721        | -                           |
| 0.5591 | 175  | 0.7994        | -                           |
| 0.5623 | 176  | 1.5655        | -                           |
| 0.5655 | 177  | 1.2068        | -                           |
| 0.5687 | 178  | 1.2747        | -                           |
| 0.5719 | 179  | 1.0729        | -                           |
| 0.5751 | 180  | 0.9977        | -                           |
| 0.5783 | 181  | 1.3537        | -                           |
| 0.5815 | 182  | 1.0964        | -                           |
| 0.5847 | 183  | 0.8029        | -                           |
| 0.5879 | 184  | 0.765         | -                           |
| 0.5911 | 185  | 1.0457        | -                           |
| 0.5942 | 186  | 1.2928        | -                           |
| 0.5974 | 187  | 1.2354        | -                           |
| 0.6006 | 188  | 1.031         | -                           |
| 0.6038 | 189  | 1.2561        | -                           |
| 0.6070 | 190  | 1.1676        | -                           |
| 0.6102 | 191  | 1.2186        | -                           |
| 0.6134 | 192  | 1.1786        | -                           |
| 0.6166 | 193  | 1.283         | -                           |
| 0.6198 | 194  | 0.8316        | -                           |
| 0.6230 | 195  | 1.2239        | -                           |
| 0.6262 | 196  | 1.08          | -                           |
| 0.6294 | 197  | 1.7637        | -                           |
| 0.6326 | 198  | 1.2315        | -                           |
| 0.6358 | 199  | 1.5375        | -                           |
| 0.6390 | 200  | 1.4388        | 0.73                        |
| 0.6422 | 201  | 1.3918        | -                           |
| 0.6454 | 202  | 1.37          | -                           |
| 0.6486 | 203  | 1.3753        | -                           |
| 0.6518 | 204  | 1.137         | -                           |
| 0.6550 | 205  | 1.4457        | -                           |
| 0.6581 | 206  | 1.3072        | -                           |
| 0.6613 | 207  | 2.0953        | -                           |
| 0.6645 | 208  | 1.6811        | -                           |
| 0.6677 | 209  | 0.9206        | -                           |
| 0.6709 | 210  | 0.9801        | -                           |
| 0.6741 | 211  | 0.961         | -                           |
| 0.6773 | 212  | 1.386         | -                           |
| 0.6805 | 213  | 1.5354        | -                           |
| 0.6837 | 214  | 0.6571        | -                           |
| 0.6869 | 215  | 1.2631        | -                           |
| 0.6901 | 216  | 1.2122        | -                           |
| 0.6933 | 217  | 1.6253        | -                           |
| 0.6965 | 218  | 1.266         | -                           |
| 0.6997 | 219  | 1.7445        | -                           |
| 0.7029 | 220  | 1.1527        | -                           |
| 0.7061 | 221  | 1.7681        | -                           |
| 0.7093 | 222  | 1.4941        | -                           |
| 0.7125 | 223  | 1.8236        | -                           |
| 0.7157 | 224  | 1.4117        | -                           |
| 0.7188 | 225  | 0.7363        | -                           |
| 0.7220 | 226  | 1.4519        | -                           |
| 0.7252 | 227  | 1.4138        | -                           |
| 0.7284 | 228  | 1.0758        | -                           |
| 0.7316 | 229  | 1.6275        | -                           |
| 0.7348 | 230  | 1.6303        | -                           |
| 0.7380 | 231  | 1.4706        | -                           |
| 0.7412 | 232  | 0.5958        | -                           |
| 0.7444 | 233  | 1.2442        | -                           |
| 0.7476 | 234  | 1.3782        | -                           |
| 0.7508 | 235  | 1.3971        | -                           |
| 0.7540 | 236  | 1.3412        | -                           |
| 0.7572 | 237  | 0.9017        | -                           |
| 0.7604 | 238  | 1.6336        | -                           |
| 0.7636 | 239  | 1.2652        | -                           |
| 0.7668 | 240  | 1.0598        | -                           |
| 0.7700 | 241  | 1.3082        | -                           |
| 0.7732 | 242  | 0.9677        | -                           |
| 0.7764 | 243  | 1.2684        | -                           |
| 0.7796 | 244  | 1.3539        | -                           |
| 0.7827 | 245  | 1.7301        | -                           |
| 0.7859 | 246  | 1.2539        | -                           |
| 0.7891 | 247  | 1.1073        | -                           |
| 0.7923 | 248  | 1.079         | -                           |
| 0.7955 | 249  | 1.3488        | -                           |
| 0.7987 | 250  | 1.0672        | -                           |
| 0.8019 | 251  | 1.4308        | -                           |
| 0.8051 | 252  | 1.126         | -                           |
| 0.8083 | 253  | 1.131         | -                           |
| 0.8115 | 254  | 0.9585        | -                           |
| 0.8147 | 255  | 0.9348        | -                           |
| 0.8179 | 256  | 1.1288        | -                           |
| 0.8211 | 257  | 1.2577        | -                           |
| 0.8243 | 258  | 1.286         | -                           |
| 0.8275 | 259  | 1.1985        | -                           |
| 0.8307 | 260  | 1.2386        | -                           |
| 0.8339 | 261  | 1.6239        | -                           |
| 0.8371 | 262  | 0.8122        | -                           |
| 0.8403 | 263  | 1.42          | -                           |
| 0.8435 | 264  | 0.9854        | -                           |
| 0.8466 | 265  | 0.9861        | -                           |
| 0.8498 | 266  | 1.2226        | -                           |
| 0.8530 | 267  | 1.1535        | -                           |
| 0.8562 | 268  | 1.634         | -                           |
| 0.8594 | 269  | 1.0699        | -                           |
| 0.8626 | 270  | 1.2927        | -                           |
| 0.8658 | 271  | 1.2269        | -                           |
| 0.8690 | 272  | 0.8528        | -                           |
| 0.8722 | 273  | 1.6345        | -                           |
| 0.8754 | 274  | 1.4596        | -                           |
| 0.8786 | 275  | 0.9795        | -                           |
| 0.8818 | 276  | 1.1772        | -                           |
| 0.8850 | 277  | 1.135         | -                           |
| 0.8882 | 278  | 0.994         | -                           |
| 0.8914 | 279  | 0.8705        | -                           |
| 0.8946 | 280  | 0.976         | -                           |
| 0.8978 | 281  | 1.2215        | -                           |
| 0.9010 | 282  | 1.4685        | -                           |
| 0.9042 | 283  | 1.6724        | -                           |
| 0.9073 | 284  | 1.3882        | -                           |
| 0.9105 | 285  | 1.2283        | -                           |
| 0.9137 | 286  | 1.0334        | -                           |
| 0.9169 | 287  | 1.2039        | -                           |
| 0.9201 | 288  | 1.0914        | -                           |
| 0.9233 | 289  | 1.7033        | -                           |
| 0.9265 | 290  | 1.7687        | -                           |
| 0.9297 | 291  | 1.2867        | -                           |
| 0.9329 | 292  | 1.196         | -                           |
| 0.9361 | 293  | 0.9771        | -                           |
| 0.9393 | 294  | 1.1878        | -                           |
| 0.9425 | 295  | 1.235         | -                           |
| 0.9457 | 296  | 1.4398        | -                           |
| 0.9489 | 297  | 1.475         | -                           |
| 0.9521 | 298  | 1.2632        | -                           |
| 0.9553 | 299  | 1.5732        | -                           |
| 0.9585 | 300  | 1.0147        | 0.725                       |
| 0.9617 | 301  | 1.0345        | -                           |
| 0.9649 | 302  | 1.2582        | -                           |
| 0.9681 | 303  | 1.0398        | -                           |
| 0.9712 | 304  | 1.3973        | -                           |
| 0.9744 | 305  | 1.6701        | -                           |
| 0.9776 | 306  | 1.2617        | -                           |
| 0.9808 | 307  | 1.5779        | -                           |
| 0.9840 | 308  | 1.0839        | -                           |
| 0.9872 | 309  | 1.3117        | -                           |
| 0.9904 | 310  | 1.6139        | -                           |
| 0.9936 | 311  | 1.0128        | -                           |
| 0.9968 | 312  | 0.837         | -                           |
| 1.0    | 313  | 1.3687        | 0.723                       |

</details>

### Framework Versions
- Python: 3.12.3
- Sentence Transformers: 3.3.1
- Transformers: 4.44.2
- PyTorch: 2.5.1
- Accelerate: 1.2.1
- Datasets: 2.19.0
- Tokenizers: 0.19.1

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