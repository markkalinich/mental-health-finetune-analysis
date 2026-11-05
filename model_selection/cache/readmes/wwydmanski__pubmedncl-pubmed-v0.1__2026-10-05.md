---
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- generated_from_trainer
- dataset_size:11312
- loss:MultipleNegativesRankingLoss
base_model: malteos/PubMedNCL
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
- name: SentenceTransformer based on malteos/PubMedNCL
  results:
  - task:
      type: triplet
      name: Triplet
    dataset:
      name: triplet dev
      type: triplet-dev
    metrics:
    - type: cosine_accuracy
      value: 0.65
      name: Cosine Accuracy
---

# SentenceTransformer based on malteos/PubMedNCL

This is a [sentence-transformers](https://www.SBERT.net) model finetuned from [malteos/PubMedNCL](https://huggingface.co/malteos/PubMedNCL) on the json dataset. It maps sentences & paragraphs to a 768-dimensional dense vector space and can be used for semantic textual similarity, semantic search, paraphrase mining, text classification, clustering, and more.

## Model Details

### Model Description
- **Model Type:** Sentence Transformer
- **Base model:** [malteos/PubMedNCL](https://huggingface.co/malteos/PubMedNCL) <!-- at revision a3844bf206a5855b574b855bcb04a6d1e5f6d722 -->
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
    'Calcineurin inhibitor-sparing regimen',
    'Belatacept-based immunosuppression: A calcineurin inhibitor-sparing regimen in heart transplant recipients. ',
    'Neurotoxicity of calcineurin inhibitors: impact and clinical management. ',
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

#### Triplet

* Dataset: `triplet-dev`
* Evaluated with [<code>TripletEvaluator</code>](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#sentence_transformers.evaluation.TripletEvaluator)

| Metric              | Value    |
|:--------------------|:---------|
| **cosine_accuracy** | **0.65** |

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
* Size: 11,312 training samples
* Columns: <code>anchor</code>, <code>positive</code>, and <code>negative</code>
* Approximate statistics based on the first 1000 samples:
  |         | anchor                                                                           | positive                                                                          | negative                                                                          |
  |:--------|:---------------------------------------------------------------------------------|:----------------------------------------------------------------------------------|:----------------------------------------------------------------------------------|
  | type    | string                                                                           | string                                                                            | string                                                                            |
  | details | <ul><li>min: 3 tokens</li><li>mean: 7.33 tokens</li><li>max: 37 tokens</li></ul> | <ul><li>min: 4 tokens</li><li>mean: 19.54 tokens</li><li>max: 67 tokens</li></ul> | <ul><li>min: 4 tokens</li><li>mean: 11.81 tokens</li><li>max: 45 tokens</li></ul> |
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
| 0      | 0    | -             | 0.541                       |
| 0.0032 | 1    | 1.8857        | -                           |
| 0.0064 | 2    | 1.3201        | -                           |
| 0.0096 | 3    | 1.6458        | -                           |
| 0.0128 | 4    | 1.783         | -                           |
| 0.0160 | 5    | 1.6226        | -                           |
| 0.0192 | 6    | 1.7636        | -                           |
| 0.0224 | 7    | 1.6457        | -                           |
| 0.0256 | 8    | 1.7128        | -                           |
| 0.0288 | 9    | 1.6293        | -                           |
| 0.0319 | 10   | 1.8555        | -                           |
| 0.0351 | 11   | 1.9232        | -                           |
| 0.0383 | 12   | 1.5314        | -                           |
| 0.0415 | 13   | 1.6542        | -                           |
| 0.0447 | 14   | 1.5947        | -                           |
| 0.0479 | 15   | 1.849         | -                           |
| 0.0511 | 16   | 1.5738        | -                           |
| 0.0543 | 17   | 1.556         | -                           |
| 0.0575 | 18   | 1.5806        | -                           |
| 0.0607 | 19   | 1.5298        | -                           |
| 0.0639 | 20   | 1.7878        | -                           |
| 0.0671 | 21   | 1.7792        | -                           |
| 0.0703 | 22   | 1.7247        | -                           |
| 0.0735 | 23   | 1.4215        | -                           |
| 0.0767 | 24   | 1.7255        | -                           |
| 0.0799 | 25   | 1.3724        | -                           |
| 0.0831 | 26   | 1.7002        | -                           |
| 0.0863 | 27   | 1.4362        | -                           |
| 0.0895 | 28   | 1.2914        | -                           |
| 0.0927 | 29   | 1.8951        | -                           |
| 0.0958 | 30   | 1.7748        | -                           |
| 0.0990 | 31   | 1.5147        | -                           |
| 0.1022 | 32   | 1.4271        | -                           |
| 0.1054 | 33   | 1.401         | -                           |
| 0.1086 | 34   | 1.5386        | -                           |
| 0.1118 | 35   | 1.1083        | -                           |
| 0.1150 | 36   | 1.6985        | -                           |
| 0.1182 | 37   | 1.3883        | -                           |
| 0.1214 | 38   | 1.2327        | -                           |
| 0.1246 | 39   | 1.1182        | -                           |
| 0.1278 | 40   | 1.1503        | -                           |
| 0.1310 | 41   | 1.0549        | -                           |
| 0.1342 | 42   | 1.1005        | -                           |
| 0.1374 | 43   | 1.2327        | -                           |
| 0.1406 | 44   | 1.4466        | -                           |
| 0.1438 | 45   | 1.053         | -                           |
| 0.1470 | 46   | 1.2527        | -                           |
| 0.1502 | 47   | 1.2469        | -                           |
| 0.1534 | 48   | 1.4009        | -                           |
| 0.1565 | 49   | 0.9248        | -                           |
| 0.1597 | 50   | 1.5937        | -                           |
| 0.1629 | 51   | 1.4656        | -                           |
| 0.1661 | 52   | 1.4136        | -                           |
| 0.1693 | 53   | 1.178         | -                           |
| 0.1725 | 54   | 1.3482        | -                           |
| 0.1757 | 55   | 1.2768        | -                           |
| 0.1789 | 56   | 1.2803        | -                           |
| 0.1821 | 57   | 1.3748        | -                           |
| 0.1853 | 58   | 1.3586        | -                           |
| 0.1885 | 59   | 1.2199        | -                           |
| 0.1917 | 60   | 1.3183        | -                           |
| 0.1949 | 61   | 1.4524        | -                           |
| 0.1981 | 62   | 0.8348        | -                           |
| 0.2013 | 63   | 1.123         | -                           |
| 0.2045 | 64   | 1.076         | -                           |
| 0.2077 | 65   | 0.8969        | -                           |
| 0.2109 | 66   | 0.7729        | -                           |
| 0.2141 | 67   | 1.1902        | -                           |
| 0.2173 | 68   | 1.4572        | -                           |
| 0.2204 | 69   | 1.2323        | -                           |
| 0.2236 | 70   | 1.1836        | -                           |
| 0.2268 | 71   | 0.9406        | -                           |
| 0.2300 | 72   | 1.1957        | -                           |
| 0.2332 | 73   | 0.7556        | -                           |
| 0.2364 | 74   | 1.1107        | -                           |
| 0.2396 | 75   | 0.776         | -                           |
| 0.2428 | 76   | 0.9051        | -                           |
| 0.2460 | 77   | 1.2314        | -                           |
| 0.2492 | 78   | 1.2717        | -                           |
| 0.2524 | 79   | 1.1385        | -                           |
| 0.2556 | 80   | 0.9591        | -                           |
| 0.2588 | 81   | 1.2769        | -                           |
| 0.2620 | 82   | 0.9365        | -                           |
| 0.2652 | 83   | 1.0268        | -                           |
| 0.2684 | 84   | 1.2769        | -                           |
| 0.2716 | 85   | 1.4569        | -                           |
| 0.2748 | 86   | 1.2353        | -                           |
| 0.2780 | 87   | 1.1564        | -                           |
| 0.2812 | 88   | 1.128         | -                           |
| 0.2843 | 89   | 1.2359        | -                           |
| 0.2875 | 90   | 1.0234        | -                           |
| 0.2907 | 91   | 0.9329        | -                           |
| 0.2939 | 92   | 0.9122        | -                           |
| 0.2971 | 93   | 1.046         | -                           |
| 0.3003 | 94   | 1.1084        | -                           |
| 0.3035 | 95   | 1.5154        | -                           |
| 0.3067 | 96   | 1.394         | -                           |
| 0.3099 | 97   | 0.9329        | -                           |
| 0.3131 | 98   | 1.1751        | -                           |
| 0.3163 | 99   | 1.4136        | -                           |
| 0.3195 | 100  | 1.0859        | 0.6                         |
| 0.3227 | 101  | 1.3132        | -                           |
| 0.3259 | 102  | 1.1107        | -                           |
| 0.3291 | 103  | 1.1071        | -                           |
| 0.3323 | 104  | 1.3991        | -                           |
| 0.3355 | 105  | 1.1542        | -                           |
| 0.3387 | 106  | 1.5527        | -                           |
| 0.3419 | 107  | 1.3701        | -                           |
| 0.3450 | 108  | 1.1583        | -                           |
| 0.3482 | 109  | 1.1743        | -                           |
| 0.3514 | 110  | 0.9375        | -                           |
| 0.3546 | 111  | 1.0193        | -                           |
| 0.3578 | 112  | 0.9705        | -                           |
| 0.3610 | 113  | 1.2329        | -                           |
| 0.3642 | 114  | 1.0263        | -                           |
| 0.3674 | 115  | 1.1292        | -                           |
| 0.3706 | 116  | 0.9325        | -                           |
| 0.3738 | 117  | 1.0293        | -                           |
| 0.3770 | 118  | 1.0638        | -                           |
| 0.3802 | 119  | 1.0024        | -                           |
| 0.3834 | 120  | 1.1966        | -                           |
| 0.3866 | 121  | 0.874         | -                           |
| 0.3898 | 122  | 1.1094        | -                           |
| 0.3930 | 123  | 1.1334        | -                           |
| 0.3962 | 124  | 1.5534        | -                           |
| 0.3994 | 125  | 0.8601        | -                           |
| 0.4026 | 126  | 1.172         | -                           |
| 0.4058 | 127  | 0.9888        | -                           |
| 0.4089 | 128  | 1.1072        | -                           |
| 0.4121 | 129  | 0.9179        | -                           |
| 0.4153 | 130  | 0.8901        | -                           |
| 0.4185 | 131  | 1.2932        | -                           |
| 0.4217 | 132  | 0.8809        | -                           |
| 0.4249 | 133  | 1.407         | -                           |
| 0.4281 | 134  | 1.1723        | -                           |
| 0.4313 | 135  | 0.7617        | -                           |
| 0.4345 | 136  | 0.8623        | -                           |
| 0.4377 | 137  | 1.1092        | -                           |
| 0.4409 | 138  | 0.9422        | -                           |
| 0.4441 | 139  | 0.8478        | -                           |
| 0.4473 | 140  | 1.0439        | -                           |
| 0.4505 | 141  | 0.9857        | -                           |
| 0.4537 | 142  | 0.8718        | -                           |
| 0.4569 | 143  | 1.0178        | -                           |
| 0.4601 | 144  | 1.4263        | -                           |
| 0.4633 | 145  | 0.9818        | -                           |
| 0.4665 | 146  | 1.1999        | -                           |
| 0.4696 | 147  | 1.0042        | -                           |
| 0.4728 | 148  | 0.7386        | -                           |
| 0.4760 | 149  | 0.8121        | -                           |
| 0.4792 | 150  | 0.982         | -                           |
| 0.4824 | 151  | 0.9998        | -                           |
| 0.4856 | 152  | 1.2617        | -                           |
| 0.4888 | 153  | 1.124         | -                           |
| 0.4920 | 154  | 0.948         | -                           |
| 0.4952 | 155  | 1.1027        | -                           |
| 0.4984 | 156  | 0.8592        | -                           |
| 0.5016 | 157  | 0.7257        | -                           |
| 0.5048 | 158  | 1.1329        | -                           |
| 0.5080 | 159  | 0.7886        | -                           |
| 0.5112 | 160  | 1.1468        | -                           |
| 0.5144 | 161  | 0.8234        | -                           |
| 0.5176 | 162  | 1.0084        | -                           |
| 0.5208 | 163  | 1.3117        | -                           |
| 0.5240 | 164  | 0.6839        | -                           |
| 0.5272 | 165  | 1.0097        | -                           |
| 0.5304 | 166  | 1.3979        | -                           |
| 0.5335 | 167  | 0.9312        | -                           |
| 0.5367 | 168  | 1.1595        | -                           |
| 0.5399 | 169  | 0.9771        | -                           |
| 0.5431 | 170  | 0.8747        | -                           |
| 0.5463 | 171  | 0.9973        | -                           |
| 0.5495 | 172  | 1.1271        | -                           |
| 0.5527 | 173  | 1.5213        | -                           |
| 0.5559 | 174  | 0.7934        | -                           |
| 0.5591 | 175  | 0.9291        | -                           |
| 0.5623 | 176  | 1.1036        | -                           |
| 0.5655 | 177  | 1.0352        | -                           |
| 0.5687 | 178  | 1.0123        | -                           |
| 0.5719 | 179  | 0.8707        | -                           |
| 0.5751 | 180  | 0.8158        | -                           |
| 0.5783 | 181  | 1.0186        | -                           |
| 0.5815 | 182  | 0.9716        | -                           |
| 0.5847 | 183  | 0.6801        | -                           |
| 0.5879 | 184  | 0.9617        | -                           |
| 0.5911 | 185  | 0.7656        | -                           |
| 0.5942 | 186  | 1.1093        | -                           |
| 0.5974 | 187  | 0.8643        | -                           |
| 0.6006 | 188  | 0.7412        | -                           |
| 0.6038 | 189  | 1.097         | -                           |
| 0.6070 | 190  | 0.6598        | -                           |
| 0.6102 | 191  | 0.8787        | -                           |
| 0.6134 | 192  | 0.8798        | -                           |
| 0.6166 | 193  | 1.1196        | -                           |
| 0.6198 | 194  | 0.7264        | -                           |
| 0.6230 | 195  | 0.9405        | -                           |
| 0.6262 | 196  | 0.9194        | -                           |
| 0.6294 | 197  | 1.4257        | -                           |
| 0.6326 | 198  | 0.8355        | -                           |
| 0.6358 | 199  | 0.9674        | -                           |
| 0.6390 | 200  | 0.6853        | 0.638                       |
| 0.6422 | 201  | 1.2965        | -                           |
| 0.6454 | 202  | 1.1806        | -                           |
| 0.6486 | 203  | 1.1466        | -                           |
| 0.6518 | 204  | 0.8743        | -                           |
| 0.6550 | 205  | 1.1603        | -                           |
| 0.6581 | 206  | 1.333         | -                           |
| 0.6613 | 207  | 1.211         | -                           |
| 0.6645 | 208  | 1.3726        | -                           |
| 0.6677 | 209  | 0.6753        | -                           |
| 0.6709 | 210  | 0.8125        | -                           |
| 0.6741 | 211  | 0.9256        | -                           |
| 0.6773 | 212  | 1.0996        | -                           |
| 0.6805 | 213  | 0.9329        | -                           |
| 0.6837 | 214  | 0.9108        | -                           |
| 0.6869 | 215  | 1.1639        | -                           |
| 0.6901 | 216  | 0.9787        | -                           |
| 0.6933 | 217  | 1.0471        | -                           |
| 0.6965 | 218  | 1.3486        | -                           |
| 0.6997 | 219  | 1.1849        | -                           |
| 0.7029 | 220  | 1.023         | -                           |
| 0.7061 | 221  | 1.1853        | -                           |
| 0.7093 | 222  | 1.0969        | -                           |
| 0.7125 | 223  | 0.9121        | -                           |
| 0.7157 | 224  | 1.1646        | -                           |
| 0.7188 | 225  | 0.6575        | -                           |
| 0.7220 | 226  | 0.9888        | -                           |
| 0.7252 | 227  | 0.8568        | -                           |
| 0.7284 | 228  | 1.0076        | -                           |
| 0.7316 | 229  | 0.9794        | -                           |
| 0.7348 | 230  | 1.1174        | -                           |
| 0.7380 | 231  | 1.078         | -                           |
| 0.7412 | 232  | 0.6901        | -                           |
| 0.7444 | 233  | 1.0532        | -                           |
| 0.7476 | 234  | 1.0519        | -                           |
| 0.7508 | 235  | 1.1772        | -                           |
| 0.7540 | 236  | 0.89          | -                           |
| 0.7572 | 237  | 0.9911        | -                           |
| 0.7604 | 238  | 1.0053        | -                           |
| 0.7636 | 239  | 1.0855        | -                           |
| 0.7668 | 240  | 1.1801        | -                           |
| 0.7700 | 241  | 0.9228        | -                           |
| 0.7732 | 242  | 0.5901        | -                           |
| 0.7764 | 243  | 1.0322        | -                           |
| 0.7796 | 244  | 1.1607        | -                           |
| 0.7827 | 245  | 0.937         | -                           |
| 0.7859 | 246  | 1.0137        | -                           |
| 0.7891 | 247  | 1.2338        | -                           |
| 0.7923 | 248  | 0.672         | -                           |
| 0.7955 | 249  | 0.8709        | -                           |
| 0.7987 | 250  | 0.9364        | -                           |
| 0.8019 | 251  | 1.4397        | -                           |
| 0.8051 | 252  | 0.9922        | -                           |
| 0.8083 | 253  | 0.8738        | -                           |
| 0.8115 | 254  | 1.2506        | -                           |
| 0.8147 | 255  | 1.0251        | -                           |
| 0.8179 | 256  | 0.7608        | -                           |
| 0.8211 | 257  | 0.7537        | -                           |
| 0.8243 | 258  | 1.0931        | -                           |
| 0.8275 | 259  | 0.7419        | -                           |
| 0.8307 | 260  | 1.0598        | -                           |
| 0.8339 | 261  | 1.2947        | -                           |
| 0.8371 | 262  | 0.9113        | -                           |
| 0.8403 | 263  | 1.1814        | -                           |
| 0.8435 | 264  | 1.008         | -                           |
| 0.8466 | 265  | 0.8872        | -                           |
| 0.8498 | 266  | 1.0446        | -                           |
| 0.8530 | 267  | 1.0517        | -                           |
| 0.8562 | 268  | 1.6135        | -                           |
| 0.8594 | 269  | 0.6549        | -                           |
| 0.8626 | 270  | 1.1515        | -                           |
| 0.8658 | 271  | 0.9095        | -                           |
| 0.8690 | 272  | 0.9574        | -                           |
| 0.8722 | 273  | 1.4922        | -                           |
| 0.8754 | 274  | 1.0787        | -                           |
| 0.8786 | 275  | 0.9104        | -                           |
| 0.8818 | 276  | 1.009         | -                           |
| 0.8850 | 277  | 1.0063        | -                           |
| 0.8882 | 278  | 0.842         | -                           |
| 0.8914 | 279  | 0.9313        | -                           |
| 0.8946 | 280  | 0.9677        | -                           |
| 0.8978 | 281  | 0.83          | -                           |
| 0.9010 | 282  | 1.1904        | -                           |
| 0.9042 | 283  | 1.3531        | -                           |
| 0.9073 | 284  | 0.7808        | -                           |
| 0.9105 | 285  | 0.6189        | -                           |
| 0.9137 | 286  | 1.1642        | -                           |
| 0.9169 | 287  | 0.7282        | -                           |
| 0.9201 | 288  | 1.0109        | -                           |
| 0.9233 | 289  | 0.7644        | -                           |
| 0.9265 | 290  | 1.3702        | -                           |
| 0.9297 | 291  | 0.9911        | -                           |
| 0.9329 | 292  | 1.0527        | -                           |
| 0.9361 | 293  | 1.1148        | -                           |
| 0.9393 | 294  | 0.995         | -                           |
| 0.9425 | 295  | 0.7739        | -                           |
| 0.9457 | 296  | 1.1728        | -                           |
| 0.9489 | 297  | 1.3264        | -                           |
| 0.9521 | 298  | 1.0306        | -                           |
| 0.9553 | 299  | 1.0521        | -                           |
| 0.9585 | 300  | 0.7472        | 0.649                       |
| 0.9617 | 301  | 0.9635        | -                           |
| 0.9649 | 302  | 1.1699        | -                           |
| 0.9681 | 303  | 1.143         | -                           |
| 0.9712 | 304  | 0.939         | -                           |
| 0.9744 | 305  | 1.3473        | -                           |
| 0.9776 | 306  | 1.2086        | -                           |
| 0.9808 | 307  | 1.0876        | -                           |
| 0.9840 | 308  | 0.866         | -                           |
| 0.9872 | 309  | 0.9147        | -                           |
| 0.9904 | 310  | 1.1839        | -                           |
| 0.9936 | 311  | 1.0603        | -                           |
| 0.9968 | 312  | 1.0036        | -                           |
| 1.0    | 313  | 1.0408        | 0.65                        |

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