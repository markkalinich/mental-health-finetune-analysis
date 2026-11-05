---
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- generated_from_trainer
- dataset_size:11172
- loss:MultipleNegativesRankingLoss
base_model: jxm/cde-small-v1
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
- name: SentenceTransformer based on jxm/cde-small-v1
  results:
  - task:
      type: triplet
      name: Triplet
    dataset:
      name: triplet dev
      type: triplet-dev
    metrics:
    - type: cosine_accuracy
      value: 0.71
      name: Cosine Accuracy
---

# SentenceTransformer based on jxm/cde-small-v1

This is a [sentence-transformers](https://www.SBERT.net) model finetuned from [jxm/cde-small-v1](https://huggingface.co/jxm/cde-small-v1) on the json dataset. It maps sentences & paragraphs to a None-dimensional dense vector space and can be used for semantic textual similarity, semantic search, paraphrase mining, text classification, clustering, and more.

## Model Details

### Model Description
- **Model Type:** Sentence Transformer
- **Base model:** [jxm/cde-small-v1](https://huggingface.co/jxm/cde-small-v1) <!-- at revision 9e2ed1d8d569d34458913d2d246935c1b2324d11 -->
- **Maximum Sequence Length:** None tokens
- **Output Dimensionality:** None dimensions
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
  (0): Transformer({}) with Transformer model: PeftModelForFeatureExtraction 
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

| Metric              | Value    |
|:--------------------|:---------|
| **cosine_accuracy** | **0.71** |

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
* Size: 11,172 training samples
* Columns: <code>anchor</code>, <code>positive</code>, and <code>negative</code>
* Approximate statistics based on the first 1000 samples:
  |         | anchor                                                                          | positive                                                                          | negative                                                                          |
  |:--------|:--------------------------------------------------------------------------------|:----------------------------------------------------------------------------------|:----------------------------------------------------------------------------------|
  | type    | string                                                                          | string                                                                            | string                                                                            |
  | details | <ul><li>min: 3 tokens</li><li>mean: 9.5 tokens</li><li>max: 42 tokens</li></ul> | <ul><li>min: 4 tokens</li><li>mean: 23.37 tokens</li><li>max: 82 tokens</li></ul> | <ul><li>min: 4 tokens</li><li>mean: 14.13 tokens</li><li>max: 59 tokens</li></ul> |
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
| 0      | 0    | -             | 0.566                       |
| 0.0032 | 1    | 3.7786        | -                           |
| 0.0064 | 2    | 3.0207        | -                           |
| 0.0096 | 3    | 3.4699        | -                           |
| 0.0128 | 4    | 3.9642        | -                           |
| 0.0160 | 5    | 2.9183        | -                           |
| 0.0192 | 6    | 3.1035        | -                           |
| 0.0224 | 7    | 3.2608        | -                           |
| 0.0256 | 8    | 3.7062        | -                           |
| 0.0288 | 9    | 3.2258        | -                           |
| 0.0319 | 10   | 2.9817        | -                           |
| 0.0351 | 11   | 3.9166        | -                           |
| 0.0383 | 12   | 3.4075        | -                           |
| 0.0415 | 13   | 3.097         | -                           |
| 0.0447 | 14   | 2.6437        | -                           |
| 0.0479 | 15   | 2.751         | -                           |
| 0.0511 | 16   | 3.0026        | -                           |
| 0.0543 | 17   | 3.2352        | -                           |
| 0.0575 | 18   | 2.9763        | -                           |
| 0.0607 | 19   | 3.5151        | -                           |
| 0.0639 | 20   | 2.3222        | -                           |
| 0.0671 | 21   | 3.347         | -                           |
| 0.0703 | 22   | 2.7674        | -                           |
| 0.0735 | 23   | 3.2104        | -                           |
| 0.0767 | 24   | 2.7494        | -                           |
| 0.0799 | 25   | 3.209         | -                           |
| 0.0831 | 26   | 2.8368        | -                           |
| 0.0863 | 27   | 2.5643        | -                           |
| 0.0895 | 28   | 2.6125        | -                           |
| 0.0927 | 29   | 3.5675        | -                           |
| 0.0958 | 30   | 3.6836        | -                           |
| 0.0990 | 31   | 2.6156        | -                           |
| 0.1022 | 32   | 2.1644        | -                           |
| 0.1054 | 33   | 2.3822        | -                           |
| 0.1086 | 34   | 2.9865        | -                           |
| 0.1118 | 35   | 3.2025        | -                           |
| 0.1150 | 36   | 2.407         | -                           |
| 0.1182 | 37   | 1.8443        | -                           |
| 0.1214 | 38   | 1.8141        | -                           |
| 0.1246 | 39   | 1.9261        | -                           |
| 0.1278 | 40   | 2.3911        | -                           |
| 0.1310 | 41   | 2.5934        | -                           |
| 0.1342 | 42   | 2.6681        | -                           |
| 0.1374 | 43   | 2.0246        | -                           |
| 0.1406 | 44   | 2.027         | -                           |
| 0.1438 | 45   | 2.3277        | -                           |
| 0.1470 | 46   | 3.252         | -                           |
| 0.1502 | 47   | 2.1263        | -                           |
| 0.1534 | 48   | 3.0712        | -                           |
| 0.1565 | 49   | 2.077         | -                           |
| 0.1597 | 50   | 3.0536        | -                           |
| 0.1629 | 51   | 3.1603        | -                           |
| 0.1661 | 52   | 3.3711        | -                           |
| 0.1693 | 53   | 2.4095        | -                           |
| 0.1725 | 54   | 2.0411        | -                           |
| 0.1757 | 55   | 2.4364        | -                           |
| 0.1789 | 56   | 3.1587        | -                           |
| 0.1821 | 57   | 2.8662        | -                           |
| 0.1853 | 58   | 2.8759        | -                           |
| 0.1885 | 59   | 2.8717        | -                           |
| 0.1917 | 60   | 3.515         | -                           |
| 0.1949 | 61   | 3.192         | -                           |
| 0.1981 | 62   | 2.253         | -                           |
| 0.2013 | 63   | 2.8449        | -                           |
| 0.2045 | 64   | 2.0755        | -                           |
| 0.2077 | 65   | 1.9475        | -                           |
| 0.2109 | 66   | 1.8015        | -                           |
| 0.2141 | 67   | 2.4801        | -                           |
| 0.2173 | 68   | 3.0986        | -                           |
| 0.2204 | 69   | 2.8571        | -                           |
| 0.2236 | 70   | 2.8611        | -                           |
| 0.2268 | 71   | 2.0581        | -                           |
| 0.2300 | 72   | 2.7042        | -                           |
| 0.2332 | 73   | 2.2055        | -                           |
| 0.2364 | 74   | 2.3948        | -                           |
| 0.2396 | 75   | 2.1092        | -                           |
| 0.2428 | 76   | 3.2277        | -                           |
| 0.2460 | 77   | 2.0378        | -                           |
| 0.2492 | 78   | 2.1426        | -                           |
| 0.2524 | 79   | 2.6016        | -                           |
| 0.2556 | 80   | 2.8198        | -                           |
| 0.2588 | 81   | 2.3303        | -                           |
| 0.2620 | 82   | 2.4117        | -                           |
| 0.2652 | 83   | 2.8172        | -                           |
| 0.2684 | 84   | 2.2824        | -                           |
| 0.2716 | 85   | 2.3764        | -                           |
| 0.2748 | 86   | 1.7689        | -                           |
| 0.2780 | 87   | 1.8861        | -                           |
| 0.2812 | 88   | 2.0835        | -                           |
| 0.2843 | 89   | 2.3946        | -                           |
| 0.2875 | 90   | 2.4478        | -                           |
| 0.2907 | 91   | 2.0612        | -                           |
| 0.2939 | 92   | 1.6599        | -                           |
| 0.2971 | 93   | 2.6267        | -                           |
| 0.3003 | 94   | 1.9966        | -                           |
| 0.3035 | 95   | 2.3953        | -                           |
| 0.3067 | 96   | 2.4832        | -                           |
| 0.3099 | 97   | 1.7252        | -                           |
| 0.3131 | 98   | 2.1252        | -                           |
| 0.3163 | 99   | 2.4232        | -                           |
| 0.3195 | 100  | 1.8645        | 0.663                       |
| 0.3227 | 101  | 2.3749        | -                           |
| 0.3259 | 102  | 2.1641        | -                           |
| 0.3291 | 103  | 1.6162        | -                           |
| 0.3323 | 104  | 2.118         | -                           |
| 0.3355 | 105  | 2.2934        | -                           |
| 0.3387 | 106  | 2.6288        | -                           |
| 0.3419 | 107  | 2.6996        | -                           |
| 0.3450 | 108  | 1.6489        | -                           |
| 0.3482 | 109  | 2.4605        | -                           |
| 0.3514 | 110  | 1.9531        | -                           |
| 0.3546 | 111  | 1.8193        | -                           |
| 0.3578 | 112  | 1.9936        | -                           |
| 0.3610 | 113  | 2.26          | -                           |
| 0.3642 | 114  | 1.9986        | -                           |
| 0.3674 | 115  | 2.4304        | -                           |
| 0.3706 | 116  | 2.1585        | -                           |
| 0.3738 | 117  | 1.8003        | -                           |
| 0.3770 | 118  | 2.4486        | -                           |
| 0.3802 | 119  | 2.637         | -                           |
| 0.3834 | 120  | 2.1322        | -                           |
| 0.3866 | 121  | 2.0404        | -                           |
| 0.3898 | 122  | 2.0502        | -                           |
| 0.3930 | 123  | 2.0422        | -                           |
| 0.3962 | 124  | 2.236         | -                           |
| 0.3994 | 125  | 2.3226        | -                           |
| 0.4026 | 126  | 2.469         | -                           |
| 0.4058 | 127  | 1.8761        | -                           |
| 0.4089 | 128  | 2.3535        | -                           |
| 0.4121 | 129  | 1.5602        | -                           |
| 0.4153 | 130  | 1.266         | -                           |
| 0.4185 | 131  | 2.3524        | -                           |
| 0.4217 | 132  | 1.7668        | -                           |
| 0.4249 | 133  | 1.8161        | -                           |
| 0.4281 | 134  | 2.1238        | -                           |
| 0.4313 | 135  | 2.0247        | -                           |
| 0.4345 | 136  | 2.2131        | -                           |
| 0.4377 | 137  | 1.9424        | -                           |
| 0.4409 | 138  | 1.8134        | -                           |
| 0.4441 | 139  | 2.2077        | -                           |
| 0.4473 | 140  | 1.17          | -                           |
| 0.4505 | 141  | 2.2172        | -                           |
| 0.4537 | 142  | 1.903         | -                           |
| 0.4569 | 143  | 1.9001        | -                           |
| 0.4601 | 144  | 1.7742        | -                           |
| 0.4633 | 145  | 1.7324        | -                           |
| 0.4665 | 146  | 2.2174        | -                           |
| 0.4696 | 147  | 2.1008        | -                           |
| 0.4728 | 148  | 1.6292        | -                           |
| 0.4760 | 149  | 1.4405        | -                           |
| 0.4792 | 150  | 1.7845        | -                           |
| 0.4824 | 151  | 1.8363        | -                           |
| 0.4856 | 152  | 1.8181        | -                           |
| 0.4888 | 153  | 1.6015        | -                           |
| 0.4920 | 154  | 2.0204        | -                           |
| 0.4952 | 155  | 1.4804        | -                           |
| 0.4984 | 156  | 1.4607        | -                           |
| 0.5016 | 157  | 1.8526        | -                           |
| 0.5048 | 158  | 1.731         | -                           |
| 0.5080 | 159  | 1.1399        | -                           |
| 0.5112 | 160  | 1.8764        | -                           |
| 0.5144 | 161  | 1.7151        | -                           |
| 0.5176 | 162  | 2.4042        | -                           |
| 0.5208 | 163  | 2.1513        | -                           |
| 0.5240 | 164  | 1.31          | -                           |
| 0.5272 | 165  | 1.8768        | -                           |
| 0.5304 | 166  | 1.8048        | -                           |
| 0.5335 | 167  | 1.6037        | -                           |
| 0.5367 | 168  | 2.3568        | -                           |
| 0.5399 | 169  | 1.8979        | -                           |
| 0.5431 | 170  | 1.4007        | -                           |
| 0.5463 | 171  | 1.466         | -                           |
| 0.5495 | 172  | 1.8892        | -                           |
| 0.5527 | 173  | 2.1865        | -                           |
| 0.5559 | 174  | 1.6588        | -                           |
| 0.5591 | 175  | 1.3176        | -                           |
| 0.5623 | 176  | 1.9557        | -                           |
| 0.5655 | 177  | 1.6885        | -                           |
| 0.5687 | 178  | 2.0255        | -                           |
| 0.5719 | 179  | 1.7787        | -                           |
| 0.5751 | 180  | 1.9642        | -                           |
| 0.5783 | 181  | 1.8975        | -                           |
| 0.5815 | 182  | 1.7           | -                           |
| 0.5847 | 183  | 1.3562        | -                           |
| 0.5879 | 184  | 1.78          | -                           |
| 0.5911 | 185  | 1.6219        | -                           |
| 0.5942 | 186  | 2.3187        | -                           |
| 0.5974 | 187  | 1.4364        | -                           |
| 0.6006 | 188  | 1.4302        | -                           |
| 0.6038 | 189  | 1.9611        | -                           |
| 0.6070 | 190  | 1.299         | -                           |
| 0.6102 | 191  | 1.5023        | -                           |
| 0.6134 | 192  | 1.6221        | -                           |
| 0.6166 | 193  | 1.8834        | -                           |
| 0.6198 | 194  | 1.9183        | -                           |
| 0.6230 | 195  | 1.666         | -                           |
| 0.6262 | 196  | 1.2618        | -                           |
| 0.6294 | 197  | 2.1579        | -                           |
| 0.6326 | 198  | 2.0658        | -                           |
| 0.6358 | 199  | 1.7967        | -                           |
| 0.6390 | 200  | 2.0332        | 0.706                       |
| 0.6422 | 201  | 1.8525        | -                           |
| 0.6454 | 202  | 1.914         | -                           |
| 0.6486 | 203  | 2.1121        | -                           |
| 0.6518 | 204  | 1.6235        | -                           |
| 0.6550 | 205  | 2.165         | -                           |
| 0.6581 | 206  | 2.1271        | -                           |
| 0.6613 | 207  | 2.6429        | -                           |
| 0.6645 | 208  | 2.1433        | -                           |
| 0.6677 | 209  | 1.6523        | -                           |
| 0.6709 | 210  | 1.3249        | -                           |
| 0.6741 | 211  | 1.6668        | -                           |
| 0.6773 | 212  | 1.7824        | -                           |
| 0.6805 | 213  | 2.276         | -                           |
| 0.6837 | 214  | 1.0015        | -                           |
| 0.6869 | 215  | 1.549         | -                           |
| 0.6901 | 216  | 1.9478        | -                           |
| 0.6933 | 217  | 2.0875        | -                           |
| 0.6965 | 218  | 1.6177        | -                           |
| 0.6997 | 219  | 1.9426        | -                           |
| 0.7029 | 220  | 1.5141        | -                           |
| 0.7061 | 221  | 2.3293        | -                           |
| 0.7093 | 222  | 1.7937        | -                           |
| 0.7125 | 223  | 1.7204        | -                           |
| 0.7157 | 224  | 1.9365        | -                           |
| 0.7188 | 225  | 1.0698        | -                           |
| 0.7220 | 226  | 1.7878        | -                           |
| 0.7252 | 227  | 1.5305        | -                           |
| 0.7284 | 228  | 1.7989        | -                           |
| 0.7316 | 229  | 1.7433        | -                           |
| 0.7348 | 230  | 2.2788        | -                           |
| 0.7380 | 231  | 1.6643        | -                           |
| 0.7412 | 232  | 1.2865        | -                           |
| 0.7444 | 233  | 1.6712        | -                           |
| 0.7476 | 234  | 2.0329        | -                           |
| 0.7508 | 235  | 2.3507        | -                           |
| 0.7540 | 236  | 2.0751        | -                           |
| 0.7572 | 237  | 1.3945        | -                           |
| 0.7604 | 238  | 1.7766        | -                           |
| 0.7636 | 239  | 2.0564        | -                           |
| 0.7668 | 240  | 1.8347        | -                           |
| 0.7700 | 241  | 1.676         | -                           |
| 0.7732 | 242  | 1.5643        | -                           |
| 0.7764 | 243  | 1.9716        | -                           |
| 0.7796 | 244  | 1.8792        | -                           |
| 0.7827 | 245  | 1.8918        | -                           |
| 0.7859 | 246  | 1.8682        | -                           |
| 0.7891 | 247  | 1.7447        | -                           |
| 0.7923 | 248  | 1.4158        | -                           |
| 0.7955 | 249  | 1.6805        | -                           |
| 0.7987 | 250  | 1.4564        | -                           |
| 0.8019 | 251  | 2.2649        | -                           |
| 0.8051 | 252  | 1.6834        | -                           |
| 0.8083 | 253  | 1.4704        | -                           |
| 0.8115 | 254  | 1.9097        | -                           |
| 0.8147 | 255  | 1.6388        | -                           |
| 0.8179 | 256  | 1.4111        | -                           |
| 0.8211 | 257  | 1.3129        | -                           |
| 0.8243 | 258  | 2.0162        | -                           |
| 0.8275 | 259  | 1.9092        | -                           |
| 0.8307 | 260  | 1.5773        | -                           |
| 0.8339 | 261  | 1.791         | -                           |
| 0.8371 | 262  | 2.0667        | -                           |
| 0.8403 | 263  | 2.1272        | -                           |
| 0.8435 | 264  | 1.6405        | -                           |
| 0.8466 | 265  | 1.5684        | -                           |
| 0.8498 | 266  | 1.6187        | -                           |
| 0.8530 | 267  | 1.6393        | -                           |
| 0.8562 | 268  | 1.6839        | -                           |
| 0.8594 | 269  | 1.3771        | -                           |
| 0.8626 | 270  | 1.888         | -                           |
| 0.8658 | 271  | 1.9585        | -                           |
| 0.8690 | 272  | 1.7324        | -                           |
| 0.8722 | 273  | 2.2049        | -                           |
| 0.8754 | 274  | 1.8384        | -                           |
| 0.8786 | 275  | 1.2521        | -                           |
| 0.8818 | 276  | 1.6959        | -                           |
| 0.8850 | 277  | 1.949         | -                           |
| 0.8882 | 278  | 1.5847        | -                           |
| 0.8914 | 279  | 1.3838        | -                           |
| 0.8946 | 280  | 1.467         | -                           |
| 0.8978 | 281  | 1.6706        | -                           |
| 0.9010 | 282  | 1.7329        | -                           |
| 0.9042 | 283  | 1.8004        | -                           |
| 0.9073 | 284  | 1.518         | -                           |
| 0.9105 | 285  | 1.659         | -                           |
| 0.9137 | 286  | 1.5457        | -                           |
| 0.9169 | 287  | 1.5093        | -                           |
| 0.9201 | 288  | 1.6979        | -                           |
| 0.9233 | 289  | 2.0024        | -                           |
| 0.9265 | 290  | 2.3541        | -                           |
| 0.9297 | 291  | 1.6111        | -                           |
| 0.9329 | 292  | 1.6866        | -                           |
| 0.9361 | 293  | 1.5074        | -                           |
| 0.9393 | 294  | 1.9874        | -                           |
| 0.9425 | 295  | 1.9216        | -                           |
| 0.9457 | 296  | 1.6023        | -                           |
| 0.9489 | 297  | 2.344         | -                           |
| 0.9521 | 298  | 2.3418        | -                           |
| 0.9553 | 299  | 1.4993        | -                           |
| 0.9585 | 300  | 1.4566        | 0.708                       |
| 0.9617 | 301  | 1.5179        | -                           |
| 0.9649 | 302  | 1.5219        | -                           |
| 0.9681 | 303  | 1.8588        | -                           |
| 0.9712 | 304  | 1.5196        | -                           |
| 0.9744 | 305  | 2.124         | -                           |
| 0.9776 | 306  | 1.6914        | -                           |
| 0.9808 | 307  | 1.8972        | -                           |
| 0.9840 | 308  | 1.5841        | -                           |
| 0.9872 | 309  | 1.9003        | -                           |
| 0.9904 | 310  | 1.8052        | -                           |
| 0.9936 | 311  | 1.7956        | -                           |
| 0.9968 | 312  | 1.7592        | -                           |
| 1.0    | 313  | 2.0598        | 0.71                        |

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